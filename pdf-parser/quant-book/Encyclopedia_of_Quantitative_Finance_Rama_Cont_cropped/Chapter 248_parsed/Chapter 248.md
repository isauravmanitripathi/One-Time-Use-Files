# **Monotone Schemes**

Monotone numerical schemes are particularly relevant for partial differential equations (PDEs) occurring in finance, for example, in the pricing of American options, exotic options, and in portfolio problems [4]. Although naive numerical schemes for such problems may not converge, or if they converge, may converge to an incorrect solution, monotone schemes converge to the correct solution under very weak assumptions on the schemes, equations, and boundary conditions. The drawback is that these schemes may converge slowly, as they are only firstor second-order accurate.

result. Finally, we discuss error estimates for convex problems.

# **Viscosity Solutions**

The concept of viscosity solution was introduced by Crandall and Lions in 1983. A general reference on the subject is the User's Guide [14]. Several books have also been written on the subject, see for example,  $[1-3, 19, 21]$ . Viscosity solutions are particularly important for nonlinear or degenerate PDEs of first and second order. There are many such problems in finance, we show some examples taken from [4]. Lower indices denote partial derivatives.

$$\begin{cases} -u_t - \frac{1}{2}\sigma^2 S^2 u_{SS} - r S u_S + r u - \frac{S}{T} u_Z = 0 & \text{in } \mathbb{R}^+ \times \mathbb{R}^+ \times (0, T) \\ u(S, Z, T) = (Z - S)^+ & \text{in } \mathbb{R}^+ \times \mathbb{R}^+ \end{cases} \tag{1}$$

$$\begin{cases} \min\{-u_t - \frac{1}{2}\sigma^2 S^2 u_{SS} - r S u_S + r u, u - (K - S)^+\} = 0 & \text{in } \mathbb{R}^+ \times (0, T) \\ u(S, T) = (K - S)^+ & \text{in } \mathbb{R}^+ \end{cases} \tag{2}$$

$$\min\left\{\inf_{c\geq 0} \left[ -v_t - \frac{1}{2}\sigma^2 y^2 u_{yy} - (rx - c)u_x - byv_y - U(c) + \beta v \right], \right.$$
  
$$\left. -v_y + (1+\lambda)v_x, -(1-\mu)v_x + v_y \right\} = 0 \qquad (3)$$
  
$$\ln \left\{ (x,y) : x + (1-\mu)y \geq 0, x + (1+\lambda)y \geq 0 \right\} \times (0,T)$$

Convergence results and error estimates for monotone schemes can be obtained using the concept of viscosity solution. The main goal of this survey is to introduce these methods and describe the results they lead to. The main results are (i) a general convergence theorem and (ii) error estimates for convex problems.

Viscosity solutions are (very) weak solutions of linear and nonlinear first- and second-order equations. They are closely related to the maximum (comparison) principle from which uniqueness of solutions follows. Viscosity solutions are useful for proving convergence of numerical schemes, because they are stable under very weak continuity assumptions: if a sequence of equations and their viscosity solutions converge locally uniformly, then the limit solution is a viscosity solution of the limit equation. The general convergence results is an extension of this statement.

We first motivate and define viscosity solutions and discuss basic facts about them. Then we discuss monotone schemes and give the general convergence

and in the last case we also impose state-constrained boundary conditions. The first two problems are related to the pricing of Asian and American options. The first equation is degenerate in the  $Z$ -direction and at  $S = 0$  (meaning there is no diffusion here), the second equation is an obstacle problem with degeneracy at  $S = 0$ . The last one, related to an investmentconsumption model by Tourin and Zariphopoulou, is nonlinear, degenerate, and has difficult boundary conditions.

Note that to solve these problems numerically, we must reduce to bounded domains and hence we need to impose further boundary conditions. All of these equations are *degenerate elliptic* equations that can be written in the following abstract form:

$$F(x, u(x), Du(x), D2u(x)) = 0 \quad \text{in} \quad \Omega \quad (4)$$

for some domain (open connected set)  $\Omega$  in  $\mathbb{R}^N$  and function  $F(x, r, p, X)$  on  $\Omega \times \mathbb{R} \times \mathbb{R}^N \times S_N$  where  $\mathcal{S}_N$  is the space of all real symmetric  $N \times N$  matrices,

and where *F* satisfies the condition

$$F(x, r, p, X) \le F(x, s, p, Y)$$
 whenever  $r \le s$   
and  $X \ge Y$  (5)

Here, *X* ≥ 0 means that *X* is a positive semidefinite matrix. The assumption that *F* is nonincreasing in *X* is called *degenerate ellipticity*. Note that assumption (5) rules out many quasi-linear equations like, for example, conservation laws, and that we represent both time-dependent and time-independent problems in the form (4). In the time-dependent case, we take *x* = *(t, x )* for *t* ≥ 0, *x* ∈ *<sup>N</sup>*−<sup>1</sup> . It is an instructive exercise to check that the above equations satisfy equation (5). This abstract formulation will help us formulate results in an economical way.

A *classical solution* of equation (4) is a function *u* in *C*<sup>2</sup>*()* (twice continuous differentiable functions on ) satisfying equation (4) in every point in . We now define viscosity solution for equation (4) starting with the following observation: if *u* is a classical solution of equation (4), *φ* belongs to *C*<sup>2</sup>*()*, and *u* − *φ* has local maximum at *x*<sup>0</sup> ∈ , then

$$Du(x_0) = D\phi(x_0)$$
 and  $D^2u(x_0) \le D^2\phi(x_0)$  (6)

and hence by equations (4) and (5) we must have

$$F(x_0, u(x_0), D\phi(x_0), D^2\phi(x_0)) \le 0 \tag{7}$$

On the other hand, if *x*<sup>0</sup> is a local minimum point of *u* − *φ*, then we get the opposite inequality. If these inequalities hold for *all test functions φ* and *all maximum/minimum points x*<sup>0</sup> of *u* − *φ* and the function *u* belongs to *C*2, then it easily follows that *u* is a classical solution of equation (4).

This second definition of classical solutions can be used to define viscosity solutions simply by relaxing the regularity assumption on *u* from *C*<sup>2</sup> to continuous. Note that in this definition, only test functions need to be differentiated.

**Definition 1** *A viscosity solution of equation (4) is a continuous function u on satisfying*

$$F(x_0, u(x_0), D\phi(x_0), D^2\phi(x_0)) \le 0 \tag{8}$$

*for all C*<sup>2</sup> *test functions φ and all maximum points x*<sup>0</sup> *of u* − *φ, and*

$$F(x_1, u(x_1), D\phi(x_1), D^2\phi(x_1)) \ge 0 \qquad (9)$$

*for all C*<sup>2</sup> *test functions φ and all minimum points x*<sup>1</sup> *of u* − *φ.*

By the previous discussion, we see that all classical solutions are viscosity solutions and that all *C*<sup>2</sup> viscosity solutions are classical solutions.

A problem that is often encountered when you study nonlinear equations is that classical solutions may not exist and weak solutions are not unique [2, 18]. To pick out the physically relevant solution (and solve the nonuniqueness problem), we often have to require that additional (entropy) inequalities are satisfied by the solution. One of the main strengths of viscosity solutions is that they are unique under very general assumptions—in some sense the additional constraints are built into the definition.

**Example 1** Consider the following initial value problem,

$$u_t + |u_x| = 0 \text{ in } \mathbb{R} \times (0, +\infty),$$
  
$$u(0, x) = |x| \text{ in } \mathbb{R}$$
(10)

It has *no* classical solutions, *infinitely many* generalized solutions (functions satisfying the equation a.e.), and one *unique* viscosity solution. Two generalized solutions are |*x*| − *t* and *(*|*x*| − *t)*<sup>+</sup>, and the last one is also the viscosity solution.

Now we explain how to impose boundary conditions for degenerate equations satisfying equation (5). Consider

$$\begin{cases} F(x, u(x), Du(x), D^2u(x)) = 0 & \text{in} \\ G(x, u, Du) = 0 & \text{in} \\ \end{cases} \quad \begin{cases} \Omega \\ \partial \Omega \end{cases} \tag{11}$$

where *G* gives the boundary conditions. Dirichlet and Neumann boundary conditions are obtained by choosing

$$G(x, r, p) = r - g(x)$$
  
and 
$$G(x, r, p) = p \cdot n(x) - h(x) \qquad (12)$$

respectively, where *n(x)* is the exterior unit normal vector field of *∂*. The problem here is that under assumption (5), the equation may be degenerate on all or a part of the boundary *∂*. This part of the boundary may not be *regular* with respect to the equation, meaning that boundary conditions imposed here do not influence the solution of equation  $(11)$  in  $\nΩ\n$ . In  $\nΩ\n$ , a solution of equation (11) is determined only by the equation and the boundary conditions on  $\partial\Omega_{\text{reg}}$ , the regular part of the boundary. Imposing boundary conditions in  $\partial\Omega_{irreg} = \partial\Omega \setminus \partial\Omega_{reg}$  therefore makes the solution *discontinuous* in  $\partial \Omega_{irreg}$  in general. We refer to [5, 14, 28] for a more detailed

Note that the continuous extension  $\tilde{u}$  of the solution u from  $\Omega$  to  $\overline{\Omega}$ , satisfies by continuity  $F=0$ also in  $\partial \Omega_{irreg}$  (under suitable assumptions). Hence at any boundary point,  $\tilde{u}$  satisfies either the boundary condition  $or$  the equation.

discussion.

Now we give the precise definition of discontinuous viscosity solutions. This concept is crucial for the main convergence result of this survey, and as we have just seen, the boundary value problem (11) is well posed in general only if solutions can be discontinuous on the boundary. To this end, we define the upper and lower semicontinuous envelopes of u,

$$u^*(x) = \limsup_{\Omega \ni y \to x} u(y) \quad \text{and} \quad u_*(x) = \liminf_{\Omega \ni y \to x} u(y)$$
(13)

A function  $u$  is upper semicontinuous, lower semicontinuous, or continuous at  $x \in \Omega$  if and only if  $u(x) = u^*(x)$ ,  $u(x) = u_*(x)$ , or  $u(x) = u^*(x) =$  $u_*(x)$ , respectively. At a boundary point, the definition requires that either the boundary condition or the equation holds.

**Definition 2** A discontinuous viscosity subsolution of equation (11) is a locally bounded function u on  $\bar{\Omega}$ satisfying for all  $\phi \in C^2(\bar{\Omega})$  and all local maximum points  $x_0 \in \bar{\Omega}$  of  $u^* - \phi$ ,

$$\begin{cases}\nF(x_0, u^*(x_0), D\phi(x_0), D^2\phi(x_0)) \le 0 & \text{if } x_0 \in \Omega \\
\min \left\{ F(x_0, u^*(x_0), D\phi(x_0), D^2\phi(x_0)), \\
G(x_0, u^*(x_0), D\phi(x_0)) \right\} \le 0 & \text{if } x_0 \in \partial\Omega\n\end{cases}\n$$
(14)

A discontinuous viscosity supersolution of equation (11) is a locally bounded function u on  $\overline{\Omega}$  satisfying for all  $\phi \in C^2(\overline{\Omega})$  and all local minimum points

$$x_0 \in \bar{\Omega} \text{ of } u_* - \phi$$

$$\begin{cases}\nF(x_0, u_*(x_0), D\phi(x_0), D^2\phi(x_0)) \ge 0 & \text{if } x_0 \in \Omega \\
\max \left\{ F(x_0, u_*(x_0), D\phi(x_0), D^2\phi(x_0)), \\
G(x_0, u_*(x_0), D\phi(x_0)) \right\} \ge 0 & \text{if } x_0 \in \partial\Omega\n\end{cases}\n$$
(15)

A discontinuous viscosity solution of equation  $(11)$  is sub and supersolution at the same time.

Viscosity solutions are unique under very weak assumptions and stable under continuous perturbations of the equation. From the strong comparison result (a uniqueness result) and Perron's method, interior continuity and existence follows. We refer to  $[14]$ for precise statements and a wider discussion.

A classical way to compute the solution of degenerate boundary value problem is via elliptic/parabolic regularization. This method is called the *vanishing viscosity method*: if  $u^{\epsilon}$ ,  $\epsilon > 0$ , are classical (or viscosity) solutions of

$$\begin{cases} -\epsilon \Delta u + F(x, u, \\ Du, D^2 u) = 0 \quad \text{in} \quad \Omega \\ G(x, u, Du) = 0 \quad \text{in} \quad \partial\Omega \end{cases} \tag{16}$$

then  $u_{\epsilon}$  converge pointwise as  $\epsilon \to 0$  to the discontinuous viscosity solution of equation (11) under mild assumptions [14]. In the regularized problem, boundary conditions are assumed continuously, but as  $\epsilon \to 0$  there will be formation of boundary layers near  $\partial\Omega_{irreg}$ , and in the limit the solution will be discontinuous here.

**Example 2** Let  $\epsilon > 0$  and consider the boundary value problem

$$\begin{cases} -\epsilon u''(x) + u'(x) - 1 = 0, & x \in (0, 1) \\ u(x) = 0, & x \in \{0, 1\} \end{cases}$$
(17)

Here, the unique (classical) solution  $u_{\epsilon}$  converges pointwise (but not uniformly) as  $\epsilon \to 0$  to a discontinuous function  $u$ :

$$u_{\epsilon}(x) = x - \frac{1 - e^{-\frac{1}{\epsilon}x}}{1 - e^{-\frac{1}{\epsilon}}}$$
$$\longrightarrow \qquad u = \begin{cases} 0, & x = 0\\ x - 1, & x \in (0, 1] \end{cases} \tag{18}$$

By formally taking the limit in equation  $(17)$ , we get the following boundary value problem,

$$\begin{cases}\n u'(x) - 1 = 0, & x \in (0, 1) \\
 u(x) = 0, & x \in \{0, 1\}\n\end{cases} \n$$
(19)

We write this problem in the form  $(11)$  by taking  $F(p) \equiv p - 1$  and  $G(r) \equiv r$ . Then, since  $u^* \equiv u$  and  $u_* \equiv x - 1$  in [0, 1], it is easy to see that in the viscosity sense,

$$\begin{cases}\nF\left(\frac{\mathrm{d}u^*}{\mathrm{d}x}\right) \le 0, & x \in (0, 1), \\
G(u^*) \le 0, & x = 0, \\
G(u^*) \le 0, & x = 1,\n\end{cases}\n$$
and
$$\n\begin{cases}\nF\left(\frac{\mathrm{d}u_*}{\mathrm{d}x}\right) \ge 0, & x \in (0, 1) \\
F\left(\frac{\mathrm{d}u_*}{\mathrm{d}x}\right) \ge 0, & x = 0 \\
G(u_*) \ge 0, & x = 1\n\end{cases} \tag{20}$$

Hence,  $u$  is a viscosity solution of equation (19) according to Definition 2.

To have an even more compact notation, we define

$$H(x, r, p, X) = \begin{cases} F(x, r, p, X) & \text{if } x \in \Omega \\ G(x, r, p) & \text{if } x \in \partial\Omega \end{cases} (21)$$

and note that  $H^*$ ,  $H_*$  equals  $H$  in  $\Omega$  and  $\max(F, G)$ ,  $\min(F, G)$ , respectively, on  $\partial\Omega$ . Hence, by the above discussion,  $u$  is viscosity solution of equation (11), or equivalently, of

$$H(x, u, Du, D^2u) = 0 \quad \text{in} \quad \bar{\Omega} \tag{22}$$

if the following inequalities hold in the viscosity sense:

$$H_*(x, u, Du, D^2 u) \le 0 \quad \text{in} \quad \bar{\Omega} \tag{23}$$

$$H^*(x, u, Du, D^2u) \ge 0 \quad \text{in} \quad \bar{\Omega} \tag{24}$$

# **Monotone Schemes and Convergence**

*Monotone* schemes, or schemes of *positive type*, were introduced by Motzkin and Wasow [26] for linear equations and later extended to nonlinear equations (see [27]). Monotone schemes satisfy the discrete maximum principle (under natural assumptions) and the principal error term in the formal error expansion is elliptic. Hence, the schemes produce "smooth" and monotone approximations to a regularized version of the original problem.

The main advantage of monotone schemes is that they "always" converge to the physically relevant solution [10]. For nonlinear or degenerate elliptic/parabolic equations, weak solutions are not unique in general, and extra conditions are needed to select the physically relevant solution. Nonmonotone schemes do not converge in general [27], and can even produce nonphysical solutions [29].

The main *disadvantage* of monotone schemes is the low order of convergence: first order for firstorder PDEs and at most second order for secondorder PDEs [27].

The main result of this section is the general convergence result of Barles and Souganidis for monotone, consistent, and stable schemes. We write a numerical scheme for the boundary value problem  $(22)$  or  $(11)$  as

$$S(h, x, u_h(x), u_h) = 0 \quad \text{on} \quad \Omega_h \tag{25}$$

where S is a real-valued function defined on  $\mathbb{R}^+ \times$  $\n\Omega_h \times \mathbb{R} \times B(\Omega_h)\n$  where  $B(\Omega_h)$  is the set of bounded functions on  $\Omega_h$ . Typically,  $\{u_h(x), u_h\}$  is the stencil of the method and  $u_h$  denotes the values at the neighbors of x. The "grid"  $\Omega_h$  satisfies

$$\Omega_h \subset \Omega \text{ is closed}\n$$
 and  
 $\n\lim_{h \to 0} \Omega_h = \{x : \exists \{x_h\}, x_h \in \Omega_h, x_h \to x\} = \bar{\Omega} \quad (26)$ 

that is, any point in  $\overline{\Omega}$  can be reached by a sequence of grid points. This assumption is satisfied for any natural family of grids, and it is necessary to have convergence. The grid  $\Omega_h$  may be discrete or continuous ( $\Omega_h = \bar{\Omega}$ ) depending on the scheme. We assume that the scheme  $(25)$  is

**Monotone:** For any  $h > 0$ ,  $x \in \Omega_h$ ,  $r$ , and  $u, v \in$  $B(\Omega_h)$ 

$$u \ge v \implies S(h, x, r, u) \le S(h, x, r, v) \quad (27)$$

**Consistent:** For any smooth function  $\phi$ ,

$$\begin{array}{ll} \liminf_{h \to 0, \ \xi \to 0} S(h, x_h, \phi(x_h) + \xi, \phi + \xi) \\ \Omega_h \ni x_h \to x \end{array}$$
  
 
$$\geq H_*(x, \phi(x), D\phi(x), D^2\phi(x)) \quad \text{and}$$

**Table 1** Monotone explicit and implicit finite-difference schemes

| Equation                                                                 | Scheme                                                                                                                                                                                                                                             | $\text{CFL}$                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| $u_t = \sigma^2 u_{xx}$<br>$\frac{2\sigma^2 \Delta t}{\Delta x^2} \le 1$ | $\begin{cases} u_m^{n+1} = u_m^n + \frac{\sigma^2 \Delta t}{\Delta x^2} \Big[ u_{m+1}^n - 2u_m^n + u_{m-1}^n \Big] \\ u_m^{n+1} = u_m^n + \frac{\sigma^2 \Delta t}{\Delta x^2} \Big[ u_{m+1}^{n+1} - 2u_m^{n+1} + u_{m-1}^{n+1} \Big] \end{cases}$ |                                          |
| $u_t = H(u_x)$                                                           | $u_{m}^{n+1} = u_{m}^{n} + \Delta t \left  H\left(\frac{u_{m+1}^{n} - u_{m-1}^{n}}{\Delta x}\right) + \ H'\ \frac{u_{m+1}^{n} - 2u_{m}^{n} + u_{m-1}^{n}}{\Delta x}\right $                                                                        | $\frac{2\ H'\ \Delta t}{\Delta x} \le 1$ |

 $\limsup S(h, x_h, \phi(x_h) + \xi, \phi + \xi)$  $h \rightarrow 0, \xi \rightarrow 0$  $\Omega_h \ni x_h \to x$  $< H^*(x, \phi(x), D\phi(x), D^2\phi(x))$ 

$$\leq H^*(x,\phi(x),D\phi(x),D^2\phi(x))\tag{28}$$

**Stable** ( $L^{\infty}$  stable): For any  $h > 0$ , there is a solution  $u_h$  of equation (25). Moreover,  $u_h$  is uniformly bounded, that is, there is a constant  $K > 0$  such that for any  $h > 0$ ,

$$|u_h| \le K \qquad \text{in} \qquad \Omega_h \tag{29}$$

**Example 3** Monotone, consistent, and stable schemes are given in Table 1. Note that an explicit scheme is monotone (and stable) only when a CFL condition hold.

Here,  $u_m^n \approx u(x_m, t_n)$  and  $\|\cdot\| = \|\cdot\|_{L^{\infty}}$ . The second equation is a Hamilton-Jacobi equation and the corresponding scheme is called the *Lax-Friedrich* scheme [15].

We assume that the boundary value problem  $(22)$ satisfies the following:

**Strong Comparison Result:** If  $u, v \in B(\overline{\Omega})$  are upper and lower semicontinuous respectively,  $u$  is a subsolution of equation (22), and  $v$  is a supersolution of equation  $(22)$ , then

 $u \le v$  in  $\Omega \cup \Gamma$ where  $\n\Gamma \subset \partial\Omega\n$  (30)

Under the above assumptions, we have the following convergence result:

**Theorem 1** The solution  $u_h$  of equation (25) converge locally uniformly (uniformly on compact subsets) in  $\Omega \cup \Gamma$  to the unique viscosity solution of  $equation (22)$ .

The result is due to Barles and Souganidis and it gives sufficient conditions for locally uniform convergence of approximations. It applies to a very large class of equations, initial/boundary conditions, and (monotone) schemes, see for example, [4, 10, 19]. The only regularity required of the approximating sequence is uniform boundedness. The proof makes use of the Barles-Perthame method of "half relaxed limits" and can be found in  $[10]$ .

Outline of proof: Define

$$\underline{u}(x) = \liminf_{\substack{h \to 0 \\ \Omega_h \ni x_h \to x}} u_h(x_h)\n$$
and
$$\n\overline{u}(x) = \limsup_{\substack{h \to 0 \\ \Omega_h \ni x_h \to x}} u_h(x_h)\n$$
(31)

These functions are upper and lower semicontinuous in  $\overline{\Omega}$ , and by monotonicity and consistency they are respectively sub- and supersolutions of the limiting equation (22). Then, by the strong comparison result it follows that  $\overline{u} < u$  in  $\Omega \cup \Gamma$ . But by definition  $\overline{u} \geq u$  in  $\Omega$ , and hence we have

$$\overline{u} = u \quad \text{in} \quad \Omega \cup \Gamma \tag{32}$$

This immediately implies pointwise convergence. Locally, uniform convergence is followed by a variation of Dini's theorem.

**Remark 1** In Theorem 1 and the strong comparison result, the set  $\Gamma$  always contains all regular points on the boundary  $(\partial \Omega_{\text{reg}} \subset \Gamma)$  and may equal  $\emptyset$ ,  $\partial\Omega$ , or a proper subset of  $\partial\Omega$ . It is equal to  $\partial\Omega$ for Neumann problems or when  $\partial\Omega_{\text{reg}} = \partial\Omega$ . For Dirichlet problems, we refer to papers given in Table 2 below for the precise definition of  $\Gamma$ . When  $\Gamma \neq \partial \Omega$ , then the solution of equation (22) may be discontinuous in  $\partial\Omega \setminus \Gamma$ , see the discussion in the section Viscosity Solutions. In this case, there will be formation of boundary layers in the numerical solutions that prevents (locally) uniform convergence in  $\partial \Omega \setminus \Gamma$ .

**Example 4** A boundary value problem for a heat equation on  $(0, 1)$  and its finite-difference approximation may be written in the forms  $(22)$  and  $(25)$ choosing

$$G(u, u_t, u_{xx}) = \begin{cases} u_t - \sigma^2 u_{xx} + bu_x, & t > 0, \ x \in (0, 1) \\ u, & t > 0, \ x \in \{0, 1\} \end{cases}$$
(33)

where  $b \ge 0$ , and for  $\Delta x = 1/N$ ,  $(0, 1)_{\Delta x}$ <br>=  $\{m\Delta x\}_{m=1}^{N-1}$ , and  $\Delta t = c\Delta x^2$ 

$$S(\Delta x, u_{m}^{n+1}, \{u_{m}^{n}, u_{m\pm 1}^{n}\})$$

$$= \begin{cases} \frac{u_{m}^{n+1} - u_{m}^{n}}{c\Delta x^{2}} - \sigma^{2} \frac{u_{m+1}^{n} - 2u_{m}^{n} + u_{m-1}^{n}}{\Delta x^{2}} \\ + b \frac{u_{m}^{n} - u_{m-1}^{n}}{\Delta x}, & x_{m} \in (0, 1)_{\Delta x} \\ u_{m}^{n+1}, & x_{m} \in \{0, 1\} \end{cases}$$
(34)

The (explicit) scheme is monotone if  $c \le (1/2\sigma^2)$  $+b\Delta x$ ), and consistent:

$$\begin{aligned} |G[\phi] - S[\phi]| &\leq \\ \left\{ \begin{aligned} \left[ \|\phi_{tt}\|c + \frac{\sigma^2}{12} \|\phi_{xxxx}\| \right] \Delta x^2 \\ &+ \frac{b}{2} \|\phi_{xx}\| \Delta x, \end{aligned} \right. & \text{at } x_m \in (0, 1)_{\Delta x} \\ 0, & \text{at } x_m \in \{0, 1\} \end{aligned} \tag{35}$$

The scheme is also stable if  $c \leq (1/2\sigma^2 + b\Delta x)$ and  $\max_{m} |u_{m}^{n+1}| \leq \max_{m} |u_{m}^{0}|$ . If  $\sigma \neq 0, b \geq 0$  are constants,  $u(x, 0)$  is continuous, and  $u(0, 0) = 0 =$  $u(1,0)$ , then the strong comparison result holds in  $[0, 1]$  [13]. Hence by Theorem 1, the finite-difference solution converge locally uniformly as  $\Delta x \rightarrow 0$  to the solution of the equation.

**Example 5** (Degeneracy, boundary layers). In Example 4, we replace  $\sigma$ , b by functions, either

(i) 
$$b = 0, \ \sigma(x) = \begin{cases} \frac{1}{4} - x, & x \in \left(0, \frac{1}{4}\right) \\ 0, & x \in \left(\frac{1}{4}, \frac{3}{4}\right) \\ x - \frac{3}{4}, & x \in \left(\frac{3}{4}, 1\right) \end{cases}$$
  
r (ii)  $b = 1, \ \sigma(x) = x$  (36)

In both cases, the strong comparison result follows from [13], see also [5, 14].

 $\Omega$ 

In case (i), the equation degenerates for  $x \in \left(\frac{1}{4}, \frac{3}{4}\right)$ and the solution is not more than continuous here. But there are no degeneracies at the boundary (it is regular) so the comparison result holds on  $[0, 1]$ and Theorem 1 implies uniform convergence of the numerical solution in  $[0, 1]$ .

In case (ii), the equation degenerates only at the boundary  $x = 0$ . At this point, the exact solution will be discontinuous for  $t > 0$ , and the strong comparison result holds only on  $(0, 1]$ . This is also where the numerical solution will converge by Theorem 1. *Uniform* convergence in  $x = 0$  is not possible because of formation of boundary layers as the numerical solution is refined, see also Example 2.

**Remark 2** (The strong comparison result). A main difficulty in applying Theorem 1 is that the boundary value problem must satisfy the strong comparison result. There are general results that cover most (but probably not all) applications in finance, see Table 2.

In particular, the results of [13] cover Dirichlet (and state constrained) problems for linear and convex second-order PDEs (with or without time) when the domain satisfies an outer ball condition. This includes, for example, all box and convex polyhedral domains in  $\mathbb{R}^n$ .

**Remark 3** (Assumptions on the scheme). See also the discussion in  $[4, 27]$ .

Monotonicity: This condition is analogous to ellipticity of the equation [4, 10, 27], see the discussion at the beginning of this section. For approximations

**Table 2** Strong comparison results

| BC                | Equation                                 | Domain    | Paper      |
|-------------------|------------------------------------------|-----------|------------|
| Dirichlet         | Linear in second<br>derivatives          | Smooth    | [5]        |
|                   | Convex fully<br>nonlinear                | Smooth    | [8]        |
|                   | (includes linear<br>equations)           | Nonsmooth | [13]       |
|                   | Second-order<br>quasilinear              | Smooth    | [9]        |
| Neumann/<br>Robin | Second-order<br>quasi/fully<br>nonlinear |           | see $[14]$ |

of stationary linear equations on a grid  $\{x_m\}_m$ , monotonicity means [26]:

$$u_m = \sum_{k \neq 0} a_k u_{m+k} \quad \text{for} \quad a_k \ge 0 \qquad (u_m \approx u(x_m))$$
(37)

Consistency: The strange formulation above is necessary since we consider the equation and the boundary conditions at the same time, see Example 4.

Stability: The type of stability required here is  $L^{\infty}$ stability and it is more restrictive than  $L^2$  or von Neumann stability. For example, the Crank-Nicolson scheme is unconditionally von Neumann stable but not  $L^{\infty}$  stable in general [7].

Generally speaking, stability (in  $L^{\infty}$ ) follows if  $S(h, x, r, v)$  defined in equation (25) is monotone and *strictly* increasing in  $r$ . This is typically the case for approximations of

- parabolic problems;
- degenerate elliptic problems where  $F$  def. in equation (4) is strictly increasing in  $u$ ;
- uniformly elliptic problems.

Some very general stability results can be found in [7, 27] for whole space problems, while [17, 25, 26] deal with more particular problems on domains.

#### **Error Estimates for Convex Equations**

For linear and nondegenerate problems satisfying condition (5), error estimates follow from classical  $(L^2)$  methods that can be found in most advanced textbooks on numerical solutions of PDEs. For degenerate and/or nonlinear problems these methods do not

apply, and there exists no general theory today. For equations  $(4)$  satisfying condition  $(5)$  there are results in the following cases:

- 1. General first-order equations [15];
- Convex or concave second-order equations 2. [7, 17];
- 3. Nondegenerate second-order equations [12].

In the first case, and to some degree also in the second case, there are rather satisfactory and extensive results. In the rest of this section, we concentrate on the case (ii), since most PDEs in finance belong to this category (including linear ones). The first result in this direction came in two papers of Krylov [22, 23], and his ideas have been developed and improved by several authors since, we refer to  $[7, 17]$  for the most general results at this time.

In what follows, we rewrite the available results in a framework inspired by Barles and Jakobsen [6, 7] and present them in the context of the following possibly degenerate, fully nonlinear, convex model equation:

$$u_{t} + \sup_{\vartheta \in \Theta} \left\{ -\text{tr}[\sigma^{\vartheta} \sigma^{\vartheta} T D^{2} u] - b^{\vartheta} Du + c^{\vartheta} u + f^{\vartheta} \right\}$$
$$= 0 \quad \text{in} \quad \mathbb{R}^{N} \times (0, T) \tag{38}$$

where  $\sigma$  (matrix), b (vector), c, f are functions of  $t, x, \vartheta$ , and <sup>T</sup>/tr denotes transpose/trace of matrices. Note that equation (38) is linear if  $\Theta$  is a singleton. All the results in this section requires that the initial value problem for equation  $(38)$  has a unique solution, which is Lipschitz continuous in  $x$  uniformly in  $t$ . This is the case  $[7]$  if, for example,

$$|u(\cdot, 0)|_1 + |\sigma^{\vartheta}|_1 + |b^{\vartheta}|_1 + |c^{\vartheta}|_1 + |f^{\vartheta}|_1 \le K$$
  
for some *K* independent of  $\vartheta$  (39)

where  $|\phi|_1 = \sup_{x,t} |\phi(x,t)| + \sup_{x \neq y,t} (|\phi(x,t)|$  $-\phi(y, t)/|x - y|$ ). Without loss of generality we also assume that  $c^{\theta} \geq 0$ .

We approximate equation  $(38)$  by a scheme  $(25)$ , which we assume to be as follows:

Monotone and parabolic:  $\phi(t) \in C^1$ ,  $u \le v$  in  $\Omega_h$ 

 $\implies S(h, t, x, r + \phi(t), u + \phi) \ge S(h, t, x, r, v)$ 

$$+\phi'(t) - \frac{Kh^2}{2} \|\phi''\|_{\infty} \tag{40}$$

Consistent:  $\phi(t, x) \in C^{\infty}$ 

Continuous:  $S(h, t, x, r, u)$  uniformly continuous in r uniformly in  $t, x$ .

> $\implies$   $|F(t,x,\phi,\partial_t\phi,D_x\phi,D_x^2\phi)$  $- S(h, t, x, \phi(t, x), \phi)$  $\leq \sum_{i,j} K_{i,j} \|\partial_t^i D_x^j \phi\|_{\infty} h^{\alpha_{i,j}}$  $(41)$

Here  $K, K_{ij}, \alpha_{ij} \geq 0$  are constants independent of h and  $(t, x)$ . Under all of the previously mentioned assumptions, we have the following upper bound on the error:

**Theorem 2** (Upper bound).

$$u - u_{h} \leq C_{u} \min_{\epsilon > 0} \left\{ \epsilon + \sum_{i,j} K_{i,j} \epsilon^{1 - 2i - j} h^{\alpha_{i,j}} \right\} \quad \text{in} \quad \Omega_{h}$$

$$(42)$$

This result was first proved in [23], and we refer to [7] for a discussion on the present formulation. For the most common monotone finite-difference schemes, this result produces the upper bound  $Kh^{1/2}$ [20, 24], which is optimal [16] in this setting.

To get a lower bound, we need additional assumptions as follows:

Convexity:  $S(h, t, x, r, u)$  is convex in  $(r, u)$  and commutes with translations in  $x$ .

Approximation and regularity: For  $h$  small enough and  $0 \leq \epsilon < 1$ , there is unique solution  $u_h^{\epsilon}$  of the scheme

$$\max_{0 \le s \le \epsilon^2, |e| \le \epsilon} S(h, t+s, x+\mathsf{e}, u_h^{\epsilon}(x), u_h^{\epsilon}) = 0 \quad \text{on} \quad \Omega_h$$
(43)

where  $u_h := u_h^0$  solves equation (25), and there is a constant C such that for all s, t, x, y, h,  $\epsilon$ ,

$$|u_h^{\epsilon}(t,x) - u_h^{\epsilon}(s,y)| \le C(|t-s|^{1/2} + |x-y|),$$
  
$$|u_h^0(t,x) - u_h^{\epsilon}(t,x)| \le C\epsilon \tag{44}$$

Under all of the above assumptions, we have the first lower bound:

**Theorem 3** (Lower bound I).

$$u - u_{h} \geq -C_{l_{1}} \min_{\epsilon > 0} \left\{ \epsilon + \sum_{i,j} K_{i,j} \epsilon^{1 - 2i - j} h^{\alpha_{i,j}} \right\}$$
  
in  $\Omega_{h}$  (45)

Alternatively, we may replace the last two assumptions on the scheme  $(25)$  by slightly stronger assumptions on the equation  $(38)$ :

Continuity in  $\vartheta$ :  $\Theta$  is a separable metric space, and  $\sigma, b, c, f$  are continuous in  $\vartheta$  for every  $(t, x)$ . Then we have the second lower bound:

**Theorem 4** (Lower bound II).

$$u - u_h \geq -C_{l_2} \min_{\epsilon > 0} \left\{ \epsilon^{1/3} + \sum_{i,j} K_{i,j} \epsilon^{1 - 2i - j} h^{\alpha_{i,j}} \right\}$$
  
in  $\Omega_h$  (46)

The typical lower bounds produced by Theorems 3 and 4 are  $Kh^{1/2}$ ,  $Kh^{1/5}$ , respectively. The first bound is again optimal, but the result applies only to particular schemes and equations  $[6, 20, 22, 24]$ . The second result is not optimal in general, but it applies to any consistent monotone scheme, see  $[7]$  for the most general results and a wider discussion. Theorem 3 was (essentially) stated in the present general form in [6, 20] and follows from arguments of [22, 23]. Theorem 4 was stated and proved in [6].

**Remark 4** (Approximation and regularity). Under quite general assumptions, see [24], it is possible to show that the "Approximation and regularity" assumption of Theorem 3 holds for any  $\epsilon \in [0, 1)$ whenever it holds for  $\epsilon = 0$ , that is, what we need is a uniform in h Hölder estimate on the solution of  $u_h$ of the scheme  $(25)$ .

**Remark 5** (Proofs). There are  $3-4$  main ideas.

- 1. Mollification of the equation produce a smooth subsolution by convexity. An upper bound on the error then follows from classical  $L^{\infty}$ -argument using monotonicity and consistency [22].
- The method of shaking the coefficients allows 2. to treat general problems with variable coefficients [23].
- 3. The lower bound. Either you (i) interchange the role of the scheme and the equation in

part (1) to get bound I, or (ii) you introduce additional approximations to avoid working with the scheme and get a type II bound [7, 23]. In case (i), you need a uniform Lipschitz bound on the solutions of the scheme, which is very difficult to obtain in general.

**Remark 6** (Extensions). Stationary problems have been considered in several papers, including some boundary value problems, see [7, 17]. There have been papers treating more general equations like parabolic obstacle problems, impulse control problems, and integro-differential problems (see Partial Integro-differential Equations (PIDEs)). When solutions are less regular (Hölder continuous), lower rates have been obtained in  $[6, 7]$  and in some cases when solutions are more regular, higher order of convergence can be obtained  $[16]$ .

**Example 6** Consider a special case of equation (38),

$$u_{t} + \sup_{\vartheta \in \Theta} \Big\{ -\sum_{\beta} \Big[ (\bar{\sigma}_{\beta}^{\vartheta})^{2} D_{\beta}^{2} + \bar{b}^{\vartheta} D_{\beta} \Big] u + c^{\vartheta} u + f^{\vartheta} \Big\}$$
$$= 0 \quad \text{in} \quad \mathbb{R}^{N} \times (0, T) \tag{47}$$

where  $\bar{b} \geq 0$ ,  $\bar{\sigma}$  are scalar functions,  $D_{\beta} = \beta \cdot D$  is a directional derivative, and  $\{\beta\}$  is a finite collection of vectors in  $\mathbb{Z}^N$ . We approximate on a uniform grid  $\Omega_h = h\mathbb{Z} \times ch^2\mathbb{Z}^+$  by an implicit finite-difference scheme proposed in  $[11, 24]$ 

$$u_{\alpha}^{n+1} = u_{\alpha}^{n} + \Delta t \sup_{\theta \in \Theta} \left\{ -\sum_{\beta} \left[ (\bar{\sigma}_{\beta}^{\vartheta})^{2} \Delta_{h\beta} + \bar{b}^{\vartheta} \delta_{\beta h}^{+} \right] \right.$$
$$\left. \times u_{\alpha}^{n+1} + c^{\theta} u_{\alpha}^{n+1} - f^{\theta} \right\} = 0 \tag{48}$$

$$\times u_{\alpha}^{++} + c^* u_{\alpha}^{++} - f^* \} = 0 \tag{4}$$

for  $n \in \mathbb{Z}^+$ ,  $\alpha \in \mathbb{Z}^n$ , and where

$$\Delta_{h\beta}w(x) = \frac{w(x+h\beta) - 2w(x) + w(x-h\beta)}{h^2|\beta|^2}$$

and 
$$\delta_{h\beta}^+ w(x) = \frac{w(x+\beta h) - w(x)}{h|\beta|} \tag{49}$$

This scheme is obviously monotone and a Taylor expansion shows that

$$|F(t, x, \phi, \partial_t \phi D\phi, D^2\phi) - S(h, t, x, \phi(t, x), \phi)|$$
  

$$\leq C(ch^2|\phi_{tt}|_0 + h|D^2\phi|_0 + h^2|D^4\phi|_0)$$
(50)

If  $\bar{\sigma}, \bar{b}, c, f, u(0, \cdot)$  are uniformly x-Lipschitz, then  $u_h$  is also uniformly x-Lipschitz [24], and by Theorems 2 and 3 we get

$$|u - u_{\alpha}^{n}| \le Ch^{1/2} \tag{51}$$

From a practical or probabilistic point of view,  $\bar{\sigma}$ need not be Lipschitz. In this case, Theorems 2 and 4 vield a worse bound:

$$|u - u_{\alpha}^{n}| \le Ch^{1/5} \tag{52}$$

Note that we have imposed the CFL condition  $\Delta t =$  $c\Delta x^2$  ( $\Delta x = h$ ). If this condition is not satisfied, then the rates will be reduced. We refer to [7] for more general explicit and implicit schemes of this kind.

# References

- [1] Bardi, M. & Capuzzo-Dolcetta, I. (1997). Optimal Control and Viscosity Solutions of Hamilton-Jacobi-Bellman Equations, Birkhäuser.
- [2] Bardi, M., Crandall, M.G., Evans, L.C., Soner, H.M. & Souganidis, P.E. (1997). Viscosity solutions and applications, Lecture Notes in Mathematics, Springer-Verlag, Berlin, pp. 1660.
- [3] Barles, G. (1994). Solutions de Viscosite des Equations de Hamilton-Jacobi, Mathematiques & Applications, Springer-Verlag, Paris, p. 17.
- Barles, G. (1997). Convergence of numerical schemes [4] for degenerate parabolic equations arising in finance theory, in Numerical Methods in Finance, Newton Institute, Cambridge University Press, Cambridge, pp. 1-21.
- [5] Barles, G. & Burdeau, J. (1995). The Dirichlet problem for semilinear second-order degenerate elliptic equations and applications to stochastic exit time control problems. Communications in Partial Differential Equations  $20(1-2), 129-178.$
- [6] Barles, G. & Jakobsen, E.R. (2002). On the convergence rate of approximation schemes for Hamilton-Jacobi-Bellman equations, M2AN Mathematical Modelling and Numerical Analysis 36(1), 33-54.
- Barles, G. & Jakobsen, E.R. (2007). Error bounds [7] for monotone approximation schemes for parabolic Hamilton-Jacobi-Bellman equations, Mathematics of Computation 76(260), 1861-1893.
- Barles, G. & Rouy, E. (1998). A strong comparison [8] result for the Bellman equation arising in stochastic exit time control problems and its applications, Communications in Partial Differential Equations 23(11-12), 1995-2033.
- [9] Barles, G., Rouy, E. & Souganidis, P.E. (1999). Remarks on the Dirichlet problem for quasilinear elliptic and parabolic equations, in Stochastic Analysis, Control, Optimization and Applications, W.M. McEneaney, G.G. Yin & Q. Zhang, eds, Systems & Control Foundations & Applications, Birkhäuser, Boston, pp. 209-222.

- [10] Barles, G. & Souganidis, P.E. (1991). Convergence of approximation schemes for fully nonlinear second order equations, *Asymptotic Analysis* **4**(3), 271–283.
- [11] Bonnans, F. & Zidani, H. (2003). Consistency of generalized finite difference schemes for the stochastic HJB equation, *SIAM Journal of Numerical Analysis* **41**(3), 1008–1021.
- [12] Caffarelli, L.A. & Souganidis, P.E. (2008). A rate of convergence for monotone finite difference approximations to fully nonlinear, uniformly elliptic PDEs. *Communications on Pure Applied Mathematics* **61**(1), 1–17.
- [13] Chaumont, S. (2004). Uniqueness to elliptic and parabolic Hamilton–Jacobi–Bellman equations with non-smooth boundary, *C. R. Mathematical Academy of Science, Paris* **339**(8), 555–560.
- [14] Crandall, M.G., Ishii, H. & Lions, P.-L. (1992). User's guide to viscosity solutions of second order partial differential equations, *Bulletin of the American Mathematical Society (N.S.)* **27**(1), 1–67.
- [15] Crandall, M.G. & Lions, P.-L. (1984). Two approximations of solutions of Hamilton–Jacobi equations, *Mathematics of Computation* **43**(167), 1–19.
- [16] Dong, H. & Krylov, N.V. (2005). Rate of convergence of finite-difference approximations for degenerate linear parabolic equations with *C*<sup>1</sup> and *C*<sup>2</sup> coefficients, *Electronic Journal of Differential Equations* **2005**(102), 1–25.
- [17] Dong, H. & Krylov, N.V. (2007). The rate of convergence of finite-difference approximations for parabolic Bellman equations with Lipschitz coefficients in cylindrical domains, *Applied Mathematics and Optimization* **56**(1), 37–66.
- [18] Evans, L.C. (1998). *Partial Differential Equations*, *Graduate Studies in Mathematics*, American Mathematical Society, Providence, p. 19.
- [19] Fleming, W.H. & Soner, H.M. (1993). *Controlled Markov Processes and Viscosity Solutions*, Springer-Verlag, New York.
- [20] Jakobsen, E.R. (2003). On the rate of convergence of approximation schemes for Bellman equations associated with optimal stopping time problems, *Mathematical Models and Methods in Applied Science (M3AS)* **13**(5), 613–644.

- [21] Koike, S. (2004). *A Beginner's Guide to the Theory of Viscosity Solutions*, *MSJ Memoirs*, Mathematical Society of Japan, Tokyo, p. 13.
- [22] Krylov, N.V. (1997). On the rate of convergence of finite-difference approximations for Bellman's equations, *St. Petersburg Mathematical Journal* **9**(3), 639–650.
- [23] Krylov, N.V. (2000). On the rate of convergence of finite-difference approximations for Bellman's equations with variable coefficients, *Probability Theory and Related Fields* **117**, 1–16.
- [24] Krylov, N.V. (2005). On the rate of convergence of finite-difference approximations for Bellman equations with Lipschitz coefficients, *Applied Mathematics and Optimization* **52**(2), 365–399.
- [25] Kuo, H. & Trudinger, N.S. (1995). Local estimates for parabolic difference operators, *Journal of Differential Equations* **122**(2), 398–413.
- [26] Motzkin, T.S. & Wasow, W. (1953). On the approximation of linear elliptic differential equations by difference equations with positive coefficients, *Journal of Mathematical Physics* **31**, 253–259.
- [27] Oberman, A.M. (2006). Convergent difference schemes for degenerate elliptic and parabolic equations: Hamilton-Jacobi equations and free boundary problems, *SIAM Journal of Numerical Analysis* **44**(2), 879–895.
- [28] Oleinik, O.A. & Radkevic, E.V. (1973). *Second Order Equations with Nonnegative Characteristic Form*, Plenum Press, New York-London.
- [29] Pooley, D.M., Forsyth, P.A. & Vetzal, K.R. (2003). Numerical convergence properties of option pricing PDEs with uncertain volatility, *IMA Journal of Numerical Analysis* **23**(2), 241–267.

# **Further Reading**

Kushner, H.J. & Dupuis, P. (2001). *Numerical Methods for Stochastic Control Problems in Continuous Time*, Springer-Verlag, New York.

ESPEN R. JAKOBSEN
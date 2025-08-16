# **Finite Element Methods**

The finite element method (FEM) has been invented by engineers around 1950 for solving the partial differential equations arising in solid mechanics; the main idea was to use the principle of virtual work for designing discrete approximations of the boundary value problems. The most popular reference on FEM in solid mechanics is the book by Zienckienwicz [14]. Generalizations to other fields of physics or engineering have been done by applied mathematicians through the concept of variational formulations and weak forms of the partial differential equations (see, e.g. [4]).

In finance, partial differential equations (PDEs) or partial integro-differential equations (PIDEs) may be used for option pricing. For approximating their solutions, at least four classes of numerical methods can be used:

- *Finite difference methods* are by far the simplest, except when mesh adaptivity is required in which case it is rather difficult to control the numerical error.
- Finite volume methods are not really natural, because these methods are better suited for hyperbolic PDEs. In finance, they may be useful, for example, for Asian options when the PDE becomes close to hyperbolic near maturity.
- Spectral methods are Galerkin methods with Fourier series of high degree polynomials. They are ideal when the coefficients of the PDE are constant, which is rarely the case in financial engineering. For a very efficient adaptation of spectral methods to finance, see [10].
- Finite element methods seem at first glance unnecessarily complex for finance where a large class of problems are one dimensional in space. Yet, they are very flexible for mesh adaptivity and the implementation difficulties are only apparent.

## A Simple Example

Take the simplest case, the Black–Scholes model for a put option with a strike  $K$  and a maturity  $T$ . The price of the underlying asset is assumed to be a geometric Brownian motion

$$dS_t = S_t(\mu \, dt + \sigma \, dW_t) \tag{1}$$

and the volatility  $\sigma$  is allowed to depend on  $S_t$  and t. If the volatility function satisfies suitable regularity conditions, the Black-Scholes formula gives the option's price at time  $t < T$ :

$$P_t = \mathbb{E}^* (\mathrm{e}^{-r(T-t)} (K - S_T)^+ | \mathcal{F}_t) \tag{2}$$

where  $\mathbb{E}^*(|\mathcal{F}_t)$  stands for the conditional expectation with respect to the risk neutral probability. It can be proved that with  $\sigma = \sigma(S_t, T - t)$ , then  $P_{T-t} =$  $u(S_{T-t}, T-t)$ , where u is the solution of

$$\begin{cases} \partial_t u - \frac{\sigma^2 x^2}{2} \partial_{xx} u - rx \partial_x + ru = 0\\ \text{for } x > 0, 0 < t \le T\\ u(x, 0) = (K - x)^+ \end{cases} \tag{3}$$

The variational formulation of equation  $(3)$  consists of finding a continuous function  $u$  defined on the time interval  $[0, T]$  with value in a Hilbert space V (see equation  $(5)$  such that

$$\frac{\mathrm{d}}{\mathrm{d}t}(u, w) + a_t(u, w) = 0$$
  
for a.a.  $t \in (0, T) \quad \forall w \in V$   
$$u(x, 0) = (K - x)^+ \tag{4}$$

where

$$V = \left\{ v \in L^2(\mathbb{R}_+) : x \frac{\mathrm{d}v}{\mathrm{d}x} \in L^2(\mathbb{R}_+) \right\}$$
$$\times a_t(u, w) = \left( \frac{\sigma^2 x^2}{2} \partial_x u, \partial_x w \right)$$
$$+ \left( x \partial_x u, (\sigma^2 + x \sigma \partial_x \sigma - r) w \right) + (ru, w)$$
$$\times (u, w) = \int_0^\infty u(x) w(x) \, \mathrm{d}x \tag{5}$$

Problem  $(4)$  is obtained by multiplying equation  $(3)$ by  $w(x)$ , integrate on  $\mathbb{R}^+$ , and integrate by part the term containing  $\partial_{xx}u$ . The precise meaning of equation  $(4)$  and the conditions for equation  $(4)$  to have a unique solution are subtle. The choice of the space  $V$  is dictated by the following: the integrals in equation (4) must exist, and the bilinear form  $a_t$ must be continuous on  $V \times V$  uniformly in time and satisfy Gårding's coercivity inequality, that is, that there exist constants c and  $\lambda$ ,  $c > 0$  and  $\lambda \ge 0$  such that

$$a_t(v, v) \ge c \|v\|_V^2 - \lambda \|v\|_{L^2(\mathbb{R}_+)}^2 \quad \forall v \in V \tag{6}$$

**Proposition 1** If  $\sigma$  is a continuous function such that for all  $x, t, \sigma(x, t) \in [\sigma_m, \sigma_M], \sigma_m > 0$ , and if  $x \mapsto x\sigma$  is Lipschitz continuous with a Lispschitz constant independent of  $t$ , then equation (4) has a unique solution.

The simplest finite element methods are discrete versions of equation (4) obtained by replacing  $V$ with a finite dimensional space  $V_h$ , that is, finding a continuous function  $u_h$  defined on the time interval  $[0, T]$  with value in the finite dimensional space  $V_h \subset V$  such that

$$\frac{d}{dt}(u_h, w_h) + a_t(u_h, w_h) = 0 \text{ for a.a. } t \in (0, T)$$
(7)

If  $\{w^i\}_1^N$  is a basis of  $V_h$ , then equation (6) is equivalent to

$$\frac{\mathrm{d}}{\mathrm{d}t} \left( \sum_{1}^{N} u_{j} w^{j}, w^{i} \right) + a_{t} \left( \sum_{1}^{N} u_{j} w^{j}, w^{i} \right) = 0$$
  
$$\forall i = 1, \dots, N \tag{8}$$

which is a system of differential equations

$$B\frac{\mathrm{d}U}{\mathrm{d}t} + A(t)U = 0 \quad \text{where } B_{ij} = (w^j, w^i)$$
  
$$A_{ij}(t) = a_t(w^j, w^i) \tag{9}$$

A discrete time stepping scheme has still to be applied to equation (9), for instance, the Euler implicit scheme

$$B\frac{U^{m+1} - U^m}{\delta t_m} + A^{m+1}U^{m+1} = 0 \qquad (10)$$

where  $A^m = A(t_m)$ . The easiest choice is to take  $V_h$ as a space of piecewise linear functions (linear finite elements), that is,

$$V_h = \{v_h \text{ continuous, linear on each subinterval}$$
  
 $[x_{i-1}, x_i], v_h(L) = 0\}$ 

where  $(x_i)_{i=1,\dots,N}$  is an increasing sequence in the interval  $[0, L] \approx \mathbb{R}^+$ , with  $x_1 = 0$  and  $x_N = L$ . Then a good choice for  $w^i$  is to be the (hat) function of  $V_h$ , which is equal to one at  $x_i$  and zero at  $x_j$ ,  $j \neq i$ (see [2]). With this basis, called the *nodal basis*, the integrals  $B_{ij}$  and  $A_{ij}$  can be computed exactly.

It is easy to show that the matrices  $A$  and  $B$  are tridiagonal so that a resolution of the linear system  $(10)$  at each time step is best done with a Gaussian elimination method or an LU factorization. In the end the computational complexity is the same as for a finite difference method with either an explicit or an implicit time scheme.

Convergence in the  $V$ -norm can be proved to be of the order of  $h + \delta t$  ( $h^2 + \delta t$  in the  $L^2$ -norm); it is possible to improve it by using Crank-Nicolson scheme and higher order polynomials instead of the linear ones. Most interesting is the following  $a$ *posteriori* estimate:

#### **Proposition 2**

$$\begin{split} &[[u - u_{h,\delta t}]](t_n) \le c(u_0)\delta t \\ &+ c \frac{\mu}{\sigma_m^2} \left( \sum_{m=1}^n \eta_m^2 + (1+\rho)^2 \max(2, 1+\rho) \right. \\ &\times \sum_{m=1}^n \frac{\delta t_m}{\sigma_m^2} \prod_{i=1}^{m-1} (1-2\lambda \delta t_i) \sum_{\omega \in \mathcal{T}_{mh}} \eta_{m,\omega}^2 \right)^{1/2} \end{split} \tag{11}$$

where  $\mu$  is the continuity constant of  $a_t$ ,  $\rho =$  $\max_{2\leq n\leq N} \delta t_n/\delta t_{n-1}$ ,  $\mathcal{T}_{mh}$  is the partition of  $(0, L)$  in small intervals  $\omega$  at time  $t_m$  and

$$\eta_m^2 = \delta t_m e^{-2\lambda t_{m-1}} \frac{\sigma_m^2}{2} |u_h^m - u_h^{m-1}|_V^2$$
  
$$\eta_{m,\omega} = \frac{h_\omega}{x_{\text{max}}(\omega)} \left\| \frac{u_h^m - u_h^{m-1}}{\delta t_m} - rx \frac{\partial u_h^m}{\partial x} + ru_h^m \right\|_{L^2(\omega)}$$
  
(12)

and  $h_{\omega}$  is the diameter of  $\omega$ .

Note that everything is known after the computation of  $u_h$ ; the mesh can then be adapted by using the error indicators  $\eta_m$  and  $\eta_{m,\omega}$ . Figure 1 shows the computed *a posteriori* error and the actual error for

![](_page_2_Figure_1.jpeg)

Figure 1 (a) The graph displays the error between the computed solution on a uniform mesh and one computed with Black-Scholes formula. (b) The graph shows  $\rho_{\delta t}$ ; (c) the graphs show  $\eta_{n,\omega}$  as a function of x and t. The parameters are  $K = 100, T = 0.5, r = 0, \sigma = 0.3, 50 \text{ time steps, and } 100 \text{ mesh points}$ 

a vanilla put with constant volatility and comparison with the Black-Scholes analytic formula.

#### **Stochastic Volatility Models**

We now discuss a more involved stochastic volatility model where  $dS_t = S_t(\mu dt + \sigma_t dW_t)$ , with  $\sigma_t =$  $f(Y_t)$  and  $Y_t$  is a mean-reverting Onrstein-Uhlenbeck process

$$dY_t = \alpha (m - Y_t) dt + \beta d\hat{Z}_t \tag{13}$$

and  $\hat{Z}_t = \rho W_t + \sqrt{1 - \rho^2} Z_t$   $W_t$  and  $Z_t$  are two uncorrelated Brownian motions. In the Stein-Stein model, see [12],  $f(Y_t) = |Y_t|$ .

If  $P(S, y, T - t)$  is the pricing function of a put option, it is convenient to introduce

$$u(S, y, t) = P(S, y, T - t)e^{-(1-\eta)(y-m)^2/2\nu^2} \quad (14)$$

where  $\eta$  is any parameter between 0 and 1 and  $\nu^2 = \beta^2/(2\alpha).$ 

A clever financial argument (see  $[7]$ ) shows that when  $\rho = 0$  for simplicity, the new unknown u satisfies, for all  $x > 0, y \in \mathbb{R}, t > 0$ 

$$\begin{cases} \frac{\partial u}{\partial t} - \frac{1}{2}y^2 x^2 \frac{\partial^2 u}{\partial x^2} - \frac{1}{2}\beta^2 \frac{\partial^2 u}{\partial y^2} - rx\frac{\partial u}{\partial x} + e\frac{\partial u}{\partial y} \\ + fu = 0 \\ u(x, y, 0) = (K - x)^+ \quad \text{for} \quad x > 0, y \in \mathbb{R} \end{cases} \tag{15}$$

whereof

$$e = -(1 - 2\eta)\alpha(y - m) + \beta\gamma$$
  
$$f = r + 2\frac{\alpha^2}{\beta^2}\eta(1 - \eta)(y - m)^2$$

$$+2(1-\eta)\frac{\alpha}{\beta}(y-m)\gamma-\alpha(1-\eta) \quad (16)$$

and  $\gamma$  is a risk premium factor, possibly a function of  $x, y, t$ ; see [1] for the details.

This parabolic equation is degenerate near the axis y = 0 because the coefficient in front of  $x^2 \frac{\partial^2 P}{\partial x^2}$ vanishes on  $y = 0$ . Following [1], see also [2, 3], let us consider the weighted Sobolev space  $V$  on  $Q = \mathbb{R}^+ \times \mathbb{R}$ :

$$V = \left\{ v : \ v\sqrt{1+y^2}, \ \frac{\partial v}{\partial y}, x|y|\frac{\partial v}{\partial x} \in L^2(Q) \right\} \tag{17}$$

which is a Hilbert space such that all the properties needed by the variational arguments sketched earlier hold.

**Theorem 1** If the data are smooth (see [1, 3]) and if

$$r(t) \ge r_0 > 0, \quad \alpha^2 > 2\beta^2, \quad 2\alpha^2 \eta (1 - \eta) > \beta^2$$
(18)

then equation  $(15)$  has a unique weak solution.

#### Finite Element Solution

As usual, we localize the problem in  $\Omega := (0, L_r) \times$  $(-L_{\rm v}, L_{\rm v})$ . No boundary condition is needed on the axis  $x = 0$  since the PDE is degenerate there. Note also that  $u$  is expected to tend to zero as  $x$  tends to infinity. For large  $y$ , no arguments seem to give a boundary condition. However, if  $L_{\nu}$  is chosen such that  $\alpha(L_{\rm v} \pm m) \gg \beta^2$ , then for  $y \sim \pm L_{\rm v}$ , the coefficient of the advection term in the  $y$  direction, that is,  $\alpha(y - m)$ , is much larger in absolute value

than the coefficient of the diffusion in the  $y$  direction, that is,  $\frac{\beta^2}{2}$ . Furthermore, near  $y = \pm L_y$ , the vertical velocity  $\alpha(y - m)$  is directed outward  $\Omega$ . Therefore, the error caused by an artificial condition on  $y = \pm L_y$ is damped away from the boundaries, and localized in boundary layers whose width is of the order of  $\frac{\beta^2}{\alpha \bar{\nu}}$ . We may thus apply a Neumann condition.

Then one must write the problem in variational form: find u in  $V_0$  the subset of V of functions that are zero at  $x = L_x$  and

$$\begin{cases} \frac{\mathrm{d}}{\mathrm{d}t}(u,w) + a(u,w) = 0 \quad \forall w \in V_0 \\ u(x,y,0) \text{ given} \end{cases} \tag{19}$$

with

$$a(u, w) = \int_{\Omega} \frac{y^2 x^2}{2} \partial_x u \partial_x w + \frac{\beta^2}{2} \partial_y u \partial_y w$$
  
+ 
$$(y^2 - r) x \partial_x u + (e + \beta \partial_y \beta) \partial_y u + f u) w$$
  
(20)

Now  $\Omega$  is triangulated into a set of nonintersecting triangles  $\{\omega_k\}_1^K$  in such a way that no vertices lie in the middle of an edge of another triangle.  $V_0$ is approximated by  $V_{0h}$  the space of continuous piecewise linear functions on the triangulation, which vanish at  $x = L_x$ .

The functions of  $V_{0h}$  are completely determined by their values at the vertices of the triangles, so if we denote by  $w^i$  the function in  $V_{0h}$ , which takes the value zero at all vertices except the  $i$ th one where it is one, then  $\{w^i\}_1^N$  is a basis of  $V_{0h}$  if N is the number of vertices not on  $x = L_x$  (it is convenient for the presentation to number the nodes on the boundary last).

As in the one-dimensional case

$$u_h^m(x, y) = \sum_{1}^{N} u_i^m w^i(x, y) \tag{21}$$

is an approximation of  $u(t_m)$  if the  $u_i^{m+1}$ are solutions of

$$B\frac{U^{m+1} - U^m}{\delta t_m} + AU^{m+1} = 0 \tag{22}$$

with  $B_{ij} = (w^j, w^i)$  and  $A_{ij} = a(w^j, w^i)$ .

#### *Numerical Implementation*

Integrals of polynomial expressions of  $x, y$  can be evaluated exactly on triangles (formula  $(4.19)$  in [2]). The difficulty is in the strategy to solve the linear systems (22). Multigrid seems to give the best results in term of speed [11], but the computer program may not be so easy to write for an arbitrary triangulation. Since the number of vertices are not likely to exceed a few thousands, fast multifrontal libraries such as SuperLU [6] can be used with a minimum programming effort. Table 1 shows the gain in time over more classical algorithms.

Alternatively one could also use a preconditioned conjugate gradient-like iterative method (see Conjugate Gradient Methods). Another way is eqf12-005 to use FreeFem++ [9], which is a general twodimensional PDE solver particularly well suited to these option pricing models, where the coefficients are involved functions and one may want to try to change them often. Results for equation (22) obtained with the following FreeFem++ code are shown in Figure 2.

A similar program has been developed in 3D by S. Delpino: freefem3d. However, mesh refinement is not yet implemented. A basket option has been computed for illustration (Figure 3). The script that drives the program is self-explanatory and gives the values used.

<table>

 **Table 1** Comparison of CPU time for the LU algorithm and superLU for a product put option on
 a uniform mesh and 200 step time (computed by N. Lantos)

| Mesh size        | $Gauss-LU(s)$ | Relative error $(\%)$ | $\text{SuperLU (s)}$ | Relative error $(\%)$ |
|------------------|---------------|-----------------------|----------------------|-----------------------|
| $101 \times 101$ | 10.094        | 3.532                 | 2.39                 | 3.076                 |
| $126 \times 126$ | 14.547        | 1.338                 | 4.016                | 1.797                 |
| $151 \times 151$ | 22.313        | 0.751                 | 6.203                | 0.489                 |
| $176 \times 176$ | 31.985        | 1.131                 | 8.735                | 0.790                 |
| $201 \times 201$ | 43.938        | 0.432                 | 12.109               | 0.670                 |

```
real T=1, K=100, r=0.05, alpha=1, beta=1 , m=0.2 , gamma=0, eta=0.5;
int Lx=800, Ly=3, Nmax=50;
real scale=100, dt =T/Nmax;
mesh th = square(50,50,[x*Lx,(2*y-1)*Ly*scale]);
fespace Vh(th,P1);
func u0 = max(K-x,0.)*exp(-(1-eta)*(y/scale-m)^2 * alpha/(beta^2));
func e = beta*gamma -(1-2*eta)*alpha*(y/scale-m);
func f = r + 2*(alpha/beta)^2 * eta*(1-eta)*(y/scale-m)^2
     + 2*(1-eta)*(alpha/beta)*(y/scale-m)*gamma - alpha*(1-eta);
Vh uold=u0,u,v;
problem stein(u,v,init=n) = int2d(th)( u*v*(f+1/dt)
   + dx(u)*dx(v) *(x*y/scale)^2/2 + dy(u)*dy(v) *(beta*scale)^2/2
   + dx(u)*v *x*((y/scale)^2-r) + dy(u)*v *e*scale
   ) - int2d(th)(uold*v/dt) + on(2,u=0) ;
for (int n=0; n<Nmax ; n++){ stein; uold=u; };
// call to keyword adaptmesh not shown..
double N = 25; double L=200.0; double T=0.5;
double dt = T / 15 ; double K=100; double r = 0.02;
double s1 = 0.3; double s2 = 0.2; double s3 = 0.25;
double q12 = -0.2*s1*s2; double q13 = -0.1*s1*s3;
double q23 = -0.2*s2*s3; double s11 = s1*s1/2;
double s22=s2*s2/2; double s33=s3*s3/2;
vector n = (N,N,N);
vector a = (0,0,0);
vector b = (L,L,L);
mesh M = structured(n,a,b);
femfunction uold(M) = max(K-x-y-z,0);
femfunction u(M);
double t=0; do {
   solve(u) in M cg(maxiter=900,epsilon=1E-10)
   {
pde(u) (1./dt+r)*u-dx(s11*x*x*dx(u))-dy(s22*y*y*dy(u))-dz(s33*z*z*dz(u))
       - dx(q12*x*y*dy(u)) - dx(q13*x*z*dz(u)) - dy(q23*y*z*dz(u))
       - r*x*dx(u) - r*y*dy(u) - r*z*dz(u) = uold/dt;
      dnu(u)=0 on M;
   }; t = t + dt;
} while(t<T);
save(medit,"u",u,M); save(medit,"u",M);
```

![](_page_5_Figure_1.jpeg)

**Figure 2** Solution of equation  $(15)$  for a put with maturity  $T = 1$ , strike  $K = 100$  with  $r = 0.02$ ,  $\beta = \alpha = 1$ , and  $m = 0.2$ . We have used the automatic mesh adaptivity of FreeFem++; the contours and the triangulation are shown

![](_page_5_Figure_3.jpeg)

Figure 3 A put on a basket of three assets computed with freefem3d [5] with maturity  $T = 0.5$ , strike  $K = 100$ , and so on (see the listing). The visualization is done with medit also public domain [8]

# **Asian Calls**

For the financial modeling of Asian options, we refer to  $[13]$  and the references therein.

We consider an Asian put with fixed strike whose payoff is  $P_0(S, y) = (y - K)_+$ , calling y the average value of the asset in time,  $y = 1/t \int_0^t S(\tau) d\tau$ . The price of the option is found by solving for all

![](_page_5_Figure_8.jpeg)

**Figure 4** Solution of equation (24) for an Asian option of maturity  $T = 4$  and strike  $K = 100$  when the interest rate is  $0.03$  and the volatility  $0.3$ . The figure shows the contours at times  $0.96$  (a),  $1.96$  (b), and  $3.96$  (c)

 $\{x, y, t\} \in \mathbb{R}^+ \times \mathbb{R}^+ \times (0, T)$ 

$$\partial_t u - \partial_x \left( \frac{\sigma^2 x^2}{2} \partial_x u \right) + (\sigma^2 - r) x \partial_x u$$
$$+ \frac{y - x}{2} \partial_x u + r u = 0 \tag{23}$$

$$+\frac{y-x}{T-t}\partial_y u + ru = 0\tag{23}$$

$$u(x, y, 0) = (y - K)^{+}, \ \partial_{x}u|_{+\infty, y, t}$$
  
$$\approx \left| \frac{\frac{t}{T}e^{-rt} \text{if } y < \frac{KT}{T - t}}{\frac{1 - re^{-rt}}{Tr}} \text{ otherwise} \right|$$
(24)

The difficulties of this problem is that the secondorder part of the differential operator is incomplete and the convective velocity  $v = \left((\sigma^2 - r)x, \frac{y-x}{T-t}\right)^T$ tends to infinity as  $t \rightarrow T$ ; so great care must be taken for the upwinding of these first-order terms. One of the best upwinding is the characteristic finite element method, whereby

$$\partial_t u + v \cdot \nabla u|_{x,y,t_{m+1}} \approx \frac{1}{\delta t} (u^{m+1}(q) - u^m(Q))$$

with

$$Q = q - \delta t v \left( q - v(q) \frac{\delta t}{2} \right) \text{ where } q = (x, y)^{\text{T}}$$
(25)

The discontinuous  $P^2$  reconstruction with characteristic convection of the gradient and of the value at the center of gravity is applied. The domain is localized to  $(0, L) \times (0, L)$ , with  $L = 250$ , that is, greater than twice the contract price  $K = 100$ , in this example; the interest rate is  $r = 3\%$  and the volatility  $\sigma = 0.3$ . The square domain is triangulated by a uniform  $50 \times 50$ mesh and we have taken 50 time steps over the fouryears period of this example  $(T = 4)$ . The results are shown in Figure 4 at time  $t = 0.96$ , 1.96, and 3.96.

### References

- Achdou, Y. & Tchou, N. (2002). Variational analysis for [1] the Black and Scholes equation with stochastic volatility, M2AN Mathematical Modelling and Numerical Analysis 36(3), 373-395.
- [2] Achdou, Y. & Pironneau, O. (2005). Computational Methods For Option Pricing, Frontiers in Applied Math*ematics*, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA.
- [3] Achdou, Y. & Pironneau, O. (2009). chapter Partial differential equations for option pricing. Handbook on *Mathematical Finance*, Elsevier, to appear.
- [4] Ciarlet, P.G. (1991). Basic error estimates for elliptic problems, Handbook of Numerical Analysis, North-Holland, Amsterdam, Vol. II, pp. 17-351.
- [5] Delpino, S. freefem3d, www.freefem.org.
- [6] Demmel, J.W., Gilbert, J.R. & Li, X.S. (1999). SuperLU Users' Guide, LBNL-44289, Ernest Orlando Lawrence Berkeley National Laboratory, Berkeley, CA.
- Fouque, J.P., Papanicolaou, G. & Sircar, K.R. (2000). [7] Derivatives in Financial Markets with Stochastic Volatility, Cambridge University Press, Cambridge.
- [8] Frey, P. Medit a Visualization Software, www.ann. jussieu.fr/~frey/logiciels/medit.html.
- [9] Hecht, F. & Pironneau, O. *freefem++*, www.freefem. org.
- [10] Huang, X. & Cornelis, W. (2008). *Oosterlee Adaptive* integration for multi-factor portfolio credit loss models, Finance and Stochastics, to appear.
- [11] Ikonen, S. & Toivanen, J. (2008). Efficient numerical methods for pricing American options under stochastic volatility, Numerical Methods for Partial Differential Equations  $24(1)$ , 104-126.
- [12] Stein, E. & Stein, J. (1991). Stock price distributions with stochastic volatility : an analytic approach, The Review of Financial Studies 4(4), 727-752.
- [13] Wilmott, P., Dewynne, J. & Howison, S. (1993). *Option* Pricing. Oxford Financial Press, Oxford.
- [14] Zienkiewicz, O.C. & Taylor, R.L. (2000). The Finite Element Method, 5th Edition, Butterworth-Heinemann, Oxford, Vol. 1, The basis.

YVES ACHDOU & OLIVIER PIRONNEAU
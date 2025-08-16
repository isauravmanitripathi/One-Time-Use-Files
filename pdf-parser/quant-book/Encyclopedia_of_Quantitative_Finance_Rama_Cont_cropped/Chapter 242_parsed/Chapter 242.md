# **Alternating Direction** Implicit (ADI) Method

In the Black-Scholes model, option values are characterized as solutions of certain partial differential equations (PDEs) for European options or partial differential inequalities for American options (see Partial Differential Equations). In general, these option values have to be evaluated numerically, for example using the finite difference method (see Finite Difference Methods for Barrier Options; Finite Difference Methods for Early Exercise Options). Unfortunately, when considering the pricing of options depending on several assets, the finite difference method suffers from the curse of dimensionality. The alternating direction implicit (ADI) algorithm of Peaceman-Rachford [8], first proposed for the numerical solution of heat equation in two space dimensions, is to reduce the numerical solution of higher dimensional PDEs to a sequence of steps involving only one-dimensional finite difference operators, involving a simple tridiagonal matrix. The resulting algorithms are memory efficient and easy to parallelize. We illustrate this method in a Black-Scholes model with two risky assets.

## **Black–Scholes Equation for Multiasset** Options

Consider a filtered probability space  $(\Omega, \mathcal{F}, \mathcal{F}_t, \mathbb{I}P)$ and let  $(W_t)_{t\geq 0}$  be a standard bidimensional  $\mathcal{F}_t$ Brownian motion on it. We consider options written on two dividend-paying stocks whose price  $S_t^1$ ,  $S_t^2$ satisfies the stochastic differential equation:

$$\frac{\mathrm{d}S_t^i}{S_t^i} = (r - \delta_i) \,\mathrm{d}t + \sum_{j=1}^2 \sigma_{ij} \,\mathrm{d}W_t^j, \quad i = 1, 2 \quad (1)$$

where r is the interest rate,  $\delta_i$  is the dividend rate of the stock *i*, and the matrix  $\Sigma = (\sigma_{ij})_{1 \le i,j \le n}$  is assumed to be invertible, which ensures that the market is complete. In this setting, the value at time  $t$  of an European option with maturity  $T$  and payoff function  $\psi$  is given by  $U(t, S_t)$  where

$$U(t,x) = I\!E \left( e^{-r(T-t)} \psi \left( S_T^{t,x} \right) \right) \tag{2}$$

while the value at time  $t$  of an American option with maturity T and payoff function  $\psi$  is given by  $U_{am}(t, S_t)$  where

$$U_{am}(t,x) = \sup_{\tau \in \mathcal{T}_{0,T-t}} I\!E \left( e^{-r\tau} \psi \left( S^x_{\tau} \right) \right) \tag{3}$$

where  $\mathcal{T}_{0,T-t}$  is the set of all stopping times with values in  $[0, T - t]$ .

To see this, we shall use the following notation:

- $\mu$  is the vector with components  $(r \delta_i \frac{1}{2} \sum_{j=1}^{2} \sigma_{ij}^{2} \big)_{i=1,2}.$ <br>
  • for  $x = (x_1, x_2) \in \mathbb{R}^2$ ;  $\exp(x) = (e^{x_1}, e^{x_2})$

Hence, if we denote by  $S_t^{\exp(x)}$  the solution of equation (1) with  $S_0 = \exp(x)$ , we have

$$S_t^{\exp(x)} = \exp(x + \mu t + \Sigma W_t) \tag{4}$$

We make the following change in variables,  $\alpha =$  $\Sigma^{-1}\mu$ ,  $\rho = r + (||\alpha||^2/2)$ . The Girsanov theorem (Equivalence of Probability Measures) ensures that there exists a probability measure  $\mathbb{I}^{P^{(\alpha)}}$ <br>defined on  $(\Omega, \mathcal{F}_T)$  by  $\frac{\mathrm{d}P^{(\alpha)}}{\mathrm{d}P} = M_T^{(\alpha)}$ , where  $M_T^{(\alpha)} =$  $e^{-\alpha.W_T - \frac{|\alpha|^2}{2}T}$  such that  $(W_t^{(\alpha)} = W_t + \alpha t)_{0 \le t \le T}$  is a standard  $\mathbb{P}^{(\alpha)}$ -Brownian motion. Therefore, we have for  $x \in \mathbb{R}^2$ ,

$$U(t, \exp(x)) = I\!\!E \Big( e^{-r(T-t)} M_{T-t}^{(\alpha)}$$
$$\times e^{(\alpha.W_{T-t} + |\alpha|^2/2(T-t))} \psi \big( \exp\big(x + \Sigma W_{T-t}^{(\alpha)}\big) \big) \Big)$$
$$= I\!\!E^{(\alpha)} \big( e^{-\rho(T-t)} e^{\alpha.W_{T-t}^{(\alpha)}} \psi \big( \exp\big(x + \Sigma W_{T-t}^{(\alpha)}\big) \big) \big) \tag{5}$$

Define for  $y \in \mathbb{R}^2$ ,

$$V(t, y) = I\!E^{(\alpha)} \left( e^{-\rho(T-t)} \phi \left( y + W_{T-t}^{(\alpha)} \right) \right) \tag{6}$$

with  $\phi(y) = e^{\alpha y} \psi(\exp(\Sigma y))$ . We have  $U(t,$  $\exp(\Sigma y) = e^{-\alpha y} V(t, y)$ , the valuation of an European option is now reduced to the computation of  $V.$  By means of the same transformation, we have  $U_{am}(t, \exp(\Sigma y)) = e^{-\alpha y} V_{am}(t, y)$ , where

$$V_{am}(t, y) = \sup_{\tau \in \mathcal{T}_{0, T - t}} I\!E^{(\alpha)} \left( e^{-\rho \tau} \phi \left( y + W_{\tau}^{(\alpha)} \right) \right) \tag{7}$$

Introduce the parabolic operator  $\mathcal{L}$  defined by

$$\mathcal{L}v = \frac{\partial v}{\partial t} + \frac{1}{2}\Delta v - \rho v \tag{8}$$

where  $\Delta$  stands for the Laplacian. Then the function  $V$  is the solution of the following PDE:

$$\begin{cases}\n\mathcal{L}v = 0 \\
v(T,.) = \phi\n\end{cases} \tag{9}$$

while the function  $V_{am}$  satisfies the following obstacle problem on  $[0, T] \times \mathbb{R}^2$ 

$$\begin{cases} \max(\mathcal{L}v, \phi - v) = 0\\ v(T,.) = \phi \end{cases} \tag{10}$$

either in the sense of variational inequalities [7] or in the sense of viscosity solutions  $[9, \text{Prop } 1.2]$  (see Monotone Schemes).

### **ADI Methods**

The idea of Peaceman-Rachford ADI methods can be outlined as follows: consider a two-dimensional PDE arising from the valuation of a European option

$$\frac{\partial u}{\partial t} + \mathcal{A}u = 0 \tag{11}$$

where the operator  $\mathcal{A}$  can be decomposed into  $\mathcal{A} =$  $A_1 + A_2$  where each term acts on one variable. The ADI methods consist in splitting each time interval of length  $\Delta t$  in two subintervals and applying the implicit scheme for  $A_1$  and the explicit scheme for  $\mathcal{A}_2$  on the time interval  $[t_n, t_{n+1/2}]$  and the implicit scheme for  $A_2$  and the explicit scheme for  $A_1$  on the time interval  $[t_{n+1/2}, t_{n+1}]$ . If we denote by  $u_n$ the vector  $u(t_n, .)$ , the ADI methods compute  $u_n$ from  $u_{n+1}$  in two steps as follows: first we compute an intermediate value function  $u_{n+1/2}$  applying the implicit scheme for the differential operator  $\mathcal{A}_1$ 

$$u_{n+1} - u_{n+1/2} + \frac{\Delta t}{2} \left( \mathcal{A}_1 u_{n+1/2} + \mathcal{A}_2 u_{n+1} \right) = 0$$
(12)

next, we compute  $u_n$  from  $u_{n+1/2}$  applying an implicit scheme to  $\mathcal{A}_2$ 

$$u_{n+1/2} - u_n + \frac{\Delta t}{2} \left( \mathcal{A}_1 u_{n+1/2} + \mathcal{A}_2 u_n \right) = 0 \quad (13)$$

Each intermediate equation are afterwards discretized in space using finite difference approximation.

#### **ADI Methods for American Options**

We now treat the example of pricing of two-asset American options. The first step is to formulate  $(10)$ in a bounded domain, for example on  $Q_l = [0, T] \times$  $\Omega_l$  where  $\Omega_l = ] - l, l[^2]$ :

$$\begin{cases} \max(\mathcal{L}v_{am}, \phi - v_{am}) = 0\\ v_{am}(T, .) = \phi \end{cases} \tag{14}$$

with a Dirichlet boundary condition  $v_{am} = \phi$  on  $]0,T[\times \partial \Omega_l.$ 

For the numerical resolution of the obstacle problem  $(14)$  by finite difference methods, we shall introduce a grid of mesh points  $(nk, ih, jh)$  where h, k are mesh parameters that are thought of as tending to zero. Denote by  $N = \lceil T/k \rceil$  and M the greatest integer such that  $(M + \frac{1}{2}) h \leq l$ . For each point  $x_{ij} = (ih, jh)$ , consider a square

$$C_{ij}^{(h)} = \left] (i - 1/2)h, (i + 1/2)h \right[ \times \left] (j - 1/2)h, (j + 1/2)h \right[ \tag{15}$$

and define

$$\Omega_h = \left\{ x_{ij} \; ; \; C_{ij}^{(h)} \subset \Omega_l \right\}\n$$

$$\n= \left\{ x_{ij} \; ; \; -M \le i, \, j \le M \right\} \tag{16}$$

In the sequel,  $V_h$  is the space generated by  $\chi_{ij}^{(h)}$  where  $\chi_{ij}^{(h)}$  is the indicator function of the squares  $C_{ij}^{(h)}$ . If  $u_h \in V_h$ , we write  $u_h(x) = \sum_{i,j=-M}^M u_{ij} \chi_{ij}^{(h)}(x)$ . Note that  $u_{ii} = u(ih, jh)$ . Moreover, we denote by  $\phi_{h,k}$ the approximation of the payoff function  $\phi$  in the grid defined by

$$\phi_{h,k}(t,x) = \sum_{n=0}^{N} \phi_h(x) \mathbf{1}_{[nk,(n+1)k[}(t))$$
$$= \sum_{n=0}^{N} \left( \sum_{i,j=-M}^{M} \phi_{ij} \chi_{ij}^{(h)}(x) \right) \mathbf{1}_{[nk,(n+1)k[}(t))}$$
(17)

where  $\phi_{ij} = \phi(x_{ij})$  and  $\mathbf{1}_I$  is the indicator function of the interval  $I$ . We replace the Laplacian operator by a finite difference approximation and denote throughout

the paper A, B the linear operators defined on  $V_h$ by

$$(Au_h)(x) = \sum_{i,j=-M}^{M} (Au_h)_{ij} \chi_{ij}^{(h)}(x) \qquad (18)$$

$$(Bu_h)(x) = \sum_{i,j=-M}^{M} (Bu_h)_{ij} \chi_{ij}^{(h)}(x) \qquad (19)$$

where

$$(Au_h)_{ij} = 1/2(u_{i+1,j} - 2u_{ij} + u_{i-1,j}) \quad (20)$$

$$(Bu_h)_{ij} = 1/2(u_{i,j+1} - 2u_{ij} + u_{i,j-1}) \quad (21)$$

with the convention  $u_{ij} = 0$  if  $|i| \geq M + 1$  and  $|j| \geq$  $M + 1$ . Finally, we shall denote by  $(.,.)_l$  the inner product on  $\Omega_l$  and  $|.|_l = \sqrt{(\cdot,\cdot)_l}$ .

## **Dynamic Programming and ADI Method**

Barles *et al.* [1] discuss a splitting method, which can be viewed as an analytic version of the dynamic programming principle: one builds the approximate solution

$$u_{h,k} = \sum_{n=0}^{N} u_h^n(x) \mathbf{1}_{[nk,(n+1)k[}(t))$$
(22)

in a recursive way, starting from  $u_h^N = \phi$  and computing  $u_h^n$  for  $0 < n < N$  in two steps:

*First step*: One solves the following Cauchy problem on  $[nk, (n + 1)k] \times \Omega_l$  with Dirichlet boundary conditions.

$$\begin{cases}\n\mathcal{L}v = 0 \\
v(n+1, .) = u_h^{n+1}(.)\n\end{cases} \n$$
(23)

and denote the solution by  $S(k)[u_h^{n+1}]$ .

*Second step*: One computes

$$u(n,.) = \max\left(\phi_h(.), S(k)[u_h^{n+1}]\right) \tag{24}$$

The ADI method consists in splitting the initial system into two intermediate unidimensional linear systems:  $u^{n+1}$  given in  $V_h$  with  $u_{ij}^{n+1} = \phi_{ij}$  if  $|i| =$  $M + 1$  or  $|j| = M + 1$ .

One computes an intermediate value function  $v_h^{n+1/2} = (v_{ij}^{n+1/2})_{-M \leq i, j \leq M}$  by

• for  $|i| \leq M - 1$  and  $|j| \leq M - 1$ ,

$$\frac{u_{ij}^{n+1} - v_{ij}^{n+1/2}}{\frac{k}{2}} + \frac{v_{i+1,j}^{n+1/2} - 2v_{ij}^{n+1/2} + v_{i-1,j}^{n+1/2}}{2h^2} + \frac{u_{i,j+1}^{n+1} - 2u_{ij}^{n+1} + u_{i,j-1}^{n+1}}{2h^2} - \frac{\rho}{2} \left( u_{ij}^{n+1} + v_{ij}^{n+1/2} \right) = 0 \quad (25)$$

for  $i = M$  and  $|j| \leq M - 1$  (right boundary conditions).

$$\frac{u_{M,j}^{n+1} - v_{M,j}^{n+1/2}}{\frac{k}{2}} + \frac{\phi_{M+1,j} - 2v_{M,j}^{n+1/2} + v_{M-1,j}^{n+1/2}}{2h^2} + \frac{u_{M,j+1}^{n+1} - 2u_{M,j}^{n+1} + u_{M,j-1}^{n+1}}{2h^2} - \frac{\rho}{2} \left( u_{Mj}^{n+1} + v_{Mj}^{n+1/2} \right) = 0 \quad (26)$$

for  $i = -M$  and  $|j| \leq M - 1$  (left boundary con- $\bullet$ ditions),

$$\frac{u_{-M,j}^{n+1} - v_{-M,j}^{n+1/2}}{\frac{k}{2}} + \frac{\phi_{-M-1,j} - 2v_{M,j}^{n+1/2} + v_{-M+1,j}^{n+1/2}}{2h^2} + \frac{u_{-M,j+1}^{n+1} - 2u_{-M,j}^{n+1} + u_{-M,j-1}^{n+1}}{2h^2} - \frac{\rho}{2} \left( u_{-Mj}^{n+1} + v_{-Mj}^{n+1/2} \right) = 0 \quad (27)$$

and the symmetric equations for  $|j| = M$ . In a more compact form:

$$\frac{u^{n+1} - v^{n+1/2}}{\frac{k}{2}} + \frac{Av^{n+1/2} + a}{h^2} + \frac{Bu^{n+1} + b}{h^2} - \frac{\rho}{2} \left( u^{n+1} + v^{n+1/2} \right) = 0 \qquad (28)$$

with

$$a_{Mj} = \frac{1}{2}\phi_{M+1,j}, \quad a_{-Mj} = \frac{1}{2}\phi_{-M-1,j}$$
  
$$a_{ij} = 0 \quad \text{for } |i| \le M - 1 \tag{29}$$

$$b_{iM} = \frac{1}{2}\phi_{i,M+1}, \quad b_{i,-M} = \frac{1}{2}\phi_{i,-M-1}$$
$$b_{ij} = 0 \quad \text{for } |j| \le M-1 \tag{30}$$

In the same  $v_{h}^{n} =$ manner, one computes  $(v_{ij}^n)_{-M \leq i,j \leq M}$  by

$$\frac{v^{n+1/2} - v^n}{\frac{k}{2}} + \frac{Av^{n+1/2} + a}{h^2} + \frac{Bv^n + b}{h^2} - \frac{\rho}{2} \left( v^n + v^{n+1/2} \right) = 0 \tag{31}$$

Equations  $(28)$  and  $(31)$  give

$$\left[ \left( 1 + \frac{\rho k}{4} \right) I - \frac{k}{2h^2} A \right] v_h^{n+1/2}$$
  
= 
$$\left[ \left( 1 - \frac{\rho k}{4} \right) I + \frac{k}{2h^2} B \right] u^{n+1} + \frac{k}{2h^2} (a+b) \quad (32)$$

and

$$\left[ \left( 1 + \frac{\rho k}{4} \right) I - \frac{k}{2h^2} B \right] v_h^n\n$$

$$\n= \left[ \left( 1 - \frac{\rho k}{4} \right) I + \frac{k}{2h^2} A \right] v_h^{n+1/2} + \frac{k}{2h^2} (a+b) \quad (33)$$

If we set  $\eta_{h,k} = \frac{k}{2h^2}(a+b)$ ,

$$A_{h,k}^{+} = \left(1 + \frac{\rho k}{4}\right)I - \frac{k}{2h^{2}}A$$
$$A_{h,k}^{-} = \left(1 - \frac{\rho k}{4}\right)I + \frac{k}{2h^{2}}A \tag{34}$$

and

$$B_{h,k}^{+} = \left(1 + \frac{\rho k}{4}\right)I - \frac{k}{2h^{2}}B$$
$$B_{h,k}^{-} = \left(1 - \frac{\rho k}{4}\right)I + \frac{k}{2h^{2}}B \tag{35}$$

one obtains

$$\begin{cases}\nA_{h,k}^{+}v^{n+1/2} = B_{h,k}^{-}u^{n+1} + \eta_{h,k} \\
B_{h,k}^{+}v^{n} = A_{h,k}^{-}v^{n+1/2} + \eta_{h,k}\n\end{cases} \n\tag{36}$$

Finally, the computation of  $u_h^n$  may be summarized by:

$$u_h^n = \max\left(\phi_h, T_{h,k}[u_h^{n+1}]\right)$$

where the operator  $T_{h,k}$  is defined on  $V_h$  by:

$$T_{h,k}[u_h] = (A_{h,k}^+)^{-1} (B_{h,k}^+)^{-1} A_{h,k}^- B_{h,k}^- [u_h]$$
  
 
$$+ (A_{h,k}^+)^{-1} (B_{h,k}^+)^{-1} A_{h,k}^- \eta_{h,k}$$
(37)  
 
$$+ (B_{h,k}^+)^{-1} \eta_{h,k}$$

in which one implicitly used the fact that  $(A_{h,k}^+)^{-1}$ ,  $(B_{h,k}^+)^{-1}, A_{h,k}^- \text{ and } B_{h,k}^- \text{ commute.}$ 

Villeneuve and Zanette have proved the stability and the convergence of this scheme (see [9, Proposition 2.4 and Theorem 2.1]). Under a condition on the mesh parameters of the form

$$\lim_{h,k\downarrow 0} \frac{k}{h^2} = 0\tag{38}$$

From a numerical viewpoint, the systems (28) and (31) involve a tridiagonal matrix. Therefore, each intermediate system can be easily solved by Gaussian elimination, which takes part in the accuracy of the ADI method.

# **Linear Complementarity Problem** and ADI Method

In this section, we describe a second numerical method, which adapts the ADI algorithm to solve the linear complementarity problem (LCP) arising from the discretization of the parabolic variational inequalities related to the pricing of American options.

When the American option value is computed using standard finite differences approximation, one obtains finite dimensional LCP as follows:

$$AU \leq b$$
  

$$U \geq \psi$$
  

$$(U - \psi)^{\mathrm{T}} (AU - b) = 0$$
(39)

where U is the  $(M + 1)^2$  vector of American option values on the space grid and  $A$  is a block tridiagonal matrix.

There is an extensive literature on the resolution of LCPs and a complete survey can be found in [3]. In particular, the matrix  $A$  of the LCP arising from a variational inequality exhibits special properties like sparseness, which make it possible to use efficient algorithms including projected SOR [4] or direct pivoting methods [5].

Once again, the idea of the ADI method is to exploit the rapid  $LU$  decomposition algorithm for tridiagonal matrices by solving recursively a sequence of *one-dimensional* linear complementarity problems involving a tridiagonal matrix. Speed and flexibility of ADI methods come again from this decomposition:

$$u_{h,k}(t,x) = \sum_{n=0}^{N-1} \left( u_h^n(x) \mathbf{1}_{[nk,(n+1/2)k]}(t) + u_h^{n+1/2}(x) \mathbf{1}_{[(n+1/2)k,(n+1)k]}(t) \right) + u_h^N \mathbf{1}_{[Nk,(N+1/2)k]}(t) \tag{40}$$

where  $u_h^0, u_h^{1/2}, \ldots, u_h^N$  are the elements of the vector space  $V_h$  satisfying the variational inequalities:

complementarity problems (see the next proposition): pivoting methods (algorithms of Cryer [5], Brennan-Schwartz [2]) and iterative methods (e.g., PSOR [4]) (see Finite Difference Methods for Early Exercise **Options**). In the sequel, we specify the computational treatment of equation (41). The inner product in  $R^{d^2}$ is denoted by  $(u, v)$  and we write  $u > v$  if  $u_i > v_i$ for all  $i \in \{1, \ldots, d^2\}$ . The variational inequality (41) becomes a linear complementarity problem in finite dimensions:

Proposition 1 (Linear complementarity problem [3, 7]). Let A a  $d^2 \times d^2$  matrix and  $u, \theta, \phi \in R^{d^2}$ . The following systems are equivalent:

• 
$$(S)Au \ge \theta, \quad u \ge \phi$$
  
 $(Au - \theta, \phi - u) = 0$  (44)

$$\begin{cases}\n u_{h}^{N} = \phi_{h} \text{ and } \forall n \leq N - 1 \\
\forall v_{h} \geq \phi_{h} \quad \left( \frac{u_{h}^{n+1} - u_{h}^{n+1/2}}{\frac{k}{2}} + \frac{1}{h^{2}} A u_{h}^{n+1/2} + \frac{1}{h^{2}} B u_{h}^{n+1} - \frac{\rho}{2} \left( u_{h}^{n+1/2} + u_{h}^{n+1} \right), v_{h} - u_{h}^{n+1/2} \right)_{l} \leq 0 \\
\forall v_{h} \geq \phi_{h} \quad \left( \frac{u_{h}^{n+1/2} - u_{h}^{n}}{\frac{k}{2}} + \frac{1}{h^{2}} A u_{h}^{n+1/2} + \frac{1}{h^{2}} B u_{h}^{n} - \frac{\rho}{2} \left( u_{h}^{n+1/2} + u_{h}^{n} \right), v_{h} - u_{h}^{n} \right)_{l} \leq 0\n\end{cases} \tag{41}$$

with the Dirichlet conditions

 $\sim N$ 

$$\forall n \quad u_h^n(x_{ij}) = u_h^{n+1/2}(x_{ij}) = \phi_{ij}$$
  
for  $|i| = M$  and  $|j| = M$  (42)

 $\sim$   $\sim$ 

As usual, we had rather write the system in the following more compact form:

...

• 
$$(S')u \ge \phi, \quad \forall v \ge \phi$$
  
 $(Au - \theta, v - u) \ge 0$  (45)

For any matrix  $u = (u_{ij})_{1 \le i, j \le d}$ , we choose one of the most obvious methods of ordering

$$u = [u_{11}, \dots, u_{d1}, \dots, u_{1d}, \dots, u_{dd}] \tag{46}$$

$$\begin{cases} u_{h}^{n} = \phi_{h} \text{ and } \forall n \leq N - 1\\ \forall v_{h} \geq \phi_{h} \quad \left( \left( I + \frac{k}{2h^{2}} B - \frac{\rho}{2} \right) u^{n+1} - \left( I - \frac{k}{2h^{2}} A + \frac{\rho}{2} \right) u_{h}^{n+1/2}, v_{h} - u_{h}^{n+1/2} \right)_{l} \leq 0\\ \forall v_{h} \geq \phi_{h} \quad \left( \left( I + \frac{k}{2h^{2}} B - \frac{\rho}{2} \right) u^{n} - \left( I - \frac{k}{2h^{2}} A + \frac{\rho}{2} \right) u_{h}^{n+1/2}, v_{h} - u_{h}^{n} \right)_{l} \leq 0 \end{cases} \tag{43}$$

From a theoretical viewpoint, Villeneuve and Zanette  $[9, Theorem 3.2]$  have proved the convergence of this approximation procedure, using the weaker notion of quadratic convergence.

From a numerical viewpoint, there are mainly two families for solving variational inequalities in finite dimension by exploiting their link with linear

The ADI scheme (41) consists in approximating  $u(nk, ih, jh)_{0 \le n \le N; -M \le i, j \le M}$  by  $(u_{ij}^n)$  ordered in the way defined above by

$$u_{ij}^{N} = \phi(ih, jh) = \phi_{ij} \qquad \text{for } -M \le i, j \le M \tag{47}$$

and for  $0 \le n \le N-1$  and  $-M \le i, j \le M$ ,

$$\begin{cases} u_{ij}^{n+1/2} \geq \phi_{ij} \text{ and } u_{ij}^{n} \geq \phi_{ij} \\ u_{ij}^{n+1/2} = \phi_{ij} \text{ and } u_{ij}^{n} = \phi_{ij} \text{ for } |i| = M+1 \text{ or } |j| = M+1 \\ \frac{-1}{2} u_{i+1,j}^{n+1/2} + \alpha u_{ij}^{n+1/2} - \frac{1}{2} u_{i-1,j}^{n+1/2} \geq \frac{-1}{2} u_{i+1,j}^{n+1} + \alpha u_{ij}^{n+1} - \frac{1}{2} u_{i-1,j}^{n+1} \\ \left( \left( \frac{-1}{2} u_{i+1,j}^{n+1/2} + \alpha u_{ij}^{n+1/2} - \frac{1}{2} u_{i-1,j}^{n+1/2} \right) - \frac{1}{2} u_{i+1,j}^{n+1} - \alpha u_{ij}^{n+1} + \frac{1}{2} u_{i-1,j}^{n+1} u_{ij}^{n+1/2} - \phi_{ij} \right) = 0 \\ \frac{-1}{2} u_{i,j+1}^{n} + \alpha u_{ij}^{n} - \frac{1}{2} u_{i,j-1}^{n} \geq \frac{-1}{2} u_{i,j+1}^{n+1/2} + \alpha u_{ij}^{n+1/2} - \frac{1}{2} u_{i,j-1}^{n+1/2} \\ \left( \left( \frac{-1}{2} u_{i,j+1}^{n} + \alpha u_{ij}^{n} - \frac{1}{2} u_{i,j-1}^{n} \right) - \left( \frac{-1}{2} u_{i,j+1}^{n+1/2} + \alpha u_{ij}^{n+1/2} - \frac{1}{2} u_{i,j-1}^{n+1/2} \right), u_{ij}^{n} - \phi_{ij} \right) = 0 \end{cases} \tag{48}$$

where  $\alpha = \left(1 + \frac{\rho k}{4} - \frac{k}{2h^2}\right)$ . The Kronecker product of two matrices  $M, N \in \mathcal{M}_d(R)$  is the  $d^2 \times d^2$  matrix denoted by  $M \otimes N$  with entries  $(M \otimes N)_{ij} = M_{ij}N$  for  $1 \leq i, j \leq d$ . To take into account the boundary conditions, for  $u \in \mathcal{M}_{d^2}(R)$  with  $d = 2M + 1$ , we define  $\bar{u} \in \mathcal{M}_{d^2}(R)$  with components  $i = 1$ 

$$\begin{cases} \bar{u}_{11} = u_{11} - \frac{k}{h^2} (\phi(-(M+1)h, -Mh) + \phi(-Mh, -(M+1)h)) \\ \bar{u}_{1j} = u_{1j} - \frac{k}{h^2} (\phi(-(M+1)h, (-M+1) + j)h)) \quad 2 \le j \le d-1 \\ \bar{u}_{1d} = u_{1d} - \frac{k}{h^2} (\phi(-(M+1)h, Mh) + \phi(-Mh, (M+1)h)) \end{cases} \tag{49}$$

 $2 \le i \le d-1$ 

$$\bar{u}_{i1} = u_{i1} - \frac{k}{h^2} (\phi((-(M+1)+i)h, -(M+1)h))$$
  

$$\bar{u}_{ij} = u_{ij}\bar{u}_{id} = u_{id} - \frac{k}{h^2} (\phi((-(M+1)+i)h, (M+1)h))$$
  
(50)

 $i = d$ 

$$\bar{u}_{d1} = u_{d1} - \frac{k}{h^2} (\phi((M+1)h, -Mh) + \phi(Mh, -(M+1)h))$$
  

$$\bar{u}_{dj} = u_{dj} - \frac{k}{h^2} (\phi((M+1)h, -(M+1) + j)h)) \quad 2 \le j \le d-1$$
  

$$\bar{u}_{dd} = u_{dd} - \frac{k}{h^2} (\phi((M+1)h, Mh) + \phi(Mh, (M+1)h))$$
  
(51)

Then, the linear complementary problem can be written as

$$\begin{cases}\n u^{n+1/2} \geq \phi_{h} \text{ and } u^{n} \geq \phi_{h} \\
 \left[ I \otimes \left( I + \frac{\rho k}{2} I - \frac{k}{2h^{2}} T \right) \right] u^{n+1/2} \geq \left[ I \otimes \left( I - \frac{\rho k}{2} I + \frac{k}{2h^{2}} T \right) \right] \bar{u}^{n+1} \\
 \left( I \otimes \left( I + \frac{\rho k}{2} I - \frac{k}{2h^{2}} T \right) u^{n+1/2} - I \otimes \left( I - \frac{\rho k}{2} I + \frac{k}{2h^{2}} T \right) \bar{u}^{n+1}, u^{n+1/2} - \phi \right) = 0 \\
 \left[ \left( I + \frac{\rho k}{2} I - \frac{k}{2h^{2}} T \right) \otimes I \right] u^{n} \geq \left[ \left( I - \frac{\rho k}{2} I + \frac{k}{2h^{2}} T \right) \otimes I \right] \bar{u}^{n+1/2} \\
 \left( \left[ \left( I + \frac{\rho k}{2} I - \frac{k}{2h^{2}} T \right) \otimes I \right] u^{n} - \left[ \left( I - \frac{\rho k}{2} I + \frac{k}{2h^{2}} T \right) \otimes I \right] \bar{u}^{n+1/2}, u^{n} - \phi \right) = 0\n\end{cases} \tag{52}$$

with

$$T = \begin{pmatrix} -2 & 1 & \cdots & \cdots & 0 \\ 1 & -2 & 1 & \cdots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ \vdots & \vdots & 1 & -2 & 1 \\ 0 & \cdots & \cdots & 1 & -2 \end{pmatrix} \tag{53}$$

Hence, the pricing of the American option defined by  $\phi$  is now reduced to the computation of the bidimensional linear complementarity problem (52), which has been split in two intermediate unidimensional linear complementarity problems involving a tridiagonal matrix.

To summarize, ADI methods

- are competitive in terms of speed of computation . in comparison with standard iterative methods used in financial literature for solving linear complementarity problems;
- lead to algorithms that are very easy to implement . in the Black-Scholes setting; and
- are unconditionally stable for the  $L^2$  norm [6], which simplifies their implementation in practice.

#### References

[1] Barles, G., Daher, Ch. & Romano, M. (1995). Convergence of numerical Schemes for problems arising in Finance theory, Mathematical Models and Methods in Applied sciences  $5(1)$ ,  $125-143$ .

- [2] Brennan, M.J. & Schwartz, E. (1977). The valuation of the American put option, Journal of Finance 32, 449–462.
- [3] Cottle, R.W., Pang, J.S. & Stone, R.E. (1992). The Linear Complementarity Problem, Academic Press.
- [4] Cryer, C.W. (1971). The solution of a quadratic programming problem using systematic overrelaxation, SIAM Journal on Control and Optimization 9, 385–392.
- [5] Cryer, C.W. (1983). The efficient solution of linear complementarity problems for tridiagonal Minkowski matrices, ACM Transactions on Mathematical Software 9, 199-214.
- [6] Hout, K.J. & Welfert, B.D. (2007). Stability of ADI schemes applied to convestion-diffusion equations with mixed derivative terms, Applied Numerical Mathematics 57, 19-35.
- [7] Jaillet, P., Lamberton, D. & Lapeyre, B. (1990). Variational inequalities and the pricing of the American options, Acta Applicandae Mathematicae 21, 263-289.
- [8] Peaceman, P.W. & Rachford, H.H. (1955). The numerical solution of Parabolic and Elliptic differential equation, Journal of the Society for Industrial and Applied Mathematics 3, 28-42.
- [9] Villeneuve, S. & Zanette, A. (2002). Parabolic A.D.I. methods for pricing American options on two stocks, Mathematics of Operation Research 27(1), 121-149.

STÉPHANE VILLENEUVE
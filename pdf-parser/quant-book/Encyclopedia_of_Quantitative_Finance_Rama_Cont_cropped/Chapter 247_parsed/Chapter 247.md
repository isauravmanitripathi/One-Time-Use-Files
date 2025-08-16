# Crank-Nicolson Scheme

In a paper published in 1947 [2], John Crank and Phyllis Nicolson presented a numerical method for the approximation of diffusion equations. Starting from the simplest example

$$\frac{\partial V}{\partial t} = \frac{\partial^2 V}{\partial x^2} \tag{1}$$

a spatial approximation on a uniform grid with spacing  $h$  leads to the semidiscrete equations

$$\frac{\mathrm{d}V_j}{\mathrm{d}t} = h^{-2} \,\delta_j^2 V_j \tag{2}$$

where  $V_i(t)$  is an approximation to  $V(x_i, t)$  and  $\delta_i^2 V_i \equiv V_{i+1} - 2V_i + V_{i-1}$  is a central second difference. Crank-Nicolson time-marching discretizes this in time with a uniform timestep  $k$  using the approximation

$$k^{-1} \left( V_j^{n+1} - V_j^n \right) = \frac{1}{2} h^{-2} \left( \delta_j^2 V_j^{n+1} + \delta_j^2 V_j^n \right) \quad (3)$$

which can be rearranged to give

$$\left(1 - \frac{1}{2}kh^{-2}\delta_j^2\right)V_j^{n+1} = \left(1 + \frac{1}{2}kh^{-2}\delta_j^2\right)V_j^n \qquad (4)$$

This can be viewed as the  $\theta = \frac{1}{2}$  case of the more general  $\theta$  scheme

$$\left(1 - \theta \, kh^{-2} \delta_j^2\right) V_j^{n+1} = \left(1 + (1 - \theta) \, kh^{-2} \delta_j^2\right) V_j^n \tag{5}$$

 $\theta = 0$  corresponds to explicit Euler time-marching, while  $\theta = 1$  corresponds to fully implicit Euler timemarching. For  $\theta > 0$ , the  $\theta$ -scheme defines a tridiagonal system of simultaneous equations, which can be solved very efficiently using the Thomas algorithm to obtain the values for  $V_i^{n+1}$ . The scheme is unconditionally stable in the  $\vec{L}_2$  norm, meaning that the  $L_2$  norm of the solution does not increase for any value of k, provided  $\theta \ge 1/2$ . The Crank–Nicolson scheme is thus on the boundary of unconditional stability. It is also special in having a numerical error for smooth initial data, which is  $O(h^2, k^2)$ , whereas the error is  $O(h^2, k)$  for other values of  $\theta$ . The unconditional  $L_2$  stability means that one can choose to make  $k$  proportional to  $h$ , and, together with the secondorder accuracy, this makes the scheme both accurate

and efficient, and hence a very popular choice for approximating parabolic PDEs (see **Partial Differ**ential Equations).

## **Application to Black–Scholes Equation**

The Crank-Nicolson method is used extensively in mathematical finance for approximating parabolic PDEs such as the Black-Scholes equation, which can be written in reversed-time form (with  $\tau \equiv T - t$ being the time to maturity  $T$ ) as

$$\frac{\partial V}{\partial \tau} = -rV + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \tag{6}$$

Switching to the new coordinate  $x \equiv \log S$  gives the transformed equation

$$\frac{\partial V}{\partial \tau} = -rV + \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2} \tag{7}$$

and its Crank-Nicolson discretization on a grid with uniform timestep  $k$  and uniform grid spacing  $h$  is

$$\left(I + \frac{1}{2}D\right) V_j^{n+1} = \left(I - \frac{1}{2}D\right) V_j^n \tag{8}$$

where the discrete operator  $D$  is defined by

$$D = r k - \frac{1}{2}kh^{-1} \left(r - \frac{1}{2}\sigma^2\right) \delta_{2j} - \frac{1}{2}kh^{-2} \sigma^2 \delta_j^2$$
(9)

with the central first difference operator  $\delta_{2j}$  defined by  $\delta_{2j} V_j \equiv V_{j+1} - V_{j-1}$ .

For an European call option with strike  $K$ , the initial data at maturity is  $V(S, 0) = \max(S - K, 0)$ . Figure 1a shows the numerical solution  $V(S, 2)$ for parameter values  $r = 0.05$ ,  $\sigma = 0.2$ ,  $K = 1$ , and timestep/spacing ratio  $\lambda \equiv k/h = 10$ . The agreement between the numerical solution and the known analytic solution appears quite good, but b and c show much poorer agreement for the approximations to  $\Delta \equiv \partial V/\partial S$  and  $\Gamma \equiv \partial^2 V/\partial S^2$  (see **Delta Hedging**; Gamma Hedging) obtained by central differencing of the numerical solution  $V_i^n$ . In particular, note that the maximum error in the computed value for  $\Gamma$ occurs at  $S=1$ , which is the location of the discontinuity in the first derivative of the initial data. Figure  $2a-c$  show the behavior of the maximum error as the computational grid is refined, keeping fixed the ratio  $\lambda \equiv k/h$ . It can be seen that for

![](_page_1_Figure_1.jpeg)

**Figure 1** *V* , and for a European call option, with *λ* ≡ *k/h* = 10

largest value of *λ* the numerical solution *Vj* exhibits first-order convergence, while the discrete approximation to does not converge, and the approximation to diverges. For smaller values of *λ*, it appears that the convergence is better, but, in fact, the asymptotic behavior is exactly the same except that it becomes evident only on much finer grids.

At first sight, this is a little surprising as textbooks almost always describe the Crank–Nicolson method as unconditionally stable and second-order accurate. The key is that it is only unconditionally stable in the *L*<sup>2</sup> norm, and this only ensures convergence in the *L*<sup>2</sup> norm for initial data, which has a finite *L*<sup>2</sup> norm [9]. Furthermore, the order of convergence may be less than second order for initial data, which is not

![](_page_2_Figure_1.jpeg)

**Figure 2** Grid convergence for a European call option, with fixed  $\lambda \equiv k/h$ 

smooth; for example, the  $L_2$  order of convergence for discontinuous initial data is 1/2. With the European call Black–Scholes application, the initial data for  $V$ lies in  $L_2$ , as does its first derivative, but the second derivative is the Dirac delta function, which does not lie in  $L_2$ . This is the root cause of the observed failure

to converge as the grid is refined. Furthermore, it is the maximum error, the  $L_{\infty}$  error, which is most relevant in financial applications.

One solution to this problem is to use an alternative second-order backward difference method, but these methods require special start-up procedures because they require more than one previous time level, and they are usually less accurate than the Crank-Nicolson method for the same number of timesteps. Better alternatives are higher order backward difference methods [5] or the Rannacher start-up procedure described in the next section.

#### **Rannacher Start-up Procedure**

Rannacher analyzed this problem of poor  $L_2$  convergence of convection-diffusion approximations with discontinuous initial data [8], and recovered secondorder convergence by replacing the Crank-Nicolson approximation for the very first timestep by two halftimesteps of implicit Euler time integration, and by using a finite element projection of the discontinuous initial data onto the computational grid. This technique, often referred to as *Rannacher timestep* $ping$ , has been used with success in approximations of the Black-Scholes equations [6, 7], with the halftimestep implicit Euler discretization given by

$$\left(I + \frac{1}{2}D\right) V_j^{n+1/2} = V_j^n \tag{10}$$

The problem has been further investigated by Giles and Carter [4] who analyzed the maximum errors in finance applications and proved that it is necessary to go further and replace the first two Crank-Nicolson timesteps by four half-timesteps of implicit Euler to achieve second-order accuracy in the  $L_{\infty}$  norm for V,  $\Delta$  and  $\Gamma$  for put, call, and digital options. The improved accuracy is demonstrated by  $(d-f)$  in Figures 1 and 2.

#### **Nonlinear and Multifactor Extensions**

The use of a nonlinear penalty function in approximating American options (see Finite Difference Methods for Early Exercise Options) leads to a nonlinear discretization of the form [3]

$$\left(I + \frac{1}{2}D\right) V_j^{n+1} = \left(I - \frac{1}{2}D\right) V_j^n + P\left(V_j^{n+1}\right) \tag{11}$$

where the nonlinear penalty term  $P(V_j^{n+1})$  is negligible in the region where the option is not exercised, and elsewhere ensures that  $V_i^{n+1}$  is approximately equal to the exercise value.

This nonlinear system of equations can be solved using a Newton iteration, starting with  $V_j^{n+1,0} = V_j^n$ 

and defining the  $m+1^{th}$  iterate to be  $V_i^{n+1,m+1} =$  $V_i^{n+1,m} + \Delta V_i$  with the correction  $\Delta V_j$  given by the linear equations

$$\begin{aligned} \left(I + \frac{1}{2}D - \frac{\partial P}{\partial V}\right) \Delta V_j \\ &= -\left(I + \frac{1}{2}D\right) V_j^{n+1,m} \\ &+ \left(I - \frac{1}{2}D\right) V_j^n + P\left(V_j^{n+1,m}\right) \end{aligned} \tag{12}$$

Alternatively, one can use just one step of the Newton iteration, in which case one has  $V_i^{n+1} = V_i^n + \Delta V_j$ with the change  $\Delta V_i$  given by

$$\left(I + \frac{1}{2}D - \frac{\partial P}{\partial V}\right)\Delta V_j = -D V_j^n + P(V_j^n) \quad (13)$$

In one dimension, the linear equations are a tridiagonal system that can be solved very efficiently. In higher dimensions, the direct solution cost is much greater and alternative approaches are usually adopted. One is to use an Alternating Direction Implicit (ADI) Method approximate factorization into a product of operators, each of which involves differences in only one direction [9]. To maintain second-order accuracy, it is necessary to use the Craig-Sneyd treatment for any cross-derivative term  $[1]$ . Another approach is to use a preconditioned iterative solver such as BiCGStab with ILU preconditioning (see Conjugate Gradient Methods).

# References

- [1] Craig, I.J.D. & Sneyd, A.D. (1988). An alternatingdirection implicit scheme for parabolic equations with mixed derivatives, Computers and Mathematics with Applications 16(4), 341-350.
- [2] Crank, J. & Nicolson, P. (1947). A practical method for numerical integration of solutions of partial differential equations of heat-conduction type. Proceedings Cambridge Philosophical Society 43, 50.
- [3] Forsyth, P.A. & Vetzal, K.R. (2002). Quadratic convergence for valuing American options using a penalty method, SIAM Journal on Scientific Computing 23(6), 2095-2122.
- [4] Giles, M.B. & Carter, R. (2006). Convergence analysis of Crank-Nicolson and Rannacher time-marching, Journal of Computational Finance  $9(4)$ ,  $89-112$ .
- [5] Khaliq, A.Q.M., Voss, D.A., Yousuf, R. & Wendland, W. (2007). Pricing exotic options with L-stable Padé schemes, Journal of Banking and Finance 31(11), 3438-3461.

- [6] Pooley, D.M., Forsyth, P.A. & Vetzal, K.R. (2003). Numerical convergence properties of option pricing PDEs with uncertain volatility, *IMA Journal of Numerical Analysis* **23**, 241–267.
- [7] Pooley, D.M., Vetzal, K.R. & Forsyth, P.A. (2003). Convergence remedies for non-smooth payoffs in option pricing, *Journal of Computational Finance* **6**(4), 25–40.
- [8] Rannacher, R. (1984). Finite element solution of diffusion problems with irregular data, *Numerische Mathematik* **43**, 309–327.
- [9] Richtmyer, R.D. & Morton, K.W. (1967). *Difference Methods for Initial-value Problems*, 2nd Edition, John

Wiley & Sons. Reprint Edition (1994), Krieger Publishing Company, Malabar.

## **Related Articles**

**Alternating Direction Implicit (ADI) Method**; **Conjugate Gradient Methods**; **Finite Difference Methods for Barrier Options**; **Finite Difference Methods for Early Exercise Options**; **Finite Element Methods**; **Partial Differential Equations**.

MICHAEL B. GILES
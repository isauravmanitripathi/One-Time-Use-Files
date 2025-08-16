# **Finite Difference Methods** for Barrier Options

Barrier options, options that cease to exist (knockout barrier options) or that only come into existence (knock-in barrier options) when some observable market parameter crosses a designated level (the barrier), have become ubiquitous in financial contracts for virtually all asset classes, including equities, foreign exchange, fixed income, and commodities.

Pricing of continuously monitored barrier options using partial differential equations (PDEs) enables the use of coordinate transformations to obtain smooth, rapid convergence, highly desirable properties that are difficult to obtain using traditional lattice methods. The finite difference method is perhaps the most straight forward and intuitive approach to the numerical solution of PDEs. Yet even in this seemingly simple approach, there exist subtleties that can be exploited for tremendous gains in accuracy and/or computational efficiency [7]. We explore several ways in which finite difference pricing models for barrier options may be designed for increased accuracy and performance.

Pricing models in which the monitoring of the barrier knockout or knock-in condition is approximated as being continuous have been popular principally because they may yield analytic solutions, at least for simple underlying processes (e.g., Black-Scholes.) Even for underlying process for which numerical PDE solution methods are required (e.g., stochastic volatility models with correlation of the underlying level and its instantaneous variance), the continuously monitored barrier condition is often easier to treat with simple numerical methods.

However, in the vast majority of barrier option contracts, the barrier conditions are monitored at discrete times or dates. For the volatilities observed in most markets, even barrier monitoring as frequently as daily yields barrier option prices surprisingly far from those yielded by a continuous monitoring approximation. Broadie et al. [2] derive a formula for shifting a discrete barrier so that pricing with continuously monitored barrier yields the discretely monitored barrier price to lowest order in the monitoring interval for a lognormal process. In many cases of interest, however, direct numerical solution of the discretely monitored barrier pricing problem is required. Therefore, in this article, the continuously monitored barrier case is discussed fairly briefly, while the majority of space is devoted to the discretely monitored barrier case.

For simplicity of notation, we focus on a simple Black-Scholes [1] pricing PDE but none of the methods discussed require that PDE coefficients be constant, so the methods are directly applicable to local volatility models. When methods of conforming finite difference grids to barrier and/or strike positions are discussed, they apply only to the coordinate representing the financial factor subject to a barrier. Other coordinate grids, for example, the instantaneous volatility in a stochastic volatility model [5], or a second or third asset in a basket model are unaffected. Therefore, the methods presented are applicable to these problems as well.

The case of jump-diffusion models requires further analysis and is discussed in [3] (see Partial Integrodifferential Equations (PIDEs)).

### **Continuous Monitoring**

The simplest pricing partial differential equations (PDEs) typically encountered is the Black-Scholes equation [1], written in the form

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - q)S \frac{\partial V}{\partial S} - rV = 0 \quad (1)$$

where  $V$  is the option value,  $S$  is the underlying asset price,  $r$  and  $q$  are the forward rate and continuous dividend yield, respectively, and  $\sigma$  is the volatility.

A simple up-out call option is used for illustration. In this case, the payoff condition at option expiration  $t = T$  is

$$V(S, T) = \max(S - K, 0) : S < B \tag{2}$$

$$V(S,T) = R: \quad S \ge B \tag{3}$$

where  $B$  is the up-out barrier,  $K$  is the option strike, and  $R$  is a rebate paid immediately upon knockout. The upper grid boundary can be placed at  $S = B$ with boundary condition  $V(B, t) = R$ , while that for the lower boundary  $S_{\text{Min}}$  is not well defined unless  $S_{\text{Min}} = 0$ . Terminating the grid at  $S_{\text{Min}} = 0$  may be a quite inefficient use of finite difference grid points, since the option value may be very small over most of the grid. Rather, one may choose a simple rule of thumb such as

$$S_{\text{Min}} = S_0 e^{-N\sigma\sqrt{T}} \tag{4}$$

which places the lower boundary  $N$  standard deviations below the initial asset price  $S_0$ , so that for  $N \ge 4$ there is only a minuscule chance of the asset price reaching the strike price before expiration to yield a positive payoff. Then  $V(S_{\text{Min}}, t) = 0$  becomes an accurate boundary condition.

The commonly used coordinate transformation  $x = \log(S)$  is avoided here for three reasons: (i) since the volatility may have a dependence on  $S$  (local volatility), it does not necessarily yield a PDE with constant coefficients. (ii) In a fully numerical PDE solution, constant coefficients are of marginal benefit. (iii) It is far more useful to employ other, more general coordinate transformations.

In particular, the transformation used here is a slight warping of an otherwise uniform grid. The grid is warped so that the strike  $K$  is "pinned" midway between two grid points independent of  $S_{\text{Min}}$ or the number of grid points, while keeping the grid spacing as uniform as possible. The benefit of doing so is that smooth monotonic convergence—superior to that typical of lattice methods—is obtained as demonstrated by Tavella and Randall [7]. In the transformed coordinates, the PDE becomes

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{S^2(x)}{J(x)} \frac{\partial}{\partial x} \left(\frac{1}{J(x)} \frac{\partial V}{\partial x}\right) + (r-q) \frac{S(x)}{J(x)} \frac{\partial V}{\partial x} - rV = 0 \tag{5}$$

where  $J(x) = \partial S(x)/\partial x$  is the Jacobian of the transformation. The new coordinate  $x$  is by convention equally spaced on a grid,  $x_0 \le x_i \le x_I$ , where  $0 \le i \le I$  and subject to the boundary conditions,  $S(x_0) = S_{\text{Min}}, S(x_1) = B$ , and the "pinning condition"  $K = (S_p + S_{p+1})/2$ , where p is the index of the grid point just below  $K$ .

A method for numerically computing a smoothly varying coordinate transformation  $S(x)$  so as to place particular "pinning" points (e.g.,  $K$ ) either exactly on grid points or exactly midway between grid points through the use of spline interpolation, is also discussed in detail in [7].

Table 1 shows the convergence of the numerical results versus the number of grid points  $I$  for an

**Table 1** Finite difference results for a continuously monitored up-out barrier call. Parameters:  $T = 1, K = 100, B =$ 110,  $R = 0.5$ ,  $r = 0.05$ ,  $q = 0.03$ ,  $\sigma = 0.1$ , and  $\Delta_0 = 100$ 

|      | $V(S_0)$  | Error        | Ratio |
|------|-----------|--------------|-------|
| 50   | 0.8493291 | $-0.0006945$ |       |
| 100  | 0.8498746 | $-0.0001491$ | 4.65  |
| 200  | 0.8499891 | $-0.0000345$ | 4.32  |
| 400  | 0.8500147 | $-0.0000086$ | 3.85  |
| 800  | 0.8500214 | $-0.0000022$ | 4.07  |
| 1600 | 0.8500231 | $-0.0000005$ | 3.96  |
| 3200 | 0.8500235 | $-0.0000001$ | 3.95  |

at-the-money up-out call option. The option and market parameters are given in the caption. The column labeled  $V(S_0)$  is the present value, that labeled *Error* is the finite difference result minus the converged result, and that column labeled *Ratio* is the ratio of *Errors* for grid  $I$  and grid  $I/2$ . The numerical solution converges smoothly and monotonically because the option strike (where the payoff has a discontinuity of slope) always has a fixed relationship to the grid, namely it is always midway between two grid points. The convergence is almost exactly quadratic, that is, *Ratio* is very close to 4 when  $I$  is doubled. In order to make time discretization error negligible so that the spatial grid discretization effects of interest could be examined in isolation,  $50\,000$  time steps have been used with a Rannacher [4] time discretization scheme. Time discretization effects with practical numbers of time steps are discussed later.

(One of the benefits of full or partially implicit PDE methods like Crank-Nicolson or Rannacher is that the number of spatial grid points and time steps are independent, whereas in lattice methods they are closely coupled.)

### **Discrete Monitoring**

In modeling continuously monitored barrier options, as in the previous section, it is sufficient to place the barrier(s) on the grid boundaries and enforce a boundary condition  $V(B, t) = R$ . It is of no consequence that gradient of option value  $V(S)$  (the option  $\Delta$ ) is discontinuous at the barriers because the pricing PDE (which includes second derivative terms that become singular) is not solved at the barriers. Boundary conditions are enforced instead.

When modeling discretely sampled barriers, however, the barriers appear inside the solution region, allowing the option value  $V(S)$  to "diffuse" across the barriers between monitoring times. The knockout conditions are enforced only at the monitoring times. Consequently, the pricing PDE is solved at the barrier position, and the grid must resolve the very strong gradients that are periodically created there by the discrete monitoring. To do this efficiently, it is convenient to use a coordinate transformation that results in a concentration of grid points near a specified set of points, for example, the strike  $K$  and barrier  $B$ .

A transformation useful for this purpose can be obtained as the solution of the ordinary differential  $\text{equation (ODE)}$ 

$$\frac{\mathrm{d}S}{\mathrm{d}x} = \frac{A}{\left[\sum_{i} \frac{\alpha^{2} + (S - P_{i})^{2}}{\alpha^{2} \beta^{2} + (S - P_{i})^{2}}\right]^{1/2}}$$
(6)

where  $A$  is a constant to be determined through the boundary conditions  $S(x_{\text{Min}}) = S_{\text{Min}}$  and  $S(x_{\text{Max}}) =$  $S_{\text{Max}}$ , and the summation is over the set of specified points  $P_i$ ,  $0 \le i \le n_p$ . The properties of the transformation are easiest to see in the special case of a single specified point, where the ODE simplifies to

$$\frac{\text{d}S}{\text{d}x} = A \left[ \frac{\alpha^2 \beta^2 + (S - P)^2}{\alpha^2 + (S - P)^2} \right]^{1/2} \tag{7}$$

Thus, far from the specified point,  $|S - P| > \alpha$ ,  $dS/dx = A$  is a constant. If x is uniformly spaced, then far from the specified point  $P$ ,  $S$  is uniformly spaced as well. In the neighborhood of the specified point  $S = P$ ,  $dS/dx = \beta A$  is minimized  $(\beta < 1)$ , and the *S* grid is finer by the ratio  $\beta$ .

To compute that transformation in equation  $(6)$ , a uniform grid is first created in the underlying coordinate  $x$  and an initial guess for the constant  $A$ is made. After enforcing the left boundary condition  $S(x_{\text{Min}}) = S_{\text{Min}}$ , a simple ODE solver such as Runge-Kutta can be used to step through the  $x$  grid, computing  $S(x)$ . If, at the right end of the grid, the boundary condition  $S(x_{\text{Max}}) = S_{\text{Max}}$  is not satisfied to a given precision, then the constant  $A$  is adjusted via a Newton's method and the ODE solution repeated until the right boundary condition is satisfied. Convergence is typically rapid. Finally, a secondary transformation is applied, slightly warping the computed  $S$  grid so as to place the set of specified points either exactly at grid points or at grid midpoints as described in [7].

Table 2 Finite difference results for a discretely monitored up-out barrier call. Parameters:  $T = 1, K = 100, B =$ 110,  $R = 0.5$ ,  $r = 0.05$ ,  $q = 0.03$ ,  $\sigma = 0.1$ ,  $S_0 = 100$ , 250 monitoring dates, 50 000 time steps,  $\alpha = 20$ ,  $\beta = 0.1$ 

|      | $V(S_0)$  | Error     | Ratio |
|------|-----------|-----------|-------|
| 50   | 0.9244337 | 0.0052293 |       |
| 100  | 0.9203730 | 0.0011686 | 4.47  |
| 200  | 0.9194832 | 0.0002788 | 4.19  |
| 400  | 0.9192736 | 0.0000692 | 4.02  |
| 800  | 0.9192216 | 0.0000172 | 4.03  |
| 1600 | 0.9192087 | 0.0000043 | 4.04  |
| 3200 | 0.9192055 | 0.0000011 | 4.01  |

Table 2 shows the convergence of option value with the number of grid points  $I$  for an at-the-money up-out call option, discretely monitored 250 times per year. The option and market parameters are given in the caption. The column labeled  $V(S_0)$  is the present value, that labeled *Error* is the finite difference result minus the analytic result, and that column labeled *Ratio* is the ratio of *Errors* for grid I and grid  $I/2$ . Even in this case of frequent discrete monitoring of the barrier, in which discontinuities of option value  $V$ are created periodically throughout the integration of the PDE, the numerical solution converges smoothly and monotonically. This is possible because the option strike and the barrier both always have a fixed relationship to the grid, namely, they are always midway between two grid points. The convergence is again almost exactly quadratic, that is, Ratio is very close to 4 when the number of grid points is doubled. Again, a very large number of time steps  $(50\,000)$  have been used in order to isolate spatial grid discretization effects.

Smooth convergence according to a known scaling law also allows fairly robust extrapolation to the continuum result from several computationally inexpensive sparse grid computations.

$$V(I \to \infty) \approx \frac{4V(2I) - V(I)}{3} \tag{8}$$

For example, using  $I = 100$  in equation (8), the estimated continuum result is 0.919187, which is very close to the presumed converged result 0.919204. Thus, one extrapolates to very near the converged value from two very cheap and fast sparse grid computations. Robust extrapolation from lattice computations of barrier option value is typically not possible.

The converged values of the continuously monitored and daily monitored options differ by over 8%

![](_page_3_Figure_1.jpeg)

**Figure 1** Option value (a), option (b), and grid spacing (c) for a discretely monitored up-out barrier call. Parameters: *T* = 1*, K* = 100*, B* = 110*, R* = 0*.*5*, r* = 0*.*05*, q* = 0*.*03*, σ* = 0*.*1*, S*<sup>0</sup> = 100, 250 monitoring dates, 50 000 time steps, *α* = 20*, β* = 0*.*1*, I* = 100 grid points

even for this relatively low volatility case. The continuity correction formula in [2] yields an option value of 0.9217721, which is much closer to the converged value of the daily monitored option, but still too large by approximately 0.3%. Since the formula is basically an expansion in *σ* <sup>√</sup>*tB*, where *tB* is the monitoring interval, the accuracy of the correction will degrade for larger volatilities and/or less frequent monitoring. The accuracy of the formula also depends on the proximity of *S*<sup>0</sup> and *B*.

The grids used in the computations of Table 2 were concentrated about the option strike and barrier, with coordinate transformation parameters *α* = 20, *β* = 0*.*1. Figure 1 displays the present *(t* = 0*)* option value *V (S)*, option delta = *∂V (S)/∂S*, and the grid spacing *S(S)* = *J (S)x* when *I* = 100. With the next barrier monitoring date one day hence, the option has significantly larger value at the barrier *S* = *B* = 110 than the discounted rebate value of approximately *R* = 0*.*5. The option changes rapidly in the neighborhood of the barrier, but remains continuous. The grid spacing *S* is minimized near the two designated points *K* = 100 and *B* = 110 yielding a ratio of largest to smallest spacing on the grid of about a factor of 7. Even with just *I* = 100 grid points, the small grid spacing near the barrier resolves the rapid change of through the region. Similarly, the small spacing near the strike helps resolve the rapid variation of in the region close to option expiration.

Table 3 compares the accuracy of the solution for an up-out call option for three finite difference grids. Grid A is equally spaced *(β* = 1*)* with the barrier exactly on a grid point. (The strike remains at a grid midpoint.) Grid B is also equally spaced, but with the barrier at a midpoint. Finally, Grid C is the nonuniform grid of Table 2, whose data is simply reproduced for comparison.

In the case of Grid A, the fixed relationship of the strike and barrier to the grid yields smooth monotonic

**Table 3** Finite difference results for a discretely monitored up-out barrier call using three finite difference grids. Parameters: *T* = 1*, K* = 100*, B* = 110*, R* = 0*.*5*, r* = 0*.*05*, q* = 0*.*03*, σ* = 0*.*1*, S*<sup>0</sup> = 100, 250 monitoring dates, 50 000 time steps. The three grids are described in the text

| Grid I | V (S0)    | Error      | Ratio |
|--------|-----------|------------|-------|
| Grid A |           |            |       |
| 50     | 0.8638922 | −0.0553122 | —     |
| 100    | 0.878615  | −0.0405894 | 1.36  |
| 200    | 0.8958347 | −0.0233697 | 1.73  |
| 400    | 0.9066875 | −0.0125169 | 1.87  |
| 800    | 0.9127664 | −0.0064380 | 1.94  |
| 1600   | 0.9159481 | −0.0032563 | 1.98  |
| 3200   | 0.9175651 | −0.0016393 | 1.99  |
| Grid B |           |            |       |
| 50     | 0.969642  | 0.0504376  | —     |
| 100    | 0.9321862 | 0.0129818  | 3.88  |
| 200    | 0.9220514 | 0.0028470  | 4.55  |
| 400    | 0.9199134 | 0.0007090  | 4.01  |
| 800    | 0.9193805 | 0.0001761  | 4.02  |
| 1600   | 0.9192481 | 0.0000438  | 4.02  |
| 3200   | 0.9192153 | 0.0000109  | 4.00  |
| Grid C |           |            |       |
| 50     | 0.9244337 | 0.0052293  | —     |
| 100    | 0.9203730 | 0.0011686  | 4.47  |
| 200    | 0.9194832 | 0.0002788  | 4.19  |
| 400    | 0.9192736 | 0.0000692  | 4.02  |
| 800    | 0.9192216 | 0.0000172  | 4.03  |
| 1600   | 0.9192087 | 0.0000043  | 4.04  |
| 3200   | 0.9192055 | 0.0000011  | 4.01  |

convergence, but it is only linear (*Ratio* is close to 2 when *I* is doubled) and the observed error is 1–3 orders of magnitude larger than that of Grid C.

In the case of Grid B, the barrier is at a grid midpoint and quadratic convergence (*Ratio* ∼ 4) is restored, but because the grid is still uniform, the spacing near the barrier is roughly three times larger than it is for Grid C. As a result, the observed error, while far superior to that of Grid A, is about an order of magnitude larger than that of the nonuniform Grid C. Clearly, use of a nonuniform grid, while taking care to place a discretely sampled barrier at a grid midpoint yields superior convergence. The computational effort involved in computing such a grid is generally negligible compared to the PDE solution itself and obviously worth the effort.

Continuously monitored barriers are optimally priced when the barrier(s) coincide with grid points, while the foregoing numerical results seem to establish that a discretely sampled barrier option is optimally priced when the barrier is midway between two grid points. Of course, as the monitoring frequency is increased, a discretely monitored barrier becomes a continuously monitored one. Therefore, a dimensionless parameter is needed, one that, given a monitoring frequency, determines the optimal grid style to be used. An obvious choice is the ratio of characteristic grid diffusion time near the barrier to the monitoring interval:

$$R_{\Delta t} = \frac{\Delta t_{\text{Grid}}}{\Delta t_B}$$
$$\Delta t_{\text{Grid}} = \frac{(\Delta S/B)^2}{\sigma^2/2}$$
$$\Delta t_B = \frac{T}{n_B} \tag{9}$$

where *T* is option expiration and *nB* is the number of monitoring dates. One expects that for *Rt >* 1, the discretely monitored barrier is effectively continuously monitored to the resolution of the grid, and the barrier should be placed at a grid point. Conversely, when *Rt <* 1 then the barrier should be midway between grid points for optimal accuracy.

This criterion, which is easy to verify numerically, can be used to choose where to place a discretely sampled barrier for optimal accuracy. However, it is easy to see that for almost any discretely sampled barrier option with typical parameters, the barrier(s)

![](_page_5_Figure_1.jpeg)

**Figure 2** Option  $\Delta$  in the neighborhood of the barrier for two time discretizations for a discretely monitored up-out barrier call: Rannacher (a), and Crank-Nicolson (b). Parameters:  $T = 1, K = 100, B = 110, R = 0.5, r = 0.5$  $0.05, q = 0.03, \sigma = 0.1, S_0 = 100, 250$  monitoring dates, 1000 time steps,  $\alpha = 20, \beta = 0.1, I = 100$  grid points

are optimally at grid midpoints. For example, choosing the nonuniform grid with  $I = 100$  in Figure 1, one computes  $\Delta t_{\text{Grid}} \approx 0.00066$ . Since the approximate daily sampling interval is  $\Delta t_B \approx 0.004$ , the ratio is  $R_{\Delta t} \approx 0.16$  and best results are achieved with the barrier midway between grid points. For finer grids, the ratio  $R_{\Delta t}$  is even smaller. Thus, for fairly typical parameters, the monitoring interval for which placing barriers on grid points becomes optimal is so small that simply modeling the option as continuously monitored to begin with is probably sufficiently accurate. It is surely much more efficient, because the time steps can be much larger than  $\Delta t_{\text{Grid}}$  when semi-implicit time-stepping

methods like Crank-Nicolson or Rannacher [4] are used.

### **Time Discretization**

In the examples thus far, very large numbers of time steps have been used (far in excess of what is practical or desirable), to eliminate time discretization error and isolate spatial discretization error. Considering for the moment the simple heat equation (written in reverse time as it might be in the context of finance),

$$\frac{\partial V}{\partial t} + \kappa \frac{\partial^2 V}{\partial x^2} = 0 \tag{10}$$

the following partially implicit time discretization can be proposed:

$$\frac{V^{n+1} - V^n}{\Delta t} + \theta \kappa \frac{\partial^2 V^{n+1}}{\partial x^2} + (1 - \theta) \kappa \frac{\partial^2 V^n}{\partial x^2} = 0$$
(11)

to advance the solution from  $t^{n+1}$  to  $t^n$ , where  $\theta$  is the "implicitness" parameter.

The Crank-Nicolson method, which is often recommended because its truncation error is  $O(\Delta t^2)$ , corresponds to  $\theta = 0.5$ . As is well known [5, 6], a Fourier analysis of equation (11) shows that the Crank-Nicolson method is also unconditionally stable. No individual Fourier mode grows exponentially as  $n \to \infty$  no matter the size of  $\Delta t$  relative to the characteristic diffusion time of the grid. However, the Nyquist modes, which change sign at alternate grid points, while stable for large time steps, do not diffuse away, but simply alternate sign on succeeding time steps. On the other hand, a fully implicit method  $\theta = 1$  has truncation error  $O(\Delta t)$ , but the Nyquist modes decay rapidly when  $\Delta t$  is large relative to the diffusion time of the grid.

In pricing discretely sampled barrier options, one enforces the knockout or knock-in conditions by simply changing the option value  $V(S)$  appropriately on monitoring dates. Doing so creates discontinuities that add energy to the Nyquist portion of the Fourier spectrum. Thus, while the Nyquist modes formally remain stable under Crank-Nicolson differencing, their amplitude can still grow with each periodic monitoring. The result can be oscillatory solutions near the barrier. And because the Nyquist modes are highly oscillatory, they have a much larger polluting effect on the Greeks  $\Delta$  and  $\gamma$  than on the value itself [6].

In the Rannacher [4] method, several fully implicit time steps are taken after each barrier monitoring date (or more generally after any event that can result in value or  $\Delta$  becoming discontinuous), followed by Crank-Nicolson steps. If the number of implicit steps remains constant as the total number of time steps is increased, then the method is  $O(\Delta t^2)$ . However, it has superior performance when applied to solutions with discontinuities such as digital options or discretely monitored barrier options, since the fully implicit steps in Rannacher drastically reduce the Nyquist modes. An alternative three-level time discretization that likewise has truncation error

of  $O(\Delta t^2)$  while eliminating Nyquist modes can also be formulated for the parabolic PDEs common in computation finance. See [7] for a detailed discussion of the three-level scheme for pricing discretely monitored barrier options. Here, the Rannacher scheme is used because of its simplicity.

Figure 2 displays the present  $(t = 0)$  option delta  $=\partial V(S)/\partial S$  in the immediate neighborhood of the barrier for Grid C of Table 3 when  $I = 200$ , for both Rannacher discretization and Crank-Nicolson. However, the number of time steps is a more practical 1000. The accumulation of Nyquist mode energy near the barrier is evident for Crank-Nicolson differencing, but absent for Rannacher in which two fully implicit time steps were used after each monitoring date. With 250 monitoring dates and 1000 time steps, fully one half of the time steps were implicit. Hence, time discretization error is fairly large despite the stability. However, as the number of time steps is increased, the fraction of fully implicit steps decreases and convergence is quadratic in  $\Delta t$ as shown in Table 4.

Comparing the results of Table 2 ( $N = 50000$ time steps) to those of Table 4,  $(N \text{ varies with } I)$ it is apparent that most of the error in Table 4 can be ascribed to time discretization, even with a scheme that is clearly quadratically convergent. This is expected for a barrier option with high frequency (approximately daily) monitoring. The monitoring periodically creates discontinuous option values  $V(S)$ in the neighborhood of the barrier, and sufficient time steps are required to resolve the evolution of the strong gradients (large  $\Delta s$  and  $\gamma s$ ) created.

#### References

Table 4 Finite difference results for a discretely monitored up-out barrier call.  $I$  is the number of grid points, N the number of time steps. Parameters:  $T = 1, K = 100,$  $B = 110, R = 0.5, r = 0.05, q = 0.03, \sigma = 0.1, S_0 = 100,$ 250 monitoring dates,  $\alpha = 20$ ,  $\beta = 0.1$ 

|      | N     | $V(S_0)$  | Error     | Ratic |
|------|-------|-----------|-----------|-------|
| 100  | 500   | 0.9284932 | 0.0092888 |       |
| 200  | 1000  | 0.9212974 | 0.0020930 | 4.44  |
| 400  | 2000  | 0.9197262 | 0.0005218 | 4.01  |
| 800  | 4000  | 0.9193361 | 0.0001317 | 3.96  |
| 1600 | 8000  | 0.9192377 | 0.0000333 | 3.96  |
| 3200 | 16000 | 0.9192129 | 0.0000085 | 3.91  |

- [1] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–659.
- [2] Broadie, M., Glasserman, P. & Kou, S.G. (1997). A continuity correction for discrete barrier options, *Mathematical Finance* **7**, 325–349.
- [3] Cont, R. & Voltchkova, E. (2005). A finite difference scheme for option pricing in jump diffusion and exponential Levy models, *SIAM Journal on Numerical Analysis* **43**(4), 1596–1626.
- [4] Giles, M. & Carter, R. (2006). Convergence of Crank– Nicolson and Rannacher time stepping, *Journal of Computational Finance* **9**, 89–112.
- [5] Heston, S. (1993). A closed-form solution for options with stochastic volatility with applications to bond and currency options, *Review of Financial Studies* **6**, 327–343.

- [6] Shaw, W. (1998). *Modeling Financial Derivatives with Mathematica*, Cambridge University Press, Cambridge.
- [7] Tavella, D. & Randall, C. (2000). *Pricing Financial Instruments: The Finite Difference Method*, John Wiley & Sons, New York.

## **Related Articles**

**Barrier Options**; **Corridor Options**; **Crank–Nicolson Scheme**; **Finite Difference Methods for Early Exercise Options**; **Partial Integro-differential Equations (PIDEs)**; **Tree Methods**.

CURT RANDALL
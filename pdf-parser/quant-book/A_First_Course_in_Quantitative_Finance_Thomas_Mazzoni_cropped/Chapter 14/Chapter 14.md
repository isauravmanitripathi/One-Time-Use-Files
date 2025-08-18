# Exotics in the Black-Scholes-Model

Analytic solutions are very rare exceptional cases in derivative pricing. Most of the time, the *Black–Scholes*-equation has to be solved numerically. The strategy for solving the equation depends on the nature of the contract under consideration. There are two major avenues one can take: solving the *Black–Scholes*-PDE with finite difference methods, and Monte Carlo simulation. Both strategies are intimately linked by the duality we already encountered several times. In the *Black-Scholes*-world, the connection is provided explicitly by the *Feynman–Kac*-theorem.

#### Finite Difference Methods 14.1

The solution of the *Black-Scholes*-PDE is a function  $V(S, t)$  that is much like a map of geographic elevation above the S-t-plane. Finite difference techniques represent the S-t-plane by a finite discrete grid, see Figure 14.1. The idea is to solve the respective PDE approximately at the grid points and afterwards, if necessary, to interpolate intermediate values. The method is only approximately exact, because differentials are replaced by finite differences. The order of magnitude of the resulting error depends on how fine- or course-grained we choose our grid. This is also an ideal opportunity to briefly discuss what we mean exactly by the order of magnitude.

![](_page_0_Figure_5.jpeg)

Fig. 14.1 Finite difference scheme with terminal and boundary conditions

The concept is best understood by considering a concrete example. Suppose you *Taylor*-expand the exponential  $e^x$  around  $x = 0$ , but because x is small, you want to indicate that terms of order  $x^2$  are probably negligible. You thus write

$$e^x = 1 + x + O(x^2). \tag{14.1}$$

The symbol O is called the *Landau*-symbol and it represents all terms of order  $x^2$  and higher in (14.1). More precisely, an arbitrary function  $f(x)$  is said to be of order  $g(x)$ ,  $f(x) \in O(g(x))$ , if

$$\lim_{x \to x_0} \frac{f(x)}{g(x)} = c < \infty, \tag{14.2}$$

with c being a constant. We can check this definition in our example. Clearly  $x_0 = 0$ and  $g(x) = x^2$ . The function  $f(x)$  is given by all missing terms in the *Taylor*-expansion, that is

$$f(x) = \sum_{k=2}^{\infty} \frac{x^k}{k!}.$$
 (14.3)

We can now evaluate  $(14.2)$ ,

$$\lim_{x \to 0} \frac{f(x)}{x^2} = \lim_{x \to 0} \left( \frac{1}{2} + \frac{x}{6} + \frac{x^2}{24} + \dots \right) = \frac{1}{2}.$$
 (14.4)

So we know that our notation in  $(14.1)$  is consistent. But what does the *O*-term tell us? If we neglect terms that can be represented by a function  $f(x)$ , then the approximation error we make is  $c \cdot g(x)$  for  $x \to x_0$ . So in our above example, the approximation error for small x is given by

$$e^{x} - (1+x) \approx \frac{x^{2}}{2}.$$
 (14.5)

There are two important things to note about the *Landau*-symbol. First, nothing changes whether we add or subtract the order term, because we can always change the sign of the constant  $c$ . More generally, we can absorb any constant in front of the order term into c. Second, if we have a function  $f(x) \in O(x^n)$ , then the order of  $x^m \cdot f(x)$ is  $O(x^{m+n})$ .

Let's now turn to the problem of discretizing the *Black–Scholes*-equation. Let's reverse the direction of time by focusing on the time to expiry  $\tau = T - t$ . The generalized *Black–Scholes-PDE* in terms of  $\tau$  is

$$\frac{\partial V}{\partial \tau} = bS \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV.$$
 (14.6)

Suppose, we have already established a grid as in Figure 14.1. Then the values of the independent variables at the grid points are  $S = n \cdot \Delta S$  for  $n = 0, \dots, N$ , and  $\tau = m \cdot \Delta \tau$ for  $m = 0, \ldots, M = \frac{T}{\Lambda \tau}$ . We will represent the function values at the grid points by the following notation, analogous to the binomial model of Chapter 12,

$$V(S,\tau) = V(n\Delta S, m\Delta \tau) = V_m^{(n)}.$$
(14.7)

#### **293 Exotics in the Black–Scholes-Model**

Now let's see what we can do with the partial derivatives. Let's first *Taylor*-expand the value of the derivative *V* around τ = *m*∆τ,

$$V_{m+1}^{(n)} = V_m^{(n)} + \frac{\partial V}{\partial \tau} \Delta \tau + O(\Delta \tau^2). \tag{14.8}$$

The expansion (14.8) is exact, because all higher order terms are summarized by the *Landau*-symbol. Rearranging and dividing by ∆τ yields

$$\frac{\partial V}{\partial \tau} = \frac{V_{m+1}^{(n)} - V_m^{(n)}}{\Delta \tau} + O(\Delta \tau). \tag{14.9}$$

Additionally, we have two partial derivatives of *V* with respect to *S*, namely the delta and the gamma of the option. It is perfectly sensible to define the delta exactly the same way as the first order time derivative (14.9), but we can do better. Because we will require the change of delta in computing gamma, we have to involve at least three different grid points. So let's see if we cannot use this extra computational effort to improve the approximation of the first order derivative. We start as before by *Taylor*expanding *V* around *S* = *n*∆*S*, but this time, we do a second order expansion

$$V_m^{(n+1)} = V_m^{(n)} + \frac{\partial V}{\partial S} \Delta S + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \Delta S^2 + O(\Delta S^3). \tag{14.10}$$

Now let's do the mirror-inverted expansion

$$V_m^{(n-1)} = V_m^{(n)} - \frac{\partial V}{\partial S} \Delta S + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \Delta S^2 + O(\Delta S^3), \tag{14.11}$$

and subtract (14.11) from (14.10). The result is

$$V_m^{(n+1)} - V_m^{(n-1)} = 2 \cdot \frac{\partial V}{\partial S} \Delta S + O(\Delta S^3). \tag{14.12}$$

**Quick calculation 14.1** Can you see why the O(∆*S* 3 )-term is unaffected?

Slightly rearranging and dividing by ∆*S* yields

$$\frac{\partial V}{\partial S} = \Delta_m^{(n)} = \frac{V_m^{(n+1)} - V_m^{(n-1)}}{2\Delta S} + O(\Delta S^2). \tag{14.13}$$

We have succeeded in approximating the delta to order ∆*S* 2 , instead of order ∆*S*, by applying a central difference. Now let's move on to the second order partial derivative. If we add (14.10) and (14.11), we obtain

$$V_m^{(n+1)} + V_m^{(n-1)} = 2V_m^{(n)} + \frac{\partial^2 V}{\partial S^2} \Delta S^2 + O(\Delta S^4). \tag{14.14}$$

The equation is accurate to order  $\Delta S^4$ , because all  $\Delta S$ -terms with odd exponents cancel. Dividing by  $\Delta S^2$  and rearranging yields

$$\frac{\partial^2 V}{\partial S^2} = \Gamma_m^{(n)} = \frac{V_m^{(n+1)} - 2V_m^{(n)} + V_m^{(n-1)}}{\Delta S^2} + O(\Delta S^2). \tag{14.15}$$

Putting all the pieces together, we obtain a rule for the update of a grid point in a new time slice

$$V_{m+1}^{(n)} = V_m^{(n)} + \Delta \tau \bigg( b n \Delta S \cdot \Delta_m^{(n)} + \frac{1}{2} \sigma^2 n^2 \Delta S^2 \cdot \Gamma_m^{(n)} - r V_m^{(n)} \bigg), \tag{14.16}$$

where we have conveniently neglected the truncation error. Note that only the points  $V_m^{(n-1)}, V_m^{(n)},$  and  $V_m^{(n+1)}$  are required to compute the new point  $V_{m+1}^{(n)}$ . If all points in time slice *m* are known, then every interior point in time slice  $m + 1$  can be computed; see Figure 14.2. The overall approximation error of this scheme will be  $O(\Delta \tau, \Delta S^2)$ .

You might ask, whether this scheme is stable in that the approximation errors are guaranteed not to be accumulated and critically amplified, no matter what  $\Delta \tau$  and  $\Delta S$  is chosen? The answer is no, the scheme might very well be unstable if we choose the wrong  $\Delta \tau$ . The necessary condition can be determined in a stability analysis. We will conduct a non-rigorous version of such an analysis. Instability is always due to oscillations in the approximate solution, which are amplified over time. But oscillatory solutions occur only for second order differentials or higher. Remember that the second order ordinary differential equation (13.43) on page 260 had solutions involving sine and cosine. Thus, for analyzing the stability of the finite difference scheme, we have to concern ourselves only with that part of the *Black–Scholes*-PDE that involves second order partial derivatives,

$$\frac{\partial V}{\partial \tau} = \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}.$$
 (14.17)

![](_page_3_Figure_8.jpeg)

Fig. 14.2 Recursive finite difference approximation of the partial differential equation

#### Fxotics in the Black-Scholes-Model

For the stability analysis, we will require a discretized version of this equation

$$V_{m+1}^{(n)} = V_m^{(n)} + \frac{\Delta \tau}{2} \sigma^2 n^2 \Delta S^2 \cdot \frac{V_m^{(n+1)} - 2V_m^{(n)} + V_m^{(n-1)}}{\Delta S^2}.$$
 (14.18)

 $\sim$ 

 $\sim$   $\sim$ 

We are looking for a solution of the form

$$V_m^{(n)} = \alpha^m e^{i\omega n},\tag{14.19}$$

/ 1

which is stable, if the absolute value of the amplitude is  $|\alpha| \leq 1$ , because then the oscillations, encoded in the complex exponential, are not amplified over time. Plugging  $(14.19)$  into  $(14.18)$  yields

$$\alpha^{m+1}e^{i\omega n} = \alpha^m e^{i\omega n} + \Delta \tau \sigma^2 n^2 \cdot \alpha^m e^{i\omega n} \frac{e^{i\omega} + e^{-i\omega} - 2}{2}.$$
 (14.20)

Using the relation  $\cos \omega = \frac{e^{i\omega} + e^{-i\omega}}{2}$  and dividing by  $\alpha^m e^{i\omega n}$ , one obtains

$$\alpha = 1 + \Delta \tau \sigma^2 n^2 (\cos \omega - 1). \tag{14.21}$$

Because  $-1 \le \cos \omega \le 1$ , we have the following bounds on  $\alpha$ 

$$1 - 2\Delta\tau\sigma^2 n^2 \le \alpha \le 1,\tag{14.22}$$

from which we can immediately read off that for  $|\alpha| \le 1$ , the inequality

$$\Delta \tau \sigma^2 n^2 \le 1 \tag{14.23}$$

has to hold. This condition is most binding for  $n = N$  and therefore, we end up with the stability condition

$$\Delta \tau \le \frac{1}{\sigma^2 N^2} = \frac{\Delta S^2}{\sigma^2 S_{\text{max}}^2},\tag{14.24}$$

where  $S_{\text{max}} = N\Delta S$  is the upper boundary of the grid in the spatial direction. Of course there are other schemes that are unconditionally stable. For example the one of Crank and Nicolson (1996), which is the working horse of derivative pricing. Furthermore, it has an overall approximation error of  $O(\Delta \tau^2, \Delta S^2)$ . But our first order finite difference scheme has its advantages. It is hard to make mistakes in coding and the implementation of American exercise right is straightforward.

We have one issue left out so far: Boundary conditions. We are only able to recursively compute one time slice after another, if we know the values  $V_m^{(0)}$  and  $V_m^{(N)}$  for  $m = 0, \ldots, M$  in advance, see again Figure 14.2. Strictly speaking, this is not entirely correct. There are two possible types of boundary conditions we can impose, *Dirichlet*- and *Neumann*-boundary conditions. They are best understood by referring to our earlier ordinary differential equation  $(13.43)$ 

$$\frac{d^2x(t)}{dt^2} = -x(t).$$
 (14.25)

Assume that we are interested in a solution of this equation in the interval  $t \in [0, \pi]$ . We have seen earlier that there are multiple solutions to this problem, but by imposing

![](_page_5_Figure_1.jpeg)

**Fig. 14.3** *Dirichlet*- (left) and *Neumann*-boundary conditions (right)

boundary conditions, we can single out a smaller subset. Let's first impose a *Dirichlet*condition. This condition requires that the value at the boundary is fixed. We impose such a condition on both boundaries, say

$$x(0) = 0$$
 and  $x(\pi) = 0,$  (14.26)

see also Figure 14.3 left. It is immediately clear that the boundary conditions  $(14.26)$ only allow solutions of the form

$$x(t) = c \sin t, \tag{14.27}$$

even though the value of the constant c is not yet determined. This is similar to the derivative pricing problem, where the fair value of an option can only be determined. when boundary and initial conditions are known. Now let's look into *Neumann*boundary conditions. In this kind of condition not the value of the function itself is fixed at the boundary, but the value of its first derivative. You can think of such a condition as describing an elastic string, where the ends can move freely along the poles at  $t = 0$  and  $t = \pi$  in Figure 14.3 right. But the angle between the string and the respective pole at  $t = 0$  and  $t = \pi$  is fixed by the *Neumann*-condition. If we impose the *Neumann*-boundary conditions

$$x'(0) = 0$$
 and  $x'(\pi) = 0$  (14.28)

on the differential equation  $(14.25)$ , it is easily seen that we can only have solutions of the form

$$x(t) = c\cos t. \tag{14.29}$$

Of course nothing prevents us from imposing mixed boundary conditions, for example a *Dirichlet*-condition on the lower boundary and a *Neumann*-condition on the upper boundary.

**Quick calculation 14.2** Verify that the mixed boundary conditions  $x(0) = c_1$  and  $x'(\pi) =$  $c_2$  require the solution  $x(t) = c_1 \cos t - c_2 \sin t$  of (14.25).

Let's now investigate some boundary conditions for our finite difference scheme. We will give examples for both *Dirichlet*- and *Neumann*-boundary conditions. Let's start with the lower boundary  $V_m^{(0)}$  for  $m = 0, \ldots, M$ . If the derivative under consideration is

#### Fxotics in the Black-Scholes-Model

a call option, then the payoff at expiry is  $C_0^{(0)} = 0$ . Remember that expiry means  $\tau = 0$ . But it also stays zero at every time and thus, the *Dirichlet*-boundary condition in this case is

$$C_m^{(0)} = 0,\t(14.30)$$

for  $m = 0, \ldots, M$ . More generally, if we investigate the *Black–Scholes*-equation for  $S = 0$ , we are left with the ordinary differential equation

$$\frac{\partial V}{\partial \tau} = -rV. \tag{14.31}$$

But that is nothing more than saying that the partial derivative of  $V$  with respect to  $S$  is zero. Of course the second order partial derivative of V with respect to S has to vanish also in this case. So (14.31) is the result of the Neumann-condition

$$\left. \frac{\partial V}{\partial S} \right|_{S=0} = 0. \tag{14.32}$$

Using our finite difference approximation  $(14.9)$  on the left hand side of  $(14.31)$ , and slightly rearranging yields

$$V_{m+1}^{(0)} = (1 - r\Delta\tau)V_m^{(0)}.$$
 (14.33)

This is the *Neumann*-boundary condition at  $S = 0$ . It holds for most contracts, including call and put options.

An ideal situation for an upper boundary *Dirichlet*-condition is a barrier option with upper knockout barrier. Because the value of the contract turns to zero immediately if the barrier is hit, we have for  $S_u = N\Delta S$ 

$$V_m^{(N)} = 0. \t(14.34)$$

An ordinary call option can also be equipped with an upper *Dirichlet*-boundary condition. If  $S$  is sufficiently larger than the exercise price  $K$ , then the option price is approximately equal to the price of a forward contract,  $C_t(K, T) \approx S_t - e^{-r(T-t)}K$ . Thus, the boundary condition is

$$C_m^{(N)} = N\Delta S - e^{-rm\Delta\tau}K. \tag{14.35}$$

There is a more elegant way that also covers almost all contracts you will encounter. Most contracts have a payoff that becomes linear for large values of  $S$ . That means, we have the Neumann-boundary conditions

$$\left. \frac{\partial V}{\partial S} \right|_{S \gg K} = \text{const.} \tag{14.36}$$

There is an even more useful consequence of  $(14.36)$ ; the second partial derivative of V with respect to S has to vanish. Assume this holds already for  $\Gamma_m^{(N-1)}$ , then trivial rearrangements yield the upper boundary condition

$$V_m^{(N)} = 2V_m^{(N-1)} - V_m^{(N-2)}.\t(14.37)$$

# **Numerical Valuation and Coding**

Since for all practical purposes numerical computation of option prices is unavoidable, the necessary algorithms are presented in terms of a hopefully intuitive pseudo-code, not referring to any particular programming language. We will use only a minimum of commands: Set, Int, Draw, and Print. The Set-command fixes parameters we have chosen, usually the upper boundary value  $S_{\text{max}}$  and the vertical resolution of the grid N. Int returns the integer part of a real number, for example Int  $\pi = 3$  or Int  $e = 2$ . Note that Int always rounds down. Draw generates a random number from a specified distribution. For example Draw  $z \sim N(0, 1)$  generates a realization z of a standard normally distributed random variable. This command will be used later in coding Monte Carlo simulations. Finally, the Print-command enables the algorithm to generate output.

Besides those simple commands, we will use two structural elements, a simple loop construction and an If-then gate. A loop always has the architecture

```
For n = n_0 to N
Next n
```

where the elements to be repeatedly executed (body of the loop) are enclosed by the For-Next-marks. The If-then gate has always the form

If (condition) then (implication).

If the condition is true, the implication becomes effective, otherwise nothing happens. There are of course more sophisticated versions of loops and gates, but we want to keep things simple and transparent.

To enhance structural clarity of our code, there are three very useful formatting tricks at our disposal. First, we will separate different structural parts of the algorithm by horizontal lines. Second, we will emphasize loops by indenting the body, and third, we will include comments in the form of non-executable code, indicated by the symbol  $\triangleright$ . The use of such structuring tools is imperative in programming, if you are to have the slightest hope of being able to reconstruct what you have done, when looking at your code at a later time. Furthermore, you may want to design your code so that it is as versatile as possible, in order to use it for many different option types with only minor modifications. In this case, a clear structure and ample use of comments is also enormously helpful.

To see how all this works, consider a very simple example of a plain vanilla European call option. Of course, we can solve this problem analytically, but let's do it anyway and afterwards check the quality of our numerical result.

| Box 14.1 Pseudo-code for plain vanilla European call option                                                                                         |                                  |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--|--|
| $\text{Set } S_{\text{max}}, N$                                                                                                                     | Initialization                   |  |  |
| $h = r$                                                                                                                                             | Cost-of-carry rate               |  |  |
| $\Delta S = S_{\text{max}}/N$                                                                                                                       |                                  |  |  |
| $M = \text{Int}\left(T\sigma^2 S_{\text{max}}^2/\Delta S^2\right) + 1$                                                                              | Stability constraint             |  |  |
| $\Delta \tau = T/M$                                                                                                                                 |                                  |  |  |
| For $n = 0$ to N                                                                                                                                    | Initial condition                |  |  |
| $V_0^{(n)} = \max(n\Delta S - K, 0)$                                                                                                                |                                  |  |  |
| Next n                                                                                                                                              |                                  |  |  |
| For $m = 1$ to M                                                                                                                                    | $\triangleright$ Time slices     |  |  |
| For $n=1$ to $N-1$                                                                                                                                  | $\triangleright$ Interior points |  |  |
| $\Delta = \left(V_{m-1}^{(n+1)} - V_{m-1}^{(n-1)}\right) / (2\Delta S)$                                                                             |                                  |  |  |
| $\Gamma = \left(V_{m-1}^{(n+1)} - 2V_{m-1}^{(n)} + V_{m-1}^{(n-1)}\right) / \Delta S^2$                                                             |                                  |  |  |
| $V_{m}^{(n)} = V_{m-1}^{(n)} + \Delta \tau \left( b n \Delta S \Delta + \frac{1}{2} \sigma^{2} n^{2} \Delta S^{2} \Gamma - r V_{m-1}^{(n)} \right)$ |                                  |  |  |
| $Next \ n$                                                                                                                                          |                                  |  |  |
| $V_m^{(0)} = 0$                                                                                                                                     | ⊳ Boundary conditions            |  |  |
| $V_m^{(N)} = 2V_m^{(N-1)} - V_m^{(N-2)}$                                                                                                            |                                  |  |  |
| $Next \ m$                                                                                                                                          |                                  |  |  |
| Print $V_M$                                                                                                                                         | ⊳ Output                         |  |  |

Example 14.1

Consider a plain vanilla European call option, contingent on a non-dividend paying stock, with known r,  $\sigma$ , K, and T. What is the fair price of this option at  $t = 0$ , when valuated numerically?

#### Solution

The entire pseudo-code for pricing this option is provided in Box 14.1. The algorithm is divided into four parts: initialization, determination of the initial condition, main part, and output of the results. Furthermore, there was a Dirichlet-condition imposed at the lower boundary  $n = 0$  and a *Neumann*-condition at the upper boundary  $n = N$ . Finally, the output  $V_M$  is shorthand for  $V_M^{(n)}$  with  $n = 0, \ldots, N$ .

To make the problem of Example 14.1 concrete, choose the parameters  $r = 5\%$ ,  $\sigma =$ 20%,  $K = 10$ , and  $T = 1$  year. To start the numerical valuation algorithm, we fix the upper boundary by  $S_{\text{max}} = 20$  and the number of grid points in the spatial direction

![](_page_9_Figure_1.jpeg)

**Fig. 14.4** 3D Numerical solution of the European plain vanilla call valuation problem

*N* = 100. From those values, we immediately find that in order to obey the stability condition (14.24), we have to use ∆τ ≤ 2.5 · 10<sup>−</sup><sup>3</sup> . Figure 14.4 shows the interpolated result of the finite difference approximation over the entire interval [0,*T*]. The surface cannot be distinguished from the one produced by the analytical *Black–Scholes*-formula with the naked eye. To get an impression of the precision of the numerical solution, the difference between the exact and the approximate surface is indicated in Figure 14.5. The spatial spacing ∆*S* is roughly O(10<sup>−</sup><sup>1</sup> ). Thus, ∆*S* <sup>2</sup> has to be O(10<sup>−</sup><sup>2</sup> ). The error in the time direction can be neglected, because ∆τ is O(10<sup>−</sup><sup>3</sup> ). It is easily seen that the maximal approximation error is within the correct order of magnitude. The rapid increase around the exercise price at expiry is partly due to interpolation and should not be taken too seriously.

Now that we have successfully valuated our first contract numerically, we can move on to the more severe cases, where numerical valuation is not a fancy alternative to the analytic solution, but the only way to determine the fair price of an option.

![](_page_9_Figure_5.jpeg)

**Fig. 14.5** 3D Approximation error ϵ in percent of the numerical solution for the plain vanilla call option

# **Weak Path Dependence and Early Exercise**

We have already learned that knockout barrier options are only weakly path dependent. Although there exist analytical formulas for a number of standard barrier contracts (see Haug,  $2007$ , sect.  $4.17$ ), we will continue pricing them numerically, mainly for two reasons. First, most barrier options are very sensitive to changes in volatility near the barrier, and since the assumption of a constant volatility of the underlying is a kind of flaw in the *Black–Scholes*-theory, barrier options are usually valuated numerically within local or stochastic volatility models. Second, this class of options are optimal candidates for numerical schemes like our first order finite difference scheme. The reason is that we can easily impose a *Dirichlet*-condition on the knockout boundary. Think for example of the plain vanilla call option we have just valuated. If there were a knockout barrier, say at  $S_u = 15$ , we would only have to make two tiny modifications in the pseudo-code, provided in Box 14.1. Naturally, we would have chosen  $S_{\text{max}} = S_u$ , because the value of the contract at  $S > S_u$  does not matter anymore, the option is knocked out. The first modification would have affected the initial condition. The code fragment would have changed into

For  $n=0$  to  $N-1$  $V_0^{(n)} = \max(n\Delta S - K, 0)$  $Next \ n$  $V_{0}^{(N)} = 0.$ 

The second modification is even smaller and concerns the upper boundary condition, which simplifies to  $V_m^{(N)} = 0$ . Everything else in our code remains unchanged. If we run the algorithm, we get the solution for the barrier knockout call indicated in Figure 14.6. Of course, we can immediately compute the fair price for the associated knockin call option from barrier put-call parity  $(12.56)$  on page 242. The solution for this option is provided in Figure 14.7. Note that the interpolation is not very accurate around  $S_u$  at expiry, because a violent jump in the value of the option occurs at the boundary.

![](_page_10_Figure_5.jpeg)

Fig. 14.6 BD Numerical solution for the European plain vanilla knockout barrier call option

### 14.3

![](_page_11_Figure_1.jpeg)

Fig. 14.7 3D Numerical solution for the plain vanilla knockin barrier call option from barrier put-call parity

What modifications do we have to make if there is American exercise right? In this case we have to compare the value of the option at every grid point with the value if immediately exercising the contract. The easiest way to accomplish this task is to insert an additional code fragment immediately after the update of the boundary conditions in Box 14.1

```
\begin{array}{c} \text{For} \; n=0 \; \texttt{to} \; N \\ V^{(n)}_m = \max \left( V^{(n)}_m, \, V^{(n)}_0 \right) \end{array}Next n.
```

Because  $V_0^{(n)}$  is the payoff of the option at grid point *n*, we do not even need to worry about the particular type of contract we are dealing with. Thus, there is no need for additional modifications for a vast variety of options. Let's take a look at an individually designed contract.

#### Example 14.2

Consider the contract specified by the term sheet given in Table 14.1. Assume that the annual domestic interest rate r and the volatility of the foreign currency  $\sigma$  is known. How can this option be valuated numerically?

| <b>Table 14.1</b> Option term sheet |                                           |  |  |
|-------------------------------------|-------------------------------------------|--|--|
| Option type:                        | Knockout call option                      |  |  |
| Barrier type:                       | Lower barrier $S_l$ with rebate R         |  |  |
| Underlying:                         | Foreign currency with interest rate $r_f$ |  |  |
| Exercise right:                     | American                                  |  |  |
| Exercise price:                     | K                                         |  |  |
| Expiry date:                        |                                           |  |  |

| Box 14.2<br>Pseudo-code for individually contracted option                                                                          |                        |  |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------|--|
| Set<br>Smax,<br>N                                                                                                                   | ◃ Initialization       |  |
| b = r −<br>rf                                                                                                                       | ◃ Cost-of-carry rate   |  |
| −<br>/N<br>∆S =<br>(<br>Smax<br>Sl<br>)                                                                                             |                        |  |
| (<br>)<br>2S<br>2<br>2<br>M = Int<br>Tσ<br>max/∆S<br>+ 1                                                                            | ◃ Stability constraint |  |
| ∆τ<br>= T/M                                                                                                                         |                        |  |
| For<br>n = 1 to<br>N                                                                                                                | ◃ Initial condition    |  |
| (n)<br>+ n∆S −<br>= max (<br>K,<br>V<br>Sl<br>0<br>)<br>0                                                                           |                        |  |
| Next<br>n                                                                                                                           |                        |  |
| (0)<br>V<br>= R<br>0                                                                                                                | ◃ Rebate               |  |
| For<br>m = 1 to<br>M                                                                                                                | ◃ Time slices          |  |
| N −<br>For<br>n = 1 to<br>1                                                                                                         | ◃ Interior points      |  |
| (n−1)<br>∆ = (<br>(n+1)<br>)<br>−<br>/(2∆S)<br>V<br>V<br>m−1<br>m−1                                                                 |                        |  |
| (n−1)<br>(n+1)<br>(n)<br>Γ = (<br>)<br>−<br>2<br>/∆S<br>V<br>2V<br>+ V<br>m−1<br>m−1<br>m−1                                         |                        |  |
| (n)<br>(n)<br>rV(n)<br>(<br>)<br>+ n∆S)∆ + 1<br>2<br>2Γ<br>−<br>+ ∆τ<br>σ<br>V<br>m = V<br>b(Sl<br>(Sl<br>+ n∆S)<br>m−1<br>m−1<br>2 |                        |  |
| Next<br>n                                                                                                                           |                        |  |
| (0)<br>m = R<br>V                                                                                                                   | ◃ Boundary conditions  |  |
| (N−1)<br>(N−2)<br>(N)<br>−<br>= 2V<br>V<br>V<br>m<br>m<br>m                                                                         |                        |  |
| For<br>n = 1 to<br>N                                                                                                                | ◃ American exercise    |  |
| (n)<br>(n)<br>(n)<br>m = max (<br>)<br>m ,<br>V<br>V<br>V<br>0                                                                      |                        |  |
| Next<br>n                                                                                                                           |                        |  |
| Next<br>m                                                                                                                           |                        |  |
| Print<br>VM                                                                                                                         | ◃ Output               |  |

#### Solution

The pseudo-code for valuating this contract is provided in Box 14.2. The grid points are now concentrated in the spatial direction between *S<sup>l</sup>* and *S*max, because the contract is knocked out for *S* < *S<sup>l</sup>* . The lower boundary condition includes the rebate *R* and there is an additional code fragment, accounting for the American exercise right. ........................................................................................................................

# **14.4 Girsanov's Theorem**

Girsanov's theorem is one of the cornerstones of derivative pricing. We have assumed that the price process of an arbitrary underlying *S* is governed by the geometric *Brown*ian motion

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$dS_t = \mu S_t dt + \sigma S_t dW_t. \tag{14.38}$$

Of course this process is embedded in a background probability space  $(\Omega, \mathcal{F}, P)$ , equipped with a filtration  $\mathcal{F}_t$ , to which  $S_t$  is adapted. But this model is with respect to the physical probability measure  $P$ . By now we know very well that pricing is governed by another probability measure  $Q$ , referred to as the risk-neutral probability measure. Girsanov's theorem tells us how the geometric *Brownian* motion (14.38) transforms, if  $W_t$  is perceived under the risk-neutral measure O. At first sight this theorem appears cryptic. We will first state it in full generality and afterwards reduce and decipher it step by step.

**Theorem 14.1 (Girsanov's theorem)** Let  $(\Omega, \mathcal{F}, P)$  be a probability space, equipped with a natural filtration  $\mathcal{F}_t$ , generated by the Wiener-process  $W_t$  for  $0 \le t \le T$ . If  $\lambda_t$  is a  $\mathcal{F}_t$ adapted process, such that

$$\int_0^T \lambda_s^2 ds < \infty$$

holds almost surely, and the process  $M_t$ , defined by

$$M_t = e^{-\int_0^t \lambda_s dW_s - \frac{1}{2} \int_0^t \lambda_s^2 ds}$$

is a martingale, then there exists an equivalent probability measure Q, induced by the Radon-Nikodym-derivative  $\frac{dQ}{dP}\Big|_{\mathcal{F}_t} = M_t$ , such that

$$W_t^Q = W_t + \int_0^t \lambda_s ds$$

is a standard Wiener-process under  $Q$ .

Don't get fooled by the fancy terms and integrals.  $M_t$  is strongly related to the stochastic discount factor of Chapter 9 and we have

$$E[M_t S_t] = E^{\mathcal{Q}}[S_t].\tag{14.39}$$

The most delicate piece in Theorem 14.1 is the requirement that  $M_t$  is a *P*-martingale. There is a simple condition which provides sufficient support, but may be too restrictive in some cases.

**Theorem 14.2 (Novikov-condition)** The process 
$$M_t$$
 is a P-martingale if

$$E\!\left[e^{\frac{1}{2}\int_0^T\lambda_s^2ds}\right]<\infty$$

holds.

Let's see if we can make head or tail of this. In going from  $W_t$  to  $W_t^Q$  in Theorem 14.1, there is something added that looks like a risk premium. To see this even clearer, let's rewrite the equation in differential notation

$$dW_t^Q = dW_t + \lambda_t dt. \t\t(14.40)$$

#### Exotics in the Black-Scholes-Model

We know that in our complete market framework, the risk premium is

$$\lambda = \frac{\mu - r}{\sigma}.\tag{14.41}$$

**Ouick calculation 14.3** Verify that  $\lambda$  satisfies the *Novikov*-condition.

This is very convenient, because  $\lambda$  is neither a stochastic process, nor time dependent. So we can easily determine how the geometric *Brownian* motion (14.38) looks under the risk-neutral measure O, by simply replacing  $dW_t$  with  $dW_t^Q - \lambda dt$ ,

$$dS_t = \mu S_t dt + \sigma S_t dW_t^Q - (\mu - r) S_t dt$$
  
=  $r S_t dt + \sigma S_t dW_t^Q$ . (14.42)

The expected rate of return  $\mu$  is simply replaced by the risk-free rate of return r under the risk-neutral measure Q. Because under Q,  $W_t^Q$  is again  $N(0, t)$ -distributed, we usually omit the superscript. The even more interesting question is why the *Girsanov*theorem changes the drift, but leaves the volatility unaltered. This is indeed not an easy one so let's see if we can understand heuristically what is going on.

Once more define a simple random variable X, based on a coin flip experiment, with

$$X(\omega) = \begin{cases} +1 & \text{for } \omega = \uparrow \\ -1 & \text{for } \omega = \downarrow \,. \end{cases} \tag{14.43}$$

Let the probabilities for the up- and down-state be  $p = \frac{1}{2}$  and  $1 - p = \frac{1}{2}$ . Clearly, we have  $E[X] = 0$  and  $Var[X] = 1$ .

**Quick calculation 14.4** Check that the variance of X is indeed one.

Let  $X_n$  for  $n = 1, \ldots, N$  be identical but independent copies of  $X$  and define the new random variable  $S_n$  by

$$S_n = \sum_{k=1}^n X_k. \tag{14.44}$$

Furthermore, we will give the ratio  $n/N$  a new name and call it  $t = \frac{n}{N}$ . Take a third random variable  $Z_t$ , defined by

$$Z_t = \frac{S_n}{\sqrt{N}},\tag{14.45}$$

and let's analyze this quantity a little bit. It is quite obvious that the expectation value is  $E[Z_t] = 0$ . But what is the variance? Let's compute it

$$\operatorname{Var}[Z_t] = \frac{1}{N} \cdot n \cdot \operatorname{Var}[X] = \frac{n}{N} = t. \tag{14.46}$$

305

That is, *Z<sup>t</sup>* has the same first two moments as *W<sup>t</sup>* , for *t* ∈ [0, 1]. But there is more. Due to the central limit theorem, *Z<sup>t</sup>* converges in distribution to *W<sup>t</sup>* as *N* → ∞,

$$Z_t \xrightarrow{D} W_t \sim N(0, t). \tag{14.47}$$

We have now a limit process for the *Wiener*-process for 0 ≤ *t* ≤ 1. Furthermore, because *Zt* is a binomial kind of process, it is very easy to manipulate the probability measure and to see what happens in the limit. Define a new probability measure *Q* by

$$q = \frac{1}{2} + \frac{\varepsilon}{2\sqrt{N}}.\tag{14.48}$$

We have to scale the ε-correction by *N*<sup>−</sup>1/<sup>2</sup> in order to keep the moments of *Z<sup>t</sup>* constant when *N* → ∞. Note that the central limit theorem still holds and *Z<sup>t</sup>* approaches a normal distribution. But what are the moments now? Let's first do the computations for *X*. One obtains the expectation

$$E^{\mathcal{Q}}[X] = 1 \cdot \left(\frac{1}{2} + \frac{\varepsilon}{2\sqrt{N}}\right) - 1 \cdot \left(\frac{1}{2} - \frac{\varepsilon}{2\sqrt{N}}\right) = \frac{\varepsilon}{\sqrt{N}},\tag{14.49}$$

and the variance

$$\text{Var}^{\mathcal{Q}}[X] = E^{\mathcal{Q}}[X^2] - E^{\mathcal{Q}}[X]^2 = 1 - \frac{\varepsilon^2}{N}.$$
 (14.50)

It is now straightforward to compute the moments of *Z<sup>t</sup>* ,

$$E^{Q}[Z_{t}] = \frac{n}{N} \cdot \varepsilon = t \cdot \varepsilon, \qquad (14.51)$$

and

$$\operatorname{Var}^{Q}[Z_{t}] = \frac{n}{N} \cdot \left(1 - \frac{\varepsilon^{2}}{N}\right) = t \cdot \left(1 - \frac{\varepsilon^{2}}{N}\right). \tag{14.52}$$

Taking the limit *N* → ∞, we can now see that *Z<sup>t</sup>* approaches a *Brown*ian motion with drift ε under measure *Q*, because the variance is still

$$\lim_{N \to \infty} \text{Var}^{\mathcal{Q}}[Z_t] = t. \tag{14.53}$$

This argument shows in a constructive way, why the change of measure under the *Girsanov*-transformation only affects the drift, but leaves the volatility unchanged.

# **14.5 The Feynman–Kac-Formula**

## The *Feynman–Kac*-theorem is a very general connection between parabolic partial differential equations and stochastic differential equations of the *Itô*-type. It is named after the Nobel laureate Richard Feynman and the Polish mathematician Mark Kac. The theorem is a rigorous proof of Feynman's path integral formalism in the real domain. We will, as in the previous section, first state the theorem and subsequently elaborate on it.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

**Theorem 14.3 (Feynman–Kac-theorem)** Fix the usual probability space  $(\Omega, \mathcal{F}, P)$  and let  $S_t$  be a  $\mathcal{F}_t$ -measurable Itô-process of the general kind

$$dS_t = \mu(S_t, t)dt + \sigma(S_t, t)dW_t.$$

For  $0 \le t \le T$ , let  $V(S, t)$  be a sufficiently smooth function with known terminal function values  $V(S, T)$ , such that

$$V(S_t, t) = E\left[e^{-\int_t^T r(S_\tau, \tau)d\tau} V(S_T, T)\middle|\mathcal{F}_t\right]$$

holds. Then  $V(S, t)$  satisfies the parabolic partial differential equation

$$\frac{\partial V}{\partial t} + \mu(S, t) \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2(S, t) \frac{\partial^2 V}{\partial S^2} - r(S, t) V = 0,$$

subject to the terminal condition  $V(S, T)$ .

To understand this result, we first have to generalize the concept of an adjoint differential operator. For a simple operator  $D_n = \frac{d^n}{dx^n}$ , we found earlier that the adjoint operator is  $D_n^{\dagger} = (-1)^n \frac{d^n}{dx^n}$ , and for a sufficiently well behaved test function  $\varphi(x)$ , we have

$$\langle D_n f | \varphi \rangle = \langle f | D_n^\dagger \varphi \rangle. \tag{14.54}$$

Adjoining an operator means of course successive application of integration by parts. because the abstract *Dirac*-bracket of two functions is nothing else than an integral over both components. Now assume we have an operator of the form

$$L(x) = g(x)\frac{d}{dx}.$$
(14.55)

Applying our routine of integration by parts, we find

$$\langle Lf|\varphi\rangle = \int_{-\infty}^{\infty} g(x) \frac{df(x)}{dx} \varphi(x) dx$$
  
=  $g(x)f(x)\varphi(x)\Big|_{-\infty}^{+\infty} - \int_{-\infty}^{\infty} f(x) \frac{dg(x)\varphi(x)}{dx} dx$   
=  $-\langle f|\frac{d}{dx}g\varphi\rangle$ , (14.56)

from which we immediately conclude that  $L^{\dagger}(x) = -\frac{d}{dx}g(x)$ . Assume, there are two arbitrary operators  $L(x)$  and  $K(x)$ . It is obvious that we can adjoin them successively using integration by parts, that is

$$\langle LKf|\varphi\rangle = \langle Kf|L^{\dagger}\varphi\rangle = \langle f|K^{\dagger}L^{\dagger}\varphi\rangle. \tag{14.57}$$

We can thus conclude that  $(LK)^{\dagger}(x) = K^{\dagger}L^{\dagger}(x)$  holds. Of course an analogous statement for an arbitrary sequence of operators is also true. Let's define the operator

$$L_n(x) = g(x)\frac{d^n}{dx^n} = L_1 D_{n-1}(x),\tag{14.58}$$

where again  $D_n = \frac{d^n}{dx^n}$ . This one obviously has the adjoint operator

$$L_n^{\dagger}(x) = (-1)^n \frac{d^n}{dx^n} g(x) = D_{n-1}^{\dagger} L_1^{\dagger}(x). \tag{14.59}$$

There is another important consequence of the rule for adjoining a sequence of operators. Suppose we apply  $L(x)$  successively two times, then we obtain  $(L^2)^{\dagger}(x) = (L^{\dagger})^2(x)$ for the adjoint sequence. Of course this statement also holds true for arbitrary exponents. Combining this property with the bilinearity of inner products, we obtain for the exponential of an operator

$$\left(e^{L(x)}\right)^{\dagger} = \sum_{k=0}^{\infty} \frac{\left(L^{k}\right)^{\dagger}(x)}{k!} = \sum_{k=0}^{\infty} \frac{\left(L^{\dagger}\right)^{k}(x)}{k!} = e^{L^{\dagger}(x)}.$$
(14.60)

**Quick calculation 14.5** Use the bilinearity of inner products to prove that  $(L + K)^{\dagger}(x)$  =  $L^{\dagger}(x) + K^{\dagger}(x)$  holds.

Let's now turn to a very special operator, sometimes called the Kolmogorovbackward-operator

$$A(S) = rS\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2}{\partial S^2}.$$
 (14.61)

It is also referred to as the infinitesimal generator of the  $It\hat{o}$ -diffusion. Note that using (14.61), we can write the *Black–Scholes*-equation in a very compact form

$$\frac{\partial V}{\partial t} + (A(S) - r)V = 0. \tag{14.62}$$

Not only is (14.62) a neat way to write the *Black–Scholes-PDE*, it almost looks like an ordinary differential equation. If this were the case, we could immediately write the solution

$$V(S,T) = e^{-(A(S)-r)T}V(S,0). \tag{14.63}$$

Because we do not have an initial value problem, but a terminal value problem,  $V(S, T)$ is known, but not  $V(S, 0)$ . Thus, we should divide both sides by the exponential factor to obtain

$$V(S,0) = e^{(A(S)-r)T}V(S,T).$$
(14.64)

Of course this is a purely formal statement, because we cannot operate on  $V(S,T)$ directly with the exponential of an operator. At best, we would have to *Taylor*-expand the exponential and operate with the resulting products of  $A(S)$ . This would certainly be a very messy business most of the time. But instead, we can do something far more clever. Assume that at  $t = 0$ , the price of the underlying is  $S = S_0$ , with  $S_0 > 0$ . Otherwise, we would not have a valuation problem because the price would not change over time anymore. We can thus write

$$V(S_0, 0) = e^{-rT} \int_0^\infty \left( e^{A(S)T} V(S, T) \right) \delta(S - S_0) dS \tag{14.65}$$

#### **309 Exotics in the Black–Scholes-Model**

for the price of the derivative at *t* = 0. This already looks similar to a discounted expectation value. But it is also an inner product with an operator *e A*(*S*)*T* , operating on the first component. So adjoining this operator, we obtain

$$V(S_0,0) = e^{-rT} \int_0^\infty V(S,T) \, e^{A^{\dagger}(S)T} \delta(S-S_0) dS. \tag{14.66}$$

This indeed looks like an expectation and it should do, because the martingale pricing principle tells us that the value of the derivative at *t* = 0 is the discounted expected payoff at *t* = *T*, under the risk-neutral probability measure *Q*. Therefore, the second component in the integral has to be the risk-neutral probability density

$$q(S,T) = e^{A^{\dagger}(S)T} q(S,0), \qquad (14.67)$$

where *q*(*S*, 0) = δ(*S* − *S*0). If this is correct, it is also inevitable that *q*(*S*, *t*) has to satisfy the partial differential equation

$$\frac{\partial}{\partial t}q(S,t) = A^{\dagger}(S)q(S,t) = -\frac{\partial}{\partial S}rSq(S,t) + \frac{1}{2}\frac{\partial^2}{\partial S^2}\sigma^2 S^2 q(S,t). \tag{14.68}$$

This equation is known as the *Fokker–Planck*-equation and it governs the evolution of the risk-neutral probability density. Its solution is also known as the weak solution to the geometric *Brown*ian motion (14.42) with risk-neutral drift rate *r*. In the most general case of the *Feynman–Kac*-theorem 14.3, the associated *Fokker–Planck*-equation has the form

$$\frac{\partial}{\partial t}p(S,t) = -\frac{\partial}{\partial S}\mu(S,t)p(S,t) + \frac{1}{2}\frac{\partial^2}{\partial S^2}\sigma^2(S,t)p(S,t),\tag{14.69}$$

with *p*(*S*, 0) = δ(*S* − *S*0). We can now see that conditioning an expectation value on the filtration F*<sup>t</sup>* , generated by the stochastic process *S<sup>t</sup>* , corresponds to a (degenerate) probability density *p*(*S*, *t*) = δ(*S* − *St*). We can thus write a semi-general version of the *Feynman–Kac*-formula in two ways

$$V(S_t, t) = e^{-r(T-t)} E^{\mathcal{Q}} [V(S_T, T) | \mathcal{F}_t]$$
  
=  $e^{-r(T-t)} \int_0^\infty V(S, T) q(S, T) dS,$  (14.70)

with the density *q*(*S*,*T*) provided by the solution of the *Fokker–Planck*-equation, with initial condition *q*(*S*, *t*) = δ(*S* − *St*).

Let's conclude this section by calculating the weak solution to the risk-neutral geometric *Brown*ian motion

$$dS_t = rS_t dt + \sigma S_t dW_t. \tag{14.71}$$

To simplify the computation, let *x<sup>t</sup>* = log *S<sup>t</sup>* be the logarithmic price process and apply Itô's lemma

$$dx_{t} = \left(rS_{t}\frac{\partial x}{\partial S} + \frac{1}{2}\sigma^{2}S_{t}^{2}\frac{\partial^{2} x}{\partial S^{2}}\right)dt + \sigma S_{t}\frac{\partial x}{\partial S}dW_{t}$$
  
$$= \left(r - \frac{1}{2}\sigma^{2}\right)dt + \sigma dW_{t}.$$
 (14.72)

This can be integrated easily, and one obtains

$$x_{t} = x_{0} + \left(r - \frac{1}{2}\sigma^{2}\right)t + \sigma W_{t}.$$
 (14.73)

We can already see that  $x$  is normally distributed, with time-dependent expectation value and variance. The probability density function is

$$q_{x}(x,t) = \frac{1}{\sqrt{2\pi\sigma^{2}t}} \exp\left(-\frac{1}{2}\left(\frac{x - x_{0} - (r - \frac{1}{2}\sigma^{2})t}{\sigma\sqrt{t}}\right)^{2}\right). \tag{14.74}$$

It is easily checked, even though this is not a quick calculation, that  $(14.74)$  satisfies the Fokker-Planck-equation

$$\frac{\partial q_x}{\partial t} = -\left(r - \frac{1}{2}\sigma^2\right)\frac{\partial q_x}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 q_x}{\partial x^2}.\tag{14.75}$$

To express the probability density in terms of ordinary stock prices S, we use the fact that the logarithm is a monotone transformation. Thus, all infinitesimal areas under the probability densities have to coincide, and we have

$$q_x(x,t)dx = q_S(S,t)dS \quad \Leftrightarrow \quad q_S(S,t) = q_x(\log S, t)\frac{dx}{dS}.$$
 (14.76)

Thus, the weak solution to the risk-neutral geometric *Brown*ian motion is

$$q_S(S,t) = \frac{1}{S\sqrt{2\pi\sigma^2 t}} \exp\left(-\frac{1}{2}\left(\frac{\log(S/S_0) - (r - \frac{1}{2}\sigma^2)t}{\sigma\sqrt{t}}\right)^2\right),\tag{14.77}$$

for  $S \ge 0$ .

# 14.6

# Monte Carlo Simulation

There are generally two ways to use the *Feynman–Kac*-formula (14.70). Either one can use the weak solution to compute the integral numerically, or one can approximate the expectation value by an appropriate average value. The former is essentially what we will do later, when the risk-neutral probability density of more elaborate processes is not known explicitly, but only in terms of its inverse *Fourier*-transform; the latter is the domain of Monte Carlo simulation. The key equation for valuating a given contract with simulation methods is

$$V(S_t, t) = e^{-r(T-t)} E^{\mathcal{Q}}[V(S_T, T) | \mathcal{F}_t] \approx e^{-r(T-t)} \frac{1}{N} \sum_{n=1}^N V(S_T^{(n)}, T).$$
(14.78)

**311 Exotics in the Black–Scholes-Model**

This equation needs some comment. First of all, Monte Carlo simulation never generates exact results, but you can make the solution as precise as you want, if you are willing to commit enough computational resources. Second, averaging is pathwise, where in (14.78) all *N* paths start at *S<sup>t</sup>* , but because of the simulated randomness, each one will end at a different value *S* (*n*) *T* . Obviously, we need the strong (pathwise) solution of the geometric *Brown*ian motion to generate the *N* paths. More precisely, we need the strong solution of the risk-neutral version, because the expectation is under the measure *Q*. We obtain this version of course by applying the *Girsanov*-transformation to the original geometric *Brown*ian motion under *P*. We already know that the only effect of the measure change is that the drift µ is replaced by the risk-free interest rate *r*. Thus, in complete analogy to (13.12) on page 251, the required strong solution is

$$S_t = S_0 e^{(r - \frac{1}{2}\sigma^2)t + \sigma W_t}.$$
(14.79)

Because the increments of the *Wiener*-process are independent and *W*<sup>0</sup> = 0, we have

$$W_t - W_s = W_{t-s}, \t\t(14.80)$$

for 0 ≤ *s* ≤ *t*. This is most convenient, because it allows for an easy conditioning. In the situation of equation (14.78), we would write the strong solution as

$$S_T = S_t e^{(r - \frac{1}{2}\sigma^2)(T - t) + \sigma W_{T - t}}.$$
(14.81)

Recall that for computational purposes, it is often more convenient to always use standard normally distributed random variables. We can apply the old scaling trick *Wt*−*<sup>s</sup>* = √ *t* − *s Z<sup>t</sup>* , where *Z<sup>t</sup>* ∼ *N*(0, 1). That leaves us with

$$S_T = S_t e^{(r - \frac{1}{2}\sigma^2)(T - t) + \sigma\sqrt{T - t}Z_T}.$$
(14.82)

To see how valuation with Monte Carlo simulation actually works, let's return to the basic valuation problem of Example 14.1. We can use our analytic result for the value of the European plain vanilla call to assess the quality of the Monte Carlo approximation.

# **Example 14.3**

Assume that today's price of the underlying in the plain vanilla call example 14.1 is *S*0. How can this contract be valuated using Monte Carlo simulation?

#### Solution

The Monte Carlo pseudo-code is provided in Box 14.3. There is only one loop for simulating the outcome of the *N* independent paths of the risk-neutral geometric *Brown*ian motion.

........................................................................................................................

We have earlier valuated this contract numerically with the ambient parameters *r* = 5% σ= 20%, *K* = \$10, and *T*= 1 year. In order to do the same via Monte Carlo simulation,

| Box 14.3 Pseudo-code for Monte Carlo simulation of a plain vanilla call   |                                     |  |
|---------------------------------------------------------------------------|-------------------------------------|--|
| $\texttt{Set} \ N$                                                        | ⊳ Initialization                    |  |
| $b = r$                                                                   | $\triangleright$ Cost-of-carry rate |  |
| For $n = 1$ to N                                                          | Path replication                    |  |
| Draw $z \sim N(0, 1)$                                                     | Random number generation            |  |
| $S_T = S_0 \exp\left((b - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}z\right)$ |                                     |  |
| $V_T^{(n)} = \max(S_T - K, 0)$                                            | $\triangleright$ Payoff function    |  |
| $Next \ n$                                                                |                                     |  |
| $V_0 = \exp(-rT) \cdot 1/N \sum_{n=1}^{N} V_T^{(n)}$                      |                                     |  |
| $Drin+V_{-}$                                                              | $\wedge$ Nutnut                     |  |

we have additionally to specify the current price of the underlying. Let this price be  $S_0 =$  \$8. The result will be an estimate  $\hat{V}_0$  of the true but unknown price of the derivative  $V_0$ . This estimate is itself an asymptotically normally distributed random variable with moments

$$E[\hat{V}_0] = V_0 \quad \text{and} \quad \text{Var}[\hat{V}_0] = \frac{\hat{\sigma}_{V_0}^2}{N}, \tag{14.83}$$

where the sample variance  $\hat{\sigma}_{V_0}^2$  is given by

$$\hat{\sigma}_{V_0}^2 = \frac{1}{N-1} \sum_{n=1}^N \left( e^{-rT} V_T^{(n)} - \hat{V}_0 \right)^2. \tag{14.84}$$

What (14.83) tells us is that the variance goes down by a factor of N, but this also means that the standard deviation goes down only by a factor of  $\sqrt{N}$ . For illustration purposes, the simulation was conducted with  $N = 500$ ,  $N = 1000$ , and  $N = 5000$  path replications. The probability density functions of the resulting estimates are illustrated in Figure 14.8. The true value of the option, as computed from the *Black–Scholes*formula, is indicated by a vertical line. It is quite obvious that there is still a substantial amount of variability in the estimate, even if we sample 5000 paths.

Monte Carlo simulation is usually conducted with a lot more replicated paths. Additionally, variance reduction techniques like antithetic-, stratified-, and importancesampling can be used. We will not pursue this road any further, but an excellent source for background information is Glasserman (2010).

#### 14.7 **Strongly Path Dependent Contracts**

If the payoff of a derivative contract does not only depend on the path to hit a predefined barrier, but on the entire history of the path, we call it strongly path dependent.

![](_page_22_Figure_1.jpeg)

**Fig. 14.8** Monte Carlo simulation of European plain vanilla call option price  $- N = 500$ (gray),  $N = 1000$  (dashed), and  $N = 5000$  (black)

Such a contract introduces a new variable into the *Black–Scholes*-equation. To analyze the situation, define the new random process

$$I_t = \int_0^t f(S_\tau, \tau) d\tau, \tag{14.85}$$

with an appropriate function  $f(S, t)$ , collecting all the relevant path information. What information is relevant, depends on the contract itself. For a continuously averaged arithmetic Asian fixed strike call, we have  $f(S, t) = S$  and the payoff becomes

$$V(S, I, T) = \left(\frac{I}{T} - K\right)^{+}.$$
 (14.86)

But we could have far more fancy contracts. Imagine an option that pays one unit of currency per time the price of the underlying is above a certain barrier  $S_u$ . The function  $f(S, t)$ , collecting this information over the entire path, would be

$$f(S,t) = \theta(S - S_u),\tag{14.87}$$

the *Heaviside-* $\theta$ -function. How is the *Black–Scholes*-equation affected by the additional variable *I*? Again assuming a geometric *Brown*ian motion as model for the price process of the underlying, we can establish our usual hedge-portfolio and apply Itô's lemma to obtain

$$d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \frac{\partial V}{\partial I} dI + \left(\frac{\partial V}{\partial S} - \Delta\right) dS,\tag{14.88}$$

where we have arranged the equation with respect to the different increments. If we choose the hedge-ratio  $\Delta = \frac{\partial V}{\partial S}$ , the portfolio is risk-free, because from (14.85) a small change in the process  $I_t$  is given by

$$dI_t = f(S_t, t)dt. \t(14.89)$$

Thus, equating the change in the hedge-portfolio with the growth rate *r*Π*dt*, induced by the risk-free interest rate, and rearranging yields

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + f(S, t)\frac{\partial V}{\partial I} - rV = 0.$$
 (14.90)

This is a modified version of the *Black–Scholes*-PDE, which has an additional spatial dimension *I*. In counting dimensions, it is customary to only count the spatial dimensions and so we have a two-dimensional problem. In principle, such a problem can be solved by finite difference methods in a three-dimensional lattice. A collection of appropriate schemes can be found in Wilmott (2006c, chap. 79). But generally, the higher the dimension of the problem, the less appropriate finite difference methods are, because they become exceedingly computationally demanding. We will therefore use Monte Carlo simulation, if the problem is not one-dimensional.

Probably the most prominent examples in the class of strongly path dependent contracts are Asian options. We already learned some characterizations of those contracts in Chapter 12. So let's start our discussion with a surprise. For the continuously averaged geometric fixed strike option with European exercise right, there exists a generalized closed form solution (Kemna and Vorst, 1990). The price of such an Asian call, when written at *t* = 0, is

$$C_0^{\mathbb{Y}}(K,T,S_0) = e^{(b_{\text{adj.}}-r)T} S_0 \Phi(d_+) - e^{-rT} K \Phi(d_-), \tag{14.91}$$

with

$$d_{+/-} = \frac{\log(S_0/K) + (b_{\text{adj.}} \pm \frac{1}{2}\sigma_{\text{adj.}}^2)T}{\sigma_{\text{adj.}}\sqrt{T}}, \ b_{\text{adj.}} = \frac{1}{2}\left(b - \frac{\sigma^2}{6}\right), \text{ and } \ \sigma_{\text{adj.}} = \frac{\sigma}{\sqrt{3}}. \tag{14.92}$$

For a later time *t* in the life of the contract, the formulas for the fair price *V* U *t* ( *K*,*T*, *S*¯ *t* ) become more complex but nevertheless remain completely analytic (see for example Wilmott, 2006b, sect. 25.11). The lucky coincidence that makes this work is that the geometric average of a log-normal distributed random variable is also log-normal distributed. The price for the geometric average fixed strike put is

$$P_0^{\mathbb{X}}(K,T,S_0) = -e^{(b_{\text{adj.}}-r)T}S_0\Phi(-d_+) + e^{-rT}K\Phi(-d_-),\tag{14.93}$$

with *d*+/<sup>−</sup>, *b*adj., and σadj. as in (14.92). That is how far analytical computations will carry us. From here on, we have to completely rely on numerical approximations. So let's start by approximating an individual path of our standard risk-neutral geometric *Brown*ian motion. Such a path *S<sup>t</sup>* for 0 ≤ *t* ≤*T* is a (almost surely) continuous function

#### **315 Exotics in the Black–Scholes-Model**

of the state variable ω∈ Ω. But that does not help much for any computational purpose. So let's discretize it by

$$S_{t+\Delta t} = S_t e^{(r-\frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}Z_{t+\Delta t}},\tag{14.94}$$

where again *Z<sup>t</sup>* is assumed independently standard normally distributed, *Z<sup>t</sup>* ∼ *N*(0, 1). Once we have chosen ∆*t*, we can represent the continuous path by the sequence of discrete values *Sm*∆*<sup>t</sup>* for *m* = 0, . . . , *M* = *T* ∆*t* . That is indeed all we need to run a simulation based numerical pricing algorithm.

### **Example 14.4**

Suppose a fixed strike arithmetic Asian call option with European exercise right has strike price *K* and expiry date *T*. The current price *S*<sup>0</sup> and annual volatility σ of the underlying is known, also the risk-free interest rate *r*. The underlying pays no dividend. How can this contract be valuated?

#### Solution

The pseudo-code for this problem is provided in Box 14.4. The only additional fragments are due to the discretization of the path and the computation of the arithmetic average. ........................................................................................................................

From the pseudo-code in Box 14.4 it is obvious that it is hard to make mistakes in setting up a simple Monte Carlo pricing algorithm. This is an important aspect, because

| Box 14.4<br>Pseudo-code for fixed strike arithmetic Asian call                 |                            |  |  |
|--------------------------------------------------------------------------------|----------------------------|--|--|
| Set<br>N,<br>M                                                                 | ◃ Initialization           |  |  |
| b = r                                                                          | ◃ Cost-of-carry rate       |  |  |
| ∆t = T/M                                                                       |                            |  |  |
| For<br>n = 1 to<br>N                                                           | ◃ Path replication         |  |  |
| For<br>m = 1 to<br>M                                                           | ◃ Path discretization      |  |  |
| z ∼<br>Draw<br>N(0,<br>1)                                                      | ◃ Random number generation |  |  |
| √<br>exp ((<br>∆t z)<br>1<br>b −<br>2<br>= Sm−1<br>σ<br>∆t + σ<br>Sm<br>)<br>2 |                            |  |  |
| Next<br>m                                                                      |                            |  |  |
| S¯<br>∑M<br>T = 1/(M<br>+ 1)<br>m=0 Sm                                         | ◃ Arithmetic average       |  |  |
| S¯<br>(n)<br>T −<br>= max (<br>K,<br>V<br>0<br>)<br>T                          | ◃ Payoff function          |  |  |
| Next<br>n                                                                      |                            |  |  |
| (n)<br>∑N<br>= exp (−rT)<br>·<br>1/N<br>V0<br>n=1 V<br>T                       |                            |  |  |
| Print<br>V0                                                                    | ◃ Output                   |  |  |

often there is no way to check against analytical references in order to see, if there is an error in the code.

Of course we can have additional barrier conditions within an Asian option. Assume the contract in Example 14.4 would have expired worthlessly, if the underlying had hit the lower knockout barrier *S<sup>l</sup>* during the lifetime of the contract. Then we would have only to insert the fragment

If min ( *S*0, . . . , *S<sup>M</sup>* ) ≤ *S<sup>l</sup>* then *V* (*n*) *T* = 0

immediately below the payoff function. You might suspect that we could have valuated barrier options as well via Monte Carlo simulation and that is correct. But since barrier type contracts are so well suited to finite difference schemes, it would have been inefficient. On the other hand American options cannot be dealt with easily in a simulation framework. The reason is that we have to determine the early exercise boundary, as we are progressing backwards in time. But Monte Carlo simulation is a purely forward progressing scheme. There are workarounds like the method of Longstaff and Schwartz (2001) to be discussed in the next section, but valuation of high-dimensional contracts with American exercise right are the most challenging problems in quantitative finance.

There is another common path dependent option type called a lookback option. This kind of option is the dream of every trader, because its payoff depends on the minimum or maximum price of the underlying during the lifetime of the contract. It generally comes in two flavors (fixed and floating):

#### **Strike type**

• Fixed strike: The exercise price is fixed and not affected by the path of the underlying. The payoffs are

$$\overleftarrow{C}(K, T, S_{\text{max}}) = (S_{\text{max}} - K)^{+}$$
 and  $\overleftarrow{P}(K, T, S_{\text{min}}) = (K - S_{\text{min}})^{+},$ 

where *S*max and *S*min are the maximum and minimum prices of the underlying over the lifetime of the contract.

• Floating strike: The exercise price itself is given by the maximum *S*max or the minimum *S*min of the path of the underlying, respectively. The payoffs are

$$\overleftarrow{C}(S_{\min}, T) = S_T - S_{\min}$$
 and  $\overleftarrow{P}(S_{\max}, T) = S_{\max} - S_T$ .

The path dependence of the lookback option is very clear. It is thus very surprising that explicit formulas exist in the *Black–Scholes*-framework. For the floating strike case they are due to Goldman et al. (1979), and for the fixed strike due to Conze and Viswanathan (1991). The formulas are a little bulky and therefore the reader is referred to Haug (2007, sect. 4.15), where also additional versions of the lookback option can be found. Of course nothing prevents us from valuating a lookback option numerically.

**Quick calculation 14.6** How is the pseudo-code in Box 14.4 to be modified, to valuate a European fixed strike lookback call?

# Valuating American Contracts with Monte Carlo

Higher-dimensional contracts can be equipped with American exercise right as well. The problem with this is that we are used to pricing such contracts by Monte Carlo simulation, which builds a path from many small simulated increments. The point is that this construction progresses forward in time. We cannot simulate the path backwards, because we only know the price of the underlying today, not at expiry. To determine the optimal exercise strategy, and hence the fair price of an American contract, we have to compute the *Snell*-envelope, which has to be done recursively backwards in time. If today is time  $t = 0$  and the contract under consideration expires at  $t = T$ , then the *Snell*-envelope is computed by

$$X_{t} = \begin{cases} e^{-rT} V_{T} & \text{for } t = T\\ \max\left(e^{-rt} V_{t}, E^{\mathcal{Q}}[X_{t+\Delta t}|\mathcal{F}_{t}]\right) & \text{for } t < T, \end{cases} \tag{14.95}$$

with  $V_t$  denoting the intrinsic value of the contract at time t. Of course we have assumed implicitly in (14.95) that all paths are simulated in discrete time steps of length  $\Delta t$ . The problem is now very clear. For any given path we obtained by simulation, we have to work backwards in  $\Delta t$ -steps from  $t = T$  to  $t = 0$  to determine the *Snell*-envelope. But in the process, at every time  $t < T$  we need the conditional expectation  $E^Q[X_{t+\Delta t}|\mathcal{F}_t]$ . We could of course try to approximate it by again forward simulating paths, but note that the expectation has to cover all possible early exercise events of those new paths as well. So this strategy becomes unmanageable very rapidly from a computational point of view.

The idea of Longstaff and Schwartz (2001) is both simple and brilliant. They suggest to generate the required paths independently by simulation and afterwards use crosssectional information to approximate the required conditional expectation values. To be more precise, they approximate the expectation value at time  $t$  by least-squares regression from all paths that are in the money at that time. The resulting approach is called LSM-algorithm (least-squares Monte Carlo) and is best understood by looking at a simplified numerical example.

#### Example 14.5

Based on the example in Longstaff and Schwartz (2001, sect. 1), valuate an American put option on a non dividend paying stock with current price  $S_0 = 100$ , exercise price  $K = 110$ , time to expiry  $T = 3$  years, and annual risk-free interest rate  $r = 6\%$ . Assume that  $\Delta t = 1$  year and the option is exercisable at times  $t = 1, 2, 3$ . A total of  $N = 8$  simulated paths under the risk-neutral measure Q is provided in Table 14.2.

#### LSM-Algorithm

The first step is to compute the *Snell*-envelope at expiry

$$X_3 = e^{-3r}(K - S_3)^+$$

14.8

| <b>Table 14.2</b> Simulated paths of $S_t$ |       |       |         |         |
|--------------------------------------------|-------|-------|---------|---------|
| Path $\omega_n$                            | $t=0$ | $t=1$ | $t = 2$ | $t = 3$ |
| 1                                          | 100   | 109   | 108     | 134     |
| 2                                          | 100   | 116   | 126     | 154     |
| 3                                          | 100   | 122   | 107     | 103     |
| 4                                          | 100   | 93    | 97      | 92      |
| 5                                          | 100   | 111   | 156     | 152     |
| 6                                          | 100   | 76    | 77      | 90      |
| 7                                          | 100   | 92    | 84      | 101     |
| 8                                          | 100   | 88    | 122     | 134     |

for every path  $\omega_n$ . The result is given in Table 14.3. These cashflows are the pathwise present values of a European put option. If the option is in the money at time  $t = 2$ , the holder has to make the decision whether or not to exercise it immediately or to hold it until  $t = 3$ . To make the right decision, she requires knowledge of the conditional expectation  $E^{\mathcal{Q}}[X_3|\mathcal{F}_2]$ . This expectation value can be approximated by least-squares regression. The key idea is to formulate a stochastic model of the form

$$X_{t+1} = \sum_{k=0}^{K} \beta_k S_t^k + \epsilon_{t+1}.$$

Note that even though powers of  $S_t$  are involved, the stochastic model is still linear in its coefficients. That means one can easily obtain the least-squares estimator

$$\hat{\beta}\rangle = \begin{pmatrix} \hat{\beta}_0 \ \vdots \ \hat{\beta}_K \end{pmatrix}$$

as already elaborated in Chapter 7. In the present example,  $K = 2$  was chosen and the realizations of the response variable and the regressors are provided in Table 14.4. Only paths that are in the money at  $t = 2$  are considered in the regression, because only in

| <b>Table 14.3</b> Snell-envelope at $t = 3$ |       |       |       |
|---------------------------------------------|-------|-------|-------|
| Path $\omega_n$                             | $t=1$ | $t=2$ | $t=3$ |
| 1                                           |       |       | 0     |
| 2                                           |       |       | 0     |
| 3                                           |       |       | 5.85  |
| 4                                           |       |       | 15.03 |
| 5                                           |       |       | 0     |
| 6                                           |       |       | 16.71 |
| 7                                           |       |       | 7.52  |
| 8                                           |       |       |       |

| Table 14.4<br>Regression at time<br>t =<br>2 |       |     |             |
|----------------------------------------------|-------|-----|-------------|
| Path ωn                                      | X3    | S2  | 2<br>S<br>2 |
| 1                                            | 0     | 108 | 11 664      |
| 2                                            | –     | –   | –           |
| 3                                            | 5.85  | 107 | 11 449      |
| 4                                            | 15.03 | 97  | 9 409       |
| 5                                            | –     | –   | –           |
| 6                                            | 16.71 | 77  | 5 929       |
| 7                                            | 7.52  | 84  | 7 056       |
| 8                                            | –     | –   | –           |

those states of the world, does the holder have to make an exercise decision at that time. It is not prohibited to include all paths in the regression, but Longstaff and Schwartz found that in this case more regressors are needed to obtain accurate results. In the current regression model for *t* = 2, one obtains

$$E^{\mathcal{Q}}[\hat{X}_3|\mathcal{F}_2] = -94.665 + 2.641 \cdot S_2 - 0.016 \cdot S_2^2.$$

This quantity is the least-squares estimator for the conditional expectation *E <sup>Q</sup>*[*X*3|F2] and is used as a proxy in the early exercise decision. All required information for this decision at *t* = 2 is now available. The discounted intrinsic values from early exercise and the conditional expectation proxies from least-squares regression are summarized in Table 14.5. From this, one can now easily compute the *Snell*-envelope at *t* = 2; see Table 14.6.

The entries in the last two tables require some explanation. First of all, all values *X* (*n*) 2 , resulting from early exercise, are identified by a star. That has happened in paths 4, 6, and 7. But take a closer look at those paths with negative exercise decision. In path 1, the option is not exercised at *t* = 2, even though it is now in the money and its discounted exercise value is \$1.77. That is because the exercise decision is based on comparing the discounted intrinsic value and the conditional expectation of *X*ˆ <sup>3</sup>. The optimal strategy in this case is not to exercise the option early. Of course the terminal

| Table 14.5 | t =<br>Exercise decision at<br>2 |                            |  |
|------------|----------------------------------|----------------------------|--|
| Path ωn    | −2r<br>(K −<br>S2)<br>e          | Xˆ<br>Q[<br>3 F2<br>E<br>] |  |
| 1          | 1.77                             | 3.94                       |  |
| 2          | –                                | –                          |  |
| 3          | 2.66                             | 4.74                       |  |
| 4          | 11.53                            | 10.97                      |  |
| 5          | –                                | –                          |  |
| 6          | 29.27                            | 13.83                      |  |
| 7          | 23.06                            | 14.28                      |  |
| 8          | –                                | –                          |  |

|         | Table 14.6<br>Snell-envelope at<br>t =<br>2 |        |       |
|---------|---------------------------------------------|--------|-------|
| Path ωn | t = 1                                       | t = 2  | t = 3 |
| 1       | –                                           | 0      | 0     |
| 2       | –                                           | 0      | 0     |
| 3       | –                                           | 5.85   | 5.85  |
| 4       | –                                           | 11.53∗ | 15.03 |
| 5       | –                                           | 0      | 0     |
| 6       | –                                           | 29.27∗ | 16.71 |
| 7       | –                                           | 23.06∗ | 7.52  |
| 8       | –                                           | 0      | 0     |

intrinsic value in this path vanishes, so that it had better been exercised at *t* = 2, but this information is not available to the decision maker at that point, because it is not contained in F2. Only the omniscient observer, running the simulation, knows that. In path 3, the option is also not exercised early, which means the cashflow is still obtained at *t* = 3 and thus, its present value is unchanged. Unlike in path 1, this exercise decision is optimal from both points of view, the one of the option holder, as well as the one of the spectator with complete knowledge.

It is worthwhile to stop for a minute and go back to the binomial model of Chapter 12, in order to understand how the exercise decision is made and the continuation value is generated in the LSM-approach. There is a fundamental difference in the architecture of binomial models and Monte Carlo simulated paths regarding the way they fill the space of potential realizations of the price process of the underlying; see Figure 14.9. In particular, in the binomial model, every node has two successors, and the space of potential prices is swept out systematically. Systematically here means that ascending nodes in every time slice represent ascending prices of the underlying. In a set of simulated paths, every node, except for the zeroth, has only one successor and the paths fill the space of potential prices randomly. These differences have severe implications for the way the early exercise decision is made and the continuation value of

![](_page_29_Figure_4.jpeg)

**Fig. 14.9** Organization of nodes and edges – Binomial tree (left) and Monte Carlo simulation (right)

| <b>Table 14.7</b> Regression at time $t = 1$ |       |       |         |
|----------------------------------------------|-------|-------|---------|
| Path $\omega_n$                              | $X_2$ | $S_1$ | $S_1^2$ |
| 1                                            | 0     | 109   | 11881   |
| 2                                            |       |       |         |
| 3                                            |       |       |         |
| 4                                            | 11.53 | 93    | 8649    |
| 5                                            |       |       |         |
| 6                                            | 29.27 | 76    | 5776    |
| 7                                            | 23.06 | 92    | 8464    |
| 8                                            | 0     | 88    | 7744    |

the option is generated. For both types of schemes, the *Snell*-envelope in an arbitrary branch has to satisfy

$$X_{t}^{(n)} = \begin{cases} e^{-rt}(K - S_{t}^{(n)}) & \text{if option is exercised} \\ E^{Q}[X_{t+1}|\mathcal{F}_{t}] & \text{if option is continued} \end{cases}$$

for  $t < T$ . In the binomial model, the exercise decision is made by directly comparing the discounted value of immediate exercise and the continuation value

$$E^{Q}[X_{t+1}|\mathcal{F}_{t}] = q \cdot X_{t+1}^{(n+1)} + (1-q) \cdot X_{t+1}^{(n)},$$

where  $q$  is the risk-neutral probability for entering the upper branch. That is possible, because the binomial tree is organized systematically. A simulated mesh is not organized that way, and hence the LSM-algorithm uses the proxy  $E^{\mathcal{Q}}[\hat{X}_{t+1}|\mathcal{F}_t]$  for the exercise decision. Because simulated paths do not branch out, the subsequent node is attained with probability one for  $0 < t < T$ , and thus the continuation value is

$$E^{Q}[X_{t+1}|\mathcal{F}_{t}] = X_{t+1}^{(n)}$$

That is the reason why in Table 14.6 the terminal value of the *Snell*-envelope is unchanged in all paths, where no early exercise occurs.

Continuing the original example, the next step is to pick out the in-the-money paths at time  $t = 1$  and to regress them on  $X_2$ ; see Table 14.7. The result of the least-squares estimation is

$$E^{\mathcal{Q}}[\hat{X}_2|\mathcal{F}_1] = 191.917 - 3.142 \cdot S_1 + 0.013 \cdot S_1^2.$$

Now all necessary information for the exercise decision at  $t = 1$  is available and is summarized in Table 14.8. With exception of path 1, the option is exercised early in all paths that are in the money at time  $t = 1$ . One can thus finally compute the entire *Snell*envelope; see Table 14.9. Early exercise is again indicated by a star and occurs in paths 4, 6, 7, and 8 at  $t = 1$ . Take a closer look at path number 7. In this path, early exercise is recommended at two times, which means  $\tau = 1$  and  $\tau = 2$  are stopping times. Obviously

| <b>Table 14.8</b> Exercise decision at $t = 1$ |                 |                                            |  |
|------------------------------------------------|-----------------|--------------------------------------------|--|
| Path $\omega_n$                                | $e^{-r}(K-S_1)$ | $E^{\mathcal{Q}}[\hat{X}_2 \mathcal{F}_1]$ |  |
|                                                | 0.94            | 3.89                                       |  |
| 2                                              |                 |                                            |  |
| 3                                              |                 |                                            |  |
| 4                                              | 16.01           | 12.15                                      |  |
| 5                                              |                 |                                            |  |
| 6                                              | 32.02           | 28.21                                      |  |
| 7                                              | 16.95           | 12.89                                      |  |
| 8                                              | 20.72           | 16.09                                      |  |
|                                                |                 |                                            |  |

the discounted value of the option is larger, if exercised at  $t = 2$ . Nevertheless, the optimal exercise policy for an American option is associated with the smallest stopping time

$$\tau^* = \inf \{ t \in \mathcal{T} : X_t = e^{-rt} (K - S_t)^+ \}.$$

Again, defining the stopped process  $Y_t$  by

$$Y_t = \begin{cases} X_t & \text{if } t < \tau^* \\ X_{\tau^*} & \text{if } t \ge \tau^* \end{cases}$$

as in Equation (12.53) on page 238, one can easily approximate the value of the American put option by

$$Y_0 = E^{\mathcal{Q}}[Y_3|\mathcal{F}_0] \approx \frac{1}{N} \sum_{n=1}^N Y_3^{(n)} = 11.44,$$

because  $Y_t$  is a Q-martingale. On the other hand, the price of the corresponding European put option can be obtained from the terminal expectation value of  $X$ ,

$$E^{\mathcal{Q}}[X_3|\mathcal{F}_0] \approx \frac{1}{N} \sum_{n=1}^N X_3^{(n)} = 5.64.$$

| Table 14.9 <i>Snell</i> -envelope at $t = 1$ |           |       |       |
|----------------------------------------------|-----------|-------|-------|
| Path $\omega_n$                              | $t=1$     | $t=2$ | $t=3$ |
| 1                                            | 0         | 0     | 0     |
| 2                                            | 0         | 0     | 0     |
| 3                                            | 5.85      | 5.85  | 5.85  |
| 4                                            | $16.01*$  | 11.53 | 15.03 |
| 5                                            | 0         | 0     | 0     |
| 6                                            | $32.02*$  | 29.27 | 16.71 |
| 7                                            | $16.95^*$ | 23.06 | 7.52  |
| 8                                            | $20.72*$  |       |       |

#### Fxotics in the Black-Scholes-Model

Thus, the right to exercise the option at any time during its lifetime adds substantial value to the contract.

Of course a simple plain vanilla American put option can be valued more efficiently by finite difference methods. But an Asian option with American exercise right would make a perfect candidate for the LSM-algorithm. Its value does not depend exclusively on the price process  $S_t$ , but also on the integrated process  $I_t$ . Thus, in conducting a leastsquares regression up to quadratic order to make the appropriate exercise decision at time  $t$ , one would use the stochastic model

$$X_{t+1} = \beta_0 + \beta_1 S_t + \beta_2 I_t + \beta_3 S_t^2 + \beta_4 S_t I_t + \beta_5 I_t^2 + \epsilon_{t+1}.$$
 (14.96)

There is generally no limit to the order of the polynomials or the number of variables to be included in (14.96), as long as there are enough simulated in-the-money paths to conduct least-squares estimation. Longstaff and Schwartz (2001) even suggest to use orthogonal basis functions as regressors instead of simple powers. In particular they used *Laguerre*-polynomials, which are orthogonal with respect to the weight function  $e^{-x}$  in the domain  $\mathbb{R}^+_{0}$ . However, their results indicate that the functional form of the regressors is circumstantial.

### 14.9

# **Further Reading**

A gentle introduction to exotic contracts is Hull (2009, chap. 24). An accessible and very well written treatment of the subject is Wilmott (2006b, part 2). For a comprehensive collection of analytical formulas see Haug  $(2007)$ . Finite difference schemes frequently used in financial engineering are introduced in Wilmott (2006c, part 6). An authority for Monte Carlo simulation in finance is Glasserman (2010). Girsanov's theorem, generators, and the *Feynman–Kac*-formula are treated in a very comprehensible way in Neftci (2000, chap. 14 & 21). For a more rigorous discussion of the Girsanovtransformation see Shiryaev (1999, sect. 7.3b). The connection between path integrals and derivatives is discussed in Baaquie (2004, chap. 5). For Monte Carlo valuation of American options see Glasserman (2010, chap. 8) and the original paper of Longstaff and Schwartz (2001).

# 14.10

### Problems

**14.1** Suppose instead of  $(14.16)$  on page 294, we had chosen the scheme

$$V_{m+1}^{(n)} = V_m^{(n)} + \Delta \tau \left( b n \Delta S \cdot \Delta_m^{(n)} + \frac{1}{2} \sigma^2 n^2 \Delta S^2 \cdot \Gamma_m^{(n)} - r V_{m+1}^{(n)} \right)$$

where the last term in parenthesis is with respect to time  $\tau = (m+1)\Delta\tau$ . Prove that this scheme is still explicit and use a martingale argument to show that the stability condition  $(14.23)$  on page 295, as well as the additional condition

 $\sigma^2 n > h$ 

have to hold, in order for the scheme to be consistent.

- **14.2** A power option is a contract, whose value depends on the payoff  $V(S, T)$ , with  $S = S^{\alpha}$ . Show that the generalized *Black–Scholes*-equation can be expressed in terms of S, with adjusted cost-of-carry rate  $b_{\text{adi}}$  and volatility  $\sigma_{\text{adi}}$ .
- **14.3** Suppose the underlying S follows the standard geometric *Brownian* motion

$$dS_t = \mu S_t dt + \sigma S_t dW_t.$$

Use the associated *Fokker–Planck*-equation, together with the definition of the probability current

$$F(S,t) = \left(\mu S - \frac{1}{2}\frac{\partial}{\partial S}\sigma^2 S^2\right) p(S,t),$$

to prove that the probability mass is conserved over time,

$$\frac{\partial}{\partial t} \int_0^\infty p(S, t) dS = \int_0^\infty \frac{\partial}{\partial t} p(S, t) dS = 0.$$

Assume that the probability density function  $p(S, t)$  is a sufficiently rapid decreasing function, which is true.

**14.4** Monte Carlo simulation approximates an unknown expectation value by an arithmetic mean, computed from a random sample. This mean can be understood as the expectation value with respect to the estimated probability density

$$\hat{f}(x) = \frac{1}{N} \sum_{n=1}^{N} \delta(x - x^{(n)}).$$

Show that for an arbitrary function  $h(x)$ , the arithmetic mean

$$\hat{h} = \frac{1}{N} \sum_{n=1}^{N} h(x^{(n)})$$

is the exact expectation value with respect to  $\hat{f}(x)$ , and that  $\hat{f}(x)$  itself is an unbiased estimator for the true density  $f(x)$ .

**14.5** An important variance reduction technique in Monte Carlo simulation is importance sampling. The idea behind this concept is to approximate an expectation by a weighted average value

$$\hat{h} = \sum_{n=1}^{N} w_n h(x^{(n)}),$$

where the normalized weights are proportional to the so-called likelihood ratio

$$w_n \propto \frac{f(x^{(n)})}{N \cdot g(x^{(n)})}$$
 and  $\sum_{n=1}^N w_n = 1$ ,

and the sampling is conducted with respect to the importance density *g*(*x*), not the original density *f* (*x*). Show that the expectation of ˆ*h* is still unbiased.

**14.6** A continuously exponential averaged arithmetic Asian option is a contract, where the average price of the underlying is computed as

$$\bar{S}_t = e^{-\lambda t} S_0 + \lambda \int_0^t e^{-\lambda(t-\tau)} S_\tau d\tau.$$

The parameter λ ≥ 0 is an arbitrary weight factor. Rewrite the averaging condition in differential form and explain the effect of the parameter λ.

**14.7** Consider a floating strike version of an exponential arithmetic Asian call (Problem 14.6) with European exercise right, contingent on a forward contract with *T<sup>F</sup>* > *T*. Assume that *S*0,*T*,*r*, σ, and λ are known. Additionally, the option is knocked out, if *ST*/<sup>2</sup> ≤ *S*¯ *<sup>T</sup>*/<sup>2</sup> holds. Create a pseudo-code algorithm to valuate this contract at time *t* = 0.
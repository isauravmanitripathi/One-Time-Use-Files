# **Method of Lines**

The complexity of a partial differential equation (PDE) grows with the number of independent variables. In applied mathematics, the *method of lines* (MoL) is frequently used to reduce the number of independent variables by one. For this reduction, one has to pay a price, which is twofold:

- 1. A *system* of several dependent variables arises.
- 2. The system is an approximation—that is, a discretization error is introduced.

In finance, the method of lines is applied to the Black–Scholes PDE, which involves two independent variables, namely, time *t* and price *S* of the underlying asset. The continuous domain is the *half strip* 0 ≤ *t* ≤ *T* , *S >* 0, where *T* denotes the time to maturity. Introducing the backward running time *τ* := *T* − *t*, the Black–Scholes equation is

$$-\frac{\partial V(S,\tau)}{\partial \tau} + \mathcal{L}_{\text{BS}}(V(S,\tau)) = 0 \text{ with}$$
  
$$\mathcal{L}_{\text{BS}}(V(S,\tau)) := \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - \delta)S\frac{\partial V}{\partial S} - rV$$
 (1)

Here, the dependent variable *V (S, τ )* denotes the value function of a vanilla American put option, *r* is the risk-free interest rate, *δ* denotes a constant dividend yield, and *σ* the volatility (*see* **Options: Basic Definitions**). According to the Black–Scholes model, *r, σ, δ* are taken as constants. For a put option of the American style with strike *K*, the payoff at time *T* is

$$(K - S)^{+} := \max(K - S, 0) \tag{2}$$

The initially unknown early exercise curve *Sf* separates the half strip into two parts: stopping region *S* ≤ *Sf* , where *V* equals the payoff, and the continuation region, where *V* solves the Black–Scholes equation:

$$V = (K - S)^{+} \text{ for } S \leq S_{f}$$
  
V solves equation (1) for  $S > S_{f}$  (3)

The geometry of the domain is illustrated in Figure 1.

Since equation (1) depends on two independent variables, MoL leads to a system with only one independent variable—that is, to a system of ordinary differential equations (ODEs). For introducing "lines" in our context, we have two possibilities: either we set up lines parallel to the *t*-axis or we work with lines parallel to the *S*-axis. The former approach leads to a fully numerical method; it is described in Exercise 4.10 of [6]. Our focus is on the latter MoL approach, with lines parallel to the *S*-axis. This approach (which goes back to [3]) is attractive because the resulting ODEs can be solved analytically.

# **Semidiscretization**

The method of lines replaces the half strip by a set of equidistant lines, each line defined by a constant value of *τ* . To this end, the interval 0 ≤ *τ* ≤ *T* is discretized into *n* subintervals by

$$\tau_{\nu} := \nu \Delta \tau, \quad \Delta \tau := T/n, \quad \nu = 1, \dots, n-1 \tag{4}$$

(Figure 1). On this discrete set of lines, the partial derivative *∂V /∂τ* is approximated by the difference quotient

$$\frac{V(S,\tau) - V(S,\tau - \Delta \tau)}{\Delta \tau} \tag{5}$$

This gives a semidiscretized version of equation (1), namely, for each *τν* the ODE

$$w(S, \tau - \Delta \tau) - w(S, \tau) + \Delta \tau \mathcal{L}_{\text{BS}}(w(S, \tau)) = 0$$
(6)

which holds for *S* ≥ *Sf* . Here, we use the notation *w* rather than *V* to indicate that a discretization error is involved. As this semidiscretized version of equation (6) is applied for each of the parallel lines, *τ* = *τν* , *ν* = 1*,...,n* − 1, a coupled system of ODEs is derived.

# **Analytic Solution**

Substituting equation (1) into equation (6) gives the equation to be solved for each line *τν*

$$\frac{1}{2}\Delta\tau\,\sigma^2S^2\frac{\partial^2 w}{\partial S^2} + \Delta\tau\,(r-\delta)S\frac{\partial w}{\partial S} - (1+r\,\Delta\tau)w$$
$$= -w(S,\,\tau_{\nu-1})\tag{7}$$

![](_page_1_Figure_1.jpeg)

Figure 1 Method of lines applied to an American-style vanilla put

where the argument of  $w$  on the left-hand side is  $(S, \tau_{v})$ . This is a second-order ODE for  $w(S, \tau_{v})$ , with boundary conditions for  $S_f(\tau_v)$  and  $S \to \infty$ . For any line  $\tau = \tau_{\nu}$ , the function  $w(S, \tau_{\nu-1})$  of the righthand side is known from the previous line, starting from the known payoff for  $\tau = 0$ . The right-hand function  $q(S) := -w(S, \tau_{\nu-1})$  is an inhomogeneous term of the ODE.

The analytic solution exploits that the equation  $(7)$ is linear in  $w$  and of the simple type of an inhomogeneous Euler equation

$$\alpha S^2 w'' + \beta S w' + \gamma w = q(S)$$
  
with  $\alpha = \frac{1}{2} \Delta \tau \sigma^2$ ,  $\beta = (r - \delta) \Delta \tau$ , (8)  
 $\gamma = -(1 + r \Delta \tau)$ 

where the prime denotes differentiation with respect to  $S$ . The solution method for such a simple type of ODE is standard and found in any ODE text book. It is based on substituting  $S^{\lambda}$  into the homogeneous ODE ( $q \equiv 0$ ). This yields a quadratic equation with zeros

$$\lambda_{1,2} := \frac{1}{2} - \frac{r - \delta}{\sigma^2}$$
$$\pm \sqrt{\left(\frac{1}{2} - \frac{r - \delta}{\sigma^2}\right)^2 + \frac{2(1 + r\Delta\tau)}{\sigma^2 \Delta\tau}} \quad (9)$$

Solutions to the homogeneous ODE are obtained by linear combinations of the  $S^{\lambda}$ ,

$$aS^{\lambda_1} + bS^{\lambda_2} \tag{10}$$

for suitable constants  $a$  and  $b$ . A solution of the inhomogeneous equation is added. Note that this analytical solution avoids a truncation error in Sdirection.

#### **Matching Solution Parts**

In our context, we need (at least) two such solutions for every line, because the inhomogeneous terms change. The early exercise curve  $S_f$  separates each of the parallel lines into two parts (Figure 2). As for the previous line  $\tau_{\nu-1}$ , the separation point lies more "on the right" (recall that for a put the curve  $S_f(\tau)$  is monotonically decreasing for growing  $\tau$ ), the inhomogeneous term  $w(\cdot, \tau_{\nu-1})$  consists of (at least) two parts as well, but separated differently. Neglecting for a moment the previous history of lines  $\tau_{\nu-2}, \tau_{\nu-3}, \ldots$ , the analytic solution of equation (7) for  $\tau_{\nu}$  consists of three parts, defined on the three subintervals

A: 
$$0 < S \leq S_f(\tau_{\nu})$$
  
B:  $S_f(\tau_{\nu}) < S \leq S_f(\tau_{\nu-1})$  (11)  
C:  $S_f(\tau_{\nu-1}) < S$ 

![](_page_1_Figure_15.jpeg)

**Figure 2** Detail of Figure 1, situation along line  $\tau_{\nu}$ : A: solution is given by payoff; B: inhomogeneous term of differential equation given by payoff; and C: inhomogeneous term given by  $-w(., \tau_{\nu-1})$ 

On the left-hand interval A,  $w$  equals the payoff; nothing needs to be calculated. For the middle interval B, the inhomogeneous term  $-w(., \tau_{v-1})$  is given by the payoff,  $q(S) = -(K - S)$ . As we need solutions for both subintervals B and C, a second pair of constants is required for C. In this subinterval, the value of a put vanishes for  $S \rightarrow \infty$ , which contradicts  $\lambda_1 > 0$ ; the root  $\lambda_1$  drops out for the solution part in C. Hence, this solution is of the type  $cS^{\lambda_2}$  for a constant c. When we consider the dependence on previous lines, then we realize that there are recursively several B-type subintervals, and only one C-type interval for  $S > S_f(\tau_0) = K$ . To illustrate this, merge Figures 1 and 2. For  $S_f(\tau_0) = K$ to hold, assume in addition  $\delta < r$  for a put ( $\delta > r$  for a call).

## **First Line**

Let us discuss for the first line  $\nu = 1$  how the solution is setup. For this exposition, we take specifically  $\delta = 0$ . For  $\nu = 1$ , we have  $S_f(\tau_{\nu-1}) = K$  and  $q =$  $w(S, \tau_{\nu-1}) = 0$  for  $S > K$ . Hence, in subinterval C the inhomogeneous solution is 0. And  $q = S - K$  for  $S_f(\tau_1) < S < K$ , hence

$$\frac{K}{1+r\,\Delta\tau} - S\tag{12}$$

solves the inhomogeneous equation for subinterval B. This leads to the three parts of the solution along the first line  $\tau = \tau_1$ 

$$w(S; \tau_1) = K - S \quad \text{for A}$$
  
$$w(S; \tau_1) = \frac{K}{1 + r \Delta \tau} - S + a^{(1)} S^{\lambda_1} + b^{(1)} S^{\lambda_2} \quad \text{for B}$$
  
$$w(S; \tau_1) = c^{(1)} S^{\lambda_2} \quad \text{for C}$$
 (13)

The value of  $S_f(\tau_1)$  is still undetermined as well as the three constants  $a^{(1)}, b^{(1)}$  and  $c^{(1)}$ . To determine these four parameters, we require four equations.

The unknown separation point  $S_f(\tau_v)$  is fixed by the high-contact conditions

$$V(S_f, \tau) = K - S_f, \quad \frac{\partial V(S_f, \tau)}{\partial S} = -1 \quad (14)$$

This is applied to the approximation  $w$  as well. Two remaining conditions are given by the requirement that both  $w$  and  $dw/dS$  are continuous at the matching point  $S_f(\tau_{\nu-1})$ . This fixes all variables. For the first line, the four equations for the parameters are (with  $E := S_f(\tau_1)$ )

$$\frac{K}{1+r \ \Delta \tau} - E + a^{(1)}E^{\lambda_1} + b^{(1)}E^{\lambda_2} = K - E \tag{15}$$

$$-1 + \lambda_1 a^{(1)} E^{\lambda_1 - 1} + \lambda_2 b^{(1)} E^{\lambda_2 - 1} = -1 \tag{16}$$

$$\frac{K}{1+r\ \Delta\tau} - K + a^{(1)}K^{\lambda_1} + b^{(1)}K^{\lambda_2} = c^{(1)}K^{\lambda_2}$$
(17)

$$-1 + \lambda_1 a^{(1)} K^{\lambda_1 - 1} + \lambda_2 b^{(1)} K^{\lambda_2 - 1} = \lambda_2 c^{(1)} K^{\lambda_2 - 1}$$
(18)

which has made use of  $S_f(\tau_0) = K$ . The solution of this system is tedious, we skip the derivation. This explains the analytic solution of equation  $(13)$  along the first line.

#### **General Case**

The following lines  $(v \ge 2)$  lead to even more involved equations, because in subinterval C the inhomogeneous solution is nontrivial, and additional subintervals B are inserted for each new line. The general structure of the solutions of the ODE is the same in the subintervals B, but the coefficients differ. And, of course, the points  $S_f(\tau_v)$  vary. The resulting analytic method of lines is quite involved. The final formulas from [3] for a put with  $\delta < r$  are the following:

Notations

$$\begin{aligned} \gamma &= \frac{1}{2} - \frac{r - \delta}{\sigma^2} \\ R &= \frac{1}{1 + r\Delta\tau} \quad \text{(single-period discount factor)} \\ D &= \frac{1}{1 + \delta\Delta\tau} \\ \varepsilon &= \sqrt{\gamma^2 + \frac{2}{R\sigma^2\Delta\tau}} \\ p &= \frac{\varepsilon - \gamma}{2\varepsilon} \ , \ q = 1 - p \end{aligned}$$

$$\hat{p} = \frac{\varepsilon - \gamma + 1}{2\varepsilon} , \ \hat{q} = 1 - \hat{p}$$
  
$$S_{f,\nu} := S_f(\tau_\nu)$$
  
$$V^{(n)}(S) = \text{approximation of the American put for}$$
  
$$t = 0$$

After *n* lines, the solutions consist of  $n + 2$  pieces,

$$V^{(n)}(S) = \begin{cases} K - S & \text{for } S \leq S_{f,n} \\ v_{\nu}^{(n)}(S) + b_{\nu}^{(n)}(S) + A_{\nu}^{(n)}(S;1) \\ & \text{for } S_{f,\nu} < S \leq S_{f,\nu-1} \ , \ \nu = 1,\dots,n \\ p_{0}^{(n)}(S) + b_{1}^{(n)}(S) & \text{for } S > S_{f,0} \equiv K \end{cases}$$
(19)

This piecewise defined function represents  $w(S, \tau_n)$ and corresponds to  $V(S, 0)$ . The coefficients are

$$p_0^{(n)}(S) = \left(\frac{S}{K}\right)^{\gamma-\varepsilon} \sum_{k=0}^{n-1} \frac{(2\varepsilon \ln(S/K))^k}{k!} \times \sum_{l=0}^{n-k-1} {n-1+l \choose n-1} \times \left[ KR^n q^n p^{l+k} - KD^n \hat{q}^n \hat{p}^{l+k} \right]$$
(20)

$$v_{\nu}^{(n)}(S) = KR^{n-\nu+1} - SD^{n-\nu+1} \tag{21}$$

$$b_{\nu}^{(n)}(S) = \sum_{j=1}^{n-\nu+1} \left(\frac{S}{S_{f,n-j+1}}\right)^{\gamma-\varepsilon}$$
$$\times \sum_{k=0}^{j-1} \frac{(2\varepsilon \ln(S/S_{f,n-j+1}))^k}{k!}$$
$$\times \sum_{l=0}^{j-k-1} {j-1+l \choose j-1}$$
$$\times \left[q^j p^{k+l} R^j K r - \hat{q}^j \hat{p}^{k+l} D^j S_{f,n-j+1} \delta\right] \Delta \tau \tag{22}$$

$$A_{\nu}^{(n)}(S;i) = \sum_{j=i}^{n-\nu+1} \left(\frac{S}{S_{f,n-j+1}}\right)^{\nu+\varepsilon} \times \sum_{k=0}^{j-1} \frac{(2\varepsilon \ln(S_{f,n-j+1}/S))^k}{k!}$$

$$\times \sum_{l=0}^{j-k-1} {j-1+l \choose j-1} \\
\times \left[ p^j q^{k+l} R^j K r \right] \\
- \hat{p}^j \hat{q}^{k+l} D^j S_{f,n-j+1} \delta \right] \Delta \tau \n$$
(23)

The approximation of the optimal exercise prices  $S_{f,m}$ are solutions of the equations

$$c_{1}^{(m)}(K) - A_{1}^{(m)}(K;2)$$
  
=  $\left(\frac{K}{S_{f,m}}\right)^{\gamma+\varepsilon} \left[pRKr - \hat{p}DS_{f,m}\delta\right] \Delta \tau$  (24)

for  $m = 1, \ldots, n$ , where

 $\sim$ 

 $\sim$ 

$$c_{1}^{(m)}(K) = \sum_{l=0}^{m-1} {m-1+l \choose m-1} \times \left[KD^{m}\hat{p}^{m}\hat{q}^{l} - KR^{m}p^{m}q^{l}\right] \qquad (25)$$

This equation is solved iteratively with Newton's method. In case no dividend is paid ( $\delta = 0, D = 1$ ), no iteration is needed, and the solution is

$$S_{f,m} = K \left(\frac{pRKr\Delta\tau}{c_1^{(m)}(K) - A_1^{(m)}(K;2)}\right)^{1/(\gamma+\varepsilon)} \tag{26}$$

This value would serve as initial guess for the Newton iteration in case  $\delta > 0$ . The formulas of these triple sums are also collected in [2]. The corresponding formulas for a call are available too. Instead, the put-call symmetry relation from [4] can be used as well.

## Extrapolation

For small values of  $n$ , the method does not provide high accuracy in its basic state. To enhance the quality of the approximation, Richardson extrapolation is applied. Let  $\overline{V}_n$  denote the result of the above MoL with  $n$  lines, evaluating equation (19) for a given value of S. Assume that three approximations  $\overline{V}_1$ ,  $\overline{V}_2$ , and  $\overline{V}_3$  are calculated. Note that  $\overline{V}_1$  means that only a single timestep of size  $\Delta \tau = T$  is used. Then the extrapolated value

$$\overline{V}^{1:3} := \frac{1}{2}(9\overline{V}_3 - 8\overline{V}_2 + \overline{V}_1) \tag{27}$$

| Table 1<br>S | Test results of the tuned V 1:3 for<br>K = 100 |     |      |      |          |
|--------------|------------------------------------------------|-----|------|------|----------|
|              | T                                              | σ   | r    | δ    | V (S, 0) |
| 80           | 0.5                                            | 0.4 | 0.06 | 0.00 | 21.6257  |
| 100          | 0.5                                            | 0.4 | 0.02 | 0.00 | 10.7899  |
| 80           | 3.0                                            | 0.4 | 0.06 | 0.02 | 29.2323  |

gives an accurate result with order *(τ )*3. As shown in [1], the obtainable accuracy of the combined MoL/extrapolation approach compares well to the other methods. Reference [3] applies a fine tuning to the three-point formula *V* 1:3 replacing the coefficient 8 in the above formula by 8*(*1 − 0*.*0002*(*5 − *T )*<sup>+</sup>*)*. Even with only two approximations, *V* <sup>1</sup>*, V* 2, extrapolation enhances the accuracy significantly. The formula

$$\overline{V}^{1:2} := -\overline{V}^1 + 2\overline{V}^2 \tag{28}$$

is of the order *(τ )*2. The justification of Richardson extrapolation in this context does not yet appear fully explored; smoothness in time is assumed. This is not a disadvantage since equations (27) or (28) serve as analytic-approximation formulas.

# **Further Remarks**

For comparison, we provide in Table 1, three test values of the tuned version of the three-line extrapolation equation (27). To check the accuracy, an independent computation with a highly accurate version of a finite-difference approach was run. This has revealed relative errors of about 10<sup>−</sup><sup>3</sup> in the three examples reported in Table 1—that is, three digits are correct. For testing purposes, the MoL method with the tuned version of the formula *V* 1:3 of equation (27) is installed in the option-calculator of the website www.compfin.de. Note that the above describes the analytic method of [3]; the MoL approach of [5] solves equation (7) numerically.

# **References**

- [1] Broadie, M. & Detemple, J. (1996). American option valuation: new bounds, approximations, and a comparison of existing methods, *Review of Financial Studies* **9**, 1211–1250.
- [2] Carr, P. (1998). Randomization and the American put, *Review Financial Studies* **11**, 597–626.
- [3] Carr, P. & Faguet, D. (1995). *Fast Accurate Valuation of American Options*, Working Paper, Cornell University.
- [4] McDonald, R.L. & Schroder, M.D. (1998). A parity result for American options, *Journal of Computational Finance* **1**(3), 5–13.
- [5] Meyer, G.H. & van der Hoek, J. (1997). The valuation of American options with the method of lines, *Advances in Futures and Options Research* **9**, 265–285.
- [6] Seydel, R. (2006). *Tools for Computational Finance*, Springer, Berlin.

RUDIGER ¨ U. SEYDEL
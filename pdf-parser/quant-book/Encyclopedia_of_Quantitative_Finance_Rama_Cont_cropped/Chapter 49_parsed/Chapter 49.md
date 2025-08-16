## Itô's Formula

For a function depending on space and time parameters, rules of differentiation are well known. For a function depending on space and time parameters and also on a randomness parameter, Itô's formulas provide rules of differentiation. These rules of differentiation are based on the complementary notion of stochastic integration (see Stochastic Integrals). More precisely, given a probability space  $(\Omega, \mathbb{I}P, \mathcal{F},$  $(\mathcal{F}_t)_{t>0}$ ), Itô's formulas deal with  $(F(X_t); t \ge 0)$ , where  $F$  is a deterministic function defined on  $\mathbb{R}$ and  $(X_t)_{t>0}$  is a random process such that integration of locally bounded predictable processes is possible with respect to  $(X_t)_{t\geq 0}$  and satisfies a property equivalent to the Lebesgue dominated convergence theorem. This means that  $(X_t)_{t\geq 0}$  is a semimartingale and therefore has a finite quadratic variation process ( $[X]_t$ ,  $t > 0$ ) (see Stochastic Integrals) defined as

$$[X]_{t} = \lim_{n \to \infty} \sum \left( X_{s_{i+1}^{n}} - X_{s_{i}^{n}} \right)^{2} \text{ in probability,}$$
  
uniformly on time intervals (1)

where  $(s_i^n)_{1 \le i \le n}$  is a subdivision of [0, t] whose mesh converges to 0 as *n* tends to  $\infty$ .

We will see that Itô's formulas also provide information on the stochastic structure of the process  $(F(X_t), t > 0)$ . We first introduce the formula established by Itô in 1951. Consider a process  $(X_t)_{t>0}$  of the form

$$X_t = \int_0^t H_s \, \mathrm{d}B_s + \int_0^t G_s \, \mathrm{d}s \tag{2}$$

where  $(B_s)_{s\geq 0}$  is a real-valued Brownian motion, and  $(H_s)_{s\geq 0}$  and  $(G_s)_{s\geq 0}$  are locally bounded predictable processes. Then for every  $C^2$ -function F from  $\mathbb{R}$  to  $\mathbb{R}$ , we have

$$F(X_t) = F(X_0) + \int_0^t F'(X_s) H_s \, \mathrm{d}B_s$$
  
+ 
$$\int_0^t F'(X_s) G_s \, \mathrm{d}s + \frac{1}{2} \int_0^t H_s^2 F''(X_s) \, \mathrm{d}s$$
(3)

The process defined in formula (2) is an example of continuous semimartingale. Here is the classical Itô formula for a general semimartingale  $(X_s)_{s\geq 0}$  (e.g., [7, 9]) and F in  $\mathcal{C}^2$ 

$$F(X_t) = F(X_0) + \int_0^t F'(X_{s_-}) \, \mathrm{d}X_s$$
  
+  $\frac{1}{2} \int_0^t F''(X_s) \, \mathrm{d}[X]_s^c$   
+  $\sum_{0 \le s \le t} \left\{ F(X_s) - F(X_{s_-}) - F'(X_{s_-}) \Delta X_s \right\}$  (4)

where  $[X]^c$  is the continuous part of  $[X]$ . For continuous semimartingales, formula (4) becomes

$$F(X_t) = F(X_0) + \int_0^t F'(X_s) \, \mathrm{d}X_s$$
$$+ \frac{1}{2} \int_0^t F''(X_s) \, \mathrm{d}[X]_s \tag{5}$$

In the special case when  $(X_t)_{t\geq 0}$  is a real Brownian motion, then  $[X]_t = t$ .

The multidimensional version of formula (4) gives the expansion of  $F(X_t^{(1)}, X_t^{(2)}, \ldots, X_t^{(d)})$  for F a real-valued function of  $\mathcal{C}^2(\mathbb{R}^d)$  and d semimartingales  $X^{(1)}, X^{(2)}, \ldots, X^{(d)}$ . We set  $X = (X^{(1)},$  $X^{(2)}, \ldots, X^{(d)}$ :

$$F(X_{t}) = F(X_{0}) + \sum_{i=1}^{d} \int_{0}^{t} \frac{\partial F}{\partial x_{i}}(X_{s-}) \, \mathrm{d}X_{s}^{(i)}$$
$$+ \frac{1}{2} \sum_{1 \leq i, j \leq d} \int_{0}^{t} \frac{\partial^{2} F}{\partial x_{i} \partial x_{j}}(X_{s-}) \, \mathrm{d} \left[ X^{(i)}, X^{(j)} \right]_{s}^{c}$$
$$+ \sum_{0 \leq s \leq t} \left\{ F(X_{s}) - F(X_{s-}) \right\}$$
$$- \sum_{i=1}^{d} \frac{\partial F}{\partial x_{i}}(X_{s-}) \Delta X_{s}^{(i)} \right\} \tag{6}$$

Note the Itô formula corresponding to the case of the couple of semimartingales  $(X_t, t)_{t \ge 0}$  with X

continuous and F in  $\mathcal{C}^2(\mathbb{R}^2)$ 

$$F(X_t, t) = F(X_0, 0) + \int_0^t \frac{\partial F}{\partial x}(X_s, s) \, \mathrm{d}X_s$$
$$+ \int_0^t \frac{\partial F}{\partial t}(X_s, s) \, \mathrm{d}s$$
$$+ \frac{1}{2} \int_0^t \frac{\partial^2 F}{\partial x^2}(X_s, s) \, \mathrm{d}[X]_s \tag{7}$$

Each of the above Itô formulas gives a decomposition of the process  $(F(X_t), t > 0)$  that can be reduced to the sum of a local martingale and an adapted bounded variation process. This shows that  $F(X)$  is a semimartingale. In practical situations, the considered function F might not be a  $C^2$ -function and the process  $F(X)$  might not be a semimartingale. Hence, many authors have written extensions of the above formulas enlightening this  $C^2$ -condition. Some of them use the notion of local times (see **Local Times**) whose definition can actually be set by the following first extension of the Itô formula.

For  $F$  real-valued convex function and  $X$  semimartingale,  $F(X)$  is a semimartingale too and

$$F(X_t) = F(X_0) + \int_0^t F'(X_{s-}) \, \mathrm{d}X_s + A_t \qquad (8)$$

where F' is the left derivative of F and  $(A_t, t > 0)$  is an adapted, right continuous increasing process such that  $\Delta A_s = F(X_s) - F(X_{s-}) - F'(X_{s-})\Delta X_s$ .

Choosing  $F(x) = |x - a|$ , one obtains the existence of an increasing process  $(L^a_t, t \ge 0)$  such that

$$|X_t - a| = |X_0 - a| + \int_0^t \operatorname{sgn}(X_{s-} - a) \, \mathrm{d}X_s + L_t^a$$
$$+ \sum_{0 < s \le t} \left\{ |X_s - a| - |X_{s-} - a| \right.$$
$$- \operatorname{sgn}(X_{s-} - a) \Delta X_s \right\} \tag{9}$$

The process  $L^a$  is called the *local time process* of X at  $a$  (see **Local Times** for alternative definition and basic properties). Note that  $L^a$  is continuous in t.

Coming back to formula (8), denote by  $\mu$  the second derivative of  $F$  in the generalized function sense; then the Meyer-Itô formula goes further by giving the expression of the bounded variation

process  $A$ :

$$F(X_{t}) = F(X_{0}) + \int_{0}^{t} F'(X_{s-}) dX_{s}$$
  
+ 
$$\sum_{0 < s \le t} \left\{ F(X_{s}) - F(X_{s-}) - F'(X_{s-}) \Delta X_{s} \right\}$$
  
+ 
$$\frac{1}{2} \int_{\mathbb{R}} L_{t}^{x} \mu(dx)$$
 (10)

The Meyer-Itô formula is also obviously available for functions  $F$ , which are difference of two convex functions.

For the semimartingales  $X$ , such that for every  $t>0$ :  $\sum_{0\leq s\leq t}|\Delta X_{s}|<\infty$  a.s., Bouleau and Yor extended the Meyer-Itô formula to functions  $F$ , admitting a Radon-Nicodym derivative with respect to the Lebesgue measure. Indeed, the Bouleau-Yor formula  $[2]$  states in that case

$$F(X_t) = F(X_0) + \int_0^t F'(X_{s-}) \, \mathrm{d}X_s$$
  
+ 
$$\sum_{0 < s \le t} \left\{ F(X_s) - F(X_{s-}) - F'(X_{s-}) \Delta X_s \right\}$$
  
- 
$$\frac{1}{2} \int_{\mathbb{R}} F'(x) \, \mathrm{d}_x L_t^x \tag{11}$$

Note that the Bouleau-Yor formula requires the construction of a stochastic integration of deterministic functions with respect to the process  $(L^x, x \in \mathbb{R})$ , although this last process might not be a semimartingale. Besides, this formula shows that the process  $(F(X_t), t \ge 0)$  might not be a semimartingale but a Dirichlet process (i.e., the sum of a local martingale and a 0-quadratic variation process).

In the special case of a real Brownian motion  $(B_t, t \ge 0)$ , Föllmer, Protter, and Shiryayev formula offers an extension of the Bouleau-Yor formula to space-time functions G defined on  $\mathbb{R} \times \mathbb{R}_+$  admitting a Radon-Nikodym derivative with respect to the space parameter  $\partial G/\partial x$  with some continuity properties (see [6], for the detailed assumptions)

$$G(B_t, t) = G(B_0, t) + \int_0^t G(B_s, \, \mathrm{d}s)$$
$$+ \int_0^t \frac{\partial G}{\partial x}(B_s, s) \, \mathrm{d}B_s + \frac{1}{2} \left[ \frac{\partial G}{\partial x}(B_+, .), B \right]_t \tag{12}$$

with  $\int_0^t G(B_s, ds) = \lim_{n \to \infty} \sum_{i=1}^n (G(B_{s_{i+1}^n}, s_{i+1}^n) G(B_{s_{i+1}^n}, s_i^n)$  in probability, where  $(s_i^n)_{1 \le i \le n}$  is a subdivision of  $[0, t]$  whose mesh converges to 0 as n tends to  $\infty$  (Reference 5 contains a similar result and Reference 1 extends it to nondegenerate diffusions).

Another way to extend the Bouleau-Yor formula, in the case of a real Brownian motion, consists in the construction of the stochastic integration of locally bounded deterministic space-time functions  $f(x, t)$  with respect to the local time process  $(L^x, x \in \mathbb{R}, t > 0)$  of B. That way one obtains, for the functions  $G$  admitting locally bounded first-order derivatives, Eisenbaum's formula [3]:

$$G(B_t, t) = G(B_0, t) + \int_0^t \frac{\partial G}{\partial x}(B_s, s) \, \mathrm{d}B_s$$
$$+ \int_0^t \frac{\partial G}{\partial t}(B_s, s) \, \mathrm{d}s$$
$$- \frac{1}{2} \int_0^t \int_{\mathbb{R}} \frac{\partial G}{\partial x}(x, s) \, \mathrm{d}L_s^x \qquad (13)$$

The comparison of formula  $(13)$  with formulas  $(12)$ and (7) provides some rules of integration with respect to the local time process of  $B$  such as

for  $f$  continuous function on  $\mathbb{R} \times \mathbb{R}_+$ 

$$\int_0^t \int_{\mathbb{R}} f(x, s) \, \mathrm{d}L_s^x = -[f(B_{.}, .), B_{.}]_t \quad (14)$$

for f locally bounded function on  $\mathbb{R} \times \mathbb{R}_+$ admitting a locally bounded Radon-Nikodym derivative  $\partial f/\partial x$ 

$$\int_0^t \int_{\mathbb{R}} f(x,s) \, \mathrm{d}L_s^x = -\int_0^t \frac{\partial f}{\partial x}(X_s,s) \, \mathrm{d}s \quad (15)$$

See [2] for an extension of formula (13) to Lévy processes.

We now mention the special case of a space-time function  $G(x, s)$  defined as follows:

$$G(x,s) = G_1(x,s)1_{\{x>b(s)\}} + G_2(x,s)1_{\{x \le b(s)\}}$$
(16)

where  $(b(s), s \ge 0)$  is a continuous curve and  $G_1$ and  $G_2$  are  $C^2$ -functions that coincide on  $x = b(s)$  (but not their derivatives). This case is treated in [8] for X continuous semimartingale and in [4] for  $X$ Lévy process such that  $\sum_{0 \le s \le t} |\Delta X_s| < \infty$  a.s. Both use the notion of local time of  $X$  along the curve  $b$ denoted  $(L_s^{b(.)}, s \ge 0)$ , defined as

$$L_t^{b(.)} = \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_0^t 1_{(|X_s - b(s)| < \epsilon)} d[X]_s^c$$
  
uniformly on compacts in  $L^1$  (17)

When b is a equal to the constant a,  $L^{b(.)}$  coincides with the local time at the value  $a$ . These formulas have the following form:

$$X_{t}, t) = G(X_{0}, 0) + \int_{0}^{t} \frac{\partial G}{\partial x}(X_{s-}, s) dX_{s}$$
  
+ 
$$\int_{0}^{t} \frac{\partial G_{1}}{\partial t}(X_{s}, s)1_{(X_{s} < b(s))} ds$$
  
+ 
$$\int_{0}^{t} \frac{\partial G_{2}}{\partial t}(X_{s}, s)1_{(X_{s} \ge b(s))} ds$$
  
+ 
$$\frac{1}{2} \int_{0}^{t} \left(\frac{\partial^{2} G_{1}}{\partial x^{2}}(X_{s}, s)1_{(x < b(s))}\right) ds$$
  
+ 
$$\frac{\partial^{2} G_{2}}{\partial x^{2}}(X_{s}, s)1_{(x \ge b(s))} \right) d[X]_{s}^{c}$$
  
+ 
$$\frac{1}{2} \int_{0}^{t} \left(\frac{\partial G_{2}}{\partial x} - \frac{\partial G_{1}}{\partial x}\right) (b(s), s) d_{s}L_{s}^{b(.)}$$
  
+ 
$$\sum_{0 < s \le t} \left\{ G(X_{s}, s) - G(X_{s-}, s) - \frac{\partial G}{\partial x}(X_{s-}, s) \Delta X_{s} \right\}$$
 (18)

Note that  $\partial G/\partial x$  exists as a Radon-Nikodym derivative and is equal to  $(\partial G_1/\partial x)(x, s)1_{(x < b(s))}$  +  $(\partial G_2/\partial x)(x, s)1_{(x \ge b(s))}$ . The formula (18) is helpful in free-boundary problems of optimal stopping. Other illustrations of formula  $(13)$  are given in [4] for multidimensional Lévy processes.

## References

 $G($ 

Bardina X. & Jolis M. (1997). An extension of Itô's for- $[1]$ mula for elliptic diffusion processes, Stochastic Processes and their Applications 69, 83-109.

- [2] Bouleau N. & Yor M. (1981). Sur la variation quadratique des temps locaux de certaines semimartingales, *Comptes Rendus de l'Acad´emie des Sciences* **292**, 491–494.
- [3] Eisenbaum N. (2000). Integration with respect to local time, *Potential Analysis* **13**, 303–328.
- [4] Eisenbaum N. (2006). Local time-space stochastic calculus for Levy processes, ´ *Stochastic Processes and their Applications* **116**(5), 757–778.
- [5] Errami M., Russo F. & Vallois P. (2002). Ito formula ˆ for *C*<sup>1</sup>*,λ*-functions of a cadl ` ag process, ` *Probability Theory and Related Fields* **122**, 191–221.
- [6] Follmer H., Protter P. & Shiryayev A.N. (1995). Quad- ¨ ratic covariation and an extension of Ito's formula, ˆ *Bernoulli* **1**(1/2), 149–169.

- [7] Jacod J. & Shiryayev A.N. (2003). *Limit Theorems for Stochastic Processes*, 2nd Edition, Springer.
- [8] Peskir G. (2005). A change-of-variable formula with local time on curves, *Journal of Theoretical Probability* **18**, 499–535.
- [9] Protter, P. (2004). *Stochastic Integration and Differential Equations*, 2nd Edition, Springer.

## **Related Articles**

## **Levy Processes ´** ; **Local Times**; **Stochastic Integrals**.

NATHALIE EISENBAUM
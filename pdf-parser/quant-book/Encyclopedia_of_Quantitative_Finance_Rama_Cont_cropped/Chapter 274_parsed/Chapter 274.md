# **Stochastic Taylor Expansions**

## **Deterministic Taylor Formula**

As the concept of a stochastic Taylor expansion can be widely applied, we first review the *deterministic Taylor expansion*, using some terminology which will facilitate the presentation of its stochastic counterparts. Let us consider the solution *X* = {*Xt, t* ∈ [0*, T* ]} of the ordinary differential equation d*Xt* = *a(Xt)* d*t*, for *t* ∈ [0*, T* ] with initial value *X*0. We can write this equation in its integral form as

$$X_t = X_0 + \int_0^t a(X_s) \, \mathrm{d}s \tag{1}$$

To justify the following calculations, we require the drift function *a* to be smooth and such that the solution of equation (1) does not explode. Then by using the deterministic chain rule, we can write

$$df(X_t) = a(X_t) \frac{\partial}{\partial x} f(X_t) dt \tag{2}$$

Using the operator *L* = *a ∂/∂x*, we may express equation (2) as the integral equation

$$f(X_t) = f(X_0) + \int_0^t L f(X_s) \, \mathrm{d}s \tag{3}$$

for all *t* ∈ [0*, T* ]. Note for the special case *f (x)* ≡ *x* we have *Lf* = *a*, *LLf* = *(L)*<sup>2</sup>*f* = *La, . . .* , and equation (3) reduces to equation (1). If we now apply relation (3) to the integrand *f* = *a* in equation (1), then we obtain

$$X_{t} = X_{0} + \int_{0}^{t} \left( a(X_{0}) + \int_{0}^{s} L \, a(X_{z}) \, \mathrm{d}z \right) \, \mathrm{d}s$$
  
$$= X_{0} + a(X_{0}) \int_{0}^{t} \, \mathrm{d}s + \int_{0}^{t} \int_{0}^{s} L \, a(X_{z}) \, \mathrm{d}z \, \mathrm{d}s \tag{4}$$

which is the simplest nontrivial Taylor expansion for *Xt* . We can now apply equation (3) to the function *f* = *La* in the above double integral in equation (4). Consequently, we obtain

$$X_{t} = X_{0} + a(X_{0}) \int_{0}^{t} ds$$
  
+  $La(X_{0}) \int_{0}^{t} \int_{0}^{s} dz ds + R_{1}$  (5)

with remainder term

$$R_1 = \int_0^t \int_0^s \int_0^z (L)^2 a(X_u) \, \mathrm{d}u \, \mathrm{d}z \, \mathrm{d}s \qquad (6)$$

for *t* ∈ [0*, T* ]. Continuing this way then we get a version of the classical deterministic *Taylor formula*

$$f(X_t) = f(X_0) + \sum_{l=1}^r \frac{t^{\ell}}{l!} (L)^{\ell} f(X_0)$$
$$+ \int_0^t \cdots \int_0^{s_2} (L)^{r+1} f(X_{s_1}) \, \mathrm{d}s_1 \dots \, \mathrm{d}s_{r+1} \tag{7}$$

for *t* ∈ [0*, T* ] and *r* ∈ N. In the sum on the righthand side of equation (5), we find the expansion terms that are expanded at time zero or, more precisely, at the value *X*0. Furthermore, the last term, which is a multiple integral, represents the remainder term. Its integrand is, in general, not a constant. The deterministic Taylor formula allows the approximation of a sufficiently smooth function in a neighborhood of a given expansion point to any desired order of accuracy as long as *f* and *a* are sufficiently smooth.

## **Wagner–Platen Expansion**

It is important to be able to approximate the increments of smooth functions of solutions of stochastic differential equations. For these tasks, a stochastic expansion, with analogous properties to the deterministic Taylor formula, is needed. The *Wagner–Platen expansion* (see [1, 2, 5, 8, 10, 11]) is such a stochastic Taylor expansion. We derive here one of its versions for a diffusion process *X* = {*Xt, t* ∈ [0*, T* ]} satisfying

$$X_{t} = X_{0} + \int_{0}^{t} a(X_{s}) \, \mathrm{d}s + \int_{0}^{t} b(X_{s}) \, \mathrm{d}W_{s} \qquad (8)$$

for  $t \in [0, T]$ , where *W* is a standard Wiener process. The coefficient functions  $a$  and  $b$  are assumed to be sufficiently smooth, real valued, and such that a unique solution of equation (6) exists. Then, for a sufficiently smooth function  $f: \Re \rightarrow \Re$ , the Itô formula provides the representation

$$f(X_t) = f(X_0) + \int_0^t L^0 f(X_s) \, \mathrm{d}s$$
$$+ \int_0^t L^1 f(X_s) \, \mathrm{d}W_s \tag{9}$$

for  $t \in [0, T]$ , where we used the operators  $L^0 =$  $a\left(\frac{\partial}{\partial x}\right) + \frac{1}{2}b^2\left(\frac{\partial^2}{\partial x^2}\right)$  and  $L^1 = b\left(\frac{\partial}{\partial x}\right)$ .

Obviously, for the special case  $f(x) \equiv x$ , we have  $L^0 f = a$  and  $L^1 f = b$ , for which the representation  $(9)$  reduces to equation  $(8)$ . Since the representation  $(9)$  involves integrands that are functions of processes, we can now apply the Itô formula (9) to the functions  $a$  and  $b$  in equation (8) to obtain

$$X_{t} = X_{0} + \int_{0}^{t} \left( a(X_{0}) + \int_{0}^{s} L^{0} a(X_{z}) \, \mathrm{d}z \right)$$
  
+ 
$$\int_{0}^{s} L^{1} a(X_{z}) \, \mathrm{d}W_{z} \right) \, \mathrm{d}s + \int_{0}^{t} \left( b(X_{0}) + \int_{0}^{s} L^{0} b(X_{z}) \, \mathrm{d}W_{z} \right) \, \mathrm{d}W_{s} \, \mathrm{d}W_{s}$$
  
= 
$$X_{0} + a(X_{0}) \int_{0}^{t} \mathrm{d}s + b(X_{0}) \int_{0}^{t} \mathrm{d}W_{s} + R_{2} \qquad (10)$$

with remainder term

$$R_{2} = \int_{0}^{t} \int_{0}^{s} L^{0} a(X_{z}) \, \mathrm{d}z \, \mathrm{d}s$$
  
+ 
$$\int_{0}^{t} \int_{0}^{s} L^{1} a(X_{z}) \, \mathrm{d}W_{z} \, \mathrm{d}s$$
  
+ 
$$\int_{0}^{t} \int_{0}^{s} L^{0} b(X_{z}) \, \mathrm{d}z \, \mathrm{d}W_{s}$$
  
+ 
$$\int_{0}^{t} \int_{0}^{s} L^{1} b(X_{z}) \, \mathrm{d}W_{z} \, \mathrm{d}W_{s} \qquad (11)$$

This already represents a simple example of a Wagner-Platen expansion. We can extend the above expansion by applying the Itô formula (9), for

instance, to the function  $L^1b$  in the remainder. In this case, we obtain the expansion

$$X_{t} = X_{0} + a(X_{0}) \int_{0}^{t} \mathrm{d}s + b(X_{0}) \int_{0}^{t} \mathrm{d}W_{s}$$
$$+ L^{1}b(X_{0}) \int_{0}^{t} \int_{0}^{s} \mathrm{d}W_{z} \mathrm{d}W_{s} + R_{3} \quad (12)$$

with a new remainder  $R_3$ . In equation (12), the leading terms are functions of the value of the diffusion at the expansion point, which are weighted by corresponding multiple stochastic integrals. In principle, one can derive such an expansion for a general multifactor diffusion process  $X$ , a general smooth function  $f$ , and an arbitrary high expansion level (see  $[6]$ ). The main properties of this type of expansion are already apparent in the preceding example. The Wagner-Platen expansion can be interpreted as a generalization of both the Itô formula and the classical deterministic Taylor formula. It can be derived *via* an iterated application of the Itô formula.

The following version of a Wagner-Platen expansion, involving triple integrals in the expansion part, can be useful in various applications:

$$X_{t} = X_{0} + a I_{(0)} + b I_{(1)} + (a a' + 1/2 b^{2} a'') I_{(0,0)}$$
  
+  $(a b' + 1/2 b^{2} b'') I_{(0,1)} + b a' I_{(1,0)} + b b' I_{(1,1)}$   
+  $[a (a a'' + (a')^{2} + b b' a'' + 1/2 b^{2} a'')$   
+  $1/2 b^{2} (a a''' + 3 a' a'' + ((b')^{2} + b b'') a''$   
+  $2 b b' a''') + 1/4 b^{4} a^{(4)}] I_{(0,0,0)}$   
+  $[a (a'b' + a b'' + b b'b'' + 1/2 b^{2} b''')$   
+  $1/2 b^{2} (a''b' + 2 a'b'' + a b''' + ((b')^{2} + b b'') b''$   
+  $2 b b'b''' + 1/2 b^{2} b^{(4)})] I_{(0,0,1)} + [a (b'a' + b a'')$   
+  $1/2 b^{2} (b''a' + 2 b'a'' + b a''')] I_{(0,1,0)}$   
+  $[a ((b')^{2} + b b'') + 1/2 b^{2} (b''b' + 2 b b'' + b b'')'] I_{(0,1,1)} + b (a a'' + (a')^{2} + b b'a'' + 1/2 b^{2} a''')] I_{(1,0,0)} + b (a b'' + a'b' + b b'b'' + 1/2 b^{2} b'''') I_{(1,0,1)} + b (a b'' + a'b' + b b'b'' + 1/2 b^{2} b'''') I_{(1,0,1)} + b (a'b' + a''b) I_{(1,1,0)}$   
+  $b ((b')^{2} + b b'') I_{(1,1,1)} + R_{6}$  (13)

Here, the coefficient functions  $a, b$ , and their derivatives  $a'$ ,  $b'$ ,  $a''$ ,  $b''$ ,  $a'''$ ,  $b'''$  are valued at the expansion point  $X_0$ , which we suppress in our notation. The multiple stochastic integrals  $I_{(i_1, i_2, i_3)} =$  $\int_0^t \int_0^s \int_0^z \mathrm{d} W_u^{j_1} \mathrm{d} W_z^{j_2} \mathrm{d} W_s^{j_3}$ , where we set  $\mathrm{d} W_t^0 = \mathrm{d} t$ and  $dW_t^1 = dW_t$ , are taken on [0, t]. Important applications of Wagner-Platen expansions arise in the construction of strong and weak discrete time approximations for scenario simulation (see Stochastic Differential Equations: Scenario Simulation) and Monte Carlo simulation (see Monte Carlo Simulation for Stochastic Differential Equations). Detailed results for higher level stochastic Taylor expansions and derivations of estimates for the remainder can be found in [6].

### **Generalized Wagner–Platen Expansions**

By following the same ideas, one can expand the changes of a function value with respect to the underlying diffusion process  $X$  itself. For example, from an iterated application of the Itô formula it follows for a sufficiently smooth function  $f: [0, T] \times \mathbb{R} \to \mathbb{R}$  an expansion of the form

$$f(t, X_{t}) = f(0, X_{0}) + \frac{\partial}{\partial t} f(0, X_{0}) t$$
  

$$+ \frac{\partial}{\partial x} f(0, X_{0}) (X_{t} - X_{0})$$
  

$$+ \frac{1}{2} \frac{\partial^{2}}{\partial x^{2}} f(0, X_{0}) \langle X \rangle_{t}$$
  

$$+ \frac{\partial^{2}}{\partial x \partial t} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dX_{z} ds$$
  

$$+ \frac{1}{2} \frac{\partial^{2}}{\partial x^{2}} \frac{\partial}{\partial t} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dX_{z} ds$$
  

$$+ \frac{\partial^{2}}{\partial t \partial x} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dZ_{z} dX_{s}$$
  

$$+ \frac{\partial^{2}}{\partial x^{2}} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dZ_{z} dX_{s}$$
  

$$+ \frac{1}{2} \frac{\partial^{3}}{\partial x^{3}} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dX_{z} dX_{s}$$
  

$$+ \frac{1}{2} \frac{\partial^{3}}{\partial t \partial x^{3}} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dZ_{z} dX_{s}$$
  

$$+ \frac{1}{2} \frac{\partial^{3}}{\partial t \partial x^{3}} f(0, X_{0}) \int_{0}^{t} \int_{0}^{s} dZ_{z} dX_{s}$$

$$+\frac{1}{4} \frac{\partial^4}{\partial x^4} f(0, X_0) \int_0^t \int_0^s \mathrm{d}\langle X \rangle_z \,\mathrm{d}\langle X \rangle_s$$
$$+\bar{R}_f(0, t) \tag{14}$$

for  $t \in [0, T]$ , where  $\bar{R}_f(0, t)$  expresses the corresponding remainder term.

There exist multidimensional versions of Wagner-Platen expansions with respect to several driving processes. By using such expansions, one can, for instance, expand the increment of an option price in a multifactor setting. This provides a better understanding of the sensitivities with respect to given factor processes. Another application is the approximate evaluation of risk measures, for instance, Value-at-**Risk** (see [12]).

General stochastic Taylor expansions in a semimartingale setting have been derived in [8, 10]. Stochastic Taylor expansions based on multiple Stratonovich integrals are detailed in [5]. Wagner-Platen expansions for jump-diffusions and pure jump processes can be found in [3, 4, 9]. Expansions of functionals of Lévy processes *via* power processes have been described in  $[7]$ .

#### References

- $[1]$ Azencott, R. (1982). Stochastic Taylor formula and asymptotic expansion of Feynman integrals, Sèminaire de Probabilitès XVI, Supplement, Lecture Notes in Mathematics, Vol. 921, Springer, pp. 237-285.
- [2] BenArous, G. (1989). Flots et series de Taylor stochastiques, Probability Theory Related Fields 81, 29-77.
- [3] Bruti-Liberati, N. & Platen, E. (2007). Strong approximations of stochastic differential equations with jumps, Journal of Computational and Applied Mathematics 205(2), 982-1001.
- Engel, D. (1982). The multiple stochastic integral, Mem-[4] oirs of the American Mathematical Society 38, 265.
- [5] Kloeden, P.E. & Platen, E. (1991). Stratonovich and Itô stochastic Taylor expansions, Mathematische Nachrichten 151, 33-50.
- Kloeden, P.E. & Platen, E. (1999). Numerical Solution of [6] Stochastic Differential Equations, Applied Mathematics, Vol. 23, Springer (Third Printing).
- Nualart, D. & Schoutens, W. (2000). Chaotic and pre-[7] dictable representations for Lèvy processes, Stochastic Processes and Their Applications 90, 109–122.
- [8] Platen, E. (1981). A Taylor formula for semimartingales solving a stochastic differential equation, Stochastic Differential Systems, Lecture Notes in Control and Information Sciences, Vol. 36, Springer, pp. 157-164.

- [9] Platen, E. (1982). An approximation method for a class of Ito processes with jump component, ˆ *Lietuvos Matematikos Rinkinys* **22**(2), 124–136.
- [10] Platen, E. (1982). A generalized Taylor formula for solutions of stochastic differential equations, *Sankhya A* **44**(2), 163–172.
- [11] Platen, E. & Wagner, W. (1982). On a Taylor formula for a class of Ito processes, ˆ *Probability and Mathematical Statistics* **3**(1), 37–51.
- [12] Schoutens, W. & Studer, M. (2003). Short term risk management using stochastic Taylor expansions under Levy models, ` *Insurance: Mathematics and Economics* **33**(1), 173–188.

## **Related Articles**

**Monte Carlo Simulation for Stochastic Differential Equations**; **Stochastic Differential Equations: Scenario Simulation**; **Stochastic Differential Equations with Jumps: Simulation**.

ECKHARD PLATEN
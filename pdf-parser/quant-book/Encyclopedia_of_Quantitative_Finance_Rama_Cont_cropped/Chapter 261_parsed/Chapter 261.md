# **Monte Carlo Simulation** for Stochastic Differential Equations

## **Weak Convergence Criterion**

There exists a well-developed literature on classical Monte Carlo methods. We might mention, among others, Hammersley and Handscomb [3] and Fishman [1]. This literature, however, does not focus on approximating functionals of solutions of stochastic differential equations (SDEs). Exploiting the stochastic analytic structure of the underlying SDEs in discrete-time approximations allows to obtain deeper insight and significant benefits in a Monte Carlo simulation. One can construct more efficient methods than usually would be obtained under the classical Monte Carlo approach. Monographs on Monte Carlo methods for SDEs include [6, 7, 10]. The area of Monte Carlo methods in finance is the focus of the well-written books by Jackel [5] and Glasserman [2]. In [12], one can find a brief survey of such methods. In many circumstances, when other numerical methods fail or are difficult to implement, Monte Carlo methods can still provide a reasonable answer. This applies, in particular, to problems involving a large number of factors.

First, let us introduce a criterion that provides a classification of different simulation schemes. In Monte Carlo simulation, one concentrates on the approximation of probabilities and expectations of payoffs. Consider the process  $X = \{X_t, t \in [0, T]\},\$ which is the solution of the SDE

$$dX_t = a(X_t) dt + b(X_t) dW_t$$
(1)

for  $t \in [0, T]$  with  $X_0 \in \mathbb{R}$ . We shall say that a discrete-time approximation  $Y^{\Delta}$  converges with weak *order*  $\beta > 0$  to X at time T as  $\Delta \rightarrow 0$  if for each polynomial  $g: \mathbb{R} \to \mathbb{R}$  there exists a constant  $C_g$ , which does not depend on  $\Delta$ , and a  $\Delta_0 \in [0, 1]$  such that

$$\mu(\Delta) = |E(g(X_T)) - E(g(Y_T^{\Delta}))| \le C_g \,\Delta^{\beta} \qquad (2)$$

for each  $\Delta \in (0, \Delta_0)$ . We call this also the *weak* convergence criterion.

# **Systematic and Statistical Error**

Under the weak convergence criterion (2) functionals of the form

$$u = E(g(X_T)) \tag{3}$$

are approximated *via weak approximations*  $Y^{\Delta}$  of the solution of the SDE (1). One can form a raw Monte *Carlo estimate* by using the sample average

$$u_{N,\Delta} = \frac{1}{N} \sum_{k=1}^{N} g(Y_T^{\Delta}(\omega_k)) \tag{4}$$

with N independent simulated realizations  $Y_T^{\Delta}(\omega_1)$ ,  $Y_T^{\Delta}(\omega_2), \ldots, Y_T^{\Delta}(\omega_N)$  of a discrete-time weak approximation  $Y_T^{\Delta}$  at time T, where  $\omega_k \in \Omega$  for  $k \in$  $\{1, 2, \ldots, N\}$ . The corresponding weak error  $\hat{\mu}_{N,\Delta}$ has the form

$$\hat{\mu}_{N,\Delta} = u_{N,\Delta} - E(g(X_T)) \tag{5}$$

which we decompose into a *systematic error*  $\mu_{\text{sys}}$  and a *statistical error*  $\mu_{\text{stat}}$ , such that

$$\hat{\mu}_{N,\Delta} = \mu_{\text{sys}} + \mu_{\text{stat}} \tag{6}$$

Here, we set

$$\mu_{\text{sys}} = E(\hat{\mu}_{N,\Delta})$$
  
=  $E\left(\frac{1}{N}\sum_{k=1}^{N}g(Y_{T}^{\Delta}(\omega_{k}))\right) - E(g(X_{T}))$   
=  $E(g(Y_{T}^{\Delta})) - E(g(X_{T}))$  (7)

Thus, we have

$$\mu(\Delta) = |\mu_{\text{sys}}| \tag{8}$$

The absolute systematic error  $|\mu_{\text{sys}}|$  can be interpreted as the absolute weak error and is a critical variable under the weak convergence criterion (2).

For a large number  $N$  of simulated independent realizations of  $Y^{\Delta}$ , we can conclude from the central limit theorem that the statistical error  $\mu_{\text{stat}}$  becomes asymptotically Gaussian with mean 0 and variance of the form

$$\text{Var}(\mu_{\text{stat}}) = \text{Var}(\hat{\mu}_{N,\Delta}) = \frac{1}{N} \text{Var}(g(Y_T^{\Delta})) \qquad (9)$$

Note that in equation  $(9)$  we used the independence of the realization for each  $\omega_k$ . The expression (9) reveals a major disadvantage of the raw Monte Carlo method. One notes that the variance of the statistical error  $\mu_{\text{stat}}$  decreases only with  $1/N$ . Consequently, the deviation

$$\text{Dev}(\mu_{\text{stat}}) = \sqrt{\text{Var}(\mu_{\text{stat}})} = \frac{1}{\sqrt{N}} \sqrt{\text{Var}(g(Y_T^{\Delta}))}$$
(10)

of the statistical error decreases at only the slow rate  $1/\sqrt{N}$  as  $N \to \infty$ . This means that, unless one has to estimate the expectation of a random variable  $g(Y_T^{\Delta})$  with a small variance, one may need an extremely large number  $N$  of sample paths to achieve a reasonably small confidence interval. However, there exist various *variance reduction techniques* (see **Variance Reduction**), that deal with this problem.

We shall discuss now discrete-time approximations of solutions of SDEs that are appropriate for the Monte Carlo simulation of derivative prices or other functionals of diffusion processes. This means that we study the weak order of convergence of discretetime approximations. By truncating appropriately the Wagner-Platen expansion (see Stochastic Taylor **Expansions**) one obtains *weak Taylor schemes*. The desired order of weak convergence determines the kind of truncation that must be used [6]. However, the truncations will be different from those required for the strong convergence of a comparable order, as described in Stochastic Differential Equations: Scenario Simulation. In general, weak Taylor schemes involve fewer terms compared with the strong Taylor schemes of the same order.

## **Euler and Simplified Weak Euler Scheme**

The simplest weak Taylor scheme is the Euler scheme (see also **Stochastic Taylor Expansions**), which has the form

$$Y_{n+1} = Y_n + a \Delta + b \Delta W_n \tag{11}$$

with  $\Delta W_n = W_{\tau_{n+1}} - W_{\tau_n}$  and initial value  $Y_0 = X_0$ , where  $\tau_n = n\Delta$ ,  $\Delta > 0$ . Here and in the following, we suppress in our notation of coefficient functions, as a and b, the dependence on  $\tau_n$  and  $Y_n$ .

The Euler scheme (11) corresponds to the truncated Wagner-Platen expansion that contains only the time integral and the single Itô integral with respect to the Wiener process. The Euler scheme has order of weak convergence  $\beta = 1.0$  if the drift and diffusion coefficient are sufficiently smooth and regular.

For weak convergence, we only need to approximate the probability measure induced by the process  $X$ . Here, we can replace the Gaussian increments  $\Delta W_n$  in (11) by other simpler random variables  $\Delta \hat{W}_n$ with similar moment properties as  $\Delta W_n$ . We can thus obtain a simpler scheme by choosing more easily generated random variables. This leads to the *simplified* weak Euler scheme

$$Y_{n+1} = Y_n + a \Delta + b \Delta \hat{W}_n \tag{12}$$

where the  $\Delta \hat{W}_n$  are independent random variables with moments satisfying the moment-matching condition

$$\left| E\left(\Delta \hat{W}_{n}\right) \right| + \left| E\left(\left(\Delta \hat{W}_{n}\right)^{3}\right) \right|$$
  
+ 
$$\left| E\left(\left(\Delta \hat{W}_{n}\right)^{2}\right) - \Delta \right| \leq K \Delta^{2}$$
(13)

for some constant  $K$ . The simplest example of such a simplified random variable  $\Delta \hat{W}_n$  to be used in equation (12) is a two-point distributed random variable with

$$P\left(\Delta\hat{W}_n = \pm\sqrt{\Delta}\right) = 1/2\tag{14}$$

When the drift and diffusion coefficients are only Hölder continuous, then it has been shown in  $[8]$  that the Euler scheme still converges weakly, but with some weak order  $\beta < 1.0$ .

#### Weak Order 2.0 Taylor Scheme

Now, let us consider the Taylor scheme of weak order  $\beta = 2.0$ . This scheme is obtained by adding all of the double stochastic integrals from the Wagner-Platen expansion to the terms of the Euler scheme, as shown in Stochastic Taylor Expansions. This scheme was

first proposed in [9]. The weak order 2.0 Taylor *scheme* has the form

$$Y_{n+1} = Y_n + a \Delta + b \Delta W_n + \frac{1}{2} b b' \left\{ (\Delta W_n)^2 - \Delta \right\}$$
  
+  $a' b \Delta Z_n + \frac{1}{2} \left( a a' + \frac{1}{2} a'' b^2 \right) \Delta^2$   
+  $\left( a b' + \frac{1}{2} b'' b^2 \right) \left\{ \Delta W_n \Delta - \Delta Z_n \right\}$  (15)

The random variable  $\Delta Z_n = \int_{\tau_n}^{\tau_{n+1}} \int_{\tau_n}^{s_2} dW_{s_1} ds_2$  represents a stochastic double integral. One can easily generate the pair of correlated Gaussian random variables  $\Delta W_n$  and  $\Delta Z_n$  from independent Gaussian random variables.

Under the weak convergence criterion, one has more freedom than under the strong convergence criterion (see Stochastic Differential Equations: Scenario Simulation) in constructing the random variables in a discrete-time weak approximation. For instance, from the above scheme, one can derive the simplified weak order 2.0 Taylor scheme

$$Y_{n+1} = Y_n + a \Delta + b \Delta \hat{W}_n$$
  
+ 1/2 b b'  $\left\{ \left( \Delta \hat{W}_n \right)^2 - \Delta \right\}$   
+ 1/2  $(a' b + a b' + 1/2 b'' b^2) \Delta \hat{W}_n \Delta$   
+ 1/2  $(a a' + 1/2 a'' b^2) \Delta^2$  (16)

Here the simplified random variable  $\Delta \hat{W}_n$  must satisfy the moment-matching condition

$$\left| E\left(\Delta \hat{W}_{n}\right) \right| + \left| E\left(\left(\Delta \hat{W}_{n}\right)^{3}\right) \right|$$
  
+ 
$$\left| E\left(\left(\Delta \hat{W}_{n}\right)^{5}\right) \right| + \left| E\left(\left(\Delta \hat{W}_{n}\right)^{2}\right) - \Delta \right|$$
  
+ 
$$\left| E\left(\left(\Delta \hat{W}_{n}\right)^{4}\right) - 3\Delta^{2} \right| \leq K \Delta^{3}$$
  
(17)

for some constant K. For instance, an  $N(0, \Delta)$ Gaussian distributed random variable satisfies the condition (17). So also does a three-point distributed random variable  $\Delta \hat{W}_n$  with

$$P\left(\Delta \hat{W}_n = \pm \sqrt{3\Delta}\right) = \frac{1}{6} \quad \text{and}$$
$$P\left(\Delta \hat{W}_n = 0\right) = \frac{2}{3} \tag{18}$$

Under appropriate conditions on the drift and diffusion coefficients, the scheme converges with weak order 2.0 [6].

## Weak Order 3.0 Taylor Scheme

As shown in [6], Taylor schemes of weak order  $\beta = 3.0$  need to include from the Wagner–Platen expansion all of the multiple Itô integrals of up to multiplicity three. The following simplified weak order 3.0 Taylor scheme can he obtained

$$Y_{n+1} = Y_n + a \Delta + b \Delta \tilde{W}_n + \frac{1}{2} L^1 b \left\{ \left( \Delta \tilde{W}_n \right)^2 - \Delta \right\}$$
  
+  $L^1 a \Delta \tilde{Z}_n + \frac{1}{2} L^0 a \Delta^2 + L^0 b$   
 $\times \left\{ \Delta \tilde{W}_n \Delta - \Delta \tilde{Z}_n \right\}$   
+  $\frac{1}{6} \left( L^0 L^0 b + L^0 L^1 a + L^1 L^0 a \right) \Delta \tilde{W}_n \Delta^2$   
+  $\frac{1}{6} \left( L^1 L^1 a + L^1 L^0 b + L^0 L^1 b \right)$   
 $\times \left\{ \left( \Delta \tilde{W}_n \right)^2 - \Delta \right\} \Delta$   
+  $\frac{1}{6} L^0 L^0 a \Delta^3 + \frac{1}{6} L^1 L^1 b$   
 $\times \left\{ \left( \Delta \tilde{W}_n \right)^2 - 3\Delta \right\} \Delta \tilde{W}_n$  (19)

Here  $\Delta \tilde{W}_n$  and  $\Delta \tilde{Z}_n$  are correlated Gaussian random variables with

$$\Delta \tilde{W}_n \sim N(0, \Delta), \qquad \Delta \tilde{Z}_n \sim N\left(0, 1/3 \,\Delta^3\right)\n$$
(20)

and covariance

$$E\left(\Delta\tilde{W}_n\,\Delta\tilde{Z}_n\right) = 1/2\,\Delta^2\tag{21}$$

Furthermore, we use here the operators

$$L^{0} = \frac{\partial}{\partial t} + a \frac{\partial}{\partial x} + \frac{1}{2} b^{2} \frac{\partial^{2}}{\partial x^{2}}$$
 (22)

and  $L^1 = b \frac{\partial}{\partial x}$ 

## Weak Order 4.0 Taylor Scheme

To construct the weak order 4.0 Taylor scheme, we also need to include all of the fourth-order multiple stochastic integrals from the Wagner-Platen expansion.

In the case of particular SDEs, for instance those with additive noise, one obtains highly accurate schemes in this manner. For accurate Monte Carlo simulation, the following *simplified weak order* 4.0 *Taylor scheme for additive noise* can be used:

$$Y_{n+1} = Y_n + a \Delta + b \Delta \tilde{W}_n + \frac{1}{2} L^0 a \Delta^2$$
  
+  $L^1 a \Delta \tilde{Z}_n + L^0 b \left\{ \Delta \tilde{W}_n \Delta - \Delta \tilde{Z}_n \right\}$   
+  $\frac{1}{3!} \left\{ L^0 L^0 b + L^0 L^1 a \right\} \Delta \tilde{W}_n \Delta^2$   
+  $L^1 L^1 a \left\{ 2 \Delta \tilde{W}_n \Delta \tilde{Z}_n - \frac{5}{6} \left( \Delta \tilde{W}_n \right)^2 \Delta \right\}$   
-  $\frac{1}{6} \Delta^2 \right\}$   
+  $\frac{1}{3!} L^0 L^0 a \Delta^3 + \frac{1}{4!} L^0 L^0 L^0 a \Delta^4$   
+  $\frac{1}{4!} \left\{ L^1 L^0 L^0 a + L^0 L^1 L^0 a \right\}$   
+  $L^0 L^0 L^1 a + L^0 L^0 L^0 b \right\} \Delta \tilde{W}_n \Delta^3$   
+  $\frac{1}{4!} \left\{ L^1 L^1 L^0 a + L^0 L^1 L^1 a + L^1 L^0 L^1 a \right\}$   
 $\times \left\{ \left( \Delta \tilde{W}_n \right)^2 - \Delta \right\} \Delta^2$   
+  $\frac{1}{4!} L^1 L^1 L^1 a \Delta \tilde{W}_n \left\{ \left( \Delta \tilde{W}_n \right)^2 - 3\Delta \right\} \Delta \right\} \Delta$   
(23)

Here  $\Delta \tilde{W}_n$  and  $\Delta \tilde{Z}_n$  are correlated Gaussian random variables with  $\Delta \tilde{W}_n \sim N(0, \Delta), \ \Delta \tilde{Z}_n \sim N(0, \frac{1}{2}\Delta^3)$ and  $E(\Delta \tilde{W}_n \Delta \tilde{Z}_n) = \frac{1}{2} \Delta^2$ . The weak order of convergence of the above schemes is derived in [6].

# **Explicit Weak Schemes**

Higher order weak Taylor schemes require the evaluation of derivatives of various orders of the drift and diffusion coefficients. We can construct derivativefree discrete-time weak approximations, which avoid the use of such derivatives.

The following *explicit weak order* 2.0 *scheme* was suggested by Platen

$$Y_{n+1} = Y_n + 1/2 \left( a \left( \bar{\Upsilon}_n \right) + a \right) \Delta$$
  
+ 1/4 \left( b \left( \bar{\That{\Theta}}\_n^+ \right) + b \left( \bar{\Theta}\_n^- \right) + 2b \right) \Delta \hat{W}\_n \right)  
+ 1/4 \left( b \left( \bar{\Theta}\_n^+ \right) - b \left( \bar{\Theta}\_n^- \right) \right)  
\times \left\{ \left( \Delta \hat{W}\_n \right)^2 - \Delta \right\} \Delta^{1/2} \qquad (24)

with supporting values

$$\bar{\Upsilon}_n = Y_n + a \,\Delta + b \,\Delta \hat{W}_n \tag{25}$$

and

$$\bar{\Upsilon}_{n}^{\pm} = Y_{n} + a \,\Delta \pm b \,\sqrt{\Delta} \tag{26}$$

Here  $\Delta \hat{W}_n$  is required to satisfy the moment condition (17). This means,  $\Delta \hat{W}_n$  can be, for instance, Gaussian or three-point distributed with

$$P\left(\Delta \hat{W}_n = \pm \sqrt{3\Delta}\right) = 1/6$$
 and  
 $P\left(\Delta \hat{W}_n = 0\right) = 2/3$  (27)

By comparing equation  $(24)$  with the corresponding simplified weak Taylor scheme (16), one notes that equation  $(24)$  avoids the derivatives that appear in equation  $(16)$  by using additional supporting values.

For *additive noise* the second-order weak scheme  $(24)$  reduces to the relatively simple algorithm

$$Y_{n+1} = Y_n + 1/2 \left\{ a \left( Y_n + a \Delta + b \Delta \hat{W}_n^j \right) + a \right\} \Delta$$
$$+ b \Delta \hat{W}_n^j \tag{28}$$

For the case with additive noise, one finds in [6] the explicit weak order 3.0 scheme

$$Y_{n+1} = Y_n + a \Delta + b \Delta \hat{W}_n$$
  
+  $\frac{1}{2} \left( a_{\zeta_n}^+ + a_{\zeta_n}^- - \frac{3}{2} a - \frac{1}{4} \left( \tilde{a}_{\zeta_n}^+ + \tilde{a}_{\zeta_n}^- \right) \right) \Delta$   
+  $\sqrt{\frac{2}{\Delta}} \left( \frac{1}{\sqrt{2}} \left( a_{\zeta_n}^+ - a_{\zeta_n}^- \right) - \frac{1}{4} \left( \tilde{a}_{\zeta_n}^+ - \tilde{a}_{\zeta_n}^- \right) \right) \zeta_n \Delta \hat{Z}_n$   
+  $\frac{1}{6} \Big[ a \left( Y_n + \left( a + a_{\zeta_n}^+ \right) \Delta + \left( \zeta_n + \varrho_n \right) b \sqrt{\Delta} \right) - a_{\zeta_n}^+ - a_{\varrho_n}^+ + a \Big]$   
 $\times \Big[ \left( \zeta_n + \varrho_n \right) \Delta \hat{W}_n \sqrt{\Delta} + \Delta$   
+  $\zeta_n \varrho_n \left\{ \left( \Delta \hat{W}_n \right)^2 - \Delta \right\} \Big]$ (29)

with

$$a_{\phi}^{\pm} = a \left( Y_n + a \Delta \pm b \sqrt{\Delta} \phi \right) \tag{30}$$

and

$$\tilde{a}_{\phi}^{\pm} = a \left( Y_n + 2a \Delta \pm b \sqrt{2\Delta} \phi \right) \tag{31}$$

where  $\phi$  is either  $\zeta_n$  or  $\varrho_n$ . Here, one can use two correlated Gaussian random variables  $\Delta \hat{W}_n \sim N(0, \Delta)$ and  $\Delta \hat{Z}_n \sim N(0, 1/3 \Delta^3)$  with  $E(\Delta \hat{W}_n \Delta \hat{Z}_n) =$  $1/2\Delta^2$ , together with two independent two-point distributed random variables  $\zeta_n$  and  $\varrho_n$  with

$$P(\zeta_n = \pm 1) = P(\varrho_n = \pm 1) = 1/2 \qquad (32)$$

## **Extrapolation Methods**

Extrapolation provides an efficient, yet simple way of obtaining a higher order weak approximation when using only lower order weak schemes. Only equidistant time discretizations of the time interval  $[0, T]$ with  $\tau_{n_T} = T$  are used in what follows. As before, we denote the considered discrete-time approximation with time step size  $\Delta > 0$  by  $Y^{\Delta}$ , with value  $Y_{\tau_n}^{\Delta} = Y_n^{\Delta}$  at the discretization time  $\tau_n$ , and the corresponding approximation with twice this step size by  $Y^{2\Delta}$ , and so on.

Suppose that we have evaluated *via* simulation the functional  $\sim$  A

$$E\left(g\left(Y_{T}^{\Delta}\right)\right)$$

of a weak order 1.0 approximation using, say, the Euler scheme (11) or the simplified Euler scheme (12) with step size  $\Delta$ . Let us repeat this Monte Carlo simulation with the double step size  $2\Delta$  to obtain a Monte Carlo estimate of the functional

$$E\left(g\left(Y_{T}^{2\Delta}\right)\right)$$

We can then combine these two functionals to obtain the *weak order* 2.0 *extrapolation* 

$$V_{g,2}^{\Delta}(T) = 2E\left(g\left(Y_{T}^{\Delta}\right)\right) - E\left(g\left(Y_{T}^{2\Delta}\right)\right) \tag{33}$$

which was proposed in [13]. It is a stochastic generalization of the well-known *Richardson extrapolation*.

As is shown in [6], if a weak method exhibits a certain representation of the leading error term, then a corresponding extrapolation method can be constructed. For instance, one can use a weak order  $\beta = 2.0$  approximation  $Y^{\Delta}$  and extrapolate it to obtain a fourth-order weak approximation of the targeted functional. A *weak order* 4.0 *extrapolation* has the form

$$V_{g,4}^{\Delta}(T) = 1/21 \bigg[ 32 E \left( g \left( Y_T^{\Delta} \right) \right)$$
$$- 12 E \left( g \left( Y_T^{2\Delta} \right) \right) + E \left( g \left( Y_T^{4\Delta} \right) \right) \bigg]$$
(34)

Suitable weak order 2.0 approximations include the weak order 2.0 Taylor scheme (15), the simplified weak order  $2.0$  Taylor scheme (16), and the explicit weak order  $2.0$  scheme (24).

The practical use of extrapolations of discrete time approximations depends strongly on the numerical stability of the underlying weak schemes. These weak methods need to have almost identical leading error coefficients for a wide range of step sizes and should yield numerically stable simulation results; see Stochastic Differential Equations: Scenario Simulation.

## Implicit Methods

In Monte Carlo simulation, the numerical stability of a scheme has highest priority. Introducing some type of implicitness into a scheme usually improves its numerical stability. The simplest implicit weak schemes can be found in the family of drift implicit simplified Euler schemes

$$Y_{n+1} = Y_n + \{(1 - \alpha) a(Y_n) + \alpha a(Y_{n+1})\} \Delta$$
  
+  $b(Y_n) \Delta \hat{W}_n$  (35)

where the random variables  $\Delta \hat{W}_n$  are independent two-point distributed with

$$P\left(\Delta\hat{W}_n = \pm\sqrt{\Delta}\right) = 1/2\tag{36}$$

The parameter  $\alpha$  is the *degree of drift implicitness*. With  $\alpha = 0$ , the scheme (35) reduces to the simplified Euler scheme (12), whereas with  $\alpha = 0.5$  it represents a stochastic generalization of the trapezoidal method. Under sufficient regularity conditions, one can show that the scheme (35) converges with weak order  $\beta = 1.0$ . The scheme (35) is A-stable for  $\alpha \in [0.5, 1]$ , whereas for  $\alpha \in [0, 0.5)$  its region of A-stability, in the sense of what is discussed in Stochastic **Differential Equations: Scenario Simulation**, is the interior of the interval that begins at  $-2(1-2\alpha)^{-1}$ and finishes at 0.

The possible use of bounded random variables in weak simplified schemes allows us to construct fully implicit weak schemes that is, algorithms where also the approximate diffusion term becomes implicit.

The fully implicit weak Euler scheme has the form

$$Y_{n+1} = Y_n + \bar{a}(Y_{n+1}) \Delta + b(Y_{n+1}) \Delta \hat{W}_n \qquad (37)$$

where  $\Delta \hat{W}_n$  is as in equation (35) and  $\bar{a}$  is some adjusted drift coefficient defined by

$$\bar{a} = a - b \, b' \tag{38}$$

The drift adjustment is necessary, otherwise the approximation would not converge toward the correct solution of the given Itô SDE.

We also mention a family of implicit weak Euler schemes

$$Y_{n+1} = Y_n + \left\{ \alpha \, \bar{a}_{\eta}(Y_{n+1}) + (1 - \alpha) \, \bar{a}_{\eta}(Y_n) \right\} \Delta$$
$$+ \left\{ \eta \, b(Y_{n+1}) + (1 - \eta) \, b(Y_n) \right\} \Delta \hat{W}_n \tag{39}$$

where the random variables  $\Delta \hat{W}_n$  are as in equation (35) and the corrected drift coefficient  $\bar{a}_{\eta}$  is defined

as

$$\bar{a}_{\eta} = a - \eta \, b \, \frac{\partial b}{\partial x} \tag{40}$$

for  $\alpha, \eta \in [0, 1]$ .

One can avoid the calculation of derivatives in the above family of implicit schemes by using differences instead. The following *implicit weak order* 2.0 *scheme* can be found in  $[11]$ , where

$$Y_{n+1} = Y_n + 1/2 \ (a + a \ (Y_{n+1})) \ \Delta$$
  
+ 1/4 \ \ (b \ (\tilde{\gamma}\_n^+) + b \ (\tilde{\gamma}\_n^-) + 2 b \) \ \ \Delta \hat{W}\_n \\  
+ 1/4 \ (b \ (\tilde{\gamma}\_n^+) - b \ (\tilde{\gamma}\_n^-) \) \  
\ \ \ \ \ \ \left( \Delta \hat{W}\_n \right)^2 - \Delta \right\} \ \Delta^{-1/2} \qquad (41)

with supporting values

$$\bar{\Upsilon}_{n}^{\pm} = Y_{n} + a \,\Delta \pm b \,\sqrt{\Delta} \tag{42}$$

Here, the random variable  $\Delta \hat{W}_n$  can be chosen as in (18).

Note that the scheme  $(39)$  is A-stable. In [6], it is shown that the above second-order weak scheme converges under appropriate conditions with weak order  $\beta = 2.0$ .

# **Weak Predictor-Corrector Methods**

In general, implicit schemes require an algebraic equation to be solved at each time step. This imposes an additional computational burden. However, without giving a weak scheme some kind of implicitness the simulation might not turn out to be of much practical use due to inherent numerical instabilities.

Predictor-corrector methods are similar to implicit methods but do not require the solution of an algebraic equation at each time step. They are used mainly because of their good numerical stability properties, which they inherit from the implicit counterparts of their corrector. The following predictor-corrector methods can be found in [11].

One has the following family of weak order 1.0 *predictor–corrector methods* with corrector

$$Y_{n+1} = Y_n + \left\{ \alpha \, \bar{a}_{\eta}(\bar{Y}_{n+1}) + (1 - \alpha) \, \bar{a}_{\eta}(Y_n) \right\} \Delta$$
$$+ \left\{ \eta \, b(\bar{Y}_{n+1}) + (1 - \eta) \, b(Y_n) \right\} \Delta \hat{W}_n \tag{43}$$

for  $\alpha, \eta \in [0, 1]$ , where

$$\bar{a}_{\eta} = a - \eta \, b \, \frac{\partial b}{\partial x} \tag{44}$$

and with predictor

$$\bar{Y}_{n+1} = Y_n + a \,\Delta + b \,\Delta \hat{W}_n \tag{45}$$

Here, the random variables  $\Delta \hat{W}_n$  are as in (14). Note that the corrector (43) with  $\eta > 0$  allows to include some implicitness in the diffusion terms. This scheme often provides efficient and numerically reliable methods for appropriate choices of  $\alpha$  and  $\eta$ . By performing the Monte Carlo simulation with different parameter choices for  $\alpha$  and  $\eta$  one can obtain useful information about the numerical stability of the scheme for the given application.

A weak order 2.0 predictor–corrector method is obtained by choosing as corrector

$$Y_{n+1} = Y_n + 1/2 \left\{ a \left( \bar{Y}_{n+1} \right) + a \right\} \Delta + \Psi_n \qquad (46)$$

with

$$\Psi_n = b \,\Delta \hat{W}_n + 1/2 \,b \,b' \left\{ \left( \Delta \hat{W}_n \right)^2 - \Delta \right\} \\
+ 1/2 \left( a \,b' + \frac{1}{2} \,b^2 \,b'' \right) \Delta \hat{W}_n \,\Delta \tag{47}$$

and as predictor

$$\bar{Y}_{n+1} = Y_n + a \Delta + \Psi_n + 1/2 a' b \Delta \hat{W}_n \Delta + 1/2 (a a' + 1/2 a'' b^2) \Delta^2$$
(48)

Here the random variable  $\Delta \hat{W}_n$  can be, for instance,  $N(0, \Delta)$  Gaussian or three-point distributed as in equation  $(18)$ .

Another derivative-free weak order 2.0 predic*tor-corrector method* has corrector

$$Y_{n+1} = Y_n + 1/2 \left\{ a \left( \bar{Y}_{n+1} \right) + a \right\} \Delta + \phi_n \qquad (49)$$

where

$$\phi_n = 1/4 \left( b \left( \bar{\Upsilon}_n^+ \right) + b \left( \bar{\Upsilon}_n^- \right) + 2 b \right) \Delta \hat{W}_n \n+ 1/4 \left( b \left( \bar{\Upsilon}_n^+ \right) - b \left( \bar{\Upsilon}_n^- \right) \right) \n\times \left\{ \left( \Delta \hat{W}_n \right)^2 - \Delta \right\} \Delta^{-1/2} \n$$
(50)

with supporting values

$$\bar{\Upsilon}_n^{\pm} = Y_n + a \,\Delta \pm b \,\sqrt{\Delta} \tag{51}$$

and with predictor

$$\bar{Y}_{n+1} = Y_n + 1/2 \left\{ a \left( \bar{\Upsilon}_n \right) + a \right\} \Delta + \phi_n \qquad (52)$$

using the supporting value

$$\bar{\Upsilon}_n = Y_n + a \,\Delta + b \,\Delta \hat{W}_n \tag{53}$$

Here the random variable  $\Delta \hat{W}_n$  can be chosen as in equation  $(18)$ .

Predictor-corrector methods of the above kind have been successfully used in the Monte Carlo simulation of various asset price models, see, for instance, [4].

## References

- Fishman, G.S. (1996). Monte Carlo: Concepts, Algo-[1] rithms and Applications, Springer.
- Glasserman, P. (2004). Monte Carlo Methods in Finan-[2] cial Engineering, Applied Mathematics, Springer, Vol. 53.
- Hammersley, J.M. & Handscomb, D.C. (1964). Monte [3] Carlo Methods, Methuen, London.
- Hunter, C.J., Jäckel, P. & Joshi, M.S. (2001). Getting [4] the drift, Risk  $14(7)$ ,  $81-84$ .
- [5] Jäckel, P. (2002). Monte Carlo Methods in Finance, John Wiley & Sons.
- Kloeden, P.E. & Platen, E. (1999). Numerical Solution of [6] Stochastic Differential Equations, Applied Mathematics, Springer, Vol. 23 (Third Printing).

# **8 Monte Carlo Simulation for Stochastic Differential Equations**

- [7] Kloeden, P.E., Platen, E. & Schurz, H. (2003). *Numerical Solution of SDE's Through Computer Experiments*, Universitext, Springer (Third Corrected Printing).
- [8] Mikulevicius, R. & Platen, E. (1991). Rate of convergence of the Euler approximation for diffusion processes, *Mathematische Nachrichten* **151**, 233–239.
- [9] Milstein, G.N. (1978). A method of second order accuracy integration of stochastic differential equations, *Theory of Probability and its Applications* **23**, 396–401.
- [10] Milstein, G.N. (1995). *Numerical Integration of Stochastic Differential Equations*, Mathematics and Its Applications, Kluwer.
- [11] Platen, E. (1995). On weak implicit and predictor– corrector methods, *Mathematics and Computers in Simulation* **38**, 69–76.
- [12] Platen, E. & Heath, D. (2006). *A Benchmark Approach to Quantitative Finance*, Springer.

[13] Talay, D. & Tubaro, L. (1990). Expansion of the global error for numerical schemes solving stochastic differential equations, *Stochastic Analysis and Applications* **8**(4), 483–509.

# **Related Articles**

**Backward Stochastic Differential Equations: Numerical Methods**; **LIBOR Market Model**; **LIBOR Market Models: Simulation**; **Pseudorandom Number Generators**; **Simulation of Square-root Processes**; **Stochastic Differential Equations: Scenario Simulation**; **Stochastic Differential Equations with Jumps: Simulation**; **Stochastic Integrals**; **Stochastic Taylor Expansions**; **Variance Reduction**.

NICOLA BRUTI-LIBERATI & ECKHARD PLATEN
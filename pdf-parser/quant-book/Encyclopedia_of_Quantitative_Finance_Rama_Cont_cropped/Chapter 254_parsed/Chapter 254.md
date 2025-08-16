# **Tikhonov Regularization**

An important issue in quantitative finance is *model calibration*. The calibration problem is the *inverse* of the pricing problem. Instead of computing prices in a model with given values for its parameters, one wishes to compute the values of the model parameters that are consistent with observed prices (up to the bid-ask spread).

Many examples of such inverse problems are illposed. Recall that a problem is *well posed* (as defined by Hadamard) if its solution exists, is unique, and depends continuously on its input data. Thus there are three reasons for which a problem might be ill posed:

- ٠ It admits no solution.
- It admits more than one solution.
- The solution/solutions to the inverse problem does/do not depend on the input data in a continuous way.

In the case of calibration problems in finance. except for trivial situations, there exists typically *no* instance of a given class of models that is exactly consistent with a full calibration data set, including a number of option prices, a zero-coupons curve, an expected dividend yield curve on the underlying, and so on. However, there are often various instances of a given class of models that fit the data within the *bid-ask spread.* In such cases, if one perturbs the data (e.g., if the observed prices change by some small amount between today and tomorrow), it is quite typical that a numerically determined best fit solution of the calibration problem switches from one "basin of attraction" to the other, and thus the numerically determined solution is *not stable* either.

To get a well-posed problem, we need to introduce some regularization. The most widely known and applicable regularization method is the Tikhonov(-*Phillips*) regularization method [9, 14, 16].

## Tikhonov Regularization of Nonlinear **Inverse Problems**

We consider a Hilbert space  $\mathcal{H}$ , a closed convex nonvoid subset  $\mathcal{A}$  of  $\mathcal{H}$ , a direct operator ("pricing functional")

$$\mathcal{H} \supseteq \mathcal{A} \ni a \xrightarrow{\Pi} \Pi(a) \in \mathbb{R}^d \tag{1}$$

(so  $a$  corresponds to the set of model parameters), noisy data ("observed prices")  $\pi^{\delta}$ , and a *prior*  $a_0 \in \mathcal{H}$ ( $a$  priori guess for  $a$ ). The Tikhonov regularization method for *inverting*  $\prod$  at  $\pi^{\delta}$ , or estimating the model parameter *a* given the observation  $\pi^{\delta}$ , consists in

reformulating the inverse problem as the following nonlinear least squares problem:

$$\min_{a \in \mathcal{A}} \left\| \Pi \left( a \right) - \pi^{\delta} \right\|^2 \tag{2}$$

to ensure *existence* of a solution;

- selecting the solutions of the previous nonlinear  $\bullet$ least squares problem that minimize  $\|a - a_0\|^2$ over the set of all solutions; and
- introducing a trade-off between accuracy and reg- $\bullet$ ularity, parameterized by a level of regularization  $\alpha > 0$ , to ensure *stability*.

More precisely, we introduce the following *cost* criterion:

$$J_{\alpha}^{\delta}(a) \equiv \left\| \Pi(a) - \pi^{\delta} \right\|^{2} + \alpha \left\| a - a_{0} \right\|^{2} \quad (3)$$

Given  $\alpha$ ,  $\delta$ , and a further parameter  $\eta$ , where  $\eta$ represents an error tolerance on the minimization, we define a regularized solution to the inverse problem for  $\Pi$  at  $\pi^{\delta}$  as any model parameter  $a_{\alpha}^{\delta,\eta} \in \mathcal{A}$  such that

$$J_{\alpha}^{\delta} \left( a_{\alpha}^{\delta,\eta} \right) \leq J_{\alpha}^{\delta} \left( a \right) + \eta, \quad a \in \mathcal{A} \tag{4}$$

Under suitable assumptions, one can show that the regularized inverse problem is well posed, as follows. We first postulate that the direct operator  $\Pi$  satisfies the following regularity assumption.

**Assumption 1 (Compactness)**  $\prod (a_n)$  *converges to*  $\n\Pi\n$  (a) in  $\mathbb{R}^d$  if  $a_n$  weakly converges to a in  $\mathcal{H}$ .

We then have the following *stability* result.

**Theorem 1 (Stability)** Let  $\pi^{\delta_n} \to \pi^{\delta}$ ,  $\eta_n \to 0$  when  $n \to \infty$ . Then any sequence of regularized solutions  $a_{\alpha}^{\delta_n,\eta_n}$  admits a subsequence that converges toward a regularized solution  $a_{\alpha}^{\delta,\eta=0}$ .

Assuming further that the data lie in the range of the model leads to *convergence* properties of regularized solutions to (unregularized) solutions of the inverse problem as  $midi \rightarrow 0$ . Let us then make the following additional assumption on  $\Pi$ .

#### Assumption 2 (Range Property) $\pi \in \Pi(\mathcal{A})$ .

**Definition 1** By an  $a_0$ -solution to the inverse problem for  $\Pi$  at  $\pi$ , we mean any  $a \in \operatorname*{Argmin}$   $\|\mathbf{a} - \mathbf{a}_0\|$ . Note that the set of  $a_0$ -solutions is non-empty, by Assumption 2.

Theorem 2 (Convergence; see, for instance, Theorem 2.3 of Engl et al [10]) Let the perturbed parameters  $\alpha_n$ ,  $\delta_n$ ,  $\eta_n$  and the perturbed data  $\pi_n \in \mathbb{R}^d$ satisfy

$$\begin{array}{lll}\n(n \in \mathbb{N}) & \|\pi - \pi_n\| \le \delta_n & (5) \\
(n \to \infty) & \alpha_n, \quad \delta_n^2/\alpha_n, \quad \eta_n/\alpha_n & \longrightarrow & 0\n\end{array}$$

Then any sequence of regularized solutions  $a_{\alpha}^{\delta_n,\eta_n}$ admits a subsequence that converges toward an  $a_0$ solution a of the inverse problem for  $\Pi$  at  $\pi$ . In particular, in the case when this problem admits a unique  $a_0$ -solution  $a$ ,  $a_{\alpha_n}^{\delta_n,\eta_n}$  converges to  $a$ .

**Remark 1** In the special case where the direct operator  $\Pi$  is linear, Tikhonov regularization thus appears as an approximating scheme for the pseudoinverse of  $\Pi$ .

Finally, assuming further regularity of  $\Pi$ , one can get convergence rates estimates, uniform over all data  $\pi \in \Pi(\mathcal{A})$  sufficiently close and smooth with respect to the prior  $a_0$  (so that the additional *source condition* 12 is satisfied). Let us thus make the following additional assumption on  $\Pi$ .

#### Assumption 3 (Twice Gateaux Differentiability)

There exist linear and bilinear forms  $d\Pi(a)$  on  $\mathcal{H}$ and  $d^2\Pi(a)$  on  $\mathcal{H}^2$  such that

$$\begin{aligned} \Pi\left(a+\varepsilon h\right) &= \Pi\left(a\right) + \varepsilon d\Pi\left(a\right) \cdot h \\ &+ \frac{\varepsilon^2}{2} d^2 \Pi\left(a\right) \cdot \left(h, h\right) + \mathsf{o}\left(\varepsilon^2\right); \\ a, a+h \in \mathcal{A} \qquad (6) \\ \|d\Pi\left(a\right) \cdot h\| &\leq C \left\|h\right\|, \\ \|d^2 \Pi\left(a\right) \cdot \left(h, h'\right)\| &\leq C \left\|h\right\| \left\|h'\right\|; \end{aligned}$$

$$a \in \mathcal{A} \ , \quad h, h' \in \mathcal{H}$$
 (7)

where C is a constant independent of  $a \in A$ .

In the following theorem, the operator

$$d\Pi(a)^* : \mathbb{R}^d \ni \lambda \mapsto d\Pi(a)^* \lambda \in \mathcal{H}^1 \tag{8}$$

denotes the *adjoint* of

$$d\Pi(a) : \mathcal{H}^1 \ni h \mapsto d\Pi(a) \, h \in \mathbb{R}^d \tag{9}$$

in the sense that (see  $[9]$ )

$$\langle h, \mathrm{d}\Pi(a)^{\star}\lambda\rangle_{\mathcal{H}^{1}} = \lambda' \mathrm{d}\Pi(a).h \; ; \quad (h,\lambda) \in \mathcal{H}^{1} \times \mathbb{R}^{d}$$
(10)

Theorem 3 (Convergence Rates; see, for instance, Theorem 10.4 of Engl et al [9]) Assume

$$\begin{array}{cc} (n \in \mathbb{N}) & \|\pi - \pi_n\| \le \delta_n, \\\\ (n \to \infty) & \alpha_n \longrightarrow 0, \quad \alpha_n \sim \delta_n, \quad \eta_n = \mathcal{O}\left(\delta_n^2\right) \end{array} \tag{11}$$

Then  $\|a_{\alpha_n}^{\delta_n,\eta_n}-a\| = O(\sqrt{\delta_n})$ , for any  $a_0$ -solution a of the inverse problem for  $\Pi$  at  $\pi$  such that

$$a - a_0 = d\Pi \left( a \right)^* \lambda \tag{12}$$

for some  $\lambda$  sufficiently small in  $\mathbb{R}^d$  (in particular, there exists at most one such  $a_0$ -solution a).

**Remark 2** An interesting feature of Tikhonov regularization is that the data set  $\pi$  does not need to belong to the range of the direct operator for applicability of the method-even if Assumption 2 is the simplest assumption for the previous results regarding convergence and convergence rates (in fact, a minimal assumption for such results is the existence of a least squares solution to the inverse problem; see Proposition 3.2 of Binder et al [2]).

An important issue, in practice, is the choice of the *regularization parameter*  $\alpha$  that determines the tradeoff between accuracy and regularity in the method. To set  $\alpha$ , the two main approaches are

- *a priori* methods, in which the choice of  $\alpha$  only depends on  $\delta$ , the level of noise on the data (such as the size of the bid-ask spread, in the case of market prices data in finance);
- more general *a posteriori* methods, in which  $\alpha$ may depend on the data in a less specific way.

In applications to calibration problems in finance, the most commonly used method for choosing  $\alpha$ is the *a posteriori* method based on the so-called discrepancy principle, which consists in choosing the greatest level of  $\alpha$  for which the "distance"  $\|\Pi(a_{\alpha}^{\delta,\eta}) - \pi^{\delta}\|$  (for given  $\delta, \eta$ ) does not exceed the level of noise  $\delta$  on the observations (as measured by the bid-ask spread).

## Implementation

For implementation purposes, the minimization problem 3 is discretized, and thus it effectively becomes a nonlinear minimization problem on (some subset of)  $\mathbb{R}^k$  (see, e.g., [13]), where k is the number of model parameters to be estimated.

In the case of a strictly convex cost criterion  $J = J_{\alpha}^{\delta}$  in equation 3, and if, additionally, J is differentiable, one can prove the convergence to the (unique) minimum of various gradient descent algorithms. These consist, at each iteration, in making a step of a certain length (fixed-step descent vs. optimal step descent) in a direction defined by the gradient  $\nabla J$  in the current step of the algorithm, in combination with, in some variants of the method (conjugate gradient method, quasi-Newton algorithms, etc.), the  $gradient(s) \nabla J$  in the previous step(s).

In the *nonstrictly convex* case, (actually, in the context of calibration problems in finance,  $J$  is typically not even convex with respect to  $a$ ), or if the cost criterion is only almost everywhere differentiable (as in the American calibration problem, see Remark 3 (i)), such algorithms can still be used, in which case, they typically converge to one among many  $local \ minima \ of \ J$ .

When there are no constraints (the case when  $\mathcal{A} =$  $\mathcal{H}$ ), the minimization problem is, in practice, much easier, and many implementations of the related gradient descent algorithms are available (e.g., in [15]). As for constrained problems, a state-of-the-art opensource implementation of the quasi-Newton method for minimizing a function in a box, the L-BFGS algorithm, is available on www.ece.northwestern. edu/~nocedal/lbfgsb.html.

When the gradient  $\nabla J$  is neither computable in closed form nor computable numerically with the required accuracy, an alternative to gradient descent methods is to use the nonlinear simplex method (not to be confused with the simplex algorithm for solving linear programming problems, see [15]). As opposed to gradient descent methods, the nonlinear simplex algorithm only uses the *values* (and not the *gradient*) of  $J$ , but the convergence of the algorithm is not proved in general, and there are known counterexamples in which it does not converge.

## **Application: Extracting Local Volatility**

In the case of *parametric* models in finance, namely, models with a small number of scalar parameters, such as Heston's stochastic volatility model or Merton's jump-diffusion model (as opposed to models with *functional*, e.g., time-dependent, parameters), the choice of a suitable regularization term is generally not obvious. In this case, the calibration industry standard rather consists in solving the unregularized nonlinear least squares problem 2. So Tikhonov regularization is rather used for calibrating *nonparametric* financial models.

In this section, we consider the problem of inferring a *local volatility function*  $\sigma(t, S)$  (see [7]) from observed option prices, namely, European vanilla calls and/or puts with various strikes and maturities on the underlying  $S$ . The local volatility function thus inferred may then be used to price exotic options and/or compute Greeks, consistently with the market (e.g., [5]).

### The Ill-posed Local Volatility Calibration Problem

The local volatility calibration problem, however, is underdetermined (since the set of observed prices is finite whereas the nonparametric function  $\sigma$  has an infinite degrees of freedom) and ill posed. So a naive approach based on numerical differentiation using the so-called *Dupire's formula* [7] gives a local volatility that is highly oscillatory (Figure 1), and thus unstable, for instance when performing a dayto-day calibration.

To address this issue, the first idea that comes to mind is to seek for  $\sigma$  within a parameterized family of functions. However, finding classes of functions with all the flexibility required for fitting implied volatility surfaces with several hundred implied volatility points and a variety of shapes turns out to be a very challenging task (unless a large family of splines is considered, see Coleman et al. [3], in which case, the ill-posedness of the problem shows up again).

![](_page_3_Figure_1.jpeg)

**Figure 1** Local Variance  $\sigma(t, S)^2$  obtained by application of Dupire's formula on the DAX index, May 2, 2001

The best way to proceed is to stay nonparametric, and to use regularization methods to stabilize the calibration procedure. Since we use a nonparametric local volatility, the model contains sufficient number of degrees of freedom to provide a perfect fit to virtually any market smile. Furthermore, the regularization method guarantees that the local volatility thus calibrated is nice and smooth.

#### Approach by Tikhonov Regularization

Among the various regularization methods at hand, the most popular one is the Tikhonov regularization method described in the section Tikhonov Regularization of Nonlinear Inverse Problems. One thus rewrites the local volatility calibration problem as the following nonlinear minimization problem:

$$\min_{\{\sigma \equiv \sigma(t,S); \underline{\sigma} \le \sigma \le \overline{\sigma}\}} J(\sigma)$$
  
=  $\|\Pi(\sigma) - \pi\|^2 + \alpha \|\sigma - \sigma_0\|_{\mathcal{H}^1}^2$  (13)

where

the bounds  $\underline{\sigma}$  and  $\overline{\sigma}$  are given positive constants specifying the abstract set  $\mathcal{A}$  in the section Tikhonov Regularization of Nonlinear Inverse Problems;

- $\pi$  is the vector of market prices observed at the calibration time;  $\Pi(\sigma)$  is the related vector of prices in the Dupire model with volatility function  $\sigma$ ;
- $\sigma_0$  is a suitable prior (*a* priori guess on  $\sigma$ ), and for  $u \equiv u(t, S)$ ,

$$\|u\|_{\mathcal{H}^{1}}^{2} = \int_{t_{0}}^{\infty} \int_{0}^{\infty} \left[ u(t, S)^{2} + (\partial_{t} u(t, S))^{2} + (\partial_{S} u(t, S))^{2} \right] dt dS \quad (14)$$

Problem 13 and a related gradient descent approach to solve it numerically (cf. the section Implementation) were introduced in [12]. Crépey [6] (see also [8]) further showed that the general conditions of the section Tikhonov Regularization of Nonlinear Inverse Problems are satisfied in this case. Stability and convergence of the method follow.

In [5] an efficient trinomial tree implementation of this approach was presented, based on an exact computation of the gradient of the (discretized) cost criterion  $J$  in equation 13. Figure 2 displays the local variance surface  $\sigma(t, S)^2$  (to be compared with that of Figure 1), the corresponding implied volatility surface, and the accuracy of the calibration, obtained by running this algorithm on the DAX index European options data set of May 2, 2001 (consisting

![](_page_4_Figure_1.jpeg)

Figure 2 (a) Local variance, (b) implied volatility, and (c) calibration accuracy obtained by application of the Tikhonov regularization method on the DAX index, May 2, 2001

of about 300 European vanilla option prices distributed throughout six maturities with moneyness  $K/S_0 \in [0.8, 1.2]$ ). At the initiation of the algorithm, the norm of the gradient of the cost criterion  $J$  in equation 13 was equal to  $5.73E - 02$ , and upon convergence after 65 iterations of the gradient descent algorithm, a local minimum of the cost criterion was found, with related value of the norm of the gradient of the cost criterion equal to  $6.83E - 07$ . In the accuracy graph, implied volatility mismatch refers to the difference between the Black-Scholes implied volatility corresponding to the market price of an option and its price in the calibrated local volatility model, for each option in the calibration data set.

Such calibration procedures are typically computationally intensive; however, it is possible to make them faster by resorting to parallel computing (see Table 1 and [5]).

**Table 1** Calibration CPU times on a cluster of *nproc* 1.3-GHz processors connected on a fast Myrinet network. using a calibration tree with *n* time steps (thus  $n^2/2$  nodes in the tree)

| $n \times n \n$ proc |                          |                          |                          |
|----------------------|--------------------------|--------------------------|--------------------------|
| 54                   | 25s                      | 9s                       | 10s                      |
| 101                  | $4 \text{m} 30 \text{s}$ | $1 \text{m} 57 \text{s}$ | $1 \text{m} 36 \text{s}$ |

**Remark 3** (1) This approach by Tikhonov regularization can be extended to the problem of calibrating a local volatility function using American observed option prices as input data [5], or to the problem of calibrating a *Lévy model with local jump measure* (see  $[4]$  and  $[11]$ ).

 $(2)$  An alternative approach for this problem is to use entropic regularization, rewriting the local volatility calibration problem as a related stochastic control problem [1].

## **References**

- [1] Avellaneda, M., Friedman, C., Holmes, R. & Samperi, D. (1997). Calibrating volatility surfaces via relativeentropy minimization, *Applied Mathematical Finance* **41**, 37–64.
- [2] Binder, A., Engl, H.W., Groetsch, C.W., Neubauer, A. & Scherzer, O. (1994). Weakly closed nonlinear operators and parameter identification in parabolic equations by Tikhonov regularization, *Applicable Analysis* **55**, 13–25.
- [3] Coleman, T., Li, Y. & Verma, A. (1999). Reconstructing the unknown volatility function, *Journal of Computational Finance* **2**(3), 77–102.
- [4] Cont, R. & Rouis, M.(2006). *Estimating Exponential L´evy Models from Option Prices via Tikhonov Regularization*, Working Paper.
- [5] Crepey, S. (2003). Calibration of the local volatility in ´ a trinomial tree using Tikhonov regularization, *Inverse Problems* **19**, 91–127.
- [6] Crepey, S. (2003). Calibration of the local volatility ´ in a generalized Black–Scholes model using Tikhonov regularization, *SIAM Journal on Mathematical Analysis* **34**(5), 1183–1206.
- [7] Dupire, B. (1994). Pricing with a smile, *Risk* **7**, 18–20.
- [8] Egger, H. & Engl, H.W. (2005). Tikhonov regularization applied to the inverse problem of option pricing: convergence analysis and rates, *Inverse Problems* **21**, 1027–1045.
- [9] Engl, H.W., Hanke, M. & Neubauer, A. (1996). *Regularization of Inverse Problems*, Kluwer, Dordrecht.
- [10] Engl, H.W. Kunisch, K. & Neubauer, A. (1989). Convergence rates for Tikhonov regularisation of nonlinear ill-posed problems, *Inverse Problems* **5**(4), 523–540.

- [11] Kindermann, S., Mayer, P., Albrecher, H. & Engl, H.W. (2008). Identification of the local speed function in a Levy model for option pricing, ´ *Journal of Integral Equations and Applications* **20**(2), 161–200.
- [12] Lagnado, R. & Osher, S. (1997). A technique for calibrating derivative security pricing models: numerical solution of an inverse problem, *Journal of Computational Finance* **1**(1), 13–25.
- [13] Nocedal, J. & Wright, S.J. (2006). *Numerical Optimization*, 2nd Edition, Springer.
- [14] Phillips, D. (1962). A technique for the numerical solution of certain integral equations of the first kind, *Journal of the ACM* **9**, 84–97.
- [15] Press, W.H., Flannery, B.P., Teukolsky, S.A. & Vetterling, W.T. (1992). *Numerical Recipes in C: The Art of Scientific Computing*, 2nd Edition, Cambridge University Press.
- [16] Tikhonov, A. (1963). Solution of incorrectly formulated problems and the regularization method, *Soviet Mathematics Doklady* **4**, 1035–1038, English translation of *Doklady Akademii Nauk SSSR* **151**, 501–504, 1963.

## **Related Articles**

**Conjugate Gradient Methods**; **Dupire Equation**; **Local Volatility Model**; **Model Calibration**; **Tree Methods**.

STEPHANE ´ CREPEY ´
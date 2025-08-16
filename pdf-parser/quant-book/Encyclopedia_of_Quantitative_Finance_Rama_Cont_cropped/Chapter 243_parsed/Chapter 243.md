# **Conjugate Gradient** Methods

In option pricing on the basis of the Black-Scholes model [3], the value of an option is governed by a partial differential equation (PDE) (see Partial Dif**ferential Equations**). Except for special cases, analytic solutions generally do not exist and numerical methods are necessary to approximate the solution. For instance, finite difference methods [20] approximate the solution on a mesh of discrete asset prices. An implicit discretization of the PDE then requires in each time step solving a linear system:

$$Ax = b \tag{1}$$

where  $x$  is the solution of next time step,  $b$  is the right-hand side, and A is an  $N \times N$  matrix (see **Finite** Difference Methods for Barrier Options; Finite **Difference Methods for Early Exercise Options).** It is interesting to note that matrices arising from option pricing PDEs are often sparse and typically have  $O(N)$  nonzeros.

The solution time and storage for solving large linear systems can be very significant. Gaussian elimination is a standard method for solving linear systems, but owing to the issue of fill-in [5], it is usually deemed too expensive in practice when the underlying has more than two assets. Iterative methods [10, 18], for example, Jacobi, Gauss-Seidel, and successive over-relaxation (SOR), on the other hand, are simple to apply. However, their convergence rates, typically depending on the mesh size, are very slow for large problems. The ADI method [16] (see Alternating Direction Implicit (ADI) Method) has been used in option pricing. While it can be made efficient for some linear PDEs, it is not clear how it can be easily extended to more general and nonlinear equations.

One way to improve on the classical iterative methods is to use dynamically computed parameters based on the current (and previous) iteration information. The hope is that the appropriately selected parameters would compute "optimal" solutions in some sense. Ideally, it would be desirable to have an iterative method, which (i) is simple to implement, (ii) takes advantage of sparsity structure of  $A$ , and (iii) generates solutions whose errors are minimized

in some way. It turns out that such a method can be developed, which is known as the *conjugate gradi*ent (CG) method [11]. We begin the discussion for symmetric matrices and then generalize the idea to general nonsymmetric cases.

## **Symmetric Case**

Consider the linear system (1) and assume for now that  $A$  is symmetric positive definite (i.e., all eigenvalues are positive). To search the solution  $x$  in the N-dimensional space  $\mathbb{R}^N$  is generally difficult when  $N$  is large. A simpler problem would be to search an approximate solution  $x^k$  from a low-dimensional subspace  $S_k$  where the dimension k is typically much smaller than  $N$ .

There are different ways to select  $x^k$  from  $S_k$ . Intuitively,  $x^k$  is "optimal" if  $||x - x^k||$  is minimized. Geometrically, it is equivalent to saying that the error  $e^k \equiv x - x^k$  is orthogonal to  $S_k$ , that is,  $\langle e^k, s \rangle \equiv$  $\sum_{i=1}^N e_i^k s_i = 0$  for all  $s \in S_k$ . To enforce this condition, one would need  $e^k$ , which is not known. To address this issue, the A-inner product, defined as  $\langle u, v \rangle_A \equiv \langle Au, v \rangle$ , is used instead. The orthogonality condition then becomes

$$0 = \langle e^k, s \rangle_A = \langle A e^k, s \rangle = \langle r^k, s \rangle \quad \forall s \in S_k \quad (2)$$

where  $r^k \equiv b - Ax^k$  is the residual vector, which is computable. What it does is to minimize  $\langle e^k, e^k \rangle_A \equiv$  $||e^k||_A^2$ , the A-norm of the error.

Different choices of  $S$  lead to different methods. For instance, the method of Steepest descent (SD) [9, 18] chooses the one-dimensional subspace  $S = \text{span}\{p\}$ , where p is the residual vector of the current approximation. A new approximate solution is obtained by enforcing the orthogonality condition (2). The procedure is repeated with another search direction. Note that SD does not increase the dimension of the search subspace  $S$  but rather changes  $S$ from every iteration. The main drawback of SD is slow convergence in practice, typically because the search directions may repeat and so SD may end up searching in the same direction again and again [10].

## Conjugate Gradient

To avoid unnecessary duplicated search effort as in SD, the conjugate gradient (CG) method [11, 18] is used to find an optimal solution  $x^k$  from a set of search directions  $\{p^i\}$ , which are A-orthogonal; that is,  $\langle p^i, p^j \rangle_A = 0$  if  $i \neq j$ . The A-orthogonality property guarantees that each of the  $p^k$  searches in a unique subspace and one never has to look in that subspace again.

The basic idea of CG is to start with an initial guess  $x^0$  and then find an approximate solution in a subspace S. It first begins with a small (dimension 1) subspace and then increases the dimension one by one to obtain better approximation. More precisely, at the  $k$ th step, the search subspace is

$$S_k = \text{span}\{p^0, p^1, \dots, p^{k-1}\}$$
 (3)

where  $\{p^i\}_{i=1}^{k-1}$  are search vectors computed from previous steps. CG then looks for the best approximate solution  $x^k \in x^0 + S_k$ , that is,

$$x^{k} = x^{0} + \sum_{i=0}^{k-1} \alpha_{i} p^{i}$$
 (4)

The orthogonality condition  $(2)$  and the A-orthogonality property of  $\{p^i\}$  yield  $\alpha_i = \langle p^i, r^0 \rangle / \langle p^i, p^i \rangle_A$ . Note that  $\alpha_i$  does not depend on k. Hence,

$$x^{k} = x^{0} + \sum_{i=0}^{k-2} \alpha_{i} p^{i} + \alpha_{k-1} p^{k-1} = x^{k-1} + \alpha_{k-1} p^{k-1}$$
(5)

Thus, only the last search direction needs to be stored to update  $x^k$  from  $x^{k-1}$ .

Once  $x^k$  is known, SD would use the residual  $r^k$ as the new search direction. CG, however, makes  $r^k$ A-orthogonalized against all previous  $\{p^i\}$  to obtain  $p^k$ , that is,

$$p^{k} = r^{k} + \sum_{i=0}^{k-1} \beta_{i} p^{i}$$
 (6)

where  $\beta_i = -\langle r^k, p^i \rangle_A / \langle p^i, p^i \rangle_A$  given by the Aorthogonality condition. The new search subspace is then defined as  $S_{k+1} = \text{span}\{p^0, \ldots, p^k\}$  and the new approximate solution  $x^{k+1}$  is computed until it is sufficiently accurate.

A potential drawback of CG is to store all  $\{p^i\}$  for computing  $p^k$ . Simplification is necessary to make the method practical. An important observation in deriving CG is that  $S_k$  is the same as the Krylov subspace [9, 10, 18], defined as

$$\mathcal{K}_k \equiv \text{span}\{r^0, Ar^0, \dots, A^{k-1}r^0\} \tag{7}$$

As a result,

$$p' \in \text{span}\{p^0, \dots, p^i\} = S_{i+1} = \mathcal{K}_{i+1}$$
  
=  $\text{span}\{r^0, \dots, A^i r^0\}$  (8)

 $Ap^i \in \text{span}\{Ar^0, \ldots, A^{i+1}r^0\} \subset \mathcal{K}_{i+2} =$ Hence,  $S_{i+2}$ . By equation (2),  $r^k \perp S_j$ ,  $j = 1, \ldots, k$  and hence,  $r^k \perp S_{i+2}$  for any  $i \leq k-2$ . Thus,  $\langle Ap^i, r^k \rangle =$  $0 = \beta_i$ ,  $i \leq k - 2$ , and equation (6) is simplified to

$$p^{k} = r^{k} + \beta_{k-1} p^{k-1} \tag{9}$$

Thus, as for  $x^k$ , only the last search vector needs to be stored. Besides, more convenient formulas for  $\alpha_k$  and  $\beta_k$  can be derived by applying the various orthogonality properties. Finally, the CG algorithm is given as follows:

## Algorithm: Conjugate Gradient

$$x^{0} = \text{initial guess}$$
  

$$r^{0} = b - Ax^{0}$$
  

$$(p^{-1} = 0, \ \beta_{-1} = 0)$$
  
for  $k = 0, 1, 2, \dots$ , until convergence  

$$p^{k} = r^{k} + \beta_{k-1} p^{k-1}$$
  

$$\alpha_{k} = \langle r^{k}, r^{k} \rangle / \langle p^{k}, Ap^{k} \rangle$$
  

$$x^{k+1} = x^{k} + \alpha_{k} p^{k}$$
  

$$r^{k+1} = r^{k} - \alpha_{k} A p^{k}$$
  

$$\beta_{k} = \langle r^{k+1}, r^{k+1} \rangle / \langle r^{k}, r^{k} \rangle$$

end

Note that the CG algorithm only involves simple vector operations and matrix-vector multiply, and hence the sparsity structure of  $A$  can be fully and easily explored. Moreover, two-term recurrence formulas exist for the updates of  $x^k$  and other variables. As such, the work and storage for one CG iteration are  $O(N)$ . Note also that the matrix A is not really needed as long as one can compute the matrix-vector product. This property is particularly useful when  $A$ is not available explicitly; see the section Application.

#### Convergence of CG

Compared to other iterative methods, CG has the desirable property that  $x^k$  is the "best" approximation from  $S_k$ . Thus, the CG solution  $x^k$  improves as the dimension of  $S_k$  increases. When  $k = N$ , then  $S_N = \mathbb{R}^N$  and so  $e^N = 0$ . Hence, CG obtains the exact solution in at most  $N$  iterations (known as the finite termination property [18]). In practice,

however, CG is often treated as an iterative method in the sense that only a small number of iterations are performed. In many cases, the approximate solution  $x^k$  is sufficiently accurate for  $k \ll N$ .

The number of CG iterations needed depends on the rate of convergence, which is very complex in general. A well-known estimate [9, 18] is given as follows:

$$\|e^{k}\|_{A} \le 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^{k} \|e^{0}\|_{A}$$
 (10)

where  $\kappa$  is the condition number [8] of A. For a parabolic PDE, with timestep size  $O(h)$ ,  $\kappa =$  $O(h^{-1})$ , where h is the mesh size of the discrete asset prices. The rates of convergence for Jacobi, Gauss-Seidel, and SD are  $1 - O(h)$ , whereas the rate for CG, based on the above error bound, is  $1 - O(\sqrt{h})$ , an order of magnitude improvement. SOR also has the same asymptotic convergence rate as CG, but it would require the knowledge of the optimal over-relaxation parameter. In practice, the CG error bound is often too pessimistic and the actual CG convergence is considerably much faster than the classical iterative methods.

## Nonsymmetric Case

CG computes an optimal approximation  $x^k$  ( $||e^k||_A$  is minimized) using short (two-term) recurrence update formulas for  $x^k$  and other quantities. Could one do the same for nonsymmetric matrices, such as the discretized Black–Scholes equation? Unfortunately, the answer is provably no [6]. Thus, when generalizing CG to the nonsymmetric case, one keeps some desirable properties of CG and sacrifices the others. There are many different possibilities, which yield numerous methods collectively known as the Krylov subspace methods [1]. Here, we describe two of these methods commonly used in practice.

The generalized minimal residual (GMRES) method [17] minimizes the norm of the residual vector:

$$\min_{x^k} \|b - Ax^k\|_2, \quad x^k \in x^0 + \mathcal{K}_k \tag{11}$$

As a result, the residual norm is nonincreasing. Furthermore, convergence is guaranteed for a wide class of matrices. However, it needs to store all the basis vectors for  $\mathcal{K}_k$ . Thus, work and storage increase with iteration. A remedy is to restart GMRES every  $m$  iterations ( $m$  small constant). The convergence of the restarted GMRES, however, may stagnate, that is,  $||r^k|| \approx ||r^{k-1}||$  for many iterations.

The other method is BiCGSTAB [23], which is derived from the biconjugate gradient (BCG) method [7]. BCG enforces a similar orthogonality condition on  $r^k$  as in equation (2) but allows two different Krylov subspaces to be used: more precisely.

$$r^k \perp \tilde{\mathcal{K}}_k \quad \text{and} \quad x^k \in x^0 + \mathcal{K}_k$$
 (12)

where  $\tilde{\mathcal{K}}_k = \text{span}\{\tilde{r}^0, A^T \tilde{r}^0, \dots, (A^T)^{k-1} \tilde{r}^0\}$  for some vector  $\tilde{r}^0$ . By enforcing the so-called bi-orthogonality condition, which makes the basis vectors  $\{v^j\}$  for  $\mathcal{K}_k$  and the basis vectors  $\{w^j\}$  for  $\tilde{\mathcal{K}}_k$  orthogonal to each other, two-term recurrence formulas for updating  $x^k$  and other quantities can be found. It has an advantage over GMRES in terms of storage. However, since it does not have the minimization property as GMRES, the residual norm can be very irregular as iterations continue. BiCGSTAB essentially is a "smooth" variant of BCG and its convergence is much more stabilized.

A more comprehensive overview of various Krylov subspace methods can be found in [1]. Similar to CG, the algorithms of the nonsymmetric methods involve only simple vector operations and matrix-vector products.

#### Preconditioning

CG methods would not have been so popular without the powerful technique called *preconditioning*, which can accelerate convergence drastically. Consider a nonsingular matrix  $M$ . The main idea is that the preconditioned system

$$M^{-1}Ax = M^{-1}b \t\t(13)$$

is equivalent to equation  $(1)$  but the convergence of CG now depends on  $M^{-1}A$  instead. The key is to construct a preconditioner M such that  $\kappa(M^{-1}A) \ll$  $\kappa(A)$  in order to obtain fast convergence. It is clear that if  $M \approx A$ , then  $M^{-1}A \approx I$ , which has condition number 1. On the other hand,  $M$  should be simple enough that the matrix-vector product by  $M^{-1}$  is easy to compute.

Generally speaking, it is difficult to determine what the optimal  $M$  is. Often it is problem specific. A general class of preconditioners widely used in practice is called *incomplete LU* (ILU) factorization [14, 18]. A full LU would result in Gaussian elimination, which is expensive. An approximate LU factorization trades-off between efficiency and accuracy. Other effective preconditioners include multigrid [15, 22], domain decomposition [19], and sparse approximation inverse [2]. Once a preconditioner is chosen, to incorporate preconditioning into any CG algorithms only requires changing a few lines of code.

## Application

CG methods have been used for pricing different options, for instance, American options [12], options with stochastic volatility [25], and options on Lévy driven assets [13]. Comparisons of SOR and CG methods for multiasset problem can be found in [21]. As an example, we consider pricing European options in a rather general exponential Lévy model (cf. [24] for more details in the special case of CGMY). The option value,  $V(S, \tau)$ , satisfies a partial integro-differential equation (see Partial Integrodifferential Equations (PIDEs)), which is similar to the Black-Scholes equation [3] but with an extra integral term for the jump process:

$$\begin{split} \frac{\partial V}{\partial \tau} &= \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV \\ &+ \int_{-\infty}^{\infty} v(y) \bigg[ V(Se^y, \tau) - V(S, \tau) \\ &- S(e^y - 1) \frac{\partial V}{\partial S} \bigg] \mathrm{d}y \end{split} \tag{14}$$

where S is the value of the underlying asset,  $\tau$  the time from expiry,  $\sigma$  the volatility, r the interest rate, and  $v(y)$  a Lévy measure. Let  $\{S_i\}_{i=1}^N$  be a set of discrete asset prices. Also, let  $V^n = (V_1^n, \ldots, V_N^n)$ , where  $V_i^n$  is an approximation of  $V(S_i, \tau^n)$  at time  $\tau^n$ . Then a fully implicit finite difference discretization requires solving a linear system (1) at each timestep with  $x = V^{n+1}$  and  $b = V^n$ . (The second order Crank-Nicolson discretization results in a similar matrix and right-hand side.) The matrix  $A$  can be written as a sum of two matrices:  $A = L + B$ , where  $L$  corresponds to the discretization of the differential term (which is similar to the Black-Scholes matrix) and  $B$  corresponds to the discretization of the integral term. While L is sparse, B is not; it has  $O(N^2)$ 

nonzeros. Since  $A$  is dense because of  $B$ , it is not practical (time and storage) to form  $A$  explicitly even for moderate size  $N$ . In this case, Gaussian elimination and the classical iterative methods would not be easily applicable.

CG methods, on the other hand, can be used with ease. Note that  $B$  has a special convolution structure so that matrix-vector multiply can be computed efficiently using an FFT [4]. Thus, while  $A$ may not be available explicitly, the matrix-vector product by  $A$  can be computed, which is all CG methods require. In this problem,  $A$  is nonsymmetric and BiCGSTAB is used to solve the linear system [24]. Mesh-independent convergence is obtained for the infinite activity and finite variation case and there is a slight increase in iteration numbers for the infinite variation case. In both the cases, it shows an improvement of factor 4 in CPU times over another iterative method on the basis of a fixed point iteration.

## Summary

CG methods generate "optimal" approximate solutions by performing simple vector operations and matrix-vector multiply. More importantly, by combining with the right choice of preconditioners, CG methods have been shown to be robust and efficient for solving option pricing PDEs. The discussion has been mainly focused on linear problems. In more general cases, one can apply preconditioned CG methods to the linearized equations from nonlinear problems without making any special modification.

## Acknowledgments

The author was supported by the Natural Sciences and Engineering Research Council of Canada.

### References

- Barret, R., Berry, M., Chan, T.F., Demmel, J., Donato, J., [1] Dongarra, J., Eijkhout, V., Pozo, R., Romine, C. & Van der Vorst, H. (1994). Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods, 2nd Edition, SIAM, Philadelphia.
- [2] Benzi, M., Meyer, C.D. & Tuma, M. (1996). A sparse approximate inverse preconditioner for the conjugate gradient method, SIAM Journal on Scientific Computing 17, 1135-1149.

- [3] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [4] d'Halluin, Y., Forsyth, P.A. & Vetzal, K. (2005). Robust numerical methods for contingent claims under jump diffusion processes, *IMA Journal on Numerical Analysis* **25**, 87–112.
- [5] Duff, I.S., Erisman, A.M. & Reid, J.K. (1986). *Direct Methods for Sparse Matrices*, Oxford Press, UK.
- [6] Faber, V. & Manteuffel, T. (1984). Necessary and sufficient conditions for the existence of a conjugate gradient method, *SIAM Journal on Numerical Analysis* **21**, 352–362.
- [7] Fletcher, R. (1975). Conjugate gradient methods for indefinite systems, in *The Dundee Biennial Conference on Numerical Analysis, 1974*, G.A. Watson, ed, Springer-Verlag, New York, pp. 73–89.
- [8] Golub, G. & Van Loan, C. (1996). *Matrix Computations*, The Johns Hopkins University Press, Baltimore.
- [9] Greenbaum, A. (1997). *Iterative Methods for Solving Linear Systems*, SIAM, Philadelphia.
- [10] Hackbusch, W. (1994). *Iterative Solution of Large Sparse Systems of Equations*, Springer-Verlag, New York.
- [11] Hestenes, M.R. & Stiefel, E.L. (1952). Methods of conjugate gradients for solving linear systems, *Journal of Research of the National Bureau of Standards, Section B* **49**, 409–436.
- [12] Khaliq, A.Q.M., Voss, D.A. & Kazmi, S.H.K. (2006). A linearly implicit predictor-corrector scheme for pricing American options using a penalty method approach, *Journal of Banking and Finance* **30**, 489–502.
- [13] Matache, A.M., von Petersdorff, T. & Schwab, C. (2004). Fast deterministic pricing of options on Levy ´ driven assets, *Mathematical Modelling and Numerical Analysis* **38**, 37–72.
- [14] Meijerink, J.A. & Van der Vorst, H. (1977). An iterative solution method for linear systems of which the coefficient matrix is a symmetric M-matrix, *Mathematics of Computation* **31**, 148–162.

- [15] Oosterlee, C.W. (2003). On multigrid for linear complementarity problems with applications to American-style options, *Electronic Transactions on Numerical Analysis* **15**, 165–185.
- [16] Peaceman, D. & Rachford, H. (1955). The numerical solution of elliptic and parabolic differential equations, *Journal of SIAM* **3**, 28–41.
- [17] Saad, Y. & Schultz, M.H. (1986). GMRES: a generalized minimal residual algorithm for solving nonsymmetric linear systems, *SIAM Journal on Scientific and Statistical Computing* **7**, 856–869.
- [18] Saad, Y. (2003). *Iterative Methods for Sparse Linear Systems*, 2nd Edition, SIAM, Philadelphia.
- [19] Smith, B., Bjørstad, P. & Gropp, W. (1996). *Domain Decomposition: Parallel Multilevel Methods for Elliptic Partial Differential Equations*, Cambridge University Press, Cambridge.
- [20] Strikwerda, J. (2004). *Finite Difference Schemes and Partial Differential Equations*, 2nd Edition, SIAM, Philadelphia.
- [21] Tavella, D. & Randall, C. (2000). *Pricing Financial Instruments: The Finite Difference Method*, John Wiley & Sons, USA.
- [22] Trottenbery, U., Oosterlee, C. & Schuller, A. (2001). ¨ *Multigrid*, Academic Press.
- [23] Van der Vorst, H.A. (1992). Bi-CGSTAB: a fast and smoothly converging variant of Bi-CG for the solution of non-symmetric linear systems, *SIAM Journal on Scientific and Statistical Computing* **13**, 631–644.
- [24] Wang, I.R., Wan, J.W.L. & Forsyth, P.A. (2007). Robust numerical valuation of European and American options under the CGMY process, *Journal of Computational Finance* **10**, 31–69.
- [25] Zvan, R., Forsyth, P.A. & Vetzal, K.R. (1998). Penalty methods for American options with stochastic volatility, *Journal of Computational and Applied Mathematics* **91**, 199–218.

JUSTIN W.L. WAN
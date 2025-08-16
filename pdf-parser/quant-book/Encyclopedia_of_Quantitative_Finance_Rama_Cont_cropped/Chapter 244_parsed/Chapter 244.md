# **Multigrid Methods**

## **Multigrid Basics**

The multigrid iterative solution method has the unique potential of solving partial differential equations (PDEs) discretized with  $N^d$  unknowns in  $\mathcal{O}(N^d)$  work. This property forms the basis for efficiently solving very large computational problems. Initiated by Brandt [2], the development of multigrid has been particularly stimulated by the work done in computational fluid dynamics toward the end of the twentieth century. Introductions to multigrid can be found in [4, 15].

The insights and algorithms developed can be directly transferred to finance, that is, for solving the higher dimensional versions of convection-diffusionreaction type PDE operators efficiently. These higher dimensional PDEs arise, for example, when dealing with stochastic volatility or with multiasset options under Black-Scholes dynamics. The aim is to solve these discrete PDE problems in just a few multigrid iterations within a split second.

### Linear Multigrid

We would like to solve iteratively the discrete problem resulting from a PDE,

$$A_h u_h = f_h, \text{ on grid } G_h \tag{1}$$

for unknown  $u_h$ . For any approximation  $u_h^m$ , after iteration  $m$ , of the solution  $u_h$ , we denote the error by  $e_h^m := u_h - u_h^m$ , and the defect (or residual) by  $d_h^m := f_h - A_h u_h^m$ . Multigrid methods are motivated by the fact that many iterative methods, such as the well-known pointwise Gauss-Seidel iteration (PGS), have a smoothing effect on  $e_h^m$ . A smooth error can be well represented on a coarser grid, containing substantially fewer points, where its approximation is much cheaper. The defect equation,

$$A_h e_h^m = d_h^m \tag{2}$$

represents the error; it is equivalent to the original equation, since  $u_h = u_h^m + e_h^m$ . Departing from the insight of a smooth error,  $e_h^m$ , the idea is to use an appropriate approximation,  $A_H$ , of  $A_h$  on a coarser *grid*,  $G_H$  (for instance, a grid with double the mesh size in each direction). The defect equation is then replaced by

$$A_H \widehat{e}_H^m = d_H^m \tag{3}$$

where  $A_H: G_H \to G_H$ , dim  $G_H < \dim G_h$  and  $A_H$ is invertible. As  $d_H^m$  and  $\widehat{e}_H^m$  are grid functions on the coarser grid,  $G_H$ , we need two transfer operators between the fine and coarse grid.  $I_h^H$  is used to restrict  $d_h^m$  to  $G_H$ , and  $I_H^h$  is used to interpolate (or prolongate) the correction,  $\widehat{e}_{H}^{m}$ , back to  $G_{h}$ :

$$d_H^m := I_h^H d_h^m, \ \widehat{e}_h^m := I_H^h \widehat{e}_H^m \tag{4}$$

This defines an iterative two-grid solution method, the two-grid correction scheme:

- 1.  $v_1$  smoothing steps on the fine grid:  $\widehat{u}_h \Longleftarrow S^{\nu_1}(u_h^0, f_h);$
- 2. computation of fine-grid residuals:  $d_h := f_h - A_h \widehat{u}_h;$
- 3. restriction of residuals from fine to coarse:  $d_H := I_h^H d_h;$
- 4. solution of coarse-grid problem:  $A_H \widehat{e}_H = d_H$ ;
- 5. prolongation of corrections from coarse to fine:  $\widehat{e}_h := I^h_H \widehat{e}_H;$
- 6. add correction to fine-grid approximation:  $\widehat{u}_h \Longleftarrow \widehat{u}_h + e_h;$
- 7.  $\nu_2$  smoothing steps on the fine grid:<br> $u_h^1 \longleftarrow S^{\nu_2}(\widehat{u}_h, f_h).$

Steps  $(1)$  and  $(7)$  are pre and postsmoothing steps, consisting of a few Gauss-Seidel iterations. Steps  $(2)-(6)$  form the "coarse-grid correction cycle". In a well-converging two-grid method, it is not necessary to solve this coarse-grid defect equation exactly. Instead, one can replace  $\widehat{e}_{H}^{m}$  by a suitable approximation. A natural way is to apply the two-grid idea again to the coarse-grid equation, now employing an even coarser grid than  $G_H$ . This can be done recursively; on each grid  $\gamma$  two-grid iteration steps are applied. With  $\gamma = 1$ , the multigrid V-cycle is obtained.

The smoothness of the error after Gauss-Seidel iterations depends on the discrete PDE under consideration. For nicely elliptic operators such as the Laplacian, errors will become smooth in all grid directions and grid coarsening can take place along every direction. For the convection-diffusion type equations, we obtain similar smooth errors if we process the grid points according to the directions governed by the convective term [15]. The choice of coarse grid highly depends on the smoothness of the error in the approximation. We coarsen in those directions in which this error is smooth. Coarsening is simple for structured Cartesian grids, where one can remove every second grid point to obtain the coarse grid. For irregular grids, the resulting matrix  $A_h$  assists in determining the smoothness of the error. The matrix can accordingly be reduced algebraically (algebraic multigrid, AMG, see, e.g., [15]). In geometric multigrid, coarse grids are defined on the basis of a given fine grid, and coarse-grid corrections are computed from the PDE discretized on the coarse grids.

If  $N^d$  is the number of unknowns on  $G_h$  and  $N^d/\beta$  is the number of nodes on the coarse grid, then the multigrid algorithm requires  $\mathcal{O}(N^d)$  storage and, for accuracy commensurable with discretization accuracy,  $\mathcal{O}(N^d \log N^d)$  work, if  $\gamma < \beta$ . To get  $\mathcal{O}(N^d)$  work, the multigrid cycles must be preceded by nested iteration, also called full multigrid [4, 15].

# **Multiasset Options; Dealing with Grid** Anisotropies in Multigrid

In this section, we discuss the numerical treatment with multigrid for the multiasset Black-Scholes operator. Because this operator can be transformed to the multidimensional heat equation [11], we focus the discussion on the Laplacian operator for simplicity.

The major hindrance in the numerical solution of multidimensional PDEs is the so-called *curse of* dimensionality, which implies that with growth in the number of dimensions, we have an exponential growth in the number of grid points on tensor-product grids. Although we do not address this issue, in particular, we would like to stress that a way to handle dimensionality is the sparse-grid method [5, 14, 18]. One of the characteristics of these sparse grids is that they are essentially *nonequidistant* and, therefore, efficient multigrid solution methods for this type of grid are quite important.

We therefore consider here the discrete 2D Laplacian, discretized by finite differences on a grid with  $h_{y} \gg h_{x}$ , meaning that the matrix elements related to the x-derivative,  $O(h_x^{-2})$ , are significantly larger than those for the y-derivative,  $O(h_{\nu}^{-2})$ . If we apply

a PGS to this discrete operator, we find that its smoothing effect is very poor in the y-direction. The reason is that PGS has a smoothing effect only with respect to the "strong coupling" in the operator, in this case the  $x$ -direction. A multigrid method based on pointwise smoothing and grid coarsening in all directions will not converge well, as we coarsen along directions in which the error is nonsmooth.

An algorithmic improvement is to keep the pointwise relaxation for smoothing, but to *change the grid coarsening* according to the one-dimensional smoothness of errors: the coarse grid defined by doubling the mesh size only in that direction in which the errors are smooth will result in an efficient multigrid method. Figure 1 shows an example of semicoarsening along the  $x$ -axis.

A second successful approach is to keep the grid coarsening in all directions, but to change the smoothing procedure from a pointwise to linewise iteration. Line relaxations are block iterations in which each block of unknowns corresponds to a line. This smoother generates smooth error in all grid directions in the case of grid anisotropies.

These two strategies for excellent convergence, that is, to maintain standard coarsening and change the smoother, or to keep the pointwise smoothing procedure but adapt the coarsening, remain valid for higher dimensional problems. In a 3D problem, this implies that *planewise relaxation* should be employed (in combination with standard coarsening), in which all unknowns lying in the plane of strongly coupled unknowns are relaxed simultaneously. In contrast to line relaxation, which leads to tridiagonal matrices, in plane relaxation we need to solve a discrete 2D problem. A multigrid treatment of high-dimensional PDEs in finance based on hyperplane relaxation has been proposed in [13], while the use of pointwise

![](_page_1_Figure_11.jpeg)

**Figure 1** An example of  $x$ -semicoarsening using three grids

smoothing and coarsening the grid simultaneously along all dimensions where the errors are strongly coupled by *simultaneous partial grid coarsening* has been employed in [18, 19], until the coarse-grid problem is isotropic to the point where full coarsening is feasible. The resulting multigrid methods are highly efficient.

# American Options; Multigrid Treatment of **Nonlinear Problems**

Next, we discuss multigrid methods for the computation of the value of an American-style option. In [17], it was shown that for American-style options the theory related to free boundary problems, as it was developed in the  $1970s$  [1, 8], applies. It is possible to rewrite the arising free boundary problem as a linear complementarity problem (LCP), of the form

$$Au \le f_1 \quad \mathbf{x} \in \Omega \tag{5}$$

$$u \ge f_2 \quad \mathbf{x} \in \Omega \tag{6}$$

$$(u - f_2)(Au - f_1) = 0 \quad \mathbf{x} \in \Omega \tag{7}$$

The LCP formulation is beneficial for iterative solution, since the unknown boundary does not appear explicitly and can be obtained in a postprocessing step. The LCP problem is, however, nonlinear, which implies that we have to generalize the linear multigrid algorithm to the nonlinear situation. We can distinguish in solutions of LCPs a so-called active region from an inactive region. In the active region, constraint (6) holds with equality sign, whereas in the inactive region, constraint (5) is valid with equality sign.

#### Nonlinear Multigrid

The fundamental idea of multigrid for nonlinear  $PDEs$  of the form

$$N_h u_h = f_h \tag{8}$$

is the same as that for linear equations. First, the errors in the solution have to be smoothed so that they can be approximated on a coarser grid. In the nonlinear case, the fine-grid defect equation is given by

$$N_h \Big(\overline{u}_h^m + e_h^m\Big) - N_h \overline{u}_h^m = d_h^m \tag{9}$$

where  $\overline{u}_h^m$  is the approximation of the solution after relaxation in the *i*th multigrid cycle,  $e_h^m$  is the error and  $d_h^m$  is the corresponding defect. This equation is approximated on a coarse grid by

$$N_H \Big(\overline{u}_H^m + \widehat{e}_H^m\Big) - N_H \overline{u}_H^m = d_H^m \qquad (10)$$

Not only is the defect,  $d_h^m$ , transferred to the coarse grid by some restriction operator  $I_h^H$  but also the relaxed approximation  $\overline{u}_h^m$  itself by a restriction operator  $\widehat{I}_{h}^{H}$ .

However, as in the linear case, only the coarsegrid corrections,  $\widehat{e}_H$ , are interpolated back to the fine grid, where the fine-grid errors are smoothed again. This forms the basis of the well-known full approximation scheme (FAS) [2]. The nonlinearity of the problems enters in the smoothing operators. If  $N_h$  and  $N_H$  are linear operators, the FAS method is equivalent to the linear multigrid scheme. For many problems, however, the nonlinearity can also be handled globally, resulting in a sequence of linear problems that can be solved efficiently with linear multigrid.

## Multigrid for Linear Complementarity Problems

In 1983, Brandt and Cryer [3] proposed a multigrid method for LCPs arising from free boundary problems. The algorithm is based on the projected successive over-relaxation (SOR) method [7] and is called the *projected full approximation scheme (PFAS)* in [3]. PFAS has been successfully used in the financial community for American options with stochastic volatility in  $[6, 12]$ .

For the smoothing method in PFAS, one employs a projected version of the PGS, consisting of two partial steps per unknown: In a first step, a Gauss-Seidel iteration is applied to equation (5) at  $(x_i, y_i)$  with equality sign. In the second partial step, the solution at  $(x_i, y_i)$  is projected, so that constraint (6) is satisfied,

$$\overline{u}^{m}(x_{i}, y_{j}) = \max\{f_{2}(x_{i}, y_{j}), \widehat{u}(x_{i}, y_{j})\}$$
$$\forall (x_{i}, y_{i}) \in G_{h} \tag{11}$$

where  $\overline{u}^m$  denotes the unknown at  $(x_i, y_i)$  after PGS and  $\hat{u}$  the unknown after the Gauss–Seidel iteration. A linewise variant of PGS has been applied in [6].

The following LCP holds for  $e_h^m := u_h - \overline{u}_h^m$ :

$$A_{h}e_{h}^{m} \leq d_{h}^{m} \quad \mathbf{x} \in \Omega$$
$$e_{h}^{m} + \overline{u}_{h}^{m} \geq f_{2,h} \quad \mathbf{x} \in \Omega$$
$$(e_{h}^{m} + \overline{u}_{h}^{m} - f_{2,h})(A_{h}e_{h}^{m} - d_{h}^{m}) = 0 \quad \mathbf{x} \in \Omega \quad (12)$$

with defect:  $d_h^m = f_{1,h} - A_h \overline{u}_h^m$ . A smooth error,  $e_h^m$ , can be approximated on a coarse grid without any essential loss of information. The LCP coarse-grid equation for the coarse-grid approximation of the error  $\widehat{e}_{H}^{m}$  is therefore defined in PFAS by:

$$A_{H}\widehat{e}_{H}^{m} \leq I_{h}^{H}d_{h}^{m}$$
$$\widehat{e}_{H}^{m} + \widehat{I}_{h}^{H}\overline{u}_{h}^{m} \geq f_{2,H}$$
$$(\widehat{e}_{H}^{m} + \widehat{I}_{h}^{H}\overline{u}_{h}^{m} - f_{2,H})(A_{H}\widehat{e}_{H}^{m} - I_{h}^{H}d_{h}^{m}) = 0 \quad (13)$$

For LCPs, we need to choose "constraint preserving" restriction operators that do not mix information from active and inactive regions on coarse grids. Further, the bilinear interpolation operator  $I_H^h$ is applied only to unknowns on the "active" points [3].

We finally mention that in  $[10]$ , another multigrid variant for LCPs, the so-called monotone multigrid method, has been presented, used in finance in [9].

#### Multigrid as a Preconditioner

Multigrid as a preconditioner is particularly interesting for robustness. An argument for combining multigrid with an acceleration technique is that problems become more and more complex if we treat real-life applications. The fundamental idea of multigrid, to reduce the high-frequency error components by smoothing and to take care of the low frequency error by coarse-grid correction, does not always work optimally if straightforward multigrid approaches are used. In such situations, the combination with Krylov subspace methods, such as conjugate gradient, generalized minimal residual (GMRES), or BiCGSTAB, have the potential to give a substantial convergence acceleration. Often, sophisticated multigrid components may also lead to very satisfactory convergence factors, but they can be difficult to realize and implement.

From the multigrid point of view, multigrid as a preconditioner can also be interpreted as an acceleration of multigrid by iterant recombination. This interpretation easily allows generalizations, for example, to nonlinear problems and to LCPs. Let  $u_h^0$  be an initial approximation for solving  $A_h u_h = f_h$ , and  $d_h^0 = f_h - \hat{A}_h u_h^0$  its defect. The *Krylov subspace*,  $K_h^m$ , is defined by  $K_h^m := \text{span}[d_h^0, A_h d_h^0, \dots, A_h^{m-1} d_h^0].$ This subspace can also be represented by span $[u_h^0]$  $u_h^m, u_h^1 - u_h^m, \ldots, u_h^{m-1} - u_h^m$ , where the  $u_h^m$  are previous approximations to the solution. To find an improved approximation  $u_{h,\text{acc}}^m$ , we now consider a linear combination of the  $\tilde{m}+1$  latest approximations:

$$u_{h,\text{acc}}^{m} = u_h^{m} + \sum_{i=1}^{\widetilde{m}} \overline{\alpha}_i (u_h^{m-i} - u_h^{m}) \qquad (14)$$

In order to obtain an improved approximation  $u_{h,\text{acc}}^m$ , the parameters  $\overline{\alpha}_i$  are determined in such a way that the defect  $d_{h,\text{acc}}^m$  is minimized, for example, with respect to the  $l_2$ -norm  $||\cdot||_2$ . This is a classical defect minimization problem [16]. This technique was generalized to LCPs in [12], where PFAS was used as the method whose iterants were recombined.

#### Acknowledgments

This research has been partially supported by the Dutch government through the national program BSIK: knowledge and research capacity, in the ICT project BRICKS (http://www.bsik-bricks.nl), theme MSV1.

#### References

- Bensoussan, A. & Lions, J.L. (1982). Applications des [1] in Équations Variationelles en Contrôle Stochastique, North-Holland, Dunot, Amsterdam, English Translation 1978.
- Brandt, A. (1977). Multi-level adaptive solutions to [2] boundary-value problems, Mathematics of Computation 31, 333-390.
- Brandt, A. & Cryer, C.W. (1983). Multigrid algorithms [3] for the solution of linear complementarity problems arising from free boundary problems, SIAM Journal on Scientific Computing 4, 655–684.
- [4] Briggs, W.L., Emden Henson, V. & McCormick, S.F. (2000). A Multigrid Tutorial, 2nd Edition, SIAM, Philadelphia, PA.
- Bungartz, H.J. & Griebel, M. (2004). Sparse grids, Acta [5] Numerica 13, 147-269.

- [6] Clarke, N. & Parrot, K. (1999). Multigrid for American option pricing with stochastic volatility, *Applied Mathematics and Finance* **6**, 177–197.
- [7] Cryer, C.W. (1971). The solution of a quadratic programming problem using systematic overrelaxation, *SIAM Journal on Control* **9**, 385–392.
- [8] Friedman, A. (1982). *Variational Principles and Free Boundary Problems*, Wiley, New York.
- [9] Holtz, M. & Kunoth, A. (2007). B-spline based monotone multigrid methods. *SIAM Journal on Numerical Analysis* **45**, 1175–1199.
- [10] Kornhuber, R. (1994). Monotone multigrid methods for elliptic variational inequalities I, *Applied Numerical Mathematics* **69**, 167–184.
- [11] Kwok, Y.K. (1998). *Mathematical Models of Financial Derivatives*, 2nd Edition, Springer, Singapore.
- [12] Oosterlee, C.W. (2003). On multigrid for linear complementarity problems with application to American-style options. *Electronic Transactions on Numerical Analysis*, **15**, 165–185.
- [13] Reisinger, C. & Wittum, G. (2004). On multigrid for anisotropic equations and variational inequalities, *Computers and Visual Science*, **7**, 189–197.

- [14] Reisinger, C. & Wittum, G. (2007). Efficient hierarchical approximation of high-dimensional option pricing problems, *SIAM Journal On Scientific Computing* **29**, 440–458.
- [15] Trottenberg, U., Oosterlee, C.W. & Schuller, A. (2000). ¨ *Multigrid*, Academic Press, London.
- [16] Washio, T. & Oosterlee, C.W. (1997). Krylov subspace acceleration for nonlinear multigrid schemes. *Electronic Transactions on Numerical Analysis* **6**, 271–290.
- [17] Wilmott, P., Dewynne, J. & Howison, S. (1993). *Option Pricing*, Oxford Financial Press.
- [18] bin Zubair, H., Leentvaar, C.C.W. & Oosterlee, C.W. (2007). Efficient *d*-multigrid preconditioners for sparse-grid solution of high dimensional partial differential equations, *International Journal Of Computer Mathematics* **84**, 1129–1146.
- [19] bin Zubair, H., Oosterlee, C.W. & Wienands, R. (2007). Multigrid for high dimensional elliptic partial differential equations on non-equidistant grids, *SIAM Journal On Scientific Computing* **29**, 1613–1636.

CORNELIS W. OOSTERLEE
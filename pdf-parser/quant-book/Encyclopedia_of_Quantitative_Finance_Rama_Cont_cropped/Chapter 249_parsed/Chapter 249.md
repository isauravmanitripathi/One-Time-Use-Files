# **Sparse Grids**

The sparse grid method is a general numerical discretization technique for multivariate function representation, integration and partial differential equations. This approach, first introduced by the Russian mathematician Smolyak in 1963 [26], constructs a multidimensional multilevel basis by a special truncation of the tensor product expansion of a one-dimensional multilevel basis (see Figure 1 for an example of a sparse grid).

Discretizations on sparse grids involve only  $O(N(\log N)^{d-1})$  degrees of freedom, where d is the problem dimension and  $N$  denotes the number of degrees of freedom in one coordinate direction. The accuracy obtained this way is comparable to one using a full tensor product basis involving  $O(N^d)$ degrees of freedom, if the underlying problem is smooth enough, that is, if the solution has bounded mixed derivatives.

This way, the curse of dimension, that is, the exponential dependence of conventional approaches on the dimension  $d$ , can be overcome to a certain extent. This makes the sparse grid approach particularly attractive for the numerical solution of moderate and higher dimensional problems. Still, the classical sparse grid method is not completely independent of the dimension due to the above logarithmic term in the complexity.

Sparse grid methods are known under various names, such as hyperbolic cross points, discrete blending, Boolean interpolation, or splitting extrapolation. For a comprehensive introduction to sparse grids, see [5].

In computational finance, sparse grid methods have been employed for the valuation of *multiasset* options such as basket [24] (see Basket Options) or outperformance options [12], various types of pathdependent derivatives, due to the high dimension of the arising partial differential equations, or integration problems.

### **One-dimensional Multilevel Basis**

The first ingredient of a sparse grid method is a onedimensional multilevel basis. In the classical sparse grid approach, a hierarchical basis based on standard

hat functions,

$$\phi(x) := \begin{cases}\n1 - |x| & \text{if } x \in [-1, 1], \\
0 & \text{otherwise}\n\end{cases} \tag{1}$$

is used. Then, a set of equidistant grids  $\Omega_l$  of level l on the unit interval  $\bar{\Omega} = [0, 1]$  and mesh width  $2^{-l}$ is considered. The grid points  $x_{l,i}$  are given by

$$x_{l,i} := i \cdot h_l, 0 \le i \le 2^l \tag{2}$$

The standard hat function is then taken to generate a family of basis functions  $\phi_{l,i}(x)$  having support  $[x_{l,i} - h_l, x_{l,i} + h_l]$  by dilation and translation, that is.

$$\phi_{l,i}(x) := \phi\left(\frac{x - i \cdot h_l}{h_l}\right) \tag{3}$$

Thereby, the index  $i$  indicates the location of a basis function or a grid point. This basis is usually termed as nodal basis or Lagrange basis (see Figure 2, bottom). These basis functions are then used to define function spaces  $V_l$  consisting of piecewise linear functions<sup>a</sup>

$$V_{l} := \text{span} \left\{ \phi_{l,i} : 1 \le i \le 2^{l} - 1 \right\} \tag{4}$$

With these function spaces, the hierarchical increment spaces  $W_l$ ,

$$W_l := \text{span}\left\{\phi_{l,i} : i \in I_l\right\} \tag{5}$$

using the index set

$$I_l = \{i \in \mathbb{N} : 1 \le i \le 2^l - 1, i \text{ odd}\}\tag{6}$$

are defined. These increment spaces satisfy the relation

$$V_l = \bigoplus_{k \le l} W_k \tag{7}$$

The basis corresponding to  $W_l$  is hierarchical basis (see Figure 2, top) and any function  $u \in V_l$  can be uniquely represented as

$$u(x) = \sum_{k=1}^{l} \sum_{i \in I_k} v_{k,i} \cdot \phi_{k,i}(x) \tag{8}$$

with coefficient values  $v_{k,i} \in \mathbb{R}$ . Note that the supports of all basis functions  $\phi_{k,i}$  spanning  $W_k$  are mutually disjoint.

| ٠ |                   |                           | ٠.<br>$\bullet$                            | ٠                                 |
|---|-------------------|---------------------------|--------------------------------------------|-----------------------------------|
|   | . .<br>٠          | ٠<br>$\cdot$ $\cdot$<br>٠ | $\cdot \cdot \cdot \cdot$<br>. .<br>٠<br>٠ | $\cdot$ $\cdot$ $\cdot$<br>٠<br>٠ |
|   | ٠<br>٠            | :<br>٠                    | :<br>٠.                                    | $\mathbf{.}$                      |
|   |                   |                           | i                                          |                                   |
| ٠ | ٠<br>٠<br>$\cdot$ | .<br>٠                    | ٠<br>٠                                     | ٠<br>٠<br>٠                       |
|   | ٠                 | ٠<br>:<br>٠               | :                                          | ٠<br>. .                          |
|   | ٠                 | ٠                         |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
|   |                   |                           |                                            |                                   |
| ٠ | ٠<br>٠<br>$\cdot$ | $\bullet$                 | ٠                                          | ٠                                 |
|   |                   |                           | ĺ<br>$\cdot$<br>. .                        | ٠<br>٠                            |
|   | ٠                 | ٠                         | ٠                                          |                                   |

**Figure 1** A regular two-dimensional sparse grid of level 7

![](_page_1_Figure_3.jpeg)

Figure 2 Piecewise linear hierarchical basis (a) versus nodal basis (b) of level 4

## **Tensor Product Construction**

From this one-dimensional hierarchical basis, a multidimensional basis on the  $d$ -dimensional unit cube  $\bar{\Omega} := [0, 1]^d$  is obtained by a tensor product construction. With the multiindex  $\mathbf{l} = (l_1, \ldots, l_d) \in \mathbb{N}^d$ , which indicates the level in a multivariate sense, the set of d-dimensional standard rectangular grids  $\Omega_l$ on  $\bar{\Omega}$  with mesh size  $\mathbf{h}_{\mathbf{l}} := (h_{l_1}, \ldots, h_{l_d}) := 2^{-\mathbf{l}}$  are

considered. Each grid  $\Omega_{l}$  is equidistant with respect to each individual coordinate direction, but, in general, may have varying mesh sizes in the different directions. The grid points  $x_{l,i}$  of the grid  $\Omega_l$  are the points

$$\mathbf{x}_{\mathbf{l},\mathbf{i}} := (x_{l_1,i_1}, \dots, x_{l_d,i_d}), \mathbf{1} \le \mathbf{i} \le 2^{\mathbf{l}} - \mathbf{1} \qquad (9)$$

where for the above multiindices, all arithmetic operations are to be understood component-wise.

Then, for each grid point  $\mathbf{x}_{l,i}$ , an associated piecewise *d*-linear basis function  $\phi_{l,i}(x)$  (see Figure 3) is defined as the product of the one-dimensional basis functions

$$\phi_{\mathbf{l},\mathbf{i}}(\mathbf{x}) := \prod_{j=1}^{a} \phi_{l_j,i_j}(x_j) \tag{10}$$

Each of the multidimensional (nodal) basis functions  $\phi_{\text{L,i}}$  has a support of size  $2 \cdot \mathbf{h}_{\text{L}}$ . These basis functions are again used to define function spaces  $V_1$  consisting of piecewise  $d$ -linear functions, which are 0 on the boundary of  $\bar{\Omega}$ ,

$$V_{\mathbf{l}} := \operatorname{span} \left\{ \phi_{\mathbf{l},\mathbf{i}} : \mathbf{1} \le \mathbf{i} \le 2^{\mathbf{l}} - \mathbf{1} \right\} \tag{11}$$

Similar to the one-dimensional case, the hierarchical increments  $W_1$  are defined by

$$W_{\mathbf{l}} := \text{span}\left\{\phi_{\mathbf{l},\mathbf{i}} : \mathbf{i} \in \mathbf{I}_{\mathbf{l}}\right\} \tag{12}$$

with the index set

$$\mathbf{I}_{\mathbf{l}} := \left\{ \mathbf{i} \in \mathbb{N}^{d} : \mathbf{1} \le \mathbf{i} \le 2^{\mathbf{l}} - \mathbf{1}, \atop i_{j} \text{ odd for all } 1 \le j \le d \right\}$$
(13)

This way, the hierarchical increment spaces  $W_1$  are related to the nodal spaces  $V_1$  by

$$V_{\mathbf{l}} = \bigoplus_{\mathbf{k} \le \mathbf{l}} W_{\mathbf{k}} \tag{14}$$

Again, the supports of all multidimensional hierarchical basis functions  $\phi_{\text{Li}}$  spanning  $W_{\text{I}}$  are mutually disjoint. Also, again each function  $u \in V_1$  can uniquely be represented by

$$u_{\mathbf{l}}(\mathbf{x}) = \sum_{\mathbf{k}=\mathbf{1}}^{l} \sum_{\mathbf{i} \in \mathbf{I}_{\mathbf{k}}} v_{\mathbf{k},\mathbf{i}} \cdot \phi_{\mathbf{k},\mathbf{i}}(\mathbf{x}) \tag{15}$$

with hierarchical coefficients  $v_{k,i} \in \mathbb{R}$ .

![](_page_2_Figure_1.jpeg)

**Figure 3** Tensor product approach to generate the piecewise bilinear basis functions  $\phi_{(2,1),(1,1)}$  and  $\phi_{(2,1),(1,1)}$  from the one-dimensional basis functions  $\phi_{2,1}, \phi_{2,2}$  and  $\phi_{1,1}$ 

## **Classical Sparse Grids**

The classical sparse grid construction arises from a cost-to-benefit analysis in function approximation. Thereby, functions  $u: \Omega \to \mathbb{R}$  which have bounded mixed second derivatives

$$D^{\alpha}u := \frac{\partial^{|\alpha|_1}u}{\partial x_1^{\alpha_1}\dots\partial x_d^{\alpha_d}}\tag{16}$$

for  $|\alpha|_{\infty} \leq 2$  are considered. These functions belong to the Sobolev space  $H_2^{\text{mix}}(\bar{\Omega})$  with

$$H_2^{\text{mix}}(\bar{\Omega}) := \{ u : \bar{\Omega} \to \mathbf{R} : D^{\alpha}u \in L_2(\Omega), \newline \times |\boldsymbol{\alpha}|_{\infty} \le 2, u|_{\partial\Omega} = 0 \}$$
(17)

Here, the two norms  $|\pmb{\alpha}|_1$  and  $|\pmb{\alpha}|_{\infty}$  for multiindices are defined by

$$|\boldsymbol{\alpha}|_1 := \sum_{j=1}^d \alpha_j \text{ and } |\boldsymbol{\alpha}|_{\infty} := \max_{1 \le j \le d} \alpha_j$$
 (18)

For functions  $u \in H_2^{\text{mix}}(\bar{\Omega})$ , the hierarchical coefficients  $v_{\mathbf{l},i}$  decay as

$$|v_{\mathbf{l},\mathbf{i}}| = O\left(2^{-2|\mathbf{l}|_1}\right) \tag{19}$$

On the other hand, the size (i.e., the number of degrees of freedom) of the subspaces  $W_1$  is given by

$$|W_{\mathbf{l}}| = O\left(2^{|\mathbf{l}|_1}\right) \tag{20}$$

An optimization with respect to the number of degrees of freedom and the resulting approximation accuracy directly leads to *sparse grid* spaces  $\hat{V}_n$  of level  $n$  defined by

$$\hat{V}_n := \bigoplus_{|\mathbf{l}|_1 \le n + d - 1} W_{\mathbf{l}} \tag{21}$$

![](_page_2_Figure_16.jpeg)

**Figure 4** All subspaces  $W_1$  for levels  $|l|_{\infty} \leq 3$  which together form the full grid space  $V_3$ . The corresponding sparse grid space  $\hat{V}_3$  consists of all subspaces above the dashed line ( $|\mathbf{l}|_1 \le 4$ )

In comparison to the standard full grid space

$$V_n := V_{(n,\ldots,n)} = \bigoplus_{|\mathbf{l}|_{\infty} \le n} W_{\mathbf{l}} \tag{22}$$

which corresponds to cubic sectors of subspaces, sparse grids use triangular or simplicial sectors, see Figure 4. The dimension of the space  $\hat{V}_n$ , that is, the number of degrees of freedom or grid points is given by

$$\left| \hat{V}_n \right| = \sum_{i=0}^{n-1} 2^i \cdot \binom{d-1+i}{d-1}$$
  
=  $O(h_n^{-1} \cdot |\log_2 h_n|^{d-1})$  (23)

This shows the order  $O(2^n n^{d-1})$ , which is a significant reduction of the number of degrees of freedom and, thus, of the computational and storage requirement compared to the order  $O(2^{nd})$  of the dimension of the full grid space  $|V_n|$ .

On the other hand, the approximation accuracy of the sparse grid spaces for functions  $u \in H_2^{\text{mix}}(\bar{\Omega})$  is in the  $L_p$  norms for  $1 \le p \le \infty$  given by

$$||u - \hat{u}_n||_p = O(h_n^2 \cdot n^{d-1}) \tag{24}$$

For the corresponding full grid spaces, the accuracy is

$$||u - u_n||_p = O(h_n^2)$$
 (25)

This shows the crucial advantage of the sparse grid space  $\hat{V}_n$  in comparison with the full grid space  $V_n$ : the number of degrees of freedom is significantly reduced, whereas the accuracy is only slightly deteriorated. This way, the curse of dimensionality can be overcome, at least to some extent. The dimension still enters through logarithmic terms both in the computational cost and the accuracy estimate as well as in the constants hidden in the order notation.

#### **Extensions and Applications**

The classical sparse grid concept has been generalized in various ways. First, there are special sparse grids, which are optimized with respect to the energy seminorm [4]. These energy-based sparse grids are further sparsified and possess a cost complexity of  $O(h_n^{-1})$  for an accuracy of  $O(h_n)$ . Thus, the dependence on the dimension  $d$  in the order is completely removed (but is still present in the hidden constants [8]). A generalization to sparse grids, which is optimal with respect to other Sobolev norms, can be found in  $[13]$ . In case the underlying space is not known *a priori*, dimension-adaptive methods [11] can be applied to find optimized sparse grids.

The sparse grid approach based on piecewise linear interpolation can be generalized to higher order polynomial [5] or wavelet discretizations (e.g., interpolets or prewavelets) [15, 25], which allows to utilize additional properties (such as higher polynomial exactness or vanishing moments) of the basis.

Furthermore, sparse grid methods can be applied to nonsmooth problems by using spatially adaptive refinement methods [2], see Figure 5 for an adaptively refined sparse grid. Spatial adaptivity helps if the original smoothness conditions for the sparse grid approach are not fulfilled. This is the case in nearly

![](_page_3_Figure_11.jpeg)

Figure 5 An at-a-corner singularity adaptively refined three-dimensional sparse grid

all option pricing problems since they lead to discontinuities in the initial conditions, which can, in some cases, extend into the interior of the domain. Here, adaptive refinement methods can often attain the same convergence rates as for smooth problems, which can be shown using approximation theory in Besov spaces [20]. Additionally, transformations that align areas of discontinuities with coordinate axes can significantly enhance the efficiency of sparse grid methods, as was shown in  $[24]$ .

Sparse grids have been applied for the solution of different kinds of low- and moderate-dimensional partial differential equations, such as elliptic [5, 27], parabolic [1, 14], and hyperbolic [17] problems. In this context, finite element methods [2], finite difference methods [7], and finite volume methods [19] have been used in the discretization process.

For the solution of partial differential equations, often the so-called combination technique [9] is employed. Here, a sparse grid solution is obtained by a combination of anisotropic full grid solutions according to the combination formula

$$\hat{u}_{n}(\mathbf{x}) = \sum_{n \leq |\mathbf{l}|_{1} \leq n+d-1} (-1)^{n+d-|\mathbf{l}|_{1}-1} \begin{pmatrix} d-1 \\ |\mathbf{l}|_{1}-n \end{pmatrix} u_{1}(\mathbf{x})$$
(26)

![](_page_4_Figure_1.jpeg)

Figure 6 The combination technique in two dimensions for level  $n = 3$ : combine coarse full grids  $\Omega_{\mathbf{l}}, |\mathbf{l}|_{1} \in \{3, 4\},\$ with mesh widths  $2^{-l_1}$  and  $2^{-l_2}$  to get a sparse grid  $\hat{\Omega}_n$ corresponding to  $\hat{V}_n$ 

where  $u_1(\mathbf{x})$  is a full grid solution on an anisotropic grid with mesh width  $2^{-l}$ , see Figure 6 for a twodimensional example. The combination technique can be further optimized with respect to the underlying differential operator  $[18]$ .

The sparse grid approach can also be used for numerical integration, for example, for the computation of expectations [10, 23]. Thereby, the classical sparse grid construction starts with a sequence of onedimensional quadrature formulas  $Q_1 f$  using  $n_1$  points to integrate a function  $f$  on the unit interval [0, 1],

$$Q_l f := \sum_{i=1}^{n_l} w_{li} \cdot f(x_{li})$$
 (27)

Using the difference quadrature formulas

$$\Delta_k f := (Q_k - Q_{k-1})f \text{ with } Q_0 f := 0 \qquad (28)$$

the sparse grid quadrature formula  $Q_n f$  of level n for a d-dimensional function f on the cube  $[0, 1]^d$ is then defined by

$$\hat{Q}_n f := \sum_{\|\mathbf{l}\|_1 \le n + d - 1} (\Delta_{l_1} \otimes \cdots \otimes \Delta_{l_d}) f \qquad (29)$$

Again, this construction can be improved by using spatially adaptive or dimension-adaptive refinement [3, 11].

The sparse grid methodology has also been successfully applied to the solution of integral equations [16], interpolation and approximation [21], and data analysis  $[6, 22]$ .

## **End Notes**

<sup>a.</sup>In order to simplify this exposition, we assume that the functions in  $V_l$  are 0 on the boundary of  $\bar{\Omega}$ . This restriction can be overcome by adding appropriate boundary basis functions.

# References

- [1] Balder, R. & Zenger, C. (1996). The solution of the multidimensional real Helmholtz equation on sparse grids, SIAM Journal on Scientific Computing 17, 631-646.
- [2] Bungartz, H. (1992). An adaptive Poisson solver using hierarchical bases and sparse grids, in Iterative Methods in Linear Algebra, R. Beauwens, ed, North-Holland, рр. 293-310.
- [3] Bungartz, H. & Dirnstorfer, S. (2003). Multivariate quadrature on adaptive sparse grids, Computing 71,  $89 - 114$
- [4] Bungartz, H. & Griebel, M. (1999). A note on the complexity of solving Poisson's equation for spaces of bounded mixed derivatives, Journal of Complexity 15,  $1 - 121$
- [5] Bungartz, H. & Griebel, M. (2004). Sparse grids, Acta Numerica 13, 147-269.
- Garcke, J., Griebel, M. & Thess, M. (2001). Data mining [6] with sparse grids, Computing 67, 225-253.
- [7] Griebel, M. (1998). Adaptive sparse grid multilevel methods for elliptic PDEs based on finite differences, Computing 61, 151-179.
- Griebel, M. (2006). Sparse grids and related approx-[8] imation schemes for higher dimensional problems, in Proceedings of FoCM05, L. Pardo, A. Pinkus, E. Suli & M. Todd, eds, Cambridge University Press.
- [9] Griebel, M., Schneider, M. & Zenger, C. (1992). A combination technique for the solution of sparse grid problems, in Iterative Methods in Linear Algebra, P. de Groen & R. Beauwens, eds, Elsevier, pp. 263-281.
- [10] Gerstner, T. & Griebel, M. (1998). Numerical integration using sparse grids, Numerical Algorithms 18, 209-232.
- [11] Gerstner, T. & Griebel, M. (2003). Dimension-adaptive tensor-product quadrature, *Computing* **71**, 65–87.
- Gerstner, T. & Holtz, M. (2008). Valuation of perfor-[12] mance-dependent options, Applied Mathematical Finance  $15$ , 1–20.
- [13] Griebel, M. & Knapek, S. (2000). Optimized tensorproduct approximation spaces, Constructive Approximation 16, 525-540.
- $[14]$ Griebel, M. & Oeltz, D. (2007). A sparse grid space-time discretization scheme for parabolic problems, Computing  $81$ , 1–34.

- [15] Griebel, M. & Oswald, P. (1995). Tensor product type subspace splitting and multilevel iterative methods for anisotropic problems, Advances in Computational Mathematics 4, 171-206.
- [16] Griebel, M., Oswald, P. & Schiekofer, T. (1999). Sparse grids for boundary integral equations, Numerishche Mathematik 83, 279-312.
- [17] Griebel, M. & Zumbusch, G. (1999). Adaptive sparse grids for hyperbolic conservation laws, in *Hyperbolic* Problems: Theory, Numerics, Applications, M. Fey & R. Jeltsch, eds, Birkhäuser, pp. 411-422.
- [18] Hegland, M., Garcke, J. & Challis, V. (2007). The combination technique and some generalisations, Linear Algebra and Its Applications 420, 249-275.
- [19] Hemker, P. (1995). Sparse-grid finite-volume multigrid for 3D-problems, Advances in Computational Mathematics 4,  $83-110$ .
- [20] Hochmuth, R. (2001). Wavelet characterizations of anisotropic Besov spaces, Applied and Computational Harmonic Analysis 12, 179-208.
- [21] Klimke, A. & Wohlmuth, B. (2005). Algorithm 847: Spinterp: piecewise multilinear hierarchical sparse grid interpolation in MATLAB, ACM Transactions on Mathematical Software 31, 561-579.
- [22] Laffan, S., Nielsen, O., Silcock, H. & Hegland, M. (2005). Sparse grids: a new predictive modelling method for the analysis of geographical data, *International Jour*nal of Geographical Information Science 19, 267-292.

- [23] Novak, E. & Ritter, K. (1996). High dimensional integration of smooth functions over cubes, Numerische Mathematik 75, 79-97.
- [24] Reisinger, C. & Wittum, G. (2007). Efficient hierarchical approximation of high-dimensional option pricing problems, SIAM Journal on Scientific Computing 29,  $440 - 458.$
- [25] Schwab, C. & Todor, R. (2003). Sparse finite elements for stochastic elliptic problems: higher order moments, Computing 71, 43-63.
- [26] Smolyak, S. (1963). Interpolation and quadrature formulas for the classes  $W_s^a$  and  $E_s^a$ , Soviet Mathematics Doklady 4, 240-243.
- [27] Zenger, C. (1991). Sparse grids, in *Parallel Algorithms* for Partial Differential Equations, W. Hackbusch, ed, Vieweg, pp. 241–251.

# **Related Articles**

Finite Difference Methods for Barrier Options; Finite Difference Methods for Early Exercise Options; Finite Element Methods; Wavelet Galerkin Method.

THOMAS GERSTNER & MICHAEL GRIEBEL
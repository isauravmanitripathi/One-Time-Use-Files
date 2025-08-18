This chapter discusses alternatives to Monte Carlo simulation known as *quasi*-*Monte Carlo* or *low-discrepancy* methods. These methods differ from ordinary Monte Carlo in that they make no attempt to mimic randomness. Indeed, they seek to increase accuracy specifically by generating points that are too evenly distributed to be random. Applying these methods to the pricing of derivative securities requires formulating a pricing problem as the calculation of an integral and thus suppressing its stochastic interpretation as an expected value. This contrasts with the variance reduction techniques of Chapter 4, which take advantage of the stochastic formulation to improve precision.

Low-discrepancy methods have the potential to accelerate convergence from the  $O(1/\sqrt{n})$  rate associated with Monte Carlo (*n* the number of paths or points generated) to nearly  $O(1/n)$  convergence: under appropriate conditions, the error in a quasi-Monte Carlo approximation is  $O(1/n^{1-\epsilon})$  for all  $\epsilon > 0$ . Variance reduction techniques, affecting only the implicit constant in  $O(1/\sqrt{n})$ , are not nearly so ambitious. We will see, however, that the  $\epsilon$  in  $O(1/n^{1-\epsilon})$  hides a dependence on problem *dimension*.

The tools used to develop and analyze low-discrepancy methods are very different from those used in ordinary Monte Carlo, as they draw on number theory and abstract algebra rather than probability and statistics. Our goal is therefore to present key ideas and methods rather than an account of the underlying theory. Niederreiter  $[281]$  provides a thorough treatment of the theory.

## 5.1 General Principles

This section presents definitions and results from the theory of quasi-Monte Carlo (QMC) methods. It is customary in this setting to focus on the problem of numerical integration over the unit hypercube. Recall from Section 1.1 and the many examples in Chapter 3 that each replication in a Monte Carlo simulation can be interpreted as the result of applying a series of transformations

(implicit in the simulation algorithm) to an input sequence of independent uniformly distributed random variables  $U_1, U_2, \ldots$  Suppose there is an upper bound  $d$  on the number of uniforms required to produce a simulation output and let  $f(U_1,\ldots,U_d)$  denote this output. For example, f may be the result of transformations that convert the  $U_i$  to normal random variables, the normal random variables to paths of underlying assets, and the paths to the discounted payoff of a derivative security. We suppose the objective is to  $\text{calculate}$ 

$$\mathsf{E}[f(U_1,\ldots,U_d)] = \int_{[0,1)^d} f(x) \, dx. \tag{5.1}$$

Quasi-Monte Carlo approximates this integral using

$$\int_{[0,1)^d} f(x) \, dx \approx \frac{1}{n} \sum_{i=1}^n f(x_i), \tag{5.2}$$

for carefully (and deterministically) chosen points  $x_1, \ldots, x_n$  in the unit hypercube  $[0,1)^d$ .

A few issues require comment:

- $\circ$  The function f need not be available in any explicit form; we merely require a method for evaluating  $f$ , and this is what a simulation algorithm does.
- $\circ$  Whether or not we include the boundary of the unit hypercube in (5.1) and  $(5.2)$  has no bearing on the value of the integral and is clearly irrelevant in ordinary Monte Carlo. But some of the definitions and results in QMC require care in specifying the set to which points on a boundary belong. It is convenient and standard to take intervals to be closed on the left and open on the right, hence our use of  $[0,1)^d$  as the unit hypercube.
- o In ordinary Monte Carlo simulation, taking a scalar i.i.d. sequence of uniforms  $U_1, U_2, \ldots$  and forming vectors  $(U_1, \ldots, U_d), (U_{d+1}, \ldots, U_{2d}), \ldots$  produces an i.i.d. sequence of points from the  $d$ -dimensional hypercube. In QMC, the construction of the points  $x_i$  depends explicitly on the dimension of the problem — the vectors  $x_i$  in  $[0,1)^d$  cannot be constructed by taking sets of  $d$  consecutive elements from a scalar sequence.

The dependence of QMC methods on problem dimension is one of the features that most distinguishes them from Monte Carlo. If two different Monte Carlo algorithms corresponding to functions  $f: [0,1]^{d_1} \to \Re$  and  $g: [0,1)^{d_2} \rightarrow \Re$  resulted in  $f(U_1,\ldots,U_{d_1})$  and  $g(U_1,\ldots,U_{d_2})$  having the same distribution, then these two algorithms would have the same bias and variance properties. The preferred algorithm would be the one requiring less time to evaluate; the dimensions  $d_1, d_2$  would be irrelevant except to the extent that they affect the computing times. In ordinary Monte Carlo one rarely even bothers to think about problem dimension, whereas in QMC the dimension must be identified explicitly before points can be generated. Lowerdimensional representations generally result in smaller errors. For some Monte Carlo algorithms, there is no upper bound  $d$  on the number of input uniforms

required per output; this is true, for example, of essentially all simulations using acceptance-rejection methods, as noted in Section  $2.2.2$ . Without an upper bound  $d$ , QMC methods are inapplicable.

For the rest of this chapter, we restrict attention to problems with a finite dimension d and consider approximations of the form in  $(5.2)$ . The goal of low-discrepancy methods is to construct points  $x_i$  that make the error in  $(5.2)$  small for a large class of integrands f. It is intuitively clear (and, as we will see, correct in a precise sense) that this is equivalent to choosing the points  $x_i$  to fill the hypercube uniformly.

### 5.1.1 Discrepancy

 $\mathbb{R}^{\mathbb{C}}$ 

A natural first attempt at filling the hypercube uniformly would choose the  $x_i$  to lie on a grid. But grids suffer from several related shortcomings. If the integrand  $f$  is nearly a separable function of its  $d$  arguments, the information contained in the values of f at  $n^d$  grid points is nearly the same as the information in just  $nd$  of these values. A grid leaves large rectangles within  $[0,1)^d$  devoid of any points. A grid requires specifying the total number of points  $n$  in advance. If one refines a grid by adding points, the number of points that must be added to reach the next favorable configuration grows very quickly. Consider, for example, a grid constructed as the Cartesian product of  $2^k$  points along each of d dimensions for a total of  $2^{kd}$  points. Now refine the grid by adding a point in each gap along each dimension; i.e., by doubling the number of points along each dimension. The total number of points added to the original grid to reach the new grid is  $2^{(k+1)d} - 2^{kd}$ , which grows very quickly with  $k$ . In contrast, there are low-discrepancy sequences with guarantees of uniformity over bounded-length extensions of an initial segment of the sequence.

To make these ideas precise, we need a precise notion of uniformity  $-$  or rather deviation from uniformity, which we measure through various notions of *discrepancy*. Given a collection  $\mathcal{A}$  of (Lebesgue measurable) subsets of  $[0,1)^d$ , the discrepancy of the point set  $\{x_1,\ldots,x_n\}$  relative to  $\mathcal{A}$  is

$$D(x_1,\ldots,x_n;\mathcal{A}) = \sup_{A\in\mathcal{A}} \left| \frac{\#\{x_i\in A\}}{n} - \text{vol}(A) \right|.$$
(5.3)

Here,  $\#\{x_i \in A\}$  denotes the number of  $x_i$  contained in A and vol(A) denotes the volume (measure) of  $A$ . Thus, the discrepancy is the supremum over errors in integrating the indicator function of A using the points  $x_1, \ldots, x_n$ . (In all interesting cases the  $x_i$  are distinct points, but to cover the possibility of duplication, count each point according to its multiplicity in the definition of discrepancy.)

Taking  $\mathcal{A}$  to be the collection of all rectangles in  $[0,1)^d$  of the form

$$\prod_{j=1}^{d} [u_j, v_j), \quad 0 \le u_j < v_j \le 1,$$

yields the ordinary (or *extreme*) discrepancy  $D(x_1,\ldots,x_n)$ . Restricting  $\mathcal{A}$  to rectangles of the form

$$\prod_{j=1}^{d} [0, u_j) \tag{5.4}$$

defines the *star* discrepancy  $D^*(x_1,\ldots,x_n)$ . The star discrepancy is obviously no larger than the ordinary discrepancy; Niederreiter [281], Proposition 2.4, shows that

$$D^*(x_1,\ldots,x_n) \leq D(x_1,\ldots,x_n) \leq 2^d D^*(x_1,\ldots,x_n),$$

so for fixed  $d$  the two quantities have the same order of magnitude.

Requiring each of these discrepancy measures to be small is consistent with an intuitive notion of uniformity. However, both measures focus on products of intervals and ignore, for example, a rotated subcube of the unit hypercube. If the integrand  $f$  represents a simulation algorithm, the coordinate axes may not be particularly meaningful. The asymmetry of the star discrepancy may seem especially odd: in a Monte Carlo simulation, we could replace any uniform input  $U_i$  with  $1-U_i$  and thus interchange 0 and 1 along one coordinate. If, as may seem more natural, we take  $\mathcal{A}$  to be all convex subsets of  $[0,1]^d$ , we get the *isotropic* discrepancy; but the magnitude of this measure can be as large as the dth root of the ordinary discrepancy (see p.17 of Niederreiter [281] and Chapter 3 of Matoušek  $[256]$ ). We return to this point in Section 5.1.3.

We will see in Section  $5.1.3$  that these notions of discrepancy are indeed relevant to measuring the approximation error in  $(5.2)$ . It is therefore sensible to look for points that achieve low values of these discrepancy measures, and that is what low-discrepancy methods do.

In dimension  $d = 1$ , Niederreiter [281], pp.23–24, shows that

$$D^*(x_1, \dots, x_n) \ge \frac{1}{2n}, \quad D(x_1, \dots, x_n) \ge \frac{1}{n}, \tag{5.5}$$

and that in both cases the minimum is attained by

$$x_i = \frac{2i-1}{2n}, \quad i = 1, \dots, n.$$
 (5.6)

For this set of points,  $(5.2)$  reduces to the midpoint rule for integration over the unit interval. Notice that  $(5.6)$  does not define the first n points of an infinite sequence; in fact, the set of points defined by  $(5.6)$  has no values in common with the corresponding set for  $n+1$ .

Suppose, in contrast, that we fix an infinite sequence  $x_1, x_2, \ldots$  of points in  $[0, 1)$  and measure the discrepancy of the first n points. From the perspective of numerical integration, this is a more relevant case if we hope to be able to increase the number of points in an approximation of the form  $(5.2)$ . Niederreiter [281],  $p.24$ , cites references showing that in this case

 $5.1$  General Principles  $285$ 

$$D(x_1,\ldots,x_n) \ge D^*(x_1,\ldots,x_n) \ge \frac{c \log n}{n}$$

for infinitely many  $n$ , with  $c$  a constant. This situation is typical of lowdiscrepancy methods, even in higher dimensions: one can generally achieve a lower discrepancy by fixing the number of points  $n$  in advance; using the first  $n$  points of a sequence rather than a different set of points for each  $n$  typically increases discrepancy by a factor of  $\log n$ .

Much less is known about the best possible discrepancy in dimensions higher than 1. Niederreiter [281],  $p.32$ , states that "it is widely believed" that in dimensions  $d \geq 2$ , any point set  $x_1, \ldots, x_n$  satisfies

$$D^*(x_1,\ldots,x_n) \ge c_d \frac{(\log n)^{d-1}}{n}$$

and the first *n* elements of any sequence  $x_1, x_2, \ldots$  satisfy

$$D^*(x_1,\ldots,x_n) \ge c'_d \frac{(\log n)^d}{n},$$

for constants  $c_d$ ,  $c'_d$  depending only on the dimension d. These order-ofmagnitude discrepancies are achieved by explicit constructions (discussed in Section  $5.2$ ). It is therefore customary to reserve the informal term "lowdiscrepancy" for methods that achieve a star discrepancy of  $O((\log n)^d/n)$ . The logarithmic term can be absorbed into any power of  $n$ , allowing the looser bound  $O(1/n^{1-\epsilon})$ , for all  $\epsilon > 0$ .

Although any power of  $\log n$  eventually becomes negligible relative to n, this asymptotic property may not be relevant at practical values of  $n$  if  $d$  is large. Accordingly, QMC methods have traditionally been characterized as appropriate only for problems of moderately high dimension, with some authors putting the upper limit at 40 dimensions, others putting it as low as 12 or 15. But in many recent applications of QMC to problems in finance, these methods have been found to be effective in much higher dimensions. We present some evidence of this in Section  $5.5$  and comment further in Section  $5.6$ .

### 5.1.2 Van der Corput Sequences

Before proceeding with a development of further theoretical background, we introduce a specific class of one-dimensional low-discrepancy sequences called Van der Corput sequences. In addition to illustrating the general notion of discrepancy, this example provides the key element of many multidimensional constructions.

By a *base* we mean an integer  $b \ge 2$ . Every positive integer k has a unique representation (called its base-b or b-ary expansion) as a linear combination of nonnegative powers of b with coefficients in  $\{0, 1, \ldots, b-1\}$ . We can write  $\text{this as}$ 

 $\gamma$ 

$$k = \sum_{j=0}^{\infty} a_j(k) b^j, \qquad (5.7)$$

with all but finitely many of the coefficients  $a_i(k)$  equal to zero. The *radical inverse function*  $\psi_b$  maps each k to a point in [0, 1) by flipping the coefficients of k about the base-b "decimal" point to get the base-b fraction  $.a_0a_1a_2...$ More precisely,

$$\psi_b(k) = \sum_{j=0}^{\infty} \frac{a_j(k)}{b^{j+1}}.$$
(5.8)

The base-b Van der Corput sequence is the sequence  $0 = \psi_b(0), \psi_b(1), \psi_b(2),$  $\ldots$  Its calculation is illustrated in Table 5.1 for base 2.

| k | $k$ Binary | $\psi_2(k)$ Binary | $\left\langle k\right\rangle$ |
|---|------------|--------------------|-------------------------------|
| 0 | 0          | 0                  |                               |
| 1 | 1          | 0.1                | 1/2                           |
| 2 | 10         | 0.01               | 1/4                           |
| 3 | 11         | 0.11               | 3/4                           |
| 4 | 100        | 0.001              | 1/8                           |
| 5 | 101        | 0.101              | 5/8                           |
| 6 | 110        | 0.011              | 3/8                           |
| 7 | 111        | 0.111              | 7/8                           |

**Table 5.1.** Illustration of radical inverse function  $\psi_b$  in base  $b = 2$ .

Figure 5.1 illustrates how the base-2 Van der Corput sequence fills the unit interval. The kth row of the array in the figure shows the first  $k$  nonzero elements of the sequence; each row refines the previous one. The evolution of the point set is exemplified by the progression from the seventh row to the last row, in which the "sixteenths" are filled in. As these points are added, they appear on alternate sides of  $1/2$ : first  $1/16$ , then  $9/16$ , then  $5/16$ , and so on. Those that are added to the left of  $1/2$  appear on alternate sides of  $1/4$ : first  $1/16$ , then  $5/16$ , then  $3/16$ , and finally  $7/16$ . Those on the right side of  $1/2$ similarly alternate between the left and right sides of  $3/4$ . Thus, while a naive refinement might simply insert the new values in increasing order  $1/16, 3/16,$  $5/16, \ldots, 15/16$ , the Van der Corput inserts them in a maximally balanced wav.

The effect of the size of the base  $b$  can be seen by comparing Figure 5.1 with the Van der Corput sequence in base 16. The first 15 nonzero elements of this sequence are precisely the values appearing the last row of Figure 5.1, but now they appear in increasing order. The first seven values of the base-16 sequence are all between 0 and  $1/2$ , whereas those of the base-2 sequence are spread uniformly over the unit interval. The larger the base, the greater the number of points required to achieve uniformity.

|                               |                                                                       |                | $\frac{1}{4}$                                     |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
|-------------------------------|-----------------------------------------------------------------------|----------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------|----------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------------------|-----------------|
|                               |                                                                       |                |                                                   |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 | $\frac{3}{4}$                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                 |                                     |                 |
|                               |                                                                       |                |                                                   |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
|                               |                                                                       |                | $\frac{1}{4} \quad \frac{1}{4} \quad \frac{1}{4}$ |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
|                               |                                                                       |                | $\frac{1}{4}$                                     |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
|                               | $\frac{1}{8}$ $\frac{1}{8}$ $\frac{1}{8}$ $\frac{1}{8}$ $\frac{1}{8}$ |                |                                                   |                                                                                                                                      | 38 38 38      |                | $\frac{1}{2} \ \frac{1}{2} \ \frac{1}{2} \ \frac{1}{2} \ \frac{1}{2} \ \frac{1}{2} \ \frac{1}{2} \ \frac{1}{2}$ |                                                       | 518 518 518 518 518 |                 | $\begin{array}{c}3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{4} \\3\overline{$ |                 |                                     |                 |
| $\frac{1}{16}$                |                                                                       |                | $\frac{1}{4} \\ \frac{1}{4}$                      |                                                                                                                                      |               |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
|                               | $\frac{1}{8}$                                                         |                | $\frac{1}{4}$                                     |                                                                                                                                      |               |                |                                                                                                                 | $\frac{9}{16}$                                        |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
| $\frac{1}{16}$ $\frac{1}{16}$ | $\frac{1}{8}$                                                         |                | $\frac{1}{4}$                                     |                                                                                                                                      | 3 8 3 8 3 8   |                |                                                                                                                 |                                                       |                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                 |                                     |                 |
| $\frac{1}{16}$ $\frac{1}{16}$ | $\frac{1}{8}$                                                         |                | $\frac{1}{4}$                                     | $\begin{array}{r} \underline{5} \\ \underline{16} \\ \underline{5} \\ \underline{16} \\ \underline{5} \\ \underline{16} \end{array}$ |               |                | $\frac{1}{2}$<br>$\frac{1}{2}$<br>$\frac{1}{2}$                                                                 | $\frac{9}{16} \frac{9}{16} \frac{9}{16} \frac{9}{16}$ | $\frac{5}{8}$       |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $\frac{13}{16}$ |                                     |                 |
|                               | $\frac{1}{8}$                                                         | $\frac{3}{16}$ | $\frac{1}{4}$                                     |                                                                                                                                      | $\frac{3}{8}$ |                |                                                                                                                 |                                                       | $\frac{5}{8}$       |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $\frac{13}{16}$ |                                     |                 |
| $\frac{1}{16}$                | $\frac{1}{8}$                                                         | $\frac{3}{16}$ | $\frac{1}{4}$                                     | $\frac{5}{16}$                                                                                                                       | $\frac{3}{8}$ |                | $\frac{1}{2}$<br>$\frac{1}{2}$                                                                                  |                                                       | $\frac{5}{8}$       | $\frac{11}{16}$ | $\frac{3}{4}$                                                                                                                                                                                                                                                                                                                                                                                                                                                 | $\frac{13}{16}$ | 7 8 7 8 7 8 7 8 7 8 7 8 7 8 7 8 7 8 |                 |
| $\frac{1}{16}$                | $\frac{1}{8}$                                                         | $\frac{3}{16}$ | $\frac{1}{4}$                                     |                                                                                                                                      | $\frac{3}{8}$ | $\frac{7}{16}$ | $\frac{1}{2}$                                                                                                   |                                                       | $\frac{5}{8}$       | $\frac{11}{16}$ | $\frac{3}{4}$                                                                                                                                                                                                                                                                                                                                                                                                                                                 | $\frac{13}{16}$ |                                     |                 |
| $\frac{1}{16}$                | $\frac{1}{8}$                                                         | $\frac{3}{16}$ | $\frac{1}{4}$                                     | $\frac{5}{16}$ $\frac{5}{16}$                                                                                                        | $\frac{3}{8}$ | $\frac{7}{16}$ | $\frac{1}{2}$                                                                                                   | $\frac{9}{16}$ $\frac{9}{16}$                         | $\frac{5}{8}$       | $\frac{11}{16}$ | $\frac{3}{4}$                                                                                                                                                                                                                                                                                                                                                                                                                                                 | $\frac{13}{16}$ |                                     | $\frac{15}{16}$ |

Fig. 5.1. Illustration of the Van der Corput sequence in base 2. The  $k$ th row of this array shows the first  $k$  nonzero elements of the sequence.

Theorem 3.6 of Niederreiter [281] shows that all Van der Corput sequences are low-discrepancy sequences. More precisely, the star discrepancy of the first n elements of a Van der Corput sequence is  $O(\log n/n)$ , with an implicit constant depending on the base  $b$ .

### 5.1.3 The Koksma-Hlawka Bound

In addition to their intuitive appeal as indicators of uniformity, discrepancy measures play a central role in bounding the error in the approximation  $(5.2)$ . The key result in this direction is generally known as the *Koksma-Hlawka inequality* after a one-dimensional result published by Jurjen Koksma in 1942 and its generalization by Edmund Hlawka in 1961. This result bounds the integration error in  $(5.2)$  by the product of two quantities, one depending only on the integrand  $f$ , the other — the star discrepancy of  $x_1,\ldots,x_n$  depending only on the point set used.

## **Finite Variation**

The bound depends on the integrand  $f$  through its *Hardy-Krause variation*, which we now define, following Niederreiter [281]. For this we need  $f$  defined (and finite) on the closed unit hypercube  $[0,1]^d$ . Consider a rectangle of the  $\text{form}$ 

$$J = [u_1^-, u_1^+] \times [u_2^-, u_2^+] \times \cdots \times [u_d^-, u_d^+],$$

with  $0 \leq u_i^- \leq u_i^+ \leq 1$ ,  $i = 1, \ldots, d$ . Each vertex of  $J$  has coordinates of the form  $u_i^{\pm}$ . Let  $\mathcal{E}(J)$  be the set of vertices of  $J$  with an even number of  $+$ superscripts and let  $\mathcal{O}(J)$  contain those with an odd number of + superscripts. Define

$$\Delta(f;J) = \sum_{u \in \mathcal{E}(J)} f(u) - \sum_{u \in \mathcal{O}(J)} f(u);$$

this is the sum of  $f(u)$  over the vertices of J with function values at adjacent vertices given opposite signs.

The unit hypercube can be partitioned into a set  $\mathcal{P}$  of rectangles of the form of J. Letting  $\mathcal{P}$  range over all such partitions, define

$$V^{(d)}(f) = \sup_{\mathcal{P}} \sum_{J \in \mathcal{P}} |\Delta(f; J)|.$$

This is a measure of the variation of  $f$ . Niederreiter [281, p.19] notes that

$$V^{(d)}(f) = \int_0^1 \cdots \int_0^1 \left| \frac{\partial^d f}{\partial u_1 \cdots \partial u_d} \right| \, du_1 \cdots du_d,$$

if the partial derivative is continuous over  $[0,1]^d$ . This expression makes the interpretation of  $V^{(d)}$  more transparent, but it should be stressed that  $f$  need not be differentiable for  $V^{(d)}(f)$  to be finite.

For any  $1 \leq k \leq d$  and any  $1 \leq i_1 < i_2 < \cdots < i_k \leq d$ , consider the function on  $[0,1]^k$  defined by restricting f to points  $(u_1,\ldots,u_d)$  with  $u_j=1$ if  $j \notin \{i_1,\ldots,i_k\}$  and  $(u_{i_1},\ldots,u_{i_k})$  ranging over all of  $[0,1]^k$ . Denote by  $V^{(k)}(f; i_1, \ldots, i_k)$  the application of  $V^{(k)}$  to this function. Finally, define

$$V(f) = \sum_{k=1}^{d} \sum_{1 \le i_1 < \dots < i_k \le d} V^{(k)}(f; i_1, \dots, i_k). \tag{5.9}$$

This is the variation of  $f$  in the sense of Hardy and Krause.

We can now state the Koksma-Hlawka bound: if the function  $f$  has finite Hardy-Krause variation  $V(f)$ , then for any  $x_1, \ldots, x_n \in [0, 1)^d$ ,

$$\left|\frac{1}{n}\sum_{i=1}^{n}f(x_{i}) - \int_{[0,1]^{d}}f(u)\,du\right| \le V(f)D^{*}(x_{1},\ldots,x_{n}).\tag{5.10}$$

As promised, this result bounds the integration error through the product of two terms. The first term is a measure of the variation of the integrand; the second term is a measure of the deviation from uniformity of the points at which the integrand is evaluated.

Theorem 2.12 of Niederreiter [281] shows that  $(5.10)$  is a tight bound in the sense that for each  $x_1, \ldots, x_n$  and  $\epsilon > 0$  there is a function f for which the error on the left comes within  $\epsilon$  of the bound on the right. The function can be chosen to be infinitely differentiable, so in this sense  $(5.10)$  is tight even for very smooth functions.

 $\mathcal{L}$ 

It is natural to contrast the Koksma-Hlwaka inequality with the error information available in ordinary Monte Carlo. To this end, let  $U, U_1, U_2, \ldots$  be independent and uniformly distributed over the  $d$ -dimensional unit hypercube and let  $\sigma_f^2 = \text{Var}[f(U)]$ . From the central limit theorem, we know that

$$\left| \frac{1}{n} \sum_{i=1}^{n} f(U_i) - \int_{[0,1]^d} f(u) \, du \right| \le z_{\delta/2} \frac{\sigma_f}{\sqrt{n}},\tag{5.11}$$

with probability approximately equal to  $1 - \delta$ , with  $-z_{\delta/2}$  the  $\delta/2$  quantile of the standard normal distribution. From Chebyshev's inequality we know that for any  $\delta > 0$ ,

$$\left|\frac{1}{n}\sum_{i=1}^{n}f(U_i) - \int_{[0,1]^d}f(u)\,du\right| \le \frac{\sigma_f}{\sqrt{\delta n}},\tag{5.12}$$

with probability at least  $1-\delta$ . The following observations are relevant in comparing the quasi-Monte Carlo and ordinary Monte Carlo error information:

- $\circ$  The Koksma-Hlawka inequality (5.10) provides a strict bound on the integration error, whereas  $(5.11)$  and  $(5.12)$  are probabilistic bounds and  $(5.11)$ requires n to be large. In both  $(5.11)$  and  $(5.12)$  we may, however, choose  $\delta > 0$  to bring the probability  $1 - \delta$  arbitrarily close to 1.
- $\circ$  Both of the terms  $V(f)$  and  $D^*(x_1,\ldots,x_n)$  appearing in the Koksma-Hlawka inequality are difficult to compute — potentially much more so than the integral of f. In contrast, the unknown parameter  $\sigma_f$  in (5.11) and  $(5.12)$  is easily estimated from  $f(U_1), \ldots, f(U_n)$  with negligible additional computation.
- $\circ$  In cases where  $V(f)$  and  $D^*(x_1,\ldots,x_n)$  are known, the Koksma-Hlawka bound is often found to grossly overestimate the true error of integration. In contrast, the central limit theorem typically provides a sound and informative measure of the error in a Monte Carlo estimate.
- $\circ$  The condition that  $V(f)$  be finite is restrictive. It requires, for example, that  $f$  be bounded, a condition often violated in option pricing applications.

In light of these observations, it seems fair to say that despite its theoretical importance the Koksma-Hlawka inequality has limited applicability as a practical error bound. This is a shortcoming of quasi-Monte Carlo methods in comparison to ordinary Monte Carlo methods, for which effective error information is readily available. The most important consequence of the Koksma-Hlawka inequality is that it helps guide the search for effective point sets and sequences by making precise the role of discrepancy.

The Koksma-Hlawka inequality is the best-known example of a set of related results. Hickernell [181] generalizes the inequality by extending both the star discrepancy and the Hardy-Krause variation using more general norms.

One such bound uses an  $L_2$  discrepancy defined by replacing the maximum absolute deviation in  $(5.3)$  with a root-mean-square deviation. An analog of (5.10) then holds for this notion of discrepancy, with  $V(f)$  replaced by an  $L_2$ notion of variation. An advantage of the  $L_2$  discrepancy is that it is comparatively easy to calculate  $-$  through simulation, for example.

Integrands arising in derivative pricing applications sometimes vanish off a subset of  $[0,1)^d$  (once formulated as functions on the hypercube) and may be discontinuous at the boundary of this domain. This is typical of barrier options, for example. Such integrands usually have infinite variation, as explained in Figure 5.2. The Koksma-Hlawka inequality is therefore uninformative for a large class of interesting integrands. An important variant of  $(5.10)$ , one of several cited in Niederreiter [281], p.21, applies to integrals over arbitrary convex subsets of the hypercube. Thus, if our integrand would have finite variation but for the presence of the indicator function of a convex set, this result allows us to absorb the indicator into the integration domain and obtain a bound on the integration error. However, the bound in this case involves the isotropic discrepancy which, as we noted in Section  $5.1.1$ , exhibits a much stronger dependence on dimension.

This points to another limitation of the Koksma-Hlawka bound, at least from the perspective of our intended application. The Koksma-Hlawka result is oriented to the axes of the hypercube, through the definitions of both  $V(f)$ and the star discrepancy. The indicator of a rectangle, for example, has finite variation if the rectangle is parallel to the axes but infinite variation if the rectangle is rotated, as illustrated in Figure 5.2. This focus on a particular choice of coordinates seems unnatural if the function  $f$  is the result of transforming a simulation algorithm into a function on the unit hypercube; dropping this focus leads to much larger error bounds with a qualitatively different dependence on dimension (cf. Matoušek  $[257]$ ). In Section 5.5.2, we discuss applications of QMC methods that take account of more specific features of integrands  $f$  arising in derivative pricing applications.

### 5.1.4 Nets and Sequences

Despite its possible shortcomings as a practical bound on integration error, the Koksma-Hlawka inequality  $(5.10)$  nevertheless suggests that constructing point sets and sequences with low discrepancy is a fruitful approach for numerical integration. A valuable tool for constructing and describing such point sets is the notion of a  $(t, m, d)$ -net and a  $(t, d)$ -sequence introduced by Niederreiter [280], extending ideas developed in base 2 by Sobol' [335]. These are more commonly referred to as  $(t, m, s)$ -nets and  $(t, s)$ -sequences; the parameter s in this terminology refers to the dimension, for which we have consistently used d. Briefly, a  $(t, m, d)$ -net is a finite set of points in  $[0, 1)^d$  possessing a degree of uniformity quantified by t; a  $(t, d)$ -sequence is a sequence of points certain segments of which form  $(t, m, d)$ -nets.

![](_page_10_Figure_1.jpeg)

Fig. 5.2. Variation of the indicator function of the shaded square. In the left panel, each small box has a  $\Delta(f;J)$  value of zero except the one containing the corner of the shaded square; the variation remains finite. In the right panel, each small box has a  $|\Delta(f;J)|$  value of 1, except the one on the corner. Because the boxes can be made arbitrarily small, the indicator function on the right has infinite variation.

To formulate the defintions of these sets and sequences, we first need to define a *b*-ary box, also called an elementary interval in base b, with  $b \ge 2$  an integer. This is a subset of  $[0,1)^d$  of the form

$$\prod_{i=1}^d \left[ \frac{a_i}{b^{j_i}}, \frac{a_i+1}{b^{j_i}} \right),$$

with  $j_i \in \{0, 1, \ldots\}$  and  $a_i \in \{0, 1, \ldots, b^{j_i} - 1\}$ . The vertices of a b-ary box thus have coordinates that are multiples of powers of  $1/b$ , but with restrictions. In base 2, for example,  $[3/4, 1)$  and  $[3/4, 7/8)$  are admissible but  $[5/8, 7/8)$  is not. The volume of a *b*-ary box is  $1/b^{j_1+\cdots+j_d}$ .

For integers  $0 \le t \le m$ , a  $(t, m, d)$ -net in base b is a set of  $b^m$  points in  $[0,1)^d$  with the property that exactly  $b^t$  points fall in each b-ary box of volume  $b^{t-m}$ . Thus, the net correctly estimates the volume of each such b-ary box in the sense that the fraction of points  $b^t/b^m$  that lie in the box equals the volume of the box.

A sequence of points  $x_1, x_2, \ldots$  in  $[0,1)^d$  is a  $(t,d)$ -sequence in base b if for all  $m > t$  each segment  $\{x_i : jb^m < i \leq (j+1)b^m\}, j = 0, 1, ...,$  is a  $(t, m, d)$ -net in base b.

In these definitions, it should be evident that smaller values of  $t$  are associated with greater uniformity; with smaller  $t$ , even small b-ary boxes contain the right number of points. It should also be clear that, other things being equal, a smaller base  $b$  is preferable because the uniformity properties of  $(t, m, d)$ -nets and  $(t, d)$ -sequences are exhibited in sets of  $b^m$  points. With larger  $b$ , more points are required for these properties to hold.

Figure 5.3 displays two nets. The 81 ( $= 3^4$ ) points in the left panel comprise a  $(0, 4, 2)$ -net in base 3. Dotted lines in the figure show 3-ary boxes with dimensions  $1/9 \times 1/9$  and  $1/27 \times 1/3$  containing one point each, as they must. (For points on the boundaries, recall our convention that intervals are closed

on the left and open on the right.) The right panel shows a  $(1,7,2)$ -net in base 2 (with  $2^7 = 128$  points) that is not a  $(0, 7, 2)$ -net. The dotted lines in the figure show that 2-ary boxes with area  $1/64$  contain two points, but they also show boxes with dimensions  $1/16 \times 1/8$  that do not contain any points.

![](_page_11_Figure_2.jpeg)

**Fig. 5.3.** Left panel shows 81 points comprising a  $(0, 4, 2)$ -net in base 3. Right panel shows 128 points comprising a  $(1, 7, 2)$ -net in base 2. Both include a point at the origin.

Niederreiter [281] contains an extensive analysis of discrepancy bounds for  $(t, m, d)$ -nets and  $(t, d)$ -sequences. Of his many results we quote just one, demonstrating that  $(t, d)$ -sequences are indeed low-discrepancy sequences. More precisely, Theorem 4.17 of Niederreiter [281] states that if  $x_1, x_2, \ldots$ is a  $(t, d)$ -sequence in base b, then for  $n > 2$ ,

$$D^*(x_1, \dots, x_n) \le C(d, b)b^t \frac{(\log n)^d}{n} + O\left(\frac{b^t (\log n)^{d-1}}{n}\right).$$
(5.13)

The factor  $C(d, b)$  (for which Niederreiter provides an explicit expression) and the implicit constant in the  $O(\cdot)$  term do not depend on n or t. Theorem 4.10 of Niederreiter [281] provides a similar bound for  $(t, m, d)$ -nets, but with each exponent of  $\log n$  reduced by 1.

In the next section, we describe several specific constructions of lowdiscrepancy sequences. The simplest constructions, producing Halton sequences and Hammersley points, are the easiest to introduce, but they yield neither  $(t, d)$ -sequences nor  $(t, m, d)$ -nets. Faure sequences are  $(0, d)$ -sequences and thus optimize the uniformity parameter  $t$ ; however, they require a base at least as large as the smallest prime greater than or equal to the dimension  $d.$  Sobol' sequences use base 2 regardless of the dimension (which has computational as well as uniformity advantages) but their  $t$  parameter grows with the dimension  $d$ .

## 5.2 Low-Discrepancy Sequences

We turn now to specific constructions of low-discrepancy sequences in arbitrary dimension d. We provide algorithms for the methods we consider and make some observations on the properties and relative merits of various sequences. All methods discussed in this section build on the Van der Corput sequences discussed in Section  $5.1.2$ .

### 5.2.1 Halton and Hammersley

Halton [165], extending work of Hammersley [168], provides the simplest construction and first analysis of low-discrepancy sequences in arbitrary dimension  $d$ . The coordinates of a Halton sequence follow Van der Corput sequences in distinct bases. Thus, let  $b_1, \ldots, b_d$  be relatively prime integers greater than  $1$ , and set

$$x_k = (\psi_{b_1}(k), \psi_{b_2}(k), \dots, \psi_{b_d}(k)), \quad k = 0, 1, 2, \dots, \tag{5.14}$$

with  $\psi_b$  the radical inverse function defined in (5.8).

The requirement that the  $b_i$  be relatively prime is necessary for the sequence to fill the hypercube. For example, the two-dimensional sequence defined by  $b_1 = 2$  and  $b_2 = 6$  has no points in  $[0, 1/2) \times [5/6, 1]$ . Because we prefer smaller bases to larger bases, we therefore take  $b_1, \ldots, b_d$  to be the first  $d$  prime numbers. The two-dimensional cases, using bases 2 and 3, is illustrated in Figure 5.4. With the convention that intervals are closed on the left and open on the right, each cell in the figure contains exactly one point.

![](_page_12_Figure_8.jpeg)

Fig. 5.4. First twelve points of two-dimensional Halton sequence.

A word about zero: Some properties of low-discrepancy sequences are most conveniently stated by including a 0th point, typically zero itself, as in  $(5.14)$ .

When the points are fed into a simulation algorithm, there is often good reason to avoid zero — for example,  $\Phi^{-1}(0) = -\infty$ . In practice, we therefore omit it. Depending on whether or not  $x_0$  is included,  $x_k$  is either the kth or  $(k+1)$ th point in the sequence, but we always take  $x_k$  to be the point constructed from the integer k, as in (5.14). Omission of  $x_0$  has no bearing on asymptotic properties.

Halton points form an infinite sequence. We can achieve slightly better uniformity if we are willing to fix the number of points  $n$  in advance. The  $n$ points

$$\{(k/n, \psi_{b_1}(k), \dots, \psi_{b_{d-1}}(k)), k = 0, 1, \dots, n-1\}$$

with relatively prime  $b_1, \ldots, b_{d-1}$  form a *Hammersley point set* in dimension  $d.$ 

The star discrepancy of the first  $n$  Halton points in dimension  $d$  with relatively prime bases  $b_1, \ldots, b_d$  satisfies

$$D^*(x_0,\ldots,x_{n-1}) \leq C_d(b_1,\ldots,b_d) \frac{(\log n)^d}{n} + O\left(\frac{(\log n)^{d-1}}{n}\right),$$

with  $C_d(b_1,\ldots,b_d)$  independent of n; thus, Halton sequences are indeed lowdiscrepancy sequences. The corresponding  $n$ -element Hammersley point set  $satisfies$ 

$$D^*(x_0,\ldots,x_{n-1}) \leq C_{d-1}(b_1,\ldots,b_{d-1}) \frac{(\log n)^{d-1}}{n} + O\left(\frac{(\log n)^{d-2}}{n}\right).$$

The leading orders of magnitude in these bounds were established in Halton  $[165]$  and subsequently refined through work reviewed in Niederreiter [281, p.44].

A formula for  $C_d(b_1,\ldots,b_d)$  is given in Niederreiter [281]. This upper bound is minimized by taking the bases to be the first d primes. With  $C_d$ denoting this minimizing value, Niederreiter  $[281]$ , p.47, observes that

$$\lim_{d \to \infty} \frac{\log C_d}{d \log d} = 1,$$

so the bounding constant  $C_d$  grows superexponentially. This indicates that while the Halton and Hammersley points exhibit good uniformity for fixed  $d$ as  $n$  increases, their quality degrades rapidly as  $d$  increases.

The deterioration of the Halton sequence and Hammersley points in high dimensions follows from the behavior of the Van der Corput sequence with a large base. The Van der Corput sequence in base  $b$  consists of consecutive monotone segments of length  $b$ . If the base is large, the sequence produces long monotone segments, and projections of a Halton sequence onto coordinates using large bases will have long diagonal segments in the projected hypercube.

This pattern is illustrated in Figure 5.5, which shows two projections of the first 1000 nonzero points of the Halton sequence in dimension 30. The left

panel is the projection onto the first two coordinates, which use bases 2 and 3; the right panel is the projection onto the last two coordinates, which use bases 109 and 113, the 29th and 30th prime numbers. The impact of increasing the bases — and thus also of increasing the dimension — is evident from the figure.

![](_page_14_Figure_2.jpeg)

**Fig. 5.5.** First 1000 points of the Halton sequence in dimension 30. Left panel shows projection onto first two coordinates (bases 2 and 3); right panel shows projection onto last two coordinates (bases 109 and 113).

As a possible remedy for the problem illustrated in Figure 5.5, Kocis and Whiten  $[213]$  suggest using a *leaped* Halton sequence

$$x_k = (\psi_{b_1}(k\ell), \psi_{b_2}(k\ell), \dots, \psi_{b_d}(k\ell)), \quad k = 0, 1, 2, \dots,$$

for some integer  $\ell \geq 2$ . They recommend choosing  $\ell$  to be relatively prime to the bases  $b_1, \ldots, b_d$ .

This idea is illustrated in Figure 5.6, where we have applied it to a twodimensional Halton sequence with bases 109 and 113, the same bases used in the right panel of Figure 5.5. Each panel of Figure 5.6 shows  $1000$  points, using leaps  $\ell = 3$ ,  $\ell = 107$  (the prime that precedes 109), and  $\ell = 127$ (the prime that succeeds 113). The figures suggest that leaping can indeed improve uniformity, but also that its effect is very sensitive to the choice of leap parameter  $\ell$ .

The decline in uniformity of Halton sequences with increasing dimension is inherent to their construction. Several studies have concluded through numerical experiments that Halton sequences are not competitive with other methods in high dimensions; these studies include Fox [126], Kocis and Whiten [213], and, in financial applications, Boyle et al. [53] and Paskov [295]. An exception is Morokoff and Caflisch [272], where Halton sequences are found to be effective on a set of test problems; see also the comments of Matoušek [257,  $p.543$  supporting randomized Halton sequences.

![](_page_15_Figure_1.jpeg)

Fig. 5.6. First 1000 points of leaped Halton sequence with bases 109 and 113. From left to right, the leap parameters are  $\ell = 3$ ,  $\ell = 107$ , and  $\ell = 127$ .

### Implementation

Generating Halton points is essentially equivalent to generating a Van der Corput sequence, which in turn requires little more than finding base- $b$  expansions. We detail these steps because they will be useful later as well.

Figure 5.7 displays an algorithm to compute the base-b expansion of an integer  $k \geq 0$ . The function returns an array **a** whose elements are the coefficients of the expansion ordered from most significant to least. Thus, B- $\text{ARY}(6,2)$  is  $(1,1,0)$  and B-ARY $(135,10)$  is  $(1,3,5)$ .

![](_page_15_Figure_6.jpeg)

**Fig. 5.7.** Function B-ARY $(k, b)$  returns coefficients of base-b expansion of integer k in array  $\mathbf{a}$ . Rightmost element of  $\mathbf{a}$  is least significant digit in the expansion.

To generate elements  $x_{n_1}, x_{n_1+1}, \ldots, x_{n_2}$  of the Van der Corput sequence in base b, we need the expansions of  $k = n_1, n_1 + 1, \ldots, n_2$ . But computing all of these through calls to B-ARY is wasteful. Instead, we can use B-ARY to expand  $n_1$  and then update the expansion recursively. A function NEXTB-ARY that increments a base- $b$  expansions by 1 is displayed in Figure 5.8.

```
\text{NEXTB-ARY}(\mathbf{a}_{\text{in}}, b)m \leftarrow \text{length}(\mathbf{a}_{\text{in}}), \text{carry} \leftarrow \text{TRUE}for i = m, \ldots, 1if carry
                  if (\mathbf{a}_{\text{in}}(i) = b-1)\mathbf{a}_{\text{out}}(i) \leftarrow 0else
                           \mathbf{a}_{\text{out}}(i) \leftarrow \mathbf{a}_{\text{in}}(i) + 1carry \leftarrow FALSEelse
                  \mathbf{a}_{\text{out}}(i) \leftarrow \mathbf{a}_{\text{in}}(i)if carry \mathbf{a}_{\text{out}} \leftarrow (1, \mathbf{a}_{\text{out}}(1), \dots, \mathbf{a}_{\text{out}}(m))\text{return } \mathbf{a}_{\text{out}}
```

Fig. 5.8. Function NEXTB-ARY( $a_{\text{in}}, b$ ) returns coefficients of base-b expansion of integer  $k+1$  in array  $\mathbf{a}_{\text{out}}$ , given coefficients for integer k in array  $\mathbf{a}_{\text{in}}$ .

Elements  $x_{n_1}, \ldots, x_{n_2}$  of the base-*b* Van der Corput sequence can now be calculated by making an initial call to B-ARY $(n_1, b)$  to get the coefficients of the expansion of  $n_1$  and then repeatedly applying NEXTB-ARY to get subsequent coefficients. If the array  $\mathbf{a}$  for a point  $n$  has  $m$  elements, we compute  $x_n$  as follows:

$$x_n \leftarrow 0, \ q \leftarrow 1/b$$
  
for  $j = 1, \dots, m$   
 $x_n \leftarrow x_n + q * \mathbf{a}(m - j + 1)$   
 $q \leftarrow q/b$ 

This evaluates the radical-inverse function  $\psi_b$ . By applying the same procedure with prime bases  $b_1, \ldots, b_d$ , we construct Halton points in dimension d.

As noted by Halton [165], it is also easy to compute  $\psi_b(k+1)$  recursively from  $\psi_b(k)$  without explicitly calculating the base-b expansion of either k or  $k+1$ . Halton and Smith [166] provide a numerically stable implementation of this idea, also used in Fox [126]. We will, however, need the base-b expansions for other methods.

### 5.2.2 Faure

We noted in the previous section that the uniformity of Halton sequences degrades in higher dimensions because higher-dimensional coordinates are constructed from Van der Corput sequences with large bases. In particular, the  $d\text{th}$  coordinate uses a base at least as large as the  $d\text{th}$  prime, and this grows superexponentially with d. Faure [116] developed a different extension of Van der Corput sequences to multiple dimensions in which all coordinates use a common base. This base must be at least as large as the dimension itself, but

č.

can be much smaller than the largest base used for a Halton sequence of equal dimension.

In a  $d$ -dimensional Faure sequence, the coordinates are constructed by permuting segments of a single Van der Corput sequence. For the base  $b$  we choose the smallest prime number greater than or equal to d. As in  $(5.7)$ , let  $a_{\ell}(k)$  denote the coefficients in the base-b expansion of k, so that

$$k = \sum_{\ell=0}^{\infty} a_{\ell}(k) b^{\ell}.$$
 (5.15)

The *i*th coordinate,  $i = 1, \ldots, d$ , of the *k*th point in the Faure sequence is given by

$$\sum_{j=1}^{\infty} \frac{y_j^{(i)}(k)}{b^j},\tag{5.16}$$

where

$$y_j^{(i)}(k) = \sum_{\ell=0}^{\infty} \binom{\ell}{j-1} (i-1)^{\ell-j+1} a_{\ell}(k) \mod b, \tag{5.17}$$

with

$$\binom{m}{n} = \begin{cases} m!/(m-n)!n!, \, m \ge n, \\ 0, & \text{otherwise} \end{cases}$$

and  $0! = 1$ .

Each of the sums in  $(5.15)$ – $(5.17)$  has only a finite number of nonzero terms. Suppose the base-b expansion of k in (5.15) has exactly r terms, meaning that  $a_{r-1}(k) \neq 0$  and  $a_{\ell}(k) = 0$  for all  $\ell \geq r$ . Then the summands in (5.17) vanish for  $\ell \geq r$ . If  $j \geq r+1$ , then the summands for  $\ell = 0, \ldots, r-1$ also vanish, so  $y_j^{(i)}(k) = 0$  if  $j \ge r + 1$ , which implies that (5.16) has at most  $r$  nonzero terms. The construction may thus be viewed as the result of the matrix-vector calculation

$$\begin{pmatrix} y_1^{(i)}(k) \\ y_2^{(i)}(k) \\ \vdots \\ y_r^{(i)}(k) \end{pmatrix} = \mathbf{C}^{(i-1)} \begin{pmatrix} a_0(k) \\ a_1(k) \\ \vdots \\ a_{r-1}(k) \end{pmatrix} \bmod b, \tag{5.18}$$

where  $\mathbf{C}^{(i)}$  is the  $r \times r$  matrix with entries

$$\mathbf{C}^{(i)}(m,n) = \binom{n-1}{m-1} i^{n-m} \tag{5.19}$$

for  $n \geq m$  and zero otherwise. With the convention that  $0^0 = 1$  and  $0^j = 0$  for  $j > 0$ , this makes  $\mathbf{C}^{(0)}$  the identity matrix. (Note that in (5.18) the coefficients  $a_i(k)$  are ordered from least significant to most significant.

These *generator* matrices have the following cyclic properties:

$$\mathbf{C}^{(i)} = \mathbf{C}^{(1)} \mathbf{C}^{(i-1)}, \quad i = 1, 2, \dots,$$

and for  $i \geq 2$ ,  $\mathbf{C}^{(i)}$  mod *i* is the identity matrix.

. ....

To see the effect of the transformations  $(5.16)$ – $(5.17)$ , consider the integers from 0 to  $b^r-1$ . These are the integers whose base-b expansions have r or fewer terms. As k varies over this range, the vector  $\mathbf{a}(k)$  =  $(a_0(k), a_1(k), \ldots, a_{r-1}(k))^\top$  varies over all  $b^r$  vectors with elements in the set  $\{0, 1, \ldots, b-1\}$ . The matrices  $\mathbf{C}^{(i)}$  have the property that the product  $\mathbf{C}^{(i)}\mathbf{a}(k)$  (taken mod b) ranges over exactly the same set. In other words,

$$\mathbf{C}^{(i)} \mathbf{a}(k) \bmod b, \quad 0 \le k < b^r$$

is a permutation of  $\mathbf{a}(k)$ ,  $0 \le k \le b^r$ . In fact, the same is true if we restrict k to any range of the form  $jb^r \leq k < (j+1)b^r$ , with  $0 \leq j \leq b-1$ . It follows that the *i*th coordinate  $x_k^{(i)}$  of the points  $x_k$ , for any such set of k, form a permutation of the segment  $\psi_b(k)$ ,  $jb^r \leq k < (j+1)b^{r+1}$ , of the Van der Corput sequence.

As a simple illustration, consider the case  $r = 2$  and  $b = 3$ . The generator  $\text{matrices are}$ 

$$\mathbf{C}^{(1)} = \begin{pmatrix} 1 \ 1 \\ 0 \ 1 \end{pmatrix}, \quad \mathbf{C}^{(2)} = \mathbf{C}^{(1)}\mathbf{C}^{(1)} = \begin{pmatrix} 1 \ 2 \\ 0 \ 1 \end{pmatrix}.$$

For  $k = 0, 1, \ldots, 8$ , the vectors  $\mathbf{a}(k)$  are

$$\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \end{pmatrix}.$$

The vectors  $\mathbf{C}^{(1)}\mathbf{a}(k) \pmod{b}$  are

$$\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \end{pmatrix}.$$

And the vectors  $\mathbf{C}^{(2)}\mathbf{a}(k) \pmod{b}$  are

$$\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \end{pmatrix}.$$

Now we apply  $(5.16)$  to convert each of these sets of vectors into fractions, by premultiplying each vector by  $(1/3, 1/9)$ . Arranging these fractions into three  $rows, we get$ 

$$\begin{array}{cccccccc} 0 & 1/3 & 2/3 & 1/9 & 4/9 & 7/9 & 2/9 & 5/9 & 8/9 \\ 0 & 1/3 & 2/3 & 4/9 & 7/9 & 1/9 & 8/9 & 2/9 & 5/9 \\ 0 & 1/3 & 2/3 & 7/9 & 1/9 & 4/9 & 5/9 & 8/9 & 2/9 \end{array}$$

The first row gives the first nine elements of the base-3 Van der Corput sequence and the next two rows permute these elements. Finally, by taking each

column in this array as a point in the three-dimensional unit hypercube, we get the first nine points of the three-dimensional Faure sequence.

والمراجل والمراج

Faure [116] showed that the discrepancy of the d-dimensional sequence constructed through  $(5.16)$ – $(5.17)$  satisfies

$$D^*(x_1,\ldots,x_n) = F_d \frac{(\log n)^d}{n} + O\left(\frac{(\log n)^{d-1}}{n}\right)$$

with  $F_d$  depending on d but not n; thus, Faure sequences are indeed lowdiscrepancy sequences. In fact,  $F_d \to 0$  quickly as  $d \to \infty$ , in marked contrast to the increase in the constant for Halton sequences.

In the terminology of Section 5.1.4, Faure sequences are  $(0, d)$ -sequences and thus achieve the best possible value of the uniformity parameter  $t$ . The example in the left panel of Figure 5.3 is the projection onto dimensions two and three of the first 81 points of the three-dimensional Faure sequence with  $\text{base } 3.$ 

As a consequence of the definition of a  $(t, d)$ -sequence, any set of Faure points of the form  $\{x_k : jb^m \le k < (j+1)b^m\}$  with  $0 \le j \le b-1$  and  $m \ge 1$  is a  $(0, m, d)$ -net, which we call a *Faure net*. (Recall that  $x_0 = 0$ .) The discussion following  $(5.19)$  may then be summarized as stating that, over a Faure net, all one-dimensional projections are the same, as each is a permutation of a segment of the Van der Corput sequence.

The cyclic properties of the generator matrices  $\mathbf{C}^{(i)}$  have implications for higher dimensional projections as well. The projection of the points in a Faure net onto the *i*th and *j*th coordinates depends only on the distance  $j-i$ , modulo the base b. Thus, if the dimension equals the base, the  $b(b-1)$  two-dimensional projections comprise at most  $b-1$  distinct sets in  $[0,1)^2$ . If we identify sets in  $[0,1)^2$  that result from interchanging coordinates, then there are at most  $(b-1)/2$  distinct projections. Similar conclusions hold for projections onto more than two coordinates.

This phenomenon is illustrated in Figure 5.9, which is based on a Faure net in base 31, the 961 points constructed from  $k = 5(31)^2, \ldots, 6(31)^2 - 1$ . The projection onto coordinates  $1$  and  $2$  is identical to the projection onto coordinates 19 and 20. The projection onto coordinates 1 and 31 would look the same as the other two if plotted with the axes interchanged because modulo  $31, 1$  is the successor of  $31.$ 

### Implementation

The construction of Faure points builds on the construction of Van der Corput sequences in Section 5.2.1. To generate the d coordinates of the Faure point  $x_k$ in base b, we record the base-b expansion of  $k$  in a vector, multiply the vector  $(\text{mod } b)$  by a generator matrix, and then convert the resulting vector to a point in the unit interval. We give a high-level description of an implementation, omitting many programming details. Fox  $[126]$  provides FORTRAN code to generate Faure points.

![](_page_20_Figure_1.jpeg)

Fig. 5.9. Projections of 961 Faure points in 31 dimensions using base 31. From left to right, the figures show coordinates 1 and 2, 19 and 20, and 1 and 31. The first two are identical; the third would look the same as the others if the axes were interchanged.

A key step is the construction of the generator matrices  $(5.19)$ . Because these matrices have the property that  $\mathbf{C}^{(i)}$  is the *i*th power of  $\mathbf{C}^{(1)}$ , it is possible to construct just  $\mathbf{C}^{(1)}$  and then recursively evaluate products of the form  $\mathbf{C}^{(i)}\mathbf{a}$  as  $\mathbf{C}^{(1)}\mathbf{C}^{(i-1)}\mathbf{a}$ . However, to allow extensions to more general matrices, we do not take advantage of this in our implementation.

As noted by Fox [126] (for the case  $i = 1$ ), in calculating the matrix entries in  $(5.19)$ , evaluation of binomial coefficients can be avoided through the recursion

$$\binom{n+1}{k+1} = \binom{n}{k+1} + \binom{n}{k},$$

 $n \geq k \geq 0$ . Figure 5.10 displays a function FAUREMAT that uses this recursion to construct  $\mathbf{C}^{(i)}$ .

```
FAUREMAT(r, i)\mathbf{C}(1,1) \leftarrow 1for m = 2, \ldots, r\mathbf{C}(m,m) \leftarrow 1\mathbf{C}(1,m) \leftarrow i \ast \mathbf{C}(1,m-1)for n = 3, \ldots, rfor m = 2, ..., n - 1C(m, n) = C(m - 1, n - 1) + i * C(m, n - 1)\text{return } C
```

**Fig. 5.10.** Function FAUREMAT $(r, i)$  returns  $r \times r$  generator matrix  $\mathbf{C}^{(i)}$ .

The function  $FAUREPTS$  in Figure 5.11 uses  $FAUREMAT$  to generate Faure points. The function takes as inputs the starting index  $n_0$ , the total number of points to generate  $n_{\text{pts}}$ , the dimension d, and the base b. The

an experience from these

column in this array as a point in the three-dimensional unit hypercube, we get the first nine points of the three-dimensional Faure sequence.

Faure [116] showed that the discrepancy of the  $d$ -dimensional sequence constructed through  $(5.16)$ – $(5.17)$  satisfies

$$D^*(x_1,\ldots,x_n) = F_d \frac{(\log n)^d}{n} + O\left(\frac{(\log n)^{d-1}}{n}\right)$$

with  $F_d$  depending on d but not n; thus, Faure sequences are indeed lowdiscrepancy sequences. In fact,  $F_d \to 0$  quickly as  $d \to \infty$ , in marked contrast to the increase in the constant for Halton sequences.

In the terminology of Section 5.1.4, Faure sequences are  $(0, d)$ -sequences and thus achieve the best possible value of the uniformity parameter  $t$ . The example in the left panel of Figure 5.3 is the projection onto dimensions two and three of the first 81 points of the three-dimensional Faure sequence with base  $3.$ 

As a consequence of the definition of a  $(t, d)$ -sequence, any set of Faure points of the form  $\{x_k : jb^m \le k < (j+1)b^m\}$  with  $0 \le j \le b-1$  and  $m \ge 1$  is a  $(0, m, d)$ -net, which we call a *Faure net*. (Recall that  $x_0 = 0$ .) The discussion following  $(5.19)$  may then be summarized as stating that, over a Faure net, all one-dimensional projections are the same, as each is a permutation of a segment of the Van der Corput sequence.

The cyclic properties of the generator matrices  $\mathbf{C}^{(i)}$  have implications for higher dimensional projections as well. The projection of the points in a Faure net onto the *i*th and *j*th coordinates depends only on the distance  $j-i$ , modulo the base b. Thus, if the dimension equals the base, the  $b(b-1)$  two-dimensional projections comprise at most  $b-1$  distinct sets in  $[0,1)^2$ . If we identify sets in  $[0,1)^2$  that result from interchanging coordinates, then there are at most  $(b-1)/2$  distinct projections. Similar conclusions hold for projections onto more than two coordinates.

This phenomenon is illustrated in Figure 5.9, which is based on a Faure net in base 31, the 961 points constructed from  $k = 5(31)^2, \ldots, 6(31)^2 - 1$ . The projection onto coordinates  $1$  and  $2$  is identical to the projection onto coordinates 19 and 20. The projection onto coordinates 1 and 31 would look the same as the other two if plotted with the axes interchanged because modulo  $31, 1$  is the successor of  $31$ .

### Implementation

The construction of Faure points builds on the construction of Van der Corput sequences in Section 5.2.1. To generate the d coordinates of the Faure point  $x_k$ in base b, we record the base-b expansion of  $k$  in a vector, multiply the vector  $(\text{mod } b)$  by a generator matrix, and then convert the resulting vector to a point in the unit interval. We give a high-level description of an implementation,  $\text{omitting many programming details.}$  Fox [126] provides FORTRAN code to generate Faure points.

![](_page_22_Figure_1.jpeg)

Fig. 5.9. Projections of 961 Faure points in 31 dimensions using base 31. From left to right, the figures show coordinates 1 and 2, 19 and 20, and 1 and 31. The first two are identical; the third would look the same as the others if the axes were interchanged.

A key step is the construction of the generator matrices  $(5.19)$ . Because these matrices have the property that  $\mathbf{C}^{(i)}$  is the *i*th power of  $\mathbf{C}^{(1)}$ , it is possible to construct just  $\mathbf{C}^{(1)}$  and then recursively evaluate products of the form  $\mathbf{C}^{(i)}\mathbf{a}$  as  $\mathbf{C}^{(1)}\mathbf{C}^{(i-1)}\mathbf{a}$ . However, to allow extensions to more general matrices, we do not take advantage of this in our implementation.

As noted by Fox [126] (for the case  $i = 1$ ), in calculating the matrix entries in  $(5.19)$ , evaluation of binomial coefficients can be avoided through the recursion

$$\binom{n+1}{k+1} = \binom{n}{k+1} + \binom{n}{k},$$

 $n \geq k \geq 0$ . Figure 5.10 displays a function FAUREMAT that uses this recursion to construct  $\mathbf{C}^{(i)}$ .

```
FAUREMAT(r, i)\mathbf{C}(1,1) \leftarrow 1for m = 2, \ldots, r\mathbf{C}(m,m) \leftarrow 1\mathbf{C}(1,m) \leftarrow i \ast \mathbf{C}(1,m-1)for n = 3, \ldots, rfor m = 2, ..., n - 1\mathbf{C}(m,n) = \mathbf{C}(m-1,n-1) + i * \mathbf{C}(m,n-1)\text{return } C
```

**Fig. 5.10.** Function FAUREMAT $(r, i)$  returns  $r \times r$  generator matrix  $\mathbf{C}^{(i)}$ .

The function FAUREPTS in Figure 5.11 uses FAUREMAT to generate Faure points. The function takes as inputs the starting index  $n_0$ , the total number of points to generate  $n_{\text{pts}}$ , the dimension d, and the base b. The

starting index  $n_0$  must be greater than or equal to 1 and the base b must be a prime number at least as large as  $d$ . One could easily modify the function to include an array of prime numbers to save the user from having to specify the base. Calling FAUREPTS with  $n_0 = 1$  starts the sequence at the first nonzero point. Fox [126] recommends starting at  $n_0 = b^4 - 1$  to improve uniformity.

The advantage of generating  $n_{\text{pts}}$  points in a single call to the function lies in constructing the generator matrices just once. In FAUREPTS,  $r_{\text{max}}$  is the number of places in the base-b representation of  $n_0 + n_{\text{pts}} - 1$ , so the largest generator matrices needed are  $r_{\text{max}} \times r_{\text{max}}$ . We construct these and then use the submatrices needed to convert smaller integers. The variable  $r$  keeps track of the length of the expansion **a** of the current integer  $k$ , so we use the first r rows and columns of the full generator matrices to produce the required  $r \times r$ generator matrices. The variable r increases by one each time k reaches  $q_{\text{next}}$ , the next power of  $b$ .

```
\text{FAUREPTS}(n_0, n_{\text{pts}}, d, b)n_{\text{max}} \leftarrow n_0 + n_{\text{pts}} - 1, \quad r_{\text{max}} \leftarrow 1 + \lfloor \log(n_{\text{max}}) / \log(b) \rfloorP \leftarrow 0 \ [n_{\max} \times d], \quad \mathbf{y}(1, \dots, r_{\max}) \leftarrow 0r \leftarrow 1 + \left| \log(\max(1, n_0 - 1)) / \log(b) \right|,q_{\text{next}} \leftarrow b^r\mathbf{a} \leftarrow \text{B-ARY}(n_0 - 1, b, 1)for i = 1, ..., d - 1\mathbf{C}^{(i)} \leftarrow \text{FAUREMAT}(r_{\text{max}}, i)b_{\text{pwrs}} \leftarrow (1/b, 1/b^2, \dots, 1/b^{r_{\text{max}}})for k = n_0, \ldots, n_{\text{max}}\mathbf{a} \leftarrow \text{NEXTB-ARY}(\mathbf{a}, b)if (k = q_{\text{next}})r \leftarrow r + 1q_{\text{next}} \leftarrow b * q_{\text{next}}for j = 1, \ldots, rP(k - n_0 + 1, 1) \leftarrow P(k - n_0 + 1, 1) + b_{\text{pwrs}}(j) \ast \mathbf{a}(r - j + 1)for i = 2, \ldots, dfor m = 1, \ldots, rfor n = 1, \ldots, r\mathbf{y}(m) \leftarrow \mathbf{y}(m) + \mathbf{C}^{(i)}(m,n) \ast \mathbf{a}(r-n+1)\mathbf{y}(m) \leftarrow \mathbf{y}(m) \bmod bP(k - n_0 + 1, i) \leftarrow P(k - n_0 + 1, i) + b_{\text{pwrs}}(m) \ast \mathbf{y}(m)\mathbf{y}(m) \leftarrow 0return P
```

**Fig. 5.11.** Function FAUREPTS $(n_0, n_{\text{pts}}, d, b)$  returns  $n_{\text{pts}} \times d$  array whose rows are coordinates of d-dimensional Faure points in base b, starting from the  $n_0$ th nonzero point.

The loop over  $m$  and  $n$  near the bottom of FAUREPTS executes the matrix-vector product in  $(5.18)$ . The algorithm traverses the elements of the vector **a** from the highest index to the lowest because the variable **a** in the algorithm is flipped relative to the vector of coefficients in  $(5.18)$ . This results from a conflict in two notational conventions: the functions B-ARY and NEXTB-ARY follow the usual convention of ordering digits from most significant to least, whereas in  $(5.18)$  and the surrounding discussion we prefer to start with the least significant digit.

In FAUREPTS, we apply the mod- $b$  operation only after multiplying each vector of base- $b$  coefficients by a generator matrix. We could also take the remainder mod b after each multiplication of an element of  $\mathbf{C}^{(i)}$  by an element of **a**, or in setting up the matrices  $\mathbf{C}^{(i)}$ ; indeed, we could easily modify FAU-REMAT to return  $\mathbf{C}^{(i)}$  mod b by including b as an argument of that function. Taking remainders at intermediate steps can eliminate problems from overflow, but requires additional calculation.

An alternative construction of Faure points makes it possible to replace the matrix-vector product in  $(5.18)$  (the loop over m and n in FAUREPTS) with a single vector addition. This alternative construction produces permutations of Faure points, rather than the Faure points themselves. It relies on the notion of a Gray code in base  $b$ ; we return to it in the next section after a more general discussion of Gray codes.

### 5.2.3 Sobol'

 $\mathcal{L}_{\text{eff}}$ 

Sobol' [335] gave the first construction of what is now known as a  $(t, d)$ sequence (he used the name  $LP_{\tau}$ -sequence). The methods of Halton and Hammersley have low discrepancy, but they are not  $(t, d)$ -sequences or  $(t, m, d)$ nets. Sobol's construction can be succinctly contrasted with Faure's as follows: Whereas Faure points are  $(0, d)$ -sequences in a base at least as large as d, Sobol's points are  $(t, d)$ -sequences in base 2 for all d, with values of t that depend on  $d$ . Faure points therefore achieve the best value of the uniformity parameter t, but Sobol' points have the advantage of a much smaller base. Working in base 2 also lends itself to computational advantages through bit-level operations.

Like the methods of Halton, Hammersley, and Faure, Sobol' points start from the Van der Corput sequence, but now exclusively in base 2. The various coordinates of a  $d$ -dimensional Sobol' sequence result from permutations of segments of the Van der Corput sequence. As in Section 5.2.2, these permutations result from multiplying (binary) expansions of consecutive integers by a set of generator matrices, one for each dimension. The key difference lies in the construction of these generator matrices.

All coordinates of a Sobol' sequence follow the same construction, but each with its own generator. We may therefore begin by discussing the construction of a single coordinate based on a generator matrix  $\mathbf{V}$ . The elements of  $\mathbf{V}$  are equal to  $0$  or  $1$ . Its columns are the binary expansions of a set of *direction* 

numbers  $v_1, \ldots, v_r$ . Here, r could be arbitrarily large; in constructing the kth point in the sequence, think of  $r$  as the number of terms in the binary expansion of k. The matrix  $\mathbf{V}$  will be upper triangular, so regardless of the number of rows in the full matrix, it suffices to consider the square matrix consisting of the first  $r$  rows and columns.

Let  $\mathbf{a}(k) = (a_0(k), \ldots, a_{r-1}(k))^{\top}$  denote the vector of coefficients of the binary representation of  $k$ , so that

$$k = a_0(k) + 2a_1(k) + \cdots + 2^{r-1}a_{r-1}(k).$$

 $\text{Let}$ 

$$\begin{pmatrix} y_1(k) \\ y_2(k) \\ \vdots \\ y_r(k) \end{pmatrix} = \mathbf{V} \begin{pmatrix} a_0(k) \\ a_1(k) \\ \vdots \\ a_{r-1}(k) \end{pmatrix} \bmod 2; \n$$
(5.20)

then  $y_1(k), \ldots, y_r(k)$  are coefficients of the binary expansion of the kth point in the sequence; more explicitly,

$$x_k = \frac{y_1(k)}{2} + \frac{y_2(k)}{4} + \dots + \frac{y_r(k)}{2^r}.$$

If  $\mathbf{V}$  is the identity matrix, this produces the Van der Corput sequence in base 2.

The operation in  $(5.20)$  can be represented as

$$a_0(k)v_1 \oplus a_1(k)v_2 \oplus \cdots \oplus a_{r-1}(k)v_r, \tag{5.21}$$

where the  $v_j$  are the columns of (the  $r \times r$  submatrix of) V and  $\oplus$  denotes binary addition,

$$0 \oplus 0 = 0$$
,  $0 \oplus 1 = 1 \oplus 0 = 1$ ,  $1 \oplus 1 = 0$ .

This formulation is useful in computer implementation. If we reinterpret  $v_i$ as the computer representation of a number (i.e., as a computer word of bits rather than as an array) and implement  $\oplus$  through a bitwise XOR operation, then (5.21) produces the computer representation of  $x_k$ .

We turn now to the heart of Sobol's method, which is the specification of the generator matrices — equivalently, of the direction numbers  $v_j$ . We use the same symbol  $v_i$  to denote the number itself (a binary fraction) as we use to denote the vector encoding its binary representation. For a  $d$ -dimensional Sobol' sequence we need  $d$  sets of direction numbers, one for each coordinate; for simplicity, we continue to focus on a single coordinate.

Sobol's method for choosing a set of direction numbers starts by selecting a *primitive polynomial* over binary arithmetic. This is a polynomial

$$x^{q} + c_{1}x^{q-1} + \dots + c_{q-1}x + 1, \tag{5.22}$$

with coefficients  $c_i$  in  $\{0,1\}$ , satisfying the following two properties (with respect to binary arithmetic):

o it is irreducible (i.e., it cannot be factored):

a i

 $\circ$  the smallest power p for which the polynomial divides  $x^p + 1$  is  $p = 2^q - 1$ .

Irreducibility implies that the constant term 1 must indeed be present as implied by  $(5.22)$ . The largest power q with a nonzero coefficient is the degree of the polynomial. The polynomials

 $x + 1$ ,  $x^{2} + x + 1$ ,  $x^{3} + x + 1$ ,  $x^{3} + x^{2} + 1$ 

are all the primitive polynomials of degree one, two, or three.

Table 5.2 lists 53 primitive polynomials, including all those of degree  $8 \text{ or }$ less. (A list of  $360$  primitive polynomials is included in the implementation of Lemieux, Cieslak, and Luttmer [231].) Each polynomial in the table is encoded as the integer defined by interpreting the coefficients of the polynomial as bits. For example, the integer 37 in binary is 100101, which encodes the polynomial  $x^5 + x^2 + 1$ . Table 5.2 includes a polynomial of degree 0; this is a convenient convention that makes the construction of the first coordinate of a multidimensional Sobol' sequence consistent with the construction of the other coordinates.

Degree Primitive Polynomials

| U |                                                 |
|---|-------------------------------------------------|
|   | $3(x+1)$                                        |
| 2 | $7\ (x^2+x+1)$                                  |
| 3 | $11 (x^3 + x + 1), 13 (x^3 + x^2 + 1)$          |
| 4 | 19, 25                                          |
| 5 | [37, 59, 47, 61, 55, 41]                        |
| 6 | 67, 97, 91, 109, 103, 115                       |
|   | $ 131, 193, 137, 145, 143, 241, 157, 185, 167 $ |
|   | $229, 171, 213, 191, 253, 203, 211, 239, 247$   |
| 8 | $(285, 369, 299, 425, 301, 361, 333, 357, 351)$ |
|   | 501, 355, 397, 391, 451, 463, 487               |
|   |                                                 |

**Table 5.2.** Primitive polynomials of degree 8 or less. Each number in the right column, when represented in binary, gives the coefficients of a primitive polynomial.

The polynomial  $(5.22)$  defines a recurrence relation

$$m_j = 2c_1m_{j-1} \oplus 2^2c_2m_{j-2} \oplus \cdots \oplus 2^{q-1}c_{q-1}m_{j-q+1} \oplus 2^qm_{j-q} \oplus m_{j-q}. \tag{5.23}$$

The  $m_i$  are integers and  $\oplus$  may again be interpreted either as binary addition of binary vectors (by identifying  $m_j$  with its vector of binary coefficients) or as bit-wise XOR applied directly to the computer representations of the operands. By convention, the recurrence relation defined by the degree-0 polynomial is  $m_i \equiv 1$ . From the  $m_i$ , the direction numbers are defined by setting

$$v_j = m_j/2^j.$$

For this to fully define the direction numbers we need to specify initial values  $m_1, \ldots, m_q$  for (5.23). A minimal requirement is that each initializing  $m_i$  be an odd integer less than  $2^j$ ; all subsequent  $m_j$  defined by (5.23) will then share this property and each  $v_j$  will lie strictly between 0 and 1. More can be said about the proper initialization of  $(5.23)$ ; we return to this point after considering an example.

Consider the primitive polynomial

 $x^3 + x^2 + 1$ 

with degree  $q = 3$ . The recurrence (5.23) becomes

$$m_j = 2m_{j-1} \oplus 8m_{j-3} \oplus m_{j-3}$$

and suppose we initialize it with  $m_1 = 1, m_2 = 3, m_3 = 3$ . The next two elements in the sequence are as follows:

$$\begin{array}{l} m_4 = (2 \cdot 3) \oplus (8 \cdot 1) \oplus 1 \\ = 0110 \oplus 1000 \oplus 0001 \\ = 1111 \\ = 15 \\ m_5 = (2 \cdot 15) \oplus (8 \cdot 3) \oplus 3 \\ = 11110 \oplus 11000 \oplus 00011 \\ = 00101 \\ = 5 \end{array}$$

From these five values of  $m_j$ , we can calculate the corresponding values of  $v_i$  by dividing by  $2^j$ . But dividing by  $2^j$  is equivalent to shifting the "binary point" to the left j places in the representation of  $m_j$ . Hence, the first five direction numbers are

$$v_1 = 0.1, v_2 = 0.11, v_3 = 0.011, v_4 = 0.1111, v_5 = 0.00101,$$

and the corresponding generator matrix is

$$\mathbf{V} = \begin{pmatrix} 1 \ 1 \ 0 \ 1 \ 0 \\ 0 \ 1 \ 1 \ 1 \ 0 \\ 0 \ 0 \ 1 \ 1 \ 1 \\ 0 \ 0 \ 0 \ 1 \ 0 \\ 0 \ 0 \ 0 \ 0 \ 1 \end{pmatrix} . \tag{5.24}$$

Observe that taking  $m_j = 1, j = 1, 2, \ldots$ , (i.e., using the degree-0 polynomial) produces the identity matrix.

Finally, we illustrate the calculation of the sequence  $x_1, x_2, \ldots$  For each k, we take the vector  $\mathbf{a}(k)$  of binary coefficients of k and premultiply it (mod 2) by the matrix  $\mathbf{V}$ . The resulting vector gives the coefficients of a binary fraction. The first three vectors are

 $5.2$  Low-Discrepancy Sequences 307

$$\mathbf{V} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{V} \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{V} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix},$$

which produce the points  $1/2$ ,  $3/4$ , and  $1/4$ . For  $k = 29, 30, 31$  (the last three points that can be generated with a  $5 \times 5$  matrix), we have

$$\mathbf{V} \begin{pmatrix} 1 \\ 0 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{V} \begin{pmatrix} 0 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{V} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix},$$

which produce  $7/32$ ,  $15/32$ , and  $31/32$ .

Much as in the case of Faure points, this procedure produces a permutation of the segment  $\psi_2(k)$ ,  $2^{r-1} \leq k < 2^r$ , of the Van der Corput sequence when **V** is  $r \times r$ . This crucial property relies on the fact that **V** was constructed from a primitive polynomial.

### Gray Code Construction

Antanov and Saleev [18] point out that Sobol's method simplifies if the usual binary representation  $\mathbf{a}(k)$  is replaced with a Gray code representation. In a Gray code, k and  $k+1$  have all but one coefficient in common, and this makes it possible to construct the values  $x_k$  recursively.

One way to define a Gray code is to take the bitwise binary sum of the usual binary representation of  $k, a_{r-1}(k) \cdots a_1(k) a_0(k)$ , with the shifted string  $0a_{r-1}(k)\cdots a_1(k)$ ; in other words, take the  $\oplus$ -sum of the binary representations of k and  $\lfloor k/2 \rfloor$ . This encodes the numbers 1 to 7 as follows:

|                                                                                   | 1 2 3 4 5 6 7 |  |  |  |
|-----------------------------------------------------------------------------------|---------------|--|--|--|
| Binary 001 010 011 100 101 110 111                                                |               |  |  |  |
| Gray code $\quad 001 \quad 011 \quad 010 \quad 110 \quad 111 \quad 101 \quad 100$ |               |  |  |  |

For example, the Gray code for 3 is calculated as  $011 \oplus 001$ .

Exactly one bit in the Gray code changes when k is incremented to  $k+1$ . The position of that bit is the position of the rightmost zero in the ordinary binary representation of  $k$ , taking this to mean an initial zero if the binary representation has only ones. For example, since the last bit of the binary representation of  $4$  is zero, the Gray codes for  $4$  and  $5$  differ in the last bit. Because the binary representation of  $7$  is displayed as  $111$ , the Gray code for 8 differs from the Gray code for 7 through the insertion of an initial bit, which would produce  $1100$ .

÷.

The binary strings formed by the Gray code representations of the integers  $0, 1, \ldots, 2^r - 1$  are a permutation of the sequence of strings formed by the usual binary representations of the same integers, for any  $r$ . If in the definition of the radical inverse function  $\psi_2$  in (5.8) we replaced the usual binary coefficients with Gray code coefficients, the first  $2^r-1$  values would be a permutation of the corresponding elements of the Van der Corput sequence. Hence, the two sequences have the same asymptotic discrepancy. Antanov and Saleev [18] show similarly that using a Gray code with Sobol's construction does not affect the asymptotic discrepancy of the resulting sequence.

Suppose, then, that in (5.21) we replace the binary coefficients  $a_j(k)$  with Gray code coefficients  $g_i(k)$  and redefine  $x_k$  to be

$$x_k = g_0(k)v_1 \oplus g_1(k)v_2 \oplus \cdots \oplus g_{r-1}(k)v_r.$$

Suppose that the Gray codes of k and  $k+1$  differ in the  $\ell$ th bit; then

$$x_{k+1} = g_0(k+1)v_1 \oplus g_1(k+1)v_2 \oplus \cdots \oplus g_{r-1}(k+1)v_r$$
  
$$= g_0(k)v_1 \oplus g_1(k)v_2 \oplus \cdots \oplus (g_\ell(k)\oplus 1)v_\ell \oplus \cdots \oplus g_{r-1}(k)v_r$$
  
$$= x_k \oplus v_\ell.$$
  
(5.25)

Rather than compute  $x_{k+1}$  from (5.21), we may thus compute it recursively from  $x_k$  through binary addition of a single direction number. The computer implementations of Bratley and Fox  $[57]$  and Press et al.  $[299]$  use this formulation.

It is worth noting that if we start the Sobol' sequence at  $k = 0$ , we never need to calculate a Gray code. To use (5.25), we need to know only  $\ell$ , the index of the bit that would change if we calculated the Gray code. But, as explained above,  $\ell$  is completely determined by the ordinary binary expansion of k. To start the Sobol' sequence at an arbitrary point  $x_n$ , we need to calculate the Gray code of  $n$  to initialize the recursion in  $(5.25)$ .

The simplification in  $(5.25)$  extends to the construction of Faure points in any arbitrary (prime) base  $b$  through an observation of Tezuka [348]. We digress briefly to explain this extension. Let  $a_0(k), a_1(k), \ldots, a_r(k)$  denote the coefficients in the base- $b$  expansion of  $k$ . Setting

$$\begin{pmatrix} g_0(k) \\ g_1(k) \\ \vdots \\ g_r(k) \end{pmatrix} = \begin{pmatrix} 1 & & & \\ b-1 \ 1 & & & \\ & & \ddots & \\ & & b-1 \ 1 & \\ & & b-1 \ 1 \end{pmatrix} \begin{pmatrix} a_0(k) \\ a_1(k) \\ \vdots \\ a_r(k) \end{pmatrix} \mod b$$

defines a base- $b$  Gray code, in the sense that the vectors thus calculated for k and  $k+1$  differ in exactly one entry. The index of the entry that changes is the smallest  $\ell$  for which  $a_{\ell}(k) \neq b-1$  (padding the expansion of k with an initial zero, if necessary, to ensure it has the same length as the expansion of  $k+1$ ). Moreover,  $g_{\ell}(k+1) = g_{\ell}(k) + 1$  modulo b.

This simplifies the Faure construction. Instead of defining the coefficients  $y_i^{(i)}(k)$  through the matrix-vector product (5.18), we may set

$$(y_1^{(i)}(k+1), \dots, y_r^{(i)}(k+1)) = (y_1^{(i)}(k), \dots, y_r^{(i)}(k)) + (\mathbf{C}^{(i)}(1,\ell), \dots, \mathbf{C}^{(i)}(r,\ell)) \bmod b,$$

once  $\ell$  has been determined from the vector  $\mathbf{a}(k)$ . This makes it possible to replace the loop over both  $m$  and  $n$  near the bottom of FAUREPTS in Figure 5.11 with a loop over a single index. See Figure  $5.13$ .

### Choosing Initial Direction Numbers

In initializing the recurrence (5.23), we required only that each  $m_j$  be an odd integer less than  $2^j$ . But suppose we initialize two different sequences (corresponding to two different coordinates of a  $d$ -dimensional sequence) with the same values  $m_1, \ldots, m_r$ . The first r columns of their generator matrices will then also be the same. The  $k$ th value generated in a Sobol' sequence depends only on as many columns as there are coefficients in the binary expansion of k; so, the first  $2^r-1$  values of the two sequences would be identical. Thus, whereas the choice of initial values may not be significant in constructing a one-dimensional sequence, it becomes important when  $d$  such sequences are voked together to make a  $d$ -dimensional sequence.

Sobol' [336] provides some guidance for choosing initial values. He establishes two results on uniformity properties achieved by initial values satisfying additional conditions. A d-dimensional sequence  $x_0, x_1, \ldots$  satisfies Sobol's Property A if for every  $j = 0, 1, \ldots$  exactly one of the points  $x_k$ ,  $j2^d \leq k < (j+1)2^d$  falls in each of the  $2^d$  cubes of the form

$$\prod_{i=1}^{d} \left[ \frac{a_i}{2}, \frac{a_i+1}{2} \right), \quad a_i \in \{0, 1\}.$$

The sequence satisfies Sobol's Property A' if for every  $j = 0, 1, \ldots$  exactly one of the points  $x_k, j2^{2d} \leq k < (j+1)2^{2d}$  falls in each of the  $2^{2d}$  cubes of the  $\text{form}$ 

$$\prod_{i=1}^{d} \left[ \frac{a_i}{4}, \frac{a_i+1}{4} \right), \quad a_i \in \{0, 1, 2, 3\}.$$

These properties bear some resemblance to the definition of a  $(t, d)$ -sequence but do not fit that definition because they restrict attention to specific equilateral boxes.

Let  $v_i^{(i)}$  denote the *j*th direction number associated with the *i*th coordinate of the sequence. The generator matrix of the  $i$ th sequence is then

$$\mathbf{V}^{(i)} = [v_1^{(i)} | v_2^{(i)} | \cdots | v_r^{(i)}],$$

where we again use  $v_j^{(i)}$  to denote the (column) vector of binary coefficients of a direction number as well as the direction number itself. Sobol' [336] shows that Property A holds if and only if the determinant constructed from the first  $d$  elements of the first row of each of the matrices satisfies

$$\begin{vmatrix} \mathbf{V}_{11}^{(1)} \ \mathbf{V}_{12}^{(1)} \ \cdots \mathbf{V}_{1d}^{(1)} \\ \mathbf{V}_{11}^{(2)} \ \mathbf{V}_{12}^{(2)} \ \cdots \mathbf{V}_{1d}^{(2)} \\ \vdots \ \vdots \ \vdots \ \vdots \\ \mathbf{V}_{11}^{(d)} \ \mathbf{V}_{12}^{(d)} \ \cdots \mathbf{V}_{1d}^{(d)} \end{vmatrix} \neq 0 \text{ mod } 2.$$

Property A applies to sets of size  $2^d$  and generating the first  $2^d$  points involves exactly the first  $d$  columns of the matrices. Sobol' also shows that Property A' holds if and only if the determinant constructed from the first  $2d$  elements of the first two rows of each of the matrices satisfies

$$\begin{vmatrix} \mathbf{V}_{11}^{(1)} \ \mathbf{V}_{12}^{(1)} \ \cdots \ \mathbf{V}_{1,2d}^{(1)} \\ \vdots & \vdots & \vdots \\ \mathbf{V}_{11}^{(d)} \ \mathbf{V}_{12}^{(d)} \ \cdots \ \mathbf{V}_{1,2d}^{(d)} \\ \mathbf{V}_{21}^{(1)} \ \mathbf{V}_{22}^{(1)} \ \cdots \ \mathbf{V}_{2,2d}^{(1)} \\ \vdots & \vdots & \vdots \\ \mathbf{V}_{21}^{(d)} \ \mathbf{V}_{22}^{(d)} \ \cdots \ \mathbf{V}_{2,2d}^{(d)} \end{vmatrix} \neq 0 \text{ mod } 2.$$

To illustrate, suppose  $d = 3$  and suppose the first three  $m_j$  values for the first three coordinates are as follows:

$$(m_1, m_2, m_3) = (1, 1, 1), \quad (m_1, m_2, m_3) = (1, 3, 5), \quad (m_1, m_2, m_3) = (1, 1, 7).$$

The first coordinate has  $m_j = 1$  for all j. The second coordinate is generated by a polynomial of degree 1, so all subsequent values are determined by  $m_1$ ; and because the third coordinate is generated by a polynomial of degree 2, that sequence is determined by the choice of  $m_1$  and  $m_2$ .

From the first three  $m_i$  values in each coordinate, we determine the ma $trices$ 

$$\mathbf{V}^{(1)} = \begin{pmatrix} 1 \ 0 \ 0 \\ 0 \ 1 \ 0 \\ 0 \ 0 \ 1 \end{pmatrix}, \quad \mathbf{V}^{(2)} = \begin{pmatrix} 1 \ 1 \ 1 \\ 0 \ 1 \ 0 \\ 0 \ 0 \ 1 \end{pmatrix}, \quad \mathbf{V}^{(3)} = \begin{pmatrix} 1 \ 0 \ 1 \\ 0 \ 1 \ 1 \\ 0 \ 0 \ 1 \end{pmatrix}.$$

From the first row of each of these we assemble the matrix

$$D = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}.$$

Because this matrix has a determinant of 1, Sobol's Property A holds.

The test matrix  $D$  can in fact be read directly from the  $m_j$  values:  $D_{ij} = 1$ if the  $m_i$  value for the *i*th coordinate is greater than or equal to  $2^{j-1}$ , and  $D_{ij} = 0$  otherwise.

Table 5.3 displays initial values of the  $m_i$  for up to 20 dimensions. Recall that the number of initial values required equals the degree of the corresponding primitive polynomial, and this increases with the dimension. The values displayed in parentheses are determined by the initial values in each row. The values displayed are from Bratley and Fox [57], who credit unpublished work of Sobol' and Levitan (also cited in Sobol' [336]). These values satisfy Property A; Property A' holds for  $d < 6$ .

|    | $m_1$ | $m_2$ | $m_3$        | $m_4$ | $m_5$ | $m_6$ | $m_7$ | $m_8$ |
|----|-------|-------|--------------|-------|-------|-------|-------|-------|
| 1  | 1     | (1)   | (1)          | (1)   | (1)   | (1)   | (1)   | (1)   |
| 2  | 1     | (3)   | (5)          | (15)  | (17)  | (51)  | (85)  | (255) |
| 3  | 1     | 1     | (7)          | (11)  | (13)  | (61)  | (67)  | (79)  |
| 4  | 1     | 3     | 7            | (5)   | (7)   | (43)  | (49)  | (147) |
| 5  | 1     | 1     | 5            | (3)   | (15)  | (51)  | (125) | (141) |
| 6  | 1     | 3     | 1            | 1     | (9)   | (59)  | (25)  | (89)  |
| 7  | 1     | 1     | 3            | 7     | (31)  | (47)  | (109) | (173) |
| 8  | 1     | 3     | 3            | 9     | 9     | (57)  | (43)  | (43)  |
| 9  | 1     | 3     | $\mathbf{7}$ | 13    | 3     | (35)  | (89)  | (9)   |
| 10 | 1     | 1     | 5            | 11    | 27    | (53)  | (69)  | (25)  |
| 11 | 1     | 3     | 5            | 1     | 15    | (19)  | (113) | (115) |
| 12 | 1     | 1     | 7            | 3     | 29    | (51)  | (47)  | (97)  |
| 13 | 1     | 3     | $\mathbf{7}$ | 7     | 21    | (61)  | (55)  | (19)  |
| 14 | 1     | 1     | 1            | 9     | 23    | 37    | (97)  | (97)  |
| 15 | 1     | 3     | 3            | 5     | 19    | 33    | (3)   | (197) |
| 16 | 1     | 1     | 3            | 13    | 11    | 7     | (37)  | (101) |
| 17 | 1     | 1     | 7            | 13    | 25    | 5     | (83)  | (255) |
| 18 | 1     | 3     | 5            | 11    | 7     | 11    | (103) | (29)  |
| 19 | 1     | 1     | 1            | 3     | 13    | 39    | (27)  | (203) |
| 20 | 1     | 3     | 1            | 15    | 17    | 63    | 13    | (65)  |

Table 5.3. Initial values satisfying Sobol's Property A for up to 20 dimensions. In each row, values in parentheses are determined by the previous values in the sequence.

Bratley and Fox [57] include initializing values from the same source for up to 40 dimensions. A remark in Sobol' [336] indicates that the Sobol'-Levitan values should satisfy Property A for up to 51 dimensions; however, we find (as does Morland [270]) that this property does not consistently hold for  $d > 20$ . More precisely, for d ranging from 21 to 40, we find that Property A holds only at dimensions 23, 31, 33, 34, and 37. We have therefore limited Table 5.3 to the first 20 dimensions. The complete set of values used by Bratley and Fox [57] is in their FORTRAN program, available through the Collected Algorithms of the ACM.

Press et al. [299] give initializing values for up to six dimensions; their values fail the test for Property A in dimensions three, five, and six. A further distinction merits comment. We assume (as do Sobol' [336] and Bratley and Fox [57]) that the first coordinate uses  $m_i \equiv 1$ ; this makes the first generator matrix the identity and thus makes the first coordinate the Van der Corput sequence in base 2. We use the polynomial  $x + 1$  for the second coordinate, and so on. Press et al. [299] use  $x+1$  for the first coordinate. Whether or not Property A holds for a particular set of initializing values depends on whether the first row (with  $m_i \equiv 1$ ) of Table 5.3 is included. Thus, one cannot interchange the initializing values used here with those used by Press et al. [299] for the same primitive polynomial, even in cases where both satisfy Property A.

The implementation of Lemieux, Cieslak, and Luttmer [231] includes initializing values for up to 360 dimensions. These values do not necessarily satisfy Sobol's property  $A$ , but they are the result of a search for good values based on a *resolution* criterion used in design of random number generators. See  $[231]$  and references cited there.

### Discrepancy

In the terminology of Section 5.1.4, Sobol' sequences are  $(t, d)$ -sequences in base 2. The example in the right panel of Figure  $5.3$  is the projection onto dimensions four and five of the first 128 points of a five-dimensional Sobol' sequence.

Theorem 3.4 of Sobol' [335] provides a simple expression for the t parameter in a  $d$ -dimensional sequence as

$$t = q_1 + q_2 + \dots + q_{d-1} - d + 1, \tag{5.26}$$

where  $q_1 \leq q_2 \leq \cdots \leq q_{d-1}$  are the degrees of the primitive polynomials used to construct coordinates 2 through  $d$ . Recall that the first coordinate is constructed from the degenerate recurrence with  $m_i \equiv 1$ , which may be considered to have degree zero. If instead we used polynomials of degrees  $q_1, \ldots, q_d$  for the d coordinates, the t value would be  $q_1 + \cdots + q_d - d$ . Sobol' [335] shows that while t grows faster than d, it does not grow faster than  $d \log d$ .

Although  $(5.26)$  gives a valid value for t, it does not always give the best possible value: a d-dimensional Sobol' sequence may be a  $(t', d)$ -sequence for some  $t' < t$ . Sobol [335] provides conditions under which (5.26) is indeed the minimum valid value of  $t$ .

Because they are  $(t, d)$ -sequences, Sobol' points are low-discrepancy sequences; see  $(5.13)$  and the surrounding discussion. Sobol' [335] provides more detailed discrepancy bounds.

### Implementation

Bratley and Fox  $[57]$  and Press et al.  $[299]$  provide computer programs to generate Sobol' points in FORTRAN and C, respectively. Both take advantage of bit-level operations to increase efficiency. Timings reported in Bratley and Fox  $[57]$  indicate that using bit-level operations typically increases speed by a factor of more than ten, with greater improvements in higher dimensions.

We give a somewhat more schematic description of an implementation, suppressing programming details in the interest of transparency. Our description also highlights similarities between the construction of Sobol' points and Faure points.

As in the previous section, we separate the construction of generator matrices from the generation of the points themselves. Figure  $5.12$  displays a function SOBOLMAT to produce a generator matrix as described in the discussion leading to (5.24). The function takes as input a binary vector  $c_{\text{vec}}$ giving the coefficients of a primitive polynomial, a vector  $m_{\text{init}}$  of initializing values, and a parameter  $r$  determining the size of the matrix produced. For a polynomial of degree q, the vector  $c_{\text{vec}}$  has the form  $(1, c_1, \ldots, c_{q-1}, 1)$ ; see (5.22). The vector  $m_{\text{init}}$  must then have q elements — think of using the row of Table 5.3 corresponding to the polynomial  $c_{\text{vec}}$ , including only those values in the row that do not have parentheses. The parameter r must be at least as large as q. Building an  $r \times r$  matrix requires calculating  $m_{q+1}, \ldots, m_r$  from the initial values  $m_1, \ldots, m_q$  in  $m_{\text{init}}$ . These are ultimately stored in  $m_{\text{vec}}$ which (to be consistent with Table 5.3) orders  $m_1, \ldots, m_r$  from left to right. In calling SOBOLMAT, the value of  $r$  is determined by the number of points to be generated: generating the point  $x_{2^k}$  requires  $r = k + 1$ .

The function SOBOLMAT could almost be substituted for FAUREMAT in the function FAUREPTS of Figure 5.11: the only modification required is passing the *i*th primitive polynomial and the *i*th set of initializing values, rather than just  $i$  itself. The result would be a legitimate algorithm to generate Sobol' points.

Rather than reproduce what we did in FAUREPTS, here we display an implementation using the Gray code construction of Antanov and Saleev [18]. The function SOBOLPTS in Figure 5.13 calls an undefined function GRAY-CODE2 to find a binary Gray code representation. This can implemented  $\text{as}$ 

### $\text{GRAYCODE2}(n) = \text{B-ARY}(n, 2) \oplus \text{B-ARY}(|n/2|, 2),$

after padding the second argument on the right with an initial zero to give the two arguments the same length.

In SOBOLPTS, a Gray code representation is explicitly calculated only for  $n_0 - 1$ . The Gray code vector **g** is subsequently incremented by toggling the  $\ell$ th bit, with  $\ell$  determined by the usual binary representation **a**, or by inserting a leading 1 at each power of 2 (in which case  $\ell = 1$ ). As in (5.25), the value of  $\ell$  is then the index of the column of  $\mathbf{V}^{(i)}$  to be added (mod 2) to the previous point. The coefficients of the binary expansion of the *i*th

```
\text{SOBOLMAT}(c_{\text{vec}}, m_{\text{init}}, r)[c_{\text{vec}} \text{ has the form } (1, c_1, \ldots, c_{q-1}, 1), m_{\text{init}} \text{ has length } q \leq r]q \leftarrow \text{length}(c_{\text{vec}}) - 1if (q = 0) \mathbf{V} \leftarrow I \quad [r \times r \text{ identity}]if (q > 0)m_{\text{vec}} \leftarrow (m_{\text{init}}(1,\ldots,q),0,\ldots,0)\left[\text{length } r\right]m_{\text{state}} \leftarrow m_{\text{init}}for i = q + 1, \ldots, rm_{\text{next}} \leftarrow 2c_1 m_{\text{state}}(q) \oplus 4c_2 m_{\text{state}}(q-1) \oplus \cdots \oplus 2^q m_{\text{state}}(1) \oplus m_{\text{state}}(1)m_{\text{vec}}(i) \leftarrow m_{\text{next}}m_{\text{state}} \leftarrow (m_{\text{state}}(2, \ldots, q), m_{\text{next}})for j = 1, \ldots, rm_{\text{bin}} \leftarrow \text{B-ARY}(m_{\text{vec}}(j), 2)k \leftarrow \text{length}(m_{\text{bin}})for i = 1, \ldots, k\mathbf{V}(j-i+1,j) \leftarrow m_{\text{bin}}(k-i+1)\text{return } V
```

service converges a

**Fig. 5.12.** Function SOBOLMAT( $c_{\text{vec}}, m_{\text{init}}, r$ ) returns  $r \times r$  generator matrix V constructed from polynomial coefficients  $(1, c_1, \ldots, c_{q-1}, 1)$  in  $c_{\text{vec}}$  and  $q$  initial values in array  $m_{\text{init}}$ .

coordinate of each point are held in the *i*th column of the array  $y$ . Taking the inner product between this column and the powers of  $1/2$  in  $b_{\text{pwrs}}$  maps the coefficients to  $[0,1)$ . The argument  $p_{\text{pvec}}$  is an array encoding primitive polynomials using the numerical representation in Table 5.2, and  $m_{\text{mat}}$  is an array of initializing values (as in Table  $5.3$ ).

### 5.2.4 Further Constructions

The discussions in Sections  $5.2.2$  and  $5.2.3$  make evident similarities between the Faure and Sobol' constructions: both apply permutations to segments of the Van der Corput sequence, and these permutations can be represented through generator matrices. This strategy for producing low-discrepancy sequences has been given a very general formulation and analysis by Niederreiter [281]. Points constructed in this framework are called *digital* nets or sequences. Section 4.5 of Niederreiter  $[281]$  presents a special class of digital sequences, which encompass the constructions of Faure and Sobol'. Niederreiter shows how to achieve a  $t$  parameter through this construction (in base 2) strictly smaller than the best  $t$  parameter for Sobol' sequences in all dimensions greater than seven. Thus, these *Niederreiter* sequences have some theoretical superiority over Sobol' sequences. Larcher  $[219]$  surveys more recent theoretical developments in digital point sets.

Bratley, Fox, and Niederreiter  $[58]$  provide a FORTRAN generator for Niederreiter sequences. They note that for base 2 their program is "essentially

```
\text{SOBOLPTS}(n_0, n_{\text{pts}}, d, p_{\text{vec}}, m_{\text{mat}})n_{\text{max}} \leftarrow n_0 + n_{\text{pts}} - 1r_{\max} \leftarrow 1 + \lfloor (\log(n_{\max}) / \log(2)) \rfloor,r \leftarrow 1P \leftarrow 0 \quad [n_{\text{pts}} \times d], \qquad \mathbf{y} \leftarrow 0 \quad [r_{\text{max}} \times d]if (n_0 > 1) r \leftarrow 1 + |(\log(n_0 - 1)/\log(2))|q_{\text{next}} \leftarrow 2^r\mathbf{a} \leftarrow \text{B-ARY}(n_0 - 1, 2)\mathbf{g} \leftarrow \text{GRAYCODE2}(n_0 - 1)for i = 1, \ldots, d [build matrices using polynomials in p_{\text{vec}}]
       q \leftarrow |(\log(p_{\text{vec}}(i))/\log(2))|c_{\text{vec}} \leftarrow \text{B-ARY}(p_{\text{vec}}(i), 2)\mathbf{V}^{(i)} \leftarrow \text{SOBOLMAT}(c_{\text{vec}}, (m_{\text{mat}}(i, 1), \dots, m_{\text{mat}}(i, q)), r_{\text{max}})b_{\text{pwrs}} \leftarrow (1/2, 1/4, \dots, 1/2^{r_{\text{max}}})for i = 1, \ldots, d [Calculate point n_0 - 1 using Gray code]
       for m = 1, \ldots, rfor n = 1, \ldots, r\mathbf{y}(m,i) \leftarrow \mathbf{y}(m,i) + \mathbf{V}^{(i)}(m,n) \ast \mathbf{g}(r-n+1) \bmod 2for k = n_0, \ldots, n_{\text{max}}if (k = q_{\text{next}})r \leftarrow r + 1\mathbf{g} \leftarrow (1, \ \mathbf{g})[\text{insert 1 in Gray code at powers of 2}]\ell \leftarrow 1 [first bit changed]
             q_{\text{next}} \leftarrow 2 * q_{\text{next}}else\ell \leftarrow \text{index of rightmost zero in } \mathbf{a}\mathbf{g}(\ell) \leftarrow 1 - \mathbf{g}(\ell) \quad \text{[increment Gray code]}\mathbf{a} \leftarrow \text{NEXTB-ARY}(\mathbf{a}, 2)for i = 1, \ldots, d [Calculate point k recursively]
            for m = 1, \ldots, r\mathbf{y}(m,i) \leftarrow \mathbf{y}(m,i) + \mathbf{V}^{(i)}(m,r-\ell+1) \bmod 2for j = 1, \ldots, rP(k - n_0 + 1, i) \leftarrow P(k - n_0 + 1, i) + b_{\text{pwrs}}(j) \ast \mathbf{y}(j, i)return P
```

**Fig. 5.13.** Function SOBOLPTS $(n_0, n_{\text{pts}}, d, p_{\text{vec}}, m_{\text{mat}})$  returns  $n_{\text{pts}} \times d$  array whose rows are coordinates of  $d$ -dimensional Sobol' points, using polynomials encoded in  $p_{\text{vec}}$  and initializing values in the rows of  $m_{\text{mat}}$ .

identical" to one for generating Sobol' points, differing only in the choice of generator matrices. Their numerical experiments indicate roughly the same accuracy using Niederreiter and Sobol' points on a set of test integrals.

Tezuka [347] introduces a counterpart of the radical inverse function with respect to polynomial arithmetic. This naturally leads to a generalization of Halton sequences; Tezuka also extends Niederreiter's digital construction to this setting and calls the resulting points generalized Niederreiter sequences.

Tezuka and Tokuyama [349] construct  $(0, d)$ -sequences in this setting using generator matrices for which they give an explicit expression that generalizes the expression in  $(5.19)$  for Faure generator matrices. Tezuka [348] notes that these generator matrices have the form

$$\mathbf{A}^{(i)}(\mathbf{C}^{(1)})^{i-1}, \quad i = 1, \dots, d,\tag{5.27}$$

with  $\mathbf{C}^{(1)}$  as in (5.19), and  $\mathbf{A}^{(i)}$  arbitrary nonsingular (mod b) lower triangular matrices. The method of Tezuka and Tokuyama [349] is equivalent to taking  $\mathbf{A}^{(i)}$  to be the transpose of  $(\mathbf{C}^{(1)})^{i-1}$ . Tezuka [348] shows that all sequences constructed using generator matrices of the form (5.27) in a prime base  $b \geq d$ are  $(0, d)$ -sequences. He calls these *generalized Faure sequences*; they are a special case of his generalized Niederreiter sequences and they include ordinary Faure sequences (take each  $\mathbf{A}^{(i)}$  to be the identity matrix). Although the path leading to  $(5.27)$  is quite involved, the construction itself requires only minor modification of an algorithm to generate Faure points.

Faure [117] proposes an alternative method for choosing generator matrices to construct  $(0, d)$ -sequences and shows that these do not have the form in  $(5.27).$ 

A series of theoretical breakthroughs in the construction of low-discrepancy sequences have been achieved by Niederreiter and Xing using ideas from algebraic geometry; these are reviewed in their survey article  $[282]$ . Their methods lead to  $(t, d)$ -sequences with theoretically optimal t parameters. Pirsic [298] provides a software implementation and some numerical tests. Further numerical experiments are reported in Hong and Hickernell [187].

## 5.3 Lattice Rules

The constructions in Sections  $5.2.1-5.2.3$  are all based on extending the Van der Corput sequence to multiple dimensions. The *lattice rules* discussed in this section provide a different mechanism for constructing low-discrepancy point sets. Some of the underlying theory of lattice methods suggests that they are particularly well suited to smooth integrands, but they are applicable to essentially any integrand.

Lattice methods primarily define fixed-size point sets, rather than infinite sequences. This is a shortcoming when the number of points required to achieve a satisfactory precision is not known in advance. We discuss a mechanism for extending lattice rules after considering the simpler setting of a fixed number of points.

A rank-1 lattice rule of  $n$  points in dimension  $d$  is a set of the form

$$\left\{\frac{k}{n}\mathbf{v} \bmod 1, \quad k = 0, 1, \dots, n-1\right\},\tag{5.28}$$

with  $\mathbf{v}$  a d-vector of integers. Taking the remainder modulo 1 means taking the fractional part of a number  $(x \mod 1 = x - \lfloor x \rfloor)$ , and the operation is

applied separately to each coordinate of the vector. To ensure that this set does indeed contain  $n$  distinct points (i.e., that no points are repeated), we require that  $n$  and the components of  $\mathbf{v}$  have 1 as their greatest common divisor.

An  $n$ -point lattice rule of rank  $r$  takes the form

r.

$$\left\{\sum_{i=1}^{r} \frac{k_i}{n_i} \mathbf{v}_i \bmod 1, \quad k_i = 0, 1, \dots, n_i - 1, \quad i = 1, \dots, r\right\},\$$

for linearly independent integer vectors  $\mathbf{v}_1, \ldots, \mathbf{v}_r$  and integers  $n_1, \ldots, n_r \geq 2$ with each  $n_i$  dividing  $n_{i+1}, i = 1, \ldots, r-1$ , and  $n_1 \cdots n_r = n$ . As in the rank-1 case, we require that  $n_i$  and the elements of  $\mathbf{v}_i$  have 1 as their greatest common divisor.

Among rank-1 lattices, a particularly simple and convenient class are the *Korobov rules*, which have a generating vector **v** of the form  $(1, a, a^2, \ldots, a^{d-1})$ , for some integer  $a$ . In this case, (5.28) can be described as follows: for each  $k = 0, 1, \ldots, n - 1$ , set  $y_0 = k, u_0 = k/n$ ,

$$y_i = ay_{i-1} \bmod n, \quad i = 1, \ldots, d-1, \quad u_i = y_i/n,$$

and set  $x_k = (u_0, u_1, \ldots, u_{d-1})$ . Comparison with Section 2.1.2 reveals that this is the set of vectors formed by taking  $d$  consecutive outputs from a multiplicative congruential generator, from all initial seeds  $y_0$ .

It is curious that the same mechanism used in Chapter 2 to mimic randomness is here used to try to produce low discrepancy. The apparent paradox is resolved by noting that here we intend to use the full period of the generator (we choose the modulus  $n$  equal to the number of points to be generated), whereas the algorithms of Section 2.1 are designed so that we use a small fraction of the period. To reconcile the two applications, we would like the discrepancy of the first N out of n points to be  $O(1/\sqrt{N})$  for small N and  $O((\log N)^d/N)$  for large N.

The connection between Korobov rules and multiplicative congruential generators has useful consequences. It simplifies implementation and it facilitates the selection of generating vectors by making relevant the extensively studied properties of random number generators; see Hellekalek [176], Hickernell, Hong, L'Ecuyer, and Lemieux [184], L'Ecuyer and Lemieux [226], Lemieux and L'Ecuyer [232], and Niederreiter [281]. Hickernell [182], Chapter 5 of Niederreiter [281], and Sloan and Joe [333] analyze the discrepancy of lattice rules and other measures of their quality.

Tables of good generating vectors  $\mathbf{v}$  can be found in Fang and Wang [115] for up to 18 dimensions. Sloan and Joe [333] give tables for higher-rank lattice rules in up to 12 dimensions. L'Ecuyer and Lemieux [226] provide tables of multipliers  $a$  for Korobov rules passing tests of uniformity.

### Integration Error

The Koksma-Hlawka bound  $(5.10)$  applies to lattice rules as it does to all point sets. But the special structure of lattice rules leads to a more explicit expression for the integration error using such a rule, and this in turn sheds light on both the design and scope of these methods.

Fix an integrand f on  $[0,1]^d$ , and for each d-vector of integers z define the Fourier coefficient

$$\hat{f}(z) = \int_{[0,1)^d} f(x) e^{-2\pi\sqrt{-1}x^\top z} dx.$$

The integral of f over the hypercube is  $\hat{f}(0)$ . Suppose that f is sufficiently regular to be represented by its Fourier series, in the sense that

$$f(x) = \sum_{z} \hat{f}(z)e^{2\pi\sqrt{-1}x^{\top}z},$$
 (5.29)

the sum ranging over all integer vectors  $z$  and converging absolutely.

A rank-1 lattice rule approximation to the integral of  $f$  is

$$\frac{1}{n} \sum_{k=0}^{n-1} f\left(\frac{k}{n} \mathbf{v} \bmod 1\right) = \frac{1}{n} \sum_{k=0}^{n-1} \sum_{z} \hat{f}(z) \exp\left(2\pi\sqrt{-1}k\mathbf{v}^{\top}z/n\right)$$
$$= \sum_{z} \hat{f}(z) \frac{1}{n} \sum_{k=0}^{n-1} \left[\exp\left(2\pi\sqrt{-1}\mathbf{v}^{\top}z/n\right)\right]^{k} . \tag{5.30}$$

The first equality follows from the Fourier representation of  $f$  and the periodicity of the function  $u \mapsto \exp(2\pi\sqrt{-1}u)$ , which allows us to omit the reduction modulo 1. For the second equality, the interchange in the order of summation is justified by the assumed absolute convergence of the Fourier series for  $f$ . Now the average over  $k$  in (5.30) simplifies to

$$\frac{1}{n} \sum_{k=0}^{n-1} \left[ \exp\left(2\pi\sqrt{-1}\mathbf{v}^{\top}z/n\right) \right]^k = \begin{cases} 1, \text{ if } \mathbf{v}^{\top}z = 0 \text{ mod } n, \\ 0, \text{ otherwise.} \end{cases}$$

To see why, observe that if  $\mathbf{v}^{\top}z/n$  is an integer then each of the summands on the left is just  $1$ ; otherwise,

$$\sum_{k=0}^{n-1} \left[ \exp\left(2\pi\sqrt{-1}\mathbf{v}^{\top}z/n\right) \right]^{k} = \frac{1 - \exp(2\pi\sqrt{-1}\mathbf{v}^{\top}z)}{1 - \exp(2\pi\sqrt{-1}\mathbf{v}^{\top}z/n)} = 0$$

because  $\mathbf{v}^{\top}z$  is an integer. Using this in (5.30), we find that the lattice rule approximation simplifies to the sum of  $\hat{f}(z)$  over all integer vectors z for which  $\mathbf{v}^{\top}z=0 \bmod n$ . The correct value of the integral is  $\hat{f}(0)$ , so the error in the approximation is

 $5.3$  Lattice Rules 319

$$\sum_{z \neq 0, \mathbf{v}^\top z = 0 \bmod n} \hat{f}(z). \tag{5.31}$$

The values of  $|\hat{f}(z)| = |\hat{f}(z_1,\ldots,z_d)|$  for large values of  $|z| = |z_1| + \cdots + |z_d|$ reflect the smoothness of  $f$ , in the sense that large values of  $|z|$  correspond to high-frequency oscillation terms in the Fourier representation of  $f$ . The expression in  $(5.31)$  for the integration error thus suggests the following:

- (i) the generator **v** should be chosen so that  $\mathbf{v}^{\top}z = 0 \mod n$  only if  $|z|$  is large — vectors  $\mathbf{v}$  with this property are known informally as *good lattice*  $points;$
- (ii) lattice rules are particularly well suited to integrands  $f$  that are smooth precisely in the sense that  $\hat{f}(z)$  decreases quickly as  $|z|$  increases.

The first of these observations helps guide the search for effective choices of  $\mathbf{v}$ . (Results showing the *existence* of good lattice points are detailed in Chapter 5 of Niederreiter [281].) Precise criteria for selecting  $\mathbf{v}$  are related to the spectral test mentioned in the discussion of random number generators in Section 2.1. Recommended values are tabulated in Fang and Wang [115].

The direct applicability of observation (ii) seems limited, at least for the integrands implicit in derivative pricing. Bounding the Fourier coefficients of such functions is difficult, and there is little reason to expect these functions to be smooth. Moreover, the derivation leading to  $(5.31)$  obscures an important restriction: for the Fourier series to converge absolutely,  $f$  must be continuous on  $[0,1]^d$  and periodic at the boundaries (because absolute convergence makes  $f$  the uniform limit of functions with these properties). Sloan and Joe [333] advise caution in applying lattice rules to nonperiodic integrands; in their numerical results, they find Monte Carlo to be the best method for discontinuous integrands.

#### Extensible Lattice Rules

We conclude our discussion of lattice rules with a method of Hickernell et al. [184] for extending fixed-size lattice rules to infinite sequences.

Consider a rank-1 lattice rule with generating vector  $\mathbf{v} = (v_1, \ldots, v_d)$ . Suppose the number of points n equals  $b^r$  for some base b and integer r. Then the segment  $\psi_b(0), \psi_b(1), \ldots, \psi_b(n-1)$  of the Van der Corput sequence in base b is a permutation of the coefficients  $k/n$ ,  $k = 0, 1, \ldots, n-1$ , appearing in  $(5.28)$ . The point set is therefore unchanged if we represent it as

$$\{\psi_b(k)\mathbf{v} \bmod 1, \ k = 0, 1, \ldots, n-1\}.$$

We may now drop the upper limit on  $k$  to produce an infinite sequence.

The first  $b^r$  points in this sequence are the original lattice point set. Each of the next  $(b-1)$  nonoverlapping segments of length  $b^r$  will be shifted versions of the original lattice. The first  $b^{r+1}$  points will again form a lattice rule of

the type (5.28), but now with n replaced by  $b^{r+1}$ , and so on. In this way, the construction extends and refines the original lattice.

Hickernell et al. [184] give particular attention to extensible Korobov rules, which are determined by the single parameter  $a$ . They provide a table of values of this parameter that exhibit good uniformity properties when extended using  $b = 2$ . Their numerical results use  $a = 17797$  and  $a = 1267$ .

## $5.4$ Randomized QMC

We began this chapter with the suggestion that choosing points deterministically rather than randomly can reduce integration error. It may therefore seem odd to consider randomizing points chosen carefully for this purpose. There are, however, at least two good reasons for randomizing QMC.

The first reason is as immediately applicable as it is evident: by randomizing QMC points we open the possibility of measuring error through a confidence interval while preserving much of the accuracy of pure QMC. Randomized QMC thus seeks to combine the best features of ordinary Monte Carlo and quasi-Monte Carlo. The tradeoff it poses — sacrificing some precision to  $\text{get a better measure of error}$  — is essentially the same one we faced with several of the variance reduction techniques of Chapter 4.

The second reason to consider randomizing QMC is less evident and may also be less practically relevant: there are settings in which randomization actually improves accuracy. A particularly remarkable result of this type is a theorem of Owen [289] showing that the root mean square error of integration using a class of randomized nets is  $O(1/n^{1.5-\epsilon})$ , whereas the error without randomization is  $O(1/n^{1-\epsilon})$ . Owen's result applies to smooth integrands and may therefore be of limited applicability to pricing derivatives; nevertheless, it is notable that randomization takes advantage of the additional smoothness though QMC does not appear to. Hickernell [180], Matoušek [257], and L'Ecuyer and Lemieux  $[226]$  discuss other ways in which randomization can improve accuracy.

We describe four methods for randomizing QMC. For a more extensive treatment of the topic, see the survey article of L'Ecuyer and Lemieux  $[226]$ and Chapter 14 of Fox [127]. We limit the discussion to randomization of point sets of a fixed size  $n$ . We denote such a point set generically by

$$P_n = \{x_1, \ldots, x_n\},\$$

each  $x_i$  an element of  $[0,1)^d$ .

### Random Shift

The simplest randomization of the point set  $P_n$  generates a random vector U uniformly distributed over the  $d$ -dimensional unit hypercube and shifts each point in  $P_n$  by U, modulo 1:

 $5.4$  Randomized QMC 321

$$P_n(U) = \{x_i + U \text{ mod } 1, i = 1, \dots, n\}.$$

$$(5.32)$$

The reduction mod 1 applies separately to each coordinate. The randomized QMC estimate of the integral of  $f$  is

$$I_f(U) = \frac{1}{n} \sum_{i=1}^n f(x_i + U \text{ mod } 1).$$

This mechanism was proposed by Cranley and Patterson [92] in the setting of a lattice rule, but can be applied with other low-discrepancy point sets. It should be noted, however, that the transformation changes the discrepancy of a point set and that a shifted  $(t, m, d)$ -net need not be a  $(t, m, d)$ -net.

For any  $P_n \subseteq [0,1)^d$ , each element of  $P_n(U)$  is uniformly distributed over the hypercube, though the points are clearly not independent. Repeating the randomization with independent replications of  $U$  produces independent batches of  $n$  points each. Each batch yields a QMC estimate of the form  $I_f(U)$ , and these estimates are independent and identically distributed. Moreover, each  $I_f(U)$  is an unbiased estimate of the integral f, so computing an asymptotically valid confidence interval for the integral is straightforward.

L'Ecuyer and Lemieux [226] compare the variance of  $I_f(U)$  and an ordinary Monte Carlo estimate with  $P_n$  a lattice rule. They show that either variance could be smaller, depending on the integrand f, but argue that  $I_f(U)$  often has smaller variance in problems of practical interest.

The random-shift procedure may be viewed as an extreme form of systematic sampling (discussed in Section 4.2), in which a single point  $U$  is chosen randomly and  $n$  points are then chosen deterministically conditional on  $U$ . The variance calculation of L'Ecuyer and Lemieux  $[226]$  for a randomly shifted lattice rule has features in common with the calculation for systematic sampling in Section  $4.2$ .

### Random Permutation of Digits

Another mechanism for randomizing QMC applies a random permutation of  $0, 1, \ldots, b-1$  to the coefficients in the base-b expansion of the coordinates of each point. Consider, first, the one-dimensional case and write  $x_k = 0.a_1(k)a_2(k)\dots$  for a b-ary representation of  $x_k$ . Let  $\pi_j, j = 1, 2, \dots$ be independent random permutations of  $\{0, 1, \ldots, b-1\}$ , uniformly distributed over all b! permutations of the set. Randomize  $P_n$  by mapping each point  $x_k$  to the point  $0.\pi_1(a_1(k))\pi_2(a_2(k))\ldots$ , applying the same permutations  $\pi_i$ to all points  $x_k$ . For a d-dimensional point set, randomize each coordinate in this way, using independent permutations for different coordinates.

Randomizing an arbitrary point  $x \in [0,1)^d$  in this way produces a random vector uniformly distributed over  $[0,1)^d$ . Thus, for any  $P_n$ , the average of f over the randomization of  $P_n$  is an unbiased estimate of the integral of  $f.$  Independent randomizations produce independent estimates that can be combined to estimate a confidence interval.

Matoušek  $[257]$  analyzes the expected mean-square discrepancy for a general class of randomization procedures that includes this one. This randomization maps b-ary boxes to b-ary boxes of the same volume, so if  $P_n$  is a  $(t, m, d)$ -net, its randomization is too.

### Scrambled Nets

Owen  $[287, 288, 289]$  introduces and analyzes a randomization mechanism that uses a hierarchy of permutations. This *scrambling* procedure permutes each digit of a *b*-ary expansion, but the permutation applied to the *j*th digit depends on the first  $j-1$  digits.

To make this more explicit, first consider the one-dimensional case. Suppose x has b-ary representation  $0.a_1a_2a_3...$  The first coefficient  $a_1$  is mapped to  $\pi(a_1)$ , with  $\pi$  a random permutation of  $\{0,1,\ldots,b-1\}$ . The second coefficient is mapped to  $\pi_{a_1}(a_2)$ , the third coefficient to  $\pi_{a_1a_2}(a_3)$ , and so on; the random permutations  $\pi, \pi_{a_1}, \pi_{a_1 a_2}, \ldots, a_j = 0, 1, \ldots, b-1, j = 1, 2, \ldots,$ are independent with each uniformly distributed over the set of all permutations of  $\{0, 1, \ldots, b-1\}$ . To scramble a d-dimensional point set, apply this procedure to each coordinate, using independent sets of permutations for each coordinate.

Owen [290] describes scrambling as follows. In each coordinate, partition the unit interval into b subintervals of length  $1/b$  and randomly permute those subintervals. Further partition each subinterval into  $b$  subintervals of length  $1/b^2$  and permute those, randomly and independently, and so on. At the jth step, this procedure constructs  $b^{j-1}$  partitions, each consisting of b intervals, and permutes each partition independently. In contrast, Matoušek's random digit permutation applies the same permutation to all  $b^{j-1}$  partitions at each step  $j$ .

Owen [287] shows that a scrambled  $(t, m, d)$ -net is a  $(t, m, d)$ -net with probability one, and a scrambled  $(t, d)$ -sequence is a  $(t, d)$ -sequence with probability one. Owen  $[288, 289, 290]$  shows that the variance of a scrambled net estimator converges to zero faster than the variance of an ordinary Monte Carlo estimator does, while cautioning that the faster rate may not set in until the number of points becomes very large. For sufficiently smooth integrands, the variance is  $O(1/n^{3-\epsilon})$  in the sample size n. The superior asymptotic performance with randomization results from cancellation of error terms. For fixed sample sizes, Owen  $[288, 290]$  bounds the amount by which the scrambled net variance can exceed the Monte Carlo variance. Hickernell and Hong [183] analyze the mean square discrepancy of scrambled nets.

Realizing the attractive features of scrambled nets in practice is not entirely straightforward because of the large number of permutations required for scrambling. Tan and Boyle  $[345]$  propose an approximate scrambling method based on permuting just the first few digits and find experimentally that it works well. Matoušek  $[257]$  outlines an implementation of full scramoling that reduces memory requirements at the expense of increasing computing time: rather than store a permutation, he stores the state of the random number generator and regenerates each permutation when it is needed. Hong and Hickernell [187] define a simplified form of scrambling and provide algorithms that generate scrambled points in about twice the time required for unscrambled points.

### Linear Permutation of Digits

í.

As an alternative to full scrambling, Matoušek [257] proposes a "linear" permutation method. This method maps a base-b expansion  $0.a_1a_2...$  to  $0.\tilde{a}_1\tilde{a}_2\ldots$  using

$$\tilde{a}_j = \sum_{i=1}^j h_{ij} a_i + g_j \bmod b,$$

with the  $h_{ij}$  and  $g_j$  chosen randomly and independently from  $\{0, 1, \ldots, b-1\}$ and the  $h_{ii}$  required to be positive. This method is clearly easier to implement than full scrambling. Indeed, if the  $g_i$  were all 0, this would reduce to the generalized Faure method in (5.27) when applied to a Faure net  $P_n$ . The condition that the diagonal entries  $h_{ii}$  be positive ensures the nonsingularity required in  $(5.27)$ .

All of the randomization methods described in this section produce points uniformly distributed over  $[0,1)^d$  and thus unbiased estimators of integrals over  $[0,1)^d$  when applied in the QMC approximation (5.2). Through independent replications of any of these it is a simple matter to construct asymptotically valid confidence intervals. The methods vary in evident ways in their computational requirements; the relative merits of the estimates they produce are less evident and warrant further investigation.

## 5.5 The Finance Setting

Our discussion of quasi-Monte Carlo has thus far been fairly abstract, dealing with the generic problem of numerical integration over  $[0,1)^d$ . In this section, we deal more specifically with the application of QMC to the pricing of derivative securities. Section  $5.5.1$  discusses numerical results comparing QMC methods and ordinary Monte Carlo on some test problems. Section 5.5.2 discusses ways of taking advantage of the structure of financial models to enhance the effectiveness of QMC methods.

### 5.5.1 Numerical Examples

Several articles have reported numerical results obtained by applying QMC methods to financial problems. These include Acworth et al. [4], Berman [45],

Boyle et al. [53], Birge [47], Caflisch, Morokoff, and Owen [73], Joy. Boyle, and Tan [204], Ninomiya and Tezuka [283], Papageorgiou and Traub [293], Paskov [295], Paskov and Traub [296], Ross [309], and Tan and Boyle [345]. These investigations consider several different QMC methods applied to various pricing problems and find that they work well. We comment more generally on the numerical evidence after considering some examples.

A convenient set of problems for testing QMC methods are options on geometric averages of lognormally distributed asset prices. These options are tractable in arbitrarily high dimensions (and knowing the correct answer is useful in judging performance of numerical methods) while sharing features of more challenging multiple-asset and path-dependent pricing problems. We consider, then, options with payoffs  $(\bar{S} - K)^+$  where either

$$\bar{S} = \prod_{i=1}^{d} S_i(T)^{1/d} \tag{5.33}$$

for multiple assets  $S_1, \ldots, S_d$ , or

$$\bar{S} = \prod_{i=1}^{d} S(iT/d)^{1/d}, \qquad (5.34)$$

for a single asset S. The underlying assets  $S_1, \ldots, S_d$  or S are modeled as geometric Brownian motion. Because  $\bar{S}$  is lognormally distributed in both cases, the option price is given by a minor modification of the Black-Scholes formula, as noted in Section  $3.2.2$ .

The two cases  $(5.33)$  and  $(5.34)$  reflect two potential sources of high dimensionality in financial problems:  $d$  is the number of underlying assets in  $(5.33)$ and it is the number of time steps in  $(5.34)$ . Of course, in both cases S is the geometric average of (jointly) lognormal random variables so this distinction is purely a matter of interpretation. The real distinction is the correlation structure among the averaged random variables. In  $(5.34)$ , the correlation is determined by the dynamics of geometric Brownian motion and is rather high; in  $(5.33)$ , we are free to choose any correlation matrix for the (logarithms of the)  $d$  assets. Choosing a high degree of correlation would be similar to reducing the dimension of the problem; to contrast with  $(5.34)$ , in  $(5.33)$  we choose the  $d$  assets to be independent of each other.

A comparison of methods requires a figure of merit. For Monte Carlo methods, variance is an appropriate figure of merit  $-$  at least for unbiased estimators with similar computing requirements, as argued in Section  $1.1.3$ . The average of  $n$  independent replications has a variance exactly  $n$  times smaller than the variance of a single replication, so a comparison of variances is not tied to a particular sample size. In contrast, the integration error produced by a QMC method does depend on the number of points  $n$ , and often quite erratically. Moreover, the QMC error can be quite sensitive to problem parameters. This makes the comparison of QMC methods less straightforward.

As our figure of merit, we take the root mean square error or root mean square relative error over a fixed set of problem instances. This is somewhat arbitrary (especially in the choice of instances) but nevertheless informative. Given m problems with true values  $C_1, \ldots, C_m$  and n-point QMC approximations  $\hat{C}_1(n), \ldots, \hat{C}_m(n)$ , the root mean square error is

RMSE
$$(n)$$
 =  $\sqrt{\frac{1}{m} \sum_{i=1}^{m} (\hat{C}_i(n) - C_i)^2}$ 

and the RMS relative error is

$$\sqrt{\frac{1}{m}\sum_{i=1}^{m}\left(\frac{\hat{C}_i(n)-C_i}{C_i}\right)^2}.$$

In order to compare QMC methods with Monte Carlo, we extend these definitions to random estimators  $\hat{C}_i(n)$  by replacing  $(\hat{C}_i(n) - C_i)^2$  with  $\mathsf{E}[(\hat{C}_i(n) - C_i)^2]$  in both cases.

Our first example is based on (5.33) with  $d = 5$  assets; as this is a relatively low-dimensional problem, it should be particularly well suited to QMC methods. For simplicity, we take the five assets to be independent copies of the same process GBM $(r, \sigma^2)$  with an initial value of  $S_i(0) = 100$ . We fix r at 5%, and construct 500 problem instances through all combinations of the following parameters: the maturity T is 0.15, 0.25, 0.5, 1, or 2 years; the volatility  $\sigma$ varies from 0.21 to 0.66 in increments of 0.05; and the strike K varies from  $94$  to  $103$  in increments of 1. These 500 options range in price from 0.54 to  $12.57$ ; their average value is 5.62, and half lie between 4.06 and 7.02.

Figure 5.14 plots the RMSE against the number of points, using a log scale for both axes. For the QMC methods, the figure displays the exact number of points used. For the Sobol' points, we skipped the first 256 points and then chose the number of points to be powers of two. For the Faure points, we skipped the first  $625 (= 5^4)$  points and then chose the number of points to be powers of five (the base). These choices are favorable for each method. For the lattice rules the number of points is fixed. We used the following generating vectors from  $p.287$  of Fang and Wang [115]:

| n       |                   |                                                                                               |                 |  |
|---------|-------------------|-----------------------------------------------------------------------------------------------|-----------------|--|
| 1069 1, | 63.               |                                                                                               | 762, 970, 177   |  |
|         | $4001 1, \ 1534,$ |                                                                                               | 568, 3095, 2544 |  |
|         |                   |                                                                                               |                 |  |
|         |                   | $15019$ , $10641$ , $2640$ , $6710$ , $784$<br>$71053$ , $33755$ , $65170$ , $12740$ , $6878$ |                 |  |

These we implemented using the shifted points  $k(\mathbf{v}-0.5)/n \pmod{1}$  as suggested in Fang and Wang [115], rather than  $(5.28)$ . We also tested Korobov rules from L'Ecuyer and Lemieux [226] generated by  $a = 331, 219, 1716, 7151,$ 665 and 5603 these cave rather poor and erratic results and are therefore

 $\mathcal{L}$ 

omitted from the figure. Using Monte Carlo, the RMSE scales exactly with  $\sqrt{n}$ , so we estimated it at  $n = 64000$  and then extended this value to other values of  $n$ .

Figure 5.14 suggests several observations. The QMC methods produce root mean square errors three to ten times smaller than those of Monte Carlo over the range of sample sizes considered. Faure points appear to outperform the lattice rules and Sobol' points outperform the Faure points. In addition to producing smaller errors, the QMC methods appear to converge at a faster rate than Monte Carlo: their graphs are not only lower, they have a steeper slope. For Sobol' and Faure points, a convergence rate close to  $O(1/n)$  (evidenced by a slope close to  $-1$ ) sets in after a few thousand points. The slope for Monte Carlo is exactly  $-1/2$  by construction.

![](_page_47_Figure_3.jpeg)

Fig. 5.14. Root mean square errors in pricing 500 options on the geometric mean of five underlying assets.

The relative smoothness of the convergence of the Faure and Sobol' approximations relies critically on our choice of favorable values of  $n$  for each method. For example, taking  $n = 9000$  produces larger RMS errors than  $n = 3125$  for the Faure sequence and larger than  $n = 4096$  for the Sobol' sequence. The various points plotted for lattice rules are unrelated to each other because each value of  $n$  uses a different generating vector, whereas the Sobol' and Faure results use initial segments of infinite sequences.

Figures  $5.15$  and  $5.16$  examine the effect of increasing problem dimension while keeping the number of points nearly fixed. Figure 5.15 is based on  $(5.33)$ with  $d = 10, 30, 40, 70, 100, \text{ and } 150$ . For this comparison we held the maturity T fixed at 0.25, let the strike K range from 94 to 102 in increments of 2, and let  $\sigma$  vary as before. Thus, we have fifty options for each value of d.

 $\sim$ 

Because increasing  $d$  in the geometric mean (5.33) has the effect of reducing the volatility of  $\bar{S}$ , the average option price decreases with d, dropping from 3.46 at  $d = 10$  to 1.85 at  $d = 150$ . Root mean square errors also decline, so to make the comparison more meaningful we look at relative errors. These increase with  $d$  for all three methods considered in Figure 5.15. The Monte Carlo results are estimated RMS relative errors for a sample size of 5000, but estimated from 64,000 replications. The Sobol' sequence results in all dimensions skip 4096 points and use  $n = 5120$ ; this is  $2^{12} + 2^{10}$  and should be favorable for a base-2 construction. For the Faure sequence, the base changes with dimension. For each d we chose a value of n near 5000 that should be favorable for the corresponding base: these values are  $4 \cdot 11^3$ ,  $5 \cdot 31^2 + 7 \cdot 31$ ,  $3 \cdot 41^2$ ,  $71^2$ ,  $50 \cdot 101$ , and  $34 \cdot 151$ . In each case, we skipped the first  $b^4$  points, with  $b$  the base. The figure suggests that the advantage of the QMC methods relative to Monte Carlo declines with increasing dimension but is still evident at  $d = 150$ .

![](_page_48_Figure_3.jpeg)

Fig. 5.15. Root mean square relative error in pricing options on the geometric average of  $d$  assets, with  $d$  the dimension.

The comparison in Figure 5.16 is similar but uses  $(5.34)$ , so d now indexes the number of averaging dates along the path of a single asset. For this comparison we fixed T at 0.25. we let K vary from 96 to 104 in increments of 2,

and let  $\sigma$  vary as before, to produce a total of fifty options. Each option price approaches a limit as  $d$  increases (the price associated with the continuous average), and the Monte Carlo RMSE is nearly constant across dimensions. The errors using Faure points show a sharp increase at  $d = 100$  and  $d = 150$ . The errors using Sobol' points show a much less severe dependence on dimension. The number of points used for all three methods are the same in Figure 5.16 as Figure  $5.15$ .

![](_page_49_Figure_2.jpeg)

Fig. 5.16. Root mean square error in pricing options on the geometric time-average of  $d$  values of a single asset, with  $d$  the dimension.

Without experimentation, it is difficult to know how many QMC points to use to achieve a desired accuracy. In ordinary Monte Carlo, one can use a standard error estimated from a modest number of replications to determine the number of replications to undertake in a second stage of sampling to reach a target precision. Some authors have proposed stopping rules for QMC based on monitoring fluctuations in the approximation — rules that stop once the fluctuations are smaller than the required error tolerance. But such procedures are risky, as illustrated in Figure 5.17. The figure plots the running average of the estimated price of an option on the geometric average of 30 assets (with  $T = 0.25$ ,  $\sigma = 0.45$ , and  $K = 100$ ) using Faure points. An automatic stopping rule would likely detect convergence — erroneously — near  $6000$ points or 13000 points where the average plateaus. But in both cases, the QMC approximation remains far from the true value, which is not crossed until after more than 19000 points. These results use Faure points from the start of the sequence (in base  $31$ ); skipping an initial portion of the sequence would reduce the severity of this problem but would not eliminate it.

![](_page_50_Figure_1.jpeg)

Fig. 5.17. Cumulative average approximation to a 30-dimensional option price using Faure points. The left panel magnifies the inset in the right panel. The approximation approaches the true value through plateaus that create the appearance of convergence.

Next we compare randomized QMC point sets using a random shift modulo 1 as in  $(5.32)$ . For this comparison we consider a single option — a call on the geometric average of five assets, with  $T = 0.25$ ,  $K = 100$ , and  $\sigma = 0.45$ . Because of the randomization, we can now compare methods based on their variances; these are displayed in Table 5.4. To compensate for differences in the cardinalities of the point sets, we report a product  $n\sigma^2$ , where n is the number of points in the set and  $\sigma^2$  is the variance of the average value of the integrand over a randomly shifted copy of the point set. This measure makes the performance of ordinary Monte Carlo independent of the choice of  $n$ .

For the Faure and Sobol' results, we generated each point set of size  $n$  by starting at the *n*th point in the sequence; each  $n$  is a power of the corresponding base. The lattice rules are the same as those used for Figure 5.14. For the Korobov rules we display the number of points and the multiplier  $a$ ; these values are from L'Ecuyer and Lemieux  $[226]$ .

All the QMC methods show far smaller variance than ordinary Monte Carlo. Sobol' points generally appear to produce the smallest variance, but the smallest variance overall corresponds to a lattice rule. The Korobov rules have larger variances than the other methods.

The numerical examples considered here suggest some general patterns: the QMC methods produce substantially more precise values than ordinary Monte Carlo; this holds even at rather small values of n, before  $O(1/n^{1-\epsilon})$ 

| Lattice |                  | $\text{Korobov}$                 |  |             | Faure |                 |                                               |                  | Sobol' Monte Carlo |  |
|---------|------------------|----------------------------------|--|-------------|-------|-----------------|-----------------------------------------------|------------------|--------------------|--|
|         | $n \; n\sigma^2$ | n(a)                             |  | $n\sigma^2$ |       | $n \ n\sigma^2$ |                                               | $n \; n\sigma^2$ | $n\sigma^2$        |  |
|         |                  |                                  |  |             |       | 125 11.9        | 128 5.9                                       |                  | 34.3               |  |
|         |                  | 1069 2.7 1021 (331) 2.7 3125 1.1 |  |             |       |                 | $1024 \quad 2.0$                              |                  | 34.3               |  |
|         |                  | 4001 0.6 4093 (219) 1.5          |  |             |       |                 | $4096 \quad 0.9$                              |                  | 34.3               |  |
|         |                  |                                  |  |             |       |                 | 15019 0.3 16381 (665) 3.5 15625 0.4 16384 0.4 |                  | 34.3               |  |

**Table 5.4.** Variance comparison for randomly shifted QMC methods and Monte Carlo.

convergence is evident; Sobol' points generally produce smaller errors than Faure points or lattice rules; the advantages of QMC persist even in rather high dimensions, especially for Sobol' points; randomized QMC point sets produce low-variance estimates.

The effectiveness of QMC methods in high-dimensional pricing problems runs counter to the traditional view that these methods are unsuitable in high dimensions. The traditional view is rooted in the convergence rate of  $O((\log n)^d/n)$ : if d is large then n must be *very* large for the denominator to overwhelm the numerator. The explanation for this apparent contradiction may lie in the structure of problems arising in finance — these highdimensional integrals might be well-approximated by much lower-dimensional integrals, a possibility we exploit in Section  $5.5.2$ .

Extrapolating from a limited set of examples (we have considered just one type of option and just one model of asset price dynamics) is risky, so we comment on results from other investigations. Accord et al.  $[4]$  and Boyle et al. [53] find that Sobol' points outperform Faure points and that both outperform ordinary Monte Carlo in comparisons similar to those reported here. Morland [270] reports getting better results with Sobol' points than Niederreiter points (of the type generated in Bratley, Fox, and Niederreiter  $[58]$ ). Joy et al.  $[204]$  test Faure sequences on several different types of options, including an HJM swaption pricing application, and find that they work well. Berman  $[45]$  compares methods on a broad range of options and models; he finds that Sobol' points give more precise results than ordinary Monte Carlo, but he also finds that with some simple variance reduction techniques the two methods perform very similarly. Paskov [295], Paskov and Traub [296], and Caflisch et al.  $[73]$  find that Sobol' points work well in pricing mortgagebacked securities formulated as 360-dimensional integrals. Papageorgiou and Traub [293] report improved results using a generalized Faure sequence and Ninomiya and Tezuka  $[283]$  report superior results for similar problems using a generalized Niederreiter sequence, but neither specifies the exact construction  $used.$ 

For the most part, these comparisons (like those presented here) pit QMC methods against only the simplest form of Monte Carlo. Variance reduction techniques can of course improve the precision of Monte Carlo estimates; they provide a mechanism for taking advantage of special features of a model to

a much greater extent than QMC. Indeed, the "black-box" nature of QMC methods is part of their appeal. As discussed in Section  $5.1.3$ , the ready availability of error information through confidence intervals is an advantage of Monte Carlo methods.

For calculations that need to be repeated often with only minor changes in parameters — for example, options that need to be priced every day this suggests the following approach: tailor a Monte Carlo method to the specific problem, using estimates of standard errors to compare algorithms, and determine the required sample size; once the problem and its solution are well understood, replace the random number generator with a quasi-Monte  $\text{Carlo generator.}$ 

### 5.5.2 Strategic Implementation

QMC methods have the potential to improve accuracy for a wide range of integration problems without requiring an integrand-specific analysis. There are, however, two ways in which the application of QMC methods can be tailored to a specific problem to improve performance:

- (i) changing the order in which coordinates of a sequence are assigned to arguments of an integrand;
- (ii) applying a change of variables to produce a more tractable integrand.

The first of these transformations is actually a special case of the second but it merits separate consideration.

The strategy in  $(i)$  is relevant when some coordinates of a low-discrepancy sequence exhibit better uniformity properties than others. This holds for Halton sequences (in which coordinates with lower bases are preferable) and for Sobol' sequences (in which coordinates generated by lower-degree polynomials are preferable), but not for Faure sequences. As explained in Section 5.2.2, all coordinates of a Faure sequence are equally well distributed. But the more general strategy in (ii) is potentially applicable to all QMC methods.

As a simple illustration of (ii), consider the function on  $[0,1)^5$  defined by

$$f(u_1, u_2, u_3, u_4, u_5) = \mathbf{1}\{|\Phi^{-1}(u_4)| + |\Phi^{-1}(u_5)| \le 2\sqrt{2}\},\$$

with  $\Phi^{-1}$  the inverse cumulative normal distribution. Although this reduces to a bivariate integrand, we have formulated it as a five-dimensional problem for purposes of illustration. The integral of this function is the probability that a pair of independent standard normal random variables fall in the square in  $\Re^2$  with vertices  $(0, \pm 2\sqrt{2})$  and  $(\pm 2\sqrt{2}, 0)$ , which is approximately 0.9111. Applying an orthogonal transformation to a pair of independent standard normal random variables produces another pair of independent standard normal random variables, so the same probability applies to the rotated square with vertices  $(\pm 2, \pm 2)$ . Thus, a change of variables transforms the integrand above  $\text{to}$ 

$$\tilde{f}(u_1, u_2, u_3, u_4, u_5) = \mathbf{1}\{\max(|\Phi^{-1}(u_4)|, |\Phi^{-1}(u_5)|) \le 2\}.$$

Figure 5.18 compares the convergence of QMC approximations to  $f$  (the dotted line) and  $f$  (the solid line) using a five-dimensional Faure sequence starting at the 625th point. In this example, the rotation has an evident impact on the quality of the approximation: after 3125 points, the integration error for f is nearly four times as large as the error for  $f$ . That a rotation could affect convergence in this way is not surprising in view of the orientation displayed by Faure sequences, as in, e.g., Figure  $5.3$ .

![](_page_53_Figure_3.jpeg)

**Fig. 5.18.** Both squares on the left have probability  $0.9111$  under the bivariate standard normal distribution. The right panel shows the convergence of QMC approximations for the probabilities of the two squares. The solid horizontal line shows the exact value.

### Assigning Coordinates

We proceed with an illustration of strategy (i) in which the form of the integrand is changed only through a permutation of its arguments. In the examples we considered in Section 5.5.1, the integrands are symmetric functions of their arguments because we took the underlying assets to be identical in  $(5.33)$  and we took the averaging dates to be equally spaced in  $(5.34)$ . Changing the assignment of coordinates to variables would therefore have no effect on the value of a  $\text{QMC}$  approximation.

To break the symmetry of the multi-asset option in Section  $5.5.1$ , we assign linearly increasing volatilities  $\sigma_i = i\sigma_1, i = 1, \ldots, d$ , to the d assets. We take the volatility of the  $i$ th asset as a rough measure of the importance of the  $i$ th coordinate (and continue to assume the assets are uncorrelated). With this interpretation, assigning the coordinates of a Sobol' sequence to the assets in reverse order should produce better results than assigning the *i*th coordinate to the  $i$ th asset.

To test this idea we take  $d = 30$ ; the degrees of the primitive polynomials generating the coordinates then increase from  $0$  to  $8$ . We compare straightforward application of Sobol' points with a reversed assignment of coordinates based on root mean square relative error. Given an average level of volatility  $\bar{\sigma}$ , we choose  $\sigma_1$  so that  $\bar{\sigma}^2 = (\sigma_1^2 + \cdots + \sigma_d^2)/d$ , with  $\sigma_i = i\sigma_1$ . We let  $\bar{\sigma}$  range from 0.21 to 0.66 in increments of 0.05, and we let  $K$  vary from 94 to 102 in increments of 2 to get the same fifty option values we used for Figure  $5.15$ .

Table 5.5 displays the resulting RMS relative errors. The first row shows the number of points  $n$ . We specifically avoided values of  $n$  equal to powers of 2 in order to further differentiate the coordinates of the sequence; this makes the convergence of both methods erratic. In this example the reversed assignment usually produces smaller errors, but not always.

|                                                                                  | 750 |                                                                 |  | $1500$ $2500$ $3500$ $5000$ $7500$ $10000$ $12000$ |  |  |
|----------------------------------------------------------------------------------|-----|-----------------------------------------------------------------|--|----------------------------------------------------|--|--|
| Sobol'                                                                           |     | $0.023$ $0.012$ $0.017$ $0.021$ $0.013$ $0.012$ $0.007$ $0.005$ |  |                                                    |  |  |
| $\text{Reverse} = 0.020 = 0.021 = 0.010 = 0.015 = 0.009 = 0.007 = 0.005 = 0.003$ |     |                                                                 |  |                                                    |  |  |

**Table 5.5.** RMS relative errors for options on the geometric average of 30 assets with linearly increasing volatilities. Top row gives the number points. Second row is based on assigning  $i$ th coordinate to  $i$ th asset; last row uses reversed assignment.

### Changing Variables

A general strategy for improving QMC approximations applies a change of variables to produce an integrand for which only a small number of arguments are "important" and then applies the lowest-indexed coordinates of a QMC sequence to those coordinates. Finding an effective transformation presents essentially the same challenge as finding good stratification variables, a topic treated in Section  $4.3.2$ . As is the case in stratified sampling, the Gaussian setting offers particular flexibility.

In the application of QMC to derivatives pricing, the integrand  $f$  subsumes the dynamics of underlying assets as well as the form of the derivative contract. In the absence of specific information about the payoff of a derivative, one might consider transformations tied to the asset dynamics.

A simple yet effective example of this idea is the combination of Sobol' sequences with the Brownian bridge construction of Brownian motion developed in Section 3.1. In a straightforward application of Sobol' points to the generation of Brownian paths, the  $i$ th coordinate of each point would be transformed to a sample from the standard normal distribution (using  $\Phi^{-1}$ ), and these would be scaled and summed using the random walk construction  $(3.2)$ . To the extent that the initial coordinates of a Sobol' sequence have uniformity superior to that of higher-indexed coordinates, this construction does a particularly good job of sampling the first few increments of the Brownian path.

However, many option contracts would be primarily sensitive to the *terminal* value of the Brownian path.

Through the Brownian bridge construction, the first coordinate of a Sobol' sequence determines the terminal value of the Brownian path, so this value should be particularly well distributed. Moreover, the first several coordinates of the Sobol' sequence determine the general shape of the Brownian path; the last few coordinates influence only the fine detail of the path, which is often less important. This combination of Sobol' points with the Brownian bridge construction was proposed by Moskowitz and Caflisch [273] and has been found by several authors (including Acworth et al. [4], Åkesson and Lehoczky  $[9]$ , and Caflisch et al.  $[73]$ ) to be highly effective in finance applications.

As discussed in Section 3.1, the principal components construction of a discrete Brownian path (or any other Gaussian vector) has an optimality property that maximizes the importance (in the statistical sense of explained variance) of any initial number of independent normals used to construct the vector. Though this property lacks a precise relation to discrepancy, it suggests a construction in which the *i*th coordinate of a Sobol' sequence is assigned to the *i*th principal component. Unlike the Brownian bridge construction, the principal components construction is applicable with any covariance matrix.

This construction was proposed and tested in Acworth et al. [4]. Tables 5.6 and 5.7 show some of their results. The tables report RMS relative errors comparing an ordinary application of Sobol' sequences with the Brownian bridge and principal components constructions. The errors are computed over 250 randomly generated problem instances as described in  $[4]$ . Table 5.6 reports results for barrier options and geometric average options on a single underlying asset. The results indicate that both the Brownian bridge (BB) and principal components  $(PC)$  constructions can produce substantial error reductions compared to straightforward application of Sobol' points in a random walk construction. This is particularly evident at smaller values of  $n$ .

Table 5.7 shows results for options on the geometric average of  $d$  assets. The Brownian bridge construction is inapplicable in this setting, so only an ordinary application of Sobol' points (using Cholesky factorization) and the principal components construction appear in the table. These methods are compared for uncorrelated assets and assets for which all correlations are  $0.3.$  In the case of uncorrelated assets, the principal components construction simply permutes the coordinates of the Sobol' sequence, assigning the *i*th coordinate to the asset with the *i*th largest volatility. This suggests that the differences between the two methods should be greater in the correlated case, and this is borne out by the results in the table.

Neither the Brownian bridge nor the principal components construction is tailored to a particular type of option payoff. Given additional information about a payoff, we could try to find still better changes of variables. As an example, consider again an option on the geometric mean of  $d$  uncorrelated assets. A standard simulation would map a point  $(u_1,\ldots,u_d) \in [0,1)^d$  to a value of the average  $\bar{S}$  in (5.33) by first mapping each  $u_i$  to  $\Phi^{-1}(u_i)$  and then

|  |  | 5.6 Concluding Remarks | 335 |
|--|--|------------------------|-----|
|--|--|------------------------|-----|

|                      |        | Barrier Options |             |        | $\text{Average Options}$ |             |  |  |
|----------------------|--------|-----------------|-------------|--------|--------------------------|-------------|--|--|
|                      | Sobol' | $\text{BB}$     | $\text{PC}$ | Sobol' | $\text{BB}$              | $\text{PC}$ |  |  |
| $d = 10, n = 1,250$  | 1.32   | 0.78            | 0.97        | 2.14   | 0.71                     | 0.32        |  |  |
| 5,000                | 0.75   | 0.41            | 0.49        | 0.18   | 0.24                     | 0.11        |  |  |
| 20,000               | 0.48   | 0.53            | 0.50        | 0.08   | 0.08                     | 0.02        |  |  |
| 80,000               | 0.47   | 0.47            | 0.47        | 0.03   | 0.03                     | 0.01        |  |  |
| $d = 50, n = 1,250$  | 7.10   | 1.14            | 1.18        | 4.24   | 0.53                     | 0.33        |  |  |
| 5,000                | 1.10   | 0.87            | 0.59        | 0.61   | 0.16                     | 0.11        |  |  |
| 20,000               | 0.30   | 0.25            | 0.31        | 0.24   | 0.05                     | 0.02        |  |  |
| 80,000               | 0.22   | 0.12            | 0.08        | 0.06   | 0.03                     | 0.01        |  |  |
| $d = 100, n = 1,250$ | 9.83   | 1.32            | 1.41        | 10.12  | 0.63                     | 0.33        |  |  |
| 5,000                | 1.70   | 0.91            | 0.46        | 1.27   | 0.18                     | 0.11        |  |  |
| 20,000               | 0.62   | 0.23            | 0.28        | 0.24   | 0.04                     | 0.02        |  |  |
| 80,000               | 0.19   | 0.09            | 0.11        | 0.05   | 0.03                     | 0.01        |  |  |

**Table 5.6.** RMS relative errors (in percent) for single-asset options with  $d$  steps per path and  $n$  paths, using three different constructions of the underlying Brownian paths.

setting

$$\bar{S} = \left(\prod_{i=1}^{d} S_i(0)\right)^{1/d} \exp\left(rT - \frac{T}{2d} \sum_{i=1}^{d} \sigma_i^2 + \frac{\sqrt{T}}{d} \sum_{i=1}^{d} \sigma_i \Phi^{-1}(u_i)\right).$$

However, a simple change of variables allows us to replace

$$\sum_{i=1}^d \sigma_i \Phi^{-1}(u_i) \quad \text{ with } \quad \sqrt{\sum_{i=1}^d \sigma_i^2 \Phi^{-1}(u_1)}.$$

This reduces the problem to a one-dimensional integral and uses the first coordinate  $u_1$  for that integration. This example is certainly not typical, but it illustrates the flexibility available to change variables, particularly for models driven by normal random variables. All of the examples of stratified sampling in Section  $4.3.2$  can similarly be applied as changes of variables for QMC methods. Further strategies for improving the accuracy of QMC methods are developed in Fox  $[127]$ .

## 5.6 Concluding Remarks

The preponderance of the experimental evidence amassed to date points to Sobol' sequences as the most effective quasi-Monte Carlo method for applications in financial engineering. They often produce more accurate results than other QMC and Monte Carlo methods, and they can be generated very quickly through the algorithms of Bratley and Fox [57] and Press et al. [299].

5 Quasi-Monte Carlo 336

|                      | $\text{Correlation } 0$ |             | Correlation $0.3$ |             |
|----------------------|-------------------------|-------------|-------------------|-------------|
|                      | Sobol'                  | $\text{PC}$ | Sobol'            | $\text{PC}$ |
| $d = 10, n = 1,250$  | 1.20                    | 1.01        | 1.03              | 0.23        |
| 5,000                | 0.37                    | 0.50        | 0.17              | 0.06        |
| 20,000               | 0.19                    | 0.20        | 0.06              | 0.02        |
| 80,000               | 0.06                    | 0.03        | 0.04              | 0.01        |
| $d = 50, n = 1,250$  | 3.55                    | 2.45        | 1.58              | 0.16        |
| 5,000                | 0.50                    | 0.34        | 0.21              | 0.05        |
| 20,000               | 0.18                    | 0.08        | 0.05              | 0.02        |
| 80,000               | 0.08                    | 0.04        | 0.04              | 0.01        |
| $d = 100, n = 1,250$ | 3.18                    | 3.59        | 2.15              | 0.16        |
| 5,000                | 0.53                    | 0.56        | 0.34              | 0.04        |
| 20,000               | 0.13                    | 0.10        | 0.06              | 0.02        |
| 80,000               | 0.07                    | 0.02        | 0.03              | 0.00        |

**Table 5.7.** RMS relative errors (in percent) for options on the geometric average of  $d$  assets using  $n$  paths.

Although QMC methods are based on a deterministic perspective, the performance of Sobol' sequences in derivatives pricing can often be improved through examination of the underlying stochastic model. Because the initial coordinates of a Sobol' sequence are more uniform than later coordinates, a strategic assignment of coordinates to sources of randomness can improve accuracy. The combination of Sobol's points with the Brownian bridge construction is an important example of this idea, but by no means the only one. The applications of stratified sampling in Section  $4.3.2$  provide further examples, because good directions for stratification are also good candidates for effective use of the best Sobol' coordinates.

One might consider applying methods from Chapter  $4 - a$  control variate, for example — in a QMC numerical integration. We prefer to take such combinations in the opposite order: first analyze a stochastic problem stochastically and use this investigation to find an effective variance reduction technique; then reformulate the variance-reduced simulation problem as an integration problem to apply QMC. Thus, one might develop an importance sampling technique and then implement it using QMC. It would be much more difficult to derive effective importance sampling methods of the type illustrated in Section 4.6 starting from a QMC integration problem.

Indeed, we view postponing the integration perspective as a good way to apply QMC techniques to stochastic problems more generally. The transformation to a Brownian bridge construction, for example, is easy to understand from a stochastic perspective but would be opaque if viewed as a change of variables for an integration problem. Also, the simple error estimates provided by Monte Carlo simulation are especially useful in developing and comparing algorithms. After finding a satisfactory algorithm one may apply QMC to try to further improve accuracy. This is particularly useful if similar problems need to be solved repeatedly, as is often the case in pricing applications. Randomized QMC methods make it possible to compute simple error estimates for QMC calculations and can sometimes reduce errors too.

The effectiveness of QMC methods in high-dimensional pricing problems cannot be explained by comparing the  $O(1/\sqrt{n})$  convergence of Monte Carlo with the  $O(1/n^{1-\epsilon})$  convergence of QMC because of the  $(\log n)^d$  factor subsumed by the  $\epsilon$ . An important part of the explanation must be that the main source of dimensionality in most finance problems is the number of time steps, and as the Brownian bridge and principal components constructions indicate, this may artificially inflate the nominal dimension. Recent work has identified abstract classes of integration problems for which QMC is provably effective in high dimensions because of the diminishing importance of higher dimensions; see Sloan and Wózniakowski [334] for a detailed analysis, Sloan [332] for an overview, and Larcher, Leobacher, and Scheicher [220] for an application of these ideas to the Brownian bridge construction. Owen [291] argues that the key requirement for the effectiveness of QMC in high dimensions is that the integrand be well-approximated by a sum of functions depending on a small number of variables each.
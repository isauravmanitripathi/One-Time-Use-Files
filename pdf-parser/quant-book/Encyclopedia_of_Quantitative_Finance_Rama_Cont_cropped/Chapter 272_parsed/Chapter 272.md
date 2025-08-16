# **Quasi-Monte Carlo Methods**

Many typical problems of modern computational finance can be rephrased mathematically as problems of calculating integrals with high-dimensional integration domains (see the section Applications to Computational Finance for several examples). In fact, the dimensions may very well be in the hundreds or even in the thousands. Very often in such finance problems the integrand will be quite complicated, so that the integral cannot be evaluated analytically and precisely. In such cases, one has to resort to *numerical integration*, that is, to a numerical scheme for the approximation of integrals.

High-dimensional numerical integration is a challenging problem. Classical methods for multidimensional numerical integration, namely Cartesian products of one-dimensional integration rules such as the trapezoidal rule and Simpson's rule (see [15]), work well only for dimensions up to three or four, or if the given high-dimensional integral can be reduced to a low-dimensional integral by analytic tricks. For most high-dimensional integrals arising in finance, the classical methods fail.

A more powerful approach to multidimensional numerical integration employs Monte Carlo methods. In a nutshell, a *Monte Carlo method* is a numerical method based on random sampling. A comprehensive treatment of Monte Carlo methods can be found in [20].

Monte Carlo methods for numerical integration can be explained in a straightforward manner. In many cases, by using suitable transformations, we can assume that the integration domain is an *s*-dimensional unit cube *I <sup>s</sup>* := [0*,* 1]*<sup>s</sup>*, so this is the situation on which we focus. We assume also that the integrand *f* is square integrable over *I <sup>s</sup>*. Then the *Monte Carlo approximation* for the integral is

$$\int_{I^s} f(\mathbf{u}) \, \mathrm{d} \mathbf{u} \approx \frac{1}{N} \sum_{n=1}^N f(\mathbf{x}_n) \tag{1}$$

where **x**1*,...,* **x***<sup>N</sup>* are independent random samples drawn from the uniform distribution on *I <sup>s</sup>*. In statistics, we approximate the expected value of a random variable by sample means. The law of large numbers guarantees that with probability 1 (i.e., for "almost all" sequences of sample points) we have

$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_n) = \int_{I^s} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} \tag{2}$$

and so the Monte Carlo method for numerical integration converges almost surely.

We can, in fact, be more precise about the error committed in the Monte Carlo approximation (1). It can be verified quite easily that the square of the error in equation (1) is, on the average over all samples of size *N*, equal to *σ*<sup>2</sup>*(f )N*<sup>−</sup>1, where *σ*<sup>2</sup>*(f )* is the variance of *f* . Thus, with overwhelming probability we have

$$\int_{I^{s}} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} - \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_{n}) = O(N^{-1/2}) \quad (3)$$

This means, very roughly, that if we want to compute the given integral with an error tolerance of the order 10<sup>−</sup>2, say, then we need about 104 sample points, and to reduce the error tolerance by one order of magnitude, we need to increase the sample size by a factor of about 100. An important fact here is that the convergence rate in equation (3) is independent of the dimension *s*, and this makes Monte Carlo methods attractive for high-dimensional problems.

Despite the initial appeal of Monte Carlo methods for numerical integration, there are several drawbacks of these methods: (i) it is difficult to generate truly random samples; (ii) Monte Carlo methods for numerical integration provide only probabilistic error bounds; and (iii) in many applications the convergence rate in equation (3) is considered too slow. Quasi-Monte Carlo (QMC) methods were introduced to address these concerns.

# **General Background on QMC Methods**

A *QMC method* is a deterministic version of a Monte Carlo method, in the sense that the random samples used in the implementation of a Monte Carlo method are replaced by *quasi-random points*, which are judiciously chosen deterministic points with good distribution properties. The general idea is that the Monte Carlo error bound (3) describes the average performance of integration points **x**1*,...,* **x***<sup>N</sup>* , and there should exist points that perform better than average. These are the quasi-random points we are seeking.

We again consider these methods in the context of numerical integration over an  $s$ -dimensional unit cube  $I^s = [0, 1]^s$ . The approximation scheme is the same as for the Monte Carlo method, namely

$$\int_{I^{s}} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} \approx \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_{n}) \tag{4}$$

but now  $\mathbf{x}_1, \ldots, \mathbf{x}_N$  are deterministic points in  $I^s$ . For such a deterministic numerical integration scheme we expect a deterministic error bound, and this is indeed provided by the Koksma–Hlawka inequality. It depends on the star discrepancy, a measure for the irregularity of distribution of a point set  $P$  consisting of  $\mathbf{x}_1, \ldots, \mathbf{x}_N \in I^s$ . For any Borel set  $M \subseteq I^s$ , let  $A(M; P)$  be the number of integers n, with  $1 \le n \le$ *N* such that  $\mathbf{x}_n$  ∈ *M*. We put

$$R(M;P) = \frac{A(M;P)}{N} - \lambda_s(M) \tag{5}$$

which is the difference between the relative frequency of the points of  $P$  in  $M$  and the s-dimensional Lebesgue measure  $\lambda_s(M)$  of M. If the points of P have a very uniform distribution over  $I^s$ , then the values of  $R(M; P)$  will be close to 0 for a reasonable collection of Borel sets, such as for all subintervals of  $I^s$ .

**Definition 1** The star discrepancy of the point set  $P$  is given by

$$D_N^* = D_N^*(P) = \sup_J |R(J;P)| \tag{6}$$

where the supremum is extended over all intervals  $J = \prod_{i=1}^{s} [0, u_i]$  with  $0 < u_i \le 1$  for  $1 \le i \le s$ .

#### Koksma-Hlawka Inequality

For any function  $f$  of bounded variation  $V(f)$  on  $I<sup>s</sup>$  in the sense of Hardy and Krause and any points  $\mathbf{x}_1,\ldots,\mathbf{x}_N\in[0,1)^s$ , we have

$$\left| \int_{I^s} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} - \frac{1}{N} \sum_{n=1}^N f(\mathbf{x}_n) \right| \le V(f) D_N^* \qquad (7)$$

where  $D_N^*$  is the star discrepancy of  $\mathbf{x}_1, \ldots, \mathbf{x}_N$ .

Note that  $V(f)$  is a measure for the oscillation of the function  $f$ . The precise definition of the variation

 $V(f)$  can be found in [49, p. 19]. For  $f(\mathbf{u}) =$  $f(u_1,\ldots,u_s)$ , a sufficient condition for  $V(f)$  $\infty$  is that the partial derivative  $\partial^s f/\partial u_1 \cdots \partial u_s$ be continuous on  $I^s$ . A detailed proof of the Koksma-Hlawka inequality is by Kuipers and Niederreiter [37, Section 2.5]. There are all types of variants of this inequality; see [46, 49, Section 2.2, 24].

A different kind of error bound for OMC integration was shown by Niederreiter [50]. It relies on the following concept.

**Definition 2** Let  $M$  be a nonempty collection of Borel sets in  $I^s$ . Then a point set P of elements of  $I^s$  is called  $(\mathcal{M}, \lambda_s)$ -uniform if  $R(M; P) = 0$  for all  $M \in \mathcal{M}$ .

Now let  $\mathcal{M} = \{M_1, \ldots, M_k\}$  be a partition of  $I^s$ into nonempty Borel subsets of  $I^s$ . For a bounded Lebesgue-integrable function  $f$  on  $I^s$  and for  $1 <$  $j \leq k$ , we put

$$G_j(f) = \sup_{\mathbf{u} \in M_j} f(\mathbf{u}), \quad g_j(f) = \inf_{\mathbf{u} \in M_j} f(\mathbf{u}) \quad (8)$$

Then for any  $(\mathcal{M}, \lambda_s)$ -uniform point set consisting of  $\mathbf{x}_1,\ldots,\mathbf{x}_N\in I^s$  we have the error bound

$$\left| \int_{I^{s}} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} - \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_{n}) \right|$$
  
$$\leq \sum_{j=1}^{k} \lambda_{s}(M_{j})(G_{j}(f) - g_{j}(f)) \tag{9}$$

An analog of the bound (9) holds, in fact, for numerical integration over any probability space (see [50]).

A family of QMC methods that is particularly suited for periodic integrands is formed by lattice rules. For a given dimension  $s > 1$ , consider the factor group  $\mathbb{R}^s/\mathbb{Z}^s$ , which is an abelian group under addition of residue classes. Let  $L/\mathbb{Z}^s$  be an arbitrary finite subgroup of  $\mathbb{R}^s/\mathbb{Z}^s$  and let  $\mathbf{x}_n + \mathbb{Z}^s$  with  $\mathbf{x}_n \in$  $[0, 1)^s$  for  $1 \le n \le N$  be the distinct residue classes making up the group  $L/\mathbb{Z}^s$ . The points  $\mathbf{x}_1,\ldots,\mathbf{x}_N$ form the integration points of an  $N$ -point lattice rule. This terminology stems from the fact that the subset  $L = \bigcup_{n=1}^{N} (\mathbf{x}_{n} + \mathbb{Z}^{s})$  of  $\mathbb{R}^{s}$  is an *s*-dimensional lattice. The dual lattice  $L^{\perp}$  of L is defined by

$$L^{\perp} = \{ \mathbf{h} \in \mathbb{Z}^s : \mathbf{h} \cdot \mathbf{x} \in \mathbb{Z} \text{ for all } \mathbf{x} \in L \} \tag{10}$$

where  $\mathbf{h} \cdot \mathbf{x}$  denotes the standard inner product of  $\mathbf{h}$ and **x**. For real numbers,  $\alpha > 1$  and  $C > 0$ , let  $\mathcal{E}^s_{\alpha}(C)$ be the class of all continuous periodic functions f on  $\mathbb{R}^s$  with period interval  $I^s$  and with Fourier coefficients  $\hat{f}(\mathbf{h})$  satisfying

$$|\hat{f}(\mathbf{h})| \leq Cr(\mathbf{h})^{-\alpha}$$
 for all nonzero  $\mathbf{h} \in \mathbb{Z}^s$  (11)

where for  $\mathbf{h} = (h_1, \ldots, h_s) \in \mathbb{Z}^s$ , we put

$$r(\mathbf{h}) = \prod_{i=1}^{s} \max(1, |h_i|) \tag{12}$$

Then it can be shown that with the notation above.

$$\max_{f \in \mathcal{E}_{\alpha}^{s}(C)} \left| \int_{I^{s}} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} - \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_{n}) \right|$$
$$= C \sum_{\mathbf{h} \in L^{\perp} \setminus \{\mathbf{0}\}} r(\mathbf{h})^{-\alpha} \tag{13}$$

Further analysis leads to the result that for any  $s \ge 2$  and  $N \ge 2$  there exists an s-dimensional Npoint lattice rule with an error bound of order  $O(N^{-\alpha}(\log N)^{c(\alpha,s)})$  for all  $f \in \mathcal{E}^s_\alpha(C)$ , where the exponent  $c(\alpha, s) > 0$  depends only on  $\alpha$  and s. Expository accounts of the theory of lattice rules are given in [49, Chapters 5, 71]. A more recent detailed discussion of lattice rules can be found in [25]. Algorithms for the construction of efficient lattice rules are presented, for example, in [16, 58, 72].

This article can present only a rough overview of OMC methods. For a full treatment of OMC methods, we refer to [49]. Developments from the invention of QMC methods in the early 1950s up to 1978 are covered in detail in the survey article [46].

### **Low-discrepancy Sequences**

The Koksma-Hlawka inequality leads to the conclusion that point sets with small star discrepancy guarantee small errors in QMC integration over  $I^s$ . This raises the question of how small we can make the star discrepancy of N points in  $I^s$  for fixed N and s. For any  $N \ge 2$  and  $s \ge 1$ , the least order of magnitude that can be achieved at present is

$$D_N^*(P) = O(N^{-1}(\log N)^{s-1}) \tag{14}$$

where the implied constant is independent of  $N$ . (Strictly speaking, one has to consider infinitely many values of  $N$ , that is, an infinite collection of point sets of increasing size, for this  $O$ -bound to make sense in a rigorous fashion, but this technicality is often ignored.) A point set  $P$  achieving equation (14) is called a *low-discrepancy point set*. The points in a low-discrepancy point set are an ideal form of quasirandom points. It is conjectured that the order of magnitude in equation  $(14)$  is best possible, that is, the star discrepancy of any  $N \ge 2$  points in  $I^s$  is at least of the order of magnitude  $N^{-1}(\log N)^{s-1}$ . This conjecture is proved for  $s = 1$  and  $s = 2$  (see [37, Sections  $2.1$  and  $2.21$ ).

A very useful concept is that of a *low-discrepancy sequence*, which is an infinite sequence  $S$  of points in  $I^s$  such that for all  $N > 2$  the star discrepancy  $D^*_N(S)$ of the first  $N$  terms of  $S$  satisfies

$$D_N^*(S) = O(N^{-1}(\log N)^s)$$
(15)

with an implied constant independent of  $N$ . It is conjectured that the order of magnitude in equation  $(15)$ is best possible, but in this case the conjecture has been verified only for  $s = 1$  (see [37, Section 2.2]).

Low-discrepancy sequences have several practical advantages. In the first place, if  $\mathbf{x}_1, \mathbf{x}_2, \ldots \in I^s$  is a low-discrepancy sequence and  $N \ge 2$  is an integer, then it is easily seen that the points

$$\mathbf{y}_n = \left(\frac{n-1}{N}, \mathbf{x}_n\right) \in I^{s+1}, \quad n = 1, \dots, N \quad (16)$$

form a low-discrepancy point set. Thus, if a lowdiscrepancy sequence has been constructed, then we immediately obtain arbitrarily large low-discrepancy point sets. Hence, in the following, we concentrate on the construction of low-discrepancy sequences. Furthermore, given a low-discrepancy sequence S and a budget of  $N$  integration points, we can simply use the first  $N$  terms of the sequence  $S$  to get a good QMC method. If later on we want to increase  $N$ to achieve a higher accuracy, we can do so while retaining the results of the earlier computation. This is an advantage of low-discrepancy sequences over low-discrepancy point sets.

It is clear from the Koksma-Hlawka inequality and equation  $(15)$  that if we apply QMC integration with an integrand  $f$  of bounded variation on  $I^s$  in the sense of Hardy and Krause and with the first  $N$  terms  $\mathbf{x}_1, \ldots, \mathbf{x}_N \in [0, 1)^s$  of a low-discrepancy sequence, then

$$\int_{I^{s}} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} - \frac{1}{N} \sum_{n=1}^{N} f(\mathbf{x}_{n}) = O(N^{-1} (\log N)^{s}) \tag{17}$$

This yields a significantly faster convergence rate than the convergence rate  $O(N^{-1/2})$  in equation (3). Thus, for many types of integrals, the OMC method will outperform the Monte Carlo method.

Over the years, various constructions of lowdiscrepancy sequences have been obtained. Historically, the first one was designed by Halton [23]. For integers  $b \ge 2$  and  $n \ge 1$ , let

$$n-1 = \sum_{j=0}^{\infty} a_j(n)b^j, \quad a_j(n) \in \{0, 1, \dots, b-1\}$$
(18)

be the digit expansion of  $n-1$  in base b. Then put

$$\phi_b(n) = \sum_{j=0}^{\infty} a_j(n) b^{-j-1} \tag{19}$$

Now let  $p_1 = 2, p_2 = 3, \ldots, p_s$  be the first s prime numbers. Then

$$\mathbf{x}_n = (\phi_{p_1}(n), \dots, \phi_{p_s}(n)) \in I^s, \quad n = 1, 2, \dots$$
(20)

is the *Halton sequence* in the bases  $p_1, \ldots, p_s$ . This sequence  $S$  satisfies

$$D_N^*(S) = O(N^{-1}(\log N)^s)$$
 (21)

for all  $N \geq 2$ , with an implied constant depending only on  $s$ . The standard software implementation of Halton sequences is that of Fox [21]. More sophisticated constructions of better low-discrepancy sequences are described in the following section.

#### Nets and $(T, s)$ -Sequences

Current methods of constructing low-discrepancy sequences rely on the following definition, which is a special case of Definition 2.

**Definition 3** Let  $s \ge 1$ ,  $b \ge 2$ , and  $0 \le t \le m$  be integers and let  $\mathcal{M}_{b,m,t}^{(s)}$  be the collection of all subintervals  $J$  of  $I^s$  of the form

$$J = \prod_{i=1}^{s} \left[ a_i b^{-d_i}, \quad (a_i + 1)b^{-d_i} \right) \tag{22}$$

with integers  $d_i \ge 0$  and  $0 \le a_i < b^{d_i}$  for  $1 \le i \le s$ and with  $\lambda_s(J) = b^{t-m}$ . Then an  $(\mathcal{M}_{b,m,t}^{(s)}, \lambda_s)$ -uniform point set consisting of  $b^m$  points in  $I^s$  is called a  $(t, m, s)$ -net in base b.

It is important to note that the smaller the value of  $t$  for given  $b$ ,  $m$ , and  $s$ , the larger the collection  $\mathcal{M}_{b,m,t}^{(s)}$  of intervals in Definition 3, and so the stronger the uniform point set property in Definition 2. Thus, the primary interest is in  $(t, m, s)$ -nets in base  $b$  with a small value of  $t$ .

There is an important sequence analog of Definition 3. Given a real number  $x \in [0, 1]$ , let

$$x = \sum_{j=1}^{\infty} z_j b^{-j}, \quad z_j \in \{0, 1, \dots, b-1\}$$
 (23)

be a *b*-adic expansion of *x*, where the case  $z_i = b - 1$ for all but finitely many  $j$  is allowed. For an integer  $m \ge 1$ , we define the truncation

$$[x]_{b,m} = \sum_{j=1}^{m} z_j b^{-j} \tag{24}$$

If  $\mathbf{x} = (x^{(1)}, \dots, x^{(s)}) \in I^s$  and the  $x^{(i)}, 1 < i < s$ , are given by prescribed  $b$ -adic expansions, then we define

$$[\mathbf{x}]_{b,m} = \left( \left[ x^{(1)} \right]_{b,m}, \dots, \left[ x^{(s)} \right]_{b,m} \right) \tag{25}$$

We write  $\mathbb{N}$  for the set of positive integers and  $\mathbb{N}_0$ for the set of nonnegative integers.

**Definition 4** Let  $s \ge 1$  and  $b \ge 2$  be integers and let  $\mathbf{T}: \mathbb{N} \to \mathbb{N}_0$  be a function with  $\mathbf{T}(m) \leq m$  for all  $m \in \mathbb{N}$ . Then a sequence  $\mathbf{x}_1, \mathbf{x}_2, \ldots$  of points in  $I^s$ is a  $(\mathbf{T}, s)$ -sequence in base b if for all  $k \in \mathbb{N}_0$  and  $m \in \mathbb{N}$ , the points  $[\mathbf{x}_n]_{b,m}$  with  $kb^m < n \leq (k+1)b^m$ form a  $(\mathbf{T}(m), m, s)$ -net in base b. If for some integer  $t > 0$ , we have  $\mathbf{T}(m) = m$  for  $m < t$  and  $\mathbf{T}(m) = t$  for  $m > t$ , then we speak of a  $(t, s)$ -sequence in base b.

A general theory of  $(t, m, s)$ -nets and  $(t, s)$ sequences was developed by Niederreiter [47]. The concept of a  $(\mathbf{T}, s)$ -sequence was introduced by Larcher and Niederreiter [40], with the variant in Definition 4 being due to Niederreiter and Özbudak [53]. Recent surveys of this topic are presented in [51, 52]. For a  $(t, s)$ -sequence in base b we have

$$D_{N}^{*}(S) = O(b^{t}N^{-1}(\log N)^{s}) \tag{26}$$

for all  $N > 2$ , where the implied constant depends only on b and s. Thus, any  $(t, s)$ -sequence is a lowdiscrepancy sequence.

The standard technique of constructing  $(T, s)$ sequences is the *digital method*. Fix a dimension  $s > 1$  and a base  $b > 2$ . Let R be a finite commutative ring with identity and of order  $b$ . Set up a map  $\rho: R^{\infty} \to [0, 1]$  by selecting a bijection  $\eta: R \to$  $\mathbb{Z}_b := \{0, 1, \ldots, b-1\}$  and putting

$$\rho(r_1, r_2, \ldots) = \sum_{j=1}^{\infty} \eta(r_j) b^{-j} \quad \text{for } (r_1, r_2, \ldots) \in R^{\infty}$$
(27)

Furthermore, choose  $\infty \times \infty$  matrices  $C^{(1)}, \ldots, C^{(s)}$ over  $R$  which are called *generating matrices*. For  $n = 1, 2, \dots$  let

$$n-1 = \sum_{j=0}^{\infty} a_j(n) b^j, \quad a_j(n) \in \mathbb{Z}_b \qquad (28)$$

be the digit expansion of  $n-1$  in base b. Choose a bijection  $\psi: \mathbb{Z}_b \to R$  with  $\psi(0) = 0$  and associate with  $n$  the sequence

$$\mathbf{n} = (\psi(a_0(n)), \psi(a_1(n)), \ldots) \in R^{\infty} \tag{29}$$

Then the sequence  $\mathbf{x}_1, \mathbf{x}_2, \ldots$  of points in  $I^s$  is defined by

$$\mathbf{x}_n = (\rho(\mathbf{n}C^{(1)}), \dots, \rho(\mathbf{n}C^{(s)})) \quad \text{for } n = 1, 2, \dots$$
(30)

Note that the products  $\mathbf{n}C^{(i)}$  are well defined since  $\mathbf{n}$  contains only finitely many nonzero terms. In practice, the ring  $R$  is usually chosen to be a finite field  $\mathbb{F}_q$  of order q, where q is a prime power. The success of the digital method depends on a careful choice of the generating matrices  $C^{(1)}, \ldots, C^{(s)}$ .

The first application of the digital method occurred in the construction of Sobol' sequences in [76]. This construction uses primitive polynomials over  $\mathbb{F}_2$  to set up the generating matrices  $C^{(1)}, \ldots, C^{(s)}$  and leads

to  $(t, s)$ -sequences in base 2. The wider family of irreducible polynomials was used in the construction of Niederreiter sequences in [48], and this construction works for arbitrary prime-power bases  $q$ . Let  $p_1, \ldots, p_s$  be the first s monic irreducible polynomials over  $\mathbb{F}_q$ , ordered according to nondecreasing degrees and put,

$$T_q(s) = \sum_{i=1}^{s} (\deg(p_i) - 1) \tag{31}$$

The construction of Niederreiter sequences yields  $(t, s)$ -sequences in base q with  $t = T<sub>q</sub>(s)$ . Let  $U(s)$ denote the least value of  $t$  that can be achieved by Sobol' sequences for given s. Then  $T_2(s) =$  $U(s)$  for  $1 \le s \le 7$  and  $T_2(s) < U(s)$  for all  $s \ge 8$ . Thus, according to equation (26), for all dimensions  $s \ge 8$  Niederreiter sequences in base 2 lead to a smaller upper bound on the star discrepancy than Sobol' sequences. Convenient software implementations of Sobol' and Niederreiter sequences are described in  $[8-10]$ .

The potentially smallest, and thus best,  $t$ -value for any  $(t, s)$ -sequence in base b would be  $t =$ 0. However, according to [49, Corollary 4.24], a necessary condition for the existence of a  $(0, s)$ sequence in base b is  $s \leq b$ . For primes p, a construction of  $(0, s)$ -sequences in base p for  $s \leq p$ was given by Faure [18]. For prime powers  $q$ , a construction of  $(0, s)$ -sequences in base  $q$  for  $s \le q$ was given by Niederreiter [47]. Since  $T_a(s) = 0$  for  $s \leq q$  by equation (31), the Niederreiter sequences in [48] also yield  $(0, s)$ -sequences in base q for  $s < q$ .

An important advance in the construction of lowdiscrepancy sequences was made in the mid-1990s with the design of *Niederreiter-Xing* sequences, which utilizes powerful tools from algebraic geometry and the theory of algebraic function fields and generalizes the construction of Niederreiter sequences. The basic articles here are [54, 83], and expository accounts of this work and further results are given in [55, 56, 57, Chapter 8]. Niederreiter-Xing sequences are  $(t, s)$ -sequences in a primepower base q with  $t = V_q(s)$ . Here,  $V_q(s)$  is a number determined by algebraic curves (or equivalently algebraic function fields) over  $\mathbb{F}_q$ , and we have  $V_q(s) \leq$  $T_q(s)$  for all  $s \ge 1$ . In fact, much more is true. If we fix q and consider  $V_q(s)$  and  $T_q(s)$  as functions of s, then  $V_q(s)$  is of the order of magnitude s, whereas  $T_q(s)$  is of the order of magnitude  $s \log s$ .

This yields an enormous improvement on the bound for the star discrepancy in equation (7). It is known that for any *(t, s)*-sequences in base *b* the parameter *t* must grow at least linearly with *s* for fixed *b* (see [55, Section 10]), and so Niederreiter–Xing sequences yield *t*-values of the optimal order of magnitude as a function of *s*. A software implementation of Niederreiter–Xing sequences is described in [68] and available at http://math.iit.edu/˜mcqmc/Software.html by following the appropriate links.

To illustrate the comparative quality of the above constructions of *(t, s)*-sequences, we consider the case of the most convenient base 2 and tabulate some values of *U (s)* for Sobol' sequences, of *T*2*(s)* for Niederreiter sequences, and of *V*2*(s)* for Niederreiter–Xing sequences in Table 1. Note that the values of *V*2*(s)* in Table 1 for 2 ≤ *s* ≤ 7 are the least values of *t* for which a *(t, s)*-sequence in base 2 can exist.

The approach by algebraic function fields was followed up recently by Mayor and Niederreiter [45] who gave an alternative construction of Niederreiter–Xing sequences using differentials of global function fields. Niederreiter and Ozbudak [53] obtain- ¨ ed the first improvement on Niederreiter–Xing sequences for some special pairs *(q, s)* of prime-power bases *q* and dimensions *s*. For instance, consider the case where *q* is an arbitrary prime power and *s* = *q* + 1. Then *Tq (q* + 1*)* = 1 by equation (8) and this is the least possible *t*-value for a *(t, q* + 1*)* sequence in base *q*. However, the construction in [53] yields a *(***T***, q* + 1*)*-sequence in base *q* with **T***(m)* = 0 for even *m* and **T***(m)* = 1 for odd *m*, which is even better.

We remark that all constructions mentioned in this section are based on the digital method. We note also that the extensive database at http://mint.sbg.ac.at is devoted to *(t, m, s)*-nets and *(t, s)*-sequences. In summary, for a given prime-power base *q*, the currently best low-discrepancy sequences are as follows: (i) the Faure or Niederreiter sequences (depending on whether *q* is prime or not) for all dimensions

**Table 1** Values of *U (s)*, *T*2*(s)*, and *V*2*(s)*

| s     | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | 10 | 15 | 20 |
|-------|---|---|---|---|---|----|----|----|----|----|----|
| U (s) | 0 | 1 | 3 | 5 | 8 | 11 | 15 | 19 | 23 | 45 | 71 |
| T2(s) | 0 | 1 | 3 | 5 | 8 | 11 | 14 | 18 | 22 | 43 | 68 |
| V2(s) | 0 | 1 | 1 | 2 | 3 | 4  | 5  | 6  | 8  | 15 | 21 |

*s* ≤ *q* and (ii) the Niederreiter–Xing sequences for all dimensions *s>q*, except for some special values of *s>q* where the Niederreiter–Ozbudak sequences ¨ are better. We emphasize that the bound (7) on the star discrepancy of *(t, s)*-sequences is completely explicit; see [49, Section 4.1] and a recent improvement in [36]. For the best *(t, s)*-sequences, the coefficient of the leading term *N*<sup>−</sup><sup>1</sup>*(*log *N )s* in the bound on the star discrepancy tends to 0 at a superexponential rate as *s* → ∞.

# **Effective Dimension**

In view of equation (6), the QMC method for numerical integration performs asymptotically better than the Monte Carlo method for any dimension *s*. However, in practical terms, the number *N* of integration points cannot be taken too large, and then already for moderate values of *s* the size of the factor *(*log *N )s* may wipe out the advantage over the Monte Carlo method. On the other hand, numerical experiments with many types of integrands have shown that even for large dimensions *s* the QMC method will often lead to a convergence rate *O(N*<sup>−</sup><sup>1</sup>*)* rather than *O(N*<sup>−</sup><sup>1</sup>*(*log *N )s )* as predicted by the theory, thus beating the Monte Carlo method by a wide margin. One reason may be that the Koksma–Hlawka inequality is in general overly pessimistic. Another explanation can sometimes be given by means of the nature of the integrand *f* . Even though *f* is a function of *s* variables, the influence of these variables could differ greatly. For numerical purposes, *f* may behave like a function of much fewer variables, so that the numerical integration problem is in essence a lowdimensional one with a faster convergence rate. This idea is captured by the notion of effective dimension.

We start with the ANOVA decomposition of a random variable *f (***u***)* = *f (u*1*,...,us)* on *I <sup>s</sup>* of finite variance. This decomposition amounts to writing *f* in the form

$$f(\mathbf{u}) = \sum_{K \subseteq \{1,\ldots,s\}} f_K(\mathbf{u}) \tag{32}$$

where *f*<sup>∅</sup> is the expected value of *f* and each *fK(***u***)* with *K* = ∅ depends only on the variables *ui* with *i* ∈ *K* and has expected value 0. Furthermore, *fK*<sup>1</sup> and *fK*<sup>2</sup> are orthogonal whenever *K*<sup>1</sup> = *K*2. Then the variance  $\sigma^2(f)$  of f decomposes as

$$\sigma^{2}(f) = \sum_{K \subseteq \{1,\dots,s\}} \sigma^{2}(f_{K}) \tag{33}$$

The following definition relates to this decomposition.

**Definition 5** Let d be an integer with  $1 < d < s$  and r a real number with  $0 < r < 1$ . Then the function  $f$  has effective dimension  $d$  at the rate  $r$  in the superposition sense if

$$\sum_{|K| \le d} \sigma^2(f_K) \ge r\sigma^2(f) \tag{34}$$

The function  $f$  has effective dimension  $d$  at the rate  $r$  in the truncation sense if

$$\sum_{K \subseteq \{1,\dots,d\}} \sigma^2(f_K) \ge r\sigma^2(f) \tag{35}$$

Values of r of practical interest are  $r = 0.95$  and  $r = 0.99$ , for instance. The formalization of the idea of effective dimension goes back to the articles of Caflisch et al. [13] and Hickernell [25]. There are many problems of high-dimensional numerical integration arising in computational finance for which the integrands have a relatively small effective dimension, one possible reason being discount factors, which render variables corresponding to distant time horizons essentially negligible. The classical example here is that of the valuation of mortgage-backed securities (see  $[13, 66]$ ). For further interesting work on the ANOVA decomposition and effective dimension, with applications to the pricing of Asian and barrier options, we refer to [32, 42, 43, 81].

A natural way of capturing the relative importance of variables is to attach weights to them. More generally, one may attach weights to any collection of variables, thus measuring the relative importance of all projections—and not just of the one-dimensional projections—of the given integrand. This leads then to a weighted version of the theory of QMC methods, an approach that was pioneered by Sloan and Woźniakowski [75].

Given a dimension s we consider the set  $\{1, \ldots, s\}$ of coordinate indices. To any nonempty subset  $K$  of  $\{1,\ldots,s\}$  we attach a weight  $\gamma_K \geq 0$ . To avoid a trivial case, we assume that not all weights are 0. Let  $\gamma$ denote the collection of all these weights  $\gamma_K$ . Then we

introduce the *weighted star discrepancy*  $D_{N,\nu}^*$ , which generalizes Definition 1. For  $\mathbf{u} = (u_1, \ldots, u_s) \in I^s$ , we abbreviate the interval  $\prod_{i=1}^{s} [0, u_i]$  by [0, u). For any nonempty  $K \subseteq \{1, \ldots, s\}$ , let  $\mathbf{u}_K$  denote the point in  $I^s$  with all coordinates whose indices are not in  $K$  replaced by 1. Now for a point set  $P$  consisting of N points from  $I^s$ , we define

$$D_{N,\gamma}^* = \sup_{\mathbf{u}\in I^s} \max_K \gamma_K |R([\mathbf{0},\mathbf{u}_K);P)| \qquad (36)$$

We recover the classical star discrepancy if we choose  $\gamma_{\{1,\dots,s\}} = 1$  and  $\gamma_K = 0$  for all nonempty proper subsets  $K$  of  $\{1, \ldots, s\}$ . With this weighted star discrepancy, one can then prove a weighted analog of the Koksma-Hlawka inequality (see [75]).

There are some special kinds of weights that are of great practical interest. In the case of *product weights*, one attaches a weight  $\eta_i$  to each  $i \in \{1, \ldots, s\}$  and puts

$$\gamma_K = \prod_{i \in K} \eta_i \quad \text{for all } K \subseteq \{1, \dots, s\}, \ K \neq \emptyset \quad (37)$$

In the case of *finite-order weights*, one chooses a threshold k and puts  $\gamma_K = 0$  for all K of cardinality larger than  $k$ .

The theoretical analysis of the performance of weighted QMC methods requires the introduction of weighted function spaces in which the integrands live. These can, for instance, be weighted Sobolev spaces or weighted Korobov spaces. In this context again, the weights reflect the relative importance of variables or collections of variables. The articles [38, 70, 75] are representative for this approach.

The analysis of the integration error utilizing weighted function spaces also leads to powerful results on tractability, a concept stemming from the theory of information-based complexity. The emphasis here is on the performance of multidimensional numerical integration schemes as a function not only of the number  $N$  of integration points but also of the dimension s as  $s \to \infty$ . Let  $\mathcal{F}_s$  be a Banach space of integrands f on  $I^s$  with norm  $|| f ||$ . Write

$$L_s(f) = \int_{I^s} f(\mathbf{u}) \, \mathrm{d}\mathbf{u} \qquad \text{for } f \in \mathcal{F}_s \tag{38}$$

Consider numerical integration schemes of the form

$$\mathcal{A}(f) = \sum_{n=1}^{N} a_n f(\mathbf{x}_n) \tag{39}$$

with real numbers *a*1*,...,aN* and points **x**1*,...,* **x***<sup>N</sup>* ∈ *I <sup>s</sup>*. The QMC method is of course a special case of such a scheme. For A as in equation (39), we write card*(*A*)* = *N*. Furthermore, we put

$$\operatorname{err}(\mathcal{A}, \mathcal{F}_s) = \sup_{\|f\| \le 1} |L_s(f) - \mathcal{A}(f)| \qquad (40)$$

For any *N* ≥ 1 and *s* ≥ 1, the *N*th minimal error of the *s*-dimensional numerical integration problem is defined by

$$\operatorname{err}(N, \mathcal{F}_s) = \inf \{ \operatorname{err}(\mathcal{A}, \mathcal{F}_s) : \mathcal{A} \text{ with } \operatorname{card}(\mathcal{A}) = N \}$$
(41)

The numerical integration problem is called *tractable* if there exist constants *C* ≥ 0, *e*<sup>1</sup> ≥ 0, and *e*<sup>2</sup> *>* 0 such that

$$\operatorname{err}(N, \mathcal{F}_s) \leq C s^{e_1} N^{-e_2} \|L_s\|_{\operatorname{op}}$$
  
for all  $N \geq 1, s \geq 1$  (42)

where *Ls* op is the operator norm of *Ls*. If, in addition, the exponent *e*<sup>1</sup> may be chosen to be 0, then the problem is said to be *strongly tractable*.

Tractability and strong tractability depend very much on the choice of the spaces F*s*. Weighted function spaces using product weights have proved particularly effective in this connection. Since the interest is in *s* → ∞, product weights are set up by choosing a sequence *η*1*, η*2*,...* of positive numbers and then, for fixed *s* ≥ 1, defining appropriate weights *γK* by equation (37). If the *ηi* tend to 0 sufficiently quickly as *i* → ∞, then in a Hilbert-space setting strong tractability can be achieved by QMC methods based on Halton, Sobol', or Niederreiter sequences (see [29, 79]). Further results on (strong) tractability as it relates to QMC methods can be found, for example, in [27, 28, 73, 74, 80, 82].

## **Randomized QMC**

Conventional QMC methods are fully deterministic and thus do not allow statistical error estimation as in Monte Carlo methods. However, one may introduce an element of randomness into a QMC method by randomizing (or "scrambling") the deterministic integration points used in the method. In this way, one can combine the advantages of QMC methods, namely faster convergence rates, and those of Monte Carlo methods, namely the possibility of error estimation.

Historically, the first scrambling scheme is *Cranley–Patterson rotation*, which was introduced in [14]. This scheme can be applied to any point set in *I <sup>s</sup>*. Let **x**1*,...,* **x***<sup>N</sup>* ∈ *I <sup>s</sup>* be given and put

$$\mathbf{y}_n = \{\mathbf{x}_n + \mathbf{r}\} \quad \text{for } n = 1, \dots, N \tag{43}$$

where **r** is a random vector uniformly distributed over *I <sup>s</sup>* and {·} denotes reduction modulo 1 in each coordinate of a point in *<sup>s</sup>* . This scheme transforms low-discrepancy point sets into low-discrepancy point sets.

A sophisticated randomization of *(t, m, s)*-nets and *(t, s)*-sequences is provided by *Owen scrambling* (see [60]). This scrambling scheme works with mutually independent random permutations of the digits in the *b*-adic expansions of the coordinates of all points in a *(t, m, s)*-net in base *b* or a *(t, s)*-sequence in base *b*. The scheme is set up in such a way that the scrambled version of a *(t, m, s)*-net, respectively *(t, s)*-sequence, in base *b* is a *(t, m, s)*-net, respectively *(t, s)*-sequence, in base *b* with probability 1. Further investigations of this scheme, particularly regarding the resulting mean square discrepancy and variance, were carried out, for example, by Hickernell and Hong [26], Hickernell and Yue [30], and Owen [61–63].

Since Owen scrambling is quite time consuming, various faster special versions have been proposed, such as a method of Matousek [44] and the method ˇ of *digital shifts* in which the permutations in Owen scrambling are additive shifts modulo *b* and the shift parameters may depend on the coordinate index *i* ∈ {1*,...,s*} and on the position of the digit in the digit expansion of the coordinate. In the binary case *b* = 2, digital shifting amounts to choosing *s* infinite bit strings **B**1*,...,* **B***<sup>s</sup>* and then taking each point **x***<sup>n</sup>* of the given *(t, m, s)*-net or *(t, s)*-sequence in base 2 and bitwise XORing the binary expansion of the *i*th coordinate of **x***<sup>n</sup>* with **B***<sup>i</sup>* for 1 ≤ *i* ≤ *s*. Digital shifts and their applications are discussed, for example, in [17, 41]. The latter article presents also a general survey of randomized QMC methods and stresses the interpretation of these methods as variance reduction techniques.

Convenient scrambling schemes are also obtained by operating on the generating matrices of *(t, m, s)* nets and *(t, s)*-sequences constructed by the digital method. The idea is to multiply the generating matrices by suitable random matrices from the left or from the right in such a way that the value of the parameter *t* is preserved. We refer to [19, 64] for such scrambling schemes. Software implementations of randomized low-discrepancy sequences are described in [22, 31] and are integrated into the Java library SSJ available at http://www.iro.umontreal.ca/∼simardr/ssj, which contains also many other simulation tools.

## **Applications to Computational Finance**

The application of Monte Carlo methods to challenging problems in computational finance was pioneered by Boyle [3] in 1977. Although QMC methods were already known at that time, they were not applied to computational finance because it was thought that they would be inefficient for problems involving the high dimensions occurring in this area.

A breakthrough came in the early 1990s when Paskov and Traub applied QMC integration to the problem of pricing a 30-year collateralized mortgage obligation provided by Goldman Sachs; see [67] for a report on this work. This problem required the computation of 10 integrals of dimension 360 each, and the results were astounding. For the hardest of the 10 integrals, the QMC method achieved accuracy 10<sup>−</sup><sup>2</sup> with just 170 points, whereas the Monte Carlo method needed 2700 points for the same accuracy. When higher accuracy is desired, the QMC method can be about 1000 times faster than the Monte Carlo method. For further work on the pricing of mortgagebacked securities, we refer to [13, 66, 78].

Applications of QMC methods to option pricing were first considered in the technical report of Birge [2] and the article of Joy *et al.* [35]. These works concentrated on European and Asian options. In the case of path-dependent options, if the security's terminal value depends only on the prices at *s* intermediate times, then after discretization the expected discounted payoff under the risk-neutral measure can be converted into an integral over the *s*-dimensional unit cube *I <sup>s</sup>*. For instance, in [35] an Asian option with 53 time steps is studied numerically.

A related problem in which an *s*-dimensional integral arises is the pricing of a multiasset option with *s* assets; see [1] in which numerical experiments comparing Monte Carlo and QMC methods are reported for dimensions up to *s* = 100. This article also discusses Brownian bridge constructions for option pricing. Related work on the pricing of multiasset European-style options using QMC and randomized QMC methods was carried out in [39, 69, 77], and comparative numerical experiments for Asian options can be found in [4, 59]. Jiang [33] gave a detailed error analysis of the pricing of Europeanstyle options using QMC methods, which is based on a variant of the bound (3) and requires only minimal smoothness assumptions.

Owing to its inherent difficulty, it took much longer for Monte Carlo and QMC methods to be applied to the problem of pricing American options. An excellent survey of early work on Monte Carlo methods for pricing American options is presented in [4]. The first important idea in this context was the *bundling algorithm* in which paths in state space for which the stock prices behave in a similar way are grouped together in the simulation. Initially, the bundling algorithm was applicable only to single-asset American options. Jin *et al.* [34] recently extended the bundling algorithm in order to price high-dimensional American-style options, and they also showed that computing representative states by a QMC method improves the performance of the algorithm.

Another approach to pricing American options by simulation is the *stochastic mesh method*. The choice of mesh density functions at each discrete time step is crucial for the success of this method. The standard mesh density functions are mixture densities, and so in a Monte Carlo approach one can use known techniques for generating random samples from mixture densities. In a QMC approach, these random samples are replaced by deterministic points whose empirical distribution function is close to the target distribution function. Work on the latter approach was carried out by Boyle, Kolkiewicz, and Tan [5–7] and Broadie *et al.* [11]. Another application of QMC methods to the pricing of American options occurs in *regression-based methods*, which are typically leastsquares Monte Carlo methods. Here Caflisch and Chaudhary [12] have shown that QMC versions improve the performance of such methods.

We conclude by mentioning two more applications of QMC methods to computational finance, namely by Papageorgiou and Paskov [65] to value-at-risk computations and by Jiang [33] to the pricing of interest-rate derivatives in a LIBOR market model.

## **References**

- [1] Acworth, P., Broadie, M. & Glasserman, P. (1998). A comparison of some Monte Carlo and quasi Monte Carlo techniques for option pricing, in *Monte Carlo and Quasi-Monte Carlo Methods 1996*, H. Niederreiter, P. Hellekalek, G. Larcher & P. Zinterhof, eds, Springer, New York, pp. 1–18.
- [2] Birge, J.R. (1994). Quasi-Monte Carlo approaches to option pricing, Technical report 94–19, Department of Industrial and Operations Engineering, University of Michigan, Ann Arbor, MI.
- [3] Boyle, P.P. (1977). Options: a Monte Carlo approach, *Journal of Financial Economics* **4**, 323–338.
- [4] Boyle, P., Broadie, M. & Glasserman, P. (1997). Monte Carlo methods for security pricing, *Journal of Economic Dynamics and Control* **21**, 1267–1321.
- [5] Boyle, P.P., Kolkiewicz, A.W. & Tan, K.S. (2001). Valuation of the reset options embedded in some equitylinked insurance products, *North American Actuarial Journal* **5**(3), 1–18.
- [6] Boyle, P.P., Kolkiewicz, A.W. & Tan, K.S. (2002). Pricing American derivatives using simulation: a biased low approach, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 181–200.
- [7] Boyle, P.P., Kolkiewicz, A.W. & Tan, K.S. (2003). An improved simulation method for pricing highdimensional American derivatives, *Mathematics and Computers in Simulation* **62**, 315–322.
- [8] Bratley, P. & Fox, B.L. (1988). Algorithm 659: implementing Sobol's quasirandom sequence generator, *ACM Transactions on Mathematical Software* **14**, 88–100.
- [9] Bratley, P., Fox, B.L. & Niederreiter, H. (1992). Implementation and tests of low-discrepancy sequences, *ACM Transactions on Modeling and Computer Simulation* **2**, 195–213.
- [10] Bratley, P., Fox, B.L. & Niederreiter, H. (1994). Algorithm 738: programs to generate Niederreiter's lowdiscrepancy sequences, *ACM Transactions on Mathematical Software* **20**, 494–495.
- [11] Broadie, M., Glasserman, P. & Ha, Z. (2000). Pricing American options by simulation using a stochastic mesh with optimized weights, in *Probabilistic Constrained Optimization: Methodology and Applications*, S.P. Uryasev, ed, Kluwer Academic Publishers, Dordrecht, pp. 26–44.
- [12] Caflisch, R.E. & Chaudhary, S. (2004). Monte Carlo simulation for American options, in *A Celebration of Mathematical Modeling*, D. Givoli, M.J. Grote & G.C. Papanicolaou, eds, Kluwer Academic Publishers, Dordrecht, pp. 1–16.
- [13] Caflisch, R.E., Morokoff, M. & Owen, A. (1997). Valuation of mortgage-backed securities using Brownian

bridges to reduce effective dimension, *The Journal of Computational Finance* **1**, 27–46.

- [14] Cranley, R. & Patterson, T.N.L. (1976). Randomization of number theoretic methods for multiple integration, *SIAM Journal on Numerical Analysis* **13**, 904–914.
- [15] Davis, P.J. & Rabinowitz, P. (1984). *Methods of Numerical Integration*, 2nd Edition, Academic Press, New York.
- [16] Dick, J. & Kuo, F.Y. (2004). Constructing good lattice rules with millions of points, in *Monte Carlo and Quasi-Monte Carlo Methods 2002*, H. Niederreiter, ed, Springer, Berlin, pp. 181–197.
- [17] Dick, J. & Pillichshammer, F. (2005). Multivariate integration in weighted Hilbert spaces based on Walsh functions and weighted Sobolev spaces, *Journal of Complexity* **21**, 149–195.
- [18] Faure, H. (1982). Discrepance de suites associ ´ ees ´ a` un systeme de num ` eration (en dimension ´ *s*), *Acta Arithmetica* **41**, 337–351.
- [19] Faure, H. & Tezuka, S. (2002). Another random scrambling of digital *(t, s)*-sequences, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 242–256.
- [20] Fishman, G.S. (1996). *Monte Carlo: Concepts, Algorithms, and Applications*, Springer, New York.
- [21] Fox, B.L. (1986). Algorithm 647: implementation and relative efficiency of quasirandom sequence generators, *ACM Transactions on Mathematical Software* **12**, 362–376.
- [22] Friedel, I. & Keller, A. (2002). Fast generation of randomized low-discrepancy point sets, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 257–273.
- [23] Halton, J.H. (1960). On the efficiency of certain quasi-random sequences of points in evaluating multidimensional integrals, *Numerische Mathematik* **2**, 84–90, 196.
- [24] Hickernell, F.J. (1998). A generalized discrepancy and quadrature error bound, *Mathematics of Computation* **67**, 299–322.
- [25] Hickernell, F.J. (1998). Lattice rules: how well do they measure up? in *Random and Quasi-Random Point Sets*, P. Hellekalek & G. Larcher, eds, Springer, New York, pp. 109–166.
- [26] Hickernell, F.J. & Hong, H.S. (1999). The asymptotic efficiency of randomized nets for quadrature, *Mathematics of Computation* **68**, 767–791.
- [27] Hickernell, F.J., Sloan, I.H. & Wasilkowski, G.W. (2004). On tractability of weighted integration for certain Banach spaces of functions, in *Monte Carlo and Quasi-Monte Carlo Methods 2002*, H. Niederreiter, ed, Springer, Berlin, pp. 51–71.
- [28] Hickernell, F.J., Sloan, I.H. & Wasilkowski, G.W. (2004). The strong tractability of multivariate integration using lattice rules, in *Monte Carlo and Quasi-Monte Carlo Methods 2002*, H. Niederreiter, ed, Springer, Berlin, pp. 259–273.

- [29] Hickernell, F.J. & Wang, X.Q. (2002). The error bounds and tractability of quasi-Monte Carlo algorithms in infinite dimension, *Mathematics of Computation* **71**, 1641–1661.
- [30] Hickernell, F.J. & Yue, R.-X. (2001). The mean square discrepancy of scrambled *(t, s)*-sequences, *SIAM Journal on Numerical Analysis* **38**, 1089–1112.
- [31] Hong, H.S. & Hickernell, F.J. (2003). Algorithm 823: implementing scrambled digital sequences, *ACM Transactions on Mathematical Software* **29**, 95–109.
- [32] Imai, J. & Tan, K.S. (2004). Minimizing effective dimension using linear transformation, in *Monte Carlo and Quasi-Monte Carlo Methods 2002*, H. Niederreiter, ed, Springer, Berlin, pp. 275–292.
- [33] Jiang, X.F. (2007). *Quasi-Monte Carlo methods in finance*. Ph.D. dissertation, Northwestern University, Evanston, IL.
- [34] Jin, X., Tan, H.H. & Sun, J.H. (2007). A state-space partitioning method for pricing high-dimensional Americanstyle options, *Mathematical Finance* **17**, 399–426.
- [35] Joy, C., Boyle, P.P. & Tan, K.S. (1996). Quasi-Monte Carlo methods in numerical finance, *Management Science* **42**, 926–938.
- [36] Kritzer, P. (2006). Improved upper bounds on the star discrepancy of *(t, m, s)*-nets and *(t, s)*-sequences, *Journal of Complexity* **22**, 336–347.
- [37] Kuipers, L. & Niederreiter, H. (1974). *Uniform Distribution of Sequences*, Wiley, New York. Reprint by Dover Publications, Mineola, NY, 2006.
- [38] Kuo, F.Y. (2003). Component-by-component constructions achieve the optimal rate of convergence for multivariate integration in weighted Korobov and Sobolev spaces, *Journal of Complexity* **19**, 301–320.
- [39] Lai, Y.Z. & Spanier, J. (2000). Applications of Monte Carlo/quasi-Monte Carlo methods in finance: option pricing, in *Monte Carlo and Quasi-Monte Carlo Methods 1998*, H. Niederreiter & J. Spanier, eds, Springer, Berlin, pp. 284–295.
- [40] Larcher, G. & Niederreiter, H. (1995). Generalized *(t, s)*-sequences, Kronecker-type sequences, and diophantine approximations of formal Laurent series, *Transactions of the American Mathematical Society* **347**, 2051–2073.
- [41] L'Ecuyer, P. & Lemieux, C. (2002). Recent advances in randomized quasi-Monte Carlo methods, in *Modeling Uncertainty: An Examination of Stochastic Theory, Methods, and Applications*, M. Dror, P. L'Ecuyer & F. Szidarovszky, eds, Kluwer Academic Publishers, Boston, pp. 419–474.
- [42] Lemieux, C. & Owen, A.B. (2002). Quasi-regression and the relative importance of the ANOVA components of a function, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 331–344.
- [43] Liu, R.X. & Owen, A.B. (2006). Estimating mean dimensionality of analysis of variance decompositions, *Journal of the American Statistical Association* **101**, 712–721.

- [44] Matousek, J. (1998). On the ˇ *L*2-discrepancy for anchored boxes, *Journal of Complexity* **14**, 527–556.
- [45] Mayor, D.J.S. & Niederreiter, H. (2007). A new construction of *(t, s)*-sequences and some improved bounds on their quality parameter, *Acta Arithmetica* **128**, 177–191.
- [46] Niederreiter, H. (1978). Quasi-Monte Carlo methods and pseudo-random numbers, *Bulletin of the American Mathematical Society* **84**, 957–1041.
- [47] Niederreiter, H. (1987). Point sets and sequences with small discrepancy, *Monatshefte f¨ur Mathematik* **104**, 273–337.
- [48] Niederreiter, H. (1988). Low-discrepancy and lowdispersion sequences, *Journal of Number Theory* **30**, 51–70.
- [49] Niederreiter, H. (1992). *Random Number Generation and Quasi-Monte Carlo Methods*, SIAM, Philadelphia.
- [50] Niederreiter, H. (2003). Error bounds for quasi-Monte Carlo integration with uniform point sets, *Journal of Computational and Applied Mathematics* **150**, 283–292.
- [51] Niederreiter, H. (2005). Constructions of *(t, m, s)*-nets and *(t, s)*-sequences, *Finite Fields and Their Applications* **11**, 578–600.
- [52] Niederreiter, H. (2008). Nets, *(t, s)*-sequences, and codes, in *Monte Carlo and Quasi-Monte Carlo Methods 2006*, A. Keller, S. Heinrich & H. Niederreiter, eds, Springer, Berlin, pp. 83–100.
- [53] Niederreiter, H. & Ozbudak, F. (2007). Low-discrepancy ¨ sequences using duality and global function fields, *Acta Arithmetica* **130**, 79–97.
- [54] Niederreiter, H. & Xing, C.P. (1996). Low-discrepancy sequences and global function fields with many rational places, *Finite Fields and Their Applications* **2**, 241–273.
- [55] Niederreiter, H. & Xing, C.P. (1996). Quasirandom points and global function fields, in *Finite Fields and Applications*, S. Cohen & H. Niederreiter, eds, Cambridge University Press, Cambridge, pp. 269–296.
- [56] Niederreiter, H. & Xing, C.P. (1998). Nets, *(t, s)* sequences, and algebraic geometry, in *Random and Quasi-Random Point Sets*, P. Hellekalek & G. Larcher, eds, Springer, New York, pp. 267–302.
- [57] Niederreiter, H. & Xing, C.P. (2001). *Rational Points on Curves over Finite Fields: Theory and Applications*, Cambridge University Press, Cambridge.
- [58] Nuyens, D. & Cools, R. (2006). Fast algorithms for component-by-component construction of rank-1 lattice rules in shift-invariant reproducing kernel Hilbert spaces, *Mathematics of Computation* **75**, 903–920.
- [59] Okten, G. & Eastman, W. (2004). Randomized quasi- ¨ Monte Carlo methods in pricing securities, *Journal of Economic Dynamics and Control* **28**, 2399–2426.
- [60] Owen, A.B. (1995). Randomly permuted *(t, m, s)*-nets and *(t, s)*-sequences, in *Monte Carlo and Quasi-Monte Carlo Methods in Scientific Computing*, H. Niederreiter & P.J.-S. Shiue, eds, Springer, New York, pp. 299–317.

- [61] Owen, A.B. (1997). Monte Carlo variance of scrambled net quadrature, *SIAM Journal on Numerical Analysis* **34**, 1884–1910.
- [62] Owen, A.B. (1997). Scrambled net variance for integrals of smooth functions, *The Annals of Statistics* **25**, 1541–1562.
- [63] Owen, A.B. (1998). Scrambling Sobol' and Niederreiter-Xing points, *Journal of Complexity* **14**, 466–489.
- [64] Owen, A.B. (2003). Variance with alternative scramblings of digital nets, *ACM Transactions on Modeling and Computer Simulation* **13**, 363–378.
- [65] Papageorgiou, A. & Paskov, S. (1999). Deterministic simulation for risk management, *Journal of Portfolio Management* **25**(5), 122–127.
- [66] Paskov, S.H. (1997). New methodologies for valuing derivatives, in *Mathematics of Derivative Securities*, M.A.H. Dempster & S.R. Pliska, eds, Cambridge University Press, Cambridge, pp. 545–582.
- [67] Paskov, S.H. & Traub, J.F. (1995). Faster valuation of financial derivatives, *Journal of Portfolio Management* **22**(1), 113–120.
- [68] Pirsic, G. (2002). A software implementation of Niederreiter-Xing sequences, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 434–445.
- [69] Ross, R. (1998). Good point methods for computing prices and sensitivities of multi-asset European style options, *Applied Mathematical Finance* **5**, 83–106.
- [70] Sloan, I.H. (2002). QMC integration—beating intractability by weighting the coordinate directions, in *Monte Carlo and Quasi-Monte Carlo Methods 2000*, K.T. Fang, F.J. Hickernell & H. Niederreiter, eds, Springer, Berlin, pp. 103–123.
- [71] Sloan, I.H. & Joe, S. (1994). *Lattice Methods for Multiple Integration*, Oxford University Press, Oxford.
- [72] Sloan, I.H., Kuo, F.Y. & Joe, S. (2002). Constructing randomly shifted lattice rules in weighted Sobolev spaces, *SIAM Journal on Numerical Analysis* **40**, 1650–1665.
- [73] Sloan, I.H., Kuo, F.Y. & Joe, S. (2002). On the stepby-step construction of quasi-Monte Carlo integration rules that achieve strong tractability error bounds in

weighted Sobolev spaces, *Mathematics of Computation* **71**, 1609–1640.

- [74] Sloan, I.H., Wang, X.Q. & Wozniakowski, H. (2004). ´ Finite-order weights imply tractability of multivariate integration, *Journal of Complexity* **20**, 46–74.
- [75] Sloan, I.H. & Wozniakowski, H. (1998). When are quasi- ´ Monte Carlo algorithms efficient for high dimensional integrals? *Journal of Complexity* **14**, 1–33.
- [76] Sobol', I.M. (1967). Distribution of points in a cube and approximate evaluation of integrals, *USSR Computational Mathematics and Mathematical Physics* **7**(4), 86–112.
- [77] Tan, K.S. & Boyle, P.P. (2000). Applications of randomized low discrepancy sequences to the valuation of complex securities, *Journal of Economic Dynamics and Control* **24**, 1747–1782.
- [78] Tezuka, S. (1998). Financial applications of Monte Carlo and quasi-Monte Carlo methods, in *Random and Quasi-Random Point Sets*, P. Hellekalek & G. Larcher, eds, Springer, New York, pp. 303–332.
- [79] Wang, X.Q. (2002). A constructive approach to strong tractability using quasi-Monte Carlo algorithms, *Journal of Complexity* **18**, 683–701.
- [80] Wang, X.Q. (2003). Strong tractability of multivariate integration using quasi-Monte Carlo algorithms, *Mathematics of Computation* **72**, 823–838.
- [81] Wang, X.Q. & Sloan, I.H. (2005). Why are highdimensional finance problems often of low effective dimension? *SIAM Journal on Scientific Computing* **27**, 159–183.
- [82] Wozniakowski, H. (2000). Efficiency of quasi-Monte ´ Carlo algorithms for high dimensional integrals, in *Monte Carlo and Quasi-Monte Carlo Methods 1998*, H. Niederreiter & J. Spanier, eds, Springer, Berlin, pp. 114–136.
- [83] Xing, C.P. & Niederreiter, H. (1995). A construction of low-discrepancy sequences using global function fields, *Acta Arithmetica* **73**, 87–102.

HARALD NIEDERREITER
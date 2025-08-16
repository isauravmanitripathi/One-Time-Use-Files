# **Ouantization Methods**

The origin of optimal vector quantization goes back to the early  $1950s$  as a way to discretize a (stationary) signal so that it could be transmitted for a given cost with the lowest possible degradation. The starting idea is to consider the best approximation in the mean quadratic sense—or, more generally, in an  $L^p$ -sense—of an  $\mathbb{R}^d$ -valued random vector X by a random variable  $q(X)$  taking at most N values (with respect to a given norm on  $\mathbb{R}^d$ , usually the canonical Euclidean norm).

More recently (in the late 1990s), it has been introduced as an efficient tool in numerical probability—first, for numerical integration in medium dimensions [15, 16], and soon as a method for the computation of conditional expectations. The main motivation was the pricing and hedging of multiasset American-style options [2, 4] and more generally to devise some realistic numerical schemes for the reflected backward stochastic differential equations (SDEs) (see Backward Stochastic Differen**tial Equations** and  $[1, 3]$ ). Presently, this ability to compute conditional expectations has led to tackling other nonlinear problems like stochastic control (portfolio management [18], pricing of swing options [5, 6]), nonlinear filtering with some applications to stochastic volatility models [20], and some classes of stochastic partial differential equations (PDEs) like stochastic Zakai and McKean-Vlasov equations [8]. In all these problems, quantization is used to produce a space discretization of the underlying (Markov) dynamics at the time discretization instants (see also [19]).

# **Optimal Vector Quantization: A Short** Background

Assume  $\mathbb{R}^d$  is equipped with the Euclidean norm  $|.|$ . Let  $X : (\Omega, \mathcal{A}, \mathbb{P}) \to \mathbb{R}^d$  be a random vector. For a given set  $\Gamma = \{x_1, \ldots, x_N\} \subset \mathbb{R}^d, N \ge 1$ , any (Borel) projection  $\widehat{X}^{\Gamma}$  of X on  $\Gamma$  following the nearest neighbor rule provides an optimal solution

$$|X - \widehat{X}^{\Gamma}| = d(X, \Gamma) = \min_{1 \le i \le N} |X - x_i| \qquad (1)$$

The projection is essentially unique if all hyperplanes have 0-mass for the distribution of X. If  $X \in L^2(\mathbb{P})$ ,

the induced mean quadratic error  $||X - \widehat{X}^{\Gamma}||$ , reaches a minimum as  $\Gamma$  runs over all subsets of  $\mathbb{R}^d$ of size at most N. Any such minimizer  $\Gamma^{N,*}$  is called an *optimal quadratic N-quantizer* of  $X$  and  $\widehat{X}^{\Gamma^{N,*}}$  is called an *optimal quadratic N-quantization* of  $X$ . Using the property that conditional expectation given a  $\sigma$ -field  $\mathcal{B}$  is the best  $\mathcal{B}$ -measurable quadratic approximation, one derives the result that an optimal quantizer satisfies the so-called *stationary property*:

$$\mathbb{E}(X|\widehat{X}) = \widehat{X}$$
 with  $\widehat{X} := \widehat{X}^{\Gamma^{N,*}}$  (2)

It is easy to show that the minimal mean quantization error  $\|\widehat{X} - \widehat{X}^{\Gamma^{N,*}}\|_{2}$  is nonincreasing and goes to zero as  $N \to \infty$  (decreasing if the support of X is infinite). Optimal quantizers also exist with respect to the  $L^r(\mathbb{P})$ -norm,  $r \neq 2$ . The rate of convergence is ruled by the Zador Theorem.

**Theorem 1** (a) Sharp rate [9]. Let  $X \in L^{r+\eta}(\mathbb{P})$ for some  $r, \eta > 0$ . Let  $\mathbb{P}_{v}(d\xi) = \varphi(\xi) d\xi + v(d\xi)$  be the canonical decomposition of the distribution of  $X$  $(v \text{ and the Lebesgue measure are singular}).$  Then there exists a real constant  $\tilde{J}_{r,d} \in (0,\infty)$  such that

$$\begin{split} &\lim_{N} N^{\frac{1}{d}} \min_{\Gamma \subset \mathbb{R}^{d}, \operatorname{card}(\Gamma) \leq N} \|X - \widehat{X}^{\Gamma}\|_{r} \sim \widetilde{J}_{r,d} \\ &\quad \times \left(\int_{\mathbb{R}^{d}} \varphi^{\frac{d}{d+r}}(u) \, \mathrm{d}u\right)^{\frac{1}{d} + \frac{1}{r}} \quad \textit{as} \quad N \to +\infty \end{split} \tag{3}$$

(b) Nonasymptotic upper bound [13]. Let  $d \in \mathbb{N}$ . Let  $r, \eta > 0$ . There exists  $C_{d,r,\eta} \in (0,\infty)$  such that, for every  $\mathbb{R}^d$ -valued random vector X,

$$\forall N \ge 1,$$
  
$$\min_{\Gamma \subset \mathbb{R}^d, |\Gamma| \le N} \|X - \widehat{X}^{\Gamma}\|_{r} \le C_{d,r,\eta} \|X\|_{r+\eta} N^{-\frac{1}{d}} \quad (4)$$

The real constant  $\tilde{J}_{r,d}$  (which depends on the underlying norm on  $\mathbb{R}^d$ ) corresponds to the case of the uniform distribution over  $[0, 1]^d$  for which the above " $\lim_{N}$ " also holds as an " $\inf_{N}$ " as well. When  $d = 1$ ,  $\widetilde{J}_{r,1} = (r+1)^{-\frac{1}{r}}/2$ . When  $d = 2$ , with the canonical Euclidean norm,  $\widetilde{J}_{2,d} = \sqrt{\frac{5}{18\sqrt{3}}}$ . For  $d \ge 3$ one only knows that  $\widetilde{J}_{2,d} \sim \sqrt{\frac{d}{2\pi e}} \approx \sqrt{\frac{d}{17.08}}$  as  $d \to$ 

![](_page_1_Figure_1.jpeg)

**Figure 1**  $N$ -quantizer (and its Voronoi diagram) of the normal distribution  $\mathcal{N}(0; I_2)$  on  $\mathbb{R}^2$  with  $N = 500$  (The Voronoi diagram never needs to be computed for numerics)

 $+\infty$ . For more results on the theoretical aspects of vector quantization we refer to  $[9]$  and the references therein. Figure 1 shows a quantization of the bivariate normal distribution of size  $N = 500$ .

### Some Quantization-based Cubature Formulae

Let  $X$  be an  $\mathbb{R}^d$ -valued random vector and  $Y$  an  $\mathbb{R}^q$ -valued random vector; let  $\Gamma_X = \{x_1, \ldots, x_{N_X}\},\$  $\Gamma_Y = \{y_1, \ldots, y_{N_Y}\}\$  be two quantizers of X and Y, respectively. Let  $F: \mathbb{R}^d \longrightarrow \mathbb{R}$  be a (continuous) function. It seems natural to approximate these quantities by their quantized version, that is,

$$\mathbb{E}(F(\widehat{X}) \approx \mathbb{E}(F(\widehat{X}^{\Gamma_{X}})) \quad \text{and}$$

$$\mathbb{E}(F(X)|Y) \approx \mathbb{E}(F(\widehat{X}^{\Gamma_{X}})|\widehat{Y}^{\Gamma_{Y}})$$

$$\text{where } \mathbb{E}(F(\widehat{X}^{\Gamma_{X}})) = \sum_{1 \le i \le N_{X}} F(x_{i}) \mathbb{P}(\widehat{X}^{\Gamma_{X}} = x_{i}) \quad (5)$$

$$\mathbb{E}(F(\widehat{X}^{\Gamma_{X}})|\widehat{Y}^{\Gamma_{Y}})$$

$$= \sum_{1 \le i \le N_{X}} F(x_{i}) \mathbb{P}(\widehat{X}^{\Gamma^{X}} = x_{i}|\widehat{Y}^{\Gamma_{Y}} = y_{j}),$$

$$1 \le j \le N_{Y} \quad (6)$$

 $\mathbb{E}(F(\widehat{X}^{\Gamma_X}))$ Numerical computation of and  $\mathbb{E}(F(\widehat{X}^{\Gamma_X})|\widehat{Y}^{\Gamma_Y})$  is possible as soon as  $F(\xi)$  is computable at any  $\xi \in \mathbb{R}^d$  and both the distribution  $(\mathbb{P}(\widehat{X}^{\Gamma_X} = x_i))_{1 \le i \le N}$  of  $\widehat{X}^{\Gamma_X}$  and the conditional distribution of  $\widehat{X}^{\Gamma_X}$  given  $\widehat{Y}^{\Gamma_Y}$  are made explicit.

Likewise, one can consider *a priori* the  $\sigma(\widehat{X}^{\Gamma_X})$ measurable random variable  $F(\widehat{X}^{\Gamma_X})$  as a good approximation of the conditional expectation  $\mathbb{E}(F(X)|\widehat{X}^{\Gamma_X})$ . One shows (see, e.g., [25]) that

$$\|X - \widehat{X}^{\Gamma_X}\|_{_{1}} = \sup_{[F]_{\mathrm{Lip}} \le 1} |\mathbb{E}F(X) - \mathbb{E}F(\widehat{X}^{\Gamma_X})| \quad (7)$$

where  $[F]_{\text{Lip}}$  denotes the Lipschitz coefficient of  $F$ . If, furthermore,  $\varphi_{\scriptscriptstyle F}:\mathbb{R}^q\to\mathbb{R}$ , which is a (Borel) version of the conditional expectation, that is, satisfying  $\mathbb{E}(F(X)|Y) = \varphi_{F}(Y)$  turns out to be Lipschitz, then

$$\begin{split} \|\mathbb{E}(F(X)|Y) - \mathbb{E}(F(\widehat{X}^{\Gamma_{X}})|\widehat{Y}^{\Gamma_{Y}})\|_{2} \\ \leq [F]_{\text{Lip}} \|X - \widehat{X}^{\Gamma_{X}}\|_{2} + [\varphi_{F}]_{\text{Lip}} \|Y - \widehat{Y}^{\Gamma_{Y}}\|_{2} \end{split} \tag{8}$$

When  $F$  is twice differentiable with a Lipschitz differential and  $\Gamma_X$  is a stationary quantizer, then

$$|\mathbb{E}F(X) - \mathbb{E}F(\widehat{X}^{\Gamma_X})| \leq [DF]_{\text{Lip}} \|X - \widehat{X}^{\Gamma_X}\|_{2}^{2} \quad (9)$$

Similar cubature formulas can be established for locally Lipschitz functions such that  $|F(x) |F(y)| \leq C|x-y|(1+g(x)+g(y))$  where g is a nonnegative, nondecreasing, convex function (e.g.,  $g(x) = e^{|a||x|}$ . Finally, when F is convex and  $\widehat{X}^{\Gamma_X}$  is stationary, Jensen's inequality yields

$$\mathbb{E}\left(F(X)|\widehat{X}^{\Gamma_{X}}\right) \geq F(\mathbb{E}(X|\widehat{X}^{\Gamma_{X}}))$$
$$= F(\widehat{X}^{\Gamma_{X}}) \quad \left(\text{so that } \mathbb{E}\left(F(\widehat{X}^{\Gamma_{X}})\right) \leq \mathbb{E}\left(F(X)\right)\right)$$
$$(10)$$

# Example: Pricing a Bermuda Option **Using a Quantization Tree**

Let  $(X_k)_{0 \le k \le n}$  be a Markov chain modeling the dynamics of  $d$  traded risky assets (interest rate is set to 0 for simplicity), assumed to be homogeneous for the sake of simplicity, with Lipschitz transition  $P(x, dy) = \mathcal{L}(X_{k+1}|X_k = x)$ , that is, satisfying the condition that for every Lipschitz continuous function  $f$ ,  $[Pf]_{\text{Lip}} \leq [P]_{\text{Lip}}[f]_{\text{Lip}}$ . Let  $(\widehat{X}_k)_{0 \leq k \leq n}$  be a sequence of quantizations ( $\widehat{X}_k := \widehat{X}_k^{\Gamma_k}$  where the grids  $\Gamma_k := \{x_1^k, \ldots, x_{N_k}^k\} \subset \mathbb{R}^d$  are optimal, see the section How to Get Optimal Quantization below). These grids (and the related quantized transition probability weights defined below) are called a *quantization tree* of the chain.

$$\mathcal{V}_0 = \sup \left\{ \mathbb{E}(h(X_\tau)), \tau \mathcal{F}^X \text{-stopping time} \right\} \quad (11)$$

of the option by implementing a backward quantized dynamic programming formula as follows:

$$\widehat{\mathcal{V}}_{n} = h(\widehat{X}_{n}),$$
  

$$\widehat{\mathcal{V}}_{k} = \max(h(\widehat{X}_{k}), \mathbb{E}(\widehat{\mathcal{V}}_{k+1}|\widehat{X}_{k})), \ k = 0, \dots, n-1$$
(12)

in which the Markov property is "forced" since  $(\widehat{X}_k)_{0 \le k \le n}$  has no reason to be a Markov chain. In practice, one shows that  $\widehat{\mathcal{V}}_k = v_k(\widehat{X}_k)$  where the functions  $v_k$  defined on  $\Gamma_k$  satisfy the following backward induction:

$$v_n(x_i^n) = h(x_i^n), \quad i = 1, \dots, N_n$$
 (13)

$$v_k(x_i^k) = \max\left(h(x_i^k), \sum_{x_j \in \Gamma_{k+1}} \widehat{p}_k^{ij} v_{k+1}(x_j^{k+1})\right),\newline i = 1, \dots, N_k \tag{14}$$

where  $\widehat{p}_{k}^{ij} = \mathbb{P}\left(\widehat{X}_{k+1} = x_{j}^{k+1} | \widehat{X}_{k} = x_{i}^{k}\right)$  $(15)$ 

The point is that once the transitions  $\widehat{p}_k^{ij}$  have been computed (e.g., by a—possibly parallelized, see  $[5]$ —Monte Carlo simulation), the above backward induction can be applied to any (reasonable) payoff: the quantization-based approach is not payoff dependent as the regression-based simulation methods (see **Bermudan Options**) are. The resulting error bound, combining equation  $(8)$  and the Zador Theorem $(b)$  is

$$|\mathcal{V}_0 - \mathbb{E}v_0(X_0)| \le C_{[P]_{\text{Lip}},d} \sum_{k=0}^n \|X_k - \widehat{X}_k\|_2$$
$$= O\left(\frac{n}{\bar{N}^{\frac{1}{d}}}\right) \tag{16}$$

where  $\bar{N} := \frac{1}{n+1} \sum_{k=0}^{n} N_k$ . First-order schemes have been devised involving the approximation  $\widehat{Dv_k}$  of the (space) differential of  $Dv_k$  of  $v_k$  in [3]. Other quantization-based schemes have been devised for many other problems (stochastic control, nonlinear filtering [20], etc.).

#### **How to Get Optimal Quantization**

For this aspect, which is clearly critical for applications, we mainly refer to  $[17, 21, 25]$  and the references therein. We just say that the two main procedures are both based on the stationary equation  $\widehat{X}^{\Gamma} = \mathbb{E}(X|\widehat{X}^{\Gamma}).$  The randomized Lloyd's I is the induced fixed-point procedure whereas the *com*petitive learning vector quantization algorithm is a recursive stochastic gradient zero search procedure. Both are based on the massive simulation of independent and identically distributed (i.i.d.) copies of  $X$  and nearest neighbor search. Recent developments in the field of fast versions of such procedures  $[7, 14]$ clearly open new perspectives to the online implementation of quantization-based methods. Regarding the Gaussian distribution, a quantization process has been completed and some optimal grids are available on the website [23]: www.quantize.maths-fi.com.

## **New Directions**

Although optimal quantization is an autonomous field of research at the intersection of approximation theory, information theory, and probability theory, which has its own life, it seems that it generates many ideas that can easily and efficiently be applied to numerical probability and computational finance.

One important direction, not developed here, is functional quantization where a stochastic process—for example, the Brownian motion, a Lévy process, or a diffusion-is quantized as a random variable taking values in its path space (see  $[10-12]$ ) or [17] for a survey, and the references therein). This has been applied to the pricing of path-dependent options in [22]. See also the website [23] to download optimal quadratic functional quantizers of the Brownian motion.

Another direction is variance reduction where quantization can be used either as a control variate or a stratification method, with, in both cases, the specificity being an optimal way to proceed among Lipschitz continuous functions/functionals [22, 24, 25].

#### References

Bally, V. & Pagès, G. (2003). A quantization algorithm  $[1]$ for solving discrete time multidimensional optimal stopping problems, Bernoulli 9(6), 1003-1049.

## **4 Quantization Methods**

- [2] Bally, V., Pages, G. & Printems, J. (2001). A stochastic ` quantization method for non-linear problems, *Monte Carlo Methods and Applications* **7**(1), 21–34.
- [3] Bally, V., Pages, G. & Printems, J. (2003). First order ` schemes in the numerical quantization method, *Mathematical Finance* **13**(1), 1–16.
- [4] Bally, V., Pages, G. & Printems, J. (2005). A quanti- ` zation tree method for pricing and hedging multidimensional American options, *Mathematical Finance* **15**(1), 119–168.
- [5] Bardou, O., Bouthemy, S. & Pages, G. (2007). Pric- ` ing swing options using optimal quantization, preprint LPMA-1146, to appear in *Applied Mathematical Finance*.
- [6] Bardou, O., Bouthemy, S. & Pages, G. (2007). When ` are swing option bang-bang and how to use it? pre-print LPMA-1141, submitted.
- [7] Friedman, J.H., Bentley, J.L. & Finkel, R.A. (1977). An algorithm for finding best matches in logarithmic expected time, *ACM Transactions on Mathematical Software* **3**(3), 209–226.
- [8] Gobet, E., Pages, G., Pham, H. & Printems, J. (2007). ` Discretization and simulation of the Zakai equation, *SIAM Journal on Numerical Analysis* **44**(6), 2505–2538. See also, Discretization and simulation for a class of SPDEs with applications to Zakai and McKean-Vlasov equations, Pre-pub. PMA-958, 2005. ´
- [9] Graf, S. and Luschgy, H. (2000). *Foundations of Quantization for Probability Distributions*, Lecture Notes in Mathematics 1730, Springer, Berlin, 230.
- [10] Luschgy, H. & Pages, G. (2002). Functional quantization ` of Gaussian processes, *Journal of Functional Analysis* **196**(2), 486–531.
- [11] Luschgy, H. & Pages, G. (2004). Sharp asymptotics ` of the functional quantization problem for Gaussian processes, *The Annals of Probability* **32**(2), 1574–1599.
- [12] Luschgy, H. & Pages, G. (2006). Functional quantiza- ` tion of a class of Brownian diffusions: A constructive approach, *Stochastic Processes and Applications* **116**, 310–336.
- [13] Luschgy, H. & Pages, G. (2008). Functional quantization ` rate and mean regularity of processes with an application to Levy processes, ´ *Annals of Applied Probability* **18**(2), 427–469.
- [14] McNames, J. (2001). A fast nearest-neighbor algorithm based on a principal axis search tree, *IEEE Transactions on Pattern Analysis and Machine Intelligence* **23**(9), 964–976.
- [15] Pages, G. (1993). Voronoi tessellation, space quantiza- ` tion algorithm and numerical integration, in *Proceedings of the ESANN'93*, M. Verleysen, ed, Editions D Facto, Bruxelles, p. 221–228.
- [16] Pages, G. (1998). A space vector quantization method ` for numerical integration, *Journal of Computational and Applied Mathematics* **89**, 1–38.

- [17] Pages, G. (2007). Quadratic optimal functional quantiza- ` tion methods and numerical applications, in *Proceedings of MCQMC, Ulm'06*, Springer, Berlin, p. 101–142.
- [18] Pages, G. & Pham, H. (2005). Optimal quantization ` methods for non-linear filtering with discrete-time observations, *Bernoulli* **11**(5), 893–932.
- [19] Pages, G., Pham, H. & Printems, J. (2003). Opti- ` mal quantization methods and applications to numerical methods in finance in *Handbook of Computational and Numerical Methods in Finance*, S.T. Rachev, ed, Birkhauser, Boston, p. 429. ¨
- [20] Pages, G., Pham, H. & Printems, J. (2004). An optimal ` Markovian quantization algorithm for multidimensional stochastic control problems, *Stochastics and Dynamics* **4**(4), 501–545.
- [21] Pages, G. & Printems, J. (2003). Optimal quadratic ` quantization for numerics: the Gaussian case, *Monte Carlo Methods and Applications* **9**(2), 135–165.
- [22] Pages, G. & Printems, J. (2005). Functional quantization ` for numerics with an application to option pricing, *Monte Carlo Methods and Applications* **11**(4), 407–446.
- [23] Pages, G. & Printems, J. (2005). Website devoted to ` *vector and functional optimal quantization*, www.quantize. maths-fi.com.
- [24] Pages, G. & Printems, J. (2008). Reducing variance ` using quantization, pre-pub. LPMA, submitted.
- [25] Pages, G. & Printems, J. (2008). Optimal quantization ` for finance: from random vectors to stochastic processes, in *Handbook of Numerical Analysis*, P. G. Ciarlet, ed, special volume: Mathematical Modelling and Numerical Methods in Finance, A. Bensoussan & Q. Zhang, (guest editors), North-Holland, Netherlands, Vol. XV pp. 595–648, ISBN: 978-0-444-51879-8.

## **Further Reading**

- Bally, V. & Pages, G. (2003). Error analysis of the quantization ` algorithm for obstacle problems, *Stochastic Processes & Their Applications*, **106**(1), 1–40.
- Pages, G. & Sellami, A. (2007). Convergence of multi- ` dimensional quantized SDE's, Pre-print LPMA-1196, ´ submitted.

## **Related Articles**

**American Options**; **Bermudan Options**; **Stochastic Mesh Method**; **Tree Methods**.

GILLES PAGES`
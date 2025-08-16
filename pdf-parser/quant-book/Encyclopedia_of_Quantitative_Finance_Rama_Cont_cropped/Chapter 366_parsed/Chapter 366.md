# **Jump Processes**

# **Processes with Jumps in General**

Although, historically, models in mathematical finance were based on Brownian motion and thus are models with continuous price paths, jump processes now play a key role across all areas of finance (see, e.g., [5]). One reason for this move into a new class of processes is that because of their distributional properties, diffusions in many cases cannot provide a realistic picture of empirically observed facts. Another reason is the enormous progress made in understanding and handling jump processes due to the development of semimartingale theory on one side and of computational power on the other side.

The simplest jump process is a process with just one jump. Let *T* be a random time—actually a stopping time with respect to an information structure given by a filtration *(*F*t)t*≥0—then

$$X_t = \mathbb{1}_{\{T \le t\}} \quad (t \ge 0) \tag{1}$$

has the value 0 until a certain event occurs and then 1. Although this process looks simple, it is important in modeling credit risk, namely as the process that describes the time of default of a company. The next step leads to processes that have integer values with positive jumps of size 1 only, the so-called *counting processes (Xt)t*≥0. *Xt* describes the number of events that have occurred between time 0 and *t*. This could be the number of defaults in a large credit portfolio or the number of claims customers report to an insurance company. The standard case is a *Poisson process (Nt)t*≥0, where the distribution of *Xt* is given by a Poisson distribution with parameter *λt*. Equivalently, one can describe this process by requiring that the waiting times between successive jumps are independent, exponentially distributed random variables with parameter *λ*.

The natural extension is a *compound Poisson process (Xt)t*≥0, that is, a process with stationary independent increments where the jump size is no longer 1, but given by a probability law *µ*. Let *(Yk )k*<sup>≥</sup><sup>1</sup> be a sequence of independent random variables with distribution L*(Yk )* = *µ* for all *k* ≥ 1. Denote by *(Nt)t*<sup>≥</sup><sup>0</sup> a standard Poisson process with parameter *λ >* 0 as described above, which is independent of *(Yk )k*≥1. Then we can represent *(Xt)t*<sup>≥</sup><sup>0</sup> in the following form:

$$X_t = \sum_{k=1}^{N_t} Y_k \tag{2}$$

A typical application of compound Poisson processes is to model the cumulative claim size up to time *t* in a portfolio of insurance contracts where the individual claim size is distributed according to *µ*. For the sake of analytical tractability, it is often useful to *compensate* this process, that is, to subtract the average claim size *E*[*Xt*]. Assuming that *µ* has a finite expectation and using stationarity and independence, we conclude *E*[*Xt*] = *tE*[*X*1] and therefore get the following representation:

$$X_t = tE[X_1] + (X_t - E[X_t])$$
 (3)

The compensated process *(Xt* − *E*[*Xt*]*)t*<sup>≥</sup><sup>0</sup> is a martingale and, therefore, equation (3) is a decomposition of the process in a linear drift *E*[*X*1] · *t* and a martingale. Representation (3) motivates the definition of a general *semimartingale* as a process that is adapted to a filtration *(*F*t)t*≥0, has paths that are right-continuous and have left limits (cadl ` ag paths), ` and allows a decomposition

$$X_t = X_0 + V_t + M_t \quad (t \ge 0) \tag{4}$$

where *V* = *(Vt)t*<sup>≥</sup><sup>0</sup> is an adapted cadl ` ag process of ` finite variation and *M* = *(Mt)t*<sup>≥</sup><sup>0</sup> is a local martingale. There exist processes that are not semimartingales. An important class of examples is fractional Brownian motions with the exception of usual Brownian motion, which is a semimartingale. We do not go beyond semimartingales in this discussion mainly because for semimartingales there is a well-developed theory of stochastic integration, a fact which is crucial for modeling in finance.

In general, the representation (4) is not unique. It becomes unique with a *predictable* process *V* if we consider *special semimartingales*. A semimartingale can be made special by taking the big jumps away, for example, jumps with absolute jump size larger than 1. This follows from the well-known fact that a semimartingale with bounded jumps is special [11, I.4.24]. Denote by *-Xt* = *Xt* − *Xt*<sup>−</sup> the jump at time *t* if there is any. Then

$$X_t - \sum_{s \le t} \Delta X_s \mathbbm{1}_{\{|\Delta X_s| > 1\}} \tag{5}$$

has bounded jumps. Further, let us note that any local martingale M (with  $M_0 = 0$ ) admits a unique (orthogonal) decomposition into a local martingale with continuous paths  $M^c$  and a purely discontinuous, local martingale  $M^d$  ([11, I.4.18]). Assuming  $X_0 = 0$ , we got the following unique representation for semimartingales:

$$X_t = V_t + M^c + M^d + \sum_{s \le t} \Delta X_s \mathbb{1}_{\{|\Delta X_s| > 1\}} \qquad (6)$$

To analyze  $M^d$  in more detail, we introduce the random measure of jumps

$$\mu^{X}(\omega; \mathrm{d}t, \mathrm{d}x) = \sum_{s>0} \mathbbm{1}_{\{\Delta X_{s}(\omega) \neq 0\}} \varepsilon_{(s, \Delta X_{s}(\omega))}(\mathrm{d}t, \mathrm{d}x) \tag{7}$$

where  $\varepsilon_a$  denotes as usual the unit mass in a. Thus,  $\mu^{X}$  is a random measure which, for fixed  $\omega$ , places a point mass of size 1 on each pair  $(s, \Delta X_s(\omega)) \in$  $\mathbb{R}_+ \times \mathbb{R}$  whenever for this  $\omega$  the process jumps by  $\Delta X_s(\omega)$  at time s. Expressed differently for any Borel subset  $B \subset \mathbb{R}, \mu^X(\omega; [0, t] \times B)$  counts the number of jumps with size in  $B$  which can be observed along the path  $(X_s(\omega))_{0 \le s \le t}$ . With this notation, equation  $(5)$  can be written as

$$X_{t} - \int_{0}^{t} \int_{\mathbb{R}} x \, \mathbb{1}_{\{|x|>1\}} \mu^{X}(\mathrm{d}s, \mathrm{d}x) \tag{8}$$

The purely discontinuous local martingale  $M^d$ , that is, the process of *compensated jumps* of absolute size less than 1, has then the following form:

$$M_t^d = \int_0^t \int_{\mathbb{R}} x \, \mathbb{1}_{\{|x| \le 1\}} (\mu^X - \nu^X)(\mathrm{d}s, \mathrm{d}x) \quad (9)$$

where  $v^X$  is another random measure, the (*predictable*) compensator of  $\mu^X$ . Whereas  $\mu^X$  counts the exact number of jumps,  $v^X$  roughly stands for the expected, that is, the average number of jumps. The integral with respect to  $\mu^X - \nu^X$  in equation (9), in general, cannot be separated in an integral with respect to  $\mu^X$  and another one with respect to  $\nu^X$ . This is because the sum of the small jumps

$$\sum_{s\leq t} \Delta X_s \mathbbm{1}_{\{|\Delta X_s|\leq 1\}} = \int_0^t \int_{\mathbb{R}} x \mathbbm{1}_{\{|x|\leq 1\}} \mu^X(\mathrm{d}s, \mathrm{d}x) \tag{10}$$

does not converge, in general.

## Lévy Processes

For many applications, it is sufficient to reduce generality and to consider the subclass of *Lévy processes*, that is, processes with stationary and independent increments. The components in equations  $(6)$  and  $(9)$ are then

$$V_t = bt \quad (t \ge 0)$$
  
$$M_t^c = \sqrt{c} W_t \quad (t \ge 0)$$
  
$$v^X([0, t] \times B) = tK(B) \tag{11}$$

where b and c are real numbers,  $c \ge 0$ ,  $(W_t)_{t \ge 0}$  is a standard Brownian motion, and  $K$ , the Lévy mea*sure*, is a (possibly infinite) measure on the real line that satisfies  $\int (1 \wedge x^2) K(\mathrm{d}x) < \infty$ . The law of X is completely determined by the triplet of local char*acteristics*  $(b, c, K)$  since these are the parameters that appear in the classical Lévy-Khintchine formula. This formula expresses the characteristic function  $\varphi_{X_t}(u) = E[\exp(iuX_t)]$  in the form

$$\varphi_{X_t}(u) = \exp(t\psi(u)) \tag{12}$$

with the characteristic exponent

$$\begin{split} \psi(u) &= \mathrm{i} u b - \frac{1}{2} u^2 c \\ &+ \int \left( \mathrm{e}^{\mathrm{i} u x} - 1 - \mathrm{i} u x \, \mathbb{1}_{\{|x| \le 1\}} \right) K(\mathrm{d} x) \, (13) \end{split}$$

The *truncation function*  $h(x) = x \mathbb{1}_{\{|x| < 1\}}$  could be replaced by other versions of truncation functions, for example, smooth functions that are identical to the identity in a neighborhood of the origin and go to 0 outside this neighborhood. Changing  $h$  affects the drift parameter  $b$ , but not  $c$  or  $K$ . All the information on the jump behavior of the process  $(X_t)_{t>0}$  is contained in K. The frequency of large jumps, expressed by the weight  $K$  puts on the tails, determines finiteness of the moments of the process as the following result states (for proofs of the propositions see  $[15]$ ).

**Proposition 1** Let  $X = (X_t)_{t>0}$  be a Lévy process with Lévy measure K. Then  $E[|X_t|^p]$  is finite for any  $p \in \mathbb{R}_+$  if and only if  $\int_{\{|x|>1\}} |x|^p K(\mathrm{d}x) < \infty.$ 

We note that if  $X_1$  and consequently any  $X_t$ has finite expectation, then one does not have to truncate in equation (13), that is,  $h(x) = x \mathbb{1}_{\{|x| < 1\}}$  can be replaced by  $h(x) = x$ .

The sum of the big jumps which is subtracted in equation  $(5)$  is finite since there are only finitely many of them from 0 to  $t$  for every path. The fine structure of the paths is determined by the frequency of the small jumps. A process is said to have *finite activity* if almost all paths have only a finite number of jumps along finite time intervals. The simplest examples are Poisson and compound Poisson processes. A process is said to have *infinite activity* if almost all paths have infinitely many jumps along any time interval of finite length.

**Proposition 2** Let  $X = (X_t)_{t \ge 0}$  be a Lévy process with Lévy measure K. Then  $\overline{X}$  has finite activity if  $K(R) < \infty$  and has infinite activity if  $K(R) = \infty$ .

Since a Lévy measure has *a priori* finite mass in the tails, that is,  $\int_{\{|x|>1\}} K(dx) < \infty$ , the finiteness of  $K(R)$  means finiteness of  $\int_{\{|x|\leq 1\}} K(dx)$ . Consequently, having a finite or an infinite number of jumps along finite time intervals is determined by the mass of  $K$  around the origin. From the distribution of mass around the origin, one can also see if the sum of (infinitely many) small jumps converges or not. First, let us recall that a standard Brownian motion has paths of infinite variation. Therefore, a Lévy process has infinite variation as soon as it has a continuous martingale component, that is,  $c > 0$  in equation (11), but infinite variation can also come from the jumps.

**Proposition 3** Let  $X = (X_t)_{t>0}$  be a Lévy process with triplet  $(b, c, K)$ . Then almost all paths of X have *finite variation if*  $c = 0$  *and*  $\int_{\{|x| < 1\}} |x| K(\mathrm{d}x) < \infty$ . *If* this integral is infinite or  $c > 0$ , then almost all paths of  $X$  have infinite variation.

Figure 1 shows a simulated path of a purely discontinuous, infinite activity process with finite variation, whereas Figure 2 shows a corresponding path with infinite variation.

#### **Important Examples**

Now we discuss some of the standard examples. The Poisson process with intensity parameter  $\lambda$  that we considered at the beginning has a finite number of jumps in any finite time interval and is constant between successive jumps. In terms of equation  $(11)$ ,

![](_page_2_Figure_9.jpeg)

**Figure 1** Simulation of a purely discontinuous Lévy process with infinite activity and finite variation

![](_page_2_Figure_11.jpeg)

**Figure 2** Simulation of a purely discontinuous Lévy process with infinite activity and infinite variation

it is characterized by  $b = E[X_1] = \lambda$ ,  $c = 0$ , and  $K = \lambda \varepsilon_1$ . For the compound Poisson process (2), the unit mass  $\varepsilon_1$  in K is replaced by a probability measure  $\mu$ , the law of  $Y_1$ , that is,  $K = \lambda \mu$ . For the drift parameter b, one gets  $\lambda E[Y_1]$ . One gets a Lévy jump diffusion by adding a general drift term bt and a scaled Brownian motion to equation  $(2)$ ,

$$X_{t} = bt + \sqrt{c}W_{t} + \sum_{k=1}^{N_{t}} Y_{k}$$
 (14)

This is the model introduced by Merton [14] to describe asset returns. Merton chose normally distributed variables  $Y_k$ . In an article, Kou [12] used

double-exponentially distributed jump sizes  $Y_k$ . If one replaces in equation (14) the Brownian motion with drift by a general diffusion process one gets a *jump diffusion*. The key property of jump diffusions is that one adds only a finite number of jumps in any finite time interval to a process with continuous paths. In other words, the jump times can be given by successive stopping times  $T_1 < T_2 < T_3 < \cdots$ . We also note that the distribution of  $X_t$  is not known for diffusions, in general. The same holds for jump diffusions. This reduces their applicability in mathematical finance. A key advantage of the pure jump Lévy processes that we discuss now is that they are distributionally very flexible and the distributions are known explicitly.

Generalized hyperbolic (GH) Lévy motions  $(X_t)_{t>0}$  (see Generalized hyperbolic models in this encyclopedia or in [6, 9]) represent a very large class of Lévy processes which are generated by GH distributions [1], that is, the distribution of  $X_1$ ,  $\mathcal{L}(X_1)$ , is GH. Using equation  $(12)$  all other distributions  $\mathcal{L}(X_t)$  are determined. GH distributions have an explicit Lebesgue density as has the corresponding Lévy measure. GH distributions can be represented as normal mean-variance mixtures, where the mixing distribution is a generalized inverse Gaussian (GIG) distribution. Moments of any order exist. Since  $c = 0$  in equation (13) GH Lévy motions have purely discontinuous paths. They are infinite activity processes. Important subclasses are hyperbolic Lévy motions ([7]) and normal inverse Gaussian (NIG) Lévy motions ([2]). Many well-known distributions can be obtained as limiting cases of GH distributions, which generate the corresponding processes [10]. Among those are the variance gamma distributions (see [13]), scaled and shifted Cauchy distributions, shifted Student- $t$  distributions, GIG distributions, and the gamma, as well as the normal distributions.

The CGMY process introduced in [4] is another purely discontinuous Lévy process, which can be defined by the Lévy density of  $\mathcal{L}(X_1)$ :

$$g_{\text{CGMY}}(x) = \begin{cases} C \frac{\exp(-G|x|)}{|x|^{1+Y}} & x < 0\\ C \frac{\exp(-Mx)}{x^{1+Y}} & x > 0 \end{cases}$$
(15)

where  $Y \in (-\infty, 2)$ . The process has infinite activity iff  $Y \in [0, 2)$  and it has infinite variation iff  $Y \in$  $[1, 2)$ . For  $Y = 0$ , it reduces to the variance gamma process.

A very classical class is given by  $\alpha$ -stable Lévy processes where  $0 < \alpha < 2$ . For  $\alpha = 2$  one gets Brownian motion, whereas for  $\alpha < 2$  one gets purely discontinuous processes. Only for three special cases explicit densities are known: the Gaussian, the Cauchy, and the Lévy distribution.

A tractable extension of Lévy processes are timeinhomogeneous, Lévy processes that is, processes with independent increments and absolutely continuous characteristics, called  $PIIAC$  in [11]. For any fixed t, the triplet of  $\mathcal{L}(X_t)$  for these processes is given in the form  $b = \int_0^t b_s \mathrm{d}s$ ,  $c = \int_0^t c_s \mathrm{d}s$ , and  $K(\mathrm{d}x) = \int_0^t K_s(\mathrm{d}x) \mathrm{d}s$ . This class of processes has been used extensively in the context of interest rate models (see e.g.,  $[8]$ ).

Jump processes with paths that are rather different from those discussed so far were introduced by Barndorff-Nielsen and Shephard [3] in the context of stochastic volatility models. Let  $(Z_t)_{t\geq 0}$  be a subordinator, that is, a Lévy process, starting at 0 with increasing paths and consequently without a Gaussian component. The volatility process  $(\sigma_t^2)_{t>0}$  is modeled by an Ornstein–Uhlenbeck-type stochastic differential equation

$$\mathrm{d}\sigma_t^2 = -\lambda \sigma_t^2 \mathrm{d}t + \mathrm{d}Z_{\lambda t} \tag{16}$$

for some  $\lambda > 0$ . The solution  $(\sigma_t^2)_{t \ge 0}$  moves up entirely by jumps and then tails off exponentially.  $\sigma_t$  is fed into a Brownian semimartingale that then represents the price process.

### References

- $[1]$ Barndorff-Nielsen, O.E. (1978). Hyperbolic distributions and distributions on hyperbolae, Scandinavian Journal of Statistics 5, 151-157.
- Barndorff-Nielsen, O.E. (1998). Processes of normal [2] inverse Gaussian type, Finance and Stochastics 2(1),  $41 - 68$
- Barndorff-Nielsen, O.E. & Shephard, O.E. (2001). Non-[3] Gaussian Ornstein-Uhlenbeck-based models and some of their uses in financial economics. Journal of the Royal Statistical Society, Series B 63, 167-207.
- Carr, P., Geman, H., Madan, D. & Yor, M. (2002). The [4] fine structure of asset returns: an empirical investigation, Journal of Business 75, 305-332.
- [5] Cont, R. & Tankov, P. (2004). Financial Modelling with Jump Processes, Chapman & Hall/CRC.
- [6] Eberlein, E. (2001). Application of generalized hyperbolic Lévy motions to finance, in Lévy Processes. Theory and Applications, O.E. Barndorff-Nielsen, T. Mikosch & S.I. Resnick, eds, Birkhäuser, 319-336.

- [7] Eberlein, E. & Keller, U. (1995). Hyperbolic distributions in finance, *Bernoulli* **1**(3), 281–299.
- [8] Eberlein, E. & Kluge, W. (2006). Exact pricing formulae for caps and swaptions in a Levy term structure model, ´ *Journal of Computational Finance* **9**, 99–125.
- [9] Eberlein, E., Prause, K. (2002). The generalized hyperbolic model: financial derivatives and risk measures, in *Mathematical Finance—Bachelier Congress*, Springer, Paris, pp. 245–267.
- [10] Eberlein, E. & von Hammerstein, E.A. (2004). Generalized hyperbolic and inverse Gaussian distributions: limiting cases and approximation of processes, in R.C. Dalang, M. Dozzi & F. Russo, eds, *Seminar on Stochastic Analysis, Random Fields and Applications IV*, *Progress in Probability 58*, Birkhauser, pp. 221–264. ¨

- [11] Jacod, J. & Shiryaev, A.N. (1987). *Limit Theorems for Stochastic Processes*, Springer.
- [12] Kou, S.G. (2002). A jump diffusion model for option pricing, *Management Science* **48**, 1086–1101.
- [13] Madan, D. & Seneta, E. (1990). The variance gamma (V.G.) model for share market returns, *Journal of Business* **63**, 511–524.
- [14] Merton, R.C. (1976). Option pricing when underlying stock returns are discontinuous, *Journal of Financial Economics* **3**, 125–144.
- [15] Sato, K.-I. (1999). *L´evy Processes and Infinitely Divisible Distributions*, Cambridge University Press.

ERNST EBERLEIN
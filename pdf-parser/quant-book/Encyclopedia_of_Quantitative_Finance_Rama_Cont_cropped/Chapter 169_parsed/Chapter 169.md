# **Large Pool** Approximations

The loss distribution of a large credit portfolio can be valued by Monte Carlo methods. This is perhaps the most common approach used by practitioners today. The problem is that Monte Carlo methods are computationally intensive usually taking a significant amount of time to achieve the required accuracy. Therefore, although such methods may lend themselves to pricing and structuring of credit derivatives, they are not appropriate for risk management where simulation and stress testing are required. In fact, nesting a second level of simulation, for pricing, within the risk management simulation represents a performance challenge.

Analytical approximations of losses of large portfolios represent an efficient alternative to Monte Carlo simulation. The following methods can be applied for approximation of a large portfolio's loss distribution: the law of large numbers (LLN), the central limit theorem (CLT), and large deviation theory.

The analytical methods for approximation of credit portfolio losses are usually applied in an additive scheme: the portfolio losses due to default,  $\mathcal{L}$ , over some fixed time horizon (single step) are represented as

$$\mathcal{L} = \sum_{k=1}^{K} L_k \tag{1}$$

where  $L_k$  is the loss of the *k*th name in the portfolio and  $K$  is the number of names. Application of limit theorems for stochastic process becomes quite natural as  $K$  increases. The main technical difficulties are related to dependency of default events and losses of the counterparties.

The analytical methods for portfolio losses are applied in the conditional independence framework pioneered in [14] (see also [7, 9]), based on the assumption that there is a random vector,  $X$ , such that conditional on the values of  $X$ , the default events are independent. Usually,  $X$  is interpreted as a vector of credit drivers describing the state of the economy or a sector of the economy, at the end of the time horizon  $[3, 5, 8, 12]$ . In multistep models, X can be a random process describing the dynamics of the credit drivers [7]. In this case, computation of conditional default and migration probabilities requires efficient numerical quadratures for multidimensional integrals [7]. The multistep portfolio modeling is applied when it is necessary to incorporate the effect of stochastic portfolio exposure, as in the integrated market and credit risk framework in [7].

**The notation**  $\mathbb{P}_x$  denotes the regular conditional probability measure, conditional on  $X = x$ ;  $\mathbb{E}_x$  is the corresponding conditional expectation operator.

A general approach to approximate the distribution of the random variable  $\mathcal{L}$  can be described as follows:

- Choose a sufficiently rich family of distributions, 1.  $F_{\theta}$ , such that  $\theta \mapsto F_{\theta}$  is a Borel measurable mapping of a vector of parameters  $\theta$ .
- 2. Fix a value of the variable,  $X = x$  and compute parameters,  $\theta(x)$ , of the approximating family of distributions,  $F_{\theta(x)}(\ell)$ , such that the conditional distribution,  $\mathbb{P}_x(\mathcal{L} \leq \ell) = \mathbb{P}(\mathcal{L} \leq \ell \mid X = x)$ , is approximated by  $F_{\theta(x)}(\ell)$ . (It is assumed that  $x \mapsto \theta(x)$  is Borel measurable, so that  $x \mapsto$  $F_{\theta(x)}(\ell)$  is also measurable, for each  $\ell$ .)
- Find the unconditional approximating distribu-3. tion by integration over the distribution,  $G_X$ , of the variable  $X$ :

$$F^*(\ell) = \int F_{\theta(x)}(\ell) \, \mathrm{d}G_X(x) \tag{2}$$

# Law of Large Numbers: Vasicek Approximation

The first key result was obtained in [14, 13] for homogeneous portfolios. The  $K$  random variables,  $L_k$ , can be expressed as  $L_k = N \cdot I_k$ , where  $I_k$  is the indicator of default of the  $k$ th name and  $N$  is the constant loss given default. The random variables  $I_k$  are identically distributed and their sum,  $\nu =$  $\sum_{k=1}^{K} I_k$ , is the number of names in default. The portfolio losses  $\mathcal{L} = N \nu$ .

The variable,  $X$ , in the Vasicek model is latent and has a standard normal distribution,  $\Phi(x)$ . Conditional on  $X = x$ , the default events are independent and v has a binomial distribution with parameter  $p(x) =$  $\mathbb{P}(I_k = 1 \mid X = x)$  so that

$$\int_{-\infty}^{\infty} p(x) \, \mathrm{d}\Phi(x) = \pi_* \tag{3}$$

where  $\pi_*$  is the common unconditional probability of default. The unconditional distribution of  $\nu$  is then a generalized binomial distribution and

$$\mathbb{P}(\mathcal{L} = mN) = \mathbb{P}(v = m)$$
$$= {K \choose m} \int_{-\infty}^{\infty} p^{m}(x) q^{K-m}(x) \, \mathrm{d}\Phi(x),$$
$$m = 0, 1, \dots, K \tag{4}$$

where  $q(x) = 1 - p(x)$ .

The following specification<sup>a</sup> of the conditional default probability is widely used in the literature [6, 14], and so on.

$$p(x) = \Phi\left(\frac{H - \beta x}{\sigma}\right) \qquad \beta^2 + \sigma^2 = 1 \quad (5)$$

where  $H = \Phi^{-1}(\pi_*)$ , and  $\beta$  is a parameter that determines the correlation between default events.

Consider the ratio  $v_K = v/K$  determining the portfolio losses. If  $\beta = 0$ , then  $p(x) \equiv \pi_*$  and

$$\lim_{K \to \infty} \nu_K = \pi_* \quad \text{almost surely} \tag{6}$$

in accordance with the strong law of large numbers. If  $\beta \neq 0$  the limit in equation (6) is in distribution, to a random variable with the same distribution as  $\xi = p(X)$ . Thus, one obtains

$$\lim_{K \to \infty} \mathbb{P} \left( \nu_K \le \ell \right) = \Phi \left( \frac{\sigma \Phi^{-1}(\ell) - H}{\beta} \right), \quad 0 \le \ell \le 1 \tag{7}$$

It follows from equation  $(7)$  that the quantile approximation,  $\ell_q^*$ , corresponding to the probability q, is

$$\ell_q^* = N\Phi\left(\frac{\beta\Phi^{-1}(q) + H}{\sigma}\right) \tag{8}$$

In terms of the general approach, one has  $\theta = \mu$  with  $F_{\theta}(\ell) = \mathbb{1}_{[\mu,\infty)}(\ell) \text{ and } \theta(x) \equiv \mu(x) = K N p(x).$ 

## **Central Limit Theorem**

The heterogeneous case is treated at the outset, as it is no more difficult than the homogeneous case, which is described as a special case at the end. Once again, X is univariate and latent. Denote by  $N_k$ , the loss

given default of the  $k$ th name in the portfolio, and by  $p_k(x)$ , the conditional default probability of the kth name. Then the conditional mean,  $\mu(x)$ , and the conditional variance,  $\sigma^2(x)$ , of the portfolio losses are

$$\mu(x) = \sum_{k=1}^{K} N_k p_k(x),$$
  
$$\sigma^2(x) = \sum_{k=1}^{K} N_k^2 p_k(x) \cdot (1 - p_k(x)) \qquad (9)$$

Under mild conditions on the notionals,  $N_k$  (which are vacuous in the homogeneous case), the conditional distribution of the portfolio losses satisfies

$$\mathbb{P}_{x}\left(\frac{\mathcal{L}-\mu(x)}{\sigma(x)} \leq \ell\right) \to \Phi(\ell) \quad \text{as } K \to \infty$$
(10)

Let a probability,  $q$ ,  $0 < q < 1$ , be fixed and consider the equation

$$q = \mathbb{P}(\mathcal{L} \le \ell_q) \tag{11}$$

for the quantile of the distribution of the random variable  $\mathcal{L}$ . One has

$$\mathbb{P}(\mathcal{L} \leq \ell_q) = \int_{-\infty}^{\infty} \mathbb{P}_x(\mathcal{L} \leq \ell_q) \, \mathrm{d}\Phi(x)$$
$$\stackrel{\cdot}{=} \int_{-\infty}^{\infty} \Phi\left(\frac{\ell_q - \mu(x)}{\sigma(x)}\right) \mathrm{d}\Phi(x) \quad (12)$$

Therefore the quantile approximation,  $\ell_a^*$ , is the solution of the equation

$$q = \int_{-\infty}^{\infty} \Phi\left(\frac{\ell_q^* - \mu(x)}{\sigma(x)}\right) d\Phi(x) \qquad (13)$$

In terms of the general approach, one has  $\theta = (\mu, \sigma)$ with  $F_{\theta}(\ell) = \Phi\left(\frac{\ell-\mu}{\sigma}\right)$  and  $\theta(x) = (\mu(x), \sigma(x)).$ 

In the case of a homogeneous portfolio, considered in  $[14, 13]$  one has the simplifications

$$\mu(x) = K N p(x) \quad \sigma^2(x) = K N^2 \left( p(x) - p^2(x) \right) \tag{14}$$

The normal approximation is just the classical central limit theorem (CLT). The equation for the quantile approximation simplifies to

$$q = \int_{-\infty}^{\infty} \Phi\left(\frac{\ell_q^* / N - Kp(x)}{\sqrt{Kp(x)(1 - p(x))}}\right) \mathrm{d}\Phi(x) \quad (15)$$

#### **Generalized Poisson Approximation**

Consider a homogeneous portfolio, for which the number,  $K$ , of obligors is moderately large but not very large. If also the conditional mean number of default events in the portfolio,  $K \cdot p(x)$ , takes moderate values, the conditional distribution of  $\nu$  might be better approximated by a Poisson distribution

$$\mathbb{P}_x(\nu = m) \doteq \exp\left(-\lambda(x)\right) \frac{\lambda^m(x)}{m!}, \quad m = 0, 1, 2, \dots$$
(16)

than by a normal distribution, where  $\lambda(x) = Kp(x)$ . In this case, the (unconditional) portfolio losses can be approximated by the generalized Poisson distribution: for moderately large  $K$ ,

$$\mathbb{P}(\mathcal{L}=mN) \doteq \int e^{-\lambda(x)} \frac{\lambda^m(x)}{m!} \, \mathrm{d}G_X(x),$$
  
$$m = 0, 1, 2 \dots. \tag{17}$$

In terms of the general approach, one has  $F_{\theta}$  being the Poisson distribution function with mean  $\theta$  and  $\theta(x) = \lambda(x).$ 

In particular, for the quantile approximation, one obtains

$$q = \int \sum_{m=0}^{\ell_q^*/N} e^{-\lambda(x)} \frac{\lambda^m(x)}{m!} dG_X(x) \qquad (18)$$

#### **Compound Poisson Approximation**

In order to extend the result of the previous section to heterogeneous portfolios, one needs to consider compound Poisson distributed random variables. The compound Poisson distribution is a well known approximation in insurance models [11]. In risk management of credit derivatives, the approach was used in [2] and [6] for synthetic collateralized debt obligation (CDO) pricing. The same approach is applicable for approximation of portfolio losses.

In the case of a heterogeneous portfolio, it is not sufficient to approximate the distribution of the number of losses suffered. One must keep track of who defaults or at least the sizes of the individual potential losses because, given only the number of defaults, one cannot infer the losses incurred. To see how this added complexity is handled and how the compound Poisson distribution arises quite naturally, the simplest heterogeneous case is analyzed first; namely, when there are only two distinct recoveryadjusted notional values among the obligors in the portfolio.

Denote by  $N_{(1)}$  and  $N_{(2)}$ , the two distinct values of the recovery-adjusted notionals in the pool. The portfolio then divides into two groups: one with obligors having the common recovery-adjusted notional equaling  $N_{(1)}$ ; the other having common recovery-adjusted notional equaling  $N_{(2)}$ . Denote the number of defaults in each of the two groups, by  $v_1$  and  $v_2$ , respectively. Conditionally, their distributions are independent and can be approximated by a Poisson distribution with conditional mean  $\lambda_i(x) = \sum_{k: N_k = N_{(i)}} p_k(x), i = 1, 2,$ provided both group sizes are moderately large. (This assumption on the group sizes, is only being made in the context of this example.) The total number of defaults in the portfolio,  $\nu = \nu_1 + \nu_2$ , is conditionally Poisson with conditional mean  $\lambda(x) = \lambda_1(x) +$  $\lambda_2(x)$ . The total portfolio loss is the sum of the losses of the first and second groups:

$$\mathcal{L} = \nu_1 N_{(1)} + \nu_2 N_{(2)} \tag{19}$$

As a positive linear combination of conditionally independent Poisson random variables,  $L$  is conditionally a compound Poisson random variable with the same distribution as that of

$$\tilde{\mathcal{L}} := \sum_{j=1}^{\nu} \mathcal{N}^{(j)} \tag{20}$$

where  $\mathcal{N}^{(j)}$  is a conditionally independent and identically distributed (i.i.d.) sequence of random variables, each taking two values,  $N_{(1)}$  and  $N_{(2)}$ , with corresponding conditional probabilities  $\frac{\lambda_1(x)}{\lambda(x)}$  and  $\frac{\lambda_2(x)}{\lambda(x)}$  and conditionally independent of  $\nu$ . (This is an elementary

calculation using the conditional characteristic functions of  $\mathcal{L}$  and  $\mathcal{L}$ .) More formally, the conditional distribution of  $\mathcal{N}^{(j)}$  is

$$f(N;x) \equiv \mathbb{P}_x \left( \mathcal{N}^{(j)} = N \right)$$
$$= \begin{cases} \frac{\lambda_1(x)}{\lambda(x)}, & N = N_{(1)} \\ \frac{\lambda_2(x)}{\lambda(x)}, & N = N_{(2)} \end{cases} \tag{21}$$

In the general case where the recovery-adjusted notionals take more than two values, the conditional distribution of the random variable,  $\mathcal{N}^{(j)}$ , is

$$f(N;x) = \sum_{k:N_k=N} p_k(x)/\lambda(x) \tag{22}$$

where  $\lambda(x) = \sum_{k=1}^{K} p_k(x)$  and N represents a possible individual loss

In the special case where  $p_k$  does not depend on  $k, f$  is simply the relative frequency of the notional values and does not depend on  $x$ :

$$f(N) = [\#k \in \{1, 2, \dots, K\} : N_k = N]/K \quad (23)$$

In general, the function  $f(N;x)$  is a probability mass function with respect to  $N$ , which approximates the conditional probability that the portfolio loss is of size  $N$ , given that there has been only one default.

More generally, it can be shown that

$$\mathbb{P}_{x}(\mathcal{L}=N|\nu=m) \approx f^{*m}(N;x) \tag{24}$$

where  $f^{\star m}$  denotes the *m*-fold convolution of f with itself, as a probability mass function (for notational convenience,  $f^{*1} \equiv f$  and  $f^{*0}(N; x) = 1$  if and only if  $N = 0$ ). Given that there have been exactly m defaults, the pool loss amounts to a sum of  $m$  notional amounts but, as one does not know who defaulted, in the heterogeneous case there is still some randomness left; that randomness is captured (approximately) by  $f^{\star m}$ .

Assuming that a monetary unit has been chosen and that all recovery-adjusted notionals are expressed as integers—that is, integer multiples of the monetary unit—one has the following result  $[6]$ :

**Theorem 1** In the limiting case of a large portfolio  $(K \text{ large})$ , the following approximate equality holds in distribution under  $\mathbb{P}_x$  (i.e., conditional on  $X = x$ ):

*for fixed*  $i = 1, 2, ..., n$ ,

$$\mathcal{L} \stackrel{\mathcal{D}}{\approx} \sum_{m=1}^{\nu} \mathcal{N}^{(m)} \tag{25}$$

where  $(\mathcal{N}^{(m)})_{m=1}^{K}$  is an i.i.d. sequence of random variables with common probability mass function  $f$ and independent of  $v$ , the number of defaults in the pool, which is approximately Poisson distributed under  $\mathbb{P}_r$ 

$$\nu \stackrel{D}{\approx} \text{Pois}(\lambda(x)) \tag{26}$$

More precisely,

$$\max_{N} \left| \mathbb{P}_{x} \left( \mathcal{L} = N \right) - \mathbb{P}_{x} \left( \sum_{m=1}^{\nu} \mathcal{N}^{(m)} = N \right) \right|$$
$$= \mathcal{O} \left( \sum_{k=1}^{K} \left( p_{k}(x) \right)^{2} \right) \tag{27}$$

For the unconditional loss distribution,

$$\mathbb{P}(\mathcal{L} \leq \ell) \doteq \int \sum_{N \leq \ell} \sum_{m=0}^{\infty} f^{*m}(N; x) \frac{e^{-\lambda(x)} \lambda^m(x)}{m!} \, \mathrm{d}G_X(x) \tag{28}$$

In terms of the general approach, one has  $F_{\theta}$  being the compound Poisson distribution function with parameter  $\theta = (\theta_1, \theta_2, \dots, \theta_K) \in [0, 1]^K$  and  $\theta(x) =$  $(p_1(x), p_2(x), \ldots, p_K(x)); F_{\theta}$  is defined as

$$F_{\theta} = \sum_{N \le \ell} \sum_{m=0}^{\infty} f^{\star m}(N) \frac{\mathrm{e}^{-\lambda} \lambda^m}{m!} \tag{29}$$

where  $\lambda := \sum_{k=1}^{K} \theta_k$ ,  $f(N) := \lambda^{-1} \sum_{k: N_k = N} \theta_k$ . In practice, the convolutions, would be calculated recursively using the fast Fourier transform.

#### **Large Deviations**

Approximations based on large deviation theory usually lead to exponential approximations of the tail of the conditional portfolio loss distribution. These approximations are derived using the saddlepoint method for the characteristic function of the portfolio losses,

$$\Psi_{\mathcal{L}}(s) = \mathbb{E}[\exp{(is\mathcal{L})}]\n$$

$$\n= \int \prod_{k=1}^{K} \left(1 - p_k(x) + p_k(x)e^{isN_k}\right) \mathrm{d}G_X(x)\n$$
(30)

The technical details can be found in [1] (see also Saddlepoint Approximation).

### **Other Methods**

There are some methods of approximation that deal only with quantiles of the loss distribution directly, focusing on quantiles with high quantile probability, which is the case of interest for credit risk. The large deviation approximations are examples of such methods.

Another one of these methods is due to Pykhtin [12] who, building on the work of Martin and Wilde [10], adapted the tools of an earlier investigation [4] in market-risk sensitivity to position sizes, to the credit risk setting. Note that this method is a direct. analytical approximation to the quantile of the *unconditional* loss distribution using an approximate model, unlike the other semianalytic methods described so far, which calculate the quantile by making analytical approximations to the conditional loss distribution (conditional on a systemic credit scenario). It is also worth noting that the result is in closed form, a qualitative description of which is given here.

Pykhtin's approach can be described at a high level as follows. It consists of a three-stage series of approximations:

- 1. A single-factor model, which is an approximation based on an LLN type of loss function; that is, it is a Vasicek type of model.
  - The single factor is built as a weighted sum a) of the portfolio's counterparties' credit drivers.
  - b) The weights are chosen to maximize the single factor's correlation with the drivers.
  - The weights use the counterparties' loss c) characteristics such as default probabilities and losses given default.

- 2. An analytic adjustment (approximation) to a full multifactor model that is still based on an LLN type of loss function. This adjustment is called a *multifactor* adjustment.
- An analytic adjustment, bridging the LLN-type 3. loss function of the second stage to the usual Merton-type one with full specific risk. This adjustment is called a *granularity* adjustment.

The reason behind the terminology for the two adjustments, is that for a single-factor model, the multifactor adjustment vanishes, whereas for an infinitely granular portfolio (i.e., a very large, homogeneous one), the granularity adjustment vanishes.

The approximations, in both the second and third stages, are based on a single formula for quantile approximation, due originally to Gourieroux et al. [4]. The formula is a second-order Taylor expansion, for the quantile, in a small parameter that is used to express the full loss model as a perturbation of the single-factor model. The first-order Taylor coefficient is the difference between the single-factor (conditional) loss and the conditional expected loss of the full model, conditional on the single factor. The single factor is constructed so that the first-order Taylor term vanishes.

The second-order Taylor coefficient is related to the conditional variance of the full loss, conditional on the single factor. The well-known conditional variance decomposition from statistics is used to split the Taylor coefficient into two terms, which are the approximations in the second and third stages.

The end result for the entire adjustment to the single-factor quantile, is expressed as a sum of four quadratic forms in the recovery-adjusted exposures, with coefficients involving the bivariate and univariate normal cumulative distribution functions, evaluated in terms of the input statistical parameters of the model. The result is thus in closed form. The reader is referred to  $[12]$  for the quantitative details of the construction, the formulae for the terms in the quantile approximation, and a study of the scope of applicability of the method.

## **End Notes**

<sup>&</sup>lt;sup>a.</sup>This specification is a partial case of the famous Gaussian copula model [9].

## **References**

- [1] Dembo, A., Deushel, J.-D. & Duffie, D. (2004). Large portfolio losses, *Finance and Stochastics* **8**(1), 3–16.
- [2] De Prisco, B., Iscoe, I. & Kreinin, A. (2005). Loss in translation, *Risk* **18**(6), 77–82.
- [3] Gordy, M. (2003). A risk-factor model foundation for ratings-based bank capital rules, *Journal of Financial Intermediation* **12**(3), 199–232.
- [4] Gourieroux, C., Laurent, J.-P. & Scaillet, O. (2000). Sensitivity analysis of values at risk, *Journal of Empirical Finance* **7**, 225–245.
- [5] Huang, X., Oosterlee, C. & Mesters, M. (2007). Computation of VaR and VaR contribution in the Vasicek portfolio credit loss model: a comparative study, *The Journal of Credit Risk* **3**(3), 75–96.
- [6] Iscoe, I. & Kreinin, A. (2007). Valuation of synthetic CDOs, *Journal of Banking and Finance* **31**, 3357–3376.
- [7] Iscoe, I., Kreinin, A. & Rosen, D. (1999). Integrated market and credit risk portfolio model, *Algorithmics Research Quarterly* **2**(3), 21–38.
- [8] Koyluoglu, H.U. & Hickman, A. (1998). *A Generalized Framework for Credit Risk Portfolio Models*, Working paper, CSFP Capital.
- [9] Li, D. (1999). *On Default Correlation: A Copula Function Approach*, The RiskMetrics group, Working paper, 99-07.
- [10] Martin, R. & Wilde, T. (2002). Unsystematic credit risk, *Risk* **15**(11), 123–128.
- [11] Panjer, H. & Willmot, G. (1992). *Insurance Risk Models*, Society of Actuaries, Shaumburg.

- [12] Pykhtin, M. (2004). Multi-factor adjustment, *Risk* March, 85–90.
- [13] Vasicek, O. (1987). *Probability of Loss on Loan Portfolio*, KMV, available at www.kmv.com
- [14] Vasicek, O. (2002). Loan portfolio value, *Risk*, December.

## **Further Reading**

- Emmer, S. & Tasche, D. (2003). *Calculating Credit Risk Capital Charges with the One-Factor Model*, Working Paper, September 2003.
- Gordy, M. (2002). Saddlepoint approximations of credit risk, *Journal of Banking and Finance* **26**, 1335–1353.
- Gordy, M. & Jones, D. (2003). Random tranches, *Risk* March, 78–83.
- Gregory, J. & Laurent, J.-P. (2003). I will survive, *Journal of Risk* **16**(6), 103–108.
- Hull, J. & White, A. (2003). Valuation of a CDO and an *nth* to default CDS without Monte Carlo simulation, *Journal of Derivatives* **12**(2), 8–23.
- Laurent, J.-P. & Gregory, J. (2003). Basket default swaps, CDO's and factor copulas, *Presentation at the Conference Quant'03* , London, September 2003, p. 21, www.defaultrisk. com
- Schonbucher, P. (2003). ¨ *Credit Derivatives Pricing Models*, John Wiley & Sons.

IAN ISCOE & ALEX KREININ
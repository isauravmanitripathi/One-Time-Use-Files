# **Poisson Process**

In this article, we present the main results on Poisson processes, which are standard examples of jump processes. The reader can refer to the books [2, 5] for the study of standard Poisson processes, or  $[1, 3,$ 4, 6] for general Poisson processes.

# **Counting Processes and Stochastic** Integrals

Let  $(T_n, n \ge 0)$  be a strictly increasing sequence of random times (i.e., nonnegative random variables on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  such that  $\lim_{n\to\infty} T_n = \infty$ , with  $T_0 = 0$ . The counting process N associated with  $(T_n, n \ge 0)$  is defined as

$$N_t = \begin{cases} n & \text{if } t \in [T_n, T_{n+1}[\\ +\infty & \text{otherwise} \end{cases} \tag{1}$$

or, equivalently,

$$N_t = \sum_{n\geq 1} \mathbb{1}_{\{T_n \leq t\}} = \sum_{n\geq 1} n \mathbb{1}_{\{T_n \leq t < T_{n+1}\}} \qquad (2)$$

It is an increasing, right-continuous process. We denote by  $N_{t^-}$  the left limit of  $N_s$  when  $s \to t$ ,  $s < t$ and by  $\Delta N_s = N_s - N_{s^-}$  the jump process of N. The stochastic integral of a real-valued process  $C$  with respect to the increasing process  $N$  is defined as

$$(C \star N)_t := \int_0^t C_s \, \mathrm{d}N_s = \int_{]0,t]} C_s \, \mathrm{d}N_s$$
$$= \sum_{n=1}^\infty C_{T_n} \, 1\!\!1_{\{T_n \le t\}} \tag{3}$$

The natural filtration of  $N$  (i.e., the smallest rightcontinuous and complete filtration that makes the process N adapted) is denoted by  $\mathbf{F}^N$ .

# **Standard Poisson Process**

The standard Poisson process is a counting process  $(N_t, t \ge 0)$  with stationary and independent increments, that is,

for every  $s, t \ge 0, N_{t+s} - N_t$  is independent of  $\mathcal{F}_{t}^{N}$ ; and

• for every  $s, t \ge 0$ , the r.v.  $N_{t+s} - N_t$  has the same law as  $N_{\rm s}$ .

For any fixed  $t \ge 0$ , the random variable  $N_t$  has a Poisson law, with parameter  $\lambda t$ , that is,  $\mathbb{P}(N_t = n) =$  $e^{-\lambda t} ((\lambda t)^n/n!)$  and, for every  $x > 0, t > 0, u, \alpha \in \mathbb{R}$ 

$$\mathbb{E}(N_t) = \lambda t, \quad \text{Var}(N_t) = \lambda t$$
  

$$\mathbb{E}(x^{N_t}) = e^{\lambda t (x-1)}; \mathbb{E}(e^{iuN_t}) = e^{\lambda t (e^{iu} - 1)};$$
  

$$\mathbb{E}(e^{\alpha N_t}) = e^{\lambda t (e^{\alpha} - 1)}$$
  
(4)

From the property of independence and stationarity of the increments, it follows that the process  $(M_t)$  $N_t - \lambda t, t \ge 0$  is a martingale. More generally, if H is an  $\mathbf{F}^N$ -predictable<sup>a</sup> bounded process, then the following processes are  $\mathbf{F}^N$ -martingales:

$$(H \star M)_t := \int_0^t H_s \, \mathrm{d}M_s = \int_0^t H_s \, \mathrm{d}N_s - \lambda \int_0^t H_s \, \mathrm{d}s$$
$$((H \star M)_t)^2 - \lambda \int_0^t H_s^2 \, \mathrm{d}s$$
$$\exp\left(\int_0^t H_s \, \mathrm{d}N_s - \lambda \int_0^t (\mathrm{e}^{H_s} - 1) \, \mathrm{d}s\right) \tag{5}$$

In particular, the processes  $(M_t^2 - \lambda t, t \ge 0)$  and  $(M_t^2 - N_t, t \ge 0)$  are martingales. The process  $(\lambda t,$  $t > 0$ ) is the predictable quadratic variation process of *M* (or the compensator of *N*), denoted by  $\langle N \rangle$ , the process  $(N_t, t \ge 0)$  equals in this case its optional quadratic variation, denoted by  $[N]$ .

The above martingale properties do not extend to  $\mathbf{F}^N$ -adapted processes H. For example, from the simple equality  $\int_0^t (N_s - N_{s-}) dM_s = N_t$ , it follows that  $\int_0^t N_s \, \mathrm{d}M_s$  is not a martingale.

#### Predictable Representation Property

**Proposition 1** Let  $N$  be a Poisson process, and  $H_{\infty} \in L^2(\mathcal{F}^N_{\infty})$ , a square-integrable random variable. Then, there exists an  $\mathbf{F}^N$ -predictable process (h.,  $s \ge 0$ ) such that

$$H_{\infty} = \mathbb{E}(H_{\infty}) + \int_{0}^{\infty} h_s \, \mathrm{d}M_s \tag{6}$$

and  $\mathbb{E}\left(\int_0^\infty h_s^2 \, \mathrm{d}s\right) < \infty$ , where  $M_t = N_t - \lambda t$ .

It follows that if X is a square-integrable  $\mathbf{F}^N$ martingale, there exists an  $\mathbf{F}^N$ - predictable process  $(x_s, s \ge 0)$  such that  $X_t = X_0 + \int_0^t x_s \, \mathrm{d}M_s$ .

## Independent Poisson Processes

Here, we assume that the probability space  $(\Omega, \mathcal{F}, \mathbb{P})$ is endowed with a filtration  $\mathbf{F}$ .

A process  $(N^1,\ldots,N^d)$  is a d-dimensional **F**-Poisson process (with  $d > 1$ ) if each  $(N^j, i =$  $1, \ldots, d)$  is a right-continuous **F**-adapted process such that  $N_0^j = 0$ , and if there exist constants  $(\lambda_j, j = 1, \ldots, d)$  such that for every  $t \ge s \ge 0$ ,  $\forall n_i \in \mathbb{N},$ 

$$\mathbb{P}\left[\bigcap_{j=1}^{d}(N_t^j - N_s^j = n_j)|\mathcal{F}_s\right]$$
$$= \prod_{j=1}^{d} e^{-\lambda_j(t-s)} \frac{(\lambda_j(t-s))^{n_j}}{n_j!} \tag{7}$$

**Proposition 2** An  $\mathbf{F}$ -adapted process N is a  $d$ -dimensional **F**-Poisson process if and only if

- 1. each  $N^j$  is an **F**-Poisson process
- 2. no two  $N^j$ 's jump simultaneously.

#### Inhomogeneous Poisson Processes

We assume that the probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  is endowed with a filtration  $\mathbf{F}$ .

## Definition

Let  $\lambda$  be an **F**-adapted nonnegative process satisfying  $\mathbb{E}\left(\int_0^t \lambda_s \, \mathrm{d}s\right) < \infty, \forall t, \text{ and } \int_0^\infty \lambda_s \, \mathrm{d}s = \infty.$ 

An inhomogeneous Poisson process  $N$  with stochastic intensity  $\lambda$  is a counting process such that for every nonnegative **F**-predictable process  $(\phi_t,$  $t \ge 0$ ), the following equality is satisfied:

$$\mathbb{E}\left(\int_0^\infty \phi_s \, \mathrm{d}N_s\right) = \mathbb{E}\left(\int_0^\infty \phi_s \lambda_s \, \mathrm{d}s\right) \qquad (8)$$

Therefore  $(M_t = N_t - \int_0^t \lambda_s \, ds, \, t \ge 0)$  is an **F**martingale, and if  $\phi$  is an **F**-predictable process such that  $\forall t, \ \mathbb{E}(\int_0^t |\phi_s| \lambda_s \, \mathrm{d}s) < \infty$ , then  $(\int_0^t \phi_s \, \mathrm{d}M_s,$  $t \ge 0$ ) is an **F**-martingale. The process  $\Lambda_t = \int_0^t \lambda_s \, ds$ is called the *compensator of*  $N$ .

An inhomogeneous Poisson process with stochastic intensity  $\lambda$  can be viewed as a time change of  $\widetilde{N}$ , a standard Poisson process: indeed, the process  $(N_t = N_{\Lambda_t}, t \ge 0)$  is an inhomogeneous Poisson process with stochastic intensity  $(\lambda_t, t \ge 0)$ .

For  $H$  an **F**-predictable process satisfying some integrability conditions, the following processes are martingales:

$$(H \star M)_t = \int_0^t H_s \, \mathrm{d}M_s = \int_0^t H_s \, \mathrm{d}N_s - \int_0^t \lambda_s H_s \, \mathrm{d}s$$
$$((H \star M)_t)^2 - \int_0^t \lambda_s H_s^2 \, \mathrm{d}s$$
$$\exp\left(\int_0^t H_s \, \mathrm{d}N_s - \int_0^t \lambda_s (\mathrm{e}^{H_s} - 1) \, \mathrm{d}s\right) \tag{9}$$

## Stochastic Calculus

**Integration by Parts Formula.** Let  $dX_t = b_t dt +$  $\varphi_t \, \mathrm{d}M_t$  and  $\mathrm{d}Y_t = c_t \, \mathrm{d}t + \psi_t \, \mathrm{d}M_t$ , where  $\varphi$  and  $\psi$  are predictable processes, and  $b, c$  are adapted processes such that the processes  $X$  and  $Y$  are well defined. Then,

$$X_t Y_t = xy + \int_0^t Y_{s^-} dX_s + \int_0^t X_{s^-} dY_s + [X, Y]_t$$
(10)

where  $[X, Y]_t$  is the quadratic covariation process, defined as

$$[X, Y]_t: = \int_0^t \varphi_s \psi_s \, \mathrm{d}N_s \tag{11}$$

In particular, if  $dX_t = \varphi_t dM_t$  and  $dY_t = \psi_t dM_t$  (i.e., X and Y are local martingales), the process  $(X_t Y_t [X, Y]_t, t \ge 0$  is a martingale. It can be noted that, in that case, the process  $(X_t Y_t - \langle X, Y \rangle_t, t \ge 0)$ ,<br>where  $\langle X, Y \rangle_t = \int_0^t \varphi_s \psi_s \lambda_s \, ds$  is also a martingale. The process  $\langle X, Y \rangle$  is the compensator of  $[X, Y]$ if  $[X, Y]$  is integrable (see **Compensators**). The predictable process  $(\langle X, Y \rangle_t, t \ge 0)$  is called the *predictable covariation process* of the pair  $(X, Y)$ , or the *compensator* of the product XY. If  $dX_t^i = x_t^i dN_t^i$ , where  $N^i$ ,  $i = 1, 2$  are independent inhomogeneous Poisson processes, the covariation processes  $[X^1, X^1]$ and  $\langle X^1, X^2 \rangle$  are null, and  $X^1 X^2$  is a martingale.

Itô's Formula. Itô's formula is a special case of the general one; it is a bit simpler and is used for the processes that are within bounded variation. Let  $b$  be an adapted process and  $\varphi$  a predictable process with adequate integrability conditions, and

$$dX_t = b_t dt + \varphi_t dM_t = (b_t - \varphi_t \lambda_t) dt + \varphi_t dN_t$$
(12)

and  $F \in C^{1,1}(\mathbb{R}^+ \times \mathbb{R})$ . Then, the process  $(F(t, X_t),$  $t > 0$ ) is a semimartingale with decomposition

$$F(t, X_t) = Z_t + A_t \tag{13}$$

where  $Z$  is a local martingale given by

$$Z_{t} = F(0, X_{0})$$
  
+ 
$$\int_{0}^{t} [F(s, X_{s^{-}} + \varphi_{s}) - F(s, X_{s^{-}})] dM_{s} \quad (14)$$

and  $A$  a bounded variation process

$$A_{t} = \int_{0}^{t} \left( \partial_{t} F(s, X_{s}) + b_{s} \partial_{x} F(s, X_{s}) \right.$$
  
$$+ \lambda_{s} \left[ F(s, X_{s} - \varphi_{s}) - F(s, X_{s}) - \varphi_{s} \partial_{x} F(s, X_{s}) \right] \right) \mathrm{d}s \tag{15}$$

#### Exponential Martingales

**Proposition 3** Let  $N$  be an inhomogeneous Poisson process with stochastic intensity  $(\lambda_t, t \ge 0)$ , and  $(\mu_t, t \ge 0)$  a predictable process such that  $\int_0^t |\mu_s| \lambda_s \, ds < \infty$ . Then, the process L defined by

$$L_{t} = \begin{cases} \exp\left(-\int_{0}^{t} \mu_{s} \lambda_{s} \, \mathrm{d}s\right) & \text{if } t < T_{1} \\ \prod_{n, T_{n} \leq t} (1 + \mu_{T_{n}}) \\ \times \exp\left(-\int_{0}^{t} \mu_{s} \lambda_{s} \, \mathrm{d}s\right) & \text{if } t \geq T_{1} \end{cases} \tag{16}$$

is a local martingale solution of

$$L_t = L_{t-} \mu_t \, \mathrm{d}M_t, \quad L_0 = 1 \tag{17}$$

*Moreover, if*  $\mu$  *is such that*  $\forall s, \mu_s > -1$ *,* 

$$L_{t} = \exp\left[-\int_{0}^{t} \mu_{s} \lambda_{s} \, \mathrm{d}s + \int_{0}^{t} \ln(1+\mu_{s}) \, \mathrm{d}N_{s}\right]$$
$$= \exp\left[-\int_{0}^{t} (\mu_{s} - \ln(1+\mu_{s}))\lambda_{s} \, \mathrm{d}s + \int_{0}^{t} \ln(1+\mu_{s}) \, \mathrm{d}M_{s}\right]$$
(18)

The local martingale L is denoted by  $\mathcal{E}(\mu \star M)$  and named the *Doléans-Dade exponential* (alternatively, the *stochastic exponential*) of the process  $\mu \star M$ . If  $\mu > -1$ , the process L is nonnegative and is a martingale if  $\forall t$ ,  $\mathbb{E}(L_t) = 1$  (this is the case if  $\mu$ satisfies  $-1 + \delta < \mu_s < C$  where C and  $\delta > 0$  are two constants).

If  $\mu$  is not greater than  $-1$ , then the process L defined in equation  $(16)$  may take negative values.

#### Change of Probability Measure

Let  $\mu$  be a predictable process such that  $\mu > -1$ , and  $\int_0^t \lambda_s |\mu_s| ds < \infty$ , and let L be the positive exponential local martingale solution of

$$dL_t = L_{t-} \mu_t dM_t, \quad L_0 = 1 \tag{19}$$

Assume that L is a martingale, and let  $\mathbb{Q}$  be the probability measure equivalent to  $\mathbb{P}$  defined on  $\mathcal{F}_t$ by  $\mathbb{Q}|_{\mathcal{F}_t} = L_t \mathbb{P}|_{\mathcal{F}_t}$ . Under  $\mathbb{Q}$ , the process

$$M_t^{\mu} := M_t - \int_0^t \mu_s \lambda_s \, \mathrm{d}s$$
  
=  $N_t - \int_0^t (\mu_s + 1) \lambda_s \, \mathrm{d}s \quad t \ge 0$  (20)

is a local martingale, hence *N* is a  $\mathbb{Q}$ -inhomogeneous Poisson process, with intensity  $\lambda(1+\mu)$ .

#### **Compound Poisson Processes**

#### Definition and Properties

Let  $\lambda$  be a positive number, and  $F(\mathrm{d}y)$  be a probability law on  $\mathbb{R}$ . A  $(\lambda, F)$ -compound Poisson process is a process  $X = (X_t, t \ge 0)$  of the form

$$X_{t} = \sum_{n=1}^{N_{t}} Y_{n} = \sum_{n>0, T_{n} \leq t} Y_{n}$$
 (21)

where  $N$  is a standard Poisson process with intensity  $\lambda > 0$ , and the  $(Y_n, n \ge 1)$  are i.i.d. square-integrable random variables with law  $F(dy) = \mathbb{P}(Y_1 \in dy)$ , independent of  $N$ .

**Proposition 4** A compound Poisson process has  $stationary$  and  $independent$   $increments$ ; for fixed  $t$ , the *cumulative distribution function of*  $X_t$  *is* 

$$\mathbb{P}(X_t \le x) = e^{-\lambda t} \sum_{n=0}^{\infty} \frac{(\lambda t)^n}{n!} F^{*n}(x) \qquad (22)$$

where the star indicates a convolution.

If  $\mathbb{E}(|Y_1|) < \infty$ , the process  $(Z_t = X_t - t\lambda \mathbb{E}(Y_1),$  $t \geq 0$ ) is a martingale and  $\mathbb{E}(X_t) = \lambda t \mathbb{E}(Y_1)$ . If  $\mathbb{E}(Y_1^2) < \infty$ , the process  $(Z_t^2 - t\lambda \mathbb{E}(Y_1^2))$ ,  $t \ge 0$ ) is a martingale and Var  $(X_t) = \lambda t \mathbb{E}(Y_t^2)$ .

Introducing the random measure  $\mu = \sum_{n=1}^{\infty} \delta_{T_n, Y_n}$  on  $\mathbb{R}^+ \times \mathbb{R}$ , that is,

$$\mu(\omega, ]0, t], A) = \sum_{n>0, T_n(\omega) \le t} \mathbb{1}_{Y_n(\omega) \in A} \tag{23}$$

and denoting by  $(f * \mu)_t$ , the integral

$$\int_0^t \int_{\mathbb{R}} f(x) \mu(\omega, \, \mathrm{d}s, \, \mathrm{d}x) = \sum_{n>0, T_n \le t} f(Y_n(\omega))$$
$$= \sum_{n=1}^{N_t} f(Y_n(\omega)) \tag{24}$$

we obtain that

$$M_t^f = (f * \mu)_t - t\lambda \mathbb{E}(f(Y_1))$$
  
= 
$$\int_0^t \int_{\mathbb{R}} f(x)(\mu(\omega, ds, dx) - \lambda F(dx) ds) \tag{25}$$

is a martingale.

#### Martingales

**Proposition 5** If X is a  $(\lambda, F)$ -compound Poisson process, for any  $\alpha$  such that  $\int_{-\infty}^{\infty} e^{\alpha x} F(dx) < \infty$ , the  $process$ 

$$Z_{t} = \exp\left(\alpha X_{t} - \lambda t \int_{-\infty}^{\infty} (e^{\alpha x} - 1) F(dx)\right) \quad (26)$$

is a martingale and

$$\mathbb{E}(\mathrm{e}^{\alpha X_{t}}) = \exp\left(\lambda t \int_{-\infty}^{\infty} (\mathrm{e}^{\alpha x} - 1) F(\mathrm{d}x)\right)$$
$$= \exp\left(\lambda t (\mathbb{E}(\mathrm{e}^{\alpha Y_{1}} - 1))\right) \tag{27}$$

In other words, for any  $\alpha$  such that  $\mathbb{E}(e^{\alpha X_t}) <$  $\infty$  (or equivalently  $\mathbb{E}(e^{\alpha Y_1}) < \infty$ ), the process  $(e^{\alpha X_t}/\mathbb{E}(e^{\alpha \bar{X}_t}), t \ge 0)$  is a martingale. More generally, let  $f$  be a bounded Borel function. Then, the process

$$\exp\left(\sum_{n=1}^{N_t} f(Y_n) - \lambda t \int_{-\infty}^{\infty} (e^{f(x)} - 1) F(dx)\right) \tag{28}$$

is a martingale. In particular,

$$\mathbb{E}\left(\exp\left(\sum_{n=1}^{N_t} f(Y_n)\right)\right)$$
$$=\exp\left(\lambda t \int_{-\infty}^{\infty} (e^{f(x)} - 1) F(dx)\right) \qquad (29)$$

#### Change of Measure

Let X be a  $(\lambda, F)$ -compound Poisson process,  $\tilde{\lambda} > 0$ , and  $\tilde{F}$  a probability measure on  $\mathbb{R}$ , absolutely continuous with respect to  $F$ , with Radon-Nikodym density  $\varphi$ , that is,  $F(\mathrm{d}x) = \varphi(x)F(\mathrm{d}x)$ . The process

$$L_{t} = \exp\left(t(\lambda - \widetilde{\lambda}) + \sum_{s \leq t} \ln\left(\frac{\widetilde{\lambda}}{\lambda} \varphi(\Delta X_{s})\right)\right) \tag{30}$$

is a positive martingale (take  $f(x) = \ln((\tilde{\lambda}/\lambda) \varphi(x))$ in equation (28)) with expectation 1. Set  $d\mathbb{Q}|_{\mathcal{F}}$  =  $L_t d\mathbb{P}|_{\mathcal{F}_t}$ .

**Proposition 6** Under  $\mathbb{Q}$ , the process X is a  $(\widetilde{\lambda}, \widetilde{F})$ compound Poisson process.

Let  $\alpha$  be such that  $\mathbb{E}(e^{\alpha Y_1}) < \infty$ . The particular case with  $\varphi(x) = (e^{\alpha x}/\mathbb{E}(e^{\alpha Y_1}))$  and  $\widetilde{\lambda} = \lambda \mathbb{E}(e^{\alpha Y_1})$ corresponds to the Esscher transform for which

$$d\mathbb{Q}|_{\mathcal{F}_t} = \frac{e^{\alpha X_t}}{\mathbb{E}(e^{\alpha X_t})} d\mathbb{P}|_{\mathcal{F}_t}$$
(31)

We emphasize that there exist changes of probability that do not preserve the compound Poisson process property. For the predictable representation theorem, see Point Processes.

### *An Example: Double Exponential Model*

# **References**

The compound Poisson process is said to be a double exponential process if the law of the random variable *Y*<sup>1</sup> is

$$F(\mathrm{d}x) = \left(p\theta_1 \mathrm{e}^{-\theta_1 x} \mathbbm{1}_{\{x>0\}} + (1-p)\theta_2 \mathrm{e}^{\theta_2 x} \mathbbm{1}_{\{x<0\}}\right) \mathrm{d}x$$
(32)

where *p* ∈]0*,* 1[ and *θi, i* = 1*,* 2 are positive numbers. Under an Esscher transform, this model is still a double exponential model. This particular dynamic allows one to compute the Laplace transform of the first hitting times of a given level.

# **End Notes**

a*.* We recall that adapted continuous-on-left processes are predictable. The process *N* is not predictable.

- [1] Bremaud, P. (1981). ´ *Point Processes and Queues: Martingale Dynamics*, Springer-Verlag, Berlin.
- [2] ¸Cinlar, E. (1975). *Introduction to Stochastic Processes*, Prentice Hall.
- [3] Cont, R. & Tankov, P. (2004). *Financial Modeling with Jump Processes*, Chapman & Hall/CRC.
- [4] Jeanblanc, M., Yor, M. & Chesney, M. (2009). *Mathematical Models for Financial Markets*, Springer, Berlin.
- [5] Karlin, S. & Taylor, H. (1975). *A First Course in Stochastic Processes*, Academic Press, San Diego.
- [6] Protter, P.E. (2005). *Stochastic Integration and Differential Equations*, 2nd Edition, Springer, Berlin.

# **Related Articles**

**Levy Processes ´** ; **Martingales**; **Martingale Representation Theorem**.

MONIQUE JEANBLANC
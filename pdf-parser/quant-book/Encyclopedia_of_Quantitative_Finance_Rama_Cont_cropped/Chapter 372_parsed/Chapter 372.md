# **Stochastic Volatility Models: Extremal** Behavior

Extreme value theory for financial models mostly concerns the martingale (see **Martingales**) component of the logarithm of a price process, since random volatility determines the extreme risk in price fluctuations. The increments  $(Y_n)_{n\in\mathbb{Z}}$  and  $(Y_t)_{t\in\mathbb{R}}$  of length 1 of this martingale part often have the structure

$$Y_n = \sigma_n \varepsilon_n, \quad n \in \mathbb{Z}, \quad \text{or}$$
  
$$Y_t = \int_{(t-1,t)} \sigma_{s-} \, \mathrm{d}L_s, \quad t \in \mathbb{R} \tag{1}$$

for a discrete-time or continuous-time model, respectively. Here, the volatility is modeled by  $\sigma$ , and  $(\varepsilon_n)_{n\in\mathbb{Z}}$  or  $(L_t)_{t\in\mathbb{R}}$  are typically independent and identically distributed (i.i.d.) sequences or a Lévy process (see Lévy Processes), respectively. The usual prerequisite of extreme value theory for a stochastic process is its strict stationarity. Note that, in most cases, strict stationarity of the log price increment process  $Y$  is inherited from stationarity of the volatility process  $\sigma$ . Consequently, we present conditions for strict stationarity of the models below, followed by the extremal analysis of a stationary version.

The importance of extreme value theory for such pricing models is twofold. First, the tail behavior for large absolute arguments describes the fluctuations of the prices. We distinguish between light- and heavy-tailed models: light tailed means normal or exponential models, whereas heavy-tailed models are defined *via* regular variation. We say a random variable  $X$  has regularly varying tail, if there are  $\alpha > 0$  and slowly varying  $\ell : (0, \infty) \to (0, \infty)$ , that is,  $\lim_{x\to\infty} \ell(tx)/\ell(x) = 1$  for all  $t > 0$ , such that

$$P(X > x) = \ell(x)x^{-\alpha}, \quad x > 0 \tag{2}$$

We write  $X \in \mathcal{R}(-\alpha)$ . If the volatility  $\sigma$  has regularly varying tail and the noise  $\varepsilon$  or L is light tailed and independent of the volatility, then the log price increments are again regularly varying by Breiman's classical result. The same holds for a light-tailed volatility and independent regularly varying noise. If both, volatility and noise, are light tailed, the distribution of the product depends even asymptotically on both factors and may be more difficult to estimate. Symmetry or tail balance of the right and left tails of the noise often simplifies the calculations.

Second, volatility clusters on high levels induce extreme price clusters, which can cause a particularly risky situation. For discrete-time models, such clusters are described by a limit of point processes of exceedances over high thresholds. For certain models, this limit is simply a Poisson process, indicating that exceedances happen as single points and at completely random times. However, more realistic models capture the fact that the limit process is not a Poisson process but a compound Poisson process, which describes also the cluster size distribution. A crude, but simple, measure of the cluster size of extremes is the *extremal index*  $\theta \in (0, 1]$ , where  $1/\theta$ can be interpreted as the mean size of a cluster. It also appears in the distributional limit of the running maxima

$$M_n^Z = \max\{Z_1, \dots, Z_n\}, \quad n \in \mathbb{N} \tag{3}$$

of a stationary sequence  $(Z_n)_{n \in \mathbb{Z}}$ . More precisely, under weak conditions on  $Z_1$ , there exist  $a_n > 0$  and  $b_n \in \mathbb{R}$  such that the *Poisson condition* 

$$nP(Z_1 > a_n x + b_n) = -\log G(x), \quad x \in \mathbb{R} \quad (4)$$

holds, and if the process satisfies further mixing conditions, then the extremal index of  $(Z_n)_{n\in\mathbb{Z}}$  is the unique number  $\theta \in (0, 1]$  such that

$$\lim_{n \to \infty} P(a_n^{-1}(M_n^Z - b_n) \le x) = G^{\theta}(x), \quad x \in \mathbb{R}$$
(5)

Here,  $G$  is an extreme value distribution, that is, it is of the same type as a Fréchet distribution  $\Phi_{\alpha}(x) = \mathbf{1}_{(0,\infty)}(x) \exp(-x^{-\alpha})$  for some  $\alpha > 0$ (heavy-tailed case), a Gumbel distribution  $\Lambda(x)$  =  $\exp(-e^{-x})$  (light-tailed case), or a Weibull distribution  $\Psi_{\alpha}$  for some  $\alpha > 0$ . We refer to the books [11, 24] for this and further information about extreme value theory.

For  $\theta = 1$ , we interpret the stochastic process as a process without clusters in the extremes, whereas if  $\theta$  < 1 we speak of a process with cluster possibilities in the extremes. Using a point process approach, the whole cluster size distribution can be derived, giving much more insight into the extremal behavior of time series models. This, however, would go beyond the scope of this article and we refer to the references given throughout for more details.

As for discrete-time models, the extremal behavior of continuous-time models can be described by the limit behavior of point processes. A simple measure is again given by an extension of the extremal index: if  $(Z_t)_{t \in \mathbb{R}}$  is a continuous-time process, we define for fixed  $h > 0$  the discrete-time process

$$M_k^Z(h) := \sup_{(k-1)h \le t \le kh} Z_t, \quad k \in \mathbb{Z} \tag{6}$$

Denoting  $\theta(h)$  as the extremal index of the sequence  $(M_k^Z(h))_{k\in\mathbb{Z}}$ , we follow [13] and call  $\theta(h)$ for  $h \in (0, \infty)$  the *extremal index function* of Z. The function  $\theta$  is increasing, and we shall say that the continuous-time process  $Z$  has extremal clusters if  $\lim_{h\to 0} \theta(h) < 1$ , that is, if there is some  $h > 0$  such that the discrete skeleton  $(M_k^Z(h))_{k\in\mathbb{Z}}$  has extremal index less than 1, that is, it clusters.

There exist various publications on extreme value theory for time-dependent data; we mention, for example,  $[7, 8, 11, 17-20, 24]$  and references therein.

#### **Discrete-time Stochastic Volatility Models**

The simple stochastic volatility model is given by

$$Y_n = \sigma_n \varepsilon_n, \quad \log \sigma_n^2 = \alpha_0 + \sum_{j=0}^{\infty} c_j \eta_{n-j}, \quad n \in \mathbb{Z}$$
(7)

where  $(\eta_n)_{n\in\mathbb{Z}}$  is i.i.d.  $N(0, s^2)$  with  $\sum_{i=0}^{\infty} c_i^2 < \infty$ and  $(\varepsilon_n)_{n\in\mathbb{Z}}$  is i.i.d., independent of  $(\eta_n)_{n\in\mathbb{Z}}$ . This covers the case when  $(\log \sigma_n^2)_{n \in \mathbb{Z}}$  is a causal ARMA process with i.i.d. Gaussian noise  $(\eta_n)_{n\in\mathbb{Z}}$ , the most prominent case being the volatility model of Taylor [28]:

$$Y_n = \sigma_n \varepsilon_n, \quad \log \sigma_n^2 = \alpha_0 + \psi \log \sigma_{n-1}^2 + \eta_n,$$
  
$$n \in \mathbb{Z}, \quad |\psi| < 1 \tag{8}$$

when the log volatility is a causal Gaussian  $AR(1)$ process.

Extreme value analysis for equation  $(7)$  is based on the transformation

$$X_n = \log Y_n^2 = \alpha_0 + \sum_{j=0}^{\infty} c_j \eta_{n-j}$$
$$+ \log \varepsilon_n^2, \quad n \in \mathbb{Z}$$
(9)

which is a Gaussian linear process plus an i.i.d. noise. From  $[5, 7]$  we have the following theorem:

**Theorem 1** (Tail Behavior and Extremes of the Stochastic Volatility Model). Assume the stochastic volatility model (7) as above with  $X_n$  defined by equation (9).

(a) If  $\varepsilon_1$  is  $N(0, 1)$  denote  $\widetilde{s}^2 = s^2 \sum_{i=0}^{\infty} c_i^2$  and  $k = \log(2/\widetilde{s}^2)$ .

Then the tail of the stationary process  $(X_n)_{n\in\mathbb{Z}}$ satisfies as  $x \to \infty$ 

$$P(X_1 > x + \alpha_0) = \frac{\widetilde{s}^2}{\sqrt{\pi}} \exp\left\{-\frac{x^2}{2\widetilde{s}^2} + \frac{x \log x}{\widetilde{s}^2} + \frac{(k-1)x}{\widetilde{s}^2} + \frac{(k+\widetilde{s}^2)\log x}{\widetilde{s}^2} - \frac{(\log x)^2}{2\widetilde{s}^2} - \frac{k^2}{2\widetilde{s}^2} + O\left(\frac{(\log x)^2}{x}\right)\right\}$$
(10)

The tail of the stationary log price increments is given by

$$P(Y_1 > \sqrt{y}) = \frac{1}{2}P(|Y_1| > \sqrt{y})$$
  
=  $\frac{1}{2}P(X_1 > \log y), \quad n \in \mathbb{Z} \tag{11}$ 

If, furthermore, the autocorrelation function  $\rho$  of  $(\log \sigma_n^2)_{n \in \mathbb{Z}}$  satisfies

$$\rho(h) = \text{corr}(\log \sigma_n^2, \log \sigma_{n+h}^2)$$
$$= o((\log h)^{-1}), \quad h \to \infty \tag{12}$$

then each of the sequences  $(X_n)_{n\in\mathbb{Z}}$  and  $(Y_n)_{n\in\mathbb{Z}}$  has extremal index 1, and the extreme value distribution  $G$  appearing in equations (4) and (5) is the Gumbel distribution  $\Lambda$  for both X and Y.

(b) Assume that  $\varepsilon_1 \in \mathcal{R}(-\alpha)$  for some  $\alpha > 0$ . Then as  $x \to \infty$  we have

$$P(Y_1 > x) \sim E(\sigma_1^{\alpha}) P(\varepsilon_1 > x) \tag{13}$$

If, moreover, for  $p \in (0, 1]$  the tail balance condition for  $x \to \infty$   $P(\varepsilon_1 > x) \sim p P(|\varepsilon_1| > x)$  holds, then  $(Y_n)_{n\in\mathbb{Z}}$  has extremal index 1 and the extreme value distribution G appearing in  $(4)$  and  $(5)$  is the Fréchet distribution  $\Phi_{\alpha}$ .

Here,  $f(x) \sim g(x)$  as  $x \to \infty$  for two strictly positive functions f and g means that  $\lim_{x\to\infty} f(x)$  $g(x) = 1$ . Berman's condition (12) is very weak and, for example, satisfied, whenever  $\log \sigma_n^2$  follows a causal ARMA equation (in particular, for the volatility model (8) of Taylor). This means that for most stochastic volatility models (7) with Gaussian  $\eta$ and either light- or heavy-tailed noise  $\varepsilon$ , the extremal index is 1, so that the point processes of exceedances over high thresholds converge to a Poisson process. The model cannot model clusters of extremes.

Extensions of the  $\eta_n$  to non-Gaussian random variables in equation (7) have been considered. In most cases, the qualitative behavior remains the same provided that the processes  $\sigma$  and  $\varepsilon$  are independent and  $\n\eta_1\n$  is light-tailed [9, 10, 22].

#### EGARCH model

A model related to stochastic volatility models is the EGARCH model of Nelson [26] given by

$$Y_n = \sigma_n \varepsilon_n, \quad \log \sigma_n^2 = \alpha_0 + \sum_{j=1}^{\infty} c_j g(\varepsilon_{n-j}), \quad n \in \mathbb{Z}$$
(14)

where  $(\varepsilon_n)_{n\in\mathbb{Z}}$  is i.i.d. normal (or more generally follows a generalized error distribution  $\text{GED}(v)$ ), the real coefficients  $\alpha_0$  and  $(c_j)_{j \in \mathbb{N}}$  decay sufficiently fast, and  $g$  is a deterministic function. The infinite moving average representation for  $\log \sigma^2$  typically arises from EGARCH $(p, q)$  equations of the form

$$\log \sigma_n^2 = \alpha_0 + \sum_{j=1}^p \alpha_j g(\varepsilon_{n-j}) + \sum_{j=1}^q \beta_j \log(\sigma_{n-j}^2)$$
(15)

with real coefficients  $\alpha_i$  and  $\beta_i$ . The standard choice for g is  $g(x) = \varphi x + \gamma(|x| - E|\varepsilon_0|)$ , where  $\varphi$  and  $\gamma$  are real constants, so that g is an affine linear function and  $g(\varepsilon_n)$  allows the volatility to respond asymmetrically to negative and positive innovations. Depending on the size of  $\varphi$  and  $\gamma$ , different cases arise, but the most important one is for  $\gamma - \varphi > \gamma +$  $\varphi > 0$ , in which case a negative innovation increases the volatility more than a positive innovation of the same modulus (i.e., it models the leverage effect).

As for stochastic volatility models, extreme value analysis for equation  $(14)$  is based on the transformed process (which is stationary by equation  $14$ )

$$X_{n} = \log Y_{n}^{2}$$
  
=  $\alpha_{0} + \sum_{j=1}^{\infty} c_{j} g(\varepsilon_{n-j}) + \log \varepsilon_{n}^{2}, \quad n \in \mathbb{Z}$   
(16)

The following theorem follows from  $[9, 10, 22]$ :

Theorem 2 (Tail Behavior and Extremes of EGARCH). Assume the EGARCH model as above with  $(\varepsilon_n)_{n\in\mathbb{N}}$  i.i.d.  $N(0,1)$  and  $\gamma-\varphi>\gamma+\varphi>$ 0. Suppose further that the coefficients  $(c_i)_{i \in \mathbb{N}}$  are nonnegative and that  $c_j = O(j^{-\delta})$  as  $j \to \infty$  for *some*  $\delta > 1$ . *Denote* 

$$A := (\gamma - \varphi)^2 \sum_{j=1}^{\infty} c_j^2 \quad \text{and} \quad B := -\gamma E |\varepsilon_0| \sum_{j=1}^{\infty} c_j$$
(17)

*Then the stationary processes*  $(X_n)_{n\in\mathbb{Z}}$  *and*  $(Y_n)_{n\in\mathbb{Z}}$ satisfy, as  $x \to \infty$ ,

$$P(X_1 > \alpha_0 + x) = \exp\left(-[x^2 - x \log x - (B + \log(2/A) - 1)x]/A + o(x)\right)$$
(18)

and (11), respectively. Both processes  $(X_n)_{n\in\mathbb{Z}}$  and  $(Y_n)_{n\in\mathbb{Z}}$  have extremal index 1, and the extreme value distribution G appearing in equation  $(4)$  and  $(5)$  is the Gumbel distribution.

Observe that for an EGARCH $(p, q)$  process as in equation (15) with  $\alpha_1, \ldots, \alpha_p, \ \beta_1, \ldots, \beta_q \ge 0$ and such that  $\sum_{j=1}^{q} \beta_j < 1$ , the coefficients  $(c_j)_{j \in \mathbb{N}}$ 

in equation  $(14)$  are automatically nonnegative and decay exponentially, so that Theorem 2 applies. In particular, the EGARCH process with normal innovations cannot cluster. Extensions to other light-tailed innovations  $\varepsilon$  such as GED(v) distributions with  $\nu > 1$  are possible; cf [10].

### GARCH(1.1) Model

In the GARCH(1,1) model (see GARCH Models) of Engle [12] and Bollerslev [4] the log price increments  $(Y_n)_{n\in\mathbb{Z}}$  and the volatilities  $(\sigma_n)_{n\in\mathbb{Z}}$  are given by

$$Y_n = \sigma_n \varepsilon_n, \quad \sigma_n^2 = \gamma + \alpha Y_{n-1}^2 + \beta \sigma_{n-1}^2, \quad n \in \mathbb{Z}$$
(19)

where  $(\varepsilon_n)_{n\in\mathbb{Z}}$  are i.i.d. and  $\alpha, \beta, \gamma > 0$ . Rewriting

$$\sigma_{n+1}^2 = \gamma + (\alpha \varepsilon_n^2 + \beta)\sigma_n^2, \quad n \in \mathbb{Z} \tag{20}$$

it becomes clear that a stationary and causal solution exists if and only if  $E \log(\alpha \varepsilon_1^2 + \beta) < 0$ . The following result on the tail behavior is included in Kesten's seminal work: see [8] for further results and references. The calculation of the extremal index can be found in [19, 25].

Theorem 3 (Tail Behavior and Extremes of  $GARCH(1,1)$ ). Assume the  $GARCH(1,1)$  model such that  $\varepsilon_1$  is symmetric and has a positive density on  $\mathbb{R}$ such that  $E(|\varepsilon_1|^h) < \infty$  for  $h < h_0$  and  $E(|\varepsilon_1|^{h_0}) =$  $\infty$  for  $h \ge h_0$  for some  $h_0 \in (0, \infty]$ . Then there exist unique  $\kappa > 0$  and  $c > 0$  such that

$$E(\alpha \varepsilon_1^2 + \beta)^{\kappa/2} = 1 \tag{21}$$

and the stationary distributions have tails for  $x \to \infty$ 

$$P(\sigma_1 > x) \sim cx^{-\kappa} \quad and$$
  
$$P(Y_1 > x) \sim \frac{1}{2} cE(|\varepsilon_1|^{\kappa}) x^{-\kappa}$$
(22)

The extremal indices of  $(\sigma_n)_{n\in\mathbb{Z}}$  and  $(|Y_n|)_{n\in\mathbb{Z}}$  are given by

$$\theta_{\sigma} = \int_{1}^{\infty} P\left(\sup_{n\geq 1} \prod_{j=1}^{n} (\alpha \varepsilon_{j}^{2} + \beta) \leq y^{-1}\right)$$

$$\times \frac{\kappa}{2} y^{-(\kappa/2)-1} \, \mathrm{d}y \in (0, 1) \quad \text{and}\n$$

$$\n\theta_{|Y|} = \frac{E\left(|\varepsilon_1|^{\kappa} - \sup_{m \ge 1} |\varepsilon_{m+1}|^{\kappa} \prod_{j=1}^m (\alpha \varepsilon_j^2 + \beta)^{\kappa/2}\right)^+}{E|\varepsilon_1|^{\kappa}}\n$$

$$\n\in (0, 1) \tag{23}$$

respectively. Also the extremal index  $\theta_Y \in (0, 1)$ , and for all three sequences  $\sigma$ ,  $|Y|$  and  $Y$ , the extreme value distribution  $G$  appearing in equations (4) and (5) is the Fréchet distribution  $\Phi_{\kappa}$ .

We conclude that the  $GARCH(1,1)$  process is able to model clusters in the extremes. Extensions to higher order GARCH processes are given in [3, 8].

# **Continuous-time Models**

While for discrete-time volatility models many results on the extremal behavior are formulated for both the volatility process and the log price increments process, with few exceptions, most of the literature on extremes for continuous-time models concentrates on the volatility process. Hence, in the following, we often state results concerning the volatility process only.

#### The Wiggins Model

In the volatility model of Wiggins [30] (see also [27]) the log volatility is modeled as a Gaussian Ornstein-Uhlenbeck (OU) process. More precisely, the log price increments  $Y_t$  and the volatility  $\sigma_t$  are given by

$$Y_{t} = \int_{(t-1,t)} \sigma_{s-} \, \mathrm{d}B_{s},$$
  
$$\mathrm{d} \log \sigma_{t}^{2} = (b_{1} - b_{2} \log \sigma_{t}^{2}) \, \mathrm{d}t + \delta \, \mathrm{d}W_{t},$$
  
$$t \in \mathbb{R} \tag{24}$$

with two independent standard Brownian motions  $B$ and W, and real constants  $b_1$ ,  $b_2$  and  $\delta \neq 0$ . The volatility has a stationary solution if and only if  $b_2 > 0$ , in which case it is given by

$$\log \sigma_t^2 = \int_{-\infty}^t e^{-b_2(t-s)} (b_1 \, \mathrm{d}s + \delta \, \mathrm{d}W_s), \quad t \in \mathbb{R}$$

 $(25)$ 

Sampling the log volatility at integer points results in a causal Gaussian  $AR(1)$  process, so that the Euler type approximation  $\overline{Y}_n := \sigma_{n-1}(B_n - B_{n-1})$  to equation  $(24)$  is the discrete-time volatility model  $(8)$ of Taylor.

From the above representation, it is clear that  $\log \sigma_t^2$  is  $N(b_1/b_2, \delta^2/(2b_2))$  distributed. The extremal index function of  $\log \sigma^2$  and hence  $\sigma^2$ follows from results in [24] as shown in [13].

Theorem 4 (Extremal Index Function of the Volatility). Under the assumptions above, the extremal index function  $\theta_{\sigma}(h)$  for  $h \in (0, \infty)$  of the stationary volatility process  $\sigma^2$  in (24) is identical to 1.

We conclude that the volatility in the model (24) does not allow for extremal clusters. This continues to hold if the Gaussian OU process for the log volatility in equation  $(24)$  is replaced by any Gaussian process with continuous sample paths satisfying equation (12). While it is easy to show that the stationary log price increment  $Y_1$ in equation (24) is distributed as  $\left(\int_0^1 \sigma_t^2 dt\right)^{1/2} \varepsilon_1$ with  $\varepsilon_1$  standard normally distributed and independent of  $(\sigma_t)_{t \in \mathbb{R}}$ , we are not aware of any explicit expressions for the tail behavior and the extremal index function of  $Y_1$  or  $\log Y_1^2$  as in Theorem  $1(a)$ .

#### Barndorff-Nielsen and Shephard (BNS) Model

In [1, 2], Barndorff-Nielsen and Shephard (BNS) model (see Barndorff-Nielsen and Shephard (BNS) **Models**) the volatility process as a Lévy-driven OU process, which results in the model

$$Y_{t} = \int_{(t-1,t)} \sigma_{s-} \, \mathrm{d}B_{s},$$
  
$$\sigma_{t}^{2} = \int_{-\infty}^{t} \mathrm{e}^{-\lambda(t-s)} \, \mathrm{d}L_{\lambda s}, \quad t \in \mathbb{R} \tag{26}$$

where B is Brownian motion,  $\lambda > 0$  and L is a Lévy process with increasing sample paths (i.e., a subordinator), independent of  $B$ . The volatility process is stationary and satisfies the stochastic differential equation (SDE)  $d\sigma_t^2 = -\lambda \sigma_t^2 dt + dL_{\lambda t}$ .

The extremal behavior of this model depends on the driving Lévy process and has been analyzed in  $[13-15]$ . For regularly varying noise, as shown in [14], one obtains the following.

**Theorem 5** (Tail and Extremes for Noise in  $\mathcal{R}(-\alpha)$ ). Consider the stationary BNS-model (26) and assume that  $L_1 \in \mathcal{R}(-\alpha)$  with  $\alpha > 0$ . Then  $\sigma_1 \in$  $\mathcal{R}(-2\alpha)$ ,  $Y_1 \in \mathcal{R}(-2\alpha)$  and we have for  $x \to \infty$ 

$$P(\sigma_1^2 > x) \sim \alpha^{-1} P(L_1 > x)$$
  
$$P(Y_1^2 > x) \sim E(|\varepsilon_1|^{2\alpha}) \left(\frac{(1 - e^{-\lambda})^{\alpha}}{\alpha \lambda^{\alpha}} + \frac{1}{\lambda^{\alpha}} \int_0^1 (1 - e^{s - \lambda})^{\alpha} ds\right) P(L_1 > x)$$

 $P(Y_1 > x) = \frac{1}{2}P(Y_1^2 > x^2)$  $(27)$ 

respectively, where  $\varepsilon_1$  is a standard normal random variable. The extremal index function  $\theta_{\sigma}$  of the *volatility process is furthermore given by* 

$$\theta_{\sigma}(h) = (h\alpha\lambda)(h\alpha\lambda + 1)^{-1}, \quad h > 0 \tag{28}$$

Observe that for a regularly varying noise process, the tail of  $\sigma^2$  is of the same order as that of the driving noise process. Also, since  $\theta_{\sigma}(h) < 1$ , the process exhibits cluster possibilities. This is in contrast to the case when  $L$  has exponential tail as in the next theorem; see  $[13, 18]$ :

**Theorem 6** (Tail and Extremes for Exponential-type Noise). Consider the stationary BNS-model (26) as above and assume that  $L_1$  has an exponential-type distribution tail:

$$P(L_1 > x)$$
  
=  $c(x) \exp\left\{-\int_0^x (a(y))^{-1} dy\right\}, \quad x > 0$   
(29)

where  $\lim_{x\to\infty} c(x) = c > 0$  and  $a > 0$  is absolutely *continuous with*  $\lim_{x\to\infty} a(x) = \gamma^{-1}$  and  $\lim_{x\to\infty}$  $a'(x) = 0$ , where  $\gamma \in [0, \infty)$ . Assume also that  $L_1 \in S(\gamma)$ , that is,  $P(L_2 > x) \sim E(e^{\gamma L_1})P(L_1 > x)$ as  $x \to \infty$  with  $E(e^{\gamma L_1}) < \infty$ . Then

$$P(\sigma_1^2 > x) \sim \frac{a(x)}{x} \frac{E e^{\gamma \sigma_1^2}}{E e^{\gamma L_1}} P(L_1 > x), \quad x \to \infty$$
(30)

In particular,  $P(\sigma_1^2 > x) = o(P(L_1 > x))$  for  $x \to \infty$ . The extremal index function  $\theta_{\sigma}$  is equal to 1, that is,  $\theta_{\sigma}(h) = 1$  for all  $h > 0$ .

Brockwell [6] suggests to model the volatility in equation (26) by Lévy-driven continuous-time ARMA (CARMA) processes, with the  $CAR(1)$  process being the OU process. As shown in [13-15], for CARMA processes driven by regularly varying noise processes, clusters occur as in Theorem 5, while for driving Lévy processes as described in Theorem 6, CARMA processes may or may not model clusters, depending on the corresponding kernel function. Todorov and Tauchen [29] suggest to model the volatility by a  $CARMA(2,1)$  process with a mixture of gamma distributions as driving noise process. For this model the results presented here do not apply.

#### Continuous-time GARCH(1,1) Models

As a diffusion limit of  $GARCH(1,1)$  processes, Nelson [26] obtained

$$Y_t = \int_{(t-1,t)} \sigma_{s-} \, \mathrm{d}B_s,$$
  
$$\mathrm{d}\sigma_t^2 = (\beta - \varphi \sigma_t^2) \, \mathrm{d}t + \lambda \sigma_t^2 \, \mathrm{d}W_t, \quad t \ge 1 \quad (31)$$

where  $B$  and  $W$  are independent standard Brownian motions and  $\beta \geq 0, \lambda > 0$  and  $\varphi \in \mathbb{R}$  are parameters. It has a strictly stationary solution if and only if  $2\varphi/\lambda^2 > -1$  and  $\beta > 0$ , in which case the marginal distribution is inverse gamma. The two independent driving processes in equation  $(31)$  are in contrast to the situation for discrete-time GARCH processes, where price and volatility are both driven by the same noise sequence  $(\varepsilon_n)_{n\in\mathbb{Z}}$ . Inspired by this, Klüppelberg et al. [23] constructed another continuous-time GARCH model, termed COGA- $RCH(1,1)$ , which meets the features of discrete-time GARCH better and for which the volatility jumps, unlike for the diffusion limit (31). Let  $(L_t)_{t\geq 0}$  be a Lévy process with nonzero Lévy measure and  $\eta, \varphi, \beta > 0$  be parameters. Defining the auxiliary Lévy process

$$R_{t} = \eta t - \sum_{0 < s \le t} \log(1 + \varphi(\Delta L_{s})^{2}), \quad t \ge 0 \quad (32)$$

the log price increments Y and the volatility  $\sigma$  are given by

$$Y_{t} = \int_{(t-1,t)} \sigma_{s-} \mathrm{d}L_{s},$$
  
$$\sigma_{t}^{2} = \left(\beta \int_{0}^{t} \mathrm{e}^{R_{s-}} \mathrm{d}s + \sigma_{0}^{2}\right) \mathrm{e}^{-R_{t}}, \ t \ge 1 \quad (33)$$

where  $\sigma_0^2$  is independent of L. A sufficient condition for strict stationarity of  $(33)$  is the existence of some  $\kappa > 0$  such that

$$|L_1|^{\kappa} \log^+ |L_1| < \infty \quad \text{and} \quad E(e^{-R_1 \kappa/2}) = 1 \quad (34)$$

Observe that the volatility in Nelson's diffusion limit (31) has also a solution (33), with  $R_t$  defined by

$$R_t := (\varphi + \lambda^2/2)t - \lambda W_t, \quad t \ge 0 \tag{35}$$

For the stationary choice, we have

$$E(e^{-R_1\kappa/2}) = 1$$
 with  $\kappa := 2 + 4\varphi/\lambda^2 > 0$  (36)

The following result is from  $[16, 18]$ :

**Theorem 7** (Tail and Extremes of Continuous-time GARCH). *Consider the stationary diffusion limit (31)* or COGARCH(1,1) process as above with  $\kappa > 0$  as given by equations  $(36)$  or  $(34)$ , respectively. Then there exists a constant  $c > 0$  such that

$$P(\sigma_1 > x) \sim c x^{-\kappa}, \quad x \to \infty \tag{37}$$

In the case of the  $COGARCH(1,1)$  process, assume *further that there is*  $d > \max\{1, \kappa\}$  *such that*  $E|L_1|^{2d}$  $< \infty$  with  $\kappa > 0$  as defined in equation (34) and that  $L$  is not the negative of a subordinator. Denote  $M_t := B_t$  for the diffusion limit (31) and  $M_t := L_t$  for the  $COGARCH(1,1)$  process. Then

$$P(Y_1 > x) \sim E\left[\left(\int_0^1 e^{-R_{t-}/2} dM_t\right)^+\right]^k$$
$$P(\sigma_1 > x), \quad x \to \infty \tag{38}$$

and  $\sigma$  has extremal index function

$$\theta_{\sigma}(h) = \frac{E\left(\sup_{0 \le t \le h} e^{-R_t \kappa/2} - \sup_{t \ge h} e^{-R_t \kappa/2}\right)^{+}}{E\left(\sup_{0 \le t \le h} e^{-R_t \kappa/2}\right)}$$

$$<1, \quad h>0 \tag{39}$$

The extremal index of the discrete-time process  $(Y_n)_{n\in\mathbb{N}}$  of the log price increments at integer times is given by

$$\theta = \frac{E\left[\left(I_1^{\kappa} - \max_{k\geq 2} I_k^{\kappa}\right)^+\right]}{E[I_1^{\kappa}]} < 1 \tag{40}$$

It follows that both the diffusion limit and the  $\text{COGARCH}(1,1)$  can model extremal clusters. Since the diffusion limit  $(31)$  has continuous sample paths, one can also consider its clustering behavior via epsilon-upcrossings. Choosing such an approach, the diffusion limit of Nelson does not cluster, as reported in [18]. In particular, both notions of extremal clustering for processes with continuous sample paths do not lead to the same interpretation.

Similar to the definition of COGARCH, a continuous-time analog to the EGARCH process has been proposed in [21]. So far, no analog to Theorem 2 for the continuous-time EGARCH process seems to be available.

## References

- Barndorff-Nielsen, O.E. & Shephard, N. (2001). [1] Non-Gaussian Ornstein-Uhlenbeck-based models and some of their uses in financial economics (with discussion), Journal of the Royal Statistical Society. Series B 63, 167-241.
- [2] Barndorff-Nielsen, O.E. & Shephard, N. (2002). Econometric analysis of realised volatility and its use in estimating stochastic volatility models, Journal of the Royal Statistical Society. Series B 64, 253-280.
- Basrak, B., Davis, R.A. & Mikosch, T. (2002). Regular [3] variation of GARCH processes, Stochastic Process and *their Applications* **99**, 95–116.
- [4] Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity, Journal of Economometrics 31, 307-327.
- Breidt, F.J. & Davis, R.A. (1998). Extremes of stochas-[5] tic volatility models, Annals of Applied Probability 8, 664-675.
- Brockwell, P.J. (2004). Representations of continuous [6] time ARMA processes, Journal of Applied Probability 41A.  $375 - 382$ .
- [7] Davis, R.A. & Mikosch, T. (2008). Extremes of stochastic volatility models, in Handbook of Financial Time Series, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, Heidelberg, 355-364.
- [8] Davis, R.A. & Mikosch, T. (2008). Extreme value theory for GARCH processes, in Handbook of Financial Time

Series, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, Heidelberg, 187-199.

- [9] Drude, N. (2006). Extremwertverhalten von unendlichen Moving Average Prozessen mit leicht taillierten Innovationen und Anwendungen auf EGARCH Prozesse. Diplomarbeit, Technische Universität München.
- [10] Drude, N. & Lindner, A. (2008). Extremes of Sums of Infinite Moving Average Processes with Light Tails and Applications to EGARCH, in preparation.
- [11] Embrechts, P., Klüppelberg, C. & Mikosch, T. (1997). Modelling Extremal Events for Insurance and Finance, Springer, Berlin.
- [12] Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation, *Econometrica* 50, 987-1008.
- [13] Fasen, V.M. (2004). Extremes of Lévy Driven Moving Average Processes with Applications in Finance. PhD thesis, Technische Universität München.
- [14] Fasen, V. (2005). Extremes of regularly varying mixed moving average processes, Advances in Applied Probability 37, 993-1014.
- [15] Fasen, V. (2009). Extremes of Lévy Driven Mixed MA Processes with Convolution Equivalent Distributions  $12(3)$  265-296.
- [16] Fasen, V. (2008). Asymptotic Results for Sample Autocovariance Functions and Extremes of Integrated Generalized Ornstein-Uhlenbeck Processes, to appear.
- [17] Fasen, V. (2008). Extremes of continuous-time processes, in Handbook of Financial Time Series, T.G. Andersen, R.A. Davis, J.-P. Kreiss & T. Mikosch, eds, Springer, Heidelberg, 653–667.
- [18] Fasen, V., Klüppelberg, C. & Lindner, A. (2006). Extremal behavior of stochastic volatility models, in Stochastic Finance, M.D.R. Grossinho, A.N. Shiryaev, M. Esquivel & P.E. Oliviera, eds, Springer, New York, pp. 107-155.
- [19] Fasen, V., Klüppelberg, C. & Schlather, M. (2007). High-level Dependence in Time Series Models, to appear.
- [20] Finkenstädt, B. & Rootzén, H. (eds) (2004). Extreme Values in Finance, Telecommunications, and the Environment, Chapman & Hall/CRC, Boca Raton.
- [21] Haug, S. & Czado, C. (2007). An exponential continuous time GARCH process, Journal of Applied Probability 44, 960-976.
- [22] Klüppelberg, C. & Lindner, A. (2005). Extreme value theory for moving average processes with light-tailed innovations, Bernoulli 11, 381-410.
- [23] Klüppelberg, C., Lindner, A. & Maller, R. (2004). A continuous time GARCH process driven by a Lévy process: stationarity and second order behaviour, Journal of Applied Probability 41, 601-622.
- [24] Leadbetter, M.R., Lindgren, G. & Rootzén, H. (1983). Extremes and Related Properties of Random Sequences and Processes, Springer, Berlin.
- [25] Mikosch, T. & Stărică, C. (2000). Limit theory for the sample autocorrelations and extremes of a  $GARCH(1,1)$ process, Annals of Statistics 28, 1427-1451.

- [26] Nelson, D.B. (1991). Conditional heteroskedasticity in asset returns: a new approach, *Econometrica* **59**, 347–370.
- [27] Scott, L.O. (1987). Option pricing when the variance changes randomly: theory, estimation and application, *Journal of Financial Quantitative Analysis* **22**, 419–439.
- [28] Taylor, S.J. (1982). Financial returns modelled by the product of two stochastic processes – a study of daily sugar prices 1961–79, in *Time Series Analysis: Theory and Practice 1*, O.D. Anderson, ed., North-Holland, Amsterdam, pp. 203–226.
- [29] Todorov, V. & Tauchen, G. (2006). Simulation methods for Levy-driven CARMA sto ´ chastic volatility models, *Journal of Business and Economic Statistics* **24**, 455–469.

[30] Wiggins, J.B. (1987). Option values under stochastic volatility: theory and empirical estimates, *Journal of Financial Economics* **19**, 351–372.

## **Related Articles**

**Autoregressive Moving Average (ARMA) Processes**; **Barndorff-Nielsen and Shephard (BNS) Models**; **Bates Model**; **Extreme Value Theory**; **GARCH Models**; **Heavy Tails**; **Risk Measures: Statistical Estimation**; **Stochastic Volatility Models**; **Stylized Properties of Asset Returns**.

CLAUDIA KLUPPELBERG ¨ & A. LINDNER
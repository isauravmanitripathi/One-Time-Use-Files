# **Multiname Reduced Form** Models

Currently, there are three established approaches for describing the default of a single credit: (i) reduced-form; (ii) structural; and (iii) hybrid. It has been an outstanding goal for many researchers to extend these approaches to baskets of several (potentially many) credits. In this article, we concentrate on the reduced-form approach and show how it works in single-name and multiname settings.

## **Single-name Intensity Models**

For a single name, the main assumptions of the reduced-form model are as follows [8, 9, 12]). The name defaults at the first time a Cox process jumps from 0 to 1. The default intensity (hazard rate)  $X(t)$  of this process is governed by a mean-reverting nonnegative jump-diffusion process

$$dX(t) = f(t, X(t)) dt + g(t, X(t)) dW(t) + J dN(t), \t X(0) = X_0 \t (1)$$

where  $W(t)$  is a standard Wiener process,  $N(t)$ is a Poisson process with intensity  $\lambda(t)$ , and J is a positive jump distribution;  $W, N, J$  are mutually independent. It is clear that we have to impose the following constraints:

$$f(t, 0) \ge 0, \quad f(t, \infty) < 0, \quad g(t, 0) = 0$$
 (2)

plus a number of other technical conditions to ensure that  $X(t)$  stays nonnegative and is mean reverting.

For analytical convenience (rather than for stronger reasons), it is customary to assume that  $X$ is governed by the square-root stochastic differential equation (SDE):

$$dX(t) = \kappa \left(\theta(t) - X(t)\right) dt + \sigma \sqrt{X(t)} dW(t)$$
$$+ J dN(t), \quad X(0) = X_0 \tag{3}$$

with exponential (or hyperexponential) jump distribution [4]. However, for practical purposes it is more convenient to consider discrete jump distributions with jump values  $J_m > 0$ ,  $1 \le m \le M$ , occurring with probabilities  $\pi_m > 0$ ; such distributions are more flexible than parametric ones because they allow one to place jumps where they are needed

In this framework, the survival probability of the name from time 0 to time  $T$  has the form

$$q(0,T) = \mathbb{E}_0 \left\{ e^{-\int_0^T X(t') dt'} \right\} = \mathbb{E}_0 \left\{ e^{-Y(T)} \right\} \quad (4)$$

where  $Y(t)$  is governed by the following degenerate SDE:

$$dY(t) = X(t) dt, \quad Y(0) = 0 \tag{5}$$

More generally, the survival probability from time  $t$  to time  $T$  conditional on no default before time  $t$ has the form

$$q(t, T | X(t), Y(t))$$

$$= \mathbb{I}_{(\tau > t)} \mathbb{E}_{t} \left\{ e^{-\int_{t}^{T} X(t') dt'} \middle| X(t), Y(t) \right\}$$

$$= e^{Y(t)} \mathbb{I}_{(\tau > t)} \mathbb{E}_{t} \left\{ e^{-Y(T)} \middle| X(t), Y(t) \right\} \quad (6)$$

where  $\tau$  is the default time and  $\mathbb{I}_{(\tau>t)}$  is the corresponding indicator function. This expectation, and, more generally, expectations of the form  $\mathbb{E}_{t} \left\{ e^{-\xi Y(T)} \middle| X(t), Y(t) \right\}$ , can be computed by solving the following augmented partial differential equation (PDE) (see [10], Chapter 13):

$$\mathcal{L}V(t, T, X, Y) + XV_Y(t, T, X, Y) = 0 \tag{7}$$

$$V(T, T, X, Y) = e^{-\xi Y}$$
(8)

where

$$\mathcal{L}V \equiv V_t + \kappa \left(\theta \left(t\right) - X\right) V_X + \frac{1}{2}\sigma^2 X V_{XX}$$
$$+ \lambda \sum_m \pi_m \left[V \left(X + J_m\right) - V \left(X\right)\right] \tag{9}$$

Specifically, the following relation holds:

$$\mathbb{E}_{t}\left\{e^{-\xi Y(T)}\middle| X\left(t\right),Y\left(t\right)\right\} = V\left(t,T,X\left(t\right),Y\left(t\right)\right) \tag{10}$$

The corresponding solution can be written in the so-called affine form:

$$V(t, T, X, Y) = e^{a(t, T, \xi) + b(t, T, \xi)X - \xi Y}$$
(11)

where  $a, b$  are functions of time governed by the following system of ordinary differential equations (ODEs):

$$\begin{cases}\n\frac{\mathrm{d}a\left(t,T,\xi\right)}{\mathrm{d}t} = -\kappa\theta\left(t\right)b\left(t,T,\xi\right) \\
-\lambda\sum_{m}\pi_{m}\left[e^{J_{m}b\left(t,T,\xi\right)}-1\right] \\
\frac{\mathrm{d}b\left(t,T,\xi\right)}{\mathrm{d}t} = \xi + \kappa b\left(t,T,\xi\right) \\
-\frac{1}{2}\sigma^{2}b^{2}\left(t,T,\xi\right)\n\end{cases}\n$$
(12)

$$a(T, T, \xi) = 0, \quad b(T, T, \xi) = 0$$
 (13)

While in the presence of discrete jumps this system cannot be solved analytically, it is very easy to solve it numerically via the standard Runge-Kutta method. The survival probability  $q(0, T)$  and default probability  $p(0, T)$  have the form

$$q(0, T) = e^{a(0,T,1)+b(0,T,1)X_0}$$
  

$$p(0, T) = 1 - q(0, T) = 1 - e^{a(0,T,1)+b(0,T,1)X_0}$$
(14)

Assuming for simplicity that the short interest rate  $r(t)$  is deterministic and the protection payments are made continuously, we can write the value  $U$  of a credit default swap (CDS) paying an up-front amount  $\upsilon$  and a coupon s in exchange for receiving  $1 - R$ 

(where  $R$  is the default recovery) on default as follows:

$$U = -\upsilon + V(0, X_0) \tag{15}$$

Here,  $V(t, X)$  solves the following pricing problem:

$$\mathcal{L}V(t,X) - (r+X)V(t,X) = s - (1-R)X$$
(16)  
$$V(T,X) = 0$$
(17)

where  $\mathcal{L}$  is given by expression (9). Using Duhamel's principle, we obtain the following expression for  $V$ :

$$V(t, X) = -s \int_{t}^{T} D(t, t') e^{a(t, t', 1) + b(t, t', 1)X} dt'$$
$$- (1 - R) \int_{t}^{T} D(t, t') d[e^{a(t, t', 1) + b(t, t', 1)X}]$$
(18)

where

$$D\left(t,t'\right) = e^{-\int_{t}^{t'} r\left(t''\right) \mathrm{d}t''} \tag{19}$$

is the discount factor between two times  $t$  and  $t'$ . Accordingly,

$$U = -\upsilon - s \int_{0}^{T} D(0, t') (1 - p(0, t')) dt'$$
  
+ (1 - R)  $\int_{0}^{T} D(0, t') dp(0, t')$  (20)

For a given up-front payment  $\nu$ , we can represent the corresponding par spread  $\hat{s}$  (i.e., the spread that makes the value of the corresponding CDS zero) as follows:

$$\hat{s}(T) = \frac{-\upsilon + (1 - R) \int_{0}^{T} D(0, t') \, \mathrm{d}p(0, t')}{\int_{0}^{T} D(0, t') \left(1 - p(0, t')\right) \, \mathrm{d}t'}$$
(21)

It is clear that the numerator represents the payout in the case of default, while the denominator represents the risky  $DV_{01}$ . Conversely, for a given

spread we can represent the par up-front payment in the form

$$\hat{v} = -s(T) \int_{0}^{T} D(0, t') (1 - p(0, t')) dt'$$
$$+ (1 - R) \int_{0}^{T} D(0, t') dp(0, t') \qquad (22)$$

In these formulas, we implicitly assume that the corresponding CDS is fully collateralized, so that in the event of default  $1 - R$  is readily available. Shortly, we will evaluate CDS spreads in the presence of the counterparty risk.

In general, there is not enough market information to calibrate the diffusion and jump parts. So, typically, they are viewed as given constants, and the mean-reversion level  $\theta$  (t) is calibrated in such a way that the whole par spread curve is matched.

## **Multiname Intensity Models**

#### The Two-name Case

It is very tempting to extend the above framework to cover several correlated names. For example, consider two credits,  $A$ ,  $B$  and assume for simplicity that their default intensities coincide,

$$X_{A}(t) = X_{B}(t) = X(t) \tag{23}$$

and both names have the same recovery  $R_A =$  $R_B = R$ . For a given maturity T, the default event correlation  $\rho$  is defined as follows:

It is clear that

$$p_A(0, T) = p_B(0, T) = p(0, T)$$
$$= 1 - e^{a(0,T,1) + b(0,T,1)X_0}$$
(27)

Simple calculation yields

$$p_{AB}(0,T) = \mathbb{E}_{0} \left\{ e^{-\int_{0}^{T} \left( X_{A}(t') + X_{B}(t') \right) dt'} \right\}$$
$$+ p_{A}(0,T) + p_{B}(0,T) - 1$$
$$= \mathbb{E}_{0} \left\{ e^{-2 \int_{0}^{T} X(t') dt'} \right\} + 2p(0,T) - 1$$
(28)

so that

$$\rho\left(0,T\right) = \frac{\mathbb{E}_{0}\left\{e^{-2\int_{0}^{T}X\left(t'\right)dt'}\right\} - \left(1-p\left(0,T\right)\right)^{2}}{p\left(0,T\right)\left(1-p\left(0,T\right)\right)}\n$$

$$\n= \frac{e^{a(0,T,2)+b(0,T,2)X_{0}} - e^{2a(0,T,1)+2b(0,T,1)X_{0}}}{\left(1-e^{a(0,T,1)+b(0,T,1)X_{0}}\right)e^{a(0,T,1)+b(0,T,1)X_{0}}}\n$$
(29)

It turns out that in the absence of jumps, the corresponding event correlation is very low [12]. However, if large positive jumps are added (while overall survival probability is preserved), then correlation can increase all the way to one. Assuming that

$$\rho\left(0,T\right) = \frac{P\left(\tau_{A} \leq T, \tau_{B} \leq T\right) - P\left(\tau_{A} \leq T\right)P\left(\tau_{B} \leq T\right)}{\sqrt{P\left(\tau_{A} \leq T\right)\left(1 - P\left(\tau_{A} \leq T\right)\right)P\left(\tau_{B} \leq T\right)\left(1 - P\left(\tau_{B} \leq T\right)\right)}}\tag{24}$$

$$\rho\left(0,T\right) = \frac{p_{AB}\left(0,T\right) - p_{A}\left(0,T\right)p_{B}\left(0,T\right)}{\sqrt{p_{A}\left(0,T\right)\left(1 - p_{A}\left(0,T\right)\right)p_{B}\left(0,T\right)\left(1 - p_{B}\left(0,T\right)\right)}}\tag{25}$$

where  $\tau_A$ ,  $\tau_B$  are the default times, and

$$p_A(0, T) = P(\tau_A \leq T), \quad p_B(0, T) = P(\tau_B \leq T)$$

$$p_{AB}(0,T) = P(\tau_A \leq T, \tau_B \leq T) \tag{26}$$

 $T = 5y, \kappa = 0.5, \sigma = 7\%$ , and  $J = 5.0$ , we illustrate this observation in Figure 1.

In the two-name portfolio, we can define two types of CDSs which depend on the correlation: (i) the first-to-default (FTD) swap;  $(ii)$  the

![](_page_3_Figure_1.jpeg)

**Figure 1** Correlation *ρ* and mean-reversion level *θ* = *X*<sup>0</sup> as functions of jump intensity *λ*. Other parameters are as follows: *T* = 5*y*, *κ* = 0*.*5, *σ* = 7%, and *J* = 5*.*0

second-to-default (STD) swap. The corresponding par spreads (assuming that there are no up-front payments) are

where *V* is the value of a fully collateralized CDS on name *B* with spread *s*, and *V*<sup>+</sup> = max {*V ,* 0}, *V*<sup>−</sup> = min {*V ,* 0}. It is clear that the discount rate

$$\hat{s}_{1}(T) = \frac{(1-R)\int_{0}^{T} D(0, t') \, \mathrm{d}\left[1 - \mathrm{e}^{a(0, t', 2) + b(0, t', 2)X_{0}}\right]}{\int_{0}^{T} D(0, t') \, \mathrm{e}^{a(0, t', 2) + b(0, t', 2)X_{0}} \, \mathrm{d}t'}$$
(30)

$$\hat{s}_{2}(T) = \frac{(1-R)\int_{0}^{T}D(0,t')\,\mathrm{d}\Big[1-\Big(2\mathrm{e}^{a(t',1)+b(t',1)X_{0}}-\mathrm{e}^{a(t',2)+b(t',2)X_{0}}\Big)\Big]}{\int_{0}^{T}D(0,t')\Big(2\mathrm{e}^{a(t',1)+b(t',1)X_{0}}-\mathrm{e}^{a(t',2)+b(t',2)X_{0}}\Big)\,\mathrm{d}t'}\tag{31}$$

It is clear that the relative values of *s*ˆ1*,s*ˆ<sup>2</sup> very strongly depend on whether or not jumps are present in the model (see Figure 2).

However, an even more important application of the above model is the evaluation of counterparty effects on fair CDS spreads. Let us assume that name *A* has written a CDS on reference name *B*. It is clear that the pricing problem for the value of the uncollateralized CDS *V*˜ can be written as follows:

$$\mathcal{L}\tilde{V}(t, X) - (r + 2X)\tilde{V}(t, X)$$
  
=  $s - (1 - R)X - (RV_{+}(t, X) + V_{-}(t, X))X$   
(32)

is increased from *r* + *X*, in equation (16), to *r* + 2*X*, in equation (32), since there are two cases when the uncollateralized CDS can be terminated due to default: when the reference name *B* defaults and when the issuer *A* defaults. The terms on the right represent a continuous stream of coupon payments, the amount received if *B* defaults before *A*, and the amount received (or paid) in case when *A* defaults before *B*. Although equation (32) is no longer analytically solvable, it can be solved numerically *via*, say, an appropriate modification of the classical Crank–Nicholson method. It turns out that in the presence of jumps the value of the fair par spread goes down dramatically.

![](_page_4_Figure_1.jpeg)

**Figure 2** FTD spread  $\hat{s}_1$ , STD spread  $\hat{s}_2$ , and single-name CDS spread  $\hat{s}$  as functions of jump intensity  $\lambda$ . Other parameters are the same as in Figure 1. It is clear that jumps are necessary to have  $\hat{s}_1$  and  $\hat{s}_2$  of similar magnitudes

#### The Multiname Case

The above modeling framework has been expanded in various directions and used as a basis for several coherent intensity-based models for credit baskets; see [2, 3, 6, 7, 11].

To start, we briefly summarize the affine jumpdiffusion model of Duffie-Garleanu [3] and Mortensen [11]. Consider a basket of  $N$  names with equal unit notionals and equal recoveries  $R$ . Let us assume that the corresponding default intensities can be decomposed as follows:

$$X_i(t) = \beta_i X_c(t) + \tilde{X}_i(t) \tag{33}$$

where  $X_c$  is the common intensity driven by the following SDE:

$$dX_c(t) = \kappa_c (\theta_c - X_c(t)) dt + \sigma_c \sqrt{X_c(t)} dW_c(t)$$
$$+ J_c dN_c(t)$$
$$X_c(0) = X_{c0} \tag{34}$$

while  $\tilde{X}_i$  are idiosyncratic intensities driven by similar SDEs:

$$d\tilde{X}_{i}(t) = \kappa_{i} \left(\theta_{i} - \tilde{X}_{i}(t)\right) dt + \sigma_{i} \sqrt{\tilde{X}_{i}(t)} dW_{i}(t)$$
$$+ \tilde{J}_{i} dN_{i}(t)$$
$$\tilde{X}_{i}(0) = \tilde{X}_{i0} \tag{35}$$

Here,  $1 \leq i \leq N$ . The processes  $\tilde{X}_i(t)$ ,  $X_c(t)$  are assumed to be independent. In this formulation,  $\beta_i$  are similar to the  $\beta_i$  appearing in the capital asset pricing model (CAPM). We note that  $\theta_c$ ,  $\theta_i$  are assumed to be constant. In the original Duffie-Garleanu formulation, it was assumed that all  $\beta_i = 1$ . However, this assumption is very restrictive since it limits the magnitude of the common factor by the size of the lowest spread  $X_i$ , so that, in general, high correlation cannot be achieved. It was lifted in the subsequent paper by Mortensen. Of course, to preserve analyticity, one needs to impose very rigid conditions on the coefficients of the corresponding SDEs, since, in general, the sum of two affine processes is not an affine process. Specifically, the following should hold:

$$\kappa_i = \kappa_c = \kappa, \quad \sigma_i = \sqrt{\beta_i} \sigma_c, \quad \lambda_i = \lambda, \quad J_{im} = \beta_i J_{cm}\n$$
(36)

Even when the above constraints are satisfied, there are too many free parameters in the model. A reduction in their number is achieved by imposing the following constraints:

$$\frac{\beta_i \theta_c}{\beta_i \theta_c + \theta_i} = \frac{\lambda_c}{\lambda_c + \lambda} = \frac{X_c(0)}{X_c(0) + X_{\text{ave}}(0)} = \omega \tag{37}$$

where  $\omega$  is a correlation-like parameter representing the systematic share of intensities, and  $X_{\text{ave}}(0)$  is the average of  $X_i$  (0). When  $\omega$  is low, the dynamics of intensities is predominantly idiosyncratic, and it is systemic when  $\omega$  is close to one.

Provided that equation  $(36)$  is true, the affine ansatz still holds, so that survival probabilities of individual names can be written in the form

$$\begin{split} q_{i}\left(t,T\,|\,X_{i}\left(t\right)\right) \\ &=\mathbb{I}_{\left(\tau_{i}>t\right)}\mathbb{E}_{t}\left\{e^{-\int_{t}^{T}X_{i}\left(t'\right)\mathrm{d}t'}\bigg|\,X_{i}\left(t\right)\right\} \\ &=\mathbb{I}_{\left(\tau_{i}>t\right)}\mathbb{E}_{t}\left\{e^{-\beta_{i}\left[Y_{c}(T)-Y_{c}(t)\right]}\bigg|\,X_{c}\left(t\right)\right\} \\ &\times\mathbb{E}_{t}\left\{e^{-\left[\tilde{Y}_{i}(T)-\tilde{Y}_{i}(t)\right]}\bigg|\,\tilde{X}_{i}\left(t\right)\right\} \\ &=\mathbb{I}_{\left(\tau_{i}>t\right)}e^{a_{c}\left(t,T,\beta_{i}\right)+b_{c}\left(t,T,\beta_{i}\right)X_{c}\left(t\right)+a_{i}\left(t,T,1\right)+b_{i}\left(t,T,1\right)\tilde{X}_{i}\left(t\right)} \end{split} \tag{38}$$

Moreover, conditioning the dynamics of spreads on the common factor  $Y_c(T)$ , we can write idiosyncratic survival probabilities as follows:

$$q_{i}\left(t,T|\tilde{X}_{i}(t),Y_{c}(T)\right)$$

$$=\mathbb{I}_{(\tau_{i}>t)}e^{-\beta_{i}[Y_{c}(T)-Y_{c}(t)]+a_{i}(t,T,1)+b_{i}(t,T,1)\tilde{X}_{i}(t)}$$
(39)

$$q_i \left( 0, T | \tilde{X}_{i0}, Y_c (T) \right)$$
  
=  $e^{-\beta_i Y_c(T) + a_i(0, T, 1) + b_i(0, T, 1)\tilde{X}_{i0}}$  (40)

First, we perform the calibration of the model parameters to fit 1y and 5y CDS spreads for individual names. Once this calibration is performed, we can apply the usual recursion and calculate the conditional probability of loss of exactly  $n$  names,  $0 \le n \le N$ , in the corresponding portfolio, or, equivalently, of the loss of size  $(1 - R) n$ , which we denote as  $p(0, T, n|Y)$ .

For a tranche of the portfolio which covers losses from the attachment point  $\alpha$  to the detachment point  $\delta$ ,  $0 \le \alpha < \delta \le 1$ , the relative tranche loss is defined as follows:

$$\Lambda_{\alpha,\delta} (L) = \frac{\max \left\{ \min \left\{ L, \delta N \right\} - \alpha N, 0 \right\}}{\left( \delta - \alpha \right) N} \tag{41}$$

Its conditional expectation has the form

$$p_{\alpha,\delta} (0, T | Y) = \sum_{n=0}^{N} \Lambda_{\alpha,\delta} ((1 - R) n) p (0, T, n | Y)$$
(42)

In order to find the unconditional expectation, we have to integrate  $p_{\alpha,\delta}(0,T|Y)$  with respect to the distribution  $f(Y)$  of the common factor Y. The latter distribution can be found via the inverse Laplace transform of the function

$$\phi\left(\xi\right) = \int_{0}^{\infty} e^{-\xi Y} f\left(Y\right) dY = e^{a_{c}(0,T,\xi) + b_{c}(0,T,\xi)X_{c0}}$$
(43)

by numerically calculating the Bromwich integral in the complex plane

$$f(Y) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} e^{\xi Y} \phi(\xi) d\xi$$
  
$$= \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} e^{\xi Y + a_c(0, T, \xi) + b_c(0, T, \xi)X_{c0}} d\xi$$
  
(44)

Both standard and more recent methods allow one to calculate the inverse transform without too much difficulty; see, for example, [1]. Finally, we calculate the unconditional expectation of the tranche loss by performing integration over the common factor:

$$p_{\alpha,\delta}\left(0,\,T\right) = \int_{0}^{\infty} p_{\alpha,\delta}\left(0,\,T\right|Y\right) f\left(Y\right) \,\mathrm{d}Y \quad (45)$$

Knowing this expectation, we can represent par spread and par up-front for the tranche in question by slightly generalizing formulas (21) and (22). In other words,

$$s_{\alpha,\delta} (T) = \frac{-\upsilon + \int_{0}^{T} D(0, t') \, \mathrm{d}p_{\alpha,\delta} (0, t')}{\int_{0}^{T} D(0, t') \left(1 - p_{\alpha,\delta} (0, t')\right) \, \mathrm{d}t'} \qquad (46)$$
$$\upsilon = -s_{\alpha,\delta} (T) \int_{0}^{T} D(0, t') \left(1 - p_{\alpha,\delta} (0, t')\right) \, \mathrm{d}t'$$
$$+ \int_{0}^{T} D(0, t') \, \mathrm{d}p_{\alpha,\delta} (0, t') \qquad (47)$$

Equity tranches with  $\alpha = 0$ ,  $\delta < 1$  (and, in some cases, other junior tranches) are traded with a fixed spread, say  $s = 5\%$ , and an up-front determined by formula (47); more senior tranches are traded with zero up-front and spread determined by formula (46).

Treatment of super-senior tranches with *δ* = 1 has to be slightly modified, but we do not discuss the corresponding details for the sake of brevity.

The affine jump-diffusion model allows one to price tranches of standard on-the-run indices, such as CDX and iTraxx with reasonable (but not spectacular) accuracy, and can be further used to price bespoke tranches; however, one can argue that the presence of the stochastic idiosyncratic components makes it unnecessarily complex. In any case, the very rigid relationships between the model parameters suggest that the choice of these components is fairly limited and rather artificial.

Two models without stochastic idiosyncratic components were independently proposed in the literature. The first one, due to Chapovsky *et al.* [2], assumes purely deterministic idiosyncratic components, and represents *qi* as follows:

$$q_i(0, T | Y_c(T)) = e^{-\beta_i(T)Y_c(T) + \xi_i(T)} \qquad (48)$$

where, *Xc, Yc* are driven by SDEs (1) and (5), while *ξi (T )* is calibrated to the survival probabilities of individual names. The second one, due to Inglis–Lipton [6], models conditional survival probabilities directly, and postulates that *qi (*0*, T* | *Yc)* can be represented in the logit form

$$q_{i}(0, T | Y_{c}(T)) = \mathbb{E}_{t} \left\{ \frac{1}{1 + e^{Y_{c}(T) + \chi_{i}(T)}} \right\} \tag{49}$$

We now describe the Inglis–Lipton model in some detail. To calibrate the model to individual CDS spreads, we need to solve the following pricing problem:

$$\hat{\mathcal{L}}V(t, X, Y) + XV_Y(t, X, Y) = 0 \tag{50}$$

$$V(T, X, Y) = \frac{1}{1 + e^{Y}} \quad (51)$$

where

$$\hat{\mathcal{L}}V \equiv V_t + f(t, X) V_X + \frac{1}{2}g^2(t, X) V_{XX}$$
$$+ \lambda \sum_m \pi_m \left[ V(X + J_m) - V(X) \right] (52)$$

and determine *χi (T )* from the following algebraic equation (rather than a PDE):

$$V(0, 0, \chi_i(T)) = q_i(0, T), \quad 1 \le i \le N \quad (53)$$

As before, we can easily calculate the probability of loss of exactly *n* names, 0 ≤ *n* ≤ *N*, *p (* 0*,T,n*| *Y ),* conditional on *Y* . We can then solve the pricing equation (50) with the terminal condition

$$V_{\alpha,\delta}\left(T,X,Y\right) = p_{\alpha,\delta}\left(0,T\right|Y) \tag{54}$$

and find the expected losses for an individual tranche at time 0:

$$p_{\alpha,\delta} (0,T) = V_{\alpha,\delta} (0, X_0, 0)$$
 (55)

Here, *pα,δ (*0*, T* | *Y )*, *pα,δ (*0*, T )* have the same meaning as in equations (42) and (45). In order to price senior tranches rare but large jumps are necessary. Since, as a rule, we need to analyze several tranches with different attachments, detachments, and maturities at once, it is more convenient to solve the forward version of equation (50) and find *pα,δ (*0*, T )* by integration. Thus, we are in a paradoxical situation when it is more efficient to perform calibration to individual names backward and calibration to tranches forward, rather than the other way round.

When derivatives explicitly depending on the number of defaults, such as leveraged super-senior (LSS) tranches, are considered, the *X, Y* dynamics requires augmentation with the dynamics of the number of defaulted names *n*. Since we are dealing with a "pure birth" process, we can use the wellknown results due to Feller [5] and others and obtain the following expression for the one-step transition probability:

$$h(t, X, Y, n) = \frac{-\sum_{n'=0}^{n} \left[ p_{t}(t, T, n' | Y) + X p_{Y}(t, T, n' | Y) \right]}{p(t, T, n | Y)}$$
$$= \frac{\sum_{n'=n+1}^{N} \left[ p_{t}(t, T, n' | Y) + X p_{Y}(t, T, n' | Y) \right]}{p(t, T, n | Y)}$$
(56)

The corresponding backward Kolmogoroff equation has the following form:

$$\hat{\mathcal{L}}V(t, X, Y, n) + XV_Y(t, X, Y, n) + h(t, x, Y, n)$$
$$\times [V(t, X, Y, n+1) - V(t, X, Y, n)] = 0 \quad (57)$$

|          |      | 5v     | 5v     | 7ν     | 7ν     | 10v    | 10v    |
|----------|------|--------|--------|--------|--------|--------|--------|
| $\alpha$ |      | Market | Model  | Market | Model  | Market | Model  |
| 0%       | 3%   | 21.75% | 21.76% | 29.00% | 28.89% | 36.88% | 36.94% |
| 3%       | 6%   | 150.5  | 149.8  | 210.5  | 215.6  | 377.0  | 379.5  |
| 6%       | 9%   | 72.5   | 73.7   | 108.0  | 100.7  | 158.0  | 159.2  |
| 9%       | 12%  | 52.5   | 51.3   | 72.0   | 72.3   | 104.5  | 98.8   |
| 12%      | 22%  | 32.5   | 32.6   | 46.0   | 47.6   | 63.5   | 64.3   |
| 0%       | 100% | 49.0   | 46.7   | 56.0   | 53.6   | 65.0   | 63.4   |

**Table 1** Market quotes and full dynamic model calibration results. We quote par up-front payments with 5% spread for equity tranches, and par spreads for all other tranches<sup>a</sup>

<sup>a</sup>adapted from [7]

![](_page_7_Figure_4.jpeg)

**Figure 3** Loss distributions for 5y, 7y, 10y implied by the calibrated dynamic model (adapted from [7])

If need occurs, a multifactor extension of the above model can be considered.

Table 1 shows the quality of calibration achievable in the above framework for the on-the-run iTraxx index on November 9, 2007. We show the corresponding loss distributions in Figure 3.

This model can naturally be used to price bespoke baskets (as long as an appropriate standard basket is determined). It does not suffer from any of the drawbacks of the standard mapping approaches used for this purpose.

We note in passing that Inglis-Lipton [6] describe a static version of their model which is perfectly adequate for the purposes of pricing standard and bespoke tranches, even under the current extreme market conditions.

## Conclusion

In general, multiname intensity models have many attractive features. They are naturally connected to single-name intensity models. In order to account for the observed tranche spreads in the market, they have to postulate periods of very high intensities which

gradually mean-revert to moderate and low levels. Mean-reversion of the default intensities serves as a useful mechanism which allows one to price tranches with different maturities in a coherent fashion. Of course, due to the presence of large jumps, it is very difficult to provide convincing hedging mechanisms in such models. However, since we assume that jumps are discrete, it is possible in principle to hedge a given bespoke tranche with a *portfolio* of standard tranches. This is a topic of active research and experimentation at the moment, and we hope to present the outcome of this research in the near future.

## Acknowledgments

I am grateful to my colleagues S. Inglis, J. Manzano, A. Rennie, A. Sepp, and D. Shelton for illuminating discussions of the subject matter.

# References

 $[1]$ Abate, J. & Whitt, W. (1995). Numerical inversion of Laplace transforms of probability distributions, ORSA Journal on Computing  $7(1)$ ,  $36-43$ .

- [2] Chapovsky, A., Rennie, A. & Tavares, P. (2001). Stochastic intensity modeling for structured credit exotics, *The International Journal of Theoretical and Applied Finance* **10**, 633–652.
- [3] Duffie, D. & Garleanu, N. (2001). Risk and valuation of collateralized debt obligations, *Financial Analysis Journal* **57**, 41–59.
- [4] Duffie, D., Pan, J. & Singleton, K. (2000). Transform analysis and asset pricing for affine jump diffusions, *Econometrica* **68**, 1343–1376.
- [5] Feller, W. (1970). *An Introduction to Probability Theory and its Applications*, Wiley, New York, Vol. 1.
- [6] Inglis, S. & Lipton, A. (2007). Factor models for credit correlation, *Risk Magazine* **20**(12), 110–115.
- [7] Inglis, S., Lipton, A., Savescu, I. & Sepp, A. (2008). Dynamic credit models, *Statistics and its Interface* **1**, 211–227.

- [8] Jarrow, R. & Turnbull, S. (1995). Pricing options on financial securities subject to credit risk, *Journal of Finance* **50**, 53–85.
- [9] Lando, D. (1998). On Cox processes and credit risky securities, *Review of Derivatives Research* **2**, 99–120.
- [10] Lipton, A. (2001). *Mathematical Methods for Foreign Exchange*, World Scientific, Singapore.
- [11] Mortensen, A. (2006). Semi-analytical valuation of basket credit derivatives in intensity-based models, *The Journal of Derivatives* **13**(4), 8–26.
- [12] Schonbucher, P. (2003). *Credit Derivatives Pricing Models*, Wiley, Chichester.

ALEXANDER LIPTON
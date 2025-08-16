# Variance-gamma Model

The variance-gamma (VG) process is a stochastic process with independent stationary increments, which allows for flexible parameterization of skewness and kurtosis of increments. It has gained popularity, especially in option pricing, because of its analytical tractability. It is an example of a pure-jump Lévy process (see Lévy Processes).

The VG model is derived from the (symmetric) VG probability distribution, which is so named because it is the distribution of a random variable  $X$  that results from mixing a normal variable on its variance by a gamma distribution. Specifically, the conditional distribution of  $X$  is given by  $X|W \sim \mathcal{N}(\mu, \sigma^2 W), \mu \in \mathbb{R}, \sigma > 0$ , where  $W \sim$  $\Gamma(\alpha, \alpha)$ ,  $\alpha > 0$ . The symbol "~" stands for "is distributed as". The symbol  $\Gamma(\alpha, \lambda)$  indicates a gamma probability distribution, with probability density function (PDF), for  $\alpha, \lambda > 0$ ,

$$f_{\Gamma}(w;\alpha,\lambda) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} w^{\alpha-1} e^{-\lambda w},$$
  
$$w > 0; = 0 \text{ elsewhere}$$
(1)

The choice  $\lambda = \alpha$  implies that  $\mathbb{E}(W) = 1$  and  $\mathbb{V}\text{ar}(W) = \frac{1}{\alpha}$ . Thus, *X* is a random variable symmetrically distributed about its mean  $\mathbb{E}(X) = \mu$ , with  $\text{Var}(X) = \sigma^2$  and a simple characteristic function (CF), so that when X is mean-corrected to  $Y =$  $X - \mu$ , the CF is

$$\mathbb{E}(\mathrm{e}^{\mathrm{i}uY}) = \left(1 + \frac{\sigma^2 u^2}{2\alpha}\right)^{-\alpha} \tag{2}$$

A random variable  $X$  having (symmetric) VG distribution may also be viewed as

$$X \stackrel{\mathcal{D}}{=} \mu + \sigma W^{\frac{1}{2}} Z, \qquad \mathbb{E}(W) = 1 \tag{3}$$

where the symbol  $\stackrel{\mathcal{D}}{=}$  means "has the same distribution as". Here  $Z \sim \mathcal{N}(0, 1)$  and W is a positive nondegenerate random variable distributed independently of  $Z$ . In the case of the VG distribution,  $W \sim \Gamma(\alpha, \alpha)$ .

Log returns of financial assets

$$X_t = \log P_t - \log P_{t-1}, \quad t = 1, 2, \dots, N$$
 (4)

reveal a kurtosis well in excess of 3, suggesting that the modeling of returns should be done by a symmetric distribution with heavier tails than the normal (see Stylized Properties of Asset Returns; Heavy Tails). For example, in 1972, Praetz [20] argued in favor of variance-dilation of the normal through variance-mixing and found that mixing according to  $X|W \sim \mathcal{N}(\mu, \sigma^2 W)$ , where W has reciprocal (inverse) gamma PDF with  $\mathbb{E}W = 1$ , gives the scaled *t*-distribution symmetric about  $\mu$  for the returns. This is a slight generalization of the classical Student's  $t$ -distribution, in that fractional degrees of freedom are permitted.

Influenced by Praetz's work, Madan and Seneta [16] took the distribution of the mixing variable  $W$ itself to be gamma (rather than reciprocal gamma). This resulted in a continuous-time model, which is now known as the (symmetric) variance-gamma model.

The VG model may be placed within the context of a more general subordinator (*see* **Time Change**) model [10], which gives the price  $P_t$  of a risky asset over continuous time  $t \ge 0$  as

$$P_t = P_0 \exp \{ \mu t + \sigma B(T_t) \} \tag{5}$$

where  $\mu$  and  $\sigma(>0)$  are real constants.  $\{T_t\}$ , the (market) activity time, is a positive, increasing random process (with stationary differences  $W_t = T_t T_{t-1}, t = 1, 2, \ldots$ ), which is independent of the standard Brownian motion  $\{B(t)\}\$ . The corresponding returns are then given as

$$X_{t} = \log P_{t} - \log P_{t-1} = \mu + \sigma(B(T_{t}) - B(T_{t-1}))$$
(6)

We assume that  $\mathbb{E}(W_t) < \infty$ , and so without loss of generality that

$$\mathbb{E}(W_t) = 1\tag{7}$$

to make the expected activity time change over unit calendar time equal to one unit, the scaling change in time being absorbed into  $\sigma$ , while noting that

$$X_t \stackrel{\mathcal{D}}{=} \mu + \sigma W_t^{\frac{1}{2}} B(1) \tag{8}$$

which is of form (3). The case  $T_t = t$  of the model  $(5)$  is the classical geometric Brownian motion (GBM) model for the process  $\{P_t\}$ , with corresponding returns being independently  $\mathcal{N}(\mu, \sigma^2)$  distributed.

In the VG model,  $\{T_t\}$  for  $t \ge 0$ , is the gamma process, a process of stationary-independent increments. The distribution of an increment over a time interval of length t is  $\Gamma(\alpha t, \alpha)$ . It is a remarkable feature that the distributional form for any  $t$  is the same; this is inherited by the VG model for  $\{\log(P_t/P_0)\}, t \ge 0$ , which is a process of stationary-independent increments, with the distribution of an increment over any time period  $t$  having CF

$$e^{i\mu ut} \left( 1 + \frac{\sigma^2 u^2}{2\alpha} \right)^{-\alpha t} \tag{9}$$

The corresponding distribution is also called a (symmetric) VG distribution. Its mean and variance are given by  $\mathbb{E} \log(P_t/P_0) = \mu t$  and  $\text{Var}(\log(P_t/P_0))$  $=\sigma^2 t$ , respectively. The whole structure is redolent of Brownian motion, to which the VG process reduces in the limit as  $\alpha \to \infty$ .

An important consequence of the VG distributional form of an increment over any time interval of length  $t$  is that, irrespective of the size of unit of time between successive data readings, returns have a VG distribution.

The CF  $(2)$ , clearly the CF of an infinitely divisible distribution, is also the CF of a difference of two independently and identically distributed (i.i.d.) gamma random variables, which reflects the fact shown in [16] that the process  $\{\log(P_t/P_0) - t\mu\}, t \ge 0$ , is the difference of two i.i.d. gamma processes.

The VG model is a pure-jump process [16] (see Jump Processes) reflecting this feature of a gamma process. This is seen from the Lévy-Khinchin representation (see Lévy Processes).

The analytical simplicity of the VG model and its pure-jump nature make it a leading candidate for modeling historical financial data. Further, the VG distribution's PDF has explicit structural form (see below), which is tractable for maximum-likelihood estimation of parameters from returns data.

Returns  $\{X_t\}, t = 0, 1, 2, \ldots$ , considered in isolation, need not be taken to be i.i.d. as in the preceding discussion, but to form (more generally) a strictly stationary sequence, to which moment estimation methods, for example, will still apply [25]. The symmetric scaled  $t$ -distribution continues to enjoy favor as a model for the distribution of returns because of its power-law (Pareto-type) probability tails, a property manifested (in contrast to the  $VG$ ) in the nonexistence of higher moments. For some data sets, empirical investigations [10, 12] suggest the nonexistence of higher moments in a model for returns (see Heavy Tails; Stylized Properties of Asset Returns) and hence the scaled  $t$ -distribution.

On the other hand, other investigations [9] suggest that it is virtually impossible to distinguish between the symmetric scaled  $t$  and VG distributions in regard to distributional tail structure by taking compatible parameter values in the two distributions. In fact, the PDFs of the two distributions reveal that the concentration of probability near the point of symmetry  $\mu$  and in the middle range of the distributions is qualitatively and quantitatively different. The VG distribution tends to increase the probability near  $\mu$ and in the tails, at the expense of the middle range. The different natures in regard to shape are most significantly revealed by the Cauchy distribution as a special case of the  $t$ -distribution and the Laplace (two-sided exponential) distribution as a special case of the VG distribution.

The first monograph to include a study of the VG model was [4]. Since then it has found a place in monographs such as [22], where it is treated in the general context of Lévy processes (see Lévy Processes).

Both the VG distribution and the scaled  $t$ distribution are extreme cases of the generalized hyperbolic (see **Generalized Hyperbolic Models**) distribution [23, 25].

#### Allowing for Skewness

A generalized normal mean-variance-mixing distribution is the distribution of  $X$ , where the conditional distribution of  $X$  is given as

$$X|W \sim \mathcal{N}(\mu + \theta W, \sigma^2 W + d^2) \tag{10}$$

Here,  $\mu$ ,  $\theta$ ,  $d$ , and  $\sigma(>0)$  are real numbers, and W is a nondegenerate positive random variable. The distribution is skew if  $\theta \neq 0$ , and it is symmetric otherwise. Press [21] studied a continuous-time model with this distribution for returns, where  $W \sim \text{Poisson}(\lambda)$ . This is a process of stationary-independent increments, resulting from adding a compound Poisson process of normal shocks to a Brownian motion, and has both continuous and jump components. Some special cases of equation  $(10)$  as a returns distribution, with focus on the estimation of parameters by the method of moments, are considered in [25].

A random variable  $X$  is said to have a normal variance-mean mixture (NVM) distribution [1] if equation (10) holds with  $d = 0$ .

The symmetric VG and scaled  $t$ -distributions are instances of equation (10), with  $d = \theta = 0$ .

The skew VG distribution, as introduced in [15], is the case of NVM where  $W$  is described by equation (1) with  $\mathbb{E}W = 1$  as in the symmetric case. (The skewed scaled  $t$ -distribution is defined analogously by taking  $W$  to have a reciprocal gamma distribution.)

The skew VG distribution has PDF

$$f_{\text{VG}}(x) = \sqrt{\frac{2}{\pi}} \frac{\alpha^{\alpha} e^{\frac{(x-\mu)\theta}{\sigma^{2}}}}{\sigma \Gamma(\alpha)} \left(\frac{|x-\mu|}{\sqrt{\theta^{2}+2\alpha\sigma^{2}}}\right)^{\alpha-\frac{1}{2}}$$
$$\times K_{\alpha-\frac{1}{2}} \left(\frac{|x-\mu|\sqrt{\theta^{2}+2\alpha\sigma^{2}}}{\sigma^{2}}\right), \ x \in \mathbb{R}$$
(11)

and CF

$$\phi_{\text{VG}}(u) = \mathbb{E}(\mathrm{e}^{\mathrm{i}ux}) = \mathrm{e}^{\mathrm{i}\mu u} \left(1 - \frac{1}{\alpha} \left(\mathrm{i}u\theta - \frac{\sigma^2 u^2}{2}\right)\right)^{-\alpha} \tag{12}$$

 $K_n(\omega)$  for  $\eta \in \mathbb{R}$  and  $\omega > 0$ , given as

$$K_{\eta}(\omega) = \frac{1}{2} \int_0^{\infty} z^{\eta - 1} e^{-\frac{\omega}{2} \left(z + \frac{1}{z}\right)} dz \qquad (13)$$

is a modified Bessel function of the third kind with index  $\eta$   $(K_n(\omega))$  is referred to as a *modified Bessel* function of the second kind in some texts).

An equivalent representation is

$$X \stackrel{\mathcal{D}}{=} \mu + \theta W + \sigma W^{\frac{1}{2}} Z, \quad EW = 1 \tag{14}$$

where Z and W are independently distributed,  $Z \sim$  $\mathcal{N}(0, 1), W \sim \Gamma(\alpha, \alpha)$  as mentioned before. This distributional structure is consistent with the continuoustime model for prices

$$P_t = P_0 \exp \{ \mu t + \theta T_t + \sigma B(T_t) \} \tag{15}$$

where  $\{T_t\}, t \ge 0$ , is a gamma process, exactly as before. The process of independent stationary increments  $\{\log(P_t/P_0)\}, t > 0$ , with the distribution of returns described by equations  $(11)$ – $(13)$ , is also

called the variance-gamma model. Its properties are extensively studied in  $[15]$ .

### **Dependence and Estimation**

The VG model described above is a Lévy process (see Lévy Processes)—a stochastic process in continuous time with stationary independent increments—whose increments are independent and VG distributed. To discuss dependence, we consider the model for returns:

$$X_{t} = \log P_{t} - \log P_{t-1} = \mu + \theta W_{t} + \sigma W_{t}^{1/2} Z_{t},$$
  
$$t = 1, 2, \dots$$
 (16)

where  $Z_t$ ,  $t = 1, 2, \ldots$ , are identically distributed  $\mathcal{N}(0, 1)$  random variables, independent of the strictly stationary process  $\{W_t\}, t = 1, 2, \ldots$  Here  $\theta, \sigma(>0)$  are constants as before.

When  $\theta = 0$ , this discrete-time model is equivalent in distribution to that described by the subordinator model of Heyde [10] given by equations (5)–(8). Note that  $\mathbb{C}ov(X_t, X_{t+k}) = 0$ , while  $\mathbb{C}\text{ov}(X_t^2, X_{t+k}^2) \neq 0, k = 1, 2, \dots$  This is an important feature inasmuch as many asset returns display a sample autocorrelation function plot characteristic of white noise, but no longer do so in a sample autocorrelation plot of squared returns and of absolute values of returns [10, 12, 17].

McLeish [17] considered the distribution of individual  $W_t \sim \Gamma(\alpha, \lambda)$ , which gives the distribution of individual  $X_t$  as (symmetric) VG, which he regarded as a robust alternative to the normal. He suggested a number of ways of introducing the dependence in the process  $\{W_t\}, t = 1, 2, \ldots$ 

The continuous-time subordinator model was expanded in [11] to allow for scaled  $t$ -distributed returns. Their specification of the activity time process in continuous time  $\{T_t\}$  incorporated selfsimilarity (a scaling property) and long-range dependence (LRD) in the stochastic process of squared returns. (LRD in the Allen sense is expressed as divergence of the sequence of ultimately nonnegative autocorrelations of a discrete stationary process.)

The general form of the continuous-time model for prices over continuous time  $t \ge 0$  as

$$P_t = P_0 \exp \{ \mu t + \theta T_t + \sigma B(T_t) \} \tag{17}$$

for which the returns are equivalent in distribution to equation  $(16)$  was given in [23] as a generalization of the subordinator model that allows for skewness in the distribution of returns in the same way as in  $[15]$ , but the returns inherit the postulated strict stationarity of the sequence  $\{W_t\}, t = 1, 2, \ldots$  Following on from [11], Finlay and Seneta [5, 6] studied in detail and in parallel the continuous time structure of the skew VG model and the skew *t*-model, with focus on skewness, asymptotic self-similarity, and LRD.

Maximum-likelihood estimation for independent readings from a symmetric VG distribution is discussed in [17] and in [23], which however proposes moment estimation in the presence of dependence. Moment estimation, allowing for dependence, is further developed in [25], along with goodness of fit of various models for several sets of asset data. A method of simulating data from long-range dependent processes with skew VG or  $t$ -distributed increments is described in [7], and various estimation procedures (method of moments, product-density maximum likelihood, and nonstandard minimum  $\chi^2$  in particular) are tested on the data to assess their performance. In the simulations considered, the product-density maximum-likelihood method performs favorably. The conclusion, within the limited testing carried out, indicates then that, in practice, ordinary product density maximumlikelihood estimation is satisfactory even in the presence of LRD. This is tantamount to saying that one may treat such data on returns as i.i.d. This entails an enormous simplification in estimation procedures in fitting the skew VG and skew  $t$ -distributions.

#### **Option Pricing Applications**

Our discussion is based on the difference of gamma (DG) models for real-world (historical) data:

$$P_t = P_0 e^{\mu t + G_1(t;a,b) - G_2(t;c,d)} \tag{18}$$

where  $\{G(t; \alpha, \beta)\}\$  is a gamma process, and so  $G(t;\alpha,\beta) \sim \Gamma(t\alpha,\beta)$  for any given t, and the two gamma processes are independent of each other. For each t, the returns (4) for  $P_t$  have the following CF:

$$\phi_{\text{DG}}(u;\mu,a,b,c,d) = e^{i\mu u} \left(1 - \frac{\mathrm{i}u}{b}\right)^{-a} \left(1 + \frac{\mathrm{i}u}{d}\right)^{-c} \quad (19)$$

Comparing equations  $(12)$  and  $(19)$ , it is clear that choosing  $c = a$  results in a (skew) VG distribution, with PDF (11) parameters  $\alpha = a, \theta = a \left(\frac{1}{b} - \frac{1}{d}\right)$ , and  $\sigma^2 = \frac{2a}{bd}$ . The further simplification  $b = d$  results in the symmetric VG process for returns.

Using this model for option pricing requires imposing parameter restrictions to ensure that  $\{e^{-rt}P_t\}$  is a martingale, where r is the interest rate. This amounts to ensuring that  $\mathbb{E}(e^{-rt}P_t|\mathcal{F}_s)$  $e^{-rs} P_s$ , where  $\mathcal{F}_s$  represents information available to time  $s < t$ . In the case of the DG process,

$$\mathbb{E}(\mathrm{e}^{-rt}P_t|\mathcal{F}_s)$$
  
=  $\mathrm{e}^{-rs}P_s \times \mathrm{e}^{(\mu-r)(t-s)} \left(\frac{b}{b-1}\right)^{a(t-s)} \left(\frac{d}{d+1}\right)^{c(t-s)}$  (20)

so that imposing the restriction

$$\mu = r - a \log\left(\frac{b}{b-1}\right) - c \log\left(\frac{d}{d+1}\right) \quad (21)$$

with  $b > 1$  results in  $\{e^{-rt} P_t\}$ , which is a martingale with four free parameters:  $a, b, c$ , and  $d$ . We label it  $MDG.$ 

The (skew) VG special case is obtained by choosing  $c = a$ . Relabeling the parameters as above,  $\alpha =$  $a, \theta = a \left(\frac{1}{b} - \frac{1}{d}\right)$ , and  $\sigma^2 = \frac{2a}{bd}$ , results in a martingale that is a (skew) VG process. The mean constraint  $(21)$  now translates to

$$\mu = r + \alpha \log \left( 1 - \frac{\theta + \frac{1}{2}\sigma^2}{\alpha} \right) \tag{22}$$

where we take  $\alpha > \theta + \frac{1}{2}\sigma^2$ . This martingale now has only three free parameters. We label it MVG. This corresponds to the labeling "VG" in [22] and is the martingale used in  $[15]$ .

Both MDG and MVG are, in the terminology of the work by Schoutens [22], "mean-correcting martingales", since the restriction  $(21)$ ,  $(22)$  is on the mean  $(\mu)$  to produce a martingale.

Another way of producing a martingale from a (skew) VG process is to begin by noting from [5] and equation  $(17)$  that irrespective of the distribution of  $T_t$ ,

$$\mathbb{E}(\mathrm{e}^{-rt} P_t | \mathcal{F}_s)$$
  
=  $\mathrm{e}^{-rs} P_s \times \mathrm{e}^{(\mu - r)(t - s)} \mathbb{E}\left(\mathrm{e}^{(\theta + \frac{1}{2}\sigma^2)(T_t - T_s)} | \mathcal{F}_s\right)$   
(23)

where the sequence  $\{W_t\}$ , where  $W_t = T_t - T_{t-1}$ , is strictly stationary.

Thus, if we take  $\mu = r$  and  $\theta = -\frac{1}{2}\sigma^2$  in (23), the right-hand side of equation (23) becomes  $e^{-st} P_s$ , and we have a martingale. This construction of a martingale, simple and quite general, is slightly restrictive, however, in that two parameters,  $\mu$  and  $\theta$ , are constrained. We shall refer to this construction as a skew-correcting martingale, since  $\theta$ , the parameter that determines skewness, is constrained. We denote this martingale model by *MSK*. Out of the "external" parameters  $\mu, \theta$ , and  $\sigma$ , the only parameter that is retained is  $\sigma$ , which is called the *historical volatility* in the Black-Scholes (BS) context, which is a special case when  $T_t = t$ . Any additional parameters in the martingale (risk-neutral) process will be those emanating from the nature of  $\{T_t\}$ , which will need to be specified for any examination of estimation and goodness of fit.

When the CF of the risk-neutral distribution of price is of the closed form, option prices may be calculated using Fourier methods (see Fourier Methods in Options Pricing) as in [3, 14]. Specifically, for  $C(\Upsilon, k)$ , the price of a European call option with time to maturity  $\Upsilon$  and strike price K and  $k = \log(K)$ , let  $q_{\Upsilon}(p)$  be the risk-neutral density of  $\log(P_{\Upsilon})$ , with  $CF \phi_{\Upsilon}(u)$ , at time  $\Upsilon$ . Thus,

$$C(\Upsilon, k) = e^{-r\Upsilon} \mathbb{E}(P_{\Upsilon} - K)^{+}$$
$$= \int_{k}^{\infty} e^{-r\Upsilon} (e^{p} - e^{k}) q_{\Upsilon}(p) \, \mathrm{d}p \quad (24)$$

Define the modified call price as

$$c(\Upsilon, k) = e^{\gamma k} C(\Upsilon, k) \tag{25}$$

for some  $\gamma$  such that  $\mathbb{E}(P_{\Upsilon}^{\gamma+1}) < \infty$ . The Fourier transform of  $c(\Upsilon, k)$  is then given as

$$\Psi_{\Upsilon}(x) = \int_{-\infty}^{\infty} e^{ixk} c(\Upsilon, k) dk\n$$

$$\n= \frac{e^{-r\Upsilon} \phi_{\Upsilon}(x - (\gamma + 1)i)}{\gamma^2 + \gamma - x^2 + ix(2\gamma + 1)} \n$$
(26)

Taking the inverse Fourier transform and using the fact that  $c(\Upsilon, k)$  is real, and using equation (25) gives

$$C(\Upsilon, k) = \frac{e^{-\gamma k}}{2\pi} \int_{-\infty}^{\infty} e^{-ixk} \Psi_{\Upsilon}(x) dx$$
$$= \frac{e^{-\gamma k}}{\pi} \int_{0}^{\infty} \Re\{e^{-ixk} \Psi_{\Upsilon}(x)\} dx \quad (27)$$

In fact, we shall use a modified version of equation (27) suggested in [14]:

$$C(\Upsilon,k) = R_{\gamma} + \frac{\mathrm{e}^{-\gamma k}}{\pi} \int_0^\infty \Re\{\mathrm{e}^{-\mathrm{i} xk} \Psi_{\Upsilon}(x)\} \,\mathrm{d}x \tag{28}$$

where  $R_{\gamma} = \phi_{\Upsilon}(-i)$  for  $-1 < \gamma < 0$ . The choice of  $\gamma$  generally impacts on the error generated by the numerical approximation of equation (28). Finally, the option price  $(28)$  is computed *via* numerical integration.

The option price in this procedure is given simply by the sum of a number of function evaluations. Lee  $[14]$  shows that with a judicious choice of tuning parameters, one can calculate the option price up to 99.99% accuracy with less than 100, and in some cases less than 10, function evaluations. This CF-based pricing method lends itself easily to the fast Fourier transform, which allows for a very fast calculation of a range of option prices.

To numerically illustrate the method and the empirical performance of MVG against some competitors, we  $[8]$  use the data set in  $[22]$ , Appendix C, which contains 77 call option prices on the S&P 500 index at the close of market on April 18, 2002. Fundamentally, each data point consists of the triple: strike, option price, and expiry date.

Fitting models involves estimating model parameters. To do this, we follow [22], p. 7, by minimizing with respect to the model parameters, the root-meansquare error (RMSE):

RMSE

$$= \sqrt{\left(\sum_{\text{options}} \frac{\text{(market price - model price)}^2}{\text{number of options}}\right)}$$
(29)

and then comparing the values of the minimized errors between models. If a model perfectly described the asset price process, the RMSE value would be zero, with all model prices matching market prices, given the single true set of parameters.

The estimates of model parameters produced for a given model correspond to the current market status of that model. The procedure is thus, for a given model, a calibration procedure. No historical data are used in this procedure. The use of this data set for comparison of several different models in this way as already done in [22] allows for easy comparison of goodness of fit. We used the tuning parameter value  $\gamma = -\frac{1}{2}$ ; the other nonmodel constants, q, r, were as in [22], Appendix C.

The RMSE surface for the MDG was reported in [8] to be quite flat, with a number of different parameter values giving essentially the same RMSE value of 2.24. The parameter values that gave the lowest value by 0.001 were as follows:  $a = 4.35, b = 240.86, c =$  $9.79 \times 10^{-6}$ ,  $d = 2.65 \times 10^{-7}$ . The four-parameter MDG model thus did better than the four-parameter CGMY and GH models reported in [22], p. 83, and shown in Table 1.

The VG (skew) model fit reported in [22], p. 83, corresponded to the parameter values  $\alpha (= a = c) =$  $5.4296 \times 10^{-3}$ ,  $b = 14.2699$ ,  $d = 5.8704$ . The recalculation of RMSE with these parameter values reported in  $[8]$  gave the value 3.57. Optimization of RMSE reported in [8] with starting values  $a = c =$  $0.01, b = d = 10$  resulted in the parameter estimates and RMSE as in [22]. Thus in Table 1, the RMSE values reported under VG and MVG are the same, 3.56.

 $As$ expected, this three-parameter model (MVG/VG) does not perform quite as well as the four-parameter models. The VG model is a special case of the GH model, so this is not unexpected.

Finlay and Seneta [8] discuss fitting an MSK martingale model, which allows for LRD in the historical data. This introduces two parameters in addition to the "historical volatility" parameter  $\sigma$ , namely, a parameter  $\alpha$  corresponding to the gamma distribution with mean 1, as before, and a "Hurst" parameter  $H$ associated with dependence. The fit of MSK produces an RMSE of 6.35 and an estimate of  $\sigma = 0.012$ . There is almost no improvement on the BS situation reported in Table 1, which is the standard BS

<table>

 **Table 1** Fit of models to Schoutens [22] option data

|  | Model MDG CGMY GH VG MVG BS        |  |  |
|--|------------------------------------|--|--|
|  | RMSE 2.24 2.76 2.88 3.56 3.56 6.73 |  |  |

martingale model; its RMSE and  $\sigma$ -estimate values are reported in [22], pp. 40-41, and are 6.73 and 0.011, respectively. This apparent insensitivity of the MSK model to departure from BS, possibly due to the skewness parameter being constrained in the martingale construction, is overcome, as reported in  $[8]$ , by a four-parameter ("lack of static arbitrage" model: [2]) model, which is termed as  $C3$ . This model, though not a martingale model, gives an RMSE  $= 0.76$ , and its parameter estimates conform with estimates from historical data for an LRD VG model [7].

Thus, for a given maturity, the three-parameter MVG model and its associated (skew) VG model for historical data perform reasonably well in fitting option prices. If a four-parameter martingale model is to be used, the parent model of MVG that should be used is the MDG, in which the gamma process continues to play a fundamental role.

#### **Historical Notes**

In the case where  $\sigma^2 = 2\alpha$  in the CF (2), the corresponding PDF (11) (with  $\mu = \theta = 0$ ) already appears in [18], p. 184, equation (xlii), and is the theme of  $[19]$ , where it is shown to be the distribution of difference of two i.i.d. gamma random variables, an idea clarified in [13]. The definition of the Bessel function  $K_n(\omega)$  used differs from equation (13). Teichroew [24] obtained the PDF (11) (with  $\mu = \theta =$ 0), in terms of a Hankel function, from the normal variance-mixing structure of the distribution of  $X$ , using form (1) for the PDF of the mixing variable W. These themes are taken up by McLeish [17] as a starting point.

The skew VG distribution with  $\alpha = 2n$ , where *n* is a positive integer, and  $-1 < \theta/\sigma^2 < 1$  appears in [26], a paper generalizing [19], which was also published in 1932.

#### Acknowledgments

Many thanks are due to Richard Finlay for his help.

#### References

 $[1]$ Barndorff-Nielsen, O.E., Kent, J. & Sørensen, M. (1982). Normal variance-mean mixtures and z distributions, International Statistical Review 50, 145–159.

- [2] Carr, P., Geman, H., Madan, D. & Yor, M. (2003). Stochastic volatility for Levy processes, ´ *Mathematical Finance* **13**, 345–382.
- [3] Carr, P. & Madan, D. (1999). Option valuation using the fast Fourier transform, *Journal of Computational Finance* **2**, 61–73.
- [4] Epps, T.W. (2000). *Pricing Derivative Securities*, World Scientific, Singapore.
- [5] Finlay, R. & Seneta, E. (2006). Stationary-increment Student and Variance-Gamma processes, *Journal of Applied Probability* **43**, 441–453.
- [6] Finlay, R. & Seneta, E. (2007). A gamma activity time process with noninteger parameter and self-similar limit, *Journal of Applied Probability* **44**, 950–959.
- [7] Finlay, R. & Seneta, E. (2008a). Stationary-increment Variance-Gamma and *t*-models: simulation and parameter estimation, *International Statistical Review* **76**, 167–186.
- [8] Finlay, R. & Seneta, E. (2008b). Option pricing with VG-like models, *International Journal of Theoretical and Applied Finance* **11**, 943–955.
- [9] Fung, T. & Seneta, E. (2007). Tailweight, quantiles and kurtosis. A study of competing distributions, *Operations Research Letters* **35**, 448–454.
- [10] Heyde, C.C. (1999). A risky asset model with strong dependence through fractal activity time, *Journal of Applied Probability* **36**, 1234–1239.
- [11] Heyde, C.C. & Leonenko, N.N. (2005). Student processes, *Advances in Applied Probability* **37**, 342–365.
- [12] Heyde, C.C. & Liu, S. (2001). Empirical realities for a minimal description risky asset model. The need for fractal features, *Journal of the Korean Mathematical Society* **38**, 1047–1059.
- [13] Kullback, S. (1936). The distribution laws of the difference and quotient of variables independently distributed in Pearson type III laws, *Annals of Mathematical Statistics* **7**, 51–53.
- [14] Lee, R. (2004). Option pricing by transform methods: extensions, unification and error control, *Journal of Computational Finance* **7**, 51–86.
- [15] Madan, D.B., Carr, P.P. & Chang, E.C. (1998). The Variance-Gamma process and option pricing, *European Finance Review* **2**, 79–105.
- [16] Madan, D.B. & Seneta, E. (1990). The Variance-Gamma (V.G.) model for share market returns, *Journal of Business* **63**, 511–524.
- [17] McLeish, D.L. (1982). A robust alternative to the normal distribution, *Canadian Journal of Statistics* **10**, 89–102.

- [18] Pearson, K., Jeffery, G.B. & Elderton, E.M. (1929). On the distribution of the first product-moment coefficient in samples drawn from an indefinitely large normal population, *Biometrika* **21**, 164–201.
- [19] Pearson, K., Stouffer, S.A. & David, F.N. (1932). Further applications in statistics of the *Tm(x)* Bessel function, *Biometrika* **24**, 316–343.
- [20] Praetz, P.D. (1972). The distribution of share price changes, *Journal of Business* **45**, 49–55.
- [21] Press, S.J. (1967). A compound events model for security prices, *Journal of Business* **40**, 317–335.
- [22] Schoutens, W. (2003). *L´evy Processes in Finance. Pricing Financial Derivatives*, Wiley, Chichester.
- [23] Seneta, E. (2004). Fitting the Variance-Gamma model to financial data, in *Stochastic Methods and Their Applications (C.C. Heyde Festschrift)*, J. Gani & E. Seneta, eds, Journal of Applied Probability, Vol. 41A, pp. 177–187.
- [24] Teichroew, D. (1957). The mixture of normal distributions with different variances, *Annals of Mathematical Statistics* **28**, 510–512.
- [25] Tjetjep, A. & Seneta, E. (2006). Skewed normal variance-mean models for asset pricing and the method of moments, *International Statistical Review* **74**, 109–126.
- [26] Wishart, J. & Bartlett, M.S. (1932). The distribution of second order moment statistics in a normal system, *Proceedings of the Cambridge Philosophical Society* **28**, 455–459.

# **Further Reading**

Seneta, E. (2007). The early years of the Variance-Gamma process, in *Advances in Mathematical Finance (Dilip B. Madan Festschrift)*, M.C. Fu, R.A. Jarrow, J.-Y.J. Yen, & R.J. Elliott, eds, Birkhauser, Boston, pp. 3–19. ¨

## **Related Articles**

**Exponential Levy Models ´** ; **Generalized Hyperbolic Models**; **Hazard Rate**; **Heavy Tails**; **Levy ´ Processes**; **Stylized Properties of Asset Returns**; **Tempered Stable Process**.

EUGENE SENETA
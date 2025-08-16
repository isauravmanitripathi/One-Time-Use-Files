# **Ruin Models with Investment Income**

The problem of ruin has a long history in risk theory, going back to Lundberg [13]. Initially the assumption was that companies do not earn any investment return on their capital. The first attempt to incorporate investment incomes was undertaken by Segerdahl [19]. Segerdahl's assumption was that capital earns interest at a fixed rate  $r$ . This model was further elaborated in [8, 11], and it remains very popular even today. Then inspired by ideas from mathematical finance, in [14] a model was suggested where capital is allowed to be invested in risky assets. Before presenting this model, we refer the reader to [16] for a more extensive survey, including several topics not covered here.

To make the ideas transparent, we introduce the risk process by means of two basic processes, that is,

- a basic risk process  $P$  with  $P_0 = 0$  and
- a return on investment-generating process  $R$  with  $R_0 = 0.$

If  $P$  and  $R$  belong to the rather general class of semimartingales, we can define the risk process as

$$Y_t = y + P_t + \int_0^t Y_{s-} \mathrm{d}R_s \tag{1}$$

so that  $Y_0 = y$ . The solution of this equation is

$$Y_t = e^{\tilde{R}_t} \left( y + \int_0^t e^{-\tilde{R}_s} dP_s \right) \tag{2}$$

where  $\tilde{R} = \log \mathcal{E}(R)$  is the logarithm of the Doléans– Dade exponential of R, that is,  $V_t = \mathcal{E}(R)_t$  satisfies the equations  $dV_t = V_{t-}dR_t$  and  $V_0 = 1$ .

In this article, it is assumed that  $P$  and  $R$  are of the following forms:

$$P_{t} = pt + \sigma_{P} W_{P,t} - \sum_{i=1}^{N_{t}} S_{i}$$
 (3)

$$R_t = rt + \sigma_R W_{R,t} \tag{4}$$

where  $W_P$  and  $W_R$  are Brownian motions, N is a Poisson process with rate  $\lambda$ , and  $\{S_i\}$  are nonnegative independent and identically distributed (i.i.d.) random

variables with distribution function  $F$ . Furthermore,  $W_P$ ,  $W_R$ , N, and  $\{S_i\}$  are all independent. The idea is that p is the premium rate,  $\{S_i\}$  are claims, while  $W_P$  represents fluctuations in premium income and maybe also small claims. The return on investmentgenerating process  $R$  is the standard Black–Scholes return process. With these assumptions,  $Y$  becomes a homogeneous, strong Markov process, a fact that allows us to draw on the vast literature on Markov processes. In addition,  $\tilde{R}_t = R_t - \frac{1}{2}\sigma_R^2 t =$  $(r-\frac{1}{2}\sigma_R^2)t+\sigma_R W_{R,t}.$ 

The time of ruin is defined as  $T = \inf\{t : Y_t < 0\},\$ with  $T = \infty$  if Y stays positive. The probability of ruin in finite *versus* infinite time is then defined as

$$\psi(t, y) = P(T \le t | Y_0 = y) \quad \text{and}$$
  
$$\psi(y) = P(T < \infty | Y_0 = y) \tag{5}$$

Mathematically,  $\psi(y)$  is the easiest, and probably as a consequence, it has by far been the most popular in the literature.

A more general concept that also allows for problems relating to the time of ruin, the size of the deficit at ruin, or the surplus immediately before ruin is the Gerber–Shiu penalty function [9]. It is given as

$$\Phi_{\alpha}(y) = E[g(Y_{T-}, |Y_T|)e^{-\alpha T}1_{\{T<\infty\}}|Y_0 = y] \quad (6)$$

where g is a nonnegative function and  $\alpha > 0$ . Various choices of g and  $\alpha$  allow for the computation of many interesting quantities related to ruin [4].

### **Some General Results**

It is shown in [15] that under weak assumptions,  $\psi(y) < 1$  if  $r > \frac{1}{2}\sigma_R^2$  (equivalence when  $\sigma_R^2 > 0$ ), and in this case it is proved in [10] that under some weak additional assumptions,  $\psi$  is twice continuously differentiable and is a solution of the equation,

$$G\psi(y) = -\lambda \bar{F}(y) \tag{7}$$

with boundary conditions

$$\lim_{y \to \infty} \psi(y) = 0 \quad \text{and} \quad \psi(0) = 1 \text{ if } \sigma_P > 0 \quad (8)$$

Here  $G$  is the integro-differential operator

$$Gh(y) = \frac{1}{2}(\sigma_P^2 + \sigma_R^2 y^2)h''(y) + (p + ry)h'(y)$$
$$+ \lambda \int_0^y h(y - x)dF(x) - \lambda h(y) \tag{9}$$

and  $\bar{F}(y) = 1 - F(y)$ . Sometimes it is more convenient to work with the survival probability  $\phi(y)$  =  $1 - \psi(y)$ , in which case equation (2) becomes  $G\phi(y) = 0$ . It is shown in [4] that the Gerber-Shiu penalty function satisfies an equation similar to  $\text{equation (2)}$ .

Following ideas from [11], it was shown in [14] that the ruin probability can be written as

$$\psi(y) = \frac{H(-y)}{E[H(-Y_T)|T < \infty]} \tag{10}$$

where  $H$  is the distribution function of the perpetuity

$$X = \int_0^\infty e^{-\left(r - \frac{1}{2}\sigma_R^2\right)t + \sigma_R W_{R,t}} dP_t \tag{11}$$

Corresponding to equation  $(2)$ , the finite time ruin probability  $\psi(t, y)$  should be the solution to the partial integro-differential equation

$$-\frac{\partial}{\partial t}\psi(t, y) + G\psi(t, y) = -\lambda \bar{F}(y) \tag{12}$$

with the additional boundary condition  $\psi(0, y) =$  $1_{\{y<0\}}$ . Here, the operator G acts on the y variable.

#### **Analytical and Numerical Solutions**

Since most analytical results are for the infinite time horizon, we start with this case. When  $\lambda = 0$ , the process is a pure diffusion process and the problem becomes rather easy. A solution can be found in [14]. When  $\lambda > 0$ , things become markedly more complex, and analytical solutions can be obtained only in a few rather simple cases. In addition, several of these solutions are very complicated. In all known solutions, it is assumed that  $\sigma_R = 0$ , so in the sequel we shall therefore tacitly let  $\sigma_R = 0$ .

We have already mentioned Segerdahl's classical work when  $\sigma_P = 0$  and claim sizes are exponentially distributed. In  $[17]$ , these solutions were extended to the case where claims are mixtures of two exponential

distributions, as well as to the case where they are Erlang (2) distributed. Extensions beyond that seem very difficult though. In [17], the case with  $\sigma_P > 0$ and claims exponentially distributed was also solved. In [5], rather explicit expressions for the Gerber-Shiu penalty function are given for the case where  $\sigma_P = 0$ and claims are exponentially distributed.

In the finite time horizon case, analytical solutions are hard to come by. In [1], a recursion for the survival probability  $\phi(t, y)$  when  $\lambda = kr$  for some positive integer  $k$  is provided. This recursion is solved and exact solutions are given for  $k = 1$  and  $k = 2$ .

The issue of computing numerical values has received comparatively little attention. In [18], using integration by parts on the equation  $G\phi(y) = 0$ , this equation was turned into a Volterra integral equation and methods from numerical analysis were used to solve this numerically. In the finite time case, several methods have been proposed when  $\sigma_P = \sigma_R = 0$ ; see, for example [3, 6]. These methods are rather intuitive in nature and are not based on any particular known procedure from numerical analysis. Their efficiency is, therefore, slightly low, but as a bonus they provide upper and lower bounds.

An alternative to traditional numerical methods is the Monte Carlo simulation, which is particularly well suited for finite time ruin problems. For infinite time ruin problems, some care has to be taken as to when the simulation should stop. An alternative is to simulate under an equivalent measure  $\tilde{P}$  so that  $\tilde{P}(T < \infty | Y_0 = y) = 1.$  Then with  $M_t$  equal to  $\frac{d\tilde{P}}{dP}$ restricted to  $\sigma\{Y_s : s < t\},\$ 

$$\psi(y) = \tilde{E}[M_T^{-1}|Y_0 = y] \tag{13}$$

Hence what is required is repetitive simulation of  $M_T$  under  $\tilde{P}$ . The catch is that this kind of importance sampling is very dangerous (due to the possible explosion of the variance of the Monte Carlo estimator) and can lead to completely wrong results.

#### **Asymptotic Results**

If there are only a few papers dealing with numerical solutions, there is certainly a fair number dealing with asymptotic results, that is, the behavior of  $\psi(y)$  or  $\psi(t, y)$  when y gets large. To present a few of the most prominent or recent results, we shall need some definitions. As before, let  $\bar{F}(x) = 1 - F(x)$  and let  $F^{*n}(x)$  be the *n*-fold convolution of *F*.

- $F \in \mathcal{R}_{-\alpha}$  if  $\bar{F}(x) = x^{-\alpha}l(x)$  where l is a slowly varying function, that is,  $\lim_{x\to\infty} \frac{l(tx)}{l(x)} = 1$  for all  $t > 0$ .
- $F \in \mathcal{S} \text{ if } \lim_{x \to \infty} \frac{\overline{F^{*2}}(x)}{\overline{F}(x)} = 2.$

We have  $\mathcal{R}_{-\alpha} \subset \mathcal{S}$ . The class  $\mathcal{S}$  is called the *class* of subexponential distributions, and among others it contains the lognormal, loggamma as well as the Weibull distribution with  $\bar{F}(x) = e^{-(x/\beta)^{\gamma}}$  for  $\gamma < 1$ . It can be shown that if  $F \in \mathcal{S}$ , then  $E[e^{tS}] = \infty$ for all  $t > 0$ , and hence the name *subexponential* distribution.

Culminating through a series of papers, it was proved in [12] that when  $\sigma_R = 0$  and  $F \in \mathcal{S}$ ,

$$\psi(t, y) \sim \frac{\lambda}{r} \int_{y}^{ye^{rt}} \frac{\bar{F}(x)}{x} \mathrm{d}x, \quad 0 < t \le \infty \quad (14)$$

For the light-tailed case with  $\sigma_R = 0$ , results are a little less explicit. Let  $\kappa = \sup\{a : E[e^{aS}] < \infty\}.$ Then it was proved in [7] that for any  $\varepsilon > 0$ ,

$$\lim_{y \to \infty} y^{(\kappa - \varepsilon)y} \psi(y) = 0 \quad \text{and}$$
  
$$\lim_{y \to \infty} y^{(\kappa + \varepsilon)y} \psi(y) = \infty \tag{15}$$

It was also shown by examples that anything can happen to  $\lim_{y\to\infty} y^{\kappa} \psi(y)$ .

When  $\sigma_R > 0$  the picture is slightly less complex. The reason for this is that the financial risk caused by variations in the return process  $R$  corresponds to claims  $F \in \mathcal{R}_{-\kappa}$  with  $\kappa = \frac{2r}{\sigma_R^2} - 1$ . Hence, when claims have lighter tails than this, the asymptotics is dominated by  $R$ . Various results in this direction appear in the literature and the most precise results for the model studied here are those in [10]. There it is assumed that  $\sigma_P = 0$ , but due to the lighttailed effect of  $W_P$ , the result is valid for  $\sigma_P > 0$  as well. To present the results, remember that  $\psi(y) = 1$ when  $\kappa < 0$ , so assume that  $\kappa > 0$  and also that  $E[S] < \infty.$ 

- 1. If for some  $\varepsilon > 0$ ,  $E[S^{\kappa+\varepsilon}] < \infty$ , then  $\lim_{\nu \to \infty}$  $y^{\kappa} \psi(y) = c$  for some (for all practical purposes) unknown  $c$ .
- 2. If  $\overline{F}(x) = x^{-\rho}l(x)$  where  $\rho < \kappa$ , then

$$\psi(y) \sim \frac{2\lambda}{\sigma_R^2 \rho(\kappa - \rho)} y^{-\rho} l(y) \qquad (16)$$

The limiting case  $F \in \mathcal{R}_{-\kappa}$  needs to be treated separately  $[10]$ .

#### Inequalities

Several inequalities for the ruin probability exist, but the problem is that either they are not very sharp or they are difficult to compute. An example that follows directly from equation  $(3)$  is

$$H(-y) \le \psi(y) \le \frac{H(-y)}{H(0)}\tag{17}$$

and when  $F$  has decreasing failure rate, the right-hand side can be strengthened to  $\frac{H(-y)}{E[H(S)]}$ . The problem here is that the distribution function *H* is not known.

An upper bound that is easier to compute, but restricted to the case with  $\sigma_P = \sigma_R = 0$  and lighttailed claims, is given in [2]. To explain, assume that the equation

$$\lambda \left( \int_0^\infty e^{\gamma(s)x} dF(x) - 1 \right) - \gamma(s)(p + rs) = 0 \tag{18}$$

has a positive solution  $\gamma^*(s)$  for all  $0 < s < \gamma$ . Then

$$\psi(y) \le e^{-\int_0^y \gamma^*(s)ds} \tag{19}$$

#### References

- Albrecher, H., Teugels, J.L. & Tichy, R.F. (2001). [1] On gamma series expansion for the time-dependent probability of collective ruin, Insurance, Mathematics and Economics 29, 345-355.
- [2] Asmussen, S. & Nielsen, H.M. (1995). Ruin probabilities via local adjustment coefficients, Journal of Applied Probability 32, 736–755.
- Brekelmans, R. & De Waegenaere, A. (2001). Approx-[3] imating the finite-time ruin probability under interest force, Insurance, Mathematics and Economics 29,  $217 - 229$
- [4] Cai, J. (2004). Ruin probabilities and penalty functions with stochastic rates of interest, Stochastic Processes and their Applications 112, 53-78.
- Cai, J. (2007). On the time value of absolute ruin [5] with debit interest, Advances in Applied Probability 39, 343-359.
- [6] Cardoso, R.M.R. & Waters, H.R. (2003). Recursive calculation of finite time ruin probabilities under interest force, Insurance, Mathematics and Economics 33, 659-676.

## **4 Ruin Models with Investment Income**

- [7] Embrechts, P. & Schmidli, H. (1994). Ruin estimation for a general insurance risk model, *Advances in Applied Probability* **26**, 404–422.
- [8] Gerber, H.U. (1971). Der Einfluss von Zins auf die Ruinwahrscheinlichkeit, *Mitteilungen der Schweizerischer Vereinigung der Versicherungsmatematiker* **71**, 63–70.
- [9] Gerber, H.U. & Shiu, E.S.W. (1998). On the time value of ruin, *North American Actuarial Journal* **2**, 48–78.
- [10] Grandits, P. (2004). A Karamata-type theorem and ruin probabilities for an insurer investing proportionally in the stock market, *Insurance, Mathematics and Economics* **34**, 297–305.
- [11] Harrison, J.M. (1977). Ruin problems with compounding assets, *Stochastic Processes and their Applications* **5**, 67–79.
- [12] Jiang, T. & Yan, H.-F. (2006). The finite-time ruin probability for the jump-diffusion model with constant interest force, *Acta Mathematicae Applicatae Sinica* **22**, 171–176.
- [13] Lundberg, F. (1903). *Approximerad Framstilling av Sannolikhetsfunktionen II. Aterfors¨ ˚ akring av Kollektivrisker*, Almquist & Wiksell, Uppsala.
- [14] Paulsen, J. (1993). Risk theory in a stochastic economic environment, *Stochastic Processes and their Applications* **46**, 327–361.

- [15] Paulsen, J. (1998). Sharp conditions for certain ruin in a risk process with stochastic return on investments, *Stochastic Processes and their Applications* **75**, 135–148.
- [16] Paulsen, J. (2008). Ruin models with investment incomes, *Probability Surveys (Electronic)* **5**, 416–434.
- [17] Paulsen, J. & Gjessing, H.K. (1997). Ruin theory with stochastic return on investments, *Advances in Applied Probability* **29**, 965–985.
- [18] Paulsen, J., Kasozi, J. & Steigen, A. (2005). A numerical method to find the probability of ultimate ruin in the classical risk model with stochastic return on investments, *Insurance, Mathematics and Economics* **36**, 399–420.
- [19] Segerdahl, C.O. (1942). Uber einige risikotheoretis- ¨ che Fragestellungen, *Skandinavisk Aktuartidsskrift* **25**, 43–83.

## **Related Articles**

**Cramer–Lundberg Estimates ´** ; **Merton Problem**; **Ruin Theory**.

JOSTEIN PAULSEN
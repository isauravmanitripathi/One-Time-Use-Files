# Saddlepoint Approximation

The classical method known variously as the *saddlepoint approximation*, the *method of steepest descents*, the *method of stationary phase*, or the *Laplace method*, applies to contour integrals that can be written in the form

$$I(s) = \int_{\mathcal{C}} e^{sf(\zeta)} d\zeta \tag{1}$$

where  $f$ , an analytic function, has a real part that goes to minus infinity at both ends of the contour  $C$ . The fundamental idea is that the value of the integral when  $s > 0$  is large should be dominated by contributions from the neighborhoods of points where the real part of  $f$  has a saddlepoint. Early use was made of the method by Debye to produce asymptotics of Bessel functions, as reviewed in, for example, [8]. Daniels [3] wrote a definitive work on the saddlepoint approximation in statistics. Later, these ideas evolved into the theory of large deviations, initiated by Varadhan in [7], which seeks to determine rigorous asymptotics for the probability of rare events.

If we write  $\zeta = x + iy$ , elementary complex analysis implies that the surface over the  $(x, y)$  plane with graph  $\Re f$  has zero mean curvature, so any critical point  $\zeta^*$  (a point where  $f' = 0$ ) will be a saddlepoint of the modulus  $|e_{f(\zeta)}^s|$ . The level curves of  $\Re f$ and  $\Im f$  form families of orthogonal trajectories: the curves of steepest descent of  $\Re f$  are the level curves of  $\Im f$ , and *vice versa*. Thus the curve of steepest descent of the function  $\Re f$  through  $\zeta^*$  is also a curve on which  $\Im f$  is constant. In other words, it is a curve of "stationary phase". On such a curve, the modulus of  $e^{sf(\zeta)}$  will have a sharp maximum at  $\zeta^*$ . If the contour  $C$  can be deformed to follow the curve of steepest descent through a unique critical point  $\zeta^*$ , and the modulus of  $e^{sf(\zeta)}$  is negligible elsewhere, the dominant contribution to the integral for large  $s$  can be computed by a local computation in the neighborhood of  $\zeta^*$ . In more complex applications, several critical points may need to be accounted for.

The tangent line to the steepest descent curve at  $\zeta^*$  can be parameterized by  $w \in \mathbb{R}$  by the equation

$$(s f^{(2)}(\zeta^*))^{1/2}(\zeta - \zeta^*) = \mathrm{i} w \tag{2}$$

(care is needed here to select the correct sign of the complex square root), and on this line, the Taylor expansion of  $f$  about  $\zeta^*$  implies

$$f(z) = f(\zeta^*) + \sum_{n \ge 2} \frac{1}{n!} f^{(n)}(\zeta^*) \left(\frac{\mathrm{i}w}{s(f^{(2)}(\zeta^*))^{1/2}}\right)^n \tag{3}$$

One can write the integrand in the form

$$e^{sf(z)} \sim e^{sf(\zeta^*) - w^2/2} \left[ 1 - i s^{-1/2} \frac{f^{(3)}(\zeta^*)}{3! (f^{(2)}(\zeta^*))^{3/2}} w^3 + s^{-1} \left( \frac{f^{(4)}(\zeta^*)}{4! (f^{(2)}(\zeta^*))^2} w^4 - \frac{(f^{(3)}(\zeta^*))^2}{2! (3!)^2 (f^{(2)}(\zeta^*))^3} w^6 \right) + \cdots \right]$$
(4)

Now approximating the integral over  $\mathcal{C}$  by the integral over the tangent line parameterized by  $w$  leads to a series of Gaussian integrals, each of which can be computed explicitly. The terms with an odd power of  $w$  all vanish, leading to the result

$$I(s) \sim \mathbf{i} \left(\frac{2\pi}{sf^{(2)}(\zeta^*)}\right)^{1/2} e^{sf(\zeta^*)}$$
$$\times \left[1 + s^{-1} \left(\frac{3f^{(4)}(\zeta^*)}{4!(f^{(2)}(\zeta^*))^2} - \frac{5 \cdot 3 \cdot (f^{(3)}(\zeta^*))^2}{2!(3!)^2 (f^{(2)}(\zeta^*))^3}\right) + \dots\right] \tag{5}$$

#### **Daniels' Application to Statistics**

Daniels [3] presented an asymptotic expansion for the probability density function (pdf)  $f_n(x)$  of the mean  $\bar{X}_n$  of *n* i.i.d. copies of a continuous random variable X with cumulative probability function  $F(x)$  and pdf  $f(x) = F'(x)$ . Assuming that the moment generating function

$$M(\tau) = e^{\Psi(\tau)} = \int_{-\infty}^{\infty} e^{\tau x} f(x) dx \qquad (6)$$

is finite for  $\tau$  in an open interval  $(-c_1, c_2)$  containing the origin, the Fourier inversion theorem implies that

$$f_n(x) = \frac{n}{2\pi i} \int_{\alpha - i\infty}^{\alpha + i\infty} e^{n(\Psi(\tau) - \tau x)} d\tau \qquad (7)$$

for any real  $\alpha \in (-c_1, c_2)$ . This integral is now amenable to a saddlepoint treatment as follows.

For each  $x$  in the support of  $f$ , one can show that the saddlepoint condition

$$\Psi'(\tau) - x = 0 \tag{8}$$

has a unique real solution  $\tau^* = \tau^*(x)$ . One now evaluates the integral given by equation (7) with  $\alpha =$  $\tau^*$ , and uses Taylor expansion and the substitution  $w = -i\sqrt{n\Psi''(\tau^*)}(\tau - \tau^*)$  to write

$$f_n(x) \sim \frac{\sqrt{n}}{2\pi\sqrt{\Psi''(\tau^*)}} \int_{-\infty}^{\infty} e^{n(\Psi(\tau^*) - \tau^* x) - w^2/2} \times \left[1 + i n^{-1/2} (\Psi''(\tau^*))^{-3/2} \Psi^{(3)}(\tau^*) w^3/3! + n^{-1} (\Psi''(\tau^*))^{-2} \Psi^{(4)}(\tau^*) w^4/4! + \ldots\right] \mathrm{d}w$$
(9)

Each term in this expansion is a Gaussian integral that can be evaluated in closed form. The odd terms all vanish, leaving an expansion in powers of  $n^{-1}$ :

$$f_n(x) \sim g_n(x) \left[ 1 + n^{-1} \left( \frac{\Psi^{(4)}(\tau^*)}{8(\Psi''(\tau^*))^2} - \frac{5(\Psi^{(3)}(\tau^*))^2}{24(\Psi''(\tau^*))^3} \right) + O(n^{-2}) \right]$$
(10)

where the leading term (called the *saddlepoint approximation*) is given by

$$g_n(x) = \left(\frac{n}{2\pi \Psi''(\tau^*)}\right)^{1/2} e^{n(\Psi(\tau^*) - \tau^* x)} \qquad (11)$$

The function  $I(x) = \sup_{\tau} \tau x - \Psi(\tau) = \tau^* x - \Psi(\tau)$  $\Psi(\tau^*)$  that appears in this expression is the Legendre transform of the cumulant generating function  $\Psi$ , and is known as the rate function or Cramér function of the random variable X. The *large deviation principle* 

$$\lim_{n \to \infty} \frac{1}{n} \log P(\bar{X}_n > x) = -I(x) \quad \text{for } x > E[X]$$
(12)

holds for very general  $X$ . Another observation is that the Edgeworth expansion of statistics comes out in a similar way, but takes 0 instead of  $\tau^*$  as the center of the Taylor expansion.

One can show, using a lemma due to Watson [8], that equation  $(10)$  is an *asymptotic expansion*,

which means roughly that when truncated at any order of  $n^{-1}$ , the remainder is of the same magnitude as the first omitted term. A more precise statement of the magnitude of the remainder is difficult to establish: the lack of a general error analysis is an acknowledged deficiency of the saddlepoint method.

### Applications to Portfolio Credit Risk

The problem of portfolio credit risk measures and the problem of evaluating arbitrage-free pricing of collateralized debt obligations (CDOs) both boil down to computation of the probability distribution of the portfolio loss at a set of times, and can be amenable to a saddlepoint treatment. To illustrate this fact, we consider a simple portfolio of credit risky instruments (e.g., corporate loans or credit default swaps), and investigate the properties of the losses caused by default of the obligors. Let  $(\Omega, \mathcal{F}, \mathcal{F}, P)$  be a filtered probability space that contains all of the random elements:  $P$  may be either the physical or the riskneutral probability measure. The portfolio is defined by the following basic quantities:

- $\bullet$  *M* reference obligors with notional amounts  $N_i, j = 1, 2, \ldots, M;$
- the default time  $\tau_i$  of the *j*th credit, an  $\mathcal{F}_t$ stopping time;
- the fractional recovery  $R_i$  after default of the jth . obligor;
- the loss  $l_i = (1 R_i)N_i/N$  caused by default of the *j*th obligor as a fraction of the total notional  $N = \sum_{i} N_{i};$
- the cumulative portfolio loss  $L(t) = \sum_{j} l_{j} I(\tau_{j} \leq t)$  $\bullet$  $t)$  up to time  $t$  as a fraction of the total notional.

For simplicity, we make the following assumptions:

- 1. The discount factor is  $v(t) = e^{-rt}$  for a constant interest rate  $r \geq 0$ .
- The fractional recovery values  $R_i$  and hence  $l_i$ 2. are deterministic constants.
- 3. There is a sub  $\sigma$ -algebra  $\mathcal{H} \subset \mathcal{F}$  generated by a *d*-dimensional random variable  $Y$ , the "condition", such that the default times  $\tau_i$  are mutually conditionally independent under  $\mathcal{H}$ . The marginal distribution of Y is denoted by  $P_Y$  and has pdf  $\rho_Y(y), y \in \mathbb{R}^d$ .

The most important consequence of these assumptions is that, conditioned on  $\mathcal{H}$ , the fractional loss  $L(t)$  is a sum of independent (but not identical) Bernoulli random variables. For fixed values of the time  $t$  and conditioning random variable  $Y$ , we note that  $\hat{L} := L(t)|_{Y} \sim \sum_{j} l_{j}X_{j}$  where  $X_{j} \sim$  $\text{Bern}(p_i(t, y)), \ p_i = \text{Prob}(\tau_i \le t | Y = y).$  The following functions are associated with the random variable  $\hat{L}$ :

- 1. the pdf  $\rho(x) := F^{(-1)}(x)$  (in our simple example, it is a sum of delta functions supported on the interval  $[0, 1]$ ;
- 2. the *cumulative distribution function* (CDF)  $F^{(0)}$  $(x) = E[I(\hat{L} \le x)];$
- 3. the higher conditional moment functions  $F^{(m)}(x)$  $=(m!)^{-1}E[((x-\hat{L})^+)^m], m=1,2,\ldots;$
- the *cumulant generating function* (CGF)  $\Psi(u) =$ 4.  $\log(E[e^{u\hat{L}}]).$

When we need to make explicit the dependence on t, v we write  $F^{(m)}(x|t, v)$ . The unconditional versions of these functions are given by

$$F^{(m)}(x|t) = E[F^{(m)}(x|t,Y)] = \int_{\mathbb{R}}^{d} F^{(m)}(x|t,y)$$
$$\times \rho_Y(\mathrm{d}y), \ m = -1, 0, \dots \tag{13}$$

According to these definitions, for all  $m = 0, 1, \ldots$ we have the integration formula

$$F^{(m)}(x) = \int_0^x F^{(m-1)}(z) \, \mathrm{d}z \tag{14}$$

#### Credit Risk Measures

In risk management, the key quantities that determine the economic capital requirement for such a credit risky portfolio are the Value at Risk (VaR) and Conditional Value at Risk (CVaR) for a fixed time horizon T and a fixed confidence level  $\alpha$  < 1. These are defined as follows:

$$\text{VaR}_{\alpha}(L_T) = \inf\{x|F^{(0)}(x|T) > \alpha\} \tag{15}$$

$$\text{CVaR}_{\alpha}(L_T) = \frac{E[(L_T - x)^+]}{1 - \alpha}$$
$$= \frac{F^{(1)}(x|T) + E[L_T] - x}{1 - \alpha} \quad (16)$$

Here, we need to take  $P$  to be the physical measure.

## CDO Pricing

CDOs are portfolio credit swaps that can be schematically decomposed into two types of basic contingent claims whose cash flows depend on the portfolio loss  $L_t$ . These cash flows are analogous to insurance and premium payments paid periodically (typically, quarterly) on dates  $t_k$ ,  $k = 1, \ldots, K$ , to cover default losses within a "tranche" that occurred during that period.

The writer (the *insurer*) of one unit of a default leg for a tranche with attachment levels  $0 \le a < b \le 1$ pays the holder (the *buyer of insurance*) at each date  $t_k$  all default losses within the interval [a, b] that occurred over  $[t_{k-1}, t_k]$ . The time 0 arbitrage price of such a contract is

$$W_{a,b} = \sum_{k} e^{-rt_{k}} E\left[ (b - L_{t_{k}})^{+} - (b - L_{t_{k-1}})^{+} - (a - L_{t_{k}})^{+} + (a - L_{t_{k-1}})^{+} \right]$$
(17)

where  $E$  is now the expectation with respect to some risk-neutral measure. The writer of one unit of a premium leg for a tranche with attachment levels  $a < b$  (the insured) pays the holder (the insurer) on each date  $t_k$  an amount jointly proportional to the year fraction  $t_k - t_{k-1}$  and the amount remaining in the tranche. We ignore a possible "accrual term" that account for defaults between payment dates. The time 0 arbitrage price of such a contract is

$$V_{a,b} = \sum_{k} e^{-rt_{k}} (t_{k} - t_{k-1}) E\left[ (b - L_{t_{k}})^{+} - (a - L_{t_{k}})^{+} \right]$$
(18)

The *CDO rate*  $s_{a,b}$  for this contract at time 0 is the number of units of the premium leg that has the same value as one unit of the default leg, that is,  $s_{a,b} = W_{a,b}/V_{a,b}.$ 

# Saddlepoint Approximations for $F^{(m)}$

We see that the credit risk management problem and the CDO pricing problem both boil down to finding an efficient method to compute  $E[F^{(m)}(x|t, y)]$  for  $m = 0$ , 1 and a large but finite set of values  $(x, t, y)$ . For the conditional loss  $\hat{L} = L_t | Y = y$ , the CGF is explicit

$$\Psi(u) = \sum_{j=1}^{M} \log \left[1 - p_j + p_j \, \mathrm{e}^{u l_j}\right] \qquad (19)$$

We suppose that the conditional default probabilities  $p_i = p_i(t, y)$  are known. A number of different strategies can be used to compute this distribution accurately:

- 1. In the fully homogeneous case when  $p_i =$  $p, l_i = l$ , the distribution is binomial.
- 2. When  $l_i = l$ , but  $p_i$  are variable (the homogeneous notional case), these probabilities can be computed highly efficiently by a recursive algorithm in  $[1, 5]$ .
- 3. When both  $l_i$ ,  $p_i$  are variable, it has been noted in  $[2, 4, 6, 9]$  that a saddlepoint treatment of these problems offer superior performance over a naive Edgeworth expansion.

We now consider the fully nonhomogeneous case and begin by using the Laplace inversion theorem to write

$$\rho(x) = F^{(-1)}(x) = \frac{1}{2\pi} \int_{\alpha - i\infty}^{\alpha + i\infty} e^{\Psi(\tau) - \tau x} d\tau \quad (20)$$

Since  $\rho$  is a sum of delta functions, this formula must be understood in the distributional sense, and holds for any real  $\alpha$ . When  $\alpha < 0$ ,

$$F^{(0)}(x) = \frac{1}{2\pi} \int_{\alpha - i\infty}^{\alpha + i\infty} e^{\Psi(\tau)} \frac{1 - e^{-\tau x}}{\tau} d\tau$$
$$= -\frac{1}{2\pi} \int_{\alpha - i\infty}^{\alpha + i\infty} \tau^{-1} e^{\Psi(\tau) - \tau x} d\tau \quad (21)$$

In the last step in this argument, one term is zero because  $e^{\Psi(\tau)}$  is analytic and decays rapidly as  $\Re \tau \rightarrow$  $-\infty$ . Similarly, for  $m = 1, 2, \ldots$  one can show that

$$F^{(m)}(x) = (-1)^{m+1} \frac{1}{2\pi} \int_{\alpha - i\infty}^{\alpha + i\infty} \tau^{-m-1} e^{\Psi(\tau) - \tau x} d\tau \tag{22}$$

provided  $\alpha < 0$ . It is also useful to consider the functions

$$G^{(m)}(x) := (-1)^{m+1} \frac{1}{2\pi} \int_{\alpha - \mathbf{i}\infty}^{\alpha + \mathbf{i}\infty} \tau^{-m-1} e^{\Psi(\tau) - \tau x} \, d\tau \tag{23}$$

defined when  $\alpha > 0$ . One can show by evaluating the residue at  $\tau = 0$  that

$$F^{(0)}(x) = G^{(m)}(x) - 1 \tag{24}$$

$$F^{(1)}(x) = G^{(1)}(x) - E[L] + x \tag{25}$$

with similar formulas relating  $F^{(m)}$  and  $G^{(m)}$  for  $m = 2, 3, \ldots$ 

Since the conditional portfolio loss is a sum of similar, but not identical, independent random variables, we can follow the argument of Daniels to produce an expansion for the functions  $F^{(m)}$ . Some extra features are involved: the cumulant generating function is not  $N$  times something, but rather a sum of  $N$  (easily computed) terms: we must deal with the factor  $\tau^{-m-1}$ ; we must deal with the fact that critical points of the exponent in these integrals may be on the positive or negative real axis and there is a pole at  $\tau = 0$ . To treat the most general case, we move the factor  $\tau^{-m-1}$  into the exponent and consider the saddlepoint condition

$$\Psi'(\tau) - (m+1)/\tau - x = 0 \tag{26}$$

Proposition 5.1 from  $[9]$  shows that a choice of two real saddlepoints solving this equation is typically available:

**Proposition 1** Suppose that  $p_j$ ,  $l_j > 0$  for all j. Then

- 1. There is a solution  $\tau^*$ , unique if it exists, of  $\Psi'(\tau) - x = 0$  if and only if  $0 < x < \sum_j l_j$ . If  $E[\hat{L}] > x > 0$ , then  $\tau^* > 0$  and if  $E[\hat{L}] < x <$  $\sum_{j} l_{j}$ , then  $\tau^* < 0$ .
- 2. For each  $m \ge 0$ , there is exactly one solution  $\tau_m^$ of equation (26) on  $(-\infty, 0)$ , if  $x < \sum_i l_i$  and no solution on  $(-\infty, 0)$ , if  $x \ge \sum_j l_j$ . Moreover, when  $x < \sum_j l_j$ , the sequence  $\{\tau_m^{\perp}\}_{m \ge 0}$  is monotonically decreasing in m.
- 3. For each  $m \ge 0$ , there is exactly one solution  $\tau_{m}^{+}$  of equation (26) on  $(0,\infty)$ , if  $x>0$  and no solution on  $(0, \infty)$ , if  $x \leq 0$ . Moreover, when  $x > 0$  the sequence  $\{\tau_m^+\}_{m\geq 0}$  is monotonically increasing in m.

At this point, the methods in [2] and [9] differ. We consider first the method in [9] for computing  $F^{(m)}$ ,  $m = 0, 1$ . The argument of Daniels directly is applied, but with the following strategy for choosing the saddlepoint. Whenever  $x < E[L]$ ,  $\tau_m^-$  is chosen as the center of the Taylor expansion for the integral in equation (22). Whenever  $x > E[\hat{L}]$ , instead,  $\tau_{m}^{+}$  is chosen as the center of the Taylor expansion for the integral in equation  $(23)$ , and either of equations  $(24)$  or (25) is used. Thus for example, when  $x > E[L]$ , the approximation for  $m = 1$  is

$$F^{(1)}(x) \sim x - E[L] + \frac{e^{\tau_1^+ x + \Psi(\tau_1^+)}}{\sqrt{2\pi \Psi^{(2)}(\tau_1^+)}}$$
$$\times \left[ 1 + \frac{\Psi^{(4)}(\tau_1^+)}{8(\Psi^{(2)}(\tau_1^+))^2} - \frac{5(\Psi^{(3)}(\tau_1^+))^2}{24(\Psi^{(2)}(\tau_1^+))^3} + \cdots \right] \quad (27)$$

In [2], the  $m = -1$  solution  $\tau^*$ , suggested by large deviation theory, is chosen as the center of the Taylor expansion, even for  $m \neq -1$ . The factor  $\tau^{-m-1}$  is then included with the other nonexponentiated terms, leading to an asymptotic expansion with terms of the form

$$\int_{-\infty}^{\infty} e^{-w^2/2} (w + w_0)^{-m-1} w^k \, \mathrm{d}w w_0 = \tau^* / \sqrt{\Psi^{(2)}(\tau^*)}$$
(28)

These integrals can be evaluated in closed form, but are somewhat complicated, and more terms are needed for a given order of accuracy.

Numerical implementation of the saddlepoint method for portfolio credit problems thus boils down to efficient computation of the appropriate solutions of the saddlepoint condition given by equation (26). This is a relatively straightforward application of onedimensional Newton-Raphson iteration, but must be done for a large number of values of  $(x, t, y)$ . For typical parameter values and up to  $2^{10}$  obligors, [9] report that saddlepoints were usually found in under 10 iterations, which suggests that a saddlepoint expansion will run no more than about 10 times

slower than the Edgeworth expansion with the same number of terms. However, both [2] and [9] observe that the accuracy of the saddlepoint expansion is often far greater.

#### Acknowledgments

Research underlying this article was supported by the Natural Sciences and Engineering Research Council of Canada and MITACS, Canada.

# References

- [1] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, Risk 16, 67-72.
- [2] Antonov, A., Mechkov, S. & Misirpashaev, T. (2005). Analytical Techniques for Synthetic CDOs and Credit Default Risk Measures, Numerix Preprint http://www. defaultrisk.com/pp\_crdry\_77.htm.
- [3] Daniels, H.E. (1954). Saddlepoint approximations in statistics. Annals of Mathematical Statistics 25, 631–650.
- [4] Gordy, M. (2002). Saddlepoint approximation of credit risk, Journal of Banking Finance 26(2), 1335-1353.
- [5] Hull, J. & White, A. (2004). Valuation of a CDO and an  $n$ th to default CDS without Monte Carlo simulation, Journal of Derivatives 2, 8-23.
- [6] Martin, R., Thompson, K. & Browne, C. (2003). Taking to the saddle, in Credit Risk Modelling: The Cutting-edge Collection, M. Gordy, ed, Riskbooks, London.
- [7] Varadhan, S.R.S. (1966). Asymptotic probabilities and differential equations, Communications on Pure and Applied Mathematics 19, 261–286.
- [8] Watson, G.N. (1995). A Treatise on the Theory of Bessel Functions, 2nd Edition, Cambridge University Press, Cambridge, reprint of the second (1944) edition.
- [9] Yang, J.P., Hurd, T.R. & Zhang, X.P. (2006). Saddlepoint approximation method for pricing CDOs, Journal of Computational Finance  $10$ , 1–20.

THOMAS R. HURD
This chapter's two parts develop key ideas from two fields, the intersection of which is the topic of this book. Section 1.1 develops principles underlying the use and analysis of Monte Carlo methods. It begins with a general description and simple examples of Monte Carlo, and then develops a framework for measuring the efficiency of Monte Carlo estimators. Section 1.2 reviews concepts from the theory of derivatives pricing, including pricing by replication, the absence of arbitrage, risk-neutral probabilities, and market completeness. The most important idea for our purposes is the representation of derivative prices as expectations, because this representation underlies the application of Monte Carlo.

# 1.1 Principles of Monte Carlo

# 1.1.1 Introduction

Monte Carlo methods are based on the analogy between probability and volume. The mathematics of measure formalizes the intuitive notion of probability, associating an event with a set of outcomes and defining the probability of the event to be its volume or measure relative to that of a universe of possible outcomes. Monte Carlo uses this identity in reverse, calculating the volume of a set by interpreting the volume as a probability. In the simplest case, this means sampling randomly from a universe of possible outcomes and taking the fraction of random draws that fall in a given set as an estimate of the set's volume. The law of large numbers ensures that this estimate converges to the correct value as the number of draws increases. The central limit theorem provides information about the likely magnitude of the error in the estimate after a finite number of draws.

A small step takes us from volumes to integrals. Consider, for example, the problem of estimating the integral of a function  $f$  over the unit interval. We may represent the integral

1

ounnanons

$$\alpha = \int_0^1 f(x) \, dx$$

as an expectation  $E[f(U)]$ , with U uniformly distributed between 0 and 1. Suppose we have a mechanism for drawing points  $U_1, U_2, \ldots$  independently and uniformly from  $[0,1]$ . Evaluating the function f at n of these random points and averaging the results produces the Monte Carlo estimate

$$\hat{\alpha}_n = \frac{1}{n} \sum_{i=1}^n f(U_i).$$

If f is indeed integrable over  $[0, 1]$  then, by the strong law of large numbers,

 $\hat{\alpha}_n \to \alpha$  with probability 1 as  $n \to \infty$ .

If  $f$  is in fact square integrable and we set

$$\sigma_f^2 = \int_0^1 (f(x) - \alpha)^2 dx,$$

then the error  $\hat{\alpha}_n - \alpha$  in the Monte Carlo estimate is approximately normally distributed with mean 0 and standard deviation  $\sigma_f/\sqrt{n}$ , the quality of this approximation improving with increasing n. The parameter  $\sigma_f$  would typically be unknown in a setting in which  $\alpha$  is unknown, but it can be estimated using the sample standard deviation

$$s_f = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (f(U_i) - \hat{\alpha}_n)^2}.$$

Thus, from the function values  $f(U_1), \ldots, f(U_n)$  we obtain not only an estimate of the integral  $\alpha$  but also a measure of the error in this estimate.

The form of the standard error  $\sigma_f/\sqrt{n}$  is a central feature of the Monte Carlo method. Cutting this error in half requires increasing the number of points by a factor of four; adding one decimal place of precision requires 100 times as many points. These are tangible expressions of the square-root convergence rate implied by the  $\sqrt{n}$  in the denominator of the standard error. n contrast, the error in the simple trapezoidal rule

$$\alpha \approx \frac{f(0) + f(1)}{2n} + \frac{1}{n} \sum_{i=1}^{n-1} f(i/n)$$

 $O(n^{-2})$ , at least for twice continuously differentiable f. Monte Carlo is enerally not a competitive method for calculating one-dimensional integrals.

The value of Monte Carlo as a computational tool lies in the fact that its  $(n^{-1/2})$  convergence rate is not restricted to integrals over the unit interval.

Indeed, the steps outlined above extend to estimating an integral over  $[0,1]^d$ (and even  $\Re^d$ ) for all dimensions d. Of course, when we change dimensions we change f and when we change f we change  $\sigma_f$ , but the standard error will still have the form  $\sigma_f/\sqrt{n}$  for a Monte Carlo estimate based on n draws from the domain  $[0,1]^d$ . In particular, the  $O(n^{-1/2})$  convergence rate holds for all d. In contrast, the error in a product trapezoidal rule in d dimensions is  $O(n^{-2/d})$  for twice continuously differentiable integrands; this degradation in convergence rate with increasing dimension is characteristic of all deterministic integration methods. Thus, Monte Carlo methods are attractive in evaluating integrals in high dimensions.

What does this have to do with financial engineering? A fundamental implication of asset pricing theory is that under certain circumstances (reviewed in Section  $1.2.1$ ), the price of a derivative security can be usefully represented as an expected value. Valuing derivatives thus reduces to computing expectations. In many cases, if we were to write the relevant expectation as an integral, we would find that its dimension is large or even infinite. This is precisely the sort of setting in which Monte Carlo methods become attractive.

Valuing a derivative security by Monte Carlo typically involves simulating paths of stochastic processes used to describe the evolution of underlying asset prices, interest rates, model parameters, and other factors relevant to the security in question. Rather than simply drawing points randomly from  $[0,1]$  or  $[0,1]^d$ , we seek to sample from a space of paths. Depending on how the problem and model are formulated, the dimension of the relevant space may be large or even infinite. The dimension will ordinarily be at least as large as the number of time steps in the simulation, and this could easily be large enough to make the square-root convergence rate for Monte Carlo competitive with alternative methods.

For the most part, there is nothing we can do to overcome the rather slow rate of convergence characteristic of Monte Carlo. (The quasi-Monte Carlo methods discussed in Chapter 5 are an exception — under appropriate conditions they provide a faster convergence rate.) We can, however, look for superior sampling methods that reduce the implicit constant in the convergence rate. Much of this book is devoted to examples and general principles for doing this.

The rest of this section further develops some essential ideas underlying Monte Carlo methods and their application to financial engineering. Section 1.1.2 illustrates the use of Monte Carlo with two simple types of option contracts. Section  $1.1.3$  develops a framework for evaluating the efficiency of simulation estimators.

## 1.1.2 First Examples

In discussing general principles of Monte Carlo, it is useful to have some simple specific examples to which to refer. As a first illustration of a Monte Carlo method, we consider the calculation of the expected present value of the payoff

of a call option on a stock. We do not yet refer to this as the option *price*; the connection between a price and an expected discounted payoff is developed in Section  $1.2.1$ .

Let  $S(t)$  denote the price of the stock at time t. Consider a call option granting the holder the right to buy the stock at a fixed price  $K$  at a fixed time T in the future; the current time is  $t=0$ . If at time T the stock price  $S(T)$  exceeds the strike price K, the holder exercises the option for a profit of  $S(T) - K$ ; if, on the other hand,  $S(T) \leq K$ , the option expires worthless. (This is a *European* option, meaning that it can be exercised only at the fixed date  $T$ ; an *American* option allows the holder to choose the time of exercise.) The payoff to the option holder at time  $T$  is thus

$$(S(T) - K)^{+} = \max\{0, S(T) - K\}.$$

To get the present value of this payoff we multiply by a discount factor  $e^{-rT}$ , with  $r$  a continuously compounded interest rate. We denote the expected present value by  $\mathsf{E}[e^{-rT}(S(T)-K)^{+}].$ 

For this expectation to be meaningful, we need to specify the distribution of the random variable  $S(T)$ , the terminal stock price. In fact, rather than simply specifying the distribution at a fixed time, we introduce a model for the dynamics of the stock price. The Black-Scholes model describes the evolution of the stock price through the stochastic differential equation (SDE)

$$\frac{dS(t)}{S(t)} = r \, dt + \sigma \, dW(t), \tag{1.1}$$

with  $W$  a standard Brownian motion. (For a brief review of stochastic calculus, see Appendix B.) This equation may be interpreted as modeling the percentage changes  $dS/S$  in the stock price as the increments of a Brownian motion. The parameter  $\sigma$  is the volatility of the stock price and the coefficient on dt in  $(1.1)$  is the mean rate of return. In taking the rate of return to be the same as the interest rate  $r$ , we are implicitly describing the risk-neutral dynamics of the stock price, an idea reviewed in Section  $1.2.1$ .

The solution of the stochastic differential equation  $(1.1)$  is

$$S(T) = S(0) \exp\left(\left[r - \frac{1}{2}\sigma^2\right]T + \sigma W(T)\right). \tag{1.2}$$

As  $S(0)$  is the current price of the stock, we may assume it is known. The random variable  $W(T)$  is normally distributed with mean 0 and variance T; this is also the distribution of  $\sqrt{TZ}$  if Z is a standard normal random variable  $(\text{mean } 0, \text{ variance } 1)$ . We may therefore represent the terminal stock price as

$$S(T) = S(0) \exp\left(\left[r - \frac{1}{2}\sigma^2\right]T + \sigma\sqrt{T}Z\right). \tag{1.3}$$

The logarithm of the stock price is thus normally distributed, and the stock price itself has a lognormal distribution.

The expectation  $\mathsf{E}[e^{-rT}(S(T)-K)^{+}]$  is an integral with respect to the lognormal density of  $S(T)$ . This integral can be evaluated in terms of the standard normal cumulative distribution function  $\Phi$  as  $\mathrm{BS}(S(0), \sigma, T, r, K)$ with

$$\begin{split}\n\text{BS}(S,\sigma,T,r,K) &= \\
S\Phi\left(\frac{\log(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right) - e^{-rT}K\Phi\left(\frac{\log(S/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right). \n\end{split} (1.4)$$

This is the Black-Scholes  $[50]$  formula for a call option.

In light of the availability of this formula, there is no need to use Monte Carlo to compute  $\mathsf{E}[e^{-rT}(S(T)-K)^{+}]$ . Moreover, we noted earlier that Monte Carlo is not a competitive method for computing one-dimensional integrals. Nevertheless, we now use this example to illustrate the key steps in Monte Carlo. From (1.3) we see that to draw samples of the terminal stock price  $S(T)$ it suffices to have a mechanism for drawing samples from the standard normal distribution. Methods for doing this are discussed in Section  $2.3$ ; for now we simply assume the ability to produce a sequence  $Z_1, Z_2, \ldots$  of independent standard normal random variables. Given a mechanism for generating the  $Z_i$ , we can estimate  $\mathsf{E}[e^{-rT}(S(T)-K)^{+}]$  using the following algorithm:

for 
$$i = 1, ..., n$$
  
generate  $Z_i$   
set  $S_i(T) = S(0) \exp\left( [r - \frac{1}{2}\sigma^2]T + \sigma\sqrt{T}Z_i \right)$   
set  $C_i = e^{-rT}(S(T) - K)^+$   
set  $\hat{C}_n = (C_1 + \dots + C_n)/n$ 

For any  $n \geq 1$ , the estimator  $\hat{C}_n$  is *unbiased*, in the sense that its expectation is the target quantity:

$$\mathsf{E}[\hat{C}_n] = C \equiv \mathsf{E}[e^{-rT}(S(T) - K)^+].$$

The estimator is *strongly consistent*, meaning that as  $n \to \infty$ ,

$$\hat{C}_n \to C$$
 with probability 1.

For finite but at least moderately large  $n$ , we can supplement the point estimate  $\hat{C}_n$  with a confidence interval. Let

$$s_C = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (C_i - \hat{C}_n)^2}$$
(1.5)

denote the sample standard deviation of  $C_1, \ldots, C_n$  and let  $z_{\delta}$  denote the  $1-\delta$ quantile of the standard normal distribution (i.e.,  $\Phi(z_{\delta}) = 1 - \delta$ ). Then

$$\hat{C}_n \pm z_{\delta/2} \frac{s_C}{\sqrt{n}} \tag{1.6}$$

is an asymptotically (as  $n \to \infty$ ) valid  $1 - \delta$  confidence interval for C. (For a 95% confidence interval,  $\delta = .05$  and  $z_{\delta/2} \approx 1.96$ .) Alternatively, because the standard deviation is estimated rather than known, we may prefer to replace  $z_{\delta/2}$  with the corresponding quantile from the t distribution with  $n-1$ degrees of freedom, which results in a slightly wider interval. In either case, the probability that the interval covers C approaches  $1 - \delta$  as  $n \to \infty$ . (These ideas are reviewed in Appendix  $A$ .)

The problem of estimating  $E[e^{-rT}(S(T)-K)^+]$  by Monte Carlo is simple enough to be illustrated in a spreadsheet. Commercial spreadsheet software typically includes a method for sampling from the normal distribution and the mathematical functions needed to transform normal samples to terminal stock prices and then to discounted option payoffs. Figure 1.1 gives a schematic illustration. The  $Z_i$  are samples from the normal distribution; the comments in the spreadsheet illustrate the formulas used to transform these to arrive at the estimate  $\hat{C}_n$ . The spreadsheet layout in Figure 1.1 makes the method transparent but has the drawback that it requires storing all  $n$  replication in  $n$  rows of cells. It is usually possible to use additional spreadsheet commands to recalculate cell values  $n$  times without storing intermediate values.

|    |                |             | Replication Normals Stock Price Option Payoff         |                                    |  |  |  |
|----|----------------|-------------|-------------------------------------------------------|------------------------------------|--|--|--|
|    | Ζ1             | S_1         | C 1                                                   |                                    |  |  |  |
| 2  | Z 2            | S_2         | C 2                                                   |                                    |  |  |  |
| 3  | Ζ3             | $S_3$       | С 3                                                   |                                    |  |  |  |
| 4  | Z_4            | S 4         |                                                       |                                    |  |  |  |
| 5  | Z 5            | S 5         | $S_1=S(0)*exp((r-0.5*\sigma^2)*T+\sigma*sqrt(T)*Z_1)$ |                                    |  |  |  |
| 6  | Z 6            | S_6         | C 6                                                   |                                    |  |  |  |
| 7  | Ζ7             | S_7         | C 7                                                   |                                    |  |  |  |
| 8  | Z_8            | S 8         | C 8                                                   | $C_8 = \exp(-rT) \max(0, S_8 - K)$ |  |  |  |
| 9  | Ζ9             | S 9         | C 9                                                   |                                    |  |  |  |
| 10 | Z 10           | S 10        | C 10                                                  |                                    |  |  |  |
| 11 | Z 11           | S 11        | C 11                                                  |                                    |  |  |  |
|    | $\ddot{\cdot}$ | ÷<br>$\sim$ |                                                       |                                    |  |  |  |
| n  | Z_n            | $S_n$       | C n                                                   |                                    |  |  |  |
|    |                |             | $\hat{C}_{n}$ = AVERAGE(C_1,,C_n)                     |                                    |  |  |  |
|    |                |             | $C = STDEV(C_1,,C_n)$                                 |                                    |  |  |  |

Fig. 1.1. A spreadsheet for estimating the expected present value of the payoff of a call option.

This simple example illustrates a general feature of Monte Carlo methods for valuing derivatives, which is that the simulation is built up in layers: each of the transformations

$$Z_i \longrightarrow S_i(T) \longrightarrow C_i$$

exemplifies a typical layer. The first transformation constructs a path of underlying assets from random variables with simpler distributions and the second calculates a discounted payoff from each path. In fact, we often have additional

layers above and below these. At the lowest level, we typically start from independent random variables  $U_i$  uniformly distributed between 0 and 1, so we need a transformation taking the  $U_i$  to  $Z_i$ . The transformation taking the  $C_i$ to the sample mean  $\hat{C}_n$  and sample standard deviation  $s_C$  may be viewed as another layer. We include another still higher level in, for example, valuing a portfolio of instruments, each of which is valued by Monte Carlo. Randomness (or apparent randomness) typically enters only at the lowest layer; the subsequent transformations producing asset paths, payoffs, and estimators are usually deterministic.

### Path-Dependent Example

 $\mathcal{L}$ 

The payoff of a standard European call option is determined by the terminal stock price  $S(T)$  and does not otherwise depend on the evolution of  $S(t)$ between times 0 and T. In estimating  $E[e^{-rT}(S(T)-K)^{+}]$ , we were able to jump directly from time 0 to time T using (1.3) to sample values of  $S(T)$ . Each simulated "path" of the underlying asset thus consists of just the two points  $S(0)$  and  $S(T)$ .

In valuing more complicated derivative securities using more complicated models of the dynamics of the underlying assets, it is often necessary to simulate paths over multiple intermediate dates and not just at the initial and terminal dates. Two considerations may make this necessary:

- the payoff of a derivative security may depend explicitly on the values of Ο underlying assets at multiple dates;
- we may not know how to sample transitions of the underlying assets exactly and thus need to divide a time interval  $[0,T]$  into smaller subintervals to obtain a more accurate approximation to sampling from the distribution at time  $T$ .

In many cases, both considerations apply.

Before turning to a detailed example of the first case, we briefly illustrate the second. Consider a generalization of the basic model  $(1.1)$  in which the dynamics of the underlying asset  $S(t)$  are given by

$$dS(t) = rS(t) dt + \sigma(S(t))S(t) dW(t). \qquad (1.7)$$

In other words, we now let the volatility  $\sigma$  depend on the current level of S. Except in very special cases, this equation does not admit an explicit solution of the type in  $(1.2)$  and we do not have an exact mechanism for sampling from the distribution of  $S(T)$ . In this setting, we might instead partition [0, T] into m subintervals of length  $\Delta t = T/m$  and over each subinterval  $[t, t + \Delta t]$ simulate a transition using a discrete (Euler) approximation to  $(1.7)$  of the  $\text{form}$ 

$$S(t + \Delta t) = S(t) + rS(t)\Delta t + \sigma(S(t))S(t)\sqrt{\Delta t}Z,$$

with Z a standard normal random variable. This relies on the fact that  $W(t +$  $\Delta t - W(t)$  has mean 0 and standard deviation  $\sqrt{\Delta t}$ . For each step, we would use an independent draw from the normal distribution. Repeating this for m steps produces a value of  $S(T)$  whose distribution approximates the exact (unknown) distribution of  $S(T)$  implied by (1.7). We expect that as m becomes larger (so that  $\Delta t$  becomes smaller) the approximating distribution of  $S(T)$ draws closer to the exact distribution. In this example, intermediate times are introduced into the simulation to reduce *discretization error*, the topic of Chapter  $6.$ 

Even if we assume the dynamics in  $(1.1)$  of the Black-Scholes model, it may be necessary to simulate paths of the underlying asset if the payoff of a derivative security depends on the value of the underlying asset at intermediate dates and not just the terminal value. Asian options are arguably the simplest path-dependent options for which Monte Carlo is a competitive computational tool. These are options with payoffs that depend on the average level of the underlying asset. This includes, for example, the payoff  $(\bar{S}-K)^+$ with

$$\bar{S} = \frac{1}{m} \sum_{j=1}^{m} S(t_j) \tag{1.8}$$

for some fixed set of dates  $0 = t_0 < t_1 < \cdots < t_m = T$ , with T the date at which the payoff is received.

To calculate the expected discounted payoff  $\mathsf{E}[e^{-rT}(\bar{S}-K)^{+}]$ , we need to be able to generate samples of the average  $\bar{S}$ . The simplest way to do this is to simulate the path  $S(t_1), \ldots, S(t_m)$  and then compute the average along the path. We saw in (1.3) how to simulate  $S(T)$  given  $S(0)$ ; simulating  $S(t_{j+1})$ from  $S(t_i)$  works the same way:

$$S(t_{j+1}) = S(t_j) \exp\left( [r - \frac{1}{2}\sigma^2](t_{j+1} - t_j) + \sigma\sqrt{t_{j+1} - t_j}Z_{j+1} \right) \tag{1.9}$$

where  $Z_1, \ldots, Z_m$  are independent standard normal random variables. Given a path of values, it is a simple matter to calculate  $\bar{S}$  and then the discounted payoff  $e^{-rT}(\bar{S}-K)^+$ .

The following algorithm illustrates the steps in simulating  $n$  paths of  $m$ transitions each. To be explicit, we use  $Z_{ij}$  to denote the jth draw from the normal distribution along the *i*th path. The  $\{Z_{ij}\}$  are mutually independent.

for 
$$i = 1, ..., n$$
  
for  $j = 1, ..., m$   
generate  $Z_{ij}$   
set  $S_i(t_j) = S_i(t_{j-1}) \exp\left( [r - \frac{1}{2}\sigma^2](t_j - t_{j-1}) + \sigma\sqrt{(t_j - t_{j-1})} Z_{ij} \right)$   
set  $\bar{S} = (S_i(t_1) + \dots + S_i(t_m))/m$   
set  $C_i = e^{-rT} (\bar{S} - K)^+$   
set  $\hat{C}_n = (C_1 + \dots + C_n)/n$ 

Figure 1.2 gives a schematic illustration of a spreadsheet implementation of this method. The spreadsheet has  $n$  rows of standard normal random variables  $Z_{ij}$  with m variables in each row. These are mapped to n paths of the underlying asset, each path consisting of  $m$  steps. From each path, the spreadsheet calculates a value of the time average  $\bar{S}_i$  and a value of the discounted payoff  $C_i$ . The  $C_i$  are averaged to produce the final estimate  $\hat{C}_n$ .

![](_page_8_Figure_2.jpeg)

Fig. 1.2. A spreadsheet for estimating the expected present value of the payoff of an Asian call option.

 $\langle \langle \nabla \hat{V} \rangle \rangle$ 

# 1.1.3 Efficiency of Simulation Estimators

Much of this book is devoted to ways of improving Monte Carlo estimators. To discuss improvements, we first need to explain our criteria for comparing alternative estimators. Three considerations are particularly important: computing time, bias, and variance.

We begin by considering unbiased estimates. The two cases considered in Section  $1.1.2$  (the standard call and the Asian call) produced unbiased estimates in the sense that in both cases  $\mathsf{E}[\hat{C}_n] = C$ , with  $\hat{C}_n$  the corresponding estimator and  $C$  the quantity being estimated. Also, in both cases the estimator  $\hat{C}_n$  was the mean of *n* independent and identically distributed samples. We proceed by continuing to consider estimators of this form because this setting is both simple and practically relevant.

Suppose, then, that

$$\hat{C}_n = \frac{1}{n} \sum_{i=1}^n C_i,$$

with  $C_i$  i.i.d.,  $\mathsf{E}[C_i] = C$  and  $\mathsf{Var}[C_i] = \sigma_C^2 < \infty$ . The central limit theorem asserts that as the number of replications  $n$  increases, the standardized estimator  $(C_n - C)/(\sigma_C/\sqrt{n})$  converges in distribution to the standard normal, a statement often abbreviated as

$$\frac{\hat{C}_n - C}{\sigma_C / \sqrt{n}} \Rightarrow N(0, 1)$$
$$\sqrt{n} [\hat{C}_n - C] \Rightarrow N(0, \sigma_C^2). \tag{1.10}$$

or, equivalently, as

Here, 
$$\Rightarrow$$
 denotes convergence in distribution and  $N(a, b^2)$  denotes the normal distribution with mean  $a$  and variance  $b^2$ . The stated convergence in distribution means that

$$\lim_{n \to \infty} P\left(\frac{\hat{C}_n - C}{\sigma_C/\sqrt{n}} \le x\right) = \Phi(x)$$

for all x, with  $\Phi$  the cumulative normal distribution. The same limit holds if  $\sigma_C$  is replaced with the sample standard devation  $s_C$  (as in (1.5)); this is important because  $\sigma_C$  is rarely known in practice but  $s_C$  is easily calculated from the simulation output. The fact that we can replace  $\sigma_C$  with  $s_C$  without changing the limit in distribution follows from the fact that  $s_C/\sigma_C \rightarrow 1$  as  $n \to \infty$  and general results on convergence in distribution (cf. Appendix A).

The central limit theorem justifies the confidence interval (1.6): as  $n \rightarrow$  $\infty$ , the probability that this interval straddles the true value C approaches  $1-\delta$ . Put differently, the central limit theorem tells us something about the distribution of the error in our simulation estimate:

$$\hat{C}_n - C \approx N(0, \sigma_C^2/n),$$

meaning that the error on the left has approximately the distribution on the right. This makes precise the intuitively obvious notion that, other things being equal, in comparing two estimators of the same quantity we should prefer the one with lower variance.

But what if other things are not equal? In particular, suppose we have a choice between two unbiased estimators and that the one with smaller variance takes longer to compute. How should we balance variance reduction and computational effort? An informal answer was suggested by Hammersley and Handscomb [169]; Fox and Glynn [128] and Glynn and Whitt [160] develop a general framework for analyzing this issue and we now review some of its main conclusions.

Suppose that generating a replication  $C_i$  takes a fixed amount of computing time  $\tau$ . Our objective is to compare estimators based on relative computational effort, so the units in which we measure computing time are unimportant. Let  $s$  denote our computational budget, measured in the same units as  $\tau$ . Then the number of replications we can complete given the available budget is  $\lfloor s/\tau \rfloor$ , the integer part of  $s/\tau$ , and the resulting estimator is  $C_{\lfloor s/\tau \rfloor}$ . Directly from  $(1.10)$ , we get

$$\sqrt{\lfloor s/\tau \rfloor} [\hat{C}_{\lfloor s/\tau \rfloor} - C] \Rightarrow N(0, \sigma_C^2)$$

as the computational budget s increases to infinity. Noting that  $|s/\tau|/s \rightarrow$  $1/\tau$ , it follows that  $\sqrt{s}[\hat{C}_{\lfloor s/\tau \rfloor} - C]$  is also asymptotically normal but with an asymptotic variance of  $\sigma_C^2 \tau$ ; i.e.,

$$\sqrt{s}[\hat{C}_{\lfloor s/\tau \rfloor} - C] \Rightarrow N(0, \sigma_C^2 \tau) \tag{1.11}$$

as  $s \to \infty$ . This limit normalizes the error in the estimator by the computing time  $s$  rather than by the number of replications. It tells us that, given a budget  $s$ , the error in our estimator will be approximately normally distributed with variance  $\sigma_C^2 \tau / s$ .

This property provides a criterion for comparing alternative unbiased estimators. Suppose, for example, that we have two unbiased estimators both of which are averages of independent replications, as above. Suppose the variance per replication  $\sigma_1^2$  of the first estimator is larger than the variance per replication  $\sigma_2^2$  of the second estimator, but the computing times per replication  $\tau_i$ ,  $i = 1, 2$ , of the two estimators satisfy  $\tau_1 < \tau_2$ . How should we choose between the faster, more variable estimator and the slower, was variable estimator? The formulation of the central limit theorem in  $(1.11)$  suggests that asymptotically (as the computational budget grows), we should prefer the estimator with the smaller value of  $\sigma_i^2 \tau_i$ , because this is the one that will produce the more precise estimate (and narrower confidence interval) from the budget  $s$ .

A feature of the product  $\sigma^2 \tau$  (variance per replication times computer time per replication) as a measure of efficiency is that it is insensitive to bundling multiple replications into a single replication. Suppose, for example, that we simply redefine a replication to be the average of two independent copies of the original replications. This cuts the variance per replication in half but doubles the computing time per replication and thus leaves the product of the two unaltered. A purely semantic change in what we call a replication does not affect our measure of efficiency.

The argument leading to the work-normalized central limit theorem  $(1.11)$ requires that the computing time per replication be constant. This would be almost exactly the case in, for example, the simulation of the Asian option considered in Section  $1.1.2$ : all replications require simulating the same number of transitions, and the time per transition is nearly constant. This feature is characteristic of many derivative pricing problems in which the time per replication is determined primarily by the number of time steps simulated. But there are also cases in which computing time can vary substantially across replications. In pricing a *barrier* option, for example (cf. Section  $3.2.2$ ), one might terminate a path the first time a barrier is crossed; the number of transitions until this happens is typically random. Sampling through acceptancerejection (as discussed in Section  $2.2.2$ ) also introduces randomness in the time per replication.

To generalize  $(1.11)$  to these cases, we replace the assumption of a fixed computing time with the condition that  $(C_1, \tau_1), (C_2, \tau_2), \ldots$  are independent and identically distributed, with  $C_i$  as before and  $\tau_i$  now denoting the computer time required for the  $i$ th replication. The number of replications that

can be completed with a computing budget  $s$  is

$$N(s) = \sup \left\{ n \ge 0 : \sum_{i=1}^{n} \tau_i \le s \right\}$$

and is also random. Our estimator based on a budget s is  $\hat{C}_{N(s)}$ , the average of the first  $N(s)$  replications. Our assumption of i.i.d. replications ensures that  $N(s)/s \to 1/\mathsf{E}[\tau]$  with probability one (this is the elementary renewal theorem) and then that  $(1.11)$  generalizes to (cf. Appendix A.1)

$$\sqrt{s}[\hat{C}_{N(s)} - C] \Rightarrow N(0, \sigma_C^2 \mathsf{E}[\tau]). \tag{1.12}$$

This limit provides a measure of asymptotic relative efficiency when the computing time per replication is variable. It indicates that in comparing alternative estimators, each of which is the average of unbiased independent replications, we should prefer the one for which the product

(variance per replication)  $\times$  (expected computing time per replication)

is smallest. This principle (an early version of which may be found in Hammersley and Handscomb  $[169]$ , p.51) is a special case of a more general formulation developed by Glynn and Whitt [160] for comparing the efficiency of simulation estimators. Their results include a limit of the form in  $(1.12)$  that holds in far greater generality than the case of i.i.d. replications we consider here.

### $\text{Bias}$

The efficiency comparisons above, based on the central limit theorems in  $(1.10)$ and  $(1.12)$ , rely on the fact that the estimators to be compared are averages of unbiased replications. In the absence of bias, estimator variability and computational effort are the most important considerations. However, reducing variability or computing time would be pointless if it merely accelerated convergence to an incorrect value. While accepting bias in small samples is sometimes necessary, we are interested only in estimators for which any bias can be eliminated through increasing computational effort.

Some simulation estimators are biased for all finite sample sizes but become asymptotically unbiased as the number of replications increases. This is true of  $\hat{C}_{N(s)}$ , for example. When the  $\tau_i$  are random,  $\mathsf{E}[\hat{C}_{N(s)}] \neq C$ , but the central limit theorem  $(1.12)$  shows that the bias in this case becomes negligible as s increases. Glynn and Heidelberger [155] show that it can be entirely eliminated by forcing completion of at least the first replication, because  $\mathsf{E}[C_{\max\{1,N(s)\}}] = C.$ 

Another example is provided by the problem of estimating a ratio of expections  $E[X]/E[Y]$  from i.i.d. replications  $(X_i, Y_i), i = 1, \ldots, n$ , of the pair  $(X,Y)$ . The ratio of sample means  $\bar{X}/\bar{Y}$  is biased for all n because

$$\mathsf{E}\left[\frac{\bar{X}}{\bar{Y}}\right] \neq \frac{\mathsf{E}[\bar{X}]}{\mathsf{E}[\bar{Y}]};$$

but  $\bar{X}/\bar{Y}$  clearly converges to  $\mathsf{E}[X]/\mathsf{E}[Y]$  with probability 1 as  $n \to \infty$ . Moreover, the normalized error

$$\sqrt{n}\left(\frac{\bar{X}}{\bar{Y}} - \frac{\mathsf{E}[X]}{\mathsf{E}[Y]}\right)$$

is asymptotically normal, a point we return to in Section  $4.3.3$ . Thus, the bias becomes negligible as the number of replications increases, and the convergence rate of the estimator is unaffected.

But not all types of bias vanish automatically in large samples — some require special effort. Three examples should help illustrate typical sources of non-negligible bias in financial engineering simulations. In each of these examples the bias persists as the number of replications increases, but the bias is nevertheless manageable in the sense that it can be made as small as necessary through additional computational effort.

**Example 1.1.1** Model discretization error. In Section 1.1.2 we illustrated the use of Monte Carlo in estimating the expected present value of the payoff of a standard call option and an Asian call option under Black-Scholes assumptions on the dynamics of the underlying stock. We obtained unbiased estimates by simulating the underlying stock using  $(1.3)$  and  $(1.9)$ . Suppose that instead of using  $(1.9)$  we divide the time horizon into small increments of length h and approximate changes in the underlying stock using the recursion

$$S((j+1)h) = S(jh) + rS(jh)h + \sigma S(jh)\sqrt{hZ_{j+1}}$$

with  $Z_1, Z_2, \ldots$  independent standard normal random variables. The joint distribution of the values of the stock price along a path simulated using this rule will not be exactly the same as that implied by the Black-Scholes dynamics in  $(1.1)$ . As a consequence, the expected present value of an option payoff estimated using this simulation rule will differ from the exact value the simulation estimator is biased. This is an example of *discretization* bias because it results from time-discretization of the continuous-time dynamics of the underlying model.

Of course, in this example, the bias can be eliminated by using the exact method  $(1.9)$  to simulate values of the underlying stock at the relevant dates. But for many models, exact sampling of the continuous-time dynamics is infeasible and discretization error is inevitable. This is typically the case if, for example, the volatility parameter  $\sigma$  is a function of the stock price S, as in  $(1.7)$ . The resulting bias can be managed because it typically vanishes as the time step h decreases. However, taking h smaller entails generating more transitions per path (assuming a fixed time horizon) and thus a higher computational burden.  $\Box$ 

**Example 1.1.2** Payoff discretization error. Suppose that in the definition of the Asian option in Section 1.1.2, we replace the discrete average in  $(1.8)$  with a continuous average

$$\bar{S} = \frac{1}{T} \int_0^T S(u) \, du.$$

In this case, even if we use (1.9) to generate values of  $S(t_i)$  at a discrete set of dates  $t_i$ , we cannot calculate  $\bar{S}$  exactly — we need to use a discrete approximation to the continuous average. A similar issue arises in estimating, e.g.,

$$\mathsf{E}[e^{-rT}(\max_{0\leq t\leq T}S(t)-S(T))],$$

the expected present value of the payoff of a *lookback* option. Even if we simulate a path  $S(0), S(t_1), \ldots, S(t_m)$  exactly (i.e., using (1.9)), the estimator

$$e^{-rT}(\max_{0\leq j\leq m}S(t_j)-S(T))$$

is biased; in particular, the maximum over the  $S(t_i)$  can never exceed and will almost surely underestimate the maximum of  $S(t)$  over all t between 0 and T. In both cases, the bias can be made arbitrarily small by using a sufficiently small simulation time step, at the expense of increasing the computational cost per path. Notice that this example differs from Example 1.1.1 in that the source of discretization error is the form of the option payoff rather than the underlying model; the  $S(t_i)$  themselves are sampled without discretization error. This type of bias is less common in practice than the model discretization error in Example 1.1.1 because option contracts are often sensitive to the value of the underlying asset at only a finite set of dates.  $\Box$ 

**Example 1.1.3** Nonlinear functions of means. Consider an option expiring at  $T_1$  to buy a call option expiring at  $T_2 > T_1$ ; this is an option on an option, sometimes called a *compound* option. Let  $C^{(2)}(x)$  denote the expected discounted payoff of the option expiring at  $T_2$  conditional on the underlying stock price equaling x at time  $T_1$ . More explicitly,

$$C^{(2)}(x) = \mathsf{E}[e^{-r(T_2 - T_1)}(S(T_2) - K_2)^{+}|S(T_1) = x]$$

with  $K_2$  the strike price. If the compound option has a strike of  $K_1$ , then the expected present value of its payoff is

$$C^{(1)} = \mathsf{E}[e^{-rT_1}(C^{(2)}(S(T_1)) - K_1)^+].$$

If the dynamics of the underlying stock are described by the Black-Scholes model (1.1),  $C^{(2)}$  and  $C^{(1)}$  can be evaluated explicitly. But consider the problem of estimating  $C^{(1)}$  by simulation. To do this, we simulate n values  $S_1(T_1), \ldots, S_n(T_1)$  of the stock at  $T_1$  and then k values  $S_{i1}(T_2), \ldots, S_{ik}(T_2)$ of the stock at  $T_2$  from each  $S_i(T_1)$ , as illustrated in Figure 1.3. We estimate the inner option value at  $S_i(T_1)$  using

$$\hat{C}_k^{(2)}(S_i(T_1)) = \frac{1}{k} \sum_{j=1}^k e^{-r(T_2 - T_1)} (S_{ij}(T_2) - K_2)^+$$

and then estimate  $C^{(1)}$  using

$$\hat{C}_n^{(1)} = \frac{1}{n} \sum_{i=1}^n e^{-rT_1} (\hat{C}_k^{(2)}(S_i(T_1)) - K_1)^+$$

![](_page_14_Figure_4.jpeg)

Fig. 1.3. Nested simulation used to estimate a function of a conditional expectation.

If we replaced the inner estimate  $\hat{C}_k^{(2)}$  with its expectation, the result would be an unbiased estimator of  $C^{(1)}$ . But because we estimate the inner expectation, the overall estimator is biased high:

$$\begin{split} \mathsf{E}[\hat{C}_n^{(1)}] &= \mathsf{E}[e^{-rT_1}(\hat{C}_k^{(2)}(S_i(T_1)) - K_1)^+] \\ &= \mathsf{E}[\mathsf{E}[e^{-rT_1}(\hat{C}_k^{(2)}(S_i(T_1)) - K_1)^+ | S_i(T_1) ]] \\ &\ge \mathsf{E}[e^{-rT_1}(\mathsf{E}[\hat{C}_k^{(2)}(S_i(T_1)) | S_i(T_1)] - K_1)^+ ] \\ &= \mathsf{E}[e^{-rT_1}(C^{(2)}(S_i(T_1)) - K_1)^+ ] \\ &= C^{(1)} . \end{split}$$

This follows from Jensen's inequality and the convexity of the function  $y \mapsto$  $(y-K_1)^+$ . As the number k of samples of  $S(T_2)$  generated per sample of  $S(T_1)$  increases, the bias vanishes because  $\hat{C}_k^{(2)}(S_i(T_1)) \to C^{(2)}(S_i(T_1))$  with probability one. The bias can therefore be managed, but once again only at the expense of increasing the computational cost per replication.

The source of bias in this example is the application of a nonlinear function (in this case, the option payoff) to an estimate of an expectation. Closely related biases arise in at least two important applications of Monte Carlo in financial engineering. In measuring portfolio risk over a fixed horizon, the value of the portfolio at the end of the horizon is a conditional expectation. In valuing American options by simulation, the option payoff at each exercise date must be compared with the conditionally expected discounted payoff from waiting to exercise. These topics are discussed in Chapters 8 and 9.  $\Box$ 

Examples  $1.1-1.1.3$  share some important features. In each case, the relevant estimator is an average of independent replications; each replication is biased but the bias can be made arbitrarily small at the expense of increasing the computational cost per replication. Given a fixed computing budget, we therefore face a tradeoff in allocating the budget. Expending more effort per replication lowers bias, but it also decreases the number of replications that can be completed and thus tends to increase estimator variance.

We need a measure of estimator performance that balances bias and variance. A standard measure is mean square error, which equals the sum of bias squared and variance. More explicitly, if  $\hat{\alpha}$  is an estimator of a quantity  $\alpha$ , then

$$\begin{aligned} \text{MSE}(\hat{\alpha}) &= \mathsf{E}[(\hat{\alpha} - \alpha)^2] \\ &= (\mathsf{E}[\hat{\alpha}] - \alpha)^2 + \mathsf{E}[(\hat{\alpha} - \mathsf{E}[\hat{\alpha}])^2] \\ &= \text{Bias}^2(\hat{\alpha}) + \text{Variance}(\hat{\alpha}) \end{aligned}$$

While exact calculation of mean square error is generally impractical, it is often possible to compare estimators through their asymptotic MSE.

For simplicity, we restrict attention to estimators that are sample means of i.i.d. replications. Extending the notation used in the unbiased case, we write  $\hat{C}(n,\delta)$  for the average of n independent replications with parameter  $\delta$ . This parameter determines the bias: we assume  $\mathsf{E}[C(n,\delta)] = \alpha_{\delta}$  and  $\alpha_{\delta} \to \alpha$ as  $\delta \to 0$ , with  $\alpha$  the quantity to be estimated. In Examples 1.1.1 and 1.1.2,  $\delta$  could be the simulation time increment along each path; in Example 1.1.3 we could take  $\delta = 1/k$ . We investigate the mean square error of  $C(n, \delta)$  as the computational budget grows.

Under reasonable additional conditions (in particular, uniform integrability), the central limit theorem in  $(1.12)$  for the asymptotically unbiased estimator  $\hat{C}_{N(s)}$  implies

$$s\mathsf{Var}[\hat{C}_{N(s)}] \to \sigma_C^2 \mathsf{E}[\tau];$$

equivalently,

$$s^{1/2}\sqrt{\text{Var}[\hat{C}_{N(s)}]} \to \sigma_C\sqrt{\mathsf{E}[\tau]}.$$
 (1.13)

The power of  $s$  on the left tells us the rate at which the standard error of  $C_{N(s)}$  (the square root of its variance) decreases, and the limit on the right tells us the constant associated with this asymptotic rate. We proceed to derive similar information in the biased case, where the asymptotic rate of decrease of the mean square error depends, in part, on how computational effort is allocated to reducing bias and variance.

For this analysis, we need to make some assumptions about the estimator. Let  $\tau_{\delta}$  be the computer time per replication at parameter  $\delta$ , which we assume to be nonrandom. For the estimator bias and computing time, we assume there are constants  $\eta, \beta > 0$ , b, and  $c > 0$  such that, as  $\delta \to 0$ ,

1.1 Principles of Monte Carlo 17

$$\alpha_{\delta} - \alpha = b\delta^{\beta} + o(\delta^{\beta}) \tag{1.14}$$

$$\tau_{\delta} = c\delta^{-\eta} + o(\delta^{-\eta}). \tag{1.15}$$

For Examples  $1.1.1-1.1.3$ , it is reasonable to expect that  $(1.15)$  holds with  $n = 1$  because in all three examples the work per path is roughly linear in  $1/\delta$ . The value of  $\beta$  can vary more from one problem to another, but typical values are  $1/2$ , 1, and 2. We will see in Chapter 6 that the value of  $\beta$  often depends on how one chooses to approximate a continuous-time process.

Given a computational budget  $s$ , we can specify an allocation of this budget to reducing bias and variance by specifying a rule  $s \mapsto \delta(s)$  for selecting the parameter  $\delta$ . The resulting number of replications is  $N(s) = \lfloor s/\tau_{\delta(s)} \rfloor$  and the resulting estimator is  $\hat{C}(s) \equiv \hat{C}(N(s), \delta(s))$ ; notice that the estimator is now indexed by the single parameter  $s$  whereas it was originally indexed by both the number of replications n and the bias parameter  $\delta$ . We consider allocation rules  $\delta(s)$  for which

$$\delta(s) = as^{-\gamma} + o(s^{-\gamma}) \tag{1.16}$$

for some constants  $a, \gamma > 0$ . A larger  $\gamma$  corresponds to a smaller  $\delta(s)$  and thus greater effort allocated to reducing bias; through (1.15), smaller  $\delta$  also implies greater computing time per replication, hence fewer replications and less effort allocated to reducing variance. Our goal is to relate the choice of  $\gamma$ to the rate at which the MSE of  $\hat{C}(s)$  decreases as s increases.

For large s, we have  $N(s) \approx s/\tau_{\delta(s)}$ ; (1.15) and (1.16) together imply that  $\tau_{\delta(s)}$  is  $O(s^{\gamma\eta})$  and hence that  $N(s)$  is  $O(s^{1-\gamma\eta})$ . A minimal requirement on the allocation rule  $\delta(s)$  is that the number of replications  $N(s)$  increase with s. We therefore restrict  $\gamma$  to be less than  $1/\eta$  so that  $1-\gamma\eta>0$ .

As a step in our analysis of the MSE, we write the squared bias as

$$(\alpha_{\delta(s)} - \alpha)^2 = b^2 \delta(s)^{2\beta} + o(\delta(s)^{2\beta})$$
  
$$= b^2 a^{2\beta} s^{-2\beta\gamma} + o(s^{-2\beta\gamma}) \tag{1.17}$$

$$= O(s^{-2\beta\gamma}) \tag{1.18}$$

using  $(1.14)$  and  $(1.16)$ .

Next we consider variance. Let  $\sigma_{\delta}^2$  denote the variance per replication at parameter  $\delta$ . Then

$$\mathsf{Var}[\hat{C}(s)] = \frac{\sigma_{\delta(s)}^2}{\lfloor s/\tau_{\delta(s)} \rfloor}$$

We assume that  $\sigma_{\delta}^2$  approaches a finite limit  $\sigma^2 > 0$  as  $\delta \to 0$ . This is a natural assumption in the examples of this section: in Examples 1.1.1 and 1.1.2,  $\sigma^2$  is the variance in the continuous-time limit; in Example 1.1.3, it is the variance that remains from the first simulation step after the variance in the second step is eliminated by letting  $k \to \infty$ . Under this assumption we have

$$\mathsf{Var}[\hat{C}(s)] = \frac{\sigma^2 \tau_{\delta(s)}}{s} + o(\tau_{\delta}(s)/s).$$

Combining this expression for the variance with  $(1.15)$  and  $(1.16)$ , we get

$$\operatorname{Var}[\hat{C}(s)] = \frac{\sigma^2 c \delta(s)^{-\eta}}{s} + o(\delta(s)^{-\eta}/s)$$
$$= \sigma^2 c a^{-\eta} s^{\gamma \eta - 1} + o(s^{\gamma \eta - 1}) \tag{1.19}$$

$$= O(s^{\gamma \eta - 1}). \tag{1.20}$$

The order of magnitude of the MSE is the sum of  $(1.18)$  and  $(1.20)$ .

Consider the effect of different choices of  $\gamma$ . If  $2\beta\gamma > 1 - \gamma\eta$  then the allocation rule drives the squared bias  $(1.18)$  to zero faster than the variance  $(1.20)$ , so the MSE is eventually dominated by the variance. Conversely, if  $2\beta\gamma < 1 - \gamma\eta$  then for large s the MSE is dominated by the squared bias. An optimal allocation rule selects  $\gamma$  to balance the two terms. Setting  $2\beta\gamma = 1-\gamma\eta$ means taking  $\gamma = 1/(2\beta + \eta)$ . Substituting this back into (1.17) and (1.19) results in

$$\text{MSE}(\hat{C}(s)) = (b^2 a^{2\beta} + \sigma^2 c a^{-\eta}) s^{-2\beta/(2\beta+\eta)} + o(s^{-2\beta/(2\beta+\eta)}) \tag{1.21}$$

and thus for the  $root$  mean square error we have

$$\text{RMSE}(\hat{C}(s)) \equiv \sqrt{\text{MSE}(\hat{C}(s))} = O(s^{-\beta/(2\beta + \eta)}). \tag{1.22}$$

The exponent of  $s$  in this approximation gives the convergence rate of the RMSE and should be contrasted with the convergence rate of  $s^{-1/2}$  in (1.13). By minimizing the coefficient in  $(1.21)$  we can also find the optimal parameter  $a$  in the allocation rule  $(1.16)$ ,

$$a_* = \left(\frac{\eta \sigma^2 c}{2\beta b^2}\right)^{\frac{1}{2\beta + \eta}};$$

but this is of less immediate practical value than the convergence rate in  $(1.22).$ 

A large  $\beta$  corresponds to a rapidly vanishing bias; as  $\beta \rightarrow \infty$  we have  $\beta/(2\beta + \eta) \rightarrow 1/2$ , recovering the convergence rate of the standard error in the unbiased case. Similarly, when  $\eta$  is small it follows from (1.16) that the computational cost of reducing bias is small; in the limit as  $\eta \to 0$  we again get  $\beta/(2\beta + \eta) \to 1/2$ . But for any finite  $\beta$  and positive  $\eta$ , (1.22) shows that we must expect a slower convergence rate using an estimator that is unbiased only asymptotically compared with one that is unbiased.

Under an allocation rule satisfying (1.16), taking  $\gamma = 1/(2\beta + \eta)$  implies that the bias parameter  $\delta$  should decrease rather slowly as the computational budget increases. Consider, for instance, bias resulting from model discretization error as in Example 1.1.1. In this setting, interpreting  $\delta$  as the simulation time increment, the values  $\beta = \eta = 1$  would often apply, resulting in  $\gamma = 1/3$ . Through  $(1.16)$ , this implies that the time increment should be cut in half with an eight-fold increase in the computational budget.

#### 1.2 Principles of Derivatives Pricing 19

In applications of Monte Carlo to financial engineering, estimator variance is typically larger than (squared) bias. With a few notable exceptions (including the pricing of American options), it is generally easier to implement a simulation with a comfortably small bias than with a comfortably small standard error. (For example, it is often difficult to measure the reduction in discretization bias achieved using the methods of Chapter 6 because the bias is overwhelmed by simulation variability.) This is consistent with the rather slow decrease in  $\delta(s)$  recommended by the analysis above, but it may also in part reflect the relative magnitudes of the constants b, c, and  $\sigma$ . These constants may be difficult to determine; the order of magnitude in  $(1.21)$  can nevertheless provide useful insight, especially when very precise simulation results are required, for which the limit  $s \to \infty$  is particularly relevant.

The argument above leading to  $(1.21)$  considers only the convergence of the mean square error. Glynn and Whitt [160] analyze asymptotic efficiency through the convergence rate of the limit in distribution of simulation estimators. Under uniform integrability conditions, a convergence rate in distribution implies a convergence rate for the MSE, but the limiting distribution also provides additional information, just as the central limit theorem  $(1.12)$  provides information beyond  $(1.13)$ .

# 1.2 Principles of Derivatives Pricing

The mathematical theory of derivatives pricing is both elegant and remarkably practical. A proper development of the theory and of the tools needed even to state precisely its main results requires a book-length treatment; we therefore assume familiarity with at least the basic ideas of mathematical finance and refer the reader to Björk [48], Duffie [98], Hunt and Kennedy [191], Lamberton and Lapeyre [218], and Musiela and Rutkowski [275] for further background. We will, however, highlight some principles of the theory, especially those that bear on the applicability of Monte Carlo to the calculation of prices. Three ideas are particularly important:

- 1. If a derivative security can be perfectly replicated (equivalently, hedged) through trading in other assets, then the price of the derivative security is the cost of the replicating trading strategy.
- 2. Discounted (or *deflated*) asset prices are martingales under a probability measure associated with the choice of discount factor (or *numeraire*). Prices are expectations of discounted payoffs under such a martingale measure.
- 3. In a *complete* market, any payoff (satisfying modest regularity conditions) can be synthesized through a trading strategy, and the martingale measure associated with a numeraire is unique. In an  $incomplete$  market there are derivative securities that cannot be perfectly hedged; the price of such a derivative is not completely determined by the prices of other assets.

The rest of this chapter is devoted to explaining these principles and to developing enough of the underlying theory to indicate why, leaving technical issues aside, they ought to be true. A reader familiar with or uninterested in this background may want to skip to the recipe in Figure 1.4, with a warning that the overly simplified summary given there is at best a starting point for applying Monte Carlo to pricing.

The first of the principles above is the foundation of an industry. Financial intermediaries can sell options to their clients and then eliminate the risk from the resulting short position in the option through trading in other assets. They need to charge what it costs to implement the trading strategy, and competition ensures that they cannot charge (much) more. Their clients could in principle run the replicating trading strategy themselves instead of buying options, but financial institutions are better equipped to do this and can do it at lower cost. This role should be contrasted with that of the insurance industry. Insurers bear risk; derivative dealers transfer it.

The second principle is the main link between pricing and Monte Carlo. The first principle gives us a way of thinking about what the price of a derivative security ought to be, but it says little about how this price might be  $\text{evaluated}$  — it leaves us with the task of finding a hedging strategy and then determining the cost of implementing this strategy. But the second principle gives us a powerful shortcut because it tells us how to represent prices as expectations. Expectations (and, more generally, integrals) lend themselves to evaluation through Monte Carlo and other numerical methods. The subtlety in this approach lies in the fact that we must describe the dynamics of asset prices not as we observe them but as they would be under a risk-adjusted probability measure.

The third principle may be viewed as describing conditions under which the price of a derivative security is determined by the prices of other assets so that the first and second principles apply. A complete market is one in which all risks can be perfectly hedged. If all uncertainty in a market is generated by independent Brownian motions, then completeness roughly corresponds to the requirement that the number of traded assets be at least as large as the number of driving Brownian motions. Jumps in asset prices will often render a model incomplete because it may be impossible to hedge the effect of discontinuous movements. In an incomplete market, prices can still be represented as expectations in substantial generality, but the risk adjustment necessary for this representation may not be uniquely determined. In this setting, we need more economic information  $-$  an understanding of investor attitudes towards risk — to determine prices, so the machinery of derivatives pricing becomes less useful.

A derivative security introduced into a complete market is a redundant asset. It does not expand investment opportunities; rather, it packages the trading strategy (from the first principle above) investors could have used anyway to synthesize the security. In this setting, pricing a derivative (using the second principle) may be viewed as a complex form of interpolation: we use a model to determine the price of the derivative relative to the prices of other assets. On this point, mathematical theory and industry practice are remarkably well aligned. For a financial institution to create a new derivative security, it must determine how it will hedge (or synthesize) the security by trading in other, more liquid assets, and it must determine the cost of this trading strategy from the prices of these other assets.

# 1.2.1 Pricing and Replication

To further develop these ideas, we consider an economy with  $d$  assets whose prices  $S_i(t), i = 1, \ldots, d$ , are described by a system of SDEs

$$\frac{dS_i(t)}{S_i(t)} = \mu_i(S(t), t) dt + \sigma_i(S(t), t)^{\top} dW^o(t), \qquad (1.23)$$

with  $W^o$  a k-dimensional Brownian motion, each  $\sigma_i$  taking values in  $\Re^k$ , and each  $\mu_i$  scalar-valued. We assume that the  $\mu_i$  and  $\sigma_i$  are deterministic functions of the current state  $S(t) = (S_1(t), \ldots, S_d(t))^{\top}$  and time t, though the general theory allows these coefficients to depend on past prices as well. (See Appendix B for a brief review of stochastic differential equations and references for further background.) Let

$$\Sigma_{ij} = \sigma_i^\top \sigma_j, \quad i, j = 1, \dots, d; \tag{1.24}$$

this may be interpreted as the covariance between the instantaneous returns on assets  $i$  and  $j$ .

A portfolio is characterized by a vector  $\theta \in \mathbb{R}^d$  with  $\theta_i$  representing the number of units held of the  $i$ th asset. Since each unit of the  $i$ th asset is worth  $S_i(t)$  at time t, the value of the portfolio at time t is

$$\theta_1 S_1(t) + \cdots + \theta_d S_d(t),$$

which we may write as  $\theta^{\top}S(t)$ . A trading strategy is characterized by a stochastic process  $\theta(t)$  of portfolio vectors. To be consistent with the intuitive notion of a trading strategy, we need to restrict  $\theta(t)$  to depend only on information available at  $t$ ; this is made precise through a measurability condition (for example, that  $\theta$  be *predictable*).

If we fix the portfolio holdings at  $\theta(t)$  over the interval  $[t, t+h]$ , then the change in value over this interval of the holdings in the *i*th asset is given by  $\theta_i(t)[S_i(t+h)-S_i(t)];$  the change in the value of the portfolio is given by  $\theta(t)^{\top}[S(t+h)-S(t)].$  This suggests that in the continuous-time limit we may describe the gains from trading over  $[0, t]$  through the stochastic integral

$$\int_0^t \theta(u)^\top \, dS(u),$$

subject to regularity conditions on S and  $\theta$ . Notice that we allow trading of arbitrarily large or small, positive or negative quantities of the underlying assets

continuously in time; this is a convenient idealization that ignores constraints on real trading.

A trading strategy is *self-financing* if it satisfies  $\frac{1}{2}$ 

$$\theta(t)^{\top} S(t) - \theta(0)^{\top} S(0) = \int_0^t \theta(u)^{\top} dS(u) \tag{1.25}$$

for all  $t$ . The left side of this equation is the change in portfolio value from time 0 to time  $t$  and the right side gives the gains from trading over this interval. Thus, the self-financing condition states that changes in portfolio value equal gains from trading: no gains are withdrawn from the portfolio and no funds are added. By rewriting  $(1.25)$  as

$$\theta(t)^{\top} S(t) = \theta(0)^{\top} S(0) + \int_0^t \theta(u)^{\top} dS(u),$$

we can interpret it as stating that from an initial investment of  $V(0)$  $\theta(0)^{\top}S(0)$  we can achieve a portfolio value of  $V(t) = \theta(t)^{\top}S(t)$  by following the strategy  $\theta$  over [0, t].

Consider, now, a derivative security with a payoff of  $f(S(T))$  at time T; this could be a standard European call or put on one of the  $d$  assets, for example, but the payoff could also depend on several of the underlying assets. Suppose that the value of this derivative at time  $t, 0 \le t \le T$ , is given by some function  $V(S(t), t)$ . The fact that the dynamics in (1.23) depend only on  $(S(t), t)$  makes it at least plausible that the same might be true of the derivative price. If we further conjecture that  $V$  is a sufficiently smooth function of its arguments,  $\text{Itô's formula (see Appendix B) gives}$ 

$$V(S(t),t) = V(S(0),0) + \sum_{i=1}^{d} \int_{0}^{t} \frac{\partial V(S(u),u)}{\partial S_{i}} dS_{i}(u) + \int_{0}^{t} \left[ \frac{\partial V(S(u),u)}{\partial u} \right]$$
$$+ \frac{1}{2} \sum_{i,j=1}^{d} S_{i}(u)S_{j}(u)\Sigma_{ij}(S(u),u) \frac{\partial^{2} V(S(u),u)}{\partial S_{i}\partial S_{j}} du, \qquad (1.26)$$

with  $\Sigma$  as in (1.24). If the value  $V(S(t),t)$  can be achieved from an initial wealth of  $V(S(0), 0)$  through a self-financing trading strategy  $\theta$ , then we also have

$$V(S(t),t) = V(S(0),0) + \sum_{i=1}^{d} \int_{0}^{t} \theta_{i}(u) \, dS_{i}(u). \tag{1.27}$$

Comparing terms in  $(1.26)$  and  $(1.27)$ , we find that both equations hold if

$$\theta_i(u) = \frac{\partial V(S(u), u)}{\partial S_i}, \quad i = 1, \dots, d,$$
(1.28)

 $\text{and}$ 

1.2 Principles of Derivatives Pricing 23

$$\frac{\partial V(S,u)}{\partial u} + \frac{1}{2} \sum_{i,j=1}^{d} \Sigma_{ij}(S,u) S_i S_j \frac{\partial^2 V(S,u)}{\partial S_i \partial S_j} = 0. \tag{1.29}$$

Since we also have  $V(S(t), t) = \theta^{\top}(t)S(t)$ , (1.28) implies

$$V(S,t) = \sum_{i=1}^{d} \frac{\partial V(S,t)}{\partial S_i} S_i.$$
 (1.30)

Finally, at  $t = T$  we must have

$$V(S,T) = f(S) \tag{1.31}$$

if  $V$  is indeed to represent the value of the derivative security.

Equations  $(1.29)$  and  $(1.30)$ , derived here following the approach in Hunt and Kennedy [191], describe V through a partial differential equation (PDE) with boundary condition (1.31). Suppose we could find a solution  $V(S, t)$ . In what sense would we be justified in calling this the price of the derivative security?

By construction, V satisfies  $(1.29)$  and  $(1.30)$ , and then  $(1.26)$  implies that the (assumed) self-financing representation  $(1.27)$  indeed holds with the trading strategy defined by  $(1.28)$ . Thus, we may sell the derivative security for  $V(S(0), 0)$  at time 0, use the proceeds to implement this self-financing trading strategy, and deliver the promised payoff of  $f(S(T),T) = V(S(T),T)$  at time T with no risk. If anyone were willing to pay more than  $V(S(0), 0)$ , we could sell the derivative and be guaranteed a riskless profit from a net investment of zero; if anyone were willing to sell the derivative for less than  $V(S(0),0)$ , we could buy it, implement the strategy  $-\theta(t)$ , and again be ensured a riskless profit without investment. Thus,  $V(S(0),0)$  is the only price that rules out riskless profits from zero net investment.

From  $(1.30)$  we see that the trading strategy that replicates V holds  $\partial V(S,t)/\partial S_i$  shares of the *i*th underlying asset at time t. This partial derivative is the *delta* of V with respect to  $S_i$  and the trading strategy is called  $\text{delta hedging.}$ 

Inspection of (1.29) and (1.30) reveals that the drift parameters  $\mu_i$  in the asset price dynamics  $(1.23)$  do not appear anywhere in the partial differential equation characterizing the derivative price  $V$ . This feature is sometimes paraphrased through the statement that the price of a derivative does not depend on the drifts of the underlying assets; it would be more accurate to say that the effect of the drifts on the price of a derivative is already reflected in the underlying asset prices  $S_i$  themselves, because V depends on the  $S_i$ and the  $S_i$  are clearly affected by the  $\mu_i$ .

The drifts of the underlying asset prices reflect investor attitudes toward risk. In a world of risk-averse investors, we may expect riskier assets to grow at a higher rate of return, so larger values of  $\sigma_{ij}$  should be associated with larger values of  $\mu_i$ . In a world of risk-neutral investors, all assets should grow at the

 $same \ rate \ - \ \text{investors} \ \text{will not demand higher returns for riskier assets. The}$ fact that the  $\mu_i$  do not appear in the equations for the derivative price V may therefore be interpreted as indicating that we can price the derivative without needing to know anything about investor attitudes toward risk. This relies critically on the existence of a self-financing trading strategy that replicates V: because we have assumed that V can be replicated by trading in the underlying assets, risk preferences are irrelevant; the price of the derivative is simply the minimal initial investment required to implement the replicating  $strategy.$ 

# Black-Scholes Model

As an illustration of the general formulation in  $(1.29)$  and  $(1.30)$ , we consider the pricing of European options in the Black-Scholes model. The model contains two assets. The first (often interpreted as a stock price) is risky and its dynamics are represented through the scalar SDE

$$\frac{dS(t)}{S(t)} = \mu \, dt + \sigma \, dW^o(t)$$

with  $W^o$  a one-dimensional Brownian motion. The second asset (often called a savings account or a money market account) is riskless and grows deterministically at a constant, continuously compounded rate  $r$ ; its dynamics are given by

$$\frac{d\beta(t)}{\beta(t)} = r \, dt.$$

Clearly,  $\beta(t) = \beta(0)e^{rt}$  and we may assume the normalization  $\beta(0) = 1$ . We are interested in pricing a derivative security with a payoff of  $f(S(T))$  at time T. For example, a standard call option pays  $(S(T)-K)^+$ , with K a constant.

If we were to formulate this model in the notation of (1.23),  $\Sigma$  would be a  $2 \times 2$  matrix with only one nonzero entry,  $\sigma^2$ . Making the appropriate substitutions,  $(1.29)$  thus becomes

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = 0. \tag{1.32}$$

Equation  $(1.30)$  becomes

$$V(S,\beta,t) = \frac{\partial V}{\partial S}S + \frac{\partial V}{\partial \beta}\beta.$$
 (1.33)

These equations and the boundary condition  $V(S, \beta, T) = f(S)$  determine the price  $V$ .

This formulation describes the price  $V$  as a function of the three variables S,  $\beta$ , and t. Because  $\beta$  depends deterministically on t, we are interested in values of V only at points  $(S, \beta, t)$  with  $\beta = e^{rt}$ . This allows us to eliminate one variable and write the price as  $\tilde{V}(S,t) = V(S,e^{rt},t)$ , as in Hunt and Kennedy [191]. Making this substitution in  $(1.32)$  and  $(1.33)$ , noting that

$$\frac{\partial \tilde{V}}{\partial t} = \frac{\partial V}{\partial \beta} r \beta + \frac{\partial V}{\partial t}$$

and simplifying yields

$$\frac{\partial \tilde{V}}{\partial t} + rS \frac{\partial \tilde{V}}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 \tilde{V}}{\partial S^2} - r\tilde{V} = 0.$$

This is the Black-Scholes PDE characterizing the price of a European derivative security. For the special case of the boundary condition  $V(S,T)$  $(S-K)^{+}$ , the solution is given by  $\tilde{V}(S,t) = \text{BS}(S,\sigma,T-t,r,K)$ , the Black-Scholes formula in  $(1.4)$ .

# 1.2.2 Arbitrage and Risk-Neutral Pricing

The previous section outlined an argument showing how the existence of a self-financing trading strategy that replicates a derivative security determines the price of the derivative security. Under assumptions on the dynamics of the underlying assets, this argument leads to a partial differential equation characterizing the price of the derivative.

Several features may, however, limit the feasibility of calculating derivative prices by solving PDEs. If the asset price dynamics are sufficiently complex, a PDE characterizing the derivative price may be difficult to solve or may even fail to exist. If the payoff of a derivative security depends on the *paths* of the underlying assets and not simply their terminal values, the assumption that the price can be represented as a function  $V(S,t)$  generally fails to hold. If the number of underlying assets required by the replicating strategy is large (greater than two or three), numerical solution of the PDE may be impractical. These are precisely the settings in which Monte Carlo simulation is likely to be most useful. However, to apply Monte Carlo we must first find a more convenient representation of derivative prices. In particular, we would like to represent derivative prices as expectations of random objects that we can simulate. This section develops such representations.

### Arbitrage and Stochastic Discount Factors

We return to the general setting described by the asset price dynamics in  $(1.23)$ , for emphasis writing  $P_o$  for the probability measure under which these dynamics are specified. (In particular, the process  $W^o$  in (1.23) is a standard Brownian motion under  $P_o$ .) The measure  $P_o$  is intended to describe objective ("real-world") probabilities and the system of SDEs in  $(1.23)$  thus describes the empirical dynamics of asset prices.

Recall the definition of a self-financing trading strategy  $\theta(t)$  as given in (1.25). A self-financing trading strategy  $\theta(t)$  is called an *arbitrage* if either of the following conditions holds for some fixed time  $t$ :

(i) 
$$\theta(0)^{\top}S(0) < 0 \text{ and } P_o(\theta(t)^{\top}S(t) \ge 0) = 1;$$
  
(ii)  $\theta(0)^{\top}S(0) = 0, \ P_o(\theta(t)^{\top}S(t) \ge 0) = 1, \text{ and } P_o(\theta(t)^{\top}S(t) > 0) > 0.$ 

In (i),  $\theta$  turns a negative initial investment into nonnegative final wealth with probability 1. In (ii),  $\theta$  turns an initial net investment of 0 into nonnegative final wealth that is positive with positive probability. Each of these corresponds to an opportunity to create something from nothing and is incompatible with economic equilibrium. Precluding arbitrage is a basic consistency requirement on the dynamics of the underlying assets in  $(1.23)$  and on the prices of any derivative securities that can be synthesized from these assets through selffinancing trading strategies.

Call a process  $V(t)$  an *attainable* price process if  $V(t) = \theta(t)^{\top} S(t)$  for some self-financing trading strategy  $\theta$ . Thus, a European derivative security can be replicated by trading in the underlying assets precisely if its payoff at expiration T coincides with the value  $V(T)$  of some attainable price process at time T. Each of the underlying asset prices  $S_i(t)$  in (1.23) is attainable through the trivial strategy that sets  $\theta_i \equiv 1$  and  $\theta_i \equiv 0$  for all  $j \neq i$ .

We now introduce an object whose role may at first seem mysterious but which is central to asset pricing theory. Call a strictly positive process  $Z(t)$  a stochastic discount factor (or a deflator) if the ratio  $V(t)/Z(t)$  is a martingale for every attainable price process  $V(t)$ ; i.e., if

$$\frac{V(t)}{Z(t)} = \mathsf{E}_o\left[\frac{V(T)}{Z(T)}|\mathcal{F}_t\right],\tag{1.34}$$

whenever  $t < T$ . Here,  $\mathsf{E}_o$  denotes expectation under  $P_o$  and  $\mathcal{F}_t$  represents the history of the Brownian motion  $W^o$  up to time t. We require that  $Z(t)$  be adapted to  $\mathcal{F}_t$ , meaning that the value of  $Z(t)$  is determined by the history of the Brownian motion up to time t. Rewriting  $(1.34)$  as

$$V(t) = \mathsf{E}_o\left[V(T)\frac{Z(t)}{Z(T)}|\mathcal{F}_t\right] \tag{1.35}$$

explains the term "stochastic discount factor": the price  $V(t)$  is the expected discounted value of the price  $V(T)$  if we discount using  $Z(t)/Z(T)$ . (It is more customary to refer to  $1/Z(t)$  rather than  $Z(t)$  as the stochastic discount factor, deflator, or *pricing kernel*; our use of the terminology is nonstandard but leads to greater symmetry when we discuss numeraire assets.) Notice that any constant multiple of a stochastic discount factor is itself a stochastic discount factor so we may adopt the normalization  $Z(0) \equiv 1$ . Equation (1.35) then specializes to

$$V(0) = \mathsf{E}_o\left[\frac{V(T)}{Z(T)}\right].\tag{1.36}$$

Suppose, for example, that  $V(t)$  represents the price at time t of a call option on the *i*th underlying asset with strike price  $K$  and expiration  $T$ . Then  $V(T) = (S_i(T) - K)^+$ ; in particular, V is a known function of  $S_i$  at time T. Equation (1.36) states that the terminal value  $V(T)$  determines the initial value  $V(0)$  through stochastic discounting.

We may think of (1.36) as reflecting two ways in which the price  $V(0)$ differs from the expected payoff  $\mathsf{E}_{o}[V(T)]$ . The first results from "the time value of money": the payoff  $V(T)$  will not be received until T, and other things being equal we assume investors prefer payoffs received sooner rather than later. The second results from attitudes toward risk. In a world of riskaverse investors, risky payoffs should be more heavily discounted in valuing a security; this could not be accomplished through a deterministic discount factor.

Most importantly for our purposes, the existence of a stochastic discount factor rules out arbitrage. If  $\theta$  is a self-financing trading strategy, then the process  $\theta(t)^{\top}S(t)$  is an attainable price process and the ratio  $\theta(t)^{\top}S(t)/Z(t)$ must be a martingale. In particular, then,

$$\theta(0)^{\top} S(0) = \mathsf{E}_o \left[ \frac{\theta(T)^{\top} S(T)}{Z(T)} \right],$$

as in  $(1.36)$ . Compare this with conditions (i) and (ii) above for an arbitrage, recalling that Z is nonnegative. If  $\theta(T)^{\top}S(T)$  is almost surely positive, it is impossible for  $\theta(0)^{\top}S(0)$  to be negative; if  $\theta(T)^{\top}S(T)$  is positive with positive probability and almost surely nonnegative, then  $\theta(0)^{\top}S(0) = 0$  is impossible. Thus, there can be no arbitrage if the attainable price processes admit a stochastic discount factor.

It is less obvious that the converse also holds: under a variety of technical conditions on asset price dynamics and trading strategies, it has been shown that the absence of arbitrage implies the existence of a stochastic discount factor (or the closely related concept of an equivalent martingale measure). We return to this point in Section  $1.2.4$ . The equivalence of no-arbitrage to the existence of a stochastic discount factor is often termed the Fundamental Theorem of Asset Pricing, though it is not a single theorem but rather a body of results that apply under various sets of conditions. An essential early reference is Harrison and Kreps [170]; for further background and results, see Duffie [98] and Musiela and Rutkowski [275].

# Risk-Neutral Pricing

Let us suppose that among the d assets described in  $(1.23)$  there is one that is risk-free in the sense that its coefficients  $\sigma_{ij}$  are identically zero. Let us further assume that its drift, which may be interpreted as a riskless interest rate, is a constant r. As in our discussion of the Black-Scholes model in Section  $1.2.1$ , we denote this asset by  $\beta(t)$  and refer to it as the money market account. Its

dynamics are given by the equation  $d\beta(t)/\beta(t) = r dt$ , with solution  $\beta(t) = r dt$  $\beta(0) \exp(rt)$ ; we fix  $\beta(0)$  at 1.

Clearly,  $\beta(t)$  is an attainable price process because it corresponds to the trading strategy that makes an initial investment of  $1$  in the money market account and continuously reinvests all gains in this single asset. Accordingly, if the market admits a stochastic discount factor  $Z(t)$ , the process  $\beta(t)/Z(t)$ is a martingale. This martingale is positive because both  $\beta(t)$  and  $Z(t)$  are positive, and it has an initial value of  $\beta(0)/Z(0) = 1$ .

Any positive martingale with an initial value 1 defines a change of probability measure. For each fixed interval [0, T], the process  $\beta(t)/Z(t)$  defines a new measure  $P_{\beta}$  through the Radon-Nikodym derivative (or likelihood ratio  $process)$ 

$$\left(\frac{dP_{\beta}}{dP_{o}}\right)_{t} = \frac{\beta(t)}{Z(t)}, \quad 0 \le t \le T. \n$$
(1.37)

More explicitly, this means (cf. Appendix B.4) that for any event  $A \in \mathcal{F}_t$ ,

$$P_{\beta}(A) = \mathsf{E}_{o} \left[ \mathbf{1}_{A} \cdot \left( \frac{dP_{\beta}}{dP_{o}} \right)_{t} \right] = \mathsf{E}_{o} \left[ \mathbf{1}_{A} \cdot \frac{\beta(t)}{Z(t)} \right]$$

where  $\mathbf{1}_{A}$  denotes the indicator of the event A. Similarly, expectation under the new measure is defined by

$$\mathsf{E}_{\beta}\left[X\right] = \mathsf{E}_{o}\left[X\frac{\beta(t)}{Z(t)}\right] \tag{1.38}$$

for any nonnegative X measurable with respect to  $\mathcal{F}_t$ . The measure  $P_{\beta}$  is called the *risk-neutral* measure; it is equivalent to  $P_o$  in the sense of measures, meaning that  $P_{\beta}(A) = 0$  if and only if  $P_{o}(A) = 0$ . (Equivalent probability measures agree about which events are impossible.) The risk-neutral measure is a particular choice of *equivalent martingale measure*.

Consider, again, the pricing equation  $(1.36)$ . In light of  $(1.38)$ , we may rewrite it as

$$V(0) = \mathsf{E}_{\beta} \left[ \frac{V(T)}{\beta(T)} \right] = e^{-rT} \mathsf{E}_{\beta}[V(T)]. \tag{1.39}$$

This simple transformation is the cornerstone of derivative pricing by Monte Carlo simulation. Equation (1.39) expresses the current price  $V(0)$  as the expected present value of the terminal value  $V(T)$  discounted at the risk-free rate r rather than through the stochastic discount factor Z. The expectation in  $(1.39)$  is taken with respect to  $P_{\beta}$  rather than  $P_{o}$ , so estimating the expectation by Monte Carlo entails simulating under  $P_{\beta}$  rather than  $P_{o}$ . These points are crucial to the applicability of Monte Carlo because

- the dynamics of  $Z(t)$  are generally unknown and difficult to model (since 0 they embody time and risk preferences of investors);
- the dynamics of the underlying asset prices are more easily described under 0 the risk-neutral measure than under the objective probability measure.

#### 1.2 Principles of Derivatives Pricing 29

The second point requires further explanation. Equation  $(1.39)$  generalizes to

$$V(t) = \mathsf{E}_{\beta} \left[ V(T) \frac{\beta(t)}{\beta(T)} | \mathcal{F}_t \right], \quad t < T,$$
 (1.40)

with  $V(t)$  an attainable price process. In particular, then, since each  $S_i(t)$  is an attainable price process, each ratio  $S_i(t)/\beta(t)$  is a martingale under  $P_{\beta}$ . Specifying asset price dynamics under the risk-neutral measure thus entails specifying dynamics that make the ratios  $S_i(t)/\beta(t)$  martingales. If the dynamics of the asset prices in  $(1.23)$  could be expressed as

$$\frac{dS_i(t)}{S_i(t)} = r dt + \sigma_i(S(t), t)^\top dW(t), \qquad (1.41)$$

with W a standard k-dimensional Brownian motion under  $P_{\beta}$ , then

$$d\left(\frac{S_i(t)}{\beta(t)}\right) = \left(\frac{S_i(t)}{\beta(t)}\right)\sigma_i(S(t),t)^\top dW(t),$$

so  $S_i(t)/\beta(t)$  would indeed be a martingale under  $P_\beta$ . Specifying a model of the form  $(1.41)$  is simpler than specifying the original equation  $(1.23)$  because all drifts in  $(1.41)$  are set equal to the risk-free rate r: the potentially complicated drifts in  $(1.23)$  are irrelevant to the asset price dynamics under the risk-neutral measure. Indeed, this explains the name "risk-neutral." In a world of riskneutral investors, the rate of return on risky assets would be the same as the risk-free rate.

Comparison of  $(1.41)$  and  $(1.23)$  indicates that the two are consistent if

$$dW(t) = dW^{o}(t) + \nu(t) dt$$
  
for some  $\nu$  satisfying  $\mu_i = r + \sigma_i^{\top} \nu, \ i = 1, \dots, d,$  (1.42)

because making this substitution in  $(1.41)$  yields

T.

$$\begin{split} \frac{dS_i(t)}{S_i(t)} &= r \, dt + \sigma_i(S(t), t)^\top \left[ dW^o(t) + \nu(t) \, dt \right] \\ &= \left( r + \sigma_i(S(t), t)^\top \nu(t) \right) dt + \sigma_i(S(t), t)^\top dW^o(t) \\ &= \mu_i(S(t), t) \, dt + \sigma_i(S(t), t)^\top dW^o(t), \end{split}$$

as in  $(1.23)$ . The condition in  $(1.42)$  states that the objective and risk-neutral measures are related through a change of drift in the driving Brownian motion. It follows from the Girsanov Theorem (see Appendix B) that any measure equivalent to  $P_o$  must be related to  $P_o$  in this way. In particular, the diffusion terms  $\sigma_{ij}$  in (1.41) and (1.23) must be the same. This is important because it ensures that the coefficients required to describe the dynamics of asset prices under the risk-neutral measure  $P_{\beta}$  can be estimated from data observed under the real-world measure  $P_o$ .

We now briefly summarize the pricing of derivative securities through the risk-neutral measure with Monte Carlo simulation. Consider a derivative security with a payoff at time  $T$  specified through a function  $f$  of the prices of the underlying assets, as in the case of a standard call or put. To price the derivative, we model the dynamics of the underlying assets under the risk-neutral measure, ensuring that discounted asset prices are martingales, typically through choice of the drift. The price of the derivative is then given by  $\mathsf{E}_{\beta}[e^{-rT}f(S(T))]$ . To evaluate this expectation, we simulate paths of the underlying assets over the time interval  $[0, T]$ , simulating according to their risk-neutral dynamics. On each path we calculate the discounted payoff  $e^{-rT}f(S(T))$ ; the average across paths is our estimate of the derivative's price. Figure 1.4 gives a succinct statement of these steps, but it should be clear that especially the first step in the figure is an oversimplification.

### Monte Carlo Recipe for Cookbook Pricing

- $\circ$  replace drifts  $\mu_i$  in (1.23) with risk-free interest rate and simulate paths;
- o calculate payoff of derivative security on each path;
- o discount payoffs at the risk-free rate:
- o calculate average over paths.

**Fig. 1.4.** An overly simplified summary of risk-neutral pricing by Monte Carlo.

## Black-Scholes Model

To illustrate these ideas, consider the pricing of a call option on a stock. Suppose the real-world dynamics of the stock are given by

$$\frac{dS(t)}{S(t)} = \mu(S(t), t) dt + \sigma dW^{o}(t),$$

with  $W^o$  a standard one-dimensional Brownian motion under  $P_o$  and  $\sigma$  a constant. Each unit invested in the money market account at time 0 grows to a value of  $\beta(t) = e^{rt}$  at time t. Under the risk-neutral measure  $P_{\beta}$ , the stock price dynamics are given by

$$\frac{dS(t)}{S(t)} = r \, dt + \sigma \, dW(t)$$

with W a standard Brownian motion under  $P_{\beta}$ . This implies that

$$S(T) = S(0)e^{(r - \frac{1}{2}\sigma^2)T + \sigma W(T)}.$$

If the call option has strike  $K$  and expiration  $T$ , its price at time 0 is given by  $\mathsf{E}_{\beta}[e^{-rT}(S(T)-K)^{+}].$  Because  $W(T)$  is normally distributed, this expectation

can be evaluated explicitly and results in the Black-Scholes formula  $(1.4)$ . In particular, pricing through the risk-neutral measure produces the same result as pricing through the PDE formulation in Section  $1.2.1$ , as it must since in both cases the price is determined by the absence of arbitrage. This also explains why we are justified in equating the expected discounted payoff calculated in Section  $1.1.2$  with the price of the option.

# Dividends

Thus far, we have implicitly assumed that the underlying assets  $S_i$  do not pay dividends. This is implicit, for example, in our discussion of the self-financing trading strategies. In the definition (1.25) of a self-financing strategy  $\theta$ , we interpret  $\theta_i(u) dS_i(u)$  as the trading gains from the *i*th asset over the time increment  $du$ . This, however, reflects only the capital gains resulting from the change in price in the *i*th asset. If each share pays dividends at rate  $dD_i(u)$  over du, then the portfolio gains would also include terms of the form  $\theta_i(u) dD_i(u)$ .

In the presence of dividends, a simple strategy of holding a single share of a single asset is no longer self-financing, because it entails withdrawal of the dividends from the portfolio. In contrast, a strategy that continuously reinvests all dividends from an asset back into that asset is self-financing in the sense that it involves neither the withdrawal nor addition of funds from the portfolio. When dividends are reinvested, the number of shares held changes over time.

These observations suggest that we may accommodate dividends by redefining the original assets to include the reinvested dividends. Let  $\tilde{S}_i(t)$  be the *i*th asset price process with dividends reinvested, defined through the requirement

$$\frac{d\tilde{S}_i(t)}{\tilde{S}_i(t)} = \frac{dS_i(t) + dD_i(t)}{S_i(t)}.\tag{1.43}$$

The expression on the right is the instantaneous return on the *i*th original asset, including both capital gains and dividends; the expression on the left is the instantaneous return on the  $i$ th new asset in which all dividends are reinvested. For  $S_i$  to support this interpretation, the two sides must be equal.

The new assets  $\tilde{S}_i$  pay no dividends so we may apply the ideas developed above in the absence of dividends to these assets. In particular, we may reinterpret the asset price dynamics in (1.23) as applying to the  $\tilde{S}_i$  rather than to the original  $S_i$ . One consequence of this is that the  $S_i$  will have continuous paths, so any discontinuities in the cumulative dividend process  $D_i$  must be offset by the original asset price  $S_i$ . For example, a discrete dividend corresponds to a positive jump in  $D_i$  and this must be accompanied by an offsetting negative jump in  $S_i$ .

For purposes of derivative pricing, the most important point is that the martingale property under the risk-neutral measure applies to  $S_i(t)/\beta(t)$ 

rather than  $S_i(t)/\beta(t)$ . This affects how we model the dynamics of the  $S_i$ under  $P_{\beta}$ . Consider, for example, an asset paying a continuous dividend yield at rate  $\delta$ , meaning that  $dD_i(t) = \delta S_i(t) dt$ . For  $e^{-rt}\tilde{S}_i(t)$  to be a martingale, we require that the dt coefficient in  $d\tilde{S}_i(t)/\tilde{S}_i(t)$  be r. Equating dt terms on the two sides of  $(1.43)$ , we conclude that the coefficient on dt in the equation for  $dS_i(t)/S_i(t)$  must be  $r-\delta$ . Thus, in modeling asset prices under the riskneutral measure, the effect of a continuous dividend yield is to change the drift. The first step in Figure 1.4 is modified accordingly.

As a specific illustration, consider a version of the Black-Scholes model in which the underlying asset has dividend yield  $\delta$ . The risk-neutral dynamics of the asset are given by

$$\frac{dS(t)}{S(t)} = (r - \delta) dt + \sigma dW(t)$$

with solution

$$S(t) = S(0)e^{(r-\delta-\frac{1}{2}\sigma^2)t+\sigma W(t)}$$

The price of a call option with strike  $K$  and expiration  $T$  is given by the expectation  $\mathsf{E}_{\beta}[e^{-rT}(S(T)-K)^{+}],$  which evaluates to

$$e^{-\delta T}S(0)\Phi(d) - e^{-rT}K\Phi(d-\sigma\sqrt{T}), \quad d = \frac{\log(S(0)/K) + (r-\delta + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}},\tag{1.44}$$

with  $\Phi$  the cumulative normal distribution.

# 1.2.3 Change of Numeraire

The risk-neutral pricing formulas  $(1.39)$  and  $(1.40)$  continue to apply if the constant risk-free rate r is replaced with a time-varying rate  $r(t)$ , in which case the money market account becomes

$$\beta(t) = \exp\left(\int_0^t r(u) \, du\right)$$

and the pricing formula becomes

$$V(t) = \mathsf{E}_{\beta} \left[ \exp\left(-\int_{t}^{T} r(u) \, du\right) V(T) | \mathcal{F}_{t} \right]$$

The risk-neutral dynamics of the asset prices now take the form

$$\frac{dS_i(t)}{S_i(t)} = r(t) dt + \sigma_i(S(t), t)^\top dW(t),$$

with W a standard k-dimensional Brownian motion under  $P_{\beta}$ . Subject only to technical conditions, these formulas remain valid if the short rate  $r(t)$  is a stochastic process.

Indeed, our choice of  $\beta(t)$  as the asset through which to define a new probability measure in  $(1.38)$  was somewhat arbitrary. This choice resulted in pricing formulas with the appealing feature that they discount payoffs at the risk-free rate; it also resulted in a simple interpretation of the measure  $P_{\beta}$  as risk-neutral in the sense that all assets grow at the risk-free rate under this measure. Nevertheless, we could just as well have chosen a different asset as numeraire, meaning the asset relative to which all others are valued. As we explain next, all choices of numeraire result in analogous pricing formulas and the flexibility to change the numeraire is a useful modeling and computational tool.

Although we could start from the objective measure  $P_o$  as we did in Section 1.2.2, it may be simpler to start from the risk-neutral measure  $P_{\beta}$ , especially if we assume a constant risk-free rate r. Choosing asset  $S_d$  as numeraire means defining a new probability measure  $P_{S_d}$  through the likelihood ratio  $process (Radon-Nikodym derivative)$ 

$$\left(\frac{dP_{S_d}}{dP_{\beta}}\right)_t = \left.\frac{S_d(t)}{\beta(t)}\right/ \frac{S_d(0)}{\beta(0)}.$$

Recall that  $S_d(t)/\beta(t)$  is a positive martingale under  $P_\beta$ ; dividing it by its initial value produces a unit-mean positive martingale and thus defines a change of measure. Expectation under  $P_{S_d}$  is given by

$$\mathsf{E}_{S_d}[X] = \mathsf{E}_{\beta} \left[ X \left( \frac{dP_{S_d}}{dP_{\beta}} \right)_t \right] = \mathsf{E}_{\beta} \left[ X \frac{S_d(t)\beta(0)}{\beta(t)S_d(0)} \right]$$

for nonnegative  $X \in \mathcal{F}_t$ . The pricing formula (1.39) thus implies (recalling that  $\beta(0) = 1$ 

$$V(0) = \mathsf{E}_{\beta} \left[ \frac{V(T)}{\beta(T)} \right] = S_d(0) \mathsf{E}_{S_d} \left[ \frac{V(T)}{S_d(T)} \right]. \tag{1.45}$$

Equation  $(1.40)$  similarly implies

$$V(t) = S_d(t) \mathsf{E}_{S_d} \left[ \frac{V(T)}{S_d(T)} | \mathcal{F}_t \right]. \tag{1.46}$$

Thus, to price under  $P_{S_d}$ , we discount the terminal value  $V(T)$  by dividing by the terminal value of the numeraire and multiplying by the current value of the numeraire.

Some examples should help illustrate the potential utility of this transformation. Consider, first, an option to exchange one asset for another, with payoff  $(S_1(T) - S_2(T))^+$  at time T. The price of the option is given by

$$e^{-rT} \mathsf{E}_{\beta} [(S_1(T) - S_2(T))^+]$$

but also by

$$S_2(0)\mathsf{E}_{S_2}\left[\frac{(S_1(T)-S_2(T))^+}{S_2(T)}\right] = S_2(0)\mathsf{E}_{S_2}\left[([S_1(T)/S_2(T)]-1)^+\right].$$

The expression on the right looks like the price of a standard call option on the ratio of the two assets with a strike of 1; it reveals that the price of the exchange option is sensitive to the dynamics of the ratio but not otherwise to the dynamics of the individual assets. In particular, if the ratio has a constant volatility (a feature invariant under equivalent changes of measure), then the option can be valued through a variant of the Black-Scholes formula due to Margrabe  $[247]$ .

Consider, next, a call option on a foreign stock whose payoff will be converted to the domestic currency at the exchange rate prevailing at the expiration date T. Letting  $S_1$  denote the stock price in the foreign currency and letting  $S_2$  denote the exchange rate (expressed as number of domestic units per foreign unit), the payoff (in domestic currency) becomes  $S_2(T)(S_1(T)-K)^+$ with price

$$e^{-rT} \mathsf{E}_{\beta}[S_2(T)(S_1(T) - K)^+].$$

Each unit of foreign currency earns interest at a risk-free rate  $r_f$  and this acts like a continuous dividend yield. Choosing  $\tilde{S}_2(t) \equiv e^{r_f t} S_2(t)$  as numeraire, we may express the price as

$$e^{-r_f T} S_2(0) \mathsf{E}_{\tilde{S}_2} [(S_1(T) - K)^+],$$

noting that  $S_2(0) = \tilde{S}_2(0)$ . This expression involves the current exchange rate  $S_2(0)$  but not the unknown future rate  $S_2(T)$ .

The flexibility to change numeraire can be particularly valuable in a model with stochastic interest rates, so our last example applies to this setting. Consider an interest rate derivative with a payoff of  $V(T)$  at time T. Using the risk-neutral measure, we can express its price as

$$V(0) = \mathsf{E}_{\beta} \left[ \exp \left( - \int_0^T r(u) \, du \right) V(T) \right].$$

The forward measure for maturity  $T_F$  is the measure associated with taking as numeraire a zero-coupon bond maturing at  $T_F$  with a face value of 1. We denote the time-t value of the bond by  $B(t,T_F)$  (so  $B(T_F,T_F) \equiv 1$ ) and the associated measure by  $P_{T_F}$ . Using this measure, we can write the price as

$$V(0) = B(0, T_F) \mathsf{E}_{T_F} \left[ \frac{V(T)}{B(T, T_F)} \right].$$

With the specific choice  $T_F = T$ , we get

$$V(0) = B(0,T)\mathsf{E}_T[V(T)]$$

Observe that in this expression the discount factor (the initial bond price) is deterministic even though the interest rate  $r(t)$  may be stochastic. This feature often leads to useful simplifications in pricing interest rate derivatives.

To use any of the price representations above derived through a change of numeraire, we need to know the dynamics of the underlying asset prices under the corresponding probability measure. For example, if in  $(1.45)$  the terminal value  $V(T)$  is a function of the values  $S_i(T)$  of the underlying assets, then to estimate the rightmost expectation through Monte Carlo we need to be able to simulate paths of the underlying assets according to their dynamics under  $P_{S_d}$ . We encountered the same issue in Section 1.2.2 in pricing under the risk-neutral measure  $P_{\beta}$ . There we noted that changing from the objective measure  $P_o$  to the risk-neutral measure had the effect of changing the drifts of all prices to the risk-free rate; an analogous change of drift applies more generally in changing numeraire.

 $\sim$ 

Based on the dynamics in (1.41), we may write the asset price  $S_d(t)$  as

$$S_d(t) = S_d(0) \exp\left(\int_0^t \left[r(u) - \frac{1}{2} \|\sigma_d(u)\|^2\right] \, du + \int_0^t \sigma_d(u)^\top \, dW(u)\right), \tag{1.47}$$

with W a standard Brownian motion under  $P_{\beta}$ . Here, we have implicitly generalized the setting in  $(1.41)$  to allow the short rate to be time-varying and even stochastic; we have also abbreviated  $\sigma_d(S(u), u)$  as  $\sigma_d(u)$  to lighten notation. From this and the definition of  $P_{S_d}$ , we therefore have

$$\left(\frac{dP_{S_d}}{dP_{\beta}}\right)_t = \exp\left(\int_0^t -\frac{1}{2} \|\sigma_d(u)\|^2 \, du + \int_0^t \sigma_d(u)^\top \, dW(u)\right).$$

Through the Girsanov Theorem (see Appendix B), we find that changing measure from  $P_{\beta}$  to  $P_{S_d}$  has the effect of adding a drift to W. More precisely, the process  $W^d$  defined by

$$dW^{d}(t) = -\sigma_{d}(t) dt + dW(t) \qquad (1.48)$$

is a standard Brownian motion under  $P_{S_d}$ . Making this substitution in (1.41), we find that

$$\begin{split} \frac{dS_i(t)}{S_i(t)} &= r(t) \, dt + \sigma_i(t)^\top \, dW(t) \\ &= r(t) \, dt + \sigma_i(t)^\top \left[ dW^d(t) + \sigma_d(t) \, dt \right] \\ &= \left[ r(t) + \sigma_i(t)^\top \sigma_d(t) \right] dt + \sigma_i(t)^\top \, dW^d(t) \\ &= \left[ r(t) + \Sigma_{id}(t) \right] dt + \sigma_i(t)^\top \, dW^d(t) \end{split} \tag{1.49}$$

with  $\Sigma_{id}(t) = \sigma_i(t)^{\top} \sigma_d(t)$ . Thus, when we change measures from  $P_{\beta}$  to  $P_{S_d}$ , an additional term appears in the drift of  $S_i$  reflecting the instantaneous covariance between  $S_i$  and the numeraire asset  $S_d$ .

The distinguishing feature of this change of measure is that it makes the ratios  $S_i(t)/S_d(t)$  martingales. This is already implicit in (1.46) because each  $S_i(t)$  is an attainable price process and thus a candidate for  $V(t)$ . To make the martingale property more explicit, we may use (1.47) for  $S_i$  and  $S_d$  and then simplify using  $(1.48)$  to write the ratio as

$$\frac{S_i(t)}{S_d(t)} = \frac{S_i(0)}{S_d(0)} \exp\left(-\frac{1}{2} \int_0^t \|\sigma_i(u) - \sigma_d(u)\|^2 \, du + \int_0^t [\sigma_i(u) - \sigma_d(u)]^\top \, dW^d(u)\right).$$

This reveals that  $S_i(t)/S_d(t)$  is an exponential martingale (see (B.21) in Appendix B) under  $P_{S_d}$  because  $W^d$  is a standard Brownian motion under that measure. This also provides a convenient way of thinking about asset price dynamics under the measure  $P_{S_d}$ : under this measure, the drifts of the asset prices make the ratios  $S_i(t)/S_d(t)$  martingales.

### 1.2.4 The Market Price of Risk

In this section we conclude our overview of the principles underlying derivatives pricing by returning to the idea of a stochastic discount factor introduced in Section  $1.2.1$  and further developing its connections with the absence of arbitrage, market completeness, and dynamic hedging. Though not stricly necessary for the application of Monte Carlo (which is based on the pricing relations  $(1.39)$  and  $(1.45)$ ), these ideas are important parts of the underlying theory.

We proceed by considering the dynamics of a stochastic discount factor  $Z(t)$  as defined in Section 1.2.1. Just as the likelihood ratio process  $(dP_{\beta}/dP_{o})_{t}$ defined in (1.37) is a positive martingale under  $P_o$ , its reciprocal  $(dP_o/dP_\beta)_t$ is a positive martingale under  $P_{\beta}$ ; this is a general change of measure identity and is not specific to this context. From (1.37) we find that  $(dP_o/dP_\beta)_t =$  $Z(t)/\beta(t)$  and thus that  $e^{-rt}Z(t)$  is a positive martingale under  $P_{\beta}$ . (For simplicity, we assume the short rate r is constant.) This suggests that  $Z(t)$ should evolve according to an SDE of the form

$$\frac{dZ(t)}{Z(t)} = r dt + \nu(t)^{\top} dW(t), \qquad (1.50)$$

for some process  $\nu$ , with W continuing to be a standard Brownian motion under  $P_{\beta}$ . Indeed, under appropriate conditions, the martingale representation theorem (Appendix B) ensures that the dynamics of  $Z$  must have this form.

Equation  $(1.50)$  imposes a restriction on the dynamics of the underlying assets  $S_i$  under the objective probability measure  $P_o$ . The dynamics of the  $S_i$ under the risk-neutral measure are given in (1.41). Switching from  $P_{\beta}$  back to  $P_o$  is formally equivalent to applying a change of numeraire from  $\beta(t)$  to  $Z(t)$ . The process  $Z(t)$  may not correspond to an asset price, but this has no effect on the mechanics of the change of measure.

We saw in the previous section that switching from  $P_{\beta}$  to  $P_{S_d}$  had the effect of adding a drift to W; more precisely, the process  $W^d$  defined in (1.48) becomes a standard Brownian motion under  $P_{S_d}$ . We saw in (1.49) that this has the effect of adding a term to the drifts of the asset prices as viewed under  $P_{S_d}$ . By following exactly the same steps, we recognize that the likelihood ratio

$$\left(\frac{dP_o}{dP_{\beta}}\right)_t = e^{-rt}Z(t) = \exp\left(\int_0^t -\frac{1}{2} \|\nu(u)\|^2 \, du + \int_0^t \nu(u)^\top \, dW(u)\right)$$

implies (through the Girsanov Theorem) that

$$dW^o = -\nu(t) \, dt + dW(t)$$

defines a standard Brownian motion under  $P_o$  and that the asset price dynamics can be expressed as

$$\begin{split} \frac{dS_i(t)}{S_i(t)} &= r \, dt + \sigma_i(t)^\top \, dW(t) \\ &= r \, dt + \sigma_i(t)^\top \left[ dW^o(t) + \nu(t) \, dt \right] \\ &= \left[ r + \nu(t)^\top \sigma_i(t) \right] dt + \sigma_i(t)^\top \, dW^o(t). \end{split} \tag{1.51}$$

Comparing this with our original specification in  $(1.23)$ , we find that the existence of a stochastic discount factor implies that the drifts must have the  $\text{form}$ 

$$\mu_i(t) = r + \nu(t)^\top \sigma_i(t). \tag{1.52}$$

This representation suggests an interpretation of  $\nu$  as a risk premium. The components of  $\nu$  determine the amount by which the drift of a risky asset will exceed the risk-free rate r. In the case of a scalar  $W^o$  and  $\nu$ , from the equation  $\mu_i = r + \nu \sigma_i$  we see that the excess return  $\mu_i - r$  generated by a risky asset is proportional to its volatility  $\sigma_i$ , with  $\nu$  the constant of proportionality. In this sense,  $\nu$  is the *market price of risk*; it measures the excess return demanded by investors per unit of risk. In the vector case, each component  $\nu_i$  may similarly be interpreted as the market price of risk associated with the  $j$ th risk factor — the jth component of  $W^o$ . It should also be clear that had we assumed the drifts in  $(1.23)$  to have the form in  $(1.52)$  (for some  $\nu$ ) from the outset, we could have defined a stochastic discount factor Z from  $\nu$  and (1.50). Thus, the existence of a stochastic discount factor and a market price of risk vector are essentially equivalent.

An alternative line of argument (which we mention but do not develop) derives the market price of risk in a more fundamental way as the aggregate effect of the individual investment and consumption decisions of agents in an economy. Throughout this section, we have taken the dynamics of the asset prices to be specified exogenously. In a more general formulation, asset prices result from balancing supply and demand among agents who trade to optimize their lifetime investment and consumption; the market price of risk is then determined through the risk aversion of the agents as reflected in their utility for wealth and consumption. Thus, in a general equilibrium model of this type, the market price of risk emerges as a consequence of investor preferences and not just as a constraint to preclude arbitrage. For more on this approach, see Chapter 10 of Duffie  $[98]$ .

37

## Incomplete Markets

The economic foundation of the market price of risk and the closely related concept of a stochastic discount factor is particularly important in an  $in$ *complete* market. A *complete* market is one in which all risks that affect asset prices can be perfectly hedged. Any new asset (such as an option on one of the existing assets) introduced into a complete market is redundant in the sense that it can be replicated by trading in the other assets. Derivative prices are thus determined by the absence of arbitrage. In an incomplete market, some risks cannot be perfectly hedged and it is therefore possible to introduce genuinely new assets that cannot be replicated by trading in existing assets. In this case, the absence of arbitrage constrains the price of a derivative security but may not determine it uniquely.

For example, market incompleteness may arise because there are fewer traded assets than driving Brownian motions. In this case, there may be infinitely many solutions to  $(1.52)$ , and thus infinitely many choices of stochastic discount factor  $Z(t)$  for which  $S_i(t)/Z(t)$  will be martingales,  $i = 1, \ldots, d$ . Similarly, there are infinitely many possible risk-neutral measures, meaning measures equivalent to the original one under which  $e^{-rt}S_i(t)$  are martingales. As a consequence of these indeterminacies, the price of a new security introduced into the market may not be uniquely determined by the prices of existing assets. The machinery of derivatives pricing is largely inapplicable in an incomplete market.

ű

Market incompleteness can arise in various ways; a few examples should serve to illustrate this. Some assets are not traded, making them inaccessible for hedging. How would one eliminate the risk from an option on a privately held business, a parcel of land, or a work of art? Some sources of risk may not correspond to asset prices at all  $-$  think of hedging a weather derivative with a payoff tied to rainfall or temperature. Jumps in asset prices and stochastic volatility can often render a market model incomplete by introducing risks that cannot be eliminated through trading in other assets. In such cases, pricing derivatives usually entails making some assumptions, sometimes only implicitly, about the market price for bearing unhedgeable risks.
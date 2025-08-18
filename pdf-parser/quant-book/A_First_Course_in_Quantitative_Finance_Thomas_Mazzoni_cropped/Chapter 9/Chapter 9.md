✖

# **9 Financial Econcomics**

In a nutshell, financial economics tries to explain how markets and prices of risky investments evolve. This is an exceedingly difficult task, because expected returns are usually orders of magnitude smaller than the volatility of the investment under consideration. Matters become even worse considering that a serious economic theory of financial returns should also explain the existence and the magnitude of a risk-free interest rate. Attempts to meet these requirements result in some of the most famous puzzles in economic theory, like the equity premium puzzle or the volatility puzzle.

# **9.1 The Rational Valuation Principle**

An important concept in analyzing the evolution of the fair price *S<sup>t</sup>* of a risky security is the fundamental value *V<sup>t</sup>* . Let's focus on an ordinary stock for the moment. In this case, the fundamental value is determined by characteristics of the company like its size, market position, organization, financial structure, and others. The change in the fair price *St*+<sup>1</sup> − *S<sup>t</sup>* from period *t* to period *t* + 1 is due to immediate changes in the fundamental value *Vt*+<sup>1</sup> − *V<sup>t</sup>* , but also due to dividend payments *Dt*+1. We used uppercase letters here, to emphasize that both the fundamental value, as well as the dividend payments generally are random variables.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

The rational expectation hypothesis states that the best prediction of the future value of an arbitrary quantity is the expected value of that quantity, conditional on the present available information. Therefore, the best prediction for the total return *Rt*+<sup>1</sup> is given by the rational valuation formula (RVF; see Cuthbertson and Nitzsche, 2004, p. 245)

$$E[R_{t+1}|\mathcal{F}_t] = \frac{E[V_{t+1}|\mathcal{F}_t] - V_t + E[D_{t+1}|\mathcal{F}_t]}{V_t}.$$
(9.1)

Maybe the most naive assumption one can make is that investors require a fixed expected return *E*[*Rt*+1|F*t*] = µ, to compensate them for the risk they take when investing in the security. Using this assumption in (9.1), one obtains after a few algebraic manipulations

.

$$V_{t} = \delta E[V_{t+1} + D_{t+1}|\mathcal{F}_{t}], \tag{9.2}$$

with the discounting factor δ = 1 1+µ

**Quick calculation 9.1** Verify Equation (9.2).

To determine what  $V_t$  is, let's iterate (9.2) one period into the future

$$V_{t+1} = \delta E[V_{t+2} + D_{t+2} | \mathcal{F}_{t+1}]. \tag{9.3}$$

By the law of iterated expectations, we have

$$E[V_{t+1}|\mathcal{F}_t] = E\left[\delta E[V_{t+2} + D_{t+2}|\mathcal{F}_{t+1}]\big|\mathcal{F}_t\right]$$
  
=  $\delta E[V_{t+2} + D_{t+2}|\mathcal{F}_t].$  (9.4)

That is, the best prediction of tomorrow's prediction is today's prediction of the respective value. Plugging  $(9.4)$  into  $(9.2)$ , one obtains

$$V_{t} = \delta E[D_{t+1} + \delta(D_{t+2} + V_{t+2})|\mathcal{F}_{t}] \tag{9.5}$$

where we have rearranged the Ds and Vs. The  $\delta$ s can go in or outside the expectation because they are just numbers. We can apply the same argument  $T-1$  times to obtain

$$V_{t} = \sum_{k=1}^{T} \delta^{k} E[D_{t+k}|\mathcal{F}_{t}] + \delta^{T} E[V_{t+T}|\mathcal{F}_{t}]. \tag{9.6}$$

Quick calculation 9.2 Convince yourself that the last argument is indeed true.

Another assumption usually made at this point is that the so-called transversality condition is satisfied. It states that the fundamental value remains finite for all times. If this is true, and we let  $T \rightarrow \infty$ , then the last term on the right hand side of (9.6) vanishes, and we obtain for the fundamental value at time  $t$ 

$$V_t = \sum_{k=1}^{\infty} \delta^k E[D_{t+k}|\mathcal{F}_t]. \tag{9.7}$$

If the price of the stock  $S_t$  at time t deviates from the fundamental value  $V_t$ , then an investor can take the opposite position to participate in the difference of future income streams and make a profit. Thus, in equilibrium we must have  $S_t = V_t$  or

$$S_t = \sum_{k=1}^{\infty} \delta^k E[D_{t+k}|\mathcal{F}_t],\tag{9.8}$$

respectively. The rational valuation formula  $(9.8)$  is of little practical use, because we have not specified a stochastic process for  $D_t$  yet. So at this point we can conclude nothing more than that the observed stock price should represent a series of discounted future cash flows.

Now let's make a simple educated guess: Assume that the management wants the dividend stream to be as smooth as possible, in order to avoid unnecessary fluctuations in the stock price. Of course this is not always possible, therefore we assume that the dividend process follows a simple random walk

$$D_t = D_{t-1} + \epsilon_t,\tag{9.9}$$

where  $\epsilon_l$  is a zero expectation random error with variance  $\sigma_{\epsilon}^2$ . This means  $E[D_{l+k}|\mathcal{F}_l]$  =  $D_t$  for all  $k \ge 0$ . Using this relation in (9.8) yields the RVF for constant expected dividends

$$S_t = \sum_{k=1}^{\infty} \delta^k D_t = \frac{\delta}{1-\delta} D_t = \frac{D_t}{\mu}.$$
(9.10)

**Quick calculation 9.3** Verify the last equality in  $(9.10)$ .

In actuarial science  $(9.10)$  is called a perpetuity. You might wonder how the second equality was established. The sum in  $(9.10)$  is called an infinite geometric series. Let's first try to calculate a finite version of it. As strange as it might sound, the worst thing you can try in calculating such a series, is to add it up term by term. Let's instead multiply with  $\delta^{-1} - 1$ 

$$(\delta^{-1} - 1) \sum_{k=1}^{K} \delta^{k} = 1 + \delta + \delta^{2} + \dots + \delta^{K-1}$$
$$- \delta - \delta^{2} - \dots - \delta^{K-1} - \delta^{K}$$
$$= 1 - \delta^{K}.$$
(9.11)

You see how nicely the terms cancel? Dividing both sides by  $\delta^{-1} - 1$ , we get

$$\sum_{k=1}^{K} \delta^{k} = \frac{1 - \delta^{K}}{\delta^{-1} - 1} = \delta \frac{1 - \delta^{K}}{1 - \delta},\tag{9.12}$$

and we are nearly done. Remember that  $\delta = \frac{1}{1+\mu} < 1$ , as long as  $\mu > 0$ . That is not much of an assumption, because if the expected return on the stock was negative, we would keep our money. Thus, in the limit  $K \to \infty$ ,  $\delta^K$  tends towards zero, and we get

$$\sum_{k=1}^{\infty} \delta^k = \lim_{K \to \infty} \sum_{k=1}^{K} \delta^k = \frac{\delta}{1-\delta}.$$
(9.13)

There are two interesting consequences of  $(9.10)$ . The first is that the dividend-price ratio

$$\frac{D_t}{S_t} = \mu \tag{9.14}$$

is constant and equal to the required expected return the investor needs to compensate the risk. The second is that in order for this ratio to remain valid, a 1% change in dividends has to be matched exactly by a 1% change in the stock price in the same direction. In other words, dividends and stock prices have to have exactly the same volatility. We can obviously not expect this to be true, which means we expect  $\mu$  not really to be a constant. In reality, dividends and stock prices move roughly proportional to each other at best over extended periods of time. In the short and medium term,

stock prices are far more volatile than dividends. In fact, they seem to be excessively volatile as pointed out by Shiller (1981).

Another thought might occur to you; stock prices are usually assumed to exhibit an exponential growth. If (9.14) is approximately true in the long term, doesn't that mean that dividends should grow, too? This is exactly the case and pursuing this avenue leads us to Gordon's growth model (Gordon, 1959). Assume that dividends follow an AR(1)-process

$$D_t = (1+g)D_{t-1} + \epsilon_t, \tag{9.15}$$

where *g* is the dividend growth rate, and ϵ*<sup>t</sup>* is again a zero mean random error, as in (9.9). Even though *g* is also introduced as a deterministic and constant parameter, we expect this property not to hold exactly in reality. Calculating the conditional expectation of the dividend now yields

$$E[D_{t+k}|\mathcal{F}_t] = (1+g)^k D_t, \tag{9.16}$$

for all *k* ≥ 0. Using this equation in the rational valuation formula (9.8), yields the RVF for a constant growth rate of dividends

$$S_t = \sum_{k=1}^{\infty} \delta^k (1+g)^k D_t = \frac{1+g}{\mu - g} D_t,$$
(9.17)

as long as µ > *g*.

**Quick calculation 9.4** Verify the last equality in (9.17).

The condition µ > *g* is a necessary requirement for the infinite geometric series in (9.17) to converge, but it is otherwise quite ad hoc.

**Quick calculation 9.5** Can you see why this condition is necessary?

Nevertheless, empirical findings indicate that the dividend growth rate is on average indeed much smaller than the growth rate of stock prices.

To see how this can help explain the excessive stock price volatility, let's look at an example.

**Example 9.1**

Assume that the required expected return is µ = 5% and the growth rate of dividends is estimated by the investors to be *g* = 3%. Now think of bad news about the company coming in, and investors reducing their dividend growth estimation to *g* = 2%. What happens to the RVF-price of the stock?

### Solution

Before the bad news, investors calculated the RVF-price for one stock of the company as

$$S_t = \frac{103\%}{2\%} D_t = 51.5 D_t.$$

After the revision of the dividend growth estimation, the new price calculated by the investors is

$$S_t = \frac{102\%}{3\%}D_t = 34D_t.$$

Dividing the latter by the former, we see that the stock price has dropped by roughly 34%. This is a considerable amount of extra volatility. ........................................................................................................................

We will return to volatility issues later, but first study another phenomenon observed in stock markets, which is held responsible for occasional market crashes.

# **9.2 Stock Price Bubbles**

You may have listened every now and then to financial economists discussing whether a bubble is currently driving the market or not. More puzzling, if you did not manage to switch to another program in time, you may have witnessed the further discussion of whether or not such a bubble can be detected. This may surprise you, because we have established a theory that connects the rational stock price to the expected dividend stream, which is estimated in a unique way, based on the present available information. There seems to be no way for another phantom process to enter the calculation. Assume for a moment that such a process might exist, or formally

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$S_t = V_t + B_t,\t\t(9.18)$$

where *B<sup>t</sup>* > 0 (almost surely) is the mysterious bubble contribution, and ask: Can such a process remain undetected? From (9.2) we know that

$$V_t = \delta E[V_{t+1} + D_{t+1} | \mathcal{F}_t]. \tag{9.19}$$

Leading (9.18) one period into the future and plugging into (9.19), one obtains

$$V_t = \delta E[S_{t+1} - B_{t+1} + D_{t+1} | \mathcal{F}_t]. \tag{9.20}$$

Using this result back in (9.18) we get the most illuminating answer

$$S_t = \delta E[S_{t+1} + D_{t+1} | \mathcal{F}_t] + B_t - \delta E[B_{t+1} | \mathcal{F}_t]. \tag{9.21}$$

Imagine now the bubble term is a discounted martingale

$$B_t = \delta^k E[B_{t+k}|\mathcal{F}_t],\tag{9.22}$$

for  $k \ge 0$ , then only the first term on the right hand side of (9.21) would survive

$$S_t = \delta E[S_{t+1} + D_{t+1} | \mathcal{F}_t]. \tag{9.23}$$

Under rational valuation, you could not distinguish the process  $S_t$  from the process  $V_t$ and thus you would not be able to tell, if there is a bubble present or not, at least at the beginning. In order for the martingale property (9.22) to hold, the bubble has to have dynamics of the form

$$B_t = (1 + \mu)B_{t-1} + \epsilon_t, \tag{9.24}$$

where  $\epsilon_t$  is again a zero mean random error. In the limit  $t \to \infty$ ,  $B_t$  tends to infinity with probability one, and because the stock price is the sum of the fundamental value and the bubble,  $S_t$  also tends to infinity, thereby violating the transversality condition. An easy way to see this is to assume that dividends follow a random walk, which means they have no growth rate. If at time t a bubble  $B_t$  is present, then the expected stock price at a later time  $t + k$  is

$$E[S_{t+k}|\mathcal{F}_t] = \frac{D_t}{\mu} + (1+\mu)^k B_t.$$
 (9.25)

That means that the bubble becomes an increasing part of the stock price. Even if there is a positive growth rate of dividends, it is easy to see that the bubble grows faster, because the growth of the fundamental value is connected to expected dividend growth g, whereas the bubble grows with the full expected rate of return  $\mu > g$ .

**Quick calculation 9.6** Use  $(9.15)$  and  $(9.17)$  to establish this argument formally.

Observe that the occurrence of the bubble in  $(9.18)$ , even though its persistence under the rational valuation principle can be justified, is not explained by the theory. That is why Cuthbertson and Nitzsche (2004, p. 404) call such a bubble a "deus ex machina."

Furthermore,  $(9.25)$  makes clear that over an extended period of time, the price of the stock has to deviate significantly from its fundamental value. You would expect that at some point investors become suspicious, even if they cannot calculate the true fundamental value, because they do not know the dividend driving process with certainty. If this is the case, the bubble specification  $(9.22)$  is incomplete, because it does not allow for the bubble to burst. This can be remedied by defining the following bubble process (Blanchard, 1979)

$$B_{t} = \begin{cases} \frac{1+\mu}{\pi} B_{t-1} & \text{with probability } \pi \\ 0 & \text{with probability } 1-\pi. \end{cases}$$
(9.26)

**Ouick calculation 9.7** Verify that this process satisfies the martingale condition (9.22).

There is still no explanation for the formation of a bubble, but at least it can burst now. If we link intuitively the burst probability  $1 - \pi$  to the deviation of the stock price from

the estimated fundamental value, we can conclude that the bubble will burst eventually, before the stock price grows to infinity. But if we know that the bubble will burst in the future, how is it that it does not burst immediately? After all, the stock price reflects the discounted value of future payments. Obviously, the investment horizon of most agents is short enough to assume that the bubble does not burst until they sell the stock again, so that the bubble really adds value in form of intertemporal price differences.

The bubbles we have analyzed so far are completely exogenous. The problem with that is that we cannot get a handle on a creation mechanism. Froot and Obstfeld (1991) suggested another type of bubble, an intrinsic bubble, immediately linked to the dividend driving process by

$$B_t = cD_t^{\lambda}.\tag{9.27}$$

The authors do not model the dividend driving process directly, but its logarithm. This is a smart thing to do, because the dividend process is guaranteed to stay nonnegative this way. In the following, the original notation of Froot and Obstfeld (1991) is slightly modified, in order to keep alignment with the formal framework established so far. Assume, the dividend process is of the form

$$\log D_t = \log D_{t-1} + g + \epsilon_t, \tag{9.28}$$

with ϵ*<sup>t</sup>* ∼ *N*(0, σ<sup>2</sup> ϵ ). Of course again, log is the natural logarithm with respect to the basis *e*. Exponentiating both sides of (9.28) indicates that

$$D_t = D_{t-1} e^{g + \epsilon_t} \tag{9.29}$$

holds. This means, the fluctuations introduced by the random error ϵ*<sup>t</sup>* are not absolute in magnitude, but relatively scaled by the size of *Dt*−1. That seems to be a good thing too, because fluctuations can now be specified relatively as a percentage of the respective quantity. The random variable *e* ϵ*t* is logarithmic normally distributed.

We will often refer to the expectation of a log-normal distributed random variable, so let's discuss that issue a little bit. First of all observe that for an arbitrary random variable *X* ∼ *N*(µ, σ<sup>2</sup> ), the following relation always holds

$$E[e^{X}] = E[e^{\mu + Y}] = e^{\mu}E[e^{Y}], \tag{9.30}$$

with *Y* ∼ *N*(0, σ<sup>2</sup> ). Obviously, we only have to address the case of zero mean random variables, because the mean itself multiplies out of the expectation somehow. Next, *Taylor*-expand *e <sup>Y</sup>* to obtain the series representation

$$E[e^{Y}] = \sum_{k=0}^{\infty} \frac{E[Y^{k}]}{k!}.$$
(9.31)

Now remember that there is a recursive relation between the moments of a normally distributed random variable, (2.31) on page 19, which states that all odd moments vanish, and all even moments of order *k* are (*k* − 1)!!σ *k* . Using this relation in (9.31) the sum can be written as

$$E[e^{Y}] = \sum_{n=0}^{\infty} \frac{(2n-1)!!}{(2n)!} \sigma^{2n}, \tag{9.32}$$

with  $k = 2n$ . Observe that the factorial term in (9.32) can be reexpressed as

$$\frac{(2n-1)!!}{(2n)!} = \frac{1}{(2n)!!} = \frac{1}{2^n n!}.$$
(9.33)

**Quick calculation 9.8** Confirm the factorial relations established above.

Thus, we finally obtain the desired expectation value

$$E[e^{Y}] = \sum_{n=0}^{\infty} \frac{1}{n!} \left(\frac{\sigma^2}{2}\right)^n = e^{\frac{\sigma^2}{2}}.$$
 (9.34)

**Quick calculation 9.9** What is the expectation value of  $e^{X}$ ?

Returning to the bubble specification (9.27), Froot and Obstfeld (1991) chose the parameter  $\lambda$  to be the positive root of the equation

$$\lambda^2 \frac{\sigma_\epsilon^2}{2} + \lambda g + \log \delta = 0,\t(9.35)$$

whereas c is a completely free parameter. This choice of  $\lambda$  ensures that the martingale condition  $(9.22)$  is satisfied. In detail, we have

$$\delta E[B_{t+1}|\mathcal{F}_t] = \delta E[cD_{t+1}^{\lambda}|\mathcal{F}_t]\n$$

$$\n= \delta E[cD_t^{\lambda} e^{\lambda g + \lambda \epsilon_{t+1}}|\mathcal{F}_t]\n$$

$$\n= \delta B_t e^{\lambda g + \lambda^2 \frac{\sigma_e^2}{2}}\n$$

$$\n= B_{t*}\n$$
(9.36)

where we have used  $(9.35)$  in the last step.

**Quick calculation 9.10** Can you see why  $E[e^{\lambda \epsilon_{t+1}} | \mathcal{F}_t] = e^{\lambda^2 \frac{\sigma_e^2}{2}}$  in (9.36)?

Putting all the pieces together, the rational valuation formula, including an intrinsic bubble is

$$S_t = V_t + B_t = \kappa D_t + c D_t^{\lambda},\tag{9.37}$$

with

$$\kappa = \frac{e^{g + \frac{\sigma_{\epsilon}^{2}}{2}}}{1 + \mu - e^{g + \frac{\sigma_{\epsilon}^{2}}{2}}} \approx \frac{1 + g + \frac{\sigma_{\epsilon}^{2}}{2}}{\mu - g - \frac{\sigma_{\epsilon}^{2}}{2}}.$$
(9.38)

To see this, remember that the fundamental value of the stock, provided the transversality condition holds, is

$$V_{t} = \sum_{k=1}^{\infty} \delta^{k} E[D_{t+k} | \mathcal{F}_{t}] = \sum_{k=1}^{\infty} \delta^{k} e^{k\left(g + \frac{\sigma_{e}^{2}}{2}\right)} D_{t}, \tag{9.39}$$

and apply the result for the geometric series.

163

**Quick calculation 9.11** Convince yourself that the result (9.38) is correct.

The approximation in (9.38) holds for small µ, *g*, and σ 2 ϵ , and reveals a close connection to Gordon's growth model. For σ 2 <sup>ϵ</sup> = 0, we obtain the already known result. Observe that the parameter *c* is completely free. If we think of it informally as a quantity that may change over time, in particular from zero to a positive value, we at least have a clue of how a bubble creation mechanism might work.

# **9.3 Shiller's Volatility Puzzle**

By the time Shiller presented his ingenious argument, econometric indications of stock price excess volatility had already been discussed by LeRoy and Porter (1981). What he actually recognized is that there is a way to calculate a perfect foresight price process and subsequently compare this one with the price process under rational expectation. How does such a thing work? Assume you know the stock price at any terminal date *T* and you have data on dividends over an extended period of time *t* = 1, . . . ,*T*. Then, according to the rational valuation formula (RVF), the stock price calculated at time *t* is

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$S_t = \sum_{k=1}^{T-t} \delta^k E[D_{t+k}|\mathcal{F}_t] + \delta^{T-t} E[S_T|\mathcal{F}_t]. \tag{9.40}$$

But because we know the dividends since period *t* = 1 and the terminal stock price, we can calculate the price *S* ∗ *t* an agent would have computed at any time *t* = 0, . . . ,*T*, if she had perfect foresight of the future payments

$$S_t^* = \sum_{k=1}^{T-t} \delta^k D_{t+k} + \delta^{T-t} S_T.$$
 (9.41)

Neglecting the most of the time heavily discounted differences *S<sup>T</sup>* − *E*[*ST*|F*t*], we can write the residual error between the perfect foresight price and the RVF-price as

$$S_t^* - S_t = \sum_{k=1}^{T-t} \delta^k v_{t+k},$$
(9.42)

where ν*t*+*<sup>k</sup>* = *Dt*+*<sup>k</sup>* − *E*[*Dt*+*k*|F*t*] is the innovation of the dividend process. The problem with this expression is that *S<sup>t</sup>* is usually not a stationary process and thus, moments like the expectation value for example depend on time.

What Shiller (1981) essentially did to fix this problem was to introduce a particular numéraire (detrending factor) that makes the dividend process a martingale. In Gordon's growth model, the dividend process is given by

$$D_t = (1+g)D_{t-1} + \epsilon_t. \tag{9.43}$$

Shiller defined a new detrended process

$$P_t = \sum_{k=1}^{T-t} \delta^k E\left[\frac{D_{t+k}}{(1+g)^{t+k-T}} \middle| \mathcal{F}_t\right] + \delta^{T-t} E[P_T | \mathcal{F}_t],\tag{9.44}$$

where  $P_T = S_T$ , because the appropriate numéraire to detrend a time T quantity is one. Under the dynamics  $(9.43)$ , we immediately conclude that the detrended dividend process is a martingale

$$\frac{D_t}{(1+g)^{t-T}} = E\left[\frac{D_{t+k}}{(1+g)^{t+k-T}} \Big| \mathcal{F}_t\right].$$
(9.45)

**Quick calculation 9.12** Convince yourself that the last statement is true.

To see that  $P_t$  is indeed a process with approximately time independent mean, let the terminal date  $T$  grow large compared to the current time t. Then, first of all, we can neglect the last term on the right hand side of  $(9.44)$ , because of heavy discounting. Next, we can treat the geometric series as an approximately infinite series and use the martingale condition  $(9.45)$  to obtain

$$P_t \approx (1+g)^{T-t} D_t \cdot \frac{\delta}{1-\delta} = \frac{E[D_T|\mathcal{F}_t]}{\mu}.$$
(9.46)

Using the law of iterated expectations, we obtain

$$E[P_t] \approx \frac{E[D_T]}{\mu},\tag{9.47}$$

which is a constant for every  $t$ .

In complete analogy, Shiller defined the detrended perfect foresight price process  $P_{t}^{*}$ , and after subtracting one process from the other, one obtains

$$P_t^* - P_t = \sum_{k=1}^{T-t} \delta^k \omega_{t+k} = \eta_t,$$
(9.48)

where

$$\omega_{t+k} = \frac{D_{t+k}}{(1+g)^{t+k-T}} - E\left[\frac{D_{t+k}}{(1+g)^{t+k-T}} \Big| \mathcal{F}_t\right] \tag{9.49}$$

is the innovation of the detrended dividend process. The zero mean random errors  $\epsilon_t$  in the dividend process (9.43) were assumed independent of  $D_t$ . Thus, the random error  $\eta_t$ , despite a possibly complicated structure, is still an independent innovation. Rearranging  $(9.48)$  and taking variances yields

$$\text{Var}[P_t^*] = \text{Var}[P_t] + \text{Var}[\eta_t], \tag{9.50}$$

from which we can conclude that  $\text{Var}[P_t] > \text{Var}[P_t]$  has to hold. Figure 9.1 is a reproduction of Shiller's famous illustration, published in 1981 in *The American Economic Review.* He analyzed data for the Standard & Poor's and for the Dow Jones index over

![](_page_10_Figure_1.jpeg)

**Fig. 9.1** Detrended processes for Standard & Poor's Composite Stock Price Index (left) and Dow Jones Industrial Average (right) – Figures are reproduced from (Shiller, 1981) with permission of the American Economic Association

an extended period of time. Dividends were assigned according to the weight contribution of the corresponding stocks, contained in the respective index. It is immediately evident that the RVF-process *P<sup>t</sup>* is far more volatile than the perfect foresight price process *P* ∗ *t* . It seems that our analysis finally leads to a dead end.

# **9.4 Stochastic Discount Factor Models**

To understand stochastic discount factor (SDF) models, we have to go back to our discussion of utility functionals and state prices in Chapter 5. We found that a rational agent values consumption in a random future state of the world ω with the marginal rate of substitution (MRS) compared to the present consumption level

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\psi_{\omega} = \frac{\partial U/\partial c_{\omega}}{\partial U/\partial c_{0}} = -\text{MRS.}$$
(9.51)

The state price ψ<sup>ω</sup> reflects how much present consumption has to be sacrificed in order to extend the consumption in state ω by one unit, while keeping the overall utility level constant. Most of the time, a time separable *von Neumann–Morgenstern*-utility functional is chosen

$$U[C_t] = u(c_0) + e^{-\rho t} \sum_{\omega=1}^{\Omega} u(c_{t,\omega}) p_{\omega}, \qquad (9.52)$$

where ρ governs the tendency for intertemporal substitution. For large ρ, the agent is very impatient and discounts future utility very heavily. Clearly, for a time separable utility functional of the type (9.52), one obtains the state price

$$\psi_{\omega} = e^{-\rho t} \frac{u'(c_{t,\omega})}{u'(c_0)} p_{\omega},\tag{9.53}$$

where the prime indicates the derivative of the utility function *u*(*c*) with respect to its argument, and *p*<sup>ω</sup> is the probability for state ω to occur. Because for simplicity we

consider only two periods, all expectations are with respect to the information F0, and thus we can omit the conditioning argument.

A risky security *S* is a device to shift consumption from one period to another. If we assume that changes in the fundamental value and dividend payments are incorporated in the price of the security at all times, the fair price from today's perspective should equal

$$S_{0} = \langle \psi | S_{t} \rangle = \sum_{\omega=1}^{\Omega} e^{-\rho t} \frac{u'(c_{t,\omega})}{u'(c_{0})} S_{t,\omega} p_{\omega} = E\bigg[e^{-\rho t} \frac{u'(C_{t})}{u'(c_{0})} S_{t}\bigg]. \tag{9.54}$$

To simplify matters, define a new random variable

$$M_t = e^{-\rho t} \frac{u'(C_t)}{u'(c_0)},$$
(9.55)

called the stochastic discount factor. Note that *M<sup>t</sup>* is random, because the future consumption *C<sup>t</sup>* is not known initially. Thus, (9.54) simplifies to

$$S_0 = E[M_t S_t]. \tag{9.56}$$

We cannot say much about *M<sup>t</sup>* yet, because we have not specified a particular utility function *u*(*c*). But let's see if we can derive some general consequences of the SDFprinciple.

First of all, define the gross return of the risky security over the period *t* as

$$R_S^* = \frac{S_t}{S_0} = 1 + R_S,\tag{9.57}$$

and divide both sides of (9.56) by *S*<sup>0</sup> to obtain

$$1 = E[M_t R_S^*]. \t\t(9.58)$$

Now observe that the stochastic discount factor is the same random variable for all securities, because it is a function of time *t* consumption only. That means, we can plug every gross return into (9.58) and it nevertheless has to be true. Let's do the exercise with the continuous risk-free gross return *R* ∗ 0 = *e rt* ,

$$1 = E[M_t R_0^*] = E[M_t]e^{rt}.$$
(9.59)

Simply rearranging this expression yields an economic explanation of the risk-free discounting factor

$$\frac{1}{R_0^*} = e^{-rt} = E[M_t]. \tag{9.60}$$

That looks like tremendous progress, and it is getting even better. Subtract (9.60) from (9.58) to obtain

$$1 - \frac{1}{R_0^*} = E[M_t(R_S^* - 1)] = E[M_t R_S]. \tag{9.61}$$

**Quick calculation 9.13** Verify the last equation.

Now remember from elementary statistics, that the covariance of two random variables *X* and *Y* can be written as Cov[*X*, *Y*] = *E*[*XY*] − *E*[*X*]*E*[*Y*]. Applying this trick to the right hand side of (9.61) yields

$$1 - \frac{1}{R_0^*} = \text{Cov}[M_t, R_S] + E[M_t]E[R_S]. \tag{9.62}$$

Multiplying both sides by *R* ∗ 0 and rearranging yields

$$E[R_S] = R_0 - \frac{\text{Cov}[M_t, R_S]}{E[M_t]}.$$
(9.63)

**Quick calculation 9.14** Confirm that (9.63) is indeed true.

The second term on the right hand side of (9.63) is the risk premium. Don't get fooled by the minus sign. The stochastic discount factor involves marginal utility; see the definition (9.55). If an agent is risk averse, marginal utility decreases with increasing consumption levels. A positive return of security *S* means additional time *t* consumption, and thus less marginal utility. Or in other words, we should expect the covariance between *M<sup>t</sup>* and *R<sup>S</sup>* to be negative. The expectation of *M<sup>t</sup>* on the other hand is most certainly positive, because it was already identified as the risk-free discounting factor. The upshot is that the risk premium for an ordinary security is positive, which means we are entitled to expect a higher return than the risk-free rate when investing in a stock. Are there other securities, paying high returns in states with high marginal utility and an expected return below the risk-free rate? Yes there are, but we are used to calling them insurance contracts.

Let's finally see, how the stochastic discount factor framework fits into the rational valuation principle. Define the gross return of the fundamental value of an arbitrary stock as

$$R_{t+1}^* = \frac{V_{t+1} + D_{t+1}}{V_t}.$$
(9.64)

Using the conditional relation *E* [*Mt*+1*R* ∗ *t*+1 |F*t* ] = 1, we can write the time *t* value as

$$V_t = E[M_{t+1}(V_{t+1} + D_{t+1})|\mathcal{F}_t]. \tag{9.65}$$

As before, we assume the transversality condition to hold, and iterate (9.65) into the future to obtain

$$V_t = \sum_{k=1}^{\infty} E\left[\prod_{n=1}^k M_{t+n} D_{t+k} \middle| \mathcal{F}_t\right].$$
(9.66)

**Ouick calculation 9.15** Iterate (9.65) one period to confirm the construction.

Finally applying our covariance trick, and recalling that under rational valuation the fundamental value has to equal the price of the stock, we obtain

$$S_{t} = \sum_{k=1}^{\infty} E\left[\prod_{n=1}^{k} M_{t+n} \middle| \mathcal{F}_{t}\right] E[D_{t+k}|\mathcal{F}_{t}] + \sum_{k=1}^{\infty} \text{Cov}\left[\prod_{n=1}^{k} M_{t+n}, D_{t+k} \middle| \mathcal{F}_{t}\right]. \tag{9.67}$$

**Quick calculation 9.16** Convince yourself that (9.67) simplifies exactly to the original RVF (9.8) on page 157, when the stochastic discount factor is deterministic,  $M_t = \delta$ .

# C-CAPM and *Hansen–Jagannathan*-Bounds

The consumption-based capital asset pricing model (C-CAPM) comes in many guises and is strongly related to the CAPM, if we assume that agents use the market portfolio to shift consumption between periods. Let's take Equation  $(9.63)$  and remember that the stochastic discount factor is defined by

$$M_t = e^{-\rho t} \frac{u'(C_t)}{u'(c_0)}.$$
(9.68)

We then obtain the consumption-based CAPM equation

$$E[R_S] = R_0 - \frac{\text{Cov}[M_t, R_S]}{E[M_t]} = R_0 - \frac{\text{Cov}[u'(C_t), R_S]}{E[u'(C_t)]}.$$
(9.69)

It is now immediately obvious why  $(9.69)$  is called the C-CAPM, because it relates the return on the stock  $S$  to the marginal utility of consumption at time  $t$ . What is its connection to the original CAPM? To get a handle on this, let's first ask what we get for the market portfolio. Replacing  $R_S$  by  $R_{\text{MP}}$  in (9.69) and rearranging yields

$$E[u'(C_t)] = -\frac{\text{Cov}[u'(C_t), R_{\text{MP}}]}{E[R_{\text{MP}}] - R_0}.$$
(9.70)

Using  $(9.70)$  back in  $(9.69)$ , we obtain the already more familiar form

$$E[R_S] = R_0 + \frac{\text{Cov}[u'(C_t), R_S]}{\text{Cov}[u'(C_t), R_{\text{MP}}]} (E[R_{\text{MP}}] - R_0). \tag{9.71}$$

9.5

We now have to ask, what is the relation of marginal utility and the return of the market portfolio? There is more than one way to obtain a suitable answer (see Cuthbertson and Nitzsche, 2004, sect. 13.2, for four different ways). We will take the short tour here. Let's assume that the unknown utility function *u*(*c*) can be sufficiently approximated by the quadratic utility function

$$u(c) = -\frac{(\eta - c)^2}{2}.$$
(9.72)

Now remember that the agent has to divide her initial wealth endowment *w* between time zero consumption *c*<sup>0</sup> and the proportion invested in the market portfolio, making uncertain time *t* consumption available, measured in *c*0-units. Her budget constraint is thus

$$C_t = (w - c_0)(1 + R_{\text{MP}}). \tag{9.73}$$

Calculating marginal utility of the time *t* consumption *C<sup>t</sup>* under quadratic utility yields

$$u'(C_t) = \eta - C_t = \eta - (w - c_0) - (w - c_0)R_{\text{MP}} = a - bR_{\text{MP}},\tag{9.74}$$

with *a* = η − *b*, and *b* =*w* − *c*0. The important point is that the return on the market portfolio is an affine transformation of the marginal utility of consumption. Computing the covariances in (9.71) yields

$$\begin{aligned} &\operatorname{Cov}[u'(C_t), R_S] = -b \operatorname{Cov}[R_{\text{MP}}, R_S], \\ &\operatorname{Cov}[u'(C_t), R_{\text{MP}}] = -b \operatorname{Var}[R_{\text{MP}}]. \end{aligned} \tag{9.75}$$

Remember that the quotient of the two covariances in (9.75) is exactly the definition of the beta-coefficient β*<sup>S</sup>* in the original CAPM. We have thus from (9.71)

$$E[R_S] = R_0 + \beta_S(E[R_{\rm MP}] - R_0), \tag{9.76}$$

which is the capital asset pricing model.

We can even examine the relation of marginal utility and the market portfolio a little bit further. Remember that the correlation coefficient between two arbitrary random variables *X* and *Y* is defined as

$$\rho = \frac{\text{Cov}[X, Y]}{\sqrt{\text{Var}[X]\text{Var}[Y]}}.\t(9.77)$$

Correlation is a normalized measure of linear dependence of random variables. So let's calculate the correlation between marginal utility *u* ′ (*Ct*) and the market portfolio return *R*MP,

$$\rho = -\frac{b \text{Var}[R_{\text{MP}}]}{\sqrt{b^2 \text{Var}[R_{\text{MP}}] \text{Var}[R_{\text{MP}}]}} = -1. \tag{9.78}$$

**Quick calculation 9.17** Confirm the first equality.

![](_page_15_Figure_1.jpeg)

**Fig. 9.2** Hansen–Jagannathan-bounds in the  $\mu$ - $\sigma$ -diagram – Upper leg is the capital market line

Returns on the market portfolio are perfectly negative correlated with marginal utility. Negative correlation was of course to be expected because higher returns coincide with states of higher consumption and thus lower marginal utility of consumption, if the agent is risk averse. The perfect correlation is due to the affine relation of marginal utility and market portfolio returns, because the dependence structure is fully linear.

**Quick calculation 9.18** Show that for  $X = a + bY$  the correlation of X and Y is  $\rho = 1$ .

The work of Hansen and Jagannathan (1991) revealed another close connection between the C-CAPM and the original CAPM. This one is particularly important, because it ultimately implies certain empirical predictions. The basic idea is actually straightforward. Rewriting the definition of the correlation coefficient (9.77) in a slightly different way yields

$$Cov[X, Y] = \rho \sqrt{Var[X]} \sqrt{Var[Y]}.$$
(9.79)

Using this relation, we can write the C-CAPM equation  $(9.69)$  in the following form

$$\frac{E[R_S] - R_0}{\sqrt{\text{Var}[R_S]}} = -\rho \frac{\sqrt{\text{Var}[M_t]}}{E[M_t]}.$$
(9.80)

Note that the correlation coefficient is by definition  $|\rho| \leq 1$ . Therefore, we can formulate an inequality, which is valid for every security  $S$ , and in alignment with our earlier notation reads

$$\left|\frac{\mu_S - r}{\sigma_S}\right| \le \frac{\text{StD}[M_t]}{E[M_t]},\tag{9.81}$$

where again the standard deviation  $StD[\cdot]$  is the positive root of the variance. Figure 9.2 shows the *Hansen–Jagannathan*-bounds in the  $\mu$ - $\sigma$ -diagram. The upper leg is the mean-variance efficient frontier for risky assets (capital market line, CML),

whereas the lower leg represents insurance contracts that are perfectly correlated with the stochastic discount factor. For the market portfolio, which is perfectly negative correlated with marginal consumption, and therefore with the stochastic discount factor, we obtain an upper theoretical limit for the *Sharpe*-ratio

$$\text{SR}_{\text{MP}} = \frac{\mu_{\text{MP}} - r}{\sigma_{\text{MP}}} = \frac{\text{StD}[M_t]}{E[M_t]},\tag{9.82}$$

to be observed in reality, if the respective SDF model is correct.

**Quick calculation 9.19** Why are all returns on the CML perfectly negative correlated with the SDF?

# **9.6 The Equity Premium Puzzle**

The equity premium puzzle of Mehra and Prescott (1985) is probably the most prominent puzzle in modern economics. Today it is really understood to consist of two parts, the equity premium puzzle and the risk-free rate puzzle. Each part of the puzzle generates empirical predictions, irreconcilable with the other part. In order to make empirical predictions, we have to specify the stochastic discount factor concretely. Here are the assumptions originally made by Mehra and Prescott:

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

• Agents have utility functions of the HARA-type, in particular

$$u(c) = \frac{c^{1-\gamma}-1}{1-\gamma},$$

with relative risk aversion γ ≥ 0.

• Agents maximize their lifetime utility successively, according to a time separable *von Neumann–Morgenstern*-utility functional

$$U[C_{t+1}] = u(C_t) + e^{-\rho} E[u(C_{t+1})|\mathcal{F}_t],$$

depending solely on the consumption stream *C<sup>t</sup>* for *t* ∈ N0.

- Markets are complete.
- There are no frictions like trading costs, etc.

Of course the last two assumptions imply the existence of a representative agent (Constantinides, 1982). The first thing to do is to formulate a model for the historically observed consumption stream. One particularly useful model is the AR(1) process for the logarithmic consumption

$$c_t = c_{t-1} + g + \epsilon_t, \tag{9.83}$$

where we followed the widely accepted convention in economics to represent the natural logarithm of a random variable by its lowercase letter. In (9.83), *g* is the growth

rate of the consumption process and  $\epsilon_t \sim N(0, \sigma_{\epsilon}^2)$ . It will come in handy to write the consumption growth model in a slightly different form,

$$\Delta c_t = g + \epsilon_t, \tag{9.84}$$

where  $\Delta c_t = c_t - c_{t-1}$ . Note that (9.84) is a pure noise process, because  $\epsilon_t$  is not related to the history of the consumption process. Using hyperbolic risk aversion, as assumed by Mehra and Prescott (1985), we can now specify the SDF in a very concrete form

$$M_t = e^{-\rho} \left(\frac{C_t}{C_{t-1}}\right)^{-\gamma} = e^{-\rho - \gamma \Delta c_t}.$$
(9.85)

Before we proceed, let's summarize briefly the empirical findings of Mehra and Prescott. Without going into too much detail, they used various time series to calculate inflation adjusted annual returns for the Standard & Poor's Composite Stock Price Index (S&P 500), per capita real consumption growth on non-durable commodities and services and an annual risk-free interest rate proxy from relatively riskless shortterm securities like US Treasury bills, in the period of 1889 to 1978. According to this data, the S&P 500 realized an annual average growth rate of  $\hat{\mu}_{S&P} = 6.98\%$ , with a standard deviation of  $\hat{\sigma}_{S\&P} = 16.54\%$ . The average risk-free interest rate was  $r = 0.8\%$  p.a. and thus, the average equity premium was  $\hat{\mu}_{S\&P} - r = 6.18\%$ . Consumption growth rate and standard deviation of the random error in (9.84) were estimated as  $\hat{g} = 1.83\%$  and  $\hat{\sigma}_{\epsilon} = 3.57\%$ . What do these figures tell us about the agent's risk aversion? First of all, the average *Sharpe*-ratio of the S&P 500 is roughly 37.36%. We can also assume that the Standard & Poor's index is a good proxy for the market portfolio and thus it should be perfectly negative correlated with the SDF. We have thus by  $(9.82)$ 

$$SR_{S\&P} = 37.36\% = \frac{\text{StD}[M_t]}{E[M_t]}.$$
(9.86)

In order to complete our calculations we need another standard result from statistics. Consider again the log-normal distributed random variable  $Y = e^{X}$ , with  $X \sim N(\mu, \sigma^{2})$ . We already used that  $E[Y] = e^{\mu + \frac{1}{2}\sigma^2}$ . The variance of Y is given by

$$\text{Var}[Y] = (e^{\sigma^2} - 1)e^{2\mu + \sigma^2}.$$
 (9.87)

Now consider the ratio between the variance and the squared expectation value of such a random variable

$$\frac{\text{Var}[Y]}{E[Y]^2} = e^{\sigma^2} - 1 \approx \sigma^2, \tag{9.88}$$

for small variances. The ratio of standard deviation and expectation value is the positive root of (9.88).

According to (9.88), the right hand side of (9.86) is approximately  $\gamma \sigma_{\epsilon}$ , because by (9.85) we have  $M_t = e^{-\rho - \gamma g - \gamma \epsilon_t}$ . Using the estimate obtained from the data and rearranging yields

$$\hat{\gamma} \approx \frac{\text{SR}_{\text{S\&P}}}{\hat{\sigma}_{\epsilon}} = 10.47. \tag{9.89}$$

Is this alarmingly high? From experiments on gambles the relative risk aversion was expected to be in the range 3 ≤ γ ≤ 10. There is a neat self test you can try to determine your own personal relative risk aversion in Cuthbertson and Nitzsche (2004, p. 328). The bottom line is that if your relative risk aversion is too high, sticking to HARAutility leads to implausible results (see Rabin's paradox, Rabin, 2000). So the question is, is our γˆ, induced by the observed equity premium, too high? To answer this question, we need a second piece of information provided by the stochastic discount factor framework, that we have not yet extracted. This one leads to what is known as the risk-free rate puzzle.

In (9.60) on page 167, we established the relation between the risk-free gross return and the expectation value of the SDF. For continuous compounding over one period of time, we thus obtain

$$E[M_t|\mathcal{F}_{t-1}] = e^{-r}.\t$$
(9.90)

Because we have now specified the concrete family of utility functions, and we have a stochastic model for the evolution of the consumption stream, we get another equation from (9.85)

$$E[M_t|\mathcal{F}_{t-1}] = e^{-\rho - \gamma g + \frac{1}{2}\gamma^2 \sigma_{\epsilon}^2}.$$
(9.91)

Equating (9.90) and (9.91) one obtains for the risk-free interest rate

$$r = \rho + \gamma g - \frac{1}{2}\gamma^2 \sigma_{\epsilon}^2 \ge \gamma g - \frac{1}{2}\gamma^2 \sigma_{\epsilon}^2. \tag{9.92}$$

Using the estimates for γ, *g*, and σ<sup>ϵ</sup> , we have extracted from the data, we can compute a lower bound for the estimate of *r*,

$$\hat{r} \ge \hat{\gamma}\hat{g} - \frac{1}{2}\hat{\gamma}^2 \hat{\sigma}_{\epsilon}^2 \approx 12\%. \tag{9.93}$$

This is way too high. Even if we take into account that the risk-free interest rate was averaged by (Mehra and Prescott, 1985). From their data we have *r*ˆ = 0.8%, where the estimator is asymptotically normal, with standard deviation

$$\text{StD}[\hat{r}] = 0.6\%.$$
 (9.94)

There is no way this discrepancy could be explained by random fluctuations. The probability of accidently observing an average rate of *r*ˆ = 0.8% or smaller, like the one in the data, whereas the true risk-free interest rate is indeed *r* = 12% is of order O ( 10<sup>−</sup><sup>78</sup>) .

#### **Quick calculation 9.20** Can you see how this probability was computed?

This means you would have to wait something like 10<sup>78</sup> years on average, to see one such weird sample. The age of the entire universe is roughly 1.5 · 10<sup>10</sup> years. You can now appreciate how overwhelmingly improbable such an event would be.

Of course our analysis is based on certain assumptions regarding the utility structure, the consumption stream process, and so forth. It is perfectly possible that relaxing some of those restrictions might work in our favor. But there is still a long way to go and there

is no guarantee that modifying the assumptions does not make things worse. Here is one example. We assumed that the market portfolio can be represented by the S&P 500 index and thus, the correlation between the SDF and the return on the index is ρ = −1. Empirical findings indicate that the correlation could be substantially smaller, because the S&P 500 is a limited proxy of the real market portfolio. Assume that this correlation was estimated as ρˆ = − 1 2 . Where would it go in the equation? From (9.80) and (9.89) we would conclude that

$$\hat{\gamma} = -\frac{\text{SR}_{\text{S\&P}}}{\hat{\rho}\hat{\sigma}_{\epsilon}} = 2\frac{\text{SR}_{\text{S\&P}}}{\hat{\sigma}_{\epsilon}} \approx 21. \tag{9.95}$$

**Quick calculation 9.21** Confirm this result.

This would make things substantially worse. It has also been questioned, if data reaching more than 100 years into the past is appropriate, because economies and markets have undergone substantial changes due to two world wars and environmental developments in the law and social systems, globalization, technology, etc. Cochrane (2005, sect. 21.1) reports for the New York Stock Exchange index (NYSE) a post-WWII *Sharpe*-ratio of roughly one half. His empirical findings require a relative risk aversion of γ ≈ 50. The corresponding lower bound for the risk-free rate of return is *r* ≥ 37.5%. This is far beyond observation and would cause the economy to collapse because of a massive drop in consumption and investments.

The equity premium puzzle leaves us with two equivalent questions that cannot be answered simultaneously. We can either ask, how can a required moderate relative risk aversion, say in the range 0.5 ≤ γ ≤ 2.5 generate such a high equity premium as observed in the data, or we can accept a high γ, but are immediately faced with the problem of explaining far too low risk-free interest rates. A number of quite brilliant suggestions have been made since the seminal article of Mehra and Prescott (1985), to resolve the equity premium puzzle. We will discuss one of them in the sequel.

# **9.7 The Campbell–Cochrane-Model**

The model of Campbell and Cochrane (1999) resolves the puzzles discussed so far essentially by extending the state space. Until now, we assumed that utility solely depends on the consumption stream. Campbell and Cochrane added another variable, representing a common consumption level all agents in the economy got used to in the recent past. This concept is called habit formation and it generally comes in two flavors. The first one is an individual habit formation, based on becoming adapted to a certain standard of living. Hence, not the absolute levels of consumption dominate the utility function, but the changes with respect to the individual habit level. The second version of habit formation is oriented on the average consumption level of all other agents in the economy. Thus, the stimulus for a given agent is exogenous and is called

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

"keeping up with the Joneses" by Abel (1990). This is the type used by Campbell and Cochrane (1999). In particular they suggested the following utility function

$$u(c,x) = \frac{(c-x)^{1-\gamma} - 1}{1-\gamma},\tag{9.96}$$

where the second state variable *x* represents a common consumption level. There is another useful quantity called the surplus consumption ratio

$$S_t = \frac{C_t - X_t}{C_t} = 1 - \frac{X_t}{C_t}.$$
(9.97)

Obviously, the surplus consumption ratio increases with consumption and for *C<sup>t</sup>* = *Xt* , we have *S<sup>t</sup>* = 0, which is a very bad state. Let's compute the relative risk aversion of an arbitrary agent with utility function (9.96) and keep in mind that the average consumption level *X<sup>t</sup>* is exogenous for her

$$\text{RRA}(c) = -c\frac{\partial^2 u/\partial c^2}{\partial u/\partial c} = \frac{\gamma}{s},\tag{9.98}$$

with *s* = *c*−*x c* .

#### **Quick calculation 9.22** Confirm this result.

This is extremely enlightening, because we already get a glimpse of how this mechanism might work. First of all, we may have a small γ, but the surplus ratio *s*is most likely very small, because it is a relative quantity. Thus, the relative risk aversion may come out large, even if γ is small, because it is divided by a very small number. Second, in times of recession, where *S<sup>t</sup>* decreases and possibly tends to zero, the relative risk aversion becomes very large, and this is precisely what is observed in reality. The only problem is that the whole argument breaks down, if the surplus consumption ratio becomes negative. Campbell and Cochrane (1999) prevented this from happening by making suitable assumptions about the surplus consumption process.

In the following, we again stick to the economic tradition and represent the logarithm of random variables by their lowercase letters. Campbell and Cochrane (1999) also used the AR(1)-model (9.83) for logarithmic consumption *c<sup>t</sup>* = log *C<sup>t</sup>* ,

$$c_t = c_{t-1} + g + \epsilon_t, \tag{9.99}$$

with ϵ*<sup>t</sup>* ∼ *N*(0, σ<sup>2</sup> ϵ ). They also assumed that the logarithmic surplus consumption ratio process *s<sup>t</sup>* = log *S<sup>t</sup>* is a mean reverting process of the kind

$$s_t = (1 - \phi)\bar{s} + \phi s_{t-1} + \lambda(s_{t-1})\epsilon_t. \tag{9.100}$$

That is, the logarithmic surplus process is driven by the same random error as the logarithmic consumption process (random consumption shocks). For 0 ≤ ϕ < 1, the process eventually drifts towards its mean reversion level *s*¯, whereas λ(*s*) is called the sensitivity function by Campbell and Cochrane, to be determined in order to satisfy additional model assumptions. The immediate next step is to compute the stochastic discount

factor in order to see, if there is an additional contribution, accounting for the large equity premium. A somewhat lengthy calculation yields

$$\begin{split} M_{t} &= e^{-\rho} \left( \frac{S_{t}C_{t}}{S_{t-1}C_{t-1}} \right)^{-\gamma} = e^{-\rho - \gamma(\Delta c_{t} + \Delta s_{t})} \\ &= \exp \bigl( -\rho - \gamma(g + \epsilon_{t}) - \gamma \bigl( (1 - \phi)(\bar{s} - s_{t-1}) + \lambda(s_{t-1}) \epsilon_{t} \bigr) \bigr) \\ &= \exp \bigl( -\rho - \gamma(g + (1 - \phi)(\bar{s} - s_{t-1})) - \gamma(1 + \lambda(s_{t-1})) \epsilon_{t} \bigr). \end{split} \tag{9.101}$$

Using our log-normal trick  $(9.88)$ , we obtain for the ratio of the conditional standard deviation and the conditional expectation of the SDF

$$\frac{\text{StD}[M_t|\mathcal{F}_{t-1}]}{E[M_t|\mathcal{F}_{t-1}]} \approx \gamma \sigma_{\epsilon} (1 + \lambda(s_{t-1})). \tag{9.102}$$

Remember that  $(9.102)$  is the *Sharpe*-ratio of the market portfolio we expect to observe, conditional on the information  $\mathcal{F}_{t-1}$ . And indeed, there is an extra term  $\gamma \sigma_{\epsilon} \lambda(s_{t-1}),$ possibly accounting for the high equity premium observed. It all depends on how  $\lambda(s)$  is chosen. In order to determine a suitable form of  $\lambda(s)$ , Campbell and Cochrane imposed three conditions:

- The risk-free interest rate is constant.
- Habit is predetermined at the steady state  $s_t = \bar{s}$ .
- Habit moves non-negatively with consumption everywhere.

Surprisingly, these conditions are indeed sufficient to determine the sensitivity function

$$\lambda(s) = \begin{cases} \frac{\sqrt{1 - 2(s - \bar{s})}}{\bar{s}} - 1 & \text{for } s \le s_{\text{max}} \\ 0 & \text{for } s > s_{\text{max}}, \end{cases}$$
(9.103)

with  $s_{\text{max}} = \bar{s} + \frac{1}{2}(1 - \bar{S}^2)$ , and

$$\bar{S} = \sigma_{\epsilon} \sqrt{\frac{\gamma}{1 - \phi}}.\tag{9.104}$$

We will not go through the entire proof (see the original paper of Campbell and Cochrane, 1999), but let's show that the first condition is indeed satisfied. The risk-free interest rate can be computed from the conditional expectation of the SDF  $(9.101)$ . In particular for the continuous one period risk-free gross return  $R_0^* = e^r$  one obtains

$$\begin{split} r &= -\log E[M_t|\mathcal{F}_{t-1}] \\ &= \rho + \gamma (g + (1 - \phi)(\bar{s} - s_{t-1})) - \frac{1}{2}\gamma^2 \sigma_{\epsilon}^2 (1 + \lambda(s_{t-1}))^2 \\ &= \rho + \gamma g - \frac{1}{2} \left(\frac{\gamma}{\bar{S}}\right)^2 \sigma_{\epsilon}^2 = \rho + \gamma g - \frac{\gamma}{2} (1 - \phi), \end{split} \tag{9.105}$$

which is indeed constant.

**Quick calculation 9.23** Verify the first and second equality in  $(9.105)$ .

The big question is, can the large equity premium be explained by the *Campbell*-*Cochrane*-model, while maintaining a relatively small risk-free interest rate? In their

| in the set in an and composition continuity in and |                     |       |  |
|----------------------------------------------------|---------------------|-------|--|
| Parameter                                          | Variable            | Value |  |
| Mean consumption growth rate $(\%)$                | g                   | 1.89  |  |
| Standard deviation of consumption growth (%)       | $\sigma_{\epsilon}$ | 1.50  |  |
| Risk-free interest rate $(\%)$                     | r                   | 0.94  |  |
| Surplus consumption persistence coefficient        | Φ                   | 0.87  |  |
| Local utility curvature                            | $\boldsymbol{\nu}$  | 2.00  |  |
|                                                    |                     |       |  |

| <b>Table 9.1</b> Parameters in the <i>Campbell–Cochrane</i> -model |  |
|--------------------------------------------------------------------|--|
|--------------------------------------------------------------------|--|

original article, Campbell and Cochrane (1999) chose the model parameters as in Table 9.1. From these figures, we can calculate a steady state surplus consumption ratio of  $\bar{S}$  = 5.88%, and a steady state *Sharpe*-ratio of

$$\text{SR}_{\text{MP}}(\bar{s}) = \frac{\gamma \sigma_{\epsilon}}{\bar{S}} = 0.51, \tag{9.106}$$

matching more or less exactly the observed *Sharpe*-ratio of the post-WWII NYSEindex data.

But there is much more. In their subsequent paper, Campbell and Cochrane (2000) set up a toy economy with their habit formation model and simulated consumption streams, asset returns, and other quantities. The latter is possible because the pricedividend ratio can be obtained from a functional equation. To understand how this is done, first recall that for the gross return  $R_t^*$  of an arbitrary asset

$$1 = E[M_{t+1}R_{t+1}^*|\mathcal{F}_t] \tag{9.107}$$

holds, and that the gross return on a dividend paying security<sup>1</sup>  $V$  is

$$R_{V,t+1}^* = \frac{V_{t+1} + D_{t+1}}{V_t}.$$
(9.108)

Multiplying both sides of (9.107) with  $\frac{V_t}{D_t}$ , one obtains

$$\frac{V_t}{D_t} = E\bigg[M_{t+1}\frac{V_{t+1} + D_{t+1}}{D_t}\bigg|\mathcal{F}_t\bigg] = E\bigg[M_{t+1}\frac{D_{t+1}}{D_t}\bigg(1 + \frac{V_{t+1}}{D_{t+1}}\bigg)\bigg|\mathcal{F}_t\bigg].\tag{9.109}$$

**Quick calculation 9.24** Confirm the last equality in (9.109).

Equation  $(9.109)$  is a functional equation for the price-dividend ratio. To make this more transparent, let's write it in a slightly different way and call it the price-dividend function

$$\frac{V}{D}(s_t) = E\bigg[M_{t+1}\frac{D_{t+1}}{D_t}\bigg(1 + \frac{V}{D}(s_{t+1})\bigg)\bigg|\mathcal{F}_t\bigg],\tag{9.110}$$

<sup>&</sup>lt;sup>1</sup> We use the letter  $V$  for the price of a dividend paying security here, in order to avoid confusion with the surplus consumption ratio  $S$ .

where the logarithmic surplus consumption ratio  $s_t$  is the only state variable for the economy. The objective is now to find a particular function  $\frac{V}{D}(s)$  that obeys (9.110). To this end, Campbell and Cochrane assume that the logarithmic dividend process is driven by the same growth factor as consumption

$$d_t = d_{t-1} + g + \eta_t, \tag{9.111}$$

with  $d_t = \log D_t$ , and that the random error  $\eta_t \sim N(0, \sigma_n^2)$  is positively correlated with  $\epsilon_l$ . Now, the conditional expectation can be computed and (9.110) is an equation in the unknown function  $\frac{V}{D}(s)$ . Campbell and Cochrane solved this functional equation numerically on a grid for the state variable  $s_t$  and afterwards interpolated the pricedividend function. Once they obtained this function, they were able to simulate all interesting quantities inside their toy economy.

Campbell and Cochrane (2000) simulated 100000 months of time series data for their toy economy and used this artificial data to compare the performance of several asset pricing models. Here is what they surprisingly found: Asset pricing models, focusing on the return of a wealth or market portfolio, like the CAPM, perform much better than the C-CAPM pricing method, based on conventional HARA-utility. This is a remarkable result, because the artificial data was generated under the consumptionbased habit formation model. Obviously, the CAPM has the edge over the C-CAPM, because its predictions are conditional on the filtration  $\mathcal{F}_t$ , whereas the utility function

$$u(c) = \frac{c^{1-\gamma} - 1}{1 - \gamma} \tag{9.112}$$

gives rise to an unconditional stochastic discount factor

$$M_t = e^{-\rho} \left(\frac{C_t}{C_{t-1}}\right)^{-\gamma} = e^{-\rho - \gamma g - \gamma \epsilon_t}.$$
(9.113)

Campbell and Cochrane do not reject consumption-based asset pricing models in general, but they attribute the poor performance of the C-CAPM to the limitations of the simple parametric form of the utility function.

## 9.8

# **Further Reading**

There are several comprehensive and accessible textbooks on financial economics like Cochrane (2005), Cuthbertson and Nitzsche (2004), and Lengwiler (2004). The classical references on stock price bubbles are Blanchard (1979) and Froot and Obstfeld (1991). An additional approach to bubbles and crashes, based on herding and critical behavior of complex systems, can be found in Johansen et al. (2000) and Sornette (2003). For the classical paradoxes see Shiller (1981), Mehra and Prescott (1985), and also Weil (1992). To explain the equity premium puzzle, several strategies were suggested. An incomplete list covers generalizing the expected utility functional to disentangle intertemporal substitution and risk aversion (Epstein and Zin, 1989, 1991), habit formation (Constantinides, 1990), incorporating wealth into the utility function

(Bakshi and Chen, 1996), incomplete markets (Constantinides and Duffie, 1996), and habit persistence (Campbell and Cochrane, 1999, 2000).

# Problems

**9.1** In adding up an infinite sum, one usually assumes the following two properties to hold

$$\sum_{k=0}^{\infty} s_k = s_0 + \sum_{k=1}^{\infty} s_k \quad \text{and} \quad \sum_{k=0}^{\infty} \alpha s_k = \alpha \sum_{k=0}^{\infty} s_k.$$

. . . . . . . . . . . . . . . . . .

Show that using these properties, the surprising result

$$\sum_{k=0}^{\infty} 2^k = -1$$

can be established.

**9.2** The rational valuation formula for stochastic discount factor models is

$$S_{t} = \sum_{k=1}^{\infty} E\left[\prod_{n=1}^{k} M_{t+n} \middle| \mathcal{F}_{t}\right] E[D_{t+k}|\mathcal{F}_{t}] + \sum_{k=1}^{\infty} \text{Cov}\left[\prod_{n=1}^{k} M_{t+n}, D_{t+k} \middle| \mathcal{F}_{t}\right].$$

How does this formula simplify, if the SDF can be assumed conditionally uncorrelated,  $\text{Cov}[M_t, M_{t+k}|\mathcal{F}_t] = 0$  for  $k \neq 0$ ?

**9.3** Consider an economy at  $t=0$  and  $t=T$ . Show that under CARA-utility, the stochastic discount factor is

$$M_T = e^{-\rho T - \alpha (C_T - c_0)}.$$

if the usual time separable von Neumann-Morgenstern-utility functional is assumed.

**9.4** The generalized *Epstein–Zin*-utility functional is based on the idea of a discounted certainty equivalent. One possible form is

$$U[C_t] = \left(c_0^{\alpha} + e^{-\rho t}u^{-1}\left(E[u(C_t)]\right)^{\alpha}\right)^{\frac{1}{\alpha}}$$

Is this functional time separable if the utility function is  $u(c) = \sqrt{c}$  and  $\alpha = \frac{1}{2}$ ?

9.5 Show that the interest rate in the *Campbell–Cochrane*-model can be made time dependent of the form

$$r_t = r_0 + B(\overline{s} - s_{t-1})$$

for some fixed  $r_0$ , if the steady state surplus consumption ratio is modified to be

$$\bar{S} = \sigma_{\epsilon} \sqrt{\frac{\gamma}{1 - \phi - \frac{B}{\gamma}}}.$$

What is the fixed steady state rate  $r_0$ ?

## 9.9
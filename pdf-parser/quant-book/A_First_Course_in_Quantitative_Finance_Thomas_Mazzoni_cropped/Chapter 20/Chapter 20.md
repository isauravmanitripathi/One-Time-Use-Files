Until now, we have traveled the paved road of standard instruments and derivatives that are very liquidly traded. In fact, we have been rewarded for this in terms of straightforward standard pricing formulas, with all necessary ingredients provided by the market. Leaving this road, we immediately find ourselves in a jungle of term structure models with very different advantages and shortcomings. What they all have in common is that none of them is universally optimal.

#### 20.1 A Term Structure Toy Model

By now it should be very clear that the discount bond is a central element in pricing all sorts of claims. We have seen two different representations of its price,

$$P(t,T) = e^{-\int_t^T f(t,s)ds} = E^{\mathcal{Q}} \left[ e^{-\int_t^T r(s)ds} \middle| \mathcal{F}_t \right]. \tag{20.1}$$

In the preceding chapters, we mostly relied on the forward rate representation, and cleverly manipulated probability measures. But there are a few unanswered questions in this framework. For example, we are still not in a position to price a simple option on a coupon-bearing bond. We will temporarily leave this road and turn to the second equality in  $(20.1)$ . To be a little more precise, we will specify particular dynamics for the short rate  $r(t)$ , in order to compute prices by evaluating the Q-expectation. Eventually, both frameworks will be reconciled in the seminal approach of Heath et al. (1992).

Term structure models come in many flavors with respect to the number of factors, their distributional properties, time-homogeneity of their parameters, and so forth. We will start with the simplest possible specification, which is merely a toy model. But we can learn a lot about the general setup by studying this simplified version. Suppose the stochastic interest rate process under the pricing measure  $O$  is given by

$$dr(t) = \sigma_r dW(t). \tag{20.2}$$

We have now stated the time dependence in the *Wiener*-increment explicitly as a function argument to keep the notation consistent. At any later time  $s > t$ , the interest rate has changed and is given by

$$r(s) = r(t) + \sigma_r \int_t^s dW(u). \tag{20.3}$$

We can already identify this short rate model as *Gaussian*, because the  $It\hat{o}$ -integral is a normally distributed random variable. It is easy to verify that  $E^{Q}[r(s)|\mathcal{F}_{t}] = r(t)$ , and

![](_page_1_Figure_1.jpeg)

Fig. 20.1 Integration of a triangle - Order of integration switched between left and right figure

 $\text{Var}[r(s)|\mathcal{F}_t] = \sigma_r^2(s-t)$ . We can also determine the first shortcoming, common to all Gaussian models, namely that there is a nonzero probability for the interest rate to become negative. But let's ignore this problem for the moment. The quantity really needed, according to the right hand side of  $(20.1)$ , is

$$-\int_{t}^{T} r(s)ds = -r(t)\int_{t}^{T} ds - \sigma_{r}\int_{t}^{T}\int_{t}^{s} dW(u)ds.$$
 (20.4)

Even though the inner integral in the last term is stochastic, we are allowed to switch the order of integration due to a generalized version of Fubini's theorem that can be found in Filipović (2009, sect. 6.5). But something happens to the bounds of integration. Let's forget stochastic integration for a moment. Suppose you want to integrate over the area of the lower triangle inside a square with edge length  $T - t$ . If the inner integral is with respect to the vertical direction, as indicated in Figure 20.1 left, then the lower bound is  $t$  and the upper bound has to be variable. If we change the order of integration, the inner integral is with respect to the horizontal direction, as indicated in Figure 20.1 right. But now the upper bound has to be fixed at T and the lower bound has to vary. We can thus conclude that

$$\int_{t}^{T} \int_{t}^{s} duds = \int_{t}^{T} \int_{u}^{T} dsdu \tag{20.5}$$

holds. Even though the double integral in  $(20.4)$  does not represent a triangle in the usual sense, changing the bounds of integration works exactly the same, and we obtain

$$\int_{t}^{T} \int_{t}^{s} dW(u)ds = \int_{t}^{T} \int_{u}^{T} ds dW(u) = \int_{t}^{T} (T - u)dW(u). \tag{20.6}$$

A little algebra and cleaning up the notation shows that  $(20.4)$  now becomes

$$-\int_{t}^{T} r(s)ds = -r(t)(T-t) - \sigma_{r} \int_{t}^{T} (T-s)dW(s). \tag{20.7}$$

We can now see that the expression on the right hand side of  $(20.7)$  is a *Gaussian* random variable, with expectation

$$E^{Q}\left[-\int_{t}^{T}r(s)ds\middle|\mathcal{F}_{t}\right] = -r(t)(T-t),\tag{20.8}$$

and variance

$$\operatorname{Var}\left[-\int_{t}^{T} r(s)ds\middle|\mathcal{F}_{t}\right] = \sigma_{r}^{2} \int_{t}^{T} (T-s)^{2} ds = \frac{1}{3} \sigma_{r}^{2} (T-t)^{3}.$$
 (20.9)

Recalling the expectation value of a log-normal distributed random variable, one obtains the explicit price for the discount bond

$$P(t,T) = E^{\mathcal{Q}}\left[e^{-\int_t^T r(s)ds}\Big|\mathcal{F}_t\right] = e^{-r(t)(T-t) + \frac{1}{6}\sigma_r^2(T-t)^3}.\tag{20.10}$$

Applying Itô's lemma to  $(20.10)$ , we can derive the dynamics of the discount bond price. One obtains

$$dP = \left(\frac{\partial P}{\partial t} + \frac{1}{2}\frac{\partial^2 P}{\partial r^2}\sigma_r^2\right)dt + \frac{\partial P}{\partial r}\sigma_r dW$$
  
=  $rPdt - \sigma_r (T - t)PdW.$  (20.11)

**Quick calculation 20.1** Verify the second equality.

There is much internal consistency demonstrated by this result. First of all, we are in the risk-neutral probability measure  $Q$  and therefore, every security should have the drift rate  $r(t)$ . Of course, because our interest rate model is *Gaussian*, the bond price dynamics have to be log-normal, and everything works out in terms of a geometric *Brown*ian motion. But nevertheless, it is very reassuring that the drift comes out correctly. We can further deduce from  $(20.11)$  that the bond volatility is

$$\sigma_P(t) = -\sigma_r(T - t). \tag{20.12}$$

The minus sign has no particular meaning here, because the distribution of the *Wiener*increment  $dW(t)$  is symmetric. But more importantly, the pull to par requirement is satisfied. As  $t \rightarrow T$ , the bond volatility tends to zero.

So far nearly everything looks fine with our toy model, so where is the problem? Let's remember the definition of the yield to maturity

$$y(t,T) = -\frac{\log P(t,T)}{T-t}.$$
 (20.13)

Using  $(20.10)$ , the yield to maturity in this particular model is given by

$$y(t,T) = r(t) - \frac{1}{6}\sigma_r^2(T-t)^2.$$
 (20.14)

Obviously, the mapping  $T \mapsto y(t, T)$  is downward sloping with  $\lim_{T \to \infty} y(t, T) = -\infty$ . This is really bad news, because such a yield curve is definitely not observed in the market. We can furthermore extract the forward curve by

$$f(t,T) = -\frac{\partial}{\partial T} \log P(t,T) = r(t) - \frac{1}{2}\sigma_r^2 (T-t)^2.$$
 (20.15)

**Quick calculation 20.2** Confirm this result by using  $f(t, T) = y(t, T) + \frac{\partial y}{\partial T}(T - t)$ .

457

The forward curve is also downward sloping, but more importantly, changes in  $r(t)$  can only cause parallel shifts of the forward curve, but no structural changes like bending or twisting. This is the result of a shortcoming, common to all one-factor models, not particularly *Gaussian* ones. In a one-factor short rate model, the movements of all points on the yield and forward curve are perfectly correlated. That matter is not open for debate, but the situation can be improved otherwise, by making the initial yield curve an input to the model. This is the idea of yield curve fitting due to Ho and Lee (1986).

## 20.2

## **Yield Curve Fitting**

Imagine now that today is time  $t = 0$ , and you know the yield curve  $v(0, T)$  in terms of an explicit, sufficiently smooth function of T. You want a model for the short rate that is able to reproduce all bond prices  $P(0, T)$  you observe today, for every single T. Ho and Lee (1986) discovered that this goal can be achieved by simply injecting an auxiliary deterministic function  $a(t)$  into the solution (20.3),

$$r(t) = r(0) + a(t) + \sigma_r \int_0^t dW(s), \qquad (20.16)$$

with  $a(0) = 0$ . It is easy to see that this solution corresponds to the dynamic equation

$$dr(t) = \theta(t)dt + \sigma_r dW(t), \qquad (20.17)$$

where  $\theta(t) = \frac{da(t)}{dt}$  has to hold. But how should this auxiliary function  $a(t)$  be chosen to generate the desired result? Let's make an educated guess.

$$a(t) = f(0, t) - r(0) + \frac{1}{2}\sigma_r^2 t^2.$$
 (20.18)

Because the yield curve  $y(0, T)$  is known and sufficiently smooth, so is the forward curve  $f(0, T)$ . But how does this definition of  $a(t)$  help? From our discussion in the last section, we can conclude that

$$E^{Q}\left[e^{-\int_{0}^{T}r(t)dt}\Big|\mathcal{F}_{0}\right] = e^{-r(0)T+\frac{1}{6}\sigma_{r}^{2}T^{3}}e^{-\int_{0}^{T}a(t)dt}.\tag{20.19}$$

Using (20.18) and  $f(0, t) = -\frac{\partial}{\partial t} \log P(0, t)$ , the integral in the last exponential becomes

$$-\int_{0}^{T} a(t)dt = \log P(0,T) + r(0)T - \frac{1}{6}\sigma_{r}^{2}T^{3}.$$
 (20.20)

Plugging this solution into  $(20.19)$ , we indeed obtain

$$E^{\mathcal{Q}}\left[e^{-\int_0^T r(t)dt}\middle|\mathcal{F}_0\right] = P(0,T). \tag{20.21}$$

That is, we managed to reconstruct the discount bond prices, observed today at  $t = 0$ . Furthermore, we can now deduce what the drift  $\theta(t)$  in (20.17) has to be. Altogether we obtain

$$dr(t) = \left(\frac{\partial f(0,t)}{\partial t} + \sigma_r^2 t\right) dt + \sigma_r dW(t). \tag{20.22}$$

Reproducing the initial discount bond curve is unfortunately only the easy part. If we want to derive analytic expressions for bond options, we also have to derive the model induced price for a discount bond in the future, say  $P(t, T)$  for  $t > 0$ . Let's again try an educated guess and show afterwards why it is correct. The price for the discount bond  $P(t, T)$ , induced by the model (20.22), is

$$P(t,T) = \frac{P(0,T)}{P(0,t)} e^{-\frac{1}{2}\sigma_r^2 t(T-t)^2} e^{-x(t)(T-t)},$$
(20.23)

with  $x(t)$  defined by

$$x(t) = r(t) - f(0, t) = \frac{1}{2}\sigma_r^2 t^2 + \sigma_r W(t).$$
 (20.24)

The second equality results from plugging  $(20.18)$  into  $(20.16)$ . Let's see, if we can prove  $(20.23)$ . By definition we have

$$P(t,T) = E^{\mathcal{Q}}\left[e^{-\int_t^T r(s)ds}\middle|\mathcal{F}_t\right] = e^{-\int_t^T f(0,s)ds}E^{\mathcal{Q}}\left[e^{-\int_t^T x(s)ds}\middle|\mathcal{F}_t\right].\tag{20.25}$$

The integral over the forward rate accounts for the factor  $\frac{P(0,T)}{P(0,t)}$ , so we only have to compute the conditional expectation involving  $x(s)$ . So let's first compute the integral

$$\begin{split} -\int_{t}^{T} x(s)ds &= -\frac{1}{2}\sigma_{r}^{2} \int_{t}^{T} s^{2}ds - \sigma_{r} \int_{t}^{T} \int_{0}^{s} dW(u)ds \\ &= -\frac{1}{6}\sigma_{r}^{2}(T^{3} - t^{3}) - \sigma_{r} \int_{t}^{T} \int_{0}^{t} dW(u)ds - \sigma_{r} \int_{t}^{T} \int_{t}^{s} dW(u)ds \\ &= -\frac{1}{6}\sigma_{r}^{2}(T^{3} - t^{3}) - \sigma_{r} W(t)(T - t) - \sigma_{r} \int_{t}^{T} (T - s)dW(s), \end{split} \tag{20.26}$$

where we again used Fubini's theorem to change the order of integration in the last line. From this calculation, it is clear that the integral is a *Gaussian* random variable. The expectation in  $(20.25)$  is therefore with respect to a log-normal random variable and one obtains

$$E^{\mathcal{Q}}\left[e^{-\int_{t}^{T}x(s)ds}\Big|\mathcal{F}_{t}\right] = \exp\left(-\frac{1}{6}\sigma_{r}^{2}(T^{3}-t^{3}) - \sigma_{r}W(t)(T-t) + \frac{1}{6}\sigma_{r}^{2}(T-t)^{3}\right)$$
  
$$= \exp\left(-\frac{1}{2}\sigma_{r}^{2}(T^{2}t-Tt^{2}) + \frac{1}{2}\sigma_{r}^{2}t^{2}(T-t) - x(t)(T-t)\right)$$
  
$$= \exp\left(-\frac{1}{2}\sigma_{r}^{2}t(T^{2}-2Tt+t^{2}) - x(t)(T-t)\right)$$
  
$$= \exp\left(-\frac{1}{2}\sigma_{r}^{2}t(T-t)^{2} - x(t)(T-t)\right),$$
  
(20.27)

which proves (20.23). The upshot of all these computations is that *x*(*t*) is a normally distributed random variable and thus, we can derive *Black–Scholes*-like formulas to price European options on bonds, based on the short rate model (20.22). We will not push the analysis further at this point, because the shortcomings of the model still remain. In particular, we cannot hope to compute realistic option prices from it, regardless of whether we are able to derive analytic valuation formulas or not. Instead, let's move on to a more promising class of models.

## **20.3 Mean Reversion and the Vasicek-Model**

What is observed in the market is that, unlike security prices, which seem to evolve geometrically, interest rates stay in a more or less fixed band. Furthermore, it looks as if they were pulled back to an equilibrium value. Of course this effect is not that clear from the charts, because there is a significant amount of random noise involved. Vasicek (1977) therefore used a mean reverting drift specification, first proposed by Uhlenbeck and Ornstein (1930), commonly known as the *Ornstein–Uhlenbeck*-process

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$dr(t) = \kappa(\theta - r(t))dt + \sigma_r dW(t). \qquad (20.28)$$

There are two new elements involved in (20.28), the mean reversion level θ, and the mean reversion speed κ. We have already seen those elements in the stochastic volatility equation of the *Heston*-model (16.51) on page 365. The mean reversion level θ is the long-term rate to which *r*(*t*) is pulled. The mean reversion speed κ governs the strength of this pull. For κ = 0 we are back in our toy model (20.2). So let's solve the *Ornstein–Uhlenbeck*-equation to determine the properties of the *Vasicek*-model. For *s* > *t*, consider the function *y*(*s*) = *e* κ*s r*(*s*), and apply Itô's lemma,

$$dy(s) = e^{\kappa s} \kappa \theta ds + e^{\kappa s} \sigma_r dW(s). \tag{20.29}$$

**Quick calculation 20.3** Confirm this result.

This equation is easily integrated and one obtains

$$y(s) = y(t) + \kappa\theta \int_{t}^{s} e^{\kappa u} du + \sigma_r \int_{t}^{s} e^{\kappa u} dW(u). \tag{20.30}$$

Dividing both sides by *e* <sup>κ</sup>*<sup>s</sup>* and using a little bit of straightforward algebra yields

$$r(s) = \theta + (r(t) - \theta)e^{-\kappa(s-t)} + \sigma_r \int_t^s e^{-\kappa(s-u)} dW(u).$$
 (20.31)

This is again clearly a *Gaussian* random variable, with  $E^{Q}[r(s)|\mathcal{F}_{t}] = \theta + (r(t) - \theta)e^{-\kappa(s-t)}$ . and conditional variance

$$\operatorname{Var}[r(s)|\mathcal{F}_t] = \frac{\sigma_r^2}{2\kappa} (1 - e^{-2\kappa(s-t)}). \tag{20.32}$$

**Quick calculation 20.4** Use *Itô*-isometry to compute  $\text{Var}[r(s)|\mathcal{F}_t]$ .

The *Vasicek*-model is also a *Gaussian* short rate model, but its long-term characteristics are very different from those of our toy model. In particular, we have

$$\lim_{s \to \infty} E^{Q}[r(s)] = \theta \quad \text{and} \quad \lim_{s \to \infty} \text{Var}[r(s)] = \frac{\sigma_{r}^{2}}{2\kappa}.$$
 (20.33)

Most importantly, the variance tends to a finite constant in the long run. There is still a nonzero probability for the short rate to become negative, but it is usually small. In the long-term equilibrium this probability is

$$P(r(\infty) \le 0) = 1 - \Phi\left(\frac{\sqrt{2\kappa}\theta}{\sigma_r}\right),\tag{20.34}$$

where  $\Phi(x)$  is again the cumulative distribution function of a standard normally distributed random variable  $X$ .

#### **Quick calculation 20.5** Prove equation (20.34).

In order to compute bond prices, we follow the same pattern as conducted in case of our toy example. In particular, we have

$$-\int_{t}^{T} r(s)ds = -\theta \int_{t}^{T} ds - (r(t) - \theta) \int_{t}^{T} e^{-\kappa(s-t)}ds - \sigma_{r} \int_{t}^{T} \int_{t}^{s} e^{-\kappa(s-u)}dW(u)ds$$
  
$$= -\theta(T-t) - (r(t) - \theta) \frac{1 - e^{-\kappa(T-t)}}{\kappa} + \frac{\sigma_{r}}{\kappa} \int_{t}^{T} (e^{-\kappa(T-s)} - 1)dW(s),$$
  
(20.35)

where we have switched the order of integration in the last integral. The left hand side of  $(20.35)$  is again a *Gaussian* random variable with conditional expectation value given by the first two terms on the right hand side. The variance is obtained with the help of *Itô*-isometry,

$$\text{Var}\left[-\int_{t}^{T} r(s)ds\middle|\mathcal{F}_{t}\right] = \frac{\sigma_{r}^{2}}{\kappa^{2}}\int_{t}^{T} \left(e^{-\kappa(T-s)} - 1\right)^{2}ds$$
  
$$= \frac{\sigma_{r}^{2}}{\kappa^{2}} \cdot \frac{-e^{-2\kappa(T-t)} + 4e^{-\kappa(T-t)} + 2\kappa(T-t) - 3}{2\kappa}.$$
 (20.36)

As before, the discount bond price is the risk-neutral conditional expectation with respect to a log-normal random variable, and one obtains

$$E^{Q}\left[e^{-\int_{t}^{T}r(s)ds}\Big|\mathcal{F}_{t}\right] = \exp\left(-\theta(T-t) - \left(r(t) - \theta\right)\frac{1 - e^{-\kappa(T-t)}}{\kappa} + \frac{\sigma_{r}^{2}}{\kappa^{2}} \cdot \frac{-e^{-2\kappa(T-t)} + 4e^{-\kappa(T-t)} + 2\kappa(T-t) - 3}{4\kappa}\right).$$
(20.37)

That is a very messy equation, so let's see if we can clean it up a little. Let's define the auxiliary functions

$$A(t,T) = \left(\theta - \frac{\sigma_r^2}{2\kappa^2}\right) ((T-t) - B(t,T)) + \frac{\sigma_r^2}{4\kappa} B(t,T)^2 \tag{20.38}$$

$$B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}.$$
 (20.39)

With these functions, the discount bond price can be expressed very neatly as

$$P(t,T) = e^{-A(t,T) - B(t,T)r(t)}.$$
(20.40)

**Quick calculation 20.6** Check that  $A(T, T) = B(T, T) = 0$  holds.

That should ring an enormous bell. The *Vasicek*-model belongs to an affine term structure model class. We will learn more about this class later. It contains a number of term structure models, but not all of them. For the moment, let's continue with our analysis. The yield curve has the form

$$y(t,T) = -\frac{\log P(t,T)}{T-t} = \frac{A(t,T) + B(t,T)r(t)}{T-t}.$$
 (20.41)

It is not difficult to see from (20.38) and (20.39) that in the limit  $T \rightarrow \infty$ , the yield to maturity tends to

$$\lim_{T \to \infty} y(t, T) = \theta - \frac{\sigma_r^2}{2\kappa^2}.$$
 (20.42)

This is progress, because now the long-term yield tends to a fixed quantity, as observed in the market. Furthermore, some tedious but not difficult algebra shows that the yield curve can have three different shapes:

3. decreasing for  $r(t) > \theta$ .

![](_page_8_Figure_1.jpeg)

**Fig. 20.2** Possible yield curve shapes in the *Vasicek*-model – Increasing (black), humped (gray), and decreasing (dashed)

Figure 20.2 illustrates the three possible shapes of the yield curve *y*(0, *T*) in the *Vasicek*model. You might already suspect that even though we made considerable progress, the *Vasicek*-model is still not capable of reproducing all yield curve shapes observed in the market. This assessment is correct, but we can use the same trick as in our toy model to improve the situation. Namely, we can introduce an auxiliary function *a*(*t*) into the solution (20.31), and derive the required form of this function to match all observed discount bond prices. The result is the so-called *Hull–White*-extended *Vasicek*-model, and we will look into it shortly. In the meantime, let's concern ourselves with bond option pricing in the *Vasicek*-model.

## **20.4 Bond Option Pricing and the Jamshidian-Decomposition**

Suppose today is time *t*, and we want to price a European plain vanilla option with expiry *T* on a discount bond with maturity *S*, for *t* < *T*< *S*. Even though it might not seem so, this is a very trivial exercise. From our *T*-forward measure trick, we computed the price of a call option with strike price *K* in Example 19.1 on page 446. Our result was

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$C_t(K,T) = P(t,S)\Phi(d_+) - P(t,T)K\Phi(d_-). \tag{20.44}$$

It is easy to see that from the same chain of arguments, the put price is

$$P_t(K,T) = P(t,T)K\Phi(-d_-) - P(t,S)\Phi(-d_+). \tag{20.45}$$

What we do not know is what the coefficients *d*+/<sup>−</sup> are in the *Vasicek*-model. More precisely, we do not know the volatility that goes into them. To figure that out, we can either undergo some very demanding computations (see for example Cairns, 2004, appendix B.1), or we can take a clever shortcut. We know that the squared volatility we

are looking for is the variance of the logarithmic *S*-bond price at time *T*, conditional on the knowledge of *r*(*t*). Because of the affine structure of the bond price (20.40), we obtain

$$\operatorname{Var}[\log P(T, S)|\mathcal{F}_t] = B(T, S)^2 \cdot \frac{\sigma_r^2}{2\kappa} (1 - e^{-2\kappa(T - t)}). \tag{20.46}$$

The second factor on the right hand side is simply the conditional variance of *r*(*T*) as in (20.32) on page 461.

**Quick calculation 20.7** Verify the last equation.

We can thus immediately write the desired coefficients,

$$d_{+/-} = \frac{\log\left(\frac{P(t,S)}{P(t,T)K}\right) \pm \frac{1}{2}\sigma_V^2}{\sigma_V} \quad \text{with} \quad \sigma_V = \sigma_r \frac{1 - e^{-\kappa(S-T)}}{\kappa} \sqrt{\frac{1 - e^{-2\kappa(T-t)}}{2\kappa}}. \tag{20.47}$$

Let's now turn to a problem we were not able to address so far: The pricing of on option on a coupon-bearing bond.

To get an idea why it is so difficult to price a coupon bond option, let's assume that the bond pays coupons at a rate *c* on a unit principal, and that it has a swap-like tenor structure *T*0, . . . ,*TN*, with the first coupon payment at *T*1. Then the payoff of a plain vanilla European call option, expiring at *T*0, is

$$C_{T_0}(K, T_0) = \left(c\sum_{n=1}^N P(T_0, T_n) + P(T_0, T_N) - K\right)^+.$$
 (20.48)

We cannot pull the individual discount bonds out of the payoff function, and thus we are in a similar situation as before, when we were trying to price a swaption. But this time, inventing a new probability measure does not do the trick. An ingenious solution to this problem was suggested by Jamshidian (1989), and is now known as the *Jamshidian*-decomposition. To make the important point clear, we have to modify our notation temporarily. The discount bond prices in (20.48) depend on the short rate *r*(*T*0) = *r*0. So let's indicate this dependence by writing *P*(*T*0,*Tn*,*r*0) for *n* = 1, . . . , *N*. Since the discount bond price is a strictly monotonic decreasing function of *r*0, we can find a unique *r* ∗ , which solves the problem

$$c\sum_{n=1}^{N}P(T_{0},T_{n},r^{*})+P(T_{0},T_{N},r^{*})=K.$$
(20.49)

Of course this very special *r* <sup>∗</sup> has to be found by numerical root search. But that is a small price, because the problem is well posed and there is only one independent variable. The problem is indeed completely analogous to determining the yield to maturity of a coupon-bearing bond. Now define a sequence of synthetic strike prices

$$K_n = P(T_0, T_n, r^*), \tag{20.50}$$

such that due to (20.49)

$$c\sum_{n=1}^{N}K_{n}+K_{N}=K$$
 (20.51)

holds. With these synthetic strikes, we can reexpress the payoff function (20.48) as

$$C_{T_0}(K,T_0) = \left( c \sum_{n=1}^N (P(T_0,T_n,r_0) - K_n) + (P(T_0,T_N,r_0) - K_N) \right)^+.$$
 (20.52)

The heart of this payoff function is a sequence of differences of the form *P*(*T*0,*Tn*,*r*0) − *P*(*T*0,*Tn*,*r* ∗ ). Because of the monotonicity of the discount bond prices with respect to the short rate, all of these terms are either positive, if *r* <sup>∗</sup> > *r*0, or they are all smaller than or equal to zero, for *r* <sup>∗</sup> ≤ *r*0. In consequence the maximum bracket becomes distributive and we can write

$$C_{T_0}(K,T_0) = c \sum_{n=1}^{N} (P(T_0,T_n) - K_n)^+ + (P(T_0,T_N) - K_N)^+.$$
 (20.53)

But this is merely the payoff of a portfolio of discount bond options, and we already know how to price them analytically. Of course the same trick works for put options, in fact the synthetic strike prices *K<sup>n</sup>* are identical. Furthermore, the *Jamshidian*decomposition is not limited to the *Vasicek*-model, it works for every one-factor term structure model. We finally state the general pricing formula for time *t* < *T*<sup>0</sup> for European plain vanilla bond options

$$V_t^B(K, T_0) = c \sum_{n=1}^N V_t^P(K_n, T_0) + V_t^P(K_N, T_0), \qquad (20.54)$$

with the superscripts *B* and *P* referring to the ordinary and discount bond, respectively. The synthetic strikes *K<sup>n</sup>* are precisely as in (20.50) for *n* = 1, . . . , *N*.

**Quick calculation 20.8** Which modifications have to be made, if the principal is not normalized?

## **20.5 Affine Term Structure Models**

There have been many one-factor short rate models suggested over time; a small collection is reproduced in Table 20.1. Not all of them possess an affine term structure (ATS). Such a structure has the great advantage that discount bond prices can be computed

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

| Table 20.1<br>Popular one-factor short rate models |                                                                                         |          |     |
|----------------------------------------------------|-----------------------------------------------------------------------------------------|----------|-----|
| Model                                              | Dynamics                                                                                | Dist.a   | ATS |
| Ho and Lee (1986)                                  | = θ(t)dt<br>+ σdWt<br>drt                                                               | N        | Yes |
| Vasicek (1977)                                     | −<br>= κ(θ<br>rt)dt + σdWt<br>drt                                                       | N        | Yes |
| Hull and White (1990)                              | −<br>= κ<br>θ(t)<br>dt + σdWt<br>drt<br>rt<br>(<br>)                                    | N        | Yes |
| Cox et al. (CIR, 1985)                             | √<br>−<br>= κ(θ<br>rt)dt + σ<br>drt<br>rtdWt                                            | 2<br>NCχ | Yes |
| Dothan (1978)                                      | = θrtdt<br>+ σrtdWt<br>drt                                                              | LN       | No  |
| Black et al. (BDT, 1990)                           | ′<br>σ<br>(t)<br>θ(t)<br>dt + σ(t)dWt<br>d log rt<br>=<br>+<br>log rt<br>(<br>)<br>σ(t) | LN       | No  |
| Black and Karasinski (1991)                        | −<br>= κ(t)<br>θ(t)<br>dt + σ(t)dWt<br>d log rt<br>log rt<br>(<br>)                     | LN       | No  |

*<sup>a</sup>* The distribution of *r<sup>t</sup>* is either normal (N), log-normal (LN), or non-central chi-squared (NCχ 2 ).

as soon as the functions *A*(*t*,*T*) and *B*(*t*,*T*) are known. What are the requirements for a short rate model to belong to the affine class? The answer is provided by the following theorem:

**Theorem 20.1 (Affine term structure)** *Suppose the short rate dynamics are governed by a general model of the form*

$$dr = \theta(r, t)dt + \sigma(r, t)dW.$$

*This model has affine term structure, if and only if the squared diffusion and drift functions are of the form*

$$\sigma(r, t)^2 = a(t) + \alpha(t)r$$
 and  $\theta(r, t) = b(t) + \beta(t)r$ ,

*for some smooth functions a*(*t*)*, b*(*t*)*,* α(*t*)*,* β(*t*)*, and A*(*t*,*T*) *and B*(*t*,*T*) *satisfy the differential equation system*

$$\begin{aligned} \frac{\partial}{\partial t}A(t,T) &= \frac{1}{2}a(t)B(t,T)^2 - b(t)B(t,T),\\ \frac{\partial}{\partial t}B(t,T) &= \frac{1}{2}\alpha(t)B(t,T)^2 - \beta(t)B(t,T) - 1, \end{aligned}$$

*for all t* <*T*, *with A*(*T*,*T*) = *B*(*T*,*T*) = 0.

A proof of this theorem can be found in Filipović (2009, p. 84). Let's see, if we can figure out what the functions *A*(*t*,*T*) and *B*(*t*,*T*) are in the *Ho–Lee*-model (20.17) on page 458. We have obviously

$$a(t) = \sigma_r^2 \quad \text{and} \quad b(t) = \theta(t), \tag{20.55}$$

and the remaining functions  $\alpha(t) = \beta(t) = 0$ . That reduces the second differential equation to  $\frac{\partial}{\partial t}B(t,T) = -1$ , with the obvious solution

$$B(t,T) = T - t. \t(20.56)$$

**Ouick calculation 20.9** Use  $B(T, T) = 0$  to confirm this result.

Solving the first differential equation is a pure integration exercise. We have

$$A(t,T) = -\int_{t}^{T} dA(s,T) = -\frac{1}{2}\sigma_{r}^{2}\int_{t}^{T} (T-s)^{2}ds + \int_{t}^{T} \theta(s)(T-s)ds.$$
 (20.57)

For a known yield curve  $y(0, T)$ , we know from (20.22) that

$$\theta(t) = \frac{\partial f(0, t)}{\partial t} + \sigma_r^2 t \tag{20.58}$$

holds. That makes  $(20.57)$ 

$$A(t,T) = \frac{1}{2}\sigma_r^2 \left(2\int_t^T s(T-s)ds - \int_t^T (T-s)^2 ds\right) + \int_t^T \frac{\partial f(0,s)}{\partial s}(T-s)ds$$
  
$$= \frac{1}{2}\sigma_r^2 t(T-t)^2 + \int_t^T \frac{\partial f(0,s)}{\partial s}(T-s)ds.$$
  
(20.59)

The easiest way to verify the second equality is to reverse engineer the integration procedure

$$t(T-t)^{2} = -\left[s(T-s)^{2}\right]_{t}^{T} = -\int_{t}^{T} \left(\frac{d}{ds}s(T-s)^{2}\right)ds.$$
 (20.60)

Computing the derivative in the integral exactly reproduces the bracket in  $(20.59)$ . Let's now turn to the integral involving the derivative of the forward rate. This one can be computed using integration by parts.

$$\int_{t}^{T} \frac{\partial f(0,s)}{\partial s} (T-s) ds = f(0,s)(T-s) \Big|_{t}^{T} + \int_{t}^{T} f(0,s) ds$$
  
$$= -f(0,t)(T-t) + \int_{t}^{T} f(0,s) ds.$$
 (20.61)

Summarizing our results, we have

$$A(t,T) = \frac{1}{2}\sigma_r^2 t(T-t)^2 - f(0,t)(T-t) + \int_t^T f(0,s)ds.$$
 (20.62)

We can now express the discount bond price  $P(t, T)$ , calibrated to the yield curve  $y(0, T)$ as

$$P(t,T) = e^{-A(t,T)-B(t,T)r(t)} = \frac{P(0,T)}{P(0,t)}e^{-\frac{1}{2}\sigma_r^2 t(T-t)^2}e^{-x(t)(T-t)},\tag{20.63}$$

where we have again used the definition  $x(t) = r(t) - f(0, t)$ . But this is exactly Equation  $(20.23)$ , we derived earlier. So obviously, our computations were correct; we only used the much more elegant ATS-framework.

467

Let's review two more standard one-factor short rate models, the *Hull–White*extended *Vasicek*-model (Hull and White, 1990), and the *Cox–Ingersoll–Ross*-model (CIR, Cox et al., 1985). The first one is simply a yield curve fitted version of the original *Vasicek*-model,

$$dr(t) = \kappa(\theta(t) - r(t))dt + \sigma_r dW(t). \tag{20.64}$$

The *Hull–White*-version is still a *Gauss*ian short rate model and interest rates therefore can become negative. But it can now be calibrated to the initial yield curve *y*(0,*T*). The required function has the form

$$\theta(t) = f(0, t) + \frac{1}{\kappa} \frac{\partial f(0, t)}{\partial t} + \frac{\sigma_r^2}{2\kappa^2} (1 - e^{-2\kappa t}). \tag{20.65}$$

The ATS-functions can be computed in the usual way and one obtains

$$A(t,T) = \frac{\sigma_r^2}{2\kappa^2} (B(t,T) - (T-t)) + \frac{\sigma_r^2}{4\kappa} B(t,T)^2 + \kappa \int_t^T \theta(s) B(s,T) ds \qquad (20.66)$$

$$B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}.$$
 (20.67)

Solving the integral in (20.66) is not an easy task, but it can be done. In this case, one may reexpress the function *A*(*t*,*T*) as

$$A(t,T) = \int_{t}^{T} f(0,s)ds - f(0,t)B(t,T) + \frac{\sigma_r^2}{4\kappa}B(t,T)^2(1 - e^{-2\kappa t}).$$
 (20.68)

A proof for the most general form of the mean reverting *Gauss*ian model can be found in Andersen and Piterbarg (2010b, p. 416). Of course the integral over the forward rate reproduces the characteristic discount bond ratio, and one obtains

$$P(t,T) = \frac{P(0,T)}{P(0,t)} \exp\left(-\frac{\sigma_r^2}{4\kappa} \left(\frac{1 - e^{-\kappa(T-t)}}{\kappa}\right)^2 (1 - e^{-2\kappa t}) - x(t) \frac{1 - e^{-\kappa(T-t)}}{\kappa}\right),\qquad(20.69)$$

where we have again used our definition *x*(*t*) = *r*(*t*) − *f*(0, *t*).

The *Cox–Ingersoll–Ross*- or CIR-model for short is also a mean reverting specification, that looks very similar to the *Vasicek*-model at first sight,

$$dr(t) = \kappa(\theta - r(t))dt + \sigma_r \sqrt{r(t)}dW(t). \qquad (20.70)$$

But both processes are actually very different on the theoretical level already. The *Vasicek*-dynamics are clearly driven by a scaled *Brown*ian motion, whereas the CIRdynamics are linked to the class of squared *Bessel*-processes. If the stability condition 2κθ ≥σ 2 *r* is satisfied, the short rate remains positive almost surely, and the CIR-process has a stationary gamma distribution, with probability density function

$$f(r) = \frac{\beta^{\alpha}}{\Gamma(\alpha)} r^{\alpha - 1} e^{-\beta r},\tag{20.71}$$

with

$$\alpha = \frac{2\kappa\theta}{\sigma_r^2} \quad \text{and} \quad \beta = \frac{2\kappa}{\sigma_r^2}.$$
 (20.72)

Moreover, the distribution of *r*(*s*), conditional on the information F*<sup>t</sup>* for *s* > *t*, is noncentral χ 2 , as proved by Feller (1951). After spending so much time with *Gauss*ian processes, these properties may appear rather exotic. Nevertheless, the CIR-model is a member of the ATS-class, and its affine functions (see for example Filipović, 2009, p. 87) are

$$A(t,T) = -\frac{2\kappa\theta}{\sigma_r^2} \log\left(\frac{\gamma e^{\frac{\gamma+\kappa}{2}(T-t)}}{e^{\gamma(T-t)}-1}B(t,T)\right)$$
(20.73)

$$B(t,T) = \frac{2(e^{\gamma(T-t)}-1)}{(\gamma+\kappa)(e^{\gamma(T-t)}-1)+2\gamma},\tag{20.74}$$

with γ = √ κ <sup>2</sup> + 2σ 2 *r* . The CIR-model can also be calibrated to a particular yield curve as shown by Hull and White (1990).

Although those models are a great deal more realistic than our initial toy model, they are at best appropriate in some particular situations. There are still rather severe shortcomings. To calibrate the model for example to observed caplet prices, we would need a more elaborate term structure of volatility. Furthermore, the one-factor paradigm limits our ability to model structural changes in the yield curve. This is a very tough restriction when dealing with products whose payoff function depends on the shape of the yield curve. Those problems can be remedied by considering multi-factor models with the necessary degrees of freedom. Unfortunately those models are nowhere near as tractable as the one-factor models we analyzed so far. We will eventually deal with multi-factor specifications, but we will do it in a modern framework to be introduced next.

## **20.6 The Heath–Jarrow–Morton-Framework**

In 1992, Heath et al. introduced a general framework for interest rate models that caused a paradigm shift, which by no means came without resistance. The idea of the *Heath–Jarrow–Morton*- or HJM-framework for short, is not to ask how the short end of the forward curve evolves with time, but instead to identify the dynamics governing

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

the evolution of the entire forward curve itself. This was a very bold attempt and they succeeded. Let's first try to catch the idea behind the HJM-derivation by once again using our short rate toy model

$$dr(t) = \sigma_r dW(t). \tag{20.75}$$

We have already determined the forward curve in  $(20.15)$  on page 457 to have the form

$$f(t,T) = r(t) - \frac{1}{2}\sigma_r^2(T-t)^2.$$
 (20.76)

Now let's apply Itô's lemma to compute the dynamics of the forward curve. This is a trivial task in our toy model and we obtain

$$df(t,T) = \sigma_r^2(T-t)dt + \sigma_r dW(t). \tag{20.77}$$

Recognize that  $(20.77)$  indeed describes the dynamics of a whole curve. If we simulate the appropriate *Wiener*-increments, time t would progress, but for every arbitrary  $t^*$ , we can draw a curve with respect to the variable T for  $t^* \leq T < \infty$ .

It is often awkward to work in terms of maturity dates T, instead of time to maturity  $\tau = T - t$ . Therefore, one can use a slightly different form, called the *Musiela*parametrization

$$f_M(t,\tau) = f(t,t+\tau).$$
 (20.78)

Inspecting (20.78) closely, reveals that the maturity date  $T$  is now expressed as a function of t, which means  $T = t + \tau$ . Applying Itô's lemma and using the chain rule, the dynamics of  $f_M(t, \tau)$  becomes

$$df_M(t,\tau) = \frac{\partial f_M}{\partial f} df(t,T) + \frac{\partial f_M}{\partial \tau} \frac{\partial \tau}{\partial T} \frac{\partial T}{\partial t} dt$$
  
=  $df(t,T) + \frac{\partial f}{\partial T} dt,$  (20.79)

where we used that  $\frac{\partial T}{\partial t} = 1$ . That is, the dynamics of our toy forward curve (20.77) under the *Musiela*-parametrization becomes

$$df_M(t,\tau) = \sigma_r dW(t). \tag{20.80}$$

### **Quick calculation 20.10** Use $(20.76)$ to verify this result.

This result may seem even more awkward, but it is perfectly alright. In particular it does not mean that the forward curve  $f_M(t,\tau)$  is flat, it only says that the curve changes for every time to maturity by the same amount. This is the true meaning of a parallel curve shift. To make this point perfectly clear, substitute  $T = t + \tau$  in (20.76). The result is

$$f_M(t,\tau) = r(t) - \frac{1}{2}\sigma_r^2 \tau^2.$$
 (20.81)

This equation depends on *t* only through the short rate *r*(*t*). Thus, an application of Itô's lemma yields the trivial result

$$df_M(t,\tau) = dr(t). \tag{20.82}$$

Let's now turn to the real thing, the derivation of the HJM-framework. Suppose the general risk-neutral dynamics of the discount bond is given by

$$dP(t,T) = r(t)P(t,T)dt + \sigma_P(t,T)P(t,T)dW(t), \qquad (20.83)$$

with the consistency condition σ*P*(*T*,*T*) = 0. The drift under the risk-neutral measure *Q* has to be *r*(*t*) for all securities in the market. There are some other requirements regarding the integrability of σ*P*(*t*,*T*), we will not discuss at this point, even though they are by no means mere technicalities. In fact, the problems they cause under certain conditions eventually led to the development of market models, which we will encounter in the next chapter. For the moment, we just assume everything is smooth and well behaved. The forward rate is linked to the discount bond price by

$$f(t,T) = -\frac{\partial}{\partial T} \log P(t,T).$$
 (20.84)

So let's again apply Itô's lemma to determine the dynamics of the forward rate

$$df(t,T) = -\frac{\partial}{\partial T}\left(r(t) - \frac{1}{2}\sigma_P(t,T)^2\right)dt - \frac{\partial}{\partial T}\sigma_P(t,T)dW(t). \tag{20.85}$$

From this result we can already conclude that the forward rate volatility has to be

$$\sigma_f(t,T) = -\frac{\partial}{\partial T}\sigma_P(t,T). \tag{20.86}$$

Let's now examine the bracket in (20.85) a little bit closer. The derivative of the short rate *r*(*t*) with respect to *T* vanishes, because the short rate does not depend on the maturity of the discount bond. Using (20.86), we can rewrite the *T*-derivative of the second term as

$$\begin{split} \frac{\partial}{\partial T} \frac{1}{2} \sigma_P(t,T)^2 &= \sigma_P(t,T) \frac{\partial}{\partial T} \sigma_P(t,T) \\ &= \left(\frac{\partial}{\partial T} \sigma_P(t,T)\right) \int_t^T \frac{\partial}{\partial s} \sigma_P(t,s) ds \\ &= \sigma_f(t,T) \int_t^T \sigma_f(t,s) ds. \end{split} \tag{20.87}$$

In the second step, we have used that σ*P*(*t*, *t*) = 0 holds. We can thus write the celebrated HJM-condition for the risk-neutral forward rate dynamics

$$df(t,T) = \sigma_f(t,T) \int_t^T \sigma_f(t,s) ds dt + \sigma_f(t,T) dW(t). \tag{20.88}$$

The truly amazing thing about this equation is that even though the HJM-framework contains a multiverse of possible forward rate models, the dynamics of each of them are entirely governed by the specified volatility.

We have implicitly assumed that  $\sigma_P(t,T)$  and therefore  $\sigma_f(t,T)$  is deterministic, even though this restriction is not necessary for the HJM-condition to hold. It is sufficient to require  $\sigma_P(t,T)$  regular enough for  $\frac{P(t,T)}{B(t)}$  to be a square-integrable martingale, where  $B(t)$  is our usual bank account. However, deterministic volatility leads to the very tractable class of Gaussian HJM-models. But even within this class, we have to discuss an important subtlety, the so-called *Markov*-property. A *Markov*-process is special in that it stores all past information in the present state of the process itself. To see what that means, we can for example take the conditional expectation value. If  $X_t$ is a *Markov*-process, then we must have

$$E[X_t|\mathcal{F}_s] = f(X_s),\tag{20.89}$$

for  $t \ge s$  and a suitable function  $f: \mathbb{R} \to \mathbb{R}$ . Of course an analogous property holds for the entire conditional distribution, not only for the expectation value. But from the expectation we can deduce that a martingale is even more special than a *Markov*-process, in that it requires  $f(x) = x$ . We have used *Markov*-processes dozens of times, without even mentioning it. So why discuss them now? The *Itô*-process, which is the foundation of almost all dynamic processes we have discussed in this book, is a *Markov*-process. If we want to use specifications of this type any further, we have to understand under which conditions the HJM-framework breeds *Markovian* models. To this end, let's investigate the short rate in the HJM-framework. Using  $r(t) = f(t, t)$  and integrating (20.88) yields

$$r(t) = f(0, t) + \int_0^t \sigma_f(u, t) \int_u^t \sigma_f(u, s) ds du + \int_0^t \sigma_f(u, t) dW(u). \tag{20.90}$$

The delicate term in this equation is the last one on the right hand side. So let's give it a name to analyze it a little further,

$$X_t = \int_0^t \sigma_f(u, t) dW(u). \tag{20.91}$$

First of all, think of the volatility  $\sigma_t(u,t)$  as a family of functions with independent variable  $u$ , and the particular member of the family indicated by  $t$ .

**Quick calculation 20.11** Show that  $X_t$  is not a martingale.

If we compute the expectation of  $X_t$ , conditional on the information at time  $s < t$ , we obtain

$$E^{Q}[X_{t}|\mathcal{F}_{s}] = \int_{0}^{s} \sigma_{f}(u, t)dW(u) \neq f(X_{s}). \tag{20.92}$$

The volatility function in  $(20.92)$  is simply from the wrong family. The random variable  $X_{s}$  contains the volatility function  $\sigma_{f}(u, s)$ , which means the s-member of the family, not the *t*-member. This seems hopeless, but it is not. All that is necessary to manufacture *Markovian* dynamics is a particular condition on the volatility function. If  $\sigma_f(u, t)$  has the form

$$\sigma_f(u,t) = g(u)h(t), \tag{20.93}$$

then the resulting HJM-model generates a *Markovian* short rate process. Let's see if we can prove this statement. With the condition (20.93), our process  $X_t$  becomes

$$X_t = h(t) \int_0^t g(u) dW(u).$$
 (20.94)

So let's see if the *Markovian* condition is now satisfied. Again computing the conditional expectation yields

$$E[X_t|\mathcal{F}_s] = h(t) \int_0^s g(u)dW(u) = \frac{h(t)}{h(s)} X_s.$$
 (20.95)

That is, the right hand side of (20.95) is clearly a function of  $X_s$  and hence  $X_t$  is a Markov-process.

**Quick calculation 20.12** Verify that  $\sigma_{t}(t, T) = \sigma e^{-\kappa(T-t)}$  generates a *Markovian* model.

Most of the commonly used short rate models have a HJM-representation, but not all of them. The way HJM-modeling works is a kind of reverse engineering principle. One fixes the forward volatility structure and then determines the properties of the resulting model. Let's demonstrate this principle within the simplest possible specification

$$\sigma_f(t,T) = \sigma. \tag{20.96}$$

Using  $(20.88)$ , the forward rate dynamics are easily computed,

$$df(t,T) = \sigma^2(T-t)dt + \sigma dW(t). \tag{20.97}$$

Since (20.96) clearly induces a *Markovian* structure, choose for example  $g(t) = \sigma$  and  $h(T) = 1$ , we should be able to derive conventional short rate dynamics. Let's first integrate  $(20.97)$  to see what the forward rate eventually looks like

$$f(t,T) = f(0,T) + \sigma^2 \int_0^t (T-s)ds + \sigma \int_0^t dW(s)$$
  
=  $f(0,T) - \frac{1}{2}\sigma^2(T-t)^2 + \frac{1}{2}\sigma^2T^2 + \sigma W(t).$  (20.98)

Recall that the short rate and the forward rate are related through  $r(t) = f(t, t)$ . Therefore, we must have

$$dr(t) = df(t, T)\Big|_{T=t} + \frac{\partial f(t, T)}{\partial T}\Big|_{T=t} dt$$
  
=  $\sigma dW(t) + \left(\frac{\partial f(0, t)}{\partial t} + \sigma^2 t\right) dt,$  (20.99)

which is exactly the  $Ho-Lee$ -specification. What we can learn from this maybe surprising result is that HJM-models are automatically calibrated to the initial yield curve. There is nothing we have to do to force the issue. By choosing the volatility specification

$$\sigma_f(t,T) = \sigma e^{-\kappa(T-t)},\tag{20.100}$$

one obtains the *Hull–White*-extended *Vasicek*-model (for a general proof see Andersen and Piterbarg, 2010a, p. 188).

Staying within the class of *Gauss*ian HJM-models has another advantage. We know that the forward rate *f*(*t*,*T*) is a *QT*-martingale, with *f*(*T*, *T*) = *r*(*T*). On the other hand, we know that the future rate is a *Q*-martingale. Therefore, the connection between forward and future rates in the *Gauss*ian HJM-framework has to be

$$E^{Q_T}[r(T)|\mathcal{F}_t] = E^Q[r(T)|\mathcal{F}_t] - \int_t^T \sigma_f(u,T) \int_u^T \sigma_f(u,s) ds du. \tag{20.101}$$

The last term on the right hand side is called the **convexity adjustment**. We can see from (20.101) that the future rate is always greater than the forward rate, which confirms the heuristic argument about daily settlement, we introduced earlier. Furthermore, we can now understand, why for deterministic term structure both rates coincide. This is simply because the volatility vanishes. And finally, it is now very clear that the convexity adjustment is model dependent. It changes with the volatility specification we use. If we take for example σ*f*(*t*,*T*) =σ, then the convexity adjustment is

Convexity adjustment = 
$$\frac{1}{2}\sigma^2(T-t)^2$$
. (20.102)

**Quick calculation 20.13** Verify this result.

Let's finally state the HJM-equation in terms of the time to maturity τ = *T* − *t*, using the *Musiela*-parametrization. We already know that the dynamics of *fM*(*t*, τ) has the form

$$df_M(t,\tau) = df(t,T) + \frac{\partial f}{\partial T}dt.$$
 (20.103)

Using the chain rule on the partial derivative, we have

$$\frac{\partial f}{\partial T} = \frac{\partial f_M}{\partial \tau} \frac{\partial \tau}{\partial T} = \frac{\partial f_M}{\partial \tau},\tag{20.104}$$

because ∂τ ∂*T* = 1. Defining the corresponding volatility function

$$\sigma_M(t,\tau) = \sigma_f(t,t+\tau),\tag{20.105}$$

we can express the HJM-equation in terms of the *Musiela*-parametrization

$$df_M(t,\tau) = \frac{\partial f_M(t,\tau)}{\partial \tau} dt + \sigma_M(t,\tau) \int_0^\tau \sigma_M(t,s) ds dt + \sigma_M(t,\tau) dW(t). \tag{20.106}$$

This is far more convenient to use in practice, because all rates quoted in the market are with respect to a fixed tenor, not a date. Figure 20.3 illustrates a simulated evolution of the *Musiela*-parametrized forward curve, based on the volatility structure (20.100).

![](_page_20_Figure_1.jpeg)

**Fig. 20.3** 3D Simulated forward rate surface under *Musiela*-parametrization

Figure 20.4 shows the dynamics in three different τ-slices. It is not hard to see that if the short rate drops, the rates for all larger tenors decrease, too, even though by a smaller amount. The same is true for rising short rates. As mentioned earlier, this is the result of using a one-factor model. The changes in the forward curve for different tenors are all perfectly correlated. This is of course not what we are observing in the market. Thus, we have to talk about choosing a realistic HJM-model and calibrating it to historical market data.

## **20.7 Multi-Factor HJM and Historical Volatility**

We are now entering the world of multi-factor term structure models, and we will do it inside the most general HJM-framework. We have already learned that the properties of a specific HJM-model solely depend on the choice of the volatility function. We have therefore to answer two questions. First, how many factors should we take into

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

![](_page_20_Figure_7.jpeg)

**Fig. 20.4** Time evolution of forward rates for different tenors

account? And second, which volatility structure is appropriate for the particular factors? At this point, the discussion may seem pretty abstract. Therefore, let us first state the multi-factor version of the HJM-equation

$$df(t,T) = \sum_{q=1}^{Q} \sigma_q(t,T) \int_t^T \sigma_q(t,s) ds dt + \sum_{q=1}^{Q} \sigma_q(t,T) dW_q(t), \qquad (20.107)$$

with mutually uncorrelated *Wiener*-increments  $dW_a(t)$ , for  $q = 1, \ldots, Q$ . It is straightforward to state those dynamics under the *Musiela*-parametrization

$$df_M(t,\tau) = \frac{\partial f_M(t,\tau)}{\partial \tau} dt + \sum_{q=1}^{Q} \sigma_q(t,\tau) \int_0^{\tau} \sigma_q(t,s) ds dt + \sum_{q=1}^{Q} \sigma_q(t,\tau) dW_q(t), \quad (20.108)$$

where we have omitted the subscript  $M$  of the volatility functions, to simplify the notation. To require that all *Wiener*-increments are uncorrelated is the connection to classical factor analysis. Because  $dW(t)$  is normally distributed, uncorrelated means independent. That is, the forward rate is driven by  $Q$  orthogonal random factors. So let's see, how we get our hands on those factors.

To analyze the structure of the forward rate volatility, yield curve data for Treasury bonds from 2010 to the end of 2014, recorded by the US Department of the Treasury, was used. The times to maturity  $\tau_n$  are 1, 2, 3, 5, 7, 10, 20, and 30 years. From this data, the forward rates  $f(t, \tau_n)$  were computed using (18.44) on page 434, with the differential approximated by a forward difference. The variance in the change of the forward rate for a particular time to maturity  $\tau_n$  according to (20.108) is

$$\operatorname{Var}[df_M(t,\tau_n)] = \sum_{q=1}^{Q} \sigma_q(t,\tau_n)^2 dt.$$
 (20.109)

The important quantity is the scaling factor  $dt$ . Of course we cannot observe arbitrary small changes in the forward curve, and thus we have to approximate  $df_M(t,\tau_n)$  by  $\Delta f_M(t,\tau_n)$  and dt by  $\Delta t$ . In this case, daily data was used, and therefore  $\Delta t = \frac{1}{252}$ . Let  $\hat{S}$  be the *N*-dimensional empirical covariance matrix, estimated from the forward rate difference data  $\Delta f_M(t, \tau_n)$  for  $n = 1, \dots, N$ . Then the correct estimator for the annualized covariance matrix of the observed rates is

$$\hat{\Sigma} = \frac{1}{\Delta t} \hat{S}.\tag{20.110}$$

The matrix  $\hat{\Sigma}$  is symmetric and positive definite, and therefore we have a complete set of positive eigenvalues and orthogonal eigenvectors. Hence, we can apply the spectral decomposition

$$\hat{\Sigma} = V\Lambda V' = \sum_{n=1}^{N} \lambda_n |v_n\rangle\langle v_n|, \qquad (20.111)$$

![](_page_22_Figure_1.jpeg)

**Fig. 20.5** 3D Bivariate standard normal density function with correlation ρ = 0.7 and covariance ellipse

where |*vn*⟩ is the *n*-th normalized eigenvector, which means the *n*-th column of *V*. That is, we have decomposed the estimated covariance matrix into a sum of *N* outer products. If the eigenvalues are ordered along their magnitude, λ*<sup>n</sup>* > λ*n*+1, the contribution from additional terms in the sum becomes smaller and smaller. In statistics this is called principal component analysis. What really happened is that we have rotated the axes such that they coincide with the half-axes of the covariance ellipsoid. This coordinate transformation is illustrated in Figures 20.5 and 20.6 for the two-dimensional case. We can extract the desired factor volatilities immediately at the observed maturities τ*<sup>n</sup>* by

$$\sigma_q(t,\tau_n) = \sqrt{\lambda_q} v_{nq}.\tag{20.112}$$

Those volatilities are indicated by points, squares, and triangles in Figure 20.7 right, for the first three principal components. We have of course to interpolate between the observed maturities. This was done with quadratic splines in the present example. A similar analysis can also be found in Rebonato (2000, sect. 3.1) and Wilmott (2006b, sect. 37.13). They, however, used historical data of the time before the sovereign dept crisis and their first three principal components looked slightly different. In fact, the first one was nearly a perfect straight line, the second one was also nearly straight, but

![](_page_22_Figure_6.jpeg)

**Fig. 20.6** 3D Density function of Figure 20.5 with rotated axes due to principal component analysis

![](_page_23_Figure_1.jpeg)

**Fig. 20.7** Correlation matrix for different times to maturity (left) and first three principal components of the volatility structure (right) – First component (black), second one (gray), and third one (dashed)

with a slope, and the third one had a roughly parabolic shape. This result had a very nice interpretation for the first factor to cause parallel shifts in the yield curve, the second one to affect its slope, and the third one to introduce curvature. These nice shapes are not that striking in our example, but they are still partly recognizable. The correlation structure between the different rates, is indicated schematically in Figure 20.7 left. A correlation of one is represented by a black square, whereas smaller correlations are indicated by the respective gray levels. There is an anomaly in the correlation structure of the 1Y-bond. It seems that it is more strongly correlated with the 3Y-bond than it is with the 2Y-bond. We usually would expect the correlation to be a decreasing function of the difference in time to maturity. There is no logical explanation for this anomaly, as we shall see in the next chapter, except that unconstrained estimated correlation matrices are prone to such artifacts. We will talk about alternative parametric estimation methods that avoid those anomalies, when dealing with market models. For the moment we leave everything as it is and proceed with our analysis.

The question is now, how many factors should we use to represent the entire covariance structure reasonably well? This one can be answered conveniently. The matrix Λ in (20.111) is obviously the covariance matrix of a complete set of *N* random factors *Fn*. Because they are orthogonal, there are no covariance terms and we have

$$\operatorname{Var}\left[\sum_{n=1}^{N} F_{n}\right] = \sum_{n=1}^{N} \lambda_{n} = \langle 1 | \lambda \rangle. \tag{20.113}$$

If we do not include all factors, but say just *Q* < *N*, then the relative proportion of variance explained by the *Q* factors is

Variance explained = 
$$\frac{1}{\langle 1|\lambda \rangle} \sum_{q=1}^{Q} \lambda_q$$
. (20.114)

In our present example, including only the first factor explains 80.3% of the total variance. Adding the second factor accounts for 91.8%. The first three factors altogether

![](_page_24_Figure_1.jpeg)

**Fig. 20.8** 3D Simulated forward rate surface for the historically calibrated 3-factor HJM-model

explain 95.4% of the total variance. Explaining 95% of the total variance is usually considered sufficient, and thus we have to include only three factors.

We are now in a position to simulate the entire forward rate surface, as we have done before. We know the volatility functions in terms of quadratic splines, which means piecewise second order polynomials, that are easily integrated. The result of such a simulation run is illustrated in Figure 20.8. Unlike the *Vasicek*-surface, where the movements of all points on the forward curve were perfectly correlated, the different rates are now decoupled to a certain degree. The result is that the forward curve can bend and twist over time, and can take various different shapes, as seen in Figure 20.9 right, where the surface is sliced several times parallel to the τ-direction. The left illustration in Figure 20.9 shows three different slices parallel to the *t*-direction, which means the time evolution of forward rates with different times to maturity. Although there is considerable correlation, it is not perfect. Furthermore, it is very clear that the mapping *t* 7→ *fM*(*t*, τ) is a stochastic process for all τ, whereas the mapping τ 7→ *fM*(*t*, τ) is

![](_page_24_Figure_5.jpeg)

**Fig. 20.9** Time evolution of forward rates for different times to maturity (left) and several forward curves at different points in time (right)

a smooth function for all  $t$ . A mild warning is advisable here. Even though it is customary to quote and plot rates in percentage values, the true rates and also their volatilities have to be scaled properly. Otherwise, the drift of the forward rate is boosted by a factor of  $10^4$ , whereas the diffusion term only contributes with a factor of  $10^2$ .

**Quick calculation 20.14** Verify this statement by reviewing (20.107) on page 476.

It remains to discuss, how the HJM-model, based on the historical volatility structure, can be used to price non-vanilla contracts. The bad news is pricing has to be done via Monte Carlo simulation, so let's focus on European contracts. In this case an arbitrary claim  $V$ , expiring at time  $T$  can be valued today by

$$V(t,T) = E^{\mathcal{Q}} \left[ e^{-\int_t^T r(s)ds} V(T,T) \middle| \mathcal{F}_t \right]. \tag{20.115}$$

We will eventually again approximate this expectation value by an average value over many simulated forward curve scenarios. There are two elements inside the expectation that depend on the forward rate, the contract V itself, and the discount factor, containing the short rate. Chances are that knowledge of the future forward curve  $f_M(T,\tau)$  is sufficient to know the payoff  $V(T, T)$ , unless V is a second order contract or it has some forward starting features. In this case we would simply simulate the forward curve further into the future, until all necessary information is available. But the discount factor is also a function of the forward curve. To see this, let's rewrite it in a slightly different form

$$e^{-\int_t^T r(s)ds} = e^{-\int_t^T f(s,s)ds} = e^{-\int_t^T f_M(s,0)ds}.$$
 (20.116)

That is, discounting is with respect to the zeroth slice in the  $\tau$ -direction. The best way to see how it works is to look at an example. Let's revisit the bond valuation problem from Example 19.1 on page 446.

Example 20.1

What steps are necessary to price a plain vanilla European call option, expiring at  $T$ , on a discount bond with maturity date S, with  $t < T < S$  in the HJM-framework?

#### Solution

Take the following steps:

- 1. Choose a volatility function  $\sigma_q(t,\tau)$  for all included factors  $q = 1, \ldots, Q$ .
- 2. Extract the latest forward curve  $f_M(t, \tau)$  from market data.
- 3. Simulate the forward curve until time *T* to obtain  $f_M(T, \tau)$ .
- 4. Evaluate the payoff function

$$V^{(n)}(T,T) = \left(e^{-\int_0^{S-T} f_M(T,\tau)d\tau} - K\right)^+.$$

5. Discount the payoff using the short rate

$$V^{(n)}(t,T) = e^{-\int_t^T f_M(s,0)ds} V^{(n)}(T,T).$$

6. Repeat steps 3 to 5 a large number *N* of times and compute the average

$$V(t,T) \approx \frac{1}{N} \sum_{n=1}^{N} V^{(n)}(t,T).$$

This list is generic for all similar pricing problems. ........................................................................................................................

We can see from Example 20.1 that the intermediate forward rates *fM*(*s*, τ) for *t* < *s* <*T* and τ > 0 do not have to be stored, with the exception of the short rate *fM*(*s*, 0). This usually eases the computational burden considerably.

## **20.8 Further Reading**

An impressive collection of one- and multi-factor short rate models can be found in Andersen and Piterbarg (2010b), Brigo and Mercurio (2007), and also Rebonato (2000). The pros and cons of yield curve fitting are discussed in Wilmott (2006b, chap. 31). Jump-extended short rate models can be found in Nawalkha et al. (2007, chap. 5–7). For the derivation and technical details of the HJM-framework, see the original work of Heath et al. (1992), and also Filipović (2009, chap. 6). Consistency requirements are discussed very thoroughly in Filipović (2001). A detailed discussion of possible convexity adjustments can be found in Deutsch (2002, sect. 15.5). Continuous time *Markov*-processes are treated very thoroughly in Aït-Sahalia et al. (2010).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

## **20.9 Problems**

- • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • **20.1** Derive the discount bond volatility σ*P*(*t*,*T*) in the *Vasicek*-model and verify that σ*P*(*T*,*T*) = 0 holds.
- **20.2** Suppose pricing is conducted with a one-factor short rate model. Use the *Jamshidian*-decomposition to compute the generic price of a receiver swaption, expiring at *T*0, with tenor structure *t* < *T*0, . . . ,*T<sup>N</sup>* and ∆*t* = *T<sup>n</sup>* − *Tn*−1.
- **20.3** Consider the short rate model

$$dr(t) = e^{-\theta t}dt + \sigma_r dW(t).$$

Show that this model is a member of the affine term structure class and derive the ATS-functions *A*(*t*,*T*) and *B*(*t*,*T*).

**20.4** Show that the GARCH(1,1)-process *x<sup>t</sup>* , defined by

$$x_t = \sqrt{h_t} z_t$$
  
$$h_t = \omega + \alpha x_{t-1}^2 + \beta h_{t-1},$$

with independent and identically distributed innovations *z<sup>t</sup>* ∼ *N*(0, 1), is not a *Markov*-process.

- **20.5** Compute the convexity adjustment in the *Hull–White*-extended *Vasicek*-model.
- **20.6** In fitting the historical volatility structure of the HJM-factors, quadratic splines were used. Suppose there are *N* observations σ(*t*, τ*n*), for *n* = 1, . . . , *N*. Show that all spline coefficients can be computed, if the data points are matched exactly, the condition

$$\sigma'_{n}(\tau_{n+1}) = \sigma'_{n+1}(\tau_{n+1})$$

holds, and the first spline is only a linear function.
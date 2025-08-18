13.1

# The Black-Scholes-Theory

The option pricing theory of Black and Scholes (1973), and Merton (1973) is undoubtedly one of the most influential and elegant theories in economics. Sadly, Fisher Black died in 1995, before he could receive the Nobel Prize for this achievement, along with Myron Scholes and Robert Merton. The *Black–Scholes*-theory is still a cornerstone of derivative pricing and the starting point for numerous kinds of refinements.

## Geometric Brownian Motion and Itô's Lemma

We have already encountered a very simple model for the price process of a risky security. We called it a coin flip process back in Chapter 12. There we assumed that the price of a security evolves between time t and time  $t + \Delta t$  by

$$S_{t+\Delta t} = \begin{cases} u \cdot S_t & \text{for } \omega = \uparrow \\ d \cdot S_t & \text{for } \omega = \downarrow, \end{cases} \tag{13.1}$$

with probability p and  $1 - p$ , respectively. The *Black–Scholes*-theory is based on a far more sophisticated model for the price process of the underlying, called the geometric *Brown*ian motion. It is named after the Scottish botanist Robert Brown, who in 1827 documented a bizarre jittering motion of suspended pollen grain, when observed under his microscope. At that time it was not known that this peculiar motion was delivered by random collisions of molecules in the fluid. At the beginning of the twentieth century, the governing laws of this motion were discovered mainly by Einstein and Perrin. But it took nearly a century to prove the existence of such a process formally in a measure-theoretic framework. This was done in 1923 by Norbert Wiener and therefore, the process is nowadays also called the *Wiener*-process. The *Wiener*-process  $W_t$ is defined by three basic properties:

> 1.  $W_0 = 0$ , 2.  $W_t$  has independent increments,  $(13.2)$ 3.  $W_t - W_s \sim N(0, t - s)$  for  $0 \le s < t$ .

From these properties it is impossible to appreciate how strange this process really is. It can be proved that  $W_t$  has continuous paths with probability one, but at the same time it is almost surely nowhere differentiable. Because the time increments in the Black-*Scholes*-world are infinitesimal, we have a transition  $\Delta t \rightarrow dt$ , which also extends to the

increments of the *Wiener*-process. Thus, we can informally state that  $dW_t$  is normally distributed, with

$$E[dW_t] = 0 \quad \text{and} \quad \text{Var}[dW_t] = dt. \tag{13.3}$$

Louis Bachelier (1900), already suggested a model, based on *Brownian* motion, that in modern language would be written as

$$dS_t = \sigma dW_t,\tag{13.4}$$

in his PhD thesis. Remember that at this time there was no formal concept of a *Wiener*process. What Bachelier postulated is a simple scaled *Brown*ian motion. The model used by Black and Scholes is the geometric *Brown*ian motion

$$dS_t = \mu S_t dt + \sigma S_t dW_t. \tag{13.5}$$

What is the difference? Apart from the drift term  $\mu S_t dt$ , Brownian motion implies an absolute level of volatility, whereas geometric *Brownian* motion generates volatility relative to the price of the security. That is, we can say the annual volatility is  $20\%$  or so. Think about it the other way around. If absolute volatility is 50 cents, then the price of the security hardly fluctuates at all, if it currently costs 100 dollars. But if the price is merely one dollar, it is subject to very heavy fluctuations with respect to its absolute value. This somewhat strange behavior is avoided by using the geometric *Brown*ian motion. The additional drift term in  $(13.5)$  is the analogue of the riskless interest rate r in the bank account. Of course we assume  $\mu > r$ , because a security comes with risk to be compensated by a higher expected return.

The object  $(13.5)$  is called a stochastic differential equation. This term is a bit awkward, because  $W_t$  is not even differentiable. An easy way to get a feeling for what is happening, is to try to calculate its derivative. We can postulate as usual

$$\frac{dW_t}{dt} = \lim_{\Delta t \to 0} \frac{W_{t+\Delta t} - W_t}{\Delta t}.$$
(13.6)

What is the expectation value of this? It is still zero, because the increment  $W_{t+\Delta t} - W_t$ was defined to have zero expectation. But what about the variance? We get

$$\operatorname{Var}\left[\frac{dW_{t}}{dt}\right] = \lim_{\Delta t \to 0} \frac{1}{\Delta t^{2}} \operatorname{Var}[W_{t+\Delta t} - W_{t}] = \lim_{\Delta t \to 0} \frac{1}{\Delta t} = \infty.$$
(13.7)

The smaller we make the increment, the more violent the fluctuations become. In the end the process is too irregular to be differentiable. But because  $W_t$  is continuous, at least we can hope for the stochastic differential equation  $(13.5)$  to be integrable. That is indeed possible, but not with our standard integral calculus toolbox.

Recall what we did in Chapter 11, to solve for the time  $t$  value of the bank account  $B(t)$ . Initially we had the differential equation  $dB(t) = rB(t)dt$ . Then we took the logarithm to obtain

$$d\log B(t) = \frac{1}{B(t)}dB(t) = rdt.$$
 (13.8)

#### The Black-Scholes-Theory

What we applied here is of course the total differential. In fact, the total differential itself is a first order *Taylor*-series expansion. The big question is, why are there no higher order terms? This is the holy secret of calculus. You write dt instead of  $\Delta t$ , if it is so small that you can neglect higher order terms like  $dt^2$  or even  $dt^{3/2}$ . But you have to keep all terms of order dt. So let's check to what order  $dW_t$  contributes. We know from the definition of the *Wiener*-process that

$$E[dW_t^2] = dt \t\t(13.9)$$

has to hold. This is merely the variance of the infinitesimal *Wiener*-increment, because  $E[dW_t] = 0$ . But what is the variance of  $dW_t^2$ ? Remember that the *Wiener*-increments are independently normally distributed. We have already seen a formula for higher moments of normally distributed random variables,  $(2.31)$  on page 19. We thus can write

$$\text{Var}[dW_t^2] = E[dW_t^4] - E[dW_t^2]^2 = 3dt^2 - dt^2 = 2dt^2.$$
 (13.10)

But orders  $dt^2$  are supposed to be neglected, and thus the variance of  $dW_t^2$  vanishes. We can therefore conclude, at least heuristically, that  $dW_t^2 = dt$  has to hold. This also means that the order of  $dW_t$  has to be  $dt^{1/2}$ . Now let us see what we get, if we take the logarithm of the geometric *Brown*ian motion and expand the *Taylor*-series up to second order.

$$d\log S_t = \frac{1}{S_t} dS_t - \frac{1}{2} \frac{1}{S_t^2} dS_t^2$$
  
=  $\mu dt + \sigma dW_t - \frac{1}{2} \left( \mu^2 dt^2 + 2\mu \sigma dt dW_t + \sigma^2 dW_t^2 \right)$   
=  $\left( \mu - \frac{1}{2} \sigma^2 \right) dt + \sigma dW_t.$  (13.11)

Only the  $dW_t^2$  term of the quadratic contribution survives, because it is of order dt. This contribution provides an adjustment of the drift by  $-\frac{1}{2}\sigma^2$  that one would have missed, if one not kept track carefully of the order of  $dW_t$ . Now (13.11) is easily integrated, and subsequently exponentiated, to obtain

$$S_t = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t},\tag{13.12}$$

where we have to keep in mind that  $W_t$  is a normally distributed random variable with  $E[W_t] = 0$  and  $Var[W_t] = t$ . Equation (13.12) is called a strong solution to the stochastic differential equation  $(13.5)$ . There is a most illuminating way to see why the drift adjustment was necessary. Calculate the expectation value of  $(13.12)$  and recall that  $e^{\sigma W_t}$  is a log-normal distributed random variable,

$$E[S_t] = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t} E[e^{\sigma W_t}] = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t} e^{\frac{1}{2}\sigma^2 t} = S_0 e^{\mu t}.$$
 (13.13)

You can see that the expected rate of return is indeed  $\mu$ .

Everything we have motivated in the example of geometric *Brown*ian motion can be made more general and rigorous in terms of the Itô-integral. One of the most profound statements of this integration theory is the following theorem:

**Theorem 13.1 (Itô's lemma)** Let  $X_t$  be a generalized Wiener-process (Itô-process) of the form

$$dX_t = f(X_t, t)dt + g(X_t, t)dW_t,$$

and  $y(x, t)$  a sufficiently smooth function. Then the stochastic process  $Y_t = y(X_t, t)$  is also an Itô-process. with

$$dY_t = \left( f(X_t, t) \frac{\partial y}{\partial x} + \frac{\partial y}{\partial t} + \frac{1}{2} g^2(X_t, t) \frac{\partial^2 y}{\partial x^2} \right) dt + g(X_t, t) \frac{\partial y}{\partial x} dW_t,$$

where the partial derivatives are to be evaluated at  $x = X_t$ .

Itô's lemma is the generalization of the total differential to stochastic differential equations. We have left one open end. As explained, we gained the strong solution  $(13.12)$  by (implicitly) applying Itô's lemma. But is there also a weak solution, and what is the difference? There is a weak solution that describes the evolution of the probability density function of the  $It\hat{o}$ -process (13.5). It is governed by a deterministic partial differential equation called the *Fokker–Planck*-equation, but we will postpone its discussion. For the moment let's simply say that a strong solution describes the properties of a particular path, whereas a weak solution describes the properties of the whole process in terms of its probability density.

It should be emphasized again that  $W_t$  is not a differentiable process, but it is continuous everywhere, almost surely. Thus, the stochastic differential notation is purely formal and is to be understood in terms of the associated integrals. Therefore, *Itô*-calculus is a theory of integration. We will conclude this section by stating two important properties of the *Itô*-integral, which are really at the heart of Itô's lemma.

**Theorem 13.2 (Properties of the** *Itô***-integral)** Let  $X_t \in L^2(\Omega, \mathcal{F}, P)$  be a stochastic process, adapted to the natural filtration  $\mathcal{F}_t$ , generated by the Wiener-process  $W_t$ . Then the stochastic Itô-integral satisfies

$$E\bigg[\int_t^T X_s dW_s\bigg] = 0$$

for  $0 \le t \le T$ . Because of this property, the Itô-integral is a martingale

$$E\left[\int_0^T X_s dW_s \middle| \mathcal{F}_t\right] = \int_0^t X_s dW_s.$$

*Furthermore, for*  $0 \le t \le T$  *the Itô-isometry* 

$$\operatorname{Var}\left[\int_{t}^{T} X_{s} dW_{s}\right] = E\left[\left(\int_{t}^{T} X_{s} dW_{s}\right)^{2}\right] = E\left[\int_{t}^{T} X_{s}^{2} ds\right]$$

holds.

# **13.2 The Black–Scholes-Equation**

We are now entering the domain of complete *Black–Scholes*-markets. All unrealistic environmental conditions from the binomial world are relaxed here. We stick only to the following assumptions:

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

- Continuous trading is possible at any time *t* ∈ R + 0 .
- Prices of primitive assets (securities) follow a geometric *Brown*ian motion.
- Security prices are F*t*-measureable.
- There are no market frictions, transaction costs, or short-selling constraints.
- Assets are infinitely divisible.

The last two assumptions seem restrictive, but they are not. If the market is liquid, and individual trading volumes are high, transaction costs or indivisibility of a single security is absolutely negligible. In this setup, the value of a derivative contract *V*, contingent on a security *S*, is given by the function *V*(*S*, *t*), yet to be determined.<sup>1</sup> So let's try to compute it, using familiar tools. From Itô's lemma, we know the differential of *V*,

$$dV = \left(\mu S \frac{\partial V}{\partial S} + \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S} dW. \tag{13.14}$$

Now let's try what worked so well before. Build a hedge-portfolio, containing a long position in the derivative and a fractional short position in the underlying

$$\Pi = V - \Delta \cdot S. \n$$
(13.15)

Let's ask an easy question: How does this portfolio change? From (13.14) and the geometric *Brown*ian motion (13.5) we get

$$d\Pi = dV - \Delta \cdot dS$$
  
=  $dV - \Delta \cdot \mu S dt - \Delta \cdot \sigma S dW.$  (13.16)

Here comes the clever trick Black and Scholes (1973) applied. They chose the hedgeratio

$$\Delta = \frac{\partial V}{\partial S}.\tag{13.17}$$

Does that remind you of something? Take a look at the hedge-ratio in the binomial model (12.6) on page 224. The ratio (13.17) is an infinitesimal version of it. That is perfectly reconcilable with our intuition of the *Black–Scholes*-model as a certain limit of the binomial model. Let's see which terms cancel by applying (13.17)

$$d\Pi = \frac{\partial V}{\partial t}dt + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} dt.$$
 (13.18)

<sup>1</sup> To be completely rigorous, we would have to say that *V*(*S*, *t*) is a sufficiently smooth function and that *V<sup>t</sup>* = *V*(*S<sup>t</sup>* , *t*) is the stochastic *Itô*-process of the derivative contract. But let's be deliberately sloppy with the notation, to emphasize the really important aspects.

First of all, the variation of the portfolio no longer depends on the expected rate of return µ of the underlying, but far more important, it is no longer driven by the *Wiener*process. We have in fact a deterministic rule for the evolution of our hedge-portfolio. But wait, there is already such a rule for a riskless portfolio,

$$d\Pi = r\Pi dt = rV dt - rS\frac{\partial V}{\partial S}dt.$$
 (13.19)

In order to rule out arbitrage opportunities, the right hand sides of (13.18) and (13.19) have to coincide. After rearranging and dividing by *dt*, one obtains the famous *Black–Scholes*-equation

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0.$$
 (13.20)

Strictly speaking, (13.20) is a second order partial differential equation (PDE), and from this technical perspective it is hard to see why the *Black–Scholes*-PDE is such a powerful device, but it is. The fair price of every asset, tradable in the *Black–Schloes*world, is governed by (13.20). That is an outrageous statement so let's demonstrate it in a couple of examples.

**Example 13.1**

Let *V* be the risk-free bank account

$$V(S, t) = B(t) = e^{rt}.$$

Does it satisfy the *Black–Scholes*-PDE?

#### Solution

There are no partial derivatives with respect to an underlying *S*, so the *Black–Scholes*-PDE reduces to

$$\frac{\partial B}{\partial t} - rB = 0.$$

This condition is obviously satisfied. ........................................................................................................................

Here is another one:

**Example 13.2**

Let *V* be the risky security *S* itself

$$V(S, t) = S.$$

Does it satisfy the *Black–Scholes*-PDE?

#### The Black-Scholes-Theory

Solution

In this case, the partial differentials are  $\frac{\partial S}{\partial t} = 0$ ,  $\frac{\partial S}{\partial S} = 1$ , and  $\frac{\partial^2 S}{\partial S^2} = 0$ . Thus, the *Black*-Scholes-PDE becomes

$$rS\frac{\partial S}{\partial S} - rS = 0,$$

which is also true.

Let's try something more ambitious. We derived the price of a forward contract in Chapter 11 purely from arbitrage arguments. No model assumptions were involved. So let's take a look at it.

Example 13.3

Let  $V$  be the price of a forward contract

$$V(S, t) = F(S, t) = S - e^{-r(T-t)}K.$$

Does it satisfy the *Black–Scholes-PDE*?

Solution

The price of the forward contract has a partial derivative with respect to  $t$  and to  $S$ , but no second partial derivative with respect to S. Hence, the *Black–Scholes-PDE* becomes

$$\frac{\partial F}{\partial t} + rS\frac{\partial F}{\partial S} - rF = -re^{-r(T-t)}K + rS - rF = 0,$$

which is also satisfied.

At this point you should begin to see how powerful the *Black–Scholes-PDE* indeed is. But proving that prices of assets we already know obey the equation is one thing. Finding the prices of assets we do not know from the equation is the true power of the Black-Scholes-framework.

In order to find the price of a derivative, let's say a plain vanilla European call option, we have to require additional conditions to be satisfied. In case of the call option, the additional condition is the payoff function

$$V(S,T) = (S-K)^{+}.$$
 (13.21)

If we can find a function  $V(S, t)$ , satisfying the *Black–Scholes-PDE* and the additional condition  $(13.21)$  simultaneously, then we can read off the call price

$$C_t(K,T) = V(S_t, t). \t(13.22)$$

It all boils down to solving the partial differential equation  $(13.20)$  under additional conditions. Can you guess what option price we would obtain, if we can find a function  $V(S, t)$ , satisfying the *Black–Scholes-PDE*, (13.21), and additionally

$$V(S_u, t) = 0? \t(13.23)$$

Correct, this is the price of a European barrier call option  $C^{\bullet}_{\bullet}(K,T,S_u)$ , with upper knockout barrier  $S_{\mu}$ .

We will exercise the procedure of deriving the *Black–Scholes*-price of a European binary call option in detail. But first we have to learn a little bit about generalized functions

## 13.3

## Dirac's $\delta$ -Function and Tempered Distributions

A lot of mathematical and engineering applications heavily rely on the  $\delta$ -function, introduced by Paul Dirac. The problem with this function is that its definition does not fit with the requirements of ordinary functions. The *Dirac-* $\delta$ -function is defined by the properties

$$\delta(x) = \begin{cases} \infty & \text{for } x = 0\\ 0 & \text{for } x \neq 0 \end{cases} \quad \text{and} \quad \int_{-\infty}^{\infty} \delta(x) dx = 1. \tag{13.24}$$

There are two major problems with that. First of all, a function  $\delta: \mathbb{R} \to \mathbb{R}$  would require a unique definite value for each element in its domain. This requirement is violated for  $x = 0$ . Furthermore,  $\delta(x)$  is obviously not an integrable function. The old way to deal with these problems is to understand the  $\delta$ -function as a generalized function or "distribution," defined as the limit of a family of functions (see for example Lighthill, 1980, chap. 2). For example

$$\delta(x) = \lim_{\varepsilon \to 0} \Pi_{\varepsilon}(x) \quad \text{with} \quad \Pi_{\varepsilon}(x) = \begin{cases} \frac{1}{\varepsilon} & \text{for } -\frac{\varepsilon}{2} \le x \le \frac{\varepsilon}{2} \\ 0 & \text{else.} \end{cases} \tag{13.25}$$

**Quick calculation 13.1** Convince yourself that  $\phi_{\varepsilon}(x) = \frac{1}{\sqrt{2\pi e^2}} e^{-\frac{1}{2} \left(\frac{x}{e}\right)^2}$  is also a representation of the  $\delta$ -function as  $\varepsilon \to 0$ .

Figure 13.1 illustrates two different sequences of functions, approaching the  $\delta$ -function in the limit  $\varepsilon \rightarrow 0$ . The technical term "distribution" is another example of an unfortunate clash of terminology, because it has absolutely nothing to do with probability distributions. The modern, and far more powerful, way is to define  $\delta(x)$  in terms of a "pairing" with another so-called test function, which is so well behaved that all the unpleasant properties of the distribution can be rolled over to the test function. To make head or tail out of it, we have to see how it works.

![](_page_8_Figure_1.jpeg)

**Fig. 13.1** Different limit sequences for the  $\delta$ -function with  $\varepsilon = 1$  (black),  $\varepsilon = 0.5$  (dashed), and  $\varepsilon = 0.2$  (gray)

Let's start by looking for a very well behaved class of functions to be used as test functions. Call  $\varphi(x)$  a rapidly decreasing function, if

1.  $\varphi(x)$  is infinitely differentiable,

2. for every 
$$m, n \ge 0$$
, 
$$\lim_{x \to \pm \infty} |x|^m \left| \frac{d^n \varphi(x)}{dx^n} \right| = 0.$$
 (13.26)

Such functions are also called *Schwartz*-functions. Essentially, (13.26) says that every derivative of  $\varphi(x)$  decreases faster than any arbitrary power of x. That seems like a very strong statement, but one reason for choosing this class of test functions is that the probability density function of a normally distributed random variable is such a function. The *Schwartz*-functions form a vector space  $S$ , and its dual vector space is called the space of "tempered distributions." Consequently, we want a generalized function  $\mathcal{T}(x)$  to be defined by a continuous linear functional in S. We already know what it means for a functional to be linear.

1. 
$$\langle \mathcal{T} | \alpha \cdot \varphi \rangle = \alpha \cdot \langle \mathcal{T} | \varphi \rangle,$$
  
2.  $\langle \mathcal{T} | \varphi_1 + \varphi_2 \rangle = \langle \mathcal{T} | \varphi_1 \rangle + \langle \mathcal{T} | \varphi_2 \rangle.$  (13.27)

To be a continuous functional means that we have a sequence of test functions  $\varphi_n(x)$ , such that

$$\lim_{n \to \infty} \varphi_n(x) = \varphi(x) \quad \Rightarrow \quad \lim_{n \to \infty} \langle \mathcal{T} | \varphi_n \rangle = \langle \mathcal{T} | \varphi \rangle. \tag{13.28}$$

This condition is necessary to preserve certain limit properties. Actually, ensuring (13.28) is the really hard part, but let's not bother with these technical issues. Instead, define the  $\delta$ -function as such a functional on  $S$  by

$$\langle \delta | \varphi \rangle = \varphi(0). \tag{13.29}$$

To understand the meaning of  $(13.29)$ , write the functional in a more traditional form

$$\int_{-\infty}^{\infty} \delta(x)\varphi(x)dx = \varphi(0), \qquad (13.30)$$

and recall that  $\varphi(x)$  is an arbitrary function in S. In order for (13.30) to be true,  $\delta(x)$ can only be allowed to be nonzero in an infinitesimal vicinity of  $x = 0$ , so that we can pull  $\varphi(x)$  at  $x = 0$  out of the integral

$$\int_{-\infty}^{\infty} \delta(x)\varphi(x)dx = \varphi(0)\int_{-\infty}^{\infty} \delta(x)dx.$$
 (13.31)

But this means that the integral over the  $\delta$ -function has to equal one. Isn't that ingenious? Let's define another generalized function by such a continuous linear functional

$$\langle \delta_{\mathbf{y}} | \varphi \rangle = \varphi(\mathbf{y}). \tag{13.32}$$

From this definition, we can immediately conclude what  $\delta_{\nu}(x)$  is, namely

$$\int_{-\infty}^{\infty} \delta_y(x)\varphi(x)dx = \int_{-\infty}^{\infty} \delta(x-y)\varphi(x)dx = \varphi(y),\tag{13.33}$$

the shifted  $\delta$ -function. But that is only the tip of the iceberg. To demonstrate the incredible power of the formalism, let's look at two more applications: Derivatives of generalized functions and *Fourier*-transforms.

What does it mean to have a derivative of a distribution? Has the distribution itself to be differentiable? Surprisingly it does not have to be. The lack of differentiability is rolled over to the test function. Let's see how it works. Look at the following functional

$$\langle \frac{d}{dx}\mathcal{T}|\varphi\rangle = \int_{-\infty}^{\infty} \frac{d}{dx}\mathcal{T}(x)\varphi(x)dx.$$
 (13.34)

Using integration by parts, we get most easily

$$\int_{-\infty}^{\infty} \frac{d}{dx} \mathcal{T}(x)\varphi(x)dx = \mathcal{T}(x)\varphi(x)\Big|_{-\infty}^{+\infty} - \int_{-\infty}^{\infty} \mathcal{T}(x)\frac{d}{dx}\varphi(x)dx. \tag{13.35}$$

The first term on the right hand side has to vanish because of the defining properties of the test function  $\varphi(x)$  at  $x = \pm \infty$ . Thus, we can immediately conclude that

$$\langle \frac{d}{dx}\mathcal{T}|\varphi\rangle = -\langle \mathcal{T}|\frac{d}{dx}\varphi\rangle. \tag{13.36}$$

By completely analogous reasoning, we can infer that the differential operator  $D_n = \frac{d^n}{dx^n}$ has an adjoint operator  $D_n^{\dagger} = (-1)^n \frac{d^n}{dx^n}$ , such that

$$\langle D_n \mathcal{T} | \varphi \rangle = \langle \mathcal{T} | D_n^\dagger \varphi \rangle \tag{13.37}$$

holds. Let's look at two important examples.

The Black-Scholes-Theory

## Example 13.4

Let  $\theta(x)$  be the *Heaviside-* $\theta$ -function

$$\theta(x) = \begin{cases} 1 & \text{for } x \ge 0 \\ 0 & \text{for } x < 0, \end{cases}$$

and consider the functional  $\langle \frac{d}{dx} \theta | \varphi \rangle$ . What distribution is induced by it?

Solution

Follow the formalism  $(13.36)$  to obtain

$$\langle \frac{d}{dx}\theta|\varphi\rangle = -\langle \theta|\frac{d}{dx}\varphi\rangle = -\int_{-\infty}^{\infty} \theta(x)\frac{d}{dx}\varphi(x)dx = -\int_{0}^{\infty} d\varphi(x) = \varphi(0).$$

But  $\varphi(0)$  is the result of the pairing with the  $\delta$ -function, and so we have

$$\langle \frac{d}{dx} \theta | \varphi \rangle = \langle \delta | \varphi \rangle.$$

We can thus conclude that  $\frac{d}{dx}\theta(x) = \delta(x)$ .

Here is another example:

Example 13.5

Take the maximum function  $max(x, 0) = x^{+}$ , and consider the functional

 $\langle \frac{d}{dx} x^+ | \varphi \rangle$ .

What distribution is induced by this pairing?

Solution

Again stick to the formalism  $(13.36)$  to obtain

$$\langle \frac{d}{dx}x^{+}|\varphi\rangle = -\langle x^{+}|\frac{d}{dx}\varphi\rangle = -\int_{0}^{\infty}x\frac{d}{dx}\varphi(x)dx = -x\varphi(x)\Big|_{0}^{\infty} + \int_{0}^{\infty}\varphi(x)dx,$$

where we have used integration by parts in the last step. The first term on the right hand side is apparently zero, and the integral can be expressed as

$$\int_{0}^{\infty} \varphi(x) dx = \int_{-\infty}^{\infty} \theta(x) \varphi(x) dx = \langle \theta | \varphi \rangle$$

Hence, we find that  $\frac{d}{dx}x^+ = \theta(x)$ .

Those derivatives are of course only valid, if understood as distributions. They will come in handy at a later time when discussing the *Dupire*-equation.

The class of *Schwartz*-functions has another very pleasing property. It permits unconditional access to the *Fourier*-transform and the inverse *Fourier*-transform.

We will rely heavily on those transformations, when discussing stochastic volatility and *Lévy*-processes. Let's indicate the *Fourier*-transform of a function traditionally by hat-notation. How is the quantity Tˆ (*u*) defined? Again, stick to the formalism,

$$\begin{split} \langle \hat{\mathcal{T}} | \varphi \rangle &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{iux} \mathcal{T}(x) \varphi(u) dx du \\ &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mathcal{T}(x) e^{iux} \varphi(u) du dx \\ &= \int_{-\infty}^{\infty} \mathcal{T}(x) \hat{\varphi}(x) dx. \end{split} \tag{13.38}$$

That is, we have a general rule for the *Fourier*-transform of a distribution

$$\langle \hat{\mathcal{T}} | \varphi \rangle = \langle \mathcal{T} | \hat{\varphi} \rangle. \tag{13.39}$$

So let's find the *Fourier*-transform of the δ-function. We follow our new formalism (13.39) to obtain

$$\langle \delta | \hat{\varphi} \rangle = \hat{\varphi}(0) = \int_{-\infty}^{\infty} e^{i0x} \varphi(x) dx = \int_{-\infty}^{\infty} 1 \cdot \varphi(x) dx. \tag{13.40}$$

Obviously, there is a new pairing induced

$$\langle \hat{\delta} | \varphi \rangle = \langle 1 | \varphi \rangle, \tag{13.41}$$

from which we can conclude that δˆ(*u*) = 1.

Although the *Schwartz*-functions are a well-suited class of test functions, there are other appropriate classes, on which a distribution like the δ-function can be defined. In everyday life, the background connection to the respective class of test functions is usually brushed under the big carpet, and one writes

$$f(y) = \int_{-\infty}^{\infty} \delta(x - y) f(x) dx \qquad (13.42)$$

as defining equation for the *Dirac*-δ-function.

## **13.4 The Fundamental Solution**

Linear partial differential equations, as well as ordinary linear differential equations, obey the principle of superposition. This principle describes the fact that one can generate new solutions to a given problem by adding already known solutions. This should not come as a surprise, because what we call superposition is really at the heart of linearity. How can it be that a differential equation has more than one solution? Remember that such a solution is a function, not a number. Look at the following differential equation

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\frac{d^2x(t)}{dt^2} = -x(t).$$
 (13.43)

#### **261 The Black–Scholes-Theory**

Can you guess a function that satisfies this equation? Here is one, *x*(*t*) = sin *t*. Here is another one, *x*(*t*) = cos*t*. Because the differential equation (13.43) is linear, which means it contains no multiplicative terms in *x*(*t*), we can add solutions to obtain new ones,

$$x(t) = c_1 \sin t + c_2 \cos t, \tag{13.44}$$

where *c*<sup>1</sup> and *c*<sup>2</sup> are arbitrary constants. It is easily checked that (13.44) is also a solution to (13.43).

**Quick calculation 13.2** Confirm that *x*(*t*) = *e it*, with *i* = √ −1, is also a solution.

Now that we understand superposition, let's discuss the concept of an initial value problem. Suppose you deposit a fixed amount of money *B*<sup>0</sup> in your bank account at *t* = 0. *B*<sup>0</sup> is only a number, but the time value of the bank account is a function *B*(*t*), evolving as

$$\frac{dB(t)}{dt} = rB(t). \tag{13.45}$$

We know at least one solution to that differential equation, *B*(*t*) = *e rt*, but there are many others like for example

$$B(t) = ce^{rt},\tag{13.46}$$

for arbitrary values of *c*. To single out the desired individual solution, we have to exploit the initial condition *B*(0) =*B*0. Evaluating (13.46) at *t* = 0 yields *B*(0) = *c*, and thus we can conclude that *c* = *B*0. Hence, the unique solution to our initial value problem is

$$B(t) = B_0 e^{rt}.\t\t(13.47)$$

A partial differential equation like the *Black–Scholes*-equation is a rule for the evolution of a function *V*(*S*, *t*). Its initial value is not a number *V*0, but an entire function *V*(*S*, 0). And that is where the superposition principle comes in. If we can find a really special solution *V*0(*S*, *t*) that corresponds to the initial condition *V*0(*S*, 0) = δ(*S*), then we can write the initial condition as superposition

$$V(S,0) = \int_{-\infty}^{\infty} \delta(x-S)V(x,0)dx = \int_{-\infty}^{\infty} V_0(x-S,0)V(x,0)dx.$$
 (13.48)

Such a solution *V*0(*S*, *t*) is called a fundamental solution and it is so powerful, because the superposition principle is valid at any time *t*. We can immediately write the solution to the entire initial value problem

$$V(S,t) = \int_{-\infty}^{\infty} V_0(x-S,t)V(x,0)dx$$
 (13.49)

as superposition of the fundamental solution with the initial condition. Thus, our first step should be to look for a fundamental solution of the *Black–Scholes-PDE*.

In order to identify a fundamental solution to the *Black–Scholes-PDE*, we have to do some manipulations. The valuation of a European contract for example is a terminal value problem, which means that we first have to reverse the direction of time to turn it into an initial value problem. Departing from the original *Black–Scholes*-equation

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0,$$
(13.50)

we will organize the necessary steps in a way that allows us to retrace every manipulation.

## Step 1

Eliminate the inhomogeneity in the *Black–Scholes-PDE*. Make the substitution

$$V(S,t) = e^{-r(T-t)}U(S,t).$$
 (13.51)

This substitution adds an extra term to the time derivative,

$$\frac{\partial V}{\partial t} = rV + e^{-r(T-t)} \frac{\partial U}{\partial t}.$$
(13.52)

The partial derivative with respect to S is not affected by  $(13.51)$ . Thus, one obtains in terms of  $U(S, t)$ 

$$e^{-r(T-t)} \left( \frac{\partial U}{\partial t} + rS \frac{\partial U}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 U}{\partial S^2} \right) = 0. \tag{13.53}$$

We can multiply both sides by  $e^{r(T-t)}$  to obtain the final form of the *Black–Scholes-PDE* in terms of  $U(S, t)$ ,

$$\frac{\partial U}{\partial t} + rS\frac{\partial U}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 U}{\partial S^2} = 0.$$
 (13.54)

## Step 2

Reversing the flow of time. Define the time to expiry

$$\tau = T - t. \tag{13.55}$$

By the chain rule of differentiation, we can compute the partial derivative of  $U$  with respect to  $\tau$ ,

$$\frac{\partial U}{\partial \tau} = \frac{\partial U}{\partial t} \frac{dt}{d\tau} = -\frac{\partial U}{\partial t}.$$
(13.56)

That leaves us with an initial value problem and the following PDE

$$\frac{\partial U}{\partial \tau} = rS \frac{\partial U}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 U}{\partial S^2}.$$
 (13.57)

#### **Step 3**

Proceed to logarithmic prices. Define the log-price

$$x = \log S. \tag{13.58}$$

This transition has consequences for both partial derivatives of *U* with respect to *S*. The first derivative becomes

$$\frac{\partial U}{\partial S} = \frac{\partial U}{\partial x}\frac{dx}{dS} = \frac{\partial U}{\partial x} \cdot \frac{1}{S}.$$
(13.59)

The second derivative is a little more involved. One obtains

$$\frac{\partial^2 U}{\partial S^2} = \frac{\partial}{\partial S} \left( \frac{\partial U}{\partial x} \cdot \frac{1}{S} \right) = \frac{\partial^2 U}{\partial x^2} \cdot \frac{1}{S^2} - \frac{\partial U}{\partial x} \cdot \frac{1}{S^2}.$$
(13.60)

Using these derivatives, one obtains the new PDE

$$\frac{\partial U}{\partial \tau} = \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial U}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 U}{\partial x^2}.\tag{13.61}$$

#### **Step 4**

Change variables. Let

$$y = x + \left(r - \frac{1}{2}\sigma^2\right)\tau,\tag{13.62}$$

and define the new function *W* by

$$U(S,t) = U(e^{x}, T-\tau) = U(e^{y-(r-\frac{1}{2}\sigma^{2})\tau}, T-\tau) = W(y,\tau). \tag{13.63}$$

Under this transformation, the partial derivative with respect to τ changes to

$$\frac{\partial U}{\partial \tau} = \frac{\partial W}{\partial \tau} + \frac{\partial W}{\partial y} \frac{\partial y}{\partial \tau} = \frac{\partial W}{\partial \tau} + \frac{\partial W}{\partial y} \left( r - \frac{1}{2} \sigma^2 \right),\tag{13.64}$$

and the partial derivative with respect to *x* becomes

$$\frac{\partial U}{\partial x} = \frac{\partial W}{\partial y}\frac{\partial y}{\partial x} = \frac{\partial W}{\partial y}.$$
(13.65)

It is easy to see that the second partial derivative is also unaltered, <sup>∂</sup> <sup>2</sup>*U* ∂*x* <sup>2</sup> = ∂ <sup>2</sup>*W* ∂*y* 2 . One thus obtains in terms of the function *W*(*y*, τ)

$$\frac{\partial W}{\partial \tau} = \frac{1}{2} \sigma^2 \frac{\partial^2 W}{\partial y^2}.$$
 (13.66)

This partial differential equation also has a special name; it is called the diffusion equation. We can solve this equation easily, using a special trick *Fourier*-transform provides us with.

Suppose you have a sufficiently fast decreasing function  $f(x)$ , and you are looking for the *Fourier*-transform of its derivative. The definition of the *Fourier*-transform leads the way and one arrives at

$$\int_{-\infty}^{\infty} e^{iux} \frac{d}{dx} f(x) dx = e^{iux} f(x) \Big|_{-\infty}^{+\infty} - iu \int_{-\infty}^{\infty} e^{iux} f(x) dx = -iu \hat{f}(u). \tag{13.67}$$

The boundary term, generated by the integration by parts, vanishes, because we have assumed  $f(x)$  to be sufficiently fast decreasing, or in other words  $f^{(n)}(\pm \infty) = 0$ , for  $n \in \mathbb{N}_0$ . Repeating exactly the same argument successively, we can see what happens to arbitrary derivatives under *Fourier*-transform,

$$\frac{d^n}{dx^n}f(x) \longrightarrow (-iu)^n \hat{f}(u). \tag{13.68}$$

**Quick calculation 13.3** Verify (13.68) for  $n = 2$ .

This relation is instrumental in solving the diffusion equation. In *Fourier*-space, (13.66) reads

$$\frac{\partial}{\partial \tau} \hat{W}(u,\tau) = -\frac{1}{2}u^2 \sigma^2 \hat{W}(u,\tau). \tag{13.69}$$

This is nothing but an ordinary differential equation. Furthermore, we are looking for a fundamental solution, which means  $W_0(y, 0) = \delta(y)$ . But we have already seen that the *Fourier*-transform of the  $\delta$ -function is one, and therefore the initial value is  $W_0(u, 0) = 1$ . The unique fundamental solution to (13.69) in *Fourier*-space is thus

$$\hat{W}_0(u,\tau) = e^{-\frac{1}{2}u^2\sigma^2\tau}.\tag{13.70}$$

That should ring an enormous bell. Equation  $(13.70)$  is precisely the characteristic function of a normally distributed random variable with zero expectation value and variance  $\sigma^2 \tau$ . This means, the inverse *Fourier*-transform is the probability density function of such a random variable.

$$W_0(y,\tau) = \frac{1}{\sqrt{2\pi\sigma^2\tau}} e^{-\frac{1}{2}\left(\frac{y}{\sigma\sqrt{\tau}}\right)^2}.$$
 (13.71)

By retracing our steps, we have the relation  $V_0(S,t) = e^{-rt} W_0(y,\tau)$ , with  $\tau = T - t$  and  $y = \log S + (r - \frac{1}{2}\sigma^2)(T - t)$ . Thus, we have found the desired fundamental solution.

## 13.5

## **Binary and Plain Vanilla Option Prices**

Now that we know the fundamental solution, we can start computing option prices. The whole procedure is demonstrated for a binary option pair, but the methodology

#### The Black-Scholes-Theory

carries over analogously to all analytically solvable option types. The European binary call option has the payoff function  $C_T^B(K, T) = \theta(S - K)$ .

**Quick calculation 13.4** Convince yourself that for  $x = \log S$  the payoff function is equivalently formulated as  $C_T^B(K, T) = \theta(x - \log K)$ .

Using the fundamental solution, one obtains

$$C_t^B(K,T) = e^{-r\tau} \int_{-\infty}^{\infty} W_0(x-y,\tau)\theta(x-\log K)dx$$
  
$$= e^{-r\tau} \int_{\log K}^{\infty} W_0(x-y,\tau)dx$$
  
$$= e^{-r\tau} \int_{\log K}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2\tau}} e^{-\frac{1}{2}\left(\frac{x-y}{\sigma\sqrt{\tau}}\right)^2}dx.$$
  
(13.72)

Now, make the substitution  $z = \frac{x-y}{\sigma\sqrt{\tau}}$ . Under this transformation, the increment becomes  $dx = \sigma \sqrt{\tau} dz$ , and one obtains

$$C_t^B(K,T) = e^{-r\tau} \int_{\frac{\log K - y}{\sigma\sqrt{r}}}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz$$
  
$$= e^{-r\tau} \int_{-\infty}^{\frac{y - \log K}{\sigma\sqrt{r}}} \phi(z) dz,$$
  
(13.73)

where  $\phi(z)$  is again the probability density function of a standard normally distributed random variable. In the second equality, we have used the fact that  $\phi(z)$  is symmetric around  $z = 0$ . Retracing all substitutions we have made, the fair price of a European binary call option in the Black-Scholes-model is

$$C_t^B(K,T) = e^{-r(T-t)}\Phi(d), \tag{13.74}$$

with

$$d = \frac{\log(S_t/K) + (r - \frac{1}{2}\sigma^2)(T - t)}{\sigma\sqrt{T - t}},$$
(13.75)

where  $\Phi(x)$  is of course the distribution function of a standard normally distributed random variable. Except for slight notational variations, this is exactly what we already found in the limit of the binomial model, see  $(12.75)$  on page 246. To obtain a formula for the binary put option, we can simply use binary put-call parity

$$C_t^B(K,T) + P_t^B(K,T) = e^{-r(T-t)}.$$
(13.76)

**Quick calculation 13.5** Confirm this parity relation by adding the payoffs.

![](_page_17_Figure_1.jpeg)

Fig. 13.2 Fair price of European binary call (left) and plain vanilla call (right) – Different times to expiry (gray, dashed, black) in descending order

The resulting price for the binary European put option is

$$P_t^B(K,T) = e^{-r(T-t)}(1 - \Phi(d)) = e^{-r(T-t)}\Phi(-d),\tag{13.77}$$

with  $d$  as in (13.75).

**Quick calculation 13.6** Verify that  $\Phi(x) = 1 - \Phi(-x)$  holds.

Figure 13.2 left shows the fair price of a European binary call option, as a function of the current price of the underlying, for different times to expiry. The solid black line is the payoff at expiry.

Black and Scholes (1973) derived the analytic formula for a European plain vanilla call option. The steps are analogous to those in the binary case. They obtained for the fair value of that option

$$C_t(K,T) = S_t \Phi(d_1) - e^{-r(T-t)} K \Phi(d_2), \tag{13.78}$$

with

$$d_1 = \frac{\log(S_t/K) + (r + \frac{1}{2}\sigma^2)(T - t)}{\sigma\sqrt{T - t}} \quad \text{and} \quad d_2 = d_1 - \sigma\sqrt{T - t}.$$
 (13.79)

From put-call parity, the fair price for a plain vanilla put option is easily obtained as

$$P_t(K,T) = -S_t\Phi(-d_1) + e^{-r(T-t)}K\Phi(-d_2),\tag{13.80}$$

with  $d_1$  and  $d_2$  as in (13.79).

**Quick calculation 13.7** Verify the last formula from put-call parity.

#### **267 The Black–Scholes-Theory**

The fair price of a European plain vanilla call option is illustrated in Figure 13.2 right, for different times to expiry. The solid black line again indicates the payoff function at expiry.

# **13.6 Simple Extensions of the Black–Scholes-Model**

The original option pricing formula (13.78) is only valid, if the underlying neither pays dividends, nor causes costs of any kind. But it can be easily extended to cover all kinds of exceptional properties of the underlying. We will discuss the case of a continuous dividend stream in detail, and subsequently extend the basic principle to all kinds of other anomalies.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

## **13.6.1 Continuous Dividend Stream**

Suppose the underlying *S* pays a constant dividend stream *q*, also called a dividend yield, which is continuously reinvested in the position itself. That is, in every instant *dt*, the position ∆ in *S* grows by *d*∆ = *q*∆*dt*. Let's set up the usual hedge-portfolio Π = *V* − ∆ · *S* and let's analyze how it changes

$$d\Pi = dV - \Delta \cdot dS - d\Delta \cdot S$$
  
=  $dV - \Delta \cdot dS - \Delta \cdot qSdt.$  (13.81)

We have one additional term, due to the reinvestment of the dividend stream. Let's do the same as we did before, namely apply Itô's lemma and choose ∆ = <sup>∂</sup>*<sup>V</sup>* ∂*S* to obtain

$$d\Pi = \frac{\partial V}{\partial t}dt + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}dt - qS \frac{\partial V}{\partial S}dt.$$
 (13.82)

This result is completely analogous to (13.18), except for the additional last term on the right hand side. The change in portfolio value (13.82) does not depend on the *Wiener*process anymore, and should therefore be related to the riskless interest rate, *d*Π = *r*Π*dt*. Plugging everything in, one obtains a modified *Black–Scholes*-equation

$$\frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0.$$
 (13.83)

**Quick calculation 13.8** Confirm that (13.83) is correct.

We have now to repeat our earlier steps, to find a fundamental solution. But we can take a very effective shortcut. Let's execute our former step 1 and substitute *V*(*S*, *t*) = *e* <sup>−</sup>*r*(*T*−*t*)*U*(*S*, *t*). This results in the partial differential equation

$$\frac{\partial U}{\partial t} + (r - q)S\frac{\partial U}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 U}{\partial S^2} = 0.$$
 (13.84)

Now invent a "generalized cost-of-carry rate"  $b = r - q$ , and observe that we only have to make the replacement  $r \rightarrow b$ , to turn the original fundamental solution into the desired solution of the modified *Black–Scholes-PDE*. Exercising the entire computation, one obtains a new generalized *Black–Scholes*-formula for the European plain vanilla call option

$$C_t(K,T) = e^{(b-r)(T-t)} S_t \Phi(d_+) - e^{-r(T-t)} K \Phi(d_-), \qquad (13.85)$$

with

$$d_{+/-} = \frac{\log(S_t/K) + (b \pm \frac{1}{2}\sigma^2)(T - t)}{\sigma\sqrt{T - t}}.\t(13.86)$$

For the non dividend paying underlying,  $b = r$  reproduces the original *Black–Scholes*formula. For  $b = r - q$ , we obtain the modified formula for the dividend paying underlying. For the sake of completeness, the price of the corresponding put option, obtained from put-call parity is

$$P_t(K,T) = -e^{(b-r)(T-t)}S_t\Phi(-d_+) + e^{-r(T-t)}K\Phi(-d_-). \tag{13.87}$$

**Quick calculation 13.9** Confirm that  $C_t^B(K,T) = e^{-r(T-t)}\Phi(d_-)$  is the correct generalized formula for a European binary call option.

#### 13.6.2 **Options on a Foreign Currency**

Suppose the underlying is a foreign currency. The holder of a position  $\Delta$  in foreign currency receives foreign interest according to  $d\Delta = r_f \Delta dt$ , with the foreign risk-free interest rate  $r_f$ . The changes in the hedge-portfolio in this case become

$$d\Pi = dV - \Delta \cdot dS - \Delta \cdot r_f S dt, \tag{13.88}$$

and we can immediately conclude that the corresponding modified *Black-Scholes*equation is

$$\frac{\partial V}{\partial t} + (r - r_f)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0.$$
 (13.89)

Without further analysis it is obvious that our generalized framework carries over to the case of foreign currencies, with the generalized cost-of-carry rate  $b = r - r_f$ .

#### 13.6.3 **Commodity Options**

The underlying does not have to be a security of some sort, it is also common that option contracts are contingent on commodities like copper, gold, wheat, petroleum, and so forth. The primary difference between those two classes of underlyings is that commodities have to be stored. Take gold for example. It has not only to be stored, but it has additionally to be guarded. It is again sensible to assume that the overall storage costs are proportional to the size of the position and the storage period. Suppose the storage costs are funded by the proceeds of trading the associated commodity. Then we can think of storage costs as continuously reducing the position in the commodity,  $d\Delta = -c_s\Delta dt$ , where  $c_s$  is the instantaneous cost rate. This immediately induces another modification of the *Black–Scholes*-equation,

$$\frac{\partial V}{\partial t} + (r + c_s)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0,$$
(13.90)

where this time, the generalized cost-of-carry rate is  $b = r + c_s$ .

#### 13.6.4 **Options on Forwards and Futures**

We still consider the case of a deterministic risk-free interest rate. Therefore, the fair delivery or forward price of a forward or future contract, initiated at time  $t$ , is given by

$$F_t = e^{r(T_F - t)} S_t, \t\t(13.91)$$

where  $T_F \geq T$  is the delivery date of the forward or future contract. Define  $V(S, t) =$  $U(F, t)$  and let's see how the derivatives change. For the time derivative we get

$$\frac{\partial V}{\partial t} = \frac{\partial U}{\partial t} + \frac{\partial U}{\partial F}\frac{\partial F}{\partial t} = \frac{\partial U}{\partial t} - rF\frac{\partial U}{\partial F}.$$
(13.92)

The first derivative with respect to S is also altered. One obtains

$$\frac{\partial V}{\partial S} = \frac{\partial U}{\partial F} \frac{\partial F}{\partial S} = e^{r(T_F - t)} \frac{\partial U}{\partial F}.$$
(13.93)

But recall the term in the *Black–Scholes*-equation that contains this first order derivative. This particular term transforms to

$$rS\frac{\partial V}{\partial S} = re^{r(T_F - t)}S\frac{\partial U}{\partial F} = rF\frac{\partial U}{\partial F}.$$
(13.94)

Isn't that nice? And it gets even better. From (13.91) we have  $\frac{\partial^2 F}{\partial S^2} = 0$ , and thus

$$\frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S} \left( \frac{\partial U}{\partial F} \frac{\partial F}{\partial S} \right) = \frac{\partial^2 U}{\partial F^2} \left( \frac{\partial F}{\partial S} \right)^2. \tag{13.95}$$

That makes the second derivative term in the original *Black–Scholes*-equation

$$\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = \frac{1}{2}\sigma^2 F^2 \frac{\partial^2 U}{\partial F^2}.$$
 (13.96)

| <b>Table 13.1</b> Generalized cost-of-carry rates |                                     |
|---------------------------------------------------|-------------------------------------|
| Underlying                                        | Cost-of-carry rate $\boldsymbol{b}$ |
| Non dividend paying security                      | r                                   |
| Dividend paying security (dividend rate $q$ )     | $r-q$                               |
| Foreign currency (foreign interest rate $r_f$ )   | $r - r_f$                           |
| Commodity (storage cost rate $c_s$ )              | $r + c_s$                           |
| Forward or future contract                        |                                     |

Hence, the modified *Black–Scholes*-equation, where the underlying is a forward or future contract on a non dividend paying security is

$$\frac{\partial U}{\partial t} + \frac{1}{2}\sigma^2 F^2 \frac{\partial^2 U}{\partial F^2} - rU = 0. \tag{13.97}$$

We can immediately read off that the generalized cost-of-carry rate is  $b = 0$ . This version is also known as the *Black*-76-model (Black, 1976). Table 13.1 summarizes all extensions to the *Black–Scholes*-model discussed in this section.

13.7

## **Discrete Dividend Payments**

In this section, we will look at the more realistic assumption that dividend payments are to occur at discrete times over the lifetime of the option. We will still assume that the magnitude as well as the time of the dividend payment is known in advance. There are two common manifestations of this restriction. The first is a simple cash dividend  $D_n$ , paid at time  $t_n$ , for  $t < t_n < T$ . The second is a fixed discrete dividend yield  $q_n$ , that is, the dividend due at  $t_n$  is  $D_n = q_n S_{t_n}$ . We will study the latter alternative first, because it does not require any volatility adjustments.

Let's ask the question: Is the price of the dividend paying security S affected by the discrete dividend payment  $D_n$ ? To be as precise as possible, call the instant just before the dividend payment  $t_n^-$  and the successive instant, where the dividend is already paid  $t_n^+$ . Now let's see, what the holder of this security gets out of the transition. We assume heuristically that the time difference between  $t_n^-$  and  $t_n^+$  is too small for any appreciable change in the price of the underlying due to random fluctuations. Therefore, the overall value of the position cannot change, and

$$S_{t_n^-} = S_{t_n^+} + D_n \tag{13.98}$$

has to hold. If  $D_n = q_n S_{t_n}$ , we obtain an explicit expression for the ex-dividend price of the security

$$S_{t_n^+} = (1 - q_n)S_{t_n^-}.$$
 (13.99)

| Table 13.2<br>Option arbitrage portfolio |                                                             |                                                             |  |
|------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|--|
| Position                                 | −<br>Value at t<br>n                                        | +<br>Value at t<br>n                                        |  |
| Stock<br>Bank account                    | St<br>−<br>n<br>0                                           | (1 −<br>qn)St<br>−<br>n<br>qnSt<br>−<br>n                   |  |
| Option<br>Total sum                      | −∆Vt<br>−<br>n<br>−<br>∆Vt<br>= 0<br>St<br>−<br>−<br>n<br>n | −∆Vt<br>+<br>n<br>−<br>∆Vt<br>= 0<br>St<br>−<br>+<br>n<br>n |  |

This means, the price of the dividend paying security jumps during the transition from *t* − *n* to *t* + *n* . The magnitude of the jump is exactly the magnitude of the dividend, paid at *tn*. Here comes the interesting question: does a derivative, contingent on *S*, jump, too? Let's answer this one with an arbitrage argument. Suppose an investor holds a dividend paying stock *S*, just before the payment is due. The position is funded by short selling

$$\Delta = \frac{S_{t_{\overline{n}}}}{V_{t_{\overline{n}}}}\tag{13.100}$$

units of a derivative *V*, contingent on *S*. If the dividend is of the type (13.99), the overall position of the investor can be summarized as in Table 13.2. We can immediately conclude that *V<sup>t</sup>* − *<sup>n</sup>* = *V<sup>t</sup>* + *n* has to hold. This fact implies a "jump condition" in the *Black– Scholes*-equation, namely

$$V(S, t_n^-) = V((1 - q_n)S, t_n^+). \tag{13.101}$$

If you think it through, it is obvious why the security, but not the option, jumps. The holder of the security receives the dividend, but the holder of the option receives nothing. So why should the option value jump?

The principle we just encountered is so general that it applies to any kind of option. In particular, if there are *N* dividend payments to come during the lifetime of the option, and the discrete dividend yields *q<sup>n</sup>* are known for *n* = 1, . . . , *N*, then we can use any formula we already derived with the replacement

$$S_t^q = \prod_{n=1}^N (1 - q_n) S_t.$$
 (13.102)

If *q<sup>n</sup>* = *q* for all *n*, (13.102) simplifies to *S q <sup>t</sup>* = (1 − *q*) *<sup>N</sup>S<sup>t</sup>* . Let's look at an example.

## **Example 13.6**

Consider a stock with current price *S*<sup>0</sup> = 110. There is a European call option written on *S*, with exercise price *K* = 100, expiring at *T*= 0.5. The annual volatility is σ= 20%,

and the annual risk-free interest rate is *r* = 4%. How does the value of the call option change, if there are two dividend payments, in two and in five months, to be accounted for? Assume that the dividend yield is fixed at *q* = 2%.

#### Solution

Without accounting for dividend payments, the quantities *d*+/<sup>−</sup> are

$$d_{+} = \frac{\log 1.1 + 0.03}{0.1414} = 0.8862$$
 and  $d_{-} = \frac{\log 1.1 + 0.01}{0.1414} = 0.7448.$ 

The *Black–Scholes*-price for the European call is

$$C_0(K,T) = S_0\Phi(d_+) - e^{-rT}K\Phi(d_-) = 13.69.$$

With two dividend payments to come, we have to adjust the stock price *S q* 0 = (1 − *q*) <sup>2</sup>*S*<sup>0</sup> = 105.64. The adjusted quantities *d q* +/− are

$$d_{+}^{q} = \frac{\log 1.0564 + 0.03}{0.1414} = 0.6002 \quad \text{and} \quad d_{-}^{q} = \frac{\log 1.0564 + 0.01}{0.1414} = 0.4587.$$

The *Black–Scholes*-price for the European call on the dividend paying stock is

$$C_0(K,T) = S_0^q \Phi(d_+^q) - e^{-rT} K \Phi(d_-^q) = 10.34.$$

The call option on the dividend paying stock is cheaper than the contract contingent on the non dividend paying stock.

........................................................................................................................

The conclusion that dividend payments should reduce the value of a call option is reasonable, because dividend payments cause an instantaneous reduction of the stock price, driving the option in the less valuable direction.

**Quick calculation 13.10** How should the put price behave under dividend payments?

Let's now discuss simple cash dividends. The associated framework is called the "escrowed dividend model" by Haug (2007, chap. 9). Assume that there are *N* known dividends to come over the remaining lifetime of the option. More precisely, the cash dividend *D<sup>n</sup>* is scheduled at time *tn*, for *n* = 1, . . . , *N*. The idea of escrowed dividend models is that the current price of the underlying *S<sup>t</sup>* can be split into one risky part *S r t* , and the present value of all future dividend payments

$$S_t = S_t^r + D = S_t^r + \sum_{n=1}^N e^{-r(t_n - t)} D_n.$$
 (13.103)

Of course, we have to assume that the tenor of the dividend payments is *t* < *t<sup>n</sup>* < *T* for all *n*. Only *S r <sup>t</sup>* = *S<sup>t</sup>* − *D* goes into the *Black–Scholes*-formula to calculate the fair option price. But in doing so, we miss a subtle and important point. The volatility, fed into

#### **273 The Black–Scholes-Theory**

the *Black–Scholes*-formula, is usually an estimate, extracted from the history of *S*, not from the history of *S r* . Clearly *S r <sup>t</sup>* < *S<sup>t</sup>* for *t* < *t<sup>N</sup>* and thus, the true volatility of *S <sup>r</sup>* has to be greater than the one observed from *S*. There are several adjustments suggested in the literature, to compensate for the volatility bias. A simple adjustment, very popular with practitioners, is

$$\sigma_{\text{adj.}} = \sigma \frac{S_t}{S_t - D},\tag{13.104}$$

where *D* is again the present value of all future dividend payments. This adjustment is clearly a very crude one, because it does not account for the descending magnitude of the bias caused by the dividend tenor. A better adjustment can be found in Haug (2007, p. 369)

$$\sigma_{\text{adj.}}^2 = \frac{\sigma^2}{T - t} \sum_{n=1}^{N+1} \left( \frac{S_t}{S_t - \sum_{k=n}^N e^{-r(t_k - t)} D_k} \right)^2 (t_n - t_{n-1}), \tag{13.105}$$

with *t*<sup>0</sup> = *t* and *tN*+<sup>1</sup> = *T*.

**Example 13.7**

Look at the setup of Example 13.6, but now assume that the dividend is a cash dividend with *D*<sup>1</sup> = *D*<sup>2</sup> = 2. What are the volatility adjustments and the *Black–Scholes*-prices?

Solution

First calculate the risky part of the stock price *S r* 0

$$S_0^r = S_0 - \sum_{n=1}^2 e^{-rt_n} D_n = 110 - 2(e^{-0.04 \cdot \frac{2}{12}} + e^{-0.04 \cdot \frac{5}{12}}) = 106.05.$$

The simple volatility adjustment is

$$\sigma_{\text{adj.}} = \sigma \frac{S_0}{S_0^r} = 20.745\%,$$

and the corresponding *Black–Scholes*-price, using *S r* 0 and σadj. is

$$C_0(K, T) = 10.82.$$

For the tenor-based adjustment, one obtains

$$\sigma_{\text{adj.}}^2 = \frac{\sigma^2}{T} \left( \left( \frac{S_0}{S_0 - 2(e^{-0.04 \cdot \frac{S}{12}} + e^{-0.04 \cdot \frac{S}{12}})} \right)^2 \frac{2}{12} + \left( \frac{S_0}{S_0 - 2e^{-0.04 \cdot \frac{S}{12}}} \right)^2 \frac{3}{12} + \frac{1}{12} \right)$$
$$= \frac{0.04}{0.5} (0.1793 + 0.2592 + 0.0833) = 0.0417.$$

Taking the positive root yields  $\sigma_{\text{adi}} = 20.421\%$ . Plugging this adjusted volatility into the *Black–Scholes*-formula along with  $S_0^r$ , one obtains

$$C_0(K, T) = 10.74.$$

Thus, the simple volatility adjustment results in a slight overpricing of the call option.

## 13.8

## American Exercise Right

Options with American exercise right allow the holder to exercise the contract at any time during the lifetime of the option. This is an additional right for the holder that makes the contract usually more valuable, but it also makes the valuation much harder. Indeed, there exist only very few analytical formulas for American options. One special case is the American plain vanilla call option on a non-dividend paying underlying. We have already learned that under no circumstances such an option should be exercised early. Thus, its price coincides with the price of the European contract. Another rare exception, where an analytical solution is available, is the perpetual put option. We will discuss this contract shortly, but let's first think about the more general implications of American exercise right.

Recall that in deriving the *Black–Scholes*-PDE, we set up a hedge-portfolio  $\Pi = V$  $\Delta S$ , with a long position in the derivative contract. Using Itô's lemma and plugging in the hedge-ratio  $\Delta = \frac{\partial V}{\partial S}$ , eliminated the risk, and thus we concluded that the value of the hedge-portfolio has to change according to the risk-free interest rate. Our last step before stating the *Black–Scholes*-equation (13.20) on page 254 was to divide out dt, because it appeared in every single term. Let's go back to this point and slightly rearrange

$$\left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt = rVdt.$$
 (13.106)

What (13.106) tells us is that if properly hedged, we earn exactly the risk-free interest with our long position in the option contract. In case of an American option, proper hedging is not enough. We have also to exercise optimally. That is, the holder of an American contract cannot earn more than the risk-free interest, but she can very well earn less, if she does not exercise optimally. Thus, the equal to sign in  $(13.106)$  has to be replaced by a less than or equal to sign. In doing so, we obtain a more general Black–Scholes-equation

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV \le 0. \tag{13.107}$$

European contracts satisfy  $(13.107)$ , because equality holds for all of them. For American contracts equality only holds as long as the holder follows the optimal exercise **275 The Black–Scholes-Theory**

policy. Otherwise the left hand side is strictly less than zero. Let's now look at a very special American contract.

A perpetual option is a contract that never expires. You should immediately realize that such a contract can only exist, if equipped with American exercise right. So let's analyze a perpetual American put option. If optimally exercised, the value of this contract is always

$$P_t(K) \ge (K - S_t)^+.$$
 (13.108)

During the lifetime, strict inequality should hold, because the contract is to be exercised the first time equality occurs. Assume strict inequality for the moment. This means that the *Black–Scholes*-equation holds with equality. Because the contract is perpetual, the partial derivative with respect to *t* vanishes,

$$\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 P}{\partial S^2} + rS \frac{\partial P}{\partial S} - rP = 0.$$
 (13.109)

But this is only an ordinary differential equation, which makes life much easier. Unfortunately, there is no general theoretical framework for solving differential equations. It is always tinkering with trial and error. Mathematicians have developed very good instincts for making educated guesses about an ansatz that might work. In this case, let's try a power law

$$P = c_1 S^{c_2}, \tag{13.110}$$

where *c*<sup>1</sup> and *c*<sup>2</sup> are constants, yet to be determined. Plug this ansatz back into (13.109) and let's see what we get,

$$\frac{1}{2}\sigma^2 c_2(c_2 - 1)c_1 S^{c_2} + r(c_2 - 1)c_1 S^{c_2} = 0.$$
 (13.111)

From this we can immediately conclude that both,

$$c_2 = 1$$
 and  $c_2 = -\frac{2r}{\sigma^2}$  (13.112)

satisfy (13.111).

**Quick calculation 13.11** Verify the second solution for *c*2.

The original differential equation (13.109) is linear and thus, the superposition of two solutions is also a valid solution. Hence, the road leads us to a general solution of the form

$$P = c_0 S + c_1 S^{-\frac{2r}{\sigma^2}}.\t(13.113)$$

Even though this might not look like progress, it is. We know that the value of a put option has to tend to zero in the limit *S* → ∞. Therefore, the first coefficient has to be *c*<sup>0</sup> = 0. So all we have to care about is the constant *c*1. To determine this one, we need a more subtle idea. We know that the contract does not depend on time. This means there

is one particular  $S^*$ , such that the holder has to exercise immediately when approached from above, in order to follow an optimal exercise policy. In other words,

$$P^* = c_1 S^{* - \frac{2r}{\sigma^2}} = K - S^*.$$
 (13.114)

We can turn this into a definition of  $c_1$  and obtain

$$c_1 = \frac{K - S^*}{S^{* - \frac{2r}{\sigma^2}}}.$$
(13.115)

Of course we do not know  $S^*$  either, and so it again seems as if we are stuck. But that is not quite correct. Let's eliminate  $c_1$  and write the option value as

$$P = (K - S^*) \left(\frac{S}{S^*}\right)^{-\frac{2r}{\sigma^2}}.$$
 (13.116)

Because  $S^*$  is the optimal exercise price, it gives the contract its maximum value. But that means the derivative of  $P$  with respect to  $S^*$  has to vanish, and we have

$$\frac{\partial P}{\partial S^*} = -\frac{1}{S^*} \left(\frac{S}{S^*}\right)^{-\frac{2r}{\sigma^2}} \left(S^* - \frac{2r}{\sigma^2}(K - S^*)\right) = 0. \tag{13.117}$$

This condition can only be met, if the second bracket equals zero, and we thus obtain

$$S^* = \frac{K}{1 + \frac{\sigma^2}{2r}}.\tag{13.118}$$

Plugging this result into (13.116), we obtain the value of the American perpetual put option for  $S_t \geq S^*$ 

$$P_t(K) = \frac{\sigma^2 K}{2r + \sigma^2} \left(\frac{K}{S_t(1 + \frac{\sigma^2}{2r})}\right)^{\frac{2r}{\sigma^2}}.$$
 (13.119)

Observe that at the optimal exercise price  $S^*$ , the partial derivative with respect to S is

$$\left. \frac{\partial P}{\partial S} \right|_{S=S^*} = -1 = \frac{\partial (K-S)}{\partial S}.$$
(13.120)

This condition is also known as the "smooth-pasting" condition.

**Quick calculation 13.12** Verify the first equality in (13.120).

#### **Discrete Hedging and the Greeks** 13.9

We have already learned that the *Black–Scholes*-equation is motivated by a hedging argument. More precisely, we assumed that it is possible to adjust a hedge-portfolio continuously, such that it is held risk-free at every instant. The growth rate of such a portfolio was then identified with the risk-free interest rate. In reality continuous hedging is not possible. There is no general rule for discrete hedging. A good hedging strategy depends on all kinds of market imperfections like transaction costs, changes in volatility of the underlying, and so forth. As a result, the risk cannot be fully eliminated by hedging and thus, the option will be offered at a slightly higher price. In fact, we have two different prices for buying and selling an option. If we are the ones to sell the option, we have to choose a "nearly fair" price and take precautions to limit the risk. In this section, we will take a look at some general hedging strategies.

#### **Delta-Hedging** 13.9.1

Delta-hedging is not a new concept, it is closely related to what we did when deriving the *Black–Scholes-PDE*. The objective of a delta-hedge is to immunize the portfolio against small changes in the price of the underlying. To this end, one linearizes the change in the value of a derivative with respect to the price of the underlying

$$V(S + \Delta S, t) \approx V(S, t) + \frac{\partial V(S, t)}{\partial S} \Delta S.$$
 (13.121)

To first order, the change in the value of a derivative is locally proportional to the change in the value of the underlying. The factor of proportionality is called the delta of the option,

$$\Delta = \frac{\partial V}{\partial S}\bigg|_{S=S_{\epsilon}}.\tag{13.122}$$

If the *Black–Scholes*-theory is correct, we can compute the delta immediately from the analytical *Black–Scholes*-formula, if there is one. For the plain vanilla call and put formulas  $(13.78)$  and  $(13.80)$  on page 266, the delta is surprisingly simple,

$$\Delta_C = \Phi(d_1) \quad \text{and} \quad \Delta_P = \Phi(d_1) - 1. \n$$
(13.123)

The delta of the put option is most easily derived from put-call parity.

**Quick calculation 13.13** Confirm  $\Delta_C$  by differentiating (13.78) with respect to  $S_t$ .

How is a delta-hedge achieved in practice? Assume you have a short position in say  $x$ options, and you want to hedge against small changes in the price of the underlying.

Then you have to add the quantity *x* · ∆ of the underlying to immunize your position. The resulting hedge-portfolio is

$$\Pi = -x \cdot V + x \cdot \Delta \cdot S. \n$$
(13.124)

Let's check, if this modification of the position has the desired effect. First, a small change in the portfolio value is given by

$$d\Pi = \frac{\partial \Pi}{\partial V} \frac{\partial V}{\partial S} dS + \frac{\partial \Pi}{\partial S} dS.$$
 (13.125)

From this we can easily see that the portfolio itself has a delta and plugging in the ingredients from (13.124) yields

$$\Delta_{\Pi} = \frac{d\Pi}{dS} = -x \cdot \Delta + x \cdot \Delta = 0. \tag{13.126}$$

Thus, the position is called delta-neutral. It is important to realize that a position remains delta-neutral only for a very short amount of time. As soon as the price of the underlying changes, the delta of the option changes, too. As a consequence, the position will no longer be perfectly delta-neutral, see Figure 13.3 for a graphical illustration. There are two more points worth noting. The first one is a mere triviality that becomes important in more sophisticated hedging schemes: the delta of the underlying is one,

$$\Delta_S = \frac{\partial S}{\partial S} = 1. \tag{13.127}$$

Second, because the portfolio Π is a linear combination of say *N* assets, with respective quantity *x<sup>n</sup>* for *n* = 1 . . . , *N*, the delta of the entire portfolio is given by

$$\Delta_{\Pi} = \sum_{n=1}^{N} x_n \Delta_n. \tag{13.128}$$

## **13.9.2 Gamma-Hedging**

The Greek letter gamma represents the second derivative of a position with respect to the price of the underlying. Because linearity of a portfolio still holds, we obtain

$$\Gamma_{\Pi} = \frac{d^2 \Pi}{dS^2} = \sum_{n=1}^{N} x_n \Gamma_n.$$
 (13.129)

In particular, it is easy to see that the gamma of the underlying itself vanishes. We have

$$\Gamma_S = \frac{\partial}{\partial S} \Delta_S = \frac{\partial}{\partial S} 1 = 0. \tag{13.130}$$

On the other hand, the gamma for a plain vanilla call or put option can be obtained by differentiating the *Black–Scholes*-formula twice with respect to *S<sup>t</sup>* . From the result

![](_page_30_Figure_1.jpeg)

**Fig. 13.3** Hedging of a call option position – Delta-hedge (dashed) and gammahedge (gray)

for the delta (13.123), we can immediately conclude that the gammas of the call and the put option have to coincide. Computing the second derivative yields

$$\Gamma_C = \Gamma_P = \frac{\phi(d_1)}{S_t \sigma \sqrt{T - t}} \quad \text{with} \quad \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2}.\n$$
(13.131)

A portfolio that is delta- and gamma-neutral is much more robust against changes in the price of the underlying. The reason for that is easily seen from Figure 13.3. The gamma-hedge corresponds to a second order *Taylor*-expansion around the current value *S<sup>t</sup>* of the underlying, whereas the delta-hedge is only a first order expansion. If the price of the underlying changes to *S* ∗ , the hedging error is significantly smaller, if the portfolio is delta- and gamma-neutral. But there is a downside. In order to build a delta- and gamma-neutral portfolio, we need a second traded option. How is such a portfolio constructed? Assume you have already a delta-neutral portfolio. Here is a simple recipe for establishing gamma-neutrality:

- 1. Start with a delta neutral portfolio Π.
- 2. Add a quantity *x*<sup>1</sup> = − ΓΠ Γ1 of another traded option *V*1, contingent on the same underlying, to your position. The resulting overall gamma is

$$\Gamma = x_1 \Gamma_1 + \Gamma_{\Pi} = 0.$$

3. Compute the delta of the overall position

$$\Delta = x_1 \Delta_1 + \Delta_{\Pi} = x_1 \Delta_1.$$

4. Add a quantity −∆ of the underlying. The resulting position is delta- and gammaneutral.

Let's see how this recipe works out in an example.

| Table 13.3 | Initial position |       |  |  |
|------------|------------------|-------|--|--|
| Position   | Delta            | Gamma |  |  |
| Portfolio  | 0                | −3000 |  |  |
| Option 1   | 0.6              | 1.6   |  |  |

## **Example 13.8**

Assume you start with a delta-neutral portfolio and an additional traded option as in Table 13.3. How is the position gamma-neutralized?

Solution

First, the required quantity in option 1 has to be computed

$$x_1 = -\frac{\Gamma_{\Pi}}{\Gamma_1} = \frac{3000}{1.6} = 1875.$$

Second, the delta of the overall position is

$$\Delta = x_1 \Delta_1 = 1875 \cdot 0.6 = 1125.$$

Thus, 1125 units of the underlying should be shorted to restore delta-neutrality. The new position is summarized in Table 13.4. ........................................................................................................................

## **13.9.3 Vega-Hedging**

Neutralizing small changes in the volatility of the underlying is called vega-hedging. This is a kind of inconsistent concept, because in the *Black–Scholes*-world the underlying is assumed to have a fixed volatility σ. Of course in reality the volatility is neither fixed, nor measurable. Nevertheless, there is strong evidence that the level of variability of the underlying changes with time. Consequently, the partial derivative of the option value with respect to volatility is called vega,

$$\mathcal{V} = \frac{\partial V}{\partial \sigma},\tag{13.132}$$

| Table 13.4<br>∆-Γ-neutral position |       |       |  |
|------------------------------------|-------|-------|--|
| Position                           | Delta | Gamma |  |
| Portfolio                          | 0     | −3000 |  |
| 1875 ·<br>V1                       | +1125 | +3000 |  |
| −1125<br>·<br>S                    | −1125 | 0     |  |
| Total                              | 0     | 0     |  |

| <b>Table 13.5</b> Initial position |       |         |         |
|------------------------------------|-------|---------|---------|
| Position                           | Delta | Gamma   | Vega    |
| Portfolio                          |       | $-3000$ | $-5000$ |
| Option 1                           | 0.6   | 1.6     | 2.0     |
| Option 2                           | 0.5   | 1.3     | 1.0     |

which is not a Greek letter at all. Everything we said so far about linearity of positions still holds for the yega of a portfolio. Thus, we can immediately delve into the question of how to construct a delta-, gamma-, and vega-neutral portfolio. This time, we need two additional traded options,  $V_1$  and  $V_2$ . Here is the recipe:

- 1. Again, start with a delta neutral portfolio  $\Pi$ .
- 2. Solve the linear system of equations

$$x_1\Gamma_1 + x_2\Gamma_2 = -\Gamma_{\Pi}$$
$$x_1\mathcal{V}_1 + x_2\mathcal{V}_2 = -\mathcal{V}_{\Pi}$$

for  $x_1$  and  $x_2$ .

- 3. Add a quantity  $x_1$  of  $V_1$ , and  $x_2$  of  $V_2$  to the position, where both options are contingent on the same underlying. The resulting overall position is gamma- and vega-neutral.
- 4. Compute the delta of the overall position

$$\Delta = x_1 \Delta_1 + x_2 \Delta_2.$$

5. Add a quantity  $-\Delta$  of the underlying. The resulting position is delta-, gamma-, and vega-neutral.

Here again is an example:

## Example 13.9

We start again with an already delta-neutral portfolio and two additional traded options as in Table 13.5. How is the position gamma- and vega-neutralized?

Solution

We first have to solve the linear system of equations

$$\begin{pmatrix}\n1.6 & 1.3 \\
2 & 1\n\end{pmatrix}\n\begin{pmatrix}\nx_1 \\
x_2\n\end{pmatrix} = \begin{pmatrix}\n3000 \\
5000\n\end{pmatrix}.$$

This is most conveniently accomplished by matrix inversion

$$\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1.6 & 1.3 \\ 2 & 1 \end{pmatrix}^{-1} \begin{pmatrix} 3000 \\ 5000 \end{pmatrix} = \begin{pmatrix} -1 & 1.3 \\ 2 & -1.6 \end{pmatrix} \begin{pmatrix} 3000 \\ 5000 \end{pmatrix} = \begin{pmatrix} 3500 \\ -2000 \end{pmatrix}.$$

| <b>Table 13.6</b> $\Delta$ -1 - <i>V</i> -neutral position |         |         |  |
|------------------------------------------------------------|---------|---------|--|
| Delta                                                      | Gamma   | Vega    |  |
| 0                                                          | $-3000$ | $-5000$ |  |
| $+2100$                                                    | $+5600$ | $+7000$ |  |
| $-1000$                                                    | $-2600$ | $-2000$ |  |
| $-1100$                                                    | 0       | 0       |  |
|                                                            |         | 0       |  |
|                                                            |         |         |  |

. . . . . . . .

Hence, we need an additional long position in 3500  $V_1$  and a short position in  $2000 V_2$ . The delta of the overall position is now

$$\Delta = 3500 \cdot 0.6 - 2000 \cdot 0.5 = 1100.$$

Thus, we have to short 1100 units of the underlying to restore delta-neutrality. The new position is summarized in Table 13.6.

Of course there are more Greeks and thus, more possible hedging schemes. For example the partial derivative with respect to time is called the theta of an option, and the partial derivative with respect to the risk-free interest rate is called rho. Table 13.7 summarizes the most common Greeks in terms of the generalized Black-Scholes-formulas for plain vanilla European call and put options. The generalizing factor  $a = e^{(b-r)(T-t)}$  equals one in the standard *Black–Scholes*-model.

| <b>Table 13.7</b> Generalized <i>Black—Scholes</i> -Greeks |                                                    |                                                                                                              |  |
|------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--|
| Name                                                       | Symbol                                             | $\text{Formula}^a$                                                                                           |  |
| Delta (call)                                               | $\Delta_C = \frac{\partial C}{\partial S}$         | $a\,\Phi(d_{+})$                                                                                             |  |
| Delta (put)                                                | $\Delta_P = \frac{\partial P}{\partial S}$         | $-a\Phi(-d_{\perp})$                                                                                         |  |
| Gamma                                                      | $\Gamma = \frac{\partial^2 V}{\partial S^2}$       | $a \frac{\phi(d_{+})}{S_{\omega} \sqrt{T-t}}$                                                                |  |
| Vega                                                       | $\mathcal{V} = \frac{\partial V}{\partial \sigma}$ | $a S_t \sqrt{T-t} \phi(d_+)$                                                                                 |  |
| Theta (call)                                               | $\Theta_C = \frac{\partial C}{\partial t}$         | $-a S_t \left( \frac{\sigma \phi(d_+)}{2\sqrt{T-t}} + (b-r)\Phi(d_+) \right) - re^{-r(T-t)} K \Phi(d_-)$     |  |
| Theta (put)                                                | $\Theta_P = \frac{\partial P}{\partial t}$         | $-a S_t \left( \frac{\sigma \phi(d_+)}{2\sqrt{T_{-t}}} - (b-r)\Phi(-d_+) \right) + re^{-r(T-t)} K\Phi(-d_-)$ |  |
| Rho (call)                                                 | $\rho_C = \frac{\partial C}{\partial r}$           | $(T-t)e^{-r(T-t)}K\Phi(d_{-})$                                                                               |  |
| Rho (put)                                                  | $\rho_P = \frac{\partial P}{\partial r}$           | $-(T-t)e^{-r(T-t)}K\Phi(-d_{-})$                                                                             |  |

<sup>a</sup> Note:  $d_{+/-}$  as in (13.86),  $a = e^{(b-r)(T-t)}$ , and generalized cost-of-carry rate b as in Table 13.1.

# **13.10 Transaction Costs**

Except for technical issues, transaction costs are the primary reason why hedging can only be done discretely. This has far reaching consequences as we will see soon. Our analysis will take us to the *Hoggard–Whalley–Wilmott*-equation (Hoggard et al., 1994), which is a nonlinear generalization of the *Black–Scholes*-equation. The very irritating consequence of the nonlinearity of this partial differential equation is that the value of a portfolio is not necessarily the sum of the values of its components. But first we have to study some results for normally distributed random variables.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Assume *Z* is a standard normally distributed random variable. We are interested in the properties of |*Z*|. Let's first try to evaluate its expectation value

$$E[|Z|] = \int_{-\infty}^{\infty} |z| \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz$$
  
$$= -\int_{-\infty}^{0} z \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz + \int_{0}^{\infty} z \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz$$
  
$$= \frac{2}{\sqrt{2\pi}} \int_{0}^{\infty} z e^{-\frac{1}{2}z^2} dz.$$
 (13.133)

In the last step we have used the symmetry of the standard normal probability density function around *z* = 0. The final integral in (13.133) is easily solved and yields one. We have thus

$$E[|Z|] = \sqrt{\frac{2}{\pi}}.\t(13.134)$$

Another expectation we will need is *E* [ *Z* |*Z*| ] . Again, split the integral to obtain

$$E[Z|Z|] = \int_{-\infty}^{\infty} z |z| \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz$$
  
= 
$$- \int_{-\infty}^{0} z^2 \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz + \int_{0}^{\infty} z^2 \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz.$$
 (13.135)

Both, *z* <sup>2</sup> and the standard normal probability density are even functions and thus, both integrals cancel each other. Hence, the result is

$$E[Z|Z|] = 0.\t(13.136)$$

We are now ready to discuss the derivation of the *Hoggard–Whalley–Wilmott*-equation (see also the appendix to chap. 48 in Wilmott, 2006c).

The starting point, as in the derivation of the *Black–Scholes*-equation, is again the geometric *Brown*ian motion

$$dS_t = \mu S_t dt + \sigma S_t dW_t. \tag{13.137}$$

But this time, we need a discrete analogue, because our continuous hedging argument will not apply. Instead we will use the approximation

$$\Delta S_t = \mu S_t \Delta t + \sigma S_t \sqrt{\Delta t} Z_t, \tag{13.138}$$

with  $Z_t \sim N(0, 1)$ .

**Ouick calculation 13.14** Verify that the distributions of  $\Delta W_t$  and  $\sqrt{\Delta t} Z_t$  coincide.

We can set up our usual hedge-portfolio  $\Pi = V(S, t) - \Delta \cdot S$ , but this time the change after the discrete time interval  $\Delta t$  is

$$\Delta \Pi = V(S + \Delta S, t + \Delta t) - V(S, t) - \Delta \cdot \Delta S. \tag{13.139}$$

The change in the portfolio value can be *Taylor*-expanded to arbitrary order, as long as  $V(S, t)$  can be assumed sufficiently smooth. In the case of continuous hedging, we merely had to expand to order dt, but in the discrete case terms of order  $\Delta t^{3/2}$  and higher do not vanish. We will nevertheless neglect those higher order terms because they are small, but keep in mind that the results only hold approximately to leading order. We thus obtain

$$\Delta \Pi = \frac{\partial V}{\partial t} \Delta t + \frac{\partial V}{\partial S} \Delta S + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} \Delta S^2 - \Delta \cdot \Delta S\n$$

$$\n= \sqrt{\Delta t} \, \sigma S Z \bigg( \frac{\partial V}{\partial S} - \Delta \bigg) + \Delta t \bigg( \frac{\partial V}{\partial t} + \mu S \bigg( \frac{\partial V}{\partial S} - \Delta \bigg) + \frac{1}{2} \sigma^2 S^2 Z^2 \frac{\partial^2 V}{\partial S^2} \bigg). \tag{13.140}$$

But (13.140) does not yet contain any transaction costs from hedging. Hoggard et al. (1994) used the assumption of Leland (1985) that transaction costs are proportional to the price of the underlying,  $\kappa S$ , where  $\kappa$  is a dimensionless cost factor, and to the quantity  $\nu$  to be shorted or purchased. Hence the transaction costs are

$$c_{\text{tr}} = \kappa S|\nu|.\tag{13.141}$$

The quantity  $\nu$  of the underlying to be sold or purchased depends on the change of the option delta over the time interval  $\Delta t$ 

$$\nu = \left. \frac{\partial V}{\partial S} \right|_{S + \Delta S, t + \Delta t} - \left. \frac{\partial V}{\partial S} \right|_{S, t} \\
\approx \left. \frac{\partial V}{\partial S} + \frac{\partial^2 V}{\partial S^2} \Delta S + \frac{\partial^2 V}{\partial S \partial t} \Delta t - \frac{\partial V}{\partial S}.\n$$
(13.142)

We will keep only terms to leading order  $\sqrt{\Delta t}$ . This can be heuristically justified by the fact that the transactions costs involve the absolute value  $|v|$ , which is defined as the positive root of  $v^2$ . Thus, we approximately obtain

$$|v| \approx \sigma S \sqrt{\Delta t} |Z| \left| \frac{\partial^2 V}{\partial S^2} \right|. \tag{13.143}$$

#### The Black-Scholes-Theory

Subtracting the transaction costs from (13.140), the change in the hedge-portfolio value becomes

$$\Delta\Pi = \sqrt{\Delta t} \,\sigma SZ \bigg(\frac{\partial V}{\partial S} - \Delta\bigg) + \Delta t \bigg(\frac{\partial V}{\partial t} + \mu S \bigg(\frac{\partial V}{\partial S} - \Delta\bigg) + \frac{1}{2}\sigma^2 S^2 Z^2 \frac{\partial^2 V}{\partial S^2}\bigg) - \sqrt{\Delta t} \,\kappa \sigma S^2 |Z| \bigg|\frac{\partial^2 V}{\partial S^2}\bigg| \,. \tag{13.144}$$

The next step is to compute the expectation value and the variance of the portfolio changes. We will choose the hedge-ratio to minimize the variance and equate the resulting expectation to the growth rate, induced by the risk-free interest rate. Of course the expected change in the portfolio value is not risk-free, but it has the smallest possible variance. But first let's compute the expectation value

$$E[\Delta \Pi] = \Delta t \left( \frac{\partial V}{\partial t} + \mu S \left( \frac{\partial V}{\partial S} - \Delta \right) + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) - \sqrt{\Delta t} \kappa \sigma S^2 \sqrt{\frac{2}{\pi}} \left| \frac{\partial^2 V}{\partial S^2} \right|. \tag{13.145}$$

We used of course that  $E[Z^2] = \text{Var}[Z] = 1$  and (13.134). To compute the variance, remember that for any random variable X,  $\text{Var}[X] = E[X^2] - E[X]^2$  holds. Thus, let's compute the expectation of the squared portfolio change. Keep in mind that only terms up to order  $\Delta t$  survive and that  $E[Z|Z] = 0$ ,

$$E[\Delta \Pi^2] = \Delta t \left( \sigma^2 S^2 \left( \frac{\partial V}{\partial S} - \Delta \right)^2 + \kappa^2 \sigma^2 S^4 \left( \frac{\partial^2 V}{\partial S^2} \right)^2 \right). \tag{13.146}$$

**Quick calculation 13.15** Confirm this equation.

Putting both pieces together, and once again neglecting terms of higher order than  $\Delta t$ , one obtains

$$\text{Var}[\Delta \Pi] = \Delta t \left( \sigma^2 S^2 \left( \frac{\partial V}{\partial S} - \Delta \right)^2 + \left( 1 - \frac{2}{\pi} \right) \kappa^2 \sigma^2 S^4 \left( \frac{\partial^2 V}{\partial S^2} \right)^2 \right). \tag{13.147}$$

From (13.147) it is immediately clear that choosing the familiar hedge-ratio  $\Delta = \frac{\partial V}{\partial S}$ minimizes the variance. It is also obvious that the variance collapses to zero, if the cost factor  $\kappa$  is zero. Substituting the minimum-variance hedge-ratio into the expectation  $(13.145)$  yields

$$E[\Delta \Pi] = \Delta t \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) - \sqrt{\Delta t} \kappa \sigma S^2 \sqrt{\frac{2}{\pi}} \left| \frac{\partial^2 V}{\partial S^2} \right| . \tag{13.148}$$

If the hedge-portfolio were riskless, it would grow over the interval  $\Delta t$  with the risk-free interest rate

$$\Delta \Pi = r \Pi \Delta t = r V \Delta t - r S \frac{\partial V}{\partial S} \Delta t. \tag{13.149}$$

Equating the expected variance-minimal change and the risk-free change of the portfolio, and dividing by  $\Delta t$ , yields the *Hoggard–Whalley–Wilmott*-equation

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \kappa \sigma S^2 \sqrt{\frac{2}{\pi \Delta t}} \left| \frac{\partial^2 V}{\partial S^2} \right| - rV = 0. \tag{13.150}$$

Comparing (13.150) with the original *Black–Scholes-PDE*, there is an additional term, representing the influence of transaction costs. We can learn a great deal from this correction. First of all, if the cost factor is  $\kappa = 0$ , we are back in the original *Black*-Scholes-world. Second, for  $\kappa > 0$  in the limit  $\Delta t \rightarrow 0$ , the transaction costs become infinitely high, prohibiting quasi-continuous rebalancing of the hedge-portfolio. But there is more. Recall that the gamma of a plain vanilla European contract is always positive,

$$\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\phi(d_1)}{S_t \sigma \sqrt{T - t}},\tag{13.151}$$

with  $d_1$  given in (13.79) on page 266. If we assume that this also holds in the presence of transaction costs, we can abandon the modulus sign and invent a new volatility for the long position in the contract

$$\sigma_{\text{long}}^2 = \sigma^2 - 2\kappa\sigma\sqrt{\frac{2}{\pi\Delta t}}.\tag{13.152}$$

With this new volatility,  $(13.150)$  simplifies to

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma_{\rm long}^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0.$$
 (13.153)

But this is again the original *Black–Scholes*-PDE, with a corrected volatility  $\sigma_{\text{long}} < \sigma$ . But be careful, there is a very subtle point. If we had assembled the hedge-portfolio the other way around, starting with a short position in the option contract, all signs would have come out the opposite way, with exception of the transaction costs. They would have remained negative. Thus, for the short position in a plain vanilla call or put, we obtain a corrected volatility with opposite sign,

$$\sigma_{\text{short}}^2 = \sigma^2 + 2\kappa\sigma\sqrt{\frac{2}{\pi\Delta t}}.\tag{13.154}$$

The volatility corrections  $(13.152)$  and  $(13.154)$  are the main results of Leland  $(1985)$ , but the *Hoggard–Whalley–Wilmott*-equation is far more general. It explains in a very natural way why bid-offer spreads are unavoidable, if perfect hedging is not possible. Let's do one more computation. We can determine the order of magnitude of the spread to be expected, depending on a given transaction cost factor  $\kappa$ . To prepare the computation, *Taylor*-expand the corrected volatility for the short position around  $\kappa = 0$ 

$$\sigma_{\text{short}} \approx \sigma + \kappa \sqrt{\frac{2}{\pi \Delta t}}.$$
 (13.155)

**Quick calculation 13.16** Confirm this linear expansion.

We would expect the bid-offer spread to be roughly twice the difference between the original *Black–Scholes*-price and the one with corrected volatility

$$2(V_{\text{short}} - V) \approx 2 \frac{\partial V}{\partial \sigma} (\sigma_{\text{short}} - \sigma). \tag{13.156}$$

Plugging in the vega of a plain vanilla option and using the *Taylor*-expansion (13.155), one obtains √

spread 
$$\approx \frac{4\kappa S_t \phi(d_1) \sqrt{T-t}}{\sqrt{2\pi\Delta t}}$$
. (13.157)

This result again confirms that the bid-offer spread vanishes if transaction costs are zero. But remember that our volatility corrections and the spread approximation only hold for plain vanilla European contracts.

It is now clear, how the nonlinearity of the *Hoggard–Whalley–Wilmott*-equation prevents the portfolio value from being the sum of the value of its components. Because it introduces a bid-offer spread, we have different prices for short and long positions. Suppose you hold a short and a long position in a plain vanilla contract, contingent on the same underlying, with identical exercise price and time to expiry. Clearly the overall value of this position is zero, because no matter what happens, the payoffs will cancel exactly. But if you hedge this position, you lose money because of the bid-offer spread, even though the payoffs will still cancel exactly. You can see most easily that the componentwise value of this position is negative, by realizing that the short position in the plain vanilla contract is more expensive, because after the *Leland*-correction, its volatility is larger than that of the long position. Hence, the sum of both positions is negative, because the more expensive short position comes with a minus sign.

# **13.11 Merton's Firm Value Model**

Merton (1974) used a hidden connection between the financial macrostructure of a firm and option valuation, to introduce an ingenious model for the value of a firm. His idea is the basic component of what is called structural models in credit risk management today. His assumptions look a little coarse-grained but they are also very robust. Here is the framework:

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

- The firm is only funded by debt *D* and equity *S*.
- All debt is in form of a corporate zero-coupon bond *B*0(*t*,*T*), with principal *D*, due at time *T*.
- The value of the firm is the sum of debt and equity, *V<sup>t</sup>* = *S<sup>t</sup>* + *B*0(*t*,*T*).
- Both *V<sup>t</sup>* and *S<sup>t</sup>* follow a geometric *Brown*ian motion.

When the debt is due, there are only two possible scenarios. Either the firm value is greater than the liabilities, *V<sup>T</sup>* ≥ *D*, then the debt is repaid and the remaining assets

| <b>Table 13.8</b> Firm value in Merton's model |                        |                                     |                              |  |
|------------------------------------------------|------------------------|-------------------------------------|------------------------------|--|
| Event                                          | Firm value             | Liabilities                         | Equity                       |  |
| No default<br>Default                          | $V_T > D$<br>$V_T < D$ | $B_0(T,T) = D$<br>$B_0(T, T) = V_T$ | $S_T = V_T - D$<br>$S_T = 0$ |  |

belong to the investors, or the firm value is insufficient to fully repay the debt,  $V_T <$ D, then there is only a partial redemption and the investors get nothing. In this case the investors are of course not willing to provide additional capital, because creditors would immediately collect their pending debts and so this event represents default. Table 13.8 summarizes the consequences of both scenarios for the value of debt and equity.

Let's see, if we can summarize the value of the equity at the terminal date  $T$  in a simple equation

$$S_T = \max(V_T - D, 0) = (V_T - D)^{+}.$$
 (13.158)

Does that ring a bell? The value of the equity at time  $T$  matches precisely the payoff function of a call option on the firm value with exercise price  $D$ . Let's see, what we get for the liabilities

$$B_0(T,T) = \min(D, V_T) = D - (D - V_T)^+.$$
(13.159)

**Ouick calculation 13.17** Convince yourself that the last equality indeed holds.

That is, the liabilities correspond to the debt plus a short position in a plain vanilla put option. The only problem with this identification is that we cannot compute the option value.

To see where the computation fails, let's write the *Black–Scholes*-formula for the value of the equity

$$S_t = V_t \Phi(d_1) - e^{-r(T-t)} D\Phi(d_2), \tag{13.160}$$

with

$$d_{1/2} = \frac{\log(V_t/D) + (r \pm \frac{1}{2}\sigma_V^2)(T - t)}{\sigma_V \sqrt{T - t}}.$$
(13.161)

Although we might be able to estimate the parameters of the geometric *Brown*ian motion  $\mu_S$  and  $\sigma_S$  for the equity, from observing the stock price  $S_t$ , the firm value process  $V_t$  is unobservable. Thus there are two quantities we do not know,  $V_t$  and  $\sigma_V$ . But there is a remedy. Since we can observe the market price of the stock,  $(13.160)$  is one equation in two unknowns. If we can find a second equation, we are in business.

#### The Black-Scholes-Theory

Since the firm value follows a geometric *Brown*ian motion, and equity is a derivative, contingent on the firm value, we can apply Itô's lemma,

$$dS = \left(\mu_V V \frac{\partial S}{\partial V} + \frac{\partial S}{\partial t} + \frac{1}{2} \sigma_V^2 V^2 \frac{\partial^2 S}{\partial V^2}\right) dt + \sigma_V V \frac{\partial S}{\partial V} dW_V. \tag{13.162}$$

On the other hand we know that the equity process itself is a geometric *Brown*ian motion

$$dS = \mu_S S dt + \sigma_S S dW_S. \tag{13.163}$$

We not only have two equations for dS, but the distributions of  $dW_V$  and  $dW_S$  coincide. Thus we can match the terms. Taking the diffusion term yields

$$\sigma_S S = \sigma_V V \frac{\partial S}{\partial V}.$$

Finally realize that the partial derivative in (13.164) is the *Black–Scholes*-delta of the call option  $\frac{\partial S}{\partial V} = \Phi(d_1)$ . This argument is of course valid for every time  $0 \le t \le T$  and thus, we obtain the second equation

$$\sigma_S S_t = \sigma_V V_t \Phi(d_1), \tag{13.165}$$

with  $d_1$  as in (13.161). This is the second equation in the two unknowns  $V_t$  and  $\sigma_V$ . Unfortunately, there is no analytic solution for the desired quantities; they have to be determined numerically. But that is no big deal because the problem is not ill posed.

## 13.12

## **Further Reading**

The seminal papers of Black and Scholes (1973) and Merton (1973) are at the heart of the subject. There are many well written textbooks, detailing the derivation of the *Black–Scholes*-equation. A small collection is Hull (2009), Neftci (2000), Shreve (2004b), and Wilmott (2006a). For a deeper background in stochastic differential equations and the Itô-integral see Arnold (1974) and Shreve (2004b, chap. 4). For technical details about generalized functions and their *Fourier*-transforms see Rudin (1991, chap.  $6 \& 7$ ). A comprehensive source for the theory of partial differential equations is Evans (2010). Generalizations of the *Black–Scholes*-formula can be found in Haug  $(2007, \text{sect. 1.1.6})$ . The subject of discrete dividend payments is treated very accessibly in Haug  $(2007, \text{chap. } 9)$  and Wilmott  $(2006a, \text{sect. } 8.3)$ . Analytical approximations for the value of American options can be found in Haug (2007, chap. 3). General hedging strategies based on option Greeks are detailed with examples in Hull (2009, chap. 17). For more background information on transaction costs, see Wilmott (2006c, chap. 48). There is also an interesting version of Merton's firm value model provided in Wilmott (2006b, chap. 39).

13.13

# Problems

**13.1** Use Itô's lemma to show that the forward price

$$F_t = e^{r(T_F - t)} S_t$$

follows the stochastic process

$$dF_t = (\mu - r)F_t dt + \sigma F_t dW_t,$$

if the dynamics of  $S_t$  are governed by the geometric *Brownian* motion (13.5) on page 250.

**13.2** The evolution of the bank account is governed by

$$dB(t) = rB(t)dt$$
,

which can be understood as geometric *Brownian* motion with  $\sigma = 0$ . Manipulate the resulting *Black–Scholes*-equation to show that it is equivalent to the so-called transport equation

$$\frac{\partial U}{\partial t} + r \frac{\partial U}{\partial x} = 0,$$

with the substitution  $V(B, t) = e^{-r(T-t)} U(B, t)$  and  $x = \log B$ .

- **13.3** Consider the fair price of a European plain vanilla binary contract in the *Black*-*Scholes*-framework. What is the delta of a binary call and put option?
- **13.4** Prove that the so-called European put-call symmetry

$$C_t(K,T) = \frac{K}{e^{b(T-t)}S_t} P_t\left(\frac{e^{2b(T-t)}S_t^2}{K},T\right)$$

holds in the generalized *Black–Scholes*-framework.

**13.5** There is another Greek called vanna, defined by the mixed partial derivative

$$\text{vanna} = \frac{\partial^2 V}{\partial S \partial \sigma}.$$

Derive the vanna of a European plain vanilla contract and show that it is identical for both put and call options.

**13.6** Derive an explicit formula for the value of the liabilities in the *Merton*-model of the firm value.
# **Default Time Copulas**

Copulas are used in mathematical statistics to describe *multivariate distributions* in a way that separates the marginal distributions from the codependence structure. More precisely, any multivariate distribution can be "decomposed" into its *marginal distributions* and a multivariate distribution with uniform marginals. Suppose *X*1*,...,Xn* are realvalued stochastic variables with marginal distributions

$$f_i(x) = P(X_i \le x), \quad i = 1, \dots, n$$
 (1)

where the right-hand side denotes the probability that *Xi* takes a value less than or equal to *x*. Suppose further that *C* is a distribution function on the *n*-dimensional unit hypercube with uniform marginals.a Then we can define a joint distribution of *(X*1*,...,Xn)* by

$$P(X_1 \le x_1, \ldots, X_n \le x_n) = C(f_1(x_1), \ldots, f_n(x_n))$$
(2)

We say that *C* is the *copula function* of the joint distribution. Clearly, the copula function for a given distribution is unique. Existence, that is, the actual existence of a copula function for any joint distribution, is established by *Sklar's Theorem* [3]. Given the definition of a copula, it is clear that a default time copula is a copula for the joint distribution of default times. Here, as in other applications in finance, the main advantage of using a copula formulation is that the marginal distributions are implied from the market, independent of information about mutual dependencies between default times. Specifically, the distribution of the time of default of a single firm can be implied<sup>b</sup> from the par spread of the credit default swap (CDS) contracts on the debt of the firm. This distribution is represented by the "default curve":

$$p_i(t) = P(\tau_i \le t) \tag{3}$$

where *τi* is the stochastic default time of the *i*th firm.c Once we have determined the marginal distributions of the default rates of single firms in this way, we may model mutual dependencies between these default times by choosing a suitable copula function and writing the joint distribution of default times as in equation (2). From a practical point of view it is a great advantage that, by construction, the marginal distributions are unchanged under a change of copula. This allows us to preserve the calibration to market CDS quotes while adjusting the codependence structure.

## **Factor Copulas**

In practice, copula functions are rarely specified directly for the default times. Instead, we introduce stochastic "default trigger variables" *Xi* such that we can identify events

$$\{X_i \le h_i(t)\} \equiv \{\tau_i \le t\} \tag{4}$$

for suitable nondecreasing functions *hi* : <sup>+</sup> → such that

$$P(X_i \le h_i(t)) = p_i(t) \tag{5}$$

We may regard the trigger variables as just a convenient mathematical device, but we may also follow Merton [2] and view *Xi* as the (return of the) value of the assets of the *i*th firm. With this interpretation, we may further interpret *hi(T )* for some fixed time horizon *T* as the face value of the firm's debt maturing at *T* . In this picture, default coincides with insolvency.

One advantage of using default trigger variables rather than default times is that the codependency of firm values is more susceptible to economic reasoning. For example, we can think of asset values as being driven by a common factor representing general economic conditions. Then we would use a decomposition such as

$$X_i = f_i(Z) + \epsilon_i \tag{6}$$

where *Z* is the common factor, *<sup>i</sup>* are idiosyncratic components independent of each other and of *Z*, and *fi* are suitable "loading functions". Note that, conditional on a given factor value, the trigger variables and, therefore, the default times, will be independent. The (unconditional) joint distribution is determined, for given distributions of *Z* and the *i*s, by the loading functions *fi*.

A default time copula specified by default triggers with the decomposition in equation (6) is called a *factor copula*. Most, if not all, copula models used in derivatives pricing are factor copulas.

## **Pricing with Copula Models**

The generic application of default time copulas is in the pricing of CDO tranches, that is, tranches of a portfolio of debt instruments referencing a (large) number of issuers. Such a tranche is a special case of a security whose future cash flows is a function of the default times of the issuers. The present value of such a security is given by an expectation over the joint default time distribution, which, in the general case, has to be evaluated by Monte Carlo, that is, by random sampling from the distribution. However, as we shall now discuss, for certain types of securities, the expectation can be calculated by a much faster method if a factor copula is used.

#### Loss Distributions

Although it is true that a CDO tranche depends on the joint default time distribution, it does so in a rather special way since, in fact, it only depends on the total loss in the portfolio; in particular, it does not depend on the identity of the defaulted names, or on the order in which they default. More precisely, we can compute the value of a tranche if we know the distribution of the cumulated portfolio loss out to any time up to tranche maturity.<sup>d</sup> As we shall now see, the computation of such loss distributions is particularly simple in a factor model.

We shall first show how to compute the distribution of portfolio loss to some fixed horizon  $t$  conditional on some given factor value z. To lighten the notation, we suppress the parameters  $z$  and  $t$ . Let  $p_i$  be the conditional probability that the *i*th issuer defaults and assume that the loss in default is given by some constant<sup> $e$ </sup>  $u$ . Further define

$$P_l^{(n)} = P(L^{(n)} = lu) \tag{7}$$

where  $L^{(n)}$  is the default loss from the first *n* issuers (in some arbitrary order).

Then we have the following recursion relation (see [1])

$$P_{l}^{(n+1)} = (1 - p_{n+1})P_{l}^{(n)} + p_{n+1}P_{l-1}^{(n)} \qquad (8)$$

which allows us to build the loss distribution for any portfolio from the trivial case of the empty portfolio

$$P_l^{(0)} = \delta_{l,0} \tag{9}$$

From the conditional loss distributions, we obtain the unconditional loss distribution by integration<sup>f</sup> over z.

We remark that using equation (8) amounts to explicitly doing the convolution of the independent conditional loss distribution for each issuer in order to obtain the distribution of the portfolio loss. This convolution could also be done by Fourier techniques although this involves a somewhat greater computational burden. Note that by suitably inverting the convolution, one may compute the sensitivities of the tranche value to the parameters, for example, default probability, of each issuer. These are very important quantities in financial risk management.

#### **Concluding Remarks**

Models based on default time copulas are in widespread use for pricing and risk managing portfolio credit derivatives such as CDO tranches. The important special case of factor copulas combines the dual advantages of providing a clear economical interpretation of default time codependence and of allowing computationally efficient implementations.

The main practical limitation of copula models is that they are not *dynamic* models in the sense that they do not allow any conditioning on the future state of the world. This means that copula models cannot be reliably used, for example, in the pricing of options on tranches since here we have to be able to determine the distribution of the value of the underlying tranche conditioned on the state at option expiration time. To address such problems, we need a model that specifies the stochastic dynamics of a sufficient set of state variables. For example, we could specify the joint dynamics of all default intensities. Any such model would, of course, produce a joint default time distribution which would be describable by a copula and marginals. But this is not a one-toone relationship since different dynamic models can produce the same copula. In this sense, the copula approach is more efficient for securities that depend only on the joint distribution of default times.

#### **End Notes**

<sup>a</sup>. This simply means that  $C : [0, 1]^n \rightarrow [0, 1]$  is nondecreasing in each argument,  $C(0, \ldots, 0) = 0$ ,  $C(1, \ldots, 1) = 1$ , and that, for any *i* and any  $y_i \in [0, 1]$ ,

$$\int_0^1 \mathrm{d}y_1 \ldots \int_0^1 \mathrm{d}y_{i-1} \int_0^1 \mathrm{d}y_{i+1} \ldots \int_0^1 \mathrm{d}y_n \, C(y_1, \ldots, y_n) = y_i.$$

b*.* Given suitable assumptions about *recovery* in default.

c*.* Note that this distribution is the so-called risk-neutral distribution,which differs from the real-world, or physical, distribution unless there is no *risk premium* associated with the risk of default.

d*.* In practice, this is approximated by a finite set of times. e*.* This assumption is just for notational convenience; the extension to issuer specific, and possibly random, loss amounts is straightforward.

f*.* If *z* has real dimension ≤ 3, a quadrature scheme can be used, otherwise Monte Carlo integration is more efficient.

## **References**

[1] Andersen, L., Sidenius, J. & Basu, S. (2003). All your hedges in one basket, *RISK* November, 67–72.

- [2] Merton, R. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [3] Sklar, A. (1959). *Fonctions de R´epartition `a n Dimensions et Leurs Marges*, Publications de l'Institut de Statistique de L'Universite de Paris, Paris, Vol. 8, pp. 229–231. ´

## **Related Articles**

**Copulas: Estimation**; **Copulas in Econometrics**; **Copulas in Insurance**; **Exposure to Default and Loss Given Default**; **Gaussian Copula Model**; **Random Factor Loading Model (for Portfolio Credit)**; **Recovery Rate**.

JAKOB SIDENIUS
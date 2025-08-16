# **Intensity Gamma Model**

The intensity gamma model is a model for pricing portfolio credit derivatives developed in [2]. Its innovation was to use stochastic time change (*see* **Time Change**) to achieve clustering of defaults and therefore correlation between them. This was in contrast to the popular models available at the time, which relied on copulas, such as the Gaussian copula model (*see* **Gaussian Copula Model**). The model is designed to infer the joint distribution of the default times of some set of names from the marginal distributions. Some additional market information about the level of correlation is required for calibration; this is typically obtained from liquid correlation products.

Once a joint distribution for the default times has been obtained (in some suitable pricing measure), products whose cash flows depend on those defaults can be priced. The classic examples include collateralized debt obligations (CDOs) (*see* **Collateralized Debt Obligations (CDO)**) and *n*th-to-default baskets (*see* **Basket Default Swaps**). However, it is no more difficult to handle other products in which the cash flows depend on the exact defaults occurring in quite arbitrary ways, such as CDO-squared (*see* **CDO Square**). This approach is more robust and more general than techniques founded on mapping methodologies such as base correlation (*see* **Base Correlation**). The intensity gamma model, like other reduced-form models (*see* **Reduced Form Credit Risk Models**), is an arbitrage-free model that matches the market and allows pricing of derivatives on arbitrary functions of defaults, rather than attempting to interpolate prices of nontraded tranches.

On the other hand, the intensity gamma model is not designed to capture the volatility of credit spreads or stochastic correlation. The credit spreads of individual names are deterministic functions of time, within the model, up until their default. This is a significant limitation and certainly prevents the use of the model for handling certain products such as options on CDOs.

#### **Model Definition**

The core idea of the model is that defaults are driven by a business time process, *Xt* , which is an increasing adapted process with *X*<sup>0</sup> = 0. This process intuitively represents the amount of bad news that has arrived by time *t*, and as bad news arrives, each name has a chance of defaulting in response to the bad news, with names behaving *conditionally* independently, that is, for a given amount of bad news, each name then defaults independently with a certain probability. The fact that all names are driven by the same business time process introduces correlation into the defaults.

To describe more precisely, we start by considering a homogeneous default process in which individual default rates are constant across the time period of interest. The business time process *(Xt)* will be a subordinator, that is, an increasing Levy ´ process (*see* **Levy Processes ´** ), and in practice it is normally taken to be a constant drift at rate *a* plus either a gamma process or the sum of two independent gamma processes [1]. A gamma process, *(t)*, is described by two parameters, which we denote by *γ* and *λ*, and then *t* has a gamma*(γ t, λ)* distribution, that is to say a density function *f* given as

$$f(x) = \frac{\lambda^{\gamma t}}{\Gamma(\gamma t)} x^{\gamma t - 1} e^{-\lambda x} \tag{1}$$

Suppose that we have some set of reference names {*Ai* : *i* ∈ *I* }. In the most basic form of the intensity gamma model, each name *Ai* defaults at some constant rate *ci* with respect to the passage of business time as given by the process *(Xt)*. That is to say, conditional on the path *(Xt)t*<sup>≤</sup>*<sup>T</sup>* , the name *Ai* will have survived (i.e., not defaulted) to time *T* with probability

$$e^{-c_i X_T} \tag{2}$$

with the default events being independent after conditioning on *(Xt)*.

## **Calibration of the Model to Individual Default Probabilities**

We assume that single-name survival probabilities have been inferred from CDS spreads or bond prices using some simple recovery rate assumption, as is common practice in CDO pricing. The model survival probability is given by integrating the conditional survival probability (2) against the law of *XT* , which amounts to taking a Laplace transform of this law. Suppose for now that this law (and its parameters) has somehow been determined. In the case when it is a single gamma distribution with parameters *(γ T , λ)*, the required Laplace transform is simple and well known to be

$$\frac{1}{\left(1+c_i/\lambda\right)^{\gamma T}}\tag{3}$$

When *XT* is a sum of independent gamma processes, then the survival probability is the product of the corresponding probabilities for each gamma process (3); similarly, a drift of rate *a* introduces a further multiplicative term into the survival probability of e<sup>−</sup>*aciT* . Thus, there is a straightforward analytic expression for the survival probability of an individual name, and we can use this to quickly solve for *ci* to fit the market-implied survival probability for the time horizon of interest.

More generally, we may wish to calibrate to market-implied survival probabilities for a series of time horizons 0 = *t*<sup>0</sup> *< t*<sup>1</sup> *< t*<sup>2</sup> *<...<tn* = *T* . This can be done by generalizing the definition to allow a default rate (with respect to business time) *ci(t)*, which is a function of calendar time *t*, which is constant over each subinterval of calendar time of the form [*tj , tj*+1].

#### **Pricing Correlation Products**

In the following section, we discuss the issue of how to choose the parameters of our business time process *Xt* and describe now how we price a correlation product, such as a CDO, once these parameters have been specified. From the preceding section, we rapidly calibrate the default rates of all relevant individual names to the single-name credit market at some fixed sequence of time horizons, 0 = *t*<sup>0</sup> *< t*<sup>1</sup> *<...<tn* = *T* . The correlation product is then priced by Monte Carlo. For each Monte Carlo path, we must first draw the random business time process, *(Xt)t*<sup>≤</sup>*<sup>T</sup>* , where *T* is the last relevant possible default date for the product; this can be done with a finite-dimensional random draw and results in an (arbitrarily precise) approximation to the business time path by one which contains a finite number of jumps imposed on a path with a constant drift: details can be found in [2] adapted from a method in [1]. Having determined the random path *(Xt)*, one can then generate the defaults by drawing an independent uniformly distributed random variable *Ui* for each name *Ai* and saying that *Ai* has defaulted by time *S* if and only if

$$\exp\left(-\int_0^S c_i(t) \, \mathrm{d}X_t\right) < U_i \tag{4}$$

#### **Calibrating to the Correlation Market**

First, note that doubling the business time process (corresponding to doubling the *λ* parameters and the drift parameter *a*) would be canceled out exactly by halving all the default intensities *ci*; thus, the business time process effectively has a redundant parameter and we may assume, without loss of generality, that *a* = 1. Therefore, if there are two independent gamma processes, there are four free parameters controlling the process and hence the default correlation.

With four free parameters, it is possible to obtain a variety of shapes of the correlation graph, and one can therefore calibrate to multiple tranches simultaneously rather than having to use different correlations for each tranche. This ability to match the correlation smile was a major motivation for the model's introduction. For any given choice of business process parameters, calibrating to the single-name market is instant and pricing CDO tranches by Monte Carlo is fairly quick. A multidimensional route finder can then be used to calibrate the business process parameters to as many independent tranche prices as there are parameters. In practice, one will choose the quoted tranche prices from some major index such as iTraxx or CDX. The index will typically be chosen to have similar properties in terms of maturity, region, diversity, and credit quality as the bespoke correlation product that we are ultimately aiming to price.

For further details on the model, we refer the reader to the original paper [2] or to the recent book [3].

### **References**

- [1] Cont, R. & Tankov, P. (2003). *Financial Modelling with Jump Processes*, Chapman and Hall.
- [2] Joshi, M.S. & Stacey, A.M. (2006). Intensity gamma: a new approach to pricing portfolio credit derivatives, *Risk Magazine* July 78–83.
- [3] O'Kane, D. (2008). *Modelling Single-name and Multiname Credit Derivatives*, Wiley.

#### **Related Articles**

**Basket Default Swaps**; **Collateralized Debt Obligations (CDO)**; **Levy Processes ´** ; **Intensity-based Credit Risk Models**; **Reduced Form Credit Risk Models**.

MARK JOSHI & ALAN STACEY
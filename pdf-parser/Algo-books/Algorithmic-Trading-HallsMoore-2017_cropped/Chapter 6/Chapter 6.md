# Chapter 6

# Bayesian Stochastic Volatility Model

In this chapter all of the Bayesian statistical theory discussed thus far will be utilised to build a Bayesian stochastic volatility model. Such a model allows estimation of current and historical volatility levels of asset returns. Within quantitative trading this is useful from the perspective of risk management as it provides a "risk filter" mechanism for trade signals.

A Bayesian stochastic volatility model provides a full posterior probability distribution of volatility at each time point t, as opposed to a single "point estimate" often provided by other models. This posterior encapsulates the uncertainty in the parameters and can be used to obtain credible intervals (analogous to confidence intervals) and other statistics about the volatility.

This chapter is heavily influenced by two main sources. The first is a paper written by Hoffman and Gelman[53], which introduced a highly efficient form of Markov Chain Monte Carlo, known as the No-U-Turn Sampler (NUTS). The outline of NUTS is beyond the scope of the book. For a detailed reference, refer to the paper.

The paper describes a Bayesian formulation of a stochastic volatility model, the sampling of which is carried out using the presented NUTS technique. The presented model is the main inspiration for the model in this chapter. The second source is the Python PyMC3 library[10] tutorial article by Salvatier, Fonnesbeck and Wiecki[89] on applying such a model within the PyMC3 MCMC library.

This chapter will closely follow these two sources but will provide a fully functional end-to-end script that can be used to estimate volatility for daily equities returns.

# 6.1 Stochastic Volatility

A stochastic volatility model consists of an underlying generative process for the volatility of asset returns, which is then used to provide a time-varying variance in the model for the asset returns distribution itself.

They are used to account for the empirical fact that volatility in financial markets tends to cluster together. An example of which is the period of excess volatility that occured in the 2008 financial crisis. In time series analysis this "volatility clustering" is known as heteroskedasticity. Another stochastic volatility model, known as GARCH, will be considered later in the book.

Readers who have also read the C++ For Quantitative Finance ebook by QuantStart will be aware of the continuous Heston stochastic volatility model. This is specified via a pair of

stochastic differential equations (SDE). Using the same notation from that book the model is given below:

$$dS_t = \mu S_t dt + \sqrt{\nu_t} S_t dW_t^S \tag{6.1}$$

$$d\nu_t = \kappa(\theta - \nu_t)dt + \xi \sqrt{\nu_t}dW_t^{\nu}$$

$$(6.2)$$

This model says that the change in the volatility ν is a mean-reverting process, with its own variance given by ξ. Thus the volatility has a mean of κθ but can take on more extreme values occasionally.

The asset paths themselves, given by St, follow a Geometric Random Walk model with the variance given by the square root of the volatility process.

In this section a simpler stochastic volatility model will be provided that does not assume mean reversion of volatility. Instead the volatility ν will follow a Gaussian Random Walk with the returns distributed as a Student's t-distribution, with variance derived from ν.

# 6.2 Bayesian Stochastic Volatility

In order to implement the Bayesian approach to stochastic volatility it is necessary to select priors for the model parameters. These parameters include σ, which represents the scale of the volatility and ν, which represents the degrees of freedom of the Student's t-distribution. Priors must also be selected for the latent volatility process and subsequently the asset returns distribution.

At this stage the uncertainty on the parameter values is large and so the selected priors must reflect that. In addition σ and ν must be real-valued positive numbers, so we need to use a probability distribution that has positive support. As an initial choice the exponential distribution will be chosen for σ and ν. The Python code to visualise a set of PDFs for the exponential distribution is given below and plotted in Figure 6.1:

# exponential\_plot.py

```
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
if __name__ == "__main__":
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})
    x = np.linspace(0.0, 5.0, 100)
    lambdas = [0.5, 1.0, 2.0]
    for lam in lambdas:
        y = lam*np.exp(-lam*x)
        ax = plt.plot(x, y, label="$\\lambda=%s$" % lam)
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend(title="Parameters")
```

![](_page_2_Figure_1.jpeg)

Figure 6.1: Different realisations of the exponential distribution for various parameters λ.

Note that a much larger parameter value is chosen for σ than ν because there is a lot of initial uncertainty associated with the scale of the volatility generating process. As more data is provided to the model the Bayesian updating process will reduce the spread of the posterior distribution reflecting an increased certainty in the scale factor of volatility.

This stochastic volatility model makes use of a random walk model for the latent volatility variable. Random walk models are discussed in significant depth within the subsequent time series chapter on White Noise and Random Walks. However the basic idea is that the latent volatility at time point i, namely s<sup>i</sup> is a function only of the previous time point value si−<sup>1</sup> along with some normally distributed error. In probabilistic terms this is written as:

$$s_i \sim \mathcal{N}(s_{i-1}, \sigma^{-2}) \tag{6.3}$$

That is, the value of the latent vol at i, s<sup>i</sup> , has a normally distributed prior centred at the previous value (si−1) with variance σ −2 . This variance, as was seen above, is distributed as an exponential distribution.

It remains only to assign a prior to the logarithmic returns of the asset price series being modelled. The point of a stochastic volatility model is that these returns are related to the underlying latent volatility variable. Hence any prior that is assigned to the log returns must have a variance that involves s.

One approach (utilised in the PyMC3 tutorial) is to assume that the log returns, log(yi/yi−1) are distributed as a Student's t-distribution, with mean zero and variance given as the exponential of negative of the latent vol variable. Figure 6.2 shows how the PDF of a Student's t-distribution

changes as the number of degrees-of-freedom are increased. Notice that the kurtosis becomes smaller–the tails become less "fat"–representing lesser likelihood of more extreme events:

```
# student_t_plot.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
import seaborn as sns
if __name__ == "__main__":
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})
    x = np.linspace(-5.0, 5.0, 100)
    nus = [1.0, 2.0, 5.0, 50.0]
    for nu in nus:
        y = t.pdf(x, nu)
        ax = plt.plot(x, y, label="$\\nu=%s$" % nu)
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend(title="Parameters")
    plt.show()
```

![](_page_3_Figure_2.jpeg)

Figure 6.2: Different realisations of Student's t-distribution for various parameters ν.

The degrees of freedom of the Student's t–how much kurtosis it possesses–is governed by the ν parameter described above:

$$\log\left(\frac{y_i}{y_{i-1}}\right) \sim t(\nu, 0, \exp(-2s_i)) \tag{6.4}$$

Thus the full stochastic volatility model is specified by four parameters, each with an associated prior:

σ ∼ Exponential(50) (6.5)

$$\nu \sim \text{Exponential}(0.1)\n$$
(6.6)

$$s_i \sim \mathcal{N}(s_{i-1}, \sigma^{-2}) \tag{6.7}$$

$$\log\left(\frac{y_i}{y_{i-1}}\right) \sim t(\nu, 0, \exp(-2s_i)) \tag{6.8}$$

PyMC3 will now be used to fit this model to a set of historical financial asset pricing data.

# 6.3 PyMC3 Implementation

The first task is to import the necessary libraries used in the stochastic volatility model. This consists of NumPy, SciPy, Pandas, Matplotlib and Seaborn. These libraries are used for data import, manipulation and plotting.

As in previous chapters the PyMC3 library is used to carry out the MCMC procedure. The GaussianRandomWalk model is imported and is used to model the returns of the daily equity prices:

```
# pymc3_bayes_stochastic_vol.py
import datetime
import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import pymc3 as pm
from pymc3.distributions.timeseries import GaussianRandomWalk
import seaborn as sns
```

The next step is to download a suitable equities price series. In this example the historical prices of Amazon will be downloaded from Yahoo Finance.

#### 6.3.1 Obtaining the Price History

The returns of Amazon, Inc. (AMZN) are downloaded from Yahoo Finance using the pandas\_datareader module. However, it is straightforward to utilise S&P500, FTSE100 or any other asset pricing data.

Pandas is used to obtain the raw pricing information and convert it into a returns stream suitable for analysis with the stochastic vol model. This is achieved by taking the ratio of the current days adjusted close to the previous days adjusted close. These percentage returns values are then transformed with the natural logarithm function to produce the log returns.

```
def obtain_plot_amazon_prices_dataframe(start_date, end_date):
    """
    Download, calculate and plot the AMZN logarithmic returns.
    """
    print("Downloading and plotting AMZN log returns...")
    amzn = pdr.get_data_yahoo("AMZN", start_date, end_date)
    amzn["returns"] = amzn["Adj Close"]/amzn["Adj Close"].shift(1)
    amzn.dropna(inplace=True)
    amzn["log_returns"] = np.log(amzn["returns"])
    amzn["log_returns"].plot(linewidth=0.5)
    plt.ylabel("AMZN daily percentage returns")
    plt.show()
    return amzn
```

The returns are plotted in Figure [6.3.](#page-5-0)

![](_page_5_Figure_3.jpeg)

<span id="page-5-0"></span>Figure 6.3: AMZN returns over a ten year period–2006 to 2016.

#### 6.3.2 Model Specification in PyMC3

Now that the returns have been calculated attention will turn towards specifying the Bayesian model via the priors described above. As in previous chapters the model is instantiated via the pm.Model() syntax in a with context. Each prior is then defined as above:

```
def configure_sample_stoch_vol_model(log_returns, samples):
    """
    Configure the stochastic volatility model using PyMC3
    in a 'with' context. Then sample from the model using
    the No-U-Turn-Sampler (NUTS).
    Plot the logarithmic volatility process and then the
    absolute returns overlaid with the estimated vol.
    """
    print("Configuring stochastic volatility with PyMC3...")
    model = pm.Model()
    with model:
        sigma = pm.Exponential('sigma', 50.0, testval=0.1)
        nu = pm.Exponential('nu', 0.1)
        s = GaussianRandomWalk('s', sigma**-2, shape=len(log_returns))
        logrets = pm.StudentT(
            'logrets', nu,
            lam=pm.math.exp(-2.0*s),
            observed=log_returns
        )
    ..
    ..
```

It remains to sample the model with the No-U-Turn Sampler MCMC procedure.

#### 6.3.3 Fitting the Model with NUTS

Now that the model has been specified it is possible to run the NUTS MCMC sampler and generate a traceplot in a similar manner to that carried out in the previous chapter on Bayesian Linear Regression. Thankfully PyMC3 abstracts much of the implementation details of NUTS away from us, allowing us to concentrate on the important procedure of model specification.

For this example 2000 samples are used in the NUTS sampler. Note that this will take some time to calculate. It took 15-20 minutes on my desktop PC to produce the plots below. The API for sampling is very straightforward. Under a with context the model simply utilises the pm.sample method to produce a trace object that can later be used for visualisation of marginal parameter distributions and the sample trace itself:

```
..
..
print("Fitting the stochastic volatility model...")
with model:
    trace = pm.sample(samples)
```

```
pm.traceplot(trace, model.vars[:-1])
plt.show()
..
```

..

![](_page_7_Figure_1.jpeg)

The traceplot for the logarithmic values of σ and ν is given in Figure [6.4.](#page-7-0)

<span id="page-7-0"></span>Figure 6.4: Traceplot of the log ν and log σ posteriors in the stochastic volatility model

Another useful plot is that of the estimated volatility of AMZN against the trading days. To achieve such a plot it is possible to take every kth sample, for each trading day of the volatility distribution and overlay them semi-opaquely.

```
..
..
k = 10
opacity = 0.03
..
..
print("Plotting the absolute returns overlaid with vol...")
plt.plot(np.abs(np.exp(log_returns))-1.0, linewidth=0.5)
plt.plot(np.exp(trace[s][::k].T), 'r', alpha=opacity)
plt.xlabel("Trading Days")
plt.ylabel("Absolute Returns/Volatility")
plt.show()
```

Figure 6.5 displays the plot.

This code is then subsequently wrapped up in a \_\_main\_\_ function call, the full code of which is provided in the following section.

Such a volatility model provides a mechanism for detecting periods of higher vol. This can automatically trigger a risk reduction in a systematic trading strategy, such as reducing leverage or even placing vetos on trading signals.

![](_page_8_Figure_0.jpeg)

Figure 6.5: Overlay of samples from the stochastic volatility model with the actual AMZN returns

This concludes the part of the book on Bayesian Statistics. The material provided here will be used heavily in subsequent chapters on Time Series Analysis and Machine Learning, as many of these models utilise Bayesian techniques within their derivation.

# 6.4 Full Code

```
# pymc3_bayes_stochastic_vol.py
import datetime
import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import pymc3 as pm
from pymc3.distributions.timeseries import GaussianRandomWalk
import seaborn as sns
```

```
"""
    Download, calculate and plot the AMZN logarithmic returns.
    """
    print("Downloading and plotting AMZN log returns...")
    amzn = pdr.get_data_yahoo("AMZN", start_date, end_date)
    amzn["returns"] = amzn["Adj Close"]/amzn["Adj Close"].shift(1)
    amzn.dropna(inplace=True)
    amzn["log_returns"] = np.log(amzn["returns"])
    amzn["log_returns"].plot(linewidth=0.5)
    plt.ylabel("AMZN daily percentage returns")
    plt.show()
    return amzn
def configure_sample_stoch_vol_model(log_returns, samples):
    """
    Configure the stochastic volatility model using PyMC3
    in a 'with' context. Then sample from the model using
    the No-U-Turn-Sampler (NUTS).
    Plot the logarithmic volatility process and then the
    absolute returns overlaid with the estimated vol.
    """
    print("Configuring stochastic volatility with PyMC3...")
    model = pm.Model()
    with model:
        sigma = pm.Exponential('sigma', 50.0, testval=0.1)
        nu = pm.Exponential('nu', 0.1)
        s = GaussianRandomWalk('s', sigma**-2, shape=len(log_returns))
        logrets = pm.StudentT(
            'logrets', nu,
            lam=pm.math.exp(-2.0*s),
            observed=log_returns
        )
    print("Fitting the stochastic volatility model...")
    with model:
        trace = pm.sample(samples)
    pm.traceplot(trace, model.vars[:-1])
    plt.show()
    print("Plotting the log volatility...")
    k = 10
    opacity = 0.03
    plt.plot(trace[s][::k].T, 'b', alpha=opacity)
```

```
plt.xlabel('Time')
    plt.ylabel('Log Volatility')
    plt.show()
    print("Plotting the absolute returns overlaid with vol...")
    plt.plot(np.abs(np.exp(log_returns))-1.0, linewidth=0.5)
    plt.plot(np.exp(trace[s][::k].T), 'r', alpha=opacity)
    plt.xlabel("Trading Days")
    plt.ylabel("Absolute Returns/Volatility")
    plt.show()
if __name__ == "__main__":
    # State the starting and ending dates of the AMZN returns
    start_date = datetime.datetime(2006, 1, 1)
    end_date = datetime.datetime(2015, 12, 31)
    # Obtain and plot the logarithmic returns of Amazon prices
```

amzn\_df = obtain\_plot\_amazon\_prices\_dataframe(start\_date, end\_date)

log\_returns = np.array(amzn\_df["log\_returns"])

# MCMC sampling using NUTS, plotting the trace

samples = 2000

# Configure the stochastic volatility model and carry out

configure\_sample\_stoch\_vol\_model(log\_returns, samples)
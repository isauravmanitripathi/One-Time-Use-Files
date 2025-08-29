# Chapter 5

# Bayesian Linear Regression

At this stage in our journey of Bayesian statistics we inferred a binomial proportion analytically with conjugate priors and have described the basics of Markov Chain Monte Carlo via the Metropolis algorithm. In this chapter we are going to introduce linear regression modelling in the Bayesian framework and carry out inference using the PyMC3 MCMC library.

We will begin by recapping the classical, or frequentist, approach to multiple linear regression (this is discussed at length in the Machine Learning section in later chapters). Then we will discuss how a Bayesian thinks of linear regression. We will briefly describe the concept of a Generalised Linear Model (GLM), as this is necessary to understand the clean syntax of model descriptions in PyMC3.

Subsequent to the description of these models we will simulate some linear data with noise and then use PyMC3 to produce posterior distributions for the parameters of the model. This is the same procedure that we will carry out when discussing time series models such as ARMA and GARCH later on in the book. This "simulate and fit" process not only helps us understand the model, but also checks that we are fitting it correctly when we know the "true" parameter values.

Let us now turn our attention to the frequentist approach to linear regression. More on this approach can be found in the later Machine Learning chapter on Linear Regression.

### 5.1 Frequentist Linear Regression

The frequentist (classical) approach to multiple linear regression assumes a model of the form[51]:

$$f(\mathbf{X}) = \beta_0 + \sum_{j=1}^p \mathbf{X}_j \beta_j + \epsilon = \beta^T \mathbf{X} + \epsilon \tag{5.1}$$

Where, β T is the transpose of the coefficient vector β and ∼ N (0, σ<sup>2</sup> ) is the measurement error, normally distributed with mean zero and standard deviation σ.

That is, our model f(X) is linear in the predictors, X, with some associated measurement error.

If we have a set of training data (x1, y1), . . . ,(x<sup>N</sup> , y<sup>N</sup> ) then the goal is to estimate the β coefficients, which provide the best linear fit to the data. Geometrically, this means we need to find the orientation of the hyperplane that best linearly characterises the data.

"Best" in this case means minimising some form of error function. The most popular method to do this is via ordinary least squares (OLS). If we define the residual sum of squares (RSS), which is the sum of the squared differences between the outputs and the linear regression estimates:

$$RSS(\beta) = \sum_{i=1}^{N} (y_i - f(x_i))^2$$
(5.2)

$$= \sum_{i=1}^{N} (y_i - \beta^T x_i)^2 \tag{5.3}$$

Then the goal of OLS is to minimise the RSS, via adjustment of the β coefficients. Although we won't derive it here (see Hastie et al[51] for details) the Maximum Likelihood Estimate of β, which minimises the RSS, is given by:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \tag{5.4}$$

To make a subsequent prediction yN+1, given some new data xN+1, we simply multiply the components of xN+1 by the associated β coefficients and obtain yN+1.

The important point here is that βˆ is a point estimate, meaning that it is a single value in real-valued p + 1-dimensional space–R <sup>p</sup>+1. In the Bayesian formulation we will see that the interpretation differs substantially.

### 5.2 Bayesian Linear Regression

In a Bayesian framework linear regression is stated in a probabilistic manner. The above linear regression model is reformulated in probabilistic language. The syntax for a linear regression in a Bayesian framework looks like this:

$$\mathbf{y} \sim \mathcal{N}\left(\boldsymbol{\beta}^T \mathbf{X}, \sigma^2 \mathbf{I}\right) \tag{5.5}$$

The response values y are sampled from a multivariate normal distribution that has a mean equal to the product of the β coefficients and the predictors, X, and a variance of σ 2 . Here, I refers to the identity matrix, which is necessary because the distribution is multivariate.

This is different to how the frequentist approach is usually outlined. In the frequentist setting above there is no mention of probability distributions for anything other than the measurement error. In the Bayesian formulation the entire problem is recast such that the y<sup>i</sup> values are samples from a normal distribution.

A common question at this stage is "What is the benefit of doing this?". What do we get out of this reformulation? There are two main reasons for doing so[99]:

• Prior Distributions: If we have any prior knowledge about the parameters β then we can choose prior distributions that reflect this. If we do not then we can still choose non-informative priors.

• Posterior Distributions: I mentioned above that the frequentist MLE value for our regression coefficients, βˆ, was only a single point estimate. In the Bayesian formulation we receive an entire probability distribution that characterises our uncertainty on the different β coefficients. The immediate benefit of this is that after taking into account any data we can quantify our uncertainty in the β parameters via the variance of this posterior distribution. A larger variance indicates more uncertainty.

While the above formula for the Bayesian approach may appear succinct it does not provide much insight into a specification for a model that can be sampled using MCMC. Thus in the next few sections it will be demonstrated how PyMC3 can be used to formulate and utilise a Bayesian linear regression model.

### 5.3 Bayesian Linear Regression with PyMC3

In this section we are going to carry out a time-honoured approach to statistical examples, namely to simulate some data with properties that we know, and then fit a model to recover these original properties. I have used this technique many times in the past on QuantStart.com and it will feature heavily in later chapters on Time Series Analysis.

While it may seem contrived to go through such a procedure, there are in fact two major benefits. The first is that it helps us understand exactly how to fit the model. In order to do so, we have to understand it first. This provides intuition into how the model works. The second reason is that it allows us to see how the model performs in a situation where we actually know the true values trying to be estimated.

Our approach will make use of NumPy and Pandas to simulate the data and Seaborn to plot it. The Generalised Linear Models (GLM) module of PyMC3 will be used to formulate a Bayesian linear regression and sample from it, on the simulated data set.

#### 5.3.1 What are Generalised Linear Models?

Before we begin discussing Bayesian linear regression, I want to briefly outline the concept of a Generalised Linear Model (GLM) as they will be used to formulate our model in PyMC3.

A Generalised Linear Model is a flexible mechanism for extending ordinary linear regression to more general forms of regression, including logistic regression (classification) and Poisson regression (used for count data), as well as linear regression itself.

GLMs allow for response variables that have error distributions other than the normal distribution (see above, in the frequentist section). The linear model is related to the response y via a "link function" and is assumed to be generated via a statistical distribution from the exponential distribution family. This family of probability distributions encompasses many common distributions including the normal, gamma, beta, chi-squared, Bernoulli, Poisson and others.

The mean of this distribution, µ depends on X via the following relation:

$$\mathbb{E}(\mathbf{y}) = \mu = g^{-1}(\mathbf{X}\beta) \tag{5.6}$$

Where g is the link function. The variance is often some function, V , of the mean:

$$Var(\mathbf{y}) = V(\mathbb{E}(\mathbf{y})) = V(g^{-1}(\mathbf{X}\beta))$$
(5.7)

In the frequentist setting, as with ordinary linear regression above, the unknown β coefficients are estimated via a maximum likelihood approach.

I'm not going to discuss GLMs in depth here as they are not the focus of the chapter or the book. We are interested in them because we will be using the glm module from PyMC3, which was written by Thomas Wiecki[102] and others, in order to easily specify our Bayesian linear regression.

#### 5.3.2 Simulating Data and Fitting the Model with PyMC3

Before we utilise PyMC3 to specify and sample a Bayesian model, we need to simulate some noisy linear data. The following snippet carries this out, which is modified and extended from Jonathan Sedar's post[90]:

```
import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="darkgrid", palette="muted")
def simulate_linear_data(N, beta_0, beta_1, eps_sigma_sq):
    """
    Simulate a random dataset using a noisy
    linear process.
    N: Number of data points to simulate
    beta_0: Intercept
    beta_1: Slope of univariate predictor, X
    """
    # Create a pandas DataFrame with column 'x' containing
    # N uniformly sampled values between 0.0 and 1.0
    df = pd.DataFrame(
        {"x":
            np.random.RandomState(42).choice(
                map(
                    lambda x: float(x)/100.0,
                    np.arange(100)
                ), N, replace=False
            )
        }
    )
```

```
# Use a linear model (y ~ beta_0 + beta_1*x + epsilon) to
    # generate a column 'y' of responses based on 'x'
    eps_mean = 0.0
    df["y"] = beta_0 + beta_1*df["x"] + np.random.RandomState(42).normal(
        eps_mean, eps_sigma_sq, N
    )
    return df
if __name__ == "__main__":
    # These are our "true" parameters
    beta_0 = 1.0 # Intercept
    beta_1 = 2.0 # Slope
    # Simulate 100 data points, with a variance of 0.5
    N = 100
    eps_sigma_sq = 0.5
    # Simulate the "linear" data using the above parameters
    df = simulate_linear_data(N, beta_0, beta_1, eps_sigma_sq)
    # Plot the data, and a frequentist linear regression fit
    # using the seaborn package
    sns.lmplot(x="x", y="y", data=df, size=10)
    plt.xlim(0.0, 1.0)
```

The output is given in Figure 5.1:

We've simulated 100 datapoints, with an intercept β<sup>0</sup> = 1 and a slope of β<sup>1</sup> = 2. The epsilon values are normally distributed with a mean of zero and variance σ <sup>2</sup> = 1 2 . The data has been plotted using the sns.lmplot method. In addition, the method uses a frequentist MLE approach to fit a linear regression line to the data.

Now that we have carried out the simulation we want to fit a Bayesian linear regression to the data. This is where the glm module comes in. It uses a model specification syntax that is similar to how the R statistical language specifies models. To achieve this we make implicit use of the Patsy library.

In the following snippet we are going to import PyMC3, utilise the with context manager, as described in the previous chapter on MCMC and then specify the model using the glm module.

We are then going to find the maximum a posteriori (MAP) estimate for the MCMC sampler to begin sampling from. Finally, we are going to use the No-U-Turn Sampler[53] to carry out the actual inference and then plot the trace of the model, discarding the first 500 samples as "burn in":

```
def glm_mcmc_inference(df, iterations=5000):
    """
```

![](_page_5_Figure_0.jpeg)

Figure 5.1: Simulation of noisy linear data via Numpy, pandas and seaborn

Calculates the Markov Chain Monte Carlo trace of a Generalised Linear Model Bayesian linear regression model on supplied data.

```
df: DataFrame containing the data
iterations: Number of iterations to carry out MCMC for
"""
# Use PyMC3 to construct a model context
basic_model = pm.Model()
with basic_model:
    # Create the glm using the Patsy model syntax
    # We use a Normal distribution for the likelihood
    pm.glm.glm("y ~ x", df, family=pm.glm.families.Normal())
    # Use Maximum A Posteriori (MAP) optimisation
    # as initial value for MCMC
    start = pm.find_MAP()
```

```
# Use the No-U-Turn Sampler
        step = pm.NUTS()
        # Calculate the trace
        trace = pm.sample(
            iterations, step, start,
            random_seed=42, progressbar=True
        )
    return trace
...
...
if __name__ == "__main__":
    ...
    ...
    trace = glm_mcmc_inference(df, iterations=5000)
    pm.traceplot(trace[500:])
    plt.show()
```

The output of the script is as follows:

| Applied    | log-transform                            | and<br>to<br>sd | added |   | transformed |    | sd_log | to       | model. |     |     |
|------------|------------------------------------------|-----------------|-------|---|-------------|----|--------|----------|--------|-----|-----|
| [----      | 11%                                      |                 |       | ] | 563         | of | 5000   | complete | in     | 0.5 | sec |
| [--------- | 24%                                      |                 |       | ] | 1207        | of | 5000   | complete | in     | 1.0 | sec |
|            | [--------------<br>37%                   |                 |       | ] | 1875        | of | 5000   | complete | in     | 1.5 | sec |
|            | [-----------------51%                    |                 |       | ] | 2561        | of | 5000   | complete | in     | 2.0 | sec |
|            | [-----------------64%----                |                 |       | ] | 3228        | of | 5000   | complete | in     | 2.5 | sec |
|            | [-----------------78%---------           |                 |       | ] | 3920        | of | 5000   | complete | in     | 3.0 | sec |
|            | [-----------------91%--------------      |                 |       | ] | 4595        | of | 5000   | complete | in     | 3.5 | sec |
|            | [-----------------100%-----------------] |                 |       |   | 5000        | of | 5000   | complete | in     | 3.8 | sec |

The traceplot is given in Figure 5.2:

We covered the basics of traceplots in the previous chapter. Recall that Bayesian models provide a full posterior probability distribution for each of the model parameters, as opposed to a frequentist point estimate.

On the left side of the panel we can see marginal distributions for each parameter of interest. Notice that the intercept β<sup>0</sup> distribution has its mode/maximum posterior estimate almost exactly at 1, close to the true parameter of β<sup>0</sup> = 1. The estimate for the slope β<sup>1</sup> parameter has a mode at approximately 1.98, close to the true parameter value of β<sup>1</sup> = 2. The error parameter associated with the model measurement noise has a mode of approximately 0.465, which is close to the true value of = 0.5.

In all cases there is a reasonable variance associated with each marginal posterior, telling us that there is some degree of uncertainty in each of the values. Were we to simulate more data, and carry out more samples, this variance would likely decrease.

![](_page_7_Figure_0.jpeg)

Figure 5.2: Using PyMC3 to fit a Bayesian GLM linear regression model to simulated data

The key point here is that we do not receive a single point estimate for a regression line, i.e. "a line of best fit", as in the frequentist case. Instead we receive a distribution of likely regression lines.

We can plot these lines using a method of the glm library called plot\_posterior\_predictive. The method takes a trace object and the number of lines to plot (samples).

Firstly we use the seaborn lmplot method, this time with the fit\_reg parameter set to False to stop the frequentist regression line being drawn. Then we plot 100 sampled posterior predictive regression lines. Finally, we plot the "true" regression line using the original β<sup>0</sup> = 1 and β<sup>1</sup> = 2 parameters. The code snippet below produces such a plot:

```
..
..
if __name__ == "__main__":
    ..
    ..
    # Plot a sample of posterior regression lines
    sns.lmplot(x="x", y="y", data=df, size=10, fit_reg=False)
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 4.0)
    pm.glm.plot_posterior_predictive(trace, samples=100)
    x = np.linspace(0, 1, N)
    y = beta_0 + beta_1*x
    plt.plot(x, y, label="True Regression Line", lw=3., c="green")
    plt.legend(loc=0)
```

![](_page_8_Figure_0.jpeg)

![](_page_8_Figure_1.jpeg)

We can see the sampled range of posterior regression lines in Figure [5.3:](#page-8-0)

<span id="page-8-0"></span>Figure 5.3: Using PyMC3 GLM module to show a set of sampled posterior regression lines

The main takeaway here is that there is uncertainty in the location of the regression line as sampled by the Bayesian model. However, it can be seen that the range is relatively narrow and that the set of samples is not too dissimilar to the "true" regression line itself.

### 5.4 Bibliographic Note

An introduction to frequentist linear regression can be found in James et al[59]. A more technical overview, including subset selection methods, can be found in Hastie et al[51]. Gelman et al[47] discuss Bayesian linear models in depth at a reasonably technical level.

This chapter is influenced from previous blog posts by Thomas Wiecki[102] including his discussion of Bayesian GLMs[99, 101] as well as Jonathan Sedar with his posts on Bayesian Inference with PyMC3[90].

## 5.5 Full Code

```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm
import seaborn as sns
sns.set(style="darkgrid", palette="muted")
def simulate_linear_data(N, beta_0, beta_1, eps_sigma_sq):
    """
    Simulate a random dataset using a noisy
    linear process.
    N: Number of data points to simulate
    beta_0: Intercept
    beta_1: Slope of univariate predictor, X
    """
    # Create a pandas DataFrame with column 'x' containing
    # N uniformly sampled values between 0.0 and 1.0
    df = pd.DataFrame(
        {"x":
            np.random.RandomState(42).choice(
                map(
                    lambda x: float(x)/100.0,
                    np.arange(N)
                ), N, replace=False
            )
        }
    )
    # Use a linear model (y ~ beta_0 + beta_1*x + epsilon) to
    # generate a column 'y' of responses based on 'x'
    eps_mean = 0.0
    df["y"] = beta_0 + beta_1*df["x"] + np.random.RandomState(42).normal(
        eps_mean, eps_sigma_sq, N
    )
    return df
```

```
"""
    Calculates the Markov Chain Monte Carlo trace of
    a Generalised Linear Model Bayesian linear regression
    model on supplied data.
    df: DataFrame containing the data
    iterations: Number of iterations to carry out MCMC for
    """
    # Use PyMC3 to construct a model context
    basic_model = pm.Model()
    with basic_model:
        # Create the glm using the Patsy model syntax
        # We use a Normal distribution for the likelihood
        pm.glm.glm("y ~ x", df, family=pm.glm.families.Normal())
        # Use Maximum A Posteriori (MAP) optimisation
        # as initial value for MCMC
        start = pm.find_MAP()
        # Use the No-U-Turn Sampler
        step = pm.NUTS()
        # Calculate the trace
        trace = pm.sample(
            iterations, step, start,
            random_seed=42, progressbar=True
        )
    return trace
if __name__ == "__main__":
    # These are our "true" parameters
    beta_0 = 1.0 # Intercept
    beta_1 = 2.0 # Slope
    # Simulate 100 data points, with a variance of 0.5
    N = 200
    eps_sigma_sq = 0.5
    # Simulate the "linear" data using the above parameters
    df = simulate_linear_data(N, beta_0, beta_1, eps_sigma_sq)
    # Plot the data, and a frequentist linear regression fit
    # using the seaborn package
```

```
sns.lmplot(x="x", y="y", data=df, size=10)
plt.xlim(0.0, 1.0)
trace = glm_mcmc_inference(df, iterations=5000)
pm.traceplot(trace[500:])
plt.show()
# Plot a sample of posterior regression lines
sns.lmplot(x="x", y="y", data=df, size=10, fit_reg=False)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 4.0)
pm.glm.plot_posterior_predictive(trace, samples=100)
x = np.linspace(0, 1, N)
y = beta_0 + beta_1*x
plt.plot(x, y, label="True Regression Line", lw=3., c="green")
plt.legend(loc=0)
plt.show()
```
# Chapter 4

# Markov Chain Monte Carlo

In previous chapters we introduced Bayesian Statistics and considered how to infer a binomial proportion using the concept of conjugate priors. We briefly mentioned that not all models can make use of conjugate priors and thus calculation of the posterior distribution would need to be approximated numerically.

In this chapter we introduce the main family of algorithms, known collectively as Markov Chain Monte Carlo (MCMC), that allow us to approximate the posterior distribution as calculated by Bayes' Theorem. In particular, we consider the Metropolis Algorithm, which is easily stated and relatively straightforward to understand. It serves as a useful starting point when learning about MCMC before delving into more sophisticated algorithms such as Metropolis-Hastings, Gibbs Samplers, Hamiltonian Monte Carlo and the No-U-Turn Sampler (NUTS).

Once we have described how MCMC works, we will carry it out using the open-source Pythonbased PyMC3 library. The library takes care of the underlying implementation details allowing us to concentrate specifically on modelling.

# 4.1 Bayesian Inference Goals

As quants our goal in studying Bayesian Statistics is to ultimately produce quantitative trading strategies, using models derived from Bayesian methods. In order to reach that goal we need to consider a reasonable amount of Bayesian Statistics theory. So far we have:

- Introduced the philosophy of Bayesian Statistics, making use of Bayes' Theorem to update our prior beliefs on probabilities of outcomes based on new data
- Used conjugate priors as a means of simplifying the computation of the posterior distribution in the case of inference on a binomial proportion

In this chapter we are going to discuss MCMC as a means of computing the posterior distribution when conjugate priors are not applicable.

Subsequent to a discussion on the Metropolis algorithm using PyMC3, we will consider more sophisticated samplers and then apply them to more complex models. Ultimately we will arrive at the point where our models are useful enough to provide insight into asset returns prediction. At that stage we will be able to begin building a trading model from our Bayesian analysis.

# 4.2 Why Markov Chain Monte Carlo?

In the previous chapter we saw that conjugate priors gave us a significant mathematical "shortcut" to calculating the posterior distribution in Bayes' Rule. A perfectly legitimate question at this point would be to ask why we need MCMC at all if we can simply use conjugate priors.

The answer lies in the fact that not all models can be succinctly stated in terms of conjugate priors. There are many more complicated modelling situations such as those related to hierarchical models with hundreds of parameters, which are completely intractable using analytical methods.

If we recall Bayes' Rule:

$$P(\theta|D) = \frac{P(D|\theta)P(\theta)}{P(D)}$$
(4.1)

We can see that we need to calculate the evidence P(D). In order to achieve this we need to evaluate the following integral, which integrates over all possible values of the parameter θ:

$$P(D) = \int_{\Theta} P(D,\theta) \mathrm{d}\theta \tag{4.2}$$

The fundamental problem is that we are often unable to evaluate this integral analytically and so must turn to a numerical approximation instead.

An additional problem is that our models might require a large number of parameters. This means that our prior distributions could potentially have a large number of dimensions. Hence our posterior distributions will also be high dimensional. Thus we are in a situation where we have to numerically evaluate an integral in a potentially very large dimensional space.

This means we are in a situation often described as the Curse of Dimensionality. Informally this means that the volume of a high-dimensional space is so vast that any available data residing within it becomes extremely sparse within that space. It leads to problems of sufficient statistical significance. In order to gain any statistical significance the volume of data within the space must grow exponentially with the number of dimensions.

Such problems are often extremely difficult to tackle unless they are approached in an intelligent manner. The motivation behind Markov Chain Monte Carlo methods is that they perform an intelligent search within a high dimensional space and thus Bayesian Models in high dimensions become tractable.

The basic idea is to sample from the posterior distribution by combining a "random search" (the Monte Carlo aspect) with a mechanism for intelligently "jumping" around, but in a manner that ultimately doesn't depend on where we started from (the Markov Chain aspect). Hence Markov Chain Monte Carlo methods are memoryless searches performed with intelligent jumps.

As an aside, MCMC is not just for carrying out Bayesian Statistics. It is also widely used in computational physics and computational biology as it can be applied generally to the approximation of any high dimensional integral.

### 4.2.1 Markov Chain Monte Carlo Algorithms

Markov Chain Monte Carlo is a family of algorithms, rather than one particular method. In this section we are going to concentrate on a particular method known as the Metropolis Algorithm. In later sections we will use more sophisticated samplers, such as the No-U-Turn Sampler (NUTS). The latter is actually incorporated into PyMC3, which is the software we will be using to numerically infer our binomial proportion in this chapter.

# 4.3 The Metropolis Algorithm

The MCMC algorithm considered in this chapter is due to Metropolis[69], which was developed in 1953. Clearly it is not a recent method! While there have been substantial improvements on MCMC sampling algorithms since, the intuition gained on this simpler method will help us understand more complex samplers used throughout the following chapters.

The basic recipes for most MCMC algorithms tend to follow this pattern (see Davidson-Pilon[36] for more details):

- 1. Begin the algorithm at the current position in parameter space (θcurrent)
- 2. Propose a "jump" to a new position in parameter space (θnew)
- 3. Accept or reject the jump probabilistically using the prior information and available data
- 4. If the jump is accepted, move to the new position and return to step 1
- 5. If the jump is rejected, stay where you are and return to step 1
- 6. After a set number of jumps have occurred, return all of the accepted positions

The main difference between MCMC algorithms occurs in how you jump as well as how you decide whether to jump.

The Metropolis algorithm uses a normal distribution to propose a jump. This normal distribution has a mean value µ which is equal to the current parameter position in parameter space and takes a "proposal width" for its standard deviation σ.

This proposal width is a separate parameter of the Metropolis algorithm and has a significant impact on convergence. A larger proposal width will jump further and cover more space in the posterior distribution, but might initially miss a region of higher probability. A smaller proposal width will not cover much of the space as quickly and could take longer to converge.

A normal distribution is a good choice for such a proposal distribution (for continuous parameters) as, by definition, it is more likely to select points nearer to the current position than further away. However, it will occassionally choose points further away, allowing the space to be explored.

Once the jump has been proposed, we need to decide (in a probabilistic manner) whether it is a good move to jump to the new position. How do we do this? We calculate the ratio of the proposal distribution of the new position and the proposal distribution at the current position to determine the probability of moving, p:

$$p = P(\theta_{\text{new}}) / P(\theta_{\text{current}}) \tag{4.3}$$

We then generate a uniform random number on the interval [0, 1]. If this number is contained within the interval [0, p] then we accept the move, otherwise we reject it.

While this is a relatively simple algorithm it isn't immediately clear why this makes sense and how it helps us avoid the intractable problem of calculating a high dimensional integral of the evidence, P(D).

As Thomas Wiecki[102] points out in his article on MCMC sampling, we are actually dividing the posterior of the proposed parameter by the posterior of the current parameter. Utilising Bayes' Rule this eliminates the evidence, P(D) from the ratio:

$$\frac{P(\theta_{\text{new}}|D)}{P(\theta_{\text{current}}|D)} = \frac{\frac{P(D|\theta_{\text{new}})P(\theta_{\text{new}})}{P(D)}}{\frac{P(D|\theta_{\text{current}})P(\theta_{\text{current}})P(\theta_{\text{current}})}{P(D)}} = \frac{P(D|\theta_{\text{new}})P(\theta_{\text{new}})}{P(D|\theta_{\text{current}})P(\theta_{\text{current}})}$$
(4.4)

The right hand side of the latter equality contains only the likelihoods and the priors, both of which we can calculate easily. Hence by dividing the posterior at one position by the posterior at another, we're sampling regions of higher posterior probability more often than not, in a manner which fully reflects the probability of the data.

# 4.4 Introducing PyMC3

PyMC3[10] is a Python library that carries out "Probabilistic Programming". That is, we can define a probabilistic model specification and then carry out Bayesian inference on the model, using various flavours of Markov Chain Monte Carlo. In this sense it is similar to the JAGS and Stan packages. PyMC3 has a long list of contributors and is currently under active development.

PyMC3 has been designed with a clean syntax that allows extremely straightforward model specification, with minimal "boilerplate" code. There are classes for all major probability distributions and it is easy to add more specialist distributions. It has a diverse and powerful suite of MCMC sampling algorithms, including the Metropolis algorithm that we discussed above, as well as the No-U-Turn Sampler (NUTS). This allows us to define complex models with many thousands of parameters. d It also makes use of the Python Theano[94] library, often used for highly GPU-intensive Deep Learning applications, in order to maximise efficiency in execution speed.

In this chapter we will use PyMC3 to carry out a simple example of inferring a binomial proportion. This is sufficient to express the main ideas of MCMC without getting bogged down in implementation specifics. In later chapters we will explore more features of PyMC3 by carrying out inference on more sophisticated models.

# 4.5 Inferring a Binomial Proportion with Markov Chain Monte Carlo

If you recall from the previous chapter on inferring a binomial proportion using conjugate priors our goal was to estimate the fairness of a coin, by carrying out a sequence of coin flips.

The fairness of the coin is given by a parameter θ ∈ [0, 1] where θ = 0.5 means a coin equally likely to come up heads or tails.

We discussed the fact that we could use a relatively flexible probability distribution, the beta distribution, to model our prior belief on the fairness of the coin. We also learnt that by using a Bernoulli likelihood function to simulate virtual coin flips with a particular fairness, that our posterior belief would also have the form of a beta distribution. This is an example of a conjugate prior.

To be clear, this means we do not need to use MCMC to estimate the posterior in this particular case as there is already an analytic closed-form solution. However, the majority of Bayesian inference models do not admit a closed-form solution for the posterior, and hence it is necessary to use MCMC in these cases.

We are going to apply MCMC to a case where we already "know the answer", so that we can compare the results from a closed-form solution and one calculated by numerical approximation.

#### 4.5.1 Inferring a Binonial Proportion with Conjugate Priors Recap

In the previous chapter we took a particular prior belief that the coin was likely to be fair, but that we weren't particularly certain. This translated as giving the beta probability distribution of θ a mean µ = 0.5 and a standard deviation σ = 0.1.

A prior beta distribution has two parameters α and β that characterise the "shape" of our beliefs. A mean of µ = 0.5 and s.d. of σ = 0.1 translate into α = 12 and β = 12. See the previous chapter for details on this transformation.

We then carried out 50 flips and observed 10 heads. When we plugged this into our closedform solution for the posterior beta distribution, we received a posterior with α = 22 and β = 52. Figure [4.1,](#page-4-0) reproduced from the previous chapter, plots the distributions:

![](_page_4_Figure_7.jpeg)

<span id="page-4-0"></span>Figure 4.1: The prior and posterior belief distributions about the fairness θ

We can see that this intuitively makes sense, as the mass of probability has dramatically shifted to nearer 0.2, which is the sample fairness from our flips. Notice also that the peak has become narrower as we're quite confident in our results now, having carried out 50 flips.

### 4.5.2 Inferring a Binomial Proportion with PyMC3

We are now going to carry out the same analysis using the numerical Markov Chain Monte Carlo method instead.

Firstly, we need to install PyMC3:

#### pip install pymc3

Once installed, the next task is to import the necessary libraries, which include Matplotlib, Numpy, Scipy and PyMC3 itself. We also set the graphical style of the Matplotlib output to be similar to the ggplot2 graphing library from the R statistical language:

```
import matplotlib.pyplot as plt
import numpy as np
import pymc3
import scipy.stats as stats
```

```
plt.style.use("ggplot")
```

The next step is to set the prior parameters, as well as the number of coin flip trials carried out and heads returned. We also specify, for completeness, the parameters of the analyticallycalculated posterior beta distribution, which we will use for comparison with our MCMC approach. In addition we specify that we want to carry out 100,000 iterations of the Metropolis algorithm:

```
# Parameter values for prior and analytic posterior
n = 50
z = 10
alpha = 12
beta = 12
alpha_post = 22
beta_post = 52
# How many iterations of the Metropolis
# algorithm to carry out for MCMC
iterations = 100000
```

Now we actually define our beta distribution prior and Bernoulli likelihood model. PyMC3 has a very clean API for carrying this out. It uses a Python with context to assign all of the parameters, step sizes and starting values to a pymc3.Model instance (which I have called basic\_model, as per the PyMC3 tutorial).

Firstly, we specify the theta parameter as a beta distribution, taking the prior alpha and beta values as parameters. Remember that our particular values of α = 12 and β = 12 imply a prior mean µ = 0.5 and a prior s.d. σ = 0.1.

We then define the Bernoulli likelihood function, specifying the fairness parameter p=theta, the number of trials n=n and the observed heads observed=z, all taken from the parameters specified above.

At this stage we can find an optimal starting value for the Metropolis algorithm using the PyMC3 Maximum A Posteriori (MAP) optimisation, the details of which we will omit here. Finally we specify the Metropolis sampler to be used and then actually sample(..) the results. These results are stored in the trace variable:

```
# Use PyMC3 to construct a model context
basic_model = pymc3.Model()
with basic_model:
    # Define our prior belief about the fairness
    # of the coin using a Beta distribution
    theta = pymc3.Beta("theta", alpha=alpha, beta=beta)
    # Define the Bernoulli likelihood function
    y = pymc3.Binomial("y", n=n, p=theta, observed=z)
    # Carry out the MCMC analysis using the Metropolis algorithm
    # Use Maximum A Posteriori (MAP) optimisation as initial value for MCMC
    start = pymc3.find_MAP()
    # Use the Metropolis algorithm (as opposed to NUTS or HMC, etc.)
    step = pymc3.Metropolis()
    # Calculate the trace
    trace = pymc3.sample(
      iterations, step, start, random_seed=1, progressbar=True
    )
```

Notice how the specification of the model via the PyMC3 API is akin to the actual mathematical specification of the model with minimal "boilerplate" code. We will demonstrate the power of this API in later chapters when we come to specify some more complex models.

Now that the model has been specified and sampled, we wish to plot the results. We create a histogram from the trace (the list of all accepted samples) of the MCMC sampling using 50 bins. We then plot the analytic prior and posterior beta distributions using the SciPy stats.beta.pdf(..) method. Finally, we add some labelling to the graph and display it:

```
# Plot the posterior histogram from MCMC analysis
bins=50
plt.hist(
    trace["theta"], bins,
    histtype="step", normed=True,
    label="Posterior (MCMC)", color="red"
)
# Plot the analytic prior and posterior beta distributions
x = np.linspace(0, 1, 100)
plt.plot(
    x, stats.beta.pdf(x, alpha, beta),
    "--", label="Prior", color="blue"
)
```

```
plt.plot(
    x, stats.beta.pdf(x, alpha_post, beta_post),
    label='Posterior (Analytic)', color="green"
)
# Update the graph labels
plt.legend(title="Parameters", loc="best")
plt.xlabel("$\\theta$, Fairness")
plt.ylabel("Density")
plt.show()
```

When the code is executed the following output is given:

Applied logodds-transform to theta **and** added transformed theta\_logodds to model.

| [-----                             | 14%                                      | ] | 14288  | of | 100000 | complete | in | 0.5 | sec |
|------------------------------------|------------------------------------------|---|--------|----|--------|----------|----|-----|-----|
| [----------                        | 28%                                      | ] | 28857  | of | 100000 | complete | in | 1.0 | sec |
| [----------------                  | 43%                                      | ] | 43444  | of | 100000 | complete | in | 1.5 | sec |
| [-----------------58%--            |                                          | ] | 58052  | of | 100000 | complete | in | 2.0 | sec |
| [-----------------72%-------       |                                          | ] | 72651  | of | 100000 | complete | in | 2.5 | sec |
| [-----------------87%------------- |                                          | ] | 87226  | of | 100000 | complete | in | 3.0 | sec |
|                                    | [-----------------100%-----------------] |   | 100000 | of | 100000 | complete | in | 3.4 | sec |

Clearly, the sampling time will depend upon the speed of your computer. The graphical output of the analysis is given in Figure [4.2:](#page-7-0)

![](_page_7_Figure_5.jpeg)

<span id="page-7-0"></span>Figure 4.2: Comparison of the analytic and MCMC-sampled posterior belief distributions of the fairness θ, overlaid with the prior belief

In this particular case of a single-parameter model, with 100,000 samples, the convergence of the Metropolis algorithm is extremely good. The histogram closely follows the analytically calculated posterior distribution, as we would expect. In a relatively simple model such as this we do not need to compute 100,000 samples. Far fewer would be more than sufficient. However, it does emphasise the convergence properties of the Metropolis algorithm.

We can also consider a concept known as the trace, which is the vector of samples produced by the MCMC sampling procedure. We can use the helpful traceplot method to plot both a kernel density estimate (KDE) of the histogram displayed above, as well as the trace itself.

The trace plot is extremely useful for assessing convergence of an MCMC algorithm and whether we need to exclude a period of initial samples (known as the burn in). To output the trace we simply call traceplot with the trace variable:

### # Show the trace plot pymc3.traceplot(trace) plt.show()

The full trace plot is given in Figure [4.3:](#page-8-0)

![](_page_8_Figure_5.jpeg)

<span id="page-8-0"></span>Figure 4.3: Trace plot of the MCMC sampling procedure for the fairness parameter θ

As you can see, the KDE estimate of the posterior belief in the fairness reflects both our prior belief of θ = 0.5 and our data with a sample fairness of θ = 0.2. In addition we can see that the MCMC sampling procedure has "converged to the distribution" since the sampling series looks stationary.

For completeness, here is the full listing:

```
import matplotlib.pyplot as plt
import numpy as np
import pymc3
import scipy.stats as stats
```

```
plt.style.use("ggplot")
```

```
# Parameter values for prior and analytic posterior
n = 50
z = 10
alpha = 12
beta = 12
alpha_post = 22
beta_post = 52
# How many iterations of the Metropolis
# algorithm to carry out for MCMC
iterations = 100000
# Use PyMC3 to construct a model context
basic_model = pymc3.Model()
with basic_model:
    # Define our prior belief about the fairness
    # of the coin using a Beta distribution
    theta = pymc3.Beta("theta", alpha=alpha, beta=beta)
    # Define the Bernoulli likelihood function
    y = pymc3.Binomial("y", n=n, p=theta, observed=z)
    # Carry out the MCMC analysis using the Metropolis algorithm
    # Use Maximum A Posteriori (MAP) optimisation as initial value for MCMC
    start = pymc3.find_MAP()
    # Use the Metropolis algorithm (as opposed to NUTS or HMC, etc.)
    step = pymc3.Metropolis()
    # Calculate the trace
    trace = pymc3.sample(
      iterations, step, start, random_seed=1, progressbar=True
    )
# Plot the posterior histogram from MCMC analysis
bins=50
plt.hist(
    trace["theta"], bins,
    histtype="step", normed=True,
    label="Posterior (MCMC)", color="red"
)
# Plot the analytic prior and posterior beta distributions
x = np.linspace(0, 1, 100)
plt.plot(
```

```
x, stats.beta.pdf(x, alpha, beta),
    "--", label="Prior", color="blue"
)
plt.plot(
    x, stats.beta.pdf(x, alpha_post, beta_post),
    label='Posterior (Analytic)', color="green"
)
# Update the graph labels
plt.legend(title="Parameters", loc="best")
plt.xlabel("$\\theta$, Fairness")
plt.ylabel("Density")
plt.show()
# Show the trace plot
pymc3.traceplot(trace)
plt.show()
```

# 4.6 Bibliographic Note

The algorithm described in this chapter is due to Metropolis[69]. An improvement by Hastings[52] led to the Metropolis-Hastings algorithm. The Gibbs sampler is due to Geman and Geman[48]. Gelfand and Smith[46] wrote a paper that was considered a major starting point for extensive use of MCMC methods in the statistical community.

The Hamiltonian Monte Carlo approach is due to Duane et al[38] and the No-U-Turn Sampler (NUTS) is due to Hoffman and Gelman[53]. Gelman et al[47] has an extensive discussion of computional sampling mechanisms for Bayesian Statistics, including a detailed discussion on MCMC. A gentle, mathematically intuitive, introduction to the Metropolis Algorithm is given by Kruschke[66].

A very popular on-line introduction to Bayesian Statistics is by Cam Davidson-Pilon and others[36], which has a fantastic chapter on MCMC (and PyMC3). Thomas Wiecki has also written a great blog post[102] explaining the rationale for MCMC.

The PyMC3 project[10] also has some extremely useful documentation and some examples.
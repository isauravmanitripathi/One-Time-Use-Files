## Chapter 14

# Hidden Markov Models

A consistent challenge for quantitative traders is the frequent behaviour modification of financial markets, often abruptly, due to changing periods of government policy, regulatory environment and other macroeconomic effects. Such periods are known as market regimes. Detecting such changes is a common, albeit difficult, process undertaken by quantitative market participants.

These various regimes lead to adjustments of asset returns via shifts in their means, variances, autocorrelation and covariances. This impacts the effectiveness of time series methods that rely on stationarity. In particular it can lead to dynamically-varying correlation, excess kurtosis ("fat tails"), heteroskedasticity (volatility clustering) and skewed returns.

There is a clear need to effectively detect these regimes. This aids optimal deployment of quantitative trading strategies and tuning the parameters within them. The modeling task then becomes an attempt to identify when a new regime has occurred adjusting strategy deployment, risk management and position sizing criteria accordingly.

A principal method for carrying out regime detection is to use a statistical time series technique known as a Hidden Markov Model[5]. These models are well-suited to the task since they involve inference on "hidden" generative processes via "noisy" indirect observations correlated to these processes. In this instance the hidden, or latent, process is the underlying regime state, while the asset returns are the indirect noisy observations that are influenced by these states.

### This chapter will discuss the mathematical theory behind Hidden Markov Models (HMM) and how they can be applied to the problem of regime detection for quantitative trading purposes.

The discussion will begin by introducing the concept of a Markov Model[8] and their associated categorisation, which depends upon the level of autonomy in the system as well as how much information about the system is observed. The discussion will then focus specifically on the architecture of HMM as an autonomous process with partially observable information.

As in the previous chapter on State Space Models and the Kalman Filter, the inference concepts of filtering, smoothing and prediction will be outlined. Specific algorithms such as the Forward Algorithm[14] and Viterbi Algorithm[18] exist to solve these inference problems, but their derivations are beyond the scope of this book.

In this chapter the HMM will be applied to the S&P500 returns series to detect regimes. In a later chapter these detection overlays will be added to quantitative trading strategies via a "risk manager". They will be used to assess how algorithmic trading performance varies with and without regime detection.

## 14.1 Markov Models

Prior to the discussion on Hidden Markov Models it is necessary to consider the broader concept of a Markov Model. Such a stochastic state space model involves random transitions between states where the probability of the jump is only dependent upon the current state, rather than any of the previous states. The model is said to possess the Markov Property and is thus "memoryless". Random walk models, which were discussed in a previous chapter are a familiar example of a Markov Model.

Markov Models can be categorised into four broad classes depending upon the autonomy of the system and whether all or part of the information about the system can be observed at each state. The Markov Model page at Wikipedia[8] provides a useful matrix that outlines these differences, which will be repeated here:

|            | Fully Observable           | Partially Observable                            |
|------------|----------------------------|-------------------------------------------------|
| Autonomous | Markov Chain[6]            | Hidden Markov Model[5]                          |
| Controlled | Markov Decision Process[7] | Partially Observable Markov Decision Process[9] |

The simplest model, the Markov Chain, is both autonomous and fully observable. It cannot be modified by actions of an "agent" as in the controlled processes and all information is available from the model at any point in time. Good examples of Markov Chains are the various Markov Chain Monte Carlo (MCMC) algorithm used heavily in computational Bayesian inference, which were discussed in previous chapters.

If the model is still fully autonomous but only partially observable then it is known as a Hidden Markov Model. In such a model there are underlying latent states–and probability transitions between them–but they are not directly observable. Instead these latent states influence the observations. While the latent states possess the Markov Property there is no need for the observations to do so. The most common use of HMM outside of quantitative finance is in the field of speech recognition, where they are extremely successful.

Once the system is allowed to be controlled by an agent the processes come under the heading of Reinforcement Learning. This is often considered to be the "third pillar" of machine learning along with Supervised Learning and Unsupervised Learning. If the system is fully observable, but controlled, then the model is called a Markov Decision Process (MDP). A related technique is known as Q-Learning[15], which is used to optimise the action-selection policy for an agent under a Markov Decision Process model. In 2015 Google DeepMind pioneered the use of Deep Reinforcement Networks, or Deep Q Networks, to create an optimal agent for playing Atari 2600 video games solely from the pixel data within the screen buffer[70].

If the system is both controlled and only partially observable then such Reinforcement Learning models are termed Partially Observable Markov Decision Processes (POMDP). Techniques to solve high-dimensional POMDP are the subject of current academic research. The non-profit team at OpenAI spend significant time looking at such problems. They have released an opensource toolkit to allow straightforward testing of new RL agents known as the OpenAI Gym[28].

Unfortunately RL, along with MDP and POMDP, are not within the scope of this book.

Note that in this book continuous-time Markov processes are not considered. In quantitative trading the time unit is often given via ticks or bars of historical asset data. However, if the objective is to price derivatives contracts then the continuous-time machinery of stochastic calculus would be utilised.

#### 14.1.1 Markov Model Mathematical Specification

This section as well as that on the Hidden Markov Model Mathematical Specification will closely follow the notation and model specification of Murphy (2012)[71].

In quantitative finance the analysis of a time series is often of primary interest. As has been discussed in previous chapters such a time series generally consists of a sequence of T discrete observations X1, . . . , X<sup>T</sup> . An important assumption about Markov Chain models is that at any time t, the observation X<sup>t</sup> captures all of the necessary information required to make predictions about future states. This assumption will be utilised in the following specification.

Formulating the Markov Chain into a probabilistic framework allows the joint density function for the probability of seeing the observations to be written as:

$$p(X_{1:T}) = p(X_1)p(X_2 | X_1)p(X_3 | X_2) \dots \tag{14.1}$$

$$= p(X_1) \prod_{t=2}^{T} p(X_t \mid X_{t-1}) \tag{14.2}$$

This states that the probability of seeing sequences of observations is given by the probability of the initial observation multiplied T − 1 times by the conditional probability of seeing the subsequent observation, given that the previous observation has occurred. It will be assumed in this chapter that the latter term known as the transition function p(X<sup>t</sup> | Xt−1) will itself be timeindependent. In addition since the market regime models considered in this book will consist of small, discrete numbers of regimes the type of model under consideration is a Discrete-State Markov Chain (DSMC).

If there are K separate possible states (regimes) for the model to be in at any time t then the transition function can be written as a transition matrix that describes the probability of transitioning from state j to state i at any time-step t. Mathematically the elements of the transition matrix A are given by:

$$A_{ij} = p(X_t = j \mid X_{t-1} = i) \tag{14.3}$$

As an example it is possible to consider a simple two-state Markov Chain Model. Figure 14.1 represents the numbered states as circles while the arcs represent the probability of jumping from state to state:

Notice that the probabilities sum to unity for each state, i.e. α + (1 − α) = 1. The transition matrix A for this system is a 2 × 2 matrix given by:

![](_page_3_Figure_0.jpeg)

Figure 14.1: Two-state Markov Chain Model

$$A = \left(\begin{array}{cc} 1 - \alpha & \alpha \\ \beta & 1 - \beta \end{array}\right) \tag{14.4}$$

In order to simulate n steps of a general DSMC model it is possible to define the n-step transition matrix A(n) as:

$$A_{ij}(n) := p(X_{t+n} = j \mid X_t = i) \tag{14.5}$$

It can be easily shown that A(m + n) = A(m)A(n) and thus that A(n) = A(1)n. This means that n steps of a DSMC model can be simulated simply by repeated multiplication of the transition matrix with itself.

## 14.2 Hidden Markov Models

Hidden Markov Models are Markov Models where the states are now "hidden" from view, rather than being directly observable. Instead there are a set of output observations, related to the states, which are directly visible. To make this concrete for a quantitative finance example it is possible to think of the states as hidden "regimes" under which a market might be acting while the observations are the asset returns that are directly visible.

In a Markov Model it is only necessary to create a joint density function for the observations. A time-invariant transition matrix was specified allowing full simulation of the model. For Hidden Markov Models it is necessary to create a set of discrete states z<sup>t</sup> ∈ {1, . . . , K} (although for purposes of regime detection it is often only necessary to have K ≤ 3) and to model the observations with an additional probability model, p(x<sup>t</sup> | zt). That is, the conditional probability of seeing a particular observation (asset return) given that the state (market regime) is currently equal to zt.

Depending upon the specified state and observation transition probabilities a Hidden Markov

Model will tend to stay in a particular state and then suddenly jump to a new state, remaining in that state for some time. This is precisely the behaviour desired from such a model when trying to apply it to market regimes. The regimes themselves are not expected to change too quickly. Consider regulatory changes and other slow-moving macroeconomic effects, for instance. However when they do change they are expected to persist for some time.

#### 14.2.1 Hidden Markov Model Mathematical Specification

The corresponding joint density function for the HMM is given by (again using notation from Murphy (2012)[71]):

$$p(\mathbf{z}_{1:T} | \mathbf{x}_{1:T}) = p(\mathbf{z}_{1:T})p(\mathbf{x}_{1:T} | \mathbf{z}_{1:T}) \tag{14.6}$$

$$= \left[ p(z_1) \prod_{t=2}^{T} p(z_t \mid z_{t-1}) \right] \left[ \prod_{t=1}^{T} p(\mathbf{x}_t \mid z_t) \right] \tag{14.7}$$

The first line states that the joint probability of seeing the full set of hidden states and observations is equal to the probability of seeing the hidden states multiplied by the probability of seeing the observations, conditional on the states. This makes sense as the observations cannot affect the states, but the hidden states do indirectly affect the observations.

The second line splits these two distributions into transition functions. The transition function for the states is given by p(z<sup>t</sup> | zt−1) while that for the observations (which depend upon the states) is given by p(x<sup>t</sup> | zt).

As with the Markov Model description above it will be assumed that both the state and observation transition functions are time-invariant. This means that it is possible to utilise the K × K state transition matrix A as before with the Markov Model for that component of the model.

However for the application considered here, namely observations of asset returns, the values are in fact continuous. This means the model choice for the observation transition function is more complex. A common choice is to make use of a conditional multivariate Gaussian distribution with mean µ<sup>k</sup> and covariance σk. This is formalised below:

$$p(\mathbf{x}_t \mid z_t = k, \theta) = \mathcal{N}(\mathbf{x}_t \mid \mu_k, \sigma_k)$$
(14.8)

That is, if the state z<sup>t</sup> is currently equal to k, then the probability of seeing observation xt, given the parameters of the model θ, is distributed as a multivariate Gaussian.

In order to make this a little clearer Figure 14.2 shows the evolution of the states z<sup>t</sup> and how they lead indirectly to the evolution of the observations, xt:

#### 14.2.2 Filtering of Hidden Markov Models

With the joint density function specified it remains to consider the how the model will be utilised. In general state-space modelling there are often three main tasks of interest: Filtering, smoothing and prediction. The previous chapter on State-Space Models and the Kalman Filter described these briefly. They will be repeated here for completeness:

![](_page_5_Figure_0.jpeg)

Figure 14.2: Hidden Markov Model: States and Observations

- Prediction Forecasting subsequent values of the state
- Filtering Estimating the current values of the state from past and current observations
- Smoothing Estimating the past values of the state given the observations

Filtering and smoothing are similar but not identical. Smoothing is concerned with wanting to understand what has happened to states in the past given current knowledge, whereas filtering is concerned with what is happening with the state right now.

It is beyond the scope of this book to describe in detail the algorithms developed for filtering, smoothing and prediction. The main goal of this chapter is to apply Hidden Markov Models to Regime Detection. Hence the task at hand reduces to determining which "market regime state" the world is currently in, utilising the asset returns available to date. This is a filtering problem.

Mathematically, the conditional probability of the state at time t given the sequence of observations up to time t is the object of interest. This involves determining p(z<sup>t</sup> | x1:<sup>T</sup> ). As with the Kalman Filter it is possible to recursively apply Bayes' Rule in order to achieve filtering on a Hidden Markov Model.

## 14.3 Regime Detection with Hidden Markov Models

In this section Hidden Markov Models will be implemented using the R statistical language via the Dependent Mixture Models depmixS4 package. HMM will be used to analyse when US equities markets are currently experiencing various regime states. In a later chapter these regime overlays will be used in a subclassed RiskManager module of QSTrader to adjust trade signal suggestions in a systematic trend-following strategy.

Within the chapter a simulation of streamed market returns across two separate regimes– "bullish" and "bearish"–will be carried out. A Hidden Markov Model will be fitted to the returns stream to identify the posterior probability of being in a particular regime state.

Subsequent to outlining the procedure on simulated data the Hidden Markov Model will be applied to US equities data in order to determine two- and three-state underlying regimes.

Acknowledgements: This chapter and code is heavily influenced by the article over at Systematic Investor on Regime Detection[58]. Please take a look at the article and references therein for additional discussion.

#### 14.3.1 Market Regimes

Applying Hidden Markov Models to regime detection is tricky since the problem is actually a form of unsupervised learning. That is, there is no "ground truth" or labelled data on which to "train" the model. It is also unclear how many regime states exist a priori. Are there two, three, four or more "true" hidden market regimes?

Answers to these questions depend heavily on the asset class being modelled, the choice of time frame and the nature of data utilised. For instance, daily returns data in equities markets often exhibits periods of lower volatility, even over a number of years, with exceptional periods of high volatility in moments of "panic" or "correction". Is it natural then to consider modelling equity indices with two states? Might there be a third intermediate state representing more vol than usual but not outright panic?

Utilising Hidden Markov Models as overlays to a risk manager that can interfere with strategygenerated orders requires careful research analysis and a solid understanding of the asset class(es) being modelled. In a later chapter the performance of a systematic trading strategy will be studied under a Hidden Markov Model-based risk manager.

#### 14.3.2 Simulated Data

In this section simulated returns data will be generated from two separate Gaussian distributions, each of which represents a "bullish" or "bearish" market regime. The bullish returns draw from a Gaussian distribution with positive mean and low variance, while the bearish returns draw from a Gaussian distribution with slight negative mean but higher variance.

Five separate market regime periods will be simulated and "stitched" together in R. The subsequent stream of returns will then be utilised by a Hidden Markov Model in order to infer posterior probabilities of the regime states, given the sequence of observations.

The first task is to install the depmixS4 and quantmod libraries and then import them into R. The random seed will also be fixed in order to allow consistent replication of results:

```
> install.packages('depmixS4')
```

- > install.packages('quantmod')
- > library('depmixS4')
- > library('quantmod')

```
> set.seed(1)
```

At this stage a two-regime market will be simulated. This is achieved by assuming market returns are normally distributed. Separate regimes will be simulated with each containing N<sup>k</sup> days of returns. Each of the k regimes will be bullish or bearish. The goal of the Hidden Markov Model will be to identify when the regime has switched from bullish to bearish and vice versa.

In this example k = 5 and each N<sup>k</sup> is drawn from the interval [50, 150] uniformly. The bull market is distributed as N (0.1, 0.1) while the bear market is distributed as N (−0.05, 0.2). The parameters are set via the following code:

```
> # Create the parameters for the bull and
> # bear market returns distributions
> Nk_lower <- 50
> Nk_upper <- 150
> bull_mean <- 0.1
```

- > bull\_var <- 0.1
- > bear\_mean <- -0.05
- > bear\_var <- 0.2

The N<sup>k</sup> values are randomly chosen:

```
> # Create the list of durations (in days) for each regime
> days <- replicate(5, sample(Nk_lower:Nk_upper, 1))
```

The returns for each kth period are randomly drawn:

```
> # Create the various bull and bear markets returns
> market_bull_1 <- rnorm( days[1], bull_mean, bull_var )
> market_bear_2 <- rnorm( days[2], bear_mean, bear_var )
> market_bull_3 <- rnorm( days[3], bull_mean, bull_var )
> market_bear_4 <- rnorm( days[4], bear_mean, bear_var )
> market_bull_5 <- rnorm( days[5], bull_mean, bull_var )
```

The R code for creating the true regime states (either 1 for bullish or 2 for bearish) and final list of returns is given by the following:

```
> # Create the list of true regime states and full returns list
> true_regimes <- c( rep(1,days[1]), rep(2,days[2]), rep(1,days[3]),
    rep(2,days[4]), rep(1,days[5]))
> returns <- c( market_bull_1, market_bear_2, market_bull_3,
```

```
market_bear_4, market_bull_5)
```

Plotting the returns shows the clear changes in mean and variance between the regime switches. See Figure 14.3.

```
> plot(returns, type="l", xlab='', ylab="Returns")
```

At this stage the Hidden Markov Model can be specified and fit using the Expectation Maximisation algorithm[2], the details of which are beyond the scope of this book. The family of distributions is specified as gaussian and the number of states is set to two (nstates = 2):

```
> # Create and fit the Hidden Markov Model
> hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 2,
    data=data.frame(returns=returns))
> hmmfit <- fit(hmm, verbose = FALSE)
```

Subsequent to model fitting it is possible to plot the posterior probabilities of being in a particular regime state. post\_probs contain the posterior probabilities. These are compared with the underlying true states. Notice that the Hidden Markov Model does a good job of correctly identifying regimes, albeit with some lag. See Figure 14.4.

```
> # Output both the true regimes and the
> # posterior probabilities of the regimes
> post_probs <- posterior(hmmfit)
> layout(1:2)
> plot(post_probs$state, type='s', main='True Regimes',
    xlab='', ylab='Regime')
```

![](_page_8_Figure_0.jpeg)

Figure 14.3: Simulated market returns from two Gaussian distributions

```
> matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
```

```
> legend(x='topright', c('Bull','Bear'), fill=1:2, bty='n')
```

Figure 14.4: Comparison of true regime states with Hidden Markov Model posterior probabilities The discussion will now turn towards applying the Hidden Markov Model to real world

historical financial data.

#### 14.3.3 Financial Data

In the above section it was straightforward for the Hidden Markov Model to determine regimes because they had been simulated from a pre-specified set of Gaussians. The problem of regime detection is actually an unsupervised learning challenge since the number of states is not known a priori, nor is there any "ground truth" on which to train the HMM.

In this section two separate modelling tasks will be carried out. The first will involve fitting the HMM with two regime states to S&P500 returns, while the second will utilise three states. The results between the two models will be compared.

The process for applying the Hidden Markov Model provided by depmixS4 is similar to that carried out for the simulated data. Instead of generating the returns stream from two Gaussian distributions it will simply be downloaded using the quantmod library:

```
> # Obtain S&P500 data from 2004 onwards and
> # create the returns stream from this
> getSymbols( "^GSPC", from="2004-01-01" )
> gspcRets = diff( log( Cl( GSPC ) ) )
> returns = as.numeric(gspcRets)
```

The gspcRets time series object can be plotted, showing the volatile periods around 2008 and 2011. See Figure [14.5.](#page-9-0)

#### > plot(gspcRets)

<span id="page-9-0"></span>Figure 14.5: Returns of the S&P500 over the period from 2004 onwards

As before a two-state Hidden Markov Model is fitted using the EM algorithm. The returns and posterior probabilities of each regime are plotted. See Figure 14.6.

```
> # Fit a Hidden Markov Model with two states
> # to the S&P500 returns stream
> hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 2,
    data=data.frame(returns=returns))
> hmmfit <- fit(hmm, verbose = FALSE)
> post_probs <- posterior(hmmfit)
>
> # Plot the returns stream and the posterior
> # probabilities of the separate regimes
> layout(1:2)
> plot(returns, type='l', main='Regime Detection', xlab='', ylab='Returns')
> matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
> legend(x='bottomleft', c('Regime #1','Regime #2'), fill=1:2, bty='n')
```

![](_page_10_Figure_1.jpeg)

Figure 14.6: Two-state Hidden Markov Model applied to S&P500 returns data

Notice that within 2004 and 2007 the markets were calmer and hence the Hidden Markov Model has given high posterior probability to Regime #2 for this period. However between 2007- 2009 the markets were incredibly volatile due to the financial crisis. This has the initial effect of rapidly changing the posterior probabilities between the two states but being fairly consistently in Regime #1 during 2008 itself.

The markets became calmer in 2010 but additional volatility occurred in 2011, leading once again for the HMM to give high posterior probability to Regime #1. Subsequent to 2011 the markets became calmer once again and the HMM is consistently giving high probability to Regime #2. In 2015 the markets once again became choppier and this is reflected in the increased switching between regimes for the HMM.

The same process will now be carried out for a three-state HMM. There is little to modify between the two, with the exception of modifying nstates = 3 and adjusting the plotting legend. See Figure [14.7.](#page-11-0)

```
> # Fit a Hidden Markov Model with three states
> # to the S&P500 returns stream
> hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 3,
    data=data.frame(returns=returns))
> hmmfit <- fit(hmm, verbose = FALSE)
> post_probs <- posterior(hmmfit)
>
> # Plot the returns stream and the posterior
> # probabilities of the separate regimes
> layout(1:2)
> plot(returns, type='l', main='Regime Detection',
    xlab='', ylab='Returns')
> matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
> legend(x='bottomleft', c('Regime #1','Regime #2', 'Regime #3'),
    fill=1:3, bty='n')
```

![](_page_11_Figure_2.jpeg)

<span id="page-11-0"></span>Figure 14.7: Three-state Hidden Markov Model applied to S&P500 returns data

The length of data makes the posterior probabilities chart somewhat trickier to interpret. Since the model is forced to consider three separate regimes it leads to a switching behaviour between Regime #2 and Regime #3 in the calmer period of 2004-2007. However in the volatile periods of 2008, 2010 and 2011, Regime #1 dominates the posterior probability indicating a highly volatile state. Subsequent to 2011 the model reverts to switching between Regime #2 and Regime #3.

It is clear that choosing the initial number of states to apply to a real returns stream is a challenging problem. It will depend upon the asset class being utilised, how the trading for that asset is carried out as well as the time period chosen.

## 14.4 Next Steps

In a later chapter the Hidden Markov Model will be used by a RiskManager subclass in QSTrader. It will determine when to veto and close signals generated by a Strategy class in an attempt to improve profitability over the case of no risk management.

## 14.5 Bibliographic Note

An overview of Markov Models (as well as their various categorisations), including Hidden Markov Models (and algorithms to solve them), can be found in the introductory articles on Wikipedia[8], [5], [7], [9], [6], [14], [18].

A highly detailed textbook mathematical overview of Hidden Markov Models, with applications to speech recognition problems and the Google PageRank algorithm, can be found in Murphy (2012)[71]. Bishop (2007)[22] covers similar ground to Murphy (2012), including the derivation of the Maximum Likelihood Estimate (MLE) for the HMM as well as the Forward-Backward and Viterbi Algorithms. The discussion concludes with Linear Dynamical Systems and Particle Filters.

Regime detection has a long history in the quant blogosphere. Quantivity (2009, 2012)[83, 82, 84] replicates the research of Kritzman et al (2012)[65] using R to determine US equity "regimes" via macroeconomic indicators. Slaff (2015)[93] applies the depmixS4 HMM library in R to EUR/USD forex data to detect volatility regimes.

Systematic Investor (2012, 2015)[56, 57] initially uses simulated data and the RHmm package in R to determine regime states, but then applies these methods to SPY using a rolling window approach. A later post[58] reintroduces the methods using the depmixS4 package.

Gekkoquant (2014, 2015)[44, 43, 42, 45] provides a four-part series on applying HMM for regime detection, using the RHmm package. The first two posts concentrate solely on the mathematics of the model along with the derivation of the Viterbi algorithm. The third post considers two approaches to using HMM: One HMM with each state representing a regime and another with multiple HMM, one per regime. The final post applies this to a trend-following strategy, ultimately leading to a Sharpe Ratio of 0.857.

Wiecki (2013)[100] presents a Guassian HMM in the Quantopian framework, although this is not directly applied to a trading strategy.

## 14.6 Full Code

# Import the necessary packages and set # random seed for replication consistency install.packages('depmixS4')

```
install.packages('quantmod')
library('depmixS4')
library('quantmod')
set.seed(1)
# Create the parameters for the bull and
# bear market returns distributions
Nk_lower <- 50
Nk_upper <- 150
bull_mean <- 0.1
bull_var <- 0.1
bear_mean <- -0.05
bear_var <- 0.2
# Create the list of durations (in days) for each regime
days <- replicate(5, sample(Nk_lower:Nk_upper, 1))
# Create the various bull and bear markets returns
market_bull_1 <- rnorm( days[1], bull_mean, bull_var )
market_bear_2 <- rnorm( days[2], bear_mean, bear_var )
market_bull_3 <- rnorm( days[3], bull_mean, bull_var )
market_bear_4 <- rnorm( days[4], bear_mean, bear_var )
market_bull_5 <- rnorm( days[5], bull_mean, bull_var )
# Create the list of true regime states and full returns list
true_regimes <- c( rep(1,days[1]), rep(2,days[2]), rep(1,days[3]),
    rep(2,days[4]), rep(1,days[5]))
returns <- c( market_bull_1, market_bear_2, market_bull_3,
    market_bear_4, market_bull_5)
# Create and fit the Hidden Markov Model
hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 2,
    data=data.frame(returns=returns))
hmmfit <- fit(hmm, verbose = FALSE)
post_probs <- posterior(hmmfit)
# Output both the true regimes and the
# posterior probabilities of the regimes
layout(1:2)
plot(post_probs$state, type='s', main='True Regimes',
    xlab='', ylab='Regime')
matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
legend(x='topright', c('Bull','Bear'), fill=1:2, bty='n')
```

```
# Obtain S&P500 data from 2004 onwards and
# create the returns stream from this
getSymbols( "^GSPC", from="2004-01-01" )
gspcRets = diff( log( Cl( GSPC ) ) )
returns = as.numeric(gspcRets)
# Fit a Hidden Markov Model with two states
# to the S&P500 returns stream
hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 2,
    data=data.frame(returns=returns))
hmmfit <- fit(hmm, verbose = FALSE)
post_probs <- posterior(hmmfit)
# Plot the returns stream and the posterior
# probabilities of the separate regimes
layout(1:2)
plot(returns, type='l', main='Regime Detection',
    xlab='', ylab='Returns')
matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
legend(x='topright', c('Regime #1','Regime #2'),
    fill=1:2, bty='n')
# Fit a Hidden Markov Model with three states
# to the S&P500 returns stream
hmm <- depmix(returns ~ 1, family = gaussian(), nstates = 3,
    data=data.frame(returns=returns))
hmmfit <- fit(hmm, verbose = FALSE)
post_probs <- posterior(hmmfit)
# Plot the returns stream and the posterior
# probabilities of the separate regimes
layout(1:2)
plot(returns, type='l', main='Regime Detection',
    xlab='', ylab='Returns')
matplot(post_probs[,-1], type='l',
    main='Regime Posterior Probabilities',
    ylab='Probability')
legend(x='bottomleft', c('Regime #1','Regime #2',
    'Regime #3'), fill=1:3, bty='n')
```

## Part IV

# Statistical Machine Learning
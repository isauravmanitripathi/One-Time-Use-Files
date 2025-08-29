# Chapter 13

# State Space Models and the Kalman Filter

Thus far in our analysis of time series we have considered linear time series models including ARMA, ARIMA as well as the GARCH model for conditional heteroskedasticity. In this chapter we are going to consider a more general class of models known as state space models. The primary benefit of these models is that unlike the ARIMA family their parameters can adapt over time.

State space models are very general and it is possible to put the models we have considered to date into a state space formulation. However in order to keep the analysis straightforward it is often better to use the simpler representation previously described.

The general premise of a state space model is that we have a set of states that evolve in time (such as the hedge ratio between two cointegrated pairs of equities) but our observations of these states contain statistical noise (such as market microstructure noise), and hence we are unable to ever directly observe the "true" states.

The goal of the state space model is to infer information about the states, given the observations, as new information arrives. A famous algorithm for carrying out this procedure is the Kalman Filter, which we will discuss at length in this chapter.

The Kalman Filter is ubiquitous in engineering control problems such as guidance & navigation, spacecraft trajectory analysis and manufacturing. However it is also widely used in quantitative finance.

In engineering, for instance, a Kalman Filter will be used to estimate values of the state, which are then used to control the system under study. This introduces a feedback loop–often in real-time.

Perhaps the most common usage of a Kalman Filter in quantitative trading is to update hedging ratios between assets in a statistical arbitrage pairs trade. We will consider such an example in this, and subsequent, chapters.

Generally there are three types of inference that are of interest when considering state space models:

- Prediction Forecasting subsequent values of the state
- Filtering Estimating the current values of the state from past and current observations

• Smoothing - Estimating the past values of the state given the observations

Filtering and smoothing are similar, but not the same. Perhaps the best way to think of the difference is that with smoothing we are really wanting to understand what has happened to states in the past given our current knowledge, whereas with filtering we really want to know what is happening with the state right now.

In this chapter we are going to discuss the theory of the state space model and how we can use the Kalman Filter to carry out the various types of inference described above. We will then apply it to trading situations such as cointegrated pairs later in the book.

A Bayesian approach will be utilised for the problem. This is the statistical framework that allows updates of beliefs in light of new information, which is precisely the desired behaviour sought from the Kalman Filter.

I would like to warn you that state-space models and Kalman Filters suffer from an abundance of mathematical notation, even if the conceptual ideas behind them are relatively straightforward. I will try and explain all of this notation in depth, as it can be confusing for those new to engineering control problems or state-space models in general. Fortunately we will be letting Python do the heavy lifting of solving the model for us, so the verbose notation will not be a problem in practice.

# 13.1 Linear State-Space Model

Let us begin by discussing all of the elements of the linear state-space model.

Since the states of the system are time-dependent we need to subscript them with t. We will use θ<sup>t</sup> to represent a column vector of the states.

In a linear state-space model we say that these states are a linear combination of the prior state at time t − 1 as well as system noise (random variation). In order to simplify the analysis we are going to suggest that this noise is drawn from a multivariate normal distribution. Other distributions can be used for alternative models but they will not be considered here.

The linear dependence of θ<sup>t</sup> on the previous state θt−<sup>1</sup> is given by the matrix Gt, which can also be time-varying (hence the subscript t). The multivariate time-dependent noise is given by wt. The relationship is summarised below in what is often called the state equation:

$$\theta_t = G_t \theta_{t-1} + w_t \tag{13.1}$$

This equation is only half of the story. We also need to discuss the observations–what we actually see–since the states are hidden to us.

We can denote the time-dependent observations by yt. The observations are a linear combination of the current state and some additional random variation known as measurement noise, which is also drawn from a multivariate normal distribution.

If we denote the linear dependence matrix of θ<sup>t</sup> on y<sup>t</sup> by F<sup>t</sup> (also time-dependent) and the measurement noise by v<sup>t</sup> we have the observation equation:

$$y_t = F_t^T \theta_t + v_t \tag{13.2}$$

Where F T is the transpose of F.

In order to fully specify the model we need to provide the first state θ0, as well as the variancecovariance matrices for the system noise and measurement noise. These terms are distributed as:

$$\theta_0 \sim \mathcal{N}(m_0, C_0) \tag{13.3}$$

$$v_t \sim \mathcal{N}(0, V_t) \tag{13.4}$$

$$w_t \sim \mathcal{N}(0, W_t) \tag{13.5}$$

Clearly that is a lot of notation to specify the model. For completeness I will summarise all of the terms here to help you get to grips with it:

- θ<sup>t</sup> The state of the model at time t
- y<sup>t</sup> The observation of the model at time t
- G<sup>t</sup> The state-transition matrix between current and prior states at time t and t − 1 respectively
- F<sup>t</sup> The observation matrix between the current observation and current state at time t
- w<sup>t</sup> The system noise drawn from a multivariate normal distribution
- v<sup>t</sup> The measurement noise drawn from a multivariate normal distribution
- m<sup>0</sup> The mean value of the multivariate normal distribution of the initial state, θ<sup>0</sup>
- C<sup>0</sup> The variance-covariance matrix of the multivariate normal distribution of the initial state, θ<sup>0</sup>
- W<sup>t</sup> The variance-covariance matrix for the multivariate normal distribution from which the system noise is drawn
- V<sup>t</sup> The variance-covariance matrix for the multivariate normal distribution from from which the measurement noise is drawn

Now that we have specified the linear state-space model we need an algorithm to actually solve it. This is where the Kalman Filter comes in. We can use Bayes' Rule and conjugate priors, as discussed in the previous part of the book, to help us derive the algorithm.

# 13.2 The Kalman Filter

This section follows very closely the notation and analysis carried out in Pole et al[81]. I decided it was not particularly helpful to invent my own notation for the Kalman Filter as I want you to be able to relate it to other research papers or texts.

#### 13.2.1 A Bayesian Approach

Recall from the prior chapters on Bayesian inference that Bayes' Rule is given by:

$$P(\theta|D) = P(D|\theta)P(\theta)/P(D) \tag{13.6}$$

Where θ refers to our parameters and D refers to our data or observations.

We want to apply the rule to the idea of updating the probability of seeing a state given all of the previous data we have and our current observation. Unfortunately we need to introduce more notation!

If we are at time t then we can represent all of the data known about the system by the quantity Dt. Oour current observations are denoted by yt. Thus we can say that D<sup>t</sup> = (Dt−1, yt). Our current knowledge is a mixture of our previous knowledge plus our most recent observation.

Applying Bayes' Rule to this situation gives the following:

$$P(\theta_t | D_{t-1}, y_t) = \frac{P(y_t | \theta_t) P(\theta_t | D_{t-1})}{P(y_t)}$$
(13.7)

What does this mean? It says that the posterior or updated probability of obtaining a state θt, given our current observation y<sup>t</sup> and previous data Dt−1, is equal to the likelihood of seeing an observation yt, given the current state θ<sup>t</sup> multiplied by the prior or previous belief of the current state, given only the previous data Dt−1, normalised by the probability of seeing the observation y<sup>t</sup> regardless.

While the notation may be somewhat verbose, it is a very natural statement. It says that we can update our view on the state, θt, in a rational manner given the fact that we have new information in the form of the current observation, yt.

One of the extremely useful aspects of Bayesian inference is that if our prior and likelihood are both normally distributed we can use the concept of conjugate priors to state that our posterior of θ<sup>t</sup> will also be normally distributed.

We utilised the same concept, albeit with different distributional forms in our previous discussion on the inference of binomial proportions.

So how does this help us produce a Kalman Filter?

Let us specify the terms that we will be using from Bayes' Rule above. Firstly we specify the distributional form of the prior:

$$\theta_t | D_{t-1} \sim \mathcal{N}(a_t, R_t) \tag{13.8}$$

This says that the prior view of θ at time t, given our knowledge at time t − 1 is distributed as a multivariate normal distribution with mean a<sup>t</sup> and variance-covariance Rt. The latter two parameters will be defined below.

Now let us consider the likelihood:

$$y_t | \theta_t \sim \mathcal{N}(F_t^T \theta_t, V_t) \tag{13.9}$$

This says that the likelihood function of the current observation y<sup>t</sup> is distributed as a multivariate normal distribution with mean F T t θ<sup>t</sup> and variance-covariance Vt. We have already outlined these terms in the list above.

Finally we have the posterior of θt:

$$\theta_t | D_t \sim \mathcal{N}(m_t, C_t) \tag{13.10}$$

This says that the posterior view of the current state θt, given our current knowledge at time t is distributed as a multivariate normal distribution with mean m<sup>t</sup> and variance-covariance Ct.

The Kalman Filter is what links all of these terms together for t = 1, . . . , n. We we will not derive where these values actually come from. Instead they will simply be states. Thankfully we can use library implementations in Python to carry out the "heavy lifting" calculations for us:

$$a_t = G_t m_{t-1} \tag{13.11}$$

$$R_t = G_t C_{t-1} G_t^T + W_t \tag{13.12}$$

$$e_t = y_t - f_t \tag{13.13}$$

$$m_t = a_t + A_t e_t \tag{13.14}$$

$$f_t = F_t^T a_t \tag{13.15}$$

$$Q_t = F_t^T R_t F_t + V_t \t\t(13.16)$$

$$A_t = R_t F_t Q_t^{-1} \tag{13.17}$$

$$C_t = R_t - A_t Q_t A_t^T \tag{13.18}$$

Clearly that is a lot of notation. As I said above we need not worry about the excessive verboseness of the Kalman Filter since we can simply use libraries in Python to calculate the algorithm for us.

How does it all fit together? Well, f<sup>t</sup> is the predicated value of the observation at time t, where we make this prediction at time t − 1. Since e<sup>t</sup> = y<sup>t</sup> − ft, we can see easily that e<sup>t</sup> is the error associated with the forecast–the difference between f and y.

Importantly the posterior mean is a weighting of the prior mean and the forecast error, since m<sup>t</sup> = a<sup>t</sup> + Ate<sup>t</sup> = Gtmt−<sup>1</sup> + Atet, where G<sup>t</sup> and A<sup>t</sup> are our weighting matrices.

Now that we have an algorithmic procedure for updating our views on the observations and states we can use it to make predictions as well as smooth the data.

#### 13.2.2 Prediction

The Bayesian approach to the Kalman Filter leads naturally to a mechanism for prediction. Since we have our posterior estimate for the state θ<sup>t</sup> we can predict the next day's values by considering the mean value of the observation.

Let us take the expected value of the observation tomorrow given our knowledge of the data today:

$$E[y_{t+1}|D_t] = E[F_{t+1}^T \theta_t + v_{t+1}|D_t] \qquad (13.19)$$

$$= F_{t+1}^T E[\theta_{t+1}|D_t] \tag{13.20}$$

$$= F_{t+1}^T a_{t+1} \tag{13.21}$$

$$= f_{t+1} \tag{13.22}$$

Where does this come from? Let us try and follow through the analysis.

Since the likelihood function for today's observation yt, given today's state θt, is normally distributed with mean F T t θ<sup>t</sup> and variance-covariance V<sup>t</sup> (see above), we have that the expectation of tomorrow's observation yt+1, given our data today, Dt, is precisely the expectation of the multivariate normal for the likelihood, namely E[F T <sup>t</sup>+1θt+vt+1|Dt]. Once we make this connection it simply reduces to applying rules about the expectation operator to the remaining matrices and vectors, ultimately leading us to ft+1.

However it is not sufficient to simply calculate the mean, we must also know the variance of tomorrow's observation given today's data, otherwise we cannot truly characterise the distribution on which to draw tomorrow's prediction.

$$\text{Var}[y_{t+1}|D_t] = \text{Var}[F_{t+1}^T \theta_t + v_{t+1}|D_t] \tag{13.23}$$

$$= F_{t+1}^T \operatorname{Var}[\theta_{t+1}|D_t]F_{t+1} + V_{t+1}$$
(13.24)

$$= F_{t+1}^T R_{t+1} F_{t+1} + V_{t+1} \tag{13.25}$$

$$= Q_{t+1} \tag{13.26}$$

Now that we have the expectation and variance of tomorrow's observation, given today's data, we are able to provide the general forecast for k steps ahead, by fully characterising the distribution on which these predictions are drawn:

$$y_{t+k}|D_t \sim \mathcal{N}(f_{t+k|t}, Q_{t+k|t}) \tag{13.27}$$

Note that I have used some odd notation here. What does it mean to have a subscript of t + k|t? It allows us to write a convenient shorthand for the following:

$$f_{t+k|t} = F_{t+k}^T G^{k-1} a_{t+1} \tag{13.28}$$

$$Q_{t+k|t} = F_{t+k}^T R_{t+k} F_{t+k} + V_{t+k} \t\t(13.29)$$

$$R_{t+k|t} = G^{k-1}R_{t+1}(G^{k-1})^T + \sum_{j=2}^k G^{k-j}W_{t+j}(G^{k-j})^T$$
(13.30)

As I have mentioned repeatedly in this chapter we should not concern ourselves too much with the verboseness of the Kalman Filter and its notation. Instead we should think about the overall procedure and its Bayesian underpinnings.

We now have the means of predicting new values of the series. This is an alternative to the predictions produced by combining ARIMA and GARCH.

# 13.3 Dynamic Hedge Ratio Between ETF Pairs Using the Kalman Filter

A common quant trading technique involves taking two assets that form a cointegrating relationship and utilising a mean-reverting approach to construct a trading strategy. This can be carried out by performing a linear regression between the two assets (such as a pair of ETFs) and using this to determine how much of each asset to long and short at particular thresholds.

One of the major concerns with such a strategy is that any parameters introduced via this structural relationship such as the hedging ratio between the two assets are likely to be timevarying. They will not be fixed throughout the period of the strategy. In order to improve profitability it would be useful if we could determine a mechanism for adjusting the hedging ratio over time.

One approach to this problem is to utilise a rolling linear regression with a lookback window. This involves updating the linear regression on every bar so that the slope and intercept terms "follow" the latest behaviour of the cointegration relationship. However it also introduces another free parameter into the strategy–the lookback window length. This must be optimised often via cross-validation.

A more sophisticated approach is to utilise a state space model that treats the "true" hedge ratio as an unobserved hidden variable and attempts to estimate it with "noisy" observations. In our case this means the pricing data of each asset.

The Kalman Filter performs exactly this task. In the previous section we took an in-depth look at the Kalman Filter and how it could be viewed as a Bayesian updating process.

In this section we are going to make use of the Kalman Filter via the [PyKalman](https://pykalman.github.io/) Python library to help us dynamically estimate the slope and intercept (and hence hedging ratio) between a pair of ETFs.

This technique will ultimately be backtested with QSTrader in a later chapter. It will enable us to see how performance of such a strategy has changed in the last few years.

The plots in this chapter were largely inspired by and extended from a post[74] written by Aidan O'Mahoney who runs [The Algo Engineer](http://www.thealgoengineer.com/) blog. Head over to his blog to check out more great posts on algo trading.

#### 13.3.1 Linear Regression via the Kalman Filter

How do we utilise this state space model approach to incorporate the information in a linear regression?

In a subsequent chapter we define the multiple linear regression as a model which possesses a response value y that is a linear function of its feature inputs x:

$$y(\mathbf{x}) = \boldsymbol{\beta}^T \mathbf{x} + \boldsymbol{\epsilon} \tag{13.31}$$

Where β <sup>T</sup> = (β0, β1, . . . , βp) represents the transpose vector of the intercept β<sup>0</sup> and slopes βi , with ∼ N (µ, σ<sup>2</sup> ) represents the error term.

Since we are in a one-dimensional setting we can simply write β <sup>T</sup> = (β0, β1) and x = (x, 1)<sup>T</sup> . We set the (hidden) states of our system to be given by the vector β <sup>T</sup> –the intercept and slope of our linear regression. The next step is to assume that tomorrow's intercept and slope are equal to today's intercept and slope with the addition of some random system noise. This gives it the nature of a random walk, the behaviour of which is discussed at length in the previous chapter on white noise and random walk models.

$$\beta_{t+1} = \mathbf{I}\beta_t + w_t \tag{13.32}$$

Where the transition matrix is set to the two-dimensional indentify matrix, G<sup>t</sup> = I. This is one half of the state space model. The next step is to actually use one of the ETFs in the pair as the "observations".

#### 13.3.2 Applying the Kalman Filter to a Pair of ETFs

To form the observation equation it is necessary to choose one of the ETF pricing series to be the "observed" variables, yt, and the other to be given by xt, which provides the linear regression formulation as above:

$$y_t = F_t \mathbf{x}_t + v_t \tag{13.33}$$

$$= (\beta_0, \beta_1) \begin{pmatrix} 1 \\ x_t \end{pmatrix} + v_t \tag{13.34}$$

Thus we have the linear regression reformulated as a state space model, which allows us to estimate the intercept and slope as new price points arrive via the Kalman Filter.

#### 13.3.3 TLT and ETF

We are going to consider two fixed income ETFs, namely the [iShares 20+ Year Treasury Bond](https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf) [ETF \(TLT\)](https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf) and the [iShares 3-7 Year Treasury Bond ETF \(IEI\).](https://www.ishares.com/us/products/239455/ishares-37-year-treasury-bond-etf) Both of these ETFs track the performance of varying duration US Treasury bonds and as such are both exposed to similar market factors. We will analyse their regression behaviour over the last five years or so.

#### 13.3.4 Scatterplot of ETF Prices

We are now going to use a variety of Python libraries, including NumPy, Matplotlib, Pandas and PyKalman to to analyse the behaviour of a dynamic linear regression between these two securities. As with all Python programs the first task is to import the necessary libraries:

```
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
from pykalman import KalmanFilter
```

Note: You will likely need to run pip install pykalman to install the PyKalman library as it is not bundled with Anaconda.

The next step is write the function draw\_date\_coloured\_scatterplot to produce a scatterplot of the asset adjusted closing prices (such a scatterplot is inspired by that produced by Aidan O'Mahony[74]). The scatterplot will be coloured using a Matplotlib colour map, specifically "Yellow To Red", where yellow represents price pairs closer to 2010, while red represents price pairs closer to 2016:

```
def draw_date_coloured_scatterplot(etfs, prices):
    """
    Create a scatterplot of the two ETF prices, which is
    coloured by the date of the price to indicate the
    changing relationship between the sets of prices
    """
    # Create a yellow-to-red colourmap where yellow indicates
    # early dates and red indicates later dates
    plen = len(prices)
    colour_map = plt.cm.get_cmap('YlOrRd')
    colours = np.linspace(0.1, 1, plen)
    # Create the scatterplot object
    scatterplot = plt.scatter(
        prices[etfs[0]], prices[etfs[1]],
        s=30, c=colours, cmap=colour_map,
        edgecolor='k', alpha=0.8
    )
    # Add a colour bar for the date colouring and set the
    # corresponding axis tick labels to equal string-formatted dates
    colourbar = plt.colorbar(scatterplot)
    colourbar.ax.set_yticklabels(
        [str(p.date()) for p in prices[::plen//9].index]
    )
    plt.xlabel(prices.columns[0])
    plt.ylabel(prices.columns[1])
    plt.show()
```

I have commented the code to make it fairly straightforward to see what all of the commands are doing. The main work is being done within the colour\_map, colours and scatterplot variables. It is given in Figure 13.1.

#### 13.3.5 Time-Varying Slope and Intercept

The next step is to actually use PyKalman to dynamically adjust the intercept and slope between TFT and IEI. This function is more complex and requires some explanation.

Firstly we define a variable called delta, which is used to control the transition covariance for the system noise. This controls the value of Wt. We simply multiply such a value by the

![](_page_9_Figure_0.jpeg)

Figure 13.1: Scatterplot of the fixed income ETFs, TFT vs IEI

two-dimensional identity matrix.

Subsequently we create the observation matrix. As we previously described, this matrix is a row vector consisting of the prices of TFT and a sequence of unity values. To construct this we utilise the NumPy vstack method to vertically stack these two price series into a single column vector, which we then transpose.

At this point we use the KalmanFilter class from PyKalman to create the Kalman Filter instance. We supply it with the dimensionality of the observations, which is unity in this case. We also supply it with the dimensionality of the states, which is two, as we are looking at the intercept and slope in the linear regression.

We also need to supply the mean and covariance of the initial state. In this instance we set the initial state mean to be zero for both intercept and slope, while we take the two-dimensional identity matrix for the initial state covariance. The transition matrices are also given by the two-dimensional identity matrix.

The last terms to specify are the observation matrices as above in obs\_mat, with its covariance equal to unity. Finally the transition covariance matrix (controlled by delta) is given by trans\_cov, described above.

Now that we have the kf Kalman Filter instance we can use it to filter based on the adjusted prices from IEI. This provides us with the state means of the intercept and slope. This is ultimately what we are after. In addition we also receive the covariances of the states.

This is all wrapped up in the calc\_slope\_intercept\_kalman function:

#### **def** calc\_slope\_intercept\_kalman(etfs, prices): """

```
Utilise the Kalman Filter from the PyKalman package
to calculate the slope and intercept of the regressed
ETF prices.
"""
delta = 1e-5
trans_cov = delta / (1 - delta) * np.eye(2)
obs_mat = np.vstack(
    [prices[etfs[0]], np.ones(prices[etfs[0]].shape)]
).T[:, np.newaxis]
kf = KalmanFilter(
    n_dim_obs=1,
    n_dim_state=2,
    initial_state_mean=np.zeros(2),
    initial_state_covariance=np.ones((2, 2)),
    transition_matrices=np.eye(2),
    observation_matrices=obs_mat,
    observation_covariance=1.0,
    transition_covariance=trans_cov
)
```

```
state_means, state_covs = kf.filter(prices[etfs[1]].values)
return state_means, state_covs
```

Finally we plot these values as returned from the previous function. To achieve this we simply create a Pandas DataFrame of the slopes and intercepts at time values t using the index from the prices DataFrame and plot each column as a subplot:

```
def draw_slope_intercept_changes(prices, state_means):
    """
    Plot the slope and intercept changes from the
    Kalman Filter calculated values.
    """
    pd.DataFrame(
        dict(
            slope=state_means[:, 0],
            intercept=state_means[:, 1]
        ), index=prices.index
    ).plot(subplots=True)
    plt.show()
```

The output is given in Figure 13.2.

Clearly the time-varying slope changes dramatically over the 2011 to 2016 period, dropping from around 1.38 in 2011 to around 0.9 in 2016. It is not difficult to see that utilising a fixed hedge ratio in a pairs trading strategy would be far too rigid.

In addition the estimate of the slope is relatively noisy. This can be controlled by the delta variable given in the code above but has the effect of also reducing the responsiveness of the filter

![](_page_11_Figure_0.jpeg)

Figure 13.2: Time-varying slope and intercept of a linear regression between ETFs TFT and IEI

to changes in the "true" unobserved hedge ratio between the two ETFs.

If this was to be put into production as a live trading strategy it would be necessary to optimise the delta parameter across baskets of pairs of ETFs utilising cross-validation.

# 13.4 Next Steps

Now that we have been able to construct a dynamic hedging ratio between the two ETFs we need a way to actually carry out a trading strategy based off of this information. A later chapter makes use of QSTrader to perform a backtest on the pair of ETFs mentioned above.

# 13.5 Bibliographic Note

Utilising the Kalman Filter for "online linear regression" has been carried out by many quant trading individuals. Ernie Chan utilises the technique in his book[32] to estimate the dynamic linear regression coefficients between the two ETFs: EWA and EWC.

Aidan O'Mahony used Matplotlib and PyKalman to also estimate the regression coefficients in his post[74], which inspired the diagrams for this chapter.

Jonathan Kinlay discusses the application of the Kalman Filter to simulated financial data[64] and suggests that it might be advisable to use the KF to suppress trade signals generated in periods of high noise, or to increase allocations to pairs where the noise is low.

An introductory discussion about the Kalman Filter, using the R programming language, can be found in Cowpertwait and Metcalfe[35].

# 13.6 Full Code

```
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
from pykalman import KalmanFilter
def draw_date_coloured_scatterplot(etfs, prices):
    """
    Create a scatterplot of the two ETF prices, which is
    coloured by the date of the price to indicate the
    changing relationship between the sets of prices
    """
    # Create a yellow-to-red colourmap where yellow indicates
    # early dates and red indicates later dates
    plen = len(prices)
    colour_map = plt.cm.get_cmap('YlOrRd')
    colours = np.linspace(0.1, 1, plen)
    # Create the scatterplot object
    scatterplot = plt.scatter(
        prices[etfs[0]], prices[etfs[1]],
        s=30, c=colours, cmap=colour_map,
        edgecolor='k', alpha=0.8
    )
    # Add a colour bar for the date colouring and set the
    # corresponding axis tick labels to equal string-formatted dates
    colourbar = plt.colorbar(scatterplot)
    colourbar.ax.set_yticklabels(
        [str(p.date()) for p in prices[::plen//9].index]
    )
    plt.xlabel(prices.columns[0])
    plt.ylabel(prices.columns[1])
    plt.show()
def calc_slope_intercept_kalman(etfs, prices):
    """
    Utilise the Kalman Filter from the PyKalman package
    to calculate the slope and intercept of the regressed
    ETF prices.
    """
```

```
delta = 1e-5
    trans_cov = delta / (1 - delta) * np.eye(2)
    obs_mat = np.vstack(
        [prices[etfs[0]], np.ones(prices[etfs[0]].shape)]
    ).T[:, np.newaxis]
    kf = KalmanFilter(
        n_dim_obs=1,
        n_dim_state=2,
        initial_state_mean=np.zeros(2),
        initial_state_covariance=np.ones((2, 2)),
        transition_matrices=np.eye(2),
        observation_matrices=obs_mat,
        observation_covariance=1.0,
        transition_covariance=trans_cov
    )
    state_means, state_covs = kf.filter(prices[etfs[1]].values)
    return state_means, state_covs
def draw_slope_intercept_changes(prices, state_means):
    """
    Plot the slope and intercept changes from the
    Kalman Filter calculated values.
    """
    pd.DataFrame(
        dict(
            slope=state_means[:, 0],
            intercept=state_means[:, 1]
        ), index=prices.index
    ).plot(subplots=True)
    plt.show()
if __name__ == "__main__":
    # Choose the ETF symbols to work with along with
    # start and end dates for the price histories
    etfs = ['TLT', 'IEI']
    start_date = "2010-8-01"
    end_date = "2016-08-01"
    # Obtain the adjusted closing prices from Yahoo finance
    etf_df1 = pdr.get_data_yahoo(etfs[0], start_date, end_date)
```

etf\_df2 = pdr.get\_data\_yahoo(etfs[1], start\_date, end\_date)

```
prices = pd.DataFrame(index=etf_df1.index)
prices[etfs[0]] = etf_df1["Adj Close"]
prices[etfs[1]] = etf_df2["Adj Close"]
draw_date_coloured_scatterplot(etfs, prices)
state_means, state_covs = calc_slope_intercept_kalman(etfs, prices)
```

draw\_slope\_intercept\_changes(prices, state\_means)
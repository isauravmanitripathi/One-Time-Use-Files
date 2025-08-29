#### 12.1 Introduction

In many of the previous chapters, the agent made trading decisions based on three key ingredients: (i) the midprice, (ii) the arrival of incoming market orders (MOs), and (iii) the agent's own inventory. In some cases, these state variables were supplemented by observables such as order flow (see, e.g., Section  $7.3$  and Chapter 9), short-term-alpha in 10.4.2, and co-integration of prices in Chapter 11, among others. In this chapter, we investigate the role that another important state variable plays: the quoted volume order imbalance (or simply order imbalance). This is a measure of the buy versus sell pressure on an asset and, as we will see, it contains predictive power on both the arrival rates of MOs, and the direction and size of future price movements. Hence, it is an important factor to include when designing trading algorithms.

The chapter is organised as follows: in Section  $12.2$  we define order imbalance, and show using NASDAQ data how it typically evolves at an intraday level. The section also introduces three Markov Chain models for order imbalance, arrival of MOs and price jumps, and develops maximum likelihood estimators of the model parameters. Section 12.3 provides a brief discussion of the daily features exhibited by order imbalance using functional data analysis. Finally, Section 12.4 provides an analysis of the optimal liquidation problem, using limit orders (LOs) only, in the presence of order imbalance.

#### 12.2 Intraday Features

We define limit order imbalance  $\rho_t$  at time t as the ratio of the quoted volume imbalance to the total quoted volume, i.e.

$$\rho_t = \frac{V_t^b - V_t^a}{V_t^b + V_t^a} \,,$$

where  $V_t^b$  denotes the volume of LOs posted on the bid side of the LOB and  $V_t^a$ denotes the volume of LOs posted on the ask side of the LOB. For simplicity, from now on we refer to the LO imbalance as order imbalance. The volumes may be computed by looking only at-the-touch, the best  $n$ -levels of the LOB,

![](_page_1_Figure_1.jpeg)

or volume that is posted within  $n$  ticks of the midprice. All of these are viable measures, and it is up to the agent to decide which is best in a given situation. Some studies suggest that the best trade-off between predictive power versus model complexity is strongest using only the touch. For simplicity we use only this information for our estimations, although nothing in the model dictates this restriction.

Figure  $12.1$  shows order imbalance for Oracle Corporation (ORCL) computed from the Nov  $1, 2013$  event data (NASDAQ exchange) sampled every millisecond and averaged over 100ms, and as mentioned above, using volume posted only atthe-touch. The bottom left and right panels show the imbalance for two-minute periods starting at  $10:00$ am and  $10:15$ am together with 5 regimes of imbalance chosen to be equally spaced along the points  $\rho_t \in \{-1, -0.6, -0.2, 0.2, 0.6, 1\}.$ The top panel shows the order imbalance for the entire day and illustrates the significant fluctuations in order imbalance throughout the day. When imbalance is placed into bins, the fluctuation rates are somewhat mitigated. Figure 12.2 shows some properties of MO arrivals. The left panel shows the percentage of MOs which are buys/sells/total when order imbalance is in a particular regime  $-$  so that, e.g., when buy MOs arrive, 40.1 percent of the time order imbalance is in regime 4. The right panel shows the arrival rate (per second) of MOs by normalising the number of MOs that arrive in a regime according to the time that order imbalance spends in that regime. It appears that the arrival of buy MOs is biased towards times when order imbalance is high, and similarly sell

![](_page_2_Figure_1.jpeg)

Figure 12.2 MO arrival for ORCL on Nov 1, 2013 conditional on imbalance regimes.

![](_page_2_Figure_3.jpeg)

Figure 12.3 Auto-correlation of imbalance (left panel) and correlation of order imbalance with price changes (right panel) for ORCL on Nov 1, 2013.

MOs arrive more frequently when order imbalance is negative. The total arrival rates exhibit a U-shaped pattern as a function of order imbalance, indicating that MOs tend to arrive more frequently when the LOB is bid-heavy ( $\rho$  close to 1) or ask-heavy ( $\rho$  close to -1). We explore these features more deeply later in this chapter.

Figure 12.3 shows the auto-correlation function  $(ACF)$  over 2,000 lags which equals 200 secs, as well as the correlation between imbalance and the price change (conditional on a price change occurring) over the next  $n$ -intervals. As the plot shows, there is a significant amount of auto-correlation in order imbalance. Moreover, order imbalance is positively correlated with price changes. This correlation naturally becomes less significant as the lag increases.

#### A Markov Chain Model 12.2.1

We provide a simple Markov chain model for order imbalance and show how to calibrate it to market data. Let  $Z_t \in \{1, \ldots, K\}$  denote the order imbalance regime observed at time t, here taken to be discrete  $t \in \{1, 2, \ldots, T\}$ . We assume that order imbalance is described by a Markov chain with transition matrix  $A$ .

## Maximum Likelihood Estimator

Let  $z_1, z_2, \ldots, z_T$  denote a sequence of observations from the Markov chain Z. Below we show that the maximum likelihood estimator (MLE) of the elements of the transition matrix  $A$  is given by

$$\hat{A}_{ij} = \frac{n_{ij}}{\sum_{j=1}^{K} n_{ij}} \,, \tag{12.1}$$

where  $n_{ij} = \sum_{t=2}^{T} \mathbb{1}_{\{Z_{t-1}=i, Z_{t}=j\}}$ , i.e.  $n_{ij}$  is the number of observed transitions from regime  $i$  to regime  $j$ .

To demonstrate this result, we first write the likelihood  $L$  of the sequence of  $\text{observations as}$ 

$$L = A_{Z_1, Z_2} \times A_{Z_2, Z_3} \times \cdots \times A_{Z_{T-1}, Z_T} = \prod_{i,j=1}^K A_{ij}^{n_{ij}}.$$

The second equality follows from collecting like terms together. Next, note that the transition matrix is constrained so that  $A_{ij} \geq 0$  and the sum along each row equals 1, i.e.  $\sum_{j=1}^{K} A_{ij} = 1$  for  $i = 1, \ldots, K$ . Next, we wish to maximise L, or equivalently, the log-likelihood ( $\log L$ ) subject to this summation constraint (the positivity constraint will be automatic). To this end, we introduce the Lagrange multipliers,  $\gamma_1, \ldots, \gamma_K$  and aim to maximise

$$f(\boldsymbol{A}, \boldsymbol{\gamma}) = \log L + \sum_{i=1}^{K} \gamma_i \left( \sum_{j=1}^{K} A_{ij} - 1 \right)$$
  
= 
$$\sum_{i,j=1}^{K} n_{ij} \log A_{ij} + \sum_{i=1}^{K} \gamma_i \left( \sum_{j=1}^{K} A_{ij} - 1 \right)$$

The first order conditions,  $\partial_{A_{ii}} f(\boldsymbol{A}, \boldsymbol{\gamma}) = 0$  and  $\partial_{\gamma_i} f(\boldsymbol{A}, \boldsymbol{\gamma}) = 0$ , imply that the MLE estimator  $\hat{A}$  of  $A$  satisfies

$$0 = \frac{n_{ij}}{\hat{A}_{ij}} + \gamma_i \,, \tag{12.2a}$$

$$0 = \sum_{j=1}^{K} \hat{A}_{ij} - 1.$$
 (12.2b)

From (12.2a) we can write the Lagrange multiplier in terms of  $n_{ij}$  and  $A_{ij}$  as

$$\gamma_i = -\frac{n_{ij}}{\hat{A}_{ij}}\,. \tag{12.3}$$

Next, multiplying (12.2a) by  $\hat{A}_{ij}$  and then summing over j from 1 to K implies

that

$$0 = \sum_{j=1}^{K} n_{ij} + \gamma_i \sum_{j=1}^{K} \hat{A}_{ij} = \sum_{j=1}^{K} n_{ij} + \gamma_i = \sum_{j=1}^{K} n_{ij} - \frac{n_{ij}}{\hat{A}_{ij}},$$

where in the second equality we use the constraint (12.2b) to write  $\sum_{j=1}^{K} \hat{A}_{ij} = 1$ and in the third equality we use  $(12.3)$  to eliminate the Lagrange multiplier. Solving for  $A_{ij}$  provides us with the result in (12.1).

# Estimation from Data

For the model estimation from data we use ORCL on Nov 1, 2013 with order balance measured every millisecond (volume at-the-touch) and averaged over the last 100ms. We then bin the order imbalance into 5 equally spaced regimes, and find the following estimator for the transition matrix:

$$\hat{\mathbf{A}} = \begin{pmatrix} 0.946 & 0.050 & 0.003 & 0.000 & 0.000 \\ 0.006 & 0.973 & 0.020 & 0.001 & 0.000 \\ 0.000 & 0.009 & 0.979 & 0.012 & 0.000 \\ 0.000 & 0.000 & 0.013 & 0.980 & 0.008 \\ 0.000 & 0.000 & 0.001 & 0.023 & 0.976 \end{pmatrix} . \tag{12.4}$$

The estimated transition rates indicate that the chain tends to move only between its neighbours. Moreover, for this specific asset and day, the slightly bidheavy regime 4 appears to be the "stickiest" since the probability of remaining there is highest. There also appears to be transition pressure towards cycling back and forth between the neutral  $(3)$  and slightly bid-heavy  $(4)$  regimes – because  $A_{34} > A_{32}$  and  $A_{43} > A_{45}$ .

### From Discrete- to Continuous-Time Markov Models

In the previous section, we focused on a discrete-time Markov model for order imbalance. When developing stochastic models for algorithmic trading, however, it proves more useful to utilise continuous-time Markov models because we are using the tools of continuous-time stochastic control. Indeed, there is a simple transformation that transforms the discrete-time model into a continuous-time one. First, recall that a continuous-time Markov model  $Z = \{Z_t\}_{0 \le t \le T}$  with  $Z_t \in$  $\{1,\ldots,K\}$ , has a generator matrix **B** which produces transition probabilities

$$\mathbb{P}(Z_t = j \,|\, Z_s = i) = \left[ \exp\{B\left(t - s\right)\} \right]_{ij} \,, \qquad t \ge s \,,$$

where the exponential here is a matrix exponential and  $[\cdot]_{ij}$  denotes the  $ij^{th}$ element of the matrix in the braces. Also recall that the generator matrix must satisfy the conditions

$$B_{ij} \ge 0 \,, \quad \forall \, i \ne j \,, \qquad \text{and} \qquad \sum_{i=1}^{K} B_{ij} = 0 \,,$$

so that the diagonal elements equal negative the sum of the off diagonal elements. The absolute value of the diagonal elements represent the rate of flow out of that regime.

The continuous-time model can then be estimated from the discrete-time one by matching the estimated transition probability in the discrete setting from the previous section. Specifically, we set

$$\exp\{\hat{B}\,\Delta T\} = \hat{A} \quad \Rightarrow \quad \hat{B} = \frac{1}{\Delta T}\log\hat{A} \,.$$

In the above, the logarithm is to be interpreted as a matrix logarithm and  $\Delta T$  is the time between observations in the discrete Markov chain. In the next section we show a more formal approach to the estimation which also takes into account the arrival of  $\text{MOs.}$ 

For the 100ms transition rate matrix which we estimated at the start of the previous subsection (see  $(12.4)$ ), the corresponding generator matrix is

$$\hat{\boldsymbol{B}} = \begin{pmatrix}\n-0.553 & 0.521 & 0.030 & 0.002 & 0.000 \\
0.068 & -0.279 & 0.205 & 0.005 & 0.001 \\
0.001 & 0.089 & -0.219 & 0.128 & 0.001 \\
0.000 & 0.002 & 0.128 & -0.209 & 0.078 \\
0.000 & 0.001 & 0.008 & 0.235 & -0.244\n\end{pmatrix}.\n$$
(12.5)

Focusing on the diagonal elements, which represent minus one times the sum of the rate of transition out of the corresponding regime, we see that the chain tends to flow out of the ask-heavy regimes towards the slightly bid-heavy regime. Once there, it tends to flow back to the neutral regime.

#### 1222 Jointly Modelling Market Orders

We extend the continuous-time Markov model of the previous section to include the modelling of MO arrivals. We also note that the continuous-time approximation above has one important flaw - the discrete-time model is estimated from average order imbalance over a 100ms window, therefore a continuous-time limit based on this estimate will not account properly for the interdependence of overlapping time windows.

To address these issues, we assume that, conditional on being within a given regime  $k$ , market buy and sell orders arrive independently at the arrival times of independent Poisson processes with rates  $\lambda_k^+$  and  $\lambda_k^-$ , respectively. That is, the counting processes  $M^{\pm} = \{M^{\pm}_t\}_{0 \le t \le T}$  of market buy (sell) orders are doubly stochastic Poisson processes with activity rates  $\Lambda_t^{\pm} = \lambda_{Z_t}^{\pm}$ , where  $\lambda_1^{\pm}, \lambda_2^{\pm}, \ldots, \lambda_K^{\pm}$ denote the activity rates in the various regimes. In addition, the order imbalance will be observed at every event, and the inter-arrival times of the events will play a role.

Referring to Figure 12.4, let  $\tau_1, \tau_2, \ldots, \tau_N$  denote the switching times of the regimes, i.e. the times at which the continuous-time Markov chain  $Z$  changes (with generator matrix denoted by **B**). We call the time interval  $[\tau_r, \tau_{r+1})$  the

![](_page_6_Figure_1.jpeg)

Figure 12.4 Snapshot of the event timeline for computing the within epoch likelihood.

 $r^{th}$  epoch  $(r = 0, \ldots, N)$  with  $\tau_{N+1} = T$  the end of the observation time horizon. Next, let  $\{b_{r,1}, b_{r,2}, \ldots, b_{r,m_r}\}$  and  $\{s_{r,1}, s_{r,2}, \ldots, s_{r,n_r}\}$  denote the arrival times of buy and sell MOs, respectively, during the  $r^{th}$  epoch. Then, since arrivals within an epoch of buys and sells are i.i.d., the likelihood within the  $r^{th}$ -epoch is

$$L_{r} = \underbrace{\lambda_{Z_{\tau_{r}}}^{+} e^{-\lambda_{Z_{\tau_{r}}}^{+} (b_{r,1} - b_{r,0})} \times \cdots \times \lambda_{Z_{\tau_{r}}}^{+} e^{-\lambda_{Z_{\tau_{r}}}^{+} (b_{r,m_{r}} - b_{r,m_{r}-1})}}_{\text{buy arrivals}}$$

$$\times \underbrace{e^{-\lambda_{Z_{\tau_{r}}}^{+} (\tau_{r+1} - b_{r,m_{r}})}}_{\text{no more buys}}$$

$$\times \underbrace{\lambda_{Z_{\tau_{r}}}^{-} e^{-\lambda_{Z_{\tau_{r}}}^{-} (s_{r,1} - s_{0,1})} \times \cdots \times \lambda_{Z_{\tau_{r}}}^{-} e^{-\lambda_{Z_{\tau_{r}}}^{-} (s_{r,n_{r}} - s_{r,n_{r}-1})}}_{\text{sell arrivals}}$$

$$\times \underbrace{e^{-\lambda_{Z_{\tau_{r}}}^{-} (\tau_{r+1} - s_{r,n_{r}})}}_{\text{no more sells}}$$

$$= \left(\lambda_{Z_{\tau_{r}}}^{+}\right)^{M_{r}^{+}} e^{-\lambda_{Z_{\tau_{r}}}^{+} (\tau_{r+1} - \tau_{r})} \times \left(\lambda_{Z_{\tau_{r}}}^{-}\right)^{M_{r}^{-}} e^{-\lambda_{Z_{\tau_{r}}}^{-} (\tau_{r+1} - \tau_{r})}.$$

Here, we set  $b_{r,0} = s_{r,0} = \tau_r$  for notational convenience. In the first equality, the first (second) line represents the likelihood of the sequence of buy (sell) orders. In each line, the first to second last terms, of the form  $\lambda_{Z_{\tau_n}}^{\pm}e^{-\lambda_{Z_{\tau_r}}^{\pm}(t_{r,l}-t_{r,l-1})}$ , represent the survival since the last order arrival, and then the arrival of an MO at time  $t_r$ . The last term in each line represents the probability that no event arrives between the last buy (sell) MO and the time at which the Markov chain switches. The second equality is obtained by re-arranging the terms and letting  $M_r^{\pm}$  denote the number of buy and sell MOs which arrive in the  $r^{th}$ -epoch.

The full likelihood is obtained by sewing together the within epoch likelihoods with the transition probability and the arrival of orders that occur after the last regime change, but before the sample ends. In all,

$$L = L_0 \times [e^{\boldsymbol{B}\tau_1}]_{Z_{\tau_0}Z_{\tau_1}} \times [\boldsymbol{B}]_{Z_{\tau_0}Z_{\tau_1}} \times \cdots \times L_{N-1} \times [e^{\boldsymbol{B}(\tau_N - \tau_{N-1})}]_{Z_{\tau_{N-1}}Z_{\tau_N}} \times [\boldsymbol{B}]_{Z_{\tau_{N-1}}Z_{\tau_N}}.$$

Recall that  $\tau_0 = 0$  and  $\tau_{N+1} = T$  is the time of the last MO (buy or sell) after the last regime change. We in fact exclude the data from this last regime change to avoid some issues with censored data - which render the maximisation analytically intractable, although it is still amenable to numerical methods. Next,

recall that a continuous-time Markov chain generator matrix has rows which sum to zero, and the non-diagonal elements are non-negative. Hence, we write the generator matrix  $\boldsymbol{B}$  as

$$B = \begin{pmatrix} -\Lambda_1 & \lambda_{12} & \lambda_{13} & \dots & \lambda_{1K} \\ \lambda_{21} & -\Lambda_2 & \lambda_{23} & \dots & \lambda_{2K} \\ \lambda_{31} & \lambda_{32} & -\Lambda_3 & \dots & \lambda_{3K} \\ \vdots & \vdots & & \ddots & \vdots \\ \lambda_{K1} & \lambda_{K2} & \lambda_{K3} & \dots & -\Lambda_K \end{pmatrix},$$

where  $\Lambda_i := \sum_{j\neq i}^K \lambda_{ij}$  represents the total rate of outflow from regime *i*. The survival probability of the time  $\tau_i$  at which the chain transitions out of regime i is given by

$$\mathbb{P}(\tau_i > t \,|\, Z_s = i) = e^{-\Lambda_i \, (t-s)}, \qquad s \le t \,,$$

and conditional on a transition occurring, the chain will switch from regime  $i$  to regime  $j$  with probability

$$[P]_{ij} = \frac{\lambda_{ij}}{\Delta_i}, \quad \text{for } i \neq j.$$

Using this representation for the transition probability and expanding the likelihood above, we have

$$L = \prod_{n=1}^{N} \left\{ \left( \lambda_{Z_{\tau_{n-1}}}^{+} \right)^{M_{n-1}^{+}} e^{-\lambda_{Z_{\tau_{n-1}}}^{+} (\tau_{n} - \tau_{n-1})} \left( \lambda_{Z_{\tau_{n-1}}}^{-} \right)^{M_{n-1}^{-}} e^{-\lambda_{Z_{\tau_{n-1}}}^{-} (\tau_{n} - \tau_{n-1})} \right.$$
$$\times \left. \Lambda_{Z_{\tau_{n-1}}} e^{-\Lambda_{Z_{\tau_{n-1}}} (\tau_{n} - \tau_{n-1})} \left[ \boldsymbol{P} \right]_{Z_{\tau_{n-1}} Z_{\tau_{n}}} \right\}.$$

Next, we re-arrange the terms by collecting like regimes and like transitions to obtain

$$L = \left(\prod_{i=1}^{K} \left(\lambda_{i}^{+}\right)^{\hat{M}_{i}^{+}} e^{-\lambda_{i}^{+}\Delta\tau_{i}} \times \left(\lambda_{i}^{-}\right)^{\hat{M}_{i}^{-}} e^{-\lambda_{i}^{-}\Delta\tau_{i}}\right)$$
$$\times \left(\prod_{i,j=1}^{K} \left([\boldsymbol{P}]_{ij}\right)^{n_{ij}}\right) \times \left(\prod_{i=1}^{K} \Lambda_{i}^{n_{i}} e^{-\Lambda_{i}\Delta\tau_{i}}\right)$$

Here,  $\hat{M}_{i}^{\pm}$  denotes the number of market buy (sell) orders that occur while the chain is in regime i,  $\Delta \tau_i$  denotes the total time the Markov chain spent in regime i, and  $n_{ij}$  denotes the number of times the chain switches from i to j. Since the times  $\tau_1, \tau_2, \ldots, \tau_N$  are by definition the times at which the Markov chain switches regime, we must have  $n_{ii} = 0$  and so  $[P]_{ii} = 0$ .

Finally, we optimise the likelihood over the parameters  $\lambda_i^{\pm}$ ,  $\boldsymbol{P}$  and  $\Lambda_i$ . Each of these optimisations can be carried out independently, and follow along the lines

outlined in the earlier subsection. Here, we simply record the final results for the MLE estimators of the model parameters:

$$\hat{\lambda}_{i}^{\pm} = \frac{\hat{M}_{i}^{\pm}}{\Delta \tau_{i}}, \qquad \hat{\Lambda}_{i} = \frac{\sum_{j \neq i} n_{ij}}{\Delta \tau_{i}}, \qquad \text{and} \qquad [\hat{\boldsymbol{P}}]_{ij} = \frac{n_{ij}}{\sum_{j \neq i} n_{ij}}, \qquad (12.6)$$

from which we find that the MLE estimate of the off-diagonal elements of the generator matrix is

$$\hat{\lambda}_{ij} = \frac{n_{ij}}{\Delta \tau_i}$$

The above results are similar to the simple Markov chain model, but now we also account for the regime specific arrival rate of market buy and sell orders.

Applying the MLE procedure to the ORCL data on Nov 1, 2013, using the imbalance at every event time, we obtain the following estimates (with time  $measured \text{ in seconds})$ :

$$\hat{\lambda}^{+} = \begin{pmatrix} 0.074 \\ 0.042 \\ 0.037 \\ 0.074 \\ 0.216 \end{pmatrix}, \qquad \hat{\lambda}^{-} = \begin{pmatrix} 0.856 \\ 0.123 \\ 0.048 \\ 0.027 \\ 0.025 \end{pmatrix},\n$$
and
$$\n\hat{B} = \begin{pmatrix} -3.34 & 2.34 & 0.59 & 0.28 & 0.13 \\ 0.31 & -0.93 & 0.54 & 0.01 & 0.07 \\ 0.01 & 0.26 & -0.58 & 0.30 & 0.02 \\ 0.03 & 0.01 & 0.29 & -0.56 & 0.23 \\ 0.03 & 0.03 & 0.09 & 0.74 & -0.88 \end{pmatrix}.\n$$
(12.7)

Comparing the estimate  $(12.7)$  with the estimate  $(12.5)$  we see some difference in the overall rates. This difference results from the fact that  $(12.5)$  is estimated using the average order imbalance over the previous  $100 \text{ms}$ , while  $(12.7)$  is estimated using the instantaneous order imbalance. Nonetheless, the chain has the same tendency to move to the slightly bid-heavy regime 4. The estimated arrival rates show a clear bias towards sell MOs on this day, with a total sell arrival rate of  $1.079$  per second versus a total buy arrival rate of  $0.444$  per second. Interestingly, although the overall day was a sell-heavy one, if we condition on being in a bid-heavy regime  $(4 \text{ or } 5)$ , the arrival rate of buy MOs is significantly larger than that of sell MOs. This observation indicates that the order imbalance is indeed a good predictor of order flow.

#### 12.2.3 Modelling Price Jumps

Up to this point, we have been concerned with understanding how order imbalance influences the rate of arrival of MOs. An important and interesting related question is to determine the distribution of price changes conditional on the arrival of buy and sell MOs and the order imbalance regime prior to the arrival of that MO. To answer this question, we record the time of each MO and compute the midprice change ls afterwards, conditional on the order imbalance regime when split into 5 equal bins with knots at {-1, -¾, -¼, +¼, +¾, +1 }, as in the previous section. The corresponding states and imbalance p is given by

$$Z = \begin{cases} -2, & \rho \in [-1, -\frac{3}{5}], & \text{sell-heavy,} \\ 0, & \rho \in [-\frac{3}{5}, -\frac{1}{5}), & \text{sell-bias,} \\ 0, & \rho \in [-\frac{1}{5}, +\frac{1}{5}), & \text{neutral,} \\ \rho \in [+\frac{1}{5}, +\frac{3}{5}), & \text{ buy-bias,} \\ \rho \in [+\frac{3}{5}, +1], & \text{ buy-heavy.} \end{cases}$$

Table 12.1 shows the price change distribution conditional on the order imbalance regimes.

| Buy Market Orders                                                                        |       |       |       |       |        |       |
|------------------------------------------------------------------------------------------|-------|-------|-------|-------|--------|-------|
|                                                                                          |       | Z= -2 | Z= -1 | Z=O   | Z = +1 | Z=+2  |
|                                                                                          | >,+   | 0.074 | 0.042 | 0.037 | 0.075  | 0.216 |
| Ct)<br><i< td=""><td>-300</td><td></td><td></td><td></td><td></td><td></td></i<>         | -300  |       |       |       |        |       |
|                                                                                          | -0.02 |       |       |       |        |       |
|                                                                                          | -0.01 |       | 0.05  | 0.01  | 0.01   |       |
|                                                                                          | 0.00  | 1.00  | 0.86  | 0.77  | 0.78   | 0.70  |
|                                                                                          | 0.01  |       | 0.09  | 0.21  | 0.20   | 0.28  |
|                                                                                          | 0.02  |       |       |       |        | 0.02  |
|                                                                                          | 0.03  |       |       |       |        |       |
|                                                                                          |       |       |       |       |        |       |
| Sell Market Orders                                                                       |       |       |       |       |        |       |
|                                                                                          |       | Z= -2 | Z= -1 | Z =0  | Z = +1 | Z= +2 |
|                                                                                          | >.-   | 0.856 | 0.123 | 0.048 | 0.027  | 0.025 |
| Ct)<br><i< td=""><td>-300</td><td></td><td></td><td></td><td>0.01</td><td>0.03</td></i<> | -300  |       |       |       | 0.01   | 0.03  |
|                                                                                          | -0.02 | 0.01  |       | 0.01  | 0.02   | 0.01  |
|                                                                                          | -0.01 | 0.21  | 0.36  | 0.36  | 0.28   | 0.21  |
|                                                                                          | 0.00  | 0.79  | 0.64  | 0.63  | 0.69   | 0.75  |
|                                                                                          | 0.01  |       |       |       |        |       |
|                                                                                          | 0.02  |       |       |       |        |       |
|                                                                                          | 0.03  |       |       |       |        |       |

**Table 12.1** Price change distribution conditional on the order imbalance regimes for ORCL on Nov 1, 2013 (opening price is \$33.72), ask-heavy *Z* = -2, ask-bias *Z* = -1, neutral Z = 0, bid-bias Z = +1, bid-heavy Z = +2.

![](_page_10_Figure_1.jpeg)

Figure 12.5 Order imbalance for ORCL using 2013 data showing the first three functional principle components.

#### 12.3 **Daily Features**

In the previous section, we focused on intraday features of order imbalance. In a trading environment, an understanding of daily features can assist in augmenting and tweaking the intraday model to reflect historical overall behaviour. To see these daily effects, Figure 12.5 shows order imbalance for Oracle Corporation  $(ORCL)$  from the entire 2013 event data. We place order imbalance into ten equal buckets from  $-1$  to  $+1$  and compute the rate of arrival of buy and sell MOs together, conditional on an order imbalance bucket. These estimates are shown in the top panels. In the bottom panels, we show the rate of arrival of only buy MOs. The thick black, green and yellow lines are the mean curves, obtained through a functional regression using Legendre polynomials, and the  $\pm$  one standard deviation show the impact of the first three functional principle components. (We do not go into the details of how the functional principle components are obtained here.)

It is useful, however, to describe how the mean curves are obtained using functional data analysis (FDA) techniques. FDA takes the view that a sequence of observations is a realisation of a random draw from a function space, but observed discretely (in this case at the order imbalance buckets) with error. Each new collection of observations is a new random draw from this function space. In our present context, we view the trade activity  $\mu(\rho)$  as being samples

from a function space given by

$$\boldsymbol{\mu}(\rho) = \sum_{n=1}^{N} \boldsymbol{\alpha}_n \, P_n(\rho), \qquad \rho \in [0, 1],$$

where  $P_n(x)$  are the (normalised) Legendre polynomials of order 0 through N and  $\alpha_n$  are viewed as random variables on a probability space  $(\Omega, \mathbb{P}, \mathcal{F})$ . The observed imbalance activity  $\mu_t(\rho)$  on a given day is then viewed as a sample realisation of the random variables  $\alpha_n$ . In this sense, we see that  $\mu$  is in fact a random field, since it is parameterised continuously by  $\rho$ , but it is projected onto a finite dimensional space through the N random coefficients  $\alpha_n$ .

At the end of each trading day, we regress the activity as a function of imbalance (using the middle of each bucket) onto the Legendre polynomials, and determine an estimate of the realisation  $\hat{\alpha}$  of  $\{\alpha_n : n = 1, \ldots, N\}$  on that day:

$$\hat{\alpha}_t = \underset{\boldsymbol{\alpha}}{\arg\min} \sum_{m=1}^M \left( \left( \sum_{n=1}^N \alpha_n P_n(\rho_m) \right) - \mu_{t,m} \right)^2$$

Here,  $\mu_{t,m}$  denotes the sample activity on day t in imbalance bin m, and  $\rho_m$ denotes the imbalance in the middle of regime  $m$ . In this manner, we obtain a time series of coefficients  $\alpha_t$  covering the year.

The mean curve is obtained by computing the average of these daily estimates:  $\bar{\alpha}_k = \frac{1}{T} \sum_{t=1}^T \hat{\alpha}_{k,t}$ , substituting that average into (12.3) to obtain the mean curve

$$\bar{\mu}(\rho) = \sum_{n=1}^{N} \bar{\alpha}_k P_n(\rho), \qquad \rho \in [0, 1].$$

There are many other useful objects one can compute using FDA, such as the functional principle components, the estimate of the distribution of shape of the curve for the remainder of the day given what has been observed so far, and so on. For discussions on this and other tools that FDA provides we refer the interested reader to consult Ramsay & Silverman (2010).

#### 12.4 Optimal Liquidation

In this section we analyse how to incorporate order flow information in the optimal liquidation problem. Recall that in the optimal liquidation problem, the agent's goal is to liquidate all shares by the end of the trading horizon. In this section, we pose the problem for an agent who uses only LOs to make her decision and is allowed to post her order at an arbitrary depth  $\delta$  in the LO book (LOB). In particular, we use the same approach as in Section  $8.2$  for posing the agent's optimisation problem.

As in Section 8.2, the agent posts LOs at a depth  $\delta = (\delta_t)_{0 \le t \le T}$  from the midprice  $S = (S_t)_{0 \le t \le T}$ . As such, the agent's controlled cash process  $X^{\delta}$ 

(Xf)o<t<T satisfies the SDE

$$dX_t^{\delta} = (S_t + \delta_t) dN_t^{\delta} ,$$

where *N*<sup>15</sup>= *(Nf* )09�T is the controlled counting process which counts the agent's filled LOs posted at depth 5t at time t - assumed to be F-predictable. To keep the framework simple, we assume the agent's orders are filled at a rate *Ai'*<sup>15</sup>= e-" <sup>15</sup> , >..t, where >.. <sup>±</sup>= (>..;)o�t�T represent the rate of arrival of buy (sell) MOs from other agents. In this manner, the deeper the agent posts in the book, the less likely it is that her order is filled. More specifically, conditional on an MO arriving, the probability that her order is filled when she is posted at depth 5t is e-"<sup>15</sup> '. We further let JvJ<sup>±</sup>= (lvft±)o<t<T denote the counting processes for other agent's buy (sell) MOs, with intensities >.. ± .

Now we proceed by developing a model that incorporates the empirical observations described in the previous section, and in particular we jointly model the rate of arrival of MOs, price movements, and order imbalance. To this end, the midprice process should have jumps that are biased upwards when order imbalance is near + 1, it should have jumps that are biased downwards when order imbalance is near -1, and it should have symmetric jumps when order imbalance is near zero.

Moreover, arrival rates of MOs should also be biased in a similar fashion. For this purpose, we will use the Markov chain Z = (Zt)o<t<T to represent the order imbalance regime, with Zt E { -1, 0, + 1} representing sell-heavy, neutral and buy-heavy regimes - one could incorporate more refined regimes, but the framework remains essentially the same. We let *G* denote the generator of the order imbalance regime, and write >..; = >.. ± ( Zt) with a slight abuse of notation. Moreover, let {cci *k'* ci *k'* ... } denote i.i.d. random variables with distribution function *F:'* and { co *k* ,' c;-*k'* ... } denote i.i.d. random variables with distribution function Fi:, for k = -1, 0, 1, also mutually independent of one another. These random variables will generate jumps in the midprice when an MO arrives and the order imbalance is in regime k (see, e.g., Table 12.1).

Armed with the counting process M<sup>±</sup>for MOs, their intensities >.. <sup>±</sup> , the Markov chain driving order imbalance regimes *Z,* and the sequence of i.i.d. random variables for mid price jumps *ct) ,* we can now state a candidate model for the midprice *S* which is driven by order imbalance:

$$dS_t = \varepsilon_{M_{t^-}^+, Z_{t^-}} dM_t^+ - \varepsilon_{M_{t^-}^-, Z_{t^-}} dM_t^-$$

The random variables *ct)* are subordinated by the left-limit of the corresponding processes - this is a technical condition required to ensure that stochastic integrals with respect to the compensated counting processes are still martingales, and is the reason we indexed the random variables *ct)* beginning from O rather than l. Intuitively, the above model says that the midprice jumps the instant an MO arrives, and the rate of arrival of the orders and the distribution of the jump are regime dependent.

The model above is missing one more ingredient, which is to include the midprice changes that we observe between MO arrivals. Thus, we modify the above to include exogenous jumps which result from, e.g., additions and cancellations in the  $LOB$ :

$$dS_t = \varepsilon_{M^+_{t-}, Z^-_{t-}} dM^+_t - \varepsilon_{M^-_{t-}, Z^-_{t-}} dM^-_t + \eta_{J^+_{t-}, Z^-_{t-}} dJ^+_t - \eta_{J^-_{t-}, Z^-_{t-}} dJ^-_t.$$

Here,  $\{\eta_{0,k}^+, \eta_{1,k}^+, \dots\}$  denote i.i.d. random variables with distribution function  $L_k^+$ , and  $\{\eta_{0,k}^-, \eta_{1,k}^-, \dots\}$  denote i.i.d. random variables with distribution function  $L_{k}^{-}$ , for  $k=-1,0,1,$  and all random variables are mutually independent. These random variables generate jumps in the midprice between the arrival of MOs, due to other agents posting and cancelling orders in the LOB, and these changes can in principle be dependent on the order imbalance regime. For example, when order imbalance is buy-heavy, agents may pull their orders from the sell side of the LOB and place them in the buy side, resulting in a general upward pressure on the midprice. Reshuffling of orders generally occurs at a higher frequency than the arrival of MOs themselves.

#### 12.4.1 Optimisation Problem

Up to this point, we have specified the joint model for order imbalance, arrival of MOs, and midprice movements. Here, we pose and solve the agent's optimisation problem subject to this modelling assumption. First, the agent continues to trade until the stopping time

$$\tau = T \wedge \min\{t \,:\, Q_t^{\delta} = 0\},\,$$

i.e. the minimum of  $T$  or the first time that the inventory hits zero, because then no more trading is necessary. The agent's performance criteria is essentially the same as in Chapter  $6$ , and is given by

$$H^{\delta}(t,x,S,z,q) = \mathbb{E}_{t,x,S,z,q} \left[ X^{\delta}_{\tau} + Q^{\delta}_{\tau} \left( S_{\tau} - \alpha Q^{\delta}_{\tau} \right) - \phi \int_{t}^{\tau} \left( Q^{\delta}_{s} \right)^{2} ds \right], \quad (12.8)$$

where the notation  $\mathbb{E}_{t,x,S,z,q}[\cdot]$  represents expectation conditional on  $X_{t^-}^{\delta} = x$ ,  $S_{t^-} = S$ ,  $Z_{t^-} = z$  and  $Q_{t^-}^{\delta} = q$ . As usual, her value function is the one which maximises this performance criteria, over all admissible strategies  $\mathcal{A}$ , taken to be the set of  $\mathcal{F}$ -predictable, bounded from below, processes, so that

$$H(t, x, S, z, q) = \sup_{\delta \in \mathcal{A}} H^{\delta}(t, x, S, z, q) .$$

Applying the dynamic programming principle, we expect the value function to

satisfy the dynamic programming equation (using  $(t, \cdot)$  to denote  $(t, x, S, z, q)$ ):

$$\begin{split} \phi \, q^2 &= \partial_t H + \lambda^+(z) \sup_{\delta} \left\{ \, e^{-\kappa \delta} \, \mathbb{E}[H(t,x+(S+\delta),S+\varepsilon^+_{0,z},z,q-1) - H(t,\cdot)] \, \right. \\ &+ \left. (1-e^{-\kappa \delta}) \, \mathbb{E}[H(t,x,S+\varepsilon^+_{0,z},z,q) - H(t,\cdot)] \, \right\} \\ &+ \lambda^-(z) \, \mathbb{E}[H(t,x,S-\varepsilon^-_{0,z},z,q) - H(t,\cdot)] \\ &+ \eta^+(z) \, \mathbb{E}[H(t,x,S+\eta^+_{0,z},z,q) - H(t,\cdot)] \\ &+ \eta^-(z) \, \mathbb{E}[H(t,x,S-\eta^-_{0,z},z,q) - H(t,\cdot)] \\ &+ \sum_{k=-1,0,1} G_{z,k} \, [H(t,x,S,k,q) - H(t,\cdot)] \, , \end{split}$$

where the expectations are over the random variables  $\varepsilon_{0,z}^{\pm}$  and  $\eta_{0,z}^{\pm}$ , and the boundary and terminal conditions are

 $H(t, x, S, z, 0) = x$ , and  $H(T, x, S, z, q) = x + q(S - \alpha q)$ .

The various terms in the equation have the interpretations given below.

- (i) The left-hand side of the first line contains the running penalty the agent has from holding inventory different from zero.
- (ii) The supremum takes into account the agent's ability to control the depth at which she posts her LOs.
- (iii) The term  $\lambda^+(z) e^{-\kappa \delta}$  represents the rate of arrival of MOs which fill the agent's posted LO at price  $S + \delta$ .
- (iv) The expectation in the first line represents the expected change in the valuation when a buy MO arrives which fills the agent's post. The agent's wealth increases by  $S + \delta$ , her inventory decreases by 1 and the midprice jumps.
- (v) The term  $\lambda^+(z) (1 e^{-\kappa \delta})$  represents the rate of arrival of buy MOs which do not fill the agents posted LO, but still induce a jump in midprice.
- (vi) The expectation in the second line represents the expected change in the valuation when a buy MO arrives which does not fill the agent's post but causes a jump in midprice.
- (vii) The third line represents the expected change in the value function when a sell MO arrives and the midprice jumps.
- (viii) The fourth and fifth lines represent the expected change in the value function when the midprice jumps due to posts and cancellations in the LOB (i.e. between MO arrivals).
  - (ix) The last line represents the change in value function when the order imbalance switches regimes.

As seen several times, the terminal and boundary conditions suggest the ansatz

$$H(t, x, S, z, q) = x + q S + h(t, z, q), \quad h(T, z, q) = -\alpha q^2, \quad h(t, z, 0) = 0,$$

so that the term  $x+qS$  is the book value of the agent's inventory and cash, while

*h* represents the excess value that optimal trading generates. Upon substituting this ansatz we find that h satisfies the coupled system of PDEs

$$0 = \partial_t h(t, z, q) + \mu(z) q - \phi q^2$$
  
+ 
$$\sup_{\delta} \left\{ \lambda^+(z) e^{-\kappa \delta} \left( \delta + h(t, z, q-1) - h(t, z, q) \right) \right\}$$
  
+ 
$$\sum_{k=-1, 0, 1} G_{z, k} \left[ h(t, k, q) - h(t, z, q) \right], \qquad (12.9)$$

where

$$\mu(z) = \lambda^+(z) \,\mathbb{E}[\varepsilon_{0,z}^+] - \lambda^-(z) \,\mathbb{E}[\varepsilon_{0,z}^-] + \eta^+(z) \,\mathbb{E}[\eta_{0,z}^+] - \eta^-(z) \,\mathbb{E}[\eta_{0,z}^-] \,,$$

is the expected drift of the midprice while the order imbalance is in regime *z.* The first two lines of this equation are of the same form as that of the liquidation problem when there are no regime changes and the midprice is a drifted Brownian motion. The third line represents the jumps between the order imbalance regimes. It is somewhat surprising how this rather rich model reduces to something intuitively simple.

The first order conditions provides us with the optimal depth as

$$\delta^*(t,q,z) = \frac{1}{\kappa} - \Delta h(t,z,q) \,,$$

where

$$\Delta h(t, z, q) = h(t, z, q) - h(t, z, q - 1),$$

and upon substituting this feedback form into the previous equation, we find that h satisfies the equation

$$0 = \partial_t h(t, z, q) + \mu(z) q - \phi q^2 + \lambda^+(z) \frac{1}{\kappa} e^{-\kappa \left(\frac{1}{\kappa} - \Delta h(t, z, q)\right)} + \sum_{k=-1, 0, 1} G_{z, k} \left[ h(t, k, q) - h(t, z, q) \right]. \tag{12.10}$$

The above coupled system of non-linear ODEs does not appear to have a simple analytic solution and one must resort to a numerical scheme such as finite differences.

The above optimal depth may become negative. One interpretation of a negative depth is that it represents executing an MO. This interpretation is purely heuristic and is not accounted for in the model. To properly account for executing MOs, we would have to pose the problem as a sequence of stopping problems similar to what we have done in Section 8.4. An alternative is to pose the problem as a constrained optimisation problem and modify the admissible set A to nonnegative F-predictable processes. The resulting DPE will receive a modification on the optimisation set, so that (12.9) becomes

$$0 = \partial_t h(t, z, q) + \mu(z) q - \phi q^2$$
  
+ 
$$\sup_{\delta \ge 0} \left\{ \lambda^+(z) e^{-\kappa \delta} \left( \delta + h(t, z, q-1) - h(t, z, q) \right) \right\}$$
  
+ 
$$\sum_{k=-1, 0, 1} G_{z, k} \left[ h(t, k, q) - h(t, z, q) \right].$$

![](_page_16_Figure_1.jpeg)

Figure 12.6 (a) The optimal depth to post for the sell-heavy (solid lines) and buy-heavy (dashed lines) regimes as a function of time and inventory. (b) The mean, median,  $5\%$  and  $95\%$  quantiles of inventory through time from  $10,000$  simulations.

Hence, the optimal depth is modified to

$$\delta^*(t,q,z) = \max\left(\frac{1}{\kappa} - \Delta h(t,z,q) \; ; \; 0\right). \tag{12.11}$$

Upon substitution of this feedback control into the DPE, we have

$$0 = \partial_{t}h + \mu(z) q - \phi q^{2}$$
  
+  $\lambda^{+}(z) \left\{ \Delta h(t,q,z) \mathbb{1}_{\Delta h(t,q,z) \geq \frac{1}{\kappa}} + \frac{e^{-\kappa(\frac{1}{\kappa} - \Delta h(t,z,q))}}{\kappa} \mathbb{1}_{\Delta h(t,q,z) < \frac{1}{\kappa}} \right\}$   
+  $\sum_{k=-1,0,1} G_{z,k} \left[ h(t,k,q) - h(t,z,q) \right].$  (12.12)

## Simulations

In this section, we perform simulations using the estimated parameters provided in Table 12.1 and  $(12.7)$ . For simplicity we do not model the movements of the LOB between MO events. Note that the invariant distribution of the Markov chain with generator matrix in  $(12.7)$  is

 $[0.0196 \ 0.1548 \ 0.3577 \ 0.3534 \ 0.1160]$ 

and from Table 12.1 we find that the invariant arrival of buy MOs is  $0.0727$  per second. In the experiments below, we use  $T = 300 \text{sec}$  and  $\mathfrak{N} = 4$  so that the trader is liquidating approximately 20 percent of the buy MO flow – which has the potential to lift her posted sell LOs. Finally, we use the following remaining parameters:

 $S_0 = 33.61,$   $\alpha = 0.01,$   $\kappa = 100,$   $\phi = 10^{-5}.$ 

We numerically solve the constrained equation  $(12.12)$  for h and then compute the optimal depth  $\delta^*$  in (12.11). Figure 12.6(a) shows the optimal depth the agent 312

![](_page_17_Figure_1.jpeg)

Figure 12.7 Sample path of the optimal strategy showing price, market buy and sell arrivals, inventory path, optimal depth and order imbalance regime.

posts for the sell-heavy (solid lines) and buy-heavy (dashed lines) regimes as a function of time and inventory. In the buy-heavy regime, the agent posts deeper in the LOB in order to capture the expected upward tendency that prices have in this regime, and hence avoids being adversely selected. Similarly, in the sellheavy regime, the agent posts closer to the midprice since she expects prices to have a downward pressure and would rather capture the current price than wait for prices to fall. Moreover, as the agent liquidates her position, she posts deeper in the LOB. Panel (b) of Figure 12.6 shows the mean, median, 5 and 95 percent quantiles of the inventory paths when the agent follows the optimal strategy.

To gain a better sense of how the strategy behaves, in Figure  $12.7$  we show a single sample path of the strategy. Panel (a) shows the midprice path (black line) and the optimal offer posting (green line) which reacts to the changes in the regimes shown in panel (d) as can be seen more clearly in the optimal depth shown in panel (c). In this case, the depth, and therefore the posting, reacts to the agent's remaining inventory which we have shown in panel (c) together with the mean inventory path. In panel (a) we also show the arrival of market sell orders (open red circles), which naturally are never matched with the agent's

posted offers, and market buy orders (blue circles) which are filled if that specific order lifted the agent's offer.

# **12.5 Bibliography and Selected Readings**

Bechler & Ludkovski (2014), Lipton, Pesavento & Sotiropoulos (2013), Cebiroglu & Horst (2015), Zheng, Moulines & Abergel (2012).

# **12.6 Exercises**

- E.12.1 Modify the setup developed in Section 12.4 for optimal liquidation using LOs only in the following cases:
  - (a) the agent optimally executes MOs only,
  - (b) the agent optimally executes MOs and optimally decides the depth at which to place LOs,
  - ( c) the agent optimally places LOs only at-the-touch,
  - ( d) the agent optimally places LOs only at-the-touch and optimally decides when to execute MOs.
- E.12.2 Extend the analysis in Section 12.4 to the case when the agent is a market maker and decides whether to post buy and sell LOs.
# PART 3

# Backtesting

- 1. <u>Chapter 10 Bet Sizing</u>
- 2. <u>Chapter 11 The Dangers of Backtesting</u>
- 3. <u>Chapter 12 Backtesting through Cross-Validation</u>
- 4. <u>Chapter 13 Backtesting on Synthetic Data</u>
- 5. Chapter 14 Backtest Statistics
- 6. Chapter 15 Understanding Strategy Risk
- 7. Chapter 16 Machine Learning Asset Allocation

# <span id="page-0-0"></span>CHAPTER 10

# **Bet Sizing**

# 10.1 Motivation

There are fascinating parallels between strategy games and investing. Some of the best portfolio managers I have worked with are excellent poker players, perhaps more so than chess players. One reason is bet sizing, for which Texas Hold'em provides a great analogue and training ground. Your ML algorithm can achieve high accuracy, but if you do not size your bets properly, your investment strategy will inevitably lose money. In this chapter we will review a few approaches to size bets from ML predictions.

## **10.2 Strategy-Independent Bet Sizing Approaches**

Consider two strategies on the same instrument. Let  $m_{i,t} \in [-1, 1]$  be the bet size of strategy *i* at time *t* , where  $m_{i,t} = -1$  indicates a full short position and  $m_{i,t}$  = 1 indicates a full long position. Suppose that one strategy produced a sequence of bet sizes [ $m_{1,1}, m_{1,2}, m_{1,3}$ ] = [.5, 1, 0], as the market price followed a sequence  $[p_1, p_2, p_3] = [1, .5, 1.25]$ , where  $p_t$  is the price at time *t*. The other strategy produced a sequence  $[m_{2,1}, m_{2,2}, m_{2,3}] = [1, .5, 0]$ , as it was forced to reduce its bet size once the market moved against the initial full position. Both strategies produced forecasts that turned out to be correct

(the price increased by 25% between *p <sup>1</sup>* and *p <sup>3</sup>* ), however the first strategy made money (0.5) while the second strategy lost money (−.125).

We would prefer to size positions in such way that we reserve some cash for the possibility that the trading signal strengthens before it weakens. One option is to compute the series *c <sup>t</sup>* = *c <sup>t</sup> , <sup>l</sup>* − *c <sup>t</sup> ,s* , where *c <sup>t</sup> , <sup>l</sup>* is the number of concurrent long bets at time *t* , and *c <sup>t</sup> ,s* is the number of concurrent short bets at time *t.* This bet concurrency is derived, for each side, similarly to how we computed label concurrency in Chapter 4 (recall the t1 object, with overlapping time spans). We fit a mixture of two Gaussians on { *c <sup>t</sup>* }, applying a method like the one described in López de Prado and Foreman [2014]. Then, the bet size is derived as

$$m_{t} = \begin{cases} \frac{F[c_{t}] - F[0]}{1 - F[0]} & \text{if } c_{t} \ge 0\\ \frac{F[c_{t}] - F[0]}{F[0]} & \text{if } c_{t} < 0 \end{cases}$$

where *F* [ *x* ] is the CDF of the fitted mixture of two Gaussians for a value *x* . For example, we could size the bet as 0.9 when the probability of observing a signal of greater value is only 0.1. The stronger the signal, the smaller the probability that the signal becomes even stronger, hence the greater the bet size.

A second solution is to follow a budgeting approach. We compute the maximum number (or some other quantile) of concurrent long bets, , and the maximum number of concurrent short bets, . Then we derive the bet size as , where *c <sup>t</sup> , <sup>l</sup>* is the number of concurrent long bets at time *t* , and *c <sup>t</sup> ,s* is the number of concurrent short bets at time *t.* The goal is that the maximum position is not reached before the last concurrent signal is triggered.

A third approach is to apply meta-labeling, as we explained in Chapter 3. We fit a classifier, such as an SVC or RF, to determine the probability of misclassification, and use that probability to derive the bet size. <sup>1</sup> This approach has a couple of advantages: First, the ML algorithm that decides the bet sizes is independent of the primary model, allowing for the incorporation of features predictive of false positives (see Chapter 3). Second, the predicted probability can be directly translated into bet size. Let us see how.

## **10.3 Bet Sizing from Predicted Probabilities**

Let us denote *p* [ *x* ] the probability that label *x* takes place. For two possible outcomes, *x* ∈ { − 1, 1}, we would like to test the null hypothesis . We compute the test statistic , with *z* ∈ ( − ∞, +∞) and where *Z* represents the standard Normal distribution. We derive the bet size as *m* = 2 *Z* [ *z* ] − 1, where *m* ∈ [ − 1, 1] and *Z* [.] is the CDF of *Z* .

For more than two possible outcomes, we follow a one-versus-rest method. Let *X* = { − 1, …, 0, …, 1} be various labels associated with bet sizes, and *x* ∈ *X* the predicted label. In other words, the label is identified by the bet size associated with it. For each label *i* = 1, …, || *X* ||, we estimate a probability *p <sup>i</sup>* , with *.* We define as the probability of *x* , and we would like to test for . <sup>2</sup> We compute the test statistic

$$z = \frac{\bar{p} - \frac{1}{\|X\|}}{\sqrt{\bar{p}(1-\bar{p})}} \sim Z \text{, with } z \in [0., . + \infty). \text{ We derive the bet size as}$$
$$m = x(2Z[z] - 1)$$
$$\in [0,1] \text{, where } m \in [-1, 1] \text{ and } Z[z] \text{ regulates the size for a prediction } x \text{ (where the side is implied by } x \text{ ).}$$

Figure 10.1 plots the bet size as a function of test statistic. Snippet 10.1 implements the translation from probabilities to bet size. It handles the possibility that the prediction comes from a meta-labeling estimator, as well

from a standard labeling estimator. In step #2, it also averages active bets, and discretizes the final value, which we will explain in the following sections.

![](_page_3_Figure_0.jpeg)

**Figure 10.1** Bet size from predicted probabilities

#### **SNIPPET 10.1 FROM PROBABILITIES TO BET SIZE**

## **10.4 Averaging Active Bets**

Every bet is associated with a holding period, spanning from the time it originated to the time the first barrier is touched, t1 (see Chapter 3). One possible approach is to override an old bet as a new bet arrives; however, that is likely to lead to excessive turnover. A more sensible approach is to average all sizes across all bets still active at a given point in time. Snippet 10.2 illustrates one possible implementation of this idea.

## **SNIPPET 10.2 BETS ARE AVERAGED AS LONG AS THEY ARE STILL ACTIVE**

## **10.5 Size Discretization**

<span id="page-5-1"></span>Averaging reduces some of the excess turnover, but still it is likely that small trades will be triggered with every prediction. As this jitter would cause unnecessary overtrading, I suggest you discretize the bet size as , where *d* ∈ (0, ..1] determines the degree of discretization. [Figure 10.2](#page-5-0) illustrates the discretization of the bet size. Snippet 10.3 implements this notion.

![](_page_5_Figure_1.jpeg)

<span id="page-5-0"></span>**[Figure 10.2](#page-5-1)** Discretization of the bet size, d = 0.2

#### **SNIPPET 10.3 SIZE DISCRETIZATION TO PREVENT OVERTRADING**

### **10.6 Dynamic Bet Sizes and Limit Prices**

Recall the triple-barrier labeling method presented in Chapter 3. Bar *i* is formed at time *t i , 0* , at which point we forecast the first barrier that will be touched. That prediction implies a forecasted price, , consistent with the barriers' settings. In the period elapsed until the outcome takes place, *t* ∈ [ *t i , 0* , *t i , 1* ], the price *p <sup>t</sup>* fluctuates and additional forecasts may be formed, , where *j* ∈ [ *i* + 1, *I* ] and *t <sup>j</sup> , <sup>0</sup>* ≤ *t i , 1* . In Sections 10.4 and 10.5 we discussed methods for averaging the active bets and discretizing the bet size as new forecasts are formed. In this section we will introduce an approach to adjust bet sizes as market price *p <sup>t</sup>* and forecast price *f i* fluctuate. In the process, we will derive the order's limit price.

Let *q <sup>t</sup>* be the current position, *Q* the maximum absolute position size, and the target position size associated with forecast *f i* , such that

$$\hat{q}_{i,t} = \text{int}[m[\omega, f_i - p_t]Q]$$
$$m[\omega, x] = \frac{x}{\sqrt{\omega + x^2}}$$

where *m* [ω, *x* ] is the bet size, *x* = *f <sup>i</sup>* − *p <sup>t</sup>* is the divergence between the current market price and the forecast, ω is a coefficient that regulates the width of the sigmoid function, and Int[ *x* ] is the integer value of *x* . Note that for a realvalued price divergence *x* , − 1 < *m* [ω, *x* ] < 1, the integer value is bounded .

The target position size can be dynamically adjusted as *p <sup>t</sup>* changes. In particular, as *p <sup>t</sup>* → *f <sup>i</sup>* we get , because the algorithm wants to realize the gains. This implies a breakeven limit price for the order size , to avoid realizing losses. In particular,

$$\bar{p} = \frac{1}{|\hat{q}_{i,t} - q_t|} \sum_{j=|q_t + \text{sgn}[\hat{q}_{i,t} - q_t]|}^{|\hat{q}_{i,t}|} L\left[f_i, \omega, \frac{j}{Q}\right]$$

where *L* [ *f i* , ω, *m* ] is the inverse function of *m* [ω, *f <sup>i</sup>* − *p <sup>t</sup>* ] with respect to *p <sup>t</sup>* ,

$$L[f_i, \omega, m] = f_i - m \sqrt{\frac{\omega}{1 - m^2}}$$

We do not need to worry about the case *m <sup>2</sup>* = 1, because *.* Since this function is monotonic, the algorithm cannot realize losses as *p <sup>t</sup>* → *f i* .

Let us calibrate ω. Given a user-defined pair ( *x* , *m* \*), such that *x* = *f <sup>i</sup>* − *p <sup>t</sup>* and *m* \* = *m* [ω, *x* ], the inverse function of *m* [ω, *x* ] with respect to ω is

$$\omega = x^2 (m^{*2} - 1)$$

Snippet 10.4 implements the algorithm that computes the dynamic position size and limit prices as a function of *p <sup>t</sup>* and *f i* . First, we calibrate the sigmoid function, so that it returns a bet size of *m* \* = .95 for a price divergence of *x* = 10 *.* Second, we compute the target position for a maximum position *Q* = 100, *f <sup>i</sup>* = 115 and *p <sup>t</sup>* = 100 *.* If you try *f <sup>i</sup>* = 110, you will get , consistent with the calibration of ω. Third, the limit price for this order of size is *p <sup>t</sup>* < 112.3657 < *f i* , which is between the current price and the forecasted price.

#### **SNIPPET 10.4 DYNAMIC POSITION SIZE AND LIMIT PRICE**

As an alternative to the sigmoid function, we could have used a power function , where ω ≥ 0, *x* ∈ [ − 1, 1], which results in . This alternative presents the advantages that:

- .
- Curvature can be directly manipulated through ω.
- For ω > 1, the function goes from concave to convex, rather than the other way around, hence the function is almost flat around the inflexion point.

<span id="page-9-1"></span>We leave the derivation of the equations for a power function as an exercise. [Figure 10.3](#page-9-0) plots the bet sizes (y-axis) as a function of price divergence *f* − *p <sup>t</sup>* (x-axis) for both the sigmoid and power functions.

![](_page_9_Figure_4.jpeg)

<span id="page-9-0"></span>**[Figure 10.3](#page-9-1)** *f* [*x* ] = *sgn* [*x* ]|*x* | 2 (concave to convex) and *f* [*x* ] = *x* (.1 + *x 2* ) − .5 (convex to concave)

## **Exercises**

1. Using the formulation in Section 10.3, plot the bet size ( *m* ) as a function of the maximum predicted probability ( when || *X* || = 2, 3, …, 10.

- 2. Draw 10,000 random numbers from a uniform distribution with bounds *U* [.5, 1.].
  - 1. Compute the bet sizes *m* for ||*X* || = 2*.*
  - 2. Assign 10,000 consecutive calendar days to the bet sizes.
  - 3. Draw 10,000 random numbers from a uniform distribution with bounds *U* [1, 25].
  - 4. Form a pandas series indexed by the dates in 2.b, and with values equal to the index shifted forward the number of days in 2.c. This is a t1 object similar to the ones we used in Chapter 3.
  - 5. Compute the resulting average active bets, following Section 10.4.
- 3. Using the t1 object from exercise 2.d:
  - 1. Determine the maximum number of concurrent long bets, .
  - 2. Determine the maximum number of concurrent short bets, .
  - 3. Derive the bet size as , where *c <sup>t</sup> , <sup>l</sup>* is the number of concurrent long bets at time *t* , and *c <sup>t</sup> ,s* is the number of concurrent short bets at time *t.*
- 4. Using the t1 object from exercise 2.d:
  - 1. Compute the series *c <sup>t</sup>* = *c <sup>t</sup> , <sup>l</sup>* − *c <sup>t</sup> ,s* , where *c <sup>t</sup> , <sup>l</sup>* is the number of concurrent long bets at time *t* , and *c <sup>t</sup> ,s* is the number of concurrent short bets at time *t.*
  - 2. Fit a mixture of two Gaussians on {*c <sup>t</sup>* }. You may want to use the method described in López de Prado and Foreman [2014].

3. Derive the bet size as 
$$m_t = \begin{cases} \frac{F[c_t] - F[0]}{1 - F[0]} & \text{if } c_t \ge 0\\ \frac{F[c_t] - F[0]}{F[0]} & \text{if } c_t < 0 \end{cases}$$
, where  $F[x]$  is the

CDF of the fitted mixture of two Gaussians for a value *x* .

- 4. Explain how this series {*m <sup>t</sup>* } differ from the bet size series computed in exercise 3.
- 5. Repeat exercise 1, where you discretize *m* with a stepSize=.01 , stepSize=.05 , and stepSize=.1 .
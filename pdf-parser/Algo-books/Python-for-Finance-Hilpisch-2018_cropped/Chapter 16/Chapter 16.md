# **Chapter 16. Automated Trading**

People worry that computers will get too smart and take over the world, but the real problem is that they're too stupid and they've already taken over the world.

Pedro Domingos

"Now what?" one might think. A trading platform is available that allows one to retrieve historical data and streaming data, to place buy and sell orders, and to check the account status. A number of different methods have been introduced to derive algorithmic trading strategies by predicting the direction of market price movements. How can this all be put together to work in automated fashion? This question cannot be answered in any generality. However, this chapter addresses a number of topics that are important in this context. The chapter assumes that a single automated algorithmic trading strategy only shall be deployed. This simplifies, among others, aspects like capital and risk management.

The chapter covers the following topics:

# *"Capital Management"*

As this section demonstrates, depending on the strategy characteristics and the trading capital available, the Kelly criterion helps with sizing the trades.

# *"ML-Based Trading Strategy"*

To gain confidence in an algorithmic trading strategy, the strategy needs to be backtested thoroughly both with regard to performance and risk characteristics; the example strategy used is based on a classification algorithm from machine learning as introduced in Chapter 15.

# *"Online Algorithm"*

To deploy the algorithmic trading strategy for automated trading, it needs to be translated into an online algorithm that works with incoming streaming data in real time.

# *"Infrastructure and Deployment"*

To run automated algorithmic trading strategies robustly and reliably, deployment in the cloud is the preferred option from an availability,

deployment in the cloud is the preferred option from an availability, performance, and security point of view.

### *"Logging and Monitoring"*

To be able to analyze the history and certain events during the deployment of an automated trading strategy, logging plays an important role; monitoring via socket communication allows one to observe events (remotely) in real time.

# **Capital Management**

A central question in algorithmic trading is how much capital to deploy to a given algorithmic trading strategy given the total available capital. The answer to this question depends on the main goal one is trying to achieve by algorithmic trading. Most individuals and financial institutions will agree that the *maximization of long-term wealth* is a good candidate objective. This is what Edward Thorpe had in mind when he derived the *Kelly criterion* for investing, as described in the paper by Rotando and Thorp (1992).

# **The Kelly Criterion in a Binomial Setting**

The common way of introducing the theory of the Kelly criterion for investing is on the basis of a coin tossing game, or more generally a binomial setting (where only two outcomes are possible). This section follows that route. Assume a gambler is playing a coin tossing game against an infinitely rich bank or casino.

Assume further that the probability for heads is some value *p* for which < *p* < 1 holds. Probability for tails is defined by < . The gambler can place bets *b* > 0 of arbitrary size, whereby the gambler wins the same amount if right and loses it all if wrong. Given the assumptions about the probabilities, the gambler would of course want to bet on heads. Therefore, the expected value for this betting game (i.e., the random variable representing this game) in a oneshot setting is:

A risk-neutral gambler with unlimited funds would like to bet as large an amount as possible since this would maximize the expected payoff. However, trading in financial markets is not a one-shot game in general. It is a repeated one. Therefore, assume that represents the amount that is bet on day *i* and that represents the initial capital. The capital at the end of day one depends on the betting success on that day and might be either or . The expected value for a gamble that is repeated *n* times then is:

$$\mathbf{E}[B^n] = c_0 + \sum_{i=1}^n (p-q) \cdot b_i$$

In classical economic theory, with risk-neutral, expected utility-maximizing agents, a gambler would try to maximize this expression. It is easily seen that it is maximized by betting all available funds — i.e., — like in the oneshot scenario. However, this in turn implies that a single loss will wipe out all

available funds and will lead to ruin (unless unlimited borrowing is possible). Therefore, this strategy does not lead to a maximization of long-term wealth.

While betting the maximum capital available might lead to sudden ruin, betting nothing at all avoids any kind of loss but does not benefit from the advantageous gamble either. This is where the Kelly criterion comes into play, since it derives

the *optimal fraction* of the available capital to bet per round of betting. Assume that *n* = *h* + *t*, where *h* stands for the number of heads observed during *n* rounds of betting and where *t* stands for the number of tails. With these definitions, the available capital after *n* rounds is:

$$c_n = c_0 \cdot (1+f)^h \cdot (1-f)^t$$

In such a context, long-term wealth maximization boils down to maximizing the average geometric growth rate per bet, which is given as:

$$r^{g} = \log \left(\frac{c_{n}}{c_{0}}\right)^{1/n}$$
  
=  $\log \left(\frac{c_{0} \cdot (1+f)^{h} \cdot (1-f)^{t}}{c_{0}}\right)^{1/n}$   
=  $\log \left((1+f)^{h} \cdot (1-f)^{t}\right)^{1/n}$   
=  $\frac{h}{n} \log (1+f) + \frac{t}{n} \log (1-f)$ 

The problem then formally is to maximize the *expected* average rate of growth by choosing *f* optimally. With and , one gets:

$$\mathbf{E}[r^g] = \mathbf{E}\left[\frac{h}{n}\log\left(1+f\right) + \frac{t}{n}\log\left(1-f\right)\right]$$
  
= 
$$\mathbf{E}\left[p\log\left(1+f\right) + q\log\left(1-f\right)\right]$$
  
= 
$$p\log\left(1+f\right) + q\log\left(1-f\right)$$
  
= 
$$G(f)$$

One can now maximize the term by choosing the optimal fraction according to the first-order condition. The first derivative is given by:

![](_page_5_Figure_2.jpeg)

From the first-order condition, one gets:

G ' ( f ) = ! 0 ⇒ f \* = p - q

If one trusts this to be the maximum (and not the minimum), this result implies that it is optimal to invest a fraction *f* \* = *p* - *q* per round of betting. With, for example, *p* = 0.55 one has *f* \* = 0.55 - 0.45 = 0.1, indicating that the optimal fraction is 10%.

The following Python code formalizes these concepts and results through

The following Python code formalizes these concepts and results through simulation. First, some imports and configurations:

```
In [1]: import math
        import time
        import numpy as np
        import pandas as pd
        import datetime as dt
        import cufflinks as cf
        from pylab import plt
In [2]: np.random.seed(1000)
        plt.style.use('seaborn')
        %matplotlib inline
```

The idea is to simulate, for example, 50 series with 100 coin tosses per series. The Python code for this is straightforward:

```
In [3]: p = 0.55
In [4]: f = p - (1 - p)
In [5]: f
Out[5]: 0.10000000000000009
In [6]: I = 50
In [7]: n = 100
```

Fixes the probability for heads.

Calculates the optimal fraction according to the Kelly criterion.

The number of series to be simulated.

The number of trials per series.

The major part is the Python function run\_simulation(), which achieves the simulation according to the prior assumptions. Figure 16-1 shows the simulation results:

```
In [8]: def run_simulation(f):
            c = np.zeros((n, I))
            c[0] = 100
            for i in range(I):
                for t in range(1, n):
```

```
o = np.random.binomial(1, p)
                   if o > 0:
                       c[t, i] = (1 + f) * c[t - 1, i]
                   else:
                       c[t, i] = (1 - f) * c[t - 1, i]
           return c
In [9]: c_1 = run_simulation(f)
In [10]: c_1.round(2)
Out[10]: array([[100. , 100. , 100. , ..., 100. , 100. , 100. ],
               [ 90. , 110. , 90. , ..., 110. , 90. , 110. ],
               [ 99. , 121. , 99. , ..., 121. , 81. , 121. ],
               ...,
               [226.35, 338.13, 413.27, ..., 123.97, 123.97, 123.97],
               [248.99, 371.94, 454.6 , ..., 136.37, 136.37, 136.37],
               [273.89, 409.14, 409.14, ..., 122.73, 150.01, 122.73]])
In [11]: plt.figure(figsize=(10, 6))
        plt.plot(c_1, 'b', lw=0.5)
        plt.plot(c_1.mean(axis=1), 'r', lw=2.5);
  Instantiates an ndarray object to store the simulation results.
  Initializes the starting capital with 100.
  Outer loop for the series simulations.
  Inner loop for the series itself.
  Simulates the tossing of a coin.
  If 1, i.e., heads …
  … then add the win to the capital.
  If 0, i.e., tails …
  … then subtract the loss from the capital.
  Runs the simulation.
```

Plots all 50 series.

Plots the average over all 50 series.

![](_page_8_Figure_4.jpeg)

The following code repeats the simulation for different values of *f*. As shown in Figure 16-2, a lower fraction leads to a lower growth rate on average. Higher values might lead to a higher average capital at the end of the simulation (*f* = 0.25) or to a much lower average capital (*f* = 0.5). In both cases where the fraction *f* is higher, the volatility increases considerably:

```
In [12]: c_2 = run_simulation(0.05)
In [13]: c_3 = run_simulation(0.25)
In [14]: c_4 = run_simulation(0.5)
In [15]: plt.figure(figsize=(10, 6))
         plt.plot(c_1.mean(axis=1), 'r', label='$f^*=0.1$')
         plt.plot(c_2.mean(axis=1), 'b', label='$f=0.05$')
         plt.plot(c_3.mean(axis=1), 'y', label='$f=0.25$')
         plt.plot(c_4.mean(axis=1), 'm', label='$f=0.5$')
         plt.legend(loc=0);
```

Simulation with *f* = 0.05.

Simulation with *f* = 0.25.

Simulation with *f* = 0.5.

![](_page_9_Figure_6.jpeg)

*Figure 16-2. Average capital over time for different fractions*

# **The Kelly Criterion for Stocks and Indices**

Assume now a stock market setting in which the relevant stock (index) can take on only two values after a period of one year from today, given its known value today. The setting is again binomial, but this time a bit closer on the modeling side to stock market realities. <sup>1</sup> Specifically, assume that:

$$P(r^{S} = \mu + \sigma) = P(r^{S} = \mu - \sigma) = \frac{1}{2}$$

with being the expected return of the stock over one year and being the standard deviation of returns (volatility). In a one-period setting, one gets for the available capital after one year (with and *f* defined as before):

$$c(f) = c_0 \cdot (1 + (1 - f) \cdot r + f \cdot r^S)$$

Here, *r* is the constant short rate earned on cash not invested in the stock. Maximizing the geometric growth rate means maximizing the term:

$$G(f) = \mathbf{E} \big[ \log \frac{c(f)}{c_0} \big]$$

Assume now that there are *n* relevant trading days in the year so that for each such trading day *i*:

$$P(r_i^S = \frac{\mu}{n} + \frac{\sigma}{\sqrt{n}}) = P(r_i^S = \frac{\mu}{n} - \frac{\sigma}{\sqrt{n}}) = \frac{1}{2}$$

Note that volatility scales with the square root of the number of trading days. Under these assumptions, the daily values scale up to the yearly ones from before and one gets:

$$c_n(f) = c_0 \cdot \prod_{i=1}^n (1 + (1 - f) \cdot \frac{r}{n} + f \cdot r_i^S)$$

One now has to maximize the following quantity to achieve maximum long-term wealth when investing in the stock:

$$\begin{array}{rcl} G_n(f) &=& \mathbf{E}\big[\log\frac{c_n(f)}{c_0}\big] \\ &=& \mathbf{E}\big[\sum_{i=1}^n\log\left(1+(1-f)\cdot\frac{r}{n}+f\cdot r_i^S\right)\big] \\ &=& \frac{1}{2}\sum_{i=1}^n\log\left(1+(1-f)\cdot\frac{r}{n}+f\cdot\left(\frac{\mu}{n}+\frac{\sigma}{\sqrt{n}}\right)\right) \\ &+& \log\left(1+(1-f)\cdot\frac{r}{n}+f\cdot\left(\frac{\mu}{n}-\frac{\sigma}{\sqrt{n}}\right)\right) \\ &=& \frac{n}{2}\log\left((1+(1-f)\cdot\frac{r}{n}+f\cdot\frac{\mu}{n})^2-\frac{f^2\sigma^2}{n}\right) \end{array}$$

Using a Taylor series expansion, one finally arrives at:

$$G_n(f) = r + (\mu - r) \cdot f - \frac{\sigma^2}{2} \cdot f^2 + \mathcal{O}\left(\frac{1}{\sqrt{n}}\right)$$

or for infinitely many trading points in time — i.e., for continuous trading — at:

$$G_{\infty}(f) = r + (\mu - r) \cdot f - \frac{\sigma^2}{2} \cdot f^2$$

The optimal fraction then is given through the first-order condition by the expression:

I.e., the expected excess return of the stock over the risk-free rate divided by the variance of the returns. This expression looks similar to the Sharpe ratio (see "Portfolio Optimization") but is different.

A real-world example shall illustrate the application of these formulae and their role in leveraging equity deployed to trading strategies. The trading strategy under consideration is simply a *passive long position in the S&P 500 index*. To this end, base data is quickly retrieved and required statistics are easily derived:

```
In [16]: raw = pd.read_csv('../../source/tr_eikon_eod_data.csv',
                          index_col=0, parse_dates=True)
In [17]: symbol = '.SPX'
In [18]: data = pd.DataFrame(raw[symbol])
In [19]: data['returns'] = np.log(data / data.shift(1))
In [20]: data.dropna(inplace=True)
In [21]: data.tail()
Out[21]: .SPX returns
        Date
        2018-06-25 2717.07 -0.013820
        2018-06-26 2723.06 0.002202
        2018-06-27 2699.63 -0.008642
        2018-06-28 2716.31 0.006160
        2018-06-29 2718.37 0.000758
```

The statistical properties of the S&P 500 index over the period covered suggest an optimal fraction of about 4.5 to be invested in the long position in the index. In other words, for every dollar available 4.5 dollars shall be invested implying a *leverage ratio* of 4.5, in accordance with the optimal Kelly "fraction" (or rather "factor" in this case). *Ceteris paribus*, the Kelly criterion implies a higher leverage the higher the expected return and the lower the volatility (variance):

```
In [22]: mu = data.returns.mean() * 252
In [23]: mu
Out[23]: 0.09898579893004976
```

```
In [24]: sigma = data.returns.std() * 252 ** 0.5
In [25]: sigma
Out[25]: 0.1488567510081967
In [26]: r = 0.0
In [27]: f = (mu - r) / sigma ** 2
In [28]: f
Out[28]: 4.4672043679706865
```

Calculates the annualized return.

Calculates the annualized volatility.

Sets the risk-free rate to 0 (for simplicity).

Calculates the optimal Kelly fraction to be invested in the strategy.

The following code simulates the application of the Kelly criterion and the optimal leverage ratio. For simplicity and comparison reasons, the initial equity is set to 1 while the initially invested total capital is set to . Depending on the performance of the capital deployed to the strategy, the total capital itself is adjusted daily according to the available equity. After a loss, the capital is reduced; after a profit, the capital is increased. The evolution of the equity position compared to the index itself is shown in Figure 16-3:

```
In [29]: equs = []
In [30]: def kelly_strategy(f):
             global equs
             equ = 'equity_{:.2f}'.format(f)
             equs.append(equ)
             cap = 'capital_{:.2f}'.format(f)
             data[equ] = 1
             data[cap] = data[equ] * f
             for i, t in enumerate(data.index[1:]):
                 t_1 = data.index[i]
                 data.loc[t, cap] = data[cap].loc[t_1] * \
                                     math.exp(data['returns'].loc[t])
                 data.loc[t, equ] = data[cap].loc[t] - \
                                     data[cap].loc[t_1] + \
                                     data[equ].loc[t_1]
                 data.loc[t, cap] = data[equ].loc[t] * f
```

```
In [31]: kelly_strategy(f * 0.5)
In [32]: kelly_strategy(f * 0.66)
In [33]: kelly_strategy(f)
In [34]: print(data[equs].tail())
                  equity_2.23 equity_2.95 equity_4.47
        Date
        2018-06-25 4.707070 6.367340 8.794342
        2018-06-26 4.730248 6.408727 8.880952
        2018-06-27 4.639340 6.246147 8.539593
        2018-06-28 4.703365 6.359932 8.775296
        2018-06-29 4.711332 6.374152 8.805026
In [35]: ax = data['returns'].cumsum().apply(np.exp).plot(legend=True,
                                                    figsize=(10, 6))
        data[equs].plot(ax=ax, legend=True);
```

Generates a new column for equity and sets the initial value to 1.

Generates a new column for capital and sets the initial value to .

Picks the right DatetimeIndex value for the previous values.

Calculates the new capital position given the return.

Adjusts the equity value according to the capital position performance.

Adjusts the capital position given the new equity position and the fixed leverage ratio.

Simulates the Kelly criterion–based strategy for half of *f* …

… for two-thirds of *f* …

… and for *f* itself.

<span id="page-15-0"></span>![](_page_15_Figure_0.jpeg)

*Figure 16-3. Cumulative performance of S&P 500 compared to equity position given different values of f*

As [Figure](#page-15-0) 16-3 illustrates, applying the optimal Kelly leverage leads to a rather erratic evolution of the equity position (high volatility) which is — given the leverage ratio of 4.47 — intuitively plausible. One would expect the volatility of the equity position to increase with increasing leverage. Therefore, practitioners often reduce the leverage to, for example, "half Kelly" — i.e., in the current example to . Therefore, [Figure](#page-15-0) 16-3 also shows the evolution of the equity position of values lower than "full Kelly." The risk indeed reduces with lower values of *f*.

# **MLBased Trading Strategy**

Chapter 14 introduces the FXCM trading platform, its REST API, and the Python wrapper package fxcmpy. This section combines an MLbased approach for predicting the direction of market price movements with historical data from the FXCM REST API to backtest an algorithmic trading strategy for the EUR/USD currency pair. It uses vectorized backtesting, taking into account this time the bid-ask spread as proportional transaction costs. It also adds, compared to the plain vectorized backtesting approach as introduced in Chapter 15, a more indepth analysis of the risk characteristics of the trading strategy tested.

# **Vectorized Backtesting**

The backtest is based on intraday data, more specifically on bars of length five minutes. The following code connects to the FXCM REST API and retrieves five-minute bar data for a whole month. Figure 16-4 visualizes the mid close prices over the period for which data is retrieved:

```
In [36]: import fxcmpy
In [37]: fxcmpy.__version__
Out[37]: '1.1.33'
In [38]: api = fxcmpy.fxcmpy(config_file='../fxcm.cfg')
In [39]: data = api.get_candles('EUR/USD', period='m5',
                               start='2018-06-01 00:00:00',
                               stop='2018-06-30 00:00:00')
In [40]: data.iloc[-5:, 4:]
Out[40]: askopen askclose askhigh asklow tickqty
        date
        2018-06-29 20:35:00 1.16862 1.16882 1.16896 1.16839 601
        2018-06-29 20:40:00 1.16882 1.16853 1.16898 1.16852 387
        2018-06-29 20:45:00 1.16853 1.16826 1.16862 1.16822 592
        2018-06-29 20:50:00 1.16826 1.16836 1.16846 1.16819 842
        2018-06-29 20:55:00 1.16836 1.16861 1.16876 1.16834 540
In [41]: data.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 6083 entries, 2018-06-01 00:00:00 to 2018-06-29 20:55:00
        Data columns (total 9 columns):
        bidopen 6083 non-null float64
        bidclose 6083 non-null float64
        bidhigh 6083 non-null float64
        bidlow 6083 non-null float64
        askopen 6083 non-null float64
        askclose 6083 non-null float64
        askhigh 6083 non-null float64
        asklow 6083 non-null float64
        tickqty 6083 non-null int64
        dtypes: float64(8), int64(1)
        memory usage: 475.2 KB
In [42]: spread = (data['askclose'] - data['bidclose']).mean()
        spread
Out[42]: 2.6338977478217845e-05
In [43]: data['midclose'] = (data['askclose'] + data['bidclose']) / 2
In [44]: ptc = spread / data['midclose'].mean()
        ptc
Out[44]: 2.255685318140426e-05
In [45]: data['midclose'].plot(figsize=(10, 6), legend=True);
```

Connects to the API and retrieves the data.

Calculates the average bid-ask spread.

Calculates the mid close prices from the ask and bid close prices.

Calculates the average proportional transaction costs given the average spread and the average mid close price.

![](_page_18_Figure_8.jpeg)

*Figure 16-4. EUR/USD exchange rate (five-minute bars)*

The ML-based strategy is based on lagged return data that is binarized. In other words, the ML algorithm learns from historical patterns of upward and downward movements whether another upward or downward movement is more likely. Accordingly, the following code creates features data with values of 0 and 1 as well as labels data with values of +1 and -1 indicating the observed market direction in all cases:

```
In [46]: data['returns'] = np.log(data['midclose'] / data['midclose'].shift(1))
In [47]: data.dropna(inplace=True)
In [48]: lags = 5
In [49]: cols = []
       for lag in range(1, lags + 1):
          col = 'lag_{}'.format(lag)
          data[col] = data['returns'].shift(lag)
          cols.append(col)
In [50]: data.dropna(inplace=True)
In [51]: data[cols] = np.where(data[cols] > 0, 1, 0)
In [52]: data['direction'] = np.where(data['returns'] > 0, 1, -1)
In [53]: data[cols + ['direction']].head()
Out[53]: lag_1 lag_2 lag_3 lag_4 lag_5 direction
       date
       2018-06-01 00:30:00 1 0 1 0 1 1
       2018-06-01 00:35:00 1 1 0 1 0 1
       2018-06-01 00:40:00 1 1 1 0 1 1
       2018-06-01 00:45:00 1 1 1 1 0 1
       2018-06-01 00:50:00 1 1 1 1 1 -1
```

Creates the lagged return data given the number of lags.

Transforms the feature values to binary data.

Transforms the returns data to directional label data.

Given the features and label data, different supervised learning algorithms can now be applied. In what follows, a support vector machine algorithm for classification is used from the scikit-learn ML package. The code trains and tests the algorithmic trading strategy based on a sequential train-test split. The accuracy scores of the model for the training and test data are slightly above 50%, while the score is even a bit higher on the test data. Instead of accuracy scores, one would also speak in a financial trading context of the *hit ratio* of the trading strategy; i.e., the number of winning trades compared to all trades. Since the hit ratio is greater than 50%, this might indicate — in the context of the Kelly criterion — a slight edge compared to a random walk setting:

```
In [54]: from sklearn.svm import SVC
         from sklearn.metrics import accuracy_score
```

```
In [55]: model = SVC(C=1, kernel='linear', gamma='auto')
In [56]: split = int(len(data) * 0.80)
In [57]: train = data.iloc[:split].copy()
In [58]: model.fit(train[cols], train['direction'])
Out[58]: SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
         decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
           max_iter=-1, probability=False, random_state=None, shrinking=True,
           tol=0.001, verbose=False)
In [59]: accuracy_score(train['direction'], model.predict(train[cols]))
Out[59]: 0.5198518823287389
In [60]: test = data.iloc[split:].copy()
In [61]: test['position'] = model.predict(test[cols])
In [62]: accuracy_score(test['direction'], test['position'])
Out[62]: 0.5419407894736842
```

The accuracy of the predictions from the trained model *in-sample* (training data).

The accuracy of the predictions from the trained model *out-of-sample* (test data).

It is well known that the hit ratio is only one aspect of success in financial trading. Also crucial are, among other things, the transaction costs implied by the trading strategy and getting the important trades right. <sup>2</sup> To this end, only a formal vectorized backtesting approach allows judgment of the quality of the trading strategy. The following code takes into account the proportional transaction costs based on the average bid-ask spread. Figure 16-5 compares the performance of the algorithmic trading strategy (without and with proportional transaction costs) to the performance of the passive benchmark investment:

```
In [63]: test['strategy'] = test['position'] * test['returns']
In [64]: sum(test['position'].diff() != 0)
Out[64]: 660
In [65]: test['strategy_tc'] = np.where(test['position'].diff() != 0,
                                       test['strategy'] - ptc,
                                       test['strategy'])
In [66]: test[['returns', 'strategy', 'strategy_tc']].sum(
                ).apply(np.exp)
Out[66]: returns 0.999324
```

```
strategy 1.026141
        strategy_tc 1.010977
        dtype: float64
In [67]: test[['returns', 'strategy', 'strategy_tc']].cumsum(
                ).apply(np.exp).plot(figsize=(10, 6));
```

Derives the log returns for the ML-based algorithmic trading strategy.

Calculates the number of trades implied by the trading strategy based on changes in the position.

Whenever a trade takes place, the proportional transaction costs are subtracted from the strategy's log return on that day.

![](_page_22_Figure_0.jpeg)

*Figure 16-5. Performance of EUR/USD exchange rate and algorithmic trading strategy*

# **LIMITATIONS OF VECTORIZED BACKTESTING**

Vectorized backtesting has its limits with regard to how closely to market realities strategies can be tested. For example, it does not allow direct inclusion of fixed transaction costs per trade. One could, as an approximation, take a multiple of the average proportional transaction costs (based on average position sizes) to account indirectly for fixed transactions costs. However, this would not be precise in general. If a higher degree of precision is required other approaches, such as *event-based backtesting* with explicit loops over every bar of the price data, need to be applied.

# **Optimal Leverage**

Equipped with the trading strategy's log returns data, the mean and variance values can be calculated in order to derive the optimal leverage according to the Kelly criterion. The code that follows scales the numbers to annualized values, although this does not change the optimal leverage values according to the Kelly criterion since the mean return and the variance scale with the same factor:

```
In [68]: mean = test[['returns', 'strategy_tc']].mean() * len(data) * 12
        mean
Out[68]: returns -0.040535
        strategy_tc 0.654711
        dtype: float64
In [69]: var = test[['returns', 'strategy_tc']].var() * len(data) * 12
        var
Out[69]: returns 0.007861
        strategy_tc 0.007837
        dtype: float64
In [70]: vol = var ** 0.5
        vol
Out[70]: returns 0.088663
        strategy_tc 0.088524
        dtype: float64
In [71]: mean / var
Out[71]: returns -5.156448
        strategy_tc 83.545792
        dtype: float64
In [72]: mean / var * 0.5
Out[72]: returns -2.578224
        strategy_tc 41.772896
        dtype: float64
```

Annualized mean returns.

Annualized variances.

Annualized volatilities.

Optimal leverage according to the Kelly criterion ("full Kelly").

Optimal leverage according to the Kelly criterion ("half Kelly").

Optimal leverage according to the Kelly criterion ("half Kelly").

Using the "half Kelly" criterion, the optimal leverage for the trading strategy is about 40. With a number of brokers, such as FXCM, and financial instruments, such as foreign exchange and contracts for difference (CFDs), such leverage ratios are feasible, even for retail traders. <sup>3</sup> [Figure](#page-25-0) 16-6 shows in comparison the performance of the trading strategy with transaction costs for different leverage values:

```
In [73]: to_plot = ['returns', 'strategy_tc']
In [74]: for lev in [10, 20, 30, 40, 50]:
             label = 'lstrategy_tc_%d' % lev
             test[label] = test['strategy_tc'] * lev
             to_plot.append(label)
In [75]: test[to_plot].cumsum().apply(np.exp).plot(figsize=(10, 6));
```

<span id="page-25-0"></span>Scales the strategy returns for different leverage values.

![](_page_26_Figure_0.jpeg)

*Figure 16-6. Performance of algorithmic trading strategy for different leverage values*

# **Risk Analysis**

Since leverage increases the risk associated with a trading strategy, a more indepth risk analysis seems in order. The risk analysis that follows assumes a leverage ratio of 30. First, the maximum drawdown and the longest drawdown period are calculated. *Maximum drawdown* is the largest loss (dip) after a recent high. Accordingly, the *longest drawdown period* is the longest period that the trading strategy needs to get back to a recent high. The analysis assumes that the initial equity position is 3,333 EUR, leading to an initial position size of 100,000 EUR for a leverage ratio of 30. It also assumes that there are no adjustments with regard to the equity over time, no matter what the performance is:

```
In [76]: equity = 3333
In [77]: risk = pd.DataFrame(test['lstrategy_tc_30'])
In [78]: risk['equity'] = risk['lstrategy_tc_30'].cumsum(
                 ).apply(np.exp) * equity
In [79]: risk['cummax'] = risk['equity'].cummax()
In [80]: risk['drawdown'] = risk['cummax'] - risk['equity']
In [81]: risk['drawdown'].max()
Out[81]: 781.7073602069818
In [82]: t_max = risk['drawdown'].idxmax()
         t_max
Out[82]: Timestamp('2018-06-29 02:45:00')
```

The initial equity.

The relevant log returns time series …

… scaled by the initial equity.

The cumulative maximum values over time.

The drawdown values over time.

The maximum drawdown value.

The point in time when it happens.

Technically a (new) high is characterized by a drawdown value of 0. The drawdown period is the time between two such highs. Figure 16-7 visualizes both the maximum drawdown and the drawdown periods:

```
In [83]: temp = risk['drawdown'][risk['drawdown'] == 0]
In [84]: periods = (temp.index[1:].to_pydatetime() -
                    temp.index[:-1].to_pydatetime())
In [85]: periods[20:30]
Out[85]: array([datetime.timedelta(seconds=68700),
                datetime.timedelta(seconds=72000),
         datetime.timedelta(seconds=1800), datetime.timedelta(seconds=300),
         datetime.timedelta(seconds=600), datetime.timedelta(seconds=300),
                datetime.timedelta(seconds=17400),
         datetime.timedelta(seconds=4500), datetime.timedelta(seconds=1500),
                datetime.timedelta(seconds=900)], dtype=object)
In [86]: t_per = periods.max()
In [87]: t_per
Out[87]: datetime.timedelta(seconds=76500)
In [88]: t_per.seconds / 60 / 60
Out[88]: 21.25
In [89]: risk[['equity', 'cummax']].plot(figsize=(10, 6))
         plt.axvline(t_max, c='r', alpha=0.5);
```

Identifies highs for which the drawdown must be 0.

Calculates the timedelta values between all highs.

The longest drawdown period in seconds …

… and hours.

![](_page_29_Figure_0.jpeg)

*Figure 16-7. Maximum drawdown (vertical line) and drawdown periods (horizontal lines)*

Another important risk measure is value-at-risk (VaR). It is quoted as a currency amount and represents the maximum loss to be expected given both a certain time horizon and a confidence level. The code that follows derives VaR values based on the log returns of the equity position for the leveraged trading strategy over time for different confidence levels. The time interval is fixed to the bar length of five minutes:

```
In [91]: import scipy.stats as scs
In [92]: percs = np.array([0.01, 0.1, 1., 2.5, 5.0, 10.0])
In [93]: risk['returns'] = np.log(risk['equity'] /
                                  risk['equity'].shift(1))
In [94]: VaR = scs.scoreatpercentile(equity * risk['returns'], percs)
In [95]: def print_var():
             print('%16s %16s' % ('Confidence Level', 'Value-at-Risk'))
             print(33 * '-')
             for pair in zip(percs, VaR):
                 print('%16.2f %16.3f' % (100 - pair[0], -pair[1]))
In [96]: print_var()
         Confidence Level Value-at-Risk
```

| --------------------------------- |         |
|-----------------------------------|---------|
| 99.99                             | 400.854 |
| 99.90                             | 175.932 |
| 99.00                             | 88.139  |
| 97.50                             | 60.485  |
| 95.00                             | 45.010  |
| 90.00                             | 32.056  |

Defines the percentile values to be used.

Calculates the VaR values given the percentile values.

Translates the percentile values into confidence levels and the VaR values (negative values) to positive values for printing.

Finally, the following code calculates the VaR values for a time horizon of one hour by resampling the original DataFrame object. In effect, the VaR values are increased for all confidence levels but the highest one:

```
In [97]: hourly = risk.resample('1H', label='right').last()
In [98]: hourly['returns'] = np.log(hourly['equity'] /
                              hourly['equity'].shift(1))
In [99]: VaR = scs.scoreatpercentile(equity * hourly['returns'], percs)
In [100]: print_var()
        Confidence Level Value-at-Risk
        ---------------------------------
                  99.99 389.524
                  99.90 372.657
                  99.00 205.662
                  97.50 186.999
                  95.00 164.869
                  90.00 101.835
```

Resamples the data from five-minute to one-hour bars.

Recalculates the VaR values for the resampled data.

# **Persisting the Model Object**

Once the algorithmic trading strategy is "accepted" based on the backtesting, leveraging, and risk analysis results, the model object might be persisted for later use in deployment. It embodies now *the* MLbased trading strategy or *the* trading algorithm: In [101]: **import pickle** In [102]: pickle.dump(model, open('algorithm.pkl', 'wb'))

# **Online Algorithm**

The trading algorithm tested so far is an *offline algorithm*. Such algorithms use a complete data set to solve a problem at hand. The problem has been to train an SVM algorithm based on binarized features data and directional label data. In practice, when deploying the trading algorithm in financial markets, it must consume data piece-by-piece as it arrives to predict the direction of the market movement for the next time interval (bar). This section makes use of the persisted model object from the previous section and embeds it into a streaming data environment.

The code that transforms the offline trading algorithm into an online trading algorithm mainly addresses the following issues:

*Tick data*

Tick data arrives in real time and is to be processed in real time

*Resampling*

The tick data is to be resampled to the appropriate bar size given the trading algorithm

# *Prediction*

The trading algorithm generates a prediction for the direction of the market movement over the relevant time interval that by nature lies in the future

# *Orders*

Given the current position and the prediction ("signal") generated by the algorithm, an order is placed or the position is kept

"Retrieving Streaming Data" shows how to retrieve tick data from the FXCM REST API in real time. The basic approach is to subscribe to a market data stream and pass a callback function that processes the data.

First, the persisted trading algorithm is loaded — it represents the trading logic to be followed. It might also be useful to define a helper function to print out the open position(s) while the trading algorithm is trading:

In [103]: algorithm = pickle.load(open('algorithm.pkl', 'rb'))

```
In [104]: algorithm
Out[104]: SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
          decision_function_shape='ovr', degree=3, gamma='auto',
          kernel='linear', max_iter=-1, probability=False,
          random_state=None, shrinking=True, tol=0.001, verbose=False)
In [105]: sel = ['tradeId', 'amountK', 'currency',
                 'grossPL', 'isBuy']
In [106]: def print_positions(pos):
              print('\n\n' + 50 * '=')
              print('Going {}.\n'.format(pos))
              time.sleep(1.5)
              print(api.get_open_positions()[sel])
              print(50 * '=' + '\n\n')
```

Defines the DataFrame columns to be shown.

Waits a bit for the order to be executed and reflected in the open positions.

Prints the open positions.

Before the online algorithm is defined and started, a few parameter values are set:

```
In [107]: symbol = 'EUR/USD'
          bar = '15s'
          amount = 100
          position = 0
          min_bars = lags + 1
          df = pd.DataFrame()
```

Instrument symbol to be traded.

Bar length for resampling; for easier testing, the bar length might be shortened compared to the real deployment length (e.g., 15 seconds instead of 5 minutes).

The amount, in thousands, to be traded.

The initial position ("neutral").

The minimum number of resampled bars required for the first prediction and trade to be possible.

An empty DataFrame object to be used later for the resampled data.

Following is the callback function automated\_strategy() that transforms the trading algorithm into a real-time context:

```
In [108]: def automated_strategy(data, dataframe):
              global min_bars, position, df
              ldf = len(dataframe)
              df = dataframe.resample(bar, label='right').last().ffill()
              if ldf % 20 == 0:
                  print('%3d' % len(dataframe), end=',')
              if len(df) > min_bars:
                  min_bars = len(df)
                  df['Mid'] = df[['Bid', 'Ask']].mean(axis=1)
                  df['Returns'] = np.log(df['Mid'] / df['Mid'].shift(1))
                  df['Direction'] = np.where(df['Returns'] > 0, 1, -1)
                  features = df['Direction'].iloc[-(lags + 1):-1]
                  features = features.values.reshape(1, -1)
                  signal = algorithm.predict(features)[0]
                  if position in [0, -1] and signal == 1:
                      api.create_market_buy_order(
                          symbol, amount - position * amount)
                      position = 1
                      print_positions('LONG')
                  elif position in [0, 1] and signal == -1:
                      api.create_market_sell_order(
                          symbol, amount + position * amount)
                      position = -1
                      print_positions('SHORT')
              if len(dataframe) > 350:
                  api.unsubscribe_market_data('EUR/USD')
                  api.close_all()
```

Captures the length of the DataFrame object with the tick data.

Resamples the tick data to the defined bar length.

Picks the relevant feature values for all lags …

… and reshapes them to a form that the model can use for prediction.

Generates the prediction value (either +1 or -1).

The conditions to enter (or keep) a *long* position.

The conditions to enter (or keep) a *short* position.

The condition to stop trading and close out any open positions (arbitrarily defined based on the number of ticks retrieved).

… and reshapes them to a form that the model can use for prediction.

# **Infrastructure and Deployment**

Deploying an automated algorithmic trading strategy with real funds requires an appropriate infrastructure. Among others, the infrastructure should satisfy the following conditions: Reliability

The infrastructure on which to deploy an algorithmic trading strategy should allow for high availability (e.g., > 99.9%) and should otherwise take care of reliability (automatic backups, redundancy of drives and web connections, etc.).

# *Performance*

Depending on the amount of data being processed and the computational demand the algorithms generate, the infrastructure must have enough CPU cores, working memory (RAM), and storage (SSD); in addition, the web connections should be sufficiently fast.

# *Security*

The operating system and the applications run on it should be protected by strong passwords as well as SSL encryption; the hardware should be protected from fire, water, and unauthorized physical access.

Basically, these requirements can only be fulfilled by renting appropriate infrastructure from a professional data center or a cloud provider. Investments in the physical infrastructure to satisfy the aforementioned requirements can in general only be justified by the bigger or even biggest players in the financial markets.

From a development and testing point of view, even the smallest Droplet (cloud instance) from DigitalOcean is enough to get started. At the time of this writing such a Droplet costs 5 USD per month; usage is billed by the hour and a server can be created within minutes and destroyed within seconds. 4

How to set up a Droplet with DigitalOcean is explained in detail in the section "Using Cloud Instances", with bash scripts that can be adjusted to reflect individual requirements regarding Python packages, for example.

### **OPERATIONAL RISKS**

Although the development and testing of automated algorithmic trading strategies is possible from a local computer (desktop, notebook, etc.), it is not appropriate for the deployment of live strategies trading real money. A simple loss of the web connection or a brief power outage might bring down the whole algorithm, leaving, for example, unintended open positions in the portfolio or causing data set corruption (due to missing out on real-time tick data), potentially leading to wrong signals and unintended trades/positions.

# **Logging and Monitoring**

Let's assume that the automated algorithmic trading strategy is to be deployed on a remote server (cloud instance, leased server, etc.), that all required Python packages have been installed (see "Using Cloud Instances"), and that, for instance, Jupyter Notebook is running [securely](http://bit.ly/2A8jkDx). What else needs to be considered from the algorithmic trader's point of view if they do not want to sit all day in front of the screen while logged in to the server?

This section addresses two important topics in this regard: *logging* and *real-time monitoring*. Logging persists information and events on disk for later inspection. It is standard practice in software application development and deployment. However, here the focus might be put rather on the financial side, logging important financial data and event information for later inspection and analysis. The same holds true for real-time monitoring making use of socket communication. Via sockets a constant real-time stream of important financial aspects can be created that can be retrieved and processed on a local computer, even if the deployment happens in the cloud.

"Automated Trading Strategy" presents a Python script implementing all these aspects and making use of the code from "Online Algorithm". The script puts the code in a shape that allows, for example, the *deployment* of the algorithmic trading strategy — based on the persisted algorithm object — on a remote server. It adds both *logging* and *monitoring* capabilities based on a custom function that, among others, makes use of [ZeroMQ](http://zeromq.org) for socket communication. In combination with the short script from "Strategy Monitoring", this allows for remote real-time monitoring of the activity on a remote server.

When the script from "Automated Trading Strategy" is run, either locally or remotely, the output that is logged and sent via the socket looks as follows: 2018-07-25 09:16:15.568208

==================================================================

### NUMBER OF BARS: 24

MOST RECENT DATA

Mid Returns Direction 2018-07-25 07:15:30 1.168885 -0.000009 -1

2018-07-25 07:15:45 1.168945 0.000043 1

2018-07-25 07:16:00 1.168895 -0.000051 -1

2018-07-25 07:16:15 1.168895 -0.000009 -1

2018-07-25 07:16:30 1.168885 -0.000017 -1

==================================================================

features: [[ 1 -1 1 -1 -1]]

position: -1

signal: -1

2018-07-25 09:16:15.581453

==================================================================

no trade placed

\*\*\*\*END OF CYCLE\*\*\*

2018-07-25 09:16:30.069737

==================================================================

## NUMBER OF BARS: 25

==================================================================

### MOST RECENT DATA

Mid Returns Direction 2018-07-25 07:15:45 1.168945 0.000043 1

2018-07-25 07:16:00 1.168895 -0.000051 -1

2018-07-25 07:16:15 1.168895 -0.000009 -1

2018-07-25 07:16:30 1.168950 0.000034 1

2018-07-25 07:16:45 1.168945 -0.000017 -1

==================================================================

features: [[-1 1 -1 -1 1]]

position: -1

signal: 1

2018-07-25 09:16:33.035094

==================================================================

==================================================

Going LONG.

tradeId amountK currency grossPL isBuy 0 61476318 100 EUR/USD -2 True ==================================================

### \*\*\*\*END OF CYCLE\*\*\*

Running the script from "Strategy Monitoring" locally then allows the real-time retrieval and processing of such information. Of course, it is easy to adjust the logging and streaming data to one's own requirements. <sup>5</sup> Similarly, one can also, for example, persist DataFrame objects as created during the execution of the trading script. Furthermore, the trading script and the whole logic can be adjusted to include such elements as stop losses or take profit targets programmatically. Alternatively, one could make use of more sophisticated order types available via the FXCM [trading](http://fxcmpy.tpq.io) API.

### **CONSIDER ALL RISKS**

Trading currency pairs and/or CFDs is associated with a number of financial risks. Implementing an algorithmic trading strategy for such instruments automatically leads to a number of additional risks. Among them are flaws in the trading and/or execution logic. as well as technical risks such as problems with socket communications or delayed retrieval or even loss of tick data during the deployment. Therefore, before one deploys a trading strategy in automated fashion one should make sure that all associated market, execution, operational, technical, and other risks have been identified, evaluated, and addressed. The code presented in this chapter is intended only for technical illustration purposes.

# **Conclusion**

This chapter is about the deployment of an algorithmic trading strategy — based on a classification algorithm from machine learning to predict the direction of market movements — in automated fashion. It addresses such important topics as capital management (based on the Kelly criterion), vectorized backtesting for performance and risk, the transformation of offline to online trading algorithms, an appropriate infrastructure for deployment, as well as logging and monitoring during deployment.

The topic of this chapter is complex and requires a broad skill set from the algorithmic trading practitioner. On the other hand, having a REST API for algorithmic trading available, such as the one from FXCM, simplifies the automation task considerably since the core part boils down mainly to making use of the capabilities of the Python wrapper package fxcmpy for tick data retrieval and order placement. Around this core, elements to mitigate operational and technical risks as far as possible have to be added.
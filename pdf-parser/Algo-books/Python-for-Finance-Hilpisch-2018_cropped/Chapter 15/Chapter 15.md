# **Chapter 15. Trading Strategies**

[T]hey were silly enough to think you can look at the past to predict the future.

### *The Economist* 1

This chapter is about the vectorized backtesting of algorithmic trading strategies. The term *algorithmic trading strategy* is used to describe any type of financial trading strategy that is based on an algorithm designed to take long, short, or neutral positions in financial instruments on its own without human interference. A simple algorithm, such as "altering every five minutes between a long and a neutral position in the stock of Apple, Inc.," satisfies this definition. For the purposes of this chapter and a bit more technically, an algorithmic trading strategy is represented by some Python code that, given the availability of new data, decides whether to buy or sell a financial instrument in order to take long, short, or neutral positions in it.

The chapter does not provide an overview of algorithmic trading strategies (see "Further Resources" for references that cover algorithmic trading strategies in more detail). It rather focuses on the technical aspects of the *vectorized backtesting* approach for a select few such strategies. With this approach the financial data on which the strategy is tested is manipulated in general as a whole, applying vectorized operations on NumPy ndarray and pandas DataFrame objects that store the financial data. 2

Another focus of the chapter is the application of *machine and deep learning algorithms* to formulate algorithmic trading strategies. To this end, classification algorithms are trained on historical data in order to predict future directional market movements. This in general requires the transformation of the financial data from real values to a relatively small number of categorical values. <sup>3</sup> This allows us to harness the pattern recognition power of such algorithms.

The chapter is broken down into the following sections:

### *"Simple Moving Averages"*

This section focuses on an algorithmic trading strategy based on simple moving averages and how to backtest such a strategy.

moving averages and how to backtest such a strategy.

### *"Random Walk Hypothesis"*

This section introduces the random walk hypothesis.

### *"Linear OLS Regression"*

This section looks at using OLS regression to derive an algorithmic trading strategy.

### *"Clustering"*

In this section, we explore using unsupervised learning algorithms to derive algorithmic trading strategies.

### *"Frequency Approach"*

This section introduces a simple frequentist approach for algorithmic trading.

### *"Classification"*

Here we look at classification algorithms from machine learning for algorithmic trading.

### *"Deep Neural Networks"*

This section focuses on deep neural networks and how to use them for algorithmic trading.

# **Simple Moving Averages**

Trading based on simple moving averages (SMAs) is a decades-old trading approach (see, for example, the paper by Brock *et al.* (1992)). Although many traders use SMAs for their discretionary trading, they can also be used to formulate simple algorithmic trading strategies. This section uses SMAs to introduce vectorized backtesting of algorithmic trading strategies. It builds on the technical analysis example in Chapter 8.

### **Data Import**

First, some imports:

```
In [1]: import numpy as np
        import pandas as pd
        import datetime as dt
        from pylab import mpl, plt
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
```

Second, the reading of the raw data and the selection of the financial time series for a single symbol, the stock of Apple, Inc. (AAPL.O). The analysis in this section is based on end-of-day data; intraday data is used in subsequent sections:

```
In [3]: raw = pd.read_csv('../../source/tr_eikon_eod_data.csv',
                        index_col=0, parse_dates=True)
In [4]: raw.info()
       <class 'pandas.core.frame.DataFrame'>
       DatetimeIndex: 2216 entries, 2010-01-01 to 2018-06-29
       Data columns (total 12 columns):
       AAPL.O 2138 non-null float64
       MSFT.O 2138 non-null float64
       INTC.O 2138 non-null float64
       AMZN.O 2138 non-null float64
       GS.N 2138 non-null float64
       SPY 2138 non-null float64
       .SPX 2138 non-null float64
       .VIX 2138 non-null float64
       EUR= 2216 non-null float64
       XAU= 2211 non-null float64
       GDX 2138 non-null float64
       GLD 2138 non-null float64
       dtypes: float64(12)
       memory usage: 225.1 KB
In [5]: symbol = 'AAPL.O'
In [6]: data = (
           pd.DataFrame(raw[symbol])
           .dropna()
       )
```

### **Trading Strategy**

Third, the calculation of the SMA values for two different rolling window sizes. [Figure](#page-4-0) 15-1 shows the three time series visually:

```
In [7]: SMA1 = 42
        SMA2 = 252
In [8]: data['SMA1'] = data[symbol].rolling(SMA1).mean()
        data['SMA2'] = data[symbol].rolling(SMA2).mean()
In [9]: data.plot(figsize=(10, 6));
```

![](_page_4_Figure_3.jpeg)

Calculates the values for the *shorter* SMA.

![](_page_4_Figure_5.jpeg)

Calculates the values for the *longer* SMA.

<span id="page-4-0"></span>![](_page_4_Figure_7.jpeg)

*Figure 15-1. Apple stock price and two simple moving averages*

Fourth, the derivation of the positions. The trading rules are:

Go *long* (= +1) when the shorter SMA is above the longer SMA.

Go *short* (= -1) when the shorter SMA is below the longer SMA. 4

The positions are visualized in [Figure](#page-5-0) 15-2:

```
In [10]: data.dropna(inplace=True)
In [11]: data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
In [12]: data.tail()
Out[12]: AAPL.O SMA1 SMA2 Position
       Date
       2018-06-25 182.17 185.606190 168.265556 1
       2018-06-26 184.43 186.087381 168.418770 1
       2018-06-27 184.16 186.607381 168.579206 1
       2018-06-28 185.50 187.089286 168.736627 1
       2018-06-29 185.11 187.470476 168.901032 1
In [13]: ax = data.plot(secondary_y='Position', figsize=(10, 6))
       ax.get_legend().set_bbox_to_anchor((0.25, 0.85));
```

np.where(cond, a, b) evaluates the condition cond element-wise and places a when True and b otherwise.

<span id="page-5-0"></span>![](_page_5_Figure_5.jpeg)

*Figure 15-2. Apple stock price, two SMAs, and resulting positions*

This replicates the results derived in Chapter 8. What is not addressed there is if

following the trading rules — i.e., implementing the algorithmic trading strategy — is superior compared to the benchmark case of simply going long on the Apple stock over the whole period. Given that the strategy leads to two periods only during which the Apple stock should be shorted, differences in the performance can only result from these two periods.

### **Vectorized Backtesting**

The vectorized backtesting can now be implemented as follows. First, the log returns are calculated. Then the positionings, represented as +1 or -1, are multiplied by the relevant log return. This simple calculation is possible since a long position earns the return of the Apple stock and a short position earns the negative return of the Apple stock. Finally, the log returns for the Apple stock and the algorithmic trading strategy based on SMAs need to be added up and the exponential function applied to arrive at the performance values:

```
In [14]: data['Returns'] = np.log(data[symbol] / data[symbol].shift(1))
In [15]: data['Strategy'] = data['Position'].shift(1) * data['Returns']
In [16]: data.round(4).head()
Out[16]: AAPL.O SMA1 SMA2 Position Returns Strategy
       Date
       2010-12-31 46.0800 45.2810 37.1207 1 NaN NaN
       2011-01-03 47.0814 45.3497 37.1862 1 0.0215 0.0215
       2011-01-04 47.3271 45.4126 37.2525 1 0.0052 0.0052
       2011-01-05 47.7142 45.4661 37.3223 1 0.0081 0.0081
       2011-01-06 47.6757 45.5226 37.3921 1 -0.0008 -0.0008
In [17]: data.dropna(inplace=True)
In [18]: np.exp(data[['Returns', 'Strategy']].sum())
Out[18]: Returns 4.017148
       Strategy 5.811299
       dtype: float64
In [19]: data[['Returns', 'Strategy']].std() * 252 ** 0.5
Out[19]: Returns 0.250571
       Strategy 0.250407
       dtype: float64
```

Calculates the log returns of the Apple stock (i.e., the benchmark investment).

Multiplies the position values, shifted by one day, by the log returns of the Apple stock; the shift is required to avoid a foresight bias. 5

Sums up the log returns for the strategy and the benchmark investment and calculates the exponential value to arrive at the absolute performance.

Calculates the annualized volatility for the strategy and the benchmark investment.

The numbers show that the algorithmic trading strategy indeed outperforms the benchmark investment of passively holding the Apple stock. Due to the type and characteristics of the strategy, the annualized volatility is the same, such that it also outperforms the benchmark investment on a risk-adjusted basis.

To gain a better picture of the overall performance, [Figure](#page-8-0) 15-3 shows the performance of the Apple stock and the algorithmic trading strategy over time:

```
In [20]: ax = data[['Returns', 'Strategy']].cumsum(
                 ).apply(np.exp).plot(figsize=(10, 6))
         data['Position'].plot(ax=ax, secondary_y='Position', style='--')
         ax.get_legend().set_bbox_to_anchor((0.25, 0.85));
```

*Figure 15-3. Performance of Apple stock and SMA-based trading strategy over time*

### **SIMPLIFICATIONS**

The vectorized backtesting approach as introduced in this subsection is based on a number of simplifying assumptions. Among others, transactions costs (fixed fees, bid-ask spreads, lending costs, etc.) are not included. This might be justifiable for a trading strategy that leads to a few trades only over multiple years. It is also assumed that all trades take place at the endof-day closing prices for the Apple stock. A more realistic backtesting approach would take these and other (market microstructure) elements into account.

### **Optimization**

A natural question that arises is if the chosen parameters SMA1=42 and SMA2=252 are the "right" ones. In general, investors prefer higher returns to lower returns *ceteris paribus*. Therefore, one might be inclined to search for those parameters that maximize the return over the relevant period. To this end, a brute force approach can be used that simply repeats the whole vectorized backtesting procedure for different parameter combinations, records the results, and does a ranking afterward. This is what the following code does:

```
In [21]: from itertools import product
In [22]: sma1 = range(20, 61, 4)
         sma2 = range(180, 281, 10)
In [23]: results = pd.DataFrame()
         for SMA1, SMA2 in product(sma1, sma2):
             data = pd.DataFrame(raw[symbol])
             data.dropna(inplace=True)
             data['Returns'] = np.log(data[symbol] / data[symbol].shift(1))
             data['SMA1'] = data[symbol].rolling(SMA1).mean()
             data['SMA2'] = data[symbol].rolling(SMA2).mean()
             data.dropna(inplace=True)
             data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
             data['Strategy'] = data['Position'].shift(1) * data['Returns']
             data.dropna(inplace=True)
             perf = np.exp(data[['Returns', 'Strategy']].sum())
             results = results.append(pd.DataFrame(
                         {'SMA1': SMA1, 'SMA2': SMA2,
                          'MARKET': perf['Returns'],
                          'STRATEGY': perf['Strategy'],
                          'OUT': perf['Strategy'] - perf['Returns']},
                          index=[0]), ignore_index=True)
```

Specifies the parameter values for SMA1.

Specifies the parameter values for SMA2.

Combines all values for SMA1 with those for SMA2.

Records the vectorized backtesting results in a DataFrame object.

The following code gives an overview of the results and shows the seven best-

performing parameter combinations of all those backtested. The ranking is implemented according to the outperformance of the algorithmic trading strategy compared to the benchmark investment. The performance of the benchmark investment varies since the choice of the SMA2 parameter influences the length of the time interval and data set on which the vectorized backtest is implemented:

|          | In [24]: results.info()                                      |                      |                    |                    |          |          |  |
|----------|--------------------------------------------------------------|----------------------|--------------------|--------------------|----------|----------|--|
|          | <class 'pandas.core.frame.dataframe'=""></class>             |                      |                    |                    |          |          |  |
|          | RangeIndex: 121 entries, 0 to 120                            |                      |                    |                    |          |          |  |
|          | Data columns (total 5 columns):                              |                      |                    |                    |          |          |  |
|          | SMA1                                                         |                      | 121 non-null int64 |                    |          |          |  |
|          | SMA2                                                         |                      |                    | 121 non-null int64 |          |          |  |
|          | MARKET                                                       | 121 non-null float64 |                    |                    |          |          |  |
|          | STRATEGY<br>121 non-null float64                             |                      |                    |                    |          |          |  |
|          | OUT<br>121 non-null float64                                  |                      |                    |                    |          |          |  |
|          | dtypes: float64(3), int64(2)                                 |                      |                    |                    |          |          |  |
|          | memory usage: 4.8 KB                                         |                      |                    |                    |          |          |  |
|          |                                                              |                      |                    |                    |          |          |  |
|          | In [25]: results.sort_values('OUT', ascending=False).head(7) |                      |                    |                    |          |          |  |
| Out[25]: |                                                              | SMA1                 | SMA2               | MARKET             | STRATEGY | OUT      |  |
|          | 56                                                           | 40                   | 190                | 4.650342           | 7.175173 | 2.524831 |  |
|          | 39                                                           | 32                   | 240                | 4.045619           | 6.558690 | 2.513071 |  |
|          | 59                                                           | 40                   | 220                | 4.220272           | 6.544266 | 2.323994 |  |
|          | 46                                                           | 36                   | 200                | 4.074753           | 6.389627 | 2.314874 |  |
|          | 55                                                           | 40                   | 180                | 4.574979           | 6.857989 | 2.283010 |  |
|          | 70                                                           | 44                   | 220                | 4.220272           | 6.469843 | 2.249571 |  |
|          | 101                                                          | 56                   | 200                | 4.074753           | 6.319524 | 2.244772 |  |

According to the brute force–based optimization, SMA1=40 and SMA2=190 are the optimal parameters, leading to an outperformance of some 230 percentage points. However, this result is heavily dependent on the data set used and is prone to overfitting. A more rigorous approach would be to implement the optimization on one data set, the in-sample or training data set, and test it on another one, the out-of-sample or testing data set.

### **OVERFITTING**

In general, any type of optimization, fitting, or training in the context of algorithmic trading strategies is prone to what is called *overfitting*. This means that parameters might be chosen that perform (exceptionally) well for the used data set but might perform (exceptionally) badly on other data sets or in practice.

# **Random Walk Hypothesis**

The previous section introduces vectorized backtesting as an efficient tool to backtest algorithmic trading strategies. The single strategy backtested based on a single financial time series, namely historical end-of-day prices for the Apple stock, outperforms the benchmark investment of simply going long on the Apple stock over the same period.

Although rather specific in nature, these results are in contrast to what the *random walk hypothesis* (RWH) predicts, namely that such predictive approaches should not yield any outperformance at all. The RWH postulates that prices in financial markets follow a random walk, or, in continuous time, an arithmetic Brownian motion without drift. The expected value of an arithmetic Brownian motion without drift at any point in the future equals its value today. 6 As a consequence, the best predictor for tomorrow's price, in a least-squares sense, is today's price if the RWH applies.

The consequences are summarized in the following quote:

For many years, economists, statisticians, and teachers of finance have been interested in developing and testing models of stock price behavior. One important model that has evolved from this research is the theory of random walks. This theory casts serious doubt on many other methods for describing and predicting stock price behavior — methods that have considerable popularity outside the academic world. For example, we shall see later that, if the random-walk theory is an accurate description of reality, then the various "technical" or "chartist" procedures for predicting stock prices are completely without value.

Eugene F. Fama (1965)

The RWH is consistent with the *efficient markets hypothesis* (EMH), which, non-technically speaking, states that market prices reflect "all available information." Different degrees of efficiency are generally distinguished, such as *weak*, *semi-strong*, and *strong*, defining more specifically what "all available information" entails. Formally, such a definition can be based on the concept of an information set in theory and on a data set for programming purposes, as the following quote illustrates:

A market is efficient with respect to an information set *S* if it is impossible to make economic profits by trading on the basis of information set *S*. Michael Jensen (1978)

Using Python, the RWH can be tested for a specific case as follows. A financial time series of historical market prices is used for which a number of *lagged* versions are created — say, five. OLS regression is then used to predict the market prices based on the lagged market prices created before. The basic idea is that the market prices from yesterday and four more days back can be used to predict today's market price.

The following Python code implements this idea and creates five lagged versions of the historical end-of-day closing levels of the S&P 500 stock index:

```
In [26]: symbol = '.SPX'
In [27]: data = pd.DataFrame(raw[symbol])
In [28]: lags = 5
       cols = []
       for lag in range(1, lags + 1):
          col = 'lag_{}'.format(lag)
          data[col] = data[symbol].shift(lag)
          cols.append(col)
In [29]: data.head(7)
Out[29]: .SPX lag_1 lag_2 lag_3 lag_4 lag_5
       Date
       2010-01-01 NaN NaN NaN NaN NaN NaN
       2010-01-04 1132.99 NaN NaN NaN NaN NaN
       2010-01-05 1136.52 1132.99 NaN NaN NaN NaN
       2010-01-06 1137.14 1136.52 1132.99 NaN NaN NaN
       2010-01-07 1141.69 1137.14 1136.52 1132.99 NaN NaN
       2010-01-08 1144.98 1141.69 1137.14 1136.52 1132.99 NaN
       2010-01-11 1146.98 1144.98 1141.69 1137.14 1136.52 1132.99
In [30]: data.dropna(inplace=True)
```

Defines a column name for the current lag value.

Creates the lagged version of the market prices for the current lag value.

Collects the column names for later reference.

Using NumPy, the OLS regression is straightforward to implement. As the optimal regression parameters show, lag\_1 indeed is the most important one in predicting the market price based on OLS regression. Its value is close to 1. The other four values are rather close to 0. [Figure](#page-15-0) 15-4 visualizes the optimal regression parameter values.

<span id="page-15-0"></span>![](_page_15_Figure_1.jpeg)

*Figure 15-4. Optimal regression parameters from OLS regression for price prediction*

When using the optimal results to visualize the prediction values as compared to the original index values for the S&P 500, it becomes obvious from Figure 15-5 that indeed lag\_1 is basically what is used to come up with the prediction value. Graphically speaking, the prediction line in Figure 15-5 is the original time series shifted by one day to the right (with some minor adjustments).

![](_page_16_Figure_0.jpeg)

*Figure 15-5. S&P 500 levels compared to prediction values from OLS regression*

All in all, the brief analysis in this section reveals some support for both the RWH and the EMH. For sure, the analysis is done for a single stock index only and uses a rather specific parameterization — but this can easily be widened to incorporate multiple financial instruments across multiple asset classes, different values for the number of lags, *etc.* In general, one will find out that the results are qualitatively more or less the same. After all, the RWH and EMH are among the financial theories that have broad empirical support. In that sense, any algorithmic trading strategy must prove its worth by proving that the RWH does not apply in general. This for sure is a tough hurdle.

# **Linear OLS Regression**

This section applies *linear OLS regression* to predict the direction of market movements based on historical log returns. To keep things simple, only two features are used. The first feature (lag\_1) represents the log returns of the financial time series lagged by *one day*. The second feature (lag\_2) lags the log returns by *two days*. Log returns — in contrast to prices — are *stationary* in general, which often is a necessary condition for the application of statistical and ML algorithms.

The basic idea behind the usage of lagged log returns as features is that they might be informative in predicting future returns. For example, one might hypothesize that after two downward movements an upward movement is more likely ("mean reversion"), or, to the contrary, that another downward movement is more likely ("momentum" or "trend"). The application of regression techniques allows the formalization of such informal reasonings.

### **The Data**

First, the importing and preparation of the data set. Figure 15-6 shows the frequency distribution of the daily historical log returns for the EUR/USD exchange rate. They are the basis for the features as well as the labels to be used in what follows:

```
In [3]: raw = pd.read_csv('../../source/tr_eikon_eod_data.csv',
                        index_col=0, parse_dates=True).dropna()
In [4]: raw.columns
Out[4]: Index(['AAPL.O', 'MSFT.O', 'INTC.O', 'AMZN.O', 'GS.N', 'SPY', '.SPX',
              '.VIX', 'EUR=', 'XAU=', 'GDX', 'GLD'],
             dtype='object')
In [5]: symbol = 'EUR='
In [6]: data = pd.DataFrame(raw[symbol])
In [7]: data['returns'] = np.log(data / data.shift(1))
In [8]: data.dropna(inplace=True)
In [9]: data['direction'] = np.sign(data['returns']).astype(int)
In [10]: data.head()
Out[10]: EUR= returns direction
        Date
        2010-01-05 1.4368 -0.002988 -1
        2010-01-06 1.4412 0.003058 1
        2010-01-07 1.4318 -0.006544 -1
        2010-01-08 1.4412 0.006544 1
        2010-01-11 1.4513 0.006984 1
```

```
In [11]: data['returns'].hist(bins=35, figsize=(10, 6));
```

![](_page_19_Figure_0.jpeg)

*Figure 15-6. Histogram of log returns for EUR/USD exchange rate*

Second, the code that creates the features data by lagging the log returns and visualizes it in combination with the returns data (see Figure 15-7):

```
In [12]: lags = 2
In [13]: def create_lags(data):
           global cols
           cols = []
           for lag in range(1, lags + 1):
              col = 'lag_{}'.format(lag)
              data[col] = data['returns'].shift(lag)
              cols.append(col)
In [14]: create_lags(data)
In [15]: data.head()
Out[15]: EUR= returns direction lag_1 lag_2
       Date
       2010-01-05 1.4368 -0.002988 -1 NaN NaN
       2010-01-06 1.4412 0.003058 1 -0.002988 NaN
       2010-01-07 1.4318 -0.006544 -1 0.003058 -0.002988
       2010-01-08 1.4412 0.006544 1 -0.006544 0.003058
       2010-01-11 1.4513 0.006984 1 0.006544 -0.006544
```

In [16]: data.dropna(inplace=True)

```
In [17]: data.plot.scatter(x='lag_1', y='lag_2', c='returns',
                           cmap='coolwarm', figsize=(10, 6), colorbar=True)
         plt.axvline(0, c='r', ls='--')
         plt.axhline(0, c='r', ls='--');
```

![](_page_20_Figure_2.jpeg)

*Figure 15-7. Scatter plot based on features and labels data*

### **Regression**

With the data set completed, linear OLS regression can be applied to learn about any potential (linear) relationships, to predict market movement based on the features, and to backtest a trading strategy based on the predictions. Two basic approaches are available: using the *log returns* or only the *direction data* as the dependent variable during the regression. In any case, predictions are real-valued and therefore transformed to either +1 or -1 to only work with the direction of the prediction:

```
In [18]: from sklearn.linear_model import LinearRegression
In [19]: model = LinearRegression()
In [20]: data['pos_ols_1'] = model.fit(data[cols],
                                      data['returns']).predict(data[cols])
In [21]: data['pos_ols_2'] = model.fit(data[cols],
                                      data['direction']).predict(data[cols])
In [22]: data[['pos_ols_1', 'pos_ols_2']].head()
Out[22]: pos_ols_1 pos_ols_2
        Date
        2010-01-07 -0.000166 -0.000086
        2010-01-08 0.000017 0.040404
        2010-01-11 -0.000244 -0.011756
        2010-01-12 -0.000139 -0.043398
        2010-01-13 -0.000022 0.002237
In [23]: data[['pos_ols_1', 'pos_ols_2']] = np.where(
                    data[['pos_ols_1', 'pos_ols_2']] > 0, 1, -1)
In [24]: data['pos_ols_1'].value_counts()
Out[24]: -1 1847
         1 288
        Name: pos_ols_1, dtype: int64
In [25]: data['pos_ols_2'].value_counts()
Out[25]: 1 1377
        -1 758
        Name: pos_ols_2, dtype: int64
In [26]: (data['pos_ols_1'].diff() != 0).sum()
Out[26]: 555
In [27]: (data['pos_ols_2'].diff() != 0).sum()
Out[27]: 762
```

The linear OLS regression implementation from scikit-learn is used.

The regression is implemented on the *log returns* directly …

… and on the *direction data* which is of primary interest.

The real-valued predictions are transformed to directional values (+1, -1).

The two approaches yield different directional predictions in general.

However, both lead to a relatively large number of trades over time.

Equipped with the directional prediction, vectorized backtesting can be applied to judge the performance of the resulting trading strategies. At this stage, the analysis is based on a number of simplifying assumptions, such as "zero transaction costs" and the usage of the same data set for both training and testing. Under these assumptions, however, both regression-based strategies outperform the benchmark passive investment, while only the strategy trained on the direction of the market shows a positive overall performance (Figure 15-8):

```
In [28]: data['strat_ols_1'] = data['pos_ols_1'] * data['returns']
In [29]: data['strat_ols_2'] = data['pos_ols_2'] * data['returns']
In [30]: data[['returns', 'strat_ols_1', 'strat_ols_2']].sum().apply(np.exp)
Out[30]: returns 0.810644
        strat_ols_1 0.942422
        strat_ols_2 1.339286
        dtype: float64
In [31]: (data['direction'] == data['pos_ols_1']).value_counts()
Out[31]: False 1093
        True 1042
        dtype: int64
In [32]: (data['direction'] == data['pos_ols_2']).value_counts()
Out[32]: True 1096
        False 1039
        dtype: int64
In [33]: data[['returns', 'strat_ols_1', 'strat_ols_2']].cumsum(
                ).apply(np.exp).plot(figsize=(10, 6));
```

Shows the number of correct and false predictions by the strategies.

![](_page_23_Figure_0.jpeg)

*Figure 15-8. Performance of EUR/USD and regression-based strategies over time*

# **Clustering**

This section applies *k*-means clustering, as introduced in "Machine Learning", to financial time series data to automatically come up with clusters that are used to formulate a trading strategy. The idea is that the algorithm identifies two clusters of feature values that predict either an upward movement or a downward movement.

The following code applies the *k*-means algorithm to the two features as used before. Figure 15-9 visualizes the two clusters:

```
In [34]: from sklearn.cluster import KMeans
In [35]: model = KMeans(n_clusters=2, random_state=0)
In [36]: model.fit(data[cols])
Out[36]: KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
             n_clusters=2, n_init=10, n_jobs=None, precompute_distances='auto',
             random_state=0, tol=0.0001, verbose=0)
In [37]: data['pos_clus'] = model.predict(data[cols])
In [38]: data['pos_clus'] = np.where(data['pos_clus'] == 1, -1, 1)
In [39]: data['pos_clus'].values
Out[39]: array([-1, 1, -1, ..., 1, 1, -1])
In [40]: plt.figure(figsize=(10, 6))
         plt.scatter(data[cols].iloc[:, 0], data[cols].iloc[:, 1],
                     c=data['pos_clus'], cmap='coolwarm');
```

Two clusters are chosen for the algorithm.

Given the cluster values, the position is chosen.

![](_page_25_Figure_0.jpeg)

Admittedly, this approach is quite arbitrary in this context — after all, how should the algorithm know what one is looking for? However, the resulting trading strategy shows a slight outperformance at the end compared to the benchmark passive investment (see Figure 15-10). It is noteworthy that no guidance (supervision) is given and that the *hit ratio* — i.e., the number of correct predictions in relationship to all predictions made — is less than 50%:

```
In [41]: data['strat_clus'] = data['pos_clus'] * data['returns']
In [42]: data[['returns', 'strat_clus']].sum().apply(np.exp)
Out[42]: returns 0.810644
        strat_clus 1.277133
        dtype: float64
In [43]: (data['direction'] == data['pos_clus']).value_counts()
Out[43]: True 1077
        False 1058
        dtype: int64
In [44]: data[['returns', 'strat_clus']].cumsum(
                ).apply(np.exp).plot(figsize=(10, 6));
```

![](_page_26_Figure_0.jpeg)

*Figure 15-10. Performance of EUR/USD and k-means-based strategy over time*

# **Frequency Approach**

Beyond more sophisticated algorithms and techniques, one might come up with the idea of just implementing a *frequency approach* to predict directional movements in financial markets. To this end, one might transform the two realvalued features to binary ones and assess the probability of an upward and a downward movement, respectively, from the historical observations of such movements, given the four possible combinations for the two binary features ((0, 0), (0, 1), (1, 0), (1, 1)).

Making use of the data analysis capabilities of pandas, such an approach is relatively easy to implement:

```
In [45]: def create_bins(data, bins=[0]):
         global cols_bin
         cols_bin = []
         for col in cols:
           col_bin = col + '_bin'
           data[col_bin] = np.digitize(data[col], bins=bins)
           cols_bin.append(col_bin)
In [46]: create_bins(data)
In [47]: data[cols_bin + ['direction']].head()
Out[47]: lag_1_bin lag_2_bin direction
      Date
      2010-01-07 1 0 -1
      2010-01-08 0 1 1
      2010-01-11 1 0 1
      2010-01-12 1 1 -1
      2010-01-13 0 1 1
In [48]: grouped = data.groupby(cols_bin + ['direction'])
      grouped.size()
Out[48]: lag_1_bin lag_2_bin direction
      0 0 -1 239
                      0 4
                      1 258
              1 -1 262
                      1 288
      1 0 -1 272
                      0 1
                      1 278
              1 -1 278
                      0 4
                      1 251
      dtype: int64
In [49]: res = grouped['direction'].size().unstack(fill_value=0)
In [50]: def highlight_max(s):
         is_max = s == s.max()
```

```
return ['background-color: yellow' if v else '' for v in is_max]
In [51]: res.style.apply(highlight_max, axis=1)
Out[51]: <pandas.io.formats.style.Styler at 0x1a194216a0>
```

Digitizes the feature values given the bins parameter.

Shows the digitized feature values and the label values.

Shows the frequency of the possible movements conditional on the feature value combinations.

Transforms the DataFrame object to have the frequencies in columns.

Highlights the highest-frequency value per feature value combination.

Given the frequency data, three feature value combinations hint at a downward movement while one lets an upward movement seem more likely. This translates into a trading strategy the performance of which is shown in Figure 15-11:

```
In [52]: data['pos_freq'] = np.where(data[cols_bin].sum(axis=1) == 2, -1, 1)
In [53]: (data['direction'] == data['pos_freq']).value_counts()
Out[53]: True 1102
        False 1033
        dtype: int64
In [54]: data['strat_freq'] = data['pos_freq'] * data['returns']
In [55]: data[['returns', 'strat_freq']].sum().apply(np.exp)
Out[55]: returns 0.810644
        strat_freq 0.989513
        dtype: float64
In [56]: data[['returns', 'strat_freq']].cumsum(
                ).apply(np.exp).plot(figsize=(10, 6));
```

Translates the findings given the frequencies to a trading strategy.

![](_page_29_Figure_0.jpeg)

*Figure 15-11. Performance of EUR/USD and frequency-based trading strategy over time*

# **Classification**

This section applies the classification algorithms from ML (as introduced in "Machine Learning") to the problem of predicting the direction of price movements in financial markets. With that background and the examples from previous sections, the application of the logistic regression, Gaussian Naive Bayes, and support vector machine approaches is as straightforward as applying them to smaller sample data sets.

### **Two Binary Features**

First, a fitting of the models based on the binary feature values and the derivation of the resulting position values:

```
In [57]: from sklearn import linear_model
         from sklearn.naive_bayes import GaussianNB
         from sklearn.svm import SVC
In [58]: C = 1
In [59]: models = {
             'log_reg': linear_model.LogisticRegression(C=C),
             'gauss_nb': GaussianNB(),
             'svm': SVC(C=C)
         }
In [60]: def fit_models(data):
             mfit = {model: models[model].fit(data[cols_bin],
                                               data['direction'])
                     for model in models.keys()}
In [61]: fit_models(data)
In [62]: def derive_positions(data):
             for model in models.keys():
                 data['pos_' + model] = models[model].predict(data[cols_bin])
In [63]: derive_positions(data)
```

A function that fits all models.

A function that derives all position values from the fitted models.

Second, the vectorized backtesting of the resulting trading strategies. Figure 15- 12 visualizes the performance over time:

```
In [64]: def evaluate_strats(data):
             global sel
             sel = []
             for model in models.keys():
                 col = 'strat_' + model
                 data[col] = data['pos_' + model] * data['returns']
                 sel.append(col)
             sel.insert(0, 'returns')
In [65]: evaluate_strats(data)
In [66]: sel.insert(1, 'strat_freq')
In [67]: data[sel].sum().apply(np.exp)
```

```
Out[67]: returns 0.810644
       strat_freq 0.989513
       strat_log_reg 1.243322
       strat_gauss_nb 1.243322
       strat_svm 0.989513
       dtype: float64
In [68]: data[sel].cumsum().apply(np.exp).plot(figsize=(10, 6));
```

A function that evaluates all resulting trading strategies.

Some strategies might show the exact same performance.

![](_page_32_Figure_5.jpeg)

*Figure 15-12. Performance of EUR/USD and classification-based trading strategies (two binary lags) over time*

### **Five Binary Features**

In an attempt to improve the strategies' performance, the following code works with five binary lags instead of two. In particular, the performance of the SVMbased strategy is significantly improved (see Figure 15-13). On the other hand, the performance of the LR-and GNB-based strategies is worse: In [69]: data = pd.DataFrame(raw[symbol]) In [70]: data['returns'] = np.log(data / data.shift(1)) In [71]: data['direction'] = np.sign(data['returns']) In [72]: lags = 5 create\_lags(data) data.dropna(inplace=True) In [73]: create\_bins(data) cols\_bin Out[73]: ['lag\_1\_bin', 'lag\_2\_bin', 'lag\_3\_bin', 'lag\_4\_bin', 'lag\_5\_bin'] In [74]: data[cols\_bin].head() Out[74]: lag\_1\_bin lag\_2\_bin lag\_3\_bin lag\_4\_bin lag\_5\_bin Date 2010-01-12 1 1 0 1 0 2010-01-13 0 1 1 0 1 2010-01-14 1 0 1 1 0 2010-01-15 0 1 0 1 1 2010-01-19 0 0 1 0 1 In [75]: data.dropna(inplace=True) In [76]: fit\_models(data) In [77]: derive\_positions(data) In [78]: evaluate\_strats(data) In [79]: data[sel].sum().apply(np.exp) Out[79]: returns 0.805002 strat\_log\_reg 0.971623 strat\_gauss\_nb 0.986420 strat\_svm 1.452406 dtype: float64 In [80]: data[sel].cumsum().apply(np.exp).plot(figsize=(10, 6));

Five lags of the log returns series are now used.

The real-valued features data is transformed to binary data.

![](_page_34_Figure_0.jpeg)

*Figure 15-13. Performance of EUR/USD and classification-based trading strategies (five binary lags) over time*

### **Five Digitized Features**

Finally, the following code uses the first and second moment of the historical log returns to digitize the features data, allowing for more possible feature value combinations. This improves the performance of all classification algorithms used, but for SVM the improvement is again most pronounced (see Figure 15- 14): In [81]: mu = data['returns'].mean() v = data['returns'].std() In [82]: bins = [mu - v, mu, mu + v] bins Out[82]: [-0.006033537040418665, -0.00010174015279231306, 0.005830056734834039] In [83]: create\_bins(data, bins) In [84]: data[cols\_bin].head() Out[84]: lag\_1\_bin lag\_2\_bin lag\_3\_bin lag\_4\_bin lag\_5\_bin Date 2010-01-12 3 3 0 2 1 2010-01-13 1 3 3 0 2 2010-01-14 2 1 3 3 0 2010-01-15 1 2 1 3 3 2010-01-19 0 1 2 1 3 In [85]: fit\_models(data) In [86]: derive\_positions(data) In [87]: evaluate\_strats(data) In [88]: data[sel].sum().apply(np.exp) Out[88]: returns 0.805002 strat\_log\_reg 1.431120 strat\_gauss\_nb 1.815304 strat\_svm 5.653433 dtype: float64 In [89]: data[sel].cumsum().apply(np.exp).plot(figsize=(10, 6));

The mean log return and …

… the standard deviation are used …

… to digitize the features data.

![](_page_36_Figure_0.jpeg)

*Figure 15-14. Performance of EUR/USD and classification-based trading strategies (five digitized lags) over time*

### **TYPES OF FEATURES**

This chapter exclusively works with lagged return data as features data, mostly in binarized or digitized form. This is mainly done for convenience, since such features data can be derived from the financial time series itself. However, in practical applications the features data can be gained from a wealth of different data sources and might include other financial time series and statistics derived thereof, macroeconomic data, company financial indicators, or news articles. Refer to López de Prado (2018) for an in-depth discussion of this topic. There are also Python packages for automated time series feature extraction available, such as [tsfresh](https://github.com/blue-yonder/tsfresh).

### **Sequential Train-Test Split**

To better judge the performance of the classification algorithms, the code that follows implements a *sequential* train-test split. The idea here is to simulate the situation where only data up to a certain point in time is available on which to train an ML algorithm. During live trading, the algorithm is then faced with data it has never seen before. This is where the algorithm must prove its worth. In this particular case, all classification algorithms outperform — under the simplified assumptions from before — the passive benchmark investment, but only the GNB and LR algorithms achieve a positive absolute performance (Figure 15- 15): In [90]: split = int(len(data) \* 0.5) In [91]: train = data.iloc[:split].copy() In [92]: fit\_models(train) In [93]: test = data.iloc[split:].copy() In [94]: derive\_positions(test) In [95]: evaluate\_strats(test) In [96]: test[sel].sum().apply(np.exp) Out[96]: returns 0.850291 strat\_log\_reg 0.962989 strat\_gauss\_nb 0.941172 strat\_svm 1.048966 dtype: float64 In [97]: test[sel].cumsum().apply(np.exp).plot(figsize=(10, 6));

Trains all classification algorithms on the training data.

Tests all classification algorithms on the test data.

![](_page_39_Figure_0.jpeg)

*Figure 15-15. Performance of EUR/USD and classification-based trading strategies (sequential train-test split)*

### **Randomized TrainTest Split**

The classification algorithms are trained and tested on binary or digitized features data. The idea is that the feature value patterns allow a prediction of future market movements with a better hit ratio than 50%. Implicitly, it is assumed that the patterns' predictive power persists over time. In that sense, it shouldn't make (too much of) a difference on which part of the data an algorithm is trained and on which part of the data it is tested — implying that one can break up the temporal sequence of the data for training and testing.

A typical way to do this is a *randomized* traintest split to test the performance of the classification algorithms out-of-sample — again trying to emulate reality, where an algorithm during trading is faced with new data on a continuous basis. The approach used is the same as that applied to the sample data in "Traintest splits: Support vector machines". Based on this approach, the SVM algorithm shows again the best performance out-of-sample (see Figure 15-16): In [98]: **from sklearn.model\_selection import** train\_test\_split In [99]: train, test = train\_test\_split(data, test\_size=0.5, shuffle=True, random\_state=100) In [100]: train = train.copy().sort\_index() In [101]: train[cols\_bin].head() Out[101]: lag\_1\_bin lag\_2\_bin lag\_3\_bin lag\_4\_bin lag\_5\_bin Date 2010-01-12 3 3 0 2 1 2010-01-13 1 3 3 0 2 2010-01-14 2 1 3 3 0 2010-01-15 1 2 1 3 3 2010-01-20 1 0 1 2 1 In [102]: test = test.copy().sort\_index() In [103]: fit\_models(train) In [104]: derive\_positions(test) In [105]: evaluate\_strats(test) In [106]: test[sel].sum().apply(np.exp) Out[106]: returns 0.878078 strat\_log\_reg 0.735893 strat\_gauss\_nb 0.765009 strat\_svm 0.695428 dtype: float64 In [107]: test[sel].cumsum().apply(np.exp).plot(figsize=(10, 6));

Train and test data sets are copied and brought back in temporal order.

![](_page_41_Figure_0.jpeg)

*Figure 15-16. Performance of EUR/USD and classification-based trading strategies (randomized traintest split)*

# **Deep Neural Networks**

Deep neural networks (DNNs) try to emulate the functioning of the human brain. They are in general composed of an input layer (the features), an output layer (the labels), and a number of hidden layers. The presence of hidden layers is what makes a neural network *deep*. It allows it to learn more complex relationships and to perform better on a number of problem types. When applying DNNs one generally speaks of *deep learning* instead of machine learning. For an introduction to this field, refer to Géron (2017) or Gibson and Patterson (2017).

### **DNNs with scikit-learn**

This section applies the MLPClassifier algorithm from scikit-learn, as introduced in "Deep neural networks". First, it is trained and tested on the whole data set, using the digitized features. The algorithm achieves exceptional performance in-sample (see Figure 15-17), which illustrates the power of DNNs for this type of problem. It also hints at strong overfitting, since the performance indeed seems unrealistically good:

```
In [108]: from sklearn.neural_network import MLPClassifier
In [109]: model = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                hidden_layer_sizes=2 * [250],
                                random_state=1)
In [110]: %time model.fit(data[cols_bin], data['direction'])
          CPU times: user 16.1 s, sys: 156 ms, total: 16.2 s
          Wall time: 9.85 s
Out[110]: MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
           beta_1=0.9,
                 beta_2=0.999, early_stopping=False, epsilon=1e-08,
                 hidden_layer_sizes=[250, 250], learning_rate='constant',
                 learning_rate_init=0.001, max_iter=200, momentum=0.9,
                 n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
                 random_state=1, shuffle=True, solver='lbfgs', tol=0.0001,
                 validation_fraction=0.1, verbose=False, warm_start=False)
In [111]: data['pos_dnn_sk'] = model.predict(data[cols_bin])
In [112]: data['strat_dnn_sk'] = data['pos_dnn_sk'] * data['returns']
In [113]: data[['returns', 'strat_dnn_sk']].sum().apply(np.exp)
Out[113]: returns 0.805002
          strat_dnn_sk 35.156677
          dtype: float64
In [114]: data[['returns', 'strat_dnn_sk']].cumsum().apply(
                      np.exp).plot(figsize=(10, 6));
```

![](_page_44_Figure_0.jpeg)

*Figure 15-17. Performance of EUR/USD and DNN-based trading strategy (scikit-learn, in-sample)*

To avoid overfitting of the DNN model, a randomized train-test split is applied next. The algorithm again outperforms the passive benchmark investment and achieves a positive absolute performance (Figure 15-18). However, the results seem more realistic now:

```
In [115]: train, test = train_test_split(data, test_size=0.5,
                                         random_state=100)
In [116]: train = train.copy().sort_index()
In [117]: test = test.copy().sort_index()
In [118]: model = MLPClassifier(solver='lbfgs', alpha=1e-5, max_iter=500,
                               hidden_layer_sizes=3 * [500], random_state=1)
In [119]: %time model.fit(train[cols_bin], train['direction'])
          CPU times: user 2min 26s, sys: 1.02 s, total: 2min 27s
          Wall time: 1min 31s
Out[119]: MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
           beta_1=0.9,
                 beta_2=0.999, early_stopping=False, epsilon=1e-08,
                 hidden_layer_sizes=[500, 500, 500], learning_rate='constant',
                 learning_rate_init=0.001, max_iter=500, momentum=0.9,
                 n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
                 random_state=1, shuffle=True, solver='lbfgs', tol=0.0001,
                 validation_fraction=0.1, verbose=False, warm_start=False)
```

```
In [120]: test['pos_dnn_sk'] = model.predict(test[cols_bin])
In [121]: test['strat_dnn_sk'] = test['pos_dnn_sk'] * test['returns']
In [122]: test[['returns', 'strat_dnn_sk']].sum().apply(np.exp)
Out[122]: returns 0.878078
         strat_dnn_sk 1.242042
         dtype: float64
In [123]: test[['returns', 'strat_dnn_sk']].cumsum(
                     ).apply(np.exp).plot(figsize=(10, 6));
```

Increases the number of hidden layers and hidden units.

![](_page_45_Figure_3.jpeg)

*Figure 15-18. Performance of EUR/USD and DNN-based trading strategy (scikit-learn, randomized traintest split)*

### **DNNs with TensorFlow**

TensorFlow has become a popular package for deep learning. It is developed and supported by Google Inc. and applied there to a great variety of machine learning problems. Zedah and Ramsundar (2018) cover TensorFlow for deep learning in depth.

As with scikit-learn, the application of the DNNClassifier algorithm from TensorFlow to derive an algorithmic trading strategy is straightforward given the background from "Deep neural networks". The training and test data is the same as before. First, the training of the model. In-sample, the algorithm outperforms the passive benchmark investment and shows a considerable absolute return (see Figure 15-19), again hinting at overfitting:

```
In [124]: import tensorflow as tf
          tf.logging.set_verbosity(tf.logging.ERROR)
In [125]: fc = [tf.contrib.layers.real_valued_column('lags', dimension=lags)]
In [126]: model = tf.contrib.learn.DNNClassifier(hidden_units=3 * [500],
                                                 n_classes=len(bins) + 1,
                                                 feature_columns=fc)
In [127]: def input_fn():
              fc = {'lags': tf.constant(data[cols_bin].values)}
              la = tf.constant(data['direction'].apply(
                               lambda x: 0 if x < 0 else 1).values,
                               shape=[data['direction'].size, 1])
              return fc, la
In [128]: %time model.fit(input_fn=input_fn, steps=250)
          CPU times: user 2min 7s, sys: 8.85 s, total: 2min 16s
          Wall time: 49 s
Out[128]: DNNClassifier(params={'head':
           <tensorflow.contrib.learn.python.learn.estimators.head._MultiClassHead
           object at 0x1a19acf898>, 'hidden_units': [500, 500, 500],
           'feature_columns': (_RealValuedColumn(column_name='lags', dimension=5,
           default_value=None, dtype=tf.float32, normalizer=None),), 'optimizer':
           None, 'activation_fn': <function relu at 0x1161441e0>, 'dropout':
           None, 'gradient_clip_norm': None, 'embedding_lr_multipliers': None,
           'input_layer_min_slice_size': None})
In [129]: model.evaluate(input_fn=input_fn, steps=1)
Out[129]: {'loss': 0.6879357, 'accuracy': 0.5379925, 'global_step': 250}
In [130]: pred = np.array(list(model.predict(input_fn=input_fn)))
          pred[:10]
Out[130]: array([0, 0, 0, 0, 0, 1, 0, 1, 1, 0])
In [131]: data['pos_dnn_tf'] = np.where(pred > 0, 1, -1)
```

```
In [132]: data['strat_dnn_tf'] = data['pos_dnn_tf'] * data['returns']
In [133]: data[['returns', 'strat_dnn_tf']].sum().apply(np.exp)
Out[133]: returns 0.805002
         strat_dnn_tf 2.437222
         dtype: float64
In [134]: data[['returns', 'strat_dnn_tf']].cumsum(
                     ).apply(np.exp).plot(figsize=(10, 6));
```

The time needed for training might be considerable.

The binary predictions (0, 1) …

… need to be transformed to market positions (-1, +1).

![](_page_47_Figure_7.jpeg)

```
Figure 15-19. Performance of EUR/USD and DNN-based trading strategy (TensorFlow, in-sample)
```

The following code again implements a randomized train-test split to get a more realistic view of the performance of the DNN-based algorithmic trading strategy. The performance is, as expected, worse out-of-sample (see Figure 15-20). In addition, given the specific parameterization the TensorFlow DNNClassifier

underperforms the scikit-learn MLPClassifier algorithm by quite few percentage points:

```
In [135]: model = tf.contrib.learn.DNNClassifier(hidden_units=3 * [500],
                                                 n_classes=len(bins) + 1,
                                                 feature_columns=fc)
In [136]: data = train
In [137]: %time model.fit(input_fn=input_fn, steps=2500)
          CPU times: user 11min 7s, sys: 1min 7s, total: 12min 15s
          Wall time: 4min 27s
Out[137]: DNNClassifier(params={'head':
           <tensorflow.contrib.learn.python.learn.estimators.head._MultiClassHead
           object at 0x116828cc0>, 'hidden_units': [500, 500, 500],
           'feature_columns': (_RealValuedColumn(column_name='lags', dimension=5,
           default_value=None, dtype=tf.float32, normalizer=None),), 'optimizer':
           None, 'activation_fn': <function relu at 0x1161441e0>, 'dropout':
           None, 'gradient_clip_norm': None, 'embedding_lr_multipliers': None,
           'input_layer_min_slice_size': None})
In [138]: data = test
In [139]: model.evaluate(input_fn=input_fn, steps=1)
Out[139]: {'loss': 0.82882184, 'accuracy': 0.48968107, 'global_step': 2500}
In [140]: pred = np.array(list(model.predict(input_fn=input_fn)))
In [141]: test['pos_dnn_tf'] = np.where(pred > 0, 1, -1)
In [142]: test['strat_dnn_tf'] = test['pos_dnn_tf'] * test['returns']
In [143]: test[['returns', 'strat_dnn_sk', 'strat_dnn_tf']].sum().apply(np.exp)
Out[143]: returns 0.878078
          strat_dnn_sk 1.242042
          strat_dnn_tf 1.063968
          dtype: float64
In [144]: test[['returns', 'strat_dnn_sk', 'strat_dnn_tf']].cumsum(
                      ).apply(np.exp).plot(figsize=(10, 6));
```

![](_page_49_Figure_0.jpeg)

*Figure 15-20. Performance of EUR/USD and DNN-based trading strategy (TensorFlow, randomized traintest split)*

### **PERFORMANCE RESULTS**

All performance results shown for the different algorithmic trading strategies from vectorized backtesting so far are illustrative only. Beyond the simplifying assumption of no transaction costs, the results depend on a number of other (mostly arbitrarily chosen) parameters. They also depend on the relative small end-of-day price data set used throughout for the EUR/USD exchange rate. The focus lies on illustrating the application of different approaches and ML algorithms to financial data, not on deriving a robust algorithmic trading strategy to be deployed in practice. The next chapter addresses some of these issues.

# **Conclusion**

This chapter is about algorithmic trading strategies and judging their performance based on vectorized backtesting. It starts with a rather simple algorithmic trading strategy based on two simple moving averages, a type of strategy known and used in practice for decades. This strategy is used to illustrate vectorized backtesting, making heavy use of the vectorization capabilities of NumPy and pandas for data analysis.

Using OLS regression, the chapter also illustrates the random walk hypothesis on the basis of a real financial time series. This is the benchmark against which any algorithmic trading strategy must prove its worth.

The core of the chapter is the application of machine learning algorithms, as introduced in "Machine Learning". A number of algorithms, the majority of which are of classification type, are used and applied based on mostly the same "rhythm." As features, lagged log returns data is used in a number of variants although this is a restriction that for sure is not necessary. It is mostly done for convenience and simplicity. In addition, the analysis is based on a number of simplifying assumptions since the focus is mainly on the technical aspects of applying machine learning algorithms to financial time series data to predict the direction of financial market movements.
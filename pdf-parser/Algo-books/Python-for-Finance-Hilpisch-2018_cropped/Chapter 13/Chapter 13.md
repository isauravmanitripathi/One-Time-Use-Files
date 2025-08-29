# **Chapter 13. Statistics**

I can prove anything by statistics except the truth. George Canning

Statistics is a vast field, but the tools and results it provides have become indispensable for finance. This explains the popularity of domain-specific languages like [R](https://www.r-project.org/) in the finance industry. The more elaborate and complex statistical models become, the more important it is to have available easy-to-use and high-performing computational solutions.

A single chapter in a book like this one cannot do justice to the richness and depth of the field of statistics. Therefore, the approach — as in many other chapters — is to focus on selected topics that seem of importance or that provide a good starting point when it comes to the use of Python for the particular tasks at hand. The chapter has four focal points: "Normality Tests"

A large number of important financial models, like modern or meanvariance portfolio theory (MPT) and the capital asset pricing model (CAPM), rest on the assumption that returns of securities are normally distributed. Therefore, this chapter presents approaches to test a given time series for normality of returns.

## *"Portfolio Optimization"*

MPT can be considered one of the biggest successes of statistics in finance. Starting in the early 1950s with the work of pioneer Harry Markowitz, this theory began to replace people's reliance on judgment and experience with rigorous mathematical and statistical methods when it comes to the investment of money in financial markets. In that sense, it is maybe the first real quantitative model and approach in finance.

## *"Bayesian Statistics"*

On a conceptual level, Bayesian statistics introduces the notion of *beliefs* of agents and the *updating of beliefs* to statistics. When it comes to linear regression, for example, this might take the form of having a statistical distribution for regression parameters instead of single point estimates (e.g., for the intercept and slope of the regression line). Nowadays, Bayesian

methods are widely used in finance, which is why this section illustrates Bayesian methods based on some examples.

# *"Machine Learning"*

Machine learning (or statistical learning) is based on advanced statistical methods and is considered a subdiscipline of artificial intelligence (AI). Like statistics itself, machine learning offers a rich set of approaches and models to learn from data sets and create predictions based on what is learned. Different algorithms of learning are distinguished, such as those for *supervised learning* or *unsupervised learning*. The types of problems solved by the algorithms differ as well, such as *estimation* or *classification*. The examples presented in this chapter fall in the category of *supervised learning for classification*.

Many aspects in this chapter relate to date and/or time information. Refer to Appendix A for an overview of handling such data with Python, NumPy, and pandas.

# **Normality Tests**

The *normal distribution* can be considered the most important distribution in finance and one of the major statistical building blocks of financial theory. Among others, the following cornerstones of financial theory rest to a large extent on the assumption that returns of a financial instrument are normally distributed: 1

## *Portfolio theory*

When stock returns are normally distributed, optimal portfolio choice can be cast into a setting where only the (expected) *mean return* and the *variance of the returns* (or the volatility) as well as the *covariances* between different stocks are relevant for an investment decision (i.e., an optimal portfolio composition).

## *Capital asset pricing model*

Again, when stock returns are normally distributed, prices of single stocks can be elegantly expressed in linear relationship to a broad market index; the relationship is generally expressed by a measure for the co-movement of a single stock with the market index called beta or β.

## *Efficient markets hypothesis*

An *efficient* market is a market where prices reflect all available information, where "all" can be defined more narrowly or more widely (e.g., as in "all publicly available" information vs. including also "only privately available" information). If this hypothesis holds true, then stock prices fluctuate randomly and returns are normally distributed.

## *Option pricing theory*

Brownian motion is *the* benchmark model for the modeling of random price movements of financial instruments; the famous Black-Scholes-Merton option pricing formula uses a geometric Brownian motion as the model for a stock's random price fluctuations over time, leading to log-normally distributed prices and normally distributed returns.

This by far nonexhaustive list underpins the importance of the normality assumption in finance.

# **Benchmark Case**

To set the stage for further analyses, the analysis starts with the geometric Brownian motion as one of the canonical stochastic processes used in financial modeling. The following can be said about the characteristics of paths from a geometric Brownian motion *S*:

*Normal log returns*

Log returns between two times 0 < *s* < *t* are *normally* distributed.

*Log-normal values*

At any time *t* > 0, the values are *log-normally* distributed.

For what follows, the plotting setup is taken care of first. Then a number of Python packages, including [scipy.stats](http://docs.scipy.org/doc/scipy/reference/stats.html) and [statsmodels.api](http://statsmodels.sourceforge.net/stable/), are imported:

```
In [1]: import math
        import numpy as np
        import scipy.stats as scs
        import statsmodels.api as sm
        from pylab import mpl, plt
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
```

The following uses the function gen\_paths() to generate sample Monte Carlo paths for the geometric Brownian motion (see also Chapter 12):

```
In [3]: def gen_paths(S0, r, sigma, T, M, I):
            ''' Generate Monte Carlo paths for geometric Brownian motion.
            Parameters
            ==========
            S0: float
                initial stock/index value
            r: float
                constant short rate
            sigma: float
                constant volatility
            T: float
                final time horizon
            M: int
                number of time steps/intervals
            I: int
                number of paths to be simulated
```

```
Returns
=======
paths: ndarray, shape (M + 1, I)
    simulated paths given the parameters
'''dt = T / M
paths = np.zeros((M + 1, I))
paths[0] = S0
for t in range(1, M + 1):
    rand = np.random.standard_normal(I)
    rand = (rand - rand.mean()) / rand.std()
    paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt +
                                     sigma * math.sqrt(dt) * rand)
return paths
```

Matching first and second moment.

Vectorized Euler discretization of geometric Brownian motion.

The simulation is based on the parameterization for the Monte Carlo simulation as shown here, generating, in combination with the function gen\_paths(), 250,000 paths with 50 time steps each. Figure 13-1 shows the first 10 simulated paths:

```
In [4]: S0 = 100.
        r = 0.05
        sigma = 0.2
        T = 1.0
        M = 50
        I = 250000
        np.random.seed(1000)
In [5]: paths = gen_paths(S0, r, sigma, T, M, I)
In [6]: S0 * math.exp(r * T)
Out[6]: 105.12710963760242
In [7]: paths[-1].mean()
Out[7]: 105.12645392478755
In [8]: plt.figure(figsize=(10, 6))
        plt.plot(paths[:, :10])
        plt.xlabel('time steps')
        plt.ylabel('index level');
```

Initial value for simulated processes.

Constant short rate.

Constant short rate.

Constant volatility factor.

Time horizon in year fractions.

Number of time intervals.

Number of simulated processes.

Expected value and average simulated value.

![](_page_5_Figure_11.jpeg)

*Figure 13-1. Ten simulated paths of geometric Brownian motion*

The main interest is in the distribution of the log returns. To this end, an ndarray object with all the log returns is created based on the simulated paths. Here, a single simulated path and the resulting log returns are shown:

In [9]: paths[:, 0].round(4)

```
Out[9]: array([100. , 97.821 , 98.5573, 106.1546, 105.899 , 99.8363,
              100.0145, 102.6589, 105.6643, 107.1107, 108.7943, 108.2449,
              106.4105, 101.0575, 102.0197, 102.6052, 109.6419, 109.5725,
              112.9766, 113.0225, 112.5476, 114.5585, 109.942 , 112.6271,
              112.7502, 116.3453, 115.0443, 113.9586, 115.8831, 117.3705,
              117.9185, 110.5539, 109.9687, 104.9957, 108.0679, 105.7822,
              105.1585, 104.3304, 108.4387, 105.5963, 108.866 , 108.3284,
              107.0077, 106.0034, 104.3964, 101.0637, 98.3776, 97.135 ,
               95.4254, 96.4271, 96.3386])
In [10]: log_returns = np.log(paths[1:] / paths[:-1])
In [11]: log_returns[:, 0].round(4)
Out[11]: array([-0.022 , 0.0075, 0.0743, -0.0024, -0.059 , 0.0018, 0.0261,
                0.0289, 0.0136, 0.0156, -0.0051, -0.0171, -0.0516, 0.0095,
                0.0057, 0.0663, -0.0006, 0.0306, 0.0004, -0.0042, 0.0177,
               -0.0411, 0.0241, 0.0011, 0.0314, -0.0112, -0.0095, 0.0167,
                0.0128, 0.0047, -0.0645, -0.0053, -0.0463, 0.0288, -0.0214,
               -0.0059, -0.0079, 0.0386, -0.0266, 0.0305, -0.0049, -0.0123,
               -0.0094, -0.0153, -0.0324, -0.0269, -0.0127, -0.0178, 0.0104,
               -0.0009])
```

This is something one might experience in financial markets as well: days when one makes a *positive return* on an investment and other days when one is *losing money* relative to the most recent wealth position.

The function print\_statistics() is a wrapper function for the scs.describe() function from the scipy.stats subpackage. It mainly generates a better (human-)readable output for such statistics as the mean, the skewness, or the kurtosis of a given (historical or simulated) data set:

```
In [13]: def print_statistics(array):
             ''' Prints selected statistics.
            Parameters
            ==========
            array: ndarray
                object to generate statistics on
             '''sta = scs.describe(array)
            print('%14s %15s' % ('statistic', 'value'))
            print(30 * '-')
            print('%14s %15.5f' % ('size', sta[0]))
            print('%14s %15.5f' % ('min', sta[1][0]))
            print('%14s %15.5f' % ('max', sta[1][1]))
            print('%14s %15.5f' % ('mean', sta[2]))
            print('%14s %15.5f' % ('std', np.sqrt(sta[3])))
            print('%14s %15.5f' % ('skew', sta[4]))
            print('%14s %15.5f' % ('kurtosis', sta[5]))
In [14]: print_statistics(log_returns.flatten())
             statistic value
        ------------------------------
                  size 12500000.00000
                   min -0.15664
                   max 0.15371
                  mean 0.00060
```

```
std 0.02828
                 skew 0.00055
             kurtosis 0.00085
In [15]: log_returns.mean() * M + 0.5 * sigma ** 2
Out[15]: 0.05000000000000005
In [16]: log_returns.std() * math.sqrt(M)
Out[16]: 0.20000000000000015
```

Annualized mean log return after correction for the Itô term. 2

Annualized volatility; i.e., annualized standard deviation of log returns.

The data set in this case consists of 12,500,000 data points with the values mainly lying between +/– 0.15. One would expect annualized values of 0.05 for the mean return (after correcting for the Itô term) and 0.2 for the standard deviation (volatility). The annualized values almost match these values perfectly (multiply the mean value by 50 and correct it for the Itô term; multiply the standard deviation by ). One reason for the good match is the use of moment matching for variance reduction when drawing the random numbers (see "Variance Reduction").

Figure 13-2 compares the frequency distribution of the simulated log returns with the probability density function (PDF) of the normal distribution given the parameterizations for r and sigma. The function used is norm.pdf() from the scipy.stats subpackage. There is obviously quite a good fit:

```
In [17]: plt.figure(figsize=(10, 6))
         plt.hist(log_returns.flatten(), bins=70, normed=True,
                  label='frequency', color='b')
         plt.xlabel('log return')
         plt.ylabel('frequency')
         x = np.linspace(plt.axis()[0], plt.axis()[1])
         plt.plot(x, scs.norm.pdf(x, loc=r / M, scale=sigma / np.sqrt(M)),
                  'r', lw=2.0, label='pdf')
         plt.legend();
```

Plots the PDF for the assumed parameters scaled to the interval length.

![](_page_8_Figure_0.jpeg)

*Figure 13-2. Histogram of log returns of geometric Brownian motion and normal density function*

Comparing a frequency distribution (histogram) with a theoretical PDF is not the only way to graphically "test" for normality. So-called *quantile-quantile (QQ) plots* are also well suited for this task. Here, sample quantile values are compared to theoretical quantile values. For normally distributed sample data sets, such a plot might look like Figure 13-3, with the absolute majority of the quantile values (dots) lying on a straight line:

```
In [18]: sm.qqplot(log_returns.flatten()[::500], line='s')
         plt.xlabel('theoretical quantiles')
         plt.ylabel('sample quantiles');
```

![](_page_9_Figure_0.jpeg)

*Figure 13-3. Quantile-quantile plot for log returns of geometric Brownian motion*

However appealing the graphical approaches might be, they generally cannot replace more rigorous testing procedures. The function normality\_tests() used in the next example combines three different statistical tests:

## *Skewness test (skewtest())*

This tests whether the skew of the sample data is "normal" (i.e., has a value close enough to zero).

## *Kurtosis test (kurtosistest())*

Similarly, this tests whether the kurtosis of the sample data is "normal" (again, close enough to zero).

## *Normality test (normaltest())*

This combines the other two test approaches to test for normality.

The test values indicate that the log returns of the geometric Brownian motion are indeed normally distributed — i.e., they show *p*-values of 0.05 or above:

```
In [19]: def normality_tests(arr):
```

```
''' Tests for normality distribution of given data set.
            Parameters
            ==========
            array: ndarray
               object to generate statistics on
            '''print('Skew of data set %14.3f' % scs.skew(arr))
            print('Skew test p-value %14.3f' % scs.skewtest(arr)[1])
            print('Kurt of data set %14.3f' % scs.kurtosis(arr))
            print('Kurt test p-value %14.3f' % scs.kurtosistest(arr)[1])
            print('Norm test p-value %14.3f' % scs.normaltest(arr)[1])
In [20]: normality_tests(log_returns.flatten())
        Skew of data set 0.001
        Skew test p-value 0.430
        Kurt of data set 0.001
        Kurt test p-value 0.541
        Norm test p-value 0.607
```

All *p*-values are well above 0.05.

Finally, a check whether the end-of-period values are indeed log-normally distributed. This boils down to a normality test, since one only has to transform the data by applying the log function to it to then arrive at normally distributed values (or maybe not). Figure 13-4 plots both the log-normally distributed endof-period values and the transformed ones ("log index level"):

```
In [21]: f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
         ax1.hist(paths[-1], bins=30)
         ax1.set_xlabel('index level')
         ax1.set_ylabel('frequency')
         ax1.set_title('regular data')
         ax2.hist(np.log(paths[-1]), bins=30)
         ax2.set_xlabel('log index level')
         ax2.set_title('log data')
```

![](_page_11_Figure_0.jpeg)

*Figure 13-4. Histogram of simulated end-of-period index levels for geometric Brownian motion*

The statistics for the data set show expected behavior — for example, a mean value close to 105. The log index level values have skew and kurtosis values close to zero and they show high *p*-values, providing strong support for the normal distribution hypothesis:

```
In [22]: print_statistics(paths[-1])
           statistic value
       ------------------------------
              size 250000.00000
               min 42.74870
               max 233.58435
              mean 105.12645
               std 21.23174
              skew 0.61116
           kurtosis 0.65182
In [23]: print_statistics(np.log(paths[-1]))
           statistic value
       ------------------------------
              size 250000.00000
               min 3.75534
               max 5.45354
              mean 4.63517
               std 0.19998
              skew -0.00092
           kurtosis -0.00327
```

|  | In [24]: normality_tests(np.log(paths[-1])) |        |  |
|--|---------------------------------------------|--------|--|
|  | Skew of data set                            | -0.001 |  |
|  | Skew test p-value                           | 0.851  |  |
|  | Kurt of data set                            | -0.003 |  |
|  | Kurt test p-value                           | 0.744  |  |
|  | Norm test p-value                           | 0.931  |  |
|  |                                             |        |  |

[Figure](#page-12-0) 13-5 compares again the frequency distribution with the PDF of the normal distribution, showing a pretty good fit (as now is, of course, to be expected):

```
In [25]: plt.figure(figsize=(10, 6))
         log_data = np.log(paths[-1])
         plt.hist(log_data, bins=70, normed=True,
                  label='observed', color='b')
         plt.xlabel('index levels')
         plt.ylabel('frequency')
         x = np.linspace(plt.axis()[0], plt.axis()[1])
         plt.plot(x, scs.norm.pdf(x, log_data.mean(), log_data.std()),
                  'r', lw=2.0, label='pdf')
         plt.legend();
```

<span id="page-12-0"></span>![](_page_12_Figure_3.jpeg)

*Figure 13-5. Histogram of log index levels of geometric Brownian motion and normal density function*

Figure 13-6 also supports the hypothesis that the log index levels are normally distributed:

![](_page_13_Figure_0.jpeg)

*Figure 13-6. Quantile-quantile plot for log index levels of geometric Brownian motion*

## **NORMALITY**

The normality assumption with regard to the uncertain returns of financial instruments is central to a number of financial theories. Python provides efficient statistical and graphical means to test whether time series data is normally distributed or not.

# **Real-World Data**

This section analyzes four historical financial time series, two for technology stocks and two for exchange traded funds (ETFs):

- APPL.O: Apple Inc. stock price
- MSFT.O: Microsoft Inc. stock price
- SPY: SPDR S&P 500 ETF Trust
- GLD: SPDR Gold Trust

The data management tool of choice is pandas (see Chapter 8). Figure 13-7 shows the normalized prices over time:

```
In [27]: import pandas as pd
In [28]: raw = pd.read_csv('../../source/tr_eikon_eod_data.csv',
                        index_col=0, parse_dates=True).dropna()
In [29]: symbols = ['SPY', 'GLD', 'AAPL.O', 'MSFT.O']
In [30]: data = raw[symbols]
        data = data.dropna()
In [31]: data.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 2138 entries, 2010-01-04 to 2018-06-29
        Data columns (total 4 columns):
        SPY 2138 non-null float64
        GLD 2138 non-null float64
        AAPL.O 2138 non-null float64
        MSFT.O 2138 non-null float64
        dtypes: float64(4)
        memory usage: 83.5 KB
In [32]: data.head()
Out[32]: SPY GLD AAPL.O MSFT.O
        Date
        2010-01-04 113.33 109.80 30.572827 30.950
```

| 2010-01-05 | 113.63 | 109.70 | 30.625684 | 30.960 |
|------------|--------|--------|-----------|--------|
| 2010-01-06 | 113.71 | 111.51 | 30.138541 | 30.770 |
| 2010-01-07 | 114.19 | 110.82 | 30.082827 | 30.452 |
| 2010-01-08 | 114.57 | 111.37 | 30.282827 | 30.660 |

```
In [33]: (data / data.iloc[0] * 100).plot(figsize=(10, 6))
```

![](_page_16_Figure_2.jpeg)

*Figure 13-7. Normalized prices of financial instruments over time*

Figure 13-8 shows the log returns of the financial instruments as histograms:

```
In [34]: log_returns = np.log(data / data.shift(1))
       log_returns.head()
Out[34]: SPY GLD AAPL.O MSFT.O
       Date
       2010-01-04 NaN NaN NaN NaN
       2010-01-05 0.002644 -0.000911 0.001727 0.000323
       2010-01-06 0.000704 0.016365 -0.016034 -0.006156
       2010-01-07 0.004212 -0.006207 -0.001850 -0.010389
       2010-01-08 0.003322 0.004951 0.006626 0.006807
```

In [35]: log\_returns.hist(bins=50, figsize=(10, 8));

![](_page_17_Figure_0.jpeg)

As a next step, consider the different statistics for the time series data sets. The kurtosis values seem to be especially far from normal for all four data sets:

```
In [36]: for sym in symbols:
           print('\nResults for symbol {}'.format(sym))
           print(30 * '-')
           log_data = np.array(log_returns[sym].dropna())
           print_statistics(log_data)
       Results for symbol SPY
       ------------------------------
            statistic value
       ------------------------------
                size 2137.00000
                 min -0.06734
                 max 0.04545
                mean 0.00041
                 std 0.00933
                skew -0.52189
             kurtosis 4.52432
```

| Results for symbol GLD                                                        |                        |  |
|-------------------------------------------------------------------------------|------------------------|--|
| ------------------------------<br>statistic<br>------------------------------ | value                  |  |
| size<br>min                                                                   | 2137.00000<br>-0.09191 |  |
| max                                                                           | 0.04795                |  |
| mean                                                                          | 0.00004                |  |
| std                                                                           | 0.01020                |  |
| skew                                                                          | -0.59934               |  |
| kurtosis                                                                      | 5.68423                |  |
| Results for symbol AAPL.O<br>------------------------------                   |                        |  |
| statistic                                                                     | value                  |  |
| ------------------------------                                                |                        |  |
| size                                                                          | 2137.00000             |  |
| min                                                                           | -0.13187               |  |
| max                                                                           | 0.08502                |  |
| mean                                                                          | 0.00084                |  |
| std                                                                           | 0.01591                |  |
| skew                                                                          | -0.23510               |  |
| kurtosis                                                                      | 4.78964                |  |
| Results for symbol MSFT.O<br>------------------------------                   |                        |  |
| statistic                                                                     | value                  |  |
| ------------------------------                                                |                        |  |
| size                                                                          | 2137.00000             |  |
| min                                                                           | -0.12103               |  |
| max                                                                           | 0.09941                |  |
| mean                                                                          | 0.00054                |  |
| std                                                                           | 0.01421                |  |
| skew                                                                          | -0.09117               |  |
| kurtosis                                                                      | 7.29106                |  |

Statistics for time series of financial instruments.

Figure 13-9 shows the QQ plot for the SPY ETF. Obviously, the sample quantile values do not lie on a straight line, indicating "non-normality." On the left and right sides there are many values that lie well below the line and well above the line, respectively. In other words, the time series data exhibits *fat tails*. This term refers to a (frequency) distribution where large negative and positive values are observed more often than a normal distribution would imply. The same conclusions can be drawn from Figure 13-10, which presents the data for the Microsoft stock. There also seems to be evidence for a fat-tailed distribution:

```
In [37]: sm.qqplot(log_returns['SPY'].dropna(), line='s')
         plt.title('SPY')
         plt.xlabel('theoretical quantiles')
         plt.ylabel('sample quantiles');
```

```
<pre>In [38]: sm.qqplot(log_returns['MSFT.0'].dropna(), line='s')
```

![](_page_20_Figure_0.jpeg)

*Figure 13-9. Quantile-quantile plot for SPY log returns*

![](_page_21_Figure_0.jpeg)

*Figure 13-10. Quantile-quantile plot for MSFT.O log returns*

This finally leads to the statistical normality tests:

```
In [39]: for sym in symbols:
           print('\nResults for symbol {}'.format(sym))
           print(32 * '-')
           log_data = np.array(log_returns[sym].dropna())
           normality_tests(log_data)
       Results for symbol SPY
       --------------------------------
       Skew of data set -0.522
       Skew test p-value 0.000
       Kurt of data set 4.524
       Kurt test p-value 0.000
       Norm test p-value 0.000
       Results for symbol GLD
       --------------------------------
       Skew of data set -0.599
       Skew test p-value 0.000
       Kurt of data set 5.684
       Kurt test p-value 0.000
       Norm test p-value 0.000
       Results for symbol AAPL.O
       --------------------------------
```

| Skew of data set                 | -0.235 |  |  |  |
|----------------------------------|--------|--|--|--|
| Skew test p-value                | 0.000  |  |  |  |
| Kurt of data set                 | 4.790  |  |  |  |
| Kurt test p-value                | 0.000  |  |  |  |
| Norm test p-value                | 0.000  |  |  |  |
|                                  |        |  |  |  |
| Results for symbol MSFT.O        |        |  |  |  |
| -------------------------------- |        |  |  |  |
| Skew of data set                 | -0.091 |  |  |  |
| Skew test p-value                | 0.085  |  |  |  |
| Kurt of data set                 | 7.291  |  |  |  |
| Kurt test p-value                | 0.000  |  |  |  |
| Norm test p-value                | 0.000  |  |  |  |

Normality test results for the times series of the financial instruments.

The *p*-values of the different tests are all zero, *strongly rejecting the test hypothesis* that the different sample data sets are normally distributed. This shows that the normal assumption for stock market returns and other asset classes — as, for example, embodied in the geometric Brownian motion model — cannot be justified in general and that one might have to use richer models that are able to generate fat tails (e.g., jump diffusion models or models with stochastic volatility).

# **Portfolio Optimization**

Modern or mean-variance portfolio theory is a major cornerstone of financial theory. Based on this theoretical breakthrough the Nobel Prize in Economics was awarded to its inventor, Harry Markowitz, in 1990. Although formulated in the 1950s, it is still a theory taught to finance students and applied in practice today (often with some minor or major modifications). <sup>3</sup> This section illustrates the fundamental principles of the theory.

Chapter 5 in the book by Copeland, Weston, and Shastri (2005) provides an introduction to the formal topics associated with MPT. As pointed out previously, the assumption of normally distributed returns is fundamental to the theory:

By looking only at mean and variance, we are necessarily assuming that no other statistics are necessary to describe the distribution of end-of-period wealth. Unless investors have a special type of utility function (quadratic utility function), it is necessary to assume that returns have a normal distribution, which can be completely described by mean and variance.

# **The Data**

The analysis and examples that follow use the same financial instruments as before. The basic idea of MPT is to make use of *diversification* to achieve a minimal portfolio risk given a target return level or a maximum portfolio return given a certain level of risk. One would expect such diversification effects for the right combination of a larger number of assets and a certain diversity in the assets. However, to convey the basic ideas and to show typical effects, four financial instruments shall suffice. Figure 13-11 shows the frequency distribution of the log returns for the financial instruments:

```
In [40]: symbols = ['AAPL.O', 'MSFT.O', 'SPY', 'GLD']
In [41]: noa = len(symbols)
In [42]: data = raw[symbols]
In [43]: rets = np.log(data / data.shift(1))
In [44]: rets.hist(bins=40, figsize=(10, 8));
```

Four financial instruments for portfolio composition.

Number of financial instruments defined.

The *covariance matrix* for the financial instruments to be invested in is the central piece of the portfolio selection process. pandas has a built-in method to generate the covariance matrix on which the same scaling factor is applied:

```
In [45]: rets.mean() * 252
Out[45]: AAPL.O 0.212359
       MSFT.O 0.136648
       SPY 0.102928
       GLD 0.009141
       dtype: float64
In [46]: rets.cov() * 252
Out[46]: AAPL.O MSFT.O SPY GLD
       AAPL.O 0.063773 0.023427 0.021039 0.001513
       MSFT.O 0.023427 0.050917 0.022244 -0.000347
       SPY 0.021039 0.022244 0.021939 0.000062
       GLD 0.001513 -0.000347 0.000062 0.026209
```

Annualized mean returns.

Annualized covariance matrix.

![](_page_26_Figure_0.jpeg)

*Figure 13-11. Histograms of log returns of financial instruments*

# **The Basic Theory**

In what follows, it is assumed that an investor is not allowed to set up short positions in a financial instrument. Only long positions are allowed, which implies that 100% of the investor's wealth has to be divided among the available instruments in such a way that all positions are long (positive) *and* that the positions add up to 100%. Given the four instruments, one could, for example, invest equal amounts into every such instrument — i.e., 25% of the available wealth in each. The following code generates four uniformly distributed random numbers between 0 and 1 and then normalizes the values such that the sum of all values equals 1:

```
In [47]: weights = np.random.random(noa)
         weights /= np.sum(weights)
In [48]: weights
Out[48]: array([0.07650728, 0.06021919, 0.63364218, 0.22963135])
In [49]: weights.sum()
Out[49]: 1.0
```

Random portfolio weights …

… normalized to 1 or 100%.

As verified here, the weights indeed add up to 1; i.e., , where *I* is the number of financial instruments and is the weight of financial instrument *i*. Equation 13-1 provides the formula for the *expected portfolio return* given the weights for the single instruments. This is an *expected* portfolio return in the sense that historical mean performance is assumed to be the best estimator for future (expected) performance. Here, the are the state-dependent future returns (vector with return values assumed to be normally distributed) and is the expected return for instrument *i*. Finally, is the transpose of the weights vector and μ is the vector of the expected security returns.

*Equation 13-1. General formula for expected portfolio return*

![](_page_28_Figure_0.jpeg)

Translated into Python this boils down to a single line of code including annualization:

```
In [50]: np.sum(rets.mean() * weights) * 252
Out[50]: 0.09179459482057793
```

Annualized portfolio return given the portfolio weights.

The second object of importance in MPT is the *expected portfolio variance*. The covariance between two securities is defined by

. The variance of a security is the special case of the covariance with itself: . Equation 13-2 provides the covariance matrix for a portfolio of securities (assuming an equal weight of 1 for every security).

*Equation 13-2. Portfolio covariance matrix*

![](_page_29_Figure_2.jpeg)

Equipped with the portfolio covariance matrix, [Equation](#page-29-0) 13-3 then provides the formula for the expected portfolio variance.

<span id="page-29-0"></span>*Equation 13-3. General formula for expected portfolio variance*

![](_page_29_Figure_5.jpeg)

In Python, this all again boils down to a single line of code, making heavy use of NumPy vectorization capabilities. The np.dot() function gives the dot product of two vectors/matrices. The T attribute or transpose() method gives the transpose of a vector or matrix. Given the portfolio variance, the (expected) portfolio standard deviation or volatility is then only one square root away:

```
In [51]: np.dot(weights.T, np.dot(rets.cov() * 252, weights))
Out[51]: 0.014763288666485574
In [52]: math.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
Out[52]: 0.12150427427249452
```

Annualized *portfolio variance* given the portfolio weights.

Annualized *portfolio volatility* given the portfolio weights.

# **PYTHON AND VECTORIZATION**

The MPT example shows how efficient it is with Python to translate mathematical concepts, like portfolio return or portfolio variance, into executable, vectorized code (an argument made in Chapter 1).

This mainly completes the tool set for mean-variance portfolio selection. Of paramount interest to investors is what risk-return profiles are possible for a given set of financial instruments, and their statistical characteristics. To this end, the following implements a Monte Carlo simulation (see Chapter 12) to generate random portfolio weight vectors on a larger scale. For every simulated allocation, the code records the resulting expected portfolio return and variance. To simplify the code, two functions, port\_ret() and port\_vol(), are defined:

```
In [53]: def port_ret(weights):
             return np.sum(rets.mean() * weights) * 252
In [54]: def port_vol(weights):
             return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
In [55]: prets = []
         pvols = []
         for p in range (2500):
             weights = np.random.random(noa)
             weights /= np.sum(weights)
             prets.append(port_ret(weights))
             pvols.append(port_vol(weights))
         prets = np.array(prets)
         pvols = np.array(pvols)
```

Monte Carlo simulation of portfolio weights.

Collects the resulting statistics in list objects.

Figure 13-12 illustrates the results of the Monte Carlo simulation. In addition, it provides results for the Sharpe ratio, defined as — i.e., the expected excess return of the portfolio over the risk-free short rate divided by the expected standard deviation of the portfolio. For simplicity, is assumed:

![](_page_32_Figure_0.jpeg)

<span id="page-32-0"></span>![](_page_32_Figure_1.jpeg)

*Figure 13-12. Expected return and volatility for random portfolio weights*

It is clear by inspection of [Figure](#page-32-0) 13-12 that not all weight distributions perform well when measured in terms of mean and volatility. For example, for a fixed risk level of, say, 15%, there are multiple portfolios that all show different returns. As an investor, one is generally interested in the maximum return given a fixed risk level or the minimum risk given a fixed return expectation. This set of portfolios then makes up the so-called *efficient frontier*. This is derived later in this section.

# **Optimal Portfolios**

This *minimization* function is quite general and allows for equality constraints, inequality constraints, and numerical bounds for the parameters.

First, the *maximization of the Sharpe ratio*. Formally, the negative value of the Sharpe ratio is minimized to derive at the maximum value and the optimal portfolio composition. The constraint is that all parameters (weights) add up to 1. This can be formulated as follows using the [conventions](http://bit.ly/using_minimize) of the minimize() function. <sup>4</sup> The parameter values (weights) are also bound to be between 0 and 1. These values are provided to the minimization function as a tuple of tuples.

The only input that is missing for a call of the optimization function is a starting parameter list (initial guess for the weights vector). An equal distribution of weights will do:

```
In [57]: import scipy.optimize as sco
In [58]: def min_func_sharpe(weights):
             return -port_ret(weights) / port_vol(weights)
In [59]: cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
In [60]: bnds = tuple((0, 1) for x in range(noa))
In [61]: eweights = np.array(noa * [1. / noa,])
         eweights
Out[61]: array([0.25, 0.25, 0.25, 0.25])
In [62]: min_func_sharpe(eweights)
Out[62]: -0.8436203363155397
```

Function to be minimized.

Equality constraint.

Bounds for the parameters.

Equal weights vector.

Calling the function returns more than just the optimal parameter values. The

results are stored in an object called opts. The main interest lies in getting the optimal portfolio composition. To this end, one can access the results object by providing the key of interest; i.e., x in this case:

```
In [63]: %%time
         opts = sco.minimize(min_func_sharpe, eweights,
                             method='SLSQP', bounds=bnds,
                             constraints=cons)
         CPU times: user 67.6 ms, sys: 1.94 ms, total: 69.6 ms
         Wall time: 75.2 ms
In [64]: opts
Out[64]: fun: -0.8976673894052725
         jac: array([ 8.96826386e-05, 8.30739737e-05, -2.45958567e-04,
          1.92895532e-05])
          message: 'Optimization terminated successfully.'
             nfev: 36
              nit: 6
             njev: 6
           status: 0
          success: True
                x: array([0.51191354, 0.19126414, 0.25454109, 0.04228123])
In [65]: opts['x'].round(3)
Out[65]: array([0.512, 0.191, 0.255, 0.042])
In [66]: port_ret(opts['x']).round(3)
Out[66]: 0.161
In [67]: port_vol(opts['x']).round(3)
Out[67]: 0.18
In [68]: port_ret(opts['x']) / port_vol(opts['x'])
Out[68]: 0.8976673894052725
```

The optimization (i.e., minimization of function min\_func\_sharpe()).

The results from the optimization.

The optimal portfolio weights.

The resulting portfolio return.

The resulting portfolio volatility.

The maximum Sharpe ratio.

Next, the *minimization of the variance* of the portfolio. This is the same as minimizing the volatility:

```
In [69]: optv = sco.minimize(port_vol, eweights,
                             method='SLSQP', bounds=bnds,
                             constraints=cons)
In [70]: optv
Out[70]: fun: 0.1094215526341138
              jac: array([0.11098004, 0.10948556, 0.10939826, 0.10944918])
          message: 'Optimization terminated successfully.'
             nfev: 54
              nit: 9
             njev: 9
           status: 0
          success: True
         x: array([1.62630326e-18, 1.06170720e-03, 5.43263079e-01,
          4.55675214e-01])
In [71]: optv['x'].round(3)
Out[71]: array([0. , 0.001, 0.543, 0.456])
In [72]: port_vol(optv['x']).round(3)
Out[72]: 0.109
In [73]: port_ret(optv['x']).round(3)
Out[73]: 0.06
In [74]: port_ret(optv['x']) / port_vol(optv['x'])
Out[74]: 0.5504173653075624
```

The minimization of the portfolio volatility.

This time, the portfolio is made up of only three financial instruments. This portfolio mix leads to the so-called *minimum volatility* or *minimum variance portfolio*.

# **Efficient Frontier**

The derivation of all optimal portfolios — i.e., all portfolios with minimum volatility for a given target return level (or all portfolios with maximum return for a given risk level) — is similar to the previous optimizations. The only difference is that one has to iterate over multiple starting conditions.

The approach taken is to fix a target return level and to derive for each such level those portfolio weights that lead to the minimum volatility value. For the optimization, this leads to two conditions: one for the target return level, tret, and one for the sum of the portfolio weights as before. The boundary values for each parameter stay the same. When iterating over different target return levels (trets), one condition for the minimization changes. That is why the constraints dictionary is updated during every loop:

```
In [75]: cons = ({'type': 'eq', 'fun': lambda x: port_ret(x) - tret},
                 {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
In [76]: bnds = tuple((0, 1) for x in weights)
In [77]: %%time
         trets = np.linspace(0.05, 0.2, 50)
         tvols = []
         for tret in trets:
             res = sco.minimize(port_vol, eweights, method='SLSQP',
                                bounds=bnds, constraints=cons)
             tvols.append(res['fun'])
         tvols = np.array(tvols)
         CPU times: user 2.6 s, sys: 13.1 ms, total: 2.61 s
         Wall time: 2.66 s
```

The two binding constraints for the efficient frontier.

The minimization of portfolio volatility for different target returns.

Figure 13-13 shows the optimization results. Crosses indicate the optimal portfolios given a certain target return; the dots are, as before, the random portfolios. In addition, the figure shows two larger stars, one for the minimum volatility/variance portfolio (the leftmost portfolio) and one for the portfolio with the maximum Sharpe ratio:

```
In [78]: plt.figure(figsize=(10, 6))
```

```
plt.scatter(pvols, prets, c=prets / pvols,
            marker='.', alpha=0.8, cmap='coolwarm')
plt.plot(tvols, trets, 'b', lw=4.0)
plt.plot(port_vol(opts['x']), port_ret(opts['x']),
         'y*', markersize=15.0)
plt.plot(port_vol(optv['x']), port_ret(optv['x']),
         'r*', markersize=15.0)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio')
```

![](_page_37_Figure_1.jpeg)

*Figure 13-13. Minimum risk portfolios for given return levels (efficient frontier)*

The *efficient frontier* is comprised of all optimal portfolios with a higher return than the absolute minimum variance portfolio. These portfolios dominate all other portfolios in terms of expected returns given a certain risk level.

# **Capital Market Line**

In addition to risky financial instruments like stocks or commodities (such as gold), there is in general one universal, riskless investment opportunity available: *cash* or *cash accounts*. In an idealized world, money held in a cash account with a large bank can be considered riskless (e.g., through public deposit insurance schemes). The downside is that such a riskless investment generally yields only a small return, sometimes close to zero.

However, taking into account such a riskless asset enhances the efficient investment opportunity set for investors considerably. The basic idea is that investors first determine an efficient portfolio of risky assets and then add the riskless asset to the mix. By adjusting the proportion of the investor's wealth to be invested in the riskless asset it is possible to achieve any risk-return profile that lies on the straight line (in the risk-return space) between the riskless asset and the efficient portfolio.

Which efficient portfolio (out of the many options) is to be taken to invest in optimally? It is the one portfolio where the tangent line of the efficient frontier goes exactly through the risk-return point of the riskless portfolio. For example, consider a riskless interest rate of . The portfolio is to be found on the efficient frontier for which the tangent goes through the point in risk-return space.

For the calculations that follow, a functional approximation and the first derivative for the efficient frontier are used. Cubic splines interpolation provides such a differentiable functional approximation (see Chapter 11). For the spline interpolation, only those portfolios from the efficient frontier are used. Via this numerical approach it is possible to define a continuously differentiable function f(x) for the efficient frontier and the respective first derivative function df(x):

```
In [79]: import scipy.interpolate as sci
In [80]: ind = np.argmin(tvols)
         evols = tvols[ind:]
         erets = trets[ind:]
In [81]: tck = sci.splrep(evols, erets)
In [82]: def f(x):
```

```
''' Efficient frontier function (splines approximation). '''
    return sci.splev(x, tck, der=0)
def df(x):
    ''' First derivative of efficient frontier function. '''
    return sci.splev(x, tck, der=1)
```

Index position of minimum volatility portfolio.

Relevant portfolio volatility and return values.

Cubic splines interpolation on these values.

What is now to be derived is a linear function representing the line that passes through the riskless asset in risk-return space and that is tangent to the efficient frontier. [Equation](#page-39-0) 13-4 describes all three conditions that the function *t*(*x*) needs to satisfy.

<span id="page-39-0"></span>*Equation 13-4. Mathematical conditions for capital market line*

![](_page_39_Figure_9.jpeg)

Since there is no closed formula for the efficient frontier or the first derivative of it, one has to solve the system of equations in [Equation](#page-39-0) 13-4 numerically. To this end, define a Python function that returns the values of all three equations given the parameter set *p* = (*a*, *b*, *x*).

The function sco.fsolve() from scipy.optimize is capable of solving such a system of equations. In addition to the function equations(), an initial parameterization is provided. Note that success or failure of the optimization might depend on the initial parameterization, which therefore has to be chosen carefully — generally by a combination of educated guesses with trial and error:

```
In [83]: def equations(p, rf=0.01):
             eq1 = rf - p[0]
             eq2 = rf + p[1] * p[2] - f(p[2])
             eq3 = p[1] - df(p[2])
             return eq1, eq2, eq3
In [84]: opt = sco.fsolve(equations, [0.01, 0.5, 0.15])
In [85]: opt
Out[85]: array([0.01 , 0.84470952, 0.19525391])
In [86]: np.round(equations(opt), 6)
Out[86]: array([ 0., 0., -0.])
```

The equations describing the capital market line (CML).

Solving these equations for given initial values.

The optimal parameter values.

The equation values are all zero.

Figure 13-14 presents the results graphically; the star represents the optimal portfolio from the efficient frontier for which the tangent line passes through the riskless asset point :

```
In [87]: plt.figure(figsize=(10, 6))
         plt.scatter(pvols, prets, c=(prets - 0.01) / pvols,
                     marker='.', cmap='coolwarm')
         plt.plot(evols, erets, 'b', lw=4.0)
         cx = np.linspace(0.0, 0.3)
         plt.plot(cx, opt[0] + opt[1] * cx, 'r', lw=1.5)
         plt.plot(opt[2], f(opt[2]), 'y*', markersize=15.0)
         plt.grid(True)
         plt.axhline(0, color='k', ls='--', lw=2.0)
         plt.axvline(0, color='k', ls='--', lw=2.0)
         plt.xlabel('expected volatility')
         plt.ylabel('expected return')
         plt.colorbar(label='Sharpe ratio')
```

<span id="page-41-0"></span>![](_page_41_Figure_0.jpeg)

*Figure 13-14. Capital market line and tangency portfolio (star) for risk-free rate of 1%*

The portfolio weights of the optimal (tangent) portfolio are as follows. Only three of the four assets are in the mix:

```
In [88]: cons = ({'type': 'eq', 'fun': lambda x: port_ret(x) - f(opt[2])},
                 {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
         res = sco.minimize(port_vol, eweights, method='SLSQP',
                            bounds=bnds, constraints=cons)
In [89]: res['x'].round(3)
Out[89]: array([0.59 , 0.221, 0.189, 0. ])
In [90]: port_ret(res['x'])
Out[90]: 0.1749328414905194
In [91]: port_vol(res['x'])
Out[91]: 0.19525371793918325
In [92]: port_ret(res['x']) / port_vol(res['x'])
Out[92]: 0.8959257899765407
```

Binding constraints for the tangent portfolio (gold star in [Figure](#page-41-0) 13-14).

The portfolio weights for this particular portfolio.

The portfolio weights for this particular portfolio.

# **Bayesian Statistics**

Bayesian statistics nowadays is widely popular in empirical finance. This chapter can for sure not lay the foundations for all concepts of the field. The reader should therefore consult, if needed, a textbook like the one by Geweke (2005) for a general introduction or Rachev (2008) for one that is financially motivated.

# **Bayes' Formula**

The most common interpretation of Bayes' formula in finance is the *diachronic interpretation*. This mainly states that over time one learns new information about certain variables or parameters of interest, like the mean return of a time series. Equation 13-5 states the theorem formally.

<span id="page-44-0"></span>*Equation 13-5. Bayes's formula* 

$$p(H \mid D) = \frac{p(H) \cdot p(D \mid H)}{p(D)}$$

Here,  $H$  stands for an event, the hypothesis, and  $D$  represents the data an experiment or the real world might present.<sup>5</sup> On the basis of these fundamental notions, one has:

# $p(H)$

The *prior* probability

# $p(D)$

The probability for the data under any hypothesis, called the *normalizing* constant

 $p(D \mid H)$ 

The *likelihood* (i.e., the probability) of the data under hypothesis  $H$ 

 $p(H \mid D)$ 

The *posterior* probability; i.e., after one has seen the data

Consider a simple example. There two boxes,  $B_1$  and  $B_2$ . Box  $B_1$  contains 30 black balls and 60 red balls, while box  $B_2$  contains 60 black balls and 30 red balls. A ball is randomly drawn from one of the two boxes. Assume the ball is *black*. What are the probabilities for the hypotheses " $H_1$ : Ball is from box  $B_1$ "; and " $H_2$ : Ball is from box  $B_2$ ," respectively?

Before the random draw of the the ball, both hypotheses are equally likely. After it is clear that the ball is black, one has to update the probability for both hypotheses according to Bayes' formula. Consider hypothesis *H*<sup>1</sup> :

- *Prior*:
- *Normalizing constant*:
- *Likelihood*:

This gives the updated probability for *H*<sup>1</sup> of .

This result also makes sense intuitively. The probability of drawing a black ball from box *B*<sup>2</sup> is twice as high as that of the same event happening with box *B*<sup>1</sup> . Therefore, having drawn a black ball, the hypothesis *H*<sup>2</sup> has with an updated probability two times as high as the updated probability for hypothesis *H*<sup>1</sup> .

# <span id="page-46-0"></span>**Bayesian Regression**

With PyMC3 the Python ecosystem provides a comprehensive package to technically implement Bayesian statistics and probabilistic programming.

Consider the following example based on noisy data around a straight line. 6 First, a linear ordinary least-squares regression (see Chapter 11) is implemented on the data set, the result of which is visualized in [Figure](#page-46-0) 13-15:

```
In [1]: import numpy as np
        import pandas as pd
        import datetime as dt
        from pylab import mpl, plt
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        np.random.seed(1000)
        %matplotlib inline
In [3]: x = np.linspace(0, 10, 500)
        y = 4 + 2 * x + np.random.standard_normal(len(x)) * 2
In [4]: reg = np.polyfit(x, y, 1)
In [5]: reg
Out[5]: array([2.03384161, 3.77649234])
In [6]: plt.figure(figsize=(10, 6))
        plt.scatter(x, y, c=y, marker='v', cmap='coolwarm')
        plt.plot(x, reg[1] + reg[0] * x, lw=2.0)
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
```

![](_page_47_Figure_0.jpeg)

*Figure 13-15. Sample data points and regression line*

The results of the OLS regression approach are fixed values for the two parameters of the regression line (intercept and slope). Note that the highestorder monomial factor (in this case, the slope of the regression line) is at index level 0 and that the intercept is at index level 1. The original parameters 2 and 4 are not perfectly recovered, but this of course is due to the noise included in the data.

Second, a Bayesian regression making use of the PyMC3 package. Here, it is assumed that the parameters are distributed in a certain way. For example,

consider the equation describing the regression line . Assume now the following *priors*:

- α is normally distributed with mean 0 and a standard deviation of 20.
- β is normally distributed with mean 0 and a standard deviation of 10.

For the *likelihood*, assume a normal distribution with a mean of and a

uniformly distributed standard deviation of between 0 and 10.

A major element of Bayesian [regression](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo) is *Markov chain Monte Carlo (MCMC) sampling*. 7 In principle, this is the same as drawing balls multiple times from boxes, as in the simple example in the previous section — just in a more systematic, automated way.

For the technical sampling, there are three different functions to call:

- find\_MAP() finds the starting point for the sampling algorithm by deriving the *local maximum a posteriori point*.
- NUTS() implements the so-called "efficient No-U-Turn Sampler with dual averaging" (NUTS) algorithm for MCMC sampling given the assumed priors.
- sample() draws a number of samples given the starting value from find\_MAP() and the optimal step size from the NUTS algorithm.

All this is to be wrapped into a PyMC3 Model object and executed within a with statement:

```
In [8]: import pymc3 as pm
In [9]: %%time
        with pm.Model() as model:
            # model
            alpha = pm.Normal('alpha', mu=0, sd=20)
            beta = pm.Normal('beta', mu=0, sd=10)
            sigma = pm.Uniform('sigma', lower=0, upper=10)
            y_est = alpha + beta * x
            likelihood = pm.Normal('y', mu=y_est, sd=sigma,
                                   observed=y)
            # inference
            start = pm.find_MAP()
            step = pm.NUTS()
            trace = pm.sample(100, tune=1000, start=start,
                              progressbar=True, verbose=False)
        logp = -1,067.8, ||grad|| = 60.354: 100%|██████████| 28/28 [00:00<00:00,
         474.70it/s]
        Only 100 samples in chain.
        Auto-assigning NUTS sampler...
        Initializing NUTS using jitter+adapt_diag...
        Multiprocess sampling (2 chains in 2 jobs)
        NUTS: [sigma, beta, alpha]
        Sampling 2 chains: 100%|██████████| 2200/2200 [00:03<00:00,
         690.96draws/s]
        CPU times: user 6.2 s, sys: 1.72 s, total: 7.92 s
        Wall time: 1min 28s
```

```
In [10]: pm.summary(trace)
Out[10]:
             mean sd mc_error hpd_2.5 hpd_97.5 n_eff Rhat
   alpha 3.764027 0.174796 0.013177 3.431739 4.070091 152.446951 0.996281
   beta 2.036318 0.030519 0.002230 1.986874 2.094008 106.505590 0.999155
   sigma 2.010398 0.058663 0.004517 1.904395 2.138187 188.643293 0.998547
In [11]: trace[0]
Out[11]: {'alpha': 3.9303300798212444,
         'beta': 2.0020264758995463,
         'sigma_interval__': -1.3519315719461853,
         'sigma': 2.0555476283253156}
```

Defines the priors.

Specifies the linear regression.

Defines the likelihood.

Finds the starting value by optimization.

Instantiates the MCMC algorithm.

Draws posterior samples using NUTS.

Shows summary statistics from samplings.

Estimates from the first sample.

The three estimates shown are rather close to the original values (4, 2, 2). However, the whole procedure yields more estimates. They are best illustrated with the help of a *trace plot*, as in Figure 13-16 — i.e., a plot showing the resulting posterior distribution for the different parameters as well as all single estimates per sample. The posterior distribution gives an intuitive sense about the uncertainty in the estimates:

In [12]: pm.traceplot(trace, lines={'alpha': 4, 'beta': 2, 'sigma': 2});

<span id="page-50-0"></span>![](_page_50_Figure_0.jpeg)

Taking only the alpha and beta values from the regression, one can draw all resulting regression lines as shown in [Figure](#page-50-0) 13-17:

```
In [13]: plt.figure(figsize=(10, 6))
         plt.scatter(x, y, c=y, marker='v', cmap='coolwarm')
         plt.colorbar()
         plt.xlabel('x')
         plt.ylabel('y')
         for i in range(len(trace)):
             plt.plot(x, trace['alpha'][i] + trace['beta'][i] * x)
```

Plots single regression lines.

![](_page_51_Figure_0.jpeg)

*Figure 13-17. Regression lines based on the different estimates*

# **Two Financial Instruments**

Having introduced Bayesian regression with PyMC3 based on dummy data, the move to real financial data is straightforward. The example uses financial time series data for the two exchange traded funds (ETFs) GLD and GDX (see Figure 13-18):

```
In [14]: raw = pd.read_csv('../../source/tr_eikon_eod_data.csv',
                          index_col=0, parse_dates=True)
In [15]: data = raw[['GDX', 'GLD']].dropna()
In [16]: data = data / data.iloc[0]
In [17]: data.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 2138 entries, 2010-01-04 to 2018-06-29
        Data columns (total 2 columns):
        GDX 2138 non-null float64
        GLD 2138 non-null float64
        dtypes: float64(2)
        memory usage: 50.1 KB
In [18]: data.ix[-1] / data.ix[0] - 1
Out[18]: GDX -0.532383
        GLD 0.080601
        dtype: float64
In [19]: data.corr()
Out[19]: GDX GLD
        GDX 1.00000 0.71539
        GLD 0.71539 1.00000
In [20]: data.plot(figsize=(10, 6));
```

Normalizes the data to a starting value of 1.

Calculates the relative performances.

Calculates the correlation between the two instruments.

![](_page_53_Figure_0.jpeg)

*Figure 13-18. Normalized prices for GLD and GDX over time*

In what follows, the dates of the single data points are visualized in scatter plots. To this end, the DatetimeIndex object of the DataFrame is transformed to matplotlib dates. Figure 13-19 shows a scatter plot of the time series data, plotting the GLD values against the GDX values and illustrating the dates of each data pair by different colorings: 8

```
In [21]: data.index[:3]
Out[21]: DatetimeIndex(['2010-01-04', '2010-01-05', '2010-01-06'],
          dtype='datetime64[ns]', name='Date', freq=None)
In [22]: mpl_dates = mpl.dates.date2num(data.index.to_pydatetime())
         mpl_dates[:3]
Out[22]: array([733776., 733777., 733778.])
In [23]: plt.figure(figsize=(10, 6))
         plt.scatter(data['GDX'], data['GLD'], c=mpl_dates,
                     marker='o', cmap='coolwarm')
         plt.xlabel('GDX')
         plt.ylabel('GLD')
         plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                      format=mpl.dates.DateFormatter('%d %b %y'));
```

Converts the DatetimeIndex object to matplotlib dates.

![](_page_54_Figure_2.jpeg)

Customizes the color bar for the dates.

*Figure 13-19. Scatter plot of GLD prices against GDX prices*

The following code implements a Bayesian regression on the basis of these two time series. The parameterizations are essentially the same as in the previous example with dummy data. Figure 13-20 shows the results from the MCMC sampling procedure given the assumptions about the prior probability distributions for the three parameters:

```
In [24]: with pm.Model() as model:
             alpha = pm.Normal('alpha', mu=0, sd=20)
             beta = pm.Normal('beta', mu=0, sd=20)
             sigma = pm.Uniform('sigma', lower=0, upper=50)
             y_est = alpha + beta * data['GDX'].values
             likelihood = pm.Normal('GLD', mu=y_est, sd=sigma,
                                    observed=data['GLD'].values)
             start = pm.find_MAP()
             step = pm.NUTS()
             trace = pm.sample(250, tune=2000, start=start,
```

progressbar=True) logp = 1,493.7, ||grad|| = 188.29: 100%|██████████| 27/27 [00:00<00:00, 1609.34it/s] Only 250 samples **in** chain. Auto-assigning NUTS sampler... Initializing NUTS using jitter+adapt\_diag... Multiprocess sampling (2 chains **in** 2 jobs) NUTS: [sigma, beta, alpha] Sampling 2 chains: 100%|██████████| 4500/4500 [00:09<00:00, 465.07draws/s] The estimated number of effective samples **is** smaller than 200 **for** some parameters. In [25]: pm.summary(trace)

Out[25]: mean sd mc\_error hpd\_2.5 hpd\_97.5 n\_eff Rhat alpha 0.913335 0.005983 0.000356 0.901586 0.924714 184.264900 1.001855 beta 0.385394 0.007746 0.000461 0.369154 0.398291 215.477738 1.001570 sigma 0.119484 0.001964 0.000098 0.115305 0.123315 312.260213 1.005246

```
In [26]: fig = pm.traceplot(trace)
```

![](_page_55_Figure_3.jpeg)

Figure 13-21 adds all the resulting regression lines to the scatter plot from before. However, all the regression lines are pretty close to each other:

```
In [27]: plt.figure(figsize=(10, 6))
         plt.scatter(data['GDX'], data['GLD'], c=mpl_dates,
                     marker='o', cmap='coolwarm')
         plt.xlabel('GDX')
         plt.ylabel('GLD')
         for i in range(len(trace)):
             plt.plot(data['GDX'],
                      trace['alpha'][i] + trace['beta'][i] * data['GDX'])
```

![](_page_56_Figure_0.jpeg)

plt.colorbar(ticks=mpl.dates.DayLocator(interval=250), format=mpl.dates.DateFormatter('%d %b %y'));

*Figure 13-21. Multiple Bayesian regression lines through GDX and GLD data*

The figure reveals a major drawback of the regression approach used: the approach does not take into account evolutions over time. That is, the most recent data is treated the same way as the oldest data.

# **Updating Estimates over Time**

As pointed out before, the Bayesian approach in finance is generally most useful when seen as diachronic — i.e., in the sense that new data revealed over time allows for better regressions and estimates through updating or learning.

To incorporate this concept in the current example, assume that the regression parameters are not only random and distributed in some fashion, but that they follow some kind of *random walk* over time. It is the same generalization used when making the transition in financial theory from random variables to stochastic processes (which are essentially ordered sequences of random variables).

To this end, define a new PyMC3 model, this time specifying parameter values as random walks. After having specified the distributions of the random walk parameters, one proceeds with specifying the random walks for alpha and beta. To make the whole procedure more efficient, 50 data points at a time share common coefficients:

```
In [28]: from pymc3.distributions.timeseries import GaussianRandomWalk
In [29]: subsample_alpha = 50
         subsample_beta = 50
In [30]: model_randomwalk = pm.Model()
         with model_randomwalk:
             sigma_alpha = pm.Exponential('sig_alpha', 1. / .02, testval=.1)
             sigma_beta = pm.Exponential('sig_beta', 1. / .02, testval=.1)
             alpha = GaussianRandomWalk('alpha', sigma_alpha ** -2,
                                 shape=int(len(data) / subsample_alpha))
             beta = GaussianRandomWalk('beta', sigma_beta ** -2,
                                 shape=int(len(data) / subsample_beta))
             alpha_r = np.repeat(alpha, subsample_alpha)
             beta_r = np.repeat(beta, subsample_beta)
             regression = alpha_r + beta_r * data['GDX'].values[:2100]
             sd = pm.Uniform('sd', 0, 20)
             likelihood = pm.Normal('GLD', mu=regression, sd=sd,
                                    observed=data['GLD'].values[:2100])
```

Defines priors for the random walk parameters.

Models for the random walks.

Brings the parameter vectors to interval length.

Defines the regression model.

The prior for the standard deviation.

Defines the likelihood with mu from regression results.

All these definitions are a bit more involved than before due to the use of random walks instead of a single random variable. However, the inference steps with the MCMC sampling remain essentially the same. Note, though, that the computational burden increases substantially since the algorithm has to estimate parameters per random walk sample — i.e., 1,950 / 50 = 39 parameter combinations in this case (instead of 1, as before):

```
In [31]: %%time
        import scipy.optimize as sco
        with model_randomwalk:
            start = pm.find_MAP(vars=[alpha, beta],
                               fmin=sco.fmin_l_bfgs_b)
            step = pm.NUTS(scaling=start)
            trace_rw = pm.sample(250, tune=1000, start=start,
                                progressbar=True)
        logp = -6,657: 2%|▏ | 82/5000 [00:00<00:08, 550.29it/s]
        Only 250 samples in chain.
        Auto-assigning NUTS sampler...
        Initializing NUTS using jitter+adapt_diag...
        Multiprocess sampling (2 chains in 2 jobs)
        NUTS: [sd, beta, alpha, sig_beta, sig_alpha]
        Sampling 2 chains: 100%|██████████| 2500/2500 [02:48<00:00, 8.59draws/s]
        CPU times: user 27.5 s, sys: 3.68 s, total: 31.2 s
        Wall time: 5min 3s
In [32]: pm.summary(trace_rw).head()
Out[32]:
                 mean sd mc_error hpd_2.5 hpd_97.5 n_eff \
   alpha__0 0.673846 0.040224 0.001376 0.592655 0.753034 1004.616544
   alpha__1 0.424819 0.041257 0.001618 0.348102 0.509757 804.760648
   alpha__2 0.456817 0.057200 0.002011 0.321125 0.553173 800.225916
   alpha__3 0.268148 0.044879 0.001725 0.182744 0.352197 724.967532
   alpha__4 0.651465 0.057472 0.002197 0.544076 0.761216 978.073246
                 Rhat
   alpha__0 0.998637
   alpha__1 0.999540
   alpha__2 0.998075
   alpha__3 0.998995
   alpha__4 0.998060
```

The summary statistics per interval (first five and alpha only).

Figure 13-22 illustrates the evolution of the regression parameters alpha and beta over time by plotting a subset of the estimates:

```
In [33]: sh = np.shape(trace_rw['alpha'])
         sh
Out[33]: (500, 42)
In [34]: part_dates = np.linspace(min(mpl_dates),
                                  max(mpl_dates), sh[1])
In [35]: index = [dt.datetime.fromordinal(int(date)) for
                 date in part_dates]
In [36]: alpha = {'alpha_%i' % i: v for i, v in
                  enumerate(trace_rw['alpha']) if i < 20}
In [37]: beta = {'beta_%i' % i: v for i, v in
                  enumerate(trace_rw['beta']) if i < 20}
In [38]: df_alpha = pd.DataFrame(alpha, index=index)
In [39]: df_beta = pd.DataFrame(beta, index=index)
In [40]: ax = df_alpha.plot(color='b', style='-.', legend=False,
                            lw=0.7, figsize=(10, 6))
         df_beta.plot(color='r', style='-.', legend=False,
                      lw=0.7, ax=ax)
         plt.ylabel('alpha/beta');
```

Shape of the object with parameter estimates.

Creates a list of dates to match the number of intervals.

Collects the relevant parameter time series in two DataFrame objects.

![](_page_60_Figure_0.jpeg)

*Figure 13-22. Selected parameter estimates over time*

# **ABSOLUTE PRICE DATA VERSUS RELATIVE RETURN DATA**

The analyses in this section are based on normalized price data. This is for illustration purposes only, because the respective graphical results are easier to understand and interpret (they are visually "more appealing"). For real-world financial applications one would instead rely on return data, for instance, to ensure stationarity of the time series data.

Using the mean alpha and beta values, Figure 13-23 illustrates how the regression is updated over time. The 39 different regression lines resulting from the mean alpha and beta values are displayed. It is obvious that updating over time improves the regression fit (for the current/most recent data) significantly — in other words, "every time period needs its own regression":

```
In [41]: plt.figure(figsize=(10, 6))
         plt.scatter(data['GDX'], data['GLD'], c=mpl_dates,
                     marker='o', cmap='coolwarm')
         plt.colorbar(ticks=mpl.dates.DayLocator(interval=250),
                      format=mpl.dates.DateFormatter('%d %b %y'))
         plt.xlabel('GDX')
         plt.ylabel('GLD')
         x = np.linspace(min(data['GDX']), max(data['GDX']))
         for i in range(sh[1]):
             alpha_rw = np.mean(trace_rw['alpha'].T[i])
             beta_rw = np.mean(trace_rw['beta'].T[i])
             plt.plot(x, alpha_rw + beta_rw * x, '--', lw=0.7,
                     color=plt.cm.coolwarm(i / sh[1]))
```

Plots the regression lines for all time intervals of length 50.

![](_page_62_Figure_0.jpeg)

*Figure 13-23. Scatter plot with time-dependent regression lines (updated estimates)*

This concludes the section on Bayesian statistics. Python offers with PyMC3 a comprehensive package to implement different approaches from Bayesian statistics and probabilistic [programming](https://oreil.ly/2PApqqL). Bayesian regression in particular is a tool that has become quite popular and important in quantitative finance.

# **Machine Learning**

In finance and many other fields, the "name of the game" these days is *machine learning* (ML). As the following quote puts it:

Econometrics might be good enough to succeed in financial academia (for now), but succeeding in practice requires ML. Marcos López de Prado (2018)

Machine learning subsumes different types of algorithms that are basically able to learn *on their own* certain relationships, patterns, *etc.* from raw data. "Further Resources" lists a number of books that can be consulted on the mathematical and statistical aspects of machine learning approaches and algorithms as well as on topics related to their implementation and practical use. For example, Alpaydin (2016) provides a gentle introduction to the field and gives a nontechnical overview of the types of algorithms that are typically used.

This section takes a rigorously practical approach and focuses on selected implementation aspects only — with a view on the techniques used in Chapter 15. However, the algorithms and techniques introduced can of course be used in many different financial areas and not only in algorithmic trading. The section covers two types of algorithms: *unsupervised* and *supervised* learning algorithms.

One of the most popular packages for machine learning with Python is scikitlearn. It not only provides [implementations](http://scikit-learn.org) of a great variety of ML algorithms, but also provides a large number of helpful tools for pre-and post-processing activities related to ML tasks. This section mainly relies on this package. It also uses [TensorFlow](http://tensorflow.org) in the context of deep neural networks (DNNs).

VanderPlas (2016) provides a concise introduction to different ML algorithms based on Python and scikit-learn. Albon (2018) offers a number of recipes for typical tasks in ML, also mainly using Python and scikit-learn.

# **Unsupervised Learning**

*Unsupervised learning* embodies the idea that a machine learning algorithm discovers insights from raw data without any further guidance. One such algorithm is the *k-means* clustering algorithm that clusters a raw data set into a number of subsets and assigns these subsets *labels* ("cluster 0," "cluster 1," etc.). Another one is *Gaussian mixture*. 9

# **The data**

Among other things, scikit-learn allows the creation of sample data sets for different types of ML problems. The following creates a sample data set suited to illustrating *k*-means clustering.

First, some standard imports and configurations:

```
In [1]: import numpy as np
        import pandas as pd
        import datetime as dt
        from pylab import mpl, plt
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        np.random.seed(1000)
        np.set_printoptions(suppress=True, precision=4)
        %matplotlib inline
```

Second, the creation of the sample data set. Figure 13-24 visualizes the sample data:

```
In [3]: from sklearn.datasets.samples_generator import make_blobs
In [4]: X, y = make_blobs(n_samples=250, centers=4,
                          random_state=500, cluster_std=1.25)
In [5]: plt.figure(figsize=(10, 6))
        plt.scatter(X[:, 0], X[:, 1], s=50);
```

Creates the sample data set for clustering with 250 samples and 4 centers.

![](_page_65_Figure_0.jpeg)

*Figure 13-24. Sample data for the application of clustering algorithms*

## **k-means clustering**

One of the convenient features of scikit-learn is that it provides a standardized API to apply different kinds of algorithms. The following code shows the basic steps for *k*-means clustering that are repeated for other models afterwards:

- Importing the model class
- Instantiating a model object
- Fitting the model object to some data
- Predicting the outcome given the fitted model for some data

Figure 13-25 shows the results:

```
In [6]: from sklearn.cluster import KMeans
In [7]: model = KMeans(n_clusters=4, random_state=0)
In [8]: model.fit(X)
```

```
Out[8]: KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
            n_clusters=4, n_init=10, n_jobs=None, precompute_distances='auto',
            random_state=0, tol=0.0001, verbose=0)
In [9]: y_kmeans = model.predict(X)
In [10]: y_kmeans[:12]
Out[10]: array([1, 1, 0, 3, 0, 1, 3, 3, 3, 0, 2, 2], dtype=int32)
In [11]: plt.figure(figsize=(10, 6))
         plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='coolwarm');
```

Imports the model class from scikit-learn.

Instantiates a model object, given certain parameters; knowledge about the sample data is used to inform the instantiation.

Fits the model object to the raw data.

Predicts the cluster (number) given the raw data.

Shows some cluster numbers as predicted.

![](_page_66_Figure_11.jpeg)

## **Gaussian mixture**

As an alternative clustering method, consider Gaussian mixture. The application is the same, and with the appropriate parameterization, the results are also the same:

```
In [12]: from sklearn.mixture import GaussianMixture
In [13]: model = GaussianMixture(n_components=4, random_state=0)
In [14]: model.fit(X)
Out[14]: GaussianMixture(covariance_type='full', init_params='kmeans',
          max_iter=100,
         means_init=None, n_components=4, n_init=1, precisions_init=None,
                 random_state=0, reg_covar=1e-06, tol=0.001, verbose=0,
                 verbose_interval=10, warm_start=False, weights_init=None)
In [15]: y_gm = model.predict(X)
In [16]: y_gm[:12]
Out[16]: array([1, 1, 0, 3, 0, 1, 3, 3, 3, 0, 2, 2])
In [17]: (y_gm == y_kmeans).all()
Out[17]: True
```

The results from *k*-means clustering and Gaussian mixture are the same.

# **Supervised Learning**

*Supervised learning* is machine learning with some guidance in the form of known results or observed data. This means that the raw data already contains what the ML algorithm is supposed to learn. In what follows, the focus lies on *classification problems* as opposed to *estimation problems*. While estimation problems are about the estimation of real-valued quantities in general, classification problems are characterized by an effort to assign to a certain feature combination a certain class (integer value) from a relatively small set of classes (integer values).

The examples in the previous subsection showed that with unsupervised learning the algorithms come up with their own categorical labels for the clusters identified. With four clusters, the labels are 0, 1, 2, and 3. In supervised learning, such categorical labels are already given, so that the algorithm can learn the *relationship* between the features and the categories (classes). In other words, during the fitting step, the algorithm *knows* the right class for the given feature value combinations.

This subsection illustrates the application of the following classification algorithms: Gaussian Naive Bayes, logistic regression, decision trees, deep neural networks, and support vector machines. 10

# **The data**

Again, scikit-learn allows the creation of an appropriate sample data set to apply classification algorithms. In order to be able to visualize the results, the sample data only contains two real-valued, informative features and a single binary label (a binary label is characterized by two different classes only, 0 and 1). The following code creates the sample data, shows some extracts of the data, and visualizes the data (see Figure 13-26):

```
In [18]: from sklearn.datasets import make_classification
In [19]: n_samples = 100
In [20]: X, y = make_classification(n_samples=n_samples, n_features=2,
                                    n_informative=2, n_redundant=0,
                                    n_repeated=0, random_state=250)
In [21]: X[:5]
```

```
Out[21]: array([[ 1.6876, -0.7976],
                [-0.4312, -0.7606],
                [-1.4393, -1.2363],
                [ 1.118 , -1.8682],
                [ 0.0502, 0.659 ]])
In [22]: X.shape
Out[22]: (100, 2)
In [23]: y[:5]
Out[23]: array([1, 0, 0, 1, 1])
In [24]: y.shape
Out[24]: (100,)
plt.figure(figsize=(10, 6))
plt.hist(X);
In [25]: plt.figure(figsize=(10, 6))
         plt.scatter(x=X[:, 0], y=X[:, 1], c=y, cmap='coolwarm');
```

The two informative, real-valued features.

The single binary label.

![](_page_69_Figure_5.jpeg)

*Figure 13-26. Sample data for the application of classification algorithms*

## **Gaussian Naive Bayes**

**Gaussian Naive Bayes**

*Gaussian Naive Bayes* (GNB) is generally considered to be a good baseline algorithm for a multitude of different classification problems. The application is in line with the steps outlined in "k-means clustering":

```
In [26]: from sklearn.naive_bayes import GaussianNB
        from sklearn.metrics import accuracy_score
In [27]: model = GaussianNB()
In [28]: model.fit(X, y)
Out[28]: GaussianNB(priors=None, var_smoothing=1e-09)
In [29]: model.predict_proba(X).round(4)[:5]
Out[29]: array([[0.0041, 0.9959],
               [0.8534, 0.1466],
               [0.9947, 0.0053],
               [0.0182, 0.9818],
               [0.5156, 0.4844]])
In [30]: pred = model.predict(X)
In [31]: pred
Out[31]: array([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1,
         0,
        0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0,
        0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0,
        0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
               0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
In [32]: pred == y
Out[32]: array([ True, True, True, True, False, True, True, True, True,
                True, False, True, True, True, True, True, True, True,
                True, True, True, True, False, False, False, True, True,
                True, True, True, True, True, True, False, True, True,
                True, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, False, True, False,
                True, True, True, True, True, True, True, True, True,
                True, True, False, True, True, True, True, True, True,
                True, True, True, True, True, True, False, True, False,
                True, True, True, True, True, True, True, True, True,
                True, True, False, True, False, True, True, True, True,
                True])
In [33]: accuracy_score(y, pred)
Out[33]: 0.87
```

Shows the probabilities that the algorithm assigns to each class after fitting.

Based on the probabilities, predicts the binary classes for the data set.

Compares the predicted classes with the real ones.

Calculates the accuracy score given the predicted values.

[Figure](#page-71-0) 13-27 visualizes the correct and false predictions from GNB:

```
In [34]: Xc = X[y == pred]
         Xf = X[y != pred]
In [35]: plt.figure(figsize=(10, 6))
         plt.scatter(x=Xc[:, 0], y=Xc[:, 1], c=y[y == pred],
                     marker='o', cmap='coolwarm')
         plt.scatter(x=Xf[:, 0], y=Xf[:, 1], c=y[y != pred],
                     marker='x', cmap='coolwarm')
```

Selects the *correct* predictions and plots them.

Selects the *false* predictions and plots them.

<span id="page-71-0"></span>![](_page_71_Figure_8.jpeg)

*Figure 13-27. Correct (dots) and false predictions (crosses) from GNB*

## **Logistic regression**

*Logistic regression* (LR) is a fast and scalable classification algorithm. The

accuracy in this particular case is slightly better than with GNB:

```
In [36]: from sklearn.linear_model import LogisticRegression
In [37]: model = LogisticRegression(C=1, solver='lbfgs')
In [38]: model.fit(X, y)
Out[38]: LogisticRegression(C=1, class_weight=None, dual=False,
          fit_intercept=True,
                   intercept_scaling=1, max_iter=100, multi_class='warn',
                   n_jobs=None, penalty='l2', random_state=None, solver='lbfgs',
                   tol=0.0001, verbose=0, warm_start=False)
In [39]: model.predict_proba(X).round(4)[:5]
Out[39]: array([[0.011 , 0.989 ],
                [0.7266, 0.2734],
                [0.971 , 0.029 ],
                [0.04 , 0.96 ],
                [0.4843, 0.5157]])
In [40]: pred = model.predict(X)
In [41]: accuracy_score(y, pred)
Out[41]: 0.9
In [42]: Xc = X[y == pred]
         Xf = X[y != pred]
In [43]: plt.figure(figsize=(10, 6))
         plt.scatter(x=Xc[:, 0], y=Xc[:, 1], c=y[y == pred],
                     marker='o', cmap='coolwarm')
         plt.scatter(x=Xf[:, 0], y=Xf[:, 1], c=y[y != pred],
                     marker='x', cmap='coolwarm');
```

## **Decision trees**

*Decision trees* (DTs) are yet another type of classification algorithm that scales quite well. With a maximum depth of 1, the algorithm already performs slightly better than both GNB and LR (see also Figure 13-28):

```
In [44]: from sklearn.tree import DecisionTreeClassifier
In [45]: model = DecisionTreeClassifier(max_depth=1)
In [46]: model.fit(X, y)
Out[46]: DecisionTreeClassifier(class_weight=None, criterion='gini',
          max_depth=1,
                     max_features=None, max_leaf_nodes=None,
                     min_impurity_decrease=0.0, min_impurity_split=None,
                     min_samples_leaf=1, min_samples_split=2,
         min_weight_fraction_leaf=0.0, presort=False, random_state=None,
                     splitter='best')
In [47]: model.predict_proba(X).round(4)[:5]
Out[47]: array([[0.08, 0.92],
                [0.92, 0.08],
                [0.92, 0.08],
                [0.08, 0.92],
```

```
[0.08, 0.92]])
```

```
In [48]: pred = model.predict(X)
In [49]: accuracy_score(y, pred)
Out[49]: 0.92
In [50]: Xc = X[y == pred]
         Xf = X[y != pred]
In [51]: plt.figure(figsize=(10, 6))
         plt.scatter(x=Xc[:, 0], y=Xc[:, 1], c=y[y == pred],
                     marker='o', cmap='coolwarm')
         plt.scatter(x=Xf[:, 0], y=Xf[:, 1], c=y[y != pred],
                     marker='x', cmap='coolwarm');
```

![](_page_73_Figure_2.jpeg)

*Figure 13-28. Correct (dots) and false predictions (crosses) from DT (max\_depth=1)*

However, increasing the maximum depth parameter for the decision tree allows one to reach a perfect result:

```
In [52]: print('{:>8s} | {:8s}'.format('depth', 'accuracy'))
         print(20 * '-')
         for depth in range(1, 7):
             model = DecisionTreeClassifier(max_depth=depth)
             model.fit(X, y)
             acc = accuracy_score(y, model.predict(X))
             print('{:8d} | {:8.2f}'.format(depth, acc))
            depth | accuracy
         --------------------
```

| 1 | 0.92 |
|---|------|
| 2 | 0.92 |
| 3 | 0.94 |
| 4 | 0.97 |
| 5 | 0.99 |
| 6 | 1.00 |

# **Deep neural networks**

*Deep neural networks* (DNNs) are considered to be among the most powerful but also computationally demanding — algorithms for both estimation and classification. The open sourcing of the TensorFlow package by Google and related success stories are in part responsible for their popularity. DNNs are capable of learning and modeling complex nonlinear relationships. Although their origins date back to the 1970s, they only recently have become feasible on a large scale due to advances in hardware (CPUs, GPUs, TPUs), numerical algorithms, and related software implementations.

While other ML algorithms, such as linear models of LR type, can be fitted efficiently based on a standard optimization problem, DNNs rely on *deep learning*, which requires in general a large number of repeated steps to adjust certain parameters (weights) and compare the results to the data. In that sense, deep learning can be compared to Monte Carlo simulation in mathematical finance where the price of, say, a European call option can be estimated on the basis of 100,000 simulated paths for the underlying. On the other hand, the Black-Scholes-Merton option pricing formula is available in closed form and can be evaluated analytically.

While Monte Carlo simulation is among the most flexible and powerful numerical techniques in mathematical finance, there's a cost to pay in terms of the high computational burden and large memory footprint. The same holds true for deep learning, which is more flexible in general than many other ML algorithms but which requires greater computational power.

# *DNNs with scikit-learn*

Although it is quite different in nature, scikit-learn provides the same API for its MLPClassifier algorithm class, <sup>11</sup> which is a DNN model, as for the other ML algorithms used before. With just two so-called *hidden layers* it reaches a perfect result on the test data (the hidden layers are what make deep learning out of simple learning — e.g., "learning" weights in the context of a linear regression

instead of using OLS regression to derive them directly):

```
In [53]: from sklearn.neural_network import MLPClassifier
In [54]: model = MLPClassifier(solver='lbfgs', alpha=1e-5,
                               hidden_layer_sizes=2 * [75], random_state=10)
In [55]: %time model.fit(X, y)
         CPU times: user 537 ms, sys: 14.2 ms, total: 551 ms
         Wall time: 340 ms
Out[55]: MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
          beta_1=0.9,
                beta_2=0.999, early_stopping=False, epsilon=1e-08,
                hidden_layer_sizes=[75, 75], learning_rate='constant',
                learning_rate_init=0.001, max_iter=200, momentum=0.9,
                n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
                random_state=10, shuffle=True, solver='lbfgs', tol=0.0001,
                validation_fraction=0.1, verbose=False, warm_start=False)
In [56]: pred = model.predict(X)
         pred
Out[56]: array([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1,
          0,
         1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0,
         0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1,
         0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1,
                0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0])
In [57]: accuracy_score(y, pred)
Out[57]: 1.0
```

# *DNNs with TensorFlow*

The API of TensorFlow is different from the scikit-learn standard. However, the application of the DNNClassifier class is similarly straightforward:

```
In [58]: import tensorflow as tf
         tf.logging.set_verbosity(tf.logging.ERROR)
In [59]: fc = [tf.contrib.layers.real_valued_column('features')]
In [60]: model = tf.contrib.learn.DNNClassifier(hidden_units=5 * [250],
                                                n_classes=2,
                                                feature_columns=fc)
In [61]: def input_fn():
             fc = {'features': tf.constant(X)}
             la = tf.constant(y)
             return fc, la
In [62]: %time model.fit(input_fn=input_fn, steps=100)
         CPU times: user 7.1 s, sys: 1.35 s, total: 8.45 s
         Wall time: 4.71 s
Out[62]: DNNClassifier(params={'head':
          <tensorflow.contrib.learn.python.learn ... head._BinaryLogisticHead
          object at 0x1a3ee692b0>, 'hidden_units': [250, 250, 250, 250, 250],
```

```
'feature_columns': (_RealValuedColumn(column_name='features',
          dimension=1, default_value=None, dtype=tf.float32, normalizer=None),),
          'optimizer': None, 'activation_fn': <function relu at 0x1a3aa75b70>,
          'dropout': None, 'gradient_clip_norm': None,
          'embedding_lr_multipliers': None, 'input_layer_min_slice_size': None})
In [63]: model.evaluate(input_fn=input_fn, steps=1)
Out[63]: {'loss': 0.18724777,
          'accuracy': 0.91,
          'labels/prediction_mean': 0.5003989,
          'labels/actual_label_mean': 0.5,
          'accuracy/baseline_label_mean': 0.5,
          'auc': 0.9782,
          'auc_precision_recall': 0.97817385,
          'accuracy/threshold_0.500000_mean': 0.91,
          'precision/positive_threshold_0.500000_mean': 0.9019608,
          'recall/positive_threshold_0.500000_mean': 0.92,
          'global_step': 100}
In [64]: pred = np.array(list(model.predict(input_fn=input_fn)))
         pred[:10]
Out[64]: array([1, 0, 0, 1, 1, 0, 1, 1, 1, 1])
In [65]: %time model.fit(input_fn=input_fn, steps=750)
         CPU times: user 29.8 s, sys: 7.51 s, total: 37.3 s
         Wall time: 13.6 s
Out[65]: DNNClassifier(params={'head':
          <tensorflow.contrib.learn.python.learn ... head._BinaryLogisticHead
          object at 0x1a3ee692b0>, 'hidden_units': [250, 250, 250, 250, 250],
          'feature_columns': (_RealValuedColumn(column_name='features',
          dimension=1, default_value=None, dtype=tf.float32, normalizer=None),),
          'optimizer': None, 'activation_fn': <function relu at 0x1a3aa75b70>,
          'dropout': None, 'gradient_clip_norm': None,
          'embedding_lr_multipliers': None, 'input_layer_min_slice_size': None})
In [66]: model.evaluate(input_fn=input_fn, steps=1)
Out[66]: {'loss': 0.09271307,
          'accuracy': 0.94,
          'labels/prediction_mean': 0.5274486,
          'labels/actual_label_mean': 0.5,
          'accuracy/baseline_label_mean': 0.5,
          'auc': 0.99759996,
          'auc_precision_recall': 0.9977609,
          'accuracy/threshold_0.500000_mean': 0.94,
          'precision/positive_threshold_0.500000_mean': 0.9074074,
          'recall/positive_threshold_0.500000_mean': 0.98,
          'global_step': 850}
```

Sets the verbosity for TensorFlow logging.

Defines the real-valued features abstractly.

Instantiates the model object.

Features and label data are to be delivered by a function.

Fits the model through learning and evaluates it.

Predicts the label values based on the feature values.

Retrains the model based on more learning steps; the previous results are taken as a starting point.

Accuracy increases after retraining.

This only scratches the surface of TensorFlow, which is used in a number of demanding use cases, such as Alphabet Inc.'s effort to build self-driving cars. In terms of speed, the training of TensorFlow's models in general benefits significantly from the use of specialized hardware such as GPUs and TPUs instead of CPUs.

## **Feature transforms**

For a number of reasons, it might be beneficial or even necessary to transform real-valued features. The following code shows some typical transformations and visualizes the results for comparison in Figure 13-29:

```
In [67]: from sklearn import preprocessing
In [68]: X[:5]
Out[68]: array([[ 1.6876, -0.7976],
                [-0.4312, -0.7606],
                [-1.4393, -1.2363],
                [ 1.118 , -1.8682],
                [ 0.0502, 0.659 ]])
In [69]: Xs = preprocessing.StandardScaler().fit_transform(X)
         Xs[:5]
Out[69]: array([[ 1.2881, -0.5489],
                [-0.3384, -0.5216],
                [-1.1122, -0.873 ],
                [ 0.8509, -1.3399],
                [ 0.0312, 0.5273]])
In [70]: Xm = preprocessing.MinMaxScaler().fit_transform(X)
         Xm[:5]
Out[70]: array([[0.7262, 0.3563],
                [0.3939, 0.3613],
```

```
[0.2358, 0.2973],
                [0.6369, 0.2122],
                [0.4694, 0.5523]])
In [71]: Xn1 = preprocessing.Normalizer(norm='l1').transform(X)
         Xn1[:5]
Out[71]: array([[ 0.6791, -0.3209],
                [-0.3618, -0.6382],
                [-0.5379, -0.4621],
                [ 0.3744, -0.6256],
                [ 0.0708, 0.9292]])
In [72]: Xn2 = preprocessing.Normalizer(norm='l2').transform(X)
         Xn2[:5]
Out[72]: array([[ 0.9041, -0.4273],
                [-0.4932, -0.8699],
                [-0.7586, -0.6516],
                [ 0.5135, -0.8581],
                [ 0.076 , 0.9971]])
In [73]: plt.figure(figsize=(10, 6))
         markers = ['o', '.', 'x', '^', 'v']
         data_sets = [X, Xs, Xm, Xn1, Xn2]
         labels = ['raw', 'standard', 'minmax', 'norm(1)', 'norm(2)']
         for x, m, l in zip(data_sets, markers, labels):
             plt.scatter(x=x[:, 0], y=x[:, 1], c=y,
                     marker=m, cmap='coolwarm', label=l)
         plt.legend();
```

Transforms the features data to standard normally distributed data with zero mean and unit variance.

Transforms the features data to a given range for every feature as defined by the minimum and maximum values per feature.

Scales the features data individually to the unit norm (L1 or L2).

![](_page_79_Figure_0.jpeg)

In terms of pattern recognition tasks, a transformation to categorical features is often helpful or even required to achieve acceptable results. To this end, the real values of the features are mapped to a limited, fixed number of possible integer values (categories, classes):

```
In [74]: X[:5]
Out[74]: array([[ 1.6876, -0.7976],
                [-0.4312, -0.7606],
                [-1.4393, -1.2363],
                [ 1.118 , -1.8682],
                [ 0.0502, 0.659 ]])
In [75]: Xb = preprocessing.Binarizer().fit_transform(X)
         Xb[:5]
Out[75]: array([[1., 0.],
                [0., 0.],
                [0., 0.],
                [1., 0.],
                [1., 1.]])
In [76]: 2 ** 2
Out[76]: 4
In [77]: Xd = np.digitize(X, bins=[-1, 0, 1])
         Xd[:5]
Out[77]: array([[3, 1],
                [1, 1],
```

```
[0, 0],
                [3, 0],
                [2, 2]])
In [78]: 4 ** 2
Out[78]: 16
```

Transforms the features to binary features.

The number of possible feature value combinations for two binary features.

Transforms the features to categorical features based on a list of values used for binning.

The number of possible feature value combinations, with three values used for binning for two features.

## **Traintest splits: Support vector machines**

At this point, every seasoned ML researcher and practitioner reading this probably has concerns with regard to the implementations in this section: they all rely on the same data for training, learning, and prediction. The quality of an ML algorithm can of course be better judged when different data (sub)sets are used for training and learning on the one hand and testing on the other hand. This comes closer to a real-world application scenario.

Again, scikit-learn provides a function to accomplish such an approach efficiently. In particular, the train\_test\_split() function allows the splitting of data sets into training and test data in a randomized, but nevertheless repeatable, fashion.

The following code uses yet another classification algorithm, the *support vector machine* (SVM). It first fits the SVM model based on the training data:

```
In [79]: from sklearn.svm import SVC
         from sklearn.model_selection import train_test_split
In [80]: train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.33,
                                                             random_state=0)
In [81]: model = SVC(C=1, kernel='linear')
```

```
In [82]: model.fit(train_x, train_y)
Out[82]: SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
             decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
           kernel='linear', max_iter=-1, probability=False, random_state=None,
           shrinking=True, tol=0.001, verbose=False)
In [83]: pred_train = model.predict(train_x)
In [84]: accuracy_score(train_y, pred_train)
Out[84]: 0.9402985074626866
```

Fits the model based on the training data.

Predicts the training data label values.

The accuracy of the training data prediction ("in-sample").

Next, the testing of the fitted model based on the test data. Figure 13-30 shows the correct and false predictions for the test data. The accuracy on the test data is — as one would naturally expect — lower than on the training data:

```
In [85]: pred_test = model.predict(test_x)
In [86]: test_y == pred_test
Out[86]: array([ True, True, True, True, True, True, True, True, True,
                True, False, False, False, True, True, True, False, False,
               False, True, True, True, True, True, True, True, True,
                True, True, True, True, False, True])
In [87]: accuracy_score(test_y, pred_test)
Out[87]: 0.7878787878787878
In [88]: test_c = test_x[test_y == pred_test]
        test_f = test_x[test_y != pred_test]
In [89]: plt.figure(figsize=(10, 6))
        plt.scatter(x=test_c[:, 0], y=test_c[:, 1], c=test_y[test_y == pred_test],
                    marker='o', cmap='coolwarm')
        plt.scatter(x=test_f[:, 0], y=test_f[:, 1], c=test_y[test_y != pred_test],
                    marker='x', cmap='coolwarm');
```

Predicts the testing data label values based on the test data.

Evaluates the accuracy of the fitted model for the test data ("out-ofsample").

![](_page_82_Figure_0.jpeg)

The SVM classification algorithm provides a number of options for the kernel to be used. Depending on the problem at hand, different kernels might lead to quite different results (i.e., accuracy scores), as the following analysis shows. The code first transforms the real-valued features into categorical ones:

```
In [90]: bins = np.linspace(-4.5, 4.5, 50)
In [91]: Xd = np.digitize(X, bins=bins)
In [92]: Xd[:5]
Out[92]: array([[34, 21],
                [23, 21],
                [17, 18],
                [31, 15],
                [25, 29]])
In [93]: train_x, test_x, train_y, test_y = train_test_split(Xd, y, test_size=0.33,
                                                              random_state=0)
In [94]: print('{:>8s} | {:8s}'.format('kernel', 'accuracy'))
         print(20 * '-')
         for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
             model = SVC(C=1, kernel=kernel, gamma='auto')
             model.fit(train_x, train_y)
             acc = accuracy_score(test_y, model.predict(test_x))
             print('{:>8s} | {:8.3f}'.format(kernel, acc))
           kernel | accuracy
         --------------------
```

| linear  | 0.848 |
|---------|-------|
| polv    | 0.758 |
| rbf     | 0.788 |
| sigmoid | 0.455 |

# **Conclusion**

Statistics is not only an important discipline in its own right, but also provides indispensable tools for many other disciplines, like finance and the social sciences. It is impossible to give a broad overview of such a large subject in a single chapter. This chapter therefore focuses on four important topics, illustrating the use of Python and several statistics libraries on the basis of realistic examples: Normality

The normality assumption with regard to financial market returns is an important one for many financial theories and applications; it is therefore important to be able to test whether certain time series data conforms to this assumption. As seen in "Normality Tests" — via graphical and statistical means — real-world return data generally is *not* normally distributed.

## *Portfolio optimization*

MPT, with its focus on the mean and variance/volatility of returns, can be considered not only one of the first but also one of the major conceptual successes of statistics in finance; the important concept of investment *diversification* is beautifully illustrated in this context.

## *Bayesian statistics*

Bayesian statistics in general (and Bayesian regression in particular) has become a popular tool in finance, since this approach overcomes some shortcomings of other approaches, as introduced, for instance, in Chapter 11; even if the mathematics and the formalism are more involved, the fundamental ideas — like the updating of probability/distribution beliefs over time — are easily grasped (at least intuitively).

# *Machine learning*

Nowadays, machine learning has established itself in the financial domain alongside traditional statistical methods and techniques. The chapter introduces ML algorithms for unsupervised learning (such as *k*-means clustering) and supervised learning (such as DNN classifiers) and illustrates selected related topics, such as feature transforms and train-test splits.
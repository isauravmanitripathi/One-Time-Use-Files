# **Section 2: Trading Signal Generation and Strategies**

In this section, you will learn how quantitative trading signals and trading strategies are developed. Learning can be applied to market research and the design of algorithmic strategies.

This section comprises the following chapters:

- Chapter 2, *Deciphering the Markets with Technical Analysis*
- Chapter 3, *Predicting the Markets with Basic Machine Learning*

# **Deciphering the Markets with Technical Analysis**

In this chapter, we will go through some popular methods of technical analysis and show how to apply them while analyzing market data. We will perform basic algorithmic trading using market trends, support, and resistance.

You may be thinking of how we can come up with our own strategies? And are there any naive strategies that worked in the past that we can use by way of reference?

As you read in the first chapter of this book, mankind has been trading assets for centuries. Numerous strategies have been created to increase the profit or sometimes just to keep the same profit. In this zero-sum game, the competition is considerable. It necessitates a constant innovation in terms of trading models and also in terms of technology. In this race to get the biggest part of the pie first, it is important to know the basic foundation of analysis in order to create trading strategies. When predicting the market, we mainly assume that the past repeats itself in future. In order to predict future prices and volumes, technical analysts study the historical market data. Based on behavioral economics and quantitative analysis, the market data is divided into two main areas.

First, are chart patterns. This side of technical analysis is based on recognizing trading patterns and anticipating when they will reproduce in the future. This is usually more difficult to implement.

Second, are technical indicators. This other side uses mathematical calculation to forecast the financial market direction. The list of technical indicators is sufficiently long to fill an entire book on this topic alone, but they are composed of a few different principal domains: trend, momentum, volume, volatility, and support and resistance. We will focus on the support and resistance strategy as an example to illustrate one of the most wellknown technical analysis approaches.

In this chapter, we will cover the following topics:

- Designing a trading strategy based on trend-and momentum-based indicators
- Creating trading signals based on fundamental technical analysis
- Implementing advanced concepts, such as seasonality, in trading instruments

# **Designing a trading strategy based on trend- and momentum-based indicators**

Trading strategies based on trend and momentum are pretty similar. If we can use a metaphor to illustrate the difference, the trend strategy uses speed, whereas the momentum strategy uses acceleration. With the trend strategy, we will study the price historical data. If this price keeps increasing for the last fixed amount of days, we will open a long position by assuming that the price will keep raising.

The trading strategy based on momentum is a technique where we send orders based on the strength of past behavior. The price momentum is the quantity of motion that a price has. The underlying rule is to bet that an asset price with a strong movement in a given direction will keep going in the same direction in the future. We will review a number of technical indicators expressing momentum in the market. Support and resistance are examples of indicators predicting future behavior.

### **Support and resistance indicators**

In the first chapter, we explained the principle of the evolution of prices based on supply and demand. The price decreases when there is an increase in supply, and the price increases when demand rises. When there is a fall in price, we expect the price fall to pause due to a concentration of demands. This virtual limit will be referred to as a support line. Since the price becomes lower, it is more likely to find buyers. Inversely, when the price starts rising, we expect a pause in this increase due to a concentration of supplies. This is referred to as the resistance line. It is based on the same principle, showing that a high price leads sellers to sell. This exploits the market psychology of investors following this trend of buying when the price is low and selling when the price is high.

To illustrate an example of a technical indicator (in this part, support and resistance), we will use the Google data from the first chapter. Since you will use the data for testing many times, you should store this data frame to your disk. Doing this will help you save time when you want to replay the data. To avoid complications with stock split, we will only take dates without splits. Therefore, we will keep only 620 days. Let's have a look at the following code:

```
import pandas as pd
from pandas_datareader import data
start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME='goog_data.pkl'
try:
 goog_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
 goog_data2 = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 goog_data2.to_pickle(SRC_DATA_FILENAME)
goog_data=goog_data2.tail(620)
lows=goog_data['Low']
highs=goog_data['High']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
highs.plot(ax=ax1, color='c', lw=2.)
lows.plot(ax=ax1, color='y', lw=2.)
plt.hlines(highs.head(200).max(),lows.index.values[0],lows.index.values[-1],linewidth=2, color='g')
plt.hlines(lows.head(200).min(),lows.index.values[0],lows.index.values[-1],linewidth=2, color='r')
plt.axvline(linewidth=2,color='b',x=lows.index.values[200],linestyle=':')
plt.show()
```

In this code, the following applies:

This retrieves the financial data from the Yahoo finance website between January 1, 2014 and January 1, 2018.

We used the maximum and minimum values to create the support and the resistance limits, as shown in the following plot:

![](_page_5_Figure_1.jpeg)

In this plot, the following applies:

- We draw the highs and lows of the GOOG price.
- The green line represents the resistance level, and the red line represents the support level.
- To build these lines, we use the maximum value of the GOOG price and the minimum value of the GOOG price stored daily.
- After the 200th day (dotted vertical blue line), we will buy when we reach the support line, and sell when we reach the resistance line. In this example, we used 200 days so that we have sufficient data points to get an estimate of the trend.
- It is observed that the GOOG price will reach the resistance line around August 2016. This means that we have a signal to enter a short position (sell).
- Once traded, we will wait to get out of this short position when the GOOG price will reach the support line.
- With this historical data, it is easily noticeable that this condition will not happen.
- This will result in carrying a short position in a rising market without having any signal to sell it, thereby resulting in a huge loss.
- This means that, even if the trading idea based on support/resistance has strong grounds in terms of economical behavior, in reality, we will need to modify this

trading strategy to make it work.

Moving the support/resistance line to adapt to the market evolution will be key to the trading strategy efficiency.

In the middle of the following chart, we show three fixed-size time windows. We took care of adding the tolerance margin that we will consider to be sufficiently close to the limits (support and resistance):

![](_page_6_Figure_3.jpeg)

If we take a new 200-day window after the first one, the support/resistance levels will be recalculated. We observe that the trading strategy will not get rid of the GOOG position (while the market keeps raising) since the price does not go back to the support level.

Since the algorithm cannot get rid of a position, we will need to add more parameters to change the behavior in order to enter a position. The following parameters can be added to the algorithm to change its position:

- There can be a shorter rolling window.
- We can count the number of times the price reaches a support or resistance line.
- A tolerance margin can be added to consider that a support or resistance value can attain around a certain percentage of this value.

This phase is critical when creating your trading strategy. You will start by observing how your trading idea will perform using historical data, and then you will increase the number

of parameters of this strategy to adjust to more realistic test cases.

In our example, we can introduce two further parameters:

- The minimum number of times that a price needs to reach the support/resistance level.
- We will define the tolerance margin of what we consider being close to the support/resistance level.

Let's now have a look at the code:

```
import pandas as pd
import numpy as np
from pandas_datareader import data
start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME='goog_data.pkl'
try:
 goog_data = pd.read_pickle(SRC_DATA_FILENAME)
 print('File data found...reading GOOG data')
except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 goog_data.to_pickle(SRC_DATA_FILENAME)
goog_data_signal = pd.DataFrame(index=goog_data.index)
goog_data_signal['price'] = goog_data['Adj Close']
```

In the code, the data is collected by using the pandas\_datareader library and by using the class. Now, let's have a look at the other part of the code where we will implement the trading strategy:

```
def trading_support_resistance(data, bin_width=20):
 data['sup_tolerance'] = pd.Series(np.zeros(len(data)))
 data['res_tolerance'] = pd.Series(np.zeros(len(data)))
 data['sup_count'] = pd.Series(np.zeros(len(data)))
 data['res_count'] = pd.Series(np.zeros(len(data)))
 data['sup'] = pd.Series(np.zeros(len(data)))
 data['res'] = pd.Series(np.zeros(len(data)))
 data['positions'] = pd.Series(np.zeros(len(data)))
 data['signal'] = pd.Series(np.zeros(len(data)))
 in_support=0
 in_resistance=0
 for x in range((bin_width - 1) + bin_width, len(data)):
 data_section = data[x - bin_width:x + 1]
 support_level=min(data_section['price'])
 resistance_level=max(data_section['price'])
 range_level=resistance_level-support_level
 data['res'][x]=resistance_level
 data['sup'][x]=support_level
 data['sup_tolerance'][x]=support_level + 0.2 * range_level
 data['res_tolerance'][x]=resistance_level - 0.2 * range_level
 if data['price'][x]>=data['res_tolerance'][x] and\
 data['price'][x] <= data['res'][x]:
 in_resistance+=1
 data['res_count'][x]=in_resistance
 elif data['price'][x] <= data['sup_tolerance'][x] and \
 data['price'][x] >= data['sup'][x]:
 in_support += 1
```

```
 data['sup_count'][x] = in_support
 else:
 in_support=0
 in_resistance=0
 if in_resistance>2:
 data['signal'][x]=1
 elif in_support>2:
 data['signal'][x]=0
 else:
 data['signal'][x] = data['signal'][x-1]
 data['positions']=data['signal'].diff()
trading_support_resistance(goog_data_signal)
```

In the preceding code, the following applies:

- The trading\_support\_resistance function defines the time window in the price that is used to calculate the resistance and support levels.
- The level of support and resistance is calculated by taking the maximum and minimum price and then subtracting and adding a 20% margin.
- We used diff to know when we place the orders.
- When the price is below/above the support/resistance, we will enter a long/short position. For that, we will have 1 for a long position and 0 for a short position.

The code will print the chart representing the time when orders go out:

```
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
goog_data_signal['sup'].plot(ax=ax1, color='g', lw=2.)
goog_data_signal['res'].plot(ax=ax1, color='b', lw=2.)
goog_data_signal['price'].plot(ax=ax1, color='r', lw=2.)
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index,
 goog_data_signal.price[goog_data_signal.positions == 1.0],
 '^', markersize=7, color='k',label='buy')
ax1.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index,
 goog_data_signal.price[goog_data_signal.positions == -1.0],
 'v', markersize=7, color='k',label='sell')
plt.legend()
plt.show()
```

The codes will return the following output. The plot shows a 20-day rolling window calculating resistance and support:

![](_page_9_Figure_0.jpeg)

From this plot, it is observed that a buy order is sent when a price stays in the resistance tolerance margin for 2 consecutive days, and that a sell order is sent when a price stays in the support tolerance margin for 2 consecutive days.

In this section, we learned the difference between trend and momentum trading strategies, and we implemented a very well used momentum trading strategy based on support and resistance levels. We will now explore new ideas to create trading strategies by using more technical analysis.

# **Creating trading signals based on fundamental technical analysis**

This section will show you how to use technical analysis to build trading signals. We will start with one of the most common methods, the simple moving average, and we will discuss more advanced techniques along the way. Here is a list of the signals we will cover:

- **Simple Moving Average** (**SMA**)
- **Exponential Moving Average** (**EMA**)
- **Absolute Price Oscillator** (**APO**)
- **Moving Average Convergence Divergence** (**MACD**)
- **Bollinger Bands** (**BBANDS**)
- **Relative Strength Indicator** (**RSI**)
- **Standard Deviation** (**STDEV**)
- **Momentum** (**MOM**)

## **Simple moving average**

**Simple moving average**, which we will refer to as **SMA**, is a basic technical analysis indicator. The simple moving average, as you may have guessed from its name, is computed by adding up the price of an instrument over a certain period of time divided by the number of time periods. It is basically the price average over a certain time period, with equal weight being used for each price. The time period over which it is averaged is often referred to as the lookback period or history. Let's have a look at the following formula of the simple moving average:

$$SimpleMovingAverage = \frac{\sum_{i=1}^{N} Pi}{N}$$

Here, the following applies:

: Price at time period *i*

: Number of prices added together or the number of time periods

Let's implement a simple moving average that computes an average over a 20-day moving window. We will then compare the SMA values against daily prices, and it should be easy to observe the smoothing that SMA achieves.

#### **Implementation of the simple moving average**

In this section, the code demonstrates how you would implement a simple moving average, using a list (history) to maintain a moving window of prices and a list (SMA values) to maintain a list of SMA values:

```
import statistics as stats
time_period = 20 # number of days over which to average
history = [] # to track a history of prices
sma_values = [] # to track simple moving average values
for close_price in close:
 history.append(close_price)
 if len(history) > time_period: # we remove oldest price because we only average over last 'time_period' prices
 del (history[0])
 sma_values.append(stats.mean(history))
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(Simple20DayMovingAverage=pd.Series(sma_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
sma = goog_data['Simple20DayMovingAverage']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
sma.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()
```

In the preceding code, the following applies:

- We have used the Python statistics package to compute the mean of the values in history.
- Finally, we used matplotlib to plot the SMA against the actual prices to observe the behavior.

The following plot is an output of the code:

![](_page_12_Figure_7.jpeg)

In this plot, it is easy to observe that the 20-day SMA has the intended smoothing effect and evens out the micro-volatility in the actual stock price, yielding a more stable price curve.

# **Exponential moving average**

The **exponential moving average**, which we will refer to as the **EMA**, is the single most well-known and widely used technical analysis indicator for time series data.

The EMA is similar to the simple moving average, but, instead of weighing all prices in the history equally, it places more weight on the most recent price observation and less weight on the older price observations. This is endeavoring to capture the intuitive idea that the new price observation has more up-to-date information than prices in the past. It is also possible to place more weight on older price observations and less weight on the newer price observations. This would try to capture the idea that longer-term trends have more information than short-term volatile price movements.

The weighting depends on the selected time period of the EMA; the shorter the time period, the more reactive the EMA is to new price observations; in other words, the EMA converges to new price observations faster and forgets older observations faster, also referred to as **Fast EMA**. The longer the time period, the less reactive the EMA is to new price observations; that is, EMA converges to new price observations slower and forgets older observations slower, also referred to as **Slow EMA**.

Based on the description of EMA, it is formulated as a weight factor, , applied to new price observations and a weight factor applied to the current value of EMA to get the new value of EMA. Since the sum of the weights should be 1 to keep the EMA units the same as price units, that is, \$s, the weight factor applied to EMA values turns out to be . Hence, we get the following two formulations of new EMA values based on old EMA values and new price observations, which are the same definitions, written in two different forms:

$$EMA = (P - EMA_{old}) \times \mu + EMA_{old}$$

Alternatively, we have the following:

$$EMA = P \times \mu + (1 - \mu) \times EMA_{old}$$

Here, the following applies:

: Current price of the instrument

: EMA value prior to the current price observation

: Smoothing constant, most commonly set to

: Number of time periods (similar to what we used in the simple moving average)

### **Implementation of the exponential moving average**

Let's implement an exponential moving average with 20 days as the number of time periods to compute the average over. We will use a default smoothing factor of *2 / (n + 1)* for this implementation. Similar to SMA, EMA also achieves an evening out across normal daily prices. EMA has the advantage of allowing us to weigh recent prices with higher weights than an SMA does, which does uniform weighting.

In the following code, we will see the implementation of the exponential moving average:

```
num_periods = 20 # number of days over which to average
K = 2 / (num_periods + 1) # smoothing constant
ema_p = 0
ema_values = [] # to hold computed EMA values
for close_price in close:
 if (ema_p == 0): # first observation, EMA = current-price
 ema_p = close_price
 else:
 ema_p = (close_price - ema_p) * K + ema_p
 ema_values.append(ema_p)
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(Exponential20DayMovingAverage=pd.Series(ema_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
ema = goog_data['Exponential20DayMovingAverage']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema.plot(ax=ax1, color='b', lw=2., legend=True)
plt.savefig('ema.png')
plt.show()
```

In the preceding code, the following applies:

- We used a list (ema\_values) to track EMA values computed so far.
- On each new observation of close price, we decay the difference from the old EMA value and update the old EMA value slightly to find the new EMA value.
- Finally, the matplotlib plot shows the difference between EMA and non-EMA prices.

Let's now have a look at the plot. This is the output of the code:

![](_page_16_Figure_0.jpeg)

From the plot, it is observed that EMA has a very similar smoothing effect to SMA, as expected, and it reduces the noise in the raw prices. However the extra parameter, , available in EMA in addition to the parameter , allows us to control the relative weight placed on the new price observation, as compared to older price observations. This allows us to build different variants of EMA by varying the parameter to make fast and slow EMAs, even for the same parameter, . We will explore fast and slow EMAs more in the rest of this chapter and in later chapters.

## **Absolute price oscillator**

The absolute price oscillator, which we will refer to as APO, is a class of indicators that builds on top of moving averages of prices to capture specific short-term deviations in prices.

The absolute price oscillator is computed by finding the difference between a fast exponential moving average and a slow exponential moving average. Intuitively, it is trying to measure how far the more reactive EMA ( ) is deviating from the more stable EMA ( ). A large difference is usually interpreted as one of two things: instrument prices are starting to trend or break out, or instrument prices are far away from their equilibrium prices, in other words, overbought or oversold:

#### **Implementation of the absolute price oscillator**

Let's now implement the absolute price oscillator, with the faster EMA using a period of 10 days and a slower EMA using a period of 40 days, and default smoothing factors being 2/11 and 2/41, respectively, for the two EMAs:

```
num_periods_fast = 10 # time period for the fast EMA
K_fast = 2 / (num_periods_fast + 1) # smoothing factor for fast EMA
ema_fast = 0
num_periods_slow = 40 # time period for slow EMA
K_slow = 2 / (num_periods_slow + 1) # smoothing factor for slow EMA
ema_slow = 0
ema_fast_values = [] # we will hold fast EMA values for visualization purposes
ema_slow_values = [] # we will hold slow EMA values for visualization purposes
apo_values = [] # track computed absolute price oscillator values
for close_price in close:
 if (ema_fast == 0): # first observation
 ema_fast = close_price
 ema_slow = close_price
 else:
 ema_fast = (close_price - ema_fast) * K_fast + ema_fast
 ema_slow = (close_price - ema_slow) * K_slow + ema_slow
 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 apo_values.append(ema_fast - ema_slow)
```

The preceding code generates APO values that have higher positive and negative values when the prices are moving away from long-term EMA very quickly (breaking out), which can have a trendstarting interpretation or an overbought/sold interpretation. Now, let's visualize the fast and slow EMAs and visualize the APO values generated:

```
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(FastExponential10DayMovingAverage=pd.Series(ema_fast_values, index=goog_data.index))
goog_data = goog_data.assign(SlowExponential40DayMovingAverage=pd.Series(ema_slow_values, index=goog_data.index))
goog_data = goog_data.assign(AbsolutePriceOscillator=pd.Series(apo_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
ema_f = goog_data['FastExponential10DayMovingAverage']
ema_s = goog_data['SlowExponential40DayMovingAverage']
apo = goog_data['AbsolutePriceOscillator']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema_f.plot(ax=ax1, color='b', lw=2., legend=True)
ema_s.plot(ax=ax1, color='r', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='APO')
apo.plot(ax=ax2, color='black', lw=2., legend=True)
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_19_Figure_0.jpeg)

One observation here is the difference in behavior between fast and slow EMAs. The faster one is more reactive to new price observations, and the slower one is less reactive to new price observations and decays slower. The APO values are positive when prices are breaking out to the upside, and the magnitude of the APO values captures the magnitude of the breakout. The APO values are negative when prices are breaking out to the downside, and the magnitude of the APO values captures the magnitude of the breakout. In a later chapter in this book, we will use this signal in a realistic trading strategy.

# **Moving average convergence divergence**

The moving average convergence divergence is another in the class of indicators that builds on top of moving averages of prices. We'll refer to it as MACD. This goes a step further than the APO. Let's look at it in greater detail.

The moving average convergence divergence was created by Gerald Appel. It is similar in spirit to an absolute price oscillator in that it establishes the difference between a fast exponential moving average and a slow exponential moving average. However, in the case of MACD, we apply a smoothing exponential moving average to the MACD value itself in order to get the final signal output from the MACD indicator. Optionally, you may also look at the difference between MACD values and the EMA of the MACD values (signal) and visualize it as a histogram. A properly configured MACD signal can successfully capture the direction, magnitude, and duration of a trending instrument price:

#### **Implementation of the moving average convergence divergence**

Let's implement a moving average convergence divergence signal with a fast EMA period of 10 days, a slow EMA period of 40 days, and with default smoothing factors of 2/11 and 2/41, respectively:

```
num_periods_fast = 10 # fast EMA time period
K_fast = 2 / (num_periods_fast + 1) # fast EMA smoothing factor
ema_fast = 0
num_periods_slow = 40 # slow EMA time period
K_slow = 2 / (num_periods_slow + 1) # slow EMA smoothing factor
ema_slow = 0
num_periods_macd = 20 # MACD EMA time period
K_macd = 2 / (num_periods_macd + 1) # MACD EMA smoothing factor
ema_macd = 0
ema_fast_values = [] # track fast EMA values for visualization purposes
ema_slow_values = [] # track slow EMA values for visualization purposes
macd_values = [] # track MACD values for visualization purposes
macd_signal_values = [] # MACD EMA values tracker
macd_histogram_values = [] # MACD - MACD-EMA
for close_price in close:
 if (ema_fast == 0): # first observation
 ema_fast = close_price
 ema_slow = close_price
 else:
 ema_fast = (close_price - ema_fast) * K_fast + ema_fast
 ema_slow = (close_price - ema_slow) * K_slow + ema_slow
 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 macd = ema_fast - ema_slow # MACD is fast_MA - slow_EMA
 if ema_macd == 0:
 ema_macd = macd
 else:
 ema_macd = (macd - ema_macd) * K_slow + ema_macd # signal is EMA of MACD values
 macd_values.append(macd)
 macd_signal_values.append(ema_macd)
 macd_histogram_values.append(macd - ema_macd)
```

In the preceding code, the following applies:

- The time period used a period of 20 days and a default smoothing factor of 2/21.
- We also computed a value ( ).

Let's look at the code to plot and visualize the different signals and see what we can understand from it:

![](_page_21_Picture_7.jpeg)

```
ax2 = fig.add_subplot(312, ylabel='MACD')
macd.plot(ax=ax2, color='black', lw=2., legend=True)
ema_macd.plot(ax=ax2, color='g', lw=2., legend=True)s
ax3 = fig.add_subplot(313, ylabel='MACD')
macd_histogram.plot(ax=ax3, color='r', kind='bar', legend=True, use_index=False)
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_22_Figure_2.jpeg)

The MACD signal is very similar to the APO, as we expected, but now, in addition, the is an additional smoothing factor on top of raw values to capture lasting trending periods by smoothing out the noise of raw values. Finally, the , which is the difference in the two series, captures (a) the time period when the trend is starting or reversion, and (b) the magnitude of lasting trends when values stay positive or negative after reversing signs.

## **Bollinger bands**

**Bollinger bands** (**BBANDS**) also builds on top of moving averages, but incorporates recent price volatility that makes the indicator more adaptive to different market conditions. Let's now discuss this in greater detail.

Bollinger bands is a well-known technical analysis indicator developed by John Bollinger. It computes a moving average of the prices (you can use the simple moving average or the exponential moving average or any other variant). In addition, it computes the standard deviation of the prices in the lookback period by treating the moving average as the mean price. It then creates an upper band that is a moving average, plus some multiple of standard price deviations, and a lower band that is a moving average minus multiple standard price deviations. This band represents the expected volatility of the prices by treating the moving average of the price as the reference price. Now, when prices move outside of these bands, that can be interpreted as a breakout/trend signal or an overbought/sold mean reversion signal.

Let's look at the equations to compute the upper Bollinger band, , and the lower Bollinger band, . Both depend, in the first instance, on the middle Bollinger band, , which is simply the simple moving average of the previous time periods( in this case, the last days ) denoted by . The upper and lower bands are then computed by adding/subtracting to , which is the product of standard deviation, , which we've seen before, and , which is a standard deviation factor of our choice. The larger the value of chosen, the greater the Bollinger bandwidth for our signal, so it is just a parameter that controls the width in our trading signal:

Here, the following applies:

: Standard deviation factor of our choice

To compute the standard deviation, first we compute the variance:

$$\sigma^2 = \frac{\sum_{i=1}^n (Pi-SMA)^2}{n}$$

Then, the standard deviation is simply the square root of the variance:

$$\sigma=\sqrt{\sigma^2}$$

#### **Implementation of Bollinger bands**

We will implement and visualize Bollinger bands, with 20 days as the time period for ( ):

```
import statistics as stats
import math as math
time_period = 20 # history length for Simple Moving Average for middle band
stdev_factor = 2 # Standard Deviation Scaling factor for the upper and lower bands
history = [] # price history for computing simple moving average
sma_values = [] # moving average of prices for visualization purposes
upper_band = [] # upper band values
lower_band = [] # lower band values
for close_price in close:
 history.append(close_price)
 if len(history) > time_period: # we only want to maintain at most 'time_period' number of price observations
 del (history[0])
 sma = stats.mean(history)
 sma_values.append(sma) # simple moving average or middle band
 variance = 0 # variance is the square of standard deviation
 for hist_price in history:
 variance = variance + ((hist_price - sma) ** 2)
 stdev = math.sqrt(variance / len(history)) # use square root to get standard deviation
 upper_band.append(sma + stdev_factor * stdev)
 lower_band.append(sma - stdev_factor * stdev)
```

In the preceding code, we used a stdev factor, , of 2 to compute the upper band and lower band from the middle band, and the standard deviation we compute.

Now, let's add some code to visualize the Bollinger bands and make some observations:

```
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(MiddleBollingerBand20DaySMA=pd.Series(sma_values, index=goog_data.index))
goog_data = goog_data.assign(UpperBollingerBand20DaySMA2StdevFactor=pd.Series(upper_band, index=goog_data.index))
goog_data = goog_data.assign(LowerBollingerBand20DaySMA2StdevFactor=pd.Series(lower_band, index=goog_data.index))
close_price = goog_data['ClosePrice']
mband = goog_data['MiddleBollingerBand20DaySMA']
uband = goog_data['UpperBollingerBand20DaySMA2StdevFactor']
lband = goog_data['LowerBollingerBand20DaySMA2StdevFactor']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
mband.plot(ax=ax1, color='b', lw=2., legend=True)
uband.plot(ax=ax1, color='g', lw=2., legend=True)
lband.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_26_Figure_0.jpeg)

For Bollinger bands, when prices stay within the upper and lower bounds, then not much can be said, but, when prices traverse the upper band, then one interpretation can be that prices are breaking out to the upside and will continue to do so. Another interpretation of the same event can be that the trading instrument is overbought and we should expect a bounce back down.

The other case is when prices traverse the lower band, then one interpretation can be that prices are breaking out to the downside and will continue to do so. Another interpretation of the same event can be that the trading instrument is oversold and we should expect a bounce back up. In either case, Bollinger bands helps us to quantify and capture the exact time when this happens.

## **Relative strength indicator**

The relative strength indicator, which we will refer to as RSI, is quite different from the previous indicators we saw that were based on moving averages of prices. This is based on price changes over periods to capture the strength/magnitude of price moves.

The relative strength indicator was developed by J Welles Wilder. It comprises a lookback period, which it uses to compute the magnitude of the average of gains/price increases over that period, as well as the magnitude of the averages of losses/price decreases over that period. Then, it computes the RSI value that normalizes the signal value to stay between 0 and 100, and attempts to capture if there have been many more gains relative to the losses, or if there have been many more losses relative to the gains. RSI values over 50% indicate an uptrend, while RSI values below 50% indicate a downtrend.

For the last n periods, the following applies:

$$Price > PreviousPrice => AbsoluteLossOverPeriod = 0$$

Otherwise, the following applies:

$$AbsoluteLossOverPeriod = PreviousPrice - Price \ Price < PreviousPrice \gets PreviousPrice \Rightarrow AbsoluteGainOverPeriod = 0$$

Otherwise, the following applies:

$$AbsoluteGainOverPeriod = Price - PreviousPrice \\\frac{\sum |GainsOverLastNPeriods|}{\frac{\sum |GainsOverLastNPeriods|}{n}}{\frac{\sum |LossesOverLastNPeriods|}{n}}$$
 $Relative Strength(RS) = \frac{\sum |GainsOverLastNPeriods|}{\sum |LossesOverLastNPeriods|}$ 

 $Relative StrengthIndicator(RSI) = 100 - \frac{100}{(1+RS)}$ 

#### **Implementation of the relative strength indicator**

Now, let's implement and plot a relative strength indicator on our dataset:

```
import statistics as stats
time_period = 20 # look back period to compute gains & losses
gain_history = [] # history of gains over look back period (0 if no gain, magnitude of gain if gain)
loss_history = [] # history of losses over look back period (0 if no loss, magnitude of loss if loss)
avg_gain_values = [] # track avg gains for visualization purposes
avg_loss_values = [] # track avg losses for visualization purposes
rsi_values = [] # track computed RSI values
last_price = 0 # current_price - last_price > 0 => gain. current_price - last_price < 0 => loss.
for close_price in close:
 if last_price == 0:
 last_price = close_price
 gain_history.append(max(0, close_price - last_price))
 loss_history.append(max(0, last_price - close_price))
 last_price = close_price
 if len(gain_history) > time_period: # maximum observations is equal to lookback period
 del (gain_history[0])
 del (loss_history[0])
 avg_gain = stats.mean(gain_history) # average gain over lookback period
 avg_loss = stats.mean(loss_history) # average loss over lookback period
 avg_gain_values.append(avg_gain)
 avg_loss_values.append(avg_loss)
 rs = 0
 if avg_loss > 0: # to avoid division by 0, which is undefined
 rs = avg_gain / avg_loss
 rsi = 100 - (100 / (1 + rs))
 rsi_values.append(rsi)
```

In the preceding code, the following applies:

- We have used 20 days as our time period over which we computed the average gains and losses and then normalized it to be between 0 and 100 based on our formula for values.
- For our dataset where prices have been steadily rising, it is obvious that the values are consistently over 50% or more.

Now, let's look at the code to visualize the final signal as well as the components involved:

```
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(RelativeStrengthAvgGainOver20Days=pd.Series(avg_gain_values, index=goog_data.index))
goog_data = goog_data.assign(RelativeStrengthAvgLossOver20Days=pd.Series(avg_loss_values, index=goog_data.index))
goog_data = goog_data.assign(RelativeStrengthIndicatorOver20Days=pd.Series(rsi_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
rs_gain = goog_data['RelativeStrengthAvgGainOver20Days']
rs_loss = goog_data['RelativeStrengthAvgLossOver20Days']
rsi = goog_data['RelativeStrengthIndicatorOver20Days']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(311, ylabel='Google price in $')
close_price.plot(ax=ax1, color='black', lw=2., legend=True)
ax2 = fig.add_subplot(312, ylabel='RS')
rs_gain.plot(ax=ax2, color='g', lw=2., legend=True)
rs_loss.plot(ax=ax2, color='r', lw=2., legend=True)
ax3 = fig.add_subplot(313, ylabel='RSI')
```

rsi.plot(ax=ax3, color='b', lw=2., legend=True) plt.show()

The preceding code will return the following output. Let's have a look at the plot:

![](_page_30_Figure_2.jpeg)

The first observation we can make from our analysis of the RSI signal applied to our GOOGLE dataset is that the AverageGain over our time frame of 20 days more often than not exceeds the AverageLoss over the same time frame, which intuitively makes sense because Google has been a very successful stock, increasing in value more or less consistently. Based on that, the RSI indicator also stays above 50% for the majority of the lifetime of the stock, again reflecting the continued gains in the Google stock over the course of its lifetime.

### **Standard deviation**

**Standard deviation**, which will be referred to as **STDEV**, is a basic measure of price volatility that is used in combination with a lot of other technical analysis indicators to improve them. We'll explore that in greater detail in this section.

Standard deviation is a standard measure that is computed by measuring the squared deviation of individual prices from the mean price, and then finding the average of all those squared deviation values. This value is known as **variance**, and the standard deviation is obtained by taking the square root of the variance. Larger STDEVs are a mark of more volatile markets or larger expected price moves, so trading strategies need to factor that increased volatility into risk estimates and other trading behavior.

To compute standard deviation, first we compute the variance:

$$\sigma^2 = \frac{\sum_{i=1}^n (Pi-SMA)^2}{n}$$

Then, standard deviation is simply the square root of the variance:

$$\sigma=\sqrt{\sigma^2}$$

: Simple moving average over n time periods.

### **Implementing standard derivatives**

Let's have a look at the following code, which demonstrates the implementation of standard derivatives.

We are going to import the statistics and the math library we need to perform basic mathematical operations. We are defining the loopback period with the variable time\_period, and we will store the past prices in the list history, while we will store the SMA and the standard deviation in sma\_values and stddev\_values. In the code, we calculate the variance, and then we calculate the standard deviation. To finish, we append to the goog\_data data frame that we will use to display the chart:

```
import statistics as stats
import math as math
time_period = 20 # look back period
history = [] # history of prices
sma_values = [] # to track moving average values for visualization purposes
stddev_values = [] # history of computed stdev values
for close_price in close:
 history.append(close_price)
 if len(history) > time_period: # we track at most 'time_period' number of prices
 del (history[0])
 sma = stats.mean(history)
 sma_values.append(sma)
 variance = 0 # variance is square of standard deviation
 for hist_price in history:
 variance = variance + ((hist_price - sma) ** 2)
 stdev = math.sqrt(variance / len(history))
 stddev_values.append(stdev)
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(StandardDeviationOver20Days=pd.Series(stddev_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
stddev = goog_data['StandardDeviationOver20Days']
```

The preceding code will build the final visualizations:

```
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='Stddev in $')
stddev.plot(ax=ax2, color='b', lw=2., legend=True)
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_33_Figure_0.jpeg)

Here, the standard deviation quantifies the volatility in the price moves during the last 20 days. Volatility spikes when the Google stock prices spike up or spike down or go through large changes over the last 20 days. We will revisit the standard deviation as an important volatility measure in later chapters.

# **Momentum**

**Momentum**, also referred to as **MOM**, is an important measure of speed and magnitude of price moves. This is often a key indicator of trend/breakout-based trading algorithms.

In its simplest form, momentum is simply the difference between the current price and price of some fixed time periods in the past. Consecutive periods of positive momentum values indicate an uptrend; conversely, if momentum is consecutively negative, that indicates a downtrend. Often, we use simple/exponential moving averages of the MOM indicator, as shown here, to detect sustained trends:

Here, the following applies:

- : Price at time *t*
- : Price *n* time periods before time *t*

### **Implementation of momentum**

Now, let's have a look at the code that demonstrates the implementation of momentum:

```
time_period = 20 # how far to look back to find reference price to compute momentum
history = [] # history of observed prices to use in momentum calculation
mom_values = [] # track momentum values for visualization purposes
for close_price in close:
 history.append(close_price)
 if len(history) > time_period: # history is at most 'time_period' number of observations
 del (history[0])
 mom = close_price - history[0]
 mom_values.append(mom)
```

This maintains a list history of past prices and, at each new observation, computes the momentum to be the difference between the current price and the price time\_period days ago, which, in this case, is 20 days:

```
goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(MomentumFromPrice20DaysAgo=pd.Series(mom_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
mom = goog_data['MomentumFromPrice20DaysAgo']
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='Momentum in $')
mom.plot(ax=ax2, color='b', lw=2., legend=True)
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_35_Figure_6.jpeg)

The plot for momentum shows us the following:

- Momentum values peak when the stock price changes by a large amount as compared to the price 20 days ago.
- Here, most momentum values are positive, mainly because, as we discussed in the previous section, Google stock has been increasing in value over the course of its lifetime and has large upward momentum values from time to time.
- During the brief periods where the stock prices drop in value, we can observe negative momentum values.

In this section, we learned how to create trading signals based on technical analysis. In the next section, we will learn how to implement advanced concepts, such as seasonality, in trading instruments.

#### **Implementing advanced concepts, such as seasonality, in trading instruments**

In trading, the price we receive is a collection of data points at constant time intervals called time series. They are time dependent and can have increasing or decreasing trends and seasonality trends, in other words, variations specific to a particular time frame. Like any other retail products, financial products follow trends and seasonality during different seasons. There are multiple seasonality effects: weekend, monthly, and holidays.

In this section, we will use the GOOG data from 2001 to 2018 to study price variations based on the months.

1. We will write the code to regroup the data by months, calculate and return the monthly returns, and then compare these returns in a histogram. We will observe that GOOG has a higher return in October:

```
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
start_date = '2001-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME='goog_data_large.pkl'
try:
 goog_data = pd.read_pickle(SRC_DATA_FILENAME)
 print('File data found...reading GOOG data')
except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 goog_data.to_pickle(SRC_DATA_FILENAME)
goog_monthly_return = goog_data['Adj Close'].pct_change().groupby(
 [goog_data['Adj Close'].index.year,
 goog_data['Adj Close'].index.month]).mean()
goog_montly_return_list=[]
for i in range(len(goog_monthly_return)):
 goog_montly_return_list.append\
 ({'month':goog_monthly_return.index[i][1],
 'monthly_return': goog_monthly_return[i]})
goog_montly_return_list=pd.DataFrame(goog_montly_return_list,
 columns=('month','monthly_return'))
goog_montly_return_list.boxplot(column='monthly_return', by='month')
ax = plt.gca()
labels = [item.get_text() for item in ax.get_xticklabels()]
labels=['Jan','Feb','Mar','Apr','May','Jun',\
 'Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticklabels(labels)
ax.set_ylabel('GOOG return')
plt.tick_params(axis='both', which='major', labelsize=7)
plt.title("GOOG Monthly return 2001-2018")
plt.suptitle("")
plt.show()
```

The preceding code will return the following output. The following screenshot represents the GOOG monthly return:

![](_page_38_Figure_0.jpeg)

In this screenshot, we observe that there are repetitive patterns. The month of October is the month when the return seems to be the highest, unlike November, where we observe a drop in the return.

- 2. Since it is a time series, we will study the stationary (mean, variance remain constant over time). In the following code, we will check this property because the following time series models work on the assumption that time series are stationary:
- Constant mean
- Constant variance
- Time-independent autocovariance

```
# Displaying rolling statistics
def plot_rolling_statistics_ts(ts, titletext,ytext, window_size=12):
 ts.plot(color='red', label='Original', lw=0.5)
 ts.rolling(window_size).mean().plot(
 color='blue',label='Rolling Mean')
 ts.rolling(window_size).std().plot(
 color='black', label='Rolling Std')
 plt.legend(loc='best')
 plt.ylabel(ytext)
 plt.title(titletext)
 plt.show(block=False)
plot_rolling_statistics_ts(goog_monthly_return[1:],'GOOG prices rolling mean and standard deviation','Monthly return')
```

plot\_rolling\_statistics\_ts(goog\_data['Adj Close'],'GOOG prices rolling mean and standard deviation','Daily prices',365)

The preceding code will return the following two charts, where we will compare the difference using two different time series.

- One shows the GOOG daily prices, and the other one shows the GOOG monthly return.
- We observe that the rolling average and rolling variance are not constant when using the daily prices instead of using the daily return.
- This means that the first time series representing the daily prices is not stationary. Therefore, we will need to make this time series stationary.

The non-stationary for a time series can generally be attributed to two factors: trend and seasonality.

The following plot shows GOOG daily prices:

![](_page_39_Figure_2.jpeg)

When observing the plot of the GOOG daily prices, the following can be stated:

- We can see that the price is growing over time; this is a trend.
- The wave effect we are observing on the GOOG daily prices comes from seasonality.
- When we make a time series stationary, we remove the trend and seasonality by modeling and removing them from the initial data.
- Once we find a model predicting future values for the data without seasonality and trend, we can apply back the seasonality and trend values to get the actual forecasted data.

The following plot shows the GOOG monthly return:

![](_page_40_Figure_0.jpeg)

For the data using the GOOG daily prices, we can just remove the trend by subtracting the moving average from the daily prices in order to obtain the following screenshot:

- We can now observe the trend disappeared.
- Additionally, we also want to remove seasonality; for that, we can apply differentiation.
- For the differentiation, we will calculate the difference between two consecutive days; we will then use the difference as data points.

![](_page_40_Figure_5.jpeg)

![](_page_41_Picture_0.jpeg)

*We recommend that you read a book on time series to go deeper in an analysis of the same: Practical Time Series Analysis: Master Time Series Data Processing, Visualization, and Modeling Using Python, Packt edition.*

3. To confirm our observation, in the code, we use the popular statistical test: the augmented Dickey-Fuller test:

- This determines the presence of a unit root in time series.
- If a unit root is present, the time series is not stationary.
- The null hypothesis of this test is that the series has a unit root.
- If we reject the null hypothesis, this means that we don't find a unit root.
- If we fail to reject the null hypothesis, we can say that the time series is non-stationary:

```
def test_stationarity(timeseries):
 print('Results of Dickey-Fuller Test:')
 dftest = adfuller(timeseries[1:], autolag='AIC')
 dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
 print (dfoutput)
test_stationarity(goog_data['Adj Close'])
```

4. This test returns a p-value of 0.99. Therefore, the time series is not stationary. Let's have a look at the test:

test\_stationarity(goog\_monthly\_return[1:])

This test returns a p-value of less than 0.05. Therefore, we cannot say that the time series is not stationary. We recommend using daily returns when studying financial products. In the example of stationary, we could observe that no transformation is needed.

5. The last step of the time series analysis is to forecast the time series. We have two possible scenarios:

- A strictly stationary series without dependencies among values. We can use a regular linear regression to forecast values.
- A series with dependencies among values. We will be forced to use other statistical models. In this chapter, we chose to focus on using the **Auto-Regression Integrated Moving Averages** (**ARIMA**) model. This model has three parameters:
  - Autoregressive *(AR)* term *(p)—*lags of dependent variables. Example for 3, the predictors for *x(t)* is *x(t-1) + x(t-2) + x(t-3).*
  - Moving average *(MA)* term *(q)—*lags for errors in prediction. Example for 3, the predictor for *x(t)* is *e(t-1) + e(t-2) + e(t-3),* where *e(i)* is the difference between the moving average value and the actual value.
  - Differentiation *(d)—* This is the *d* number of occasions where we apply differentiation between values, as was explained when we studied the GOOG daily price. If *d=1*, we proceed with the difference between two consecutive values.

The parameter values for AR(p) and MA(q) can be respectively found by using the **autocorrelation function** (**ACF**) and the **partial autocorrelation function** (**PACF**):

```
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from matplotlib import pyplot
pyplot.figure()
pyplot.subplot(211)
plot_acf(goog_monthly_return[1:], ax=pyplot.gca(),lags=10)
pyplot.subplot(212)
plot_pacf(goog_monthly_return[1:], ax=pyplot.gca(),lags=10)
pyplot.show()
```

Now, let's have a look at the output of the code:

![](_page_42_Figure_0.jpeg)

When we observe the two preceding diagrams, we can draw the confidence interval on either side of 0. We will use this confidence interval to determine the parameter values for the AR(p) and MA(q).

- **q**: The lag value is q=1 when the ACF plot crosses the upper confidence interval for the first time.
- **p**: The lag value is p=1 when the PACF chart crosses the upper confidence interval for the first time.

6. These two graphs suggest using *q=1* and *p=1*. We will apply the ARIMA model in the following code:

```
from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(goog_monthly_return[1:], order=(2, 0, 2))
fitted_results = model.fit()
goog_monthly_return[1:].plot()
fitted_results.fittedvalues.plot(color='red')
plt.show()
```

As shown in the code, we applied the ARIMA model to the time series and it is representing the monthly return.

# **Summary**

In this chapter, we explored concepts of generating trading signals, such as support and resistance, based on the intuitive ideas of supply and demand that are fundamental forces that drive market prices. We also briefly explored how you might use support and resistance to implement a simple trading strategy. Then, we looked into a variety of technical analysis indicators, explained the intuition behind them, and implemented and visualized their behavior during different price movements. We also introduced and implemented the ideas behind advanced mathematical approaches, such as **Autoregressive** (**AR**), **Moving Average** (**MA**), **Differentiation** (**D**), **AutoCorrelation Function** (**ACF**), and **Partial Autocorrelation Function** (**PACF**) for dealing with non-stationary time series datasets. Finally, we briefly introduced an advanced concept such as seasonality, which explains how there are repeating patterns in financial datasets, basic time series analysis and concepts of stationary or nonstationary time series, and how you may model financial data that displays that behavior.

In the next chapter, we will review and implement some simple regression and classification methods and understand the advantages of applying supervised statistical learning methods to trading.
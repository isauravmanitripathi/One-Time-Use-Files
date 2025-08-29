# **Section 3: Algorithmic Trading Strategies**

In this section, you will learn about the workings and implementation of some well-known trading strategies as well as learn how to trade on the basis of basic information (trends, seasonality, the correlation between symbols in the market, and correlation between events).

This section comprises the following chapters:

- Chapter 4, *Classical Trading Strategies Driven by Human Intuition*
- Chapter 5, *Sophisticated Algorithmic Strategies*
- Chapter 6, *Managing Risk in Algorithmic Strategies*

### **Classical Trading Strategies Driven by Human Intuition**

During the previous chapters, we used statistical methods to predict market price movement from historical data. You may think that you know how to manipulate data, but how can these statistical techniques be applied to real trading? After spending so much time working on data, you may also want to know some key trading strategies that you can apply to make money.

In this chapter, we will talk about basic algorithmic strategies that follow human intuition. We will learn how to create trading strategies based on momentum and trend following, and a strategy that works for markets with mean reversion behavior. We will also talk about their advantages and disadvantages. By the end of this chapter, you will know how to use an idea to create a basic trading strategy.

This chapter will cover the following topics:

- Creating a trading strategy based on momentum and trend following
- Creating a trading strategy that works for markets with mean reversion behavior
- Creating trading strategies that operate on linearly correlated groups of trading instruments

### **Creating a trading strategy based on momentum and trend following**

Momentum strategy uses the trend to predict the future of a price. For instance, if the price of an asset has increased for the last 20 days, it is likely that this price will continue rising. The moving average strategy is one example of momentum strategy.

Momentum strategies assume that the future will follow the past by following an upward or a downward trend (divergence or trend trading). Momentum investment has been used for decades: *buying low, selling high*, *buying high, and selling higher*, *selling the losers and letting the winners ride;* all these techniques are the origin of momentum trading. Momentum investing adopts short-term positions in relation to financial products going up and sells them when they go down. When we use a momentum strategy, we try to be ahead of the market; we trade fast, and then we let the market come to the same conclusion. The earlier we realize that there is a change, the more profitable we will be.

When you start working on a momentum strategy, you need to select the assets you are going to focus on while considering the risk for trading these assets. You need to ensure entering at the right time, but also not changing position too late. One of the most important drawback of this kind of strategy is the time and the fees. If your trading system is too slow, you won't manage to capture the opportunity to make money before the competition. Aside from this problem, we have to add the transaction fees, which are not negligible. By the very nature of the momentum strategy, the accuracy of this model is very low if news impacts the market.

Advantages of the momentum strategy:

This class of strategy is easy to understand.

Disadvantages of the momentum strategy:

- This class of strategy doesn't take into account noises or special events. It has a tendency to smooth out prior events.
- The transaction fees can be potentially high owing to the number of orders.

### **Examples of momentum strategies**

The following are some examples of momentum strategies:

- **Moving average crossover**: This momentum strategy principle revolves around calculating the moving average for a price of an asset and detecting when the price moves from one side of a moving average to the other. This means that when the current price intersects the moving average, there is a change in the momentum. However, this can lead to too many momentum changes. To limit this effect, we can use the dual moving average crossover.
- **Dual moving average crossover**: Because we want to limit the number of switches, we introduce an additional moving average. There will be a short-term moving average and a long-term moving average. With this implementation, the momentum shifts in the direction of the short-term moving average. When the short-term moving average crosses the long-term moving average and its value exceeds that of the long-term moving average, the momentum will be upward and this can lead to the adoption of a long position. If the movement is in the opposite direction, this can lead to take a short position instead.
- **Turtle trading**: Unlike the two other implementations, this momentum strategy doesn't use any moving average but relies on having a number of specific days, which are high and low.

### **Python implementation**

For the Python implementation of this section, we will implement the dual moving average. This strategy is based on the indicator of moving average. It is widely used to smooth out price movements by filtering non-significant noises. Let's have a look at the implementations in the following subsections.

### **Dual moving average**

In this section, we will implement the double moving average strategy. We will use the same code pattern from the prior chapters to get the GOOG data:

1. This code will first check whether the goog\_data\_large.pkl file exists. If the file does not exist, we will fetch the GOOG data from Yahoo finance:

```
import pandas as pd
import numpy as np
from pandas_datareader import data
def load_financial_data(start_date, end_date,output_file):
 try:
 df = pd.read_pickle(output_file)
 print('File data found...reading GOOG data')
 except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 df = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 df.to_pickle(output_file)
 return df
 goog_data=load_financial_data(start_date='2001-01-01',
 end_date = '2018-01-01',
 output_file='goog_data_large.pkl')
```

- 2. Next, as shown in the preceding code, we will create a double\_moving\_average function with parameters fixing the size of the two moving averages returning a data frame:
- short\_mavg: Short-term moving average values
- long\_mavg: Long-term moving average values
- signal: True if the short-term moving average is higher than the long-term moving average
- orders: 1 for the buy order, and -1 for the sell order:

```
def double_moving_average(financial_data, short_window, long_window):
 signals = pd.DataFrame(index=financial_data.index)
 signals['signal'] = 0.0
 signals['short_mavg'] = financial_data['Close'].\
 rolling(window=short_window,
 min_periods=1, center=False).mean()
 signals['long_mavg'] = financial_data['Close'].\
 rolling(window=long_window,
 min_periods=1, center=False).mean()
 signals['signal'][short_window:] =\
 np.where(signals['short_mavg'][short_window:]
 > signals['long_mavg'][short_window:], 1.0, 0.0)
 signals['orders'] = signals['signal'].diff()
 return signals
 ts=double_moving_average(goog_data,20,100)
```

The code will build the data frame, ts:

- This data frame will contain the signal column storing the signal of going long (value 1) and going short (value 0)
- The column *orders* will contain the side of the orders (buy or sell)

3. We will now write the code to display the curve representing the orders for the dual moving strategy:

```
 fig = plt.figure()
 ax1 = fig.add_subplot(111, ylabel='Google price in $')
 goog_data["Adj Close"].plot(ax=ax1, color='g', lw=.5)
 ts["short_mavg"].plot(ax=ax1, color='r', lw=2.)
 ts["long_mavg"].plot(ax=ax1, color='b', lw=2.)
 ax1.plot(ts.loc[ts.orders== 1.0].index,
 goog_data["Adj Close"][ts.orders == 1.0],
 '^', markersize=7, color='k')
 ax1.plot(ts.loc[ts.orders== -1.0].index,
 goog_data["Adj Close"][ts.orders == -1.0],
 'v', markersize=7, color='k')
 plt.legend(["Price","Short mavg","Long mavg","Buy","Sell"])
 plt.title("Double Moving Average Trading Strategy")
 plt.show()
```

This code will return the following output. Let's have a look at the plot:

![](_page_7_Figure_3.jpeg)

The plot represents the GOOG prices and the two moving averages associated with this price. Each order is represented by an arrow.

### **Naive trading strategy**

In this section, we will implement a naive strategy based on the number of times a price increases or decreases. This strategy is based on the historical price momentum. Let's have a look at the code:

```
def naive_momentum_trading(financial_data, nb_conseq_days):
 signals = pd.DataFrame(index=financial_data.index)
 signals['orders'] = 0
 cons_day=0
 prior_price=0
 init=True
 for k in range(len(financial_data['Adj Close'])):
 price=financial_data['Adj Close'][k]
 if init:
 prior_price=price
 init=False
 elif price>prior_price:
 if cons_day<0:
 cons_day=0
 cons_day+=1
 elif price<prior_price:
 if cons_day>0:
 cons_day=0
 cons_day-=1
 if cons_day==nb_conseq_days:
 signals['orders'][k]=1
 elif cons_day == -nb_conseq_days:
 signals['orders'][k]=-1
 return signals
 ts=naive_momentum_trading(goog_data, 5)
```

In this code, the following applies:

- We count the number of times a price is improved.
- If the number is equal to a given threshold, we buy, assuming the price will keep rising.
- We will sell if we assume that the price will keep going down.

We will display the evolution of the trading strategy by using the following code:

```
fig = plt.figure()
 ax1 = fig.add_subplot(111, ylabel='Google price in $')
 goog_data["Adj Close"].plot(ax=ax1, color='g', lw=.5)
```

```
 ax1.plot(ts.loc[ts.orders== 1.0].index,
 goog_data["Adj Close"][ts.orders == 1],
 '^', markersize=7, color='k')
 ax1.plot(ts.loc[ts.orders== -1.0].index,
 goog_data["Adj Close"][ts.orders == -1],
 'v', markersize=7, color='k')
 plt.legend(["Price","Buy","Sell"])
 plt.title("Turtle Trading Strategy")
 plt.show()
```

This code will return the following output. This curve represents the orders for the naive momentum trading strategy:

![](_page_9_Figure_2.jpeg)

From this plot, the following can be observed:

- The naive trading strategy does not produce many orders.
- We can have a higher return if we have more orders. For that, we will use the following strategy to increase the number of orders.

### **Turtle strategy**

In this more advanced trading strategy, we are going to create a long signal when the price reaches the highest price for the last window\_size days (in this example, we will choose 50):

1. We will create a short signal when the price reaches its lowest point. We will get out of a position by having the price crossing the moving average of the last window\_size days. This code starts the turtle\_trading function by creating a column to store the highs, the lows, and the average with a rolling window window\_size:

```
def turtle_trading(financial_data, window_size):
 signals = pd.DataFrame(index=financial_data.index)
 signals['orders'] = 0
 # window_size-days high
 signals['high'] = financial_data['Adj Close'].shift(1).\
 rolling(window=window_size).max()
 # window_size-days low
 signals['low'] = financial_data['Adj Close'].shift(1).\
 rolling(window=window_size).min()
 # window_size-days mean
 signals['avg'] = financial_data['Adj Close'].shift(1).\
 rolling(window=window_size).mean()
```

- 2. We will write the code that creates two new columns specifying the rules to place an order:
- The entry rule is stock price > the highest value for the window\_size day.
- Stock price < the lowest value for the window\_size day:

```
 signals['long_entry'] = financial_data['Adj Close'] > signals.high
 signals['short_entry'] = financial_data['Adj Close'] < signals.low
```

3. The exit rule (when placing an order to get out of a position) will be when the stock price crosses the mean of past window\_size days:

```
 signals['long_exit'] = financial_data['Adj Close'] < signals.avg
 signals['short_exit'] = financial_data['Adj Close'] > signals.avg
```

4. To draw the chart representing the orders, as shown in the code, we will give the values 1 when we enter a long position, -1 when we enter a short position, and 0 for not changing anything:

```
 init=True
 position=0
 for k in range(len(signals)):
 if signals['long_entry'][k] and position==0:
 signals.orders.values[k] = 1
 position=1
 elif signals['short_entry'][k] and position==0:
 signals.orders.values[k] = -1
 position=-1
 elif signals['short_exit'][k] and position>0:
 signals.orders.values[k] = -1
 position = 0
 elif signals['long_exit'][k] and position < 0:
 signals.orders.values[k] = 1
 position = 0
 else:
 signals.orders.values[k] = 0
 return signals
 ts=turtle_trading(goog_data, 50)
```

The turtle\_trading function from the code will display the plot that describes how the strategy behaves:

![](_page_12_Figure_0.jpeg)

From the plot, the following can be observed:

- The number of orders between the naive momentum strategy and the turtle trading strategy.
- On account of a higher number of orders, this strategy offers more potential of returns than the previous one.

### **Creating a trading strategy that works for markets with reversion behavior**

After the momentum strategy, we will now look at another very popular type of strategy, the mean reversion strategy. The underlying precept is that prices revert toward the mean. Extreme events are followed by more normal events. We will find a time where a value such as the price or the return is very different from the past values. Once established, we will place an order by forecasting that this value will come back to the mean.

Reversion strategy uses the belief that the trend of quantity will eventually reverse. This is the opposite of the previous strategy. If a stock return increases too fast, it will eventually return to its average. Reversion strategies assume that any trend will go back to the average value, either an upward or downward trend (divergence or trend trading).

Advantages of the reversion strategy:

This class of strategy is easy to understand.

Disadvantages of the reversion strategy:

This class of strategy doesn't take into account noise or special events. It has a tendency to smooth out prior events.

### **Examples of reversion strategies**

Here are the examples of reversion strategies:

- **Mean reversion strategy**: This strategy assumes that the value of a price/return will return to the average value.
- Unlike the mean reversion strategy, pair trading—mean reversion is based on the correlation between two instruments. If a pair of stocks already has a high correlation and, at some point, the correlation is diminished, it will come back to the original level (correlation mean value). If the stock with the lower price drops, we can long this stock and short the other stock of this pair.

### **Creating trading strategies that operate on linearly correlated groups of trading instruments**

We are going through the process of implementing an example of a pair trading strategy. The first step is to determine the pairs that have a high correlation. This can be based on the underlying economic relationship (for example, companies having similar business plans) or also a financial product created out of some others, such as ETF. Once we figure out which symbols are correlated, we will create the trading signals based on the value of these correlations. The correlation value can be the Pearson's coefficient, or a Z-score.

In case of a temporary divergence, the outperforming stock (the stock that moved up) would have been sold and the underperforming stock (the stock that moved down) would have been purchased. If the two stocks converge by either the outperforming stock moving back down or the underperforming stock moving back up, or both, you will make money in such cases. You won't make money in the event that both stocks move up or down together with no change in the spread between them. Pairs trading is a market neutral trading strategy as it allows traders to profit from changing market conditions:

1. Let's begin by creating a function establishing cointegration between pairs, as shown in the following code. This function takes as inputs a list of financial instruments and calculates the cointegration values of these symbols. The values are stored in a matrix. We will use this matrix to display a heatmap:

```
def find_cointegrated_pairs(data):
 n = data.shape[1]
 pvalue_matrix = np.ones((n, n))
 keys = data.keys()
 pairs = []
 for i in range(n):
 for j in range(i+1, n):
 result = coint(data[keys[i]], data[keys[j]])
 pvalue_matrix[i, j] = result[1]
 if result[1] < 0.02:
 pairs.append((keys[i], keys[j]))
 return pvalue_matrix, pairs
```

2. Next, as shown in the code, we will load the financial data by using the panda data reader. This time, we load many symbols at the same time. In this example, we use SPY (this symbol reflects market movement), APPL (technology), ADBE (technology), LUV (airlines), MSFT (technology), SKYW (airline industry), QCOM (technology), HPQ (technology), JNPR (technology), AMD (technology), and IBM (technology).

Since the goal of this trading strategy is to find co-integrated symbols, we narrow down the search space according to industry. This function will load the data of a file from the Yahoo finance website if the data is not in the multi\_data\_large.pkl file:

```
import pandas as pd
 pd.set_option('display.max_rows', 500)
 pd.set_option('display.max_columns', 500)
 pd.set_option('display.width', 1000)
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint
import seaborn
from pandas_datareader import data
 symbolsIds = ['SPY','AAPL','ADBE','LUV','MSFT','SKYW','QCOM',
 'HPQ','JNPR','AMD','IBM']
def load_financial_data(symbols, start_date, end_date,output_file):
 try:
 df = pd.read_pickle(output_file)
 print('File data found...reading symbols data')
 except FileNotFoundError:
 print('File not found...downloading the symbols data')
 df = data.DataReader(symbols, 'yahoo', start_date, end_date)
 df.to_pickle(output_file)
 return df
```

data=load\_financial\_data(symbolsIds,start\_date=**'2001-01-01'**,

```
 end_date = '2018-01-01',
 output_file='multi_data_large.pkl')
```

- 3. After we call the load\_financial\_data function, we will then call the find\_cointegrated\_pairs function, as shown in the following code:
- pvalues, pairs = find\_cointegrated\_pairs(data[**'Adj Close'**])
- 4. We will use the seaborn package to draw the heatmap. The code calls the heatmap function from the seaborn package. Heatmap will use the list of symbols on the *x* and *y* axes. The last argument will mask the pvalues higher than 0.98:

```
seaborn.heatmap(pvalues, xticklabels=symbolsIds,
 yticklabels=symbolsIds, cmap='RdYlGn_r',
 mask = (pvalues >= 0.98))
```

This code will return the following map as an output. This map shows the p-values of the return of the coin:

- If a p-value is lower than 0.02, this means the null hypothesis is rejected.
- This means that the two series of prices corresponding to two different symbols can be co-integrated.
- This means that the two symbols will keep the same spread on average. On the heatmap, we observe that the following symbols have p-values lower than 0.02:

![](_page_16_Figure_9.jpeg)

This screenshot represents the heatmap measuring the cointegration between a pair of symbols. If it is red, this means that the p-value is 1, which means that the null hypothesis is not rejected. Therefore, there is no significant evidence that the pair of symbols is co-integrated. After selecting the pairs we will use for trading, let's focus on how to trade these pairs of symbols.

5. First, let's create a pair of symbols artificially to get an idea of how to trade. We will use the following libraries:

```
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt
```

6. As shown in the code, let's create a symbol return that we will call Symbol1. The value of the Symbol1 price starts from a value of 10 and, every day, it will vary based on a random return (following a normal distribution). We will draw the price values by using the function plot of the matplotlib.pyplot package:

```
# Set a seed value to make the experience reproducible
 np.random.seed(123)
```

```
 # Generate Symbol1 daily returns
 Symbol1_returns = np.random.normal(0, 1, 100)
 # Create a series for Symbol1 prices
 Symbol1_prices = pd.Series(np.cumsum(Symbol1_returns), name='Symbol1') + 10
 Symbol1_prices.plot(figsize=(15,7))
 plt.show()
```

7. We build the Symbol2 prices based on the behavior of the Symbol1 prices, as shown in the code. In addition to copying the behavior of Symbol1, we will add noises. The noise is a random value following a normal distribution. The introduction of this noise is designed to mimic market fluctuations. It changes the spread value between the two symbol prices:

```
# Create a series for Symbol2 prices
 # We will copy the Symbol1 behavior
 noise = np.random.normal(0, 1, 100)
 Symbol2_prices = Symbol1_prices + 10 + noise
 Symbol2_prices.name = 'Symbol2'
 plt.title("Symbol 1 and Symbol 2 prices")
 Symbol1_prices.plot()
 Symbol2_prices.plot()
 plt.show()
```

This code will return the following output. The plot shows the evolution of the price of Symbol 1 and Symbol 2:

![](_page_17_Figure_4.jpeg)

8. In the code, we will check the cointegration between the two symbols by using the coint function. This takes two lists/series of values and performs a test to check whether the two series are co-integrated:

score, pvalue, \_ = coint(Symbol1\_prices, Symbol2\_prices)

In the code, pvalue contains the p-score. Its value is 10-13, which means that we can reject the null hypothesis. Therefore, these two symbols are co-integrated.

9. We will define the zscore function. This function returns how far a piece of data is from the population mean. This will help us to choose the direction of trading. If the return value of this function is positive, this means that the symbol price is higher than the average price value. Therefore, its price is expected to go down or the paired symbol value will go up. In this case, we will want to short this symbol and long the other one. The code implements the zscore function:

```
def zscore(series):
 return (series - series.mean()) / np.std(series)
```

10. We will use the ratio between the two symbol prices. We will need to set the threshold that defines when a given price is far off the mean price value. For that, we will need to use specific values for a given symbol. If we have many symbols we want to trade with, this will imply that this analysis be performed for all the symbols. Since we want to avoid this tedious work, we are going to normalize this study by analyzing the ratio of the two prices instead. As a result, we calculate the ratios of the Symbol 1 price against the Symbol 2 price. Let's have a look at the code:

 ratios = Symbol1\_prices / Symbol2\_prices ratios.plot()

This code will return the following output. In the diagram, we show the variation in the ratio between symbol 1 and symbol 2 prices:

![](_page_18_Figure_3.jpeg)

11. Let's draw the chart showing when we will place orders with the following code:

```
 train = ratios[:75]
 test = ratios[75:]
 plt.axhline(ratios.mean())
 plt.legend([' Ratio'])
 plt.show()
 zscore(ratios).plot()
 plt.axhline(zscore(ratios).mean(),color="black")
 plt.axhline(1.0, color="red")
 plt.axhline(-1.0, color="green")
 plt.show()
```

This code will return the following output. The curve demonstrates the following:

- The Z-score evolution with horizontal lines at -1 (green), +1 (red), and the average of Z-score (black).
- The average of Z-score is 0.
- When the Z-score reaches -1 or +1, we will use this event as a trading signal. The values +1 and -1 are arbitrary values.
- It should be set depending on the study we will run in order to create this trading strategy:

![](_page_19_Figure_0.jpeg)

12. Every time the Z-score reaches one of the thresholds, we have a trading signal. As shown in the code, we will present a graph, each time we go long for Symbol 1 with a green marker, and each time we go short with a red marker:

```
 ratios.plot()
 buy = ratios.copy()
 sell = ratios.copy()
 buy[zscore(ratios)>-1] = 0
 sell[zscore(ratios)<1] = 0
 buy.plot(color="g", linestyle="None", marker="^")
 sell.plot(color="r", linestyle="None", marker="v")
 x1,x2,y1,y2 = plt.axis()
 plt.axis((x1,x2,ratios.min(),ratios.max()))
 plt.legend(["Ratio", "Buy Signal", "Sell Signal"])
 plt.show()
```

This code will return the following output. Let's have a look at the plot:

![](_page_20_Figure_0.jpeg)

In this example, going long for Symbol 1 means that we will send a buy order for Symbol 1, while sending a sell order for Symbol 2 concurrently.

13. Next, we will write the following code, which represents the buy and sell order for each symbol:

```
Symbol1_prices.plot()
 symbol1_buy[zscore(ratios)>-1] = 0
 symbol1_sell[zscore(ratios)<1] = 0
 symbol1_buy.plot(color="g", linestyle="None", marker="^")
 symbol1_sell.plot(color="r", linestyle="None", marker="v")
 Symbol2_prices.plot()
 symbol2_buy[zscore(ratios)<1] = 0
 symbol2_sell[zscore(ratios)>-1] = 0
 symbol2_buy.plot(color="g", linestyle="None", marker="^")
 symbol2_sell.plot(color="r", linestyle="None", marker="v")
 x1,x2,y1,y2 = plt.axis()
 plt.axis((x1,x2,Symbol1_prices.min(),Symbol2_prices.max()))
 plt.legend(["Symbol1", "Buy Signal", "Sell Signal","Symbol2"]) plt.show()
```

The following chart shows the buy and sell orders for this strategy. We see that the orders will be placed only when zscore is higher or lower than +/-1:

![](_page_21_Figure_0.jpeg)

Following the analysis that provided us with an understanding of the pairs that are co-integrated, we observed that the following pairs demonstrated similar behavior:

- ADBE, MSFT
- JNPR, LUV
- JNPR, MSFT
- JNPR, QCOM
- JNPR, SKYW
- JNPR, SPY
- 14. We will use MSFT and JNPR to implement the strategy based on real symbols. We will replace the code to build Symbol 1 and Symbol 2 with the following code. The following code will get the real prices for MSFT and JNPR:

```
 Symbol1_prices = data['Adj Close']['MSFT']
 Symbol1_prices.plot(figsize=(15,7))
 plt.show()
 Symbol2_prices = data['Adj Close']['JNPR']
 Symbol2_prices.name = 'JNPR'
 plt.title("MSFT and JNPR prices")
 Symbol1_prices.plot()
 Symbol2_prices.plot()
 plt.legend()
 plt.show()
```

This code will return the following plots as output. Let's have a look at them:

![](_page_22_Figure_0.jpeg)

The following screenshot shows the MSFT and JNPR prices. We observe similarities of movement between the tw symbols:

![](_page_22_Figure_2.jpeg)

When running the code that we ran previously for Symbol 1 and Symbol 2 by getting the actual prices from JNPR and MSFT, we will obtain the following curves:

![](_page_23_Figure_0.jpeg)

This chart reveals a large quantity of orders. The pair correlation strategy without limitation sends too many orders. We can limit the number of orders in the same way we did previously:

- Limiting positions
- Limiting the number of orders
- Setting a higher Z-score threshold

In this section, we focused on when to enter a position, but we have not addressed when to exit a position. While the Z-score value is above or below the threshold limits (in this example, -1 or +1), a Z-score value within the range between the threshold limits denotes an improbable change of spread between the two symbol prices. Therefore, when this value is within this limit, this can be regarded as an exit signal.

In the following diagram, we illustrate when we should exit a position:

![](_page_23_Figure_7.jpeg)

In this example, the following applies:

- When the Z-score is lower than -1, we short sell Symbol 1 for \$3 and we buy it for \$4, while, when the Zscore is in the range [-1,+1], we exit the position by buying Symbol 2 for \$1 and selling it for \$3.
- If we just get 1 share of the two symbols, the profit of this trade will be (\$3-\$4)+(\$3-\$1)=\$1.
- 15. We will create a data frame, pair\_correlation\_trading\_strategy, in the code. This contains information relating to orders and position and we will use this data frame to calculate the performance of this pair correlation trading strategy:

```
pair_correlation_trading_strategy = pd.DataFrame(index=Symbol1_prices.index)
 pair_correlation_trading_strategy['symbol1_price']=Symbol1_prices
 pair_correlation_trading_strategy['symbol1_buy']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol1_sell']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol2_buy']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol2_sell']=np.zeros(len(Symbol1_prices))
```

16. We will limit the number of orders by reducing the position to one share. This can be a long or short position. For a given symbol, when we have a long position, a sell order is the only one that is allowed. When we have a short position, a buy order is the only one that is allowed. When we have no position, we can either go long (by buying) or go short (by selling). We will store the price we use to send the orders. For the paired symbol, we will do the opposite. When we sell Symbol 1, we will buy Symbol 2, and vice versa:

```
 position=0
for i in range(len(Symbol1_prices)):
 s1price=Symbol1_prices[i]
 s2price=Symbol2_prices[i]
 if not position and symbol1_buy[i]!=0:
 pair_correlation_trading_strategy['symbol1_buy'][i]=s1price
 pair_correlation_trading_strategy['symbol2_sell'][i] = s2price
 position=1
 elif not position and symbol1_sell[i]!=0:
 pair_correlation_trading_strategy['symbol1_sell'][i] = s1price
 pair_correlation_trading_strategy['symbol2_buy'][i] = s2price
 position = -1
 elif position==-1 and (symbol1_sell[i]==0 or i==len(Symbol1_prices)-1):
 pair_correlation_trading_strategy['symbol1_buy'][i] = s1price
 pair_correlation_trading_strategy['symbol2_sell'][i] = s2price
 position = 0
 elif position==1 and (symbol1_buy[i] == 0 or i==len(Symbol1_prices)-1):
 pair_correlation_trading_strategy['symbol1_sell'][i] = s1price
 pair_correlation_trading_strategy['symbol2_buy'][i] = s2price
 position = 0
```

This code will return the following output. The plot shows the decrease in the number of orders. We will now calculate the profit and loss generated by this strategy:

![](_page_25_Figure_0.jpeg)

17. We will now write the code that calculates the profit and loss of the pair correlation strategy. We make a subtraction between the vectors containing the Symbol 1 and Symbol 2 prices. We will then add these positions to create a representation of the profit and loss:

```
pair_correlation_trading_strategy['symbol1_position']=\
 pair_correlation_trading_strategy['symbol1_buy']-pair_correlation_trading_strategy['symbol1_sell']
 pair_correlation_trading_strategy['symbol2_position']=\
 pair_correlation_trading_strategy['symbol2_buy']-pair_correlation_trading_strategy['symbol2_sell']
 pair_correlation_trading_strategy['symbol1_position'].cumsum().plot() # Calculate Symbol 1 P&L
 pair_correlation_trading_strategy['symbol2_position'].cumsum().plot() # Calculate Symbol 2 P&L
 pair_correlation_trading_strategy['total_position']=\
 pair_correlation_trading_strategy['symbol1_position']+pair_correlation_trading_strategy['symbol2_position'] # Calculat
 pair_correlation_trading_strategy['total_position'].cumsum().plot()
```

This code will return the following output. In the plot, the blue line represents the profit and loss for Symbol 1, and the orange line represents the profit and loss for Symbol 2. The green line represents the total profit and loss:

![](_page_26_Figure_0.jpeg)

Until this part, we traded only one share. In regular trading, we will trade hundreds/thousands of shares. Let's analyze what can happen when we use a pair-correlation trading strategy.

Suppose we have a pair of two symbols (Symbol 1 and Symbol 2). Let's assume that the Symbol 1 price is \$100 and the Symbol 2 price is \$10. If we trade a given fixed amount of shares of Symbol 1 and Symbol 2, we can use 100 shares. If we have a long signal for Symbol 1, we will buy Symbol 1 for \$100. The notional position will be 100 x \$100 = \$10,000. Since it is a long signal for Symbol 1, it is a short signal for Symbol 2. We will have a Symbol 2 notional position of 100 x \$10 = \$1,000. We will have a delta of \$9,000 between these two positions.

By having a large price differential, this places more emphasis on the symbol with the higher price. So it means when that symbol leads the return. Additionally, when we trade and invest money on the market, we should hedge positions against market moves. For example, if we invest in an overall long position by buying many symbols, we think that these symbols will outperform the market. Suppose the whole market is depreciating, but these symbols are indeed outperforming the other ones. If we want to sell them, we will certainly lose money since the market will collapse. For that, we usually hedge our positions by investing in something that will move on the opposite side of our positions. In the example of a pair trading correlation, we should aim to have a neutral position by investing the same notional in Symbol 1 and in Symbol 2. By taking the example of having a Symbol 1 price that is markedly different to the Symbol 2 price, we cannot use the hedge of Symbol 2 if we invest the same number of shares as we invest in Symbol 1.

Because we don't want to be in either of the two situations described earlier, we are going to invest the same notional in Symbol 1 and Symbol 2. Let's say we want to buy 100 shares of Symbol 1. The notional position we will have is 100 x \$100 = \$10,000. To get the same equivalent of notional position for Symbol 2, we will need to get \$10,000 / \$10 = 1,000 shares. If we get 100 shares of Symbol 1 and 1,000 shares of Symbol 2, we will have a neutral position for this investment, and we will not give more importance to Symbol 1 over Symbol 2.

Now, let's suppose the price of symbol 2 is \$3 instead of being \$10. When dividing \$10,000 / \$3 = 3,333 + 1/3. This means we will send an order for 3,333 shares, which means that we will have a Symbol 1 position

of \$10,000 and a Symbol 2 position of 3,333 x \$3 = \$9,999, resulting in a delta of \$1. Now suppose that the traded amount, instead of being \$10,000, was \$10,000,000. This will result in a delta of \$1,000. Because we need to remove the decimal part when buying stocks, this delta will appear for any symbols. If we trade around 200 pairs of symbols, we may have \$200,000 (200 x \$1,000) of position that is not hedged. We will be exposed to market moves. Therefore, if the market goes down, we may lose out on this \$200,000. That's why it will be important to hedge with a financial instrument going in the opposite direction from this \$200,000 position. If we have positions with many symbols, resulting in having a residual of \$200,000 of a long position that is not covered, we will get a short position of the ETF SPY behaving in the same way as the market moves.

18. We replace s1prices with s1positions from the earlier code by taking into account the number of shares we want to allocate for the trading of this pair:

```
pair_correlation_trading_strategy['symbol1_price']=Symbol1_prices
 pair_correlation_trading_strategy['symbol1_buy']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol1_sell']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol2_buy']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['symbol2_sell']=np.zeros(len(Symbol1_prices))
 pair_correlation_trading_strategy['delta']=np.zeros(len(Symbol1_prices)) 
 position=0
 s1_shares = 1000000
for i in range(len(Symbol1_prices)):
 s1positions= Symbol1_prices[i] * s1_shares
 s2positions= Symbol2_prices[i] * int(s1positions/Symbol2_prices[i])
 delta_position=s1positions-s2positions
 if not position and symbol1_buy[i]!=0:
 pair_correlation_trading_strategy['symbol1_buy'][i]=s1positions
 pair_correlation_trading_strategy['symbol2_sell'][i] = s2positions
 pair_correlation_trading_strategy['delta'][i]=delta_position
 position=1
 elif not position and symbol1_sell[i]!=0:
 pair_correlation_trading_strategy['symbol1_sell'][i] = s1positions
 pair_correlation_trading_strategy['symbol2_buy'][i] = s2positions
 pair_correlation_trading_strategy['delta'][i] = delta_position
 position = -1
 elif position==-1 and (symbol1_sell[i]==0 or i==len(Symbol1_prices)-1):
 pair_correlation_trading_strategy['symbol1_buy'][i] = s1positions
 pair_correlation_trading_strategy['symbol2_sell'][i] = s2positions
 position = 0
 elif position==1 and (symbol1_buy[i] == 0 or i==len(Symbol1_prices)-1):
 pair_correlation_trading_strategy['symbol1_sell'][i] = s1positions
 pair_correlation_trading_strategy['symbol2_buy'][i] = s2positions
 position = 0
```

This code will return the following output. This graph represent the positions of Symbol 1 and Symbol 2 and the total profit and loss of this pair correlation trading strategy:

![](_page_28_Figure_0.jpeg)

The code displays the delta position. The maximum amount is \$25. Because this amount is too low, we don't need to hedge this delta position:

```
pair_correlation_trading_strategy['delta'].plot()
 plt.title("Delta Position")
 plt.show()
```

This section concludes the implementation of a trading strategy that is based on the correlation/cointegration with another financial product.

### **Summary**

In this chapter, we were introduced to two intuitive trading strategies – the momentum strategy and the mean-reversion strategy. We learned how to create a trading strategy based on momentum and trend following. We also learned to create a trading strategy that works for markets with reversion behavior. These two strategies are very popular in the trading industry and are heavily used. We explained how to implement them. We got to learned how they work, along with their advantages and disadvantages

In the next chapter, we will build on top of the basic algorithmic strategies and learn about more advanced approaches (statistical arbitrage, pair correlation), along with their advantages and disadvantages.

# **Sophisticated Algorithmic Strategies**

In this chapter, we will explore more sophisticated trading strategies employed by leading market participants in the algorithmic trading business. We will build on top of the basic algorithmic strategies and learn about more advanced approaches (such as statistical arbitrage and pair correlation) and their advantages and disadvantages. We will learn how to create a trading strategy that adjusts for trading instrument volatility. We will also learn how to create a trading strategy for economic events and understand and implement the basics of statistical arbitrage trading strategies.

This chapter will cover the following topics:

- Creating a trading strategy that adjusts for trading instrument volatility
- Creating a trading strategy for economic events
- Understanding and implementing basic statistical arbitrage trading strategies

### **Creating a trading strategy that adjusts for trading instrument volatility**

An intuitive way to think about price volatility is investor confidence in the specific instrument, that is, how willing the investors are to invest money into the specific instrument and how long they are willing to hold on to a position in that instrument. As price volatility goes up, because prices make bigger swings at faster paces, investor confidence drops. Conversely, as price volatility goes down, investors are more willing to have bigger positions and hold those positions for longer periods of time. Volatility in a few asset classes often spills over into other asset classes, thus slowly spreading volatility over to all economic fields, housing costs, consumer costs, and so on. Obviously, sophisticated strategies need to dynamically adjust to changing volatility in trading instruments by following a similar pattern of being more cautious with respect to the positions they take, how long positions are held, and what the profit/loss expectations are.

In Chapter 2, *Deciphering the Markets with Technical Analysis*, we saw a lot of trading signals; in Chapter 3, *Predicting the Markets with Basic Machine Learning*, we applied machine learning algorithms to those trading signals; and in Chapter 4, *Classical Trading Strategies Driven by Human Intuition*, we explored basic trading strategies. Most of those approaches did not directly consider volatility changes in the underlying trading instrument, or adjust or account for them. In this section, we will discuss the impact of volatility changes in trading instruments and how to deal with that to improve profitability and reduce risk exposure.

### **Adjusting for trading instrument volatility in technical indicators**

In Chapter 2, *Deciphering the Markets with Technical Analysis*, we looked at generating trading signals with predetermined parameters. What we mean by that is we decided beforehand to use, say, 20 days moving average, or the number of time periods to use, or the smoothing constants to use, and these remained constant throughout the entire period of our analysis. These signals have the benefit of being simple, but suffer from the disadvantage of performing differently as the volatility of the trading instrument changed over the course of time.

Then we also looked at signals such as Bollinger Bands and standard deviation, which adjusted for trading instrument volatility, that is, during non-volatile periods, the lower standard deviation in price movements would make the signals more aggressive to entering positions and less aggressive when closing positions. Conversely, during volatile periods, the higher standard deviation in price movements makes the signals less aggressive to entering positions. This is because the bands that depend on standard deviation widen out from the moving average, which in itself has become more volatile. Thus, these signals implicitly had some aspects of adjusting for trading instrument volatility baked right into them.

In general, it is possible to take any of the technical indicators we have seen so far and combine a standard deviation signal with it to have a more sophisticated form of the basic technical indicator that has dynamic values for number of days, or number of time periods or smoothing factors. The parameters become dynamic by depending on the standard deviation as a volatility measure. Thus, moving averages can have a smaller history or number of time periods when volatility is high to capture more observations, and a larger history or number of time periods when volatility is low to capture fewer observations. Similarly, smoothing factors can be made higher or lower in magnitude depending on volatility. In essence, that

controls how much weight is assigned to newer observations as compared to older ones. We won't go into any more detail here, but it is easy to apply these concepts to technical indicators once the basic idea of applying volatility measures to simple indicators to form complex indicators is clear.

### **Adjusting for trading instrument volatility in trading strategies**

We can apply the same concepts of adjusting for volatility measures to trading strategies. Momentum or trend-following strategies can use changing volatility to dynamically change the time period parameters used in the moving averages, or change the thresholds for how many up/down days to count as an entry signal. Another area of improvement would be using changing volatility to dynamically adjust thresholds on when to enter a position when a trend is detected, and dynamically adjust thresholds on when to exit a position when trend reversal is detected.

For mean reversion based strategies, applying volatility measures is pretty similar. In this case, we can use dynamically changing time periods for moving averages, and dynamically changing thresholds for entering positions when overbuying and overselling is detected, or dynamically changing thresholds for exiting positions when reversal to equilibrium prices are detected. Let's explore, in the rest of this chapter, different ideas of adjusting for volatility measures in trading strategies in greater detail and see the impact on the trading strategy behavior.

### **Volatility adjusted mean reversion trading strategies**

We explored mean reversion trading strategies in great detail in Chapter 4, *Classical Trading Strategies Driven by Human Intuition*. For the purposes of this chapter, we will first create a very simple variant of a mean reversion strategy and then show how one would apply volatility adjustment to the strategy to optimize and stabilize its risk-adjusted returns.

#### **Mean reversion strategy using the absolute price oscillator trading signal**

Let's explain and implement a mean reversion strategy that relies on the **Absolute Price Oscillator** (**APO**) trading signal indicator we explored in Chapter 2, *Deciphering the Markets with Technical Analysis*. It will use a static constant of 10 days for the Fast EMA and a static constant of 40 days for the Slow EMA. It will perform buy trades when the APO signal value drops below -10 and perform sell trades when the APO signal value goes above +10. In addition, it will check that new trades are made at prices that are different from the last trade price to prevent overtrading. Positions are closed when the APO signal value changes sign, that is, close short positions when APO goes negative and close long positions when APO goes positive.

In addition, positions are also closed if currently open positions are profitable above a certain amount, regardless of APO values. This is used to algorithmically lock profits and initiate more positions instead of relying only on the trading signal value. Now, let's look at the implementation in the next few sections:

1. We will fetch data the same way we have done in the past. Let's fetch 4 years of GOOG data. This code will use the DataReader function from the pandas\_datareader package. This function will fetch the GOOG prices from Yahoo Finance between 2014-01-2014 and 2018-01-01. If the .pkl file used to store the data on the disk is not present, the GOOG\_data.pkl file will be created. By doing that, we ensure that we will use the file to fetch the GOOG data for future use:

```
import pandas as pd
from pandas_datareader import data
# Fetch daily data for 4 years
SYMBOL='GOOG'
start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME=SYMBOL + '_data.pkl'
try:
 data = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
 data = data.DataReader(SYMBOL, 'yahoo', start_date, end_date)
 data.to_pickle(SRC_DATA_FILENAME)
```

2. Now we will define some constants and variables we will need to perform Fast and Slow EMA calculations and APO trading signal:

```
# Variables/constants for EMA Calculation:
NUM_PERIODS_FAST = 10 # Static time period parameter for the fast EMA
K_FAST = 2 / (NUM_PERIODS_FAST + 1) # Static smoothing factor parameter for fast EMA
ema_fast = 0
ema_fast_values = [] # we will hold fast EMA values for visualization purposes
NUM_PERIODS_SLOW = 40 # Static time period parameter for slow EMA
K_SLOW = 2 / (NUM_PERIODS_SLOW + 1) # Static smoothing factor parameter for slow EMA
ema_slow = 0
ema_slow_values = [] # we will hold slow EMA values for visualization purposes
apo_values = [] # track computed absolute price oscillator value signals
```

3. We will also need variables that define/control strategy trading behavior and position and PnL management:

```
# Variables for Trading Strategy trade, position & pnl management:
orders = [] # Container for tracking buy/sell order, +1 for buy order, -1 for sell order, 0 for no-action
positions = [] # Container for tracking positions, positive for long positions, negative for short positions, 0 for fla
pnls = [] # Container for tracking total_pnls, this is the sum of closed_pnl i.e. pnls already locked in and open_pnl i
last_buy_price = 0 # Price at which last buy trade was made, used to prevent over-trading at/around the same price
last_sell_price = 0 # Price at which last sell trade was made, used to prevent over-trading at/around the same price
position = 0 # Current position of the trading strategy
buy_sum_price_qty = 0 # Summation of products of buy_trade_price and buy_trade_qty for every buy Trade made since last 
buy_sum_qty = 0 # Summation of buy_trade_qty for every buy Trade made since last time being flat
sell_sum_price_qty = 0 # Summation of products of sell_trade_price and sell_trade_qty for every sell Trade made since l
sell_sum_qty = 0 # Summation of sell_trade_qty for every sell Trade made since last time being flat
open_pnl = 0 # Open/Unrealized PnL marked to market
closed_pnl = 0 # Closed/Realized PnL so far
```

4. Finally, we clearly define the entry thresholds, the minimum price change since last trade, the minimum profit to expect per trade, and the number of shares to trade per trade:

```
# Constants that define strategy behavior/thresholds
APO_VALUE_FOR_BUY_ENTRY = -10 # APO trading signal value below which to enter buy-orders/long-position
APO_VALUE_FOR_SELL_ENTRY = 10 # APO trading signal value above which to enter sell-orders/short-position
MIN_PRICE_MOVE_FROM_LAST_TRADE = 10 # Minimum price change since last trade before considering trading again, this is t
MIN_PROFIT_TO_CLOSE = 10 # Minimum Open/Unrealized profit at which to close positions and lock profits
NUM_SHARES_PER_TRADE = 10 # Number of shares to buy/sell on every trade
```

5. Now, let's look at the main section of the trading strategy, which has logic for the following:

- Computation/updates to Fast and Slow EMA and the APO trading signal
- Reacting to trading signals to enter long or short positions
- Reacting to trading signals, open positions, open PnLs, and market prices to close long or short positions:

```
close=data['Close']
for close_price in close:
 # This section updates fast and slow EMA and computes APO trading signal
 if (ema_fast == 0): # first observation
 ema_fast = close_price
 ema_slow = close_price
 else:
 ema_fast = (close_price - ema_fast) * K_FAST + ema_fast
 ema_slow = (close_price - ema_slow) * K_SLOW + ema_slow
 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 apo = ema_fast - ema_slow
 apo_values.append(apo)
```

- 6. The code will check for trading signals against trading parameters/thresholds and positions, to trade. We will perform a sell trade at close\_price if the following conditions are met:
- The APO trading signal value is above the Sell-Entry threshold and the difference between the last trade price and current price is different enough.
- We are long (positive position) and either the APO trading signal value is at or above 0 or current position is profitable enough to lock profit:

```
 if ((apo > APO_VALUE_FOR_SELL_ENTRY and abs(close_price - last_sell_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE) # APO ab
 or
 (position > 0 and (apo >= 0 or open_pnl > MIN_PROFIT_TO_CLOSE))): # long from negative APO and APO has gone positiv
 orders.append(-1) # mark the sell trade
 last_sell_price = close_price
 position -= NUM_SHARES_PER_TRADE # reduce position by the size of this trade
 sell_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update vwap sell-price
 sell_sum_qty += NUM_SHARES_PER_TRADE
 print( "Sell ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
```

7. We will perform a buy trade at close\_price if the following conditions are met: the APO trading signal value is below the Buy-Entry threshold and the difference between the last trade price and current price is different enough. We are short (negative position) and either the APO trading signal value is at or below 0 or current position is profitable enough to lock profit:

```
 elif ((apo < APO_VALUE_FOR_BUY_ENTRY and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE) # APO be
 or
 (position < 0 and (apo <= 0 or open_pnl > MIN_PROFIT_TO_CLOSE))): # short from positive APO and APO has gone negati
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 position += NUM_SHARES_PER_TRADE # increase position by the size of this trade
 buy_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update the vwap buy-price
 buy_sum_qty += NUM_SHARES_PER_TRADE
 print( "Buy ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
 positions.append(position)
```

8. The code of the trading strategy contains logic for position/PnL management. It needs to update positions and compute open and closed PnLs when market prices change and/or trades are made causing a change in positions:

```
# This section updates Open/Unrealized & Closed/Realized positions
 open_pnl = 0
```

```
 if position > 0:
 if sell_sum_qty > 0: # long position and some sell trades have been made against it, close that amount based on how
 open_pnl = abs(sell_sum_qty) * (sell_sum_price_qty/sell_sum_qty - buy_sum_price_qty/buy_sum_qty)
 # mark the remaining position to market i.e. pnl would be what it would be if we closed at current price
 open_pnl += abs(sell_sum_qty - position) * (close_price - buy_sum_price_qty / buy_sum_qty)
 elif position < 0:
 if buy_sum_qty > 0: # short position and some buy trades have been made against it, close that amount based on how 
 open_pnl = abs(buy_sum_qty) * (sell_sum_price_qty/sell_sum_qty - buy_sum_price_qty/buy_sum_qty)
 # mark the remaining position to market i.e. pnl would be what it would be if we closed at current price
 open_pnl += abs(buy_sum_qty - position) * (sell_sum_price_qty/sell_sum_qty - close_price)
 else:
 # flat, so update closed_pnl and reset tracking variables for positions & pnls
 closed_pnl += (sell_sum_price_qty - buy_sum_price_qty)
 buy_sum_price_qty = 0
 buy_sum_qty = 0
 sell_sum_price_qty = 0
 sell_sum_qty = 0
 last_buy_price = 0
 last_sell_price = 0
 print( "OpenPnL: ", open_pnl, " ClosedPnL: ", closed_pnl )
 pnls.append(closed_pnl + open_pnl)
```

9. Now we look at some Python/Matplotlib code to see how to gather the relevant results of the trading strategy such as market prices, Fast and Slow EMA values, APO values, Buy and Sell trades, Positions and PnLs achieved by the strategy over its lifetime and then plot them in a manner that gives us insight into the strategy's behavior:

```
# This section prepares the dataframe from the trading strategy results and visualizes the results
data = data.assign(ClosePrice=pd.Series(close, index=data.index))
data = data.assign(Fast10DayEMA=pd.Series(ema_fast_values, index=data.index))
data = data.assign(Slow40DayEMA=pd.Series(ema_slow_values, index=data.index))
data = data.assign(APO=pd.Series(apo_values, index=data.index))
data = data.assign(Trades=pd.Series(orders, index=data.index))
data = data.assign(Position=pd.Series(positions, index=data.index))
data = data.assign(Pnl=pd.Series(pnls, index=data.index))
```

10. Now we will add columns to the data frame with different series that we computed in the previous sections, first the Market Price and then the fast and slow EMA values. We will also have another plot for the APO trading signal value. In both plots, we will overlay buy and sell trades so we can understand when the strategy enters and exits positions:

```
import matplotlib.pyplot as plt
data['ClosePrice'].plot(color='blue', lw=3., legend=True)
data['Fast10DayEMA'].plot(color='y', lw=1., legend=True)
data['Slow40DayEMA'].plot(color='m', lw=1., legend=True)
plt.plot(data.loc[ data.Trades == 1 ].index, data.ClosePrice[data.Trades == 1 ], color='r', lw=0, marker='^', markersiz
plt.plot(data.loc[ data.Trades == -1 ].index, data.ClosePrice[data.Trades == -1 ], color='g', lw=0, marker='v', markers
plt.legend()
plt.show()
data['APO'].plot(color='k', lw=3., legend=True)
plt.plot(data.loc[ data.Trades == 1 ].index, data.APO[data.Trades == 1 ], color='r', lw=0, marker='^', markersize=7, la
plt.plot(data.loc[ data.Trades == -1 ].index, data.APO[data.Trades == -1 ], color='g', lw=0, marker='v', markersize=7, 
plt.axhline(y=0, lw=0.5, color='k')
for i in range( APO_VALUE_FOR_BUY_ENTRY, APO_VALUE_FOR_BUY_ENTRY*5, APO_VALUE_FOR_BUY_ENTRY ):
 plt.axhline(y=i, lw=0.5, color='r')
for i in range( APO_VALUE_FOR_SELL_ENTRY, APO_VALUE_FOR_SELL_ENTRY*5, APO_VALUE_FOR_SELL_ENTRY ):
 plt.axhline(y=i, lw=0.5, color='g')
plt.legend()
plt.show()
```

Let's take a look at what our trading behavior looks like, paying attention to the EMA and APO values when the trades are made. When we look at the positions and PnL plots, this will become completely clear:

![](_page_39_Figure_0.jpeg)

In the plot, we can see where the buy and sell trades were made as the price of the Google stock change over the last 4 years, but now, let's look at what the APO trading signal values where the buy trades were made and sell trades were made. According to the design of these trading strategies, we expect sell trades when APO values are positive and expect buy trades when APO values are negative:

![](_page_39_Figure_2.jpeg)

In the plot, we can see that a lot of sell trades are executed when APO trading signal values are positive and a lot of buy trades are executed when APO trading signal values are negative. We also observe that some buy trades are executed when APO trading signal values are positive and some sell trades are executed when APO trading signal values are negative. How do we explain that?

11. As we will see in the following code, those trades are the ones executed to close profits. Let's observe the position and PnL evolution over the lifetime of this strategy:

```
data['Position'].plot(color='k', lw=1., legend=True)
plt.plot(data.loc[ data.Position == 0 ].index, data.Position[ data.Position == 0 ], color='k', lw=0, marker='.', label=
plt.plot(data.loc[ data.Position > 0 ].index, data.Position[ data.Position > 0 ], color='r', lw=0, marker='+', label='l
plt.plot(data.loc[ data.Position < 0 ].index, data.Position[ data.Position < 0 ], color='g', lw=0, marker='_', label='s
plt.axhline(y=0, lw=0.5, color='k')
for i in range( NUM_SHARES_PER_TRADE, NUM_SHARES_PER_TRADE*25, NUM_SHARES_PER_TRADE*5 ):
 plt.axhline(y=i, lw=0.5, color='r')
for i in range( -NUM_SHARES_PER_TRADE, -NUM_SHARES_PER_TRADE*25, -NUM_SHARES_PER_TRADE*5 ):
 plt.axhline(y=i, lw=0.5, color='g')
plt.legend()
plt.show()
data['Pnl'].plot(color='k', lw=1., legend=True)
plt.plot(data.loc[ data.Pnl > 0 ].index, data.Pnl[ data.Pnl > 0 ], color='g', lw=0, marker='.')
plt.plot(data.loc[ data.Pnl < 0 ].index, data.Pnl[ data.Pnl < 0 ], color='r', lw=0, marker='.')
plt.legend()
plt.show()
```

The code will return the following output. Let's have a look at the two charts:

![](_page_40_Figure_0.jpeg)

From the position plot, we can see some large short positions around 2016-01, then again in 2017-07, and finally again in 2018-01. If we go back to the APO trading signal values, that is when APO values went through large patches of positive values. Finally, let's look at how the PnL evolves for this trading strategy over the course of the stock's life cycle:

![](_page_40_Figure_2.jpeg)

The basic mean reversion strategy makes money pretty consistently over the course of time, with some volatility in returns during 2016-01 and 2017-07, where the strategy has large positions, but finally ending around \$15K, which is close to its maximum achieved PnL.

### **Mean reversion strategy that dynamically adjusts for changing volatility**

Now, let's apply the previously introduced concepts of using a volatility measure to adjust the number of days used in Fast and Slow EMA and using a volatility-adjusted APO entry signal. We will use the **standard deviation** (**STDEV**) indicator we explored in Chapter 2, *Deciphering the Markets with Technical Analysis*, as a measure of volatility. Let's observe the output of that indicator quickly to recap the Google dataset:

![](_page_41_Figure_2.jpeg)

From the output, it seems like volatility measure ranges from somewhere between \$8 over 20 days to \$40 over 20 days, with \$15 over 20 days being the average. So we will use a volatility factor that ranges from 0 to 1, by designing it to be , where values closer to 0 indicate very low volatility, values around 1 indicate normal volatility, and values above 1 indicate above-normal volatility. The way in which we incorporate STDEV into our strategy is through the following changes:

- Instead of having static K\_FAST and K\_SLOW smoothing factors for the fast and slow EMA, we will instead make them additionally a function of volatility and use K\_FAST \* stdev\_factor and K\_SLOW \* stdev\_factor, to make them more reactive to newest observations during periods of higher than normal volatility, which makes intuitive sense.
- Instead of using static APO\_VALUE\_FOR\_BUY\_ENTRY and APO\_VALUE\_FOR\_SELL\_ENTRY thresholds for entering positions based on the primary trading signal APO, we will also incorporate volatility to have dynamic thresholds APO\_VALUE\_FOR\_BUY\_ENTRY \* stdev\_factor and APO\_VALUE\_FOR\_SELL\_ENTRY \* stdev\_factor. This makes us less aggressive in entering positions during periods of higher volatility, by increasing the threshold for entry by a factor of volatility, which also makes intuitive sense based on what we discussed in the previous section.
- Finally, we will incorporate volatility in one last threshold and that is by having a dynamic expected profit threshold to lock in profit in a position. In this case, instead of using the static MIN\_PROFIT\_TO\_CLOSE threshold, we will use a dynamic MIN\_PROFIT\_TO\_CLOSE / stdev\_factor. Here, the idea is to be more aggressive in exciting positions during periods of increased volatility, because as we discussed before, during periods of higher than normal volatility, it is riskier to hold on to positions for longer periods of time.

Let's look at the modifications needed to the basic mean reversion strategy to achieve this. First, we need some code to track and update the volatility measure (STDEV):

```
import statistics as stats
import math as math
# Constants/variables that are used to compute standard deviation as a volatility measure
SMA_NUM_PERIODS = 20 # look back period
price_history = [] # history of prices
```

Then the main strategy loop simply becomes this, while the position and PnL management section of the strategy remains the same:

```
close=data['Close']
for close_price in close:
 price_history.append(close_price)
 if len(price_history) > SMA_NUM_PERIODS: # we track at most 'time_period' number of prices
 del (price_history[0])
 sma = stats.mean(price_history)
 variance = 0 # variance is square of standard deviation
 for hist_price in price_history:
 variance = variance + ((hist_price - sma) ** 2)
 stdev = math.sqrt(variance / len(price_history))
 stdev_factor = stdev/15
 if stdev_factor == 0:
 stdev_factor = 1
 # This section updates fast and slow EMA and computes APO trading signal
 if (ema_fast == 0): # first observation
 ema_fast = close_price
 ema_slow = close_price
 else:
 ema_fast = (close_price - ema_fast) * K_FAST*stdev_factor + ema_fast
 ema_slow = (close_price - ema_slow) * K_SLOW*stdev_factor + ema_slow
 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 apo = ema_fast - ema_slow
 apo_values.append(apo)
```

And as we said, the use of the trading signal to manage positions has the same trading logic as before. First, let's look at the sell trade logic:

```
 # We will perform a sell trade at close_price if the following conditions are met:
 # 1. The APO trading signal value is above Sell-Entry threshold and the difference between last trade-price and current-price
# 2. We are long( positive position ) and either APO trading signal value is at or above 0 or current position is profitable en
 if ((apo > APO_VALUE_FOR_SELL_ENTRY*stdev_factor and abs(close_price - last_sell_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE*stde
 or
 (position > 0 and (apo >= 0 or open_pnl > MIN_PROFIT_TO_CLOSE/stdev_factor))): # long from negative APO and APO has gone po
 orders.append(-1) # mark the sell trade
 last_sell_price = close_price
 position -= NUM_SHARES_PER_TRADE # reduce position by the size of this trade
 sell_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update vwap sell-price
 sell_sum_qty += NUM_SHARES_PER_TRADE
 print( "Sell ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
```

Now, let's look at similar logic for buy trades:

```
 # We will perform a buy trade at close_price if the following conditions are met:
 # 1. The APO trading signal value is below Buy-Entry threshold and the difference between last trade-price and current-price 
 # 2. We are short( negative position ) and either APO trading signal value is at or below 0 or current position is profitable
 elif ((apo < APO_VALUE_FOR_BUY_ENTRY*stdev_factor and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE*stde
 or
 (position < 0 and (apo <= 0 or open_pnl > MIN_PROFIT_TO_CLOSE/stdev_factor))): # short from positive APO and APO has gone n
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 position += NUM_SHARES_PER_TRADE # increase position by the size of this trade
 buy_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update the vwap buy-price
 buy_sum_qty += NUM_SHARES_PER_TRADE
 print( "Buy ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
```

Let's compare PnLs from a static constant thresholds mean reversion strategy and a volatility-adjusted mean reversion strategy to see whether we improved performance or not:

![](_page_43_Figure_0.jpeg)

In this case, adjusting the trading strategy for volatility increases the strategy performance by 200%!

### **Trend-following strategy using absolute price oscillator trading signal**

Similar to the mean reversion strategy we explored, we can build a trend-following strategy that uses the APO trading signal. The only difference here is that we enter long positions when the APO is above a certain value, expecting price moves to continue in that direction, and we enter short positions when the APO is below a certain value, expecting price moves to continue going down.

In effect, this is the exact opposite trading strategy with some differences in position management. One might expect this trading strategy to be exactly opposite in performance but, as we will see, that is not the case, that is, both trend-following and mean reversion strategies can be profitable in the same market conditions:

1. First, we define the APO values we will use to enter long/short positions. In this case, the buy entry APO threshold is positive and the sell entry APO threshold is negative:

# Constants that define strategy behavior/thresholds APO\_VALUE\_FOR\_BUY\_ENTRY = 10 # APO trading signal value above which to enter buy-orders/long-position APO\_VALUE\_FOR\_SELL\_ENTRY = -10 # APO trading signal value below which to enter sell-orders/short-position

2. Next, let's look at the core trading logic that enters and exits positions.

First, look at the signal and position management code that leads to sell trades:

```
 # This section checks trading signal against trading parameters/thresholds and positions, to trade.
# We will perform a sell trade at close_price if the following conditions are met:
 # 1. The APO trading signal value is below Sell-Entry threshold and the difference between last trade-price and curre
 # 2. We are long( positive position ) and either APO trading signal value is at or below 0 or current position is pro
 if ((apo < APO_VALUE_FOR_SELL_ENTRY and abs(close_price - last_sell_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE) # APO ab
 or
 (position > 0 and (apo <= 0 or open_pnl > MIN_PROFIT_TO_CLOSE))): # long from positive APO and APO has gone negativ
 orders.append(-1) # mark the sell trade
 last_sell_price = close_price
 position -= NUM_SHARES_PER_TRADE # reduce position by the size of this trade
 sell_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update vwap sell-price
 sell_sum_qty += NUM_SHARES_PER_TRADE
 print( "Sell ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
```

Now, let's look at the signal and position management code that leads to buy trades:

```
 # We will perform a buy trade at close_price if the following conditions are met:
 # 1. The APO trading signal value is above Buy-Entry threshold and the difference between last trade-price and current-price 
 # 2. We are short( negative position ) and either APO trading signal value is at or above 0 or current position is profitable
 elif ((apo > APO_VALUE_FOR_BUY_ENTRY and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FROM_LAST_TRADE) # APO above buy 
 or
 (position < 0 and (apo >= 0 or open_pnl > MIN_PROFIT_TO_CLOSE))): # short from negative APO and APO has gone positive or po
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 position += NUM_SHARES_PER_TRADE # increase position by the size of this trade
 buy_sum_price_qty += (close_price*NUM_SHARES_PER_TRADE) # update the vwap buy-price
 buy_sum_qty += NUM_SHARES_PER_TRADE
 print( "Buy ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position )
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
```

The code to generate the visualization plots remains the same, so we've skipped it here. Let's look at trendfollowing trading strategy performance:

![](_page_45_Figure_0.jpeg)

The plot shows at what prices the buy and sell trades are made throughout the lifetime of the trading strategy applied to Google stock data. The trading strategy behavior will make more sense when we inspect the APO signal values to go along with the actual trade prices. Let's look at that in the next plot:

![](_page_45_Figure_2.jpeg)

By the definition of a trend-following strategy using the APO trading signal values, intuitively we expect buy trades when APO signal values are positive and sell trades when APO signal values are negative. There are also some buy trades when APO signal values are negative and some sell trades when APO signal values are positive, which might seem counterintuitive, but these are trades made to close out profitable positions, similar to the mean reversion strategy. Now, let's look at the evolution of positions through the course of this trading strategy:

![](_page_45_Figure_4.jpeg)

Here, compared to the mean reversion trading strategy, there are more long positions than short positions, and the positions are usually small and closed quickly and a new position (likely long) is initiated shortly after. This

observation is consistent with the fact that this is a trend-following strategy applied to a strongly upward-trending trading instrument such as the Google stock. Since Google stocks have been steadily trending upward over the course of this trading strategy, it makes sense that most of the positions are long and also makes sense that most of the long positions end up being profitable and are flattened shortly after being initiated. Finally, let's observe the evolution of PnL for this trading strategy:

![](_page_46_Figure_1.jpeg)

So, for this case, the trend-following strategy makes a third of the money that the mean reversion strategy makes; however, the trend-following strategy also makes money for the same market conditions by entering and exiting positions at different price points.

### **Trend-following strategy that dynamically adjusts for changing volatility**

Let's use STDEV as a measure of volatility and adjust the trend-following strategy to adapt to changing market volatility. We will use an identical approach to the one we used when adjusting the mean reversion trading strategy for market volatility.

The main trading logic for the trend-following strategy adjusted for market volatility looks like the following. Let's start with the trading logic that controls sell trades first:

 # This section checks trading signal against trading parameters/thresholds and positions, to trade. # We will perform a sell trade at close\_price if the following conditions are met: # 1. The APO trading signal value is below Sell-Entry threshold and the difference between last trade-price and current-price # 2. We are long( positive position ) and either APO trading signal value is at or below 0 or current position is profitable if ((apo < APO\_VALUE\_FOR\_SELL\_ENTRY/stdev\_factor and abs(close\_price - last\_sell\_price) > MIN\_PRICE\_MOVE\_FROM\_LAST\_TRADE\*stde or (position > 0 and (apo <= 0 or open\_pnl > MIN\_PROFIT\_TO\_CLOSE/stdev\_factor))): # long from positive APO and APO has gone ne orders.append(-1) # mark the sell trade last\_sell\_price = close\_price position -= NUM\_SHARES\_PER\_TRADE # reduce position by the size of this trade sell\_sum\_price\_qty += (close\_price\*NUM\_SHARES\_PER\_TRADE) # update vwap sell-price sell\_sum\_qty += NUM\_SHARES\_PER\_TRADE print( "Sell ", NUM\_SHARES\_PER\_TRADE, " @ ", close\_price, "Position: ", position )

#### Now, let's look at the trading logic code that handles buy trades:

# We will perform a buy trade at close\_price if the following conditions are met:

 # 1. The APO trading signal value is above Buy-Entry threshold and the difference between last trade-price and current-price # 2. We are short( negative position ) and either APO trading signal value is at or above 0 or current position is profitable elif ((apo > APO\_VALUE\_FOR\_BUY\_ENTRY/stdev\_factor and abs(close\_price - last\_buy\_price) > MIN\_PRICE\_MOVE\_FROM\_LAST\_TRADE\*stde or (position < 0 and (apo >= 0 or open\_pnl > MIN\_PROFIT\_TO\_CLOSE/stdev\_factor))): # short from negative APO and APO has gone p

 orders.append(+1) # mark the buy trade last\_buy\_price = close\_price position += NUM\_SHARES\_PER\_TRADE # increase position by the size of this trade buy\_sum\_price\_qty += (close\_price\*NUM\_SHARES\_PER\_TRADE) # update the vwap buy-price buy\_sum\_qty += NUM\_SHARES\_PER\_TRADE print( "Buy ", NUM\_SHARES\_PER\_TRADE, " @ ", close\_price, "Position: ", position ) else: # No trade since none of the conditions were met to buy or sell orders.append(0)

Finally, let's compare trend-following strategy performance with and without accounting for volatility changes:

![](_page_47_Figure_9.jpeg)

So, for trend-following strategies, having dynamic trading thresholds degrades strategy performance. We can explore tweaking the application of the volatility measure to see whether there are variants that actually improve performance compared to static trend-following.

### **Creating a trading strategy for economic events**

In this section, we will explore a new class of trading strategies that is different from what we've seen before. Instead of using technical indicators, we can research economic releases and use various economic releases to estimate/predict the impact on the trading instruments and trade them accordingly. Let's first take a look at what economic releases are and how instrument pricing is influenced by releases.

### **Economic releases**

Economic indicators are a measure of economic activity for a certain country or region or asset classes. These indicators are measured, researched, and released by different entities. Some of these entities are government agencies and some are private research firms. Most of these are released on a schedule, known as an economic calendar. In addition, there is plenty of data available for past releases, expected releases, and actual releases. Each economic indicator captures different economic activity measures: some might affect housing prices, some show employment information, some affect grain, corn, and wheat instruments, others affect precious metals and energy commodities. For example, possibly the most well-known economic indicator, Nonfarm Payrolls in America, is a monthly indicator released by the US Department of Labor (<https://www.bls.gov/ces/>) that represents the number of new jobs created in all non-agricultural industries. This economic release has a huge impact on almost all asset classes. Another example is the EIA Crude Oil Stockpiles report, which is a weekly indicator released by the Energy Information Administration that measures change in the number of barrels of crude oil available. This is a high-impact release for energy products, oil, gas, and so on, but does not usually directly affect things such as stocks, and interest rates.

Now that we have an intuitive idea of what economic indicators are and what economic releases capture and signify, let's look at a short list of important US economic releases. We will not be covering the details of these releases here, but we encourage the reader to explore the economic indicators mentioned here as well as others in greater detail:

ADP Employment, API Crude, Balance of Trade, Baker Hughes Oil Rig Count, Business Optimism, Business Inventories, Case-Shiller, CB Consumer Confidence, CB Leading Index, Challenger Job Cuts, Chicago PMI, Construction Spending, Consumer Credit, Consumer Inflation Expectations, Durable Goods, EIA Crude, EIA Natural Gas, Empire State Manufacturing Index, Employment Cost Index, Factory Orders, Fed Beige Book, Fed Interest Rate Decision, Fed Press Conference, Fed Manufacturing Index, Fed National Activity, FOMC Economic Projections, FOMC Minutes, GDP, Home Sales, Housing Starts, House Price Index, Import Prices, Industrial Production, Inflation Rate, ISM Manufacturing, ISM Non-Manufacturing, ISM New York Index, Jobless Claims, JOLTs, Markit Composite PMI, Markit Manufacturing PMI, Michigan Consumer Sentiment, Mortgage Applications, NAHB Housing Market Index, Nonfarm Payrolls, Nonfarm Productivity, PCE, PPI, Personal Spending, Redbook, Retail Sales, Total Vehicle Sales, WASDE & Wholesale Inventories

[More information about these releases is available at](https://tradingeconomics.com/) https://tradingeconomics. com[/.](https://tradingeconomics.com/)

### **Economic release format**

There are plenty of free and paid economic release calendars available, which can be scraped for historical release data or accessed through a proprietary API. Since the focus of this section is utilizing economic release data in trading, we will skip the details of accessing historical data, but it is quite straightforward. Most common economic release calendars look like this:

| Calendar       | CST         | Economic<br>indicator          | Actual | Previous | Consensus | Forecast |
|----------------|-------------|--------------------------------|--------|----------|-----------|----------|
| 2019-<br>05-03 | 07:30<br>AM | Non<br>Farm<br>Payrolls<br>Apr | 263K   | 189K     | 185K      | 178K     |
| 2019-<br>06-07 | 07:30<br>AM | Non<br>Farm<br>Payrolls<br>May | 75K    | 224K     | 185K      | 190K     |
| 2019-<br>07-05 | 07:30<br>AM | Non<br>Farm<br>Payrolls<br>Jun | 224K   | 72K      | 160K      | 171K     |
| 2019-<br>08-02 | 07:30<br>AM | Non<br>Farm<br>Payrolls<br>Jul | 164K   | 193K     | 164K      | 160K     |

As we discussed earlier, the date and time of releases are set well in advance. Most calendars also provide the previous year's release, or sometimes the previous month's release. The Consensus estimate is what multiple economists or firms expect the release to be; this is generally treated as the expected value of the release, and any large misses from this expectation will cause large price volatility. A lot of calendars, in addition, provide a Forecast field, which is the

calendar provider's expected value for that economic release. At the time of writing, <https://tradingeconomics.com/>, <https://www.forexfactory.com/>, and https://www.fxst reet.com/ [are some of the many free and paid economic calendar providers.](https://www.fxstreet.com/)

### **Electronic economic release services**

One last concept we need to understand before we can look into the analysis of economic releases and price movement is how to deliver these economic releases electronic to trading strategies right to the trading servers. There are a lot of service providers that provide economic releases directly to trading servers electronically via low-latency direct lines. Most providers cover most of the major economic indicators and usually deliver releases to the trading strategies in machine-parsable feeds. These releases can reach the trading servers anywhere from a few microseconds up to a few milliseconds after the official release. Nowadays, it's quite common for a lot of algorithmic trading market participants to make use of such electronic economic release providers as alternative data providers to improve trading performance.

### **Economic releases in trading**

Now that we have a good grasp of what economic indicators are, how the economic releases are scheduled, and how they can be delivered electronically directly to trading servers, let's dive in and look at some possible edge trading strategies gain from economic indicator releases. There are a couple of different ways to use economic indicator releases in algorithmic trading, but we will explore the most common and most intuitive approach. Given the history of expected economic indicator values and actual releases similar to the format we saw before, it is possible to correlate the difference between expected and actual values with price movement that follows. Generally, there are two approaches. One capitalizes on price moves that are less than expected for a big miss in expected and actual economic indicator release, that is, the price should have moved a certain amount based on historical research, but moved much less. This strategy takes a position with the view that prices will move further and tries to capture a profit if it does, similar to trend-following trading strategies in some sense.

The other approach is the opposite one, which tries to detect overreactions in price movements and make the opposite bet, that is, prices will go back to previous price levels, similar to a mean reversion strategy in some sense. In practice, this approach is often improved by using classification methods we explored in Chapter 3, *Predicting the Markets with Basic Machine Learning*. Classification methods allow us to improve the process of combining multiple economic releases that occur at the same time in addition to having multiple possible value-boundaries for each release, to provide greater granularity and thresholds. For the purposes of this example, we will not dive into the complexity of applying classification methods to this economic release trading strategy.

Let's look at a couple of Non Farm Payroll releases and observe the impact on the S&P futures. Because this requires tick data, which is not freely available, we will skip the actual analysis code, but it should be easy to

|    | Α          | B               | С     | D              | F              | F     | G                                 |
|----|------------|-----------------|-------|----------------|----------------|-------|-----------------------------------|
|    | date       | time CST actual |       | consensus miss |                |       | bid price change ask price change |
| 2  | 2019-03-08 | 7:30:00         | 25000 |                | 170000 -145000 | $-17$ | -16                               |
| 3  | 2019-06-07 | 7:30:00         | 90000 | 175000         | -85000         | -11   | -11                               |
| 4  | 2018-10-05 | 7:30:00 121000  |       | 180000         | -59000         | 18    | 18                                |
| 5  | 2018-12-07 | 7:30:00 161000  |       | 200000         | -39000         | 15    | 16                                |
| 6  | 2018-08-03 | 7:30:00 170000  |       | 189000         | -19000         | -1    | -1                                |
| 7  | 2019-08-02 | 7:30:00 148000  |       | 160000         | -12000         | -8    | -8                                |
| 8  | 2019-04-05 | 7:30:00 182000  |       | 170000         | 12000          | 22    | 23                                |
| 9  | 2018-07-06 | 7:30:00 202000  |       | 190000         | 12000          | 12    | 12                                |
| 10 | 2018-09-07 | 7:30:00 204000  |       | 190000         | 14000          |       |                                   |
| 11 | 2019-07-05 | 7:30:00 191000  |       | 153000         | 38000          | -3    | -2                                |
| 12 | 2019-05-03 | 7:30:00 236000  |       | 180000         | 56000          | 10    | 10                                |
| 13 | 2018-11-02 | 7:30:00 246000  |       | 183000         | 63000          | 11    | 11                                |
| 14 | 2019-01-04 | 7:30:00 301000  |       | 175000         | 126000         | -6    | -6                                |
| 15 | 2019-02-01 | 7:30:00 296000  |       | 170000         | 126000         | 23    | 23                                |

conceptualize this analysis and understand how to apply it to different datasets:

Let's quickly put together a scatter plot to easily visualize how price moves correspond to misses in economic indicator releases:

![](_page_56_Figure_0.jpeg)

As you can observe, positive misses (actual indicator value higher than consensus indicator values) cause prices to move higher. Conversely, negative misses (actual indicator value lower than consensus indicator values) cause prices to move lower. In general, higher NonFarm Payroll job additions are considered to indicate a healthy economy and thus cause the S&P, which tracks major stocks, to increase in value. Another interesting

thing to observe is that the larger the miss, in general, the bigger the price move. So with this simple analysis, we have expected reaction for two unknowns: the direction of a price move due to a miss and the magnitude of the price move as a function of the magnitude of the miss. Now, let's look at how to use this information.

As we discussed before, one of the approaches is to use the miss value and the research to use a trend-following approach and buy on a large positive miss and sell on a large negative miss, with the expectation that prices will move up or down a certain amount. The strategy then closes the long or short position when the expected price move has materialized. This strategy works when the price move and magnitude are in line with the research. Another important consideration is the latency between the release and when the prices begin to move. The strategy needs to be fast enough to initiate a position before the information is available to all other participants and price move has finished.

The other approach is to use the miss value and the research to detect overreaction in price moves and then take the opposite position. In this instance, for a positive miss, if the price decreases, we can have the view that this move is a mistake or an overreaction and initiate a long position with the expectation that prices will go up as our research indicates it should. The other overreaction is if prices move up due to a positive miss as our research indicated but the magnitude of the move is significantly larger than our research indicates. In that case, the strategy waits till prices have moved significantly outside of expectation and then initiates a short position, expecting the overreaction to die down and prices to revert a bit, allowing us to capture a profit. The benefit of the mean reversion trading approach to economic releases over the trend-following approach is that the latter is less sensitive to latency between economic indicator release and time window within which the trading strategy must initiate a position.

### **Understanding and implementing basic statistical arbitrage trading strategies**

**Statistical arbitrage trading strategies** (**StatArb)** first became popular in the 1980s, delivering many firms double-digit returns. It is a class of strategies that tries to capture relationships between short-term price movements in many correlated products. Then it uses relationships that have been found to be statistically significant in the past research to make predictions in the instrument being traded based on price movements in a large group of correlated products.

### **Basics of StatArb**

Statistical arbitrage or StatArb is in some way similar to pairs trading that takes offsetting positions in co-linearly related products that we explored in Chapter 4, *Classical Trading Strategies Driven by Human Intuition*. However, the difference here is that StatArb trading strategies often have *baskets* or portfolios of hundreds of trading instrument, whether they are futures instruments, equities, options, or even currencies. Also, StatArb strategies have a mixture of mean reversion and trend-following strategies. One possibility is that price deviation in the instrument being traded is less than the expected price deviation based on the expected relationship with the price deviations for the portfolio of instruments. In that case, StatArb strategies resemble a trend-following strategy by positioning themselves on the expectation that the trading instrument's price will catch up to the portfolio.

The other case is that price deviation in the instrument being traded is more than the expected price deviation based on the expected relationship with the price deviations for the portfolio of instruments. Here, StatArb strategies resemble a mean reversion strategy by positioning themselves on the expectation that the trading instrument's price will revert back to the portfolio. Most widespread applications of StatArb trading strategies lean more toward mean reversion strategies. StatArb strategies can be considered HFT but can also be medium frequency if the strategy positions last longer than a few milliseconds or a few seconds.

### **Lead-lag in StatArb**

Another important consideration is that this strategy implicitly expects the portfolio to lead and the trading instrument is lagging in terms of reaction by market participants. When this is not true, for example, when the trading instrument we are trying to trade is actually the one leading price moves across the portfolio, then this strategy doesn't perform well, because instead of the trading instrument price catching up to the portfolio, now the portfolio prices catch up to the trading instrument. This is the concept of lead-lag in StatArb; to be profitable, we need to find trading instruments that are mostly lagging and build a portfolio of instruments that are mostly leading.

A lot of the time, the way this manifests itself is that during some market hours, some instruments lead others and during other market hours, that relationship is reversed. For example, intuitively one can understand that during Asia market hours, trading instruments traded in Asian electronic exchanges such as Singapore, India, Hong Kong, and Japan lead price moves in global assets. During European market hours, trading instruments traded in Germany, London, and other European countries lead most price moves across global assets. Finally, during American market hours, trading instruments in America lead price moves. So the ideal approach is to construct portfolios and establish relationships between lead and lag instruments differently in different trading sessions.

# **Adjusting portfolio composition and relationships**

Another important factor to build StatArb strategies that perform well consistently is understanding and building systems to adapt to changing portfolio compositions and relationships between different trading instruments. The drawback of having the StatArb trading strategy depend primarily on the short-term relationships between large number of trading instruments is that it is hard to understand and adapt to changing relationships between price moves in all the different instruments that constitute a portfolio. The portfolio weights themselves change over time. Principal component analysis, a statistical tool from dimensionality reduction techniques, can be used to construct, adapt, and monitor portfolio weights and significance that change over time.

The other important issue is dealing with relationships between the trading instrument and the leading instruments and also between the trading instrument and the portfolio of leading instruments. Sometimes, localized volatility and country-specific economic events cause the fundamental relationship needed to make StatArb profitable break down. For example, political or economic conditions in Brazil can start affecting the Brazilian real currency price moves to no longer be driven by major currencies around the world. Similarly, during periods of localized economic distress in Britain, say for Brexit, or in America, say due to trade wars against China, these portfolio relationships as well as the lead-lag relationships break down from historical expectations and kill the profitability of StatArb trading strategies. Trying to deal with such conditions can require a lot more statistical edges and sophistication beyond just StatArb techniques.

### **Infrastructure expenses in StatArb**

The last big consideration in StatArb trading is the fact that to be successful in StatArb trading strategies as a business, it is very important to be connected to a lot of electronic trading exchanges to get market data across different exchanges across different countries/continents/markets. Being colocated in so many trading exchanges is extremely expensive from an infrastructure cost perspective. The other problem is that one needs to not only be connected to as many exchanges as possible, but a lot of software development investment needs to make to receive, decode, and store market data and also to send orders, since a lot of these exchanges likely use different market data feed and order gateway communication formats.

The final big consideration is that since StatArb strategies need to receive market data from all exchanges, now every venue needs a physical data link from every other venue, which gets exponentially expensive for every exchange added. Then, if one considers using the much more expensive microwave services to deliver data faster to the trading boxes, that makes it even worse. So to summarize, StatArb trading strategies can be significantly more expensive than some of the other trading strategies from an infrastructure perspective when it comes to running an algorithmic trading business.

### **StatArb trading strategy in Python**

Now that we have a good understanding of the principles involved in StatArb trading strategies and some practical considerations in building and operating an algorithmic trading business utilizing StatArb trading strategies, let's look at a realistic trading strategy implementation and understand its behavior and performance. In practice, modern algorithmic trading businesses that operate with high frequency usually use a low-level programming language such as C++.

#### **StatArb data set**

Let's first get the data set we will need to implement a StatArb trading strategy. For this section, we will use the following major currencies across the world:

- **Austrian Dollar versus American Dollar** (**AUD/USD**)
- **British Pound versus American Dollar** (**GBP/USD**)
- **Canadian Dollar versus American Dollar** (**CAD/USD**)
- **Swiss Franc versus American Dollar** (**CHF/USD**)
- **Euro versus American Dollar** (**EUR/USD**)
- **Japanese Yen versus American Dollar** (**JPY/USD**)
- **New Zealand Kiwi versus American Dollar** (**NZD/USD**)

And for this implementation of the StatArb trading strategy, we will try to trade CAD/USD using its relationship with the other currency pairs:

1. Let's fetch 4 years' worth of data for these currency pairs and set up our data frames:

```
import pandas as pd
from pandas_datareader import data
# Fetch daily data for 4 years, for 7 major currency pairs
TRADING_INSTRUMENT = 'CADUSD=X'
SYMBOLS = ['AUDUSD=X', 'GBPUSD=X', 'CADUSD=X', 'CHFUSD=X', 'EURUSD=X', 'JPYUSD=X', 'NZDUSD=X']
START_DATE = '2014-01-01'
END_DATE = '2018-01-01'
# DataSeries for each currency
symbols_data = {}
for symbol in SYMBOLS:
 SRC_DATA_FILENAME = symbol + '_data.pkl'
 try:
 data = pd.read_pickle(SRC_DATA_FILENAME)
 except FileNotFoundError:
 data = data.DataReader(symbol, 'yahoo', START_DATE, END_DATE)
 data.to_pickle(SRC_DATA_FILENAME)
 symbols_data[symbol] = data
```

2. Let's quickly visualize each currency pair's prices over the period of our data set and see what we observe. We scale the JPY/USD pair by 100.0 purely for visualization scaling purposes:

```
# Visualize prices for currency to inspect relationship between them
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
cycol = cycle('bgrcmky')
price_data = pd.DataFrame()
for symbol in SYMBOLS:
 multiplier = 1.0
 if symbol == 'JPYUSD=X':
 multiplier = 100.0
 label = symbol + ' ClosePrice'
 price_data = price_data.assign(label=pd.Series(symbols_data[symbol]['Close'] * multiplier, index=symbols_data[symbol]
 ax = price_data['label'].plot(color=next(cycol), lw=2., label=label)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Scaled Price', fontsize=18)
plt.legend(prop={'size': 18})
plt.show()
```

The code will return the following output. Let's have a look at the plot:

![](_page_65_Figure_0.jpeg)

As one would expect and can observe, these currency pairs' price moves are all similar to each other in varying degrees. CAD/USD, AUD/USD, and NZD/USD seem to be most correlated, with CHF/USD and JPY/USD being least correlated to CAD/USD. For the purposes of this strategy, we will use all currencies in the trading model because these relationships are obviously not known ahead of time.

#### **Defining StatArb signal parameters**

Now, let's define and quantify some parameters we will need to define moving averages, price deviation from moving averages, history of price deviations, and variables to compute and track correlations:

```
import statistics as stats
# Constants/variables that are used to compute simple moving average and price deviation from simple moving average
SMA_NUM_PERIODS = 20 # look back period
price_history = {} # history of prices
PRICE_DEV_NUM_PRICES = 200 # look back period of ClosePrice deviations from SMA
price_deviation_from_sma = {} # history of ClosePrice deviations from SMA
# We will use this to iterate over all the days of data we have
num_days = len(symbols_data[TRADING_INSTRUMENT].index)
correlation_history = {} # history of correlations per currency pair
delta_projected_actual_history = {} # history of differences between Projected ClosePrice deviation and actual ClosePrice devia
```

final\_delta\_projected\_history = [] # history of differences between final Projected ClosePrice deviation for TRADING\_INSTRUMENT

#### **Defining StatArb trading parameters**

Now, before we get into the main strategy loop, let's define some final variables and thresholds we will need to build our StatArb trading strategy:

# Variables for Trading Strategy trade, position & pnl management: orders = [] # Container for tracking buy/sell order, +1 for buy order, -1 for sell order, 0 for no-action positions = [] # Container for tracking positions, positive for long positions, negative for short positions, 0 for flat/no pos pnls = [] # Container for tracking total\_pnls, this is the sum of closed\_pnl i.e. pnls already locked in and open\_pnl i.e. pnls last\_buy\_price = 0 # Price at which last buy trade was made, used to prevent over-trading at/around the same price last\_sell\_price = 0 # Price at which last sell trade was made, used to prevent over-trading at/around the same price position = 0 # Current position of the trading strategy buy\_sum\_price\_qty = 0 # Summation of products of buy\_trade\_price and buy\_trade\_qty for every buy Trade made since last time bei buy\_sum\_qty = 0 # Summation of buy\_trade\_qty for every buy Trade made since last time being flat sell\_sum\_price\_qty = 0 # Summation of products of sell\_trade\_price and sell\_trade\_qty for every sell Trade made since last time sell\_sum\_qty = 0 # Summation of sell\_trade\_qty for every sell Trade made since last time being flat open\_pnl = 0 # Open/Unrealized PnL marked to market closed\_pnl = 0 # Closed/Realized PnL so far # Constants that define strategy behavior/thresholds StatArb\_VALUE\_FOR\_BUY\_ENTRY = 0.01 # StatArb trading signal value above which to enter buy-orders/long-position StatArb\_VALUE\_FOR\_SELL\_ENTRY = -0.01 # StatArb trading signal value below which to enter sell-orders/short-position

MIN\_PRICE\_MOVE\_FROM\_LAST\_TRADE = 0.01 # Minimum price change since last trade before considering trading again, this is to prev NUM\_SHARES\_PER\_TRADE = 1000000 # Number of currency to buy/sell on every trade

MIN\_PROFIT\_TO\_CLOSE = 10 # Minimum Open/Unrealized profit at which to close positions and lock profits

#### **Quantifying and computing StatArb trading signals**

1. We will see over available prices a day at a time and see what calculations need to be performed, starting with the computation of SimpleMovingAverages and price deviation from the rolling SMA first:

```
for i in range(0, num_days):
 close_prices = {}
 # Build ClosePrice series, compute SMA for each symbol and price-deviation from SMA for each symbol
 for symbol in SYMBOLS:
 close_prices[symbol] = symbols_data[symbol]['Close'].iloc[i]
 if not symbol in price_history.keys():
 price_history[symbol] = []
 price_deviation_from_sma[symbol] = []
 price_history[symbol].append(close_prices[symbol])
 if len(price_history[symbol]) > SMA_NUM_PERIODS: # we track at most SMA_NUM_PERIODS number of prices
 del (price_history[symbol][0])
 sma = stats.mean(price_history[symbol]) # Rolling SimpleMovingAverage
 price_deviation_from_sma[symbol].append(close_prices[symbol] - sma) # price deviation from mean
 if len(price_deviation_from_sma[symbol]) > PRICE_DEV_NUM_PRICES:
 del (price_deviation_from_sma[symbol][0])
```

2. Next, we need to compute the relationships between the CAD/USD currency pair price deviations and the other currency pair price deviations. We will use covariance and correlation between the series of price deviations from SMA that we computed in the previous section. In this same loop, we will also compute the CAD/USD price deviation as projected by every other lead currency pair, and see what the difference between the projected price deviation and actual price deviation is. We will need these individual deltas between projected price deviation and actual price deviation to get a final delta value that we will use for trading.

First, let's look at the code block that populates the correlation\_history and the delta\_projected\_actual\_history dictionaries:

```
 # Now compute covariance and correlation between TRADING_INSTRUMENT and every other lead symbol
 # also compute projected price deviation and find delta between projected and actual price deviations.
 projected_dev_from_sma_using = {}
 for symbol in SYMBOLS:
 if symbol == TRADING_INSTRUMENT: # no need to find relationship between trading instrument and itself
 continue
 correlation_label = TRADING_INSTRUMENT + '<-' + symbol
 if correlation_label not in correlation_history.keys(): # first entry for this pair in the history dictionary
 correlation_history[correlation_label] = []
 delta_projected_actual_history[correlation_label] = []
 if len(price_deviation_from_sma[symbol]) < 2: # need atleast two observations to compute covariance/correlation
 correlation_history[correlation_label].append(0)
 delta_projected_actual_history[correlation_label].append(0)
 continue
```

Now, let's look at the code block to compute correlation and covariance between the currency pairs:

 corr = np.corrcoef(price\_deviation\_from\_sma[TRADING\_INSTRUMENT], price\_deviation\_from\_sma[symbol]) cov = np.cov(price\_deviation\_from\_sma[TRADING\_INSTRUMENT], price\_deviation\_from\_sma[symbol]) corr\_trading\_instrument\_lead\_instrument = corr[0, 1] # get the correlation between the 2 series cov\_trading\_instrument\_lead\_instrument = cov[0, 0] / cov[0, 1] # get the covariance between the 2 series

correlation\_history[correlation\_label].append(corr\_trading\_instrument\_lead\_instrument)

Finally, let's look at the code block that computes the projected price movement, uses that to find the difference between the projected movement and actual movement, and saves it in our

delta\_projected\_actual\_history list per currency pair:

 # projected-price-deviation-in-TRADING\_INSTRUMENT is covariance \* price-deviation-in-lead-symbol projected\_dev\_from\_sma\_using[symbol] = price\_deviation\_from\_sma[symbol][-1] \* cov\_trading\_instrument\_lead\_instrumen

 # delta positive => signal says TRADING\_INSTRUMENT price should have moved up more than what it did # delta negative => signal says TRADING\_INSTRUMENT price should have moved down more than what it did. delta\_projected\_actual = (projected\_dev\_from\_sma\_using[symbol] - price\_deviation\_from\_sma[TRADING\_INSTRUMENT][-1]) delta\_projected\_actual\_history[correlation\_label].append(delta\_projected\_actual)

3. Let's combine these individual deltas between projected and actual price deviation in CAD/USD to get one final StatArb signal value for CAD/USD that is a combination of projections from all the other currency pairs. To combine these different projections, we will use the magnitude of the correlation between CAD/USD and the other currency pairs to weigh the delta between projected and actual price deviations in CAD/USD as predicted by the other pairs. Finally, we will normalize the final delta value by the sum of each individual weight (magnitude of correlation) and that is what we will use as our final signal to build our trading strategy around:

```
 # weigh predictions from each pair, weight is the correlation between those pairs
 sum_weights = 0 # sum of weights is sum of correlations for each symbol with TRADING_INSTRUMENT
 for symbol in SYMBOLS:
 if symbol == TRADING_INSTRUMENT: # no need to find relationship between trading instrument and itself
 continue
 correlation_label = TRADING_INSTRUMENT + '<-' + symbol
 sum_weights += abs(correlation_history[correlation_label][-1])
 final_delta_projected = 0 # will hold final prediction of price deviation in TRADING_INSTRUMENT, weighing projections
 close_price = close_prices[TRADING_INSTRUMENT]
 for symbol in SYMBOLS:
 if symbol == TRADING_INSTRUMENT: # no need to find relationship between trading instrument and itself
 continue
 correlation_label = TRADING_INSTRUMENT + '<-' + symbol
 # weight projection from a symbol by correlation
 final_delta_projected += (abs(correlation_history[correlation_label][-1]) * delta_projected_actual_history[correlat
 # normalize by diving by sum of weights for all pairs
 if sum_weights != 0:
 final_delta_projected /= sum_weights
 else:
 final_delta_projected = 0
 final_delta_projected_history.append(final_delta_projected)
```

#### **StatArb execution logic**

Let's execute a strategy for the StatArb signal using the following steps:

1. Now, using the StatArb signal we just computed, we can build a strategy similar to the trend-following strategy we saw before. Let's start by looking at the trading logic that controls the sell trades:

```
 if ((final_delta_projected < StatArb_VALUE_FOR_SELL_ENTRY and abs(close_price - last_sell_price) > MIN_PRICE_MOVE_FRO
 or
 (position > 0 and (open_pnl > MIN_PROFIT_TO_CLOSE))): # long from negative StatArb and StatArb has gone positive 
 orders.append(-1) # mark the sell trade
 last_sell_price = close_price
 position -= NUM_SHARES_PER_TRADE # reduce position by the size of this trade
 sell_sum_price_qty += (close_price * NUM_SHARES_PER_TRADE) # update vwap sell-price
 sell_sum_qty += NUM_SHARES_PER_TRADE
 print("Sell ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position)
 print("OpenPnL: ", open_pnl, " ClosedPnL: ", closed_pnl, " TotalPnL: ", (open_pnl + closed_pnl))
```

2. Now, let's look at the buy trade logic, which is quite similar to the sell trade logic:

```
 elif ((final_delta_projected > StatArb_VALUE_FOR_BUY_ENTRY and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FRO
 or
 (position < 0 and (open_pnl > MIN_PROFIT_TO_CLOSE))): # short from positive StatArb and StatArb has gone negati
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 position += NUM_SHARES_PER_TRADE # increase position by the size of this trade
 buy_sum_price_qty += (close_price * NUM_SHARES_PER_TRADE) # update the vwap buy-price
 buy_sum_qty += NUM_SHARES_PER_TRADE
 print("Buy ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position)
 print("OpenPnL: ", open_pnl, " ClosedPnL: ", closed_pnl, " TotalPnL: ", (open_pnl + closed_pnl))
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
 positions.append(position)
```

3. Finally, let's also look at the position management and PnL update logic, very similar to previous trading strategies:

```
 # This section updates Open/Unrealized & Closed/Realized positions
 open_pnl = 0
 if position > 0:
 if sell_sum_qty > 0: # long position and some sell trades have been made against it, close that amount based on how
 open_pnl = abs(sell_sum_qty) * (sell_sum_price_qty / sell_sum_qty - buy_sum_price_qty / buy_sum_qty)
 # mark the remaining position to market i.e. pnl would be what it would be if we closed at current price
 open_pnl += abs(sell_sum_qty - position) * (close_price - buy_sum_price_qty / buy_sum_qty)
 elif position < 0:
 if buy_sum_qty > 0: # short position and some buy trades have been made against it, close that amount based on how 
 open_pnl = abs(buy_sum_qty) * (sell_sum_price_qty / sell_sum_qty - buy_sum_price_qty / buy_sum_qty)
 # mark the remaining position to market i.e. pnl would be what it would be if we closed at current price
 open_pnl += abs(buy_sum_qty - position) * (sell_sum_price_qty / sell_sum_qty - close_price)
 else:
 # flat, so update closed_pnl and reset tracking variables for positions & pnls
 closed_pnl += (sell_sum_price_qty - buy_sum_price_qty)
 buy_sum_price_qty = 0
 buy_sum_qty = 0
 sell_sum_price_qty = 0
 sell_sum_qty = 0
 last_buy_price = 0
 last_sell_price = 0
```

pnls.append(closed\_pnl + open\_pnl)

#### **StatArb signal and strategy performance analysis**

Now, let's analyze the StatArb signal using the following steps:

1. Let's visualize a few more details about the signals in this trading strategy, starting with the correlations between CAD/USD and the other currency pairs as it evolves over time:

```
# Plot correlations between TRADING_INSTRUMENT and other currency pairs
correlation_data = pd.DataFrame()
for symbol in SYMBOLS:
 if symbol == TRADING_INSTRUMENT:
 continue
 correlation_label = TRADING_INSTRUMENT + '<-' + symbol
 correlation_data = correlation_data.assign(label=pd.Series(correlation_history[correlation_label], index=symbols_data
 ax = correlation_data['label'].plot(color=next(cycol), lw=2., label='Correlation ' + correlation_label)
for i in np.arange(-1, 1, 0.25):
 plt.axhline(y=i, lw=0.5, color='k')
plt.legend()
plt.show()
```

This plot shows the correlation between CADUSD and other currency pairs as it evolves over the course of this trading strategy. Correlations close to -1 or +1 signify strongly correlated pairs, and correlations that hold steady are the stable correlated pairs. Currency pairs where correlations swing around between negative and positive values indicate extremely uncorrelated or unstable currency pairs, which are unlikely to yield good predictions in the long run. However, we do not know how the correlation would evolve ahead of time, so we have no choice but to use all currency pairs available to us in our StatArb trading strategy:

![](_page_71_Figure_5.jpeg)

As we suspected, the currency pairs that are most strongly correlated to CAD/USD price deviations are AUD/USD and NZD/USD. JPY/USD is the least correlated to CAD/USD price deviations.

2. Now, let's inspect the delta between projected and actual price deviations in CAD/USD as projected by each individual currency pair individually:

```
# Plot StatArb signal provided by each currency pair
delta_projected_actual_data = pd.DataFrame()
for symbol in SYMBOLS:
 if symbol == TRADING_INSTRUMENT:
 continue
 projection_label = TRADING_INSTRUMENT + '<-' + symbol
 delta_projected_actual_data = delta_projected_actual_data.assign(StatArbTradingSignal=pd.Series(delta_projected_actua
 ax = delta_projected_actual_data['StatArbTradingSignal'].plot(color=next(cycol), lw=1., label='StatArbTradingSignal '
plt.legend()
plt.show()
```

This is what the StatArb signal values would look like if we used any of the currency pairs alone to project CAD/USD price deviations:

![](_page_72_Figure_1.jpeg)

Here, the plot seems to suggest that JPYUSD and CHFUSD have very large predictions, but as we saw before those pairs do not have good correlations with CADUSD, so these are likely to be bad predictions due to poor predictive relationships between CADUSD - JPYUSD and CADUSD - CHFUSD. One lesson to take away from this is that StatArb benefits from having multiple leading trading instruments, because when relationships break down between specific pairs, the other strongly correlated pairs can help offset bad predictions, which we discussed earlier.

3. Now, let's set up our data frames to plot the close price, trades, positions, and PnLs we will observe:

delta\_projected\_actual\_data = delta\_projected\_actual\_data.assign(ClosePrice=pd.Series(symbols\_data[TRADING\_INSTRUMENT][ delta\_projected\_actual\_data = delta\_projected\_actual\_data.assign(FinalStatArbTradingSignal=pd.Series(final\_delta\_projec delta\_projected\_actual\_data = delta\_projected\_actual\_data.assign(Trades=pd.Series(orders, index=symbols\_data[TRADING\_IN delta\_projected\_actual\_data = delta\_projected\_actual\_data.assign(Position=pd.Series(positions, index=symbols\_data[TRADI delta\_projected\_actual\_data = delta\_projected\_actual\_data.assign(Pnl=pd.Series(pnls, index=symbols\_data[TRADING\_INSTRUM plt.plot(delta\_projected\_actual\_data.index, delta\_projected\_actual\_data.ClosePrice, color='k', lw=1., label='ClosePrice plt.plot(delta\_projected\_actual\_data.loc[delta\_projected\_actual\_data.Trades == 1].index, delta\_projected\_actual\_data.Cl plt.plot(delta\_projected\_actual\_data.loc[delta\_projected\_actual\_data.Trades == -1].index, delta\_projected\_actual\_data.C plt.legend() plt.show()

The following plot tells us at what prices the buy and sell trades are made in CADUSD. We will need to inspect the final trading signal in addition to this plot to fully understand the behavior of this StatArb signal and strategy:

![](_page_72_Figure_6.jpeg)

Now, let's look at the actual code to build visualization for the final StatArb trading signal, and overlay buy and sell trades over the lifetime of the signal evolution. This will help us understand for what signal values buy and sell trades are made and if that is in line with our expectations:

```
plt.plot(delta_projected_actual_data.index, delta_projected_actual_data.FinalStatArbTradingSignal, color='k', lw=1., la
plt.plot(delta_projected_actual_data.loc[delta_projected_actual_data.Trades == 1].index, delta_projected_actual_data.Fi
plt.plot(delta_projected_actual_data.loc[delta_projected_actual_data.Trades == -1].index, delta_projected_actual_data.F
plt.axhline(y=0, lw=0.5, color='k')
for i in np.arange(StatArb_VALUE_FOR_BUY_ENTRY, StatArb_VALUE_FOR_BUY_ENTRY * 10, StatArb_VALUE_FOR_BUY_ENTRY * 2):
 plt.axhline(y=i, lw=0.5, color='r')
for i in np.arange(StatArb_VALUE_FOR_SELL_ENTRY, StatArb_VALUE_FOR_SELL_ENTRY * 10, StatArb_VALUE_FOR_SELL_ENTRY * 2):
 plt.axhline(y=i, lw=0.5, color='g')
plt.legend()
plt.show()
```

Since we adopted the trend-following approach in our StatArb trading strategy, we expect to buy when the signal value is positive and sell when the signal value is negative. Let's see whether that's the case in the plot:

![](_page_73_Figure_3.jpeg)

Based on this plot and our understanding of trend-following strategies in addition to the StatArb signal we built, we do indeed see many buy trades when the signal value is positive and sell trades when the signal values are negative. The buy trades made when signal values are negative and sell trades made when signal values are positive can be attributed to the trades that close profitable positions, as we saw in our previous mean reversion and trend-following trading strategies.

4. Let's wrap up our analysis of StatArb trading strategies by visualizing the positions and PnLs:

```
plt.plot(delta_projected_actual_data.index, delta_projected_actual_data.Position, color='k', lw=1., label='Position')
plt.plot(delta_projected_actual_data.loc[delta_projected_actual_data.Position == 0].index, delta_projected_actual_data.
plt.plot(delta_projected_actual_data.loc[delta_projected_actual_data.Position > 0].index, delta_projected_actual_data.P
plt.plot(delta_projected_actual_data.loc[delta_projected_actual_data.Position < 0].index, delta_projected_actual_data.P
plt.axhline(y=0, lw=0.5, color='k')
for i in range(NUM_SHARES_PER_TRADE, NUM_SHARES_PER_TRADE * 5, NUM_SHARES_PER_TRADE):
 plt.axhline(y=i, lw=0.5, color='r')
for i in range(-NUM_SHARES_PER_TRADE, -NUM_SHARES_PER_TRADE * 5, -NUM_SHARES_PER_TRADE):
 plt.axhline(y=i, lw=0.5, color='g')
plt.legend()
plt.show()
```

The position plot shows the evolution of the StatArb trading strategy's position over the course of its lifetime. Remember that these positions are in dollar notional terms, so a position of 100K is equivalent to roughly 1 future contract, which we mention to make it clear that a position of 100K does not mean a position of 100K contracts!

![](_page_74_Figure_0.jpeg)

5. Finally, let's have a look at the code for the PnL plot, identical to what we've been using before:

plt.plot(delta\_projected\_actual\_data.index, delta\_projected\_actual\_data.Pnl, color='k', lw=1., label='Pnl') plt.plot(delta\_projected\_actual\_data.loc[delta\_projected\_actual\_data.Pnl > 0].index, delta\_projected\_actual\_data.Pnl[de plt.plot(delta\_projected\_actual\_data.loc[delta\_projected\_actual\_data.Pnl < 0].index, delta\_projected\_actual\_data.Pnl[de plt.legend() plt.show()

We expect to see better performance here than in our previously built trading strategies because it relies on a fundamental relationship between different currency pairs and should be able to perform better during different market conditions because of its use of multiple currency pairs as lead trading instruments:

![](_page_74_Figure_4.jpeg)

And that's it, now you have a working example of a profitable statistical arbitrage strategy and should be able to improve and extend it to other trading instruments!

### **Summary**

This chapter made use of some of the trading signals we've seen in the previous chapters to build realistic and robust trend-following and mean reversion trading strategies. In addition, we went another step further and made those basic strategies more sophisticated by adding a volatility measure trading signal to make it more dynamic and adaptive to different market conditions. We also looked at a completely new form of trading strategy in the form of trading strategies dealing with economic releases and how to carry out the analysis for that flavor of trading strategies for our sample Non Farm Payroll data. Finally, we looked at our most sophisticated and complex trading strategy so far, which was the statistical arbitrage strategy, and applied it to CAD/USD with the major currency pairs as leading trading signals. We investigated in great detail how to quantify and parameterize the StatArb trading signal and trading strategy and visualized every step of that process and concluded that the trading strategy delivered excellent results for our data set.

In the next chapter, you will learn how to measure and manage the risk (market risk, operational risk, and software implementation bugs) of algorithmic strategies.

# **Managing the Risk of Algorithmic Strategies**

So far, we have built a good understanding of how algorithmic trading works and how we can build trading signals from market data. We also looked into some basic trading strategies, as well as more sophisticated trading strategies, so it may seem like we are in a good place to start trading, right? Not quite. Another very important requirement to be successful at algorithmic trading is understanding risk management and using good risk management practices.

Bad risk management practices can turn any good algorithmic trading strategy into a non-profitable one. On the other hand, good risk management practices can turn a seemingly inferior trading strategy into an actually profitable one. In this chapter, we will examine the different kinds of risk in algorithmic trading, look at how to quantitatively measure and compare these risks, and explore how to build a good risk management system to adhere to these risk management practices.

In this chapter, we will cover the following topics:

- Differentiating between the types of risk and risk factors
- Quantifying the risk
- Differentiating between the measures of risk
- Making a risk management algorithm

### **Differentiating between the types of risk and risk factors**

Risks in algorithmic trading strategies can basically be of two things: risks that cause money loss and risks that cause illegal/forbidden behavior in markets that cause regulatory actions. Let's take a look at the risks involved before we look at what factors lead to increasing/decreasing these risks in the business of algorithmic trading.

### **Risk of trading losses**

This is the most obvious and intuitive one—we want to trade to make money, but we always run through the risk of losing money against other market participants. Trading is a zero-sum game: some participants will make money, while some will lose money. The amount that's lost by the losing participants is the amount that's gained by the winning participants. This simple fact is what also makes trading quite challenging. Generally, less informed participants will lose money to more informed participants. Informed is a loose term here; it can mean participants with access to information that others don't have. This can include access to secretive or expensive or even illegal information sources, the ability to transport and consume such information that other participants don't have, and so on. Information edge can also be gained by participants with a superior ability to glean information from the available information, that is, some participants will have better signals, better analytics abilities, and better predictive abilities to edge out less informed participants. Obviously, more sophisticated participants will also beat less sophisticated participants.

Sophistication can be gained from technology advantages as well, such as faster reacting trading strategies. The use of a low-level language such as C/C++ is harder to develop software in but allows us to build trading software systems that react in single-digit microseconds processing time. An extreme speed advantage is available to participants that use **Field Programmable Gate Arrays** (**FPGAs**) to achieve sub-microsecond response times to market data updates. Another avenue of gaining sophistication is by having more complex trading algorithms with more complex logic that's meant to squeeze out as much edge as possible. It should be clear that algorithmic trading is an extremely complex and competitive business and that all the participants are doing their best to squeeze out every bit of profit possible by being more *informed* and *sophisticated*.

<https://news.efinancialcareers.com/us-en/291459/xr-trading-2016> discusses an example of trading losses due to decreased profitability, which occurs due to competition among market participants.

### **Regulation violation risks**

The other risk that isn't everyone's first thought has to do with making sure that algorithmic trading strategies are not violating any regulatory rules. Failing to do so often results in astronomical fines, massive legal fees, and can often get participants banned from trading from certain or all exchanges. Since setting up successful algorithmic trading businesses are multi-year, multi-million dollar ventures, getting shut down due to regulatory reasons can be crushing. The SEC (<https://www.sec.gov/>), FINRA (<https://www.finra.org/>), and CFTC (<https://www.cftc.gov/>) are just some of many regulatory governing bodies watching over algorithmic trading activity in equity, currency, futures, and options markets.

These regulatory firms enforce global and local regulations. In addition, the electronic trading exchanges themselves impose regulations and laws, the violation of which can also incur severe penalties. There are many market participants or algorithmic trading strategy behaviors that are forbidden. Some incur a warning or an audit and some incur penalties. Insider trading reports are quite well known by people inside and outside of the algorithmic trading business. While insider trading doesn't really apply to algorithmic trading or high-frequency trading, we will introduce some of the common issues in algorithmic trading here.

This list is nowhere near complete, but these are the top regulatory issues in algorithmic trading or high-frequency trading.

# **Spoofing**

**Spoofing** typically refers to the practice of entering orders into the market that are not considered bonafide. A **bonafide** order is one that is entered with the intent of trading. Spoofing orders are entered into the market with the intent of misleading other market participants, and these orders were never entered with the intent of being executed. The purpose of these orders is to make other participants believe that there are more real market participants who are willing to buy or sell than there actually are. By spoofing on the bid side, market participants are misled into thinking there is a lot of interest in buying. This usually leads to other market participants adding more orders to the bid side and moving or removing orders on the ask side with the expectation that prices will go up.

When prices go up, the spoofer then sells at a higher price than would've been possible without the spoofing orders. At this point, the spoofer initiates a short position and cancels all the spoofing bid orders, causing other market participants to do the same. This drive prices back down from these synthetically raised higher prices. When prices have dropped sufficiently, the spoofer then buys at lower prices to cover the short position and lock in a profit.

Spoofing algorithms can repeat this over and over in markets that are mostly algorithmically trading and make a lot of money. This, however, is illegal in most markets because it causes market price instability, provides participants with misleading information about available market liquidity, and adversely affects non-algorithmic trading investors/strategies. In summary, if such behavior was not made illegal, it would cause cascading instability and make most market participants exit providing liquidity. Spoofing is treated as a serious violation in most electronic exchanges, and exchanges have sophisticated algorithms/monitoring systems to detect such behavior and flag market participants who are spoofing.

The first case of spoofing got a lot of publicity, and those of you who are interested can learn more at https://www.justice.gov/usao-ndil/pr/high-frequency-t

[rader-sentenced-three-years-prison-disrupting-futures-market-first](https://www.justice.gov/usao-ndil/pr/high-frequency-trader-sentenced-three-years-prison-disrupting-futures-market-first).

### **Quote stuffing**

**Quote stuffing** is a manipulation tactic that was employed by highfrequency trading participants. Nowadays, most exchanges have many rules that make quote stuffing infeasible as a profitable trading strategy. Quote stuffing is the practice of using very fast trading algorithms and hardware to enter, modify, and cancel large amounts of orders in one or more trading instruments. Since each order action by a market participant causes the generation of public market data, it is possible for very fast participants to generate a massive amount of market data and massively slow down slower participants who can no longer react in time, thereby causing profits for high-frequency trading algorithms.

This is not as feasible in modern electronic trading markets, mainly because exchanges have put in rules on messaging limits on individual market participants. Exchanges have the ability to analyze and flag short-lived nonbonafide order flow, and modern matching engines are able to better synchronize market data feeds with order flow feeds.

[https://www.businessinsider.com/huge-first-high-frequency-trading-firm-is-charged-wi](https://www.businessinsider.com/huge-first-high-frequency-trading-firm-is-charged-with-quote-stuffing-and-manipulation-2010-9) th-quote-stuffing-and-manipulation-2010-9 discusses a recent quote stuffing market manipulation incident that caused regulatory actions.

### **Banging the close**

**Banging the close** is a disruptive and manipulative trading practice that still happens periodically in electronic trading markets, either intentionally or accidentally, by trading algorithms. This practice has to do with illegally manipulating the closing price of a derivative, also known as the settlement price. Since positions in derivatives markets such as futures are marked at the settlement price at the end of the day, this tactic uses large orders during the final few minutes or seconds of closing where many market participants are out of the market already to drive less liquid market prices in an illegal and disruptive way.

This is, in some sense, similar to spoofing, but in this case, often, the participants banging the close may not pick up new executions during the closing period, but may simply try to move market prices to make their already existing positions more profitable. For cash-settled derivatives contracts, the more favorable settlement price leads to more profit. This is why trading closes are also monitored quite closely by electronic trading derivative exchanges to detect and flag this disruptive practice.

<https://www.cftc.gov/PressRoom/PressReleases/pr5815-10> discusses an incident of banging the close for those who are interested.

### **Sources of risk**

Now that we have a good understanding of the different kinds of risk in algorithmic trading, let's look at the factors in algorithmic trading strategy development, optimization, maintenance, and operation that causes them.

### **Software implementation risk**

A modern algorithmic trading business is essentially a technology business, hence giving birth to the new term **FinTech** to mean the intersection of finance and technology. Computer software is designed, developed, and tested by humans who are error-prone and sometimes, these errors creep into trading systems and algorithmic trading strategies. Software implementation bugs are often the most overlooked source of risk in algorithmic trading. While operation risk and market risk are extremely important, software implementation bugs have the potential to cause millions of dollars in losses, and there have been many cases of firms going bankrupt due to software implementation bugs within minutes.

In recent times, there was the infamous Knight Capital incident, where a software implementation bug combined with an operations risk issue caused them to lose \$440 million within 45 minutes and they ended up getting shut down. Software implementation bugs are also very tricky because software engineering is a very complex process, and when we add the additional complexity of having sophisticated and complex algorithmic trading strategies and logic, it is hard to guarantee that the implementation of trading strategies and systems are safe from bugs. More information can be found at [https://dealbook.nytimes.com/2012/08/02/knight-capital-says-trading-mishap](https://dealbook.nytimes.com/2012/08/02/knight-capital-says-trading-mishap-cost-it-440-million/)

-cost-it-440-million/.

Modern algorithmic trading firms have rigorous software development practices to safeguard themselves against software bugs. These include rigorous unit tests, which are small tests on individual software components to verify their behavior doesn't change to an incorrect behavior as software development/maintenance being made to existing components is performed. There are also regression tests, which are tests that test larger components that are composed of smaller components as a whole to ensure the higherlevel behavior remains consistent. All electronic trading exchanges also provide a test market environment with test market data feeds and test order entry interfaces where market participants have to build, test, and certify

their components with the exchange before they are even allowed to trade in live markets.

Most sophisticated algorithmic trading participants also have backtesting software that simulates a trading strategy over historically recorded data to ensure strategy behavior is in line with expectations. We will explore backtesting further in Chapter 9, *Creating a Backtester in Python*. Finally, other software management practices, such as code reviews and change management, are also performed on a daily basis to verify the integrity of algorithmic trading systems and strategies on a daily basis. Despite all of these precautions, software implementation bugs do slip into live trading markets, so we should always be aware and cautious because software is never perfect and the cost of mistakes/bugs is very high in the algorithmic trading business, and even higher in the HFT business.

### **DevOps risk**

**DevOps risk** is the term that is used to describe the risk potential when algorithmic trading strategies are deployed to live markets. This involves building and deploying correct trading strategies and configuring the configuration, the signal parameters, the trading parameters, and starting, stopping, and monitoring them. Most modern trading firms trade markets electronically almost 23 hours a day, and they have a large number of staff whose only job is to keep an eye on the automated algorithmic trading strategies that are deployed to live markets to ensure they are behaving as expected and no erroneous behavior goes uninvestigated. They are known as the Trading Desk, or TradeOps or DevOps.

These people have a decent understanding of software development, trading rules, and exchange for provided risk monitoring interfaces. Often, when software implementation bugs end up going to live markets, they are the final line of defense, and it is their job to monitor the systems, detect issues, safely pause or stop the algorithms, and contact and resolve the issues that have emerged. This is the most common understanding of where operation risk can show up. Another source of operation risk is in algorithmic trading strategies that are not 100% black box. Black box trading strategies are trading strategies that do not require any human feedback or interaction. These are started at a certain time and then stopped at a certain time, and the algorithms themselves make all the decisions.

Gray box trading strategies are trading strategies that are not 100% autonomous. These strategies still have a lot of automated decision-making built into them, but they also have external controls that allow the traders or TradeOps engineers to monitor the strategies, as well as adjust parameters and trading strategy behavior, and even send manual orders. Now, during these manual human interventions, there is another source of risk, which is basically the risk of humans making mistakes in the commands/adjustments that are sent to these strategies. Sending incorrect parameters can cause the algorithm to behave incorrectly and cause losses.

There are also cases of sending bad commands, which can cause an unexpected and unintentional large impact on the market, causing trading losses and market disruptions that add regulatory fines. One of the common errors is the fat finger error, where prices, sizes, and buy/sell instructions are sent incorrectly due to a *fat finger*. Some examples can be found at http

[s://www.bloomberg.com/news/articles/2019-01-24/oops-a-brief-history-of-some-of-the-m](https://www.bloomberg.com/news/articles/2019-01-24/oops-a-brief-history-of-some-of-the-market-s-worst-fat-fingers) arket-s-worst-fat-fingers.

### **Market risk**

Finally, we have market risk, which is what is commonly thought of when we think of risk in algorithmic trading. This is the risk of trading against and losing money to more informed participants. Every market participant, at some point or the other, on some trade or the other, will lose money to a more informed participant. We discussed what makes an informed participant superior to a non-informed one in the previous section. Obviously, the only way to avoid market risk is to get access to more information, improve the trading edge, improve sophistication, and improve technology advantages. But since market risk is a truth of all algorithmic trading strategies, a very important aspect is to understand the behavior of the algorithmic trading strategy before deploying it to live markets.

This involves understanding what to expect normal behavior to look like and, more importantly, understanding when a certain strategy makes and loses money and quantifying loss metrics to set up expectations. Then, risk limits are set up at multiple places in an algorithmic trading pipeline in the trading strategy, then in a central risk monitoring system, then in the order gateway, sometimes at the clearing firm, and finally sometimes even at the exchange level. Each extra layer of risk check can slow down a market participant's ability to react to fast-moving markets, but it is essential to have these to prevent runaway trading algorithms from causing a lot of damage.

Once the trading strategy has violated maximum trading risk limits assigned to it, it will be shut down at one or more places where the risk validation is set up. Market risk is very important to understand, implement, and configure correctly because incorrect risk estimates can kill a profitable trading strategy by increasing the frequency and magnitude of losing trades, losing positions, losing days, and even losing weeks or months. This is because the trading strategy could have lost its profitable edge and if you leave it running for too long without adapting it to changing markets, it can erode all the profits the strategy may have generated in the past. Sometimes,

market conditions are very different than what is expected and strategies can go through periods of larger than normal losses, in which cases it is important to have risk limits set up to detect outsized losses and adjust trading parameters or stop trading.

We will look at what risk measures are common in algorithmic trading, how to quantify and research them from historical data, and how to configure and calibrate algorithmic strategies before deploying them to live markets. For now, the summary is that market risk is a normal part of algorithmic trading, but failing to understand and prepare for it can destroy a lot of good trading strategies.

# **Quantifying the risk**

Now, let's get started with understanding what realistic risk constraints look like and how to quantify them. We will list, define, and implement some of the most commonly used risk limits in the modern algorithmic trading industry today. We will use the volatility adjusted mean reversion strategy we built in Chapter 5, *Sophisticated Algorithmic Strategies*, as our realistic trading strategy, which we now need to define and quantify risk measures for.

### **The severity of risk violations**

One thing to understand before diving into all the different risk measures is defining what the severity of a risk violation means. So far, we've been discussing risk violations as being maximum risk limit violations. But in practice, there are multiple levels of every risk limit, and each level of risk limit violation is not equally as catastrophic to algorithmic trading strategies. The lowest severity risk violation would be considered a warning risk violation, which means that this risk violation, while not expected to happen regularly, can happen normally during a trading strategy operation. Intuitively, it is easy to think of this as, say, on most days, trading strategies do not send more than 5,000 orders a day, but on certain volatile days, it is possible and acceptable that the trading strategy sends 20,000 orders on that day. This would be considered an example of a warning risk violation – this is unlikely, but not a sign of trouble. The purpose of this risk violation is to warn the trader that something unlikely is happening in the market or trading strategy.

The next level of risk violation is what would be considered as something where the strategy is still functioning correctly but has reached the limits of what it is allowed to do, and must safely liquidate and shut down. Here, the strategy is allowed to send orders and make trades that flatten the position and cancel new entry orders, if there are any. Basically, the strategy is done trading but is allowed to automatically handle the violation and finish trading until a trader checks on what happens and decides to either restart and allocate higher risk limits to the trading strategy.

The final level of risk violation is what would be considered a maximum possible risk violation, which is a violation that should never, ever happen. If a trading strategy ever triggers this risk violation, it is a sign that something went very wrong. This risk violation means that the strategy is no longer allowed to send any more order flow to the live markets. This risk violation would only be triggered during periods of extremely unexpected events, such as a flash crash market condition. This severity of risk

violation basically means that the algorithmic trading strategy is not designed to deal with such an event automatically and must freeze trading and then resort to external operators to manage open positions and live orders.

### **Differentiating the measures of risk**

Let's explore different measures of risk. We will use the trading performance from the volatility adjusted mean reversion strategy we saw in Chapter 5, *Sophisticated Algorithmic Strategies*, as an example of a trading strategy in which we wish to understand the risks behind and quantify and calibrate them.

In Chapter 5, *Sophisticated Algorithmic Trading Strategies*, we built the Mean Reversion, Volatility Adjusted Mean Reversion, Trend Following, and Volatility Adjusted Trend Following strategies. During the analysis of their performance, we wrote the results into the corresponding CSV files. These can also be found in this book's GitHub repository, https://github.com/P

[acktPublishing/Learn-Algorithmic-Trading---Fundamentals-of-Algorithmic-Trading](https://github.com/PacktPublishing/Learn-Algorithmic-Trading---Fundamentals-of-Algorithmic-Trading), or by running the volatility adjusted mean reversion strategy (volatility\_mean\_reversion.py) in Chapter 5, *Sophisticated Algorithmic Strategies*, in the *Mean Reversion Strategy that dynamically adjusts for changing volatility* section. Let's load up the trading performance .csv file, as shown in the following code block, and quickly look at what fields we have available:

```
import pandas as pd
import matplotlib.pyplot as plt
results = pd.read_csv('volatility_adjusted_mean_reversion.csv')
print(results.head(1))
```

The code will return the following output:

 Date Open High Low Close Adj Close \ 0 2014-01-02 555.647278 556.788025 552.06073 554.481689 554.481689 Volume ClosePrice Fast10DayEMA Slow40DayEMA APO Trades Position PnL 0 3656400 554.481689 554.481689 554.481689 0.0 0 0 0.0

For the purposes of implementing and quantifying risk measures, the fields we are interested in are Date, High, Low, ClosePrice, Trades, Position, and PnL. We will ignore the other fields since we do not require them for the

risk measures we are currently interested in. Now, let's dive into understanding and implementing our risk measures.

### **Stop-loss**

The first risk limit we will look at is quite intuitive and is called **stop-loss**, or **max-loss**. This limit is the maximum amount of money a strategy is allowed to lose, that is, the minimum PnL allowed. This often has a notion of a time frame for that loss, meaning stop-loss can be for a day, for a week, for a month, or for the entire lifetime of the strategy. A stop-loss with a time frame of a day means that if the strategy loses a stop-loss amount of money in a single day, it is not allowed to trade any more on that day, but can resume the next day. Similarly, for a stop-loss amount in a week, it is not allowed to trade anymore for that week, but can resume next week.

Now, let's compute stop-loss levels on a week and month for the volatility adjusted mean reversion strategy, as shown in the following code:

```
num_days = len(results.index)
pnl = results['PnL']
weekly_losses = []
monthly_losses = []
for i in range(0, num_days):
 if i >= 5 and pnl[i - 5] > pnl[i]:
 weekly_losses.append(pnl[i] - pnl[i - 5])
 if i >= 20 and pnl[i - 20] > pnl[i]:
 monthly_losses.append(pnl[i] - pnl[i - 20])
plt.hist(weekly_losses, 50)
plt.gca().set(title='Weekly Loss Distribution', xlabel='$', ylabel='Frequency')
plt.show()
plt.hist(monthly_losses, 50)
plt.gca().set(title='Monthly Loss Distribution', xlabel='$', ylabel='Frequency')
plt.show()
```

The code will return the following plots as output. Let's have a look at the weekly loss distribution plot shown here:

![](_page_98_Figure_0.jpeg)

Now, let's take a look at the monthly loss distribution plot shown here:

![](_page_99_Figure_0.jpeg)

The plots show the distribution of weekly and monthly losses. From these, we can observe the following:

- A weekly loss of anything more than \$4K and a monthly loss of anything more than \$6K is highly unexpected.
- A weekly loss of more than \$12K and a monthly loss of \$14K have never happened, so it can be considered an unprecedented event, but we will revisit this later.

### **Max drawdown**

**Max drawdown** is also a PnL metric, but this measures the maximum loss that a strategy can take over a series of days. This is defined as the peak to trough decline in a trading strategy's account value. This is important as a risk measure so that we can get an idea of what the historical maximum decline in the account value can be. This is important because we can get unlucky during the deployment of a trading strategy and run it in live markets right at the beginning of the drawdown.

Having an expectation of what the maximum drawdown is can help us understand whether the strategy loss streak is still within our expectations or whether something unprecedented is happening. Let's look at how to compute it:

```
max_pnl = 0
max_drawdown = 0
drawdown_max_pnl = 0
drawdown_min_pnl = 0
for i in range(0, num_days):
 max_pnl = max(max_pnl, pnl[i])
 drawdown = max_pnl - pnl[i]
 if drawdown > max_drawdown:
 max_drawdown = drawdown
 drawdown_max_pnl = max_pnl
 drawdown_min_pnl = pnl[i]
print('Max Drawdown:', max_drawdown)
results['PnL'].plot(x='Date', legend=True)
plt.axhline(y=drawdown_max_pnl, color='g')
plt.axhline(y=drawdown_min_pnl, color='r')
plt.show()
```

The code will return the following output:

Max Drawdown: 15340.41716347829

The plots that follow are a result of the preceding code. Let's have a look:

![](_page_101_Figure_0.jpeg)

In the plot, the max drawdown occurs roughly during the middle of this PnL series, with the maximum PnL being 37K and the minimum PnL after that high being 22K, causing the maximum drawdown achieved to be roughly 15K:

![](_page_101_Figure_2.jpeg)

The plot is simply the same plot as before but zoomed in to the exact observations where the drawdown occurs. As we mentioned previously, after achieving a high of roughly 37K, PnLs have a large drawdown of 15K and drop down to roughly 22K, before rebounding.

### **Position limits**

**Position limits** are also quite straightforward and intuitive to understand. It is simply the maximum position, long or short, that the strategy should have at any point in its trading lifetime. It is possible to have two different position limits, one for the maximum long position and another for the maximum short position, which can be useful, for instance, where shorting stocks have different rules/risks associated with them than being long on stocks does. Every unit of open position has a risk associated with it. Generally, the larger the position a strategy puts on, the larger the risk associated with it. So, the best strategies are the ones that can make money while getting into as small a position as possible. In either case, before a strategy is deployed to production, it is important to quantify and estimate what the maximum positions the strategy can get into, based on historical performance, so that we can find out when a strategy is within its normal behavior parameters and when it is outside of historical norms.

Finding the maximum position is straightforward. Let's find a quick distribution of the positions with the help of the following code:

```
position = results['Position']
plt.hist(position, 20)
plt.gca().set(title='Position Distribution', xlabel='Shares', ylabel='Frequency')
plt.show()
```

The preceding code will generate the following output. Let's have a look at the position distribution chart:

![](_page_104_Figure_0.jpeg)

We can see the following from the preceding chart:

- For this trading strategy, which has been applied to Google stock data, the strategy is unlikely to have a position exceeding 200 shares and has never had a position exceeding 250.
- If it gets into position levels exceeding 250, we should be careful that the trading strategy is still performing as expected.

### **Position holding time**

While analyzing positions that a trading strategy gets into, it is also important to measure how long a position stays open until it is closed and returned to its flat position or opposition position. The longer a position stays open, the more risk it is taking on, because the more time there is for markets to make massive moves that can potentially go against the open position. A long position is initiated when the position goes from being short or flat to being long and is closed when the position goes back to flat or short. Similarly, short positions are initiated when the position goes from being long or flat to being short and is closed when the position goes back to flat or long.

Now, let's find the distribution of open position durations with the help of the following code:

```
position_holding_times = []
current_pos = 0
current_pos_start = 0
for i in range(0, num_days):
 pos = results['Position'].iloc[i]
 # flat and starting a new position
 if current_pos == 0:
 if pos != 0:
 current_pos = pos
 current_pos_start = i
 continue
 # going from long position to flat or short position or
 # going from short position to flat or long position
 if current_pos * pos <= 0:
 current_pos = pos
 position_holding_times.append(i - current_pos_start)
 current_pos_start = i
print(position_holding_times)
plt.hist(position_holding_times, 100)
plt.gca().set(title='Position Holding Time Distribution', xlabel='Holding time days', ylabel='Frequency')
plt.show()
```

The preceding code will return the following output. Let's have a look at the position holding time distribution plot:

![](_page_106_Figure_0.jpeg)

So, for this strategy, we can see that the holding time is pretty distributed, with the longest one lasting around 115 days and the shortest one lasting around 3 days.

### **Variance of PnLs**

We need to measure how much the PnLs can vary from day to day or even week to week. This is an important measure of risk because if a trading strategy has large swings in PnLs, the account value is very volatile and it is hard to run a trading strategy with such a profile. Often, we compute the Standard Deviation of returns over different days or weeks or whatever timeframe we choose to use as our investment time horizon. Most optimization methods try to find optimal trading performance as a balance between PnLs and the Standard Deviation of returns.

Computing the standard deviation of returns is easy. Let's compute the standard deviation of weekly returns, as shown in the following code:

```
last_week = 0
weekly_pnls = []
for i in range(0, num_days):
 if i - last_week >= 5:
 weekly_pnls.append(pnl[i] - pnl[last_week])
 last_week = i
from statistics import stdev
print('Weekly PnL Standard Deviation:', stdev(weekly_pnls))
plt.hist(weekly_pnls, 50)
plt.gca().set(title='Weekly PnL Distribution', xlabel='$', ylabel='Frequency')
plt.show()
```

The preceding code will return the following output:

Weekly PnL Standard Deviation: 1995.1834727008127

The following plot shows the weekly PnL distribution that was created from the preceding code:

![](_page_108_Figure_0.jpeg)

We can see that the weekly PnLs are close to being normally distributed around a mean of \$0, which intuitively makes sense. The distribution is right skewed, which yields the positive cumulative PnLs for this trading strategy. There are some very large profits and losses for some weeks, but they are very rare, which is also within the expectations of what the distribution should look like.

### **Sharpe ratio**

**Sharpe ratio** is a very commonly used performance and risk metric that's used in the industry to measure and compare the performance of algorithmic trading strategies. Sharpe ratio is defined as the ratio of average PnL over a period of time and the PnL standard deviation over the same period. The benefit of the Sharpe ratio is that it captures the profitability of a trading strategy while also accounting for the risk by using the volatility of the returns. Let's have a look at the mathematical representation:

$$\begin{aligned} SharpeRatio = \frac{AvgDailyPnl}{StandardDeviationOfDailyPnls} \ AvgDailyPnl = \frac{\sum_{i=1}^{N} Pnl_i}{N} \ StandardDeviationOfPnls = \frac{\sum_{i=1}^{N} (Pnl_i - AvgDailyPnl)^2}{N} \end{aligned}$$

Here, we have the following:

- : PnL on the trading day.
- : Number of trading days over which this Sharpe is being computed.

Another performance and risk measure similar to the Sharpe ratio is known as the Sortino ratio, which only uses observations where the trading strategy loses money and ignores the ones where the trading strategy makes money. The simple idea is that, for a trading strategy, Sharpe upside moves in PnLs are a good thing, so they should not be considered when computing the standard deviation. Another way to say the same thing would be that only downside moves or losses are actual risk observations.

Let's compute the Sharpe and Sortino ratios for our trading strategy. We will use a week as the time horizon for our trading strategy:

```
last_week = 0
weekly_pnls = []
weekly_losses = []
for i in range(0, num_days):
 if i - last_week >= 5:
 pnl_change = pnl[i] - pnl[last_week]
 weekly_pnls.append(pnl_change)
 if pnl_change < 0:
 weekly_losses.append(pnl_change)
 last_week = i
from statistics import stdev, mean
sharpe_ratio = mean(weekly_pnls) / stdev(weekly_pnls)
sortino_ratio = mean(weekly_pnls) / stdev(weekly_losses)
print('Sharpe ratio:', sharpe_ratio)
print('Sortino ratio:', sortino_ratio)
```

The preceding code will return the following output:

```
Sharpe ratio: 0.09494748065583607
Sortino ratio: 0.11925614548156238
```

Here, we can see that the Sharpe ratio and the Sortino ratio are close to each other, which is what we expect since both are risk-adjusted return metrics. The Sortino ratio is slightly higher than the Sharpe ratio, which also makes sense since, by definition, the Sortino ratio does not consider large increases in PnLs as being contributions to the drawdown/risk for the trading strategy, indicating that the Sharpe ratio was, in fact, penalizing some large +ve jumps in PnLs.

### **Maximum executions per period**

This risk measure is an interval-based risk check. An interval-based risk is a counter that resets after a fixed amount of time and the risk check is imposed within such a time slice. So, while there is no final limit, it's important that the limit isn't exceeded within the time interval that is meant to detect and avoid over-trading. The interval-based risk measure we will inspect is maximum executions per period. This measures the maximum number of trades allowed in a given timeframe. Then, at the end of the timeframe, the counter is reset and starts over. This would detect and prevent a runaway strategy that buys and sells at a very fast pace.

Let's look at the distribution of executions per period for our strategy using a week as our timeframe, as shown here:

```
executions_this_week = 0
executions_per_week = []
last_week = 0
for i in range(0, num_days):
 if results['Trades'].iloc[i] != 0:
 executions_this_week += 1
 if i - last_week >= 5:
 executions_per_week.append(executions_this_week)
 executions_this_week = 0
 last_week = i
plt.hist(executions_per_week, 10)
plt.gca().set(title='Weekly number of executions Distribution', xlabel='Number of executions', ylabel='Frequency')
plt.show()
```

The code will return the following output. Let's have a look at the plot:

![](_page_111_Figure_5.jpeg)

As we can see, for this trading strategy, it's never traded more than five times a week in the past, which is when it trades every day of the week, which doesn't help us much. Now, let's look at the maximum executions per month:

```
executions_this_month = 0
executions_per_month = []
last_month = 0
for i in range(0, num_days):
 if results['Trades'].iloc[i] != 0:
 executions_this_month += 1
```

```
 if i - last_month >= 20:
 executions_per_month.append(executions_this_month)
 executions_this_month = 0
 last_month = i
plt.hist(executions_per_month, 20)
plt.gca().set(title='Monthly number of executions Distribution', xlabel='Number of executions', ylabel='Frequency')
plt.show()
```

The preceding code will return the following output. Let's have a look at the plot:

![](_page_112_Figure_2.jpeg)

We can observe the following from the preceding plot:

- It is possible for the strategy to trade every day in a month, so this risk measure can't really be used for this strategy.
- However, this is still an important risk measure to understand and calibrate, especially for algorithmic trading strategies that trade frequently, and especially for HFT strategies.

### **Maximum trade size**

This risk metric measures what the maximum possible trade size for a single trade for the trading strategy is. In our previous examples, we use static trade sizes, but it is not very difficult to build a trading strategy that sends a larger order when the trading signal is stronger and a smaller order when the trading signal is weaker. Alternatively, a strategy can choose to liquidate a larger than normal position in one trade if it's profitable, in which case it will send out a pretty large order. This risk measure is also very helpful when the trading strategy is a gray box trading strategy as it prevents fat-finger errors, among other things. We will skip implementing this risk measure here, but all we do is find a distribution of per trade size, which should be straightforward to implement based on our implementation of previous risk measures.

### **Volume limits**

This risk metric measures the traded volume, which can also have an intervalbased variant that measures volume per period. This is another risk measure that is meant to detect and prevent overtrading. For example, some of the catastrophic software implementation bugs we discussed in this chapter could've been prevented if they had a tight volume limit in place that warned operators about risk violations and possibly a volume limit that shut down trading strategies. Let's observe the traded volume for our strategy, which is shown in the following code:

```
traded_volume = 0
for i in range(0, num_days):
 if results['Trades'].iloc[i] != 0:
 traded_volume += abs(results['Position'].iloc[i] - results['Position'].iloc[i-1])
print('Total traded volume:', traded_volume)
```

The preceding code will return the following output:

Total traded volume: 4050

In this case, the strategy behavior is as expected, that is, no overtrading is detected. We can use this to calibrate what total traded volume to expect from this strategy when it is deployed to live markets. If it ever trades significantly more than what is expected, we can detect that to be an over-trading condition.

#### **Making a risk management algorithm**

By now, we're aware of the different types of risks and factors, including the risks in a trading strategy and the most common risk metrics for algorithmic trading strategies. Now, let's have a look at incorporating these risk measures into our volatility adjusted mean reversion trading strategy to make it safer before deploying it into live markets. We will set the risk limits to 150% of the maximum achieved historically. We are doing this because it is possible that there is a day in the future that is very different from what we've seen historically. Let's get started:

1. Let's define our risk limits, which we are not allowed to breach. As we discussed previously, it will be set to 150% of the historically observed maximums:

```
# Risk limits
RISK_LIMIT_WEEKLY_STOP_LOSS = -12000 * 1.5
RISK_LIMIT_MONTHLY_STOP_LOSS = -14000 * 1.5
RISK_LIMIT_MAX_POSITION = 250 * 1.5
RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS = 120 * 1.5
RISK_LIMIT_MAX_TRADE_SIZE = 10 * 1.5
RISK_LIMIT_MAX_TRADED_VOLUME = 4000 * 1.5
```

2. We will maintain some variables to track and check for risk violations with the help of the following code:

```
risk_violated = False
traded_volume = 0
current_pos = 0
current_pos_start = 0
```

3. As we can see, we have some code for computing the Simple Moving Average and Standard Deviation for volatility adjustments. We will compute the fast and slow EMAs and the APO value, which we can use as our mean reversion trading signal:

```
close = data['Close']
for close_price in close:
 price_history.append(close_price)
 if len(price_history) > SMA_NUM_PERIODS: # we track at most 'time_period' number of prices
 del (price_history[0])
 sma = stats.mean(price_history)
 variance = 0 # variance is square of standard deviation
 for hist_price in price_history:
 variance = variance + ((hist_price - sma) ** 2)
 stdev = math.sqrt(variance / len(price_history))
 stdev_factor = stdev / 15
 if stdev_factor == 0:
 stdev_factor = 1
 # This section updates fast and slow EMA and computes APO trading signal
 if (ema_fast == 0): # first observation
 ema_fast = close_price
 ema_slow = close_price
 else:
 ema_fast = (close_price - ema_fast) * K_FAST * stdev_factor + ema_fast
 ema_slow = (close_price - ema_slow) * K_SLOW * stdev_factor + ema_slow
 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 apo = ema_fast - ema_slow
 apo_values.append(apo)
```

4. Now, before we can evaluate our signal and check whether we can send an order out, we need to perform a risk check to ensure that the trade size we may attempt is within MAX\_TRADE\_SIZE limits:

```
 if NUM_SHARES_PER_TRADE > RISK_LIMIT_MAX_TRADE_SIZE:
 print('RiskViolation NUM_SHARES_PER_TRADE', NUM_SHARES_PER_TRADE, ' > RISK_LIMIT_MAX_TRADE_SIZE', RISK_LIMIT_MAX_TR
 risk_violated = True
```

5. Now, the next section checks the trading signal to see if we should send orders as usual. However, with an additional check, that would prevent the orders from going out if risk limits have been violated. Let's look at the changes that we need to make to the sell trades:

 # We will perform a sell trade at close\_price if the following conditions are met: # 1. The APO trading signal value is above Sell-Entry threshold and the difference between last trade-price and curre # 2. We are long( +ve position ) and either APO trading signal value is at or above 0 or current position is profitab if (not risk\_violated and ((apo > APO\_VALUE\_FOR\_SELL\_ENTRY \* stdev\_factor and abs(close\_price - last\_sell\_price) > MIN\_PRICE\_MOVE\_FROM\_LAST or (position > 0 and (apo >= 0 or open\_pnl > MIN\_PROFIT\_TO\_CLOSE / stdev\_factor)))): # long from -ve APO and APO ha orders.append(-1) # mark the sell trade last\_sell\_price = close\_price position -= NUM\_SHARES\_PER\_TRADE # reduce position by the size of this trade sell\_sum\_price\_qty += (close\_price \* NUM\_SHARES\_PER\_TRADE) # update vwap sell-price sell\_sum\_qty += NUM\_SHARES\_PER\_TRADE traded\_volume += NUM\_SHARES\_PER\_TRADE print("Sell ", NUM\_SHARES\_PER\_TRADE, " @ ", close\_price, "Position: ", position)

#### Similarly, let's look at the buy trade logic:

```
 # We will perform a buy trade at close_price if the following conditions are met:
 # 1. The APO trading signal value is below Buy-Entry threshold and the difference between last trade-price and curren
 # 2. We are short( -ve position ) and either APO trading signal value is at or below 0 or current position is profita
 elif (not risk_violated and
 ((apo < APO_VALUE_FOR_BUY_ENTRY * stdev_factor and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FROM_LAST
 or
 (position < 0 and (apo <= 0 or open_pnl > MIN_PROFIT_TO_CLOSE / stdev_factor)))): # short from +ve APO and APO
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 position += NUM_SHARES_PER_TRADE # increase position by the size of this trade
 buy_sum_price_qty += (close_price * NUM_SHARES_PER_TRADE) # update the vwap buy-price
 buy_sum_qty += NUM_SHARES_PER_TRADE
 traded_volume += NUM_SHARES_PER_TRADE
 print("Buy ", NUM_SHARES_PER_TRADE, " @ ", close_price, "Position: ", position)
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
 positions.append(position)
```

6. Now, we will check that, after any potential orders have been sent out and trades have been made this round, we haven't breached any of our risk limits, starting with the Maximum Position Holding Time risk limit. Let's have a look at the following code:

```
 # flat and starting a new position
 if current_pos == 0:
 if position != 0:
 current_pos = position
 current_pos_start = len(positions)
 continue
 # going from long position to flat or short position or
 # going from short position to flat or long position
 if current_pos * position <= 0:
 current_pos = position
 position_holding_time = len(positions) - current_pos_start
 current_pos_start = len(positions)
 if position_holding_time > RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS:
 print('RiskViolation position_holding_time', position_holding_time, ' > RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS
 risk_violated = True
```

7. We will check that the new long/short position is within the Max Position risk limits, as shown in the following code:

```
 if abs(position) > RISK_LIMIT_MAX_POSITION:
 print('RiskViolation position', position, ' > RISK_LIMIT_MAX_POSITION', RISK_LIMIT_MAX_POSITION)
 risk_violated = True
```

8. Next, we also check that the updated traded volume doesn't violate the allocated Maximum Traded Volume risk limit:

```
 if traded_volume > RISK_LIMIT_MAX_TRADED_VOLUME:
 print('RiskViolation traded_volume', traded_volume, ' > RISK_LIMIT_MAX_TRADED_VOLUME', RISK_LIMIT_MAX_TRADED_VOLUME
 risk_violated = True
```

9. Next, we will write some code that updates the PnLs, unchanged from before:

```
 open_pnl = 0
 if position > 0:
 if sell_sum_qty > 0:
 open_pnl = abs(sell_sum_qty) * (sell_sum_price_qty / sell_sum_qty - buy_sum_price_qty / buy_sum_qty)
 open_pnl += abs(sell_sum_qty - position) * (close_price - buy_sum_price_qty / buy_sum_qty)
 elif position < 0:
 if buy_sum_qty > 0:
```

```
 open_pnl = abs(buy_sum_qty) * (sell_sum_price_qty / sell_sum_qty - buy_sum_price_qty / buy_sum_qty)
 open_pnl += abs(buy_sum_qty - position) * (sell_sum_price_qty / sell_sum_qty - close_price)
 else:
 closed_pnl += (sell_sum_price_qty - buy_sum_price_qty)
 buy_sum_price_qty = 0
 buy_sum_qty = 0
 sell_sum_price_qty = 0
 sell_sum_qty = 0
 last_buy_price = 0
 last_sell_price = 0
 print("OpenPnL: ", open_pnl, " ClosedPnL: ", closed_pnl, " TotalPnL: ", (open_pnl + closed_pnl))
 pnls.append(closed_pnl + open_pnl)
```

10. Now, we need to write the following code, which checks that the new Total PnL, which is the sum of realized and un-realized PnLs, is not in violation of either the Maximum allowed Weekly Stop Loss limit or the Maximum allowed Monthly Stop Loss limit:

```
 if len(pnls) > 5:
 weekly_loss = pnls[-1] - pnls[-6]
 if weekly_loss < RISK_LIMIT_WEEKLY_STOP_LOSS:
 print('RiskViolation weekly_loss', weekly_loss, ' < RISK_LIMIT_WEEKLY_STOP_LOSS', RISK_LIMIT_WEEKLY_STOP_LOSS)
 risk_violated = True
 if len(pnls) > 20:
 monthly_loss = pnls[-1] - pnls[-21]
 if monthly_loss < RISK_LIMIT_MONTHLY_STOP_LOSS:
 print('RiskViolation monthly_loss', monthly_loss, ' < RISK_LIMIT_MONTHLY_STOP_LOSS', RISK_LIMIT_MONTHLY_STOP_LOSS
 risk_violated = True
```

Here, we have added a robust risk management system to our existing trading strategy that can be extended to any other trading strategies we intend on deploying to live trading markets in the future. This will protect live trading strategies from going rogue in production or behaving outside of our expected parameters, hence providing great risk control over our trading strategies.

#### **Realistically adjusting risk**

In the risk management system we built in the previous section, we used static risk limits that we used for the duration of the strategy's lifetime. In practice, however, this is never the case. When a new algorithmic trading strategy is built and deployed, it is first deployed with very low-risk limits—usually the least amount of risk possible. This is for a variety of reasons, the first one being to make tests and work out software implementation bugs, if there are any. The larger the amount of new code being deployed to live markets, the greater the risk. The other reason is to make sure strategy behavior is consistent with what is expected based on historical performance analysis. It is usually monitored very closely by multiple people to make sure nothing unexpected happens. Then, after a couple of days or weeks, when initial bugs have been worked out and strategy performance is in line with simulation performance, it is slowly scaled up to take more risks in order to generate more profits.

Conversely, after a strategy goes through a bad patch of losses, it is often reevaluated at reduced risk limits to check whether the trading strategy's performance has degraded from historical expectations and if it is no longer profitable to deploy it in live markets anymore. The obvious objective is to make as much money as possible, but achieving that requires not only a good risk check system but also a good system to adjust risk through different PnL profiles in the lifetime of the strategy.

A simple intuitive approach to adjusting risk in trading can be to start with low risk, increase the risk slightly after a good performance, and reduce the risk slightly after a poor performance. This is generally the approach that's followed by most participants: the challenges are to quantify good/poor performance in order to increase/decrease risk and to quantify the amount by which to increase/decrease risk.

Let's look at a practical implementation using our previous volatility adjusted mean reversion strategy with risk checks. We will increase the trade size and risk after a good month and reduce the trade size and risk after a bad month by a small increment. Let's get started:

1. First, we will define the limits of how small a trade size can be and what the maximum allowed trade size can be over the course of the strategy's lifetime. For this implementation, we allow no less than 1 share per trade and no more than 50 per trade. Every time we have a good/bad month, we will increase/decrease the trade size by 2 shares. We will start very small, as we discussed previously, and increment slowly if we continue to do well. Let's have a look at the code:

```
MIN_NUM_SHARES_PER_TRADE = 1
MAX_NUM_SHARES_PER_TRADE = 50
INCREMENT_NUM_SHARES_PER_TRADE = 2
num_shares_per_trade = MIN_NUM_SHARES_PER_TRADE # Beginning number of shares to buy/sell on every trade
num_shares_history = [] # history of num-shares
abs_position_history = [] # history of absolute-position
```

2. Next, we will define similar minimum, maximum, and increment values for the different risk limits. As the strategy trade size evolves over time, the risk limits will also have to be adjusted to accommodate the increased trading size:

```
# Risk limits and increments to risk limits when we have good/bad months
risk_limit_weekly_stop_loss = -6000
INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS = -12000
risk_limit_monthly_stop_loss = -15000
INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS = -30000
risk_limit_max_position = 5
INCREMENT_RISK_LIMIT_MAX_POSITION = 3
max_position_history = [] # history of max-trade-size
RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS = 120 * 5
risk_limit_max_trade_size = 5
INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE = 2
max_trade_size_history = [] # history of max-trade-size
last_risk_change_index = 0
```

3. Now, let's look at the main loop trading section. We will only look at the sections that are different from the previous strategy, along with risk checks. Now, the minimum profit to close is no longer a constant but is a

function of the number of shares per trade, which varies over time:

- MIN\_PROFIT\_TO\_CLOSE = num\_shares\_per\_trade \* 10
- 4. Let's have a look at the main trading section. It will require some changes so that it adapts to the changing trade sizes. Let's look at the sell trade logic first:

```
 if (not risk_violated and
 ((apo > APO_VALUE_FOR_SELL_ENTRY * stdev_factor and abs(close_price - last_sell_price) > MIN_PRICE_MOVE_FROM_LAST
 or
 (position > 0 and (apo >= 0 or open_pnl > MIN_PROFIT_TO_CLOSE / stdev_factor)))): # long from -ve APO and APO ha
 orders.append(-1) # mark the sell trade
 last_sell_price = close_price
 if position == 0: # opening a new entry position
 position -= num_shares_per_trade # reduce position by the size of this trade
 sell_sum_price_qty += (close_price * num_shares_per_trade) # update vwap sell-price
 sell_sum_qty += num_shares_per_trade
 traded_volume += num_shares_per_trade
 print("Sell ", num_shares_per_trade, " @ ", close_price, "Position: ", position)
 else: # closing an existing position
 sell_sum_price_qty += (close_price * abs(position)) # update vwap sell-price
 sell_sum_qty += abs(position)
 traded_volume += abs(position)
 print("Sell ", abs(position), " @ ", close_price, "Position: ", position)
 position = 0 # reduce position by the size of this trade
```

Finally, let's look at the buy trade logic:

```
 elif (not risk_violated and
 ((apo < APO_VALUE_FOR_BUY_ENTRY * stdev_factor and abs(close_price - last_buy_price) > MIN_PRICE_MOVE_FROM_LAST
 or
 (position < 0 and (apo <= 0 or open_pnl > MIN_PROFIT_TO_CLOSE / stdev_factor)))): # short from +ve APO and APO
 orders.append(+1) # mark the buy trade
 last_buy_price = close_price
 if position == 0: # opening a new entry position
 position += num_shares_per_trade # increase position by the size of this trade
 buy_sum_price_qty += (close_price * num_shares_per_trade) # update the vwap buy-price
 buy_sum_qty += num_shares_per_trade
 traded_volume += num_shares_per_trade
 print("Buy ", num_shares_per_trade, " @ ", close_price, "Position: ", position)
 else: # closing an existing position
 buy_sum_price_qty += (close_price * abs(position)) # update the vwap buy-price
 buy_sum_qty += abs(position)
 traded_volume += abs(position)
 print("Buy ", abs(position), " @ ", close_price, "Position: ", position)
 position = 0 # increase position by the size of this trade
 else:
 # No trade since none of the conditions were met to buy or sell
 orders.append(0)
```

```
 positions.append(position)
```

5. After adjusting the PnLs, as shown in the preceding code, we will add an implementation to analyze monthly performance and increase trade size and risk limits if we had a good month and decrease trade size and risk limits if we had a bad month. First, we will look at the logic to increase the trading risk after a good month of performance:

```
 if len(pnls) > 20:
 monthly_pnls = pnls[-1] - pnls[-20]
 if len(pnls) - last_risk_change_index > 20:
 if monthly_pnls > 0:
 num_shares_per_trade += INCREMENT_NUM_SHARES_PER_TRADE
 if num_shares_per_trade <= MAX_NUM_SHARES_PER_TRADE:
 print('Increasing trade-size and risk')
 risk_limit_weekly_stop_loss += INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS
 risk_limit_monthly_stop_loss += INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS
 risk_limit_max_position += INCREMENT_RISK_LIMIT_MAX_POSITION
 risk_limit_max_trade_size += INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE
 else:
 num_shares_per_trade = MAX_NUM_SHARES_PER_TRADE
```

6. Now, let's look at some similar logic, but which reduces risk after a month of poor performance:

```
 elif monthly_pnls < 0:
 num_shares_per_trade -= INCREMENT_NUM_SHARES_PER_TRADE
 if num_shares_per_trade >= MIN_NUM_SHARES_PER_TRADE:
 print('Decreasing trade-size and risk')
 risk_limit_weekly_stop_loss -= INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS
 risk_limit_monthly_stop_loss -= INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS
 risk_limit_max_position -= INCREMENT_RISK_LIMIT_MAX_POSITION
 risk_limit_max_trade_size -= INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE
```

```
 else:
 num_shares_per_trade = MIN_NUM_SHARES_PER_TRADE
 last_risk_change_index = len(pnls)
```

7. Now, we need to look at the code to track the risk exposure evolution over time:

```
 # Track trade-sizes/positions and risk limits as they evolve over time
 num_shares_history.append(num_shares_per_trade)
 abs_position_history.append(abs(position))
 max_trade_size_history.append(risk_limit_max_trade_size)
 max_position_history.append(risk_limit_max_position)
```

8. Finally, let's visualize the performance and the evolution of trade sizes and risk limits over time:

```
data = data.assign(NumShares=pd.Series(num_shares_history, index=data.index))
data = data.assign(MaxTradeSize=pd.Series(max_trade_size_history, index=data.index))
data = data.assign(AbsPosition=pd.Series(abs_position_history, index=data.index))
data = data.assign(MaxPosition=pd.Series(max_position_history, index=data.index))
data['NumShares'].plot(color='b', lw=3., legend=True)
data['MaxTradeSize'].plot(color='g', lw=1., legend=True)
plt.legend()
plt.show()
data['AbsPosition'].plot(color='b', lw=1., legend=True)
data['MaxPosition'].plot(color='g', lw=1., legend=True)
plt.legend()
plt.show()
```

The following plots are the output of the preceding code. Let's have a look at the visualizations that we are already familiar with:

![](_page_120_Figure_6.jpeg)

The plot that shows buy and sell trades overlaid on Google stock prices still stay consistent with what we've seen in the past, which shows that strategy behavior remains mostly unchanged as it goes through phases of risk increases and decreases:

![](_page_120_Figure_8.jpeg)

The buy and sell trades that are overlaid on APO signal value changes also stay consistent with the expected strategy behavior, which we're used to from our previous analysis of mean reversion trading strategy:

![](_page_121_Figure_1.jpeg)

As shown in the preceding plot, the position plot is especially interesting because it shows how the magnitude of the positions increases over time. Initially, they are very small (less than 10 shares) and slowly increase over time as strategy performance stays consistently good and becomes quite large (more than 40 shares):

![](_page_121_Figure_3.jpeg)

As shown in the preceding plot, the PnL plot is also quite interesting and reflects what we would expect it to show. It slowly increases initially when we are trading small sizes and over time, the trading sizes increase and the PnLs increase much faster with the larger trade size and risk limits:

![](_page_121_Figure_5.jpeg)

As shown in the preceding plot, the trade size and max trade size risk limit evolution plot shows that, initially, we start with 1 share per trade, then increase it slowly when we have a positive month, then decrease it slowly when we have a negative month. Around 2016, the strategy gets into a streak of consecutively profitable months and causes the trade size to increase every month:

![](_page_122_Figure_1.jpeg)

As shown in the preceding plot, the absolute positions that the strategy puts on, as well as the max position risk limit evolution plot, stay consistent with expectations, that is, starting low and then increasing as we get into a streak of consecutive good months.

### **Summary**

In this chapter, you learned about the different types of risks and risk factors. Then, we went through the sources of risk and learned about quantifying the risks. Moving ahead, we also learned about how to measure and manage the risks (market risk, operational risk, and software implementation bugs) of algorithmic strategies. We incorporated a full production-ready risk management system into our previously built trading strategy, thus making them safe for deployment to live trading markets. Finally, we discussed and built a practical risk scaling system that starts with very low-risk exposure and dynamically manages the risk exposure over time as the strategy performance evolves.

In the next chapter, we will look at how the algorithm's trading interacts with the different factors in the trading arena. You will learn how to build a trading bot from scratch. Using the algorithm that we will build in the prior sections, you will know how to implement it, where to connect it, and how to handle it.
## Chapter 29

# Supervised Learning for Intraday Returns Prediction using QSTrader

All of the trading strategies discussed in the book so far using QSTrader have been carried out on daily OHLCV "bar" equities data. In this chapter an intraday strategy is backtested. A predictive machine learning based algorithm is outlined and implemented, which attempts to predict directional changes of minutely equities returns.

The chapter begins with a discussion of prediction goals for asset pricing data and the issues associated with classification class imbalance, which is a common situation in quantitative finance returns prediction.

Attention then turns towards building a predictive model using the Python Scikit-Learn library with a variety of machine learning based classifiers. Certain convenience functions are presented that aid such models in an intraday "online" environment.

The implementation of a Strategy class and Backtest script is presented that provides the full code for testing such a predictive model. The code is relatively straightforward and encourages significant experimentation through parameter tweaking and modification of the asset universe.

Finally backtested results are presented for a particular statistical ensemeble technique–the Random Forest classifier–on an individual equity, AREX, for the period 2013-2014, trained on data from 2007-2012.

Note that the full code is presented at the end of the chapter. It requires a working installation of the latest version of QSTrader, which can be found at the [Github project page.](https://github.com/mhallsmoore/qstrader.git)

#### 29.1 Prediction Goals with Machine Learning

In this chapter the main focus is on using supervised machine learning to make predictions about asset price directional changes. These methods have been covered before on QuantStart.com and in previous books, but they have not been placed into a robust intraday event-driven backtest system as of yet. This chapter changes that.

The first task is to determine exactly what is being predicted. There are a few of examples to consider:

• Direction - Predict the directional change of the returns of an equity in the next bar

- Short-Term Trend Predict multiple periods ahead for a set of equity returns, across a large range of assets
- Up/Down Factor Predict which equities will rise by a certain factor and not drop by another factor, over a set of future bars (e.g. 5 mins)

It is not too challenging to come up with many other examples of such predictions. In this chapter the first and third will be utilised in order to demonstrate intraday functionality.

#### 29.1.1 Class Imbalance

A substantial difficulty with making predictions in a quantitative finance setting is that they often lead to a situation of class imbalance.

Consider the third example above. There are very few instances of equities that rise at least by a certain specific factor and do not decrease by another specific factor, compared to more common patterns. Consider for example a rise of at least 2% with a decrease of no more than 1% over the next five bars, say.

If this "up/down factor" is formulated as a supervised binary classification problem, where a set of lagged bars are used as features and subsequent bars are designated as "up/down factor" bars, then the amount of bars which are not "up/down factor" bars will significantly outnumber the quantity which are.

This often manifests itself via models that simply predict the class label with the largest class size. The classification accuracy, or Hit Rate, then simply reflects the ratio of the class imbalance itself rather than correct prediction accuracy on each class.

Thankfully identification of this problem is straightforward. A confusion matrix can be calculated, which identifies true positives and true negatives along with the false positive (Type I error) and false negative (Type II error). This will clearly highlight class imbalance due to the fact that the true positive and false negative values will contain a very high proportion of the samples.

For instance, in the following binary classification problem output a respectable (for quantitative finance!) hit-rate of 58% has been achieved. However it is clear this is simply an artifact of the classifier choosing one value almost exclusively over another. This can be seen from the fact that the majority of samples are clustered on the top row:

#### Hit-Rate: 0.5885 [[48067 33618] [ 203 293]]

Many solutions exist to mitigate against this problem. It is beyond the scope of this chapter to discuss them all at length here. Common tactics include sampling more data (often tricky in quant finance settings with only one "history") and reducing the samples in the larger class to more evenly balance the class sizes.

Further compounding the issue for time series work is the serial correlation of the series. This means that each bar "sample" is not independent and identically distributed (iid) and hence cannot be easily removed from the larger class in a random sampling manner.

It is always necessary to use a confusion matrix to check that the class imbalance problem is not too severe, otherwise any deployed machine learning model attached to a trading engine will likely generate significant losses.

### 29.2 Building a Prediction Model on Historical Data

In this section a prediction model will be created using Scikit-Learn. As this is a supervised machine learning task the model is trained on a subset of the historical data. In particular data for the US equity AREX is used from late 2007 until the end of 2012, although the method will work with any intraday bar data (including equities and forex).

In order to train the model it is necessary to specify the feature predictors and the response. The features in this instance are lagged minutely returns. Feature p is the pth bar closing price return behind the current bar's closing price return. The response is either the "up/down factor" as described above (+1 or -1 for True/False) or the directional change of the returns in the next bar (+1 or -1 for up/down).

The code below generates both the "up/down factor" and the directional change, but in the trading strategy below the directional change is used as the response. It is straightforward to uncomment a line in the following snippets in order to change this to the "up/down factor" but this comes at the price of increased class imbalance. There are fewer instances of the stock going up by a certain factor and not down by another, compared to simple directional prediction.

Once the model is trained it is then serialised. This means that the Python object containing the model itself, along with its associated set of trained parameters, is written to disk in a special format. This allows the model to be deserialised in the QSTrader environment. This is known as pickling within the Python ecosystem.

Pickling is a common mechanism for deploying machine learning models into production. Scikit-Learn calls this model persistence. It provides a module called joblib for this purpose.

The first task in the code is to import the necessary libraries, including NumPy, Pandas and Scikit-Learn. For this example the LinearDiscriminantAnalysis and RandomForestClassifier are trained, but some other ensemble methods have also been imported and commented out. These can be uncommented and trained if other predictive models are desired. Finally joblib is imported for persistence and the confusion\_matrix is imported to analyse class imbalance:

# intraday\_ml\_model\_fit.py

```
import datetime
import numpy as np
import pandas as pd
import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import (
    BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
)
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

The following function create\_up\_down\_dataframe is a little complex. It is designed to create the necessary feature matrix X and the response vector y, although it concatenates them into the same Pandas DataFrame initially.

It takes the CSV file path as an input, along with the historical minutely price lags to use as features, with the future minutely lags to use as responses. The up\_down\_factor and percent\_factor control the ratio of how much a stock must go up and not go down by in the lookforward\_minutes range.

For example, if up\_down\_factor=2.0 and percent\_factor=0.01, this DataFrame will produce a column of +1 and -1 values, where +1 indicates bars for which in the next lookforward\_minutes the returns exceed at least 2% and do not reduce by more than 1%. Hence it is searching for instances where the stock is likely to increase twice as much as it is to decrease.

The function begins with reading the CSV file into Pandas. It sets the column names and index. It also parses the dates:

```
def create_up_down_dataframe(
```

```
csv_filepath,
lookback_minutes=30,
lookforward_minutes=5,
up_down_factor=2.0,
percent_factor=0.01,
start=None, end=None
```

):

"""

Creates a Pandas DataFrame that imports and calculates the percentage returns of an intraday OLHC ticker from disk.

'lookback\_minutes' of prior returns are stored to create a feature vector, while 'lookforward\_minutes' are used to ascertain how far in the future to predict across.

The actual prediction is to determine whether a ticker moves up by at least 'up\_down\_factor' x 'percent\_factor', while not dropping below 'percent\_factor' in the same period.

i.e. Does the stock move up 1% in a minute and not down by 0.5%?

```
The DataFrame will consist of 'lookback_minutes' columns for feature
vectors and one column for whether the stock adheres to the "up/down"
rule, which is 1 if True or 0 if False for each minute.
"""
ts = pd.read_csv(
    csv_filepath,
    names=[
        "Timestamp", "Open", "Low", "High",
        "Close", "Volume", "OpenInterest"
    ],
    index_col="Timestamp", parse_dates=True
)
```

The next steps consist of filtering the DataFrame via starting and ending dates as well as dropping the non-essential columns. The shift method is used to create all of the future and historical minutely lags. The rows with generated NaN values are dropped. All of the prices are then converted into returns using the pct\_change method. Once again the rows with generated NaN values are dropped:

```
# Filter on start/end dates
if start is not None:
    ts = ts[ts.index >= start]
if end is not None:
    ts = ts[ts.index <= end]
# Drop the non-essential columns
ts.drop(
    [
        "Open", "Low", "High",
        "Volume", "OpenInterest"
    ],
    axis=1, inplace=True
)
# Create the lookback and lookforward shifts
for i in range(0, lookback_minutes):
    ts["Lookback%s" % str(i+1)] = ts["Close"].shift(i+1)
for i in range(0, lookforward_minutes):
    ts["Lookforward%s" % str(i+1)] = ts["Close"].shift(-(i+1))
ts.dropna(inplace=True)
# Adjust all of these values to be percentage returns
ts["Lookback0"] = ts["Close"].pct_change()*100.0
for i in range(0, lookback_minutes):
    ts["Lookback%s" % str(i+1)] = ts[
        "Lookback%s" % str(i+1)
    ].pct_change()*100.0
for i in range(0, lookforward_minutes):
    ts["Lookforward%s" % str(i+1)] = ts[
        "Lookforward%s" % str(i+1)
    ].pct_change()*100.0
ts.dropna(inplace=True)
```

The following code carries out the calculation of the "up/down factor". It creates a list of up and down truth columns for each historical or future lag.

The "down" columns are iterated over and bitwise-added (&) to generate a final column, which is True only when all columns have not dropped below the down percent factor.

The "up" columns use bitwise-or (|) to generate a final column, which is True when at least one of the columns exceed the up percent factor. These two columns are then bitwise-added to

produce a final truth column where both conditions are met.

Since these are written with Python True and False operators they need to be converted to +1 and -1 integers, which the final two lines carry out.

```
Note that in the following code the "up/down factor" is commented out in favour of the
directional change, but is still kept in the same column name of UpDown. If you wish to use the
"up/down factor" instead of the directional change as response, you will need to uncomment out
ts["UpDown"] = down_tot & up_tot and comment out the line below it:
```

```
# Determine if the stock has gone up at least by
# 'up_down_factor' x 'percent_factor' and down no more
# then 'percent_factor'
up = up_down_factor*percent_factor
down = percent_factor
# Create the list of True/False entries for each date
# as to whether the up/down logic is true
down_cols = [
    ts["Lookforward%s" % str(i+1)] > -down
    for i in range(0, lookforward_minutes)
]
up_cols = [
    ts["Lookforward%s" % str(i+1)] > up
    for i in range(0, lookforward_minutes)
]
# Carry out the bitwise and, as well as bitwise or
# for the down and up logic
down_tot = down_cols[0]
for c in down_cols[1:]:
    down_tot = down_tot & c
up_tot = up_cols[0]
for c in up_cols[1:]:
    up_tot = up_tot | c
#ts["UpDown"] = down_tot & up_tot
ts["UpDown"] = np.sign(ts["Lookforward1"])
# Convert True/False into 1 and 0
ts["UpDown"] = ts["UpDown"].astype(int)
ts["UpDown"].replace(to_replace=0, value=-1, inplace=True)
return ts
```

This function carries out the data preparation work of the script. In the \_\_main\_\_ function the above function is called for the AREX data.

n\_estimators controls the number of decision trees to use in the RandomForestClassifier, while n\_jobs controls the number of CPU cores to use for the training.

Make sure to change your path from csv\_filepath = "/path/to/your/AREX.csv" to the path where your AREX (or other) data resides before running this script:

```
if __name__ == "__main__":
    random_state = 42
    n_estimators = 400
    n_jobs = 1
    csv_filepath = "/path/to/your/AREX.csv"
    lookback_minutes = 30
    lookforward_minutes = 5
    print("Importing and creating CSV DataFrame...")
    start_date = datetime.datetime(2007, 11, 8)
    end_date = datetime.datetime(2012, 12, 31)
    ts = create_up_down_dataframe(
        csv_filepath,
        lookback_minutes=lookback_minutes,
        lookforward_minutes=lookforward_minutes,
        start=start_date, end=end_date
    )
```

The following code uses the Pandas DataFrame generated above to create the X feature matrix and the y response vector. In this instance only the first five prior lags are used, although thirty are available in the initial data generation.

Once the data has been formatted into the X and y data-structures, a training-test split is created, with the test set equalling 30% of the data.

Note that in the final model development the data should not be split in this fashion and all of the data up to 2012 should be utilised to train the model, with the remaining 2013/2014 data used for out of sample trading strategy validation:

```
# Use the first five daily lags of AREX closing prices
print("Preprocessing data...")
X = ts[
    [
        "Lookback%s" % str(i)
        for i in range(0, 5)
    ]
]
y = ts["UpDown"]
# Use the training-testing split with 70% of data in the
# training data with the remaining 30% of data in the testing
print("Creating train/test split of data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=random_state
)
```

In this section the model is actually fit to the data. The important parameter is max\_depth, which controls the maximum depth of the grown trees in the Random Forest. It controls the

bias-variance trade-off of the model. A smaller max\_depth will have a reduced predictive capability, but will produce a much smaller file size and will execute much faster in QSTrader. Correspondingly, a larger max\_depth will potentially overfit on the training data, will have a significant filesize (the default value leads to a model of 4.1Gb in size!) and will execute slowly in QSTrader.

The Hit Rate and confusion matrix for the testing set are also output here if the training/test split is chosen as above.

Note that it is also necessary to modify the path to your data in the application of the joblib serialisation mechanism ( joblib.dump(model, '/path/to/your/ml\_model\_rf.pkl')):

```
print("Fitting classifier model...")
model = RandomForestClassifier(
    n_estimators=n_estimators,
    n_jobs=n_jobs,
    random_state=random_state,
    max_depth=10
)
model.fit(X_train, y_train)
print("Outputting metrics...")
print("Hit-Rate: %s" % model.score(X_test, y_test))
print("%s\n" % confusion_matrix(model.predict(X_test), y_test))
print("Pickling model...")
joblib.dump(model, '/path/to/your/ml_model_rf.pkl')
```

This concludes the model generation script. The pickled model file is stored in ml\_model\_rf.pkl and will be used in the following QSTrader Strategy object.

#### 29.3 QSTrader Strategy Object

Now that the predictive model has been succesfully pickled by joblib, attention will turn to using it in an "online" predictive manner within a QSTrader Strategy subclass.

The strategy itself is relatively simple. Every bar received via the event is used to form a rolling lag-length array of the previous bars' closing prices. This is then turned into a set of returns and multiplied by 100, as in the predictive model fitting stage.

For ease of understanding the procedure the strategy itself has been set to only go long and exit. It does not go short and exit, although this is a simple modification if so desired.

For every bar the models predict method is called, which returns +1 or -1 depending upon predicted direction for the next bar. If the strategy is not invested and receives a +1 then it goes long 10,000 units of AREX. If the strategy is invested and receives a -1 then it closes the 10,000 unit position.

NumPy and Pandas are both used within the class, as is joblib, for unpickling the predictive model. In addition, the usual QSTrader objects for Strategy classes are imported:

# intraday\_ml\_strategy.py

**import** numpy as np **import** pandas as pd

```
from sklearn.externals import joblib
```

```
from qstrader.price_parser import PriceParser
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
```

The initialisation of the class is relatively straightforward. It takes the model pickle file path through model\_pickle\_file as an initialisation parameter, along with the number of minutely bar lags to use for predicting the direction of the next bar, via lags.

The strategy stores the current prices in cur\_prices, which is one element longer than the current returns array, cur\_returns, since returns require n + 1 price elements to calculate n returns. The quantity qty is set to 10,000 in this instance, since there is 500,000 USD of equity. model contains the unpickled predictive model from Scikit-Learn:

**class** IntradayMachineLearningPredictionStrategy(AbstractStrategy):

```
"""
Requires:
tickers - The list of ticker symbols
events_queue - A handle to the system events queue
"""
def __init__(
    self, tickers, events_queue,
    model_pickle_file, lags=5
):
    self.tickers = tickers
    self.events_queue = events_queue
    self.model_pickle_file = model_pickle_file
    self.lags = lags
    self.invested = False
    self.cur_prices = np.zeros(self.lags+1)
    self.cur_returns = np.zeros(self.lags)
    self.minutes = 0
    self.qty = 10000
    self.model = joblib.load(model_pickle_file)
```

The \_update\_current\_returns method is used to generate the rolling lag-length array of returns of the AREX closing prices. It begins by reverse iterating through the current prices array and shifts the prices by one, adding in the new most recent price.

The computer scientists among you will recognise this behaviour as well represented by a double-ended queue (deque). Python contains such an implementation in the collections library. For simplicity I have used NumPy arrays in this example.

Once the current prices array is generated the returns list is calculated, but only once all elements have been populated into the list (i.e. after lags+1):

```
def _update_current_returns(self, event):
```

"""

```
Updates the array of current returns "features"
```

```
used by the machine learning model for prediction.
"""
# Adjust the feature vector to move all lags by one
# and then recalculate the returns
for i, f in reversed(list(enumerate(self.cur_prices))):
    if i > 0:
        self.cur_prices[i] = self.cur_prices[i-1]
    else:
        self.cur_prices[i] = event.close_price / float(
            PriceParser.PRICE_MULTIPLIER
        )
if self.minutes > (self.lags + 1):
    for i in range(0, self.lags):
        self.cur_returns[i] = ((
            self.cur_prices[i]/self.cur_prices[i+1]
        )-1.0)*100.0
```

As with all QSTrader Strategy subclasses the signal generation happens in the calculate\_signals method. Firstly, the current returns are updated upon receipt of a new market data bar. If enough minutes have passed (lags+2) then the model begins making predictions based on the current returns data.

Note that in newer versions of Scikit-Learn it is necessary to reshape one-dimensional arrays into two-dimensional arrays containing a single row otherwise a deprecation warning is given. This explains the reshape((1,-1)) method call. Finally, since model.predict returns an array of a single scalar rather than the scalar itself it is necessary to use the index element operator ([0]) to extract the value.

The remaining logic is tasked with going long or exiting depending upon whether the strategy is already invested and whether the prediction is +1 or -1. As usual, SignalEvent objects are sent to the events\_queue to be utilised by the Portfolio object:

```
def calculate_signals(self, event):
    """
    Calculate the intraday machine learning
    prediction strategy.
    """
    if event.type == EventType.BAR:
        self._update_current_returns(event)
        self.minutes += 1
        # Allow enough time to pass to populate the
        # returns feature vector
        if self.minutes > (self.lags + 2):
            pred = self.model.predict(self.cur_returns.reshape((1, -1)))[0]
            # Long only strategy
            if not self.invested and pred == 1:
                print("LONG: %s" % event.time)
                self.events_queue.put(
```

```
SignalEvent(self.tickers[0], "BOT", self.qty)
    )
    self.invested = True
if self.invested and pred == -1:
    print("CLOSING LONG: %s" % event.time)
    self.events_queue.put(
        SignalEvent(self.tickers[0], "SLD", self.qty)
    )
    self.invested = False
```

Unfortunately for more complex models the model.predict call can be extremely slow. For simpler models with minimal parameters (e.g. linear regression) the call is fast. On the desktop workstation used here to generate the results it was possible to obtain approximately 5,000 bars/second for simple models.

For more complex models such as Random Forest classifiers with many deeply grown trees this prediction speed can drop substantially, often by up to three orders of magnitude. For the Random Forest ensemble in particular the initial model generated in this example produced a 4.1Gb pickle file, which is beyond the RAM capacity of some earlier PCs. Thus the method has no choice but to swap to disk when predicting new data points, which can heavily reduce performance.

One of the goals with optimising a model is to make sure that it is possible to actually generate predictions in a reasonable time frame. In the case of the Random Forest classifier, it was necessary to experiment with the maximum depth of the tree in order to reduce the final pickle file size but still achieve reasonable prediction performance. The final model is a tradeoff between prediction accuracy and backtest execution speed, which ran at approximately 60 bars/second in the example below.

#### 29.4 QSTrader Backtest Script

Now that the Strategy class has been developed it is necessary to wrap it in an intraday backtest. This code is given below in intraday\_ml\_backtest.py. It is very similar to other QSTrader implementations.

The main differences are that a new price handler IQFeedIntradayCsvBarPriceHandler is now imported instead of one designed for Yahoo Finance daily data, as well as the periods parameter for the TearsheetStatistics class, which has been set to 252 × 6.5 × 60 = 98280. This ensures that the calculated Sharpe Ratio is correct for the number of periods being used:

# intraday\_ml\_backtest.py

```
import click
import datetime
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.iq_feed_intraday_csv_bar import \
```

```
IQFeedIntradayCsvBarPriceHandler
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.naive import NaivePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading_session.backtest import Backtest
from intraday_ml_strategy import \
    IntradayMachineLearningPredictionStrategy
def run(config, testing, tickers, filename):
    # Set up variables needed for backtest
    events_queue = queue.Queue()
    csv_dir = "/path/to/your/data/"
    initial_equity = PriceParser.parse(500000.00)
    # Use DTN IQFeed Intraday Bar Price Handler
    start_date = datetime.datetime(2013, 1, 1)
    price_handler = IQFeedIntradayCsvBarPriceHandler(
        csv_dir, events_queue, tickers, start_date=start_date
    )
    # Use the IntradayMachineLearningPredictionStrategy
    model_pickle_file = '/path/to/your/ml_model_rf.pkl'
    strategy = IntradayMachineLearningPredictionStrategy(
        tickers, events_queue, model_pickle_file, lags=5
    )
    strategy = Strategies(strategy, DisplayStrategy())
    # Use the Naive Position Sizer (suggested quantities are followed)
    position_sizer = NaivePositionSizer()
    # Use an example Risk Manager
    risk_manager = ExampleRiskManager()
    # Use the default Portfolio Handler
    portfolio_handler = PortfolioHandler(
        initial_equity, events_queue, price_handler,
        position_sizer, risk_manager
```

```
# Use the ExampleCompliance component
    compliance = ExampleCompliance(config)
    # Use a simulated IB Execution Handler
    execution_handler = IBSimulatedExecutionHandler(
        events_queue, price_handler, compliance
    )
    # Use the Tearsheet Statistics
    statistics = TearsheetStatistics(
        config, portfolio_handler,
        title=["Intraday AREX Machine Learning Prediction Strategy"],
        periods=int(252*6.5*60) # Minutely periods
    )
    # Set up the backtest
    backtest = Backtest(
        price_handler, strategy,
        portfolio_handler, execution_handler,
        position_sizer, risk_manager,
        statistics, initial_equity
    )
    results = backtest.simulate_trading(testing=testing)
    statistics.save(filename)
    return results
@click.command()
@click.option(
    '--config',
    default=settings.DEFAULT_CONFIG_FILENAME, help='Config filename'
@click.option(
    '--testing/--no-testing',
    default=False,
    help='Enable testing mode'
@click.option(
    '--tickers',
    default='SP500TR',
    help='Tickers (use comma)'
@click.option(
```

)

)

)

)

```
'--filename',
    default='',
    help='Pickle (.pkl) statistics filename'
)
def main(config, testing, tickers, filename):
    tickers = tickers.split(",")
    config = settings.from_file(config, testing)
    run(config, testing, tickers, filename)
if __name__ == "__main__":
```

main()

In order for the code to work it is necessary to change the paths to your appropriate data directories for both the AREX bar data CSV file and the directory where the pickle model lives. It will be necessary to change the following directories to point to your data:

- csv\_dir = "/path/to/your/data/"
- model\_pickle\_file = '/path/to/your/ml\_model\_rf.pkl'

To run the model type the following into the Terminal:

```
$ python intraday_ml_backtest.py --tickers=AREX
```

The results are presented in the following section.

#### 29.5 Results

Two intraday backtests are presented here, both of which cover the period 1st January 2013 to 11th March 2014, which is a little over a year. The first test trains a Linear Discriminant Analyser with default Scikit-Learn settings, while the second trains a Random Forest classifier ensemble model with a maximum tree depth equal to ten. Both models are trained on AREX data from 8th November 2007 to 31st December 2012.

Both of the backtests use the respective model "out of sample", that is on data which has not been seen by the classifiers in training. In addition both of the backtests were calculated net of standard US Interactive Brokers commission. The tests did not include slippage, market impact or the effect of spread–all of which will likely have a negative effect on the CAGR.

The tearsheet for the Linear Discriminant Analyser strategy is presented in Figure 29.1.

It posts an out-of-sample Sharpe Ratio of 2.02, which is higher than what is often found in a daily model, as is to be expected with higher frequency models. With a transaction block of 10,000 shares it posts a CAGR of 5.35%, with a maximum daily drawdown of 1.71%. The low drawdown is a consequence of the very short holding periods of the strategy, which are usually on the order of minutes. The equity curve is broadly rising although there is a period where the strategy remains underwater for three months at the end of 2013.

The tearsheet for the Random Forest strategy is presented in Figure 29.2.

It posts an out-of-sample Sharpe Ratio of 3.02, on a CAGR of 10.63%. Note that calculating a CAGR on approximately one year of data is misleading, since it will almost be equal to the

![](_page_14_Figure_0.jpeg)

Figure 29.1: Tearsheet for Linear Discriminant Analysis model on AREX

![](_page_15_Figure_0.jpeg)

Intraday AREX Machine Learning Prediction Strategy

Figure 29.2: Tearsheet for Random Forest model on AREX

total return. The Sharpe Ratio is higher than that for LDA as the returns have increased but the drawdowns have stayed approximately the same. The equity curve also looks more visually consistent. Despite this, it also remains underwater for the latter three months of 2013 and only begins to recover at the start of 2014.

#### 29.6 Next Steps

There is a lot of work to be done to turn this into an effective strategy that would be placed in production.

The first step would be to replicate this model across many tens or hundreds of equities (depending upon available capital!) as a means of attempting to generate many uncorrelated "bets" on, say, separate sectors of the market.

In addition a more robust hyperparameter study should be carried out for many of the classifiers. This will optimise the bias-variance trade-off in the models. To some extent this is controlled by the maximum depth of the tree in the Random Forest classifier.

Taking this from a backtested system to a consistently working production model will require accounting for slippage, market impact, average daily volume of shares traded and more realistic commissions.

Running at minutely frequency is clearly a lot harder than carrying out daily strategies. This is the "price to pay" for obtaining larger Sharpe ratios and thus strategies that possess improved statistical significance.

#### 29.7 Full Code

# intraday\_ml\_model\_fit.py

```
import datetime
import numpy as np
import pandas as pd
import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import (
    BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
)
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
def create_up_down_dataframe(
```

csv\_filepath, lookback\_minutes=30,

```
lookforward_minutes=5,
up_down_factor=2.0,
percent_factor=0.01,
start=None, end=None
```

):

"""

Creates a Pandas DataFrame that imports and calculates the percentage returns of an intraday OLHC ticker from disk.

'lookback\_minutes' of prior returns are stored to create a feature vector, while 'lookforward\_minutes' are used to ascertain how far in the future to predict across.

The actual prediction is to determine whether a ticker moves up by at least 'up\_down\_factor' x 'percent\_factor', while not dropping below 'percent\_factor' in the same period.

i.e. Does the stock move up 1% in a minute and not down by 0.5%?

```
The DataFrame will consist of 'lookback_minutes' columns for feature
vectors and one column for whether the stock adheres to the "up/down"
rule, which is 1 if True or 0 if False for each minute.
"""
ts = pd.read_csv(
    csv_filepath,
    names=[
        "Timestamp", "Open", "Low", "High",
        "Close", "Volume", "OpenInterest"
    ],
    index_col="Timestamp", parse_dates=True
)
# Filter on start/end dates
if start is not None:
    ts = ts[ts.index >= start]
if end is not None:
    ts = ts[ts.index <= end]
# Drop the non-essential columns
ts.drop(
    [
        "Open", "Low", "High",
        "Volume", "OpenInterest"
    ],
    axis=1, inplace=True
```

```
# Create the lookback and lookforward shifts
for i in range(0, lookback_minutes):
    ts["Lookback%s" % str(i+1)] = ts["Close"].shift(i+1)
for i in range(0, lookforward_minutes):
    ts["Lookforward%s" % str(i+1)] = ts["Close"].shift(-(i+1))
ts.dropna(inplace=True)
# Adjust all of these values to be percentage returns
ts["Lookback0"] = ts["Close"].pct_change()*100.0
for i in range(0, lookback_minutes):
    ts["Lookback%s" % str(i+1)] = ts[
        "Lookback%s" % str(i+1)
    ].pct_change()*100.0
for i in range(0, lookforward_minutes):
    ts["Lookforward%s" % str(i+1)] = ts[
        "Lookforward%s" % str(i+1)
    ].pct_change()*100.0
ts.dropna(inplace=True)
# Determine if the stock has gone up at least by
# 'up_down_factor' x 'percent_factor' and down no more
# then 'percent_factor'
up = up_down_factor*percent_factor
down = percent_factor
# Create the list of True/False entries for each date
# as to whether the up/down logic is true
down_cols = [
    ts["Lookforward%s" % str(i+1)] > -down
    for i in range(0, lookforward_minutes)
]
up_cols = [
    ts["Lookforward%s" % str(i+1)] > up
    for i in range(0, lookforward_minutes)
]
# Carry out the bitwise and, as well as bitwise or
# for the down and up logic
down_tot = down_cols[0]
for c in down_cols[1:]:
    down_tot = down_tot & c
up_tot = up_cols[0]
for c in up_cols[1:]:
    up_tot = up_tot | c
```

)

```
#ts["UpDown"] = down_tot & up_tot
    ts["UpDown"] = np.sign(ts["Lookforward1"])
    # Convert True/False into 1 and 0
    ts["UpDown"] = ts["UpDown"].astype(int)
    ts["UpDown"].replace(to_replace=0, value=-1, inplace=True)
    return ts
if __name__ == "__main__":
    random_state = 42
    n_estimators = 400
    n_jobs = 1
    csv_filepath = "/path/to/your/AREX.csv"
    lookback_minutes = 30
    lookforward_minutes = 5
    print("Importing and creating CSV DataFrame...")
    start_date = datetime.datetime(2007, 11, 8)
    end_date = datetime.datetime(2012, 12, 31)
    ts = create_up_down_dataframe(
        csv_filepath,
        lookback_minutes=lookback_minutes,
        lookforward_minutes=lookforward_minutes,
        start=start_date, end=end_date
    )
    # Use the first five daily lags of AREX closing prices
    print("Preprocessing data...")
    X = ts[
        [
            "Lookback%s" % str(i)
            for i in range(0, 5)
        ]
    ]
    y = ts["UpDown"]
    # Use the training-testing split with 70% of data in the
    # training data with the remaining 30% of data in the testing
    print("Creating train/test split of data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=random_state
    )
    print("Fitting classifier model...")
```

```
#model = BaggingClassifier(
# base_estimator=DecisionTreeClassifier(),
# n_estimators=n_estimators,
# random_state=random_state,
# n_jobs=n_jobs
#)
#model = GradientBoostingClassifier(
# n_estimators=n_estimators,
# random_state=random_state
#)
model = RandomForestClassifier(
    n_estimators=n_estimators,
    n_jobs=n_jobs,
    random_state=random_state,
    max_depth=10
)
model.fit(X_train, y_train)
#model.fit(X, y)
print("Outputting metrics...")
print("Hit-Rate: %s" % model.score(X_test, y_test))
print("%s\n" % confusion_matrix(model.predict(X_test), y_test))
print("Pickling model...")
joblib.dump(model, '/path/to/your/ml_model_rf.pkl')
```

# intraday\_ml\_strategy.py

**import** numpy as np **import** pandas as pd **from** sklearn.externals **import** joblib

```
from qstrader.price_parser import PriceParser
from qstrader.event import (SignalEvent, EventType)
from qstrader.strategy.base import AbstractStrategy
```

```
class IntradayMachineLearningPredictionStrategy(AbstractStrategy):
    """
    Requires:
    tickers - The list of ticker symbols
```

```
events_queue - A handle to the system events queue
"""
def __init__(
    self, tickers, events_queue,
    model_pickle_file, lags=5
):
    self.tickers = tickers
    self.events_queue = events_queue
    self.model_pickle_file = model_pickle_file
    self.lags = lags
    self.invested = False
    self.cur_prices = np.zeros(self.lags+1)
    self.cur_returns = np.zeros(self.lags)
    self.minutes = 0
    self.qty = 10000
    self.model = joblib.load(model_pickle_file)
def _update_current_returns(self, event):
    """
    Updates the array of current returns "features"
    used by the machine learning model for prediction.
    """
    # Adjust the feature vector to move all lags by one
    # and then recalculate the returns
    for i, f in reversed(list(enumerate(self.cur_prices))):
        if i > 0:
            self.cur_prices[i] = self.cur_prices[i-1]
        else:
            self.cur_prices[i] = event.close_price / float(
                PriceParser.PRICE_MULTIPLIER
            )
    if self.minutes > (self.lags + 1):
        for i in range(0, self.lags):
            self.cur_returns[i] = ((
                self.cur_prices[i]/self.cur_prices[i+1]
            )-1.0)*100.0
def calculate_signals(self, event):
    """
    Calculate the intraday machine learning
    prediction strategy.
    """
    if event.type == EventType.BAR:
        self._update_current_returns(event)
```

```
self.minutes += 1
            # Allow enough time to pass to populate the
            # returns feature vector
            if self.minutes > (self.lags + 2):
                pred = self.model.predict(
                    self.cur_returns.reshape((1, -1))
                )[0]
                # Long only strategy
                if not self.invested and pred == 1:
                    print("LONG: %s" % event.time)
                    self.events_queue.put(
                        SignalEvent(
                            self.tickers[0], "BOT", self.qty
                        )
                    )
                    self.invested = True
                if self.invested and pred == -1:
                    print("CLOSING LONG: %s" % event.time)
                    self.events_queue.put(
                        SignalEvent(
                            self.tickers[0], "SLD", self.qty
                        )
                    )
                    self.invested = False
# intraday_ml_backtest.py
import click
import datetime
from qstrader import settings
from qstrader.compat import queue
from qstrader.price_parser import PriceParser
from qstrader.price_handler.iq_feed_intraday_csv_bar import \
    IQFeedIntradayCsvBarPriceHandler
from qstrader.strategy import Strategies, DisplayStrategy
from qstrader.position_sizer.naive import NaivePositionSizer
from qstrader.risk_manager.example import ExampleRiskManager
from qstrader.portfolio_handler import PortfolioHandler
from qstrader.compliance.example import ExampleCompliance
from qstrader.execution_handler.ib_simulated import \
    IBSimulatedExecutionHandler
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading_session.backtest import Backtest
```

```
from intraday_ml_strategy import \
    IntradayMachineLearningPredictionStrategy
def run(config, testing, tickers, filename):
    # Set up variables needed for backtest
    events_queue = queue.Queue()
    csv_dir = "/path/to/your/data/"
    initial_equity = PriceParser.parse(500000.00)
    # Use DTN IQFeed Intraday Bar Price Handler
    start_date = datetime.datetime(2013, 1, 1)
    price_handler = IQFeedIntradayCsvBarPriceHandler(
        csv_dir, events_queue, tickers, start_date=start_date
    )
    # Use the IntradayMachineLearningPredictionStrategy
    model_pickle_file = '/path/to/your/ml_model_rf.pkl'
    strategy = IntradayMachineLearningPredictionStrategy(
        tickers, events_queue, model_pickle_file, lags=5
    )
    strategy = Strategies(strategy, DisplayStrategy())
    # Use the Naive Position Sizer
    # (suggested quantities are followed)
    position_sizer = NaivePositionSizer()
    # Use an example Risk Manager
    risk_manager = ExampleRiskManager()
    # Use the default Portfolio Handler
    portfolio_handler = PortfolioHandler(
        initial_equity, events_queue, price_handler,
        position_sizer, risk_manager
    )
    # Use the ExampleCompliance component
    compliance = ExampleCompliance(config)
    # Use a simulated IB Execution Handler
    execution_handler = IBSimulatedExecutionHandler(
        events_queue, price_handler, compliance
    )
```

```
# Use the Tearsheet Statistics
    statistics = TearsheetStatistics(
        config, portfolio_handler,
        title=["Intraday AREX Machine Learning Prediction Strategy"],
        periods=int(252*6.5*60) # Minutely periods
    )
    # Set up the backtest
    backtest = Backtest(
        price_handler, strategy,
        portfolio_handler, execution_handler,
        position_sizer, risk_manager,
        statistics, initial_equity
    )
    results = backtest.simulate_trading(testing=testing)
    statistics.save(filename)
    return results
@click.command()
@click.option(
    '--config',
    default=settings.DEFAULT_CONFIG_FILENAME,
    help='Config filename'
)
@click.option(
    '--testing/--no-testing',
    default=False,
    help='Enable testing mode'
)
@click.option(
    '--tickers',
    default='SP500TR',
    help='Tickers (use comma)'
)
@click.option(
    '--filename',
    default='',
    help='Pickle (.pkl) statistics filename'
)
def main(config, testing, tickers, filename):
    tickers = tickers.split(",")
    config = settings.from_file(config, testing)
    run(config, testing, tickers, filename)
```

**if** \_\_name\_\_ == "\_\_main\_\_": main()
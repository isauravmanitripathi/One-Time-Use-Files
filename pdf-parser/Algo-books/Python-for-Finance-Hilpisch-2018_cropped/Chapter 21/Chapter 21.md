# **Chapter 21. Market-Based Valuation**

We are facing extreme volatility. Carlos Ghosn

A major task in derivatives analytics is the *market-based valuation of options and derivatives* that are not liquidly traded. To this end, one generally calibrates a pricing model to market quotes of liquidly traded options and uses the calibrated model for the pricing of the non-traded options. 1

This chapter presents a case study based on the DX package and illustrates that this package, as developed step-by-step in the previous four chapters, is suited to implement a market-based valuation. The case study is based on the DAX 30 stock index, which is a blue chip stock market index consisting of stocks of 30 major German companies. On this index, liquidly traded European call and put options are available.

The chapter is divided into sections that implement the following major tasks:

### *"Options Data"*

One needs two types of data, namely for the DAX 30 stock index itself and for the liquidly traded European options on the index.

### *"Model Calibration"*

To value the non-traded options in a market-consistent fashion, one generally first calibrates the chosen model to quoted option prices in such a way that the model based on the optimal parameters replicates the market prices as well as possible.

### *"Portfolio Valuation"*

Equipped with the data and a market-calibrated model for the DAX 30 stock index, the final task then is to model and value the non-traded options; important risk measures are also estimated on a position and portfolio level.

The index and options data used in this chapter are from the Thomson Reuters Eikon Data API (see "Python Code").

# **Options Data**

To get started, here are the required imports and customizations:

```
In [1]: import numpy as np
        import pandas as pd
        import datetime as dt
In [2]: from pylab import mpl, plt
        plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
In [3]: import sys
        sys.path.append('../')
        sys.path.append('../dx')
```

Given the data file as created in "Python Code", the options data is read with pandas and processed such that date information is given as pd.Timestamp objects:

```
In [4]: dax = pd.read_csv('../../source/tr_eikon_option_data.csv',
                       index_col=0)
In [5]: for col in ['CF_DATE', 'EXPIR_DATE']:
          dax[col] = dax[col].apply(lambda date: pd.Timestamp(date))
In [6]: dax.info()
       <class 'pandas.core.frame.DataFrame'>
       Int64Index: 115 entries, 0 to 114
       Data columns (total 7 columns):
       Instrument 115 non-null object
       CF_DATE 115 non-null datetime64[ns]
       EXPIR_DATE 114 non-null datetime64[ns]
       PUTCALLIND 114 non-null object
       STRIKE_PRC 114 non-null float64
       CF_CLOSE 115 non-null float64
       IMP_VOLT 114 non-null float64
       dtypes: datetime64[ns](2), float64(3), object(2)
       memory usage: 7.2+ KB
In [7]: dax.set_index('Instrument').head(7)
Out[7]:
                    CF_DATE EXPIR_DATE PUTCALLIND STRIKE_PRC CF_CLOSE \
   Instrument
   .GDAXI 2018-04-27 NaT NaN NaN 12500.47
   GDAX105000G8.EX 2018-04-27 2018-07-20 CALL 10500.0 2040.80
   GDAX105000S8.EX 2018-04-27 2018-07-20 PUT 10500.0 32.00
   GDAX108000G8.EX 2018-04-27 2018-07-20 CALL 10800.0 1752.40
   GDAX108000S8.EX 2018-04-26 2018-07-20 PUT 10800.0 43.80
   GDAX110000G8.EX 2018-04-27 2018-07-20 CALL 11000.0 1562.80
   GDAX110000S8.EX 2018-04-27 2018-07-20 PUT 11000.0 54.50
```

IMP\_VOLT

| Instrument      |       |
|-----------------|-------|
| .GDAXI          | NaN   |
| GDAX105000G8.EX | 23.59 |
| GDAX105000S8.EX | 23.59 |
| GDAX108000G8.EX | 22.02 |
| GDAX108000S8.EX | 22.02 |
| GDAX110000G8.EX | 21.00 |
| GDAX110000S8.EX | 21.00 |
|                 |       |

Reads the data with pd.read\_csv().

Processes the two columns with date information.

The resulting DataFrame object.

The following code stores the relevant index level for the DAX 30 in a variable and creates two new DataFrame objects, one for calls and one for puts. Figure 21-1 presents the market quotes for the calls and their implied volatilities: 2

```
In [8]: initial_value = dax.iloc[0]['CF_CLOSE']
In [9]: calls = dax[dax['PUTCALLIND'] == 'CALL'].copy()
        puts = dax[dax['PUTCALLIND'] == 'PUT '].copy()
In [10]: calls.set_index('STRIKE_PRC')[['CF_CLOSE', 'IMP_VOLT']].plot(
             secondary_y='IMP_VOLT', style=['bo', 'rv'], figsize=(10, 6));
```

Assigns the relevant index level to the initial\_value variable.

Separates the options data for calls and puts into two new DataFrame objects.

![](_page_3_Figure_0.jpeg)

*Figure 21-1. Market quotes and implied volatilities for European call options on the DAX 30*

Figure 21-2 presents the market quotes for the puts and their implied volatilities:

```
In [11]: ax = puts.set_index('STRIKE_PRC')[['CF_CLOSE', 'IMP_VOLT']].plot(
             secondary_y='IMP_VOLT', style=['bo', 'rv'], figsize=(10, 6))
         ax.get_legend().set_bbox_to_anchor((0.25, 0.5));
```

![](_page_4_Figure_0.jpeg)

*Figure 21-2. Market quotes and implied volatilities for European put options on the DAX 30*

# **Model Calibration**

This section selects the relevant market data, models the European options on the DAX 30 index, and implements the calibration procedure itself.

# **Relevant Market Data**

Model calibration generally takes place based on a smaller subset of the available option market quotes. <sup>3</sup> To this end, the following code selects only those European call options whose strike price is relatively close to the current index level (see Figure 21-3). In other words, only those European call options are selected that are not too far in-the-money or out-of-the-money: In [12]: limit = 500 In [13]: option\_selection = calls[abs(calls['STRIKE\_PRC'] - initial\_value) < limit].copy() In [14]: option\_selection.info() <**class** '**pandas**.core.frame.DataFrame'> Int64Index: 20 entries, 43 to 81 Data columns (total 7 columns): Instrument 20 non-null object CF\_DATE 20 non-null datetime64[ns] EXPIR\_DATE 20 non-null datetime64[ns] PUTCALLIND 20 non-null object STRIKE\_PRC 20 non-null float64 CF\_CLOSE 20 non-null float64 IMP\_VOLT 20 non-null float64 dtypes: datetime64[ns](2), float64(3), object(2) memory usage: 1.2+ KB In [15]: option\_selection.set\_index('Instrument').tail() Out[15]: CF\_DATE EXPIR\_DATE PUTCALLIND STRIKE\_PRC CF\_CLOSE \ Instrument GDAX128000G8.EX 2018-04-27 2018-07-20 CALL 12800.0 182.4 GDAX128500G8.EX 2018-04-27 2018-07-20 CALL 12850.0 162.0 GDAX129000G8.EX 2018-04-25 2018-07-20 CALL 12900.0 142.9 GDAX129500G8.EX 2018-04-27 2018-07-20 CALL 12950.0 125.4 GDAX130000G8.EX 2018-04-27 2018-07-20 CALL 13000.0 109.4 IMP\_VOLT Instrument GDAX128000G8.EX 12.70 GDAX128500G8.EX 12.52 GDAX129000G8.EX 12.36 GDAX129500G8.EX 12.21 GDAX130000G8.EX 12.06 In [16]: option\_selection.set\_index('STRIKE\_PRC')[['CF\_CLOSE', 'IMP\_VOLT']].plot( secondary\_y='IMP\_VOLT', style=['bo', 'rv'], figsize=(10, 6));

Sets the limit value for the derivation of the strike price from the current index level (*moneyness* condition).

Selects, based on the limit value, the European call options to be included for the calibration.

![](_page_7_Figure_1.jpeg)

The resulting DataFrame with the European call options for the calibration.

*Figure 21-3. European call options on the DAX 30 used for model calibration*

# **Option Modeling**

Having the relevant market data defined, the DX package can now be used to model the European call options. The definition of the dx.market\_environment object to model the DAX 30 index follows, along the lines of the examples in previous chapters:

```
In [17]: import dx
In [18]: pricing_date = option_selection['CF_DATE'].max()
In [19]: me_dax = dx.market_environment('DAX30', pricing_date)
In [20]: maturity = pd.Timestamp(calls.iloc[0]['EXPIR_DATE'])
In [21]: me_dax.add_constant('initial_value', initial_value)
         me_dax.add_constant('final_date', maturity)
         me_dax.add_constant('currency', 'EUR')
In [22]: me_dax.add_constant('frequency', 'B')
         me_dax.add_constant('paths', 10000)
In [23]: csr = dx.constant_short_rate('csr', 0.01)
         me_dax.add_curve('discount_curve', csr)
```

Defines the initial or pricing date given the options data.

Instantiates the dx.market\_environment object.

Defines the maturity date given the options data.

Adds the basic model parameters.

Adds the simulation-related parameters.

Defines and adds a dx.constant\_short\_rate object.

This code then adds the model-specific parameters for the dx.jump\_diffusion class and instantiates a respective simulation object:

```
In [24]: me_dax.add_constant('volatility', 0.2)
         me_dax.add_constant('lambda', 0.8)
         me_dax.add_constant('mu', -0.2)
         me_dax.add_constant('delta', 0.1)
In [25]: dax_model = dx.jump_diffusion('dax_model', me_dax)
```

As an example for a European call option, consider the following parameterization for which the strike is set equal to the current index level of the DAX 30. This allows for a first value estimation based on Monte Carlo simulation:

```
In [26]: me_dax.add_constant('strike', initial_value)
         me_dax.add_constant('maturity', maturity)
In [27]: payoff_func = 'np.maximum(maturity_value - strike, 0)'
In [28]: dax_eur_call = dx.valuation_mcs_european('dax_eur_call',
                                 dax_model, me_dax, payoff_func)
In [29]: dax_eur_call.present_value()
Out[29]: 654.298085
```

Sets the value for strike equal to the initial\_value.

Defines the payoff function for a European call option.

Instantiates the valuation object.

Initiates the simulation and value estimation.

Similarly, valuation objects can be defined for all relevant European call options on the DAX 30 index. The only parameter that changes is the strike price:

```
In [30]: option_models = {}
         for option in option_selection.index:
             strike = option_selection['STRIKE_PRC'].loc[option]
             me_dax.add_constant('strike', strike)
             option_models[strike] = dx.valuation_mcs_european(
                                          'eur_call_%d' % strike,
                                         dax_model,
                                         me_dax,
                                         payoff_func)
```

The valuation objects are collected in a dict object.

Selects the relevant strike price and (re)defines it in the dx.market\_environment object.

Now, based on the valuation objects for all relevant options, the function calculate\_model\_values() returns the model values for all options given a set of the model-specific parameter values p0:

```
In [32]: def calculate_model_values(p0):
             ''' Returns all relevant option values.
             Parameters
             ===========
             p0: tuple/list
                 tuple of kappa, theta, volatility
             Returns
             =======
             model_values: dict
                 dictionary with model values
             '''volatility, lamb, mu, delta = p0
             dax_model.update(volatility=volatility, lamb=lamb,
                              mu=mu, delta=delta)
             return {
                     strike: model.present_value(fixed_seed=True)
                     for strike, model in option_models.items()
                 }
In [33]: calculate_model_values((0.1, 0.1, -0.4, 0.0))
Out[33]: {12050.0: 611.222524,
          12100.0: 571.83659,
          12150.0: 533.595853,
          12200.0: 496.607225,
          12250.0: 460.863233,
          12300.0: 426.543355,
          12350.0: 393.626483,
          12400.0: 362.066869,
          12450.0: 331.877733,
          12500.0: 303.133596,
          12550.0: 275.987049,
          12600.0: 250.504646,
          12650.0: 226.687523,
          12700.0: 204.550609,
          12750.0: 184.020514,
          12800.0: 164.945082,
          12850.0: 147.249829,
          12900.0: 130.831722,
          12950.0: 115.681449,
          13000.0: 101.917351}
```

The function calculate\_model\_values() is used during the calibration procedure, as described next.

# **Calibration Procedure**

Calibration of an option pricing model is, in general, a convex optimization problem. The most widely used function for the calibration — i.e., the minimization of some error function value — is the *mean-squared error* (MSE) for the model option values given the market quotes of the options. <sup>4</sup> Assume there are *N* relevant options, and also model and market quotes. The problem of calibrating an option pricing model to the market quotes based on the MSE is then given in [Equation](#page-11-0) 21-1. There, and are the market price and the model price of the *n*th option, respectively. *p* is the parameter set provided as input to the option pricing model.

<span id="page-11-0"></span>*Equation 21-1. Mean-squared error for model calibration*

![](_page_11_Figure_3.jpeg)

The Python function mean\_squared\_error() implements this approach to model calibration technically. A global variable i is used to control the output of intermediate parameter tuple objects and the resulting MSE:

```
In [34]: i = 0
         def mean_squared_error(p0):
             ''' Returns the mean-squared error given
             the model and market values.
             Parameters
             ===========
             p0: tuple/list
                 tuple of kappa, theta, volatility
             Returns
             =======
             MSE: float
                 mean-squared error
             '''global i
             model_values = np.array(list(
                     calculate_model_values(p0).values()))
```

```
market_values = option_selection['CF_CLOSE'].values
            option_diffs = model_values - market_values
            MSE = np.sum(option_diffs ** 2) / len(option_diffs)
            if i % 75 == 0:
                if i == 0:
                    print('%4s %6s %6s %6s %6s --> %6s' %
                         ('i', 'vola', 'lambda', 'mu', 'delta', 'MSE'))
                print('%4d %6.3f %6.3f %6.3f %6.3f --> %6.3f' %
                        (i, p0[0], p0[1], p0[2], p0[3], MSE))
            i += 1
            return MSE
In [35]: mean_squared_error((0.1, 0.1, -0.4, 0.0))
           i vola lambda mu delta --> MSE
           0 0.100 0.100 -0.400 0.000 --> 728.375
Out[35]: 728.3752973715275
```

Estimates the set of model values.

Picks out the market quotes.

Calculates element-wise the differences between the two.

Calculates the mean-squared error value.

Illustrates such a calculation based on sample parameters.

Chapter 11 introduces the two functions (spo.brute() and spo.fmin()) that are used to implement the calibration procedure. First, the global minimization based on ranges for the four model-specific parameter values. The result is an optimal parameter combination given all the parameter combinations checked during the *brute force minimization*:

```
In [36]: import scipy.optimize as spo
In [37]: %%time
        i = 0
        opt_global = spo.brute(mean_squared_error,
                         ((0.10, 0.201, 0.025), # range for volatility
                          (0.10, 0.80, 0.10), # range for jump intensity
                          (-0.40, 0.01, 0.10), # range for average jump size
                          (0.00, 0.121, 0.02)), # range for jump variability
                        finish=None)
           i vola lambda mu delta --> MSE
           0 0.100 0.100 -0.400 0.000 --> 728.375
          75 0.100 0.300 -0.400 0.080 --> 5157.513
```

```
150 0.100 0.500 -0.300 0.040 --> 12199.386
        225 0.100 0.700 -0.200 0.000 --> 6904.932
        300 0.125 0.200 -0.200 0.100 --> 855.412
        375 0.125 0.400 -0.100 0.060 --> 621.800
        450 0.125 0.600 0.000 0.020 --> 544.137
        525 0.150 0.100 0.000 0.120 --> 3410.776
        600 0.150 0.400 -0.400 0.080 --> 46775.769
        675 0.150 0.600 -0.300 0.040 --> 56331.321
        750 0.175 0.100 -0.200 0.000 --> 14562.213
        825 0.175 0.300 -0.200 0.100 --> 24599.738
        900 0.175 0.500 -0.100 0.060 --> 19183.167
        975 0.175 0.700 0.000 0.020 --> 11871.683
        1050 0.200 0.200 0.000 0.120 --> 31736.403
        1125 0.200 0.500 -0.400 0.080 --> 130372.718
        1200 0.200 0.700 -0.300 0.040 --> 126365.140
        CPU times: user 1min 45s, sys: 7.07 s, total: 1min 52s
        Wall time: 1min 56s
In [38]: mean_squared_error(opt_global)
Out[38]: 17.946670038040985
```

The opt\_global values are intermediate results only. They are used as starting values for the *local minimization*. Given the parameterization used, the opt\_local values are final and optimal given certain assumed tolerance levels:

```
In [39]: %%time
        i = 0
        opt_local = spo.fmin(mean_squared_error, opt_global,
                            xtol=0.00001, ftol=0.00001,
                            maxiter=200, maxfun=550)
           i vola lambda mu delta --> MSE
           0 0.100 0.200 -0.300 0.000 --> 17.947
          75 0.098 0.216 -0.302 -0.001 --> 7.885
         150 0.098 0.216 -0.300 -0.001 --> 7.371
        Optimization terminated successfully.
                 Current function value: 7.371163
                 Iterations: 100
                 Function evaluations: 188
        CPU times: user 15.6 s, sys: 1.03 s, total: 16.6 s
        Wall time: 16.7 s
In [40]: i = 0
        mean_squared_error(opt_local)
           i vola lambda mu delta --> MSE
           0 0.098 0.216 -0.300 -0.001 --> 7.371
Out[40]: 7.371162645265256
In [41]: calculate_model_values(opt_local)
Out[41]: {12050.0: 647.428189,
         12100.0: 607.402796,
         12150.0: 568.46137,
         12200.0: 530.703659,
         12250.0: 494.093839,
         12300.0: 458.718401,
         12350.0: 424.650128,
         12400.0: 392.023241,
         12450.0: 360.728543,
         12500.0: 330.727256,
```

```
12550.0: 302.117223,
12600.0: 274.98474,
12650.0: 249.501807,
12700.0: 225.678695,
12750.0: 203.490065,
12800.0: 182.947468,
12850.0: 163.907583,
12900.0: 146.259349,
12950.0: 129.909743,
13000.0: 114.852425}
```

The mean-squared error given the optimal parameter values.

The model values given the optimal parameter values.

Next, we compare the model values for the optimal parameters with the market quotes. The pricing errors are calculated as the absolute differences between the model values and market quotes and as the deviation in percent from the market quotes:

```
In [42]: option_selection['MODEL'] = np.array(list(calculate_model_values(
                                             opt_local).values()))
        option_selection['ERRORS_EUR'] = (option_selection['MODEL'] -
                                      option_selection['CF_CLOSE'])
        option_selection['ERRORS_%'] = (option_selection['ERRORS_EUR'] /
                                    option_selection['CF_CLOSE']) * 100
In [43]: option_selection[['MODEL', 'CF_CLOSE', 'ERRORS_EUR', 'ERRORS_%']]
Out[43]: MODEL CF_CLOSE ERRORS_EUR ERRORS_%
        43 647.428189 642.6 4.828189 0.751352
        45 607.402796 604.4 3.002796 0.496823
        47 568.461370 567.1 1.361370 0.240058
        49 530.703659 530.4 0.303659 0.057251
        51 494.093839 494.8 -0.706161 -0.142716
        53 458.718401 460.3 -1.581599 -0.343602
        55 424.650128 426.8 -2.149872 -0.503719
        57 392.023241 394.4 -2.376759 -0.602627
        59 360.728543 363.3 -2.571457 -0.707805
        61 330.727256 333.3 -2.572744 -0.771900
        63 302.117223 304.8 -2.682777 -0.880176
        65 274.984740 277.5 -2.515260 -0.906400
        67 249.501807 251.7 -2.198193 -0.873338
        69 225.678695 227.3 -1.621305 -0.713289
        71 203.490065 204.1 -0.609935 -0.298841
        73 182.947468 182.4 0.547468 0.300147
        75 163.907583 162.0 1.907583 1.177520
        77 146.259349 142.9 3.359349 2.350839
        79 129.909743 125.4 4.509743 3.596286
        81 114.852425 109.4 5.452425 4.983935
In [44]: round(option_selection['ERRORS_EUR'].mean(), 3)
```

```
Out[44]: 0.184
```

In [45]: round(option\_selection['ERRORS\_%'].mean(), 3)

```
Out[45]: 0.36
```

The average pricing error in EUR.

The average pricing error in percent.

Figure 21-4 visualizes the valuation results and errors:

```
In [46]: fix, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(10, 10))
         strikes = option_selection['STRIKE_PRC'].values
         ax1.plot(strikes, option_selection['CF_CLOSE'], label='market quotes')
         ax1.plot(strikes, option_selection['MODEL'], 'ro', label='model values')
         ax1.set_ylabel('option values')
         ax1.legend(loc=0)
         wi = 15
         ax2.bar(strikes - wi / 2., option_selection['ERRORS_EUR'], width=wi)
         ax2.set_ylabel('errors [EUR]')
         ax3.bar(strikes - wi / 2., option_selection['ERRORS_%'], width=wi)
         ax3.set_ylabel('errors [%]')
         ax3.set_xlabel('strikes');
```

### **CALIBRATION SPEED**

The calibration of an option pricing model to market data in general requires the recalculation of hundreds or even thousands of option values. This is therefore typically done based on analytical pricing formulae. Here, the calibration procedure relies on Monte Carlo simulation as the pricing method, which is computationally more demanding compared to analytical methods. Nevertheless, the calibration procedure does not take "too long" even on a typical notebook. The use of parallelization techniques, for instance, can speed up the calibration considerably.

![](_page_17_Figure_0.jpeg)

*Figure 21-4. Model values and market quotes after calibration*

# **Portfolio Valuation**

Being equipped with a calibrated model reflecting realities in the financial markets as represented by market quotes of liquidly traded options enables one to model and value non-traded options and derivatives. The idea is that calibration "infuses" the correct risk-neutral martingale measure into the model via optimal parameters. Based on this measure, the machinery of the Fundamental Theorem of Asset Pricing can then be applied to contingent claims beyond those used for the calibration.

This section considers a portfolio of American put options on the DAX 30 index. There are no such options available that are liquidly traded on exchanges. For simplicity, it is assumed that the American put options have the same maturity as the European call options used for the calibration. Similarly, the same strikes are assumed.

## **Modeling Option Positions**

First, the market environment for the underlying risk factor, the DAX 30 stock index, is modeled with the optimal parameters from the calibration being used:

```
In [47]: me_dax = dx.market_environment('me_dax', pricing_date)
         me_dax.add_constant('initial_value', initial_value)
         me_dax.add_constant('final_date', pricing_date)
         me_dax.add_constant('currency', 'EUR')
In [48]: me_dax.add_constant('volatility', opt_local[0])
         me_dax.add_constant('lambda', opt_local[1])
         me_dax.add_constant('mu', opt_local[2])
         me_dax.add_constant('delta', opt_local[3])
In [49]: me_dax.add_constant('model', 'jd')
```

This adds the optimal parameters from the calibration.

Second, the option positions and the associated environments are defined and stored in two separate dict objects:

```
In [50]: payoff_func = 'np.maximum(strike - instrument_values, 0)'
In [51]: shared = dx.market_environment('share', pricing_date)
         shared.add_constant('maturity', maturity)
         shared.add_constant('currency', 'EUR')
In [52]: option_positions = {}
         option_environments = {}
         for option in option_selection.index:
             option_environments[option] = dx.market_environment(
                 'am_put_%d' % option, pricing_date)
             strike = option_selection['STRIKE_PRC'].loc[option]
             option_environments[option].add_constant('strike', strike)
             option_environments[option].add_environment(shared)
             option_positions['am_put_%d' % strike] = \
                             dx.derivatives_position(
                                 'am_put_%d' % strike,
                                 quantity=np.random.randint(10, 50),
                                 underlying='dax_model',
                                 mar_env=option_environments[option],
                                 otype='American',
                                 payoff_func=payoff_func)
```

Defines a shared dx.market\_environment object as the basis for all optionspecific environments.

Defines and stores a new dx.market\_environment object for the relevant American put option.

Defines and stores the strike price parameter for the option.

Adds the elements from the shared dx.market\_environment object to the option-specific one.

Defines the dx.derivatives\_position object with a randomized quantity.

## **The Options Portfolio**

To value the portfolio with all the American put options, a valuation environment is needed. It contains the major parameters for the estimation of position values and risk statistics:

```
In [53]: val_env = dx.market_environment('val_env', pricing_date)
       val_env.add_constant('starting_date', pricing_date)
       val_env.add_constant('final_date', pricing_date)
       val_env.add_curve('discount_curve', csr)
       val_env.add_constant('frequency', 'B')
       val_env.add_constant('paths', 25000)
In [54]: underlyings = {'dax_model' : me_dax}
In [55]: portfolio = dx.derivatives_portfolio('portfolio', option_positions,
                                     val_env, underlyings)
In [56]: %time results = portfolio.get_statistics(fixed_seed=True)
       CPU times: user 1min 5s, sys: 2.91 s, total: 1min 8s
       Wall time: 38.2 s
In [57]: results.round(1)
Out[57]: name quant. value curr. pos_value pos_delta pos_vega
       0 am_put_12050 33 151.6 EUR 5002.8 -4.7 38206.9
       1 am_put_12100 38 161.5 EUR 6138.4 -5.7 51365.2
       2 am_put_12150 20 171.3 EUR 3426.8 -3.3 27894.5
       3 am_put_12200 12 183.9 EUR 2206.6 -2.2 18479.7
       4 am_put_12250 37 197.4 EUR 7302.8 -7.3 59423.5
       5 am_put_12300 37 212.3 EUR 7853.9 -8.2 65911.9
       6 am_put_12350 36 228.4 EUR 8224.1 -9.0 70969.4
       7 am_put_12400 16 244.3 EUR 3908.4 -4.3 32871.4
       8 am_put_12450 17 262.7 EUR 4465.6 -5.1 37451.2
       9 am_put_12500 16 283.4 EUR 4534.8 -5.2 36158.2
       10 am_put_12550 38 305.3 EUR 11602.3 -13.3 86869.9
       11 am_put_12600 10 330.4 EUR 3303.9 -3.9 22144.5
       12 am_put_12650 38 355.5 EUR 13508.3 -16.0 89124.8
       13 am_put_12700 40 384.2 EUR 15367.5 -18.6 90871.2
       14 am_put_12750 13 413.5 EUR 5375.7 -6.5 28626.0
       15 am_put_12800 49 445.0 EUR 21806.6 -26.3 105287.3
       16 am_put_12850 30 477.4 EUR 14321.8 -17.0 60757.2
       17 am_put_12900 33 510.3 EUR 16840.1 -19.7 69163.6
       18 am_put_12950 40 544.4 EUR 21777.0 -24.9 80472.3
       19 am_put_13000 35 582.3 EUR 20378.9 -22.9 66522.6
In [58]: results[['pos_value','pos_delta','pos_vega']].sum().round(1)
Out[58]: pos_value 197346.2
       pos_delta -224.0
       pos_vega 1138571.1
```

dtype: float64

The final\_date parameter is later reset to the final maturity date over all options in the portfolio.

The American put options in the portfolio are all written on the same underlying risk factor, the DAX 30 stock index.

This instantiates the dx.derivatives\_portfolio object.

The estimation of all statistics takes a little while, since it is all based on Monte Carlo simulation and such estimations are particularly compute-intensive for American options due to the application of the Least-Squares Monte Carlo (LSM) algorithm. Because we are dealing with long positions of American put options only, the portfolio is short delta and long vega.

# **Python Code**

The following presents code to retrieve options data for the German DAX 30 stock index from the Eikon Data API: In [1]: **import eikon as ek import pandas as pd import datetime as dt import configparser as cp** In [2]: cfg = cp.ConfigParser() cfg.read('eikon.cfg') Out[2]: ['eikon.cfg'] In [3]: ek.set\_app\_id(cfg['eikon']['app\_id']) In [4]: fields = ['CF\_DATE', 'EXPIR\_DATE', 'PUTCALLIND', 'STRIKE\_PRC', 'CF\_CLOSE', 'IMP\_VOLT'] In [5]: dax = ek.get\_data('0#GDAXN8\*.EX', fields=fields)[0] In [6]: dax.info() <**class** '**pandas**.core.frame.DataFrame'> RangeIndex: 115 entries, 0 to 114 Data columns (total 7 columns): Instrument 115 non-null object CF\_DATE 115 non-null object EXPIR\_DATE 114 non-null object PUTCALLIND 114 non-null object STRIKE\_PRC 114 non-null float64 CF\_CLOSE 115 non-null float64 IMP\_VOLT 114 non-null float64 dtypes: float64(3), object(4) memory usage: 6.4+ KB In [7]: dax['Instrument'] = dax['Instrument'].apply( **lambda** x: x.replace('/', '')) In [8]: dax.set\_index('Instrument').head(10) Out[8]: CF\_DATE EXPIR\_DATE PUTCALLIND STRIKE\_PRC CF\_CLOSE \ Instrument .GDAXI 2018-04-27 None None NaN 12500.47 GDAX105000G8.EX 2018-04-27 2018-07-20 CALL 10500.0 2040.80 GDAX105000S8.EX 2018-04- 27 2018-07-20 PUT 10500.0 32.00 GDAX108000G8.EX 2018-04-27 2018-07- 20 CALL 10800.0 1752.40 GDAX108000S8.EX 2018-04-26 2018-07-20 PUT 10800.0 43.80 GDAX110000G8.EX 2018-04-27 2018-07-20 CALL 11000.0 1562.80 GDAX110000S8.EX 2018-04-27 2018-07-20 PUT 11000.0 54.50 GDAX111500G8.EX 2018-04-27 2018-07-20 CALL 11150.0 1422.50 GDAX111500S8.EX 2018-04-27 2018-07-20 PUT 11150.0 64.30 GDAX112000G8.EX 2018-04-27 2018-07-20 CALL 11200.0 1376.10 IMP\_VOLT Instrument .GDAXI NaN GDAX105000G8.EX 23.59 GDAX105000S8.EX 23.59 GDAX108000G8.EX 22.02 GDAX108000S8.EX 22.02 GDAX110000G8.EX 21.00 GDAX110000S8.EX 21.00 GDAX111500G8.EX 20.24 GDAX111500S8.EX 20.25 GDAX112000G8.EX 19.99 In [9]: dax.to\_csv('../../source/tr\_eikon\_option\_data.csv')

Imports the eikon Python wrapper package.

Reads the login credentials for the Eikon Data API.

Defines the data fields to be retrieved.

Retrieves options data for the July 2018 expiry.

Replaces the slash character / in the instrument names.

Writes the data set as a CSV file.

# **Conclusion**

This chapter presents a larger, realistic use case for the application of the DX analytics package to the valuation of a portfolio of non-traded American options on the German DAX 30 stock index. The chapter addresses three main tasks typically involved in any real-world derivatives analytics application:

### *Obtaining data*

Current, correct market data builds the basis of any modeling and valuation effort in derivatives analytics; one needs index data as well as options data for the DAX 30.

### *Model calibration*

To value, manage, and hedge non-traded options and derivatives in a market-consistent fashion, one has to calibrate the parameters of an appropriate model (simulation object) to the relevant option market quotes (relevant with regard to maturity and strikes). The model of choice is the jump diffusion model, which is in some cases appropriate for modeling a stock index; the calibration results are quite good although the model only offers three degrees of freedom (lambda as the jump intensity, mu as the expected jump size, and delta as the variability of the jump size).

### *Portfolio valuation*

Based on the market data and the calibrated model, a portfolio with the American put options on the DAX 30 index was modeled and major statistics (position values, deltas, and vegas) were estimated.

The realistic use case in this chapter shows the flexibility and the power of the DX package; it essentially allows one to address the major analytical tasks with regard to derivatives. The very approach and architecture make the application largely comparable to the benchmark case of a Black-Scholes-Merton analytical formula for European options. Once the valuation objects are defined, one can use them in a similar way as an analytical formula — despite the fact that under the hood, computationally demanding and memory-intensive algorithms are applied.
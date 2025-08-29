# **Chapter 20. Portfolio Valuation**

Price is what you pay. Value is what you get. Warren Buffet

By now, the whole approach for building the DX derivatives analytics package and its associated benefits — should be clear. By strictly relying on Monte Carlo simulation as the only numerical method, the approach accomplishes an almost complete modularization of the analytics package: Discounting

The relevant risk-neutral discounting is taken care of by an instance of the dx.constant\_short\_rate class.

*Relevant data*

Relevant data, parameters, and other input are stored in (several) instances of the dx.market\_environment class.

*Simulation objects*

Relevant risk factors (underlyings) are modeled as instances of one of three simulation classes:

- dx.geometric\_brownian\_motion
- dx.jump\_diffusion
- dx.square\_root\_diffusion

### *Valuation objects*

Options and derivatives to be valued are modeled as instances of one of two valuation classes:

- dx.valuation\_mcs\_european
- dx.valuation\_mcs\_american

One last step is missing: the valuation of possibly complex *portfolios* of options and derivatives. To this end, the following requirements shall be satisfied:

Nonredundancy

Every risk factor (underlying) is modeled only once and potentially used by multiple valuation objects.

### *Correlations*

Correlations between risk factors have to be accounted for.

### *Positions*

An option position, for example, consists of a certain number of option contracts.

However, although it is in principle allowed (it is in fact even required) to provide a currency for both simulation and valuation objects, the following code assumes that portfolios are denominated in a *single currency* only. This simplifies the aggregation of values within a portfolio significantly, because one can abstract from exchange rates and currency risks.

The chapter presents two new classes: a simple one to model a *derivatives position*, and a more complex one to model and value a *derivatives portfolio*. It is structured as follows: "Derivatives Positions"

This section introduces the class to model a single derivatives position.

### *"Derivatives Portfolios"*

This section introduces the core class to value a portfolio of potentially many derivatives positions.

# **Derivatives Positions**

In principle, a *derivatives position* is nothing more than a combination of a valuation object and a quantity for the instrument modeled.

### **The Class**

The code that follows presents the class to model a derivatives position. It is mainly a container for data and objects. In addition, it provides a get\_info() method, printing the data and object information stored in an instance of the class:

```
#
# DX Package
#
# Portfolio -- Derivatives Position Class
#
# derivatives_position.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
class derivatives_position(object):
    ''' Class to model a derivatives position.
    Attributes
    ==========
    name: str
        name of the object
    quantity: float
        number of assets/derivatives making up the position
    underlying: str
        name of asset/risk factor for the derivative
    mar_env: instance of market_environment
        constants, lists, and curves relevant for valuation_class
    otype: str
        valuation class to use
    payoff_func: str
        payoff string for the derivative
    Methods
    =======
    get_info:
        prints information about the derivatives position
    '''def __init__(self, name, quantity, underlying, mar_env,
                 otype, payoff_func):
        self.name = name
        self.quantity = quantity
        self.underlying = underlying
        self.mar_env = mar_env
        self.otype = otype
        self.payoff_func = payoff_func
    def get_info(self):
        print('NAME')
        print(self.name, '\n')
        print('QUANTITY')
```

```
print(self.quantity, '\n')
print('UNDERLYING')
print(self.underlying, '\n')
print('MARKET ENVIRONMENT')
print('\n**Constants**')
for key, value in self.mar_env.constants.items():
    print(key, value)
print('\n**Lists**')
for key, value in self.mar_env.lists.items():
    print(key, value)
print('\n**Curves**')
for key in self.mar_env.curves.items():
    print(key, value)
print('\nOPTION TYPE')
print(self.otype, '\n')
print('PAYOFF FUNCTION')
print(self.payoff_func)
```

To define a derivatives position the following information is required, which is almost the same as for the instantiation of a valuation class:

*name*

Name of the position as a str object

*quantity*

Quantity of options/derivatives

*underlying*

Instance of simulation object as a risk factor

*mar\_env*

Instance of dx.market\_environment

*otype*

str, either "European" or "American"

*payoff\_func*

Payoff as a Python str object

### **A Use Case**

The following interactive session illustrates the use of the class. However, first a definition of a simulation object is needed (but not in full; only the most important, object-specific information is required):

```
In [99]: from dx_valuation import *
In [100]: me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))
In [101]: me_gbm.add_constant('initial_value', 36.)
          me_gbm.add_constant('volatility', 0.2)
          me_gbm.add_constant('currency', 'EUR')
In [102]: me_gbm.add_constant('model', 'gbm')
```

The dx.market\_environment object for the underlying.

The model type needs to be specified here.

Similarly, for the definition of the derivatives position, one does not need a "complete" dx.market\_environment object. Missing information is provided later (during the portfolio valuation), when the simulation object is instantiated:

```
In [103]: from derivatives_position import derivatives_position
In [104]: me_am_put = market_environment('me_am_put', dt.datetime(2020, 1, 1))
In [105]: me_am_put.add_constant('maturity', dt.datetime(2020, 12, 31))
          me_am_put.add_constant('strike', 40.)
          me_am_put.add_constant('currency', 'EUR')
In [106]: payoff_func = 'np.maximum(strike - instrument_values, 0)'
In [107]: am_put_pos = derivatives_position(
                       name='am_put_pos',
                       quantity=3,
                       underlying='gbm',
                       mar_env=me_am_put,
                       otype='American',
                       payoff_func=payoff_func)
In [108]: am_put_pos.get_info()
          NAME
          am_put_pos
          QUANTITY
          3
```

```
UNDERLYING
gbm
MARKET ENVIRONMENT
**Constants**
maturity 2020-12-31 00:00:00
strike 40.0
currency EUR
**Lists**
**Curves**
OPTION TYPE
American
PAYOFF FUNCTION
np.maximum(strike - instrument_values, 0)
```

The dx.market\_environment object for the derivative.

The payoff function of the derivative.

The instantiation of the derivatives\_position object.

# **Derivatives Portfolios**

From a portfolio perspective, a *relevant market* is mainly composed of the relevant risk factors (underlyings) and their correlations, as well as the derivatives and derivatives positions, respectively, to be valued. Theoretically, the analysis to follow now deals with a general market model ℳ as defined in Chapter 17, and applies the Fundamental Theorem of Asset Pricing (with its corollaries) to it. 1

### **The Class**

A somewhat complex Python class implementing a *portfolio valuation* based on the Fundamental Theorem of Asset Pricing — taking into account multiple relevant risk factors and multiple derivatives positions — is presented next. The class is documented inline, especially during passages that implement functionality specific to the purpose at hand:

```
#
# DX Package
#
# Portfolio -- Derivatives Portfolio Class
#
# derivatives_portfolio.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
import pandas as pd
from dx_valuation import *
# models available for risk factor modeling
models = {'gbm': geometric_brownian_motion,
          'jd': jump_diffusion,
          'srd': square_root_diffusion}
# allowed exercise types
otypes = {'European': valuation_mcs_european,
          'American': valuation_mcs_american}
class derivatives_portfolio(object):
    ''' Class for modeling and valuing portfolios of derivatives positions.
    Attributes
    ==========
```

*name: str name of the object positions: dict dictionary of positions (instances of derivatives\_position class) val\_env: market\_environment market environment for the valuation assets: dict dictionary of market environments for the assets*

```
correlations: list
    correlations between assets
fixed_seed: bool
    flag for fixed random number generator seed
Methods
=======
get_positions:
    prints information about the single portfolio positions
get_statistics:
    returns a pandas DataFrame object with portfolio statistics
'''def __init__(self, name, positions, val_env, assets,
             correlations=None, fixed_seed=False):
    self.name = name
    self.positions = positions
    self.val_env = val_env
    self.assets = assets
    self.underlyings = set()
    self.correlations = correlations
    self.time_grid = None
    self.underlying_objects = {}
    self.valuation_objects = {}
    self.fixed_seed = fixed_seed
    self.special_dates = []
    for pos in self.positions:
        # determine earliest starting_date
        self.val_env.constants['starting_date'] = \
            min(self.val_env.constants['starting_date'],
                positions[pos].mar_env.pricing_date)
        # determine latest date of relevance
        self.val_env.constants['final_date'] = \
            max(self.val_env.constants['final_date'],
                positions[pos].mar_env.constants['maturity'])
        # collect all underlyings and
        # add to set (avoids redundancy)
        self.underlyings.add(positions[pos].underlying)
    # generate general time grid
    start = self.val_env.constants['starting_date']
    end = self.val_env.constants['final_date']
    time_grid = pd.date_range(start=start, end=end,
                              freq=self.val_env.constants['frequency']
                              ).to_pydatetime()
    time_grid = list(time_grid)
    for pos in self.positions:
        maturity_date = positions[pos].mar_env.constants['maturity']
        if maturity_date not in time_grid:
            time_grid.insert(0, maturity_date)
            self.special_dates.append(maturity_date)
    if start not in time_grid:
```

```
time_grid.insert(0, start)
```

```
if end not in time_grid:
    time_grid.append(end)
# delete duplicate entries
time_grid = list(set(time_grid))
# sort dates in time_grid
time_grid.sort()
self.time_grid = np.array(time_grid)
self.val_env.add_list('time_grid', self.time_grid)
if correlations is not None:
    # take care of correlations
    ul_list = sorted(self.underlyings)
    correlation_matrix = np.zeros((len(ul_list), len(ul_list)))
    np.fill_diagonal(correlation_matrix, 1.0)
    correlation_matrix = pd.DataFrame(correlation_matrix,
                                      index=ul_list, columns=ul_list)
    for i, j, corr in correlations:
        corr = min(corr, 0.999999999999)
        # fill correlation matrix
        correlation_matrix.loc[i, j] = corr
        correlation_matrix.loc[j, i] = corr
    # determine Cholesky matrix
    cholesky_matrix = np.linalg.cholesky(np.array(correlation_matrix))
    # dictionary with index positions for the
    # slice of the random number array to be used by
    # respective underlying
    rn_set = {asset: ul_list.index(asset)
              for asset in self.underlyings}
    # random numbers array, to be used by
    # all underlyings (if correlations exist)
    random_numbers = sn_random_numbers((len(rn_set),
                                        len(self.time_grid),
                                        self.val_env.constants['paths']),
                                       fixed_seed=self.fixed_seed)
    # add all to valuation environment that is
    # to be shared with every underlying
    self.val_env.add_list('cholesky_matrix', cholesky_matrix)
    self.val_env.add_list('random_numbers', random_numbers)
    self.val_env.add_list('rn_set', rn_set)
for asset in self.underlyings:
    # select market environment of asset
    mar_env = self.assets[asset]
    # add valuation environment to market environment
    mar_env.add_environment(val_env)
    # select right simulation class
    model = models[mar_env.constants['model']]
    # instantiate simulation object
    if correlations is not None:
        self.underlying_objects[asset] = model(asset, mar_env,
                                               corr=True)
    else:
```

```
self.underlying_objects[asset] = model(asset, mar_env,
                                                    corr=False)
    for pos in positions:
        # select right valuation class (European, American)
        val_class = otypes[positions[pos].otype]
        # pick market environment and add valuation environment
        mar_env = positions[pos].mar_env
        mar_env.add_environment(self.val_env)
        # instantiate valuation class
        self.valuation_objects[pos] = \
            val_class(name=positions[pos].name,
                      mar_env=mar_env,
                      underlying=self.underlying_objects[
                positions[pos].underlying],
            payoff_func=positions[pos].payoff_func)
def get_positions(self):
    ''' Convenience method to get information about
    all derivatives positions in a portfolio. '''
    for pos in self.positions:
        bar = '\n' + 50 * '-'
        print(bar)
        self.positions[pos].get_info()
        print(bar)
def get_statistics(self, fixed_seed=False):
    ''' Provides portfolio statistics. '''
    res_list = []
    # iterate over all positions in portfolio
    for pos, value in self.valuation_objects.items():
        p = self.positions[pos]
        pv = value.present_value(fixed_seed=fixed_seed)
        res_list.append([
            p.name,
            p.quantity,
            # calculate all present values for the single instruments
            pv,
            value.currency,
            # single instrument value times quantity
            pv * p.quantity,
            # calculate delta of position
            value.delta() * p.quantity,
            # calculate vega of position
            value.vega() * p.quantity,
        ])
    # generate a pandas DataFrame object with all results
    res_df = pd.DataFrame(res_list,
                          columns=['name', 'quant.', 'value', 'curr.',
                                    'pos_value', 'pos_delta', 'pos_vega'])
    return res_df
```

### **OBJECT ORIENTATION**

The class dx.derivatives\_portfolio illustrates a number of benefits of object orientation as mentioned in Chapter 6. At first inspection, it might look like a complex piece of Python code. However, the financial problem that it solves is a pretty complex one and it provides the flexibility to address a large number of different use cases. It is hard to imagine how all this could be achieved without the use of object-oriented programming and Python classes.

### **A Use Case**

In terms of the DX analytics package, the modeling capabilities are, on a high level, restricted to a combination of a simulation and a valuation class. There are a total of six possible combinations:

```
models = {'gbm' : geometric_brownian_motion,
          'jd' : jump_diffusion
          'srd': square_root_diffusion}
otypes = {'European' : valuation_mcs_european,
          'American' : valuation_mcs_american}
```

The interactive use case that follows combines selected elements to define two different derivatives positions that are then combined into a portfolio.

Recall the derivatives\_position class with the gbm and am\_put\_pos objects from the previous section. To illustrate the use of the derivatives\_portfolio class, we'll define both an additional underlying and an additional options position. First, a dx.jump\_diffusion object:

```
In [109]: me_jd = market_environment('me_jd', me_gbm.pricing_date)
In [110]: me_jd.add_constant('lambda', 0.3)
          me_jd.add_constant('mu', -0.75)
          me_jd.add_constant('delta', 0.1)
          me_jd.add_environment(me_gbm)
In [111]: me_jd.add_constant('model', 'jd')
```

Adds jump diffusion-specific parameters.

Adds other parameters from gbm.

Needed for portfolio valuation.

Second, a European call option based on this new simulation object:

```
In [112]: me_eur_call = market_environment('me_eur_call', me_jd.pricing_date)
In [113]: me_eur_call.add_constant('maturity', dt.datetime(2020, 6, 30))
          me_eur_call.add_constant('strike', 38.)
```

```
me_eur_call.add_constant('currency', 'EUR')
In [114]: payoff_func = 'np.maximum(maturity_value - strike, 0)'
In [115]: eur_call_pos = derivatives_position(
                       name='eur_call_pos',
                       quantity=5,
                       underlying='jd',
                       mar_env=me_eur_call,
                       otype='European',
                       payoff_func=payoff_func)
```

From a portfolio perspective, the relevant market now is as shown in the following in underlyings and positions. For the moment, the definitions do not include correlations between the underlyings. Compiling a dx.market\_environment for the portfolio valuation is the last step before the instantiation of a derivatives\_portfolio object:

```
In [116]: underlyings = {'gbm': me_gbm, 'jd' : me_jd}
          positions = {'am_put_pos' : am_put_pos,
                       'eur_call_pos' : eur_call_pos}
In [117]: csr = constant_short_rate('csr', 0.06)
In [118]: val_env = market_environment('general', me_gbm.pricing_date)
          val_env.add_constant('frequency', 'W')
          val_env.add_constant('paths', 25000)
          val_env.add_constant('starting_date', val_env.pricing_date)
          val_env.add_constant('final_date', val_env.pricing_date)
          val_env.add_curve('discount_curve', csr)
In [119]: from derivatives_portfolio import derivatives_portfolio
In [120]: portfolio = derivatives_portfolio(
                          name='portfolio',
                          positions=positions,
                          val_env=val_env,
                          assets=underlyings,
                          fixed_seed=False)
```

Relevant risk factors.

Relevant portfolio postions.

Unique discounting object for the portfolio valuation.

final\_date is not yet known; therefore, set pricing\_date as preliminary

value.

Instantiation of the derivatives\_portfolio object.

Now one can harness the power of the valuation class and easily get important statistics for the derivatives\_portfolio object just defined. The *sum* of the position values, deltas, and vegas is also easily calculated. This portfolio is slightly long delta (almost neutral) and long vega:

```
In [121]: %time portfolio.get_statistics(fixed_seed=False)
         CPU times: user 4.68 s, sys: 409 ms, total: 5.09 s
         Wall time: 14.5 s
Out[121]:
              name quant. value curr. pos_value pos_delta pos_vega
   0 am_put_pos 3 4.458891 EUR 13.376673 -2.0430 31.7850
   1 eur_call_pos 5 2.828634 EUR 14.143170 3.2525 42.2655
In [122]: portfolio.get_statistics(fixed_seed=False)[
             ['pos_value', 'pos_delta', 'pos_vega']].sum()
Out[122]: pos_value 27.502731
         pos_delta 1.233500
         pos_vega 74.050500
         dtype: float64
In [123]: portfolio.get_positions()
         ...
In [124]: portfolio.valuation_objects['am_put_pos'].present_value()
Out[124]: 4.453187
In [125]: portfolio.valuation_objects['eur_call_pos'].delta()
Out[125]: 0.6514
```

Aggregation of single position values.

This method call would create a rather lengthy output about all positions.

The present value estimate for a single position.

The delta estimate for a single position.

The derivatives portfolio valuation is conducted based on the assumption that the risk factors are *not* correlated. This is easily verified by inspecting two simulated

paths (see [Figure](#page-16-0) 20-1), one for each simulation object:

In [126]: path\_no = 888

<span id="page-16-0"></span>![](_page_16_Figure_1.jpeg)

*Figure 20-1. Noncorrelated risk factors (two sample paths)*

Now consider the case where the two risk factors are highly positively correlated. In this case, there is no direct influence on the values of the single positions in the portfolio:

```
In [128]: correlations = [['gbm', 'jd', 0.9]]
In [129]: port_corr = derivatives_portfolio(
                          name='portfolio',
                          positions=positions,
                          val_env=val_env,
```

```
assets=underlyings,
                      correlations=correlations,
                      fixed_seed=True)
In [130]: port_corr.get_statistics()
Out[130]:
             name quant. value curr. pos_value pos_delta pos_vega
   0 am_put_pos 3 4.458556 EUR 13.375668 -2.0376 30.8676
   1 eur_call_pos 5 2.817813 EUR 14.089065 3.3375 42.2340
```

However, the correlation takes place behind the scenes. The graphical illustration in [Figure](#page-17-0) 20-2 takes the same combination of paths as before. The two paths now almost move in parallel:

```
In [131]: path_gbm = port_corr.underlying_objects['gbm'].\
                      get_instrument_values()[:, path_no]
          path_jd = port_corr.underlying_objects['jd'].\
                      get_instrument_values()[:, path_no]
In [132]: plt.figure(figsize=(10, 6))
          plt.plot(portfolio.time_grid, path_gbm, 'r', label='gbm')
          plt.plot(portfolio.time_grid, path_jd, 'b', label='jd')
          plt.xticks(rotation=30)
          plt.legend(loc=0);
```

<span id="page-17-0"></span>![](_page_17_Figure_3.jpeg)

*Figure 20-2. Correlated risk factors (two sample paths)*

As a last numerical and conceptual example, consider the *frequency distribution of the portfolio present value*. This is something impossible to generate in general with other approaches, like the application of analytical formulae or the binomial option pricing model. Setting the parameter full=True causes the complete set of present values per option position to be returned after the present value estimation:

```
In [133]: pv1 = 5 * port_corr.valuation_objects['eur_call_pos'].\
                    present_value(full=True)[1]
         pv1
Out[133]: array([ 0. , 39.71423714, 24.90720272, ..., 0. ,
                 6.42619093, 8.15838265])
In [134]: pv2 = 3 * port_corr.valuation_objects['am_put_pos'].\
                    present_value(full=True)[1]
         pv2
Out[134]: array([21.31806027, 10.71952869, 19.89804376, ..., 21.39292703,
                17.59920608, 0. ])
```

First, compare the frequency distribution of the two positions. The payoff profiles of the two positions, as displayed in Figure 20-3, are quite different. Note that the values for both the x-and y-axes are limited for better readability:

```
In [135]: plt.figure(figsize=(10, 6))
          plt.hist([pv1, pv2], bins=25,
                   label=['European call', 'American put']);
          plt.axvline(pv1.mean(), color='r', ls='dashed',
                      lw=1.5, label='call mean = %4.2f' % pv1.mean())
          plt.axvline(pv2.mean(), color='r', ls='dotted',
                      lw=1.5, label='put mean = %4.2f' % pv2.mean())
          plt.xlim(0, 80); plt.ylim(0, 10000)
          plt.legend();
```

![](_page_19_Figure_0.jpeg)

*Figure 20-3. Frequency distribution of present values of the two positions*

Figure 20-4 finally shows the full frequency distribution of the portfolio present values. One can clearly see the offsetting diversification effects of combining a call with a put option:

```
In [136]: pvs = pv1 + pv2
          plt.figure(figsize=(10, 6))
          plt.hist(pvs, bins=50, label='portfolio');
          plt.axvline(pvs.mean(), color='r', ls='dashed',
                      lw=1.5, label='mean = %4.2f' % pvs.mean())
          plt.xlim(0, 80); plt.ylim(0, 7000)
          plt.legend();
```

![](_page_20_Figure_0.jpeg)

*Figure 20-4. Portfolio frequency distribution of present values*

What impact does the correlation between the two risk factors have on the risk of the portfolio, measured in the standard deviation of the present values? This can be answered by the following two estimations:

```
In [137]: pvs.std()
Out[137]: 16.723724772741118
In [138]: pv1 = (5 * portfolio.valuation_objects['eur_call_pos'].
                      present_value(full=True)[1])
          pv2 = (3 * portfolio.valuation_objects['am_put_pos'].
                      present_value(full=True)[1])
          (pv1 + pv2).std()
Out[138]: 21.80498672323975
```

Standard deviation of portfolio values *with* correlation.

Standard deviation of portfolio values *without* correlation.

Although the mean value stays constant (ignoring numerical deviations), correlation obviously significantly decreases the portfolio risk when measured in this way. Again, this is an insight that it is not really possible to gain when using

alternative numerical methods or valuation approaches.

# **Conclusion**

This chapter addresses the valuation and risk management of a portfolio of multiple derivatives positions dependent on multiple (possibly correlated) risk factors. To this end, a new class called derivatives\_position is introduced to model an options or derivatives position. The main focus, however, lies on the derivatives\_portfolio class, which implements some more complex tasks. For example, the class takes care of:

- *Correlations* between risk factors (the class generates a single consistent set of random numbers for the simulation of all risk factors)
- *Instantiation of simulation objects* given the single market environments and the general valuation environment, as well as the derivatives positions
- *Generation of portfolio statistics* based on all the assumptions, the risk factors involved, and the terms of the derivatives positions

The examples presented in this chapter can only show some simple versions of derivatives portfolios that can be managed and valued with the DX package developed so far and the derivatives\_portfolio class. Natural extensions to the DX package would be the addition of more sophisticated financial models, like a stochastic volatility model, and multi-risk valuation classes to model and value derivatives dependent on multiple risk factors (like a European basket option or an American maximum call option, to name just two). At this stage, the modular modeling using OOP and the application of a valuation framework as general as the Fundamental Theorem of Asset Pricing (or "global valuation") play out their strengths: the nonredundant modeling of the risk factors and the accounting for the correlations between them will then also have a direct influence on the values and Greeks of multi-risk derivatives.

The following is a final wrapper module bringing all the components of the DX analytics package together for a single import statement:

```
#
# DX Package
#
# All components
#
# dx_package.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
from dx_valuation import *
from derivatives_position import derivatives_position
from derivatives_portfolio import derivatives_portfolio
```

And here is the now-complete *\_\_init\_\_.py* file for the *dx* folder:

```
#
# DX Package
# packaging file
# __init__.py
#
import numpy as np
import pandas as pd
import datetime as dt
```

*# frame* **from get\_year\_deltas import** get\_year\_deltas **from constant\_short\_rate import** constant\_short\_rate **from market\_environment import** market\_environment **from plot\_option\_stats import** plot\_option\_stats

*# simulation* **from sn\_random\_numbers import** sn\_random\_numbers **from simulation\_class import** simulation\_class **from geometric\_brownian\_motion import** geometric\_brownian\_motion **from jump\_diffusion import** jump\_diffusion **from square\_root\_diffusion import** square\_root\_diffusion

*# valuation* **from valuation\_class import** valuation\_class **from valuation\_mcs\_european import** valuation\_mcs\_european **from valuation\_mcs\_american import** valuation\_mcs\_american

```
# portfolio
from derivatives_position import derivatives_position
from derivatives_portfolio import derivatives_portfolio
```

## **Further Resources**

As for the preceding chapters on the DX derivatives analytics package, Glasserman (2004) is a comprehensive resource for Monte Carlo simulation in the context of financial engineering and applications. Hilpisch (2015) also provides Python-based implementations of the most important Monte Carlo algorithms:

- Glasserman, Paul (2004). *Monte Carlo Methods in Financial Engineering*. New York: Springer.
- Hilpisch, Yves (2015). *[Derivatives](http://dawp.tpq.io) Analytics with Python*. Chichester, England: Wiley Finance.

However, there is hardly any research available when it comes to the valuation of (complex) portfolios of derivatives in a consistent, nonredundant fashion by Monte Carlo simulation. A notable exception, at least from a conceptual point of view, is the brief article by Albanese, Gimonet, and White (2010a). There is a bit more detail in the working paper by the same team of authors:

- Albanese, Claudio, Guillaume Gimonet and Steve White (2010a). "Towards a Global [Valuation](http://bit.ly/risk_may_2010) Model". *Risk Magazine*, Vol. 23, No. 5, pp. 68–71.
- Albanese, Claudio, Guillaume Gimonet and Steve White (2010b). "Global Valuation and Dynamic Risk [Management".](http://bit.ly/global_valuation) Working paper.

In practice, the approach chosen here is sometimes called *global valuation* instead of *instrumentspecific valuation*. See Albanese, Gimonet, and White (2010a). 1
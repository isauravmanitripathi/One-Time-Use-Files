# **Chapter 19. Derivatives Valuation**

Derivatives are a huge, complex issue. Judd Gregg

Options and derivatives valuation has long been the domain of the so-called *rocket scientists* on Wall Street — i.e., people with a PhD in physics or a similarly demanding discipline when it comes to the mathematics involved. However, the application of the models by the means of numerical methods like Monte Carlo simulation is generally a little less involved than the theoretical models themselves.

This is particularly true for the valuation of options and derivatives with *European exercise* — i.e., where exercise is only possible at a certain predetermined date. It is a bit less true for options and derivatives with *American exercise*, where exercise is allowed at any point over a prespecified period of time. This chapter introduces and uses the *Least-Squares Monte Carlo* (LSM) algorithm, which has become a benchmark algorithm when it comes to American options valuation based on Monte Carlo simulation.

The current chapter is similar in structure to Chapter 18 in that it first introduces a generic valuation class and then provides two specialized valuation classes, one for European exercise and another for American exercise. The generic valuation class contains methods to numerically estimate the most important Greeks of an option: the *delta* and the *vega*. Therefore, the valuation classes are important not only for valuation purposes, but also for *risk management* purposes.

The chapter is structured as follows:

*"Generic Valuation Class"*

This section introduces the *generic* valuation class from which the specific ones inherit.

*"European Exercise"*

This section is about the valuation class for options and derivatives with *European* exercise.

*"American Exercise"*

This section covers the valuation class for options and derivatives with *American* exercise.

# **Generic Valuation Class**

As with the generic simulation class, one instantiates an object of the valuation class by providing only a few inputs (in this case, four):

*name*

A str object, as a name for the model simulation object

*underlying*

An instance of a simulation class representing the underlying

*mar\_env*

An instance of the dx.market\_environment class

*payoff\_func*

A Python str object containing the payoff function for the option/derivative

The generic class has three methods:

*update()*

Updates selected valuation parameters (attributes)

*delta()*

Calculates a numerical value for the delta of an option/derivative

*vega()*

Calculates the vega of an option/derivative

Equipped with the background knowledge from the previous chapters about the DX package, the generic valuation class as presented here should be almost selfexplanatory; where appropriate, inline comments are also provided. Again, the class is presented in its entirety first, then discussed in more detail:

```
#
# DX Package
#
# Valuation -- Base Class
#
# valuation_class.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
```

*#*

```
class valuation_class(object):
    ''' Basic class for single-factor valuation.
    Attributes
    ==========
    name: str
        name of the object
    underlying: instance of simulation class
        object modeling the single risk factor
    mar_env: instance of market_environment
        market environment data for valuation
    payoff_func: str
        derivatives payoff in Python syntax
        Example: 'np.maximum(maturity_value - 100, 0)'
        where maturity_value is the NumPy vector with
        respective values of the underlying
        Example: 'np.maximum(instrument_values - 100, 0)'
        where instrument_values is the NumPy matrix with
        values of the underlying over the whole time/path grid
    Methods
    =======
    update:
        updates selected valuation parameters
    delta:
        returns the delta of the derivative
    vega:
        returns the vega of the derivative
    '''def __init__(self, name, underlying, mar_env, payoff_func=''):
        self.name = name
        self.pricing_date = mar_env.pricing_date
        try:
            # strike is optional
            self.strike = mar_env.get_constant('strike')
        except:
            pass
        self.maturity = mar_env.get_constant('maturity')
        self.currency = mar_env.get_constant('currency')
        # simulation parameters and discount curve from simulation object
        self.frequency = underlying.frequency
        self.paths = underlying.paths
        self.discount_curve = underlying.discount_curve
        self.payoff_func = payoff_func
        self.underlying = underlying
        # provide pricing_date and maturity to underlying
        self.underlying.special_dates.extend([self.pricing_date,
                                              self.maturity])
    def update(self, initial_value=None, volatility=None,
               strike=None, maturity=None):
        if initial_value is not None:
            self.underlying.update(initial_value=initial_value)
        if volatility is not None:
            self.underlying.update(volatility=volatility)
        if strike is not None:
            self.strike = strike
        if maturity is not None:
            self.maturity = maturity
            # add new maturity date if not in time_grid
```

```
if maturity not in self.underlying.time_grid:
            self.underlying.special_dates.append(maturity)
            self.underlying.instrument_values = None
def delta(self, interval=None, accuracy=4):
    if interval is None:
        interval = self.underlying.initial_value / 50.
    # forward-difference approximation
    # calculate left value for numerical delta
    value_left = self.present_value(fixed_seed=True)
    # numerical underlying value for right value
    initial_del = self.underlying.initial_value + interval
    self.underlying.update(initial_value=initial_del)
    # calculate right value for numerical delta
    value_right = self.present_value(fixed_seed=True)
    # reset the initial_value of the simulation object
    self.underlying.update(initial_value=initial_del - interval)
    delta = (value_right - value_left) / interval
    # correct for potential numerical errors
    if delta < -1.0:
        return -1.0
    elif delta > 1.0:
        return 1.0
    else:
        return round(delta, accuracy)
def vega(self, interval=0.01, accuracy=4):
    if interval < self.underlying.volatility / 50.:
        interval = self.underlying.volatility / 50.
    # forward-difference approximation
    # calculate the left value for numerical vega
    value_left = self.present_value(fixed_seed=True)
    # numerical volatility value for right value
    vola_del = self.underlying.volatility + interval
    # update the simulation object
    self.underlying.update(volatility=vola_del)
    # calculate the right value for numerical vega
    value_right = self.present_value(fixed_seed=True)
    # reset volatility value of simulation object
    self.underlying.update(volatility=vola_del - interval)
    vega = (value_right - value_left) / interval
    return round(vega, accuracy)
```

One topic covered by the generic dx.valuation\_class class is the estimation of Greeks. This is worth taking a closer look at. To this end, assume that a continuously differentiable function is available that represents the present value of an option. The *delta* of the option is then defined as the first partial derivative with respect to the current value of the underlying ; i.e., .

Suppose now that from Monte Carlo valuation (see Chapter 12 and subsequent sections in this chapter) there is a numerical Monte Carlo estimator available for the option value. A numerical approximation for the delta of the

option is then given in [Equation](#page-5-0) 19-1. <sup>1</sup> This is what the delta() method of the generic valuation class implements. The method assumes the existence of a present\_value() method that returns the Monte Carlo estimator given a certain set of parameter values.

<span id="page-5-0"></span>*Equation 19-1. Numerical delta of an option*

$$\overline{\Delta} = \frac{\overline{V}(S_0 + \Delta S, \sigma_0) - \overline{V}(S_0, \sigma_0)}{\Delta S}, \, \Delta S > 0$$

Similarly, the *vega* of the instrument is defined as the first partial derivative of the present value with respect to the current (instantaneous) volatility , i.e., . Again assuming the existence of a Monte Carlo estimator for the

value of the option, [Equation](#page-5-1) 19-2 provides a numerical approximation for the vega. This is what the vega() method of the dx.valuation\_class class implements.

<span id="page-5-1"></span>*Equation 19-2. Numerical vega of an option*

$$\mathbf{V} = \frac{\overline{V}(S_0, \ \sigma_0 + \Delta \sigma) - \overline{V}(S_0, \ \sigma_0)}{\Delta \sigma}, \ \Delta \sigma > 0$$

Note that the discussion of delta and vega is based only on the *existence* of either a differentiable function or a Monte Carlo estimator for the present value of an option. This is the very reason why one can define methods to numerically estimate these quantities without knowledge of the exact definition and numerical implementation of the Monte Carlo estimator.

# **European Exercise**

The first case to which the generic valuation class is specialized is the case of European exercise. To this end, consider the following simplified recipe to generate a Monte Carlo estimator for an option value:

- 1. Simulate the relevant underlying risk factor *S* under the risk-neutral measure *I* times to come up with as many simulated values of the underlying at the maturity of the option *T* — i.e., .
- 2. Calculate the payoff of the option at maturity for every simulated value of the underlying — i.e., .
- 3. Derive the Monte Carlo estimator for the option's present value as .

### **The Valuation Class**

The following code shows the class implementing the present\_value() method based on this recipe. In addition, it contains the method generate\_payoff() to generate the simulated paths and the payoff of the option given the simulated paths. This, of course, builds the very basis for the Monte Carlo estimator:

```
#
# DX Package
#
# Valuation -- European Exercise Class
#
# valuation_mcs_european.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
```

**from valuation\_class import** valuation\_class

```
class valuation_mcs_european(valuation_class):
    ''' Class to value European options with arbitrary payoff
    by single-factor Monte Carlo simulation.
    Methods
    =======
    generate_payoff:
        returns payoffs given the paths and the payoff function
    present_value:
        returns present value (Monte Carlo estimator)
    '''def generate_payoff(self, fixed_seed=False):
        '''Parameters
        ==========
        fixed_seed: bool
            use same/fixed seed for valuation
        '''try:
            # strike is optional
            strike = self.strike
        except:
            pass
        paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed)
        time_grid = self.underlying.time_grid
```

```
try:
        time_index = np.where(time_grid == self.maturity)[0]
        time_index = int(time_index)
    except:
        print('Maturity date not in time grid of underlying.')
    maturity_value = paths[time_index]
    # average value over whole path
    mean_value = np.mean(paths[:time_index], axis=1)
    # maximum value over whole path
    max_value = np.amax(paths[:time_index], axis=1)[-1]
    # minimum value over whole path
    min_value = np.amin(paths[:time_index], axis=1)[-1]
    try:
        payoff = eval(self.payoff_func)
        return payoff
    except:
        print('Error evaluating payoff function.')
def present_value(self, accuracy=6, fixed_seed=False, full=False):
    '''Parameters
    ==========
    accuracy: int
        number of decimals in returned result
    fixed_seed: bool
        use same/fixed seed for valuation
    full: bool
        return also full 1d array of present values
    '''cash_flow = self.generate_payoff(fixed_seed=fixed_seed)
    discount_factor = self.discount_curve.get_discount_factors(
        (self.pricing_date, self.maturity))[0, 1]
    result = discount_factor * np.sum(cash_flow) / len(cash_flow)
    if full:
        return round(result, accuracy), discount_factor * cash_flow
    else:
        return round(result, accuracy)
```

The generate\_payoff() method provides some special objects to be used for the definition of the payoff of the option:

- strike is the *strike* of the option.
- maturity\_value represents the 1D ndarray object with the simulated values of the *underlying at maturity* of the option.
- mean\_value is the *average* of the underlying over a whole path from today until maturity.
- max\_value is the *maximum value* of the underlying over a whole path.

min\_value gives the *minimum value* of the underlying over a whole path.

The last three allow for the efficient handling of options with Asian (i.e., lookback or path-dependent) features.

### **FLEXIBLE PAYOFFS**

The approach taken for the valuation of options and derivatives with European exercise is quite flexible in that arbitrary payoff functions can be defined. This allows, among other things, modeling of derivatives with conditional exercise (e.g., options) as well as unconditional exercise (e.g., forwards). It also allows the inclusion of exotic payoff elements, such as lookback features.

### **A Use Case**

The application of the valuation class dx.valuation\_mcs\_european is best illustrated by a specific use case. However, before a valuation class can be instantiated, an instance of a simulation object — i.e., an underlying for the option to be valued — is needed. From Chapter 18, the

```
dx.geometric_brownian_motion class is used to model the underlying:
```

```
In [64]: me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))
In [65]: me_gbm.add_constant('initial_value', 36.)
         me_gbm.add_constant('volatility', 0.2)
         me_gbm.add_constant('final_date', dt.datetime(2020, 12, 31))
         me_gbm.add_constant('currency', 'EUR')
         me_gbm.add_constant('frequency', 'M')
         me_gbm.add_constant('paths', 10000)
In [66]: csr = constant_short_rate('csr', 0.06)
In [67]: me_gbm.add_curve('discount_curve', csr)
In [68]: gbm = geometric_brownian_motion('gbm', me_gbm)
```

In addition to a simulation object, one needs to define a market environment for the option itself. It has to contain at least a maturity and a currency. Optionally, a value for the strike parameter can be included as well:

```
In [69]: me_call = market_environment('me_call', me_gbm.pricing_date)
In [70]: me_call.add_constant('strike', 40.)
         me_call.add_constant('maturity', dt.datetime(2020, 12, 31))
         me_call.add_constant('currency', 'EUR')
```

A central element, of course, is the payoff function, provided here as a str object containing Python code that the eval() function can evaluate. A European *call* option shall be modeled. Such an option has a payoff of , with being the value of the underlying at maturity and *K* being the strike price of the option. In Python and NumPy — with vectorized storage of all simulated values — this takes on the following form:

```
In [71]: payoff_func = 'np.maximum(maturity_value - strike, 0)'
```

Having all the ingredients together, one can then instantiate an object from the

dx.valuation\_mcs\_european class. With the valuation object available, all quantities of interest are only one method call away:

```
In [72]: from valuation_mcs_european import valuation_mcs_european
In [73]: eur_call = valuation_mcs_european('eur_call', underlying=gbm,
                                 mar_env=me_call, payoff_func=payoff_func)
In [74]: %time eur_call.present_value()
         CPU times: user 14.8 ms, sys: 4.06 ms, total: 18.9 ms
         Wall time: 43.5 ms
Out[74]: 2.146828
In [75]: %time eur_call.delta()
         CPU times: user 12.4 ms, sys: 2.68 ms, total: 15.1 ms
         Wall time: 40.1 ms
Out[75]: 0.5155
In [76]: %time eur_call.vega()
         CPU times: user 21 ms, sys: 2.72 ms, total: 23.7 ms
         Wall time: 89.9 ms
Out[76]: 14.301
```

Estimates the present value of the European call option.

Estimates the delta of the option numerically; the delta is positive for calls.

Estimates the vega of the option numerically; the vega is positive for both calls and puts.

Once the valuation object is instantiated, a more comprehensive analysis of the present value and the Greeks is easily implemented. The following code calculates the present value, delta, and vega for initial values of the underlying ranging from 34 to 46 EUR. The results are presented graphically in Figure 19-1:

```
In [77]: %%time
         s_list = np.arange(34., 46.1, 2.)
         p_list = []; d_list = []; v_list = []
         for s in s_list:
             eur_call.update(initial_value=s)
             p_list.append(eur_call.present_value(fixed_seed=True))
             d_list.append(eur_call.delta())
             v_list.append(eur_call.vega())
         CPU times: user 374 ms, sys: 8.82 ms, total: 383 ms
         Wall time: 609 ms
```

- In [78]: **from plot\_option\_stats import** plot\_option\_stats
- In [79]: plot\_option\_stats(s\_list, p\_list, d\_list, v\_list)

![](_page_14_Figure_0.jpeg)

*Figure 19-1. Present value, delta, and vega estimates for European call option*

The visualization makes use of the helper function plot\_option\_stats():

```
#
# DX Package
#
# Valuation -- Plotting Options Statistics
#
# plot_option_stats.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import matplotlib.pyplot as plt
def plot_option_stats(s_list, p_list, d_list, v_list):
    ''' Plots option prices, deltas, and vegas for a set of
    different initial values of the underlying.
    Parameters
    ==========
    s_list: array or list
        set of initial values of the underlying
    p_list: array or list
        present values
```

```
d_list: array or list
    results for deltas
v_list: array or list
    results for vegas
'''plt.figure(figsize=(10, 7))
sub1 = plt.subplot(311)
plt.plot(s_list, p_list, 'ro', label='present value')
plt.plot(s_list, p_list, 'b')
plt.legend(loc=0)
plt.setp(sub1.get_xticklabels(), visible=False)
sub2 = plt.subplot(312)
plt.plot(s_list, d_list, 'go', label='Delta')
plt.plot(s_list, d_list, 'b')
plt.legend(loc=0)
plt.ylim(min(d_list) - 0.1, max(d_list) + 0.1)
plt.setp(sub2.get_xticklabels(), visible=False)
sub3 = plt.subplot(313)
plt.plot(s_list, v_list, 'yo', label='Vega')
plt.plot(s_list, v_list, 'b')
plt.xlabel('initial value of underlying')
plt.legend(loc=0)
```

This illustrates that working with the DX package — despite the fact that heavy numerics are involved — boils down to an approach that is comparable to having a closed-form option pricing formula available. However, this approach does not only apply to such simple or "plain vanilla" payoffs as the one considered so far. With exactly the same approach, one can handle more complex payoffs.

To this end, consider the following payoff, a mixture of a *regular* and an *Asian payoff*. The handling and the analysis are the same and are mainly independent of the type of payoff defined. Figure 19-2 shows that delta becomes 1 when the initial value of the underlying reaches the strike price of 40 in this case. Every (marginal) increase of the initial value of the underlying leads to the same (marginal) increase in the option's value from this particular point on:

```
In [80]: payoff_func = 'np.maximum(0.33 * '
         payoff_func += '(maturity_value + max_value) - 40, 0)'
In [81]: eur_as_call = valuation_mcs_european('eur_as_call', underlying=gbm,
                                     mar_env=me_call, payoff_func=payoff_func)
In [82]: %%time
         s_list = np.arange(34., 46.1, 2.)
         p_list = []; d_list = []; v_list = []
         for s in s_list:
             eur_as_call.update(s)
             p_list.append(eur_as_call.present_value(fixed_seed=True))
             d_list.append(eur_as_call.delta())
             v_list.append(eur_as_call.vega())
         CPU times: user 319 ms, sys: 14.2 ms, total: 333 ms
         Wall time: 488 ms
```

```
In [83]: plot_option_stats(s_list, p_list, d_list, v_list)
```

Payoff dependent on both the simulated maturity value and the maximum value over the simulated path.

![](_page_17_Figure_0.jpeg)

*Figure 19-2. Present value, delta, and vega estimates for option with Asian feature*

# **American Exercise**

The valuation of options with American exercise or Bermudan exercise is much more involved than with European exercise. <sup>2</sup> Therefore, a bit more valuation theory is needed before proceeding to the valuation class.

### **Least-Squares Monte Carlo**

Although Cox, Ross, and Rubinstein (1979) presented with their binomial model a simple numerical method to value European and American options in the same framework, only with the Longstaff-Schwartz (2001) approach was the valuation of American options by Monte Carlo simulation (MCS) satisfactorily solved. The major problem is that MCS per se is a forward-moving algorithm, while the valuation of American options is generally accomplished by backward induction, estimating the continuation value of the American option starting at maturity and working *back* to the present.

The major insight of the Longstaff-Schwartz (2001) model is to use an ordinary least-squares regression to estimate the continuation value based on the cross section of all available simulated values. <sup>3</sup> The algorithm takes into account, per path:

- The simulated value of the underlying(s)
- The inner value of the option
- The actual continuation value given the specific path

In discrete time, the value of a Bermudan option (and in the limit of an American option) is given by the *optimal stopping problem*, as presented in [Equation](#page-19-0) 19-3 for a finite set of points in time 0 < *t*<sup>1</sup> < *t*<sup>2</sup> < … < *T*. 4

<span id="page-19-0"></span>*Equation 19-3. Optimal stopping problem in discrete time for Bermudan option*

![](_page_19_Figure_8.jpeg)

Equation 19-4 presents the continuation value of the American option at date < *T*. It is the risk-neutral expectation at date under the martingale measure of the value of the American option at the subsequent date.

*Equation 19-4. Continuation value for the American option*

$$C_{t_m}(s) = e^{-r(t_{m+1}-t_m)} \mathbf{E}_{t_m}^Q(V_{t_{m\hat{1}}}(S_{t_{m\hat{1}}}) \mid S_{t_m} = s)$$

The value of the American option at date can be shown to equal the formula in [Equation](#page-20-0) 19-5 — i.e., the maximum of the payoff of immediate exercise (inner value) and the expected payoff of not exercising (continuation value).

<span id="page-20-0"></span>*Equation 19-5. Value of American option at any given date*

$$V_{t_m} = \max\left(h_{t_m}(s), \ C_{t_m}(s)\right)$$

In [Equation](#page-20-0) 19-5, the inner value is of course easily calculated. The continuation value is what makes it a bit trickier. The Longstaff-Schwartz (2001) algorithm approximates this value by a regression, as presented in [Equation](#page-20-1) 19-6. There, *i* stands for the current simulated path, *D* is the number of basis functions for the regression used, are the optimal regression parameters, and is the regression function with number *d*.

<span id="page-20-1"></span>*Equation 19-6. Regression-based approximation of continuation value*

![](_page_20_Figure_6.jpeg)

The optimal regression parameters are the result of the solution of the leastsquares regression problem presented in Equation 19-7. Here, is the actual continuation value at date for path *i* (and not a regressed/estimated one).

*Equation 19-7. Ordinary least-squares regression*

$$\min_{\alpha_{1,t_{m}},\ldots,\alpha_{D,t_{m}}} \frac{1}{I} \sum_{i=1}^{I} \left( Y_{t_{m},i} - \sum_{d=1}^{D} \alpha_{d,t_{m}} \cdot b_{d}(S_{t_{m},i}) \right)^{2}$$

This completes the basic (mathematical) tool set to value an American option by MCS.

### **The Valuation Class**

The code that follows represents the class for the valuation of options and derivatives with American exercise. There is one noteworthy step in the implementation of the LSM algorithm in the present\_value() method (which is also commented on inline): the *optimal decision step*. Here, it is important that, based on the decision that is made, the LSM algorithm takes either the inner value or the *actual* continuation value, and *not* the estimated continuation value: 5

```
#
# DX Package
#
# Valuation -- American Exercise Class
#
# valuation_mcs_american.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
```

**from valuation\_class import** valuation\_class

```
class valuation_mcs_american(valuation_class):
    ''' Class to value American options with arbitrary payoff
    by single-factor Monte Carlo simulation.
    Methods
    =======
    generate_payoff:
        returns payoffs given the paths and the payoff function
    present_value:
        returns present value (LSM Monte Carlo estimator)
        according to Longstaff-Schwartz (2001)
    '''def generate_payoff(self, fixed_seed=False):
        '''Parameters
        ==========
        fixed_seed:
            use same/fixed seed for valuation
        '''try:
            # strike is optional
```

```
strike = self.strike
    except:
        pass
    paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed)
    time_grid = self.underlying.time_grid
    time_index_start = int(np.where(time_grid == self.pricing_date)[0])
    time_index_end = int(np.where(time_grid == self.maturity)[0])
    instrument_values = paths[time_index_start:time_index_end + 1]
    payoff = eval(self.payoff_func)
    return instrument_values, payoff, time_index_start, time_index_end
def present_value(self, accuracy=6, fixed_seed=False, bf=5, full=False):
    '''Parameters
    ==========
    accuracy: int
        number of decimals in returned result
```

```
fixed_seed: bool
    use same/fixed seed for valuation
bf: int
    number of basis functions for regression
full: bool
    return also full 1d array of present values
'''instrument_values, inner_values, time_index_start, time_index_end = \
```

```
self.generate_payoff(fixed_seed=fixed_seed)
time_list = self.underlying.time_grid[
    time_index_start:time_index_end + 1]
discount_factors = self.discount_curve.get_discount_factors(
    time_list, dtobjects=True)
V = inner_values[-1]
for t in range(len(time_list) - 2, 0, -1):
    # derive relevant discount factor for given time interval
    df = discount_factors[t, 1] / discount_factors[t + 1, 1]
    # regression step
    rg = np.polyfit(instrument_values[t], V * df, bf)
    # calculation of continuation values per path
    C = np.polyval(rg, instrument_values[t])
    # optimal decision step:
    # if condition is satisfied (inner value > regressed cont. value)
    # then take inner value; take actual cont. value otherwise
    V = np.where(inner_values[t] > C, inner_values[t], V * df)
df = discount_factors[0, 1] / discount_factors[1, 1]
result = df * np.sum(V) / len(V)
if full:
    return round(result, accuracy), df * V
else:
    return round(result, accuracy)
```

### **A Use Case**

As has become by now the means of choice, a use case shall illustrate how to work with the dx.valuation\_mcs\_american class. The use case replicates all American option values as presented in Table 1 of the seminal paper by Longstaff and Schwartz (2001). The underlying is the same as before, a dx.geometric\_brownian\_motion object. The initial parameterization is as follows:

```
In [84]: me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))
In [85]: me_gbm.add_constant('initial_value', 36.)
         me_gbm.add_constant('volatility', 0.2)
         me_gbm.add_constant('final_date', dt.datetime(2021, 12, 31))
         me_gbm.add_constant('currency', 'EUR')
         me_gbm.add_constant('frequency', 'W')
         me_gbm.add_constant('paths', 50000)
In [86]: csr = constant_short_rate('csr', 0.06)
In [87]: me_gbm.add_curve('discount_curve', csr)
In [88]: gbm = geometric_brownian_motion('gbm', me_gbm)
In [89]: payoff_func = 'np.maximum(strike - instrument_values, 0)'
In [90]: me_am_put = market_environment('me_am_put', dt.datetime(2020, 1, 1))
In [91]: me_am_put.add_constant('maturity', dt.datetime(2020, 12, 31))
         me_am_put.add_constant('strike', 40.)
         me_am_put.add_constant('currency', 'EUR')
```

The next step is to instantiate the valuation object based on the numerical assumptions and to initiate the valuations. The valuation of the American put option can take quite a bit longer than the same task for the European options. Not only is the number of paths and time intervals increased, but the algorithm is also more computationally demanding due to the backward induction and the regression per induction step. The numerical estimate obtained for the first

option considered is close to the correct one reported in the original paper of

option considered is close to the correct one reported in the original paper of 4.478:

```
In [92]: from valuation_mcs_american import valuation_mcs_american
In [93]: am_put = valuation_mcs_american('am_put', underlying=gbm,
                             mar_env=me_am_put, payoff_func=payoff_func)
In [94]: %time am_put.present_value(fixed_seed=True, bf=5)
         CPU times: user 1.57 s, sys: 219 ms, total: 1.79 s
         Wall time: 2.01 s
Out[94]: 4.472834
```

Due to the very construction of the LSM Monte Carlo estimator, it represents a *lower bound* of the mathematically correct American option value. <sup>6</sup> Therefore, one expects the numerical estimate to lie under the true value in any numerically realistic case. Alternative dual estimators can provide *upper bounds* as well. 7 Taken together, two such different estimators then define an interval for the true American option value.

The main stated goal of this use case is to replicate all American option values of Table 1 in the original paper. To this end, one only needs to combine the valuation object with a nested loop. During the innermost loop, the valuation object has to be updated according to the then-current parameterization:

```
In [95]: %%time
         ls_table = []
         for initial_value in (36., 38., 40., 42., 44.):
             for volatility in (0.2, 0.4):
                 for maturity in (dt.datetime(2020, 12, 31),
                                  dt.datetime(2021, 12, 31)):
                     am_put.update(initial_value=initial_value,
                                   volatility=volatility,
                                   maturity=maturity)
                     ls_table.append([initial_value,
                                      volatility,
                                      maturity,
                                      am_put.present_value(bf=5)])
         CPU times: user 41.1 s, sys: 2.46 s, total: 43.5 s
         Wall time: 1min 30s
In [96]: print('S0 | Vola | T | Value')
         print(22 * '-')
         for r in ls_table:
             print('%d | %3.1f | %d | %5.3f' %
```

|                        |                  |  |           | (r[0], r[1], r[2].year - 2019, r[3])) |  |  |
|------------------------|------------------|--|-----------|---------------------------------------|--|--|
| S0                     | Vola   T   Value |  |           |                                       |  |  |
| ---------------------- |                  |  |           |                                       |  |  |
| 36                     | 0.2              |  | 1   4.447 |                                       |  |  |
| 36                     | 0.2              |  | 2   4.773 |                                       |  |  |
| 36                     | 0.4              |  | 1   7.006 |                                       |  |  |
| 36                     | 0.4              |  | 2   8.377 |                                       |  |  |
| 38                     | 0.2              |  | 1   3.213 |                                       |  |  |
| 38                     | 0.2              |  | 2   3.645 |                                       |  |  |
| 38                     | 0.4              |  | 1   6.069 |                                       |  |  |
| 38                     | 0.4              |  | 2   7.539 |                                       |  |  |
| 40                     | 0.2              |  | 1   2.269 |                                       |  |  |
| 40                     | 0.2              |  | 2   2.781 |                                       |  |  |
| 40                     | 0.4              |  | 1   5.211 |                                       |  |  |
| 40                     | 0.4              |  | 2   6.756 |                                       |  |  |
| 42                     | 0.2              |  | 1   1.556 |                                       |  |  |
| 42                     | 0.2              |  | 2   2.102 |                                       |  |  |
| 42                     | 0.4              |  | 1   4.466 |                                       |  |  |
| 42                     | 0.4              |  | 2   6.049 |                                       |  |  |
| 44                     | 0.2              |  | 1   1.059 |                                       |  |  |
| 44                     | 0.2              |  | 2   1.617 |                                       |  |  |
| 44                     | 0.4              |  | 1   3.852 |                                       |  |  |
| 44                     | 0.4              |  | 2   5.490 |                                       |  |  |

These results are a simplified version of Table 1 in the paper by Longstaff and Schwartz (2001). Overall, the numerical values come close to those reported in the paper, where some different parameters have been used (they use, for example, double the number of paths).

To conclude the use case, note that the estimation of Greeks for American options is formally the same as for European options — a major advantage of the implemented approach over alternative numerical methods (like the binomial model):

```
In [97]: am_put.update(initial_value=36.)
         am_put.delta()
Out[97]: -0.4631
In [98]: am_put.vega()
Out[98]: 18.0961
```

### **LEAST-SQUARES MONTE CARLO**

The LSM valuation algorithm of Longstaff and Schwartz (2001) is a numerically efficient algorithm to value options and even complex derivatives with American or Bermudan exercise features. The OLS regression step allows the approximation of the optimal exercise strategy based on an efficient numerical method. Since OLS regression can easily handle highdimensional data, it makes it a flexible method in derivatives pricing.

# **Conclusion**

This chapter is about the numerical valuation of European and American options based on Monte Carlo simulation. The chapter introduces a generic valuation class, called dx.valuation\_class. This class provides methods, for example, to estimate the most important Greeks (delta, vega) for both types of options, independent of the simulation object (i.e., the risk factor or stochastic process) used for the valuation.

Based on the generic valuation class, the chapter presents two specialized classes, dx.valuation\_mcs\_european and dx.valuation\_mcs\_american. The class for the valuation of European options is mainly a straightforward implementation of the risk-neutral valuation approach presented in Chapter 17 in combination with the numerical estimation of an expectation term (i.e., an integral by Monte Carlo simulation, as discussed in Chapter 11).

The class for the valuation of American options needs a certain kind of regression-based valuation algorithm, called Least-Squares Monte Carlo (LSM). This is due to the fact that for American options an optimal exercise policy has to be derived for a valuation. This is theoretically and numerically a bit more involved. However, the respective present\_value() method of the class is still concise.

The approach taken with the DX derivatives analytics package proves to be beneficial. Without too much effort one is able to value a relatively large class of options with the following features:

- Single risk factor
- European or American exercise
- Arbitrary payoff

In addition, one can estimate the most important Greeks for this class of options. To simplify future imports, again a wrapper module is used, this time called *dx\_valuation.py*:

*#*

```
# DX Package
#
# Valuation Classes
#
# dx_valuation.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
import pandas as pd
from dx_simulation import *
from valuation_class import valuation_class
from valuation_mcs_european import valuation_mcs_european
from valuation_mcs_american import valuation_mcs_american
```

The *\_\_init\_\_.py* file in the *dx* folder is updated accordingly:

```
#
# DX Package
# packaging file
# __init__.py
#
import numpy as np
import pandas as pd
import datetime as dt
# frame
from get_year_deltas import get_year_deltas
from constant_short_rate import constant_short_rate
from market_environment import market_environment
from plot_option_stats import plot_option_stats
# simulation
from sn_random_numbers import sn_random_numbers
from simulation_class import simulation_class
from geometric_brownian_motion import geometric_brownian_motion
from jump_diffusion import jump_diffusion
from square_root_diffusion import square_root_diffusion
# valuation
```

**from valuation\_class import** valuation\_class **from valuation\_mcs\_european import** valuation\_mcs\_european **from valuation\_mcs\_american import** valuation\_mcs\_american
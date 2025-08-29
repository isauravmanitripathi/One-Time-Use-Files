# **Chapter 17. Valuation Framework**

Compound interest is the greatest mathematical discovery of all time. Albert Einstein

This chapter provides the framework for the development of the DX library by introducing the most fundamental concepts needed for such an undertaking. It briefly reviews the Fundamental Theorem of Asset Pricing, which provides the theoretical background for the simulation and valuation. It then proceeds by addressing the fundamental concepts of *date handling* and *risk-neutral discounting*. This chapter considers only the simplest case of constant short rates for the discounting, but more complex and realistic models can be added to the library quite easily. This chapter also introduces the concept of a *market environment* — i.e., a collection of constants, lists, and curves needed for the instantiation of almost any other class to come in subsequent chapters.

The chapter comprises the following sections:

### *"Fundamental Theorem of Asset Pricing"*

This section introduces the Fundamental Theorem of Asset Pricing, which provides the theoretical background for the library to be developed.

### *"Risk-Neutral Discounting"*

This section develops a class for the risk-neutral discounting of future payoffs of options and other derivative instruments.

### *"Market Environments"*

This section develops a class to manage market environments for the pricing of single instruments and portfolios composed of multiple instruments.

# **Fundamental Theorem of Asset Pricing**

The *Fundamental Theorem of Asset Pricing* is one of the cornerstones and success stories of modern financial theory and mathematics. <sup>1</sup> The central notion underlying the theorem is the concept of a *martingale* measure; i.e., a probability measure that removes the drift from a discounted risk factor (stochastic process). In other words, under a martingale measure, all risk factors drift with the riskfree short rate — and not with any other market rate involving some kind of risk premium over the risk-free short rate.

### **A Simple Example**

Consider a simple economy at the dates today and tomorrow with a risky asset, a "stock," and a riskless asset, a "bond." The bond costs 10 USD today and pays off 10 USD tomorrow (zero interest rates). The stock costs 10 USD today and, with a probability of 60% and 40%, respectively, pays off 20 USD or 0 USD tomorrow. The riskless return of the bond is 0. The expected return of the stock is , or 20%. This is the risk premium the stock pays for its riskiness.

Consider now a call option with strike price of 15 USD. What is the fair value of such a contingent claim that pays 5 USD with 60% probability and 0 USD otherwise? One can take the expectation, for example, and discount the resulting value back (here with zero interest rates). This approach yields a value of 0.6 ⋅ 5 = 3 USD, since the option pays 5 USD in the case where the stock price moves up to 20 USD and 0 USD otherwise.

However, there is another approach that has been successfully applied to option pricing problems like this: *replication* of the option's payoff through a portfolio of traded securities. It is easily verified that buying 0.25 of the stock perfectly replicates the option's payoff (in the 60% case one then has 0.25 ⋅ 20 = 5 USD). A quarter of the stock only costs 2.5 USD and *not* 3 USD. Taking expectations under the real-world probability measure *overvalues* the option.

Why is this the case? The real-world measure implies a risk premium of 20% for the stock since the risk involved in the stock (gaining 100% or losing 100%) is "real" in the sense that it cannot be diversified or hedged away. On the other hand, there is a portfolio available that replicates the option's payoff without any risk. This also implies that someone writing (selling) such an option can completely hedge away any risk. <sup>2</sup> Such a perfectly hedged portfolio of an option and a hedge position must yield the riskless rate in order to avoid arbitrage opportunities (i.e., the opportunity to make some money out of no money with a positive probability).

Can one save the approach of taking expectations to value the call option? Yes, it is possible. One "only" has to change the probability in such a way that the risky asset, the stock, drifts with the riskless short rate of zero. Obviously, a

(martingale) measure giving equal mass of 50% to both scenarios accomplishes this; the calculation is . Now, taking expectations of the option's payoff under the new martingale measure yields the correct (arbitragefree) fair value: 0.5 ⋅ 5 + 0.5 ⋅ 0 = 2.5 USD.

### **The General Results**

The beauty of this approach is that it carries over to even the most complex economies with, for example, continuous time modeling (i.e., a continuum of points in time to consider), large numbers of risky assets, complex derivative payoffs, *etc.*

Therefore, consider a general market model in discrete time: 3

A *general market model* in discrete time is a collection of:

- A finite state space
- A filtration
- A strictly positive probability measure defined on
- A terminal date <
- A set of strictly positive security price processes

Together one has .

Based on such a general market model, one can formulate the Fundamental Theorem of Asset Pricing as follows: 4

Consider the general market model . According to the *Fundamental Theorem of Asset Pricing*, the following three statements are equivalent:

- There are no arbitrage opportunities in the market model .
- The set of *P*-equivalent martingale measures is nonempty.
- The set of consistent linear price systems is nonempty.

When it comes to valuation and pricing of contingent claims (i.e., options, derivatives, futures, forwards, swaps, etc.), the importance of the theorem is illustrated by the following corollary:

If the market model is arbitrage-free, then there exists a *unique price* associated with any attainable (i.e., replicable) contingent claim (option, derivative, etc.) . It satisfies , where is the relevant risk-neutral discount factor for a constant short rate .

This result illustrates the importance of the theorem, and shows that our simple reasoning from earlier indeed carries over to the general market model.

Due to the role of the martingale measure, this approach to valuation is also often called the *martingale approach*, or — since under the martingale measure all risky assets drift with the riskless short rate — the *risk-neutral valuation approach*. The second term might, for our purposes, be the better one because in numerical applications, one "simply" lets the risk factors (stochastic processes) drift by the risk-neutral short rate. One does not have to deal with the probability measures directly for our applications — they are, however, what theoretically justifies the central theoretical results applied and the technical approach implemented.

Finally, consider market completeness in the general market model:

The market model is *complete* if it is arbitrage-free and if every contingent claim (option, derivative, etc.) is attainable (i.e., replicable). Suppose that the market model is arbitrage-free. The market model is complete if and only if is a singleton; i.e., if there is a unique equivalent martingale measure.

This mainly completes the discussion of the theoretical background for what follows. For a detailed exposition of the concepts, notions, definitions, and results, refer to Chapter 4 of Hilpisch (2015).

# **Risk-Neutral Discounting**

Obviously, risk-neutral discounting is central to the risk-neutral valuation approach. This section therefore develops a Python class for risk-neutral discounting. However, it pays to first have a closer look at the modeling and handling of *relevant dates* for a valuation.

### **Modeling and Handling Dates**

A necessary prerequisite for discounting is the modeling of dates (see also Appendix A). For valuation purposes, one typically divides the time interval between today and the final date of the general market model into discrete time intervals. These time intervals can be homogeneous (i.e., of equal length), or they can be heterogeneous (i.e., of varying length). A valuation library should be able to handle the more general case of heterogeneous time intervals, since the simpler case is then automatically included. Therefore, the code works with lists of dates, assuming that the smallest relevant time interval is *one day*. This implies that intraday events are considered irrelevant, for which one would have to model *time* (in addition to dates). 5

To compile a list of relevant dates, one can basically take one of two approaches: constructing a list of concrete *dates* (e.g., as datetime objects in Python) or of *year fractions* (as decimal numbers, as is often done in theoretical works).

Some imports first:

```
In [1]: import numpy as np
        import pandas as pd
        import datetime as dt
In [2]: from pylab import mpl, plt
        plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
In [3]: import sys
        sys.path.append('../dx')
```

For example, the following two definitions of dates and fractions are (roughly) equivalent:

```
In [4]: dates = [dt.datetime(2020, 1, 1), dt.datetime(2020, 7, 1),
                 dt.datetime(2021, 1, 1)]
In [5]: (dates[1] - dates[0]).days / 365.
Out[5]: 0.4986301369863014
In [6]: (dates[2] - dates[1]).days / 365.
Out[6]: 0.5041095890410959
In [7]: fractions = [0.0, 0.5, 1.0]
```

They are only *roughly* equivalent since year fractions seldom lie on the beginning (0 a.m.) of a certain day. Just consider the result of dividing a year by 50.

Sometimes it is necessary to get year fractions out of a list of dates. The function get\_year\_deltas() does the job:

```
#
# DX Package
#
# Frame -- Helper Function
#
# get_year_deltas.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
def get_year_deltas(date_list, day_count=365.):
    ''' Return vector of floats with day deltas in year fractions.
    Initial value normalized to zero.
    Parameters
    ==========
    date_list: list or array
        collection of datetime objects
    day_count: float
        number of days for a year
        (to account for different conventions)
    Results
    =======
    delta_list: array
        year fractions
    '''start = date_list[0]
    delta_list = [(date - start).days / day_count
                  for date in date_list]
    return np.array(delta_list)
```

This function can then be applied as follows:

```
In [8]: from get_year_deltas import get_year_deltas
In [9]: get_year_deltas(dates)
Out[9]: array([0. , 0.49863014, 1.00273973])
```

When modeling the short rate, it becomes clear what the benefit of this conversion is.

### **Constant Short Rate**

The exposition to follow focuses on the simplest case for discounting by the short rate; namely, the case where the short rate is *constant through time*. Many option pricing models, like the ones of Black-Scholes-Merton (1973), Merton (1976), or Cox-Ross-Rubinstein (1979), make this assumption. <sup>6</sup> Assume continuous discounting, as is usual for option pricing applications. In such a case, the general discount factor as of today, given a future date and a constant short rate of , is then given by . Of course, for the end of the economy the special case holds true. Note that here both and are in year fractions.

The discount factors can also be interpreted as the value of a *unit zero-coupon bond* (ZCB) as of today, maturing at and , respectively. <sup>7</sup> Given two dates , the discount factor relevant for discounting from to is then given by the equation .

The following translates these considerations into Python code in the form of a class: 8

```
#
# DX Library
#
# Frame -- Constant Short Rate Class
#
# constant_short_rate.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
from get_year_deltas import *
class constant_short_rate(object):
    ''' Class for constant short rate discounting.
    Attributes
    ==========
    name: string
        name of the object
    short_rate: float (positive)
```

*constant rate for discounting*

```
Methods
=======
get_discount_factors:
    get discount factors given a list/array of datetime objects
    or year fractions
'''def __init__(self, name, short_rate):
    self.name = name
    self.short_rate = short_rate
    if short_rate < 0:
        raise ValueError('Short rate negative.')
        # this is debatable given recent market realities
def get_discount_factors(self, date_list, dtobjects=True):
    if dtobjects is True:
        dlist = get_year_deltas(date_list)
    else:
        dlist = np.array(date_list)
    dflist = np.exp(self.short_rate * np.sort(-dlist))
    return np.array((date_list, dflist)).T
```

The application of the class dx.constant\_short\_rate is best illustrated by a simple, concrete example. The main result is a two-dimensional ndarray object containing pairs of a datetime object and the relevant discount factor. The class in general and the object csr in particular work with year fractions as well:

```
In [10]: from constant_short_rate import constant_short_rate
In [11]: csr = constant_short_rate('csr', 0.05)
In [12]: csr.get_discount_factors(dates)
Out[12]: array([[datetime.datetime(2020, 1, 1, 0, 0), 0.9510991280247174],
               [datetime.datetime(2020, 7, 1, 0, 0), 0.9753767163648953],
               [datetime.datetime(2021, 1, 1, 0, 0), 1.0]], dtype=object)
In [13]: deltas = get_year_deltas(dates)
        deltas
Out[13]: array([0. , 0.49863014, 1.00273973])
In [14]: csr.get_discount_factors(deltas, dtobjects=False)
Out[14]: array([[0. , 0.95109913],
               [0.49863014, 0.97537672],
               [1.00273973, 1. ]])
```

This class will take care of all discounting operations needed in other classes.

### **Market Environments**

*Market environment* is "just" a name for a collection of other data and Python objects. However, it is rather convenient to work with this abstraction since it simplifies a number of operations and also allows for a consistent modeling of recurring aspects. <sup>9</sup> A market environment mainly consists of three dictionaries to store the following types of data and Python objects:

*Constants*

These can be, for example, model parameters or option maturity dates.

*Lists*

These are collections of objects in general, like a list of objects modeling (risky) securities.

#### *Curves*

These are objects for discounting; e.g., an instance of the dx.constant\_short\_rate class.

Following is the code for the dx.market\_environment class. Refer to Chapter 3 for details on the handling of dict objects:

```
#
# DX Package
#
# Frame -- Market Environment Class
#
# market_environment.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
class market_environment(object):
    ''' Class to model a market environment relevant for valuation.
    Attributes
    ==========
    name: string
        name of the market environment
    pricing_date: datetime object
        date of the market environment
    Methods
    =======
    add_constant:
        adds a constant (e.g. model parameter)
```

```
get_constant:
    gets a constant
add_list:
    adds a list (e.g. underlyings)
get_list:
    gets a list
add_curve:
    adds a market curve (e.g. yield curve)
get_curve:
    gets a market curve
add_environment:
    adds and overwrites whole market environments
    with constants, lists, and curves
'''def __init__(self, name, pricing_date):
    self.name = name
    self.pricing_date = pricing_date
    self.constants = {}
    self.lists = {}
    self.curves = {}
def add_constant(self, key, constant):
    self.constants[key] = constant
def get_constant(self, key):
    return self.constants[key]
def add_list(self, key, list_object):
    self.lists[key] = list_object
def get_list(self, key):
    return self.lists[key]
def add_curve(self, key, curve):
    self.curves[key] = curve
def get_curve(self, key):
    return self.curves[key]
def add_environment(self, env):
    # overwrites existing values, if they exist
    self.constants.update(env.constants)
    self.lists.update(env.lists)
    self.curves.update(env.curves)
```

Although there is nothing really special about the dx.market\_environment class, a simple example shall illustrate how convenient it is to work with instances of the class:

```
In [15]: from market_environment import market_environment
In [16]: me = market_environment('me_gbm', dt.datetime(2020, 1, 1))
In [17]: me.add_constant('initial_value', 36.)
In [18]: me.add_constant('volatility', 0.2)
In [19]: me.add_constant('final_date', dt.datetime(2020, 12, 31))
```

```
In [20]: me.add_constant('currency', 'EUR')
In [21]: me.add_constant('frequency', 'M')
In [22]: me.add_constant('paths', 10000)
In [23]: me.add_curve('discount_curve', csr)
In [24]: me.get_constant('volatility')
Out[24]: 0.2
In [25]: me.get_curve('discount_curve').short_rate
Out[25]: 0.05
```

This illustrates the basic handling of this rather generic "storage" class. For practical applications, market data and other data as well as Python objects are first collected, then a dx.market\_environment object is instantiated and filled with the relevant data and objects. This is then delivered in a single step to other classes that need the data and objects stored in the respective dx.market\_environment object.

A major advantage of this object-oriented modeling approach is, for example, that instances of the dx.constant\_short\_rate class can live in multiple environments (see the topic of *aggregation* in Chapter 6). Once the instance is updated — for example, when a new constant short rate is set — all the instances of the dx.market\_environment class containing that particular instance of the discounting class will be updated automatically.

#### **FLEXIBILITY**

The market environment class as introduced in this section is a flexible means to model and store any quantities and input data relevant to the pricing of options and derivatives and portfolios composed thereof. However, this flexibility also leads to operational risks in that it is easy to pass nonsensical data, objects, *etc.* to the class during instantiation, which might or might not be captured during instantiation. In a production context, a number of checks need to be added to at least capture obviously wrong cases.

### **Conclusion**

This chapter provides the basic framework for the larger project of building a Python package to value options and other derivatives by Monte Carlo simulation. The chapter introduces the Fundamental Theorem of Asset Pricing, illustrating it by a rather simple numerical example. Important results in this regard are provided for a general market model in discrete time.

The chapter also develops a Python class for risk-neutral discounting purposes to make numerical use of the mathematical machinery of the Fundamental Theorem of Asset Pricing. Based on a list object of either Python datetime objects or float objects representing year fractions, instances of the class dx.constant\_short\_rate provide the appropriate discount factors (present values of unit zero-coupon bonds).

The chapter concludes with the rather generic dx.market\_environment class, which allows for the collection of relevant data and Python objects for modeling, simulation, valuation, and other purposes.

To simplify future imports, a wrapper module called *dx\_frame.py* is used:

```
#
# DX Analytics Package
#
# Frame Functions & Classes
#
# dx_frame.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import datetime as dt
from get_year_deltas import get_year_deltas
from constant_short_rate import constant_short_rate
from market_environment import market_environment
```

A single import statement like the following then makes all framework components available in a single step:

**import dx\_frame**

Thinking of a Python package of modules, there is also the option to store all

relevant Python modules in a (sub)folder and to put in that folder a special *\_\_init\_\_.py* file that does all the imports. For example, when storing all modules in a folder called *dx*, say, the file presented next does the job. However, notice the naming convention for this particular file:

```
#
# DX Package
# packaging file
# __init__.py
#
import datetime as dt
from get_year_deltas import get_year_deltas
from constant_short_rate import constant_short_rate
from market_environment import market_environment
```

In that case you can just use the folder name to accomplish all the imports at once:

**from dx import** \*

Or, via the alternative approach:

**import dx**
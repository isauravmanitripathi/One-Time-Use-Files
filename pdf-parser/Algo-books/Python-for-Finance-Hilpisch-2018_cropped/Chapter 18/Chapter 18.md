# **Chapter 18. Simulation of Financial Models**

The purpose of science is not to analyze or describe but to make useful models of the world. Edward de Bono

Chapter 12 introduces in some detail the Monte Carlo simulation of stochastic processes using Python and NumPy. This chapter applies the basic techniques presented there to implement simulation classes as a central component of the DX package. The set of stochastic processes is restricted to three widely used ones. In particular, the chapter comprises the following sections: "Random Number Generation"

This section develops a function to generate standard normally distributed random numbers using variance reduction techniques. 1

### *"Generic Simulation Class"*

This section develops a generic simulation class from which the other specific simulatation classes inherit fundamental attributes and methods.

### *"Geometric Brownian Motion"*

This section is about the geometric Brownian motion (GBM) that was introduced to the option pricing literature through the seminal works of Black and Scholes (1973) and Merton (1973); it is used several times throughout this book and still represents — despite its known shortcomings and given the mounting empirical evidence against it — a benchmark process for option and derivative valuation purposes.

### *"Jump Diffusion"*

The jump diffusion, as introduced to finance by Merton (1976), adds a lognormally distributed jump component to the GBM. This allows one to take into account that, for example, short-term out-of-the-money (OTM) options often seem to have priced in the possibility of larger jumps; in other words, relying on GBM as a financial model often cannot explain the market values of such OTM options satisfactorily, while a jump diffusion may be

values of such OTM options satisfactorily, while a jump diffusion may be able to do so.

### *"Square-Root Diffusion"*

The square-root diffusion, popularized in finance by Cox, Ingersoll, and Ross (1985), is used to model mean-reverting quantities like interest rates and volatility; in addition to being mean-reverting, the process stays positive, which is generally a desirable characteristic for those quantities.

For further details on the simulation of the models presented in this chapter, refer also to Hilpisch (2015). In particular, that book contains a complete case study based on the jump diffusion model of Merton (1976).

# **Random Number Generation**

Random number generation is a central task of Monte Carlo simulation. 2 Chapter 12 shows how to use Python and subpackages such as numpy.random to generate random numbers with different distributions. For the project at hand, *standard normally distributed* random numbers are the most important ones. That is why it pays off to have the convenience function sn\_random\_numbers(), defined here, available for generating this particular type of random numbers:

```
#
# DX Package
#
# Frame -- Random Number Generation
#
# sn_random_numbers.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
```

```
def sn_random_numbers(shape, antithetic=True, moment_matching=True,
                      fixed_seed=False):
    ''' Returns an ndarray object of shape shape with (pseudo)random numbers
    that are standard normally distributed.
```

```
Parameters
==========
shape: tuple (o, n, m)
    generation of array with shape (o, n, m)
antithetic: Boolean
    generation of antithetic variates
moment_matching: Boolean
    matching of first and second moments
fixed_seed: Boolean
    flag to fix the seed
```

```
Results
=======
ran: (o, n, m) array of (pseudo)random numbers
'''if fixed_seed:
    np.random.seed(1000)
if antithetic:
    ran = np.random.standard_normal(
        (shape[0], shape[1], shape[2] // 2))
```

```
ran = np.concatenate((ran, -ran), axis=2)
else:
    ran = np.random.standard_normal(shape)
if moment_matching:
    ran = ran - np.mean(ran)
    ran = ran / np.std(ran)
if shape[0] == 1:
    return ran[0]
else:
    return ran
```

The variance reduction techniques used in this function, namely *antithetic paths* and *moment matching*, are also illustrated in Chapter 12. <sup>3</sup> The application of the function is straightforward:

```
In [26]: from sn_random_numbers import *
In [27]: snrn = sn_random_numbers((2, 2, 2), antithetic=False,
                                  moment_matching=False, fixed_seed=True)
         snrn
Out[27]: array([[[-0.8044583 , 0.32093155],
                 [-0.02548288, 0.64432383]],
                [[-0.30079667, 0.38947455],
                 [-0.1074373 , -0.47998308]]])
In [28]: round(snrn.mean(), 6)
Out[28]: -0.045429
In [29]: round(snrn.std(), 6)
Out[29]: 0.451876
In [30]: snrn = sn_random_numbers((2, 2, 2), antithetic=False,
                                  moment_matching=True, fixed_seed=True)
         snrn
Out[30]: array([[[-1.67972865, 0.81075283],
                 [ 0.04413963, 1.52641815]],
                [[-0.56512826, 0.96243813],
                 [-0.13722505, -0.96166678]]])
In [31]: round(snrn.mean(), 6)
Out[31]: -0.0
In [32]: round(snrn.std(), 6)
Out[32]: 1.0
```

This function will prove a workhorse for the simulation classes to follow.

# **Generic Simulation Class**

Object-oriented modeling — as introduced in Chapter 6 — allows inheritance of attributes and methods. This is what the following code makes use of when building the simulation classes: one starts with a *generic* simulation class containing those attributes and methods that all other simulation classes share and can then focus with the other classes on specific elements of the stochastic process to be simulated.

Instantiating an object of any simulation class happens by providing three attributes only: name

A str object as a name for the model simulation object

*mar\_env*

An instance of the dx.market\_environment class

*corr*

A flag (bool) indicating whether the object is correlated or not

This again illustrates the role of a *market environment*: to provide in a single step all data and objects required for simulation and valuation. The methods of the generic class are: generate\_time\_grid()

This method generates the time grid of relevant dates used for the simulation; this task is the same for every simulation class.

```
get_instrument_values()
```

Every simulation class has to return the ndarray object with the simulated instrument values (e.g., simulated stock prices, commodities prices, volatilities).

The code for the generic model simulation class follows. The methods make use of other methods that the model-tailored classes will provide, like self.generate\_paths(). The details in this regard become clear when one has the full picture of a specialized, nongeneric simulation class. First, the base class: *# # DX Package # # Simulation Class -- Base Class # # simulation\_class.py # # Python for Finance, 2nd ed. # (c) Dr. Yves J. Hilpisch #* **import numpy as np import pandas as pd class**

**simulation\_class**(object): *''' Providing base methods for simulation classes. Attributes ========== name: str name of the object mar\_env: instance of market\_environment market environment data for simulation corr: bool True if correlated with other model object Methods ======= generate\_time\_grid: returns time grid for simulation get\_instrument\_values: returns the current instrument values (array) '''* **def** \_\_init\_\_(self, name, mar\_env, corr): self.name = name self.pricing\_date = mar\_env.pricing\_date self.initial\_value = mar\_env.get\_constant('initial\_value') self.volatility = mar\_env.get\_constant('volatility') self.final\_date = mar\_env.get\_constant('final\_date') self.currency = mar\_env.get\_constant('currency') self.frequency = mar\_env.get\_constant('frequency') self.paths = mar\_env.get\_constant('paths') self.discount\_curve = mar\_env.get\_curve('discount\_curve') **try**: *# if time\_grid in mar\_env take that object # (for portfolio valuation)* self.time\_grid = mar\_env.get\_list('time\_grid') **except**: self.time\_grid = None **try**: *# if there are special dates, then add these* self.special\_dates = mar\_env.get\_list('special\_dates') **except**: self.special\_dates = [] self.instrument\_values = None self.correlated = corr **if** corr **is** True: *# only needed in a portfolio context when # risk factors are correlated* self.cholesky\_matrix = mar\_env.get\_list('cholesky\_matrix') self.rn\_set = mar\_env.get\_list('rn\_set')[self.name] self.random\_numbers = mar\_env.get\_list('random\_numbers') **def** generate\_time\_grid(self): start = self.pricing\_date end = self.final\_date *# pandas date\_range function # freq = e.g. 'B' for Business Day, # 'W' for Weekly, 'M' for Monthly* time\_grid = pd.date\_range(start=start, end=end, freq=self.frequency).to\_pydatetime() time\_grid = list(time\_grid) *# enhance time\_grid by start, end, and special\_dates* **if** start **not in** time\_grid: time\_grid.insert(0, start) *# insert start date if not in list* **if** end **not in** time\_grid: time\_grid.append(end) *# insert end date*

*if not in list* **if** len(self.special\_dates) > 0: *# add all special dates*

time\_grid.extend(self.special\_dates) *# delete duplicates* time\_grid = list(set(time\_grid)) *# sort list* time\_grid.sort() self.time\_grid = np.array(time\_grid) **def** get\_instrument\_values(self, fixed\_seed=True): **if** self.instrument\_values **is** None: *# only initiate simulation if there are no instrument values*

self.generate\_paths(fixed\_seed=fixed\_seed, day\_count=365.) **elif** fixed\_seed **is** False: *# also initiate resimulation when fixed\_seed is False* self.generate\_paths(fixed\_seed=fixed\_seed, day\_count=365.) **return** self.instrument\_values

Parsing of the market environment is embedded in the special method \_\_init\_\_(), which is called during instantiation. To keep the code concise, there are *no* sanity checks implemented. For example, the following line of code is considered a "success," no matter if the content is indeed an instance of a discounting class or not. Therefore, one has to be rather careful when compiling and passing dx.market\_environment objects to any simulation class: self.discount\_curve = mar\_env.get\_curve('discount\_curve')

[Table](#page-7-0) 18-1 shows all components a dx.market\_environment object must contain for the generic and therefore for all other simulation classes.

| Element        | Type     | Mandatory | Description                                                             |
|----------------|----------|-----------|-------------------------------------------------------------------------|
| initial_value  | Constant | Yes       | Initial<br>value<br>of<br>process<br>at<br>pricing_date                 |
| volatility     | Constant | Yes       | Volatility<br>coefficient<br>of<br>process                              |
| final_date     | Constant | Yes       | Simulation<br>horizon                                                   |
| currency       | Constant | Yes       | Currency<br>of<br>the<br>financial<br>entity                            |
| frequency      | Constant | Yes       | Date<br>frequency,<br>as<br>pandas freq parameter                       |
| paths          | Constant | Yes       | Number<br>of<br>paths<br>to<br>be<br>simulated                          |
| discount_curve | Curve    | Yes       | Instance<br>of<br>dx.constant_short_rate                                |
| time_grid      | List     | No        | Time<br>grid<br>of<br>relevant<br>dates<br>(in<br>portfolio<br>context) |
|                |          |           |                                                                         |

random\_numbers List No Random number np.ndarray object (for correlated objects)

<span id="page-7-0"></span>*Table 18-1. Elements of the market environment for all simulation classes*

| random_numbers       | List | No | Random<br>number<br>np.ndarray object<br>(for<br>correlated<br>objects)     |
|----------------------|------|----|-----------------------------------------------------------------------------|
| cholesky_matrix List |      | No | Cholesky<br>matrix<br>(for<br>correlated<br>objects)                        |
| rn_set               | List | No | dict object<br>with<br>pointer<br>to<br>relevant<br>random<br>number<br>set |

Everything that has to do with the correlation of model simulation objects is explained in subsequent chapters. In this chapter, the focus is on the simulation of single, uncorrelated processes. Similarly, the option to pass a time\_grid is only relevant in a portfolio context, something also explained later.

# **Geometric Brownian Motion**

[Geometric](#page-9-0) Brownian motion is a stochastic process, as described in Equation 18- 1 (see also Equation 12-2 in Chapter 12, in particular for the meaning of the parameters and variables). The drift of the process is already set equal to the riskless, constant short rate *r*, implying that one operates under the equivalent martingale measure (see Chapter 17).

<span id="page-9-0"></span>*Equation 18-1. Stochastic differential equation of geometric Brownian motion*

$$dS_t = rS_t dt + \sigma S_t dZ_t$$

[Equation](#page-9-1) 18-2 presents an Euler discretization of the stochastic differential equation for simulation purposes (see also Equation 12-3 in Chapter 12 for further details). The general framework is a discrete time market model, such as the general market model ℳ from Chapter 17, with a finite set of relevant dates 0 < *t*<sup>1</sup> < *t*<sup>2</sup> < … < *T*.

<span id="page-9-1"></span>*Equation 18-2. Difference equation to simulate the geometric Brownian motion*

$$S_{t_{m+1}} = S_{t_m} \exp\left(\left(r - \frac{\sigma^2}{2}\right)(t_{m+1} - t_m) + \sigma\sqrt{t_{m+1} - t_m} z_t\right)$$
  
$$0 \le t_m < t_{m+1} \le T$$

### **The Simulation Class**

Following is the specialized class for the GBM model:

```
#
# DX Package
#
# Simulation Class -- Geometric Brownian Motion
#
# geometric_brownian_motion.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
from sn_random_numbers import sn_random_numbers
from simulation_class import simulation_class
class geometric_brownian_motion(simulation_class):
    ''' Class to generate simulated paths based on
    the Black-Scholes-Merton geometric Brownian motion model.
    Attributes
    ==========
    name: string
        name of the object
    mar_env: instance of market_environment
        market environment data for simulation
    corr: Boolean
        True if correlated with other model simulation object
    Methods
    =======
    update:
        updates parameters
    generate_paths:
        returns Monte Carlo paths given the market environment
    '''def __init__(self, name, mar_env, corr=False):
        super(geometric_brownian_motion, self).__init__(name, mar_env, corr)
    def update(self, initial_value=None, volatility=None, final_date=None):
        if initial_value is not None:
            self.initial_value = initial_value
```

```
if volatility is not None:
        self.volatility = volatility
    if final_date is not None:
        self.final_date = final_date
    self.instrument_values = None
def generate_paths(self, fixed_seed=False, day_count=365.):
    if self.time_grid is None:
        # method from generic simulation class
        self.generate_time_grid()
    # number of dates for time grid
    M = len(self.time_grid)
    # number of paths
    I = self.paths
    # ndarray initialization for path simulation
    paths = np.zeros((M, I))
    # initialize first date with initial_value
    paths[0] = self.initial_value
    if not self.correlated:
        # if not correlated, generate random numbers
        rand = sn_random_numbers((1, M, I),
                                 fixed_seed=fixed_seed)
    else:
        # if correlated, use random number object as provided
        # in market environment
        rand = self.random_numbers
    short_rate = self.discount_curve.short_rate
    # get short rate for drift of process
    for t in range(1, len(self.time_grid)):
        # select the right time slice from the relevant
        # random number set
        if not self.correlated:
            ran = rand[t]
        else:
            ran = np.dot(self.cholesky_matrix, rand[:, t, :])
            ran = ran[self.rn_set]
        dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count
        # difference between two dates as year fraction
        paths[t] = paths[t - 1] * np.exp((short_rate - 0.5 *
                                        self.volatility ** 2) * dt +
                                        self.volatility * np.sqrt(dt) * ran)
        # generate simulated values for the respective date
    self.instrument_values = paths
```

In this particular case, the dx.market\_environment object has to contain only the data and objects shown in Table 18-1 — i.e., the minimum set of components.

The method update() does what its name suggests: it allows the updating of selected important parameters of the model. The method generate\_paths() is, of course, a bit more involved. However, it has a number of inline comments that should make clear the most important aspects. Some complexity is brought into this method by, in principle, allowing for the correlation between different model simulation objects — the purpose of which will become clearer later,

especially in Chapter 20.

### **A Use Case**

The following interactive IPython session illustrates the use of the GBM simulation class. First, one has to generate a dx.market\_environment object with all the mandatory elements:

```
In [33]: from dx_frame import *
In [34]: me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))
In [35]: me_gbm.add_constant('initial_value', 36.)
         me_gbm.add_constant('volatility', 0.2)
         me_gbm.add_constant('final_date', dt.datetime(2020, 12, 31))
         me_gbm.add_constant('currency', 'EUR')
         me_gbm.add_constant('frequency', 'M')
         me_gbm.add_constant('paths', 10000)
In [36]: csr = constant_short_rate('csr', 0.06)
In [37]: me_gbm.add_curve('discount_curve', csr)
```

Monthly frequency with *month end* as default.

Second, one instantiates a model simulation object to work with:

```
In [38]: from geometric_brownian_motion import geometric_brownian_motion
In [39]: gbm = geometric_brownian_motion('gbm', me_gbm)
In [40]: gbm.generate_time_grid()
In [41]: gbm.time_grid
Out[41]: array([datetime.datetime(2020, 1, 1, 0, 0),
                datetime.datetime(2020, 1, 31, 0, 0),
                datetime.datetime(2020, 2, 29, 0, 0),
                datetime.datetime(2020, 3, 31, 0, 0),
                datetime.datetime(2020, 4, 30, 0, 0),
                datetime.datetime(2020, 5, 31, 0, 0),
                datetime.datetime(2020, 6, 30, 0, 0),
                datetime.datetime(2020, 7, 31, 0, 0),
                datetime.datetime(2020, 8, 31, 0, 0),
                datetime.datetime(2020, 9, 30, 0, 0),
                datetime.datetime(2020, 10, 31, 0, 0),
                datetime.datetime(2020, 11, 30, 0, 0),
                datetime.datetime(2020, 12, 31, 0, 0)], dtype=object)
In [42]: %time paths_1 = gbm.get_instrument_values()
         CPU times: user 21.3 ms, sys: 6.74 ms, total: 28.1 ms
         Wall time: 40.3 ms
In [43]: paths_1.round(3)
Out[43]: array([[36. , 36. , 36. , ..., 36. , 36. , 36. ],
```

```
[37.403, 38.12 , 34.4 , ..., 36.252, 35.084, 39.668],
                [39.562, 42.335, 32.405, ..., 34.836, 33.637, 37.655],
                ...,
                [40.534, 33.506, 23.497, ..., 37.851, 30.122, 30.446],
                [42.527, 36.995, 21.885, ..., 36.014, 30.907, 30.712],
                [43.811, 37.876, 24.1 , ..., 36.263, 28.138, 29.038]])
In [44]: gbm.update(volatility=0.5)
In [45]: %time paths_2 = gbm.get_instrument_values()
         CPU times: user 27.8 ms, sys: 3.91 ms, total: 31.7 ms
         Wall time: 19.8 ms
```

Instantiates the simulation object.

Generates the time grid …

… and shows it; note that the initial date is added.

Simulates the paths given the parameterization.

Updates the volatility parameter and repeats the simulation.

Figure 18-1 shows 10 simulated paths for the two different parameterizations. The effect of increasing the volatility parameter value is easy to see:

```
In [46]: plt.figure(figsize=(10, 6))
         p1 = plt.plot(gbm.time_grid, paths_1[:, :10], 'b')
         p2 = plt.plot(gbm.time_grid, paths_2[:, :10], 'r-.')
         l1 = plt.legend([p1[0], p2[0]],
                         ['low volatility', 'high volatility'], loc=2)
         plt.gca().add_artist(l1)
         plt.xticks(rotation=30);
```

![](_page_15_Figure_0.jpeg)

*Figure 18-1. Simulated paths from GBM simulation class*

### **VECTORIZATION FOR SIMULATION**

As argued and shown already in Chapter 12, vectorization approaches using NumPy and pandas are well suited to writing concise and performant simulation code.

# **Jump Diffusion**

Equipped with the background knowledge from the

dx.geometric\_brownian\_motion class, it is now straightforward to implement a class for the jump diffusion model described by Merton (1976). The stochastic differential equation for the jump diffusion model is shown in [Equation](#page-17-0) 18-3 (see also Equation 12-8 in Chapter 12, in particular for the meaning of the parameters and variables).

<span id="page-17-0"></span>*Equation 18-3. Stochastic differential equation for Merton jump diffusion model*

$$dS_t = (r - r_J)S_t dt + \sigma S_t dZ_t + J_t S_t dN_t$$

An Euler discretization for simulation purposes is presented in [Equation](#page-17-1) 18-4 (see also Equation 12-9 in Chapter 12 and the more detailed explanations given there).

<span id="page-17-1"></span>*Equation 18-4. Euler discretization for Merton jump diffusion model*

$$S_{t_{m+1}} = S_{t_m} \left( \exp\left( \left( r - r_J - \frac{\sigma^2}{2} \right) (t_{m+1} - t_m) + \sigma \sqrt{t_{m+1} - t_m} z_t^1 \right) + \left( e^{\mu_J + \delta z_t^2} - 1 \right) y_t \right)$$
  
$$0 \le t_m < t_{m+1} \le T$$

### **The Simulation Class**

The Python code for the dx.jump\_diffusion simulation class follows. This class should by now contain no surprises. Of course, the model is different, but the design and the methods are essentially the same:

```
#
# DX Package
#
# Simulation Class -- Jump Diffusion
#
# jump_diffusion.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
from sn_random_numbers import sn_random_numbers
from simulation_class import simulation_class
class jump_diffusion(simulation_class):
    ''' Class to generate simulated paths based on
    the Merton (1976) jump diffusion model.
    Attributes
    ==========
    name: str
        name of the object
    mar_env: instance of market_environment
        market environment data for simulation
    corr: bool
        True if correlated with other model object
    Methods
    =======
    update:
        updates parameters
    generate_paths:
        returns Monte Carlo paths given the market environment
    '''def __init__(self, name, mar_env, corr=False):
        super(jump_diffusion, self).__init__(name, mar_env, corr)
        # additional parameters needed
        self.lamb = mar_env.get_constant('lambda')
```

```
self.mu = mar_env.get_constant('mu')
    self.delt = mar_env.get_constant('delta')
def update(self, initial_value=None, volatility=None, lamb=None,
           mu=None, delta=None, final_date=None):
    if initial_value is not None:
        self.initial_value = initial_value
    if volatility is not None:
        self.volatility = volatility
    if lamb is not None:
        self.lamb = lamb
    if mu is not None:
        self.mu = mu
    if delta is not None:
        self.delt = delta
    if final_date is not None:
        self.final_date = final_date
    self.instrument_values = None
def generate_paths(self, fixed_seed=False, day_count=365.):
    if self.time_grid is None:
        # method from generic simulation class
        self.generate_time_grid()
    # number of dates for time grid
    M = len(self.time_grid)
    # number of paths
    I = self.paths
    # ndarray initialization for path simulation
    paths = np.zeros((M, I))
    # initialize first date with initial_value
    paths[0] = self.initial_value
    if self.correlated is False:
        # if not correlated, generate random numbers
        sn1 = sn_random_numbers((1, M, I),
                                fixed_seed=fixed_seed)
    else:
        # if correlated, use random number object as provided
        # in market environment
        sn1 = self.random_numbers
    # standard normally distributed pseudo-random numbers
    # for the jump component
    sn2 = sn_random_numbers((1, M, I),
                            fixed_seed=fixed_seed)
    rj = self.lamb * (np.exp(self.mu + 0.5 * self.delt ** 2) - 1)
    short_rate = self.discount_curve.short_rate
    for t in range(1, len(self.time_grid)):
        # select the right time slice from the relevant
        # random number set
        if self.correlated is False:
            ran = sn1[t]
        else:
            # only with correlation in portfolio context
```

```
ran = np.dot(self.cholesky_matrix, sn1[:, t, :])
        ran = ran[self.rn_set]
    dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count
    # difference between two dates as year fraction
    poi = np.random.poisson(self.lamb * dt, I)
    # Poisson-distributed pseudo-random numbers for jump component
    paths[t] = paths[t - 1] * (
        np.exp((short_rate - rj -
                0.5 * self.volatility ** 2) * dt +
               self.volatility * np.sqrt(dt) * ran) +
        (np.exp(self.mu + self.delt * sn2[t]) - 1) * poi)
self.instrument_values = paths
```

Of course, since this is a different model, it needs a different set of elements in the dx.market\_environment object. In addition to those for the generic simulation class (see Table 18-1), there are three parameters required, as outlined in [Table](#page-20-0) 18-2: namely, the parameters of the log-normal jump component, lambda, mu, and delta.

<span id="page-20-0"></span>*Table 18-2. Specific elements of the market environment for dx.jump\_diffusion class*

| Element | Type     | Mandatory | Description                                 |
|---------|----------|-----------|---------------------------------------------|
| lambda  | Constant | Yes       | Jump<br>intensity<br>(probability<br>p.a.)  |
| mu      | Constant | Yes       | Expected<br>jump<br>size                    |
| delta   | Constant | Yes       | Standard<br>deviation<br>of<br>jump<br>size |

For the generation of the paths, this class needs further random numbers because of the jump component. Inline comments in the method generate\_paths() highlight the two spots where these additional random numbers are generated. For the generation of Poisson-distributed random numbers, see also Chapter 12.

### **A Use Case**

The following interactive session illustrates how to use the simulation class dx.jump\_diffusion. The dx.market\_environment object defined for the GBM object is used as a basis:

```
In [47]: me_jd = market_environment('me_jd', dt.datetime(2020, 1, 1))
In [48]: me_jd.add_constant('lambda', 0.3)
         me_jd.add_constant('mu', -0.75)
         me_jd.add_constant('delta', 0.1)
In [49]: me_jd.add_environment(me_gbm)
In [50]: from jump_diffusion import jump_diffusion
In [51]: jd = jump_diffusion('jd', me_jd)
In [52]: %time paths_3 = jd.get_instrument_values()
         CPU times: user 28.6 ms, sys: 4.37 ms, total: 33 ms
         Wall time: 49.4 ms
In [53]: jd.update(lamb=0.9)
In [54]: %time paths_4 = jd.get_instrument_values()
         CPU times: user 29.7 ms, sys: 3.58 ms, total: 33.3 ms
         Wall time: 66.7 ms
```

The three additional parameters for the dx.jump\_diffusion object. These are specific to the simulation class.

Adds a complete environment to the existing one.

Simulates the paths with the base parameters.

Increases the jump intensity parameters.

Simulates the paths with the updated parameter.

Figure 18-2 compares a couple of simulated paths from the two sets with low and high intensity (jump probability), respectively. It is easy to spot several jumps for the low-intensity case and the multiple jumps for the high-intensity

case in the figure:

```
In [55]: plt.figure(figsize=(10, 6))
         p1 = plt.plot(gbm.time_grid, paths_3[:, :10], 'b')
         p2 = plt.plot(gbm.time_grid, paths_4[:, :10], 'r-.')
         l1 = plt.legend([p1[0], p2[0]],
                         ['low intensity', 'high intensity'], loc=3)
         plt.gca().add_artist(l1)
         plt.xticks(rotation=30);
```

![](_page_22_Figure_2.jpeg)

*Figure 18-2. Simulated paths from jump diffusion simulation class*

# **Square-Root Diffusion**

The third stochastic process to be simulated is the square-root diffusion as used, for example, by Cox, Ingersoll, and Ross (1985) to model stochastic short rates. [Equation](#page-23-0) 18-5 shows the stochastic differential equation of the process (see also Equation 12-4 in Chapter 12 for further details).

<span id="page-23-0"></span>*Equation 18-5. Stochastic differential equation of square-root diffusion*

$$dx_t = \kappa(\theta - x_t)dt + \sigma\sqrt{x_t}dZ_t$$

The code uses the discretization scheme as presented in [Equation](#page-23-1) 18-6 (see also Equation 12-5 in Chapter 12, as well as Equation 12-6 for an alternative, exact scheme).

<span id="page-23-1"></span>*Equation 18-6. Euler discretization for square-root diffusion (full truncation scheme)*

$$\widetilde{x}_{t_{m+1}} = \widetilde{x}_{t_m} + \kappa(\theta - \widetilde{x}_s^+) (t_{m+1} - t_m) + \sigma \sqrt{\widetilde{x}_s^+} \sqrt{t_{m+1} - t_m} z_t$$
  
$$x_{t_{m+1}} = \widetilde{x}_{t_{m^*1}}$$

### **The Simulation Class**

Following is the Python code for the dx.square\_root\_diffusion simulation class, which is the third and final one. Apart from, of course, a different model and discretization scheme, the class does not contain anything new compared to the other two specialized classes:

```
#
# DX Package
#
# Simulation Class -- Square-Root Diffusion
#
# square_root_diffusion.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
```

```
from sn_random_numbers import sn_random_numbers
from simulation_class import simulation_class
```

```
class square_root_diffusion(simulation_class):
    ''' Class to generate simulated paths based on
    the Cox-Ingersoll-Ross (1985) square-root diffusion model.
```

```
Attributes
==========
name : string
    name of the object
mar_env : instance of market_environment
    market environment data for simulation
corr : Boolean
    True if correlated with other model object
```

```
Methods
=======
update :
    updates parameters
generate_paths :
    returns Monte Carlo paths given the market environment
'''
```

```
def __init__(self, name, mar_env, corr=False):
    super(square_root_diffusion, self).__init__(name, mar_env, corr)
```

```
# additional parameters needed
    self.kappa = mar_env.get_constant('kappa')
    self.theta = mar_env.get_constant('theta')
def update(self, initial_value=None, volatility=None, kappa=None,
           theta=None, final_date=None):
    if initial_value is not None:
        self.initial_value = initial_value
    if volatility is not None:
        self.volatility = volatility
    if kappa is not None:
        self.kappa = kappa
    if theta is not None:
        self.theta = theta
    if final_date is not None:
        self.final_date = final_date
    self.instrument_values = None
def generate_paths(self, fixed_seed=True, day_count=365.):
    if self.time_grid is None:
        self.generate_time_grid()
    M = len(self.time_grid)
    I = self.paths
    paths = np.zeros((M, I))
    paths_ = np.zeros_like(paths)
    paths[0] = self.initial_value
    paths_[0] = self.initial_value
    if self.correlated is False:
        rand = sn_random_numbers((1, M, I),
                                 fixed_seed=fixed_seed)
    else:
        rand = self.random_numbers
    for t in range(1, len(self.time_grid)):
        dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count
        if self.correlated is False:
            ran = rand[t]
        else:
            ran = np.dot(self.cholesky_matrix, rand[:, t, :])
            ran = ran[self.rn_set]
        # full truncation Euler discretization
        paths_[t] = (paths_[t - 1] + self.kappa *
                     (self.theta - np.maximum(0, paths_[t - 1, :])) * dt +
                     np.sqrt(np.maximum(0, paths_[t - 1, :])) *
                     self.volatility * np.sqrt(dt) * ran)
        paths[t] = np.maximum(0, paths_[t])
    self.instrument_values = paths
```

Table 18-3 lists the two elements of the market environment that are specific to this class.

> *Table 18-3. Specific elements of the market environment for dx.square\_root\_diffusion class*

| Element | Type     | Mandatory | Description                        |
|---------|----------|-----------|------------------------------------|
| kappa   | Constant | Yes       | Mean<br>reversion<br>factor        |
| theta   | Constant | Yes       | Long-term<br>mean<br>of<br>process |

*environment for dx.square\_root\_diffusion class*

### **A Use Case**

A rather brief example illustrates the use of the simulation class. As usual, one needs a market environment, for example, to model a volatility (index) process:

```
In [56]: me_srd = market_environment('me_srd', dt.datetime(2020, 1, 1))
In [57]: me_srd.add_constant('initial_value', .25)
         me_srd.add_constant('volatility', 0.05)
         me_srd.add_constant('final_date', dt.datetime(2020, 12, 31))
         me_srd.add_constant('currency', 'EUR')
         me_srd.add_constant('frequency', 'W')
         me_srd.add_constant('paths', 10000)
In [58]: me_srd.add_constant('kappa', 4.0)
         me_srd.add_constant('theta', 0.2)
In [59]: me_srd.add_curve('discount_curve', constant_short_rate('r', 0.0))
In [60]: from square_root_diffusion import square_root_diffusion
In [61]: srd = square_root_diffusion('srd', me_srd)
In [62]: srd_paths = srd.get_instrument_values()[:, :10]
```

Additional parameters for the dx.square\_root\_diffusion object.

The discount\_curve object is required by default but not needed for the simulation.

Instantiates the object …

… simulates the paths, and selects 10.

Figure 18-3 illustrates the mean-reverting characteristic by showing how the simulated paths on average revert to the long-term mean theta (dashed line), which is assumed to be 0.2:

```
In [55]: plt.figure(figsize=(10, 6))
         p1 = plt.plot(gbm.time_grid, paths_3[:, :10], 'b')
         p2 = plt.plot(gbm.time_grid, paths_4[:, :10], 'r-.')
         l1 = plt.legend([p1[0], p2[0]],
                         ['low intensity', 'high intensity'], loc=3)
         plt.gca().add_artist(l1)
         plt.xticks(rotation=30);
```

![](_page_28_Figure_0.jpeg)

 $Figure 18-3$ . Simulated paths from square-root diffusion simulation class (dashed line = long-term mean theta)

# **Conclusion**

This chapter develops all the tools and classes needed for the simulation of the three stochastic processes of interest: geometric Brownian motion, jump diffusions, and square-root diffusions. The chapter presents a function to conveniently generate standard normally distributed random numbers. It then proceeds by introducing a generic model simulation class. Based on this foundation, the chapter introduces three specialized simulation classes and presents use cases for these classes.

To simplify future imports one can again use a wrapper module, this one called *dx\_simulation.py*:

```
#
# DX Package
#
# Simulation Functions & Classes
#
# dx_simulation.py
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#
import numpy as np
import pandas as pd
from dx_frame import *
from sn_random_numbers import sn_random_numbers
from simulation_class import simulation_class
from geometric_brownian_motion import geometric_brownian_motion
from jump_diffusion import jump_diffusion
from square_root_diffusion import square_root_diffusion
```

As with the first wrapper module, *dx\_frame.py*, the benefit is that a single import statement makes available all simulation components:

**from dx\_simulation import** \*

Since *dx\_simulation.py* also imports everything from *dx\_frame.py*, this single import in fact exposes *all functionality* developed so far. The same holds true for the enhanced *\_\_init\_\_.py* file in the *dx* folder:

*# # DX Package # packaging file*

```
# __init__.py
#
import numpy as np
import pandas as pd
import datetime as dt
```

*# frame* **from get\_year\_deltas import** get\_year\_deltas **from constant\_short\_rate import** constant\_short\_rate **from market\_environment import** market\_environment

*# simulation* **from sn\_random\_numbers import** sn\_random\_numbers **from simulation\_class import** simulation\_class **from geometric\_brownian\_motion import** geometric\_brownian\_motion **from jump\_diffusion import** jump\_diffusion **from square\_root\_diffusion import** square\_root\_diffusion
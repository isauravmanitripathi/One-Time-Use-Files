# **Chapter 11. Mathematical Tools**

The mathematicians are the priests of the modern world. Bill Gaede

Since the arrival of the so-called Rocket Scientists on Wall Street in the 1980s and 1990s, finance has evolved into a discipline of applied mathematics. While early research papers in finance came with lots of text and few mathematical expressions and equations, current ones are mainly comprised of mathematical expressions and equations with some explanatory text around.

This chapter introduces some useful mathematical tools for finance, without providing a detailed background for each of them. There are many useful books available on this topic, so this chapter focuses on how to use the tools and techniques with Python. In particular, it covers:

## *"Approximation"*

Regression and interpolation are among the most often used numerical techniques in finance.

## *"Convex Optimization"*

A number of financial disciplines need tools for convex optimization (for instance, derivatives analytics when it comes to model calibration).

## *"Integration"*

In particular, the valuation of financial (derivative) assets often boils down to the evaluation of integrals.

## *"Symbolic Computation"*

Python provides with SymPy a powerful package for symbolic mathematics, for example, to solve (systems of) equations.

# **Approximation**

To begin with, the usual imports:

```
In [1]: import numpy as np
        from pylab import plt, mpl
In [2]: plt.style.use('seaborn')
        mpl.rcParams['font.family'] = 'serif'
        %matplotlib inline
```

Throughout this section, the main example function is the following, which is comprised of a trigonometric term and a linear term:

```
In [3]: def f(x):
            return np.sin(x) + 0.5 * x
```

The main focus is the approximation of this function over a given interval by *regression* and *interpolation* techniques. First, a plot of the function to get a better view of what exactly the approximation shall achieve. The interval of interest shall be [–2π, 2π]. Figure 11-1 displays the function over the fixed interval defined via the np.linspace() function. The function create\_plot() is a helper function to create the same type of plot required multiple times in this chapter:

```
In [4]: def create_plot(x, y, styles, labels, axlabels):
            plt.figure(figsize=(10, 6))
            for i in range(len(x)):
                plt.plot(x[i], y[i], styles[i], label=labels[i])
                plt.xlabel(axlabels[0])
                plt.ylabel(axlabels[1])
            plt.legend(loc=0)
In [5]: x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
In [6]: create_plot([x], [f(x)], ['b'], ['f(x)'], ['x', 'f(x)'])
```

The *x* values used for the plotting and the calculations.

![](_page_2_Figure_0.jpeg)

*Figure 11-1. Example function plot*

# **Regression**

Regression is a rather efficient tool when it comes to function approximation. It is not only suited to approximating one-dimensional functions but also works well in higher dimensions. The numerical techniques needed to come up with regression results are easily implemented and quickly executed. Basically, the task of regression, given a set of so-called basis functions , is to find optimal parameters according to [Equation](#page-3-0) 11-1, where for observation points. The are considered *independent* observations and the *dependent* observations (in a functional or statistical sense).

<span id="page-3-0"></span>*Equation 11-1. Minimization problem of regression*

![](_page_3_Figure_3.jpeg)

## **Monomials as basis functions**

One of the simplest cases is to take monomials as basis functions — i.e., . In such a case, NumPy has built-in functions for both the determination of the optimal parameters (namely, np.polyfit()) and the evaluation of the approximation given a set of input values (namely, np.polyval()).

Table 11-1 lists the parameters the np.polyfit() function takes. Given the returned optimal regression coefficients p from np.polyfit(), np.polyval(p, x) then returns the regression values for the *x* coordinates.

*Table 11-1. Parameters of polyfit() function*

| Parameter | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| x         | x<br>coordinates<br>(independent<br>variable<br>values)               |
| y         | y<br>coordinates<br>(dependent<br>variable<br>values)                 |
| deg       | Degree<br>of<br>the<br>fitting<br>polynomial                          |
| full      | If<br>True,<br>returns<br>diagnostic<br>information<br>in<br>addition |
| w         | Weights<br>to<br>apply<br>to<br>the<br>y<br>coordinates               |
| cov       | If<br>True,<br>returns<br>covariance<br>matrix<br>in<br>addition      |

In typical vectorized fashion, the application of np.polyfit() and np.polyval() takes on the following form for a linear regression (i.e., for deg=1). Given the regression estimates stored in the ry array, we can compare the regression result with the original function as presented in Figure 11-2. Of course, a linear regression cannot account for the sin part of the example function:

```
In [7]: res = np.polyfit(x, f(x), deg=1, full=True)
In [8]: res
Out[8]: (array([ 4.28841952e-01, -1.31499950e-16]),
         array([21.03238686]),
         2,
         array([1., 1.]),
         1.1102230246251565e-14)
In [9]: ry = np.polyval(res[0], x)
In [10]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

Linear regression step.

Full results: regression parameters, residuals, effective rank, singular values, and relative condition number.

Evaluation using the regression parameters.

![](_page_5_Figure_0.jpeg)

*Figure 11-2. Linear regression*

To account for the sin part of the example function, higher-order monomials are necessary. The next regression attempt takes monomials up to the order of 5 as basis functions. It should not be too surprising that the regression result, as seen in Figure 11-3, now looks much closer to the original function. However, it is still far from being perfect:

```
In [11]: reg = np.polyfit(x, f(x), deg=5)
         ry = np.polyval(reg, x)
In [12]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

![](_page_6_Figure_0.jpeg)

*Figure 11-3. Regression with monomials up to order 5*

The last attempt takes monomials up to order 7 to approximate the example function. In this case the result, as presented in Figure 11-4, is quite convincing:

```
In [13]: reg = np.polyfit(x, f(x), 7)
         ry = np.polyval(reg, x)
In [14]: np.allclose(f(x), ry)
Out[14]: False
In [15]: np.mean((f(x) - ry) ** 2)
Out[15]: 0.0017769134759517689
In [16]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

Checks whether the function and regression values are the same (or at least close).

Calculates the *Mean Squared Error* (MSE) for the regression values given the function values.

![](_page_7_Figure_0.jpeg)

*Figure 11-4. Regression with monomials up to order 7*

## **Individual basis functions**

In general, one can reach better regression results by choosing better sets of basis functions, e.g., by exploiting knowledge about the function to approximate. In this case, the individual basis functions have to be defined via a matrix approach (i.e., using a NumPy ndarray object). First, the case with monomials up to order 3 (Figure 11-5). The central function here is np.linalg.lstsq():

```
In [17]: matrix = np.zeros((3 + 1, len(x)))
        matrix[3, :] = x ** 3
        matrix[2, :] = x ** 2
        matrix[1, :] = x
        matrix[0, :] = 1
In [18]: reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]
In [19]: reg.round(4)
Out[19]: array([ 0. , 0.5628, -0. , -0.0054])
In [20]: ry = np.dot(reg, matrix)
In [21]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                    ['f(x)', 'regression'], ['x', 'f(x)'])
```

The ndarray object for the basis function values (matrix).

The basis function values from constant to cubic.

The regression step.

The optimal regression parameters.

The regression estimates for the function values.

<span id="page-8-0"></span>![](_page_8_Figure_10.jpeg)

*Figure 11-5. Regression with individual basis functions*

The result in [Figure](#page-8-0) 11-5 is not as good as expected based on our previous experience with monomials. Using the more general approach allows us to exploit knowledge about the example function — namely that there is a sin part in the function. Therefore, it makes sense to include a sine function in the set of basis functions. For simplicity, the highest-order monomial is replaced. The fit

now is perfect, as the numbers and Figure 11-6 illustrate:

```
In [22]: matrix[3, :] = np.sin(x)
In [23]: reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]
In [24]: reg.round(4)
Out[24]: array([0. , 0.5, 0. , 1. ])
In [25]: ry = np.dot(reg, matrix)
In [26]: np.allclose(f(x), ry)
Out[26]: True
In [27]: np.mean((f(x) - ry) ** 2)
Out[27]: 3.404735992885531e-31
In [28]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

The new basis function exploiting knowledge about the example function.

The optimal regression parameters recover the original parameters.

The regression now leads to a perfect fit.

![](_page_10_Figure_0.jpeg)

*Figure 11-6. Regression with the sine basis function*

## **Noisy data**

Regression can cope equally well with *noisy* data, be it data from simulation or from (nonperfect) measurements. To illustrate this point, independent observations with noise and dependent observations with noise are generated. Figure 11-7 reveals that the regression results are closer to the original function than the noisy data points. In a sense, the regression averages out the noise to some extent:

```
In [29]: xn = np.linspace(-2 * np.pi, 2 * np.pi, 50)
         xn = xn + 0.15 * np.random.standard_normal(len(xn))
         yn = f(xn) + 0.25 * np.random.standard_normal(len(xn))
In [30]: reg = np.polyfit(xn, yn, 7)
         ry = np.polyval(reg, xn)
In [31]: create_plot([x, x], [f(x), ry], ['b', 'r.'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

The new deterministic *x* values.

Introducing noise to the *x* values.

Introducing noise to the *y* values.

![](_page_11_Figure_3.jpeg)

*Figure 11-7. Regression for noisy data*

## **Unsorted data**

Another important aspect of regression is that the approach also works seamlessly with unsorted data. The previous examples all rely on sorted *x* data. This does not have to be the case. To make the point, let's look at yet another randomization approach for the *x* values. In this case, one can hardly identify any structure by just visually inspecting the raw data:

```
In [32]: xu = np.random.rand(50) * 4 * np.pi - 2 * np.pi
        yu = f(xu)
In [33]: print(xu[:10].round(2))
        print(yu[:10].round(2))
        [-4.17 -0.11 -1.91 2.33 3.34 -0.96 5.81 4.92 -4.56 -5.42]
        [-1.23 -0.17 -1.9 1.89 1.47 -1.29 2.45 1.48 -1.29 -1.95]
In [34]: reg = np.polyfit(xu, yu, 5)
```

```
ry = np.polyval(reg, xu)
In [35]: create_plot([xu, xu], [yu, ry], ['b.', 'ro'],
                     ['f(x)', 'regression'], ['x', 'f(x)'])
```

Randomizes the *x* values.

As with the noisy data, the regression approach does not care for the order of the observation points. This becomes obvious upon inspecting the structure of the minimization problem in Equation 11-1. It is also obvious by the results, presented in [Figure](#page-12-0) 11-8.

<span id="page-12-0"></span>![](_page_12_Figure_4.jpeg)

*Figure 11-8. Regression for unsorted data*

## **Multiple dimensions**

Another convenient characteristic of the least-squares regression approach is that it carries over to multiple dimensions without too many modifications. As an example function take fm(), as presented next:

```
In [36]: def fm(p):
             x, y = p
```

```
return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2
```

<span id="page-13-0"></span>To properly visualize this function, *grids* (in two dimensions) of independent data points are needed. Based on such two-dimensional grids of independent and resulting dependent data points, embodied in the following by X, Y, and Z, [Figure](#page-13-0) 11-9 presents the shape of the function fm():

```
In [37]: x = np.linspace(0, 10, 20)
         y = np.linspace(0, 10, 20)
         X, Y = np.meshgrid(x, y)
In [38]: Z = fm((X, Y))
         x = X.flatten()
         y = Y.flatten()
In [39]: from mpl_toolkits.mplot3d import Axes3D
In [40]: fig = plt.figure(figsize=(10, 6))
         ax = fig.gca(projection='3d')
         surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                                cmap='coolwarm', linewidth=0.5,
                                antialiased=True)
         ax.set_xlabel('x')
         ax.set_ylabel('y')
         ax.set_zlabel('f(x, y)')
         fig.colorbar(surf, shrink=0.5, aspect=5)
```

Generates 2D ndarray objects ("grids") out of the 1D ndarray objects.

Yields 1D ndarray objects from the 2D ndarray objects.

Imports the 3D plotting capabilities from matplotlib as required.

![](_page_14_Figure_0.jpeg)

*Figure 11-9. The function with two parameters*

To get good regression results, the set of basis functions is essential. Therefore, factoring in knowledge about the function fm() itself, both an np.sin() and an np.sqrt() function are included. Figure 11-10 shows the perfect regression results visually:

```
In [41]: matrix = np.zeros((len(x), 6 + 1))
         matrix[:, 6] = np.sqrt(y)
         matrix[:, 5] = np.sin(x)
         matrix[:, 4] = y ** 2
         matrix[:, 3] = x ** 2
         matrix[:, 2] = y
         matrix[:, 1] = x
         matrix[:, 0] = 1
In [42]: reg = np.linalg.lstsq(matrix, fm((x, y)), rcond=None)[0]
In [43]: RZ = np.dot(matrix, reg).reshape((20, 20))
In [44]: fig = plt.figure(figsize=(10, 6))
         ax = fig.gca(projection='3d')
         surf1 = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                     cmap=mpl.cm.coolwarm, linewidth=0.5,
                     antialiased=True)
         surf2 = ax.plot_wireframe(X, Y, RZ, rstride=2, cstride=2,
                                   label='regression')
         ax.set_xlabel('x')
```

```
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()
fig.colorbar(surf, shrink=0.5, aspect=5)
```

The np.sqrt() function for the y parameter.

The np.sin() function for the x parameter.

Transforms the regression results to the grid structure.

Plots the original function surface.

Plots the regression surface.

![](_page_16_Figure_0.jpeg)

*Figure 11-10. Regression surface for function with two parameters*

## **REGRESSION**

Least-squares regression approaches have multiple areas of application, including simple function approximation and function approximation based on noisy or unsorted data. These approaches can be applied to one-dimensional as well as multidimensional problems. Due to the underlying mathematics, the application is "almost always the same."

# **Interpolation**

Compared to regression, *interpolation* (e.g., with cubic splines) is more involved mathematically. It is also limited to low-dimensional problems. Given an ordered set of observation points (ordered in the *x* dimension), the basic idea is to do a regression between two neighboring data points in such a way that not only are the data points perfectly matched by the resulting piecewise-defined interpolation function, but also the function is continuously differentiable at the data points. Continuous differentiability requires at least interpolation of degree 3 — i.e., with cubic splines. However, the approach also works in general with quadratic and even linear splines.

```
The following code implements a linear splines interpolation, the result of which
is shown in Figure 11-11: In [45]: import scipy.interpolate as spi In
[46]: x = np.linspace(-2 * np.pi, 2 * np.pi, 25) In [47]: def f(x):
return np.sin(x) + 0.5 * x In [48]: ipo = spi.splrep(x, f(x), k=1)
  In [49]: iy = spi.splev(x, ipo) In [50]: np.allclose(f(x), iy)
  Out[50]: True In [51]: create_plot([x, x], [f(x), iy], ['b',
'ro'], ['f(x)', 'interpolation'], ['x', 'f(x)'])
```

Imports the required subpackage from SciPy.

Implements a linear spline interpolation.

Derives the interpolated values.

Checks whether the interpolated values are close (enough) to the function values.

![](_page_19_Figure_0.jpeg)

*Figure 11-11. Linear splines interpolation (complete data set)*

The application itself, given an *x*-ordered set of data points, is as simple as the application of np.polyfit() and np.polyval(). Here, the respective functions are sci.splrep() and sci.splev(). [Table](#page-19-0) 11-2 lists the major parameters that the sci.splrep() function takes.

<span id="page-19-0"></span>

| Parameter | Description                                                          |
|-----------|----------------------------------------------------------------------|
| x         | (Ordered)<br>x<br>coordinates<br>(independent<br>variable<br>values) |
| y         | (x-ordered)<br>y<br>coordinates<br>(dependent<br>variable<br>values) |
| w         | Weights<br>to<br>apply<br>to<br>the<br>y<br>coordinates              |
| xb,<br>xe | Interval<br>to<br>fit;<br>if<br>None then<br>[x[0], x[-1]]           |
| k         | Order<br>of<br>the<br>spline<br>fit<br>(<br>)                        |
| s         | Smoothing<br>factor<br>(the<br>larger,<br>the<br>more<br>smoothing)  |

*Table 11-2. Parameters of splrep() function*

full\_output If True, returns additional output

quiet If True, suppresses messages

[Table](#page-20-0) 11-3 lists the parameters that the sci.splev() function takes.

<span id="page-20-0"></span>

| Parameter | Description                                                                                                                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| x         | (Ordered)<br>x<br>coordinates<br>(independent<br>variable<br>values)                                                               |
| tck       | Sequence<br>of<br>length<br>3<br>returned<br>by<br>splrep() (knots,<br>coefficients,<br>degree)                                    |
| der       | Order<br>of<br>derivative<br>(0<br>for<br>function,<br>1 for<br>first<br>derivative)                                               |
| ext       | Behavior<br>if<br>x not<br>in<br>knot<br>sequence<br>(0<br>=<br>extrapolate,<br>1 =<br>return<br>0,<br>2 =<br>raise<br>ValueError) |

*Table 11-3. Parameters of splev() function*

Spline interpolation is often used in finance to generate estimates for dependent values of independent data points not included in the original observations. To this end, the next example picks a much smaller interval and has a closer look at the interpolated values with the linear splines. Figure 11-12 reveals that the interpolation function indeed interpolates *linearly* between two observation points. For certain applications this might not be precise enough. In addition, it is evident that the function is not continuously differentiable at the original data points — another drawback: In [52]: xd = np.linspace(1.0, 3.0, 50) iyd = spi.splev(xd, ipo) In [53]: create\_plot([xd, xd], [f(xd), iyd], ['b', 'ro'], ['f(x)', 'interpolation'], ['x', 'f(x)'])

Smaller interval with more points.

![](_page_21_Figure_0.jpeg)

*Figure 11-12. Linear splines interpolation (data subset)*

A repetition of the complete exercise, this time using cubic splines, improves the results considerably (see Figure 11-13): In [54]: ipo = spi.splrep(x, f(x), k=3) iyd = spi.splev(xd, ipo) In [55]: np.allclose(f(xd), iyd) Out[55]: False In [56]: np.mean((f(xd) - iyd) \*\* 2) Out[56]: 1.1349319851436892e-08 In [57]: create\_plot([xd, xd], [f(xd), iyd], ['b', 'ro'], ['f(x)', 'interpolation'], ['x', 'f(x)'])

Cubic splines interpolation on complete data sets.

Results applied to the smaller interval.

The interpolation is still not perfect …

… but better than before.

![](_page_22_Figure_0.jpeg)

*Figure 11-13. Cubic splines interpolation (data subset)*

## **INTERPOLATION**

In those cases where spline interpolation can be applied, one can expect better approximation results compared to a least-squares regression approach. However, remember that sorted (and "non-noisy") data is required and that the approach is limited to low-dimensional problems. It is also computationally more demanding and might therefore take (much) longer than regression in certain use cases.

# <span id="page-24-0"></span>**Convex Optimization**

In finance and economics, *convex optimization* plays an important role. Examples are the calibration of option pricing models to market data or the optimization of an agent's utility function. As an example, take the function fm():

```
In [58]: def fm(p):
             x, y = p
             return (np.sin(x) + 0.05 * x ** 2
                   + np.sin(y) + 0.05 * y ** 2)
```

[Figure](#page-24-0) 11-14 shows the function graphically for the defined intervals for x and y. Visual inspection already reveals that this function has multiple local minima. The existence of a global minimum cannot really be confirmed by this particular graphical representation, but it seems to exist:

```
In [59]: x = np.linspace(-10, 10, 50)
         y = np.linspace(-10, 10, 50)
         X, Y = np.meshgrid(x, y)
         Z = fm((X, Y))
In [60]: fig = plt.figure(figsize=(10, 6))
         ax = fig.gca(projection='3d')
         surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                                cmap='coolwarm', linewidth=0.5,
                                antialiased=True)
         ax.set_xlabel('x')
         ax.set_ylabel('y')
         ax.set_zlabel('f(x, y)')
         fig.colorbar(surf, shrink=0.5, aspect=5)
```

![](_page_25_Figure_0.jpeg)

*Figure 11-14. Linear splines interpolation (data subset)*

# **Global Optimization**

In what follows, both a *global* minimization approach and a *local* one are implemented. The functions sco.brute() and sco.fmin() that are applied are from scipy.optimize.

To have a closer look behind the scenes during minimization procedures, the following code amends the original function by an option to output current parameter values as well as the function value. This allows us to keep track of all relevant information for the procedure:

```
In [61]: import scipy.optimize as sco
In [62]: def fo(p):
            x, y = p
            z = np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2
            if output == True:
                print('%8.4f | %8.4f | %8.4f' % (x, y, z))
            return z
In [63]: output = True
        sco.brute(fo, ((-10, 10.1, 5), (-10, 10.1, 5)), finish=None)
        -10.0000 | -10.0000 | 11.0880
        -10.0000 | -10.0000 | 11.0880
        -10.0000 | -5.0000 | 7.7529
        -10.0000 | 0.0000 | 5.5440
        -10.0000 | 5.0000 | 5.8351
        -10.0000 | 10.0000 | 10.0000
         -5.0000 | -10.0000 | 7.7529
         -5.0000 | -5.0000 | 4.4178
         -5.0000 | 0.0000 | 2.2089
         -5.0000 | 5.0000 | 2.5000
         -5.0000 | 10.0000 | 6.6649
          0.0000 | -10.0000 | 5.5440
          0.0000 | -5.0000 | 2.2089
          0.0000 | 0.0000 | 0.0000
          0.0000 | 5.0000 | 0.2911
          0.0000 | 10.0000 | 4.4560
          5.0000 | -10.0000 | 5.8351
          5.0000 | -5.0000 | 2.5000
          5.0000 | 0.0000 | 0.2911
          5.0000 | 5.0000 | 0.5822
          5.0000 | 10.0000 | 4.7471
         10.0000 | -10.0000 | 10.0000
         10.0000 | -5.0000 | 6.6649
         10.0000 | 0.0000 | 4.4560
         10.0000 | 5.0000 | 4.7471
         10.0000 | 10.0000 | 8.9120
```

Out[63]: array([0., 0.])

Imports the required subpackage from SciPy.

The information to print out if output = True.

The brute force optimization.

The optimal parameter values, given the initial parameterization of the function, are x = y = 0. The resulting function value is also 0, as a quick review of the preceding output reveals. One might be inclined to accept this as the global minimum. However, the first parameterization here is quite rough, in that step sizes of 5 for both input parameters are used. This can of course be refined considerably, leading to better results in this case — and showing that the previous solution is not the optimal one:

```
In [64]: output = False
         opt1 = sco.brute(fo, ((-10, 10.1, 0.1), (-10, 10.1, 0.1)), finish=None)
In [65]: opt1
Out[65]: array([-1.4, -1.4])
In [66]: fm(opt1)
Out[66]: -1.7748994599769203
```

The optimal parameter values are now x = y = –1.4 and the minimal function value for the global minimization is about –1.7749.

# **Local Optimization**

The local convex optimization that follows draws on the results from the global optimization. The function sco.fmin() takes as input the function to minimize and the starting parameter values. Optional parameter values are the input parameter tolerance and function value tolerance, as well as the maximum number of iterations and function calls. The local optimization further improves the result:

```
In [67]: output = True
        opt2 = sco.fmin(fo, opt1, xtol=0.001, ftol=0.001,
                        maxiter=15, maxfun=20)
         -1.4000 | -1.4000 | -1.7749
         -1.4700 | -1.4000 | -1.7743
         -1.4000 | -1.4700 | -1.7743
         -1.3300 | -1.4700 | -1.7696
         -1.4350 | -1.4175 | -1.7756
         -1.4350 | -1.3475 | -1.7722
         -1.4088 | -1.4394 | -1.7755
         -1.4438 | -1.4569 | -1.7751
         -1.4328 | -1.4427 | -1.7756
         -1.4591 | -1.4208 | -1.7752
         -1.4213 | -1.4347 | -1.7757
         -1.4235 | -1.4096 | -1.7755
         -1.4305 | -1.4344 | -1.7757
         -1.4168 | -1.4516 | -1.7753
         -1.4305 | -1.4260 | -1.7757
         -1.4396 | -1.4257 | -1.7756
         -1.4259 | -1.4325 | -1.7757
         -1.4259 | -1.4241 | -1.7757
         -1.4304 | -1.4177 | -1.7757
         -1.4270 | -1.4288 | -1.7757
        Warning: Maximum number of function evaluations has been exceeded.
In [68]: opt2
Out[68]: array([-1.42702972, -1.42876755])
In [69]: fm(opt2)
Out[69]: -1.7757246992239009
```

The local convex optimization.

For many convex optimization problems it is advisable to have a global minimization before the local one. The major reason for this is that local convex optimization algorithms can easily be trapped in a local minimum (or do "basin hopping"), ignoring completely better local minima and/or a global minimum. The following shows that setting the starting parameterization to x = y = 2

gives, for example, a "minimum" value of above zero:

```
In [70]: output = False
         sco.fmin(fo, (2.0, 2.0), maxiter=250)
         Optimization terminated successfully.
                  Current function value: 0.015826
                  Iterations: 46
                  Function evaluations: 86
```

Out[70]: array([4.2710728 , 4.27106945])

# **Constrained Optimization**

So far, this section only considers unconstrained optimization problems. However, large classes of economic or financial optimization problems are constrained by one or multiple constraints. Such constraints can formally take on the form of equalities or inequalities.

As a simple example, consider the utility maximization problem of an (expected utility maximizing) investor who can invest in two risky securities. Both securities cost USD today. After one year, they have a payoff of 15 USD and 5 USD, respectively, in state *u*, and of 5 USD and 12 USD, respectively, in state *d*. Both states are equally likely. Denote the vector payoffs for the two securities by and , respectively.

The investor has a budget of USD to invest and derives utility from future wealth according to the utility function , where *w* is the wealth (USD amount) available. [Equation](#page-30-0) 11-2 is a formulation of the maximization problem where *a*, *b* are the numbers of securities bought by the investor.

<span id="page-30-0"></span>*Equation 11-2. Expected utility maximization problem (1)*

$$\begin{array}{rcl}\n\max_{a,b} \mathbf{E}(u(w_1)) & = & p\sqrt{w_{1u}} + (1-p)\sqrt{w_{1d}} \\
w_1 & = & a \cdot r_a + b \cdot r_b \\
w_0 & \geq & a \cdot q_a + b \cdot q_b \\
a, b & \geq & 0\n\end{array}$$

Putting in all numerical assumptions, one gets the problem in Equation 11-3. Note the change to the minimization of the negative expected utility.

*Equation 11-3. Expected utility maximization problem (2)*

<span id="page-31-0"></span>
$$\begin{array}{rcl}\n\min_{a,b} - \mathbf{E}(u(w_1)) &=& -(0.5 \cdot \sqrt{w_{1u}} + 0.5 \cdot \sqrt{w_{1d}}) \\
w_{1u} &=& a \cdot 15 + b \cdot 5 \\
w_{1d} &=& a \cdot 5 + b \cdot 12 \\
100 & \geq& a \cdot 10 + b \cdot 10 \\
a, b & \geq& 0\n\end{array}$$

To solve this problem, the scipy.optimize.minimize() function is appropriate. This function takes as input — in addition to the function to be minimized conditions in the form of equalities and inequalities (as a list of dict objects) as well as boundaries for the parameters (as a tuple of tuple objects). <sup>1</sup> The following translates the problem from [Equation](#page-31-0) 11-3 into Python code:

```
In [71]: import math
In [72]: def Eu(p):
             s, b = p
             return -(0.5 * math.sqrt(s * 15 + b * 5) +
                      0.5 * math.sqrt(s * 5 + b * 12))
In [73]: cons = ({'type': 'ineq',
                  'fun': lambda p: 100 - p[0] * 10 - p[1] * 10})
In [74]: bnds = ((0, 1000), (0, 1000))
In [75]: result = sco.minimize(Eu, [5, 5], method='SLSQP',
                                bounds=bnds, constraints=cons)
```

The function to be *minimized*, in order to maximize the expected utility.

The inequality constraint as a dict object.

The boundary values for the parameters (chosen to be wide enough).

The constrained optimization.

The result object contains all the relevant information. With regard to the

minimal function value, one needs to recall to shift the sign back:

```
In [76]: result
Out[76]: fun: -9.700883611487832
              jac: array([-0.48508096, -0.48489535])
          message: 'Optimization terminated successfully.'
             nfev: 21
              nit: 5
             njev: 5
           status: 0
          success: True
                x: array([8.02547122, 1.97452878])
In [77]: result['x']
Out[77]: array([8.02547122, 1.97452878])
In [78]: -result['fun']
Out[78]: 9.700883611487832
In [79]: np.dot(result['x'], [10, 10])
Out[79]: 99.99999999999999
```

The optimal parameter values (i.e., the optimal portfolio).

The negative minimum function value as the optimal solution value.

The budget constraint is binding; all wealth is invested.

# **Integration**

Especially when it comes to valuation and option pricing, integration is an important mathematical tool. This stems from the fact that risk-neutral values of derivatives can be expressed in general as the discounted *expectation* of their payoff under the risk-neutral or martingale measure. The expectation in turn is a sum in the discrete case and an integral in the continuous case. The subpackage scipy.integrate provides different functions for numerical integration. The example function is known from "Approximation": In [80]: **import scipy.integrate as sci** In [81]: **def** f(x): **return** np.sin(x) + 0.5 \* x

The integration interval shall be [0.5, 9.5], leading to the definite integral as in [Equation](#page-33-0) 11-4.

<span id="page-33-0"></span>*Equation 11-4. Integral of example function*

$$\int_{0.5}^{9.5} f(x)dx = \int_{0.5}^{9.5} \sin(x) + \frac{x}{2}dx$$

The following code defines the major Python objects to evaluate the integral: In [82]: x = np.linspace(0, 10) y = f(x) a = 0.5 b = 9.5 Ix = np.linspace(a, b) Iy = f(Ix)

Left integration limit.

Right integration limit.

Integration interval values.

Integration function values.

Figure 11-15 visualizes the integral value as the gray-shaded area under the function: 2

```
In [83]: from matplotlib.patches import Polygon
In [84]: fig, ax = plt.subplots(figsize=(10, 6))
         plt.plot(x, y, 'b', linewidth=2)
         plt.ylim(bottom=0)
         Ix = np.linspace(a, b)
         Iy = f(Ix)
         verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
         poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
         ax.add_patch(poly)
         plt.text(0.75 * (a + b), 1.5, r"$\int_a^b f(x)dx$",
                  horizontalalignment='center', fontsize=20)
         plt.figtext(0.9, 0.075, '$x$')
         plt.figtext(0.075, 0.9, '$f(x)$')
         ax.set_xticks((a, b))
         ax.set_xticklabels(('$a$', '$b$'))
         ax.set_yticks([f(a), f(b)]);
```

![](_page_34_Figure_1.jpeg)

![](_page_34_Figure_2.jpeg)

# **Numerical Integration**

The scipy.integrate subpackage contains a selection of functions to numerically integrate a given mathematical function for upper and lower integration limits. Examples are sci.fixed\_quad() for *fixed Gaussian quadrature*, sci.quad() for *adaptive quadrature*, and sci.romberg() for *Romberg integration*:

```
In [85]: sci.fixed_quad(f, a, b)[0]
Out[85]: 24.366995967084602
In [86]: sci.quad(f, a, b)[0]
Out[86]: 24.374754718086752
In [87]: sci.romberg(f, a, b)
Out[87]: 24.374754718086713
```

There are also a number of integration functions that take as input list or ndarray objects with function values and input values, respectively. Examples in this regard are sci.trapz(), using the *trapezoidal* rule, and sci.simps(), implementing *Simpson's* rule:

```
In [88]: xi = np.linspace(0.5, 9.5, 25)
In [89]: sci.trapz(f(xi), xi)
Out[89]: 24.352733271544516
In [90]: sci.simps(f(xi), xi)
Out[90]: 24.37496418455075
```

# **Integration by Simulation**

The valuation of options and derivatives by Monte Carlo simulation (see Chapter 12) rests on the insight that one can evaluate an integral by simulation. To this end, draw *I* random values of x between the integral limits and evaluate the integration function at every random value for x. Sum up all the function values and take the average to arrive at an average function value over the integration interval. Multiply this value by the length of the integration interval to derive an estimate for the integral value.

The following code shows how the Monte Carlo estimated integral value converges — although not monotonically — to the real one when one increases the number of random draws. The estimator is already quite close for relatively small numbers of random draws:

```
In [91]: for i in range(1, 20):
             np.random.seed(1000)
             x = np.random.random(i * 10) * (b - a) + a
             print(np.mean(f(x)) * (b - a))
         24.804762279331463
         26.522918898332378
         26.265547519223976
         26.02770339943824
         24.99954181440844
         23.881810141621663
         23.527912274843253
         23.507857658961207
         23.67236746066989
         23.679410416062886
         24.424401707879305
         24.239005346819056
         24.115396924962802
         24.424191987566726
         23.924933080533783
         24.19484212027875
         24.117348378249833
         24.100690929662274
         23.76905109847816
```

Number of random x values is increased with every iteration.

# **Symbolic Computation**

The previous sections are mainly concerned with numerical computation. This section now introduces *symbolic* computation, which can be applied beneficially in many areas of finance. To this end, SymPy, a library specifically dedicated to symbolic computation, is generally used.

## **Basics**

SymPy introduces new classes of objects. A fundamental class is the Symbol class:

```
In [92]: import sympy as sy
In [93]: x = sy.Symbol('x')
         y = sy.Symbol('y')
In [94]: type(x)
Out[94]: sympy.core.symbol.Symbol
In [95]: sy.sqrt(x)
Out[95]: sqrt(x)
In [96]: 3 + sy.sqrt(x) - 4 ** 2
Out[96]: sqrt(x) - 13
In [97]: f = x ** 2 + 3 + 0.5 * x ** 2 + 3 / 2
In [98]: sy.simplify(f)
Out[98]: 1.5*x**2 + 4.5
```

Defines symbols to work with.

Applies a function on a symbol.

A numerical expression defined on symbol.

A function defined symbolically.

The function expression simplified.

This already illustrates a major difference to regular Python code. Although x has no numerical value, the square root of x is nevertheless defined with SymPy since x is a Symbol object. In that sense, sy.sqrt(x) can be part of arbitrary mathematical expressions. Notice that SymPy in general automatically simplifies a given mathematical expression. Similarly, one can define arbitrary functions using Symbol objects. They are not to be confused with Python functions.

SymPy provides three basic renderers for mathematical expressions:

- LaTeX-based
- Unicode-based
- ASCII-based

When working, for example, solely in a Jupyter Notebook environment (HTMLbased), LaTeX rendering is generally a good (i.e., visually appealing) choice. The code that follows sticks to the simplest option, ASCII, to illustrate that there is no manual typesetting involved:

```
In [99]: sy.init_printing(pretty_print=False, use_unicode=False)
In [100]: print(sy.pretty(f))
               2
          1.5*x + 4.5
In [101]: print(sy.pretty(sy.sqrt(x) + 0.5))
            ___
          \/ x + 0.5
```

This section cannot go into details, but SymPy also provides many other useful mathematical functions — for example, when it comes to numerically evaluating π. The following example shows the first and final 40 characters of the string representation of π up to the 400,000th digit. It also searches for a six-digit, dayfirst birthday — a popular task in certain mathematics and IT circles:

```
In [102]: %time pi_str = str(sy.N(sy.pi, 400000))
          CPU times: user 400 ms, sys: 10.9 ms, total: 411 ms
          Wall time: 501 ms
In [103]: pi_str[:42]
Out[103]: '3.1415926535897932384626433832795028841971'
In [104]: pi_str[-40:]
Out[104]: '8245672736856312185020980470362464176198'
In [105]: %time pi_str.find('061072')
          CPU times: user 115 µs, sys: 1e+03 ns, total: 116 µs
          Wall time: 120 µs
Out[105]: 80847
```

Returns the string representation of the first 400,000 digits of π.

Shows the first 40 digits …

… and the final 40 digits.

Searches for a birthday date in the string.

# **Equations**

A strength of SymPy is solving equations, e.g., of the form . In general, SymPy presumes that one is looking for a solution to the equation obtained by equating the given expression to zero. Therefore, equations like might have to be reformulated to get the desired result. Of course, SymPy can cope with more complex expressions, like . Finally, it can also deal with problems involving imaginary numbers, such as : In [106]: sy.solve(x \*\* 2 - 1) Out[106]: [-1, 1] In [107]: sy.solve(x \*\* 2 - 1 - 3) Out[107]: [-2, 2] In [108]: sy.solve(x \*\* 3 + 0.5 \* x \*\* 2 - 1) Out[108]: [0.858094329496553, -0.679047164748276 - 0.839206763026694\*I, -0.679047164748276 + 0.839206763026694\*I] In [109]: sy.solve(x \*\* 2 + y \*\* 2) Out[109]: [{x: -I\*y}, {x: I\*y}]

## **Integration and Differentiation**

Another strength of SymPy is integration and differentiation. The example that follows revisits the example function used for numerical-and simulation-based integration and derives both a *symbolically* and a *numerically* exact solution. Symbol objects for the integration limits objects are required to get started:

```
In [110]: a, b = sy.symbols('a b')
In [111]: I = sy.Integral(sy.sin(x) + 0.5 * x, (x, a, b))
In [112]: print(sy.pretty(I))
            b
            /
           |
           | (0.5*x + sin(x)) dx
           |
          /
          a
In [113]: int_func = sy.integrate(sy.sin(x) + 0.5 * x, x)
In [114]: print(sy.pretty(int_func))
                2
          0.25*x - cos(x)
In [115]: Fb = int_func.subs(x, 9.5).evalf()
          Fa = int_func.subs(x, 0.5).evalf()
In [116]: Fb - Fa
Out[116]: 24.3747547180867
```

The Symbol objects for the integral limits.

The Integral object defined and pretty-printed.

The antiderivative derived and pretty-printed.

The values of the antiderivative at the limits, obtained via the .subs() and .evalf() methods.

The exact numerical value of the integral.

The integral can also be solved symbolically with the symbolic integration

The integral can also be solved symbolically with the symbolic integration limits:

```
In [117]: int_func_limits = sy.integrate(sy.sin(x) + 0.5 * x, (x, a, b))
In [118]: print(sy.pretty(int_func_limits))
                 2 2
         - 0.25*a + 0.25*b + cos(a) - cos(b)
In [119]: int_func_limits.subs({a : 0.5, b : 9.5}).evalf()
Out[119]: 24.3747547180868
In [120]: sy.integrate(sy.sin(x) + 0.5 * x, (x, 0.5, 9.5))
Out[120]: 24.3747547180867
```

Solving the integral symbolically.

Solving the integral numerically, using a dict object during substitution.

Solving the integral numerically in a single step.

## **Differentiation**

The derivative of the antiderivative yields in general the original function. Applying the sy.diff() function to the symbolic antiderivative illustrates this:

```
In [121]: int_func.diff()
Out[121]: 0.5*x + sin(x)
```

As with the integration example, differentiation shall now be used to derive the exact solution of the convex minimization problem this chapter looked at earlier. To this end, the respective function is defined symbolically, partial derivatives are derived, and the roots are identified.

A necessary but not sufficient condition for a global minimum is that both partial derivatives are zero. However, there is no guarantee of a symbolic solution. Both algorithmic and (multiple) existence issues come into play here. However, one can solve the two first-order conditions numerically, providing "educated" guesses based on the global and local minimization efforts from before:

```
In [122]: f = (sy.sin(x) + 0.05 * x ** 2
             + sy.sin(y) + 0.05 * y ** 2)
In [123]: del_x = sy.diff(f, x)
          del_x
Out[123]: 0.1*x + cos(x)
In [124]: del_y = sy.diff(f, y)
          del_y
Out[124]: 0.1*y + cos(y)
In [125]: xo = sy.nsolve(del_x, -1.5)
          xo
Out[125]: -1.42755177876459
In [126]: yo = sy.nsolve(del_y, -1.5)
          yo
Out[126]: -1.42755177876459
In [127]: f.subs({x : xo, y : yo}).evalf()
Out[127]: -1.77572565314742
```

The symbolic version of the function.

The two partial derivatives derived and printed.

Educated guesses for the roots and resulting optimal values.

The two partial derivatives derived and printed.

The global minimum function value.

Again, providing uneducated/arbitrary guesses might trap the algorithm in a local minimum instead of the global one:

```
In [128]: xo = sy.nsolve(del_x, 1.5)
          xo
Out[128]: 1.74632928225285
In [129]: yo = sy.nsolve(del_y, 1.5)
          yo
Out[129]: 1.74632928225285
In [130]: f.subs({x : xo, y : yo}).evalf()
Out[130]: 2.27423381055640
```

Uneducated guesses for the roots.

The local minimum function value.

This numerically illustrates that the first-order conditions are necessary but not sufficient.

## **SYMBOLIC COMPUTATIONS**

When doing (financial) mathematics with Python, SymPy and symbolic computations prove to be a valuable tool. Especially for interactive financial analytics, this can be a more efficient approach compared to nonsymbolic approaches.

# **Conclusion**

This chapter covers selected mathematical topics and tools important to finance. For example, the approximation of functions is important in many financial areas, like factor-based models, yield curve interpolation, and regression-based Monte Carlo valuation approaches for American options. Convex optimization techniques are also regularly needed in finance; for example, when calibrating parametric option pricing models to market quotes or implied volatilities of options.

Numerical integration is central to, for example, the pricing of options and derivatives. Having derived the risk-neutral probability measure for a (set of) stochastic process(es), option pricing boils down to taking the expectation of the option's payoff under the risk-neutral measure and discounting this value back to the present date. Chapter 12 covers the simulation of several types of stochastic processes under the risk-neutral measure.

Finally, this chapter introduces symbolic computation with SymPy. For a number of mathematical operations, like integration, differentiation, or the solving of equations, symbolic computation can prove a useful and efficient tool.
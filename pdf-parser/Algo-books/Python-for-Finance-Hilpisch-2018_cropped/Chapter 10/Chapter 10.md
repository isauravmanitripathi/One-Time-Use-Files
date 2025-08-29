# **Chapter 10. Performance Python**

Don't lower your expectations to meet your performance. Raise your level of performance to meet your expectations. Ralph Marston

It is a long-lived prejudice that Python per se is a relatively slow programming language and not appropriate to implement computationally demanding tasks in finance. Beyond the fact that Python is an interpreted language, the reasoning is usually along the following lines: Python is slow when it comes to loops; loops are often required to implement financial algorithms; therefore Python is too slow for financial algorithm implementation. Another line of reasoning is: other (compiled) programming languages are fast at executing loops (such as C or C++); loops are often required for financial algorithms; therefore these (compiled) programming languages are well suited for finance and financial algorithm implementation.

Admittedly, it is possible to write proper Python code that executes rather slowly — perhaps too slowly for many application areas. This chapter is about approaches to speed up typical tasks and algorithms often encountered in a financial context. It shows that with a judicious use of data structures, choosing the right implementation idioms and paradigms, as well as using the right performance packages, Python is able to compete even with compiled programming languages. This is due to, among other factors, getting compiled itself.

To this end, this chapter introduces different approaches to speed up code:

### *Vectorization*

Making use of Python's vectorization capabilities is one approach already used extensively in previous chapters.

### *Dynamic compiling*

Using the Numba package allows one to dynamically compile pure Python code using LLVM [technology.](https://llvm.org/)

### *Static compiling*

Cython is not only a Python package but a hybrid language that combines Python and C; it allows one, for instance, to use static type declarations and to statically compile such adjusted code.

### *Multiprocessing*

The multiprocessing module of Python allows for easy and simple parallelization of code execution.

This chapter addresses the following topics:

### *"Loops"*

This section addresses Python loops and how to speed them up.

### *"Algorithms"*

This section is concerned with standard mathematical algorithms that are often used for performance benchmarks, such as Fibonacci number generation.

### *"Binomial Trees"*

The binomial option pricing model is a widely used financial model that allows for an interesting case study about a more involved financial algorithm.

### *"Monte Carlo Simulation"*

Similarly, Monte Carlo simulation is widely used in financial practice for pricing and risk management. It is computationally demanding and has long been considered the domain of such languages as C or C++.

### *"Recursive pandas Algorithm"*

This section addresses the speedup of a recursive algorithm based on financial time series data. In particular, it presents different implementations for an algorithm calculating an exponentially weighted moving average (EWMA).

# **Loops**

This section tackles the Python loop issue. The task is rather simple: a function shall be written that draws a certain "large" number of random numbers and returns the average of the values. The execution time is of interest, which can be estimated by the magic functions %time and %timeit.

### **Python**

Let's get started "slowly" — forgive the pun. In pure Python, such a function might look like average\_py():

```
In [1]: import random
In [2]: def average_py(n):
            s = 0
            for i in range(n):
                s += random.random()
            return s / n
In [3]: n = 10000000
In [4]: %time average_py(n)
        CPU times: user 1.82 s, sys: 10.4 ms, total: 1.83 s
        Wall time: 1.93 s
Out[4]: 0.5000590124747943
In [5]: %timeit average_py(n)
        1.31 s ± 159 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
In [6]: %time sum([random.random() for _ in range(n)]) / n
        CPU times: user 1.55 s, sys: 188 ms, total: 1.74 s
        Wall time: 1.74 s
Out[6]: 0.49987031710661173
```

Initializes the variable value for s.

Adds the uniformly distributed random values from the interval (0, 1) to s.

Returns the average value (mean).

Defines the number of iterations for the loop.

Times the function once.

Times the function multiple times for a more reliable estimate.

Uses a list comprehension instead of the function. This sets the benchmark for the other approaches to follow.

### **NumPy**

The strength of NumPy lies in its vectorization capabilities. Formally, loops vanish on the Python level; the looping takes place one level deeper based on optimized and compiled routines provided by NumPy. <sup>1</sup> The function average\_np() makes use of this approach:

```
In [7]: import numpy as np
In [8]: def average_np(n):
            s = np.random.random(n)
            return s.mean()
In [9]: %time average_np(n)
        CPU times: user 180 ms, sys: 43.2 ms, total: 223 ms
        Wall time: 224 ms
Out[9]: 0.49988861556468317
In [10]: %timeit average_np(n)
         128 ms ± 2.01 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
In [11]: s = np.random.random(n)
         s.nbytes
Out[11]: 80000000
```

Draws the random numbers "all at once" (no Python loop).

Returns the average value (mean).

Number of bytes used for the created ndarray object.

The speedup is considerable, reaching almost a factor of 10 or an order of magnitude. However, the price that must be paid is significantly higher memory usage. This is due to the fact that NumPy attains speed by preallocating data that can be processed in the compiled layer. As a consquence, there is no way, given this approach, to work with "streamed" data. This increased memory usage might even be prohibitively large depending on the algorithm or problem at hand.

### **VECTORIZATION AND MEMORY**

It is tempting to write vectorized code with NumPy whenever possible due to the concise syntax and speed improvements typically observed. However, these benefits often come at the price of a much higher memory footprint.

### **Numba**

[Numba](https://numba.pydata.org/) is a package that allows the *dynamic compiling* of pure Python code by the use of LLVM. The application in a simple case, like the one at hand, is surprisingly straightforward and the dynamically compiled function average\_nb() can be called directly from Python:

```
In [12]: import numba
In [13]: average_nb = numba.jit(average_py)
In [14]: %time average_nb(n)
         CPU times: user 204 ms, sys: 34.3 ms, total: 239 ms
         Wall time: 278 ms
Out[14]: 0.4998865391283664
In [15]: %time average_nb(n)
         CPU times: user 80.9 ms, sys: 457 µs, total: 81.3 ms
         Wall time: 81.7 ms
Out[15]: 0.5001357454250273
In [16]: %timeit average_nb(n)
         75.5 ms ± 1.95 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

This creates the Numba function.

The compiling happens during runtime, leading to some overhead.

From the second execution (with the same input data types), the execution is faster.

The combination of pure Python with Numba beats the NumPy version *and* preserves the memory efficiency of the original loop-based implementation. It is also obvious that the application of Numba in such simple cases comes with hardly any programming overhead.

### **NO FREE LUNCH**

The application of Numba sometimes seems like magic when one compares the performance of the Python code to the compiled version, especially given its ease of use. However, there are many use cases for which Numba is not suited and for which performance gains are hardly observed or even impossible to achieve.

### **Cython**

[Cython](http://cython.org) allows one to *statically compile* Python code. However, the application is not as simple as with Numba since the code generally needs to be changed to see significant speed improvements. To begin with, consider the Cython function average\_cy1(), which introduces static type declarations for the used variables:

```
In [17]: %load_ext Cython
In [18]: %%cython -a
         import random
         def average_cy1(int n):
             cdef int i
             cdef float s = 0
             for i in range(n):
                 s += random.random()
             return s / n
Out[18]: <IPython.core.display.HTML object>
In [19]: %time average_cy1(n)
         CPU times: user 695 ms, sys: 4.31 ms, total: 699 ms
         Wall time: 711 ms
Out[19]: 0.49997106194496155
In [20]: %timeit average_cy1(n)
         752 ms ± 91.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

Imports the random module within the Cython context.

Adds static type declarations for the variables n, i, and s.

Some speedup is observed, but not even close to that achieved by, for example, the NumPy version. A bit more Cython optimization is necessary to beat even the Numba version:

```
In [21]: %%cython
         from libc.stdlib cimport rand
         cdef extern from 'limits.h':
             int INT_MAX
         cdef int i
         cdef float rn
         for i in range(5):
             rn = rand() / INT_MAX
             print(rn)
         0.6792964339256287
         0.934692919254303
```

```
0.3835020661354065
         0.5194163918495178
         0.8309653401374817
In [22]: %%cython -a
         from libc.stdlib cimport rand
         cdef extern from 'limits.h':
             int INT_MAX
         def average_cy2(int n):
             cdef int i
             cdef float s = 0
             for i in range(n):
                 s += rand() / INT_MAX
             return s / n
Out[22]: <IPython.core.display.HTML object>
In [23]: %time average_cy2(n)
         CPU times: user 78.5 ms, sys: 422 µs, total: 79 ms
         Wall time: 79.1 ms
Out[23]: 0.500017523765564
In [24]: %timeit average_cy2(n)
         65.4 ms ± 706 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

Imports a random number generator from C.

Imports a constant value for the scaling of the random numbers.

Adds uniformly distributed random numbers from the interval (0, 1), after scaling.

This further optimized Cython version, average\_cy2(), is now a bit faster than the Numba version. However, the effort has also been a bit larger. Compared to the NumPy version, Cython also preserves the memory efficiency of the original loop-based implementation.

### **CYTHON = PYTHON + C**

Cython allows developers to tweak code for performance as much as possible or as little as sensible — starting with a pure Python version, for instance, and adding more and more elements from C to the code. The compilation step itself can also be parameterized to further optimize the compiled version.

# **Algorithms**

This section applies the performance-enhancing techniques from the previous section to some well-known problems and algorithms from mathematics. These algorithms are regularly used for performance benchmarks.

### **Prime Numbers**

Prime numbers play an important role not only in theoretical mathematics but also in many applied computer science disciplines, such as encryption. A *prime number* is a positive natural number greater than 1 that is only divisible without remainder by 1 and itself. There are no other factors. While it is difficult to find larger prime numbers due to their rarity, it is easy to prove that a number is not prime. The only thing that is needed is a factor other than 1 that divides the number without a remainder.

### **Python**

There are a number of algorithmic implementations available to test if numbers are prime. The following is a Python version that is not yet optimal from an algorithmic point of view but is already quite efficient. The execution time for the larger prime p2, however, is long:

```
In [25]: def is_prime(I):
             if I % 2 == 0: return False
             for i in range(3, int(I ** 0.5) + 1, 2):
                 if I % i == 0: return False
             return True
In [26]: n = int(1e8 + 3)
         n
Out[26]: 100000003
In [27]: %time is_prime(n)
         CPU times: user 35 µs, sys: 0 ns, total: 35 µs
         Wall time: 39.1 µs
Out[27]: False
In [28]: p1 = int(1e8 + 7)
         p1
Out[28]: 100000007
In [29]: %time is_prime(p1)
         CPU times: user 776 µs, sys: 1 µs, total: 777 µs
         Wall time: 787 µs
Out[29]: True
In [30]: p2 = 100109100129162907
In [31]: p2.bit_length()
Out[31]: 57
In [32]: %time is_prime(p2)
         CPU times: user 22.6 s, sys: 44.7 ms, total: 22.6 s
```

```
Wall time: 22.7 s
Out[32]: True
```

If the number is even, False is returned immediately.

The loop starts at 3 and goes until the square root of I plus 1 with step size 2.

As soon as a factor is identified the function returns False.

If no factor is found, True is returned.

Relatively small non-prime and prime numbers.

A larger prime number which requires longer execution times.

### **Numba**

The loop structure of the algorithm in the function is\_prime() lends itself well to being dynamically compiled with Numba. The overhead again is minimal but the speedup considerable:

```
In [33]: is_prime_nb = numba.jit(is_prime)
In [34]: %time is_prime_nb(n)
         CPU times: user 87.5 ms, sys: 7.91 ms, total: 95.4 ms
         Wall time: 93.7 ms
Out[34]: False
In [35]: %time is_prime_nb(n)
         CPU times: user 9 µs, sys: 1e+03 ns, total: 10 µs
         Wall time: 13.6 µs
Out[35]: False
In [36]: %time is_prime_nb(p1)
         CPU times: user 26 µs, sys: 0 ns, total: 26 µs
         Wall time: 31 µs
Out[36]: True
In [37]: %time is_prime_nb(p2)
         CPU times: user 1.72 s, sys: 9.7 ms, total: 1.73 s
```

```
Wall time: 1.74 s
Out[37]: True
```

The first call of is\_prime\_nb() involves the compiling overhead.

From the second call, the speedup becomes fully visible.

The speedup for the larger prime is about an order of magnitude.

### **Cython**

The application of Cython is straightforward as well. A plain Cython version without type declarations already speeds up the code significantly:

```
In [38]: %%cython
         def is_prime_cy1(I):
             if I % 2 == 0: return False
             for i in range(3, int(I ** 0.5) + 1, 2):
                 if I % i == 0: return False
             return True
In [39]: %timeit is_prime(p1)
         394 µs ± 14.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
In [40]: %timeit is_prime_cy1(p1)
         243 µs ± 6.58 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

However, real improvements only materialize with the static type declarations. The Cython version then even is slightly faster than the Numba one:

```
In [41]: %%cython
         def is_prime_cy2(long I):
             cdef long i
             if I % 2 == 0: return False
             for i in range(3, int(I ** 0.5) + 1, 2):
                 if I % i == 0: return False
             return True
In [42]: %timeit is_prime_cy2(p1)
         87.6 µs ± 27.7 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
In [43]: %time is_prime_nb(p2)
         CPU times: user 1.68 s, sys: 9.73 ms, total: 1.69 s
         Wall time: 1.7 s
Out[43]: True
In [44]: %time is_prime_cy2(p2)
```

```
CPU times: user 1.66 s, sys: 9.47 ms, total: 1.67 s
         Wall time: 1.68 s
Out[44]: True
```

Static type declarations for the two variables I and i.

### **Multiprocessing**

So far, all the optimization efforts have focused on the sequential code execution. In particular with prime numbers, there might be a need to check multiple numbers at the same time. To this end, the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) module can help speed up the code execution further. It allows one to spawn multiple Python processes that run in parallel. The application is straightforward in the simple case at hand. First, an mp.Pool object is set up with multiple processes. Second, the function to be executed is *mapped* to the prime numbers to be checked:

```
In [45]: import multiprocessing as mp
In [46]: pool = mp.Pool(processes=4)
In [47]: %time pool.map(is_prime, 10 * [p1])
         CPU times: user 1.52 ms, sys: 2.09 ms, total: 3.61 ms
         Wall time: 9.73 ms
Out[47]: [True, True, True, True, True, True, True, True, True, True]
In [48]: %time pool.map(is_prime_nb, 10 * [p2])
         CPU times: user 13.9 ms, sys: 4.8 ms, total: 18.7 ms
         Wall time: 10.4 s
Out[48]: [True, True, True, True, True, True, True, True, True, True]
In [49]: %time pool.map(is_prime_cy2, 10 * [p2])
         CPU times: user 9.8 ms, sys: 3.22 ms, total: 13 ms
         Wall time: 9.51 s
Out[49]: [True, True, True, True, True, True, True, True, True, True]
```

The mp.Pool object is instantiated with multiple processes.

Then the respective function is mapped to a list object with prime numbers.

The observed speedup is significant. The Python function is\_prime() takes more than 20 seconds for the larger prime number p2. Both the is\_prime\_nb() and the is\_prime\_cy2() functions take less than 10 seconds for 10 times the prime number p2 when executed in parallel with four processes.

### **PARALLEL PROCESSING**

Parallel processing should be considered whenever different problems of the same type need to be solved. The effect can be huge when powerful hardware is available with many cores and sufficient working memory. multiprocessing is one easy-to-use module from the standard library.

### **Fibonacci Numbers**

Fibonacci numbers and sequences can be derived based on a simple algorithm. Start with two ones: 1, 1. From the third number, the next Fibonacci number is derived as the sum of the two preceding ones: 1, 1, 2, 3, 5, 8, 13, 21, …. This section analyzes two different implementations, a recursive one and an iterative one.

### **Recursive algorithm**

Similar to regular Python loops, it is known that regular recursive function implementations are relatively slow with Python. Such functions call themselves potentially a large number of times to come up with the final result. The function fib\_rec\_py1() presents such an implementation. In this case, Numba does not help at all with speeding up the execution. However, Cython shows significant speedups based on static type declarations only:

```
In [50]: def fib_rec_py1(n):
             if n < 2:
                 return n
             else:
                 return fib_rec_py1(n - 1) + fib_rec_py1(n - 2)
In [51]: %time fib_rec_py1(35)
         CPU times: user 6.55 s, sys: 29 ms, total: 6.58 s
         Wall time: 6.6 s
Out[51]: 9227465
In [52]: fib_rec_nb = numba.jit(fib_rec_py1)
In [53]: %time fib_rec_nb(35)
         CPU times: user 3.87 s, sys: 24.2 ms, total: 3.9 s
         Wall time: 3.91 s
Out[53]: 9227465
In [54]: %%cython
         def fib_rec_cy(int n):
             if n < 2:
                 return n
             else:
                 return fib_rec_cy(n - 1) + fib_rec_cy(n - 2)
In [55]: %time fib_rec_cy(35)
         CPU times: user 751 ms, sys: 4.37 ms, total: 756 ms
         Wall time: 755 ms
Out[55]: 9227465
```

The major problem with the recursive algorithm is that intermediate results are

The major problem with the recursive algorithm is that intermediate results are not cached but rather recalculated. To avoid this particular problem, a decorator can be used that takes care of the caching of intermediate results. This speeds up the execution by multiple orders of magnitude:

```
In [56]: from functools import lru_cache as cache
In [57]: @cache(maxsize=None)
         def fib_rec_py2(n):
             if n < 2:
                 return n
             else:
                 return fib_rec_py2(n - 1) + fib_rec_py2(n - 2)
In [58]: %time fib_rec_py2(35)
         CPU times: user 64 µs, sys: 28 µs, total: 92 µs
         Wall time: 98 µs
Out[58]: 9227465
In [59]: %time fib_rec_py2(80)
         CPU times: user 38 µs, sys: 8 µs, total: 46 µs
         Wall time: 51 µs
Out[59]: 23416728348467685
```

Caching intermediate results …

… leads to tremendous speedups in this case.

### **Iterative algorithm**

Although the algorithm to calculate the *n*th Fibonacci number *can* be implemented recursively, it doesn't *have* to be. The following presents an iterative implementation which is even in pure Python faster than the cached variant of the recursive implementation. This is also the terrain where Numba leads to further improvements. However, the Cython version comes out as the winner:

```
In [60]: def fib_it_py(n):
             x, y = 0, 1
             for i in range(1, n + 1):
                 x, y = y, x + y
             return x
In [61]: %time fib_it_py(80)
         CPU times: user 19 µs, sys: 1e+03 ns, total: 20 µs
         Wall time: 26 µs
```

```
Out[61]: 23416728348467685
In [62]: fib_it_nb = numba.jit(fib_it_py)
In [63]: %time fib_it_nb(80)
         CPU times: user 57 ms, sys: 6.9 ms, total: 63.9 ms
         Wall time: 62 ms
Out[63]: 23416728348467685
In [64]: %time fib_it_nb(80)
         CPU times: user 7 µs, sys: 1 µs, total: 8 µs
         Wall time: 12.2 µs
Out[64]: 23416728348467685
In [65]: %%cython
         def fib_it_cy1(int n):
             cdef long i
             cdef long x = 0, y = 1
             for i in range(1, n + 1):
                 x, y = y, x + y
             return x
In [66]: %time fib_it_cy1(80)
         CPU times: user 4 µs, sys: 1e+03 ns, total: 5 µs
         Wall time: 11 µs
Out[66]: 23416728348467685
```

Now that everything is so fast, one might wonder why we're just calculating the 80th Fibonacci number and not the 150th, for instance. The problem is with the available data types. While Python can basically handle arbitrarily large numbers (see "Basic Data Types"), this is not true in general for the compiled languages. With Cython one can, however, rely on a special data type to allow for numbers larger than the double float object with 64 bits allows for:

```
In [67]: %%time
         fn = fib_rec_py2(150)
         print(fn)
         9969216677189303386214405760200
         CPU times: user 361 µs, sys: 115 µs, total: 476 µs
         Wall time: 430 µs
In [68]: fn.bit_length()
Out[68]: 103
In [69]: %%time
         fn = fib_it_nb(150)
         print(fn)
         6792540214324356296
         CPU times: user 270 µs, sys: 78 µs, total: 348 µs
         Wall time: 297 µs
In [70]: fn.bit_length()
```

```
Out[70]: 63
In [71]: %%time
         fn = fib_it_cy1(150)
         print(fn)
         6792540214324356296
         CPU times: user 255 µs, sys: 71 µs, total: 326 µs
         Wall time: 279 µs
In [72]: fn.bit_length()
Out[72]: 63
In [73]: %%cython
         cdef extern from *:
             ctypedef int int128 '__int128_t'
         def fib_it_cy2(int n):
             cdef int128 i
             cdef int128 x = 0, y = 1
             for i in range(1, n + 1):
                 x, y = y, x + y
             return x
In [74]: %%time
         fn = fib_it_cy2(150)
         print(fn)
         9969216677189303386214405760200
         CPU times: user 280 µs, sys: 115 µs, total: 395 µs
         Wall time: 328 µs
In [75]: fn.bit_length()
Out[75]: 103
```

The Python version is fast and correct.

The resulting integer has a bit length of 103 (> 64).

The Numba and Cython versions are faster but incorrect.

They suffer from an overflow issue due to the restriction to 64-bit int objects.

Imports the special 128-bit int object type and uses it.

The Cython version fib\_it\_cy2() now is faster *and* correct.

### **The Number Pi**

The final algorithm analyzed in this section is a Monte Carlo simulation–based algorithm to derive digits for the number pi (π). <sup>2</sup> The basic idea relies on the fact that the area *A* of a circle is given by . Therefore, . For a unit circle with radius *r* = 1, it holds that π = *A*. The idea of the algorithm is to simulate random points with coordinate values (*x*, *y*), with *x*, *y* ∈ [–1, 1]. The area of an origin-centered square with side length of 2 is exactly 4. The area of the origin-centered unit circle is a fraction of the area of such a square. This fraction can be estimated by Monte Carlo simulation: count all the points in the square, then count all the points in the circle, and divide the number of points in the circle by the number of points in the square. The following example demonstrates (see Figure 10-1):

```
In [76]: import random
         import numpy as np
         from pylab import mpl, plt
         plt.style.use('seaborn')
         mpl.rcParams['font.family'] = 'serif'
         %matplotlib inline
In [77]: rn = [(random.random() * 2 - 1, random.random() * 2 - 1)
               for _ in range(500)]
In [78]: rn = np.array(rn)
         rn[:5]
Out[78]: array([[ 0.45583018, -0.27676067],
                [-0.70120038, 0.15196888],
                [ 0.07224045, 0.90147321],
                [-0.17450337, -0.47660912],
                [ 0.94896746, -0.31511879]])
In [79]: fig = plt.figure(figsize=(7, 7))
         ax = fig.add_subplot(1, 1, 1)
         circ = plt.Circle((0, 0), radius=1, edgecolor='g', lw=2.0,
                           facecolor='None')
         box = plt.Rectangle((-1, -1), 2, 2, edgecolor='b', alpha=0.3)
         ax.add_patch(circ)
         ax.add_patch(box)
         plt.plot(rn[:, 0], rn[:, 1], 'r.')
         plt.ylim(-1.1, 1.1)
         plt.xlim(-1.1, 1.1)
```

Draws the unit circle.

Draws the square with side length of 2.

Draws the square with side length of 2.

Draws the uniformly distributed random dots.

![](_page_25_Figure_0.jpeg)

*Figure 10-1. Unit circle and square with side length 2 with uniformly distributed random points*

A NumPy implementation of this algorithm is rather concise but also memoryintensive. Total execution time given the parameterization is about one second:

```
In [80]: n = int(1e7)
In [81]: %time rn = np.random.random((n, 2)) * 2 - 1
         CPU times: user 450 ms, sys: 87.9 ms, total: 538 ms
         Wall time: 573 ms
In [82]: rn.nbytes
Out[82]: 160000000
In [83]: %time distance = np.sqrt((rn ** 2).sum(axis=1))
         distance[:8].round(3)
```

```
CPU times: user 537 ms, sys: 198 ms, total: 736 ms
         Wall time: 651 ms
Out[83]: array([1.181, 1.061, 0.669, 1.206, 0.799, 0.579, 0.694, 0.941])
In [84]: %time frac = (distance <= 1.0).sum() / len(distance)
         CPU times: user 47.9 ms, sys: 6.77 ms, total: 54.7 ms
         Wall time: 28 ms
In [85]: pi_mcs = frac * 4
         pi_mcs
Out[85]: 3.1413396
```

The distance of the points from the origin (Euclidean norm).

The fraction of those points on the circle relative to all points.

This accounts for the square area of 4 for the estimation of the circle area and therewith of π.

mcs\_pi\_py() is a Python function using a for loop and implementing the Monte Carlo simulation in a memory-efficient manner. Note that the random numbers are not scaled in this case. The execution time is longer than with the NumPy version, but the Numba version is faster than NumPy in this case:

```
In [86]: def mcs_pi_py(n):
             circle = 0
             for _ in range(n):
                 x, y = random.random(), random.random()
                 if (x ** 2 + y ** 2) ** 0.5 <= 1:
                     circle += 1
             return (4 * circle) / n
In [87]: %time mcs_pi_py(n)
         CPU times: user 5.47 s, sys: 23 ms, total: 5.49 s
         Wall time: 5.43 s
Out[87]: 3.1418964
In [88]: mcs_pi_nb = numba.jit(mcs_pi_py)
In [89]: %time mcs_pi_nb(n)
         CPU times: user 319 ms, sys: 6.36 ms, total: 326 ms
         Wall time: 326 ms
Out[89]: 3.1422012
In [90]: %time mcs_pi_nb(n)
         CPU times: user 284 ms, sys: 3.92 ms, total: 288 ms
         Wall time: 291 ms
```

Out[90]: 3.142066

A plain Cython version with static type declarations only does not perform that much faster than the Python version. However, relying again on the random number generation capabilities of C further speeds up the calculation considerably:

```
In [91]: %%cython -a
         import random
         def mcs_pi_cy1(int n):
             cdef int i, circle = 0
             cdef float x, y
             for i in range(n):
                 x, y = random.random(), random.random()
                 if (x ** 2 + y ** 2) ** 0.5 <= 1:
                     circle += 1
             return (4 * circle) / n
Out[91]: <IPython.core.display.HTML object>
In [92]: %time mcs_pi_cy1(n)
         CPU times: user 1.15 s, sys: 8.24 ms, total: 1.16 s
         Wall time: 1.16 s
Out[92]: 3.1417132
In [93]: %%cython -a
         from libc.stdlib cimport rand
         cdef extern from 'limits.h':
             int INT_MAX
         def mcs_pi_cy2(int n):
             cdef int i, circle = 0
             cdef float x, y
             for i in range(n):
                 x, y = rand() / INT_MAX, rand() / INT_MAX
                 if (x ** 2 + y ** 2) ** 0.5 <= 1:
                     circle += 1
             return (4 * circle) / n
Out[93]: <IPython.core.display.HTML object>
In [94]: %time mcs_pi_cy2(n)
         CPU times: user 170 ms, sys: 1.45 ms, total: 172 ms
         Wall time: 172 ms
Out[94]: 3.1419388
```

### **ALGORITHM TYPES**

The algorithms analyzed in this section might not be directly related to financial algorithms. However, the advantage is that they are simple and easy to understand. In addition, typical algorithmic problems encountered in a financial context can be discussed within this simplified context.

## **Binomial Trees**

A popular numerical method to value options is the binomial option pricing model pioneered by Cox, Ross, and Rubinstein (1979). This method relies on representing the possible future evolution of an asset by a (recombining) tree. In this model, as in the Black-Scholes-Merton (1973) setup, there is a *risky asset*, an index or stock, and a *riskless asset*, a bond. The relevant time interval from today until the maturity of the option is divided in general into equidistant subintervals of length . Given an index level at time *s* of , the index level at is given by , where *m* is chosen randomly from with 0 < *d* < < as well as . *r* is the constant, riskless short rate.

### **Python**

The code that follows presents a Python implementation that creates a recombining tree based on some fixed numerical parameters for the model:

```
In [95]: import math
In [96]: S0 = 36.
         T = 1.0
         r = 0.06
         sigma = 0.2
In [97]: def simulate_tree(M):
             dt = T / M
             u = math.exp(sigma * math.sqrt(dt))
             d = 1 / u
             S = np.zeros((M + 1, M + 1))
             S[0, 0] = S0
             z = 1
             for t in range(1, M + 1):
                 for i in range(z):
                     S[i, t] = S[i, t-1] * u
                     S[i+1, t] = S[i, t-1] * d
                 z += 1
             return S
```

Initial value of the risky asset.

Time horizon for the binomial tree simulation.

Constant short rate.

Constant volatility factor.

Length of the time intervals.

Factors for the upward and downward movements.

Contrary to what happens in typical tree plots, an upward movement is represented in the ndarray object as a sideways movement, which decreases the ndarray size considerably:

```
In [98]: np.set_printoptions(formatter={'float':
                                    lambda x: '%6.2f' % x})
In [99]: simulate_tree(4)
Out[99]: array([[ 36.00, 39.79, 43.97, 48.59, 53.71],
              [ 0.00, 32.57, 36.00, 39.79, 43.97],
              [ 0.00, 0.00, 29.47, 32.57, 36.00],
              [ 0.00, 0.00, 0.00, 26.67, 29.47],
              [ 0.00, 0.00, 0.00, 0.00, 24.13]])
In [100]: %time simulate_tree(500)
         CPU times: user 148 ms, sys: 4.49 ms, total: 152 ms
         Wall time: 154 ms
Out[100]: array([[ 36.00, 36.32, 36.65, ..., 3095.69, 3123.50, 3151.57],
               [ 0.00, 35.68, 36.00, ..., 3040.81, 3068.13, 3095.69],
               [ 0.00, 0.00, 35.36, ..., 2986.89, 3013.73, 3040.81],
               ...,
               [ 0.00, 0.00, 0.00, ..., 0.42, 0.42, 0.43],
               [ 0.00, 0.00, 0.00, ..., 0.00, 0.41, 0.42],
               [ 0.00, 0.00, 0.00, ..., 0.00, 0.00, 0.41]])
```

Tree with 4 time intervals.

Tree with 500 time intervals.

### **NumPy**

With some trickery, such a binomial tree can be created with NumPy based on fully vectorized code:

```
In [101]: M = 4
In [102]: up = np.arange(M + 1)
         up = np.resize(up, (M + 1, M + 1))
         up
Out[102]: array([[0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4]])
In [103]: down = up.T * 2
         down
Out[103]: array([[0, 0, 0, 0, 0],
                [2, 2, 2, 2, 2],
                [4, 4, 4, 4, 4],
                [6, 6, 6, 6, 6],
                [8, 8, 8, 8, 8]])
In [104]: up - down
Out[104]: array([[ 0, 1, 2, 3, 4],
                [-2, -1, 0, 1, 2],
                [-4, -3, -2, -1, 0],
                [-6, -5, -4, -3, -2],
                [-8, -7, -6, -5, -4]])
In [105]: dt = T / M
In [106]: S0 * np.exp(sigma * math.sqrt(dt) * (up - down))
Out[106]: array([[ 36.00, 39.79, 43.97, 48.59, 53.71],
                [ 29.47, 32.57, 36.00, 39.79, 43.97],
                [ 24.13, 26.67, 29.47, 32.57, 36.00],
                [ 19.76, 21.84, 24.13, 26.67, 29.47],
                [ 16.18, 17.88, 19.76, 21.84, 24.13]])
```

ndarray object with gross *upward* movements.

ndarray object with gross *downward* movements.

ndarray object with *net* upward (positive) and downward (negative) movements.

Tree for four time intervals (upper-right triangle of values).

In the NumPy case, the code is a bit more compact. However, more importantly, NumPy vectorization achieves a speedup of an order of magnitude while not using more memory:

```
In [107]: def simulate_tree_np(M):
             dt = T / M
             up = np.arange(M + 1)
             up = np.resize(up, (M + 1, M + 1))
             down = up.transpose() * 2
             S = S0 * np.exp(sigma * math.sqrt(dt) * (up - down))
             return S
In [108]: simulate_tree_np(4)
Out[108]: array([[ 36.00, 39.79, 43.97, 48.59, 53.71],
                [ 29.47, 32.57, 36.00, 39.79, 43.97],
                [ 24.13, 26.67, 29.47, 32.57, 36.00],
                [ 19.76, 21.84, 24.13, 26.67, 29.47],
                [ 16.18, 17.88, 19.76, 21.84, 24.13]])
In [109]: %time simulate_tree_np(500)
         CPU times: user 8.72 ms, sys: 7.07 ms, total: 15.8 ms
         Wall time: 12.9 ms
Out[109]: array([[ 36.00, 36.32, 36.65, ..., 3095.69, 3123.50, 3151.57],
                [ 35.36, 35.68, 36.00, ..., 3040.81, 3068.13, 3095.69],
                [ 34.73, 35.05, 35.36, ..., 2986.89, 3013.73, 3040.81],
                ...,
                [ 0.00, 0.00, 0.00, ..., 0.42, 0.42, 0.43],
                [ 0.00, 0.00, 0.00, ..., 0.41, 0.41, 0.42],
                [ 0.00, 0.00, 0.00, ..., 0.40, 0.41, 0.41]])
```

### **Numba**

This financial algorithm should be well suited to optimization through Numba dynamic compilation. And indeed, another speedup compared to the NumPy version of an order of magnitude is observed. This makes the Numba version orders of magnitude faster than the Python (or rather hybrid) version: In [110]: simulate\_tree\_nb = numba.jit(simulate\_tree) In [111]: simulate\_tree\_nb(4) Out[111]: array([[ 36.00, 39.79, 43.97, 48.59, 53.71], [ 0.00, 32.57, 36.00, 39.79, 43.97], [ 0.00, 0.00, 29.47, 32.57, 36.00], [ 0.00, 0.00, 0.00, 26.67, 29.47], [ 0.00, 0.00, 0.00, 0.00, 24.13]]) In [112]: %time simulate\_tree\_nb(500) CPU times: user 425 µs, sys: 193 µs, total: 618 µs Wall time: 625 µs Out[112]: array([[ 36.00, 36.32, 36.65, ..., 3095.69, 3123.50, 3151.57], [ 0.00, 35.68, 36.00, ..., 3040.81, 3068.13, 3095.69], [ 0.00, 0.00, 35.36, ..., 2986.89, 3013.73, 3040.81], ..., [ 0.00, 0.00, 0.00, ..., 0.42, 0.42, 0.43], [ 0.00, 0.00, 0.00, ..., 0.00, 0.41, 0.42], [ 0.00, 0.00, 0.00, ..., 0.00, 0.00, 0.41]]) In [113]: %timeit simulate\_tree\_nb(500) 559 µs ± 46.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

### **Cython**

As before, Cython requires more adjustments to the code to see significant improvements. The following version uses mainly static type declarations and certain imports that improve the performance compared to the regular Python imports and functions, respectively:

```
In [114]: %%cython -a
          import numpy as np
          cimport cython
          from libc.math cimport exp, sqrt
          cdef float S0 = 36.
          cdef float T = 1.0
          cdef float r = 0.06
          cdef float sigma = 0.2
          def simulate_tree_cy(int M):
              cdef int z, t, i
              cdef float dt, u, d
              cdef float[:, :] S = np.zeros((M + 1, M + 1),
                                             dtype=np.float32)
              dt = T / M
              u = exp(sigma * sqrt(dt))
              d = 1 / u
              S[0, 0] = S0
              z = 1
              for t in range(1, M + 1):
                  for i in range(z):
                      S[i, t] = S[i, t-1] * u
                      S[i+1, t] = S[i, t-1] * d
                  z += 1
              return np.array(S)
Out[114]: <IPython.core.display.HTML object>
```

Declaring the ndarray object to be a C array is critical for performance.

The Cython version shaves off another 30% of the execution time compared to the Numba version:

```
In [115]: simulate_tree_cy(4)
Out[115]: array([[ 36.00, 39.79, 43.97, 48.59, 53.71],
                [ 0.00, 32.57, 36.00, 39.79, 43.97],
                [ 0.00, 0.00, 29.47, 32.57, 36.00],
                [ 0.00, 0.00, 0.00, 26.67, 29.47],
                [ 0.00, 0.00, 0.00, 0.00, 24.13]], dtype=float32)
In [116]: %time simulate_tree_cy(500)
         CPU times: user 2.21 ms, sys: 1.89 ms, total: 4.1 ms
         Wall time: 2.45 ms
Out[116]: array([[ 36.00, 36.32, 36.65, ..., 3095.77, 3123.59, 3151.65],
                [ 0.00, 35.68, 36.00, ..., 3040.89, 3068.21, 3095.77],
```

| [                | 0.00,                                     | 0.00,                   |                               |                         |                         | 35.36, , 2986.97, 3013.81, 3040.89], |
|------------------|-------------------------------------------|-------------------------|-------------------------------|-------------------------|-------------------------|--------------------------------------|
| ,<br>[<br>[<br>[ | 0.00,<br>0.00,<br>0.00,<br>dtype=float32) | 0.00,<br>0.00,<br>0.00, | 0.00, ,<br>0.00, ,<br>0.00, , | 0.42,<br>0.00,<br>0.00, | 0.42,<br>0.41,<br>0.00, | 0.43],<br>0.42],<br>0.41]],          |

In [117]: %timeit S = simulate\_tree\_cy(500)

363 µs ± 29.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

# **Monte Carlo Simulation**

Monte Carlo simulation is an indispensible numerical tool in computational finance. It has been in use since long before the advent of modern computers. Banks and other financial institutions use it, among others, for pricing and risk management purposes. As a numerical method it is perhaps the most flexible and powerful one in finance. However, it often also is the most computationally demanding one. That is why Python was long dismissed as a proper programming language to implement algorithms based on Monte Carlo simulation — at least for real-world application scenarios.

This section analyzes the Monte Carlo simulation of the geometric Brownian motion, a simple yet still widely used stochastic process to model the evolution of stock prices or index levels. Among others, the Black-Scholes-Merton (1973) theory of option pricing draws on this process. In their setup the underlying of the option to be valued follows the stochastic differential equation (SDE), as seen in [Equation](#page-37-0) 10-1. is the value of the underlying at time *t*; *r* is the constant, riskless short rate; σ is the constant instantaneous volatility; and is a Brownian motion.

<span id="page-37-0"></span>*Equation 10-1. Black-Scholes-Merton SDE (geometric Brownian motion)*

$$dS_t = rS_t dt + \sigma S_t dZ_t$$

This SDE can be discretized over equidistant time intervals and simulated according to [Equation](#page-37-1) 10-2, which represents an Euler scheme. In this case, *z* is a standard normally distributed random number. For *M* time intervals, the length of the time interval is given as where *T* is the time horizon for the simulation (for example, the maturity date of an option to be valued).

<span id="page-37-1"></span>*Equation 10-2. Black-Scholes-Merton difference equation (Euler scheme)*

$$S_t = S_{t-\Delta t} \exp\left(\left(r - \frac{\sigma^2}{2}\right)\Delta t + \sigma\sqrt{\Delta t}z\right)$$

The Monte Carlo estimator for a European call option is then given by Equation 10-3, where is the *i*th simulated value of the [underlying](#page-38-0) at maturity *T* for a total number of simulated paths *I* with *i* = 1, 2, …, *I*].

<span id="page-38-0"></span>*Equation 10-3. Monte Carlo estimator for European call option*

$$C_0 = e^{-rT} \frac{1}{I} \sum_{I} \max(S_T(i) - K, 0)$$

### **Python**

First, a Python — or rather a hybrid — version, mcs\_simulation\_py(), that implements the Monte Carlo simulation according to Equation 10-2. It is hybrid since it implements Python loops on ndarray objects. As seen previously, this might make for a good basis to dynamically compile the code with Numba. As before, the execution time sets the benchmark. Based on the simulation, a European put option is valued:

```
In [118]: M = 100
          I = 50000
In [119]: def mcs_simulation_py(p):
              M, I = p
              dt = T / M
              S = np.zeros((M + 1, I))
              S[0] = S0
              rn = np.random.standard_normal(S.shape)
              for t in range(1, M + 1):
                  for i in range(I):
                      S[t, i] = S[t-1, i] * math.exp((r - sigma ** 2 / 2) * dt +
                                            sigma * math.sqrt(dt) * rn[t, i])
              return S
In [120]: %time S = mcs_simulation_py((M, I))
          CPU times: user 5.55 s, sys: 52.9 ms, total: 5.6 s
          Wall time: 5.62 s
In [121]: S[-1].mean()
Out[121]: 38.22291254503985
In [122]: S0 * math.exp(r * T)
Out[122]: 38.22611567563295
In [123]: K = 40.
In [124]: C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
In [125]: C0 #
Out[125]: 3.860545188088036
```

The number of time intervals for discretization.

The number of paths to be simulated.

The random numbers, drawn in a single vectorized step.

The nested loop implementing the simulation based on the Euler scheme.

The mean end-of-period value based on the simulation.

The theoretically expected end-of-period value.

The strike price of the European put option.

The Monte Carlo estimator for the option.

[Figure](#page-40-0) 10-2 shows a histogram of the simulated values at the end of the simulation period (maturity of the European put option).

<span id="page-40-0"></span>![](_page_40_Figure_11.jpeg)

### **NumPy**

```
The NumPy version, mcs_simulation_np(), is not too different. It still has one
Python loop, namely over the time intervals. The other dimension is handled by
vectorized code over all paths. It is about 20 times faster than the first version:
In [127]: def mcs_simulation_np(p): M, I = p dt = T / M S =
np.zeros((M + 1, I)) S[0] = S0 rn =
np.random.standard_normal(S.shape) for t in range(1, M + 1): S[t]
= S[t-1] * np.exp((r - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt)
* rn[t]) return S In [128]: %time S = mcs_simulation_np((M, I))
CPU times: user 252 ms, sys: 32.9 ms, total: 285 ms Wall time: 252
ms In [129]: S[-1].mean() Out[129]: 38.235136032258595 In [130]:
%timeit S = mcs_simulation_np((M, I)) 202 ms ± 27.7 ms per loop
(mean ± std. dev. of 7 runs, 1 loop each)
```

The loop over the time intervals.

The Euler scheme with vectorized NumPy code handling all paths at once.

### **Numba**

It should not come as a surprise anymore that Numba is applied to such an algorithm type easily, and with significant performance improvements. The Numba version, mcs\_simulation\_nb(), is slightly faster than the NumPy version: In [131]: mcs\_simulation\_nb = numba.jit(mcs\_simulation\_py) In [132]: %time S = mcs\_simulation\_nb((M, I)) CPU times: user 673 ms, sys: 36.7 ms, total: 709 ms Wall time: 764 ms In [133]: %time S = mcs\_simulation\_nb((M, I)) CPU times: user 239 ms, sys: 20.8 ms, total: 259 ms Wall time: 265 ms In [134]: S[-1].mean() Out[134]: 38.22350694016539 In [135]: C0 = math.exp(-r \* T) \* np.maximum(K - S[-1], 0).mean() In [136]: C0 Out[136]: 3.8303077438193833 In [137]: %timeit S = mcs\_simulation\_nb((M, I)) 248 ms ± 20.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

First call with compile-time overhead.

Second call without that overhead.

### **Cython**

With Cython, again not surprisingly, the effort required to speed up the code is higher. However, the speedup itself is not greater. The Cython version, mcs\_simulation\_cy(), seems to be even a bit slower compared to the NumPy and Numba versions. Among other factors, some time is needed to transform the simulation results to an ndarray object:

```
In [138]: %%cython
          import numpy as np
          cimport numpy as np
          cimport cython
          from libc.math cimport exp, sqrt
          cdef float S0 = 36.
          cdef float T = 1.0
          cdef float r = 0.06
          cdef float sigma = 0.2
          @cython.boundscheck(False)
          @cython.wraparound(False)
          def mcs_simulation_cy(p):
              cdef int M, I
              M, I = p
              cdef int t, i
              cdef float dt = T / M
              cdef double[:, :] S = np.zeros((M + 1, I))
              cdef double[:, :] rn = np.random.standard_normal((M + 1, I))
              S[0] = S0
              for t in range(1, M + 1):
                  for i in range(I):
                      S[t, i] = S[t-1, i] * exp((r - sigma ** 2 / 2) * dt +
                                                    sigma * sqrt(dt) * rn[t, i])
              return np.array(S)
In [139]: %time S = mcs_simulation_cy((M, I))
          CPU times: user 237 ms, sys: 65.2 ms, total: 302 ms
          Wall time: 271 ms
In [140]: S[-1].mean()
Out[140]: 38.241735841791574
In [141]: %timeit S = mcs_simulation_cy((M, I))
          221 ms ± 9.26 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

### **Multiprocessing**

Monte Carlo simulation is a task that lends itself well to parallelization. One approach would be to parallelize the simulation of 100,000 paths, say, into 10 processes simulating 10,000 paths each. Another would be to parallelize the simulation of the 100,000 paths into multiple processes, each simulating a different financial instrument, for example. The former case — namely, the parallel simulation of a larger number of paths based on a fixed number of separate processes — is illustrated in what follows.

The following code again makes use of the multiprocessing module. It divides the total number of paths to be simulated *I* into smaller chunks of size with *p* > 0. After all the single tasks are finished, the results are put together in a single ndarray object via np.hstack(). This approach can be applied to any of the versions presented previously. For the particular parameterization chosen here, there is no speedup to be observed through this parallelization approach: In [142]: **import multiprocessing as mp** In [143]: pool = mp.Pool(processes=4) In [144]: p = 20 In [145]: %timeit S = np.hstack(pool.map(mcs\_simulation\_np, p \* [(M, int(I / p))])) 288 ms ± 10.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) In [146]: %timeit S = np.hstack(pool.map(mcs\_simulation\_nb, p \* [(M, int(I / p))])) 258 ms ± 8.69 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) In [147]: %timeit S = np.hstack(pool.map(mcs\_simulation\_cy, p \* [(M, int(I / p))])) 274 ms ± 11.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

The Pool object for parallelization.

The number of chunks into which the simulation is divided.

### **MULTIPROCESSING STRATEGIES**

In finance, there are many algorithms that are useful for parallelization. Some of these even allow the application of different strategies to parallelize the code. Monte Carlo simulation is a good example in that multiple simulations can easily be executed in parallel, either on a single machine or on multiple machines, and that the algorithm itself allows a single simulation to be distributed over multiple processes.

# **Recursive pandas Algorithm**

This section addresses a somewhat special topic which is, however, an important one in financial analytics: the implementation of recursive functions on financial time series data stored in a pandas DataFrame object. While pandas allows for sophisticated vectorized operations on DataFrame objects, certain recursive algorithms are hard or impossible to vectorize, leaving the financial analyst with slowly executed Python loops on DataFrame objects. The examples that follow implement what is called the *exponentially weighted moving average* (EWMA) in a simple form.

The EWMA for a financial time series , is given by [Equation](#page-46-0) 10-4.

<span id="page-46-0"></span>*Equation 10-4. Exponentially weighted moving average (EWMA)*

Although simple in nature and straightforward to implement, such an algorithm might lead to rather slow code.

### **Python**

Consider first the Python version that iterates over the DatetimeIndex of a DataFrame object containing financial time series data for a single financial instrument (see Chapter 8). Figure 10-3 visualizes the financial time series and the EWMA time series:

```
In [148]: import pandas as pd
In [149]: sym = 'SPY'
In [150]: data = pd.DataFrame(pd.read_csv('../../source/tr_eikon_eod_data.csv',
                                    index_col=0, parse_dates=True)[sym]).dropna()
In [151]: alpha = 0.25
In [152]: data['EWMA'] = data[sym]
In [153]: %%time
         for t in zip(data.index, data.index[1:]):
             data.loc[t[1], 'EWMA'] = (alpha * data.loc[t[1], sym] +
                                      (1 - alpha) * data.loc[t[0], 'EWMA'])
         CPU times: user 588 ms, sys: 16.4 ms, total: 605 ms
         Wall time: 591 ms
In [154]: data.head()
Out[154]: SPY EWMA
         Date
         2010-01-04 113.33 113.330000
         2010-01-05 113.63 113.405000
         2010-01-06 113.71 113.481250
         2010-01-07 114.19 113.658438
         2010-01-08 114.57 113.886328
In [155]: data[data.index > '2017-1-1'].plot(figsize=(10, 6));
```

Initializes the EWMA column.

Implements the algorithm based on a Python loop.

![](_page_48_Figure_0.jpeg)

*Figure 10-3. Financial time series with EWMA*

Now consider more general Python function ewma\_py(). It can be applied directly on the column or the raw financial times series data in the form of an ndarray object:

```
In [156]: def ewma_py(x, alpha):
              y = np.zeros_like(x)
              y[0] = x[0]
              for i in range(1, len(x)):
                  y[i] = alpha * x[i] + (1-alpha) * y[i-1]
              return y
In [157]: %time data['EWMA_PY'] = ewma_py(data[sym], alpha)
          CPU times: user 33.1 ms, sys: 1.22 ms, total: 34.3 ms
          Wall time: 33.9 ms
In [158]: %time data['EWMA_PY'] = ewma_py(data[sym].values, alpha)
          CPU times: user 1.61 ms, sys: 44 µs, total: 1.65 ms
          Wall time: 1.62 ms
```

Applies the function to the Series object directly (i.e., the column).

Applies the function to the ndarray object containing the raw data.

This approach already speeds up the code execution considerably — by a factor of from about 20 to more than 100.

### **Numba**

The very structure of this algorithm promises further speedups when applying Numba. And indeed, when the function ewma\_nb() is applied to the ndarray version of the data, the speedup is again by an order of magnitude: In [159]: ewma\_nb = numba.jit(ewma\_py) In [160]: %time data['EWMA\_NB'] = ewma\_nb(data[sym], alpha) CPU times: user 269 ms, sys: 11.4 ms, total: 280 ms Wall time: 294 ms In [161]: %timeit data['EWMA\_NB'] = ewma\_nb(data[sym], alpha) 30.9 ms ± 1.21 ms per loop (mean ± std. dev. of 7 runs, 10 loops each) In [162]: %time data['EWMA\_NB'] = ewma\_nb(data[sym].values, alpha) CPU times: user 94.1 ms, sys: 3.78 ms, total: 97.9 ms Wall time: 97.6 ms In [163]: %timeit data['EWMA\_NB'] = ewma\_nb(data[sym].values, alpha) 134 µs ± 12.5 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

Applies the function to the Series object directly (i.e., the column).

Applies the function to the ndarray object containing the raw data.

### **Cython**

The Cython version, ewma\_cy(), also achieves considerable speed improvements but it is not as fast as the Numba version in this case:

```
In [164]: %%cython
          import numpy as np
          cimport cython
          @cython.boundscheck(False)
          @cython.wraparound(False)
          def ewma_cy(double[:] x, float alpha):
              cdef int i
              cdef double[:] y = np.empty_like(x)
              y[0] = x[0]
              for i in range(1, len(x)):
                  y[i] = alpha * x[i] + (1 - alpha) * y[i - 1]
              return y
In [165]: %time data['EWMA_CY'] = ewma_cy(data[sym].values, alpha)
          CPU times: user 2.98 ms, sys: 1.41 ms, total: 4.4 ms
          Wall time: 5.96 ms
In [166]: %timeit data['EWMA_CY'] = ewma_cy(data[sym].values, alpha)
          1.29 ms ± 194 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

This final example illustrates again that there are in general multiple options to implement (nonstandard) algorithms. All options might lead to exactly the same results, while also showing considerably different performance characteristics. The execution times in this example range from 0.1 ms to 500 ms — a factor of 5,000 times.

### **BEST VERSUS FIRST-BEST**

It is easy in general to translate algorithms to the Python programming language. However, it is equally easy to implement algorithms in a way that is unnecessarily slow given the menu of performance options available. For interactive financial analytics, a *first-best* solution — i.e., one that does the trick but which might not be the fastest possible nor the most memoryefficient one — might be perfectly fine. For financial applications in production, one should strive to implement the *best* solution, even though this might involve a bit more research and some formal benchmarking.

# **Conclusion**

The Python ecosystem provides a number of ways to improve the performance of code: Idioms and paradigms

Some Python paradigms and idioms might be more performant than others, given a specific problem; in many cases, for instance, vectorization is a paradigm that not only leads to more concise code but also to higher speeds (sometimes at the cost of a larger memory footprint).

### *Packages*

There are a wealth of packages available for different types of problems, and using a package adapted to the problem can often lead to much higher performance; good examples are NumPy with the ndarray class and pandas with the DataFrame class.

### *Compiling*

Powerful packages for speeding up financial algorithms are Numba and Cython for the dynamic and static compilation of Python code.

### *Parallelization*

Some Python packages, such as multiprocessing, allow for the easy parallelization of Python code; the examples in this chapter only use parallelization on a single machine but the Python ecosystem also offers technologies for multi-machine (cluster) parallelization.

A major benefit of the performance approaches presented in this chapter is that they are in general easily implementable, meaning that the additional effort required is regularly low. In other words, performance improvements often are low-hanging fruit given the performance packages available as of today.
# **Chapter 4. Numerical Computing with NumPy**

Computers are useless. They can only give answers. Pablo Picasso

Although the Python interpreter itself already brings a rich variety of data structures with it, NumPy and other libraries add to these in a valuable fashion. This chapter focuses on NumPy, which provides a multidimensional array object to store homogeneous or heterogeneous data arrays and supports vectorization of code.

The chapter covers the following data structures:

| Object<br>type    | Meaning                          | Used<br>for                                   |
|-------------------|----------------------------------|-----------------------------------------------|
| ndarray (regular) | n-dimensional<br>array<br>object | Large<br>arrays<br>of<br>numerical<br>data    |
| ndarray (record)  | 2-dimensional<br>array<br>object | Tabular<br>data<br>organized<br>in<br>columns |

This chapter is organized as follows: "Arrays of Data"

This section is about the handling of arrays of data with pure Python code.

*"Regular NumPy Arrays"*

This is the core section about the regular NumPy ndarray class, the workhorse in almost all data-intensive Python use cases involving numerical data.

*"Structured NumPy Arrays"*

This brief section introduces structured (or *record*) ndarray objects for the handling of tabular data with columns.

*"Vectorization of Code"*

In this section, vectorization of code is discussed along with its benefits; the section also discusses the importance of memory layout in certain scenarios.

# **Arrays of Data**

The previous chapter showed that Python provides some quite useful and flexible general data structures. In particular, list objects can be considered a real workhorse with many convenient characteristics and application areas. Using such a flexible (mutable) data structure has a cost, in the form of relatively high memory usage, slower performance, or both. However, scientific and financial applications generally have a need for high-performing operations on special data structures. One of the most important data structures in this regard is the *array*. Arrays generally structure other (fundamental) objects of the *same data type* in rows and columns.

Assume for the moment that only numbers are relevant, although the concept generalizes to other types of data as well. In the simplest case, a one-dimensional array then represents, mathematically speaking, a *vector* of, in general, real numbers, internally represented by float objects. It then consists of a *single* row or column of elements only. In the more common case, an array represents an *matrix* of elements. This concept generalizes to *cubes* of elements in three dimensions as well as to general *n*-dimensional arrays of shape .

Mathematical disciplines like linear algebra and vector space theory illustrate that such mathematical structures are of high importance in a number of scientific disciplines and fields. It can therefore prove fruitful to have available a specialized class of data structures explicitly designed to handle arrays conveniently and efficiently. This is where the Python library NumPy comes into play, with its powerful ndarray class. Before introducing this class in the next section, this section illustrates two alternatives for the handling of arrays.

### **Arrays with Python Lists**

Arrays can be constructed with the built-in data structures presented in the previous chapter. list objects are particularly suited to accomplishing this task. A simple list can already be considered a one-dimensional array:

In [1]: v = [0.5, 0.75, 1.0, 1.5, 2.0]

list object with numbers.

Since list objects can contain arbitrary other objects, they can also contain other list objects. In that way, two-and higher-dimensional arrays are easily constructed by nested list objects:

```
In [2]: m = [v, v, v]
        m
Out[2]: [[0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0]]
```

list object with list objects …

… resulting in a matrix of numbers.

One can also easily select rows via simple indexing or single elements via double indexing (whole columns, however, are not so easy to select):

```
In [3]: m[1]
Out[3]: [0.5, 0.75, 1.0, 1.5, 2.0]
In [4]: m[1][0]
Out[4]: 0.5
```

Nesting can be pushed further for even more general structures:

```
In [5]: v1 = [0.5, 1.5]
        v2 = [1, 2]
        m = [v1, v2]
        c = [m, m]
        c
```

```
Out[5]: [[[0.5, 1.5], [1, 2]], [[0.5, 1.5], [1, 2]]]
In [6]: c[1][1][0]
Out[6]: 1
```

Cube of numbers.

Note that combining objects in the way just presented generally works with reference pointers to the original objects. What does that mean in practice? Have a look at the following operations:

```
In [7]: v = [0.5, 0.75, 1.0, 1.5, 2.0]
        m = [v, v, v]
        m
Out[7]: [[0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0]]
```

Now change the value of the first element of the v object and see what happens to the m object:

```
In [8]: v[0] = 'Python'
        m
Out[8]: [['Python', 0.75, 1.0, 1.5, 2.0],
         ['Python', 0.75, 1.0, 1.5, 2.0],
         ['Python', 0.75, 1.0, 1.5, 2.0]]
```

This can be avoided by using the deepcopy() function of the copy module:

```
In [9]: from copy import deepcopy
        v = [0.5, 0.75, 1.0, 1.5, 2.0]
        m = 3 * [deepcopy(v), ]
        m
Out[9]: [[0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0],
         [0.5, 0.75, 1.0, 1.5, 2.0]]
In [10]: v[0] = 'Python'
         m
Out[10]: [[0.5, 0.75, 1.0, 1.5, 2.0],
          [0.5, 0.75, 1.0, 1.5, 2.0],
          [0.5, 0.75, 1.0, 1.5, 2.0]]
```

Instead of reference pointer, physical copies are used.

As a consequence, a change in the original object …

As a consequence, a change in the original object …

… does not have any impact anymore.

### **The Python array Class**

There is a dedicated array module available in Python. According to the [documentation:](https://docs.python.org/3/library/array.html)

This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character.

Consider the following code, which instantiates an array object out of a list object:

```
In [11]: v = [0.5, 0.75, 1.0, 1.5, 2.0]
In [12]: import array
In [13]: a = array.array('f', v)
         a
Out[13]: array('f', [0.5, 0.75, 1.0, 1.5, 2.0])
In [14]: a.append(0.5)
         a
Out[14]: array('f', [0.5, 0.75, 1.0, 1.5, 2.0, 0.5])
In [15]: a.extend([5.0, 6.75])
         a
Out[15]: array('f', [0.5, 0.75, 1.0, 1.5, 2.0, 0.5, 5.0, 6.75])
In [16]: 2 * a
Out[16]: array('f', [0.5, 0.75, 1.0, 1.5, 2.0, 0.5, 5.0, 6.75, 0.5, 0.75, 1.0,
          1.5, 2.0, 0.5, 5.0, 6.75])
```

The instantiation of the array object with float as the type code.

Major methods work similar to those of the list object.

Although "scalar multiplication" works in principle, the result is not the mathematically expected one; rather, the elements are repeated.

Trying to append an object of a different data type than the one specified raises a TypeError:

```
In [17]: a.append('string')
         ---------------------------------------
         TypeErrorTraceback (most recent call last)
         <ipython-input-17-14cd6281866b> in <module>()
         ----> 1 a.append('string')
         TypeError: must be real number, not str
In [18]: a.tolist()
Out[18]: [0.5, 0.75, 1.0, 1.5, 2.0, 0.5, 5.0, 6.75]
```

Only float objects can be appended; other data types/type codes raise errors.

However, the array object can easily be converted back to a list object if such flexibility is required.

An advantage of the array class is that it has built-in storage and retrieval functionality:

```
In [19]: f = open('array.apy', 'wb')
         a.tofile(f)
         f.close()
In [20]: with open('array.apy', 'wb') as f:
             a.tofile(f)
In [21]: !ls -n arr*
         -rw-r--r--@ 1 503 20 32 Nov 7 11:46 array.apy
```

Opens a file on disk for writing binary data.

Writes the array data to the file.

Closes the file.

Alternative: uses a with context for the same operation.

Shows the file as written on disk.

As before, the data type of the array object is of importance when reading the data from disk:

```
In [22]: b = array.array('f')
In [23]: with open('array.apy', 'rb') as f:
             b.fromfile(f, 5)
In [24]: b
Out[24]: array('f', [0.5, 0.75, 1.0, 1.5, 2.0])
In [25]: b = array.array('d')
In [26]: with open('array.apy', 'rb') as f:
             b.fromfile(f, 2)
In [27]: b
Out[27]: array('d', [0.0004882813645963324, 0.12500002956949174])
```

Instantiates a new array object with type code float.

Opens the file for reading binary data …

… and reads five elements in the b object.

Instantiates a new array object with type code double.

Reads two elements from the file.

The difference in type codes leads to "wrong" numbers.

# **Regular NumPy Arrays**

Composing array structures with list objects works, somewhat. But it is not really convenient, and the list class has not been built with this specific goal in mind. It has rather a much broader and more general scope. The array class is a bit more specialized, providing some useful features for working with arrays of data. However, a truly specialized class could be really beneficial to handle array-type structures.

### **The Basics**

numpy.ndarray is just such a class, built with the specific goal of handling *n*dimensional arrays both conveniently and efficiently — i.e., in a highly performant manner. The basic handling of instances of this class is again best illustrated by examples:

```
In [28]: import numpy as np
In [29]: a = np.array([0, 0.5, 1.0, 1.5, 2.0])
         a
Out[29]: array([0. , 0.5, 1. , 1.5, 2. ])
In [30]: type(a)
Out[30]: numpy.ndarray
In [31]: a = np.array(['a', 'b', 'c'])
         a
Out[31]: array(['a', 'b', 'c'], dtype='<U1')
In [32]: a = np.arange(2, 20, 2)
         a
Out[32]: array([ 2, 4, 6, 8, 10, 12, 14, 16, 18])
In [33]: a = np.arange(8, dtype=np.float)
         a
Out[33]: array([0., 1., 2., 3., 4., 5., 6., 7.])
In [34]: a[5:]
Out[34]: array([5., 6., 7.])
In [35]: a[:2]
Out[35]: array([0., 1.])
```

Imports the numpy package.

Creates an ndarray object out of a list object with floats.

Creates an ndarray object out of a list object with strs.

np.arange() works similar to range() …

… but takes as additional input the dtype parameter.

With one-dimensional ndarray objects, indexing works as usual.

A major feature of the ndarray class is the *multitude of built-in methods*. For instance:

```
In [36]: a.sum()
Out[36]: 28.0
In [37]: a.std()
Out[37]: 2.29128784747792
In [38]: a.cumsum()
Out[38]: array([ 0., 1., 3., 6., 10., 15., 21., 28.])
```

The sum of all elements.

The standard deviation of the elements.

The cumulative sum of all elements (starting at index position 0).

Another major feature is the (vectorized) *mathematical operations* defined on ndarray objects:

```
In [39]: l = [0., 0.5, 1.5, 3., 5.]
        2 * l
Out[39]: [0.0, 0.5, 1.5, 3.0, 5.0, 0.0, 0.5, 1.5, 3.0, 5.0]
In [40]: a
Out[40]: array([0., 1., 2., 3., 4., 5., 6., 7.])
In [41]: 2 * a
Out[41]: array([ 0., 2., 4., 6., 8., 10., 12., 14.])
In [42]: a ** 2
Out[42]: array([ 0., 1., 4., 9., 16., 25., 36., 49.])
In [43]: 2 ** a
Out[43]: array([ 1., 2., 4., 8., 16., 32., 64., 128.])
In [44]: a ** a
Out[44]: array([1.00000e+00, 1.00000e+00, 4.00000e+00, 2.70000e+01, 2.56000e+02,
               3.12500e+03, 4.66560e+04, 8.23543e+05])
```

Scalar multiplication with list objects leads to a repetition of elements.

By contrast, working with ndarray objects implements a proper scalar multiplication.

This calculates element-wise the square values.

This interprets the elements of the ndarray as the powers.

This calculates the power of every element to itself.

*Universal functions* are another important feature of the NumPy package. They are "universal" in the sense that they in general operate on ndarray objects as well as on basic Python data types. However, when applying universal functions to, say, a Python float object, one needs to be aware of the reduced performance compared to the same functionality found in the math module:

```
In [45]: np.exp(a)
Out[45]: array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
               5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03])
In [46]: np.sqrt(a)
Out[46]: array([0. , 1. , 1.41421356, 1.73205081, 2. ,
               2.23606798, 2.44948974, 2.64575131])
In [47]: np.sqrt(2.5)
Out[47]: 1.5811388300841898
In [48]: import math
In [49]: math.sqrt(2.5)
Out[49]: 1.5811388300841898
In [50]: math.sqrt(a)
        ---------------------------------------
        TypeErrorTraceback (most recent call last)
        <ipython-input-50-b39de4150838> in <module>()
        ----> 1 math.sqrt(a)
        TypeError: only size-1 arrays can be converted to Python scalars
In [51]: %timeit np.sqrt(2.5)
        722 ns ± 13.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops
         each)
In [52]: %timeit math.sqrt(2.5)
        91.8 ns ± 4.13 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops
         each)
```

| Calculates<br>the<br>exponential<br>values<br>element-wise.                                              |
|----------------------------------------------------------------------------------------------------------|
| Calculates<br>the<br>square<br>root<br>for<br>every<br>element.                                          |
| Calculates<br>the<br>square<br>root<br>for<br>a<br>Python<br>object.<br>float                            |
| The<br>same<br>calculation,<br>this<br>time<br>using<br>the<br>module.<br>math                           |
| The<br>function<br>cannot<br>be<br>applied<br>to<br>the<br>object<br>directly.<br>math.sqrt()<br>ndarray |
| Applying<br>the<br>universal<br>function<br>to<br>a<br>Python<br>object<br>…<br>np.sqrt()<br>float       |
|                                                                                                          |

… is much slower than the same operation with the math.sqrt() function.

### **Multiple Dimensions**

The transition to more than one dimension is seamless, and all features presented so far carry over to the more general cases. In particular, the indexing system is made consistent across all dimensions: In [53]: b = np.array([a, a \* 2]) b Out[53]: array([[ 0., 1., 2., 3., 4., 5., 6., 7.], [ 0., 2., 4., 6., 8., 10., 12., 14.]]) In [54]: b[0] Out[54]: array([0., 1., 2., 3., 4., 5., 6., 7.]) In [55]: b[0, 2] Out[55]: 2.0 In [56]: b[:, 1] Out[56]: array([1., 2.]) In [57]: b.sum() Out[57]: 84.0 In [58]: b.sum(axis=0) Out[58]: array([ 0., 3., 6., 9., 12., 15., 18., 21.]) In [59]: b.sum(axis=1) Out[59]: array([28., 56.])

Constructs a two-dimensional ndarray object out of the one-dimensional one.

Selects the first row.

Selects the third element in the first row; indices are separated, within the brackets, by a comma.

Selects the second column.

Calculates the sum of *all* values.

Calculates the sum along the first axis; i.e., column-wise.

Calculates the sum along the second axis; i.e., row-wise.

There are a number of ways to initialize (instantiate) ndarray objects. One is as presented before, via np.array. However, this assumes that all elements of the array are already available. In contrast, one might like to have the ndarray objects instantiated first to populate them later with results generated during the execution of code. To this end, one can use the following functions: In [60]: c = np.zeros((2, 3), dtype='i', order='C') c Out[60]: array([[0, 0, 0], [0, 0, 0]], dtype=int32) In [61]: c = np.ones((2, 3, 4), dtype='i', order='C') c Out[61]: array([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]], dtype=int32) In [62]: d = np.zeros\_like(c, dtype='f16', order='C') d Out[62]: array([[[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]], [[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]]], dtype=float128) In [63]: d = np.ones\_like(c, dtype='f16', order='C') d Out[63]: array([[[1., 1., 1., 1.], [1., 1., 1., 1.], [1., 1., 1., 1.]], [[1., 1., 1., 1.], [1., 1., 1., 1.], [1., 1., 1., 1.]]], dtype=float128) In [64]: e = np.empty((2, 3, 2)) e Out[64]: array([[[0.00000000e+000, 0.00000000e+000], [0.00000000e+000, 0.00000000e+000], [0.00000000e+000, 0.00000000e+000]], [[0.00000000e+000, 0.00000000e+000], [0.00000000e+000, 7.49874326e+247], [1.28822975e-231, 4.33190018e-311]]]) In [65]: f = np.empty\_like(c) f Out[65]: array([[[ 0, 0, 0, 0], [ 0, 0, 0, 0], [ 0, 0, 0, 0]], [[ 0, 0, 0, 0], [ 0, 0, 740455269, 1936028450], [ 0, 268435456, 1835316017, 2041]]], dtype=int32) In [66]: np.eye(5) Out[66]: array([[1., 0., 0., 0., 0.], [0., 1., 0., 0., 0.], [0., 0., 1., 0., 0.], [0., 0., 0., 1., 0.], [0., 0., 0., 0., 1.]]) In [67]: g = np.linspace(5, 15, 12) g Out[67]: array([ 5. , 5.90909091, 6.81818182, 7.72727273, 8.63636364, 9.54545455, 10.45454545, 11.36363636, 12.27272727, 13.18181818, 14.09090909, 15. ])

Creates an ndarray object prepopulated with zeros.

Creates an ndarray object prepopulated with ones.

The same, but takes another ndarray object to infer the shape.

Creates an ndarray object not prepopulated with anything (numbers depend on the bits present in the memory).

Creates a square matrix as an ndarray object with the diagonal populated by ones.

Creates a one-dimensional ndarray object with evenly spaced intervals between numbers; parameters used are start, end, and num (number of elements).

For all these functions, one can provide the following parameters: shape

Either an int, a sequence of int objects, or a reference to another ndarray

*dtype (optional)*

A dtype — these are NumPy-specific data types for ndarray objects

*order (optional)*

The order in which to store elements in memory: C for C-like (i.e., rowwise) or F for Fortran-like (i.e., column-wise)

Here, it becomes obvious how NumPy specializes the construction of arrays with the ndarray class, in comparison to the list -based approach:

- The ndarray object has built-in *dimensions* (axes).
- The ndarray object is *immutable*; its length (size) is fixed.
- It only allows for a *single data type* (np.dtype) for the whole array.

The array class by contrast shares only the characteristic of allowing for a single data type (type code, dtype).

The role of the order parameter is discussed later in the chapter. Table 4-1 provides an overview of selected np.dtype objects (i.e., the basic data types NumPy allows).

| dtype | Description         | Example                 |
|-------|---------------------|-------------------------|
| ?     | Boolean             | ? (True<br>or<br>False) |
| i     | Signed<br>integer   | i8 (64-bit)             |
| u     | Unsigned<br>integer | u8 (64-bit)             |

| Table<br>4-1.<br>NumPy | dtype | objects |
|------------------------|-------|---------|
|------------------------|-------|---------|

| u | Unsigned<br>integer          | u8 (64-bit)                       |
|---|------------------------------|-----------------------------------|
| f | Floating<br>point            | f8 (64-bit)                       |
| c | Complex<br>floating<br>point | c32 (256-bit)                     |
| m | timedelta                    | m (64-bit)                        |
| M | datetime                     | M (64-bit)                        |
| O | Object                       | O (pointer<br>to<br>object)       |
| U | Unicode                      | U24 (24<br>Unicode<br>characters) |
| V | Raw<br>data<br>(void)        | V12 (12-byte<br>data<br>block)    |

### **Metainformation**

```
Every ndarray object provides access to a number of useful attributes: In [68]:
g.size Out[68]: 12 In [69]: g.itemsize Out[69]: 8 In [70]:
g.ndim Out[70]: 1 In [71]: g.shape Out[71]: (12,) In [72]:
g.dtype Out[72]: dtype('float64') In [73]: g.nbytes Out[73]: 96
```

The number of elements.

The number of bytes used to represent one element.

The number of dimensions.

The shape of the ndarray object.

The dtype of the elements.

The total number of bytes used in memory.

### **Reshaping and Resizing**

Although ndarray objects are immutable by default, there are multiple options to reshape and resize such an object. While *reshaping* in general just provides another *view* on the same data, *resizing* in general creates a *new* (temporary) object. First, some examples of reshaping:

```
In [74]: g = np.arange(15)
In [75]: g
Out[75]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
In [76]: g.shape
Out[76]: (15,)
In [77]: np.shape(g)
Out[77]: (15,)
In [78]: g.reshape((3, 5))
Out[78]: array([[ 0, 1, 2, 3, 4],
               [ 5, 6, 7, 8, 9],
               [10, 11, 12, 13, 14]])
In [79]: h = g.reshape((5, 3))
        h
Out[79]: array([[ 0, 1, 2],
               [ 3, 4, 5],
               [ 6, 7, 8],
               [ 9, 10, 11],
               [12, 13, 14]])
In [80]: h.T
Out[80]: array([[ 0, 3, 6, 9, 12],
               [ 1, 4, 7, 10, 13],
               [ 2, 5, 8, 11, 14]])
In [81]: h.transpose()
Out[81]: array([[ 0, 3, 6, 9, 12],
               [ 1, 4, 7, 10, 13],
               [ 2, 5, 8, 11, 14]])
```

The shape of the original ndarray object.

Reshaping to two dimensions (memory view).

Creating a new object.

The transpose of the new ndarray object.

During a reshaping operation, the total number of elements in the ndarray object is unchanged. During a resizing operation, this number changes — it either decreases ("down-sizing") or increases ("up-sizing"). Here some examples of resizing:

```
In [82]: g
Out[82]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
In [83]: np.resize(g, (3, 1))
Out[83]: array([[0],
               [1],
               [2]])
In [84]: np.resize(g, (1, 5))
Out[84]: array([[0, 1, 2, 3, 4]])
In [85]: np.resize(g, (2, 5))
Out[85]: array([[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]])
In [86]: n = np.resize(g, (5, 4))
        n
Out[86]: array([[ 0, 1, 2, 3],
               [ 4, 5, 6, 7],
               [ 8, 9, 10, 11],
               [12, 13, 14, 0],
               [ 1, 2, 3, 4]])
```

Two dimensions, down-sizing.

Two dimensions, up-sizing.

*Stacking* is a special operation that allows the horizontal or vertical combination of two ndarray objects. However, the size of the "connecting" dimension must be the same:

```
In [87]: h
Out[87]: array([[ 0, 1, 2],
               [ 3, 4, 5],
               [ 6, 7, 8],
               [ 9, 10, 11],
               [12, 13, 14]])
In [88]: np.hstack((h, 2 * h))
Out[88]: array([[ 0, 1, 2, 0, 2, 4],
               [ 3, 4, 5, 6, 8, 10],
               [ 6, 7, 8, 12, 14, 16],
               [ 9, 10, 11, 18, 20, 22],
```

```
[12, 13, 14, 24, 26, 28]])
In [89]: np.vstack((h, 0.5 * h))
Out[89]: array([[ 0. , 1. , 2. ],
               [ 3. , 4. , 5. ],
               [ 6. , 7. , 8. ],
               [ 9. , 10. , 11. ],
               [12. , 13. , 14. ],
               [ 0. , 0.5, 1. ],
               [ 1.5, 2. , 2.5],
               [ 3. , 3.5, 4. ],
               [ 4.5, 5. , 5.5],
               [ 6. , 6.5, 7. ]])
```

Horizontal stacking of two ndarray objects.

Vertical stacking of two ndarray objects.

Another special operation is the *flattening* of a multidimensional ndarray object to a one-dimensional one. One can choose whether the flattening happens rowby-row (C order) or column-by-column (F order):

```
In [90]: h
Out[90]: array([[ 0, 1, 2],
               [ 3, 4, 5],
               [ 6, 7, 8],
               [ 9, 10, 11],
               [12, 13, 14]])
In [91]: h.flatten()
Out[91]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
In [92]: h.flatten(order='C')
Out[92]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
In [93]: h.flatten(order='F')
Out[93]: array([ 0, 3, 6, 9, 12, 1, 4, 7, 10, 13, 2, 5, 8, 11, 14])
In [94]: for i in h.flat:
            print(i, end=',')
        0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,
In [95]: for i in h.ravel(order='C'):
            print(i, end=',')
        0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,
In [96]: for i in h.ravel(order='F'):
            print(i, end=',')
        0,3,6,9,12,1,4,7,10,13,2,5,8,11,14,
```

The default order for flattening is C.

Flattening with F order.

The flat attribute provides a flat iterator (C order).

The ravel() method is an alternative to flatten().

### **Boolean Arrays**

Comparison and logical operations in general work on ndarray objects the same way, element-wise, as on standard Python data types. Evaluating conditions yield by default a Boolean ndarray object (dtype is bool):

```
In [97]: h
Out[97]: array([[ 0, 1, 2],
                [ 3, 4, 5],
                [ 6, 7, 8],
                [ 9, 10, 11],
                [12, 13, 14]])
In [98]: h > 8
Out[98]: array([[False, False, False],
                [False, False, False],
                [False, False, False],
                [ True, True, True],
                [ True, True, True]])
In [99]: h <= 7
Out[99]: array([[ True, True, True],
                [ True, True, True],
                [ True, True, False],
                [False, False, False],
                [False, False, False]])
In [100]: h == 5
Out[100]: array([[False, False, False],
                 [False, False, True],
                 [False, False, False],
                 [False, False, False],
                 [False, False, False]])
In [101]: (h == 5).astype(int)
Out[101]: array([[0, 0, 0],
                 [0, 0, 1],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])
In [102]: (h > 4) & (h <= 12)
Out[102]: array([[False, False, False],
                 [False, False, True],
                 [ True, True, True],
                 [ True, True, True],
                 [ True, False, False]])
```

Is value greater than …?

Is value smaller or equal than …?

Is value equal to …?

Present True and False as integer values 0 and 1.

Is value greater than … and smaller than or equal to …?

Such Boolean arrays can be used for indexing and data selection. Notice that the following operations flatten the data:

```
In [103]: h[h > 8]
Out[103]: array([ 9, 10, 11, 12, 13, 14])
In [104]: h[(h > 4) & (h <= 12)]
Out[104]: array([ 5, 6, 7, 8, 9, 10, 11, 12])
In [105]: h[(h < 4) | (h >= 12)]
Out[105]: array([ 0, 1, 2, 3, 12, 13, 14])
```

Give me all values greater than …

Give me all values greater than … *and* smaller than or equal to …

Give me all values greater than … *or* smaller than or equal to …

A powerful tool in this regard is the np.where() function, which allows the definition of actions/operations depending on whether a condition is True or False. The result of applying np.where() is a new ndarray object of the same shape as the original one:

```
In [106]: np.where(h > 7, 1, 0)
Out[106]: array([[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 1],
                 [1, 1, 1],
                 [1, 1, 1]])
In [107]: np.where(h % 2 == 0, 'even', 'odd')
Out[107]: array([['even', 'odd', 'even'],
                 ['odd', 'even', 'odd'],
                 ['even', 'odd', 'even'],
                 ['odd', 'even', 'odd'],
                 ['even', 'odd', 'even']], dtype='<U4')
```

```
In [108]: np.where(h <= 7, h * 2, h / 2)
Out[108]: array([[ 0. , 2. , 4. ],
                [ 6. , 8. , 10. ],
                [12. , 14. , 4. ],
                [ 4.5, 5. , 5.5],
                [ 6. , 6.5, 7. ]])
```

In the new object, set 1 if True and 0 otherwise.

In the new object, set even if True and odd otherwise.

In the new object, set two times the h element if True and half the h element otherwise.

Later chapters provide more examples of these important operations on ndarray objects.

### **Speed Comparison**

We'll move on to structured arrays with NumPy shortly, but let us stick with regular arrays for a moment and see what the specialization brings in terms of performance.

As a simple example, consider the generation of a matrix/array of shape 5,000 × 5,000 elements, populated with pseudo-random, standard normally distributed numbers. The sum of all elements shall then be calculated. First, the pure Python approach, where list comprehensions are used:

```
In [109]: import random
          I = 5000
In [110]: %time mat = [[random.gauss(0, 1) for j in range(I)] \
                       for i in range(I)]
          CPU times: user 17.1 s, sys: 361 ms, total: 17.4 s
          Wall time: 17.4 s
In [111]: mat[0][:5]
Out[111]: [-0.40594967782329183,
           -1.357757478015285,
           0.05129566894355976,
           -0.8958429976582192,
           0.6234174778878331]
In [112]: %time sum([sum(l) for l in mat])
          CPU times: user 142 ms, sys: 1.69 ms, total: 144 ms
          Wall time: 143 ms
Out[112]: -3561.944965714259
In [113]: import sys
          sum([sys.getsizeof(l) for l in mat])
Out[113]: 215200000
```

The creation of the matrix via a nested list comprehension.

Some selected random numbers from those drawn.

The sums of the single list objects are first calculated during a list comprehension; then the sum of the sums is taken.

This adds up the memory usage of all list objects.

Let us now turn to NumPy and see how the same problem is solved there. For convenience, the NumPy subpackage random offers a multitude of functions to instantiate an ndarray object and populate it at the same time with pseudorandom numbers: In [114]: %time mat = np.random.standard\_normal((I, I)) CPU times: user 1.01 s, sys: 200 ms, total: 1.21 s Wall time: 1.21 s In [115]: %time mat.sum() CPU times: user 29.7 ms, sys: 1.15 ms, total: 30.8 ms Wall time: 29.4 ms Out[115]: -186.12767026606448 In [116]: mat.nbytes Out[116]: 200000000 In [117]: sys.getsizeof(mat) Out[117]: 200000112

Creates the ndarray object with standard normally distributed random numbers; it is faster by a factor of about 14.

Calculates the sum of all values in the ndarray object; it is faster by a factor of 4.5.

The NumPy approach also saves some memory since the memory overhead of the ndarray object is tiny compared to the size of the data itself.

### **USING NUMPY ARRAYS**

The use of NumPy for array-based operations and algorithms generally results in compact, easily readable code and significant performance improvements over pure Python code.

## **Structured NumPy Arrays**

The specialization of the ndarray class obviously brings a number of valuable benefits with it. However, a too narrow specialization might turn out to be too large a burden to carry for the majority of array-based algorithms and [applications.](http://bit.ly/2DHsXgn) Therefore, NumPy provides *structured* ndarray and *record* recarray objects that allow you to have a different dtype *per column*. What does "per column" mean? Consider the following initialization of a structured ndarray object:

```
In [118]: dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),
                         ('Height', 'f'), ('Children/Pets', 'i4', 2)])
In [119]: dt
Out[119]: dtype([('Name', 'S10'), ('Age', '<i4'), ('Height', '<f4'),
           ('Children/Pets', '<i4', (2,))])
In [120]: dt = np.dtype({'names': ['Name', 'Age', 'Height', 'Children/Pets'],
                       'formats':'O int float int,int'.split()})
In [121]: dt
Out[121]: dtype([('Name', 'O'), ('Age', '<i8'), ('Height', '<f8'),
           ('Children/Pets', [('f0', '<i8'), ('f1', '<i8')])])
In [122]: s = np.array([('Smith', 45, 1.83, (0, 1)),
                        ('Jones', 53, 1.72, (2, 2))], dtype=dt)
In [123]: s
Out[123]: array([('Smith', 45, 1.83, (0, 1)), ('Jones', 53, 1.72, (2, 2))],
          dtype=[('Name', 'O'), ('Age', '<i8'), ('Height', '<f8'),
           ('Children/Pets', [('f0', '<i8'), ('f1', '<i8')])])
In [124]: type(s)
Out[124]: numpy.ndarray
```

The complex dtype is composed.

An alternative syntax to achieve the same result.

The structured ndarray is instantiated with two records.

The object type is still ndarray.

In a sense, this construction comes quite close to the operation for initializing tables in a SQL database: one has column names and column data types, with maybe some additional information (e.g., maximum number of characters per str object). The single columns can now be easily accessed by their names and the rows by their index values:

```
In [125]: s['Name']
Out[125]: array(['Smith', 'Jones'], dtype=object)
In [126]: s['Height'].mean()
Out[126]: 1.775
In [127]: s[0]
Out[127]: ('Smith', 45, 1.83, (0, 1))
In [128]: s[1]['Age']
Out[128]: 53
```

Selecting a column by name.

Calling a method on a selected column.

Selecting a record.

Selecting a field in a record.

In summary, structured arrays are a generalization of the regular ndarray object type in that the data type only has to be the same *per column*, like in tables in SQL databases. One advantage of structured arrays is that a single element of a column can be another multidimensional object and does not have to conform to the basic NumPy data types.

### **STRUCTURED ARRAYS**

NumPy provides, in addition to regular arrays, structured (and record) arrays that allow the description and handling of table-like data structures with a variety of different data types per (named) column. They bring SQL table–like data structures to Python, with most of the benefits of regular ndarray objects (syntax, methods, performance).

# **Vectorization of Code**

*Vectorization* is a strategy to get more compact code that is possibly executed faster. The fundamental idea is to conduct an operation on or to apply a function to a complex object "at once" and not by looping over the single elements of the object. In Python, functional programming tools such as map() and filter() provide some basic means for vectorization. However, NumPy has vectorization built in deep down in its core.

### **Basic Vectorization**

As demonstrated in the previous section, simple mathematical operations such as calculating the sum of all elements — can be implemented on ndarray objects directly (via methods or universal functions). More general vectorized operations are also possible. For example, one can add two NumPy arrays element-wise as follows:

```
In [129]: np.random.seed(100)
          r = np.arange(12).reshape((4, 3))
          s = np.arange(12).reshape((4, 3)) * 0.5
In [130]: r
Out[130]: array([[ 0, 1, 2],
                 [ 3, 4, 5],
                 [ 6, 7, 8],
                 [ 9, 10, 11]])
In [131]: s
Out[131]: array([[0. , 0.5, 1. ],
                 [1.5, 2. , 2.5],
                 [3. , 3.5, 4. ],
                 [4.5, 5. , 5.5]])
In [132]: r + s
Out[132]: array([[ 0. , 1.5, 3. ],
                 [ 4.5, 6. , 7.5],
                 [ 9. , 10.5, 12. ],
                 [13.5, 15. , 16.5]])
```

The first ndarray object with random numbers.

The second ndarray object with random numbers.

Element-wise addition as a vectorized operation (no looping).

NumPy also supports what is called *broadcasting*. This allows you to combine objects of different shape within a single operation. Previous examples have already made use of this. Consider the following examples:

```
In [133]: r + 3
Out[133]: array([[ 3, 4, 5],
                [ 6, 7, 8],
                [ 9, 10, 11],
                [12, 13, 14]])
```

```
In [134]: 2 * r
Out[134]: array([[ 0, 2, 4],
                 [ 6, 8, 10],
                 [12, 14, 16],
                 [18, 20, 22]])
In [135]: 2 * r + 3
Out[135]: array([[ 3, 5, 7],
                 [ 9, 11, 13],
                 [15, 17, 19],
                 [21, 23, 25]])
```

During scalar addition, the scalar is broadcast and added to every element.

During scalar multiplication, the scalar is also broadcast to and multiplied with every element.

This linear transformation combines both operations.

These operations work with differently shaped ndarray objects as well, up to a certain point:

```
In [136]: r
Out[136]: array([[ 0, 1, 2],
                 [ 3, 4, 5],
                 [ 6, 7, 8],
                 [ 9, 10, 11]])
In [137]: r.shape
Out[137]: (4, 3)
In [138]: s = np.arange(0, 12, 4)
          s
Out[138]: array([0, 4, 8])
In [139]: r + s
Out[139]: array([[ 0, 5, 10],
                 [ 3, 8, 13],
                 [ 6, 11, 16],
                 [ 9, 14, 19]])
In [140]: s = np.arange(0, 12, 3)
          s
Out[140]: array([0, 3, 6, 9])
In [141]: r + s
          ---------------------------------------
          ValueErrorTraceback (most recent call last)
          <ipython-input-141-1890b26ec965> in <module>()
          ----> 1 r + s
```

```
ValueError: operands could not be broadcast together
                      with shapes (4,3) (4,)
In [142]: r.transpose() + s
Out[142]: array([[ 0, 6, 12, 18],
                 [ 1, 7, 13, 19],
                 [ 2, 8, 14, 20]])
In [143]: sr = s.reshape(-1, 1)
          sr
Out[143]: array([[0],
                 [3],
                 [6],
                 [9]])
In [144]: sr.shape
Out[144]: (4, 1)
In [145]: r + s.reshape(-1, 1)
Out[145]: array([[ 0, 1, 2],
                 [ 6, 7, 8],
                 [12, 13, 14],
                 [18, 19, 20]])
```

A new one-dimensional ndarray object of length 3.

The r (matrix) and s (vector) objects can be added straightforwardly.

Another one-dimensional ndarray object of length 4.

The length of the new s (vector) object is now different from the length of the second dimension of the r object.

Transposing the r object again allows for the vectorized addition.

Alternatively, the shape of s can be changed to (4, 1) to make the addition work (the results are different, however).

Often, custom-defined Python functions work with ndarray objects as well. If the implementation allows, arrays can be used with functions just as int or float objects can. Consider the following function:

```
In [146]: def f(x):
              return 3 * x + 5
```

```
In [147]: f(0.5)
Out[147]: 6.5
In [148]: f(r)
Out[148]: array([[ 5, 8, 11],
                 [14, 17, 20],
                 [23, 26, 29],
                 [32, 35, 38]])
```

A simple Python function implementing a linear transform on parameter x.

The function f() applied to a Python float object.

The same function applied to an ndarray object, resulting in a vectorized and element-wise evaluation of the function.

What NumPy does is to simply apply the function f to the object element-wise. In that sense, by using this kind of operation one does *not* avoid loops; one only avoids them on the Python level and delegates the looping to NumPy. On the NumPy level, looping over the ndarray object is taken care of by optimized code, most of it written in C and therefore generally faster than pure Python. This explains the "secret" behind the performance benefits of using NumPy for arraybased use cases.

### **Memory Layout**

When ndarray objects are initialized by using np.zeros(), as in "Multiple Dimensions", an optional argument for the memory layout is provided. This argument specifies, roughly speaking, which elements of an array get stored in memory next to each other (contiguously). When working with small arrays, this has hardly any measurable impact on the performance of array operations. However, when arrays get large, and depending on the (financial) algorithm to be implemented on them, the story might be different. This is when *memory layout* comes into play (see, for instance, Eli Bendersky's article "Memory Layout of [MultiDimensional](http://bit.ly/2K8rujN) Arrays").

To illustrate the potential importance of the memory layout of arrays in science and finance, consider the following construction of multidimensional ndarray objects:

```
In [149]: x = np.random.standard_normal((1000000, 5))
In [150]: y = 2 * x + 3
In [151]: C = np.array((x, y), order='C')
In [152]: F = np.array((x, y), order='F')
In [153]: x = 0.0; y = 0.0
In [154]: C[:2].round(2)
Out[154]: array([[[-1.75, 0.34, 1.15, -0.25, 0.98],
                 [ 0.51, 0.22, -1.07, -0.19, 0.26],
                 [-0.46, 0.44, -0.58, 0.82, 0.67],
                 ...,
                 [-0.05, 0.14, 0.17, 0.33, 1.39],
                 [ 1.02, 0.3 , -1.23, -0.68, -0.87],
                 [ 0.83, -0.73, 1.03, 0.34, -0.46]],
                [[-0.5 , 3.69, 5.31, 2.5 , 4.96],
                 [ 4.03, 3.44, 0.86, 2.62, 3.51],
                 [ 2.08, 3.87, 1.83, 4.63, 4.35],
                 ...,
                 [ 2.9 , 3.28, 3.33, 3.67, 5.78],
                 [ 5.04, 3.6 , 0.54, 1.65, 1.26],
                 [ 4.67, 1.54, 5.06, 3.69, 2.07]]])
```

A linear transform of the original object data.

An ndarray object with large asymmetry in the two dimensions.

A linear transform of the original object data.

This creates a two-dimensional ndarray object with C order (row-major).

This creates a two-dimensional ndarray object with F order (columnmajor).

Memory is freed up (contingent on garbage collection).

Some numbers from the C object.

Let's look at some fundamental examples and use cases for both types of ndarray objects and consider the speed with which they are executed given the different memory layouts:

```
In [155]: %timeit C.sum()
          4.36 ms ± 89.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
In [156]: %timeit F.sum()
          4.21 ms ± 71.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
In [157]: %timeit C.sum(axis=0)
          17.9 ms ± 776 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
In [158]: %timeit C.sum(axis=1)
          35.1 ms ± 999 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
In [159]: %timeit F.sum(axis=0)
          83.8 ms ± 2.63 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
In [160]: %timeit F.sum(axis=1)
          67.9 ms ± 5.16 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
In [161]: F = 0.0; C = 0.0
```

Calculates the sum of all elements.

Calculates the sums per row ("many").

Calculates the sums per columns ("few").

We can summarize the performance results as follows:

- When calculating the sum of *all elements*, the memory layout does not really matter.
- The summing up over the C-ordered ndarray objects is faster both over rows and over columns (an *absolute* speed advantage).
- With the C-ordered (row-major) ndarray object, summing up over rows is *relatively* faster compared to summing up over columns.
- With the F-ordered (column-major) ndarray object, summing up over columns is *relatively* faster compared to summing up over rows.

# **Conclusion**

NumPy is the package of choice for numerical computing in Python. The ndarray class is specifically designed to be convenient and efficient in the handling of (large) numerical data. Powerful methods and NumPy universal functions allow for vectorized code that mostly avoids slow loops on the Python level. Many approaches introduced in this chapter carry over to pandas and its DataFrame class as well (see Chapter 5).
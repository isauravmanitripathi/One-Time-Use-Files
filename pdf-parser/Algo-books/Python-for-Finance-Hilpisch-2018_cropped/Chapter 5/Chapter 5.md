# **Chapter 5. Data Analysis with pandas**

Data! Data! Data! I can't make bricks without clay! Sherlock Holmes

This chapter is about pandas, a library for data analysis with a focus on tabular data. pandas is a powerful tool that not only provides many useful classes and functions but also does a great job of wrapping functionality from other packages. The result is a user interface that makes data analysis, and in particular financial analysis, a convenient and efficient task.

This chapter covers the following fundamental data structures:

| Object<br>type | Meaning                                          | Used<br>for                                   |
|----------------|--------------------------------------------------|-----------------------------------------------|
| DataFrame      | 2-dimensional<br>data<br>object<br>with<br>index | Tabular<br>data<br>organized<br>in<br>columns |
| Series         | 1-dimensional<br>data<br>object<br>with<br>index | Single<br>(time)<br>series<br>of<br>data      |

The chapter is organized as follows: "The DataFrame Class"

This section starts by exploring the basic characteristics and capabilities of the DataFrame class of pandas by using simple and small data sets; it then shows how to transform a NumPy ndarray object into a DataFrame object.

*"Basic Analytics" and "Basic Visualization"*

Basic analytics and visualization capabilities are introduced in these sections (later chapters go deeper into these topics).

*"The Series Class"*

This rather brief section covers the Series class of pandas, which in a sense represents a special case of the DataFrame class with a single column of data only.

*"GroupBy Operations"*

One of the strengths of the DataFrame class lies in grouping data according to a single or multiple columns. This section explores the grouping capabilities of pandas.

### *"Complex Selection"*

This section illustrates how the use of (complex) conditions allows for the easy selection of data from a DataFrame object.

### *"Concatenation, Joining, and Merging"*

The combining of different data sets into one is an important operation in data analysis. pandas provides different options to accomplish this task, as described in this section.

### *"Performance Aspects"*

Like Python in general, pandas often provides multiple options to accomplish the same goal. This section takes a brief look at potential performance differences.

# **The DataFrame Class**

At the core of pandas (and this chapter) is the DataFrame, a class designed to efficiently handle data in tabular form — i.e., data characterized by a columnar organization. To this end, the DataFrame class provides, for instance, column labeling as well as flexible indexing capabilities for the rows (records) of the data set, similar to a table in a relational database or an Excel spreadsheet.

This section covers some fundamental aspects of the pandas DataFrame class. The class is so complex and powerful that only a fraction of its capabilities can be presented here. Subsequent chapters provide more examples and shed light on different aspects.

## **First Steps with the DataFrame Class**

On a fundamental level, the DataFrame class is designed to manage indexed and labeled data, not too different from a SQL database table or a worksheet in a spreadsheet application. Consider the following creation of a DataFrame object:

```
In [1]: import pandas as pd
In [2]: df = pd.DataFrame([10, 20, 30, 40],
                       columns=['numbers'],
                       index=['a', 'b', 'c', 'd'])
In [3]: df
Out[3]: numbers
       a 10
       b 20
       c 30
       d 40
  Imports pandas.
  Defines the data as a list object.
```

Specifies the column label.

Specifies the index values/labels.

Shows the data as well as column and index labels of the DataFrame object.

This simple example already shows some major features of the DataFrame class when it comes to storing data:

- Data itself can be provided in different shapes and types (list, tuple, ndarray, and dict objects are candidates).
- Data is organized in columns, which can have custom names (labels).
- There is an index that can take on different formats (e.g., numbers, strings, time information).

Working with a DataFrame object is in general pretty convenient and efficient with regard to the handling of the object, e.g., compared to regular ndarray objects, which are more specialized and more restricted when one wants to (say) enlarge an existing object. At the same time, DataFrame objects are often as computationally efficient as ndarray objects. The following are simple examples showing how typical operations on a DataFrame object work:

```
In [4]: df.index
Out[4]: Index(['a', 'b', 'c', 'd'], dtype='object')
In [5]: df.columns
Out[5]: Index(['numbers'], dtype='object')
In [6]: df.loc['c']
Out[6]: numbers 30
       Name: c, dtype: int64
In [7]: df.loc[['a', 'd']]
Out[7]: numbers
       a 10
       d 40
In [8]: df.iloc[1:3]
Out[8]: numbers
       b 20
       c 30
In [9]: df.sum()
Out[9]: numbers 100
       dtype: int64
In [10]: df.apply(lambda x: x ** 2)
Out[10]: numbers
       a 100
       b 400
       c 900
       d 1600
In [11]: df ** 2
Out[11]: numbers
       a 100
       b 400
       c 900
       d 1600
```

The index attribute and Index object.

The columns attribute and Index object.

Selects the value corresponding to index c.

Selects the two values corresponding to indices a and d.

Selects the second and third rows via the index positions.

Calculates the sum of the single column.

Uses the apply() method to calculate squares in vectorized fashion.

Applies vectorization directly as with ndarray objects.

Contrary to NumPy ndarray objects, enlarging the DataFrame object in both dimensions is possible:

```
In [12]: df['floats'] = (1.5, 2.5, 3.5, 4.5)
In [13]: df
Out[13]: numbers floats
       a 10 1.5
       b 20 2.5
       c 30 3.5
       d 40 4.5
In [14]: df['floats']
Out[14]: a 1.5
       b 2.5
       c 3.5
       d 4.5
       Name: floats, dtype: float64
```

Adds a new column with float objects provided as a tuple object.

Selects this column and shows its data and index labels.

A whole DataFrame object can also be taken to define a new column. In such a case, indices are aligned automatically:

```
In [15]: df['names'] = pd.DataFrame(['Yves', 'Sandra', 'Lilli', 'Henry'],
                                  index=['d', 'a', 'b', 'c'])
In [16]: df
Out[16]: numbers floats names
```

| a | 10 | 1.5 | Sandra |
|---|----|-----|--------|
| b | 20 | 2.5 | Lilli  |
| c | 30 | 3.5 | Henry  |
| d | 40 | 4.5 | Yves   |

Another new column is created based on a DataFrame object.

Appending data works similarly. However, in the following example a side effect is seen that is usually to be avoided — namely, the index gets replaced by a simple range index:

```
In [17]: df.append({'numbers': 100, 'floats': 5.75, 'names': 'Jil'},
                   ignore_index=True)
Out[17]: numbers floats names
       0 10 1.50 Sandra
       1 20 2.50 Lilli
       2 30 3.50 Henry
       3 40 4.50 Yves
       4 100 5.75 Jil
In [18]: df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75,
                              'names': 'Jil'}, index=['y',]))
In [19]: df
Out[19]: numbers floats names
       a 10 1.50 Sandra
       b 20 2.50 Lilli
       c 30 3.50 Henry
       d 40 4.50 Yves
       y 100 5.75 Jil
In [20]: df = df.append(pd.DataFrame({'names': 'Liz'}, index=['z',]),
                   sort=False)
In [21]: df
Out[21]: numbers floats names
       a 10.0 1.50 Sandra
       b 20.0 2.50 Lilli
       c 30.0 3.50 Henry
       d 40.0 4.50 Yves
       y 100.0 5.75 Jil
       z NaN NaN Liz
In [22]: df.dtypes
Out[22]: numbers float64
       floats float64
       names object
       dtype: object
```

Appends a new row via a dict object; this is a temporary operation during which index information gets lost.

Appends the row based on a DataFrame object with index information; the original index information is preserved.

Appends an incomplete data row to the DataFrame object, resulting in NaN values.

Returns the different dtypes of the single columns; this is similar to what's possible with structured ndarray objects.

Although there are now missing values, the majority of method calls will still work:

```
In [23]: df[['numbers', 'floats']].mean()
Out[23]: numbers 40.00
        floats 3.55
        dtype: float64
In [24]: df[['numbers', 'floats']].std()
Out[24]: numbers 35.355339
        floats 1.662077
        dtype: float64
```

Calculates the mean over the two columns specified (ignoring rows with NaN values).

Calculates the standard deviation over the two columns specified (ignoring rows with NaN values).

# **Second Steps with the DataFrame Class**

The example in this subsection is based on an ndarray object with standard normally distributed random numbers. It explores further features such as a DatetimeIndex to manage time series data: In [25]: **import numpy as np** In [26]: np.random.seed(100) In [27]: a = np.random.standard\_normal((9, 4)) In [28]: a Out[28]: array([[-1.74976547, 0.3426804 , 1.1530358 , -0.25243604], [ 0.98132079, 0.51421884, 0.22117967, -1.07004333], [-0.18949583, 0.25500144, -0.45802699, 0.43516349], [-0.58359505, 0.81684707, 0.67272081, -0.10441114], [-0.53128038, 1.02973269, -0.43813562, -1.11831825], [ 1.61898166, 1.54160517, -0.25187914, -0.84243574], [ 0.18451869, 0.9370822 , 0.73100034, 1.36155613], [-0.32623806, 0.05567601, 0.22239961, -1.443217 ], [-0.75635231, 0.81645401, 0.75044476, -0.45594693]])

Although one can construct DataFrame objects more directly (as seen before), using an ndarray object is generally a good choice since pandas will retain the basic structure and will "only" add metainformation (e.g., index values). It also represents a typical use case for financial applications and scientific research in general. For example: In [29]: df = pd.DataFrame(a) In [30]: df Out[30]: 0 1 2 3 0 -1.749765 0.342680 1.153036 -0.252436 1 0.981321 0.514219 0.221180 -1.070043 2 -0.189496 0.255001 -0.458027 0.435163 3 -0.583595 0.816847 0.672721 -0.104411 4 -0.531280 1.029733 -0.438136 -1.118318 5 1.618982 1.541605 -0.251879 -0.842436 6 0.184519 0.937082 0.731000 1.361556 7 -0.326238 0.055676 0.222400 -1.443217 8 -0.756352 0.816454 0.750445 -0.455947

Creates a DataFrame object from the ndarray object.

Table 5-1 lists the parameters that the DataFrame() function takes. In the table, "array-like" means a data structure similar to an ndarray object — a list, for example. Index is an instance of the pandas Index class.

*Table 5-1. Parameters of DataFrame() function*

| data    | ndarray/dict/DataFrame    | Data<br>for<br>DataFrame;<br>dict can<br>contain<br>Series,<br>ndarray,<br>list |
|---------|---------------------------|---------------------------------------------------------------------------------|
| index   | Index/array-like          | Index<br>to<br>use;<br>defaults<br>to<br>range(n)                               |
| columns | Index/array-like          | Column<br>headers<br>to<br>use;<br>defaults<br>to<br>range(n)                   |
| dtype   | dtype,<br>default<br>None | Data<br>type<br>to<br>use/force;<br>otherwise,<br>it<br>is<br>inferred          |
| copy    | bool,<br>default<br>None  | Copy<br>data<br>from<br>inputs                                                  |

As with structured arrays, and as seen before, DataFrame objects have column names that can be defined directly by assigning a list object with the right number of elements. This illustrates that one can define/change the attributes of the DataFrame object easily: In [31]: df.columns = ['No1', 'No2', 'No3', 'No4'] In [32]: df Out[32]: No1 No2 No3 No4 0 -1.749765 0.342680 1.153036 -0.252436 1 0.981321 0.514219 0.221180 -1.070043 2 -0.189496 0.255001 -0.458027 0.435163 3 -0.583595 0.816847 0.672721 -0.104411 4 -0.531280 1.029733 -0.438136 -1.118318 5 1.618982 1.541605 -0.251879 -0.842436 6 0.184519 0.937082 0.731000 1.361556 7 -0.326238 0.055676 0.222400 -1.443217 8 -0.756352 0.816454 0.750445 -0.455947 In [33]: df['No2'].mean() Out[33]: 0.7010330941456459

Specifies the column labels via a list object.

Picking a column is now made easy.

**Parameter Format Description**

To work with financial time series data efficiently, one must be able to handle time indices well. This can also be considered a major strength of pandas. For example, assume that our nine data entries in the four columns correspond to month-end data, beginning in January 2019. A DatetimeIndex object is then generated with the date\_range() function as follows: In [34]: dates = pd.date\_range('2019-1-1', periods=9, freq='M') In [35]: dates Out[35]: DatetimeIndex(['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30', '2019-07-31', '2019-08- 31', '2019-09-30'], dtype='datetime64[ns]', freq='M')

Creates a DatetimeIndex object.

[Table](#page-10-0) 5-2 lists the parameters that the date\_range() function takes.

<span id="page-10-0"></span>

| Parameter | Format                   | Description                                                   |
|-----------|--------------------------|---------------------------------------------------------------|
| start     | string/datetime          | Left<br>bound<br>for<br>generating<br>dates                   |
| end       | string/datetime          | Right<br>bound<br>for<br>generating<br>dates                  |
| periods   | integer/None             | Number<br>of<br>periods<br>(if<br>start or<br>end is<br>None) |
| freq      | string/DateOffset        | Frequency<br>string,<br>e.g.,<br>5D for<br>5<br>days          |
| tz        | string/None              | Time<br>zone<br>name<br>for<br>localized<br>index             |
| normalize | bool,<br>default<br>None | Normalizes<br>start and<br>end to<br>midnight                 |
| name      | string,<br>default       | None Name<br>of<br>resulting<br>index                         |

*Table 5-2. Parameters of date\_range() function*

The following code defines the just-created DatetimeIndex object as the relevant index object, making a time series of the original data set: In [36]: df.index = dates In [37]: df Out[37]: No1 No2 No3 No4 2019-01-31 -1.749765 0.342680 1.153036 -0.252436 2019-02-28 0.981321 0.514219 0.221180 -1.070043 2019-03-31 -0.189496 0.255001 -0.458027 0.435163 2019-04-30 -0.583595 0.816847 0.672721 -0.104411 2019-05-31 -0.531280 1.029733 -0.438136 -1.118318 2019-06-30 1.618982 1.541605 -0.251879 -0.842436 2019-07-31 0.184519 0.937082 0.731000 1.361556 2019-08-31 -0.326238 0.055676 0.222400 -1.443217 2019-09-30 -0.756352 0.816454 0.750445 -0.455947

When it comes to the generation of DatetimeIndex objects with the help of the date\_range() function, there are a number of choices for the frequency parameter freq. Table 5-3 lists all the options.

> *Table 5-3. Frequency parameter values for date\_range() function*

|       | for<br>date_range()<br>function                          |
|-------|----------------------------------------------------------|
| Alias | Description                                              |
| B     | Business<br>day<br>frequency                             |
| C     | Custom<br>business<br>day<br>frequency<br>(experimental) |
| D     | Calendar<br>day<br>frequency                             |
| W     | Weekly<br>frequency                                      |
| M     | Month<br>end<br>frequency                                |
| BM    | Business<br>month<br>end<br>frequency                    |
| MS    | Month<br>start<br>frequency                              |
| BMS   | Business<br>month<br>start<br>frequency                  |
| Q     | Quarter<br>end<br>frequency                              |
| BQ    | Business<br>quarter<br>end<br>frequency                  |
| QS    | Quarter<br>start<br>frequency                            |
| BQS   | Business<br>quarter<br>start<br>frequency                |
| A     | Year<br>end<br>frequency                                 |
| BA    | Business<br>year<br>end<br>frequency                     |
| AS    | Year<br>start<br>frequency                               |
| BAS   | Business<br>year<br>start<br>frequency                   |
| H     | Hourly<br>frequency                                      |
| T     | Minutely<br>frequency                                    |
| S     | Secondly<br>frequency                                    |
| L     | Milliseconds                                             |
| U     | Microseconds                                             |

In some circumstances, it pays off to have access to the original data set in the

form of the ndarray object. The values attribute provides direct access to it: In [38]: df.values Out[38]: array([[-1.74976547, 0.3426804 , 1.1530358 , -0.25243604], [ 0.98132079, 0.51421884, 0.22117967, -1.07004333], [-0.18949583, 0.25500144, -0.45802699, 0.43516349], [-0.58359505, 0.81684707, 0.67272081, -0.10441114], [-0.53128038, 1.02973269, -0.43813562, -1.11831825], [ 1.61898166, 1.54160517, -0.25187914, -0.84243574], [ 0.18451869, 0.9370822 , 0.73100034, 1.36155613], [-0.32623806, 0.05567601, 0.22239961, -1.443217 ], [-0.75635231, 0.81645401, 0.75044476, -0.45594693]]) In [39]: np.array(df) Out[39]: array([[-1.74976547, 0.3426804 , 1.1530358 , -0.25243604], [ 0.98132079, 0.51421884, 0.22117967, -1.07004333], [-0.18949583, 0.25500144, -0.45802699, 0.43516349], [-0.58359505, 0.81684707, 0.67272081, -0.10441114], [-0.53128038, 1.02973269, -0.43813562, -1.11831825], [ 1.61898166, 1.54160517, -0.25187914, -0.84243574], [ 0.18451869, 0.9370822 , 0.73100034, 1.36155613], [-0.32623806, 0.05567601, 0.22239961, -1.443217 ], [-0.75635231, 0.81645401, 0.75044476, -0.45594693]])

### **ARRAYS AND DATAFRAMES**

One can generate a DataFrame object from an ndarray object, but one can also easily generate an ndarray object out of a DataFrame by using the values attribute of the DataFrame class or the function np.array() of NumPy.

# **Basic Analytics**

Like the NumPy ndarray class, the pandas DataFrame class has a multitude of convenience methods built in. As a starter, consider the methods info() and describe():

```
In [40]: df.info()
        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 9 entries, 2019-01-31 to 2019-09-30
        Freq: M
        Data columns (total 4 columns):
        No1 9 non-null float64
        No2 9 non-null float64
        No3 9 non-null float64
        No4 9 non-null float64
        dtypes: float64(4)
        memory usage: 360.0 bytes
In [41]: df.describe()
Out[41]: No1 No2 No3 No4
        count 9.000000 9.000000 9.000000 9.000000
        mean -0.150212 0.701033 0.289193 -0.387788
        std 0.988306 0.457685 0.579920 0.877532
        min -1.749765 0.055676 -0.458027 -1.443217
        25% -0.583595 0.342680 -0.251879 -1.070043
        50% -0.326238 0.816454 0.222400 -0.455947
        75% 0.184519 0.937082 0.731000 -0.104411
        max 1.618982 1.541605 1.153036 1.361556
```

Provides metainformation regarding the data, columns, and index.

Provides helpful summary statistics per column (for numerical data).

In addition, one can easily get the column-wise or row-wise sums, means, and cumulative sums:

```
In [43]: df.sum()
Out[43]: No1 -1.351906
        No2 6.309298
        No3 2.602739
        No4 -3.490089
        dtype: float64
In [44]: df.mean()
Out[44]: No1 -0.150212
        No2 0.701033
        No3 0.289193
        No4 -0.387788
```

```
dtype: float64
In [45]: df.mean(axis=0)
Out[45]: No1 -0.150212
        No2 0.701033
        No3 0.289193
        No4 -0.387788
        dtype: float64
In [46]: df.mean(axis=1)
Out[46]: 2019-01-31 -0.126621
        2019-02-28 0.161669
        2019-03-31 0.010661
        2019-04-30 0.200390
        2019-05-31 -0.264500
        2019-06-30 0.516568
        2019-07-31 0.803539
        2019-08-31 -0.372845
        2019-09-30 0.088650
        Freq: M, dtype: float64
In [47]: df.cumsum()
Out[47]: No1 No2 No3 No4
        2019-01-31 -1.749765 0.342680 1.153036 -0.252436
        2019-02-28 -0.768445 0.856899 1.374215 -1.322479
        2019-03-31 -0.957941 1.111901 0.916188 -0.887316
        2019-04-30 -1.541536 1.928748 1.588909 -0.991727
        2019-05-31 -2.072816 2.958480 1.150774 -2.110045
        2019-06-30 -0.453834 4.500086 0.898895 -2.952481
        2019-07-31 -0.269316 5.437168 1.629895 -1.590925
        2019-08-31 -0.595554 5.492844 1.852294 -3.034142
        2019-09-30 -1.351906 6.309298 2.602739 -3.490089
```

Column-wise sum.

Column-wise mean.

Row-wise mean.

Column-wise cumulative sum (starting at first index position).

DataFrame objects also understand NumPy universal functions, as expected:

```
In [48]: np.mean(df)
Out[48]: No1 -0.150212
       No2 0.701033
       No3 0.289193
       No4 -0.387788
       dtype: float64
In [49]: np.log(df)
Out[49]: No1 No2 No3 No4
```

2019-01-31 NaN -1.070957 0.142398 NaN 2019-02-28 -0.018856 -0.665106 -1.508780 NaN 2019-03-31 NaN -1.366486 NaN -0.832033 2019-04-30 NaN -0.202303 -0.396425 NaN 2019-05-31 NaN 0.029299 NaN NaN 2019-06-30 0.481797 0.432824 NaN NaN 2019-07-31 -1.690005 -0.064984 -0.313341 0.308628 2019-08-31 NaN -2.888206 -1.503279 NaN 2019-09-30 NaN -0.202785 -0.287089 NaN In [50]: np.sqrt(abs(df)) Out[50]: No1 No2 No3 No4 2019-01-31 1.322787 0.585389 1.073795 0.502430 2019-02-28 0.990616 0.717091 0.470297 1.034429 2019-03-31 0.435311 0.504977 0.676777 0.659669 2019-04-30 0.763934 0.903796 0.820196 0.323127 2019-05-31 0.728890 1.014757 0.661918 1.057506 2019-06-30 1.272392 1.241614 0.501876 0.917843 2019-07-31 0.429556 0.968030 0.854986 1.166857 2019-08-31 0.571173 0.235958 0.471593 1.201340 2019-09-30 0.869685 0.903578 0.866282 0.675238 In [51]: np.sqrt(abs(df)).sum() Out[51]: No1 7.384345 No2 7.075190 No3 6.397719 No4 7.538440 dtype: float64 In [52]: 100 \* df + 100 Out[52]: No1 No2 No3 No4 2019-01-31 -74.976547 134.268040 215.303580 74.756396 2019-02-28 198.132079 151.421884 122.117967 -7.004333 2019-03-31 81.050417 125.500144 54.197301 143.516349 2019-04-30 41.640495 181.684707 167.272081 89.558886 2019-05-31 46.871962 202.973269 56.186438 -11.831825 2019-06-30 261.898166 254.160517 74.812086 15.756426 2019-07-31 118.451869 193.708220 173.100034 236.155613 2019-08-31 67.376194 105.567601 122.239961 -44.321700 2019-09-30 24.364769 181.645401 175.044476 54.405307

Column-wise mean.

Element-wise natural logarithm; a warning is raised but the calculation runs through, resulting in multiple NaN values.

Element-wise square root for the absolute values …

… and column-wise mean values for the results.

A linear transform of the numerical data.

### **NUMPY UNIVERSAL FUNCTIONS**

In general, one can apply NumPy universal functions to pandas DataFrame objects whenever they could be applied to an ndarray object containing the same type of data.

pandas is quite error tolerant, in the sense that it captures errors and just puts a NaN value where the respective mathematical operation fails. Not only this, but as briefly shown before, one can also work with such incomplete data sets as if they were complete in a number of cases. This comes in handy, since reality is characterized by incomplete data sets more often than one might wish.

# **Basic Visualization**

Plotting of data is only one line of code away in general, once the data is stored in a DataFrame object (see [Figure](#page-18-0) 5-1): In [53]: **from pylab import** plt, mpl plt.style.use('seaborn') mpl.rcParams['font.family'] = 'serif' %matplotlib inline In [54]: df.cumsum().plot(lw=2.0, figsize=(10, 6));

Customizing the plotting style.

Plotting the cumulative sums of the four columns as a line plot.

Basically, pandas provides a wrapper around matplotplib (see Chapter 7), specifically designed for DataFrame objects. Table 5-4 lists the parameters that the plot() method takes.

<span id="page-18-0"></span>![](_page_18_Figure_7.jpeg)

*Figure 5-1. Line plot of a DataFrame object*

| Parameter             | Format                                                                   | Description                                                   |
|-----------------------|--------------------------------------------------------------------------|---------------------------------------------------------------|
| x                     | label/position,<br>default<br>None                                       | Only<br>used<br>when<br>column<br>values<br>are<br>x<br>ticks |
| y                     | label/position,<br>default<br>None                                       | Only<br>used<br>when<br>column<br>values<br>are<br>y<br>ticks |
| subplots              | boolean,<br>default<br>False                                             | Plot<br>columns<br>in<br>subplots                             |
| sharex                | boolean,<br>default<br>True                                              | Share<br>the<br>x-axis                                        |
| sharey                | boolean,<br>default<br>False                                             | Share<br>the<br>y-axis                                        |
| use_index             | boolean,<br>default<br>True                                              | Use<br>DataFrame.index as<br>x-ticks                          |
| stacked               | boolean,<br>default<br>False                                             | Stack<br>(only<br>for<br>bar<br>plots)                        |
| sort_columns boolean, | default<br>False                                                         | Sort<br>columns<br>alphabetically<br>before<br>plotting       |
| title                 | string,<br>default<br>None                                               | Title<br>for<br>the<br>plot                                   |
| grid                  | boolean,<br>default<br>False                                             | Show<br>horizontal<br>and<br>vertical<br>grid<br>lines        |
| legend                | boolean,<br>default<br>True                                              | Show<br>legend<br>of<br>labels                                |
| ax                    | matplotlib axis<br>object                                                | matplotlib axis<br>object<br>to<br>use<br>for<br>plotting     |
| style                 | string<br>or<br>list/dictionary                                          | Line<br>plotting<br>style<br>(for<br>each<br>column)          |
| kind                  | string<br>(e.g.,<br>"line",<br>"bar",<br>"barh",<br>"kde",<br>"density") | Type<br>of<br>plot                                            |
| logx                  | boolean,<br>default<br>False                                             | Use<br>logarithmic<br>scaling<br>of<br>x-axis                 |
| logy                  | boolean,<br>default<br>False                                             | Use<br>logarithmic<br>scaling<br>of<br>y-axis                 |
| xticks                | sequence,<br>default<br>Index                                            | X-ticks<br>for<br>the<br>plot                                 |
| yticks                | sequence,<br>default<br>Values                                           | Y-ticks<br>for<br>the<br>plot                                 |
| xlim                  | 2-tuple,<br>list                                                         | Boundaries<br>for<br>x-axis                                   |
| ylim                  | 2-tuple,<br>list                                                         | Boundaries<br>for<br>y-axis                                   |

### *Table 5-4. Parameters of plot() method*

| rot         | integer,<br>default<br>None                   | Rotation<br>of<br>x-ticks                        |
|-------------|-----------------------------------------------|--------------------------------------------------|
| secondary_y | boolean/sequence,<br>default<br>False         | Plot<br>on<br>secondary<br>y-axis                |
| mark_right  | boolean,<br>default<br>True                   | Automatic<br>labeling<br>of<br>secondary<br>axis |
| colormap    | string/colormap<br>object,<br>default<br>None | Color<br>map<br>to<br>use<br>for<br>plotting     |
| kwds        | keywords                                      | Options<br>to<br>pass<br>to<br>matplotlib        |

As another example, consider a bar plot of the same data (see [Figure](#page-20-0) 5-2): In [55]: df.plot.bar(figsize=(10, 6), rot=15); *# df.plot(kind='bar', figsize=(10, 6))*

Plots the bar chart via .plot.bar().

Alternative syntax: uses the kind parameter to change the plot type.

<span id="page-20-0"></span>![](_page_20_Figure_6.jpeg)

![](_page_20_Figure_7.jpeg)

# **The Series Class**

So far this chapter has worked mainly with the pandas DataFrame class. Series is another important class that comes with pandas. It is characterized by the fact that it has only a single column of data. In that sense, it is a specialization of the DataFrame class that shares many but not all of its characteristics and capabilities. A Series object is obtained when a single column is selected from a multicolumn DataFrame object:

```
In [56]: type(df)
Out[56]: pandas.core.frame.DataFrame
In [57]: S = pd.Series(np.linspace(0, 15, 7), name='series')
In [58]: S
Out[58]: 0 0.0
        1 2.5
        2 5.0
        3 7.5
        4 10.0
        5 12.5
        6 15.0
        Name: series, dtype: float64
In [59]: type(S)
Out[59]: pandas.core.series.Series
In [60]: s = df['No1']
In [61]: s
Out[61]: 2019-01-31 -1.749765
        2019-02-28 0.981321
        2019-03-31 -0.189496
        2019-04-30 -0.583595
        2019-05-31 -0.531280
        2019-06-30 1.618982
        2019-07-31 0.184519
        2019-08-31 -0.326238
        2019-09-30 -0.756352
        Freq: M, Name: No1, dtype: float64
In [62]: type(s)
Out[62]: pandas.core.series.Series
```

The main DataFrame methods are available for Series objects as well. For illustration, consider the mean() and plot() methods (see [Figure](#page-22-0) 5-3):

<span id="page-22-0"></span>![](_page_22_Figure_1.jpeg)

*Figure 5-3. Line plot of a Series object*

# **GroupBy Operations**

pandas has powerful and flexible grouping capabilities. They work similarly to grouping in SQL as well as pivot tables in Microsoft Excel. To have something to group by one can add, for instance, a column indicating the quarter the respective data of the index belongs to:

```
In [65]: df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2',
                      'Q2', 'Q3', 'Q3', 'Q3']
       df
Out[65]: No1 No2 No3 No4 Quarter
       2019-01-31 -1.749765 0.342680 1.153036 -0.252436 Q1
       2019-02-28 0.981321 0.514219 0.221180 -1.070043 Q1
       2019-03-31 -0.189496 0.255001 -0.458027 0.435163 Q1
       2019-04-30 -0.583595 0.816847 0.672721 -0.104411 Q2
       2019-05-31 -0.531280 1.029733 -0.438136 -1.118318 Q2
       2019-06-30 1.618982 1.541605 -0.251879 -0.842436 Q2
       2019-07-31 0.184519 0.937082 0.731000 1.361556 Q3
       2019-08-31 -0.326238 0.055676 0.222400 -1.443217 Q3
       2019-09-30 -0.756352 0.816454 0.750445 -0.455947 Q3
```

The following code groups by the Quarter column and outputs statistics for the single groups:

```
In [66]: groups = df.groupby('Quarter')
In [67]: groups.size()
Out[67]: Quarter
       Q1 3
       Q2 3
       Q3 3
       dtype: int64
In [68]: groups.mean()
Out[68]: No1 No2 No3 No4
       Quarter
       Q1 -0.319314 0.370634 0.305396 -0.295772
       Q2 0.168035 1.129395 -0.005765 -0.688388
       Q3 -0.299357 0.603071 0.567948 -0.179203
In [69]: groups.max()
Out[69]: No1 No2 No3 No4
       Quarter
       Q1 0.981321 0.514219 1.153036 0.435163
       Q2 1.618982 1.541605 0.672721 -0.104411
       Q3 0.184519 0.937082 0.750445 1.361556
In [70]: groups.aggregate([min, max]).round(2)
Out[70]: No1 No2 No3 No4
               min max min max min max min max
       Quarter
       Q1 -1.75 0.98 0.26 0.51 -0.46 1.15 -1.07 0.44
```

Q2 -0.58 1.62 0.82 1.54 -0.44 0.67 -1.12 -0.10 Q3 -0.76 0.18 0.06 0.94 0.22 0.75 -1.44 1.36

Groups according to the Quarter column.

Gives the number of rows in each group.

Gives the mean per column.

Gives the maximum value per column.

Gives both the minimum and maximum values per column.

Grouping can also be done with multiple columns. To this end, another column, indicating whether the month of the index date is odd or even, is introduced:

```
In [71]: df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
                      'Odd', 'Even', 'Odd']
In [72]: groups = df.groupby(['Quarter', 'Odd_Even'])
In [73]: groups.size()
Out[73]: Quarter Odd_Even
       Q1 Even 1
              Odd 2
       Q2 Even 2
              Odd 1
       Q3 Even 1
              Odd 2
       dtype: int64
In [74]: groups[['No1', 'No4']].aggregate([sum, np.mean])
Out[74]: No1 No4
                         sum mean sum mean
       Quarter Odd_Even
       Q1 Even 0.981321 0.981321 -1.070043 -1.070043
             Odd -1.939261 -0.969631 0.182727 0.091364
       Q2 Even 1.035387 0.517693 -0.946847 -0.473423
             Odd -0.531280 -0.531280 -1.118318 -1.118318
       Q3 Even -0.326238 -0.326238 -1.443217 -1.443217
             Odd -0.571834 -0.285917 0.905609 0.452805
```

This concludes the introduction to pandas and the use of DataFrame objects. Subsequent chapters apply this tool set to real financial data sets.

# **Complex Selection**

Often, data selection is accomplished by formulation of conditions on column values, and potentially combining multiple such conditions logically. Consider the following data set:

```
In [75]: data = np.random.standard_normal((10, 2))
In [76]: df = pd.DataFrame(data, columns=['x', 'y'])
In [77]: df.info()
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 10 entries, 0 to 9
        Data columns (total 2 columns):
        x 10 non-null float64
        y 10 non-null float64
        dtypes: float64(2)
        memory usage: 240.0 bytes
In [78]: df.head()
Out[78]: x y
        0 1.189622 -1.690617
        1 -1.356399 -1.232435
        2 -0.544439 -0.668172
        3 0.007315 -0.612939
        4 1.299748 -1.733096
In [79]: df.tail()
Out[79]: x y
        5 -0.983310 0.357508
        6 -1.613579 1.470714
        7 -1.188018 -0.549746
        8 -0.940046 -0.827932
        9 0.108863 0.507810
```

ndarray object with standard normally distributed random numbers.

DataFrame object with the same random numbers.

The first five rows via the head() method.

The final five rows via the tail() method.

The following code illustrates the application of Python's comparison operators and logical operators on values in the two columns:

```
In [80]: df['x'] > 0.5
Out[80]: 0 True
       1 False
       2 False
       3 False
       4 True
       5 False
       6 False
       7 False
       8 False
       9 False
       Name: x, dtype: bool
In [81]: (df['x'] > 0) & (df['y'] < 0)
Out[81]: 0 True
       1 False
       2 False
       3 True
       4 True
       5 False
       6 False
       7 False
       8 False
       9 False
       dtype: bool
In [82]: (df['x'] > 0) | (df['y'] < 0)
Out[82]: 0 True
       1 True
       2 True
       3 True
       4 True
       5 False
       6 False
       7 True
       8 True
       9 True
       dtype: bool
```

Check whether value in column x is greater than 0.5.

Check whether value in column x is positive *and* value in column y is negative.

Check whether value in column x is positive *or* value in column y is negative.

Using the resulting Boolean Series objects, complex data (row) selection is straightforward. Alternatively, one can use the query() method and pass the conditions as str objects:

```
In [83]: df[df['x'] > 0]
Out[83]: x y
       0 1.189622 -1.690617
       3 0.007315 -0.612939
       4 1.299748 -1.733096
       9 0.108863 0.507810
In [84]: df.query('x > 0')
Out[84]: x y
       0 1.189622 -1.690617
       3 0.007315 -0.612939
       4 1.299748 -1.733096
       9 0.108863 0.507810
In [85]: df[(df['x'] > 0) & (df['y'] < 0)]
Out[85]: x y
       0 1.189622 -1.690617
       3 0.007315 -0.612939
       4 1.299748 -1.733096
In [86]: df.query('x > 0 & y < 0')
Out[86]: x y
       0 1.189622 -1.690617
       3 0.007315 -0.612939
       4 1.299748 -1.733096
In [87]: df[(df.x > 0) | (df.y < 0)]
Out[87]: x y
       0 1.189622 -1.690617
       1 -1.356399 -1.232435
       2 -0.544439 -0.668172
       3 0.007315 -0.612939
       4 1.299748 -1.733096
       7 -1.188018 -0.549746
       8 -0.940046 -0.827932
       9 0.108863 0.507810
```

All rows for which the value in column x is greater than 0.5.

All rows for which the value in column x is positive *and* the value in column y is negative.

All rows for which the value in column x is positive *or* the value in column y is negative (columns are accessed here via the respective attributes).

Comparison operators can also be applied to complete DataFrame objects at once:

In [88]: df > 0 Out[88]: x y 0 True False 1 False False

 False False True False True False False True False True False False False False True True In [89]: df[df > 0] Out[89]: x y 1.189622 NaN NaN NaN NaN NaN 0.007315 NaN 1.299748 NaN NaN 0.357508 NaN 1.470714 NaN NaN NaN NaN 0.108863 0.507810

Which values in the DataFrame object are positive?

Select all such values and put a NaN in all other places.

# **Concatenation, Joining, and Merging**

This section walks through different approaches to combine two simple data sets in the form of DataFrame objects. The two simple data sets are:

```
In [90]: df1 = pd.DataFrame(['100', '200', '300', '400'],
                            index=['a', 'b', 'c', 'd'],
                            columns=['A',])
In [91]: df1
Out[91]: A
        a 100
        b 200
        c 300
        d 400
In [92]: df2 = pd.DataFrame(['200', '150', '50'],
                            index=['f', 'b', 'd'],
                            columns=['B',])
In [93]: df2
Out[93]: B
        f 200
        b 150
        d 50
```

### **Concatenation**

*Concatenation* or *appending* basically means that rows are added from one DataFrame object to another one. This can be accomplished via the append() method or via the pd.concat() function. A major consideration is how the index values are handled: In [94]: df1.append(df2, sort=False) Out[94]: A B a 100 NaN b 200 NaN c 300 NaN d 400 NaN f NaN 200 b NaN 150 d NaN 50 In [95]: df1.append(df2, ignore\_index=True, sort=False) Out[95]: A B 0 100 NaN 1 200 NaN 2 300 NaN 3 400 NaN 4 NaN 200 5 NaN 150 6 NaN 50 In [96]: pd.concat((df1, df2), sort=False) Out[96]: A B a 100 NaN b 200 NaN c 300 NaN d 400 NaN f NaN 200 b NaN 150 d NaN 50 In [97]: pd.concat((df1, df2), ignore\_index=True, sort=False) Out[97]: A B 0 100 NaN 1 200 NaN 2 300 NaN 3 400 NaN 4 NaN 200 5 NaN 150 6 NaN 50

Appends data from df2 to df1 as new rows.

Does the same but ignores the indices.

Has the same effect as the first append operation.

Has the same effect as the second append operation.

### **Joining**

When joining the two data sets, the sequence of the DataFrame objects also matters but in a different way. Only the index values from the first DataFrame object are used. This default behavior is called a *left join*:

```
In [98]: df1.join(df2)
Out[98]: A B
       a 100 NaN
       b 200 150
       c 300 NaN
       d 400 50
In [99]: df2.join(df1)
Out[99]: B A
       f 200 NaN
       b 150 200
       d 50 400
```

Index values of df1 are relevant.

Index values of df2 are relevant.

There are a total of four different join methods available, each leading to a different behavior with regard to how index values and the corresponding data rows are handled:

```
In [100]: df1.join(df2, how='left')
Out[100]: A B
        a 100 NaN
        b 200 150
        c 300 NaN
        d 400 50
In [101]: df1.join(df2, how='right')
Out[101]: A B
        f NaN 200
        b 200 150
        d 400 50
In [102]: df1.join(df2, how='inner')
Out[102]: A B
        b 200 150
        d 400 50
In [103]: df1.join(df2, how='outer')
Out[103]: A B
        a 100 NaN
```

| b | 200 | 150 |
|---|-----|-----|
| c | 300 | NaN |
| d | 400 | 50  |
| f | NaN | 200 |

Left join is the default operation.

Right join is the same as reversing the sequence of the DataFrame objects.

Inner join only preserves those index values found in both indices.

Outer join preserves all index values from both indices.

A join can also happen based on an empty DataFrame object. In this case, the columns are created *sequentially*, leading to behavior similar to a left join:

```
In [104]: df = pd.DataFrame()
In [105]: df['A'] = df1['A']
In [106]: df
Out[106]: A
         a 100
         b 200
         c 300
         d 400
In [107]: df['B'] = df2
In [108]: df
Out[108]: A B
         a 100 NaN
         b 200 150
         c 300 NaN
         d 400 50
```

df1 as first column A.

df2 as second column B.

Making use of a dictionary to combine the data sets yields a result similar to an outer join since the columns are created *simultaneously*:

In [109]: df = pd.DataFrame({'A': df1['A'], 'B': df2['B']})

| In [110]: df |   |     |     |
|--------------|---|-----|-----|
| Out[110]:    |   | A   | B   |
|              | a | 100 | NaN |
|              | b | 200 | 150 |
|              | c | 300 | NaN |
|              | d | 400 | 50  |
|              | f | NaN | 200 |
|              |   |     |     |

The columns of the DataFrame objects are used as values in the dict object.

### **Merging**

While a join operation takes place based on the indices of the DataFrame objects to be joined, a merge operation typically takes place on a column shared between the two data sets. To this end, a new column C is added to both original DataFrame objects:

```
In [111]: c = pd.Series([250, 150, 50], index=['b', 'd', 'c'])
        df1['C'] = c
        df2['C'] = c
In [112]: df1
Out[112]: A C
        a 100 NaN
        b 200 250.0
        c 300 50.0
        d 400 150.0
In [113]: df2
Out[113]: B C
        f 200 NaN
        b 150 250.0
        d 50 150.0
```

By default, the merge operation in this case takes place based on the single shared column C. Other options are available, however, such as an *outer* merge:

```
In [114]: pd.merge(df1, df2)
Out[114]: A C B
        0 100 NaN 200
        1 200 250.0 150
        2 400 150.0 50
In [115]: pd.merge(df1, df2, on='C')
Out[115]: A C B
        0 100 NaN 200
        1 200 250.0 150
        2 400 150.0 50
In [116]: pd.merge(df1, df2, how='outer')
Out[116]: A C B
        0 100 NaN 200
        1 200 250.0 150
        2 300 50.0 NaN
        3 400 150.0 50
```

The default merge on column C.

An outer merge is also possible, preserving all data rows.

An outer merge is also possible, preserving all data rows.

Many more types of merge operations are available, a few of which are illustrated in the following code:

```
In [117]: pd.merge(df1, df2, left_on='A', right_on='B')
Out[117]: A C_x B C_y
        0 200 250.0 200 NaN
In [118]: pd.merge(df1, df2, left_on='A', right_on='B', how='outer')
Out[118]: A C_x B C_y
        0 100 NaN NaN NaN
        1 200 250.0 200 NaN
        2 300 50.0 NaN NaN
        3 400 150.0 NaN NaN
        4 NaN NaN 150 250.0
        5 NaN NaN 50 150.0
In [119]: pd.merge(df1, df2, left_index=True, right_index=True)
Out[119]: A C_x B C_y
        b 200 250.0 150 250.0
        d 400 150.0 50 150.0
In [120]: pd.merge(df1, df2, on='C', left_index=True)
Out[120]: A C B
        f 100 NaN 200
        b 200 250.0 150
        d 400 150.0 50
In [121]: pd.merge(df1, df2, on='C', right_index=True)
Out[121]: A C B
        a 100 NaN 200
        b 200 250.0 150
        d 400 150.0 50
In [122]: pd.merge(df1, df2, on='C', left_index=True, right_index=True)
Out[122]: A C B
        b 200 250.0 150
        d 400 150.0 50
```

# **Performance Aspects**

Many examples in this chapter illustrate that there are often multiple options to achieve the same goal with pandas. This section compares such options for adding up two columns element-wise. First, the data set, generated with NumPy:

```
In [123]: data = np.random.standard_normal((1000000, 2))
In [124]: data.nbytes
Out[124]: 16000000
In [125]: df = pd.DataFrame(data, columns=['x', 'y'])
In [126]: df.info()
          <class 'pandas.core.frame.DataFrame'>
          RangeIndex: 1000000 entries, 0 to 999999
          Data columns (total 2 columns):
          x 1000000 non-null float64
          y 1000000 non-null float64
          dtypes: float64(2)
          memory usage: 15.3 MB
```

The ndarray object with random numbers.

The DataFrame object with the random numbers.

Second, some options to accomplish the task at hand with performance values:

```
In [127]: %time res = df['x'] + df['y']
         CPU times: user 7.35 ms, sys: 7.43 ms, total: 14.8 ms
         Wall time: 7.48 ms
In [128]: res[:3]
Out[128]: 0 0.387242
         1 -0.969343
         2 -0.863159
         dtype: float64
In [129]: %time res = df.sum(axis=1)
         CPU times: user 130 ms, sys: 30.6 ms, total: 161 ms
         Wall time: 101 ms
In [130]: res[:3]
Out[130]: 0 0.387242
         1 -0.969343
         2 -0.863159
         dtype: float64
In [131]: %time res = df.values.sum(axis=1)
```

```
CPU times: user 50.3 ms, sys: 2.75 ms, total: 53.1 ms
          Wall time: 27.9 ms
In [132]: res[:3]
Out[132]: array([ 0.3872424 , -0.96934273, -0.86315944])
In [133]: %time res = np.sum(df, axis=1)
          CPU times: user 127 ms, sys: 15.1 ms, total: 142 ms
          Wall time: 73.7 ms
In [134]: res[:3]
Out[134]: 0 0.387242
          1 -0.969343
          2 -0.863159
          dtype: float64
In [135]: %time res = np.sum(df.values, axis=1)
          CPU times: user 49.3 ms, sys: 2.36 ms, total: 51.7 ms
          Wall time: 26.9 ms
In [136]: res[:3]
Out[136]: array([ 0.3872424 , -0.96934273, -0.86315944])
```

Working with the columns (Series objects) directly is the fastest approach.

This calculates the sums by calling the sum() method on the DataFrame object.

This calculates the sums by calling the sum() method on the ndarray object.

This calculates the sums by using the function np.sum() on the DataFrame object.

This calculates the sums by using the function np.sum() on the ndarray object.

Finally, two more options which are based on the methods eval() and apply(), respectively: 1

```
In [137]: %time res = df.eval('x + y')
         CPU times: user 25.5 ms, sys: 17.7 ms, total: 43.2 ms
         Wall time: 22.5 ms
In [138]: res[:3]
Out[138]: 0 0.387242
         1 -0.969343
```

```
2 -0.863159
         dtype: float64
In [139]: %time res = df.apply(lambda row: row['x'] + row['y'], axis=1)
         CPU times: user 19.6 s, sys: 83.3 ms, total: 19.7 s
         Wall time: 19.9 s
In [140]: res[:3]
Out[140]: 0 0.387242
         1 -0.969343
         2 -0.863159
         dtype: float64
```

eval() is a method dedicated to evaluation of (complex) numerical expressions; columns can be directly addressed.

The slowest option is to use the apply() method row-by-row; this is like looping on the Python level over all rows.

### **CHOOSE WISELY**

pandas often provides multiple options to accomplish the same goal. If unsure of which to use, compare the options to verify that the best possible performance is achieved when time is critical. In this simple example, execution times differ by orders of magnitude.

# **Conclusion**

pandas is a powerful tool for data analysis and has become the central package in the so-called *PyData* stack. Its DataFrame class is particularly suited to working with tabular data of any kind. Most operations on such objects are vectorized, leading not only — as in the NumPy case — to concise code but also to high performance in general. In addition, pandas makes working with incomplete data sets convenient (which is not the case with NumPy, for instance). pandas and the DataFrame class will be central in many later chapters of the book, where additional features will be used and introduced when necessary.
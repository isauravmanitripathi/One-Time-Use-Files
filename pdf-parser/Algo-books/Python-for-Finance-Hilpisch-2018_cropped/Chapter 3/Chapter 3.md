# **Chapter 3. Data Types and Structures**

Bad programmers worry about the code. Good programmers worry about data structures and their relationships. Linus Torvalds

This chapter introduces the basic data types and data structures of Python, and is organized as follows: "Basic Data Types"

The first section introduces basic data types such as int, float, bool, and str.

*"Basic Data Structures"*

The second section introduces the fundamental data structures of Python (e.g., list objects) and illustrates, among other things, control structures, functional programming approaches, and anonymous functions.

The aim of this chapter is to provide a general introduction to Python specifics when it comes to data types and structures. The reader equipped with a background from another programing language, say C or Matlab, should be able to easily grasp the differences that Python usage might bring along. The topics and idioms introduced here are important and fundamental for the chapters to come.

| Object<br>type                  | Meaning                  | Used<br>for                              |  |
|---------------------------------|--------------------------|------------------------------------------|--|
| int                             | Integer<br>value         | Natural<br>numbers                       |  |
| float                           | Floating-point<br>number | Real<br>numbers                          |  |
| bool                            | Boolean<br>value         | Something<br>true<br>or<br>false         |  |
| String<br>object<br>str         |                          | Character,<br>word,<br>text              |  |
| Immutable<br>container<br>tuple |                          | Fixed<br>set<br>of<br>objects,<br>record |  |
| list                            | Mutable<br>container     | Changing<br>set<br>of<br>objects         |  |

The chapter covers the following data types and structures:

| list | Mutable<br>container | Changing<br>set<br>of<br>objects      |
|------|----------------------|---------------------------------------|
| dict | Mutable<br>container | Key-value<br>store                    |
| set  | Mutable<br>container | Collection<br>of<br>unique<br>objects |

# **Basic Data Types**

Python is a *dynamically typed* language, which means that the Python interpreter infers the type of an object at runtime. In comparison, compiled languages like C are generally *statically typed*. In these cases, the type of an object has to be specified for the object before compile time. 1

### **Integers**

One of the most fundamental data types is the integer, or int:

```
In [1]: a = 10
        type(a)
Out[1]: int
```

The built-in function type provides type information for all objects with standard and built-in types as well as for newly created classes and objects. In the latter case, the information provided depends on the description the programmer has stored with the class. There is a saying that "everything in Python is an object." This means, for example, that even simple objects like the int object just defined have built-in methods. For example, one can get the number of bits needed to represent the int object in memory by calling the method bit\_length():

```
In [2]: a.bit_length()
Out[2]: 4
```

The number of bits needed increases the higher the integer value is that one assigns to the object:

```
In [3]: a = 100000
        a.bit_length()
Out[3]: 17
```

In general, there are so many different methods that it is hard to memorize all methods of all classes and objects. Advanced Python environments like IPython provide tab completion capabilities that show all the methods attached to an object. You simply type the object name followed by a dot (e.g., a.) and then press the Tab key. This then provides a collection of methods you can call on the object. Alternatively, the Python built-in function dir gives a complete list of the attributes and methods of any object.

A specialty of Python is that integers can be arbitrarily large. Consider, for example, the googol number . Python has no problem with such large numbers:

- In [4]: googol = 10 \*\* 100
- googol
- Out[4]: 10000000000000000000000000000000000000000000000000000000000000000000000000 000000000000000000000000000
- In [5]: googol.bit\_length()

Out[5]: 333

### **LARGE INTEGERS**

Python integers can be arbitrarily large. The interpreter simply uses as many bits/bytes as needed to represent the numbers.

Arithmetic operations on integers are also easy to implement:

In [6]: 1 + 4 Out[6]: 5 In [7]: 1 / 4 Out[7]: 0.25 In [8]: type(1 / 4) Out[8]: float

### **Floats**

The last expression returns the mathematically correct result of 0.25, <sup>2</sup> which gives rise to the next basic data type, the float. Adding a dot to an integer value, like in 1. or 1.0, causes Python to interpret the object as a float. Expressions involving a float also return a float object in general: 3

```
In [9]: 1.6 / 4
Out[9]: 0.4
In [10]: type (1.6 / 4)
Out[10]: float
```

A float is a bit more involved in that the computerized representation of rational or real numbers is in general not exact and depends on the specific technical approach taken. To illustrate what this implies, let us define another float object, b. float objects like this one are always represented internally up to a certain degree of accuracy only. This becomes evident when adding 0.1 to b:

```
In [11]: b = 0.35
         type(b)
Out[11]: float
In [12]: b + 0.1
Out[12]: 0.44999999999999996
```

The reason for this is that float objects are internally represented in binary format; that is, a decimal number 0 < *n* < 1 is represented by a series of the form . For certain floating-point numbers the binary representation might involve a large number of elements or might even be an infinite series. However, given a fixed number of bits used to represent such a number — i.e., a fixed number of terms in the representation series inaccuracies are the consequence. Other numbers can be represented *perfectly* and are therefore stored exactly even with a finite number of bits available. Consider the following example:

```
In [13]: c = 0.5
         c.as_integer_ratio()
Out[13]: (1, 2)
```

One-half, i.e., 0.5, is stored exactly because it has an exact (finite) binary representation as . However, for b = 0.35 one gets something different than the expected rational number :

In [14]: b.as\_integer\_ratio() Out[14]: (3152519739159347, 9007199254740992)

The precision is dependent on the number of bits used to represent the number. In general, all platforms that Python runs on use the IEEE 754 [double-precision](http://bit.ly/2S0un95) standard — i.e., 64 bits — for internal representation. This translates into a 15 digit relative accuracy.

Since this topic is of high importance for several application areas in finance, it is sometimes necessary to ensure the exact, or at least best possible, representation of numbers. For example, the issue can be of importance when summing over a large set of numbers. In such a situation, a certain kind and/or magnitude of representation error might, in aggregate, lead to significant deviations from a benchmark value.

The module decimal provides an arbitrary-precision object for floating-point numbers and several options to address precision issues when working with such numbers:

```
In [15]: import decimal
         from decimal import Decimal
In [16]: decimal.getcontext()
Out[16]: Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
          capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero,
          Overflow])
In [17]: d = Decimal(1) / Decimal (11)
         d
Out[17]: Decimal('0.09090909090909090909090909091')
```

One can change the precision of the representation by changing the respective attribute value of the Context object:

```
In [18]: decimal.getcontext().prec = 4
In [19]: e = Decimal(1) / Decimal (11)
         e
Out[19]: Decimal('0.09091')
```

```
In [20]: decimal.getcontext().prec = 50
In [21]: f = Decimal(1) / Decimal (11)
         f
Out[21]: Decimal('0.090909090909090909090909090909090909090909090909091')
```

Lower precision than default.

Higher precision than default.

If needed, the precision can in this way be adjusted to the exact problem at hand and one can operate with floating-point objects that exhibit different degrees of accuracy:

```
In [22]: g = d + e + f
         g
Out[22]: Decimal('0.27272818181818181818181818181909090909090909090909')
```

### **ARBITRARY-PRECISION FLOATS**

The module decimal provides an arbitrary-precision floating-point number object. In finance, it might sometimes be necessary to ensure high precision and to go beyond the 64-bit doubleprecision standard.

### **Booleans**

In programming, evaluating a comparison or logical expression (such as 4 > 3, 4.5 <= 3.25 or (4 > 3) and (3 > 2)) yields one of True or False as output, two important Python keywords. Others are, for example, def, for, and if. A complete list of Python keywords is available in the keyword module:

```
In [23]: import keyword
In [24]: keyword.kwlist
Out[24]: ['False',
           'None',
           'True',
           'and',
           'as',
           'assert',
           'async',
           'await',
           'break',
           'class',
           'continue',
           'def',
           'del',
           'elif',
           'else',
           'except',
           'finally',
           'for',
           'from',
           'global',
           'if',
           'import',
           'in',
           'is',
           'lambda',
           'nonlocal',
           'not',
           'or',
           'pass',
           'raise',
           'return',
           'try',
           'while',
           'with',
           'yield']
```

True and False are of data type bool, standing for *Boolean value*. The following code shows Python's *comparison* operators applied to the same operands with the resulting bool objects:

In [25]: 4 > 3 Out[25]: True

In [26]: type(4 > 3) Out[26]: bool In [27]: type(False) Out[27]: bool In [28]: 4 >= 3 Out[28]: True In [29]: 4 < 3 Out[29]: False In [30]: 4 <= 3 Out[30]: False In [31]: 4 == 3 Out[31]: False In [32]: 4 != 3 Out[32]: True

Is greater.

Is greater or equal.

Is smaller.

Is smaller or equal.

Is equal.

Is not equal.

Often, *logical* operators are applied on bool objects, which in turn yields another bool object:

In [33]: True **and** True Out[33]: True In [34]: True **and** False Out[34]: False In [35]: False **and** False Out[35]: False In [36]: True **or** True

```
Out[36]: True
In [37]: True or False
Out[37]: True
In [38]: False or False
Out[38]: False
In [39]: not True
Out[39]: False
In [40]: not False
Out[40]: True
```

Of course, both types of operators are often combined:

```
In [41]: (4 > 3) and (2 > 3)
Out[41]: False
In [42]: (4 == 3) or (2 != 3)
Out[42]: True
In [43]: not (4 != 4)
Out[43]: True
In [44]: (not (4 != 4)) and (2 == 3)
Out[44]: False
```

One major application area is to control the code flow via other Python keywords, such as if or while (more examples later in the chapter):

```
In [45]: if 4 > 3:
             print('condition true')
         condition true
In [46]: i = 0
         while i < 4:
             print('condition true, i = ', i)
             i += 1
         condition true, i = 0
         condition true, i = 1
         condition true, i = 2
         condition true, i = 3
```

If condition holds true, execute code to follow.

The code to be executed if condition holds true.

Initializes the parameter i with 0.

As long as the condition holds true, execute and repeat the code to follow.

Prints a text and the value of parameter i.

Increases the parameter value by 1; i += 1 is the same as i = i + 1.

Numerically, Python attaches a value of 0 to False and a value of 1 to True. When transforming numbers to bool objects via the bool() function, a 0 gives False while all other numbers give True:

```
In [47]: int(True)
Out[47]: 1
In [48]: int(False)
Out[48]: 0
In [49]: float(True)
Out[49]: 1.0
In [50]: float(False)
Out[50]: 0.0
In [51]: bool(0)
Out[51]: False
In [52]: bool(0.0)
Out[52]: False
In [53]: bool(1)
Out[53]: True
In [54]: bool(10.5)
Out[54]: True
In [55]: bool(-2)
Out[55]: True
```

### **Strings**

Now that natural and floating-point numbers can be represented, this subsection turns to text. The basic data type to represent text in Python is str. The str object has a number of helpful built-in methods. In fact, Python is generally considered to be a good choice when it comes to working with texts and text files of any kind and any size. A str object is generally defined by single or double quotation marks or by converting another object using the str() function (i.e., using the object's standard or user-defined str representation): In [56]: t = 'this is a string object'

With regard to the built-in methods, you can, for example, capitalize the first word in this object: In [57]: t.capitalize() Out[57]: 'This is a string object'

Or you can split it into its single-word components to get a list object of all the words (more on list objects later): In [58]: t.split() Out[58]: ['this', 'is', 'a', 'string', 'object']

You can also search for a word and get the position (i.e., index value) of the first letter of the word back in a successful case: In [59]: t.find('string') Out[59]: 10

If the word is not in the str object, the method returns -1: In [60]: t.find('Python') Out[60]: -1

Replacing characters in a string is a typical task that is easily accomplished with the replace() method: In [61]: t.replace(' ', '|') Out[61]: 'this|is|a|string|object'

The stripping of strings — i.e., deletion of certain leading/lagging characters is also often necessary: In [62]: 'http://www.python.org'.strip('htp:/') Out[62]: 'www.python.org'

Table 3-1 lists a number of helpful methods of the str object.

*Table 3-1. Selected string methods*

| Method<br>Arguments<br>Returns/result |
|---------------------------------------|
|---------------------------------------|

| capitalize () |                            | Copy<br>of<br>the<br>string<br>with<br>first<br>letter<br>capitalized                   |
|---------------|----------------------------|-----------------------------------------------------------------------------------------|
| count         | (sub[, start[, end]])      | Count<br>of<br>the<br>number<br>of<br>occurrences<br>of<br>substring                    |
| decode        | ([encoding[, errors]])     | Decoded<br>version<br>of<br>the<br>string,<br>using<br>encoding (e.g.,<br>UTF-8)        |
| encode        | ([encoding+[,<br>errors]]) | Encoded<br>version<br>of<br>the<br>string                                               |
| find          | (sub[, start[, end]])      | (Lowest)<br>index<br>where<br>substring<br>is<br>found                                  |
| join          | (seq)                      | Concatenation<br>of<br>strings<br>in<br>sequence<br>seq                                 |
| replace       | (old, new[, count])        | Replaces<br>old by<br>new the<br>first<br>count times                                   |
| split         | ([sep[, maxsplit]])        | List<br>of<br>words<br>in<br>string<br>with<br>sep as<br>separator                      |
|               | splitlines ([keepends])    | Separated<br>lines<br>with<br>line<br>ends/breaks<br>if<br>keepends is<br>True          |
| strip         | (chars)                    | Copy<br>of<br>string<br>with<br>leading/lagging<br>characters<br>in<br>chars<br>removed |
| upper         | ()                         | Copy<br>with<br>all<br>letters<br>capitalized                                           |

### **UNICODE STRINGS**

A fundamental change from Python 2.7 (used for the first edition of the book) to Python 3.7 (used for this second edition) is the encoding and decoding of string objects and the introduction of [Unicode.](http://bit.ly/1x41ytu) This chapter does not go into the many details important in this context; for the purposes of this book, which mainly deals with numerical data and standard strings containing English words, this omission seems justified.

### **Excursion: Printing and String Replacements**

Printing str objects or string representations of other Python objects is usually accomplished by the print() function:

```
In [63]: print('Python for Finance')
         Python for Finance
In [64]: print(t)
         this is a string object
In [65]: i = 0
         while i < 4:
             print(i)
             i += 1
         0
         1
         2
         3
In [66]: i = 0
         while i < 4:
             print(i, end='|')
             i += 1
         0|1|2|3|
```

Prints a str object.

Prints a str object referenced by a variable name.

Prints the string representation of an int object.

Specifies the final character(s) when printing; default is a line break (\n) as seen before.

Python offers powerful string replacement operations. There is the old way, via the % character, and the new way, via curly braces ({}) and format(). Both are still applied in practice. This section cannot provide an exhaustive illustration of all options, but the following code snippets show some important ones. First, the *old* way of doing it:

In [67]: 'this is an integer %d' % 15 Out[67]: 'this is an integer 15'

In [68]: 'this is an integer %4d' % 15 Out[68]: 'this is an integer 15' In [69]: 'this is an integer %04d' % 15 Out[69]: 'this is an integer 0015' In [70]: 'this is a float %f' % 15.3456 Out[70]: 'this is a float 15.345600' In [71]: 'this is a float %.2f' % 15.3456 Out[71]: 'this is a float 15.35' In [72]: 'this is a float %8f' % 15.3456 Out[72]: 'this is a float 15.345600' In [73]: 'this is a float %8.2f' % 15.3456 Out[73]: 'this is a float 15.35' In [74]: 'this is a float %08.2f' % 15.3456 Out[74]: 'this is a float 00015.35' In [75]: 'this is a string %s' % 'Python' Out[75]: 'this is a string Python' In [76]: 'this is a string %10s' % 'Python' Out[76]: 'this is a string Python'

int object replacement.

With fixed number of characters.

With leading zeros if necessary.

float object replacement.

With fixed number of decimals.

With fixed number of characters (and filled-up decimals).

With fixed number of characters and decimals …

… and leading zeros if necessary.

str object replacement.

With fixed number of characters.

Now, here are the same examples implemented in the *new* way. Notice the slight differences in the output in some places:

```
In [77]: 'this is an integer {:d}'.format(15)
Out[77]: 'this is an integer 15'
In [78]: 'this is an integer {:4d}'.format(15)
Out[78]: 'this is an integer 15'
In [79]: 'this is an integer {:04d}'.format(15)
Out[79]: 'this is an integer 0015'
In [80]: 'this is a float {:f}'.format(15.3456)
Out[80]: 'this is a float 15.345600'
In [81]: 'this is a float {:.2f}'.format(15.3456)
Out[81]: 'this is a float 15.35'
In [82]: 'this is a float {:8f}'.format(15.3456)
Out[82]: 'this is a float 15.345600'
In [83]: 'this is a float {:8.2f}'.format(15.3456)
Out[83]: 'this is a float 15.35'
In [84]: 'this is a float {:08.2f}'.format(15.3456)
Out[84]: 'this is a float 00015.35'
In [85]: 'this is a string {:s}'.format('Python')
Out[85]: 'this is a string Python'
In [86]: 'this is a string {:10s}'.format('Python')
Out[86]: 'this is a string Python '
```

String replacements are particularly useful in the context of multiple printing operations where the printed data is updated, for instance, during a while loop:

```
In [87]: i = 0
         while i < 4:
             print('the number is %d' % i)
             i += 1
         the number is 0
         the number is 1
         the number is 2
         the number is 3
In [88]: i = 0
         while i < 4:
             print('the number is {:d}'.format(i))
             i += 1
         the number is 0
         the number is 1
         the number is 2
```

the number  $\textbf{is } 3$ 

### **Excursion: Regular Expressions**

A powerful tool when working with str objects is *regular expressions*. Python provides such functionality in the module re:

```
In [89]: import re
```

Suppose a financial analyst is faced with a large text file, such as a CSV file, which contains certain time series and respective datetime information. More often than not, this information is delivered in a format that Python cannot interpret directly. However, the datetime information can generally be described by a regular expression. Consider the following str object, containing three datetime elements, three integers, and three strings. Note that triple quotation marks allow the definition of str objects over multiple rows:

```
In [90]: series = """
         '01/18/2014 13:00:00', 100, '1st';
         '01/18/2014 13:30:00', 110, '2nd';
         '01/18/2014 14:00:00', 120, '3rd'
         """
```

The following regular expression describes the format of the datetime information provided in the str object: 4

```
In [91]: dt = re.compile("'[0-9/:\s]+'") # datetime
```

Equipped with this regular expression, one can go on and find all the datetime elements. In general, applying regular expressions to str objects also leads to performance improvements for typical parsing tasks:

```
In [92]: result = dt.findall(series)
         result
Out[92]: ["'01/18/2014 13:00:00'", "'01/18/2014 13:30:00'", "'01/18/2014
          14:00:00'"]
```

### **REGULAR EXPRESSIONS**

When parsing str objects, consider using regular expressions, which can bring both convenience and performance to such operations.

The resulting str objects can then be parsed to generate Python datetime objects (see Appendix A for an overview of handling date and time data with Python). To parse the str objects containing the datetime information, one needs to provide information of how to parse them — again as a str object:

```
In [93]: from datetime import datetime
         pydt = datetime.strptime(result[0].replace("'", ""),
                                   '%m/%d/%Y %H:%M:%S')
         pydt
Out[93]: datetime.datetime(2014, 1, 18, 13, 0)
In [94]: print(pydt)
         2014-01-18 13:00:00
In [95]: print(type(pydt))
         <class 'datetime.datetime'>
```

Later chapters provide more information on datetime data, the handling of such data, and datetime objects and their methods. This is just meant to be a teaser for this important topic in finance.

# **Basic Data Structures**

As a general rule, data structures are objects that contain a possibly large number of other objects. Among those that Python provides as built-in structures are: tuple

An immutable collection of arbitrary objects; only a few methods available

*list*

A mutable collection of arbitrary objects; many methods available

*dict*

A key-value store object

*set*

An unordered collection object for other *unique* objects

### **Tuples**

A tuple is an advanced data structure, yet it's still quite simple and limited in its applications. It is defined by providing objects in parentheses:

```
In [96]: t = (1, 2.5, 'data')
         type(t)
Out[96]: tuple
```

You can even drop the parentheses and provide multiple objects, just separated by commas:

```
In [97]: t = 1, 2.5, 'data'
         type(t)
Out[97]: tuple
```

Like almost all data structures in Python the tuple has a built-in index, with the help of which you can retrieve single or multiple elements of the tuple. It is important to remember that Python uses *zero-based numbering*, such that the third element of a tuple is at index position 2:

```
In [98]: t[2]
Out[98]: 'data'
In [99]: type(t[2])
Out[99]: str
```

### **ZERO-BASED NUMBERING**

In contrast to some other programming languages like Matlab, Python uses zero-based numbering schemes. For example, the first element of a tuple object has index value 0.

There are only two special methods that this object type provides: count() and index(). The first counts the number of occurrences of a certain object and the second gives the index value of the first appearance of it:

```
In [100]: t.count('data')
Out[100]: 1
In [101]: t.index(1)
Out[101]: 0
```

tuple objects are *immutable* objects. This means that they, once defined, cannot be changed easily.

### **Lists**

Objects of type list are much more flexible and powerful in comparison to tuple objects. From a finance point of view, you can achieve a lot working only with list objects, such as storing stock price quotes and appending new data. A list object is defined through brackets and the basic capabilities and behaviors are similar to those of tuple objects:

```
In [102]: l = [1, 2.5, 'data']
          l[2]
Out[102]: 'data'
```

list objects can also be defined or converted by using the function list(). The following code generates a new list object by converting the tuple object from the previous example:

```
In [103]: l = list(t)
          l
Out[103]: [1, 2.5, 'data']
In [104]: type(l)
Out[104]: list
```

In addition to the characteristics of tuple objects, list objects are also expandable and reducible via different methods. In other words, whereas str and tuple objects are *immutable* sequence objects (with indexes) that cannot be changed once created, list objects are *mutable* and can be changed via different operations. You can append list objects to an existing list object, and more:

```
In [105]: l.append([4, 3])
          l
Out[105]: [1, 2.5, 'data', [4, 3]]
In [106]: l.extend([1.0, 1.5, 2.0])
          l
Out[106]: [1, 2.5, 'data', [4, 3], 1.0, 1.5, 2.0]
In [107]: l.insert(1, 'insert')
          l
Out[107]: [1, 'insert', 2.5, 'data', [4, 3], 1.0, 1.5, 2.0]
In [108]: l.remove('data')
          l
Out[108]: [1, 'insert', 2.5, [4, 3], 1.0, 1.5, 2.0]
```

```
In [109]: p = l.pop(3)
          print(l, p)
          [1, 'insert', 2.5, 1.0, 1.5, 2.0] [4, 3]
```

Append list object at the end.

Append elements of the list object.

Insert object before index position.

Remove first occurrence of object.

Remove and return object at index position.

Slicing is also easily accomplished. Here, *slicing* refers to an operation that breaks down a data set into smaller parts (of interest):

In [110]: l[2:5] Out[110]: [2.5, 1.0, 1.5]

Return the third through fifth elements.

[Table](#page-27-0) 3-2 provides a summary of selected operations and methods of the list object.

<span id="page-27-0"></span>

| Method               | Arguments | Returns/result                                                              |
|----------------------|-----------|-----------------------------------------------------------------------------|
| l[i] = x             | [i]       | Replaces<br>i-th<br>element<br>by<br>x                                      |
| l[i:j:k] = s [i:j:k] |           | Replaces<br>every<br>k-th<br>element<br>from<br>i to<br>j –<br>1<br>by<br>s |
| append               | (x)       | Appends<br>x to<br>object                                                   |
| count                | (x)       | Number<br>of<br>occurrences<br>of<br>object<br>x                            |
| del l[i:j:k] [i:j:k] |           | Deletes<br>elements<br>with<br>index<br>values<br>i to<br>j –<br>1          |
| extend               | (s)       | Appends<br>all<br>elements<br>of<br>s to<br>object                          |

*Table 3-2. Selected operations and methods of list objects*

| extend  | (s)                             | Appends<br>all<br>elements<br>of<br>s to<br>object                 |
|---------|---------------------------------|--------------------------------------------------------------------|
| index   | (x[, i[, j]])                   | First<br>index<br>of<br>x between<br>elements<br>i and<br>j –<br>1 |
| insert  | (i, x)                          | Inserts<br>x at/before<br>index<br>i                               |
| remove  | (i)                             | Removes<br>element<br>with<br>index<br>i                           |
| pop     | (i)                             | Removes<br>element<br>with<br>index<br>i and<br>returns<br>it      |
| reverse | ()                              | Reverses<br>all<br>items<br>in<br>place                            |
| sort    | ([cmp[, key[, reverse]]]) Sorts | all<br>items<br>in<br>place                                        |

### **Excursion: Control Structures**

Although a topic in themselves, *control structures* like for loops are maybe best introduced in Python based on list objects. This is due to the fact that looping in general takes place over list objects, which is quite different to what is often the standard in other languages. Take the following example. The for loop loops over the elements of the list object l with index values 2 to 4 and prints the square of the respective elements. Note the importance of the indentation (whitespace) in the second line:

```
In [111]: for element in l[2:5]:
              print(element ** 2)
          6.25
          1.0
          2.25
```

This provides a really high degree of flexibility in comparison to the typical counter-based looping. Counter-based looping is also an option with Python, but is accomplished using the range object:

```
In [112]: r = range(0, 8, 1)
          r
Out[112]: range(0, 8)
In [113]: type(r)
Out[113]: range
```

Parameters are start, end, and step-size.

For comparison, the same loop is implemented using range() as follows:

```
In [114]: for i in range(2, 5):
              print(l[i] ** 2)
          6.25
          1.0
          2.25
```

### **LOOPING OVER LISTS**

In Python you can loop over arbitrary list objects, no matter what the content of the object is. This often avoids the introduction of a counter.

Python also provides the typical (conditional) control elements if, elif, and else. Their use is comparable in other languages:

```
In [115]: for i in range(1, 10):
              if i % 2 == 0:
                  print("%d is even" % i)
              elif i % 3 == 0:
                  print("%d is multiple of 3" % i)
              else:
                  print("%d is odd" % i)
          1 is odd
          2 is even
          3 is multiple of 3
          4 is even
          5 is odd
          6 is even
          7 is odd
          8 is even
          9 is multiple of 3
```

% stands for modulo.

Similarly, while provides another means to control the flow:

```
In [116]: total = 0
          while total < 100:
              total += 1
          print(total)
          100
```

A specialty of Python is so-called *list comprehensions*. Instead of looping over existing list objects, this approach generates list objects via loops in a rather compact fashion:

```
In [117]: m = [i ** 2 for i in range(5)]
          m
Out[117]: [0, 1, 4, 9, 16]
```

In a certain sense, this already provides a first means to generate "something

like" vectorized code in that loops are implicit rather than explicit (vectorization of code is discussed in more detail in Chapters 4 and 5).

### **Excursion: Functional Programming**

Python provides a number of tools for functional programming support as well — i.e., the application of a function to a whole set of inputs (in our case list objects). Among these tools are filter(), map(), and reduce(). However, one needs a function definition first. To start with something really simple, consider a function f() that returns the square of the input x:

```
In [118]: def f(x):
              return x ** 2
          f(2)
Out[118]: 4
```

Of course, functions can be arbitrarily complex, with multiple input/parameter objects and even multiple outputs (return objects). However, consider the following function:

```
In [119]: def even(x):
              return x % 2 == 0
          even(3)
Out[119]: False
```

The return object is a Boolean. Such a function can be applied to a whole list object by using map():

```
In [120]: list(map(even, range(10)))
Out[120]: [True, False, True, False, True, False, True, False, True, False]
```

To this end, one can also provide a function definition directly as an argument to map(), making use of lambda or *anonymous* functions:

```
In [121]: list(map(lambda x: x ** 2, range(10)))
Out[121]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Functions can also be used to filter a list object. In the following example, the filter returns elements of a list object that match the Boolean condition as defined by the even function:

```
In [122]: list(filter(even, range(15)))
Out[122]: [0, 2, 4, 6, 8, 10, 12, 14]
```

### **LIST COMPREHENSIONS, FUNCTIONAL PROGRAMMING, ANONYMOUS FUNCTIONS**

It can be considered good practice to avoid loops on the Python level as far as possible. List comprehensions and functional programming tools like filter(), map(), and reduce() provide means to write code without (explicit) loops that is both compact and in general more readable. lambda or anonymous functions are also powerful tools in this context.

### **Dicts**

dict objects are dictionaries, and also mutable sequences, that allow data retrieval by keys (which can, for example, be str objects). They are so-called *key-value stores*. While list objects are ordered and sortable, dict objects are unordered and not sortable, in general. <sup>5</sup> An example best illustrates further differences to list objects. Curly braces are what define dict objects: In [123]: d = { 'Name' : 'Angela Merkel', 'Country' : 'Germany', 'Profession' : 'Chancelor', 'Age' : 64 } type(d) Out[123]: dict In [124]: **print**(d['Name'], d['Age']) Angela Merkel 64

```
Again, this class of objects has a number of built-in methods: In [125]:
d.keys() Out[125]: dict_keys(['Name', 'Country', 'Profession', 'Age'])
In [126]: d.values() Out[126]: dict_values(['Angela Merkel',
'Germany', 'Chancelor', 64]) In [127]: d.items() Out[127]:
dict_items([('Name', 'Angela Merkel'), ('Country', 'Germany'),
('Profession', 'Chancelor'), ('Age', 64)]) In [128]: birthday = True if
birthday: d['Age'] += 1 print(d['Age']) 65
```

There are several methods to get iterator objects from a dict object. The iterator objects behave like list objects when iterated over: In [129]: **for** item **in** d.items(): **print**(item) ('Name', 'Angela Merkel') ('Country', 'Germany') ('Profession', 'Chancelor') ('Age', 65) In [130]: **for** value **in** d.values(): **print**(type(value)) <**class** '**str**'> <**class** '**str**'> <**class** '**str**'> <**class** '**int**'>

Table 3-3 provides a summary of selected operations and methods of the dict object.

| Method       | Arguments | Returns/result                   |
|--------------|-----------|----------------------------------|
| d[k]         | [k]       | Item<br>of<br>d with<br>key<br>k |
| d[k] = x [k] |           | Sets<br>item<br>key<br>k to<br>x |

*Table 3-3. Selected operations and methods of dict objects*

| del d[k] [k] |       | Deletes<br>item<br>with<br>key<br>k                   |
|--------------|-------|-------------------------------------------------------|
| clear        | ()    | Removes<br>all<br>items                               |
| copy         | ()    | Makes<br>a<br>copy                                    |
| has_key      | (k)   | True if<br>k is<br>a<br>key                           |
| items        | ()    | Iterator<br>over<br>all<br>items                      |
| keys         | ()    | Iterator<br>over<br>all<br>keys                       |
| values       | ()    | Iterator<br>over<br>all<br>values                     |
| popitem      | (k)   | Returns<br>and<br>removes<br>item<br>with<br>key<br>k |
| update       | ([e]) | Updates<br>items<br>with<br>items<br>from<br>e        |

### **Sets**

The final data structure this section covers is the set object. Although set theory is a cornerstone of mathematics and also of financial theory, there are not too many practical applications for set objects. The objects are unordered collections of other objects, containing every element only once:

```
In [131]: s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
          s
Out[131]: {'d', 'du', 'u', 'ud'}
In [132]: t = set(['d', 'dd', 'uu', 'u'])
```

With set objects, one can implement basic operations on sets as in mathematical set theory. For example, one can generate unions, intersections, and differences:

```
In [133]: s.union(t)
Out[133]: {'d', 'dd', 'du', 'u', 'ud', 'uu'}
In [134]: s.intersection(t)
Out[134]: {'d', 'u'}
In [135]: s.difference(t)
Out[135]: {'du', 'ud'}
In [136]: t.difference(s)
Out[136]: {'dd', 'uu'}
In [137]: s.symmetric_difference(t)
Out[137]: {'dd', 'du', 'ud', 'uu'}
```

All of s and t.

Items in both s and t.

Items in s but not in t.

Items in t but not in s.

Items in either s or t but not both.

One application of set objects is to get rid of duplicates in a list object:

```
In [138]: from random import randint
          l = [randint(0, 10) for i in range(1000)]
          len(l)
Out[138]: 1000
In [139]: l[:20]
Out[139]: [4, 2, 10, 2, 1, 10, 0, 6, 0, 8, 10, 9, 2, 4, 7, 8, 10, 8, 8, 2]
In [140]: s = set(l)
          s
Out[140]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

1,000 random integers between 0 and 10.

Number of elements in l.

# **Conclusion**

The basic Python interpreter provides a rich set of flexible data structures. From a finance point of view, the following can be considered the most important ones: Basic data types

In Python in general and finance in particular, the classes int, float, bool, and str provide the atomic data types.

### *Standard data structures*

The classes tuple, list, dict, and set have many application areas in finance, with list being a flexible all-rounder for a number use cases.
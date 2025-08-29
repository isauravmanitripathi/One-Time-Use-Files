# **Chapter 6. Object-Oriented Programming**

The purpose of software engineering is to control complexity, not to create it. Pamela Zave

Object-oriented programming (OOP) is one of the most popular programming paradigms today. Used in the right way, it provides a number of advantages compared to, for example, procedural programming. In many cases, OOP seems to be particularly suited for financial modeling and implementing financial algorithms. However, there are also many critics, voicing their skepticism about single aspects of OOP or even the paradigm as a whole. This chapter takes a neutral stance, in that OOP is considered an important tool that might not be the best one for every single problem, but that should be at the disposal of programmers and quants working in finance.

With OOP, some new language comes along. The most important terms for the purposes of this book and chapter are (more follow later):

*Class*

An abstract definition of a class of objects. For example, a human being.

*Object*

An instance of a class. For example, Sandra.

### *Attribute*

A feature of the class (*class attribute*) or of an instance of the class (*instance attribute*). For example, being a mammal, being male or female, or color of the eyes.

### *Method*

An operation that the class can implement. For example, walking.

*Parameters*

Input taken by a method to influence its behavior. For example, three steps.

*Instantiation*

### *Instantiation*

The process of creating a specific object based on an abstract class.

Translated into Python code, a simple class implementing the example of a human being might look as follows:

```
In [1]: class HumanBeing(object):
            def __init__(self, first_name, eye_color):
                self.first_name = first_name
                self.eye_color = eye_color
                self.position = 0
            def walk_steps(self, steps):
                self.position += steps
```

Class definition statement; self refers to the current instance of the class.

Special method called during instantiation.

First name attribute initialized with parameter value.

Eye color attribute initialized with parameter value.

Position attribute initialized with 0.

Method definition for walking with steps as parameter.

Code that changes the position given the steps value.

Based on the class definition, a new Python object can be instantiated and used:

```
In [2]: Sandra = HumanBeing('Sandra', 'blue')
In [3]: Sandra.first_name
Out[3]: 'Sandra'
In [4]: Sandra.position
Out[4]: 0
In [5]: Sandra.walk_steps(5)
In [6]: Sandra.position
Out[6]: 5
```

The instantiation.

Accessing attribute values.

Calling the method.

Accessing the updated position value.

There are several *human aspects* that might speak for the use of OOP:

### *Natural way of thinking*

Human thinking typically evolves around real-world or abstract objects, like a car or a financial instrument. OOP is suited to modeling such objects with their characteristics.

### *Reducing complexity*

Via different approaches, OOP helps to reduce the complexity of a problem or algorithm and to model it feature-by-feature.

### *Nicer user interfaces*

OOP allows in many cases for nicer user interfaces and more compact code. This becomes evident, for example, when looking at the NumPy ndarray class or pandas DataFrame class.

### *Pythonic way of modeling*

Independent of the pros and cons of OOP, it is simply the dominant paradigm in Python. This is where the saying "everything is an object in Python" comes from. OOP also allows the programmer to build custom classes whose instances behave like every other instance of a standard Python class.

There are also several *technical aspects* that might speak for OOP:

### *Abstraction*

The use of attributes and methods allows building abstract, flexible models of objects, with a focus on what is relevant and neglecting what is not needed. In finance, this might mean having a general class that models a

financial instrument in abstract fashion. Instances of such a class would then be concrete financial products, engineered and offered by an investment bank, for example.

### *Modularity*

OOP simplifies breaking code down into multiple modules which are then linked to form the complete codebase. For example, modeling a European option on a stock could be achieved by a single class or by two classes, one for the underlying stock and one for the option itself.

### *Inheritance*

Inheritance refers to the concept that one class can *inherit* attributes and methods from another class. In finance, starting with a general financial instrument, the next level could be a general derivative instrument, then a European option, then a European call option. Every class might inherit attributes and methods from class(es) on a higher level.

### *Aggregation*

Aggregation refers to the case in which an object is at least partly made up of multiple other objects that might exist independently. A class modeling a European call option might have as attributes other objects for the underlying stock and the relevant short rate for discounting. The objects representing the stock and the short rate can be used independently by other objects as well.

### *Composition*

Composition is similar to aggregation, but here the single objects cannot exist independently of each other. Consider a custom-tailored interest rate swap with a fixed leg and a floating leg. The two legs do not exist independently of the swap itself.

### *Polymorphism*

Polymorphism can take on multiple forms. Of particular importance in a Python context is what is called *duck typing*. This refers to the fact that standard operations can be implemented on many different classes and their instances without knowing exactly what object one is dealing with. For a class of financial instruments this might mean that one can call a method get\_current\_price() independent of the specific type of the object (stock,

option, swap).

### *Encapsulation*

This concept refers to the approach of making data within a class accessible only via public methods. A class modeling a stock might have an attribute current\_stock\_price. Encapsulation would then give access to the attribute value via a method get\_current\_stock\_price() and would hide the data from the user (i.e., make it private). This approach might avoid unintended effects by simply working with and possibly changing attribute values. However, there are limits as to how data can be made private in a Python class.

On a somewhat higher level, many of these aspects can be summarized by *two generals goals* in software engineering:

### *Reusability*

Concepts like inheritance and polymorphism improve code reusability and increase the efficiency and productivity of the programmer. They also simplify code maintenance.

### *Nonredundancy*

At the same time, these approaches allow one to build almost nonredundant code, avoiding double implementation effort and reducing debugging and testing effort as well as maintenance effort. They might also lead to a smaller overall codebase.

This chapter is organized as follows:

### *"A Look at Python Objects"*

This section takes a look at some Python objects through the lens of OOP.

### *"Basics of Python Classes"*

This section introduces central elements of OOP in Python and uses financial instruments and portfolio positions as major examples.

### *"Python Data Model"*

This section discusses important elements of the Python data model and roles that certain special methods play.

## **A Look at Python Objects**

Let's start by taking a brief look at some standard objects encountered in previous chapters through the eyes of an OOP programmer.

### **int**

```
To start simple, consider an integer object. Even with such a simple Python
object, the major OOP features are present: In [7]: n = 5 In [8]:
type(n) Out[8]: int In [9]: n.numerator Out[9]: 5 In [10]:
n.bit_length() Out[10]: 3 In [11]: n + n Out[11]: 10 In [12]: 2
* n Out[12]: 10 In [13]: n.__sizeof__() Out[13]: 28
```

New instance n.

Type of the object.

An attribute.

A method.

Applying the + operator (addition).

Applying the \* operator (multiplication).

Calling the special method \_\_sizeof\_\_() to get the memory usage in bytes. 1

### **list**

```
list objects have some more methods but basically behave the same way: In
[14]: l = [1, 2, 3, 4] In [15]: type(l) Out[15]: list In [16]:
l[0] Out[16]: 1 In [17]: l.append(10) In [18]: l + l Out[18]:
[1, 2, 3, 4, 10, 1, 2, 3, 4, 10] In [19]: 2 * l Out[19]: [1, 2,
3, 4, 10, 1, 2, 3, 4, 10] In [20]: sum(l) Out[20]: 20 In [21]:
l.__sizeof__() Out[21]: 104
    New instance l.
    Type of the object.
```

Selecting an element via indexing.

A method.

Applying the + operator (concatenation).

Applying the \* operator (concatenation).

Applying the standard Python function sum().

Calling the special method \_\_sizeof\_\_() to get the memory usage in bytes.

### **ndarray**

int and list objects are standard Python objects. The NumPy ndarray object is a "custom-made" object from an open source package:

```
In [22]: import numpy as np
In [23]: a = np.arange(16).reshape((4, 4))
In [24]: a
Out[24]: array([[ 0, 1, 2, 3],
               [ 4, 5, 6, 7],
               [ 8, 9, 10, 11],
               [12, 13, 14, 15]])
In [25]: type(a)
Out[25]: numpy.ndarray
```

Importing numpy.

A new instance a.

Type of the object.

Although the ndarray object is not a standard object, it behaves in many cases as if it were one — thanks to the Python data model, as explained later in this chapter:

```
In [26]: a.nbytes
Out[26]: 128
In [27]: a.sum()
Out[27]: 120
In [28]: a.cumsum(axis=0)
Out[28]: array([[ 0, 1, 2, 3],
                [ 4, 6, 8, 10],
                [12, 15, 18, 21],
                [24, 28, 32, 36]])
In [29]: a + a
Out[29]: array([[ 0, 2, 4, 6],
                [ 8, 10, 12, 14],
                [16, 18, 20, 22],
                [24, 26, 28, 30]])
In [30]: 2 * a
```

```
Out[30]: array([[ 0, 2, 4, 6],
                [ 8, 10, 12, 14],
                [16, 18, 20, 22],
                [24, 26, 28, 30]])
In [31]: sum(a)
Out[31]: array([24, 28, 32, 36])
In [32]: np.sum(a)
Out[32]: 120
In [33]: a.__sizeof__()
Out[33]: 112
```

An attribute.

A method (aggregation).

A method (no aggregation).

Applying the + operator (addition).

Applying the \* operator (multiplication).

Applying the standard Python function sum().

Applying the NumPy universal function np.sum().

Calling the special method \_\_sizeof\_\_() to get the memory usage in bytes.

### **DataFrame**

Finally, a quick look at the pandas DataFrame object, which behaves similarly to the ndarray object. First, the instantiation of the DataFrame object based on the ndarray object:

```
In [34]: import pandas as pd
In [35]: df = pd.DataFrame(a, columns=list('abcd'))
In [36]: type(df)
Out[36]: pandas.core.frame.DataFrame
```

Importing pandas.

A new instance df.

Type of the object.

Second, a look at attributes, methods, and operations:

```
In [37]: df.columns
Out[37]: Index(['a', 'b', 'c', 'd'], dtype='object')
In [38]: df.sum()
Out[38]: a 24
       b 28
       c 32
       d 36
       dtype: int64
In [39]: df.cumsum()
Out[39]: a b c d
       0 0 1 2 3
       1 4 6 8 10
       2 12 15 18 21
       3 24 28 32 36
In [40]: df + df
Out[40]: a b c d
       0 0 2 4 6
       1 8 10 12 14
       2 16 18 20 22
       3 24 26 28 30
In [41]: 2 * df
Out[41]: a b c d
       0 0 2 4 6
```

```
1 8 10 12 14
       2 16 18 20 22
       3 24 26 28 30
In [42]: np.sum(df)
Out[42]: a 24
       b 28
       c 32
       d 36
       dtype: int64
In [43]: df.__sizeof__()
Out[43]: 208
```

An attribute.

A method (aggregation).

A method (no aggregation).

Applying the + operator (addition).

Applying the \* operator (multiplication).

Applying the NumPy universal function np.sum().

Calling the special method \_\_sizeof\_\_() to get the memory usage in bytes.

## **Basics of Python Classes**

This section covers major concepts and the concrete syntax to make use of OOP in Python. The context now is about building custom classes to model types of objects that cannot be easily, efficiently, or properly modeled by existing Python object types. Throughout, the example of a *financial instrument* is used.

Two lines of code suffice to create a new Python class:

```
In [44]: class FinancialInstrument(object):
             pass
In [45]: fi = FinancialInstrument()
In [46]: type(fi)
Out[46]: __main__.FinancialInstrument
In [47]: fi
Out[47]: <__main__.FinancialInstrument at 0x116767278>
In [48]: fi.__str__()
Out[48]: '<__main__.FinancialInstrument object at 0x116767278>'
In [49]: fi.price = 100
In [50]: fi.price
Out[50]: 100
```

Class definition statement. 2

Some code; here simply the pass keyword.

A new instance of the class named fi.

The type of the object.

Every Python object comes with certain "special" attributes and methods (from object); here, the special method to retrieve the string representation is called.

So-called data attributes — in contrast to regular attributes — can be

So-called data attributes — in contrast to regular attributes — can be defined on the fly for every object.

An important special method is \_\_init\_\_, which gets called during every instantiation of an object. It takes as parameters the object itself (self, by convention) and potentially multiple others:

```
In [51]: class FinancialInstrument(object):
             author = 'Yves Hilpisch'
             def __init__(self, symbol, price):
                 self.symbol = symbol
                 self.price = price
In [52]: FinancialInstrument.author
Out[52]: 'Yves Hilpisch'
In [53]: aapl = FinancialInstrument('AAPL', 100)
In [54]: aapl.symbol
Out[54]: 'AAPL'
In [55]: aapl.author
Out[55]: 'Yves Hilpisch'
In [56]: aapl.price = 105
In [57]: aapl.price
Out[57]: 105
```

Definition of a class attribute (inherited by every instance).

The special method \_\_init\_\_ called during initialization.

Definition of the instance attributes (individual to every instance).

A new instance of the class named fi.

Accessing an instance attribute.

Accessing a class attribute.

Changing the value of an instance attribute.

Prices of financial instruments change regularly, but the symbol of a financial instrument probably does not change. To introduce encapsulation to the class definition, two methods, get\_price() and set\_price(), might be defined. The code that follows additionally inherits from the previous class definition (and not from object anymore):

```
In [58]: class FinancialInstrument(FinancialInstrument):
             def get_price(self):
                 return self.price
             def set_price(self, price):
                 self.price = price
In [59]: fi = FinancialInstrument('AAPL', 100)
In [60]: fi.get_price()
Out[60]: 100
In [61]: fi.set_price(105)
In [62]: fi.get_price()
Out[62]: 105
In [63]: fi.price
Out[63]: 105
```

Class definition via inheritance from previous version.

Defines the get\_price() method.

Defines the set\_price() method …

… and updates the instance attribute value given the parameter value.

A new instance based on the new class definition named fi.

Calls the get\_price() method to read the instance attribute value.

Updates the instance attribute value via set\_price().

Direct access to the instance attribute.

Encapsulation generally has the goal of hiding data from the user working with a class. Adding *getter* and *setter* methods is one part of achieving this goal. However, this does not prevent the user from directly accessing and manipulating instance attributes. This is where *private* instance attributes come into play. They are defined by two leading underscores:

```
In [64]: class FinancialInstrument(object):
            def __init__(self, symbol, price):
                self.symbol = symbol
                self.__price = price
            def get_price(self):
                return self.__price
            def set_price(self, price):
                self.__price = price
In [65]: fi = FinancialInstrument('AAPL', 100)
In [66]: fi.get_price()
Out[66]: 100
In [67]: fi.__price
        -----------------------------------------------------------------
        AttributeError Traceback (most recent call last)
        <ipython-input-67-bd62f6cadb79> in <module>
        ----> 1 fi.__price
        AttributeError: 'FinancialInstrument' object has no attribute '__price'
In [68]: fi._FinancialInstrument__price
Out[68]: 100
In [69]: fi._FinancialInstrument__price = 105
In [70]: fi.set_price(100)
```

Price is defined as a private instance attribute.

The method get\_price() returns its value.

Trying to access the attribute directly raises an error.

If the class name is prepended with a single leading underscore, direct access and manipulation are still possible.

Sets the price back to its original value.

### **ENCAPSULATION IN PYTHON**

Although encapsulation can basically be implemented for Python classes via private instance attributes and respective methods dealing with them, the hiding of data from the user cannot be fully enforced. In that sense, it is more an engineering principle in Python than a technical feature of Python classes.

Consider another class that models a portfolio position of a financial instrument. With the two classes *aggregation* as a concept is easily illustrated. An instance of the PortfolioPosition class takes an instance of the FinancialInstrument class as an attribute value. Adding an instance attribute, such as position\_size, one can then calculate, for instance, the position value: In [71]: **class PortfolioPosition**(object): **def** \_\_init\_\_(self, financial\_instrument, position\_size): self.position = financial\_instrument self.\_\_position\_size = position\_size **def** get\_position\_size(self): **return** self.\_\_position\_size **def** update\_position\_size(self, position\_size): self.\_\_position\_size = position\_size **def** get\_position\_value(self): **return** self.\_\_position\_size \* \ self.position.get\_price() In [72]: pp = PortfolioPosition(fi, 10) In [73]: pp.get\_position\_size() Out[73]: 10 In [74]: pp.get\_position\_value() Out[74]: 1000 In [75]: pp.position.get\_price() Out[75]: 100 In [76]: pp.position.set\_price(105) In [77]: pp.get\_position\_value() Out[77]: 1050

An instance attribute based on an instance of the FinancialInstrument class.

A private instance attribute of the PortfolioPosition class.

Calculates the position value based on the attributes.

Methods attached to the instance attribute object can be accessed directly (could be hidden as well).

Updates the price of the financial instrument.

Calculates the new position value based on the updated price.

## **Python Data Model**

The examples in the previous section highlighted some aspects of the so-called Python *data* or *[object](https://docs.python.org/3/reference/datamodel.html) model*. The Python data model allows you to design classes that consistently interact with basic language constructs of Python. Among others, it supports (see Ramalho (2015), p. 4) the following tasks and constructs:

- Iteration
- Collection handling
- Attribute access
- Operator overloading
- Function and method invocation
- Object creation and destruction
- String representation (e.g., for printing)
- Managed contexts (i.e., with blocks)

Since the Python data model is so important, this section is dedicated to an example (from Ramalho (2015), with slight adjustments) that explores several aspects of it. It implements a class for one-dimensional, three-element vectors (think of vectors in Euclidean space). First, the special method \_\_init\_\_:

Three preinitialized instance attributes (think three-dimensional space).

```
In [78]: class Vector(object):
             def __init__(self, x=0, y=0, z=0):
                 self.x = x
                 self.y = y
                 self.z = z
In [79]: v = Vector(1, 2, 3)
In [80]: v
Out[80]: <__main__.Vector at 0x1167789e8>
```

Three preinitialized instance attributes (think three-dimensional space).

A new instance of the class named v.

The default string representation.

The special method \_\_repr\_\_ allows the definition of custom string representations:

```
In [81]: class Vector(Vector):
             def __repr__(self):
                 return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)
In [82]: v = Vector(1, 2, 3)
In [83]: v
Out[83]: Vector(1, 2, 3)
In [84]: print(v)
         Vector(1, 2, 3)
```

The new string representation.

abs() and bool() are two standard Python functions whose behavior on the Vector class can be defined via the special methods \_\_abs\_\_ and \_\_bool\_\_:

```
In [85]: class Vector(Vector):
             def __abs__(self):
                 return (self.x ** 2 + self.y ** 2 +
                         self.z ** 2) ** 0.5
             def __bool__(self):
                 return bool(abs(self))
In [86]: v = Vector(1, 2, -1)
In [87]: abs(v)
Out[87]: 2.449489742783178
In [88]: bool(v)
Out[88]: True
In [89]: v = Vector()
In [90]: v
Out[90]: Vector(0, 0, 0)
In [91]: abs(v)
Out[91]: 0.0
In [92]: bool(v)
```

```
Out[92]: False
```

Returns the Euclidean norm given the three attribute values.

A new Vector object with nonzero attribute values.

A new Vector object with zero attribute values only.

As shown multiple times, the + and \* operators can be applied to almost any Python object. The behavior is defined through the special methods \_\_add\_\_ and \_\_mul\_\_:

```
In [93]: class Vector(Vector):
             def __add__(self, other):
                 x = self.x + other.x
                 y = self.y + other.y
                 z = self.z + other.z
                 return Vector(x, y, z)
             def __mul__(self, scalar):
                 return Vector(self.x * scalar,
                               self.y * scalar,
                               self.z * scalar)
In [94]: v = Vector(1, 2, 3)
In [95]: v + Vector(2, 3, 4)
Out[95]: Vector(3, 5, 7)
In [96]: v * 2
Out[96]: Vector(2, 4, 6)
```

In this case, each special method returns an object of its own kind.

Another standard Python function is len(), which gives the length of an object in number of elements. This function accesses the special method \_\_len\_\_ when called on an object. On the other hand, the special method \_\_getitem\_\_ makes indexing via the square bracket notation possible:

```
In [97]: class Vector(Vector):
             def __len__(self):
                 return 3
             def __getitem__(self, i):
                 if i in [0, -3]: return self.x
```

```
elif i in [1, -2]: return self.y
                elif i in [2, -1]: return self.z
                else: raise IndexError('Index out of range.')
In [98]: v = Vector(1, 2, 3)
In [99]: len(v)
Out[99]: 3
In [100]: v[0]
Out[100]: 1
In [101]: v[-2]
Out[101]: 2
In [102]: v[3]
         -----------------------------------------------------------------
         IndexError Traceback (most recent call last)
         <ipython-input-102-f998c57dcc1e> in <module>
         ----> 1 v[3]
         <ipython-input-97-b0ca25eef7b3> in __getitem__(self, i)
               7 elif i in [1, -2]: return self.y
               8 elif i in [2, -1]: return self.z
         ----> 9 else: raise IndexError('Index out of range.')
         IndexError: Index out of range.
```

All instances of the Vector class have a length of three.

Finally, the special method \_\_iter\_\_ defines the behavior during iterations over elements of an object. An object for which this operation is defined is called *iterable*. For instance, all collections and containers are iterable:

```
In [103]: class Vector(Vector):
              def __iter__(self):
                  for i in range(len(self)):
                      yield self[i]
In [104]: v = Vector(1, 2, 3)
In [105]: for i in range(3):
              print(v[i])
          1
          2
          3
In [106]: for coordinate in v:
              print(coordinate)
          1
          2
          3
```

Indirect iteration using index values (via \_\_getitem\_\_).

Direct iteration over the class instance (using \_\_iter\_\_).

### **ENHANCING PYTHON**

The Python data model allows the definition of Python classes that interact with standard Python operators, functions, etc., seamlessly. This makes Python a rather flexible programming language that can easily be enhanced by new classes and types of objects.

As a summary, the following section provides the Vector class definition in a single code block.

### **The Vector Class**

```
In [107]: class Vector(object):
              def __init__(self, x=0, y=0, z=0):
                  self.x = x
                  self.y = y
                  self.z = z
              def __repr__(self):
                  return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)
              def __abs__(self):
                  return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
              def __bool__(self):
                  return bool(abs(self))
              def __add__(self, other):
                  x = self.x + other.x
                  y = self.y + other.y
                  z = self.z + other.z
                  return Vector(x, y, z)
              def __mul__(self, scalar):
                  return Vector(self.x * scalar,
                                self.y * scalar,
                                self.z * scalar)
              def __len__(self):
                  return 3
              def __getitem__(self, i):
                  if i in [0, -3]: return self.x
                  elif i in [1, -2]: return self.y
                  elif i in [2, -1]: return self.z
                  else: raise IndexError('Index out of range.')
              def __iter__(self):
                  for i in range(len(self)):
                      yield self[i]
```

## **Conclusion**

This chapter introduces notions and approaches from object-oriented programming, both theoretically and through Python examples. OOP is one of the main programming paradigms used in Python. It not only allows for the modeling and implementation of rather complex applications, but also allows one to create custom objects that behave like standard Python objects due to the flexible Python data model. Although there are many critics who argue against OOP, it is safe to say that it provides the Python programmer and quant with powerful tools that are helpful when a certain degree of complexity is reached. The derivatives pricing package developed and discussed in Part V presents such a case where OOP seems the only sensible programming paradigm to deal with the inherent complexities and requirements for abstraction.
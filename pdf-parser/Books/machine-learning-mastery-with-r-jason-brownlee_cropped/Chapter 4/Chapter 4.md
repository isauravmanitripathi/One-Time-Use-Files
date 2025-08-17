# Chapter 4

# Crash Course in R For Developers

As a developer you can pick-up the R programming language fast. You don't need to know much about a new language to be able to read and understanding code snippets and writing your own small scripts and programs. Learning R is not about learning the language, it is about learning the packages.

In this lesson you will discover the basic syntax, data structures and control structures that you need to know to start reading and writing R scripts. After completing this lesson you will know:

- How to assign variables in R.
- How to work with basic data structures in R like vectors, lists and data frames.
- How to use basic flow control structures like loops in R.
- How to work with functions and packages in R.

This lesson will refresh your R knowledge or teach you just enough to be able to understand the R code used throughout the rest of this book. Let's get started.

## 4.1 R Syntax is Different, But The Same

The syntax in R looks confusing, but only to begin with. It is a LISP-style language inspired by an even older language (S). The assignment syntax is probably the strangest thing you will see. Assignment uses the arrow (<-) rather than a single equals (=). Also, like many programming languages, R syntax is case sensitive.

R has all of your familiar control flow structures like if-then-else, for-loops and while loops. Comments in R use the hash (#) character. You can create your own functions and packages of helper functions for your scripts. If you have done any scripting before, like JavaScript, Python, Ruby, BASH or similar, then you will pick up R very quickly.

### 4.1.1 You Can Already Program, Just Learn the R Syntax

As a developer, you already know how to program. This means that you can take a problem and think up the type of procedure and data structures you need to implement it. The language you are using is just a detail. You only need to map your idea of the solution onto the specifics of the language you are using. This is how you can begin using R very quickly. To get started, you need to know the absolute basics, such as:

- How do you assign data to variables?
- How do you work with different data types?
- How do you work with the data structures for handling data?
- How do you use the standard flow control structures?
- How do you work with functions and third-party packages?

This chapter is designed to answer these language jump-start questions for you.

## 4.2 Assignment

The assignment operator in R is the arrow operator (<-). Below are examples of assigning an integer, double, string and a boolean, and printing each out to the console in turn.

```
> # integer
> i <- 23
> i
[1] 23
> # double
> d <- 2.3
> d
[1] 2.3
> # string
> s <- 'hello world'
> s
[1] "hello world"
> # boolean
> b <- TRUE
> b
[1] TRUE
```

Listing 4.1: Examples of variable assignment in R.

Remember, do not use equals (=) for assignment. It is the biggest mistake new R programmers make.

## 4.3 Data Structures

Let's take a look at some of the most common and most useful data structures in R.

### 4.3.1 Vectors

Vectors are lists of data that can be the same or different types:

```
> # create a vector using the c() function
> v <- c(98, 99, 100)
> v
[1] 98 99 100
> v[1:2]
[1] 98 99
> # create a vector from a range of integers
> r <- (1:10)
> r
[1] 1 2 3 4 5 6 7 8 9 10
> r[5:10]
[1] 5 6 7 8 9 10
> # add a new item to the end of a vector
> v <- c(1, 2, 3)
> v[4] <- 4
> v
[1] 1 2 3 4
```

Listing 4.2: Examples working with vectors in R.

Notice that vectors are 1-indexed (indexes start at 1 not 0). You will use the c() function a lot to combine variables into a vector.

#### 4.3.2 Lists

Lists provide a group of named items, not unlike a map.

```
# create a list of named items
a <- list(aa=1, bb=2, cc=3)
a
a$aa
# add a named item to a list
a$dd=4
a
```

Listing 4.3: Examples of working with lists in R.

You can define a new list with the list() function. A list can be initialized with values or empty. Note that the named values in the list can be accessed using the dollar operator (\$). Once referenced, they can be read or written. This is also how new items can be added to the list.

#### 4.3.3 Matrices

A matrix is a table of data of the same type (e.g. numeric). It has dimensions (rows and columns) and the columns can be named.

<sup>#</sup> Create a 2-row, 3-column matrix with named headings

```
> data <- c(1, 2, 3, 4, 5, 6)
> headings <- list(NULL, c("a","b","c"))
> m <- matrix(data, nrow=2, ncol=3, byrow=TRUE, dimnames=headings)
> m
    a b c
[1,] 1 2 3
[2,] 4 5 6
> m[1,]
a b c
1 2 3
> m[,1]
[1] 1 4
```

Listing 4.4: Examples of working with a martix in R.

A lot of useful plotting and machine learning algorithms require the data to be provided as a matrix. Note the syntax to index into rows [1,] and columns [,1] of a matrix.

#### 4.3.4 Data Frame

Data frames are useful for representing tables of your data in R.

```
# create a new data frame
years <- c(1980, 1985, 1990)
scores <- c(34, 44, 83)
df <- data.frame(years, scores)
df[,1]
df$years
```

Listing 4.5: Examples of working with a Data Frame in R.

A matrix is a much simpler structure, intended for mathematical operations. A data frame is more suited to representing a table of data and is expected by modern implementations of machine learning algorithms in R. Note that you can index into rows and columns of a data frame just like you can for a matrix. Also note that you can reference a column using its name just like a list (df\$years).

## 4.4 Flow Control

Now, let's take a look at some standard flow control structures in R. As a developer, these are all very familiar and self explanatory.

#### 4.4.1 If-Then-Else

```
# if then else
a <- 66
if (a > 55) {
 print("a is more than 55")
} else {
 print("A is less than or equal to 55")
```

```
}
[1] "a is more than 55"
```

Listing 4.6: Example of an If-Then-Else structure in R.

### 4.4.2 For Loop

```
# for loop
mylist <- c(55, 66, 77, 88, 99)
for (value in mylist) {
 print(value)
}
[1] 55
[1] 66
[1] 77
[1] 88
[1] 99
```

Listing 4.7: Example of a For-Loop in R.

## 4.4.3 While Loop

```
# while loop
a <- 100
while (a < 500) {
  a <- a + 100
}
a
[1] 500
```

Listing 4.8: Example of a While-Loop in R.

# 4.5 Functions

Functions let you group code and call it repeatedly with arguments. You have already used one function, the c() function for combining objects into a vector for example. R has many built in functions and additional functions can be provided by installing and loading third-party packages. Here is an example of using a statistical function to calculate the mean of a vector of numbers:

```
# call function to calculate the mean on a vector of integers
numbers <- c(1, 2, 3, 4, 5, 6)
mean(numbers)
```

[1] 3.5

Listing 4.9: Example of calling the mean() function in R.

#### 4.6. Packages 22

You can get help for a function in R by using the question mark operator (?) followed by the function name. You can also call the help() function and passing the function name you need help with as the operator.

```
# help with the mean() function
?mean
help(mean)
```

Listing 4.10: Example of getting help for the mean() function in R.

Often you just want to know what arguments a function takes. To check, you can call the args() function and pass the function name as an argument.

```
# function arguments
args(mean)
```

Listing 4.11: Example of showing the arguments for the mean() function in R.

You can get example usage of a function by calling the example() function and passing the name of the function as an argument.

```
# example usage of the mean function
example(mean)
```

Listing 4.12: Example of example usage of the mean() function in R.

You can define your own functions that may or may not take arguments or return a result. Below is an example of a custom function to calculate and return the sum of three numbers:

```
# define custom function
mysum <- function(a, b, c) {
 sum <- a + b + c
 return(sum)
}
# call custom function
mysum(1,2,3)
[1] 6
```

Listing 4.13: Example of defining and calling a custom function in R.

## 4.6 Packages

Packages are the way that third party R code is distributed. The Comprehensive R Archive Network (CRAN) provides hosting and listing of third party R packages that you can download<sup>1</sup> .You can install a package hosted on CRAN by calling a function. It will then pop-up a dialog to ask you which mirror you would like to download the package from. For example, here is how you can install the caret package which is very useful for machine learning in R and will be used in later lessons:

```
# install the package
install.packages("caret")
```

Listing 4.14: Example of installing the caret package in R.

```
1https://cran.r-project.org/
```

#### 4.7. 5 Things To Remember 23

You can load a package in R by calling the library() function and passing the package name as the argument (it's a confusing function name, I know). For example, you can load the caret package as follows:

```
# load the package
library(caret)
```

Listing 4.15: Example of loading the caret package in R.

A package can provide a lot of new functions. You can read up on a package on it's CRAN page, but you can also get help for the package within R by calling the library() function with the argument help="PackageName". For example, you can get help for the caret package as follows:

```
# help for the package
library(help="caret")
```

Listing 4.16: Example of getting help with the caret package in R.

## 4.7 5 Things To Remember

Here are five quick tips to remember when getting started in R:

- Assignment: R uses the arrow operator (<-) for assignment, not a single equals (=).
- Case Sensitive: The R language is case sensitive, meaning that C() and c() are two different function calls.
- Help: You can get help on any operator or function using the help() function or the question mark operator ?.
- How To Quit: You can exit the R interactive environment by calling the question function q().
- Documentation: R installs with a lot of useful documentation. You can review it in the browser by typing help.start()

## 4.8 Summary

In this lesson you took a crash course in basic R syntax and got up to speed with the R programming language, including:

- 1. Variable Assignment.
- 2. Data Structures.
- 3. Flow Control.
- 4. Functions.
- 5. Packages.

#### 4.8. Summary 24

As a developer, you now know enough to read other peoples R scripts. You discovered that learning R is not about learning the language, but it is about learning how to use R packages. You also have the tools to start writing your own scripts in the R interactive environment.

#### 4.8.1 Next Step

Now that you know some basic R syntax, it is time to learn how to load data. In the next lesson you will discover how you can very quickly and easily load standard machine learning datasets in R.
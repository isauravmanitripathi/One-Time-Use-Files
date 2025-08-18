# Chapter 6

## Load Your Machine Learning Datasets

You need to be able to load data into R when working on a machine learning problem. In this lesson, you will discover how you can load your data files into R and start your machine learning project. After completing this lesson, you will know:

1. How to load your own data into R from local CSV files.

2. How to load your own data into R from CSV files located on the web.

Let's get started.

### 6.1 Access To Your Data

The most common way to work with data in machine learning is in CSV (comma separated value) files. Data may originally be stored in all manner of formats and diverse locations. For example:

- Relational database tables.
- XML files.
- JSON files.
- Fixed-width formatted file.
- Spreadsheet file (e.g. Microsoft Office).

You need to consolidate your data into a single file with rows and columns before you can work with it on a machine learning project. The standard format for representing a machine learning dataset is a CSV file. This is because machine learning algorithms, for the most part, work with data in tabular format (e.g. a matrix of input and output vectors). Datasets in R are often represented as a matrix or data frame structure. The first step of a machine learning project in R is loading your data into R as a matrix or data frame.

### 6.2 Load Data From CSV File

This example shows the loading of the iris dataset from a CSV file. This recipe will load a CSV file without a header (e.g. column names) located in the current directory into R as a data frame.

```
# define the filename
filename <- "iris.csv"
# load the CSV file from the local directory
dataset <- read.csv(filename, header=FALSE)
# preview the first 5 rows
head(dataset)
```

Listing 6.1: Load data from a CSV file.

Running this recipe, you will see:

V1 V2 V3 V4 V5 1 5.1 3.5 1.4 0.2 Iris-setosa 2 4.9 3.0 1.4 0.2 Iris-setosa 3 4.7 3.2 1.3 0.2 Iris-setosa 4 4.6 3.1 1.5 0.2 Iris-setosa 5 5.0 3.6 1.4 0.2 Iris-setosa 6 5.4 3.9 1.7 0.4 Iris-setosa

Listing 6.2: Output of loading data from a CSV file.

This recipe is useful if you want to store the data locally with your R scripts, such as in a project managed under revision control. If the data is not in your local directory, you can either:

- 1. Specify the full path to the dataset on your local file system.
- 2. Use the setwd() function to set your current working directory to where the dataset is located

### 6.3 Load Data From CSV URL

This example shows the loading of the iris data from a CSV file located on the UCI Machine Learning Repository website. This recipe will load a CSV file without a header from a URL into R as a data frame.

```
# load the package
library(RCurl)
# specify the URL for the Iris data CSV
urlfile <-'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# download the file
downloaded <- getURL(urlfile, ssl.verifypeer=FALSE)
# treat the text data as a steam so we can read from it
connection <- textConnection(downloaded)
# parse the downloaded data as CSV
dataset <- read.csv(connection, header=FALSE)
# preview the first 5 rows
head(dataset)
```

Listing 6.3: Load a CSV file from a URL.

Running this recipe, you will see:

V1 V2 V3 V4 V5 1 5.1 3.5 1.4 0.2 Iris-setosa 2 4.9 3.0 1.4 0.2 Iris-setosa 3 4.7 3.2 1.3 0.2 Iris-setosa 4 4.6 3.1 1.5 0.2 Iris-setosa 5 5.0 3.6 1.4 0.2 Iris-setosa 6 5.4 3.9 1.7 0.4 Iris-setosa

Listing 6.4: Output of loading a CSV file from a URL.

This recipe is useful if your dataset is stored on a server, such as on your GitHub account. It is also useful if you want to use datasets from the UCI Machine Learning Repository but do not want to store them locally.

### 6.4 Summary

In this lesson, you discovered how you can load your data into R. You learned two recipes for loading your data into R:

- 1. How to load your data from a local CSV file.
- 2. How to load your data from a CSV file located on a webserver.

#### 6.4.1 Next Step

You have now seen two ways that you can load data into R: standard datasest from R packages and your own CSV files. Now it is time to start looking at some data. In the next lesson you will discover how you can start to understand your data using descriptive statistics.
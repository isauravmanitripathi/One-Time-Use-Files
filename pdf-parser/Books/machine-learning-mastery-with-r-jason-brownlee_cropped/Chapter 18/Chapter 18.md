# Chapter 18

# Your First Machine Learning Project in R Step-By-Step

You need to see how all of the pieces of a predictive modeling machine learning project actually fit together. In this lesson you will complete your first machine learning project using R. In this step-by-step tutorial project you will:

- 1. Load a dataset and understand it's structure using statistical summaries and data visualization.
- 2. Create 5 machine learning models, pick the best and build confidence that the accuracy is reliable.
- 3. If you are a machine learning beginner and looking to finally get started using R, this tutorial was designed for you.

Let's get started!

## 18.1 Hello World of Machine Learning

The best small project to start with on a new tool is the classification of iris flowers (e.g. the iris dataset described in Chapter 5). This is a good dataset for your first project because it is so well understood.

- Attributes are numeric so you have to figure out how to load and handle data.
- It is a classification problem, allowing you to practice with perhaps an easier type of supervised learning algorithm.
- It is a multi-class classification problem (multi-nominal) that may require some specialized handling.
- It only has 4 attribute and 150 rows, meaning it is small and easily fits into memory (and a screen or single sheet of paper).
- All of the numeric attributes are in the same units and the same scale not requiring any special scaling or transforms to get started.

#### 18.2. Load The Data 143

In this tutorial we are going to work through a small machine learning project end-to-end. Here is an overview of what we are going to cover:

- 1. Loading the dataset.
- 2. Summarizing the dataset.
- 3. Visualizing the dataset.
- 4. Evaluating some algorithms.
- 5. Making some predictions.

Take your time and work through each step. Try to type in the commands yourself or copy-and-paste the commands to speed things up. Start your R interactive environment and let's get started with your hello world machine learning project in R.

## 18.2 Load The Data

Here is what we are going to do in this step:

- 1. Load the iris data the easy way.
- 2. Load the iris data from CSV (optional, for purists).
- 3. Separate the data into a training dataset and a validation dataset.

#### 18.2.1 Load Data The Easy Way

You can load the iris dataset from the stats package as follows:

```
# attach the iris dataset to the environment
data(iris)
# rename the dataset
dataset <- iris
```

Listing 18.1: Load data from package.

You now have the iris data loaded in R and accessible via the dataset variable. I like to name the loaded dataset. This is helpful if you want to copy-paste code between projects and the dataset always has the same name.

### 18.2.2 Load From CSV (optional alternative)

Maybe you are a purist and you want to load the data just like you would on your own machine learning project, from a CSV file.

- 1. Download the iris dataset from the UCI Machine Learning Repository<sup>1</sup> .
- 2. Save the file as iris.csv your project directory.

<sup>1</sup><https://archive.ics.uci.edu/ml/datasets/Iris>

Load the dataset from the CSV file as follows:

```
# define the filename
filename <- "iris.csv"
# load the CSV file from the local directory
dataset <- read.csv(filename, header=FALSE)
# set the column names in the dataset
colnames(dataset) <- c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width","Species")
```

Listing 18.2: Load data from CSV.

You now have the iris data loaded in R and accessible via the dataset variable.

### 18.2.3 Create a Validation Dataset

We need to know that the model we created is any good. Later, we will use statistical methods to estimate the accuracy of the models that we create on unseen data. We also want a more concrete estimate of the accuracy of the best model on unseen data by evaluating it on actual unseen data. That is, we are going to hold back some data that the algorithms will not get to see and we will use this data to get a second and independent idea of how accurate the best model might actually be. We will split the loaded dataset into two, 80% of which we will use to train our models and 20% that we will hold back as a validation dataset.

```
# create a list of 80% of the rows in the original dataset we can use for training
validationIndex <- createDataPartition(dataset$Species, p=0.80, list=FALSE)
# select 20% of the data for validation
validation <- dataset[-validationIndex,]
# use the remaining 80% of data to training and testing the models
dataset <- dataset[validationIndex,]
```

Listing 18.3: Split data into a training dataset and a validation dataset.

You now have training data in the dataset variable and a validation set we will use later in the validation variable. Note that we replaced our dataset variable with the 80% sample of the dataset. This was an attempt to keep the rest of the code simpler and readable.

## 18.3 Summarize Dataset

Now it is time to take a look at the data. In this step we are going to take a look at the data a few different ways:

- 1. Dimensions of the dataset.
- 2. Types of the attributes.
- 3. Peek at the data itself.
- 4. Levels of the class attribute.
- 5. Breakdown of the instances in each class.
- 6. Statistical summary of all attributes.

#### 18.3.1 Dimensions of Dataset

We can get a quick idea of how many instances (rows) and how many attributes (columns) the data contains with the dim function.

```
# dimensions of dataset
dim(dataset)
```

Listing 18.4: Calculate the dimensions of the dataset.

We can see that the data has 120 instances and 5 attributes:

[1] 120 5

Listing 18.5: Output of the dimensions of the dataset.

#### 18.3.2 Types of Attributes

It is a good idea to review the types of the attributes. They could be doubles, integers, strings, factors and other types. Knowing the types is important as it will give you an idea of how to better summarize the data you have and the types of transforms you might need to use to prepare the data before you model it.

```
# list types for each attribute
sapply(dataset, class)
```

Listing 18.6: Calculate the attribute data types of the dataset.

We can see that all of the inputs are double and that the class value is a factor:

```
Sepal.Length Sepal.Width Petal.Length Petal.Width Species
"numeric" "numeric" "numeric" "numeric" "factor"
```

Listing 18.7: Output of data types of the dataset.

#### 18.3.3 Peek at the Data

It is also always a good idea to actually eyeball your data.

```
# take a peek at the first 5 rows of the data
head(dataset)
```

Listing 18.8: Display the first few rows of the dataset.

We can see the first 5 rows of the data:

|                          | Sepal.Length Sepal.Width Petal.Length Petal.Width Species |
|--------------------------|-----------------------------------------------------------|
| 1 5.1 3.5 1.4 0.2 setosa |                                                           |
| 2 4.9 3.0 1.4 0.2 setosa |                                                           |
| 3 4.7 3.2 1.3 0.2 setosa |                                                           |
| 5 5.0 3.6 1.4 0.2 setosa |                                                           |
| 6 5.4 3.9 1.7 0.4 setosa |                                                           |
| 7 4.6 3.4 1.4 0.3 setosa |                                                           |

#### 18.3.4 Levels of the Class

The class variable is a factor. A factor has multiple class labels called levels. Let's look at the levels:

```
# list the levels for the class
levels(dataset$Species)
```

Listing 18.10: Calculate the levels of the class attribute.

Notice above how we can refer to an attribute by name as a property of the dataset. In the results we can see that the class has 3 different labels:

[1] "setosa" "versicolor" "virginica"

Listing 18.11: Output of the levels of the class attribute.

This is a multi-class or a multinomial classification problem. If there were two levels, it would be a binary classification problem.

#### 18.3.5 Class Distribution

Let's now take a look at the number of instances (rows) that belong to each class. We can view this as an absolute count and as a percentage.

```
# summarize the class distribution
percentage <- prop.table(table(dataset$Species)) * 100
cbind(freq=table(dataset$Species), percentage=percentage)
```

Listing 18.12: Calculate the breakdown of the class attribute.

We can see that each class has the same number of instances (40 or 33% of the dataset).

freq percentage setosa 40 33.33333 versicolor 40 33.33333 virginica 40 33.33333

Listing 18.13: Output of the breakdown of the class attribute.

#### 18.3.6 Statistical Summary

Now finally, we can take a look at a summary of each attribute. This includes the mean, the min and max values as well as some percentiles.

```
# summarize attribute distributions
summary(dataset)
```

Listing 18.14: Summarize all attributes in the dataset.

We can see that all of the numerical values have the same scale (centimeters) and similar ranges [0,8] centimeters.

Sepal.Length Sepal.Width Petal.Length Petal.Width Species Min. :4.300 Min. :2.00 Min. :1.000 Min. :0.100 setosa :40 1st Qu.:5.100 1st Qu.:2.80 1st Qu.:1.575 1st Qu.:0.300 versicolor:40 Median :5.800 Median :3.00 Median :4.300 Median :1.350 virginica :40 Mean :5.834 Mean :3.07 Mean :3.748 Mean :1.213 3rd Qu.:6.400 3rd Qu.:3.40 3rd Qu.:5.100 3rd Qu.:1.800 Max. :7.900 Max. :4.40 Max. :6.900 Max. :2.500

Listing 18.15: Output of summary of all attributes in the dataset.

## 18.4 Visualize Dataset

We now have a basic idea about the data. We need to extend that with some visualizations. We are going to look at two types of plots:

- 1. Univariate plots to better understand each attribute.
- 2. Multivariate plots to better understand the relationships between attributes.

#### 18.4.1 Univariate Plots

We start with some univariate plots, that is, plots of each individual variable. It is helpful with visualization to have a way to refer to just the input attributes and just the output attributes. Let's set that up and call the inputs attributes x and the output attribute (or class) y.

```
# split input and output
x <- dataset[,1:4]
y <- dataset[,5]
```

Listing 18.16: Split dataset into input and output attributes.

Given that the input variables are numeric, we can create box and whisker plots of each.

```
# boxplot for each attribute on one image
par(mfrow=c(1,4))
 for(i in 1:4) {
 boxplot(x[,i], main=names(iris)[i])
}
```

Listing 18.17: Calculate box and whisker plots of data.

![](_page_5_Figure_14.jpeg)

Figure 18.1: Box and Whisker Plots pf Iris flowers data.

#### 18.4. Visualize Dataset 148

We can also create a bar plot of the Species class variable to get a graphical representation of the class distribution (generally uninteresting in this case because they're even).

# barplot for class breakdown plot(y)

Listing 18.18: Calculate bar plots of each level of the class attribute.

This confirms what we learned in the last section, that the instances are evenly distributed across the three classes:

![](_page_6_Figure_5.jpeg)

Figure 18.2: Bar Plots pf Iris flowers data.

### 18.4.2 Multivariate Plots

Now we can look at the interactions between the variables. First let's look at scatterplots of all pairs of attributes and color the points by class. In addition, because the scatterplots show that points for each class are generally separate, we can draw ellipses around them.

```
# scatterplot matrix
featurePlot(x=x, y=y, plot="ellipse")
```

Listing 18.19: Calculate a scatterplot matrix plot by class.

We can see some clear relationships between the input attributes (trends) and between attributes and the class values (ellipses):

We can also look at box and whisker plots of each input variable again, but this time broken down into separate plots for each class. This can help to tease out obvious linear separations between the classes.

```
# box and whisker plots for each attribute
featurePlot(x=x, y=y, plot="box")
```

![](_page_7_Figure_1.jpeg)

Figure 18.3: Scatterplot Matrix Iris flowers data by Class.

![](_page_7_Figure_3.jpeg)

Figure 18.4: Box and Whisker Plots Iris flowers data by Class.

This is useful as it shows that there are clearly different distributions of the attributes for each class value.

Next we can get an idea of the distribution of each attribute, again like the box and whisker plots, broken down by class value. Sometimes histograms are good for this, but in this case we will use some probability density plots to give nice smooth lines for each distribution.

```
# density plots for each attribute by class value
scales <- list(x=list(relation="free"), y=list(relation="free"))
featurePlot(x=x, y=y, plot="density", scales=scales)
```

![](_page_8_Figure_4.jpeg)

Like the boxplots, we can see the difference in distribution of each attribute by class value. We can also see the Gaussian-like distribution (bell curve) of each attribute.

![](_page_8_Figure_6.jpeg)

Figure 18.5: Density Plots of the Iris flowers data by Class.

## 18.5 Evaluate Some Algorithms

Now it is time to create some models of the data and estimate their accuracy on unseen data. Here is what we are going to cover in this step:

- 1. Set-up the test harness to use 10-fold cross validation.
- 2. Build 5 different models to predict species from flower measurements
- 3. Select the best model.

#### 18.5.1 Test Harness

We will use 10-fold cross validation to estimate accuracy. This will split our dataset into 10 parts, train in 9 and test on 1 and repeat for all combinations of train-test splits.

```
# Run algorithms using 10-fold cross validation
trainControl <- trainControl(method="cv", number=10)
metric <- "Accuracy"
```

Listing 18.22: Prepare the test harness for evaluating algorithms.

We are using the metric of Accuracy to evaluate models. This is a ratio of the number of correctly predicted instances divided by the total number of instances in the dataset multiplied by 100 to give a percentage (e.g. 95% accurate). We will be using the metric variable when we run build and evaluate each model next.

#### 18.5.2 Build Models

We don't know which algorithms would be good on this problem or what configurations to use. We do get an idea from the plots that some of the classes are partially linearly separable in some dimensions, so we are expecting generally good results. Let's evaluate 5 different algorithms:

- Linear Discriminant Analysis (LDA).
- Classification and Regression Trees (CART).
- k-Nearest Neighbors (KNN).
- Support Vector Machines (SVM) with a radial kernel.
- Random Forest (RF).

This is a good mixture of simple linear (LDA), non-linear (CART, KNN) and complex non-linear methods (SVM, RF). We reset the random number seed before reach run to ensure that the evaluation of each algorithm is performed using exactly the same data splits. It ensures the results are directly comparable. Let's build our five models:

```
# LDA
set.seed(7)
fit.lda <- train(Species~., data=dataset, method="lda", metric=metric,
   trControl=trainControl)
# CART
set.seed(7)
fit.cart <- train(Species~., data=dataset, method="rpart", metric=metric,
   trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(Species~., data=dataset, method="knn", metric=metric,
   trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(Species~., data=dataset, method="svmRadial", metric=metric,
   trControl=trainControl)
# Random Forest
```

```
set.seed(7)
fit.rf <- train(Species~., data=dataset, method="rf", metric=metric, trControl=trainControl)
```

Listing 18.23: Estimate the accuracy of a number of algorithms on the dataset.

The caret package does support the configuration and tuning of the configuration of each model, but we are not going to cover that in this tutorial.

#### 18.5.3 Select Best Model

We now have 5 models and accuracy estimations for each. We need to compare the models to each other and select the most accurate. We can report on the accuracy of each model by first creating a list of the models, gathering resample statistics and using the summary function on the result.

```
# summarize accuracy of models
results <- resamples(list(lda=fit.lda, cart=fit.cart, knn=fit.knn, svm=fit.svm, rf=fit.rf))
summary(results)
```

Listing 18.24: Calculate resample statistics from the models.

In the table of results, we can see the distribution of both the Accuracy and Kappa of the models. Let's just focus on Accuracy for now.

```
Models: lda, cart, knn, svm, rf
Number of resamples: 10
Accuracy
     Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
lda 0.9167 0.9375 1.0000 0.9750 1 1 0
cart 0.8333 0.9167 0.9167 0.9417 1 1 0
knn 0.8333 0.9167 1.0000 0.9583 1 1 0
svm 0.8333 0.9167 0.9167 0.9417 1 1 0
rf 0.8333 0.9167 0.9583 0.9500 1 1 0
Kappa
    Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
lda 0.875 0.9062 1.0000 0.9625 1 1 0
cart 0.750 0.8750 0.8750 0.9125 1 1 0
knn 0.750 0.8750 1.0000 0.9375 1 1 0
svm 0.750 0.8750 0.8750 0.9125 1 1 0
rf 0.750 0.8750 0.9375 0.9250 1 1 0
```

Listing 18.25: Output of resample statistics for the models.

We can also create a plot of the model evaluation results and compare the spread and the mean accuracy of each model. There is a population of accuracy measures for each algorithm because each algorithm was evaluated 10 times (10 fold cross validation).

# compare accuracy of models dotplot(results)

Listing 18.26: Calculate dot plots of estimated model accuracy.

The results for just the LDA model can be summarized.

#### 18.5. Evaluate Some Algorithms 153

![](_page_11_Figure_1.jpeg)

Figure 18.6: Comparison of Machine Learning Algorithms on Iris Dataset in R.

```
# summarize Best Model
print(fit.lda)
```

Listing 18.27: Display the estimated accuracy of a model.

This gives a nice summary of what was used to train the model and the mean and standard deviation (SD) accuracy achieved, specifically 97.5% accuracy +/- 4%.

```
Linear Discriminant Analysis
120 samples
 4 predictor
 3 classes: 'setosa', 'versicolor', 'virginica'
No pre-processing
Resampling: Cross-Validated (10 fold)
Summary of sample sizes: 108, 108, 108, 108, 108, 108, ...
Resampling results
 Accuracy Kappa Accuracy SD Kappa SD
 0.975 0.9625 0.04025382 0.06038074
```

Listing 18.28: Output estimated accuracy of a model.

# 18.6 Make Predictions

The LDA algorithm created the most accurate model. Now we want to get an idea of the accuracy of the model on our validation set. This will give us an independent final check on the accuracy of the best model. It is valuable to keep a validation set just in case you made a slip during such as overfitting to the training set or a data leak. Both will result in an overly optimistic result. We can run the LDA model directly on the validation set and summarize the results in a confusion matrix.

```
# estimate skill of LDA on the validation dataset
predictions <- predict(fit.lda, validation)
confusionMatrix(predictions, validation$Species)
```

Listing 18.29: Calculate predictions on unseen data.

We can see that the accuracy is 100%. It was a small validation dataset, but this result is within our expected margin of 97% +/-4% suggesting we may have an accurate and a reliably accurate model.

```
Confusion Matrix and Statistics
       Reference
Prediction setosa versicolor virginica
 setosa 10 0 0
 versicolor 0 10 0
 virginica 0 0 10
Overall Statistics
         Accuracy : 1
          95% CI : (0.8843, 1)
  No Information Rate : 0.3333
  P-Value [Acc > NIR] : 4.857e-15
           Kappa : 1
Mcnemar's Test P-Value : NA
Statistics by Class:
             Class: setosa Class: versicolor Class: virginica
Sensitivity 1.0000 1.0000 1.0000
Specificity 1.0000 1.0000 1.0000
Pos Pred Value 1.0000 1.0000 1.0000
Neg Pred Value 1.0000 1.0000 1.0000
Prevalence 0.3333 0.3333 0.3333
Detection Rate 0.3333 0.3333 0.3333
Detection Prevalence 0.3333 0.3333 0.3333
Balanced Accuracy 1.0000 1.0000 1.0000
```

Listing 18.30: Output of predictions on unseen data.

# 18.7 Summary

In this lesson you discovered step-by-step how to complete your first machine learning project in R. You discovered that completing a small end-to-end project from loading the data to making predictions is the best way to get familiar with a new platform.

## 18.7.1 Next Step

You have applied the lessons from Part II on a simple problem and completed your first machine learning project. Next you take things one step further and work through a regression predictive modeling problem. It will be a slightly more complex project and involve data transforms, algorithm tuning and use of ensemble methods to improve results.
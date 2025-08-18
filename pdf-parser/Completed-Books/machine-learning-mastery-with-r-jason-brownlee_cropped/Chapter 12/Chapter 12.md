# Chapter 12

# Spot-Check Machine Learning Algorithms

What algorithm should you use on your dataset? This is the most common question in applied machine learning. It's a question that can only be answered by trial and error, or what I call: spot-checking algorithms. In this lesson you will discover how to spot-check algorithms on a dataset using R. After completing this lesson, you will know:

- 1. How to model data with linear and non-linear machine learning algorithms directly.
- 2. How to spot-check a suite of linear and non-linear algorithms using caret.
- 3. Which linear and non-linear algorithms to start with on a new project.

Let's get started.

## 12.1 Best Algorithm For a Problem

You want the most accurate model for your dataset. That is the goal of predictive modeling. No one can tell you what algorithm to use on your dataset to get the best results. If you or anyone knew what algorithm gave the best results for a specific dataset, then you probably would not need to use machine learning in the first place because of your deep knowledge of the problem.

We cannot know beforehand the best algorithm representation or learning algorithm for that representation to use. We don't even know the best parameters to use for algorithms that we could try. We need a strategy to find the best algorithm for our dataset.

#### 12.1.1 Use Past Experience To Choose An Algorithm

One way that you could choose an algorithm for a problem is to rely on experience. This could be your experience with working on similar problems in the past. It could also be the collective experience of the field where you refer to papers, books and other resources for similar problems to get an idea of what algorithms have worked well in the past. This is a good start, but this should not be where you stop.

#### 12.1.2 Use Trial And Error To Choose An Algorithm

The most robust way to discover good or even best algorithms for your dataset is by trial and error. Evaluate a diverse set of algorithms on your dataset and see what works and drop what doesn't. I call this process spot-checking algorithms.

Once you have a shortlist of algorithms that you know are good at picking out the structure of your problem, you can focus your efforts on those algorithms. You can improve the results of candidate algorithms by either tuning the algorithm parameters or by combining the predictions of multiple models using ensemble methods. Next, let's take a look at how we can evaluate multiple machine algorithms on a dataset in R.

#### 12.1.3 Which Algorithms To Spot-Check

You can guess at what algorithms might do well on your dataset, and this can be a good starting point. I recommend trying a mixture of algorithms and see what is good at picking out the structure in your data.

- Try a mixture of algorithm representations (e.g. instance-based methods and trees).
- Try a mixture of learning algorithms (e.g. different algorithms for learning the same type of representation).
- Try a mixture of modeling types (e.g. linear and non-linear functions or parametric and non-parametric).

Let's get specific. In the next section, we will look at algorithms that you can use to spot-check on your next machine learning project in R.

## 12.2 Algorithms To Spot-Check in R

There are hundreds of machine learning algorithms available in R. I would recommend exploring many of them, especially, if making accurate predictions on your dataset is important and you have the time. Often you don't have the time, so you need to know the few algorithms that you absolutely must test on your problem.

In this lesson you will discover the linear and non-linear algorithms you should spot-check on your problem in R. This excludes ensemble algorithms such as boosting and bagging, that can come later once you have a baseline. Each algorithm will be presented from two perspectives:

- 1. The package and function used to train and make predictions for the algorithm.
- 2. The wrapper in the caret package for the algorithm.

You need to know which package and function to use for a given algorithm. This is needed when you are researching the algorithm parameters and how to get the most from the algorithm. It is also needed when you have discovered the best algorithm to use and need to prepare a final model.

You need to know how to use each algorithm with the caret package, so that you can efficiently evaluate the accuracy of the algorithm on unseen data using the pre-processing, algorithm evaluation and tuning capabilities of caret. Two standard datasets first described in Chapter 5 are used to demonstrate algorithms in this lesson:

- Boston Housing dataset for regression (BostonHousing from the mlbench package).
- Pima Indians Diabetes dataset for classification (PimaIndiansDiabetes from the mlbench package).

Algorithms are presented in two groups:

- Linear Algorithms that are simpler methods that have a strong bias but are fast to train.
- Non-linear Algorithms that are more complex methods that have a large variance but are often more accurate.

Each recipe presented in this lesson is complete and will produce a result, so that you can copy and paste it into your current or next machine learning project.

## 12.3 Linear Algorithms

These are methods that make large assumptions about the form of the function being modeled. As such they have a high bias but are often fast to train. The final models are also often easy (or easier) to interpret, making them desirable as final models. If the results are suitably accurate, you may not need to move onto using non-linear methods.

#### 12.3.1 Linear Regression

The lm() function is in the stats package and creates a linear regression model using ordinary least squares.

```
# load the package
library(mlbench)
# load data
data(BostonHousing)
# fit model
fit <- lm(medv~., BostonHousing)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, BostonHousing)
# summarize accuracy
mse <- mean((BostonHousing$medv - predictions)^2)
print(mse)
```

Listing 12.1: Example of linear regression algorithm.

The lm implementation can be used in caret as follows:

```
# load packages
library(caret)
library(mlbench)
# load dataset
data(BostonHousing)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
```

```
fit.lm <- train(medv~., data=BostonHousing, method="lm", metric="RMSE", preProc=c("center",
   "scale"), trControl=trainControl)
# summarize fit
print(fit.lm)
```

Listing 12.2: Example of linear regression algorithm in caret.

### 12.3.2 Logistic Regression

The glm() function is in the stats package and creates a generalized linear model for regression or classification. It can be configured to perform a logistic regression suitable for binary classification problems.

```
# load the package
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# fit model
fit <- glm(diabetes~., data=PimaIndiansDiabetes, family=binomial(link='logit'))
# summarize the fit
print(fit)
# make predictions
probabilities <- predict(fit, PimaIndiansDiabetes[,1:8], type='response')
predictions <- ifelse(probabilities > 0.5,'pos','neg')
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.3: Example of logistic regression algorithm.

The glm algorithm can be used in caret as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.glm <- train(diabetes~., data=PimaIndiansDiabetes, method="lm", metric="Accuracy",
   preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.glm)
```

Listing 12.4: Example of ogistic regression algorithm in caret.

### 12.3.3 Linear Discriminant Analysis

The lda() function is in the MASS package and creates a linear model of a classification problem.

```
# load the packages
library(MASS)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
```

#### 12.3. Linear Algorithms 86

```
# fit model
fit <- lda(diabetes~., data=PimaIndiansDiabetes)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, PimaIndiansDiabetes[,1:8])$class
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.5: Example of LDA algorithm.

The lda algorithm can be used in caret as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.lda <- train(diabetes~., data=PimaIndiansDiabetes, method="lda", metric="Accuracy",
   preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.lda)
```

Listing 12.6: Example of LDA algorithm in caret.

### 12.3.4 Regularized Regression

The glmnet() function is in the glmnet package and can be used for classification or regression. Classification Example:

```
# load the package
library(glmnet)
library(mlbench)
# load data
data(PimaIndiansDiabetes)
x <- as.matrix(PimaIndiansDiabetes[,1:8])
y <- as.matrix(PimaIndiansDiabetes[,9])
# fit model
fit <- glmnet(x, y, family="binomial", alpha=0.5, lambda=0.001)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, x, type="class")
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.7: Example of GLMNET algorithm for classification.

Regression Example:

```
# load the packages
library(glmnet)
library(mlbench)
```

#### 12.3. Linear Algorithms 87

```
# load data
data(BostonHousing)
BostonHousing$chas <- as.numeric(as.character(BostonHousing$chas))
x <- as.matrix(BostonHousing[,1:13])
y <- as.matrix(BostonHousing[,14])
# fit model
fit <- glmnet(x, y, family="gaussian", alpha=0.5, lambda=0.001)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, x, type="link")
# summarize accuracy
mse <- mean((y - predictions)^2)
print(mse)
```

Listing 12.8: Example of GLMNET algorithm for regression.

It can also be configured to perform three important types of regularization: lasso, ridge and elastic net by configuring the alpha parameter to 1, 0 or in [0,1] respectively. The glmnet implementation can be used in caret for classification as follows:

```
# load packages
library(caret)
library(mlbench)
library(glmnet)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.glmnet <- train(diabetes~., data=PimaIndiansDiabetes, method="glmnet",
   metric="Accuracy", preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.glmnet)
```

Listing 12.9: Example of GLMNET algorithm for classification in caret.

The glmnet implementation can be used in caret for regression as follows:

```
# load packages
library(caret)
library(mlbench)
library(glmnet)
# Load the dataset
data(BostonHousing)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.glmnet <- train(medv~., data=BostonHousing, method="glmnet", metric="RMSE",
   preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.glmnet)
```

Listing 12.10: Example of GLMNET algorithm for regression.

## 12.4 Non-linear Algorithms

These are machine learning algorithms that make fewer assumptions about the underlying function being modeled. As such, they have a higher variance but are often result in higher accuracy. They increased flexibility also can make them slower to train or increase their memory requirements.

#### 12.4.1 k-Nearest Neighbors

The knn3() function is in the caret package and does not create a model, rather makes predictions from the training set directly. It can be used for classification or regression.

Classification Example:

```
# load the packages
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# fit model
fit <- knn3(diabetes~., data=PimaIndiansDiabetes, k=3)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, PimaIndiansDiabetes[,1:8], type="class")
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.11: Example of KNN algorithm for classification.

Regression Example:

```
# load the packages
library(caret)
library(mlbench)
# load data
data(BostonHousing)
BostonHousing$chas <- as.numeric(as.character(BostonHousing$chas))
x <- as.matrix(BostonHousing[,1:13])
y <- as.matrix(BostonHousing[,14])
# fit model
fit <- knnreg(x, y, k=3)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, x)
# summarize accuracy
mse <- mean((BostonHousing$medv - predictions)^2)
print(mse)
```

Listing 12.12: Example of KNN algorithm for regression.

The knn3 implementation can be used within the caret train() function for classification as follows:

```
# load packages
library(caret)
```

```
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.knn <- train(diabetes~., data=PimaIndiansDiabetes, method="knn", metric="Accuracy",
   preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.knn)
```

Listing 12.13: Example of KNN algorithm for classification in caret.

The knn3 implementation can be used within the caret train() function for regression as follows:

```
# load packages
library(caret)
data(BostonHousing)
# Load the dataset
data(BostonHousing)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.knn <- train(medv~., data=BostonHousing, method="knn", metric="RMSE",
   preProc=c("center", "scale"), trControl=trainControl)
# summarize fit
print(fit.knn)
```

Listing 12.14: Example of KNN algorithm for regression in caret.

#### 12.4.2 Naive Bayes

The naiveBayes() function is in the e1071 package and models the probabilities of each attribute to the outcome variable independently. It can be used for classification problems.

```
# load the packages
library(e1071)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# fit model
fit <- naiveBayes(diabetes~., data=PimaIndiansDiabetes)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, PimaIndiansDiabetes[,1:8])
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.15: Example of Naive Bayes algorithm for classification.

A very similar naive Bayes implementation (NaiveBayes from the klaR package) can be used with the caret package as follows:

```
# load packages
```

```
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.nb <- train(diabetes~., data=PimaIndiansDiabetes, method="nb", metric="Accuracy",
   trControl=trainControl)
# summarize fit
print(fit.nb)
```

Listing 12.16: Example of Naive Bayes algorithm for classification in caret.

### 12.4.3 Support Vector Machine

The ksvm() function is in the kernlab package and can be used for classification or regression. It is a wrapper for the LIBSVM software package and provides a suite of kernel types and configuration options. These examples uses a Radial Basis kernel.

Classification Example:

```
# load the packages
library(kernlab)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# fit model
fit <- ksvm(diabetes~., data=PimaIndiansDiabetes, kernel="rbfdot")
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, PimaIndiansDiabetes[,1:8], type="response")
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.17: Example of SVM algorithm for classification.

Regression Example:

```
# load the packages
library(kernlab)
library(mlbench)
# load data
data(BostonHousing)
# fit model
fit <- ksvm(medv~., BostonHousing, kernel="rbfdot")
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, BostonHousing)
# summarize accuracy
mse <- mean((BostonHousing$medv - predictions)^2)
print(mse)
```

Listing 12.18: Example of SVM algorithm for regression.

The SVM with Radial Basis kernel implementation can be used with caret for classification as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.svmRadial <- train(diabetes~., data=PimaIndiansDiabetes, method="svmRadial",
   metric="Accuracy", trControl=trainControl)
# summarize fit
print(fit.svmRadial)
```

Listing 12.19: Example of SVM algorithm for classification in caret.

The SVM with Radial Basis kernel implementation can be used with caret for regression as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(BostonHousing)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.svmRadial <- train(medv~., data=BostonHousing, method="svmRadial", metric="RMSE",
   trControl=trainControl)
# summarize fit
print(fit.svmRadial)
```

Listing 12.20: Example of SVM algorithm for regression in caret.

#### 12.4.4 Classification and Regression Trees

The rpart() function in the rpart package provides an implementation of CART (Classification And Regression Trees) for classification and regression.

Classification Example:

```
# load the packages
library(rpart)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# fit model
fit <- rpart(diabetes~., data=PimaIndiansDiabetes)
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, PimaIndiansDiabetes[,1:8], type="class")
# summarize accuracy
table(predictions, PimaIndiansDiabetes$diabetes)
```

Listing 12.21: Example of CART algorithm for classification.

Regression Example:

```
# load the packages
library(rpart)
library(mlbench)
# load data
data(BostonHousing)
# fit model
fit <- rpart(medv~., data=BostonHousing, control=rpart.control(minsplit=5))
# summarize the fit
print(fit)
# make predictions
predictions <- predict(fit, BostonHousing[,1:13])
# summarize accuracy
mse <- mean((BostonHousing$medv - predictions)^2)
print(mse)
```

Listing 12.22: Example of CART algorithm for regression.

The rpart implementation can be used with caret for classification as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(PimaIndiansDiabetes)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=5)
fit.rpart <- train(diabetes~., data=PimaIndiansDiabetes, method="rpart", metric="Accuracy",
   trControl=trainControl)
# summarize fit
print(fit.rpart)
```

Listing 12.23: Example of CART algorithm for classification in caret.

The rpart implementation can be used with caret for regression as follows:

```
# load packages
library(caret)
library(mlbench)
# Load the dataset
data(BostonHousing)
# train
set.seed(7)
trainControl <- trainControl(method="cv", number=2)
fit.rpart <- train(medv~., data=BostonHousing, method="rpart", metric="RMSE",
   trControl=trainControl)
# summarize fit
print(fit.rpart)
```

Listing 12.24: Example of CART algorithm for regression in caret.

## 12.5 Other Algorithms

There are many other algorithms provided by R and available in caret. I would advise you to explore them and add more algorithms to your own shortlist of must-try algorithms on your next machine learning project. You can find a mapping of machine learning functions and packages to their name in the caret package on the Caret Model List webpage<sup>1</sup> .

This page is useful if you are using an algorithm in caret and want to know which package it belongs to so that you can read up on the parameters and get more out of it. This page is also useful if you are using a machine learning algorithm directly in R and want to know how it can be used in caret.

## 12.6 Summary

In this lesson you discovered a diverse set of 8 algorithms that you can use to spot-check on your datasets. Specifically:

- Linear Regression.
- Logistic Regression.
- Linear Discriminant Analysis.
- Regularized Regression.
- k-Nearest Neighbors.
- Naive Bayes.
- Support Vector Machine.
- Classification and Regression Trees.

You learned which packages and functions to use for each algorithm. You also learned how you can use each algorithm with the caret package that provides algorithm evaluation and tuning capabilities. You can use these algorithms as a template for spot-checking on your current or next machine learning project in R.

#### 12.6.1 Next Step

You have learned how to evaluate the skill of models, metrics and how to run the algorithms themselves. In the next lesson you will discover how you can tie all three of these elements together on a predictive modeling project and compare and choose between multiple skillful models on your dataset.

<sup>1</sup><https://topepo.github.io/caret/modelList.html>
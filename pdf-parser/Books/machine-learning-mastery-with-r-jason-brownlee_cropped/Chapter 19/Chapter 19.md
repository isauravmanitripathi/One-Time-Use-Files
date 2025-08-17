# Chapter 19

# Regression Machine Learning Case Study Project

How do you work through a predictive modeling machine learning problem end-to-end? In this lesson you will work through a case study regression predictive modeling problem in R including each step of the applied machine learning process. After completing this project, you will know:

- 1. How to work through a regression predictive modeling problem end-to-end.
- 2. How to use data transforms to improve model performance.
- 3. How to use algorithm tuning to improve model performance.
- 4. How to use ensemble methods and tuning of ensemble methods to improve model performance.

Let's get started.

## 19.1 Problem Definition

For this project we will investigate the Boston House Price dataset described in Chapter 5. Each record in the database describes a Boston suburb or town. The data was drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970. The attributes are defined as follows (taken from the UCI Machine Learning Repository):

- 1. CRIM: per capita crime rate by town
- 2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
- 3. INDUS: proportion of non-retail business acres per town
- 4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- 5. NOX: nitric oxides concentration (parts per 10 million)
- 6. RM: average number of rooms per dwelling
- 7. AGE: proportion of owner-occupied units built prior to 1940

- 8. DIS: weighted distances to five Boston employment centers
- 9. RAD: index of accessibility to radial highways
- 10. TAX: full-value property-tax rate per \$10,000
- 11. PTRATIO: pupil-teacher ratio by town
- 12. B: 1000(Bk 0.63)ˆ2 where Bk is the proportion of blacks by town
- 13. LSTAT: % lower status of the population
- 14. MEDV: Median value of owner-occupied homes in \$1000s

We can see that the input attributes have a mixture of units.

### 19.1.1 Load the Dataset

The dataset is available in the mlbench package. Let's start off by loading the required packages and loading the dataset.

```
# load packages
library(mlbench)
library(caret)
library(corrplot)
# attach the BostonHousing dataset
data(BostonHousing)
```

Listing 19.1: Load packages and the dataset.

### 19.1.2 Validation Dataset

It is a good idea to use a validation hold out set. This is a sample of the data that we hold back from our analysis and modeling. We use it right at the end of our project to confirm the accuracy of our final model. It is a smoke test that we can use to see if we messed up and to give us confidence on our estimates of accuracy on unseen data.

```
# Split out validation dataset
# create a list of 80% of the rows in the original dataset we can use for training
set.seed(7)
validationIndex <- createDataPartition(BostonHousing$medv, p=0.80, list=FALSE)
# select 20% of the data for validation
validation <- BostonHousing[-validationIndex,]
# use the remaining 80% of data to training and testing the models
dataset <- BostonHousing[validationIndex,]
```

Listing 19.2: Separate the dataset into a training and validation sets.

# 19.2 Analyze Data

The objective of this step in the process is to better understand the problem.

### 19.2.1 Descriptive Statistics

Let's start off by confirming the dimensions of the dataset, e.g. the number of rows and columns.

```
# dimensions of dataset
dim(dataset)
```

Listing 19.3: Caluclate the dimensions of the dataset.

We have 407 instances to work with and can confirm the data has 14 attributes including the class attribute medv.

```
407 14
```

Listing 19.4: Outoput of the the dimensions of the dataset.

Let's also look at the data types of each attribute.

# list types for each attribute sapply(dataset, class)

Listing 19.5: Caluclate the attribute data types.

We can see that one of the attributes (chas) is a factor while all of the others are numeric.

crim zn indus chas nox rm age dis rad tax ptratio b "numeric" "numeric" "numeric" "factor" "numeric" "numeric" "numeric" "numeric" "numeric" "numeric" "numeric" "numeric" lstat medv "numeric" "numeric"

Listing 19.6: Output of the attribute data types.

Let's now take a peak at the first 20 rows of the data.

|                     |  |  | # take a peek at the first 5 rows of the data |  |  |  |
|---------------------|--|--|-----------------------------------------------|--|--|--|
| head(dataset, n=20) |  |  |                                               |  |  |  |

Listing 19.7: Peek at the first few rows of data.

We can confirm that the scales for the attributes are all over the place because of the differing units. We may benefit from some transforms later on.

|   | crim                 | zn indus chas | nox<br>rm                        | age |  | dis rad tax ptratio |                        | b lstat medv |  |
|---|----------------------|---------------|----------------------------------|-----|--|---------------------|------------------------|--------------|--|
| 2 | 0.02731 0.0          | 7.07          | 0 0.469 6.421 78.9 4.9671 2 242  |     |  |                     | 17.8 396.90 9.14 21.6  |              |  |
| 3 | 0.02729 0.0          | 7.07          | 0 0.469 7.185 61.1 4.9671 2 242  |     |  |                     | 17.8 392.83 4.03 34.7  |              |  |
| 4 | 0.03237 0.0          | 2.18          | 0 0.458 6.998 45.8 6.0622 3 222  |     |  |                     | 18.7 394.63 2.94 33.4  |              |  |
| 5 | 0.06905 0.0          | 2.18          | 0 0.458 7.147 54.2 6.0622 3 222  |     |  |                     | 18.7 396.90 5.33 36.2  |              |  |
| 6 | 0.02985 0.0          | 2.18          | 0 0.458 6.430 58.7 6.0622 3 222  |     |  |                     | 18.7 394.12 5.21 28.7  |              |  |
| 7 | 0.08829 12.5 7.87    |               | 0 0.524 6.012 66.6 5.5605 5 311  |     |  |                     | 15.2 395.60 12.43 22.9 |              |  |
| 8 | 0.14455 12.5 7.87    |               | 0 0.524 6.172 96.1 5.9505 5 311  |     |  |                     | 15.2 396.90 19.15 27.1 |              |  |
| 9 | 0.21124 12.5 7.87    |               | 0 0.524 5.631 100.0 6.0821 5 311 |     |  |                     | 15.2 386.63 29.93 16.5 |              |  |
|   | 13 0.09378 12.5 7.87 |               | 0 0.524 5.889 39.0 5.4509 5 311  |     |  |                     | 15.2 390.50 15.71 21.7 |              |  |
|   | 14 0.62976 0.0       | 8.14          | 0 0.538 5.949 61.8 4.7075 4 307  |     |  |                     | 21.0 396.90 8.26 20.4  |              |  |
|   | 15 0.63796 0.0       | 8.14          | 0 0.538 6.096 84.5 4.4619 4 307  |     |  |                     | 21.0 380.02 10.26 18.2 |              |  |
|   | 16 0.62739 0.0       | 8.14          | 0 0.538 5.834 56.5 4.4986 4 307  |     |  |                     | 21.0 395.62 8.47 19.9  |              |  |
|   | 17 1.05393 0.0       | 8.14          | 0 0.538 5.935 29.3 4.4986 4 307  |     |  |                     | 21.0 386.85 6.58 23.1  |              |  |
|   | 18 0.78420 0.0       | 8.14          | 0 0.538 5.990 81.7 4.2579 4 307  |     |  |                     | 21.0 386.75 14.67 17.5 |              |  |
|   | 19 0.80271 0.0       | 8.14          | 0 0.538 5.456 36.6 3.7965 4 307  |     |  |                     | 21.0 288.99 11.69 20.2 |              |  |

| 20 0.72580 0.0 | 8.14 |  |  | 0 0.538 5.727 69.5 3.7965 4 307 |  | 21.0 390.95 11.28 18.2 |  |
|----------------|------|--|--|---------------------------------|--|------------------------|--|
| 23 1.23247 0.0 | 8.14 |  |  | 0 0.538 6.142 91.7 3.9769 4 307 |  | 21.0 396.90 18.72 15.2 |  |
| 25 0.75026 0.0 | 8.14 |  |  | 0 0.538 5.924 94.1 4.3996 4 307 |  | 21.0 394.33 16.30 15.6 |  |
| 26 0.84054 0.0 | 8.14 |  |  | 0 0.538 5.599 85.7 4.4546 4 307 |  | 21.0 303.42 16.51 13.9 |  |
| 27 0.67191 0.0 | 8.14 |  |  | 0 0.538 5.813 90.3 4.6820 4 307 |  | 21.0 376.88 14.81 16.6 |  |

Listing 19.8: Output of the first few rows of data.

Let's summarize the distribution of each attribute.

|                  | # summarize attribute distributions |
|------------------|-------------------------------------|
| summary(dataset) |                                     |

Listing 19.9: Calculate a summary of each attribute.

We can note that chas is a pretty unbalanced factor. We could transform this attribute to numeric to make calculating descriptive statistics and plots easier.

| crim                                         | zn              | indus          | chas           | nox               | rm<br>age               |
|----------------------------------------------|-----------------|----------------|----------------|-------------------|-------------------------|
| Min.<br>: 0.00906<br>2.90                    | Min.<br>: 0.00  | Min.<br>: 0.46 | 0:376<br>Min.  | :0.3850<br>Min.   | :3.863<br>Min.<br>:     |
| 1st Qu.: 0.08556 1st Qu.: 0.00<br>Qu.: 45.05 |                 | 1st Qu.: 5.19  | 1: 31          | 1st Qu.:0.4530    | 1st Qu.:5.873<br>1st    |
| Median : 0.28955 Median : 0.00<br>: 77.70    |                 | Median : 9.90  |                | Median :0.5380    | Median :6.185<br>Median |
| Mean<br>: 3.58281<br>68.83                   | Mean<br>:10.57  | Mean<br>:11.36 | Mean           | :0.5577<br>Mean   | :6.279<br>Mean<br>:     |
| 3rd Qu.: 3.50464 3rd Qu.: 0.00<br>Qu.: 94.55 |                 | 3rd Qu.:18.10  |                | 3rd Qu.:0.6310    | 3rd Qu.:6.611<br>3rd    |
| Max.<br>:88.97620                            | Max.<br>:95.00  | Max.<br>:27.74 | Max.           | :0.8710<br>Max.   | :8.780<br>Max.          |
| :100.00                                      |                 |                |                |                   |                         |
| dis                                          | rad             | tax            | ptratio        | b                 | lstat                   |
|                                              | medv            |                |                |                   |                         |
| Min.<br>: 1.130                              | Min.<br>: 1.000 | Min.<br>:188.0 | Min.<br>:12.60 | Min.<br>:<br>0.32 | Min.<br>: 1.730         |
| Min.<br>: 5.00                               |                 |                |                |                   |                         |
| 1st Qu.: 2.031                               | 1st Qu.: 4.000  | 1st Qu.:279.0  | 1st Qu.:17.40  | 1st Qu.:374.50    | 1st Qu.: 6.895          |
| 1st Qu.:17.05                                |                 |                |                |                   |                         |
| Median : 3.216                               | Median : 5.000  | Median :330.0  | Median :19.00  | Median :391.13    | Median :11.500          |
| Median :21.20                                |                 |                |                |                   |                         |
| Mean<br>: 3.731<br>Mean<br>:22.61            | Mean<br>: 9.464 | Mean<br>:405.6 | Mean<br>:18.49 | Mean<br>:357.88   | Mean<br>:12.827         |
| 3rd Qu.: 5.100                               | 3rd Qu.:24.000  | 3rd Qu.:666.0  | 3rd Qu.:20.20  | 3rd Qu.:396.27    | 3rd Qu.:17.175          |
| 3rd Qu.:25.00                                |                 |                |                |                   |                         |
| Max.<br>:10.710                              | Max.<br>:24.000 | Max.<br>:711.0 | Max.<br>:22.00 | Max.<br>:396.90   | Max.<br>:37.970         |
| Max.<br>:50.00                               |                 |                |                |                   |                         |

Listing 19.10: Output of the summary of each attribute.

Let's go ahead and convert chas to a numeric attribute.

dataset[,4] <- as.numeric(as.character(dataset[,4]))

Listing 19.11: Covert an attribute to a numeric type.

Now, let's now take a look at the correlation between all of the numeric attributes.

cor(dataset[,1:13])

Listing 19.12: Calculate the correlation between attributes.

This is interesting. We can see that many of the attributes have a strong correlation (e.g. > 0.70 or < 0.70). For example:

- nox and indus with 0.77.
- dist and indus with 0.71.
- tax and indus with 0.72.
- age and nox with 0.72.
- dist and nox with 0.76.

|       | crim                                                                                  | zn  | indus | chas    | nox | rm    | age | dis |
|-------|---------------------------------------------------------------------------------------|-----|-------|---------|-----|-------|-----|-----|
|       |                                                                                       | rad | tax   | ptratio | b   | lstat |     |     |
| crim  | 1.00000000 -0.19790631 0.40597009 -0.05713065 0.4232413 -0.21513269 0.3543819         |     |       |         |     |       |     |     |
|       | -0.3905097 0.64240501 0.60622608 0.2892983 -0.3021185 0.47537617                      |     |       |         |     |       |     |     |
| zn    | -0.19790631 1.00000000 -0.51895069 -0.04843477 -0.5058512 0.28942883 -0.5707027       |     |       |         |     |       |     |     |
|       | 0.6561874 -0.29952976 -0.28791668 -0.3534121 0.1692749 -0.39712686                    |     |       |         |     |       |     |     |
| indus | 0.40597009 -0.51895069 1.00000000 0.08003629 0.7665481 -0.37673408 0.6585831          |     |       |         |     |       |     |     |
|       | -0.7230588 0.56774365 0.68070916 0.3292061 -0.3359795 0.59212718                      |     |       |         |     |       |     |     |
| chas  | -0.05713065 -0.04843477 0.08003629 1.00000000 0.1027366 0.08252441 0.1093812          |     |       |         |     |       |     |     |
|       | -0.1114242 -0.00901245 -0.02779018 -0.1355438 0.0472442 -0.04569239                   |     |       |         |     |       |     |     |
| nox   | 0.42324132 -0.50585121 0.76654811 0.10273656 1.0000000 -0.29885055 0.7238371          |     |       |         |     |       |     |     |
|       | -0.7708680 0.58516760 0.65217875 0.1416616 -0.3620791 0.58196447                      |     |       |         |     |       |     |     |
| rm    | -0.21513269 0.28942883 -0.37673408 0.08252441 -0.2988506 1.00000000 -0.2325359        |     |       |         |     |       |     |     |
|       | 0.1952159 -0.19149122 -0.26794733 -0.3200037 0.1553992 -0.62038075                    |     |       |         |     |       |     |     |
| age   | 0.35438190 -0.57070265 0.65858310 0.10938121 0.7238371 -0.23253586 1.0000000          |     |       |         |     |       |     |     |
|       | -0.7503321 0.45235421 0.50164657 0.2564318 -0.2512574 0.59321281                      |     |       |         |     |       |     |     |
| dis   | -0.39050970 0.65618742 -0.72305885 -0.11142420 -0.7708680 0.19521590 -0.7503321       |     |       |         |     |       |     |     |
|       | 1.0000000 -0.49382744 -0.52649325 -0.2021897 0.2826819 -0.49573024                    |     |       |         |     |       |     |     |
| rad   | 0.64240501 -0.29952976 0.56774365 -0.00901245 0.5851676 -0.19149122 0.4523542         |     |       |         |     |       |     |     |
|       | -0.4938274 1.00000000 0.92137876 0.4531232 -0.4103307 0.47306604                      |     |       |         |     |       |     |     |
| tax   | 0.60622608 -0.28791668 0.68070916 -0.02779018 0.6521787 -0.26794733 0.5016466         |     |       |         |     |       |     |     |
|       | -0.5264932 0.92137876 1.00000000 0.4419243 -0.4184878 0.52339243                      |     |       |         |     |       |     |     |
|       | ptratio 0.28929828 -0.35341215 0.32920610 -0.13554380 0.1416616 -0.32000372 0.2564318 |     |       |         |     |       |     |     |
|       | -0.2021897 0.45312318 0.44192428 1.0000000 -0.1495283 0.35375936                      |     |       |         |     |       |     |     |
| b     | -0.30211854 0.16927489 -0.33597951 0.04724420 -0.3620791 0.15539923 -0.2512574        |     |       |         |     |       |     |     |
|       | 0.2826819 -0.41033069 -0.41848779 -0.1495283 1.0000000 -0.37661571                    |     |       |         |     |       |     |     |
| lstat | 0.47537617 -0.39712686 0.59212718 -0.04569239 0.5819645 -0.62038075 0.5932128         |     |       |         |     |       |     |     |
|       | -0.4957302 0.47306604 0.52339243 0.3537594 -0.3766157 1.00000000                      |     |       |         |     |       |     |     |

Listing 19.13: Output of the correlation between attributes.

This is collinearity and we may see better results with regression algorithms if the correlated attributes are removed.

### 19.2.2 Unimodal Data Visualizations

Let's look at visualizations of individual attributes. It is often useful to look at your data using multiple different visualizations in order to spark ideas. Let's look at histograms of each attribute to get a sense of the data distributions.

```
# histograms each attribute
par(mfrow=c(2,7))
for(i in 1:13) {
 hist(dataset[,i], main=names(dataset)[i])
}
```

Listing 19.14: Calculate histograms.

We can see that some attributes may have an exponential distribution, such as crim, zn, ange and b. We can see that others may have a bimodal distribution such as rad and tax.

![](_page_5_Figure_4.jpeg)

Figure 19.1: Histograms of Boston House Dataset Input Attributes

Let's look at the same distributions using density plots that smooth them out a bit.

```
# density plot for each attribute
par(mfrow=c(2,7))
for(i in 1:13) {
 plot(density(dataset[,i]), main=names(dataset)[i])
}
```

Listing 19.15: Calculate density plots.

This perhaps adds more evidence to our suspicion about possible exponential and bimodal distributions. It also looks like nox, rm and lsat may be skewed Gaussian distributions, which might be helpful later with transforms.

Let's look at the data with box and whisker plots of each attribute.

```
# boxplots for each attribute
par(mfrow=c(2,7))
for(i in 1:13) {
 boxplot(dataset[,i], main=names(dataset)[i])
```

![](_page_6_Figure_1.jpeg)

Figure 19.2: Density plots of Boston House Dataset Input Attributes

}

Listing 19.16: Calculate box and whisker plots.

This helps point out the skew in many distributions so much so that data looks like outliers (e.g. beyond the whisker of the plots).

### 19.2.3 Multi modal Data Visualizations

Let's look at some visualizations of the interactions between variables. The best place to start is a scatterplot matrix.

# scatterplot matrix pairs(dataset[,1:13])

```
Listing 19.17: Calculate a scatterplot matrix.
```

We can see that some of the higher correlated attributes do show good structure in their relationship. Not linear, but nice predictable curved relationships.

```
# correlation plot
correlations <- cor(dataset[,1:13])
corrplot(correlations, method="circle")
```

Listing 19.18: Calculate a correlation plot.

The larger darker blue dots confirm the positively correlated attributes we listed early (not the diagonal). We can also see some larger darker red dots that suggest some negatively correlated attributes. For example tax and rad. These too may be candidates for removal to better improve accuracy of models later on.

![](_page_7_Figure_1.jpeg)

Figure 19.3: Box and Whisker plots of Boston House Dataset Input Attributes

### 19.2.4 Summary of Ideas

There is a lot of structure in this dataset. We need to think about transforms that we could use later to better expose the structure which in turn may improve modeling accuracy. So far it would be worth trying:

- Feature selection and removing the most correlated attributes.
- Normalizing the dataset to reduce the effect of differing scales.
- Standardizing the dataset to reduce the effects of differing distributions.
- Box-Cox transform to see if flattening out some of the distributions improves accuracy.

With lots of additional time I would also explore the possibility of binning (discretization) of the data. This can often improve accuracy for decision tree algorithms.

# 19.3 Evaluate Algorithms: Baseline

We have no idea what algorithms will do well on this problem. Gut feel suggests regression algorithms like GLM and GLMNET may do well. It is also possible that decision trees and even SVM may do well. I have no idea. Let's design our test harness. We will use 10-fold cross validation (each fold will be about 360 instances for training and 40 for test) with 3 repeats. The dataset is not too small and this is a good standard test harness configuration. We will evaluate algorithms using the RMSE and R<sup>2</sup> metrics. RMSE will give a gross idea of how wrong all predictions are (0 is perfect) and R<sup>2</sup> will give an idea of how well the model has fit the data (1 is perfect, 0 is worst).

![](_page_8_Picture_1.jpeg)

Figure 19.4: Scatterplot Matrix of Boston House Dataset Input Attributes

![](_page_9_Figure_1.jpeg)

Figure 19.5: Correlation Matrix of Boston House Dataset Input Attributes

```
# Run algorithms using 10-fold cross validation
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
```

Listing 19.19: Prepare the test harness for evaluating algorithms.

Let's create a baseline of performance on this problem and spot-check a number of different algorithms. We will select a suite of different algorithms capable of working on this regression problem. The 6 algorithms selected include:

- Linear Algorithms: Linear Regression (LR), Generalized Linear Regression (GLM) and Penalized Linear Regression (GLMNET)
- Non-Linear Algorithms: Classification and Regression Trees (CART), Support Vector Machines (SVM) with a radial basis function and k-Nearest Neighbors (KNN)

We know the data has differing units of measure so we will standardize the data for this baseline comparison. This will those algorithms that prefer data in the same scale (e.g. instance based methods and some regression algorithms) a chance to do well.

```
# LM
set.seed(7)
fit.lm <- train(medv~., data=dataset, method="lm", metric=metric, preProc=c("center",
   "scale"), trControl=trainControl)
# GLM
set.seed(7)
```

```
fit.glm <- train(medv~., data=dataset, method="glm", metric=metric, preProc=c("center",
   "scale"), trControl=trainControl)
# GLMNET
set.seed(7)
fit.glmnet <- train(medv~., data=dataset, method="glmnet", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(medv~., data=dataset, method="svmRadial", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# CART
set.seed(7)
grid <- expand.grid(.cp=c(0, 0.05, 0.1))
fit.cart <- train(medv~., data=dataset, method="rpart", metric=metric, tuneGrid=grid,
   preProc=c("center", "scale"), trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(medv~., data=dataset, method="knn", metric=metric, preProc=c("center",
   "scale"), trControl=trainControl)
```

Listing 19.20: Estimate accuracy of machine learning algorithms.

The algorithms all use default tuning parameters, except CART which is fussy on this dataset and has 3 default parameters specified. Let's compare the algorithms. We will use a simple table of results to get a quick idea of what is going on. We will also use a dot plot to show the 95% confidence level for the estimated metrics.

```
# Compare algorithms
results <- resamples(list(LM=fit.lm, GLM=fit.glm, GLMNET=fit.glmnet, SVM=fit.svm,
   CART=fit.cart, KNN=fit.knn))
summary(results)
dotplot(results)
```

Listing 19.21: Collect resample statistics from models and summarize results.

It looks like SVM has the lowest RMSE, followed closely by the other non-linear algorithms CART and KNN. The linear regression algorithms all appear to be in the same ball park and slightly worse error.

```
Models: LM, GLM, GLMNET, SVM, CART, KNN
Number of resamples: 30
RMSE
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 3.514 4.056 4.773 4.963 5.529 9.448 0
GLM 3.514 4.056 4.773 4.963 5.529 9.448 0
GLMNET 3.484 4.017 4.767 4.955 5.520 9.506 0
SVM 2.377 3.010 3.750 3.952 4.463 8.177 0
CART 2.797 3.434 4.272 4.541 5.437 9.248 0
KNN 2.394 3.509 4.471 4.555 5.089 8.757 0
Rsquared
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 0.3169 0.6682 0.7428 0.7293 0.7984 0.8882 0
GLM 0.3169 0.6682 0.7428 0.7293 0.7984 0.8882 0
GLMNET 0.3092 0.6670 0.7437 0.7296 0.7989 0.8921 0
SVM 0.5229 0.7803 0.8513 0.8290 0.8820 0.9418 0
```

CART 0.3614 0.6733 0.8197 0.7680 0.8613 0.9026 0 KNN 0.4313 0.7168 0.8024 0.7732 0.8588 0.9146 0

Listing 19.22: Summary of estimated model accuracy.

We can also see that SVM and the other non-linear algorithms have the best fit for the data in their R<sup>2</sup> measures.

![](_page_11_Figure_4.jpeg)

Figure 19.6: Dotplot Compare Machine Learning Algorithms on the Boston House Price Dataset

Did centering and scaling make a difference to the algorithms other than KNN? I doubt it. But I prefer to hold the data constant at this stage. Perhaps the worse performance of the linear regression algorithms has something to do with the highly correlated attributes. Let's look at that in the next section.

## 19.4 Evaluate Algorithms: Feature Selection

We have a theory that the correlated attributes are reducing the accuracy of the linear algorithms tried in the base line spot-check in the last step. In this step we will remove the highly correlated attributes and see what effect that has on the evaluation metrics. We can find and remove the highly correlated attributes using the findCorrelation() function from the caret package as follows:

# remove correlated attributes

```
# find attributes that are highly corrected
set.seed(7)
cutoff <- 0.70
correlations <- cor(dataset[,1:13])
highlyCorrelated <- findCorrelation(correlations, cutoff=cutoff)
for (value in highlyCorrelated) {
 print(names(dataset)[value])
}
# create a new dataset without highly corrected features
datasetFeatures <- dataset[,-highlyCorrelated]
dim(datasetFeatures)
```

Listing 19.23: Remove highly correlated attributes from the dataset.

We can see that we have dropped 4 attributes: indus, box, tax and dis.

[1] "indus" [1] "nox" [1] "tax" [1] "dis" 407 10

Listing 19.24: List of highly correlated attributes.

Now let's try the same 6 algorithms from our base line experiment.

```
# Run algorithms using 10-fold cross validation
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
# lm
set.seed(7)
fit.lm <- train(medv~., data=datasetFeatures, method="lm", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# GLM
set.seed(7)
fit.glm <- train(medv~., data=datasetFeatures, method="glm", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# GLMNET
set.seed(7)
fit.glmnet <- train(medv~., data=datasetFeatures, method="glmnet", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(medv~., data=datasetFeatures, method="svmRadial", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# CART
set.seed(7)
grid <- expand.grid(.cp=c(0, 0.05, 0.1))
fit.cart <- train(medv~., data=datasetFeatures, method="rpart", metric=metric,
   tuneGrid=grid, preProc=c("center", "scale"), trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(medv~., data=datasetFeatures, method="knn", metric=metric,
   preProc=c("center", "scale"), trControl=trainControl)
# Compare algorithms
feature_results <- resamples(list(LM=fit.lm, GLM=fit.glm, GLMNET=fit.glmnet, SVM=fit.svm,
   CART=fit.cart, KNN=fit.knn))
```

```
summary(feature_results)
dotplot(feature_results)
```

Listing 19.25: Estimate accuracy of models on modified dataset.

Comparing the results, we can see that this has made the RMSE worse for the linear and the non-linear algorithms. The correlated attributes we removed are contributing to the accuracy of the models.

```
Models: LM, GLM, GLMNET, SVM, CART, KNN
Number of resamples: 30
RMSE
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 3.431 4.439 4.908 5.277 5.998 9.982 0
GLM 3.431 4.439 4.908 5.277 5.998 9.982 0
GLMNET 3.283 4.330 4.950 5.236 5.895 9.869 0
SVM 2.726 3.337 4.100 4.352 5.036 8.503 0
CART 2.661 3.550 4.462 4.618 5.246 9.558 0
KNN 2.488 3.377 4.467 4.453 5.051 8.889 0
Rsquared
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 0.2505 0.6271 0.7125 0.6955 0.7797 0.8877 0
GLM 0.2505 0.6271 0.7125 0.6955 0.7797 0.8877 0
GLMNET 0.2581 0.6274 0.7174 0.7027 0.7783 0.8905 0
SVM 0.4866 0.7522 0.8185 0.7883 0.8673 0.9168 0
CART 0.3310 0.7067 0.7987 0.7607 0.8363 0.9360 0
KNN 0.4105 0.7147 0.7981 0.7759 0.8648 0.9117 0
```

Listing 19.26: Output of estimated model accuracy on modified dataset.

## 19.5 Evaluate Algorithms: Box-Cox Transform

We know that some of the attributes have a skew and others perhaps have an exponential distribution. One option would be to explore squaring and log transforms respectively (you could try this!). Another approach would be to use a power transform and let it figure out the amount to correct each attribute. One example is the Box-Cox power transform. Let's try using this transform to rescale the original data and evaluate the effect on the same 6 algorithms. We will also leave in the centering and scaling for the benefit of the instance based method.

```
# Run algorithms using 10-fold cross validation
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
# lm
set.seed(7)
fit.lm <- train(medv~., data=dataset, method="lm", metric=metric, preProc=c("center",
   "scale", "BoxCox"), trControl=trainControl)
# GLM
set.seed(7)
fit.glm <- train(medv~., data=dataset, method="glm", metric=metric, preProc=c("center",
   "scale", "BoxCox"), trControl=trainControl)
# GLMNET
set.seed(7)
```

![](_page_14_Figure_1.jpeg)

Figure 19.7: Dotplot Compare Machine Learning Algorithms on the Boston House Price Dataset with Feature Selection

```
fit.glmnet <- train(medv~., data=dataset, method="glmnet", metric=metric,
   preProc=c("center", "scale", "BoxCox"), trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(medv~., data=dataset, method="svmRadial", metric=metric,
   preProc=c("center", "scale", "BoxCox"), trControl=trainControl)
# CART
set.seed(7)
grid <- expand.grid(.cp=c(0, 0.05, 0.1))
fit.cart <- train(medv~., data=dataset, method="rpart", metric=metric, tuneGrid=grid,
   preProc=c("center", "scale", "BoxCox"), trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(medv~., data=dataset, method="knn", metric=metric, preProc=c("center",
   "scale", "BoxCox"), trControl=trainControl)
# Compare algorithms
transformResults <- resamples(list(LM=fit.lm, GLM=fit.glm, GLMNET=fit.glmnet, SVM=fit.svm,
   CART=fit.cart, KNN=fit.knn))
summary(transformResults)
dotplot(transformResults)
```

Listing 19.27: Estimate accuracy of algorithms on transformed dataset.

We can see that this indeed decrease the RMSE and increased the R<sup>2</sup> on all except the CART algorithms. The RMSE of SVM dropped to an average of 3.761.

```
Models: LM, GLM, GLMNET, SVM, CART, KNN
Number of resamples: 30
RMSE
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 3.404 3.811 4.399 4.621 5.167 7.781 0
GLM 3.404 3.811 4.399 4.621 5.167 7.781 0
GLMNET 3.312 3.802 4.429 4.611 5.123 7.976 0
SVM 2.336 2.937 3.543 3.761 4.216 8.207 0
CART 2.797 3.434 4.272 4.541 5.437 9.248 0
KNN 2.474 3.608 4.308 4.563 5.080 8.922 0
Rsquared
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LM 0.5439 0.7177 0.7832 0.7627 0.8257 0.8861 0
GLM 0.5439 0.7177 0.7832 0.7627 0.8257 0.8861 0
GLMNET 0.5198 0.7172 0.7808 0.7634 0.8297 0.8909 0
SVM 0.5082 0.8249 0.8760 0.8452 0.8998 0.9450 0
CART 0.3614 0.6733 0.8197 0.7680 0.8613 0.9026 0
KNN 0.4065 0.7562 0.8073 0.7790 0.8594 0.9043 0
```

Listing 19.28: Output of estimated accuracy of models on transformed dataset.

## 19.6 Improve Results With Tuning

We can improve the accuracy of the well performing algorithms by tuning their parameters. In this section we will look at tuning the parameters of SVM with a Radial Basis Function (RBF). with more time it might be worth exploring tuning of the parameters for CART and KNN. It

![](_page_16_Figure_1.jpeg)

Figure 19.8: Dotplot Compare Machine Learning Algorithms on the Boston House Price Dataset with Box-Cox Power Transform

might also be worth exploring other kernels for SVM besides the RBF. Let's look at the default parameters already adopted.

print(fit.svm)

Listing 19.29: Display estimated accuracy of a model.

The C parameter is the cost constraint used by SVM. Learn more in the help for the ksvm function ?ksvm. We can see from previous results that a C value of 1.0 is a good starting point.

```
Support Vector Machines with Radial Basis Function Kernel
407 samples
13 predictor
Pre-processing: centered (13), scaled (13), Box-Cox transformation (11)
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 366, 367, 366, 366, 367, 367, ...
Resampling results across tuning parameters:
 C RMSE Rsquared RMSE SD Rsquared SD
 0.25 4.555338 0.7906921 1.533391 0.11596196
 0.50 4.111564 0.8204520 1.467153 0.10573527
 1.00 3.761245 0.8451964 1.323218 0.09487941
Tuning parameter 'sigma' was held constant at a value of 0.07491936
RMSE was used to select the optimal model using the smallest value.
The final values used for the model were sigma = 0.07491936 and C = 1.
```

Listing 19.30: Output of estimated accuracy of a model.

Let's design a grid search around a C value of 1. We might see a small trend of decreasing RMSE with increasing C, so lets try all integer C values between 1 and 10. Another parameter that caret lets us tune is the sigma parameter. This is a smoothing parameter. Good sigma values are often start around 0.1, so we will try numbers before and after.

```
# tune SVM sigma and C parametres
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
set.seed(7)
grid <- expand.grid(.sigma=c(0.025, 0.05, 0.1, 0.15), .C=seq(1, 10, by=1))
fit.svm <- train(medv~., data=dataset, method="svmRadial", metric=metric, tuneGrid=grid,
   preProc=c("BoxCox"), trControl=trainControl)
print(fit.svm)
plot(fit.svm)
```

Listing 19.31: Tune the parameters of a model.

We can see that the sigma values flatten out with larger C cost constraints. It looks like we might do well with a sigma of 0.05 and a C of 10. This gives us a respectable RMSE of 2.977085.

```
Support Vector Machines with Radial Basis Function Kernel
407 samples
13 predictor
Pre-processing: Box-Cox transformation (11)
Resampling: Cross-Validated (10 fold, repeated 3 times)
```

```
Summary of sample sizes: 366, 367, 366, 366, 367, 367, ...
Resampling results across tuning parameters:
 sigma C RMSE Rsquared RMSE SD Rsquared SD
 0.025 1 3.889703 0.8335201 1.4904294 0.11313650
 0.025 2 3.685009 0.8470869 1.4126374 0.10919207
 0.025 3 3.562851 0.8553298 1.3664097 0.10658536
 0.025 4 3.453041 0.8628558 1.3167032 0.10282201
 0.025 5 3.372501 0.8686287 1.2700128 0.09837303
 0.025 6 3.306693 0.8731149 1.2461425 0.09559507
 0.025 7 3.261471 0.8761873 1.2222133 0.09312101
 0.025 8 3.232191 0.8780827 1.2061263 0.09157306
 0.025 9 3.208426 0.8797434 1.1863449 0.08988573
 0.025 10 3.186740 0.8812147 1.1649693 0.08812914
 0.050 1 3.771428 0.8438368 1.3673050 0.09997011
 0.050 2 3.484116 0.8634056 1.2563140 0.09475264
 0.050 3 3.282230 0.8768963 1.1689480 0.08515589
 0.050 4 3.179856 0.8829293 1.1417952 0.08311244
 0.050 5 3.105290 0.8873315 1.1139808 0.08053864
 0.050 6 3.054516 0.8907211 1.0797893 0.07759377
 0.050 7 3.024010 0.8925927 1.0630675 0.07622395
 0.050 8 3.003371 0.8936101 1.0533396 0.07544553
 0.050 9 2.984457 0.8944677 1.0475715 0.07501395
 0.050 10 2.977085 0.8948000 1.0411527 0.07437254
 0.100 1 3.762027 0.8453751 1.2904160 0.09047894
...
 0.150 10 3.156134 0.8807506 0.9741032 0.07304302
RMSE was used to select the optimal model using the smallest value.
The final values used for the model were sigma = 0.05 and C = 10.
```

Listing 19.32: Output of tuning the parameters of a model.

If we wanted to take this further, we could try even more fine tuning with more grid searches. We could also explore trying to tune other parameters of the underlying ksvm() function. Finally and as already mentioned, we could perform some grid searches on the other non-linear regression methods.

# 19.7 Ensemble Methods

We can try some ensemble methods on the problem and see if we can get a further decrease in our RMSE. In this section we will look at some boosting and bagging techniques for decision trees. Additional approaches you could look into would be blending the predictions of multiple well performing models together, called stacking. Let's take a look at the following ensemble methods:

- Random Forest, bagging (RF).
- Gradient Boosting Machines boosting (GBM).
- Cubist, boosting (CUBIST).

![](_page_19_Figure_1.jpeg)

Figure 19.9: Algorithm Tuning Results for SVM on the Boston House Price Dataset

```
# try ensembles
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
# Random Forest
set.seed(seed)
fit.rf <- train(medv~., data=dataset, method="rf", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# Stochastic Gradient Boosting
set.seed(seed)
fit.gbm <- train(medv~., data=dataset, method="gbm", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl, verbose=FALSE)
# Cubist
set.seed(seed)
fit.cubist <- train(medv~., data=dataset, method="cubist", metric=metric,
   preProc=c("BoxCox"), trControl=trainControl)
# Compare algorithms
ensembleResults <- resamples(list(RF=fit.rf, GBM=fit.gbm, CUBIST=fit.cubist))
summary(ensembleResults)
dotplot(ensembleResults)
```

Listing 19.33: Estiamte accuracy of ensemble methods.

We can see that Cubist was the most accurate with an RMSE that was lower than that achieved by tuning SVM.

```
Models: RF, GBM, CUBIST
Number of resamples: 30
RMSE
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
RF 2.072 2.484 2.849 3.199 3.593 7.552 0
GBM 2.349 2.514 2.855 3.314 3.734 7.326 0
CUBIST 1.671 2.325 2.598 2.935 2.862 7.894 0
Rsquared
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
RF 0.5809 0.8736 0.9179 0.8825 0.9323 0.9578 0
GBM 0.6067 0.8425 0.9045 0.8701 0.9264 0.9494 0
CUBIST 0.5312 0.9051 0.9272 0.8945 0.9401 0.9700 0
```

Listing 19.34: Output of estimated accuracy of ensemble methods.

Let's dive deeper into Cubist and see if we can tune it further and get more skill out of it. Cubist has two parameters that are tunable with caret: committees which is the number of boosting operations and neighbors which is used during prediction and is the number of instances used to correct the rule based prediction (although the documentation is perhaps a little ambiguous on this). For more information about Cubist see the help on the function ?cubist. Let's first look at the default tuning parameter used by caret that resulted in our accurate model.

```
# look at parameters used for Cubist
print(fit.cubist)
```

#### Listing 19.35: Summarize accuracy of a model.

We can see that the best RMSE was achieved with committees = 20 and neighbors = 5.

![](_page_21_Figure_1.jpeg)

Figure 19.10: Ensemble Methods on the Boston House Price Dataset

Cubist

```
407 samples
13 predictor
Pre-processing: Box-Cox transformation (11)
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 366, 367, 366, 366, 367, 367, ...
Resampling results across tuning parameters:
 committees neighbors RMSE Rsquared RMSE SD Rsquared SD
  1 0 3.805611 0.8291291 1.446821 0.12468698
  1 5 3.372092 0.8607419 1.441227 0.12021181
  1 9 3.478679 0.8544866 1.461305 0.12201360
 10 0 3.321898 0.8684445 1.331075 0.11184780
 10 5 3.014602 0.8880220 1.310053 0.10505469
 10 9 3.087316 0.8836591 1.343094 0.10781126
 20 0 3.248094 0.8747071 1.252816 0.09983180
 20 5 2.934577 0.8944885 1.213757 0.09319354
 20 9 3.011090 0.8899419 1.253828 0.09601677
RMSE was used to select the optimal model using the smallest value.
The final values used for the model were committees = 20 and neighbors = 5.
```

Listing 19.36: Output of summary of a model.

Let's use a grid search to tune around those values. We'll try all committees between 15 and 25 and spot-check a neighbors value above and below 5.

```
# Tune the Cubist algorithm
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "RMSE"
set.seed(7)
grid <- expand.grid(.committees=seq(15, 25, by=1), .neighbors=c(3, 5, 7))
tune.cubist <- train(medv~., data=dataset, method="cubist", metric=metric,
   preProc=c("BoxCox"), tuneGrid=grid, trControl=trainControl)
print(tune.cubist)
plot(tune.cubist)
```

Listing 19.37: Tune the parameters of a model.

We can see that we have achieved a more accurate model again with an RMSE of 2.822 using committees = 18 and neighbors = 3.

```
Cubist
407 samples
13 predictor
Pre-processing: Box-Cox transformation (11)
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 366, 367, 366, 366, 367, 367, ...
Resampling results across tuning parameters:
 committees neighbors RMSE Rsquared RMSE SD Rsquared SD
 15 3 2.843135 0.9009984 1.153144 0.08574148
```

| 15 | 5 | 2.945379 0.8942976 1.196652 0.09127607                                      |
|----|---|-----------------------------------------------------------------------------|
| 15 | 7 | 2.992984 0.8913018 1.229347 0.09364576                                      |
| 16 | 3 | 2.838901 0.9006522 1.191235 0.08975360                                      |
| 16 | 5 | 2.943103 0.8937805 1.238710 0.09565818                                      |
| 16 | 7 | 2.990762 0.8907565 1.273834 0.09828343                                      |
| 17 | 3 | 2.831608 0.9014030 1.159990 0.08674319                                      |
| 17 | 5 | 2.936655 0.8944879 1.205534 0.09255285                                      |
| 17 | 7 | 2.984208 0.8915462 1.238689 0.09490105                                      |
| 18 | 3 | 2.822586 0.9018685 1.160574 0.08691505                                      |
| 18 | 5 | 2.928190 0.8949810 1.204704 0.09243459                                      |
| 18 | 7 | 2.974838 0.8920938 1.237423 0.09472307                                      |
| 19 | 3 | 2.833172 0.9015738 1.154942 0.08586679                                      |
| 19 | 5 | 2.935970 0.8947952 1.200135 0.09126598                                      |
| 19 | 7 | 2.983656 0.8918658 1.232270 0.09355376                                      |
| 20 | 3 | 2.828846 0.9014772 1.166684 0.08754715                                      |
|    |   |                                                                             |
|    |   |                                                                             |
|    |   | RMSE was used to select the optimal model using the smallest value.         |
|    |   | The final values used for the model were committees = 18 and neighbors = 3. |

Listing 19.38: Output estimated accuracy of tuned model.

![](_page_23_Figure_3.jpeg)

Figure 19.11: Tuning the Parametres of the Cubist Algorithm on the Boston House Price Dataset

With more time we could tune the Cubist algorithm further. Also, with results like this, it

also suggest it might be worth investigating whether we can get more out of the GBM or other boosting implementations.

## 19.8 Finalize Model

It looks like that cubist results in our most accurate model. Let's finalize it by creating a new standalone Cubist model with the parameters above trained using the whole dataset. We must also use the Box-Cox power transform.

```
# prepare the data transform using training data
set.seed(7)
x <- dataset[,1:13]
y <- dataset[,14]
preprocessParams <- preProcess(x, method=c("BoxCox"))
transX <- predict(preprocessParams, x)
# train the final model
finalModel <- cubist(x=transX, y=y, committees=18)
summary(finalModel)
```

Listing 19.39: Prepare the data transform and finalize the model.

We can now use this model to evaluate our held out validation dataset. Again, we must prepare the input data using the same Box-Cox transform.

```
# transform the validation dataset
set.seed(7)
valX <- validation[,1:13]
trans_valX <- predict(preprocessParams, valX)
valY <- validation[,14]
# use final model to make predictions on the validation dataset
predictions <- predict(finalModel, newdata=trans_valX, neighbors=3)
# calculate RMSE
rmse <- RMSE(predictions, valY)
r2 <- R2(predictions, valY)
print(rmse)
```

Listing 19.40: Make predictions using the finalized model.

We can see that the estimated RMSE on this unseen data is 2.666, lower but not too dissimilar from our expected RMSE of 2.822.

```
2.666336
```

Listing 19.41: Estimated accuracy on validation dataset.

# 19.9 Summary

In this lesson you worked through a regression predictive modeling machine learning problem from end-to-end using R. Specifically, the steps covered were:

- 1. Problem Definition (Boston house price data).
- 2. Analyze Data (some skewed distributions and correlated attributes).

- 3. Evaluate Algorithms (SVM with radial basis function looks good).
- 4. Feature Selection (removing correlated attributes didn't help).
- 5. Transforms (Box-Cox transform made things better).
- 6. Algorithm Tuning (getting the most from SVM).
- 7. Ensemble Methods (Bagging and Boosting and getting the most from Cubist).
- 8. Finalize Model (use all training data and confirm using validation dataset).

Working through this case study showed you how the recipes for specific machine learning tasks be can pulled together into a complete project. Working through this case study is good practice at applied machine learning using R.

### 19.9.1 Next Step

You have now completed two predictive modeling machine learning projects end-to-end. The first a multi-class classification problem and this second project on a regression problem. Next is the third and final case study on a binary classification problem.
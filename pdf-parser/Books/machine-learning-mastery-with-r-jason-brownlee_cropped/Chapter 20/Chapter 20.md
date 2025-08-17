## Chapter 20

# Binary Classification Machine Learning Case Study Project

Working through machine learning problems end-to-end is the best way to practice applied machine learning. In this lesson you will work through a binary classification problem using R from start to finish. After completing this project, you will know:

- 1. How to work through a binary classification predictive modeling problem end-to-end.
- 2. How to use data transforms and model tuning to improve model accuracy.
- 3. How to identify when you have hit an accuracy ceiling and the point of diminishing returns on a project.

Let's get started.

## 20.1 Problem Definition

For this project we will investigate the Wisconsin Breast Cancer Dataset described in Chapter 5. Each record in the dataset represents one breast cancer tissue sample. The data was collected from University of Wisconsin Hospitals. Below is a summary of the attributes taken from the UCI Machine Learning repository.

- Sample code number id number.
- Clump Thickness.
- Uniformity of Cell Size.
- Uniformity of Cell Shape.
- Marginal Adhesion.
- Single Epithelial Cell Size.
- Bare Nuclei.
- Bland Chromatin.

- Normal Nucleoli.
- Mitoses.
- Class.

Although the test methodologies differ, the best published results appear to be in the high 90% accuracy such as 96% and 97%. Achieving results in this range would be desirable in this case study.

#### 20.1.1 Load the Dataset

The dataset is available in the mlbench package. Let's start off by loading the required packages and loading the dataset.

```
# load packages
library(mlbench)
library(caret)
# Load data
data(BreastCancer)
```

Listing 20.1: Load packages and dataset.

#### 20.1.2 Validation Dataset

Let's create a validation dataset. This is a sample of our raw data that we hold back from the modeling process. We use it right at the end of the project to confirm the accuracy of our final model. It is a smoke test that we can use to see if we messed up and to give us confidence on our estimates of accuracy on unseen data.

```
# Split out validation dataset
# create a list of 80% of the rows in the original dataset we can use for training
set.seed(7)
validationIndex <- createDataPartition(BreastCancer$Class, p=0.80, list=FALSE)
# select 20% of the data for validation
validation <- BreastCancer[-validationIndex,]
# use the remaining 80% of data to training and testing the models
dataset <- BreastCancer[validationIndex,]
```

Listing 20.2: Split dataset into training and validation sets.

## 20.2 Analyze Data

The objective of this step in the process is to better understand the problem.

#### 20.2.1 Descriptive Statistics

Let's start off by confirming the dimensions of the dataset.

# dimensions of dataaset dim(dataset)

Listing 20.3: Calculate the dimensions of the dataset.

We can see that we have 560 rows and 11 attributes.

560 11

Listing 20.4: Output of the dimensions of the dataset.

Let's eye-ball some data and see what we are working with. We can preview the first 20 rows.

| # peek<br>head(dataset, n=20) |
|-------------------------------|
|-------------------------------|

Listing 20.5: Display first few rows of the dataset.

We can see that the sample number (Id) is probably not going to be useful. We can probably remove it. We can see that all of the inputs are integers. We can also see that we may have some missing data (NA).

|   |                               |   |    |   |             |    |    | Id Cl.thickness Cell.size Cell.shape Marg.adhesion Epith.c.size Bare.nuclei Bl.cromatin |    |   |
|---|-------------------------------|---|----|---|-------------|----|----|-----------------------------------------------------------------------------------------|----|---|
|   | Normal.nucleoli Mitoses Class |   |    |   |             |    |    |                                                                                         |    |   |
| 2 | 1002945                       |   | 5  |   | 4           | 4  | 5  | 7                                                                                       | 10 | 3 |
|   |                               | 2 |    | 1 | benign      |    |    |                                                                                         |    |   |
| 4 | 1016277                       |   | 6  |   | 8           | 8  | 1  | 3                                                                                       | 4  | 3 |
|   |                               | 7 |    | 1 | benign      |    |    |                                                                                         |    |   |
| 5 | 1017023                       |   | 4  |   | 1           | 1  | 3  | 2                                                                                       | 1  | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
| 6 | 1017122                       |   | 8  |   | 10          | 10 | 8  | 7                                                                                       | 10 | 9 |
|   |                               | 7 |    |   | 1 malignant |    |    |                                                                                         |    |   |
| 7 | 1018099                       |   | 1  |   | 1           | 1  | 1  | 2                                                                                       | 10 | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
| 9 | 1033078                       |   | 2  |   | 1           | 1  | 1  | 2                                                                                       | 1  | 1 |
|   |                               | 1 |    | 5 | benign      |    |    |                                                                                         |    |   |
|   | 10 1033078                    |   | 4  |   | 2           | 1  | 1  | 2                                                                                       | 1  | 2 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 11 1035283                    |   | 1  |   | 1           | 1  | 1  | 1                                                                                       | 1  | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 12 1036172                    |   | 2  |   | 1           | 1  | 1  | 2                                                                                       | 1  | 2 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 14 1043999                    |   | 1  |   | 1           | 1  | 1  | 2                                                                                       | 3  | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 15 1044572                    |   | 8  |   | 7           | 5  | 10 | 7                                                                                       | 9  | 5 |
|   |                               | 5 |    |   | 4 malignant |    |    |                                                                                         |    |   |
|   | 16 1047630                    |   | 7  |   | 4           | 6  | 4  | 6                                                                                       | 1  | 4 |
|   |                               | 3 |    |   | 1 malignant |    |    |                                                                                         |    |   |
|   | 17 1048672                    |   | 4  |   | 1           | 1  | 1  | 2                                                                                       | 1  | 2 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 18 1049815                    |   | 4  |   | 1           | 1  | 1  | 2                                                                                       | 1  | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |
|   | 19 1050670                    |   | 10 |   | 7           | 7  | 6  | 4                                                                                       | 10 | 4 |
|   |                               | 1 |    |   | 2 malignant |    |    |                                                                                         |    |   |
|   | 20 1050718                    |   | 6  |   | 1           | 1  | 1  | 2                                                                                       | 1  | 3 |
|   |                               | 1 |    | 1 | benign      |    |    |                                                                                         |    |   |

| 21 1054590 |    | 7  | 3           | 2 | 10 | 5 | 10        | 5 |  |
|------------|----|----|-------------|---|----|---|-----------|---|--|
|            | 4  |    | 4 malignant |   |    |   |           |   |  |
| 22 1054593 |    | 10 | 5           | 5 | 3  | 6 | 7         | 7 |  |
|            | 10 |    | 1 malignant |   |    |   |           |   |  |
| 23 1056784 |    | 3  | 1           | 1 | 1  | 2 | 1         | 2 |  |
|            | 1  |    | 1<br>benign |   |    |   |           |   |  |
| 24 1057013 |    | 8  | 4           | 5 | 1  | 2 | <na></na> | 7 |  |
|            | 3  |    | 1 malignant |   |    |   |           |   |  |

Listing 20.6: Output of the first few rows of the dataset.

Let's look at the attribute data types.

| # types                |  |  |  |
|------------------------|--|--|--|
| sapply(dataset, class) |  |  |  |

Listing 20.7: Display the data type of attributes in the dataset.

We can see that besides the Id, the attributes are factors. This makes sense. I think for modeling it may be more useful to work with the data as numbers than factors. Factors might make things easier for decision tree algorithms (or not). Given that there is an ordinal relationship between the levels we can expose that structure to other algorithms easier if we were working directly with the integer numbers.

```
$Id
[1] "character"
$Cl.thickness
[1] "ordered" "factor"
$Cell.size
[1] "ordered" "factor"
$Cell.shape
[1] "ordered" "factor"
$Marg.adhesion
[1] "ordered" "factor"
$Epith.c.size
[1] "ordered" "factor"
$Bare.nuclei
[1] "factor"
$Bl.cromatin
[1] "factor"
$Normal.nucleoli
[1] "factor"
$Mitoses
[1] "factor"
$Class
[1] "factor"
```

Listing 20.8: Output of the data type of attributes in the dataset.

Let's go ahead and remove the Id column and convert the dataset to numeric values.

```
# Remove redundant variable Id
dataset <- dataset[,-1]
# convert input values to numeric
for(i in 1:9) {
dataset[,i] <- as.numeric(as.character(dataset[,i]))
}
```

Listing 20.9: Remove a column and covert the dataset to numeric types.

Now, let's take a summary of the data and see what we have.

| # summary        |
|------------------|
| summary(dataset) |

Listing 20.10: Calculate a summary of attributes in the dataset.

Interestingly, we can see we have 13 NA values for the Bare.nuclei attribute. This suggests we may need to remove the records (or impute values) with NA values for some analysis and modeling techniques. We can also see that all attributes have integer values in the range [1,10]. This suggests that we may not see much benefit form normalizing attributes for instance based methods like KNN.

Cl.thickness Cell.size Cell.shape Marg.adhesion Epith.c.size Bare.nuclei Bl.cromatin Normal.nucleoli Mitoses Class Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 Min. : 1.000 benign :367 1st Qu.: 2.000 1st Qu.: 1.000 1st Qu.: 1.000 1st Qu.: 1.000 1st Qu.: 2.000 1st Qu.: 1.000 1st Qu.: 2.000 1st Qu.: 1.000 1st Qu.: 1.000 malignant:193 Median : 4.000 Median : 1.000 Median : 2.000 Median : 1.000 Median : 2.000 Median : 1.000 Median : 3.000 Median : 1.000 Median : 1.000 Mean : 4.384 Mean : 3.116 Mean : 3.198 Mean : 2.875 Mean : 3.232 Mean : 3.468 Mean : 3.405 Mean : 2.877 Mean : 1.611 3rd Qu.: 6.000 3rd Qu.: 5.000 3rd Qu.: 5.000 3rd Qu.: 4.000 3rd Qu.: 4.000 3rd Qu.: 5.000 3rd Qu.: 4.250 3rd Qu.: 4.000 3rd Qu.: 1.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000 Max. :10.000

Listing 20.11: Output summary of attributes in the dataset.

We can also see that there is some imbalance in the Class values. Let's take a closer look at the breakdown of the Class values.

| # class distribution |                                                                                     |
|----------------------|-------------------------------------------------------------------------------------|
|                      | cbind(freq=table(dataset\$Class), percentage=prop.table(table(dataset\$Class))*100) |

Listing 20.12: Summarize the breakdown of the class attribute.

There is indeed a 65% to 35% split for benign-malignant in the class values which is imbalanced, but not so much that we need to thinking about rebalancing, at least not yet.

```
freq percentage
benign 367 65.53571
malignant 193 34.46429
```

Listing 20.13: Output of the breakdown of the class attribute.

Finally, lets look at the correlation between the attributes. We have to exclude the 13 rows with NA values (incomplete cases) when calculating the correlations.

```
# summarize correlations between input variables
complete_cases <- complete.cases(dataset)
cor(dataset[complete_cases,1:9])
```

Listing 20.14: Calculate the correlation between attributes.

We can see some modest to high correlation between some of the attributes. For example between cell shape and cell size at 0.90 correlation. Some algorithms may benefit from removing the highly correlated attributes.

|                                     | Cl.thickness Cell.size Cell.shape Marg.adhesion Epith.c.size Bare.nuclei |  |           |           |           |           |  |  |  |  |  |
|-------------------------------------|--------------------------------------------------------------------------|--|-----------|-----------|-----------|-----------|--|--|--|--|--|
| Bl.cromatin Normal.nucleoli Mitoses |                                                                          |  |           |           |           |           |  |  |  |  |  |
| Cl.thickness                        | 1.0000000 0.6200884 0.6302917                                            |  | 0.4741733 | 0.5089557 | 0.5600770 | 0.5290733 |  |  |  |  |  |
| 0.5143933 0.3426018                 |                                                                          |  |           |           |           |           |  |  |  |  |  |
| Cell.size                           | 0.6200884 1.0000000 0.9011340                                            |  | 0.7141150 | 0.7404824 | 0.6687226 | 0.7502700 |  |  |  |  |  |
| 0.7072182 0.4506532                 |                                                                          |  |           |           |           |           |  |  |  |  |  |
| Cell.shape                          | 0.6302917 0.9011340 1.0000000                                            |  | 0.6846206 | 0.7043423 | 0.6896724 | 0.7276114 |  |  |  |  |  |
|                                     | 0.7127155 0.4345125                                                      |  |           |           |           |           |  |  |  |  |  |
| Marg.adhesion                       | 0.4741733 0.7141150 0.6846206                                            |  | 1.0000000 | 0.5860660 | 0.6660165 | 0.6660533 |  |  |  |  |  |
|                                     | 0.6031036 0.4314910                                                      |  |           |           |           |           |  |  |  |  |  |
| Epith.c.size                        | 0.5089557 0.7404824 0.7043423                                            |  | 0.5860660 | 1.0000000 | 0.5568406 | 0.6102032 |  |  |  |  |  |
|                                     | 0.6433364 0.4775271                                                      |  |           |           |           |           |  |  |  |  |  |
| Bare.nuclei                         | 0.5600770 0.6687226 0.6896724                                            |  | 0.6660165 | 0.5568406 | 1.0000000 | 0.6668483 |  |  |  |  |  |
|                                     | 0.5795794 0.3539473                                                      |  |           |           |           |           |  |  |  |  |  |
| Bl.cromatin                         | 0.5290733 0.7502700 0.7276114                                            |  | 0.6660533 | 0.6102032 | 0.6668483 | 1.0000000 |  |  |  |  |  |
|                                     | 0.6838547 0.3545122                                                      |  |           |           |           |           |  |  |  |  |  |
| Normal.nucleoli                     | 0.5143933 0.7072182 0.7127155                                            |  | 0.6031036 | 0.6433364 | 0.5795794 | 0.6838547 |  |  |  |  |  |
| 1.0000000 0.4084127                 |                                                                          |  |           |           |           |           |  |  |  |  |  |
| Mitoses                             | 0.3426018 0.4506532 0.4345125                                            |  | 0.4314910 | 0.4775271 | 0.3539473 | 0.3545122 |  |  |  |  |  |
|                                     | 0.4084127 1.0000000                                                      |  |           |           |           |           |  |  |  |  |  |

Listing 20.15: Output of the correlation between attributes.

#### 20.2.2 Unimodal Data Visualizations

Let's look at the distribution of individual attributes in the dataset. We'll start with histograms of all of the attributes.

```
# histograms each attribute
par(mfrow=c(3,3))
for(i in 1:9) {
 hist(dataset[,i], main=names(dataset)[i])
}
```

Listing 20.16: Calculate histograms.

We can see that almost all of the distributions have an exponential or bimodal shape to them. We may benefit from log transforms or other power transforms later on.

Let's use density plots to get a more smoothed look at the distributions.

![](_page_6_Figure_1.jpeg)

Figure 20.1: Histograms of Input Attributes for the Wisconsin Breast Cancer Dataset

```
# density plot for each attribute
par(mfrow=c(3,3))
complete_cases <- complete.cases(dataset)
for(i in 1:9) {
 plot(density(dataset[complete_cases,i]), main=names(dataset)[i])
}
```

```
Listing 20.17: Calculate density plots.
```

These plots add more support to our initial ideas. We can see bimodal distributions (two bumps) and exponential looking distributions.

![](_page_7_Figure_4.jpeg)

Figure 20.2: Density Plots of Input Attributes for the Wisconsin Breast Cancer Dataset

Let's take a look at the distributions from another perspective using box and whisker plots.

```
# boxplots for each attribute
par(mfrow=c(3,3))
for(i in 1:9) {
 boxplot(dataset[,i], main=names(dataset)[i])
}
```

Listing 20.18: Calculate box and whisker plots.

We see squashed distributions given the exponential shapes we've already observed. Also, because the attributes are scorings of some kind, the scale is limited to [1,10] for all inputs.

![](_page_8_Figure_1.jpeg)

Figure 20.3: Box and Whisker Plots of Input Attributes for the Wisconsin Breast Cancer Dataset

#### 20.2.3 Multimodal Data Visualizations

Now, let's take a look at the interactions between the attributes. Let's start with a scatterplot matrix of the attributes colored by the class values. Because the data is discrete (integer values) we need to add some jitter to make the scatterplots useful, otherwise the dots will all be on top of each other.

```
# scatterplot matrix
jittered_x <- sapply(dataset[,1:9], jitter)
pairs(jittered_x, names(dataset[,1:9]), col=dataset$Class)
```

Listing 20.19: Calculate scatter plot matrix.

We can see that the black (benign) apart to be clustered around the bottom-right corner (smaller values) and red (malignant) are all over the place.

![](_page_9_Figure_6.jpeg)

Figure 20.4: Scatterplot Matrix Plots of Input Attributes for the Wisconsin Breast Cancer Dataset

Because the data is discrete, we can use bar plots to get an idea of the interaction of the distribution of each attribute and how they breakdown by class value.

```
# bar plots of each variable by class
par(mfrow=c(3,3))
for(i in 1:9) {
barplot(table(dataset$Class,dataset[,i]), main=names(dataset)[i],
    legend.text=unique(dataset$Class))
```

#### }

Listing 20.20: Calculate bar plots.

This gives us a more nuanced idea of how the benign values clustered at the left (smaller values) of each distribution and malignant all over the place.

![](_page_10_Figure_4.jpeg)

Figure 20.5: Bar Plots by Class Value of Input Attributes for the Wisconsin Breast Cancer Dataset

## 20.3 Evaluate Algorithms: Baseline

We don't know what algorithms will perform well on this data before hand. We have to spotcheck various different methods and see what looks good then double down on those methods. Given that the data is discrete, I would generally expect decision tree and rule based methods to do well. I would expect regression and instance based methods to not do so well. This is just intuition, and it could very well be wrong. Let's try a smattering of linear and non-linear algorithms:

 Linear Algorithms: Logistic Regression (LG), Linear Discriminate Analysis (LDA) and Regularized Logistic Regression (GLMNET).

 Non-Linear Algorithms: k-Nearest Neighbors (KNN), Classification and Regression Trees (CART), Naive Bayes (NB) and Support Vector Machines with Radial Basis Functions (SVM).

Let's start off by defining the test harness. We have a good amount of data so we will use 10-fold cross validation with 3 repeats. This is a good standard test harness configuration. It is a binary classification problem. For simplicity, we will use Accuracy and Kappa metrics. Given that it is a medical test, we could have gone with the Area Under ROC Curve (AUC) and looked at the sensitivity and specificity to select the best algorithms.

```
# 10-fold cross validation with 3 repeats
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "Accuracy"
```

Listing 20.21: Prepare algorithm evaluation test harness.

Let's create our models. We will use the default parameters for each algorithm for now. Algorithm tuning is considered later. We need to reset the random number seed before training each algorithm to ensure that each algorithm is evaluated on exactly the same splits of data. This will make later comparisons simpler (e.g. apples to apples).

```
# LG
set.seed(7)
fit.glm <- train(Class~., data=dataset, method="glm", metric=metric, trControl=trainControl)
# LDA
set.seed(7)
fit.lda <- train(Class~., data=dataset, method="lda", metric=metric, trControl=trainControl)
# GLMNET
set.seed(7)
fit.glmnet <- train(Class~., data=dataset, method="glmnet", metric=metric,
   trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(Class~., data=dataset, method="knn", metric=metric, trControl=trainControl)
# CART
set.seed(7)
fit.cart <- train(Class~., data=dataset, method="rpart", metric=metric,
   trControl=trainControl)
# Naive Bayes
set.seed(7)
fit.nb <- train(Class~., data=dataset, method="nb", metric=metric, trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(Class~., data=dataset, method="svmRadial", metric=metric,
   trControl=trainControl)
# Compare algorithms
results <- resamples(list(LG=fit.glm, LDA=fit.lda, GLMNET=fit.glmnet, KNN=fit.knn,
   CART=fit.cart, NB=fit.nb, SVM=fit.svm))
summary(results)
dotplot(results)
```

Listing 20.22: Estimate the accuracy of a suite of machine learning algorithms.

We can see good accuracy across the board. All algorithms have a mean accuracy above 90%, well above the baseline of 65% if we just predicted benign. The problem is learnable. We can see that KNN (97.08%) and logistic regression (LG was 96.35% and GLMNET was 96.47%) had the highest accuracy on the problem.

```
Models: LG, LDA, GLMNET, KNN, CART, NB, SVM
Number of resamples: 30
Accuracy
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LG 0.9091 0.9455 0.9636 0.9635 0.9815 1.0000 0
LDA 0.9091 0.9447 0.9633 0.9592 0.9815 0.9821 0
GLMNET 0.9091 0.9455 0.9640 0.9647 0.9815 1.0000 0
KNN 0.9273 0.9630 0.9815 0.9708 0.9818 1.0000 0
CART 0.8571 0.9259 0.9444 0.9349 0.9455 0.9818 0
NB 0.9259 0.9444 0.9633 0.9616 0.9818 1.0000 0
SVM 0.9074 0.9325 0.9630 0.9519 0.9636 0.9818 0
Kappa
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LG 0.8014 0.8786 0.9206 0.9192 0.9599 1.0000 0
LDA 0.7989 0.8752 0.9175 0.9089 0.9599 0.9607 0
GLMNET 0.8014 0.8786 0.9219 0.9219 0.9599 1.0000 0
KNN 0.8431 0.9175 0.9589 0.9356 0.9603 1.0000 0
CART 0.6957 0.8346 0.8758 0.8573 0.8796 0.9603 0
NB 0.8336 0.8802 0.9207 0.9159 0.9593 1.0000 0
SVM 0.8041 0.8544 0.9201 0.8969 0.9215 0.9611 0
```

Listing 20.23: Output estimated accuracy of algorithms.

## 20.4 Evaluate Algorithms: Transform

We know we have some skewed distributions. There are transform methods that we can use to adjust and normalize these distributions. A favorite for positive input attributes (which we have in this case) is the Box-Cox transform. In this section we evaluate the same 7 algorithms as above except this time the data is transformed using a Box-Cox power transform to flatten out the distributions.

```
# 10-fold cross validation with 3 repeats
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "Accuracy"
# LG
set.seed(7)
fit.glm <- train(Class~., data=dataset, method="glm", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# LDA
set.seed(7)
fit.lda <- train(Class~., data=dataset, method="lda", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# GLMNET
set.seed(7)
fit.glmnet <- train(Class~., data=dataset, method="glmnet", metric=metric,
   preProc=c("BoxCox"), trControl=trainControl)
# KNN
set.seed(7)
```

![](_page_13_Figure_1.jpeg)

Figure 20.6: Baseline Accuracy on the Wisconsin Breast Cancer Dataset

```
fit.knn <- train(Class~., data=dataset, method="knn", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# CART
set.seed(7)
fit.cart <- train(Class~., data=dataset, method="rpart", metric=metric,
   preProc=c("BoxCox"), trControl=trainControl)
# Naive Bayes
set.seed(7)
fit.nb <- train(Class~., data=dataset, method="nb", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(Class~., data=dataset, method="svmRadial", metric=metric,
   preProc=c("BoxCox"), trControl=trainControl)
# Compare algorithms
transformResults <- resamples(list(LG=fit.glm, LDA=fit.lda, GLMNET=fit.glmnet, KNN=fit.knn,
   CART=fit.cart, NB=fit.nb, SVM=fit.svm))
summary(transformResults)
dotplot(transformResults)
```

Listing 20.24: Estimate accuracy on transformed dataset.

We can see that the accuracy of the previous best algorithm KNN was elevated to 97.14%. We have a new ranking, showing SVM with the most accurate mean accuracy at 97.20%.

```
Models: LG, LDA, GLMNET, KNN, CART, NB, SVM
Number of resamples: 30
Accuracy
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LG 0.9091 0.9498 0.9636 0.9629 0.9815 1.0000 0
LDA 0.9091 0.9457 0.9729 0.9684 0.9818 1.0000 0
GLMNET 0.9273 0.9630 0.9636 0.9690 0.9818 1.0000 0
KNN 0.9091 0.9636 0.9815 0.9714 0.9818 1.0000 0
CART 0.8571 0.9259 0.9444 0.9349 0.9455 0.9818 0
NB 0.9273 0.9630 0.9636 0.9690 0.9818 1.0000 0
SVM 0.9273 0.9630 0.9729 0.9720 0.9818 1.0000 0
Kappa
       Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
LG 0.8062 0.8889 0.9207 0.9184 0.9599 1.0000 0
LDA 0.8062 0.8839 0.9411 0.9317 0.9603 1.0000 0
GLMNET 0.8431 0.9190 0.9215 0.9324 0.9599 1.0000 0
KNN 0.8062 0.9199 0.9591 0.9380 0.9603 1.0000 0
CART 0.6957 0.8346 0.8758 0.8573 0.8796 0.9603 0
NB 0.8392 0.9190 0.9215 0.9324 0.9602 1.0000 0
SVM 0.8468 0.9207 0.9411 0.9397 0.9603 1.0000 0
```

Listing 20.25: Output estimated accuracy on transformed dataset.

## 20.5 Algorithm Tuning

Let's try some tuning of the top algorithms, specifically SVM and see if we can lift the accuracy.

![](_page_15_Figure_1.jpeg)

Figure 20.7: Accuracy With Data Transforms on the Wisconsin Breast Cancer Dataset

#### 20.5.1 Tuning SVM

The SVM implementation has two parameters that we can tune with caret package. The sigma which is a smoothing term, and C which is a cost constraint. You can learn more about these parameters in the help for the ksvm() function ?ksvm. Let's try a range of values for C between 1 and 10 and a few small values for sigma around the default of 0.1.

```
# 10-fold cross validation with 3 repeats
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "Accuracy"
set.seed(7)
grid <- expand.grid(.sigma=c(0.025, 0.05, 0.1, 0.15), .C=seq(1, 10, by=1))
fit.svm <- train(Class~., data=dataset, method="svmRadial", metric=metric, tuneGrid=grid,
   preProc=c("BoxCox"), trControl=trainControl)
print(fit.svm)
plot(fit.svm)
```

Listing 20.26: Tune the parameters of the SVM algorithm.

We can see that we have made very little difference to the results here. The most accurate model had a score of 97.19% (the same as our previously rounded score of 97.20%) using a sigma = 0.15 and C = 1. We could tune further, but I don't expect a payoff.

```
Support Vector Machines with Radial Basis Function Kernel
560 samples
 9 predictor
 2 classes: 'benign', 'malignant'
Pre-processing: Box-Cox transformation (9)
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 492, 492, 493, 492, 493, 493, ...
Resampling results across tuning parameters:
 sigma C Accuracy Kappa Accuracy SD Kappa SD
...
 0.100 7 0.9641278 0.9223610 0.02261232 0.04868379
 0.100 8 0.9622872 0.9181073 0.02180600 0.04732571
 0.100 9 0.9622872 0.9181073 0.02180600 0.04732571
 0.100 10 0.9622872 0.9181073 0.02180600 0.04732571
 0.150 1 0.9719958 0.9397291 0.02015647 0.04306497
 0.150 2 0.9707945 0.9370321 0.02003909 0.04288659
 0.150 3 0.9665408 0.9278046 0.02083330 0.04457734
 0.150 4 0.9647226 0.9236680 0.02128219 0.04578654
 0.150 5 0.9634993 0.9208189 0.02132057 0.04611720
 0.150 6 0.9629044 0.9191889 0.02255859 0.04930297
 0.150 7 0.9628932 0.9192086 0.02097758 0.04571537
 0.150 8 0.9622759 0.9177768 0.02014458 0.04394943
 0.150 9 0.9622872 0.9178560 0.01896851 0.04135621
 0.150 10 0.9616586 0.9164069 0.01925515 0.04194362
Accuracy was used to select the optimal model using the largest value.
The final values used for the model were sigma = 0.15 and C = 1.
```

Listing 20.27: Output estimated accuracy of tuning SVM parameters.

![](_page_17_Figure_1.jpeg)

Figure 20.8: Tuning SVM parameters on the Wisconsin Breast Cancer Dataset

#### 20.5.2 Tuning KNN

The KNN implementation has one parameter that we can tune with caret: k the number of closest instances to collect in order to make a prediction. Let's try all k values between 1 and 20.

```
# 10-fold cross validation with 3 repeats
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "Accuracy"
set.seed(7)
grid <- expand.grid(.k=seq(1,20,by=1))
fit.knn <- train(Class~., data=dataset, method="knn", metric=metric, tuneGrid=grid,
   preProc=c("BoxCox"), trControl=trainControl)
print(fit.knn)
plot(fit.knn)
```

Listing 20.28: Tune the parameters of the KNN algorithm.

We can see again that tuning has made little difference, settling on a value of k = 8 with an accuracy of 97.19%. This is higher than the previous 97.14%, but very similar (or perhaps identical!) to the result achieved by the tuned SVM.

```
k-Nearest Neighbors
560 samples
 9 predictor
 2 classes: 'benign', 'malignant'
Pre-processing: Box-Cox transformation (9)
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 492, 492, 493, 492, 493, 493, ...
Resampling results across tuning parameters:
 k Accuracy Kappa Accuracy SD Kappa SD
  1 0.9524667 0.8953398 0.02651015 0.05883977
  2 0.9482023 0.8857023 0.02411603 0.05345626
  3 0.9665079 0.9271012 0.02397303 0.05188289
  4 0.9683482 0.9310991 0.02237821 0.04843864
  5 0.9707728 0.9365613 0.02324286 0.05022458
  6 0.9701331 0.9352947 0.02173624 0.04666792
  7 0.9713676 0.9379343 0.02127377 0.04572732
  8 0.9719962 0.9393206 0.02282626 0.04915446
  9 0.9713897 0.9379635 0.02173774 0.04684891
 10 0.9707945 0.9367099 0.02217898 0.04777854
 11 0.9714117 0.9380798 0.02273735 0.04901007
 12 0.9714117 0.9380798 0.02273735 0.04901007
 13 0.9701996 0.9354319 0.02263113 0.04877625
 14 0.9707949 0.9366855 0.02221537 0.04790061
 15 0.9701776 0.9353156 0.02162533 0.04659741
 16 0.9707836 0.9367691 0.02117843 0.04543484
 17 0.9707724 0.9366901 0.02006679 0.04296231
 18 0.9719849 0.9393670 0.02129015 0.04575184
 19 0.9719849 0.9393670 0.02129015 0.04575184
 20 0.9708057 0.9367228 0.02218466 0.04778476
Accuracy was used to select the optimal model using the largest value.
The final value used for the model was k = 8
```

![](_page_19_Figure_1.jpeg)

Listing 20.29: Output estimated accuracy of tuning KNN parameters.

Figure 20.9: Tuning k-NN parameters on the Wisconsin Breast Cancer Dataset

## 20.6 Ensemble Methods

As a final check, lets look at some boosting and bagging ensemble algorithms on the dataset. I expect them to do quite well given the decision trees that underlie these methods. If our guess about hitting the accuracy ceiling is true, we may also see these methods top out around 97.20%. Let's look at 4 ensemble methods:

- Bagging: Bagged CART (BAG) and Random Forest (RF).
- Boosting: Stochastic Gradient Boosting (GBM) and C5.0 (C50).

We will use the same test harness as before including the Box-Cox transform that flattens out the distributions.

```
metric <- "Accuracy"
# Bagged CART
set.seed(7)
fit.treebag <- train(Class~., data=dataset, method="treebag", metric=metric,
   trControl=trainControl)
# Random Forest
set.seed(7)
fit.rf <- train(Class~., data=dataset, method="rf", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# Stochastic Gradient Boosting
set.seed(7)
fit.gbm <- train(Class~., data=dataset, method="gbm", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl, verbose=FALSE)
# C5.0
set.seed(7)
fit.c50 <- train(Class~., data=dataset, method="C5.0", metric=metric, preProc=c("BoxCox"),
   trControl=trainControl)
# Compare results
ensembleResults <- resamples(list(BAG=fit.treebag, RF=fit.rf, GBM=fit.gbm, C50=fit.c50))
summary(ensembleResults)
dotplot(ensembleResults)
```

Listing 20.30: Estimate accuracy of ensemble methods.

We see that Random Forest was the most accurate with a score of 97.26%. Very similar to our tuned models above. We could spend time tuning the parameters of random forest (e.g. increasing the number of trees) and the other ensemble methods, but I don't expect to see better accuracy scores other than random statistical fluctuations.

```
Models: BAG, RF, GBM, C50
Number of resamples: 30
Accuracy
     Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
BAG 0.8909 0.9325 0.9633 0.9550 0.9815 0.9818 0
RF 0.9273 0.9631 0.9726 0.9726 0.9818 1.0000 0
GBM 0.9107 0.9447 0.9636 0.9629 0.9818 1.0000 0
C50 0.9273 0.9630 0.9636 0.9666 0.9815 1.0000 0
Kappa
     Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
BAG 0.7462 0.8499 0.9196 0.9005 0.9589 0.9611 0
RF 0.8431 0.9196 0.9407 0.9405 0.9603 1.0000 0
GBM 0.7989 0.8799 0.9215 0.9181 0.9599 1.0000 0
C50 0.8392 0.9190 0.9211 0.9268 0.9599 1.0000 0
```

Listing 20.31: Output estimated accuracy of ensemble methods.

## 20.7 Finalize Model

We now need to finalize the model, which really means choose which model we would like to use. For simplicity I would probably select the KNN method, at the expense of the memory required to store the training dataset. SVM would be a good choice to trade-off space and time

![](_page_21_Figure_1.jpeg)

Figure 20.10: Bagging and Boosting Ensemble Methods on the Wisconsin Breast Cancer Dataset

complexity. I probably would not select the Random Forest algorithm given the complexity of the model. It seems overkill for this dataset, lots of trees with little benefit in Accuracy.

Let's go with the KNN algorithm. This is really simple, as we do not need to store a model. We do need to capture the parameters of the Box-Cox transform though. And we also need to prepare the data by removing the unused Id attribute and converting all of the inputs to numeric format. The implementation of KNN (knn3()) belongs to the caret package and does not support missing values. We will have to remove the rows with missing values from the training dataset as well as the validation dataset. The code below shows the preparation of the pre-processing parameters using the training dataset.

```
# prepare parameters for data transform
set.seed(7)
datasetNoMissing <- dataset[complete.cases(dataset),]
x <- datasetNoMissing[,1:9]
preprocessParams <- preProcess(x, method=c("BoxCox"))
x <- predict(preprocessParams, x)
```

Listing 20.32: Prepare the data transform for finalizing the model.

Next we need to prepare the validation dataset for making a prediction. We must:

- 1. Remove the Id attribute.
- 2. Remove those rows with missing data.
- 3. Convert all input attributes to numeric.
- 4. Apply the Box-Cox transform to the input attributes using parameters prepared on the training dataset.

```
# prepare the validation dataset
set.seed(7)
# remove id column
validation <- validation[,-1]
# remove missing values (not allowed in this implementation of knn)
validation <- validation[complete.cases(validation),]
# convert to numeric
for(i in 1:9) {
 validation[,i] <- as.numeric(as.character(validation[,i]))
}
# transform the validation dataset
validationX <- predict(preprocessParams, validation[,1:9])
```

Listing 20.33: Prepare the validation dataset for making new predictions.

Now we are ready to actually make a prediction in the training dataset.

```
# make predictions
set.seed(7)
predictions <- knn3Train(x, validationX, datasetNoMissing$Class, k=9, prob=FALSE)
confusionMatrix(predictions, validation$Class)
```

Listing 20.34: Estimate accuracy of KNN on the unseen validation dataset.

We can see that the accuracy of the final model on the validation dataset is 99.26%. This is optimistic because there is only 136 rows, but it does show that we have an accurate standalone model that we could use on other unclassified data.

```
Confusion Matrix and Statistics
         Reference
Prediction benign malignant
 benign 87 0
 malignant 1 48
             Accuracy : 0.9926
               95% CI : (0.9597, 0.9998)
   No Information Rate : 0.6471
   P-Value [Acc > NIR] : <2e-16
                Kappa : 0.984
Mcnemar's Test P-Value : 1
          Sensitivity : 0.9886
          Specificity : 1.0000
        Pos Pred Value : 1.0000
        Neg Pred Value : 0.9796
           Prevalence : 0.6471
        Detection Rate : 0.6397
  Detection Prevalence : 0.6397
     Balanced Accuracy : 0.9943
      'Positive' Class : benign
```

Listing 20.35: Output estimated accuracy of KNN on the unseen validation dataset.

## 20.8 Summary

In this lesson you have worked through a case study binary classification machine learning problem. We pulled together a number of lessons for machine learning tasks in R into an end-to-end project using the R platform. We covered the following steps:

- 1. Problem definition (predict the type of cancer from a details of a tissue sample).
- 2. Analyzed Data (noted the exponential and bimodal shapes of many of the attributes).
- 3. Evaluated Algorithms (baseline accuracy suggesting KNN is accurate on the problem).
- 4. Evaluate Algorithms with Transform (improved accuracy with a Box-Cox transform and also noted SVM does well).
- 5. Tuned Algorithms (small improvements to SVM and KNN, but nothing too exciting).
- 6. Ensemble Methods (hitting the prediction accuracy ceiling with the dataset).
- 7. Finalized Model (accurate on the validation dataset, perhaps optimistically so).

Working through this case study will give you confidence in the steps and techniques that you can use to in R to complete your own predictive modeling project.

#### 20.8.1 Next Step

This was the third and final predictive modeling project case study. Well done! You now have experience and skills in working through predictive modeling machine learning projects end-to-end. In the next section you will discover ideas for additional small case study projects that you could work on for further practice.
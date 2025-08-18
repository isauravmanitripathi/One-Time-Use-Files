# Chapter 15

# Combine Predictions From Multiple Machine Learning Models

Ensembles can give you a boost in accuracy on your dataset. In this lesson you will discover how you can create three of the most powerful types of ensembles in R. After completing this lesson, you will know:

- 1. How to use boosting and bagging algorithms on your dataset.
- 2. How to blend the predictions from multiple models using stacking.

Let's get started.

### 15.1 Increase The Accuracy Of Your Models

It can take time to find well performing machine learning algorithms for your dataset. This is because of the trial and error nature of applied machine learning. Once you have a shortlist of accurate models, you can use algorithm tuning to get the most from each algorithm. Another approach that you can use to increase accuracy on your dataset is to combine the predictions of multiple different models together. This is called an ensemble prediction.

#### 15.1.1 Combine Model Predictions Into Ensemble Predictions

The three most popular methods for combining the predictions from different models are:

- Bagging. Building multiple models (typically of the same type) from different subsamples of the training dataset.
- Boosting. Building multiple models (typically of the same type) each of which learns to fix the prediction errors of a prior model in the chain.
- Stacking. Building multiple models (typically of differing types) and supervisor model that learns how to best combine the predictions of the primary models.

In this lesson, we will look at each in turn. This lesson will not explain each of these ensemble methods.

#### 15.2 Test Dataset

Before we start building ensembles, let's define our test setup. All of the examples of ensemble predictions in this case study will use the ionosphere dataset described in Chapter 5. This dataset describes high-frequency antenna returns from high energy particles in the atmosphere and whether the return shows structure or not. The problem is a binary classification that contains 351 instances and 35 numerical attributes. Let's load the packages and the dataset.

```
# Load packages
library(mlbench)
library(caret)
library(caretEnsemble)
# Load the dataset
data(Ionosphere)
dataset <- Ionosphere
dataset <- dataset[,-2]
dataset$V1 <- as.numeric(as.character(dataset$V1))
```

Listing 15.1: Load packages and dataset.

Note that the first attribute was a factor (0,1) and has been transformed to be numeric for consistency with all of the other numeric attributes. Also note that the second attribute is a constant and has been removed. Here is a sneak-peek at the first few rows of the ionosphere dataset.

|                                                                                        | > head(dataset)                                         |     |                                                                                           |     |     |     |     |     |     |     |     |     |
|----------------------------------------------------------------------------------------|---------------------------------------------------------|-----|-------------------------------------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|                                                                                        | V1                                                      | V3  | V4                                                                                        | V5  | V6  | V7  | V8  | V9  | V10 | V11 | V12 | V13 |
|                                                                                        |                                                         | V14 | V15                                                                                       |     |     |     |     |     |     |     |     |     |
| 1                                                                                      |                                                         |     | 1 0.99539 -0.05889 0.85243 0.02306 0.83398 -0.37708 1.00000 0.03760 0.85243 -0.17755      |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.59755 -0.44945 0.60536                                                                  |     |     |     |     |     |     |     |     |     |
| 2                                                                                      |                                                         |     | 1 1.00000 -0.18829 0.93035 -0.36156 -0.10868 -0.93597 1.00000 -0.04549 0.50874 -0.67743   |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.34432 -0.69707 -0.51685                                                                 |     |     |     |     |     |     |     |     |     |
| 3                                                                                      |                                                         |     | 1 1.00000 -0.03365 1.00000 0.00485 1.00000 -0.12062 0.88965 0.01198 0.73082 0.05346       |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.85443 0.00827 0.54591                                                                   |     |     |     |     |     |     |     |     |     |
| 4                                                                                      |                                                         |     | 1 1.00000 -0.45161 1.00000 1.00000 0.71216 -1.00000 0.00000 0.00000 0.00000 0.00000       |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.00000 0.00000 -1.00000                                                                  |     |     |     |     |     |     |     |     |     |
| 5                                                                                      |                                                         |     | 1 1.00000 -0.02401 0.94140 0.06531 0.92106 -0.23255 0.77152 -0.16399 0.52798 -0.20275     |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.56409 -0.00712 0.34395                                                                  |     |     |     |     |     |     |     |     |     |
| 6                                                                                      |                                                         |     | 1 0.02337 -0.00592 -0.09924 -0.11949 -0.00763 -0.11824 0.14706 0.06637 0.03786 -0.06302   |     |     |     |     |     |     |     |     |     |
|                                                                                        | 0.00000 0.00000 -0.04572                                |     |                                                                                           |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         | V16 | V17                                                                                       | V18 | V19 | V20 | V21 | V22 | V23 | V24 | V25 | V26 |
|                                                                                        |                                                         |     | V27                                                                                       | V28 |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 1 -0.38223 0.84356 -0.38542 0.58212 -0.32192 0.56971 -0.29674 0.36946 -0.47357 0.56811    |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | -0.51171 0.41078 -0.46168                                                                 |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 2 -0.97515 0.05499 -0.62237 0.33109 -1.00000 -0.13151 -0.45300 -0.18056 -0.35734 -0.20332 |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | -0.26569 -0.20468 -0.18401                                                                |     |     |     |     |     |     |     |     |     |
| 3                                                                                      |                                                         |     | 0.00299 0.83775 -0.13644 0.75535 -0.08540 0.70887 -0.27502 0.43385 -0.12062 0.57528       |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | -0.40220 0.58984 -0.22145                                                                 |     |     |     |     |     |     |     |     |     |
| 4                                                                                      |                                                         |     | 0.14516 0.54094 -0.39330 -1.00000 -0.54467 -0.69975 1.00000 0.00000 0.00000 1.00000       |     |     |     |     |     |     |     |     |     |
|                                                                                        |                                                         |     | 0.90695 0.51613 1.00000                                                                   |     |     |     |     |     |     |     |     |     |
| 5 -0.27457 0.52940 -0.21780 0.45107 -0.17813 0.05982 -0.35575 0.02309 -0.52879 0.03286 |                                                         |     |                                                                                           |     |     |     |     |     |     |     |     |     |
| -0.65158 0.13290 -0.53206                                                              |                                                         |     |                                                                                           |     |     |     |     |     |     |     |     |     |
| 6 -0.15540 -0.00343 -0.10196 -0.11575 -0.05414 0.01838 0.03669 0.01519 0.00888 0.03513 |                                                         |     |                                                                                           |     |     |     |     |     |     |     |     |     |
| -0.01535 -0.03240 0.09223                                                              |                                                         |     |                                                                                           |     |     |     |     |     |     |     |     |     |
|                                                                                        | V29<br>V30<br>V31<br>V32<br>V33<br>V34 Class            |     |                                                                                           |     |     |     |     |     |     |     |     |     |
| 1                                                                                      | 0.21266 -0.34090 0.42267 -0.54487 0.18641 -0.45300 good |     |                                                                                           |     |     |     |     |     |     |     |     |     |

2 -0.19040 -0.11593 -0.16626 -0.06288 -0.13738 -0.02447 bad 3 0.43100 -0.17365 0.60436 -0.24180 0.56045 -0.38238 good 4 1.00000 -0.20099 0.25682 1.00000 -0.32382 1.00000 bad 5 0.02431 -0.62197 -0.05707 -0.59573 -0.04608 -0.65697 good 6 -0.07859 0.00732 0.00000 0.00000 -0.00039 0.12011 bad

Listing 15.2: Output of the first few rows of the dataset.

#### 15.3 Boosting Algorithms

We can look at two of the most popular boosting machine learning algorithms:

- C5.0.
- Stochastic Gradient Boosting.

Below is an example of the C5.0 and Stochastic Gradient Boosting (using the Gradient Boosting Modeling implementation) algorithms in R. Both algorithms include parameters that are not tuned in this example.

```
# Example of Boosting Algorithms
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
seed <- 7
metric <- "Accuracy"
# C5.0
set.seed(seed)
fit.c50 <- train(Class~., data=dataset, method="C5.0", metric=metric,
   trControl=trainControl)
# Stochastic Gradient Boosting
set.seed(seed)
fit.gbm <- train(Class~., data=dataset, method="gbm", metric=metric,
   trControl=trainControl, verbose=FALSE)
# summarize results
boostingResults <- resamples(list(c5.0=fit.c50, gbm=fit.gbm))
summary(boostingResults)
dotplot(boostingResults)
```

Listing 15.3: Run boosting algorithms on dataset.

We can see that the C5.0 algorithm produced a more accurate model with an accuracy of 94.58%.

```
Models: c5.0, gbm
Number of resamples: 30
Accuracy
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
c5.0 0.8824 0.9143 0.9437 0.9458 0.9714 1 0
gbm 0.8824 0.9143 0.9429 0.9402 0.9641 1 0
```

Listing 15.4: Output of boosting algorithms on dataset.

Learn more about caret package boosting models tree: Boosting Models<sup>1</sup> .

<sup>1</sup><http://topepo.github.io/caret/Boosting.html>

![](_page_3_Figure_1.jpeg)

Figure 15.1: Boosting Machine Learning Algorithms in R

## 15.4 Bagging Algorithms

Let's look at two of the most popular bagging machine learning algorithms:

- Bagged CART.
- Random Forest.

Below is an example of the Bagged CART and Random Forest algorithms in R. Both algorithms include parameters that are not tuned in this example.

```
# Example of Bagging algorithms
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
seed <- 7
metric <- "Accuracy"
# Bagged CART
set.seed(seed)
fit.treebag <- train(Class~., data=dataset, method="treebag", metric=metric,
   trControl=trainControl)
# Random Forest
set.seed(seed)
fit.rf <- train(Class~., data=dataset, method="rf", metric=metric, trControl=trainControl)
# summarize results
baggingResults <- resamples(list(treebag=fit.treebag, rf=fit.rf))
summary(baggingResults)
dotplot(baggingResults)
```

Listing 15.5: Run bagging algorithms on dataset.

We can see that the Random Forest algorithm produced a more accurate model with an accuracy of 93.25%.

```
Models: treebag, rf
Number of resamples: 30
Accuracy
        Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
treebag 0.8529 0.8946 0.9143 0.9183 0.9440 1 0
rf 0.8571 0.9143 0.9420 0.9325 0.9444 1 0
```

Listing 15.6: Output of bagging algorithms on dataset.

Learn more about caret package bagging model here: Bagging Models<sup>2</sup> .

#### 15.5 Stacking Algorithms

You can combine the predictions of multiple caret models using the caretEnsemble package. Given a list of caret models, the caretStack() function can be used to specify a higher-order model to learn how to best combine the predictions of sub-models together. Let's first look at creating 5 sub-models for the ionosphere dataset, specifically:

Linear Discriminate Analysis (LDA).

<sup>2</sup><http://topepo.github.io/caret/Bagging.html>

![](_page_5_Figure_1.jpeg)

Figure 15.2: Bagging Machine Learning Algorithms in R

- Classification and Regression Trees (CART).
- Logistic Regression (via Generalized Linear Model or GLM).
- k-Nearest Neighbors (KNN).
- Support Vector Machine with a Radial Basis Kernel Function (SVM).

Below is an example that creates these 5 sub-models. Note the new helpful caretList() function provided by the caretEnsemble package for creating a list of standard caret models.

```
# Example of Stacking algorithms
# create submodels
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3,
   savePredictions=TRUE, classProbs=TRUE)
algorithmList <- c('lda', 'rpart', 'glm', 'knn', 'svmRadial')
set.seed(seed)
models <- caretList(Class~., data=dataset, trControl=trainControl, methodList=algorithmList)
results <- resamples(models)
summary(results)
dotplot(results)
```

Listing 15.7: Run a suite of algorithms on dataset.

We can see that the SVM creates the most accurate model with an accuracy of 94.66%.

```
Models: lda, rpart, glm, knn, svmRadial
Number of resamples: 30
Accuracy
          Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
lda 0.7714 0.8286 0.8611 0.8645 0.9060 0.9429 0
rpart 0.7714 0.8540 0.8873 0.8803 0.9143 0.9714 0
glm 0.7778 0.8286 0.8873 0.8803 0.9167 0.9722 0
knn 0.7647 0.8056 0.8431 0.8451 0.8857 0.9167 0
svmRadial 0.8824 0.9143 0.9429 0.9466 0.9722 1.0000 0
```

Listing 15.8: Output of a suite of algorithms on the dataset.

When we combine the predictions of different models using stacking, it is desirable that the predictions made by the sub-models have low correlation. This would suggest that the models are skillful but in different ways, allowing a new classifier to figure out how to get the best from each model for an improved score. If the predictions for the sub-models were highly corrected (> 0.75) then they would be making the same or very similar predictions most of the time reducing the benefit of combining the predictions.

```
# correlation between results
modelCor(results)
splom(results)
```

Listing 15.9: Calculate comparison of models on the dataset.

We can see that all pairs of predictions have generally low correlation. The two methods with the highest correlation between their predictions are Logistic Regression (GLM) and KNN at 0.517 correlation which is not considered high (> 0.75).

![](_page_7_Figure_1.jpeg)

Figure 15.3: Comparison of Sub-Models for Stacking Ensemble in R

lda rpart glm knn svmRadial lda 1.0000000 0.2515454 0.2970731 0.5013524 0.1126050 rpart 0.2515454 1.0000000 0.1749923 0.2823324 0.3465532 glm 0.2970731 0.1749923 1.0000000 0.5172239 0.3788275 knn 0.5013524 0.2823324 0.5172239 1.0000000 0.3512242 svmRadial 0.1126050 0.3465532 0.3788275 0.3512242 1.0000000

Listing 15.10: Output of the comparison of models on the dataset.

![](_page_8_Figure_3.jpeg)

Figure 15.4: Correlations Between Predictions Made By Sub-Models in Stacking Ensemble

Let's combine the predictions of the classifiers using a simple linear model.

```
# stack using glm
stackControl <- trainControl(method="repeatedcv", number=10, repeats=3,
   savePredictions=TRUE, classProbs=TRUE)
set.seed(seed)
stack.glm <- caretStack(models, method="glm", metric="Accuracy", trControl=stackControl)
print(stack.glm)
```

Listing 15.11: Combine predictions using GLM.

We can see that we have lifted the accuracy to 94.99% which is a small improvement over using SVM alone. This is also an improvement over using random forest alone on the dataset, as observed above.

```
A glm ensemble of 2 base models: lda, rpart, glm, knn, svmRadial
Ensemble results:
Generalized Linear Model
1053 samples
  5 predictor
  2 classes: 'bad', 'good'
No pre-processing
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 948, 947, 948, 947, 949, 948, ...
Resampling results
 Accuracy Kappa Accuracy SD Kappa SD
 0.949996 0.891494 0.02121303 0.04600482
```

Listing 15.12: Output of combining predictions using GLM.

We can also use more sophisticated algorithms to combine predictions in an effort to tease out when best to use the different methods. In this case, we use the Random Forest algorithm to combine the predictions.

```
# stack using random forest
set.seed(seed)
stack.rf <- caretStack(models, method="rf", metric="Accuracy", trControl=stackControl)
print(stack.rf)
```

Listing 15.13: Combine predictions using Random Forest.

We can see that this has lifted the accuracy to 96.26% an impressive improvement over SVM alone.

```
A rf ensemble of 2 base models: lda, rpart, glm, knn, svmRadial
Ensemble results:
Random Forest
1053 samples
  5 predictor
  2 classes: 'bad', 'good'
No pre-processing
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 948, 947, 948, 947, 949, 948, ...
Resampling results across tuning parameters:
 mtry Accuracy Kappa Accuracy SD Kappa SD
 2 0.9626439 0.9179410 0.01777927 0.03936882
 3 0.9623205 0.9172689 0.01858314 0.04115226
 5 0.9591459 0.9106736 0.01938769 0.04260672
Accuracy was used to select the optimal model using the largest value.
The final value used for the model was mtry = 2.
```

Listing 15.14: Output of combining predictions using Random Forest.

#### 15.6 Summary

In this lesson you discovered that you can use ensembles of machine learning algorithms to improve the accuracy of your models. You discovered three types of ensembles of machine learning algorithms that you can build in R:

- Boosting.
- Bagging.
- Stacking.

#### 15.6.1 Next Step

In the previous lesson you discovered how you can increase the accuracy of your models using algorithm tuning, and in this lesson you discovered how you can improve the accuracy of your models by combining the predictions from multiple models. In the next lesson we wrap things up and look at how you can finalize your most accurate model.
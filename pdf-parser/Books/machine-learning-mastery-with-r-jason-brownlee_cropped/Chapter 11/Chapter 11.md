## Chapter 11

# Machine Learning Model Evaluation Metrics

What metrics can you use to evaluate your machine learning algorithms? In this lesson you will discover how you can evaluate your machine learning algorithms in R using a number of standard evaluation metrics. After completing this lesson you will know:

- 1. How to use Accuracy and Kappa to evaluate model skill on classification problems.
- 2. How to use RMSE and R<sup>2</sup> to evaluate model skill on regression problems.
- 3. How to use Area Under ROC Curve, sensitivity and specificity to evaluate model skill on binary classification problems.
- 4. How to use Logarithmic Loss to evaluate model skill on classification problems.

Let's get started.

#### 11.1 Model Evaluation Metrics in R

There are many different metrics that you can use to evaluate your machine learning algorithms in R. When you use caret to evaluate your models, the default metrics used are accuracy for classification problems and RMSE for regression. But caret supports a range of other popular evaluation metrics.

In this lesson you will step through each of the evaluation metrics provided by caret. Each example provides a complete case study that you can copy-and-paste into your project and adapt to your problem. Note that this lesson does assume that you already know how to interpret these other metrics.

## 11.2 Accuracy and Kappa

Accuracy and Kappa are the default metrics used to evaluate algorithms on binary and multiclass classification datasets in caret. Accuracy is the percentage of correctly classified instances out of all instances. It is more useful on a binary classification than multi-class classification

problem because it can be less clear exactly how the accuracy breaks down across those classes (e.g. you need to go deeper with a confusion matrix).

Kappa or Cohen's Kappa is like classification accuracy, except that it is normalized at the baseline of random chance on your dataset. It is a more useful measure to use on problems that have an imbalance in the classes (e.g. a 70% to 30% split for classes 0 and 1 and you can achieve 70% accuracy by predicting all instances are for class 0). In the example below the Pima Indians diabetes dataset is used. It has a class break down of 65% to 35% for negative and positive outcomes.

```
# load packages
library(caret)
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# prepare resampling method
trainControl <- trainControl(method="cv", number=5)
set.seed(7)
fit <- train(diabetes~., data=PimaIndiansDiabetes, method="glm", metric="Accuracy",
   trControl=trainControl)
# display results
print(fit)
```

Listing 11.1: Calculate Accuracy and Kappa metrics.

Running this example, we can see tables of Accuracy and Kappa for each machine learning algorithm evaluated. This includes the mean values (left) and the standard deviations (marked as SD) for each metric, taken over the population of cross validation folds and trials. You can see that the accuracy of the model is approximately 76% which is 11 percentage points above the baseline accuracy of 65% which is not really that impressive. The Kappa the other hand shows approximately 46% which is more interesting.

```
Generalized Linear Model
768 samples
 8 predictor
 2 classes: 'neg', 'pos'
No pre-processing
Resampling: Cross-Validated (5 fold)
Summary of sample sizes: 614, 614, 615, 615, 614
Resampling results
 Accuracy Kappa Accuracy SD Kappa SD
 0.7695442 0.4656824 0.02692468 0.0616666
```

Listing 11.2: Output of Accuracy and Kappa metrics.

## 11.3 RMSE and R<sup>2</sup>

RMSE and R<sup>2</sup> are the default metrics used to evaluate algorithms on regression datasets in caret. RMSE or Root Mean Squared Error is the average deviation of the predictions from the observations. It is useful to get a gross idea of how well (or not) an algorithm is doing, in the units of the output variable.

#### 11.4. Area Under ROC Curve 79

R<sup>2</sup> spoken as R Squared or also called the coefficient of determination provides a goodnessof-fit measure for the predictions to the observations. This is a value between 0 and 1 for no-fit and perfect fit respectively. In this example the longly economic dataset is used. The output variable is a number employed. It is not clear whether this is an actual count (e.g. in millions) or a percentage.

```
# load packages
library(caret)
# load data
data(longley)
# prepare resampling method
trainControl <- trainControl(method="cv", number=5)
set.seed(7)
fit <- train(Employed~., data=longley, method="lm", metric="RMSE", trControl=trainControl)
# display results
print(fit)
```

Listing 11.3: Calculate RMSE and RSquared metrics.

Running this example, we can see tables of RMSE and R Squared for each machine learning algorithm evaluated. Again, you can see the mean and standard deviations of both metrics are provided. You can see that the RMSE was 0.38 in the units of Employed (whatever those units are). Whereas, the R Square value shows a good fit for the data with a value very close to 1 (0.988).

```
Linear Regression
16 samples
6 predictor
No pre-processing
Resampling: Cross-Validated (5 fold)
Summary of sample sizes: 12, 12, 14, 13, 13
Resampling results
 RMSE Rsquared RMSE SD Rsquared SD
 0.3868618 0.9883114 0.1025042 0.01581824
```

Listing 11.4: Output of RMSE and RSquared metrics.

### 11.4 Area Under ROC Curve

ROC metrics are only suitable for binary classification problems (e.g. two classes). To calculate ROC information, you must change the summaryFunction in your trainControl to be twoClassSummary. This will calculate the Area Under ROC Curve (AUROC) also called just Area Under curve (AUC), sensitivity and specificity.

ROC is actually the area under the ROC curve or AUC. The AUC represents a models ability to discriminate between positive and negative classes. An area of 1.0 represents a model that predicts perfectly. An area of 0.5 represents a model as good as random. Learn more about ROC here.

 Sensitivity is the true positive rate also called the recall. It is the number of instances from the positive (first) class that actually predicted correctly.

#### 11.5. Logarithmic Loss 80

 Specificity is also called the true negative rate. Is the number of instances from the negative class (second class) that were actually predicted correctly.

ROC can be broken down into sensitivity and specificity. A binary classification problem is really a trade-off between sensitivity and specificity.

```
# load packages
library(caret)
library(mlbench)
# load the dataset
data(PimaIndiansDiabetes)
# prepare resampling method
trainControl <- trainControl(method="cv", number=5, classProbs=TRUE,
   summaryFunction=twoClassSummary)
set.seed(7)
fit <- train(diabetes~., data=PimaIndiansDiabetes, method="glm", metric="ROC",
   trControl=trainControl)
# display results
print(fit)
```

Listing 11.5: Calculate ROC metrics.

Here, you can see the good but not excellent AUC score of 0.833. The first level is taken as the positive class, in this case neg (no onset of diabetes).

Generalized Linear Model 768 samples 8 predictor 2 classes: 'neg', 'pos' No pre-processing Resampling: Cross-Validated (5 fold) Summary of sample sizes: 614, 614, 615, 615, 614 Resampling results ROC Sens Spec ROC SD Sens SD Spec SD

0.8336003 0.882 0.5600978 0.02111279 0.03563706 0.0560184

Listing 11.6: Output ROC metrics.

#### 11.5 Logarithmic Loss

Logarithmic Loss (or LogLoss) is used to evaluate binary classification but it is more common for multi-class classification algorithms. Specifically, it evaluates the probabilities estimated by the algorithms. In this case we see LogLoss calculated for the iris flower multi-class classification problem.

```
# load packages
library(caret)
# load the dataset
data(iris)
# prepare resampling method
trainControl <- trainControl(method="cv", number=5, classProbs=TRUE,
   summaryFunction=mnLogLoss)
```

```
set.seed(7)
fit <- train(Species~., data=iris, method="rpart", metric="logLoss", trControl=trainControl)
# display results
print(fit)
```

Listing 11.7: Calculate LogLoss metrics.

Logloss is minimized and we can see the optimal CART model had an argument cp value of 0 (the first row of results).

```
CART
150 samples
 4 predictor
 3 classes: 'setosa', 'versicolor', 'virginica'
No pre-processing
Resampling: Cross-Validated (5 fold)
Summary of sample sizes: 120, 120, 120, 120, 120
Resampling results across tuning parameters:
 cp logLoss logLoss SD
 0.00 0.4105613 0.6491893
 0.44 0.6840517 0.4963032
 0.50 1.0986123 0.0000000
logLoss was used to select the optimal model using the smallest value.
The final value used for the model was cp = 0.
```

Listing 11.8: Output LogLoss metrics.

## 11.6 Summary

In this lesson you discovered different metrics that you can use to evaluate the performance of your machine learning algorithms in R using caret. Specifically:

- Accuracy and Kappa.
- RMSE and R<sup>2</sup> .
- ROC (AUC, Sensitivity and Specificity).
- LogLoss.

#### 11.6.1 Next Step

In the previous lesson you learned how to evaluate the skill of models on unseen data and in this lesson you discovered performance metrics that you can use. In the next lesson we look at the third piece of your test harness which are the algorithms that you can use to actually model your data.
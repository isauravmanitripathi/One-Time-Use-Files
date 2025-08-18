## Chapter 10

# Resampling Methods To Estimate Model Accuracy

When you are building a predictive model, you need to evaluate the capability of the model on unseen data. This is typically done by estimating accuracy using data that was not used to train the model. The caret package in R provides a number of methods to estimate the accuracy of a machine learning algorithm. In this lesson you will discover 5 approaches for estimating model performance on unseen data. After completing this lesson, you will know:

- 1. How to split a dataset into train and test subsets.
- 2. How to evaluate model accuracy using the bootstrap method.
- 3. How to evaluate model accuracy using k-fold cross validation with and without repeats.
- 4. How to evaluate model accuracy using leave one out cross validation.

Let's get started.

#### 10.1 Estimating Model Accuracy

When working on a project you often only have a limited set of data and you need to choose carefully how you use it. Predictive models required data on which to train. You also need a dataset that the model has not seen during training on which it can make predictions. The accuracy of the model predictions on data unseen during training can be used as an estimate for the accuracy of the model on unseen data in general.

You cannot estimate the accuracy of the model on the data used to train it. An ideal model could just remember all of the training instances and make perfect predictions. You must hold data aside primarily for the purposes of model evaluation.

There are methods that you can use if you have a lot of data and do not need to be careful about how it is spent during training. More commonly your dataset has a fixed size and you need to use statistical techniques that make good use of a limited size dataset. These statistical methods are often called resampling methods as they take multiple samples or make multiple splits of your dataset into portions that you can use for model training and model testing. In the following sections you are going to discover how to use five different resampling methods that you can use to evaluate the accuracy of your data in R.

#### 10.2 Data Split

Data splitting involves partitioning the data into an explicit training dataset used to prepare the model and an unseen test dataset used to evaluate the models performance on unseen data. It is useful when you have a very large dataset so that the test dataset can provide a meaningful estimation of performance, or for when you are using slow methods and need a quick approximation of performance.

The example below splits the iris dataset so that 80% is used for training a Naive Bayes model and 20% is used to evaluate the models performance.

```
# load the packages
library(caret)
library(klaR)
# load the iris dataset
data(iris)
# define an 80%/20% train/test split of the dataset
trainIndex <- createDataPartition(iris$Species, p=0.80, list=FALSE)
dataTrain <- iris[ trainIndex,]
dataTest <- iris[-trainIndex,]
# train a naive Bayes model
fit <- NaiveBayes(Species~., data=dataTrain)
# make predictions
predictions <- predict(fit, dataTest[,1:4])
# summarize results
confusionMatrix(predictions$class, dataTest$Species)
```

Listing 10.1: Calcualte data split.

Running this example, you will see an estimation of model accuracy on the test subset of the data:

```
Confusion Matrix and Statistics
        Reference
Prediction setosa versicolor virginica
 setosa 10 0 0
 versicolor 0 10 2
 virginica 0 0 8
Overall Statistics
          Accuracy : 0.9333
           95% CI : (0.7793, 0.9918)
  No Information Rate : 0.3333
  P-Value [Acc > NIR] : 8.747e-12
            Kappa : 0.9
Mcnemar's Test P-Value : NA
Statistics by Class:
              Class: setosa Class: versicolor Class: virginica
Sensitivity 1.0000 1.0000 0.8000
Specificity 1.0000 0.9000 1.0000
Pos Pred Value 1.0000 0.8333 1.0000
Neg Pred Value 1.0000 1.0000 0.9091
```

| Prevalence           | 0.3333 | 0.3333 | 0.3333 |
|----------------------|--------|--------|--------|
| Detection Rate       | 0.3333 | 0.3333 | 0.2667 |
| Detection Prevalence | 0.3333 | 0.4000 | 0.2667 |
| Balanced Accuracy    | 1.0000 | 0.9500 | 0.9000 |

Listing 10.2: Output of data split.

#### 10.3 Bootstrap

Bootstrap resampling involves taking random samples from the dataset (with re-selection) against which to evaluate the model. In aggregate, the results provide an indication of the variance of the models performance. Typically, large number of resampling iterations are performed (thousands or tends of thousands). The following example uses a bootstrap with 100 resamples to estimate the accuracy of a Naive Bayes model.

```
# load the package
library(caret)
# load the iris dataset
data(iris)
# define training control
trainControl <- trainControl(method="boot", number=100)
# evalaute the model
fit <- train(Species~., data=iris, trControl=trainControl, method="nb")
# display the results
print(fit)
```

Listing 10.3: Estimate accuracy using Bootstrap.

Running this example, you will see the estimated accuracy of the Naive Bayes model with two different values for the usekernel model parameter.

```
Naive Bayes
150 samples
 4 predictor
 3 classes: 'setosa', 'versicolor', 'virginica'
No pre-processing
Resampling: Bootstrapped (100 reps)
Summary of sample sizes: 150, 150, 150, 150, 150, 150, ...
Resampling results across tuning parameters:
 usekernel Accuracy Kappa Accuracy SD Kappa SD
 FALSE 0.9536239 0.9298175 0.02567435 0.03882289
  TRUE 0.9572684 0.9353627 0.02484076 0.03743853
Tuning parameter 'fL' was held constant at a value of 0
Accuracy was used to select the optimal model using the largest value.
The final values used for the model were fL = 0 and usekernel = TRUE.
```

Listing 10.4: Output of accuracy using Bootstrap.

### 10.4 k-fold Cross Validation

The k-fold cross validation method involves splitting the dataset into k-subsets. Each subset is held out while the model is trained on all other subsets. This process is completed until accuracy is determine for each instance in the dataset, and an overall accuracy estimate is provided. It is a robust method for estimating accuracy, and the size of k can tune the amount of bias in the estimate, with popular values set to 5 and 10. The following example uses 10-fold cross validation to estimate the accuracy of the Naive Bayes algorithm on the iris dataset.

```
# load the package
library(caret)
# load the iris dataset
data(iris)
# define training control
trainControl <- trainControl(method="cv", number=10)
# evaluate the model
fit <- train(Species~., data=iris, trControl=trainControl, method="nb")
# display the results
print(fit)
```

Listing 10.5: Estimate accuracy using k-fold Cross Validation.

Running this example, you will see the estimated of the accuracy of the model using 10-fold cross validation.

Naive Bayes 150 samples 4 predictor 3 classes: 'setosa', 'versicolor', 'virginica' No pre-processing Resampling: Cross-Validated (10 fold) Summary of sample sizes: 135, 135, 135, 135, 135, 135, ... Resampling results across tuning parameters: usekernel Accuracy Kappa Accuracy SD Kappa SD FALSE 0.9533333 0.93 0.06324555 0.09486833 TRUE 0.9533333 0.93 0.05488484 0.08232726 Tuning parameter 'fL' was held constant at a value of 0 Accuracy was used to select the optimal model using the largest value. The final values used for the model were fL = 0 and usekernel = FALSE.

Listing 10.6: Output of accuracy using k-fold Cross Validation.

#### 10.5 Repeated k-fold Cross Validation

The process of splitting the data into k-folds can be repeated a number of times, this is called Repeated k-fold Cross Validation. The final model accuracy is taken as the mean from the number of repeats. The following example demonstrates 10-fold cross validation with 3 repeats to estimate the accuracy of the Naive Bayes algorithm on the iris dataset.

```
# load the package
library(caret)
# load the iris dataset
data(iris)
# define training control
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
# evaluate the model
fit <- train(Species~., data=iris, trControl=trainControl, method="nb")
# display the results
print(fit)
```

Listing 10.7: Estimate accuracy using repeated k-fold Cross Validation.

Running this example, you will see:

```
Naive Bayes
150 samples
 4 predictor
 3 classes: 'setosa', 'versicolor', 'virginica'
No pre-processing
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 135, 135, 135, 135, 135, 135, ...
Resampling results across tuning parameters:
 usekernel Accuracy Kappa Accuracy SD Kappa SD
 FALSE 0.9533333 0.9300000 0.04998084 0.07497126
  TRUE 0.9577778 0.9366667 0.04789303 0.07183954
Tuning parameter 'fL' was held constant at a value of 0
Accuracy was used to select the optimal model using the largest value.
The final values used for the model were fL = 0 and usekernel = TRUE.
```

Listing 10.8: Output of accuracy using repeated k-fold Cross Validation.

#### 10.6 Leave One Out Cross Validation

In Leave One Out Cross Validation (LOOCV), a data instance is left out and a model constructed on all other data instances in the training set. This is repeated for all data instances. The following example demonstrates LOOCV to estimate the accuracy of the Naive Bayes algorithm on the iris dataset.

```
# load the package
library(caret)
# load the iris dataset
data(iris)
# define training control
trainControl <- trainControl(method="LOOCV")
# evaluate the model
fit <- train(Species~., data=iris, trControl=trainControl, method="nb")
# display the results
print(fit)
```

Listing 10.9: Estimate accuracy using LOOCV.

Running this example, you will see:

```
Naive Bayes
150 samples
 4 predictor
 3 classes: 'setosa', 'versicolor', 'virginica'
No pre-processing
Resampling: Leave-One-Out Cross-Validation
Summary of sample sizes: 149, 149, 149, 149, 149, 149, ...
Resampling results across tuning parameters:
 usekernel Accuracy Kappa
 FALSE 0.9533333 0.93
  TRUE 0.9600000 0.94
Tuning parameter 'fL' was held constant at a value of 0
Accuracy was used to select the optimal model using the largest value.
The final values used for the model were fL = 0 and usekernel = TRUE.
```

Listing 10.10: Output accuracy using LOOCV.

### 10.7 Tips For Evaluating Algorithms

Below are tips to consider when selecting test options to evaluate the accuracy of predictive modeling machine learning algorithms on unseen data.

- Using a data split into a training and test set is a good idea when you have a lot of data and you are confident that your training sample is representative of the larger dataset.
- Using a data split is very efficient and is often used to get a quick estimate of model accuracy.
- Cross validation is a gold standard for evaluating model accuracy, often with k-folds set to 5 or 10 to balance overfitting the training data with a fair accuracy estimate.
- Repeated k-fold cross validation is preferred when you can afford the computational expense and require a less biased estimate.

#### 10.8 Summary

In this lesson you discovered 5 different methods that you can use to estimate the accuracy of your model on unseen data. Those methods were:

- Data Split.
- Bootstrap.

- k-fold Cross Validation.
- Repeated k-fold Cross Validation.
- Leave One Out Cross Validation.

#### 10.8.1 Next Step

In this lesson you discovered how you can estimate the accuracy of models on unseen data. In the next lesson you will look at metrics that you can use to evaluate the performance of models.
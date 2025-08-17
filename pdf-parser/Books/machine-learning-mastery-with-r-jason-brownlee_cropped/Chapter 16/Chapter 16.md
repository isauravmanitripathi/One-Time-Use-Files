## Chapter 16

# Save And Finalize Your Machine Learning Model

Finding an accurate machine learning model is not the end of the project. In this lesson you will discover how to finalize your machine learning model in R. After completing this lesson, you will know:

- 1. How to use your trained model to make predictions on unseen data.
- 2. How to re-create a well performing model from caret as a standalone model.
- 3. How to save your model to a file, load it later and make predictions on unseen data.

Let's get started.

#### 16.1 Finalize Your Machine Learning Model

Once you have an accurate model on your test harness you are nearly done. But not yet. There are still a number of tasks to do to finalize your model. The whole idea of creating an accurate model for your dataset was to make predictions on unseen data. There are three tasks you may be concerned with:

- 1. Making new predictions on unseen data.
- 2. Creating a standalone model using all training data.
- 3. Saving your model to file for later loading and making predictions on new data.

Once you have finalized your model you are ready to make use of it. You could use the R model directly. You could also discover the key internal representation found by the learning algorithm (like the coefficients in a linear model) and use them in a new implementation of the prediction algorithm on another platform.

The caret package is an excellent tool that you can use to find good or even best machine learning algorithms and parameters for machine learning algorithms. But what do you do after you have discovered a model that is accurate enough to use? Once you have found a good model in R, you have three main concerns:

- Making new predictions using your tuned caret model.
- Creating a standalone model using the entire training dataset.
- Saving a standalone model to file for use later.

In the following, you will look at how you can finalize your machine learning model in R.

#### 16.2 Make Predictions On New Data

You can make new predictions using a model you have tuned using caret with the predict.train() function. In the recipe below, the dataset is split into a validation dataset and a training dataset. The validation dataset could just as easily be a new dataset stored in a separate file and loaded as a data frame. A good model of the data is found using LDA. We can see that caret provides access to the best model from a training run in the finalModel variable.

We can use that model to make predictions by calling predict using the fit from train() which will automatically use the final model. We must specify the data one which to make predictions via the newdata argument.

```
# load packages
library(caret)
library(mlbench)
# load dataset
data(PimaIndiansDiabetes)
# create 80%/20% for training and validation datasets
set.seed(9)
validationIndex <- createDataPartition(PimaIndiansDiabetes$diabetes, p=0.80, list=FALSE)
validation <- PimaIndiansDiabetes[-validationIndex,]
training <- PimaIndiansDiabetes[validationIndex,]
# train a model and summarize model
set.seed(9)
trainControl <- trainControl(method="cv", number=10)
fit.lda <- train(diabetes~., data=training, method="lda", metric="Accuracy",
   trControl=trainControl)
print(fit.lda)
print(fit.lda$finalModel)
# estimate skill on validation dataset
set.seed(9)
predictions <- predict(fit.lda, newdata=validation)
confusionMatrix(predictions, validation$diabetes)
```

Listing 16.1: Make predictions on unseen data using caret.

Running this example, we can see that the estimated accuracy on the training dataset was 76.91%. Using the finalModel in the fit, we can see that the accuracy on the hold out validation dataset was 77.78%, very similar to our estimate.

Resampling results Accuracy Kappa Accuracy SD Kappa SD 0.7691169 0.45993 0.06210884 0.1537133 ...

```
Confusion Matrix and Statistics
         Reference
Prediction neg pos
      neg 85 19
      pos 15 34
              Accuracy : 0.7778
               95% CI : (0.7036, 0.8409)
   No Information Rate : 0.6536
   P-Value [Acc > NIR] : 0.000586
                Kappa : 0.5004
Mcnemar's Test P-Value : 0.606905
           Sensitivity : 0.8500
           Specificity : 0.6415
        Pos Pred Value : 0.8173
        Neg Pred Value : 0.6939
            Prevalence : 0.6536
        Detection Rate : 0.5556
  Detection Prevalence : 0.6797
     Balanced Accuracy : 0.7458
      'Positive' Class : neg
```

Listing 16.2: Output of making predictions on unseen data using caret.

### 16.3 Create A Standalone Model

In this example, we have tuned a random forest with 3 different values for mtry and ntree set to 2,000. By printing the fit and the finalModel, we can see that the most accurate value for mtry was 2. Now that we know a good algorithm (random forest) and the good configuration (mtry=2, ntree=2000) we can create the final model directly using all of the training data.

We can lookup the rf random forest implementation used by caret in the Caret List of Models<sup>1</sup> and note that it is using the randomForest package and in turn the randomForest() function. The example creates a new model directly and uses it to make predictions on the new data, this case simulated with the verification dataset.

```
# load packages
library(caret)
library(mlbench)
library(randomForest)
# load dataset
data(Sonar)
set.seed(7)
# create 80%/20% for training and validation datasets
validationIndex <- createDataPartition(Sonar$Class, p=0.80, list=FALSE)
validation <- Sonar[-validationIndex,]
training <- Sonar[validationIndex,]
```

<sup>1</sup><https://topepo.github.io/caret/modelList.html>

```
# train a model and summarize model
set.seed(7)
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
fit.rf <- train(Class~., data=training, method="rf", metric="Accuracy",
   trControl=trainControl, ntree=2000)
print(fit.rf)
print(fit.rf$finalModel)
# create standalone model using all training data
set.seed(7)
finalModel <- randomForest(Class~., training, mtry=2, ntree=2000)
# make a predictions on "new data" using the final model
finalPredictions <- predict(finalModel, validation[,1:60])
confusionMatrix(finalPredictions, validation$Class)
```

Listing 16.3: Create a standalone model and make predictions on unseen data.

We can see that the estimated accuracy of the optimal configuration was 85.07%. We can also see that the accuracy of the final standalone model trained on all of the training dataset and predicting for the validation dataset was 82.93%, very close to our estimate.

```
Random Forest
167 samples
60 predictor
 2 classes: 'M', 'R'
No pre-processing
Resampling: Cross-Validated (10 fold, repeated 3 times)
Summary of sample sizes: 151, 150, 150, 150, 151, 150, ...
Resampling results across tuning parameters:
 mtry Accuracy Kappa Accuracy SD Kappa SD
  2 0.8507353 0.6968343 0.07745360 0.1579125
 31 0.8064951 0.6085348 0.09373438 0.1904946
 60 0.7927696 0.5813335 0.08768147 0.1780100
Accuracy was used to select the optimal model using the largest value.
The final value used for the model was mtry = 2.
...
Call:
randomForest(x = x, y = y, ntree = 2000, mtry = param$mtry)
             Type of random forest: classification
                   Number of trees: 2000
No. of variables tried at each split: 2
       OOB estimate of error rate: 14.37%
Confusion matrix:
  M R class.error
M 83 6 0.06741573
R 18 60 0.23076923
...
Confusion Matrix and Statistics
```

```
Reference
Prediction M R
        M 20 5
        R 2 14
              Accuracy : 0.8293
                95% CI : (0.6794, 0.9285)
   No Information Rate : 0.5366
   P-Value [Acc > NIR] : 8.511e-05
                Kappa : 0.653
Mcnemar's Test P-Value : 0.4497
           Sensitivity : 0.9091
           Specificity : 0.7368
        Pos Pred Value : 0.8000
        Neg Pred Value : 0.8750
            Prevalence : 0.5366
        Detection Rate : 0.4878
  Detection Prevalence : 0.6098
     Balanced Accuracy : 0.8230
       'Positive' Class : M
```

Listing 16.4: Output of predictions made by standalone model.

Some simpler models, like linear models can output their coefficients. This is useful, because from these, you can implement the simple prediction procedure in your programming language of choice and use the coefficients to get the same accuracy. This gets more difficult as the complexity of the representation used buy the algorithm increases.

#### 16.4 Save and Load Your Model

You can save your best models to a file so that you can load them up later and make predictions. In this example we split the Sonar dataset into a training dataset and a validation dataset. We take our validation dataset as new data to test our final model. We train the final model using the training dataset and our optimal parameters, then save it to a file called finalModel.rds in the local working directory.

The model is serialized. It can be loaded at a later time by calling the readRDS() function and assigning the object that is loaded (in this case a random forest fit) to a variable name. The loaded random forest is then used to make predictions on new data, in this case the validation dataset.

```
# load packages
library(caret)
library(mlbench)
library(randomForest)
library(doMC)
registerDoMC(cores=8)
# load dataset
data(Sonar)
set.seed(7)
```

```
# create 80%/20% for training and validation datasets
validationIndex <- createDataPartition(Sonar$Class, p=0.80, list=FALSE)
validation <- Sonar[-validationIndex,]
training <- Sonar[validationIndex,]
# create final standalone model using all training data
set.seed(7)
finalModel <- randomForest(Class~., training, mtry=2, ntree=2000)
# save the model to disk
saveRDS(finalModel, "./finalModel.rds")
# later...
# load the model
superModel <- readRDS("./finalModel.rds")
print(superModel)
# make a predictions on "new data" using the final model
finalPredictions <- predict(superModel, validation[,1:60])
confusionMatrix(finalPredictions, validation$Class)
```

Listing 16.5: Save and load a standalone model and make predictions on unseen data.

We can see that the accuracy on the validation dataset was 82.93%.

```
Confusion Matrix and Statistics
         Reference
Prediction M R
        M 20 5
        R 2 14
              Accuracy : 0.8293
               95% CI : (0.6794, 0.9285)
   No Information Rate : 0.5366
   P-Value [Acc > NIR] : 8.511e-05
                Kappa : 0.653
Mcnemar's Test P-Value : 0.4497
           Sensitivity : 0.9091
           Specificity : 0.7368
        Pos Pred Value : 0.8000
        Neg Pred Value : 0.8750
            Prevalence : 0.5366
        Detection Rate : 0.4878
  Detection Prevalence : 0.6098
     Balanced Accuracy : 0.8230
      'Positive' Class : M
```

Listing 16.6: Output of saving and loading a standalone model.

#### 16.5 Summary

In this lesson you discovered three recipes for working with final predictive models:

- 1. How to make predictions using the best model from caret tuning.
- 2. How to create a standalone model using the parameters found during caret tuning.
- 3. How to save and later load a standalone model and use it to make predictions.

#### 16.5.1 Next Step

This concludes your lessons on the specific predictive modeling machine learning tasks in R. You now have all of the pieces you need to be able to work through the tasks of a machine learning project. Next in Part III of this book you will discover how you can tie together all of these lessons into complete end-to-end machine learning projects.
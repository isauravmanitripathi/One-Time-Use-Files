## Chapter 13

# Compare The Performance of Machine Learning Algorithms

How do you compare the estimated accuracy of different machine learning algorithms effectively? In this lesson you will discover 8 techniques that you can use to compare machine learning algorithms in R. After completing this lesson, you will know:

- 1. How to compare model skill using a table summary.
- 2. How to review and compare model skill using a range of different plots.
- 3. How to compare model skill pair-wise using xy-plots.
- 4. How to check if the difference in model skill is statistically significant.

Let's get started.

## 13.1 Choose The Best Machine Learning Model

How do you choose the best model for your dataset? When you work on a machine learning project, you often end up with multiple good models to choose from. Each model will have different performance characteristics. Using resampling methods like k-fold cross validation, you can get an estimate for how accurate each model may be on unseen data. You need to be able to use these estimates to choose one or two best models from the suite of models that you have created.

#### 13.1.1 Compare Machine Learning Models Carefully

When you have a new dataset it is a good idea to visualize the data using a number of different graphing techniques in order to look at the data from different perspectives. The same idea applies to model selection. You should use a number of different ways of looking at the estimated accuracy of your machine learning algorithms in order to choose the one or two to finalize.

The way that you can do that is to use different visualization methods to show the average accuracy, variance and other properties of the distribution of estimated model accuracies. In the next section you will discover exactly how you can do that in R. This lesson is presented as a case study. Throughout the case study you will create a number of machine learning models for the Pima Indians diabetes dataset. You will then use a suite of different visualization techniques to compare the estimated accuracy of the models. This case study is split up into three sections:

- 1. Prepare Dataset. Load the packages and dataset ready to train the models.
- 2. Train Models. Train standard machine learning models on the dataset ready for evaluation.
- 3. Compare Models. Compare the trained models using 8 different techniques.

## 13.2 Prepare Dataset

The dataset used in this case study is the Pima Indians diabetes dataset loaded from the mlbench package first described in Chapter 5. It is a binary classification problem to determine whether a patient will have an onset of diabetes within the next 5 years. The input attributes are numeric and describe medical details for female patients. Let's load the packages and dataset for this case study.

```
# load packages
library(mlbench)
library(caret)
# load the dataset
data(PimaIndiansDiabetes)
```

Listing 13.1: Load packages and dataset.

## 13.3 Train Models

In this section we will train the 5 machine learning models that we will compare in the next section. We will use repeated cross validation with 10 folds and 3 repeats, a common standard configuration for comparing models. The evaluation metric is accuracy and kappa because they are easy to interpret. The algorithms were chosen for their diversity of representation and learning style. They include:

- Classification and Regression Trees (CART).
- Linear Discriminant Analysis (LDA).
- Support Vector Machine with Radial Basis Function (SVM).
- k-Nearest Neighbors (KNN).
- Random Forest (RF).

After the models are trained, they are added to a list and resamples() is called on the list of models. This function checks that the models are comparable and that they used the same training scheme (trainControl configuration). This object contains the evaluation metrics for each fold and each repeat for each algorithm to be evaluated. The functions that we use in the next section all expect an object with this data.

```
# prepare training scheme
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
# CART
set.seed(7)
fit.cart <- train(diabetes~., data=PimaIndiansDiabetes, method="rpart",
   trControl=trainControl)
# LDA
set.seed(7)
fit.lda <- train(diabetes~., data=PimaIndiansDiabetes, method="lda", trControl=trainControl)
# SVM
set.seed(7)
fit.svm <- train(diabetes~., data=PimaIndiansDiabetes, method="svmRadial",
   trControl=trainControl)
# KNN
set.seed(7)
fit.knn <- train(diabetes~., data=PimaIndiansDiabetes, method="knn", trControl=trainControl)
# Random Forest
set.seed(7)
fit.rf <- train(diabetes~., data=PimaIndiansDiabetes, method="rf", trControl=trainControl)
# collect resamples
results <- resamples(list(CART=fit.cart, LDA=fit.lda, SVM=fit.svm, KNN=fit.knn, RF=fit.rf))
```

Listing 13.2: Train machine learning models and collect resample statistics.

## 13.4 Compare Models

In this section we will look at 8 different techniques for comparing the estimated accuracy of the constructed models.

#### 13.4.1 Table Summary

The Table Summary is the easiest comparison that you can do, simply call the summary() function and pass it the resamples result. It will create a table with one algorithm for each row and evaluation metrics for each column.

```
# summarize differences between modes
summary(results)
```

Listing 13.3: Summarize model resample statistics.

I find it useful to look at the mean and the max columns.

```
Accuracy
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
CART 0.6234 0.7115 0.7403 0.7382 0.7760 0.8442 0
LDA 0.6711 0.7532 0.7662 0.7759 0.8052 0.8701 0
SVM 0.6711 0.7403 0.7582 0.7651 0.7890 0.8961 0
KNN 0.6184 0.6984 0.7321 0.7299 0.7532 0.8182 0
RF 0.6711 0.7273 0.7516 0.7617 0.7890 0.8571 0
Kappa
      Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
CART 0.1585 0.3296 0.3765 0.3934 0.4685 0.6393 0
```

LDA 0.2484 0.4196 0.4516 0.4801 0.5512 0.7048 0 SVM 0.2187 0.3889 0.4167 0.4520 0.5003 0.7638 0 KNN 0.1113 0.3228 0.3867 0.3819 0.4382 0.5867 0 RF 0.2624 0.3787 0.4516 0.4588 0.5193 0.6781 0

Listing 13.4: Output of model resample statistics.

#### 13.4.2 Box and Whisker Plots

Box and Whisker Plots are a useful way to look at the spread of the estimated accuracies for different methods and how they relate.

```
# box and whisker plots to compare models
scales <- list(x=list(relation="free"), y=list(relation="free"))
bwplot(results, scales=scales)
```

Listing 13.5: Calculate box and whisker plots.

Note that the boxes are ordered from highest to lowest mean accuracy. I find it useful to look at the mean values (dots) and the overlaps of the boxes (middle 50% of results).

![](_page_3_Figure_8.jpeg)

Figure 13.1: Compare Machine Learning Algorithms in R Box and Whisker Plots

#### 13.4.3 Density Plots

You can show the distribution of model accuracy as density plots. This is a useful way to evaluate the overlap in the estimated behavior of algorithms.

```
# density plots of accuracy
scales <- list(x=list(relation="free"), y=list(relation="free"))
densityplot(results, scales=scales, pch = "|")
```

Listing 13.6: Calculate density plots.

I like to look at the differences in the peaks as well as the spread or base of the distributions.

![](_page_4_Figure_6.jpeg)

Figure 13.2: Compare Machine Learning Algorithms in R Density Plots

#### 13.4.4 Dot Plots

These are useful plots as the show both the mean estimated accuracy as well as the 95% confidence interval (e.g. the range in which 95% of observed scores fell).

```
# dot plots of accuracy
scales <- list(x=list(relation="free"), y=list(relation="free"))
dotplot(results, scales=scales)
```

Listing 13.7: Calculate dot plots.

I find it useful to compare the means and eye-ball the overlap of the spreads between algorithms.

![](_page_5_Figure_2.jpeg)

Figure 13.3: Compare Machine Learning Algorithms in R Dot Plots

#### 13.4.5 Parallel Plots

Parallel Plots are another way to look at the data. It shows how each trial of each cross validation fold behaved for each of the algorithms tested. It can help you see how those hold-out subsets that were difficult for one algorithm affected other algorithms.

```
# parallel plots to compare models
parallelplot(results)
```

```
Listing 13.8: Calculate parallel plots.
```

This can be a tricky plot to interpret. I like to think that this can be helpful in thinking about how different methods could be combined in an ensemble prediction (e.g. stacking) at a later time, especially if you see correlated movements in opposite directions.

#### 13.4.6 Scatterplot Matrix

This create a scatterplot matrix of all fold-trial results for an algorithm compared to the same fold-trial results for all other algorithms. All pairs are plotted.

![](_page_6_Figure_1.jpeg)

Figure 13.4: Compare Machine Learning Algorithms in R Parallel Plots

```
# pair-wise scatterplots of predictions to compare models
splom(results)
```

Listing 13.9: Calculate scatterplot matrix plots.

This is invaluable when considering whether the predictions from two different algorithms are correlated. If weakly correlated, they are good candidates for being combined in an ensemble prediction. For example, eye-balling the graphs it looks like LDA and SVM look strongly correlated, as does SVM and RF. SVM and CART look weekly correlated.

![](_page_7_Figure_4.jpeg)

Figure 13.5: Compare Machine Learning Algorithms in R Scatterplot Matrix

#### 13.4.7 Pairwise xyPlots

You can zoom in on one pair-wise comparison of the accuracy of trial-folds for two machine learning algorithms with an xyplot.

# xyplot plots to compare models xyplot(results, models=c("LDA", "SVM"))

Listing 13.10: Calculate xy-plot.

In this case we can see the seemingly correlated accuracy of the LDA and SVM models.

![](_page_8_Figure_1.jpeg)

Figure 13.6: Compare Machine Learning Algorithms in R Pair-wise Scatterplot

#### 13.4.8 Statistical Significance Tests

You can calculate the significance of the differences between the metric distributions of different machine learning algorithms. We can summarize the results directly by calling the summary() function.

```
# difference in model predictions
diffs <- diff(results)
# summarize p-values for pair-wise comparisons
summary(diffs)
```

Listing 13.11: Calculate and summarize statistical significance.

We can see a table of pair-wise statistical significance scores. The lower diagonal of the table shows p-values for the null hypothesis (distributions are the same), smaller is better. We can see no difference between CART and KNN, we can also see little difference between the distributions for LDA and SVM.

The upper diagonal of the table shows the estimated difference between the distributions. If we think that LDA is the most accurate model from looking at the previous graphs, we can get an estimate of how much better than specific other models in terms of absolute accuracy. These scores can help with any accuracy claims you might want to make between specific algorithms.

```
p-value adjustment: bonferroni
Upper diagonal: estimates of the difference
Lower diagonal: p-value for H0: difference = 0
Accuracy
    CART LDA SVM KNN RF
CART -0.037759 -0.026908 0.008248 -0.023473
LDA 0.0050068 0.010851 0.046007 0.014286
SVM 0.0919580 0.3390336 0.035156 0.003435
KNN 1.0000000 1.218e-05 0.0007092 -0.031721
RF 0.1722106 0.1349151 1.0000000 0.0034441
```

Listing 13.12: Output of statistical significance.

A good tip is to increase the number of trials to increase the size of the populations and perhaps result in more precise p-values. You can also plot the differences, but I find the plots a lot less useful than the above summary table.

## 13.5 Summary

In this lesson you discovered 8 different techniques that you can use to compare the estimated accuracy of your machine learning models in R. The 8 techniques you discovered were:

- Table Summary.
- Box and Whisker Plots.
- Density Plots.
- Dot Plots.
- Parallel Plots.

- Scatterplot Matrix.
- Pairwise xyPlots.
- Statistical Significance Tests.

### 13.5.1 Next Step

In the last few lessons you have learned each element involved in spot-checking algorithms and now how to compare the skill of the algorithms that you have spot-checked. In the next lesson you will look at the first of two approaches that you can use to improve the skill of your models called algorithm tuning.
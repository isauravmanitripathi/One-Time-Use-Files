# Chapter 14

# Tune Machine Learning Algorithms

It is difficult to find a good machine learning algorithm for your problem. But once you do, how do you get the best performance out of it. In this lesson you will discover three ways that you can tune the parameters of a machine learning algorithm in R. After completing this lesson you will know:

- How to use the caret package to perform a grid or random search of algorithm parameters.
- How to use the tools that come with algorithms to tune parameters.
- How to extend caret algorithm tuning to search additional algorithm parameters.

Let's get started.

## 14.1 Get Better Accuracy From Top Algorithms

It is difficult to find a good or even a well performing machine learning algorithm for your dataset. Through a process of trial and error you can settle on a shortlist of algorithms that show promise, but how do you know which is the best. You could use the default parameters for each algorithm. These are the parameters set by rules of thumb or suggestions in books and research papers. But how do you know the algorithms that you are settling on are showing their best performance?

#### 14.1.1 Use Algorithm Tuning To Search For Algorithm Parameters

The answer is to search for good or even best combinations of algorithm parameters for your problem. You need a process to tune each machine learning algorithm to know that you are getting the most out of it. Once tuned, you can make an objective comparison between the algorithms on your shortlist. Searching for algorithm parameters can be difficult, there are many options, such as:

- What parameters to tune?
- What search method to use to locate good algorithm parameters?
- What test options to use to limit overfitting the training data?

## 14.2 Tune Machine Learning Algorithms

You can tune your machine learning algorithm parameters in R. Generally, the approaches in this section assume that you already have a shortlist of well performing machine learning algorithms for your problem from which you are looking to get better performance. An excellent way to create your shortlist of well performing algorithms is to use the caret package. In this lesson we will look at three methods that you can use in R to tune algorithm parameters:

- Using the caret R package.
- Using tools that come with the algorithm.
- Designing your own parameter search.

Before we start tuning, let's setup our environment and test data.

## 14.3 Test Setup

Let's take a quick look at the data and the algorithm we will use in this lesson.

#### 14.3.1 Test Dataset

In this case study, we will use the Sonar test problem described in Chapter 5. This is a dataset from the UCI Machine Learning Repository that describes radar returns as either bouncing of metal or rocks. It is a binary classification problem with 60 numerical input features that describe the properties of the radar return. This is not a particularly difficult dataset, but is non-trivial and interesting for this example. Let's load the required packages and load the dataset from the mlbench package.

```
# Load packages
library(randomForest)
library(mlbench)
library(caret)
# Load Dataset
data(Sonar)
dataset <- Sonar
x <- dataset[,1:60]
y <- dataset[,61]
```

Listing 14.1: Load packages and datasets.

#### 14.3.2 Test Algorithm

We will use the popular Random Forest algorithm as the subject of our algorithm tuning. Random Forest is not necessarily the best algorithm for this dataset, but it is a very popular algorithm and no doubt you will find tuning it a useful exercise in you own machine learning work.

When tuning an algorithm, it is important to have a good understanding of your algorithm so that you know what affect the parameters have on the model you are creating. In this case study, we will stick to tuning two parameters, namely the mtry and the ntree parameters that have the following affect on our random forest model. There are many other parameters, but these two parameters are perhaps the most likely to have the biggest effect on your final accuracy.

Direct from the help page for the randomForest() function in R:

- mtry: Number of variables randomly sampled as candidates at each split.
- ntree: Number of trees to grow.

Let's create a baseline for comparison by using the recommend defaults for each parameter and mtry=floor(sqrt(ncol(x))) or mtry=7 and ntree=500.

```
# Create model with default paramters
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
seed <- 7
metric <- "Accuracy"
set.seed(seed)
mtry <- sqrt(ncol(x))
tunegrid <- expand.grid(.mtry=mtry)
rfDefault <- train(Class~., data=dataset, method="rf", metric=metric, tuneGrid=tunegrid,
   trControl=trainControl)
print(rfDefault)
```

Listing 14.2: Calculate baseline performance of algorithm.

We can see our estimated accuracy is 81.3%.

```
Resampling results
 Accuracy Kappa Accuracy SD Kappa SD
 0.8138384 0.6209924 0.0747572 0.1569159
```

Listing 14.3: Output of baseline performance of algorithm.

## 14.4 Tune Using Caret

The caret package provides an excellent facility to tune machine learning algorithm parameters. Not all machine learning algorithms are available in caret for tuning. The choice of parameters is left to the developers of the package, namely Max Khun. Only those algorithm parameters that have a large effect (e.g. really require tuning in Khun's opinion) are available for tuning in caret.

As such, only mtry parameter is available in caret for tuning. The reason is its effect on the final accuracy and that it must be found empirically for a dataset. The ntree parameter is different in that it can be as large as you like, and continues to increase the accuracy up to some point. It is less difficult or critical to tune and could be limited by compute time available more than anything.

#### 14.4.1 Random Search

One search strategy that we can use is to try random values within a range. This can be good if we are unsure of what the value might be and we want to overcome any biases we may have for setting the parameter (like the suggested equation above). Let's try a random search for mtry using the caret package:

```
# Random Search
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3, search="random")
set.seed(seed)
mtry <- sqrt(ncol(x))
rfRandom <- train(Class~., data=dataset, method="rf", metric=metric, tuneLength=15,
   trControl=trainControl)
print(rfRandom)
plot(rfRandom)
```

Listing 14.4: Tune algorithm using random search.

Note, that we are using a test harness similar to that which we would use to spot-check algorithms. Both 10-fold cross validation and 3 repeats slows down the search process, but is intended to limit and reduce overfitting on the training dataset. It won't remove overfitting entirely. Holding back a validation set for final checking is a great idea if you can spare the data.

```
Resampling results across tuning parameters:
 mtry Accuracy Kappa Accuracy SD Kappa SD
 11 0.8218470 0.6365181 0.09124610 0.1906693
 14 0.8140620 0.6215867 0.08475785 0.1750848
 17 0.8030231 0.5990734 0.09595988 0.1986971
 24 0.8042929 0.6002362 0.09847815 0.2053314
 30 0.7933333 0.5798250 0.09110171 0.1879681
 34 0.8015873 0.5970248 0.07931664 0.1621170
 45 0.7932612 0.5796828 0.09195386 0.1887363
 47 0.7903896 0.5738230 0.10325010 0.2123314
 49 0.7867532 0.5673879 0.09256912 0.1899197
 50 0.7775397 0.5483207 0.10118502 0.2063198
 60 0.7790476 0.5513705 0.09810647 0.2005012
```

Listing 14.5: Output of tuning algorithm using random search.

We can see that the most accurate value for mtry was 11 with an accuracy of 82.1%.

#### 14.4.2 Grid Search

Another search you can use is to define a grid of algorithm parameters to try. Each axis of the grid is an algorithm parameter, and points in the grid are specific combinations of parameters. Because we are only tuning one parameter, the grid search is a linear search through a vector of candidate values.

```
# Grid Search
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3, search="grid")
set.seed(seed)
tunegrid <- expand.grid(.mtry=c(1:15))
rfGrid <- train(Class~., data=dataset, method="rf", metric=metric, tuneGrid=tunegrid,
   trControl=trainControl)
```

![](_page_4_Figure_1.jpeg)

Figure 14.1: Tune Random Forest Parameters in R Using Random Search

print(rfGrid) plot(rfGrid)

Listing 14.6: Tune algorithm using grid search.

We can see that the most accurate value for mtry was 2 with an accuracy of 83.78%.

```
Resampling results across tuning parameters:
 mtry Accuracy Kappa Accuracy SD Kappa SD
  1 0.8377273 0.6688712 0.07154794 0.1507990
  2 0.8378932 0.6693593 0.07185686 0.1513988
  3 0.8314502 0.6564856 0.08191277 0.1700197
  4 0.8249567 0.6435956 0.07653933 0.1590840
  5 0.8268470 0.6472114 0.06787878 0.1418983
  6 0.8298701 0.6537667 0.07968069 0.1654484
  7 0.8282035 0.6493708 0.07492042 0.1584772
  8 0.8232828 0.6396484 0.07468091 0.1571185
  9 0.8268398 0.6476575 0.07355522 0.1529670
 10 0.8204906 0.6346991 0.08499469 0.1756645
 11 0.8073304 0.6071477 0.09882638 0.2055589
 12 0.8184488 0.6299098 0.09038264 0.1884499
 13 0.8093795 0.6119327 0.08788302 0.1821910
 14 0.8186797 0.6304113 0.08178957 0.1715189
 15 0.8168615 0.6265481 0.10074984 0.2091663
```

Listing 14.7: Output of tuning algorithm using grid search.

## 14.5 Tune Using Algorithm Tools

Some algorithm implementations provide tools for tuning the parameters of the algorithm. For example, the random forest algorithm implementation in the randomForest package provides the tuneRF() function that searches for optimal mtry values given your data.

```
# Algorithm Tune (tuneRF)
set.seed(seed)
bestmtry <- tuneRF(x, y, stepFactor=1.5, improve=1e-5, ntree=500)
print(bestmtry)
```

Listing 14.8: Tune algorithm using algorithm tools.

You can see that the most accurate value for mtry was 10 with an OOBError of 0.1442308. This does not really match up with what we saw in the caret repeated cross validation experiment above, where mtry=10 gave an accuracy of 82.04%. Nevertheless, it is an alternate way to tune the algorithm.

mtry OOBError 5.OOB 5 0.1538462 7.OOB 7 0.1538462 10.OOB 10 0.1442308 15.OOB 15 0.1682692

Listing 14.9: Output of tuning algorithm using algorithm tools.

![](_page_6_Figure_1.jpeg)

Figure 14.2: Tune Random Forest Parameters in R Using Grid Search

![](_page_7_Figure_1.jpeg)

Figure 14.3: Tune Random Forest Parameters in R using tuneRF

## 14.6 Craft Your Own Parameter Search

Often you want to search for both the parameters that must be tuned (handled by caret) and the those that need to be scaled or adapted more generally for your dataset. You have to craft your own parameter search. Two popular recommendations are:

- Tune Manually: Write R code to create lots of models and compare their accuracy using caret.
- Extend Caret: Create an extension to caret that adds in additional parameters to caret for the algorithm you want to tune.

### 14.6.1 Tune Manually

We want to keep using caret because it provides a direct point of comparison to our previous models (apples to apples, even the same data splits) and because of the repeated cross validation test harness that we like as it reduces the severity of overfitting. One approach is to create many caret models for our algorithm and pass in a different parameters directly to the algorithm manually. Let's look at an example doing this to evaluate different values for ntree while holding mtry constant.

```
# Manual Search
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3, search="grid")
tunegrid <- expand.grid(.mtry=c(sqrt(ncol(x))))
modellist <- list()
for (ntree in c(1000, 1500, 2000, 2500)) {
 set.seed(seed)
 fit <- train(Class~., data=dataset, method="rf", metric=metric, tuneGrid=tunegrid,
     trControl=trainControl, ntree=ntree)
 key <- toString(ntree)
 modellist[[key]] <- fit
}
# compare results
results <- resamples(modellist)
summary(results)
dotplot(results)
```

Listing 14.10: Tune algorithm manually.

You can see that the most accurate value for ntree was perhaps 2,000 with a mean accuracy of 82.02% (a lift over our very first experiment using the default mtry value). The results perhaps suggest an optimal value for ntree between 2,000 and 2,500. Also note, we held mtry constant at the default value. We could repeat the experiment with a possible better mtry=2 from the experiment above, or try combinations of ntree and mtry in case they have interaction effects.

```
Models: 1000, 1500, 2000, 2500
Number of resamples: 30
Accuracy
     Min. 1st Qu. Median Mean 3rd Qu. Max. NA's
1000 0.600 0.8024 0.8500 0.8186 0.8571 0.9048 0
1500 0.600 0.8024 0.8095 0.8169 0.8571 0.9500 0
```

2000 0.619 0.8024 0.8095 0.8202 0.8620 0.9048 0 2500 0.619 0.8000 0.8095 0.8201 0.8893 0.9091 0

![](_page_9_Figure_2.jpeg)

Listing 14.11: Output of tuning algorithm manually.

Figure 14.4: Tune Random Forest Parameters in R Manually

#### 14.6.2 Extend Caret

Another approach is to create a new algorithm for caret to support. This is the same random forest algorithm you have been using, only modified so that it supports multiple tuning of multiple parameters. A risk with this approach is that the caret native support for the algorithm has additional or fancy code wrapping it that subtly but importantly changes it's behavior. You may need to repeat prior experiments with your custom algorithm support.

We can define our own algorithm to use in caret by defining a list that contains a number of custom named elements that the caret package looks for, such as how to fit and how to predict. See below for a definition of a custom random forest algorithm for use with caret that takes both an mtry and ntree parameters.

```
customRF <- list(type="Classification", library="randomForest", loop=NULL)
customRF$parameters <- data.frame(parameter=c("mtry", "ntree"), class=rep("numeric", 2),
   label=c("mtry", "ntree"))
customRF$grid <- function(x, y, len=NULL, search="grid") {}
```

```
customRF$fit <- function(x, y, wts, param, lev, last, weights, classProbs, ...) {
 randomForest(x, y, mtry=param$mtry, ntree=param$ntree, ...)
}
customRF$predict <- function(modelFit, newdata, preProc=NULL, submodels=NULL)
  predict(modelFit, newdata)
customRF$prob <- function(modelFit, newdata, preProc=NULL, submodels=NULL)
  predict(modelFit, newdata, type = "prob")
customRF$sort <- function(x) x[order(x[,1]),]
customRF$levels <- function(x) x$classes
```

Listing 14.12: Define custom algorithm in caret.

Now, let's make use of this custom list in our call to the caret train function, and try tuning different values for ntree and mtry.

```
# train model
trainControl <- trainControl(method="repeatedcv", number=10, repeats=3)
tunegrid <- expand.grid(.mtry=c(1:15), .ntree=c(1000, 1500, 2000, 2500))
set.seed(seed)
custom <- train(Class~., data=dataset, method=customRF, metric=metric, tuneGrid=tunegrid,
   trControl=trainControl)
summary(custom)
plot(custom)
```

Listing 14.13: Tune algorithm custom algorithm definition in caret.

This may take a minute or two to run. You can see that the most accurate values for ntree and mtry were 2,000 and 2 with an accuracy of 84.43%. We do perhaps see some interaction effects between the number of trees and the value of ntree. Nevertheless, if we had chosen the best value for mtry found using grid search of 2 (above) and the best value of ntree found using grid search of 2,000 (above), in this case we would have achieved the same level of tuning found in this combined search. This is a nice confirmation.

| mtry | ntree | Accuracy | Kappa | Accuracy SD Kappa SD           |           |
|------|-------|----------|-------|--------------------------------|-----------|
| 1    | 1000  |          |       | 0.8442424 0.6828299 0.06505226 | 0.1352640 |
| 1    | 1500  |          |       | 0.8394805 0.6730868 0.05797828 | 0.1215990 |
| 1    | 2000  |          |       | 0.8314646 0.6564643 0.06630279 | 0.1381197 |
| 1    | 2500  |          |       | 0.8379654 0.6693773 0.06576468 | 0.1375408 |
| 2    | 1000  |          |       | 0.8313781 0.6562819 0.06909608 | 0.1436961 |
| 2    | 1500  |          |       | 0.8427345 0.6793793 0.07005975 | 0.1451269 |
| 2    | 2000  |          |       | 0.8443218 0.6830115 0.06754346 | 0.1403497 |
| 2    | 2500  |          |       | 0.8428066 0.6791639 0.06488132 | 0.1361329 |
| 3    | 1000  |          |       | 0.8350216 0.6637523 0.06530816 | 0.1362839 |
| 3    | 1500  |          |       | 0.8347908 0.6633405 0.06836512 | 0.1418106 |
|      |       |          |       |                                |           |
| 15   | 1000  |          |       | 0.8091486 0.6110154 0.08455439 | 0.1745129 |
| 15   | 1500  |          |       | 0.8109668 0.6154780 0.08928549 | 0.1838700 |
| 15   | 2000  |          |       | 0.8059740 0.6047791 0.08829659 | 0.1837809 |
| 15   | 2500  |          |       | 0.8122511 0.6172771 0.08863418 | 0.1845635 |

Listing 14.14: Output of custom algorithm tuning in caret.

![](_page_11_Figure_1.jpeg)

Figure 14.5: Custom Tuning of Random Forest parameters in R

## 14.7 Summary

In this lesson you discovered the importance of tuning well performing machine learning algorithms in order to get the best performance from them. You worked through an example of tuning the Random Forest algorithm and discovered three ways that you can tune a well performing algorithm.

- 1. Using the caret package.
- 2. Using tools that come with the algorithm.
- 3. Designing your own parameter search.

### 14.7.1 Next Step

In this lesson you discovered how you can search for combinations of algorithm parameters that yield the best results. In the next lesson you will discover another method that you can use to improve you results by combining predictions from multiple models called an ensemble.
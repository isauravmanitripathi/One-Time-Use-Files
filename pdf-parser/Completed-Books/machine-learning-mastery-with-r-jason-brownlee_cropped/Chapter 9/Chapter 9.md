# Chapter 9

# Prepare Your Data For Machine Learning With Pre-Processing

Preparing data is required to get the best results from machine learning algorithms. In this lesson you will discover how to transform your data in order to best expose its structure to machine learning algorithms in R using the caret package. You will work through 8 popular and powerful data transforms with recipes that you can study or copy and paste int your current or next machine learning project. After completing this lesson you will know:

- How to use basic data transforms like scaling, centering, standardization and normalization.
- How to use power transforms like Box-Cox and Yeo-Johnson.
- How to use linear algebra transforms like PCA and ICA.

Let's get started.

#### 9.1 Need For Data Pre-Processing

You want to get the best accuracy from machine learning algorithms on your datasets. Some machine learning algorithms require the data to be in a specific form. Whereas other algorithms can perform better if the data is prepared in a specific way, but not always. Finally, your raw data may not be in the best format to expose the underlying structure and relationships to the predicted variables.

It is important to prepare your data in such a way that it gives various different machine learning algorithms the best chance on your problem. You need to pre-process your raw data as part of your machine learning project.

#### 9.1.1 Data Pre-Processing Methods

It is hard to know which data pre-processing methods to use. You can use rules of thumb such as:

- Instance based methods are more effective if the input attributes have the same scale.
- Regression methods can work better of the input attributes are standardized.

These are heuristics, but not hard and fast laws of machine learning, because sometimes you can get better results if you ignore them. You should try a range of data transforms with a suite of different machine learning algorithms. This will help you discover both good representations for your data and algorithms that are better at exploiting the structure that those representations expose.

It is a good idea to spot-check a number of transforms both in isolation as well as combinations of transforms. In the next section you will discover how you can apply data transforms in order to prepare your data in R using the caret package.

## 9.2 Data Pre-Processing in R

The caret package in R provides a number of useful data transforms. These transforms can be used in two ways:

- Standalone : Transforms can be modeled from training data and applied to multiple datasets. The model of the transform is prepared using the preProcess() function and applied to a dataset using the predict() function.
- Training : Transforms can be prepared and applied automatically during model evaluation. Transforms applied during training are prepared using the preProcess() and passed to the train() function via the preProcess argument.

A number of data pre-processing examples are presented in this section. They are presented using the standalone method, but you can just as easily use the prepared pre-processed model during model training. All of the pre-processing examples in this section are for numerical data. Note that the preProcess() function will skip over non-numeric data without error.

You can learn more about the data transforms provided by the caret package by reading the help for the preProcess() function by typing ?preProcess and by reading the Caret Pre-Processing page<sup>1</sup> . The data transforms presented are more likely to be useful for algorithms such as regression algorithms, instance-based methods (like KNN and LVQ), support vector machines and neural networks. They are less likely to be useful for tree and rule based methods.

#### 9.2.1 Summary of Transform Methods

Below is a quick summary of all of the transform methods supported in the argument to the preProcess() function in caret.

- BoxCox: apply a Box-Cox transform, values must be non-zero and positive.
- YeoJohnson: apply a Yeo-Johnson transform, like a BoxCox, but values can be negative.
- expoTrans: apply a power transform like BoxCox and YeoJohnson.
- zv: remove attributes with a zero variance (all the same value).
- nzv: remove attributes with a near zero variance (close to the same value).

<sup>1</sup><http://topepo.github.io/caret/preprocess.html>

- center: divide values by standard deviation.
- scale: subtract mean from values.
- range: normalize values.
- pca: transform data to the principal components.
- ica: transform data to the independent components.
- spatialSign: project data onto a unit circle.

The remaining sections of this lesson will practically demonstrate some of the more popular methods.

#### 9.3 Scale Data

The scale transform calculates the standard deviation for an attribute and divides each value by that standard deviation.

```
# load packages
library(caret)
# load the dataset
data(iris)
# summarize data
summary(iris[,1:4])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(iris[,1:4], method=c("scale"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, iris[,1:4])
# summarize the transformed dataset
summary(transformed)
```

Listing 9.1: Calculate scale data transform.

Running the recipe, you will see:

```
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300
Median :5.800 Median :3.000 Median :4.350 Median :1.300
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
Created from 150 samples and 4 variables
Pre-processing:
 - ignored (0)
 - scaled (4)
 Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :5.193 Min. : 4.589 Min. :0.5665 Min. :0.1312
```

1st Qu.:6.159 1st Qu.: 6.424 1st Qu.:0.9064 1st Qu.:0.3936 Median :7.004 Median : 6.883 Median :2.4642 Median :1.7055 Mean :7.057 Mean : 7.014 Mean :2.1288 Mean :1.5734 3rd Qu.:7.729 3rd Qu.: 7.571 3rd Qu.:2.8890 3rd Qu.:2.3615 Max. :9.540 Max. :10.095 Max. :3.9087 Max. :3.2798

Listing 9.2: Output of scale data transform.

#### 9.4 Center Data

The center transform calculates the mean for an attribute and subtracts it from each value.

```
# load packages
library(caret)
# load the dataset
data(iris)
# summarize data
summary(iris[,1:4])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(iris[,1:4], method=c("center"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, iris[,1:4])
# summarize the transformed dataset
summary(transformed)
```

Listing 9.3: Calculate center data transform.

Running the recipe, you will see:

```
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300
Median :5.800 Median :3.000 Median :4.350 Median :1.300
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
Created from 150 samples and 4 variables
Pre-processing:
 - centered (4)
 - ignored (0)
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :-1.54333 Min. :-1.05733 Min. :-2.758 Min. :-1.0993
1st Qu.:-0.74333 1st Qu.:-0.25733 1st Qu.:-2.158 1st Qu.:-0.8993
Median :-0.04333 Median :-0.05733 Median : 0.592 Median : 0.1007
Mean : 0.00000 Mean : 0.00000 Mean : 0.000 Mean : 0.0000
3rd Qu.: 0.55667 3rd Qu.: 0.24267 3rd Qu.: 1.342 3rd Qu.: 0.6007
Max. : 2.05667 Max. : 1.34267 Max. : 3.142 Max. : 1.3007
```

Listing 9.4: Output center data transform.

#### 9.5 Standardize Data

Combining the scale and center transforms will standardize your data. Attributes will have a mean value of 0 and a standard deviation of 1.

```
# load packages
library(caret)
# load the dataset
data(iris)
# summarize data
summary(iris[,1:4])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(iris[,1:4], method=c("center", "scale"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, iris[,1:4])
# summarize the transformed dataset
summary(transformed)
```

Listing 9.5: Calculate standardize data transform.

Notice how we can list multiple methods in a list when specifying the preProcess argument to the train() function. Running the recipe, you will see:

```
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300
Median :5.800 Median :3.000 Median :4.350 Median :1.300
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
Created from 150 samples and 4 variables
Pre-processing:
 - centered (4)
 - ignored (0)
 - scaled (4)
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :-1.86378 Min. :-2.4258 Min. :-1.5623 Min. :-1.4422
1st Qu.:-0.89767 1st Qu.:-0.5904 1st Qu.:-1.2225 1st Qu.:-1.1799
Median :-0.05233 Median :-0.1315 Median : 0.3354 Median : 0.1321
Mean : 0.00000 Mean : 0.0000 Mean : 0.0000 Mean : 0.0000
3rd Qu.: 0.67225 3rd Qu.: 0.5567 3rd Qu.: 0.7602 3rd Qu.: 0.7880
Max. : 2.48370 Max. : 3.0805 Max. : 1.7799 Max. : 1.7064
```

Listing 9.6: Output standardize data transform.

#### 9.6 Normalize Data

Data values can be scaled into the range of [0, 1] which is called normalization.

#### 9.7. Box-Cox Transform 64

```
library(caret)
# load the dataset
data(iris)
# summarize data
summary(iris[,1:4])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(iris[,1:4], method=c("range"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, iris[,1:4])
# summarize the transformed dataset
summary(transformed)
```

Listing 9.7: Calculate normalize data transform.

Running the recipe, you will see:

```
Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300
Median :5.800 Median :3.000 Median :4.350 Median :1.300
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
Created from 150 samples and 4 variables
Pre-processing:
 - ignored (0)
 - re-scaling to [0, 1] (4)
 Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :0.0000 Min. :0.0000 Min. :0.0000 Min. :0.00000
1st Qu.:0.2222 1st Qu.:0.3333 1st Qu.:0.1017 1st Qu.:0.08333
Median :0.4167 Median :0.4167 Median :0.5678 Median :0.50000
Mean :0.4287 Mean :0.4406 Mean :0.4675 Mean :0.45806
3rd Qu.:0.5833 3rd Qu.:0.5417 3rd Qu.:0.6949 3rd Qu.:0.70833
Max. :1.0000 Max. :1.0000 Max. :1.0000 Max. :1.00000
```

Listing 9.8: Output normalize data transform.

# 9.7 Box-Cox Transform

When an attribute has a Gaussian-like distribution but is shifted, this is called a skew. The distribution of an attribute can be shifted to reduce the skew and make it more Gaussian. The BoxCox transform can perform this operation (assumes all values are positive).

```
# load packages
library(mlbench)
library(caret)
# load the dataset
data(PimaIndiansDiabetes)
# summarize pedigree and age
```

```
summary(PimaIndiansDiabetes[,7:8])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(PimaIndiansDiabetes[,7:8], method=c("BoxCox"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, PimaIndiansDiabetes[,7:8])
# summarize the transformed dataset (note pedigree and age)
summary(transformed)
```

Listing 9.9: Calculate Box-Cox data transform.

Notice, we applied the transform to only two attributes that appear to have a skew. Running the recipe, you will see:

```
pedigree age
Min. :0.0780 Min. :21.00
1st Qu.:0.2437 1st Qu.:24.00
Median :0.3725 Median :29.00
Mean :0.4719 Mean :33.24
3rd Qu.:0.6262 3rd Qu.:41.00
Max. :2.4200 Max. :81.00
Created from 768 samples and 2 variables
Pre-processing:
 - Box-Cox transformation (2)
 - ignored (0)
Lambda estimates for Box-Cox transformation:
-0.1, -1.1
   pedigree age
Min. :-2.5510 Min. :0.8772
1st Qu.:-1.4116 1st Qu.:0.8815
Median :-0.9875 Median :0.8867
Mean :-0.9599 Mean :0.8874
3rd Qu.:-0.4680 3rd Qu.:0.8938
Max. : 0.8838 Max. :0.9019
```

Listing 9.10: Output Box-Cox data transform.

For more on this transform see the Box-Cox transform Wikiepdia<sup>2</sup> .

#### 9.8 Yeo-Johnson Transform

The YeoJohnson transform another power-transform like Box-Cox, but it supports raw values that are equal to zero and negative.

```
# load packages
library(mlbench)
library(caret)
# load the dataset
data(PimaIndiansDiabetes)
```

<sup>2</sup>[https://en.wikipedia.org/wiki/Power\\_transform](https://en.wikipedia.org/wiki/Power_transform)

```
# summarize pedigree and age
summary(PimaIndiansDiabetes[,7:8])
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(PimaIndiansDiabetes[,7:8], method=c("YeoJohnson"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, PimaIndiansDiabetes[,7:8])
# summarize the transformed dataset (note pedigree and age)
summary(transformed)
```

Listing 9.11: Calculate Yeo-Johnson data transform.

Running the recipe, you will see:

pedigree age Min. :0.0780 Min. :21.00 1st Qu.:0.2437 1st Qu.:24.00 Median :0.3725 Median :29.00 Mean :0.4719 Mean :33.24 3rd Qu.:0.6262 3rd Qu.:41.00 Max. :2.4200 Max. :81.00 Created from 768 samples and 2 variables Pre-processing: - ignored (0) - Yeo-Johnson transformation (2) Lambda estimates for Yeo-Johnson transformation: -2.25, -1.15 pedigree age Min. :0.0691 Min. :0.8450 1st Qu.:0.1724 1st Qu.:0.8484 Median :0.2265 Median :0.8524 Mean :0.2317 Mean :0.8530 3rd Qu.:0.2956 3rd Qu.:0.8580 Max. :0.4164 Max. :0.8644

Listing 9.12: Output Yeo-Johnson data transform.

#### 9.9 Principal Component Analysis Transform

The PCA transforms the data to return only the principal components, a technique form multivariate statistics and linear algebra. The transform keeps those components above the variance threshold (default=0.95) or the number of components can be specified (pcaComp). The result is attributes that are uncorrelated, useful for algorithms like linear and generalized linear regression.

```
# load the packages
library(mlbench)
# load the dataset
data(iris)
```

```
# summarize dataset
summary(iris)
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(iris, method=c("center", "scale", "pca"))
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, iris)
# summarize the transformed dataset
summary(transformed)
```

Listing 9.13: Calculate PCA data transform.

Notice that when we run the recipe that only two principal components are selected.

Sepal.Length Sepal.Width Petal.Length Petal.Width Species Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100 setosa :50 1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300 versicolor:50 Median :5.800 Median :3.000 Median :4.350 Median :1.300 virginica :50 Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199 3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800 Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500 Created from 150 samples and 5 variables Pre-processing: - centered (4) - ignored (1) - principal component signal extraction (4) - scaled (4) PCA needed 2 components to capture 95 percent of the variance Species PC1 PC2 setosa :50 Min. :-2.7651 Min. :-2.67732 versicolor:50 1st Qu.:-2.0957 1st Qu.:-0.59205 virginica :50 Median : 0.4169 Median :-0.01744 Mean : 0.0000 Mean : 0.00000 3rd Qu.: 1.3385 3rd Qu.: 0.59649 Max. : 3.2996 Max. : 2.64521

Listing 9.14: Output PCA data transform.

## 9.10 Independent Component Analysis Transform

Transform the data to the independent components. Unlike PCA, ICA retains those components that are independent. You must specify the number of desired independent components with the n.comp argument. This transform may be useful for algorithms such as Naive Bayes.

```
# load packages
library(mlbench)
library(caret)
# load the dataset
data(PimaIndiansDiabetes)
# summarize dataset
summary(PimaIndiansDiabetes[,1:8])
```

```
# calculate the pre-process parameters from the dataset
preprocessParams <- preProcess(PimaIndiansDiabetes[,1:8], method=c("center", "scale",
   "ica"), n.comp=5)
# summarize transform parameters
print(preprocessParams)
# transform the dataset using the parameters
transformed <- predict(preprocessParams, PimaIndiansDiabetes[,1:8])
# summarize the transformed dataset
summary(transformed)
```

Listing 9.15: Calculate ICA data transform.

Running the recipe, you will see:

| pregnant                                                                                                                                                                                                                                                                        | glucose           | pressure                         | triceps        | insulin                           | mass           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------|----------------|-----------------------------------|----------------|
| pedigree<br>Min.<br>: 0.000<br>Min.<br>:0.0780                                                                                                                                                                                                                                  | Min.<br>:<br>0.0  | Min.<br>:<br>0.00                | Min.<br>: 0.00 | Min.<br>:<br>0.0                  | Min.<br>: 0.00 |
| 1st Qu.: 1.000                                                                                                                                                                                                                                                                  | 1st Qu.: 99.0     | 1st Qu.: 62.00                   | 1st Qu.: 0.00  | 1st Qu.: 0.0                      | 1st Qu.:27.30  |
| 1st Qu.:0.2437<br>Median : 3.000                                                                                                                                                                                                                                                | Median :117.0     | Median : 72.00                   | Median :23.00  | Median : 30.5                     | Median :32.00  |
| Median :0.3725                                                                                                                                                                                                                                                                  |                   |                                  |                |                                   |                |
| Mean<br>: 3.845<br>Mean<br>:0.4719                                                                                                                                                                                                                                              | Mean<br>:120.9    | Mean<br>: 69.11                  | Mean<br>:20.54 | Mean<br>: 79.8                    | Mean<br>:31.99 |
| 3rd Qu.: 6.000<br>3rd Qu.:0.6262                                                                                                                                                                                                                                                | 3rd Qu.:140.2     | 3rd Qu.: 80.00                   | 3rd Qu.:32.00  | 3rd Qu.:127.2                     | 3rd Qu.:36.60  |
| Max.<br>:17.000<br>Max.<br>:2.4200                                                                                                                                                                                                                                              | Max.<br>:199.0    | Max.<br>:122.00                  | Max.<br>:99.00 | Max.<br>:846.0                    | Max.<br>:67.10 |
| age<br>Min.<br>:21.00<br>1st Qu.:24.00<br>Median :29.00<br>Mean<br>:33.24<br>3rd Qu.:41.00<br>Max.<br>:81.00<br>Created from 768 samples and 8 variables<br>Pre-processing:<br>- centered (8)<br>- independent component signal extraction (8)<br>- ignored (0)<br>- scaled (8) |                   |                                  |                |                                   |                |
| ICA used 5 components                                                                                                                                                                                                                                                           |                   |                                  |                |                                   |                |
| ICA1                                                                                                                                                                                                                                                                            | ICA2              | ICA3                             | ICA4           |                                   | ICA5           |
| Min.<br>:-5.7213                                                                                                                                                                                                                                                                | Min.<br>:-4.89818 | Min.<br>:-6.0289                 | Min.           | :-2.573436<br>Min.                | :-1.8815       |
| 1st Qu.:-0.4873                                                                                                                                                                                                                                                                 |                   | 1st Qu.:-0.48188 1st Qu.:-0.4693 |                | 1st Qu.:-0.640601 1st Qu.:-0.8279 |                |
| Median : 0.1813                                                                                                                                                                                                                                                                 |                   | Median : 0.05071 Median : 0.2987 |                | Median : 0.007582 Median :-0.2416 |                |
| Mean<br>: 0.0000                                                                                                                                                                                                                                                                | Mean<br>: 0.00000 | Mean<br>: 0.0000                 | Mean           | : 0.000000<br>Mean                | : 0.0000       |
| 3rd Qu.: 0.6839                                                                                                                                                                                                                                                                 |                   | 3rd Qu.: 0.56462 3rd Qu.: 0.6941 |                | 3rd Qu.: 0.638238 3rd Qu.: 0.7048 |                |
| Max.<br>: 2.1819                                                                                                                                                                                                                                                                | Max.<br>: 4.25611 | Max.<br>: 1.3726                 | Max.           | : 3.761017<br>Max.                | : 2.9622       |

Listing 9.16: Output ICA data transform.

## 9.11 Tips For Data Transforms

Below are some tips for getting the most out of data transforms.

- Actually Use Them. You are a step ahead if you are thinking about and using data transforms to prepare your data. It is an easy step to forget or skip over and often has a huge impact on the accuracy of your final models.
- Use a Variety. Try a number of different data transforms on your data with a suite of different machine learning algorithms.
- Review a Summary. It is a good idea to summarize your data before and after applying a transform to understand the effect it had. The summary() function can be very useful.
- Visualize Data. It is also a good idea to visualize the distribution of your data before and after to get a spatial intuition for the effect of the transform.

#### 9.12 Summary

In this lesson you discovered 8 data pre-processing methods that you can use on your data in R via the caret package:

- Data scaling
- Data centering
- Data standardization
- Data normalization
- The Box-Cox Transform
- The Yeo-Johnson Transform
- PCA Transform
- ICA Transform

You can practice with the recipes presented in this section or apply them on your current or next machine learning project.

#### 9.12.1 Next Step

You now know how to load data into R, understand it and pre-process it ready for modeling. In the next lesson you will discover methods that you can use to estimate the accuracy of machine learning algorithms on your data.
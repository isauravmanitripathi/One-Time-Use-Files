# **Regularization and shrinkage – LASSO and Ridge regression**

Now that we have covered OLS, we will try to improve on that by using regularization and coefficient shrinkage using LASSO and Ridge regression. One of the problems with OLS is that occasionally, for some datasets, the coefficients assigned to the predictor variables can grow to be very large. Also, OLS can end up assigning non-zero weights to all predictors and the total number of predictors in the final predictive model can be a very large number. Regularization tries to address both problems, that is, the problem of too many predictors and the problem of predictors with very large coefficients. Too many predictors in the final model is disadvantageous because it leads to overfitting, in addition to requiring more computations to predict. Predictors with large coefficients are disadvantageous because a few predictors with large coefficients can overpower the entire model's prediction, and small changes in predictor values can cause large swings in predicted output. We address this by introducing the concepts of regularization and shrinkage.

Regularization is the technique of introducing a penalty term on the coefficient weights and making that a part of the mean squared error, which regression tries to minimize. Intuitively, what this does is that it will let coefficient values grow, but only if there is a comparable decrease in MSE values. Conversely, if reducing the coefficient weights doesn't increase the MSE values too much, then it will shrink those coefficients. The extra penalty term is known as the regularization term, and since it results in a reduction of the magnitudes of coefficients, it is known as shrinkage.

Depending on the type of penalty term involving magnitudes of coefficients, it is either L1 regularization or L2 regularization. When the penalty term is the sum of the absolute values of all coefficients, this is known as L1 regularization (LASSO), and, when the penalty term is the sum of the squared values of the coefficients, this is known as L2

regularization (Ridge). It is also possible to combine both L1 and L2 regularization, and that is known as elastic net regression. To control how much penalty is added because of these regularization terms, we control it by tuning the regularization hyperparameter. In the case of elastic net regression, there are two regularization hyperparameters, one for the L1 penalty and the other one for the L2 penalty.

Let's apply Lasso regression to our dataset and inspect the coefficients in the following code. With a regularization parameter of 0.1, we see that the first predictor gets assigned a coefficient that is roughly half of what was assigned by OLS:

```
from sklearn import linear_model
# Fit the model
lasso = linear_model.Lasso(alpha=0.1)
lasso.fit(X_train, Y_train)
# The coefficients
print('Coefficients: \n', lasso.coef_)
```

This code will return the following output:

Coefficients: [ 0.01673918 -0.04803374]

If the regularization parameter is increased to 0.6, the coefficients shrink much further to [ 0. -0.00540562], and the first predictor gets assigned a weight of 0, meaning that predictor can be removed from the model. L1 regularization has this additional property of being able to shrink coefficients to 0, thus having the extra advantage of being useful for feature selection, in other words, it can shrink the model size by removing some predictors.

Now, let's apply Ridge regression to our dataset and observe the coefficients:

```
from sklearn import linear_model
# Fit the model
ridge = linear_model.Ridge(alpha=10000)
ridge.fit(X_train, Y_train)
```

```
# The coefficients
print('Coefficients: \n', ridge.coef_)
```

This code will return the following output:

```
Coefficients:
[[ 0.01789719 -0.04351513]]
```

#### **Decision tree regression**

The disadvantage of the regression methods we've seen so far is that they are all linear models, meaning they can only capture relationships between predictors and target variables if the underlying relationship between them is linear.

Decision tree regression can capture non-linear relationships, thus allowing for more complex models. Decision trees get their name because they are structured like an upside-down tree, with decision nodes or branches and result nodes or leaf nodes. We start at the root of the tree and then, at each step, we inspect the value of our predictors and pick a branch to follow to the next node. We continue following branches until we get to a leaf node and our final prediction is then the value of that leaf node. Decision trees can be used for classification or regression, but here, we will look at using it for regression only.

# **Creating predictive models using linear classification methods**

In the first part of this chapter, we reviewed trading strategies based on regression machine learning algorithms. In this second part, we will focus on the classification of machine learning algorithms and another supervised machine learning method utilizing known datasets to make predictions. Instead of the output variable of the regression being a numerical (or continuous) value, the classification output is a categorical (or discrete value). We will use the same method as the regression analysis by finding the mapping function (f) such that whenever there is new input data (x), the output variable (y) for the dataset can be predicted.

In the following subsections, we will review three classification machine learning methods:

- K-nearest neighbors
- Support vector machine
- Logistic regression

#### **K-nearest neighbors**

**K-nearest neighbors** (or **KNN**) is a supervised method. Like the prior methods we saw in this chapter, the goal is to find a function predicting an output, *y*, from an unseen observation, *x*. Unlike a lot of other methods (such as linear regression), this method doesn't use any specific assumption about the distribution of the data (it is referred to as a non-parametric classifier).

The KNN algorithm is based on comparing a new observation to the *K* most similar instances. It can be defined as a distance metric between two data points. One of the most used frequently methods is the Euclidean distance. The following is the derivative:

$$d(x,y) = (x1-y1)^2 + (x2-y2)^2 + ... + (xn-yn)^2$$

When we review the documentation of the Python function, KNeighborsClassifier, we can observe different types of parameters:

One of them is the parameter, *p*, which can pick the type of distance.

- When *p=1*, the Manhattan distance is used. The Manhattan distance is the sum of the horizontal and vertical distances between two points.
- When *p=2*, which is the default value, the Euclidean distance is used.
- When *p>2*, this is the Minkowski distance, which is a generalization of the Manhattan and Euclidean methods. *d(x,y)=(|x1−y1|^p+|x2−y2|^p+… +|xn−yn|^p)^1/p.*

The algorithm will calculate the distance between a new observation and all the training data. This new observation will belong to the group of *K* points that are the closest to this new observation. Then, condition probabilities will be calculated for each class. The new observation will be assigned to the class with the highest probability. The weakness of this method is the time to associate the new observation to a given group.

In the code, in order to implement this algorithm, we will use the functions we declared in the first part of this chapter:

1. Let's get the Google data from January 1, 2001 to January 1, 2018:

```
goog_data=load_financial_data(start_date='2001-01-01',
 end_date = '2018-01-01',
 output_file='goog_data_large.pkl')
```

2. We create the rule when the strategy will take a long position (+1) and a short position (-1), as shown in the following code:

```
X,Y=create_trading_condition(goog_data)
```

3. We prepare the training and testing dataset as shown in the following code:

```
X_train,X_test,Y_train,Y_test=\
 create_train_split_group(X,Y,split_ratio=0.8)
```

4. In this example, we choose a KNN with *K=15*. We will train this model using the training dataset as shown in the following code:

```
knn=KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, Y_train)
accuracy_train = accuracy_score(Y_train, knn.predict(X_train))
accuracy_test = accuracy_score(Y_test, knn.predict(X_test))
```

5. Once the model is created, we are going to predict whether the price goes up or down and store the values in the original data frame, as shown in the following code:

```
goog_data['Predicted_Signal']=knn.predict(X)
```

6. In order to compare the strategy using the KNN algorithm, we will use the return of the GOOG symbol without d, as shown in the following code:

```
goog_data['GOOG_Returns']=np.log(goog_data['Close']/
 goog_data['Close'].shift(1))
cum_goog_return=calculate_return(goog_data,split_value=len(X_train),symbol='GOOG')
cum_strategy_return= calculate_strategy_return(goog_data,split_value=len(X_train))
plot_chart(cum_goog_return, cum_strategy_return,symbol='GOOG')
```

This code will return the following output. Let's have a look at the plot:

![](_page_7_Figure_0.jpeg)

### **Support vector machine**

**Support vector machine** (**SVM**) is a supervised machine learning method. As previously seen, we can use this method for regression, but also for classification. The principle of this algorithm is to find a hyper plan that separates the data into two classes.

Let's have a look at the following code, that implements the same:

```
# Fit the model
svc=SVC()
svc.fit(X_train, Y_train)
# Forecast value
goog_data['Predicted_Signal']=svc.predict(X)
goog_data['GOOG_Returns']=np.log(goog_data['Close']/
 goog_data['Close'].shift(1))
cum_goog_return=calculate_return(goog_data,split_value=len(X_train),symbol='GOOG')
cum_strategy_return= calculate_strategy_return(goog_data,split_value=len(X_train))
plot_chart(cum_goog_return, cum_strategy_return,symbol='GOOG')
```

In this example, the following applies:

- Instead of instantiating a class to create a KNN method, we used the SVC class.
- The class constructor has several parameters adjusting the behavior of the method to the data you will work on.
- The most important one is the parameter kernel. This defines the method of building the hyper plan.
- In this example, we just use the default values of the constructor.

Now, let's have a look at the output of the code:

![](_page_9_Figure_0.jpeg)

## **Logistic regression**

Logistic regression is a supervised method that works for classification. Based on linear regression, logistic regression transforms its output using the logistic sigmoid, returning a probability value that maps different classes:

![](_page_10_Figure_2.jpeg)

# **Summary**

In this chapter, we got a basic understanding of how to use machine learning in trading. We started with going through the essential terminology and notation. We learned to create predictive models that predict price movement using linear regression methods. We built several codes using Python's scikit-learn library. We saw how to create predictive models that predict buy and sell signals using linear classification methods. We also demonstrated how to apply these machine learning methods to a simple trading strategy. We also went through the tools that we can use to create a trading strategy.

The next chapter will introduce trading rules that can help to improve your trading strategies.
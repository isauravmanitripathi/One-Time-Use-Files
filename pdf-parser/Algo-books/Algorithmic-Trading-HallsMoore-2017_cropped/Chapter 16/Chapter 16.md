## Chapter 16

# Supervised Learning

Supervised Learning is the most widely utilised form of machine learning, since it performs two very general learning tasks across a multitude of domains. These tasks are classification and regression.

Classification problems involve estimating membership of a set of features into a particular categorical group. One example might be determining whether a patient is likely to possess a disease or not (binary class membership) from MRI scan data. A commonly-cited financial example is predicting whether an asset will rise or fall in price the following day, based on N days of asset price history.

Regression problems involve estimating a real-valued response from a set of features. One example would be estimating the sales volume of a product based on separate budget allocations to different forms of advertising, such as TV, radio or internet ads. A financial example would be to predict the actual value of an asset in the following day from its past price history, not just whether it has risen or fallen.

In this book techniques from both aspects of supervised learning will be considered.

### 16.1 Mathematical Framework

There are two approaches used to provide a mathematical formalism to machine learning.

The first approach formulates the problem in terms of function estimation. The "true" response variable y (categorical or real-valued) is modelled as a function f = f(x). The predictors (or features) x ∈ R p is a p-dimensional vector containing feature measurements. In addition to f there is additional noise containing information not available within x. is often assumed to be normally distributed with mean zero and variance σ 2 :

$$y = f(\mathbf{x}) + \epsilon \tag{16.1}$$

The goal of machine learning under a function estimation approach is to make an estimate of y, denoted by yˆ by attempting to find a function ˆf which "best" approximates f. Once this ˆf has been obtained it is straightforward to estimate any new yˆ given a new predictor vector xtest.

In some instances however it is harder to choose between values when classifying or regressing, as there may be some ambiguity from the feature vectors. This motivates the second approach to machine learning, which is the probabilistic formulation.

This approach reframes the problem into one of estimating the form of a probability distribution, known as conditional density estimation[51, 71]. In the supervised learning approach this probability distribution is given as p(y | x; θ). This is a conditional probability distribution, which represents the probability of y taking on any value (or category) given the feature values x, with a model parametrised by θ. It is implicitly assumed that a model form exists and that this model is applied to a set of finite feature data, often denoted by D.

Notice that although the probabilistic formulation is very different from the functional approximation approach, it is attempting to carry out the same task. That is, if a feature vector x is provided then the goal is to probabilistically estimate the "best" value of y.

The benefit of utilising this probabilistic approach is that probabilities can be assigned to different values of y, thus leading to a more general mechanism for choosing between these values.

In practice, the value of y with the highest probability is usually chosen as the best guess. However in quantitative finance the consequences of an incorrect choice can be severe as large losses can be generated. Hence threshold values are often used to ensure that the probability assigned to a particular value is significantly high and much larger than other values, reflecting a strong confidence in a choice.

### 16.2 Classification

In the classification setting y is a categorical value and is allowed to take values from a finite set of possible choices, K. These values need not be numerical, as in the case of object detection in a photo, where the (binary) class values might be "face detected" or "no face detected".

This problem is formalised as attempting to estimate p(y = k | x), for a particular k ∈ K. To estimate the best guess of y the mode of this distribution is used:

$$\hat{y} = \hat{f}(\mathbf{x}) = \operatorname{argmax}_{k \in K} p(y = k \mid \mathbf{x}) \tag{16.2}$$

That is, the best estimate for y, yˆ, is given by the argument k that maximises the value of p(y = k | x). In the Bayesian interpretation this value is known as the Maximum A Posteriori (MAP) estimate.

Common classification mechanisms include Logistic Regression (despite the name!), Naive Bayes Classifiers, Support Vector Machines and Deep Convolution Neural Networks.

Classification will be utilised in this book primarily to estimate class membership of documents for natural language processing.

### 16.3 Regression

In the regression framework the goal is similar to classification except that y ∈ R. That is, y is real-valued rather than categorical. This does not alter the mathematical goal of attempting to estimate a conditional probability distribution. The goal is still to estimate yˆ. However, the argument that maximises the the probability distribution (the mode) is now real-valued:

$$\hat{y} = \hat{f}(\mathbf{x}) = \operatorname{argmax}_{z \in \mathbb{R}} p(y = z \mid \mathbf{x}) \tag{16.3}$$

Common regression techniques include Linear Regression, Support Vector Regression and Random Forests.

Regression will be utilised in this book to estimate future asset prices in an intraday trading strategy, give previously known information.

#### 16.3.1 Financial Example

To make this concrete consider an example of modelling the next days price of the London-based equity Royal Dutch Shell (LSE:RDSB) via the historical prices of crude oil and natural gas.

Each day, which is indexed by i, has an associated pair (x<sup>i</sup> , yi) representing the feature vector and response for that day. The feature vector x<sup>i</sup> represents the historical prices of crude oil (cij ) at current day i and historical lag j; similarly for natural gas (gij ), over a period of N days, itself indexed by j ∈ 1, . . . , N. y<sup>i</sup> represents the price of RDSB tomorrow, that is at i + 1.

In this example the goal is to estimate the function f that relates tomorrows price for RDSB with the historical prices of crude oil and natural gas.

### 16.4 Training

Now that the probabilistic formulation has been defined it remains to discuss how it is possible to "supervise" or "train" the model with a specific set of data.

In order to train the model it is necessary to define a loss function between the true value of the response y and its estimate from the model yˆ, given by L(y, yˆ).

In the classification setting common loss models include the 0-1 loss and the cross-entropy. In the regression setting a common loss model is given by the Mean Squared Error (MSE):

$$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|^2 \tag{16.4}$$

This states the the total error of a model given a particular set of data is the average of the sum of the squared differences between all of the training values y<sup>i</sup> and their associated estimates yˆi .

This loss function essentially penalises estimate values far from their true values quite heavily, as the differences are squared. Notice also that the important aspect is the squared distance between values, not whether they are positive or negative deviations. MSE will be discussed in more depth in the next chapter on Linear Regression.

Equipped with this loss function it is now possible to make estimates of ˆf, and thus yˆ, by carrying out "fitting" algorithms on particular machine learning techniques that attempt to minimise the value of these loss functions, by adjusting the parameters θ of the model.

A minimal value of a loss function states that the errors between the true values and the estimated values are not too severe. This leads to the hope that the model will perform similarly when exposed to data that it has not been "trained" on.

However, a significant concern arises at this stage known as the bias-variance tradeoff. Details will not be provided here as they are discussed in depth in the chapter on Cross Validation. However, the essence of the problem is that if the loss function is minimised too severely, then the generalisation performance of the model can decrease substantially. The model has been "overfit" to the data used to train it and has not "learned" to generalise to new, unseen data.

The bias-variance tradeoff is of extreme importance in quantitative trading. A badly fit model can lead to substantial losses if it is deployed in production. Much of professional quantitative trading research goes into minimising the problems associated with overfit models.
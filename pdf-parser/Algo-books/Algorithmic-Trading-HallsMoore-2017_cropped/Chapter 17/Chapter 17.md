## Chapter 17

# Linear Regression

In this chapter a familiar statistical technique, linear regression, will be introduced in a more rigourous mathematical setting under a probabilistic, supervised learning interpretation. By studying a well-known technique in slightly more mathematical rigour than is often utilised it simplifies the extensions to more complex machine learning models discussed in subsequent chapters.

The chapter will begin by defining multiple linear regression and placing it in a probabilistic supervised learning framework. From there the optimal estimate for its parameters will be derived via a statistical technique known as maximum likelihood estimation (MLE).

To demonstrate how to fit linear regression on simulated data the Python Scikit-Learn library will be used. This will have the benefit of introducing the Scikit-Learn machine learning API, which remains similar across many differing machine learning models.

This chapter and a selection of those that follow are more mathematically rigourous than other chapters have been so far. The rationale for this is to introduce the more advanced probabilistic interpretation which pervades machine learning research. Once a few examples of simpler models in such a framework have been demonstrated it simplifies the task of studying the more advanced machine learning research papers for useful trading ideas.

## 17.1 Linear Regression

Linear regression is a familiar statistical technique. It is often taught at highschool, albeit in a simplified manner. It is generally the first technique considered when studying supervised learning since it allows many of the more advanced machine learning concepts to be discussed in a vastly simplified setting.

Formally, multiple linear regression states that a scalar response value y is a linear function of its feature inputs x. That is:

$$y(\mathbf{x}) = \beta^T \mathbf{x} + \epsilon = \sum_{j=0}^p \beta_j x_j + \epsilon \tag{17.1}$$

Where β T , x ∈ R <sup>p</sup>+1 and ∼ N (µ, σ<sup>2</sup> ). That is, β <sup>T</sup> and x are both real-valued vectors of dimension p + 1 and , the error or residual term, is normally distributed with mean µ and variance σ 2 . represents the difference between the predictions made by the linear regression and the true value of the response variable.

Note that β T , which represents the transpose of the vector β, and x are both p+1-dimensional, rather than p dimensional, because of the need to include an intercept term. β <sup>T</sup> = (β0, β1, . . . , βp), while x = (1, x1, . . . , xp). The single unity '1' is included in x as a notational "trick" to allow linear regression to be written in matrix notation.

## 17.2 Probabilistic Interpretation

An alternative way to look at linear regression is to consider it as a joint probability model as discussed in Hastie et al (2009)[51] and Murphy (2012)[71]. A joint probability model describes the behaviour of how the joint probability of the response y is conditional on the values of the feature vector x, along with any parameters of the model, themselves given by the vector θ. This leads to a mathematical model of the form p(y | x, θ). This is known as a conditional probability density (CPD) model since it involves y conditional on the features x and parameters θ.

Linear regression can be written as a CPD in the following manner:

$$p(y \mid \mathbf{x}, \theta) = \mathcal{N}(y \mid \mu(\mathbf{x}), \sigma^2(\mathbf{x})) \tag{17.2}$$

For linear regression it is assumed that µ(x) is linear and so µ(x) = β <sup>T</sup> x. It must also be assumed that the variance in the model is fixed. In particular this means that that the variance does not depend on x and that σ 2 (x) = σ 2 is a constant. Thus the full parameter vector consists of both the feature coefficients β and the variance σ 2 , given by θ = (β, σ<sup>2</sup> ).

Recall that such a probabilistic interpretation was considered in the chapter on Bayesian Linear Regression.

What is the rationale for generalising a simple technique such as linear regression in this manner? The primary benefit is that it becomes more straightforward to see how other models, especially those which handle non-linearities, fit into the same probabilistic framework. This allows derivation of results across models using similar techniques.

If only a single-dimensional feature x is considered, that is x = (1, x), it is possible to plot p(y | x, θ) against y and x to see this joint distribution graphically. In order to do so the parameters β = (β0, β1) and σ <sup>2</sup> must be fixed. The following code snippet comprises a Python script that uses Matplotlib to display the distribution:

#### # lin\_reg\_distribution\_plot.py

```
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import norm
```

```
if __name__ == "__main__":
    # Set up the X and Y dimensions
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(0, 20, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    # Create the univarate normal coefficients
    # of intercept and slope, as well as the
    # conditional probability density
    beta0 = -5.0
    beta1 = 0.5
    Z = norm.pdf(Y, beta0 + beta1*X, 1.0)
    # Plot the surface with the "coolwarm" colormap
    surf = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False
    )
    # Set the limits of the z axis and major line locators
    ax.set_zlim(0, 0.4)
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Label all of the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('P(Y|X)')
    # Adjust the viewing angle and axes direction
    ax.view_init(elev=30., azim=50.0)
    ax.invert_xaxis()
    ax.invert_yaxis()
    # Plot the probability density
    plt.show()
```

The output is given in Figure 17.1.

The plot highlights how the expectation of the response y is linearly dependent upon x. The "peak" of the distribution follows a linear path as x increases. The uncertainty associated with the error of the model is represented by a normally-distributed spread around the peak for each x. Notice in particular that the spread width does not change as x increases. This is a key assumption used in linear regression models, namely that the variance does not increase with

![](_page_3_Figure_0.jpeg)

Figure 17.1: Plot of p(y | x, θ) against y and x, influenced from a similar plot in Murphy (2012)[71]

the feature increase.

#### 17.2.1 Basis Function Expansion

One benefit of a probabilistic interpretation is the ease of modelling non-linear relationships by replacing the feature vector x with a transformation function φ(x):

$$p(y \mid \mathbf{x}, \theta) = (y \mid \beta^T \phi(\mathbf{x}), \sigma^2) \tag{17.3}$$

For x = (1, x1, x2, x3), say, it is possible to create a φ that includes higher order terms such as cross-terms, e.g.:

$$\phi(\mathbf{x}) = (1, x_1, x_1^2, x_2, x_2^2, x_1 x_2, x_3, x_3^2, x_1 x_3, \ldots) \tag{17.4}$$

A key point is that while this function is not linear in the features x it is still linear in the parameters β. Hence it is still called a linear regression.

Such a modification using a transformation function φ is known as a basis function expansion. These transformations can be used to generalise linear regression to many non-linear models. One such approach is given in the chapter on Support Vector Machines using the "kernel trick".

## 17.3 Maximum Likelihood Estimation

With the model specification in hand it is now appropriate to discuss how the optimal linear regression coefficients β are chosen to best fit the data. In the univariate case this is often known colloquially as "finding the line of best fit". However in the multivariate case considered here the feature vector is p + 1-dimensional, that is x ∈ R <sup>p</sup>+1. Hence the task is generalised to finding a p-dimensional hyperplane of best bit.

The main mechanism for finding parameters of statistical models is known as maximum likelihood estimation (MLE). While the MLE for linear regression will be derived here for completeness in this simple case, it is not generally relevant to quant trading models as most software libraries will abstract away the process.

#### 17.3.1 Likelihood and Negative Log Likelihood

MLE is an optimisation process carried out for a specific model on a particular batch of data. It is a directed algorithmic search through a multidimensional space of possible parameter choices that attempts to answer the following question: If the data were to have been generated by the model, what parameters were most likely to have been used? That is, what is the probability of seeing the data D, given a specific set of parameters θ?

Once again this reduces to a conditional probability density problem. The value sought is the θ that maximises p(D | θ). This CPD is known as the likelihood and was briefly discussed in the introductory chapter on Bayesian statistics.

This problem can be formulated as searching for the mode of p(D | θ), which is denoted by ˆθ. For reasons of computational ease an equivalent task of maximising the natural logarithm of the CPD, rather than the CPD itself, is often carried out:

$$\hat{\theta} = \operatorname{argmax}_{\theta} \log p(\mathcal{D} \mid \theta) \tag{17.5}$$

In linear regression problems an assumption is made that the feature vectors are all independent and identically distributed (iid). This simplifies the solution of the log-likelihood problem by making use of properties of natural logarithms. The natural log properties allow conversion from a product of probabilities to a sum of probabilities, which vastly simplifies subsequent differentiation necessary for the optimisation algorithm:

$$\mathcal{L}(\theta) := \log p(\mathcal{D} \mid \theta) \tag{17.6}$$

$$= \log \left( \prod_{i=1}^{N} p(y_i \mid \mathbf{x}_i, \theta) \right) \tag{17.7}$$

$$= \sum_{i=1}^{N} \log p(y_i \mid \mathbf{x}_i, \theta) \tag{17.8}$$

An additional computational reason makes it more straightforward to minimise the negative of the log-likelihood rather than maximise the log-likelihood itself. It is simple enough to append a minus sign in front of the log-likelihood expression to give us the negative log-likelihood (NLL):

$$\text{NLL}(\theta) = -\sum_{i=1}^{N} \log p(y_i \mid \mathbf{x}_i, \theta)$$
 (17.9)

This is the function that will be minimised. By doing so the optimal maximum likelihood estimate for the β coefficients will be derived. It is carried out by an algorithm known as ordinary least squares (OLS).

#### 17.3.2 Ordinary Least Squares

Restated once again, the current goal is to derive the optimal set of β coefficients that are "most likely" to have generated the data for a specific set of training data. These coefficients will form a hyperplane of "best fit" through this data set. The process is carried out as follows:

- 1. Use the definition of the normal distribution to expand the negative log likelihood function
- 2. Utilise the properties of logarithms to reformulate this in terms of the Residual Sum of Squares (RSS), which is equivalent to the sum of each residual across all observations
- 3. Rewrite the residuals in matrix form, creating the data matrix X, which is N × (p + 1) dimensional, and formulate the RSS as a matrix equation
- 4. Differentiate this matrix equation with respect to (w.r.t) the parameter vector β and set the equation to zero (with some assumptions on X)
- 5. Solve the subsequent equation for β to receive βˆOLS, the ordinary least squares (OLS) estimate.

The next section will closely follow the treatments of Hastie et al (2009)[51] and Murphy (2012)[71]. The first step is to expand the NLL using the formula for a normal distribution:

$$\text{NLL}(\theta) = -\sum_{i=1}^{N} \log p(y_i \mid \mathbf{x}_i, \theta) \tag{17.10}$$

$$= -\sum_{i=1}^{N} \log \left[ \left( \frac{1}{2\pi\sigma^2} \right)^{\frac{1}{2}} \exp \left( -\frac{1}{2\sigma^2} (y_i - \beta^T \mathbf{x}_i)^2 \right) \right]$$
(17.11)

$$= -\sum_{i=1}^{N} \frac{1}{2} \log \left( \frac{1}{2\pi\sigma^2} \right) - \frac{1}{2\sigma^2} (y_i - \beta^T \mathbf{x}_i)^2 \tag{17.12}$$

$$= -\frac{N}{2} \log \left( \frac{1}{2\pi\sigma^2} \right) - \frac{1}{2\sigma^2} \sum_{i=1}^{N} (y_i - \beta^T \mathbf{x}_i)^2 \tag{17.13}$$

$$= -\frac{N}{2} \log \left(\frac{1}{2\pi\sigma^2}\right) - \frac{1}{2\sigma^2} \text{RSS}(\beta) \tag{17.14}$$

Where RSS(β) := P<sup>N</sup> <sup>i</sup>=1(y<sup>i</sup> − β <sup>T</sup> xi) 2 is the Residual Sum of Squares, also known as the Sum of Squared Errors (SSE).

Since the first term in the equation is a constant it is only necessary to minimise the RSS, which is sufficient for producing the optimal parameter estimate.

To simplify the notation the latter term can be written in matrix form. By defining the N × (p + 1) matrix X it is possible to write the RSS term as:

$$RSS(\beta) = (\mathbf{y} - \mathbf{X}\beta)^{T} (\mathbf{y} - \mathbf{X}\beta)$$
(17.15)

This term is now differentiated w.r.t. the parameter variable β:

$$\frac{\partial RSS}{\partial \beta} = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\beta) \tag{17.16}$$

A key assumption about the data is made here. It is necessary for the matrix X<sup>T</sup> X to be positive-definite, which is only the case if there are more observations than there are dimensions. If this is not the case (which is extremely common in high-dimensional data settings) then it is not possible to find a unique set of β coefficients and thus the following matrix equation will not hold.

Under the assumption of a positive-definite X<sup>T</sup> X the differentiated equation is set to zero and solved for β:

$$\mathbf{X}^T(\mathbf{y} - \mathbf{X}\beta) = 0\tag{17.17}$$

The solution to this matrix equation provides βˆOLS:

$$\hat{\beta}_{\text{OLS}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \tag{17.18}$$

## 17.4 Simulated Data Example with Scikit-Learn

Having outlined the theoretical OLS procedure for MLE the focus will now turn to implementation of linear regression as a machine learning technique within Python. The regression problem will make use of Scikit-Learn, which is a mature machine learning library for Python.

The goal of this simple example is primarily to introduce the API used by Scikit-Learn in a simpler setting since it will be utilised heavily in the remaining chapters.

In this example a set of "feature" values x<sup>i</sup> will be randomly generated from a normal distribution with mean µ<sup>x</sup> = 0 and variance σ<sup>x</sup> = 10. These values will be used to create responses y<sup>i</sup> of the form:

$$y_i = \alpha + \beta x_i + \epsilon \tag{17.19}$$

Where α = 2 is the intercept, β = 3 is the slope and is a normally-distributed error with mean µ = 0 and variance σ = 30.

500 such (X<sup>i</sup> , yi) pairs will be generated. 400 of these will be used to form a "training" set, while the remaining 100 will be held out to form a "testing" or evaluation set.

The goal of the exercise will be to estimate the slope and intercept values on the test set solely using a trained linear regression model based on the training data. Scikit-Learn possesses a clean API to carry this out, which will be demonstrated below.

The first task is to import the necessary libraries. Matplotlib and Seaborn are imported for plotting. Importing Seaborn is not strictly necessary, but it does provide more aestheticallypleasing plots. NumPy is imported to provide random number generation, while the linear\_model object is imported from Scikit-Learn:

```
# lin_reg_sklearn.py
```

```
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import linear_model
```

In the \_\_main\_\_ function all of the parameters are set. The code is commented liberally, so it should be straightforward to ascertain the parameters from the code:

```
# Create N values, with 80% used for training
# and 20% used for testing/evaluation
N = 500
split = int(0.8*N)
# Set the intercept and slope of the univariate
# linear regression simulated data
alpha = 2.0
beta = 3.0
# Set the mean and variance of the randomly
# distributed noise in the simulated dataset
eps_mu = 0.0
eps_sigma = 30.0
# Set the mean and variance of the X data
X_mu = 0.0
X_sigma = 10.0
```

The next step is to randomly simulate some data. Firstly an array of errors is created, which is stored in the eps variable. Then normally-distributed feature values, x<sup>i</sup> , are created and used to create linear responses y<sup>i</sup> with error. The final line X = X.reshape(-1, 1) is needed to avoid a deprecation warning in earlier versions of Scikit-Learn. Leaving it out will actually cause a ValueError in version 0.19. Be warned!

```
# Create the error/noise, X and y data
eps = np.random.normal(loc=eps_mu, scale=eps_sigma, size=N)
X = np.random.normal(loc=X_mu, scale=X_sigma, size=N)
y = alpha + beta*X + eps
X = X.reshape(-1, 1) # Needed to avoid deprecation warning
```

Once the full dataset is created it is necessary to partition it into a training and test set, using Python array-slicing syntax:

```
# Split up the features, X, and responses, y, into
# training and test arrays
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]
```

The next step is to create and fit a linear regression model to the training data. The following code demonstrates the simplicity of the Scikit-Learn API for carrying this out. All of the above mentioned details regarding OLS and MLE are abstracted away by the fit(...) method:

```
# Open a scikit-learn linear regression model
# and fit it to the training data
lr_model = linear_model.LinearRegression()
lr_model.fit(X_train, y_train)
```

The lr\_model linear regression model instance can be queried for the intercept and slope parameters. The coef\_ member is actually an array of slope parameters, since it generalises to the multivariate case where there are multiple slopes, one for each feature dimension. Hence the first element is selected for this univariate case. The intercept can be obtained from the intercept\_ member:

```
# Output the estimated parameters for the linear model
print(
    "Estimated intercept, slope: %0.6f, %0.6f" % (
        lr_model.intercept_,
        lr_model.coef_[0]
    )
```

)

Sample output from executing this code is given by the following. Note that the values will lilkely be different on other machines due to the stochastic nature of the number generation and fitting procedure:

#### Estimated intercept, slope: 2.006315, 2.908600

Now that the model has been fitted to the training data it can be utilised to predict the intercept and slope on the testing data. A scatterplot of the testing data is visualised and overlaid with the (point) estimated line of best fit, given in Figure 17.2. Compare this to the Bayesian linear regression example given in the previous chapter that provides a posterior distribution of such best fit lines:

```
# Create a scatterplot of the test data for features
# against responses, plotting the estimated line
# of best fit from the ordinary least squares procedure
plt.scatter(X_test, y_test)
plt.plot(
    X_test,
```

```
lr_model.predict(X_test),
    color='black',
    linewidth=1.0
)
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```

![](_page_9_Figure_1.jpeg)

![](_page_9_Figure_2.jpeg)

In subsequent chapters similar examples will be utilised for various machine learning techniques such as Random Forests, Support Vector Machines and Boosted Trees. It will be shown that the API for fitting such models is very similar to the above, making it extremely straightforward to test new ML models in a rapid research-oriented manner.

## 17.5 Full Code

#### # lin\_reg\_distribution\_plot.py

```
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import norm
```

```
if __name__ == "__main__":
    # Set up the X and Y dimensions
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(0, 20, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    # Create the univarate normal coefficients
    # of intercept and slope, as well as the
    # conditional probability density
    beta0 = -5.0
    beta1 = 0.5
    Z = norm.pdf(Y, beta0 + beta1*X, 1.0)
    # Plot the surface with the "coolwarm" colormap
    surf = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False
    )
    # Set the limits of the z axis and major line locators
    ax.set_zlim(0, 0.4)
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Label all of the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('P(Y|X)')
    # Adjust the viewing angle and axes direction
    ax.view_init(elev=30., azim=50.0)
    ax.invert_xaxis()
    ax.invert_yaxis()
    # Plot the probability density
    plt.show()
# lin_reg_sklearn.py
import matplotlib.pyplot as plt
```

**import** numpy as np **import** seaborn as sns

```
if __name__ == "__main__":
    # Create N values, with 80% used for training
    # and 20% used for testing/evaluation
    N = 500
    split = int(0.8*N)
    # Set the intercept and slope of the univariate
    # linear regression simulated data
    alpha = 2.0
    beta = 3.0
    # Set the mean and variance of the randomly
    # distributed noise in the simulated dataset
    eps_mu = 0.0
    eps_sigma = 30.0
    # Set the mean and variance of the X data
    X_mu = 0.0
    X_sigma = 10.0
    # Create the error/noise, X and y data
    eps = np.random.normal(loc=eps_mu, scale=eps_sigma, size=N)
    X = np.random.normal(loc=X_mu, scale=X_sigma, size=N)
    y = alpha + beta*X + eps
    X = X.reshape(-1, 1) # Needed to avoid deprecation warning
    # Split up the features, X, and responses, y, into
    # training and test arrays
    X_train = X[:split]
    X_test = X[split:]
    y_train = y[:split]
    y_test = y[split:]
    # Open a scikit-learn linear regression model
    # and fit it to the training data
    lr_model = linear_model.LinearRegression()
    lr_model.fit(X_train, y_train)
    # Output the estimated parameters for the linear model
    print(
        "Estimated intercept, slope: %0.6f, %0.6f" % (
            lr_model.intercept_,
```

```
lr_model.coef_[0]
    )
)
# Create a scatterplot of the test data for features
# against responses, plotting the estimated line
# of best fit from the ordinary least squares procedure
plt.scatter(X_test, y_test)
plt.plot(
    X_test,
    lr_model.predict(X_test),
    color='black',
    linewidth=1.0
)
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```

## 17.6 Bibliographic Note

An elementary introduction to linear regression as well as shrinkage, regularisation and dimensionality reduction in the framework of supervised learning can be found James et al (2013)[59].

A more rigourous explanation of the techniques including recent developments can be found in Hastie et al (2009)[51].

A probabilistic (mainly Bayesian) approach to linear regression, along with a comprehensive derivation of the maximum likelihood estimate via ordinary least squares, and extensive discussion of shrinkage and regularisation, can be found in Murphy (2012)[71].

A "real world" example-based overview of linear regression in a high-collinearity regime, with extensive discussion on dimensionality reduction and partial least squares can be found in Kuhn et al (2013)[67].
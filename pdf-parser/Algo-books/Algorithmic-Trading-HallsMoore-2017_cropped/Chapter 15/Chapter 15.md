## Chapter 15

# Introduction to Machine Learning

Machine learning is a relatively new area of research that couples statistical analysis with computer science. It encompasses extremely effective techniques for forecasting and prediction that in many cases currently exceed human ability.

In quantitative finance machine learning is used in various ways, which include prediction of future asset prices, optimising trading strategy parameters, managing risk and detection of signals among noisy datasets.

## 15.1 What is Machine Learning?

Machine learning employs algorithms that learn how to perform tasks such as prediction or classification without explicitly being programmed to do so. In essence, the algorithms learn from data rather than prespecification.

Such algorithms are incredibly diverse. They range from more traditional statistical models that emphasise inference through to highly complex "deep" neural network architectures that excel at prediction and classification tasks.

Over the last ten years or so machine learning has been making steady gains in the quantitative finance sector. It has attracted the attention of large quant funds including Man AHL, DE Shaw, Winton, Citadel and Two Sigma.

Machine learning algorithms can be applied in many ways to quantitative finance problems. Particular examples include:

- Prediction of future asset price movements
- Prediction of liquidity movements due to redemption of capital in large funds
- Determination of mis-priced assets in niche markets
- Natural language processing of equity analyst sentiment and forecasts
- Image classification/recognition for use in commodity supply/demand signals

Unfortunately much of the work on applying machine learning algorithms to trading strategies in quantitative finance is proprietary. Hence it is difficult to gain insight into the latest techniques. With practice, however, it can be seen how to take certain datasets and find consistent ways to generate alpha.

## 15.2 Machine Learning Domains

Machine learning tasks are generally categorised into three main areas: Supervised Learning, Unsupervised Learning and Reinforcement Learning.

The methods all differ in how the machine learning algorithm is "rewarded" for being correct in its predictions or classifications.

#### 15.2.1 Supervised Learning

Supervised learning algorithms involve labelled data. That is, data annotated with values such as categories (as in supervised classification) or numerical responses (as in supervised regression). Such algorithms are "trained" on the data and learn which predictive factors influence the responses.

When applied to unseen data supervised learning algorithms attempt to make predictions based on their prior training experience. An example from the quantitative finance would be using supervised regression to predict tomorrow's stock price from the previous month's worth of price data.

#### 15.2.2 Unsupervised Learning

Unsupervised learning algorithms do not make use of labelled data. Instead they utilise the underlying structure of the data to identify patterns. The canonical method is unsupervised clustering, which attempts to partition datasets into sub-clusters that are associated in some manner. An example from quantitative finance would be the clustering of certain assets into groups that behave similarly in order to optimise portfolio allocations.

#### 15.2.3 Reinforcement Learning

Reinforcement learning algorithms attempt to perform a task within a certain dynamic environment, by taking actions inside the environment that seek to maximise a reward mechanism.

These algorithms differ from supervised learning in that there is no direct set of input/output pairs utilised within the data. Such algorithms have recently gained significant notoriety due to their use by Google DeepMind[3]. DeepMind have utilised "deep reinforcement learning" to exceed human performance in Atari video games[70] and the ancient game of Go[4]. Such algorithms have been applied in quant finance to optimise investment portfolios.

Unfortunately it won't be possible to consider Reinforcement Learning in this book as the topic is extremely broad and constantly evolving, filling many books and research papers in its own right.

## 15.3 Machine Learning Techniques

Due to its interdisciplinary nature there are a large number of differing machine learning algorithms. Most have arisen from the computer science, engineering and statistics communities.

The list of machine learning algorithms is almost endless, as they include crossover techniques and ensembles of many other algorithms. However, the algorithms frequently used within quantitative finance are considered below.

#### 15.3.1 Linear Regression

An elementary supervised technique from classical statistics that finds an optimal linear response surface from a set of labelled predictor-response pairs.

#### 15.3.2 Linear Classification

These supervised techniques classify data into groups, rather than predict numerical responses. Common techniques include Logistic Regression, Linear Discriminant Analysis and Naive Bayes Classification.

#### 15.3.3 Tree-Based Methods

Decision trees are a supervised technique that partition the predictor/feature space into hypercubic subsets. Ensembles of decision trees include Random Forests and Gradient Boosted Regression Trees.

#### 15.3.4 Support Vector Machines

SVMs are a supervised technique that attempts to create a linear separation boundary in a higher-dimensional space than the original problem in order to deal with non-linear separation of features.

#### 15.3.5 Artificial Neural Networks and Deep Learning

Neural networks are a supervised technique that create hierarchies of activation "neurons" that can approximate high-dimensional non-linear functions. "Deep" networks make use of many hidden layers of neurons to form hierarchical representations for state-of-the-art classification performance.

#### 15.3.6 Bayesian Networks

Bayesian Networks or "Bayes Nets" are a type of probabilistic graphical model that represent probabilistic relationships between variables. They are utilised both for inference and learning applications.

#### 15.3.7 Clustering

Clustering is an unsupervised technique that attempts to partition data into subsets according to some similarity criteria. A common technique is K-Means Clustering.

#### 15.3.8 Dimensionality Reduction

Dimensionality reduction algorithms are unsupervised techniques that attempt to transform the space of predictors/factors into another set that explain the "variation" in the responses with fewer dimensions. Principal Component Analysis is the canonical technique here.

## 15.4 Machine Learning Applications

Machine learning is used heavily in quantitative finance, particularly in quantitative strategy development.

#### 15.4.1 Forecasting and Prediction

Machine learning techniques naturally lend themselves to asset price prediction based on historical pricing data. The accuracy of such techniques depends greatly on the quality and availability of historical data, the particular market or asset under consideration, the time frame of the prediction and the machine learning algorithm chosen for forecasting.

Predictions can be made for a single time point ahead or for a set of future time points. Examples of such predictions include prediction of daily S&P500 returns, prediction of spreads in intraday forex prices and predictions of liquidity based on order-book dynamics.

#### 15.4.2 Natural Language Processing

Natural language processing (NLP) involves quantifying structured language data in order to derive inferential or predictive insight. One of the most widely utilised NLP domains is Sentiment Analysis, which attempts to apply a "sentiment" to a set of text, such as "bullish" or "bearish". Such analysis can be used to produce trading signals.

Another area of NLP is known as Entity Extraction. This involves identifying "entities" or "topics" being discussed in a particular set of text. When Sentiment Analysis is combined with Entity Extraction it is possible to produce strong trading signals. Such approaches are often applied in equities markets, using social media data.

#### 15.4.3 Factor Models

Factor modelling is a statistical technique that attempts to describe the variation among a set of correlated observed variables via a reduced set of unobserved variables known as factors. This is achieved by modelling the observed variables as a linear combination of the reduced factors along with error terms.

There are three types of factor models in use for studying asset returns[96]. The first makes use of macroeconomic data such as GDP and interest rates in an attempt to model asset returns. The second makes use of fundamental data for a particular firm or asset, such as book value or market capitalisation to produce factors. The third type uses statistical methods to treat these factors as "latent" or unobservable, which need to be estimated from the asset returns.

Factor analysis is strongly related to the unsupervised dimensionality reduction technique Principal Component Analysis.

#### 15.4.4 Image Classification

Image classification is an application that spans the fields of machine learning and computer vision. It has recently become more popular due to the explosion of deep learning algorithms– particularly Convolution Neural Networks–that have significantly reduced the classification error rate in many of the leading image classification benchmark datasets.

While seemingly not a traditional area that might be applied to quantitative finance, it can be used indirectly on alternative data sources such as satellite imagery, to produce information on supply and demand. For instance, analysing oil storage tank height and maritime oil freight traffic can lead to a better understanding of current supply and demand for crude oil.

#### 15.4.5 Model Accuracy

One of the trickiest aspects of machine learning is determining which model is "best" for any particular problem or dataset at hand. This is known as model selection.

For supervised learning models a major issue arises when the model flexibility is adjusted. While this helps the model adapt to more complex datasets it is also increasing the likelihood of overfitting.

This situation occurs when the model is more closely aligned to "noise" in the training data than the underlying "signal". It has the effect of reduced generalisation performance of the model on unseen data. This particular issue leads to a balancing act between flexibility and performance known as the bias-variance tradeoff.

A technique to mitigate the effects of the bias-variance tradeoff is known as cross-validation. It involves partitioning the data into random subsets and fitting the model on each. Each model fit is then assessed and averaged over the entire set, with the goal of producing a more robust model that is less prone to overfitting on unseen data.

The bias-variance tradeoff and cross-validation techniques will be discussed at length in subsequent chapters.

#### 15.4.6 Parametric and Non-Parametric Models

Statistical machine learning models can be categorised into parametric and non-parametric methods. They each have their advantages and disadvantages when applied to quantitative finance data.

#### Parametric Models

A parametric statistical learning model is one that involves a specified model form for f along with a set of parameters that define its behaviour. The canonical example of a parametric model is linear regression. It involves estimating a set of p + 1 coefficients, given by the vector β = (β0, β1, ..., βp) whereby the response Y is linearly proportional, via each proportionality constant β<sup>j</sup> , to each feature x<sup>j</sup> , plus an "intercept" term β0. The parameters of the model are the β<sup>j</sup> coefficients.

Most of the models considered in this book will be parametric. While linear parametric models may not seemingly be flexible enough to handle the non-linearities of asset price data, they can often form effective trading algorithms. As always, by increasing the number of parameters in order to increase flexibility there is always the danger of overfitting as the model is following the "noise" too closely and not the "signal".

#### Non-Parametric Models

The alternative is to consider a form for f that does not involve any parameters - it is nonparametric. The benefit of using a non-parametric model is greater flexibility. Their main disadvantages are the need to have a large quantity of observational training data, often far greater than that necessary for parametric models, as well as their proneness to overfitting.

Given the fact that there is seemingly an abundance of historical financial data it would seem that non-parametric models are an obvious choice for quantitative finance applications. However, such models are not always optimal. While the increased flexibility is attractive for modelling the non-linearities in stock market data it is very easy to overfit the model due to the poor signal to noise ratio found in financial time series.

A key example of a non-parametric machine learning model is k-nearest neighbours, which seeks to classify or predict values via the mode or mean, respectively, of a group of k nearest neighbour points in feature space.

It is non-parametric in the sense that there are no β values as in linear regression to "fit" the model to. However it does contain what is known as a hyperparameter, which in this case is the number of points in feature space, k, to take the mean or mode over.

This hyperparameter is optimised similarly to fitting parameters via methods such as k-fold cross validation, which will be discussed later in the book.

#### 15.4.7 Statistical Framework for Machine Learning Domains

In the above section on Machine Learning Domains supervised learning and unsupervised learning were both outlined.

A supervised learning model requires the predictor-response pair (x<sup>i</sup> , yi). The "supervision" or "training" of the model occurs when f is trained or fit to a particular set of data. In a statistical setting the common approach to estimating the parameters–fitting the model–is carried out using a technique known as Maximum Likelihood Estimation (MLE). For each model, the algorithm for carrying out MLE can be very different. For instance in the linear regression setting the MLE to find the coefficient estimates, βˆ, is carried out using a procedure known as Ordinary Least Squares.

An unsupervised learning model still utilises the feature vectors x<sup>i</sup> but does not have the associated response value y<sup>i</sup> . This is a much more challenging environment for an algorithm to produce effective relationship estimates as there nothing to "supervise" or "train" the model with. Moreover, it is harder to assess model accuracy as there is no easily available "fitness function" on which to compare. This does not detract from the efficiency of unsupervised techniques, however. They are widely utilised in quantitative finance, particularly for factor models.
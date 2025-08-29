# Chapter 21

# Unsupervised Learning

The previous chapters have all discussed supervised learning techniques. This chapter introduces unsupervised learning, which will allow analysis of unlabelled datasets.

Supervised learning involves working with feature/response pairs. Its goal is to try and predict the response from the associated features. It is "supervised" because in the training phase of the learning process the algorithm has access to the ground truth via known responses to certain input features. It uses these to adjust its model parameters such that when exposed to new features it can make an estimate of the response.

In unsupervised learning the features are still present but there is no associated response. Instead interest lies solely in attributes of the features themselves. This might include whether the features form specific clusters or sub-groups in feature space. It might also include whether very high-dimensional data can be described in a much lower-dimensional setting.

Unsupervised learning techniques are often motivated by the fact that it can be prohibitive in terms of time and/or money to "label" feature data, which would permit analysis using supervised techniques. An additional motivation is due to the fact that images, video, natural language documents and scientific research data (such as gene expressions), once quantified, possess very high dimensionality. Such high dimensionality requires supervised learning techniques with many degrees of freedom, potentially leading to overfitting and thus poor test performance. Unsupervised learning techniques are a partial solution to these problems.

Unfortunately the lack of ground truth or supervision for unsupervised techniques often leads to subjective assessment of their performance. There are no widely agreed approaches for quantifying how effective unsupervised algorithms are. Performance is largely determined on a case-bycase basis using heuristic approaches. Such judgement-based assessments might seem unscientific to quantitatively trained individuals, but unsupervised techniques have proven to be extremely useful in many research areas.

Unsupervised learning techniques are often deployed in the realms of anomaly detection, purchasing habit analysis, recommendation systems and natural language processing. In quantitative finance they find usage in de-noising datasets, portfolio/asset clustering, market regime detection and trading signal generation with natural language processing.

## 21.1 High Dimensional Data

Quantitative finance and algorithmic trading extend well beyond analysis of asset price time series. The increased competition from the proliferation of quantitative funds has forced new and old firms alike to consider alternative data sources. Many of these sources are inhomogeneous, non-numeric and form extremely large databases. When suitably quantified much of this data is extremely high-dimensional. Examples include satellite imagery, high-resolution video, corpora of text documents and sensor data.

To provide some scope as the extreme dimensionality of these datasets, consider a standard 1080p monitor, which has a resolution of 1920 × 1080 = 2073600 pixels. If we restrict each of these pixels to displaying either black or white then there are 2 <sup>2073600</sup> potential images that can be displayed. This is a vast number. It becomes significantly worse when considering the fact that each pixel often has 2 <sup>24</sup> potential colours - three separate 8-bit channels for red, green and blue respectively.

Hence there is significant motivation when searching through such datasets to reduce dimensionality to a manageable level. This is achieved by trying to find lower dimensional subspaces that still capture the essence of the data signal. A key problem is that even with a huge number of samples the "training data cannot be expected to populate the space"[20]. If N is the number of samples available and p is the dimensionality of the space then we are in a situation where p N. In essence, there are large subsets of the feature space where very little is known. This problem is often referred to as the Curse of Dimensionality.

Much of unsupervised learning is thus concerned with means of reducing this dimensionality to a reasonable level but still retaining the "signal" within the data. Mathematically, we are attempting to describe the key variations in the data using a lower dimensional manifold of dimension q < p, which is embedded within the larger p-dimensional space. Dimensionality reduction algorithms such as linear Principal Components Analysis (PCA) and non-linear kernel PCA have been developed for this task.

## 21.2 Mathematical Overview of Unsupervised Learning

In a supervised learning task a training set exists consisting of N pairs of feature vectors, or predictors, x<sup>i</sup> ∈ R <sup>p</sup> as well as associated outputs or responses, y<sup>i</sup> ∈ R. Thus the dataset consists of N tuples (x1, y1), . . . ,(xn, yn). The responses y<sup>i</sup> can be considered as "labels" for the set of features. They are used to guide the supervised learning algorithm in its training phase. In order to train the model we need to define a loss function between the true value of the response y and its estimate from the model yˆ, given by L(y, yˆ).

The unsupervised learning setting differs in that the only available data is a set of unlabelled predictors x<sup>i</sup> . That is, there are no associated labelled responses y<sup>i</sup> for each data point. Thus there is no concept of training or supervision for such techniques since there is nothing for the algorithm to use for ground truth. Instead interest lies solely in the structure of the xis themselves.

As with supervised learning one approach involves formulating the task probabilistically via a concept known as conditional density estimation[51, 71].

In the supervised learning case models are built of the form p(y<sup>i</sup> | x<sup>i</sup> , θ). Specific interest lies in the distribution of the responses y<sup>i</sup> , conditional on both the feature vectors x<sup>i</sup> and the parameters of the model, θ.

Conversely, in the unsupervised case there is no access to the responses y<sup>i</sup> . Hence interest lies in probabilistic models of the form p(x<sup>i</sup> | θ). That is, the distribution of the feature vectors x<sup>i</sup> conditional on the parameters of the model, θ. This is known as unconditional density estimation.

## 21.3 Unsupervised Learning Algorithms

There are two main areas of unsupervised learning that are of interest to us in quantitative finance: Dimensionality Reduction and Clustering.

#### 21.3.1 Dimensionality Reduction

We have motivated the need for dimensionality reduction above. The most common mechanism in unsupervised learning for achieving this is (linear) Principal Components Analysis (PCA).

In machine learning and quantitative finance problems we often have a large set of correlated variables in a high dimensional space. PCA allows us to summarise these datasets using a reduced number of dimensions. It achieves this by carrying out an orthogonal coordinate transformation of the original space, forming a new set of linearly uncorrelated variables called principal components.

The principal components are found as the eigenvectors of the covariance matrix of the data. Each principal component is orthogonal to each other (by construction) and explains successively less of the variability of the dataset. Usually the first few principal components are able to account for a large fraction of the variability of the original set, leading to a much lower dimensional representation in this new space.

Another way to think of PCA is that it is a change of basis. The transformation produces a set of basis vectors, a subset of which are capable of spanning a linear subspace within the original space that closely follows the data grouping.

However, not all data is easily summarised by a linear subspace. In classification problems, for instance, there are many data sources which are not linearly separable. In this case it is possible to invoke the "kernel trick", as was discussed in the previous chapter on Support Vector Machines, to linearly separate a space in a much higher dimensional space and thus carry out PCA in the transformed space. This allows PCA to be applied to non-linear datasets.

In quantitative finance PCA is often used for factor analysis. An example would be looking at a large number of correlated stocks and attempting to reduce their dimensionality by looking at a smaller set of unobserved and uncorrelated latent factors.

#### 21.3.2 Clustering

Another important unsupervised learning technique is known as cluster analysis. Its goal is to assign a cluster label to elements of a feature space in order to partition them into groupings or clusters. In certain cases this can be accomplished unambiguously if subgroupings within the feature space are clearly distinct and easily separable. In other cases clusters may "overlap", making it challenging to form a distinction boundary.

The canonical algorithm for cluster analysis is K-Means Clustering. The basic idea with the procedure is to assign all N elements of a feature space into K separate and non-overlapping clusters.

To achieve this a simple iterative algorithm is used. All elements of the feature space are initially randomly assigned a cluster k ∈ {1, . . . , K}. At this point the algorithm iterates and for each step of the iteration calculates the mean vector–the centroid–for each cluster k. It then assigns each element to the cluster possessing the nearest centroid using a Euclidean distance metric. The algorithm is iterated until the centroid locations remain fixed to within a certain pre-specified tolerance distance.

In quantitative finance clustering is commonly used to identify assets that have similar characteristics, which is useful in constructing diversified portfolios. It can also be utilised for detecting market regimes and thus potentially acting as a risk management tool. We will be studying clustering techniques for assets in the following chapter.

## 21.4 Bibliographic Note

An introduction to unsupervised learning, and its difficulties, can be found in James et al (2013)[59]. It is accessible to those without a strong mathematical background or those coming from other areas of science.

A significantly more advanced mathematical discussion, at the graduate level, can be found in Hastie et al (2009)[51]. The book discusses many unsupervised techniques, although it is primarily about supervised methods.

Barber (2012)[20] discusses high-dimensionality and the problems it causes at a reasonable mathematical level, concentrating primarily on PCA and clustering, while Murphy (2012)[71] considers unsupervised learning through the probabilistic density estimation approach at a gentler mathematical level of rigour.
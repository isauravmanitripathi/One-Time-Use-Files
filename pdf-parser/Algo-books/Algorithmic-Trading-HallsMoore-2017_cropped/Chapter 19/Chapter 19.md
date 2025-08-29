# Chapter 19

# Support Vector Machines

In this section we are going to discuss an extremely powerful machine learning technique known as the support vector machine (SVM). It is one of the best "out of the box" supervised classification techniques. It is an important tool for both the quantitative trading researcher and data scientist.

This section will cover the theory of maximal margin classifiers, support vector classifiers and support vector machines. We will be making use of Scikit-Learn to demonstrate some examples of the aforementioned theoretical techniques on actual data.

# 19.1 Motivation for Support Vector Machines

The problem to be solved in this section is one of supervised binary classification. That is, we wish to categorise new unseen objects into two separate groups based on their properties and a set of known examples that are already categorised. A good example of such a system is classifying a set of new documents into positive or negative sentiment groups, based on other documents which have already been classified as positive or negative. Similarly, we could classify new emails into spam or non-spam, based on a large set of emails that have already been marked as spam or non-spam by humans. SVMs are highly applicable to such situations.

As with other supervised machine learning techniques a support vector machine is applied to a labelled set of feature data, which resides in feature space. In the context of spam or document classification, each "feature" dimension is the prevalence or importance of a particular word appropriately quantified.

The goal of the SVM is to train a model that assigns new unseen objects into a particular category. It achieves this by creating a partition of the feature space into two subspaces. Based on the features in the new unseen objects (e.g. documents/emails), it places an object onto a specific side of the separation plane, leading to a categorisation such as spam or non-spam. This makes it an example of a non-probabilistic classifier. It is non-probabilistic because the feature values in new unseen test observations explicitly determine their location in feature space without any stochastic component.

Much of the benefit of SVMs is due to the fact that this separation plane need not actually be a linear hyperplane. Utilising a technique known as the kernel trick they can become much more flexible by introducing various types of non-linear decision boundaries. This is necessary for "real world" datasets that do not often possess straightforward linear separating boundaries

between categories.

Formally, in mathematical language, SVMs construct linear separating hyperplanes in large finite-dimensional vector spaces. Data points are viewed as (x, y) tuples, x = (x1, . . . , xp) where the x<sup>j</sup> are the feature values and y is the classification (usually given as +1 or −1). Optimal classification occurs when such hyperplanes provide maximal distance to the nearest training data points. Intuitively, this makes sense, as if the points are well separated, the classification between two groups is much clearer.

However, if in a feature space some of the sets are not linearly separable and overlap, then it is necessary to perform a transformation of the original feature space to a higher-dimensional space, in which the separation between the groups becomes more clear. However this has the consequence of making the separation boundary in the original space potentially non-linear.

In this section we will proceed by considering the advantages and disadvantages of SVMs as a classification technique. We will then define the concept of an optimal linear separating hyperplane, which motivates a simple type of linear classifier known as a maximal margin classifier (MMC). Subsequently we will show that maximal margin classifiers are not often applicable to many "real world" situations and need modification in the form of a support vector classifier (SVC). We will then relax the restriction of linearity and consider non-linear classifiers, namely support vector machines, which use kernel functions to improve computational efficiency.

# 19.2 Advantages and Disadvantages of SVMs

As a classification technique the SVM has many advantages, some of which are due to its computational efficiency on large datasets. The Scikit-Learn team have summarised the main advantages and disadvantages[12] but I have repeated and elaborated on them for completeness:

#### 19.2.1 Advantages

- High-Dimensionality The SVM is an effective tool in high-dimensional spaces, which is particularly applicable to document classification and sentiment analysis where the dimensionality can be extremely large (≥ 10<sup>6</sup> ).
- Memory Efficiency Since only a subset of the training points are used in the actual decision process of assigning new members, only these points need to be stored in memory (and calculated upon) when making decisions.
- Versatility Class separation is often highly non-linear. The ability to apply new kernels allows substantial flexibility for the decision boundaries, leading to greater classification performance.

#### 19.2.2 Disadvantages

• p n - In situations where the number of features for each object p exceeds the number of training data samples n SVMs can perform poorly. This can be seen intuitively as if the high-dimensional feature space is much larger than the number of samples then there are less effective support vectors on which to support the optimal linear hyperplanes. This leads to poorer classification performance as new unseen samples are added.

• Non-Probabilistic - Since the classifier works by placing objects above and below a classifying hyperplane, there is no direct probabilistic interpretation for group membership. However, one potential metric to determine "effectiveness" of the classification is how far from the decision boundary the new point is.

Now that we have outlined the advantages and disadvantages we are going to discuss the geometric objects and mathematical entities that will ultimately allow us to define the SVMs and how they work.

There are some fantastic references (both links and textbooks) that derive much of the mathematical detail of how SVMs function. In the following derivation I didn't want to "reinvent the wheel" too much, especially with regards notation and pedagogy, so I have formulated the following treatment based on the references provided, making strong use of James et al[59], Hastie et al[51] and the Wikibooks article on SVMs[13]. As this is ultimately a practitioner textbook on quantitative trading strategies, I have made changes to the notation where appropriate and have adjusted the narrative to suit individuals interested in quantitative trading.

# 19.3 Linear Separating Hyperplanes

The linear separating hyperplane is the key geometric entity that lies at the heart of the SVM. Informally, if we have a high-dimensional feature space, then the linear hyperplane is an object one dimension lower than this space that divides the feature space into two regions.

This linear separating plane need not pass through the origin of our feature space, i.e. it does not need to include the zero vector as an entity within the plane. Such hyperplanes are known as affine.

If we consider a real-valued p-dimensional feature space, known mathematically as R p , then our linear separating hyperplane is an affine p − 1 dimensional space embedded within it.

For the case of p = 2 this hyperplane is simply a one-dimensional straight line, which lives in the larger two-dimensional plane, whereas for p = 3 the hyerplane is a two-dimensional plane that lives in the larger three-dimensional feature space (see Figure [19.1\)](#page-2-0):

![](_page_2_Figure_8.jpeg)

<span id="page-2-0"></span>Figure 19.1: One- and two-dimensional hyperplanes

If we consider an element of our p-dimensional feature space, i.e. x = (x1, ..., xp) ∈ R p , then we can mathematically define an affine hyperplane by the following equation:

$$b_0 + b_1 x_1 + \dots + b_p x_p = 0 \tag{19.1}$$

b<sup>0</sup> 6= 0 gives us an affine plane, which does not pass through the origin. We can use a more succinct notation for this equation by introducing the summation sign:

$$b_0 + \sum_{j=1}^p b_j x_j = 0 \tag{19.2}$$

Notice however that this is nothing more than a multi-dimensional dot product (or, more generally, an inner product) and as such can be written even more succinctly as:

$$\mathbf{b} \cdot \mathbf{x} + b_0 = 0 \tag{19.3}$$

If an element x ∈ R p satisfies this relation then it lives on the p − 1-dimensional hyperplane. This hyperplane splits the p-dimensional feature space into two classification regions. This can be seen in Figure [19.2.](#page-3-0) Compare this to the hyperblock partitioning of the Decision Tree displayed in the previous chapter:

![](_page_3_Figure_6.jpeg)

<span id="page-3-0"></span>Figure 19.2: Separation of p-dimensional space by a hyperplane

Elements x above the plane satisfy:

$$\mathbf{b} \cdot \mathbf{x} + b_0 > 0 \tag{19.4}$$

While those below it satisfy:

$$\mathbf{b} \cdot \mathbf{x} + b_0 < 0 \tag{19.5}$$

The key point here is that it is possible for us to determine which side of the plane any element x will fall on by calculating the sign of the expression b · x + b0. This concept will form the basis of a supervised classification technique.

# 19.4 Classification

Continuing with our example of email spam filtering, we can think of our classification problem (say) as being provided with a thousand emails (n = 1000), each of which is marked spam (+1) or non-spam (−1). In addition each email has an associated set of keywords, which are obtained by taking each word in the email that is separated by a space. These keywords provide the features. Hence if we take the set of all possible keywords from all of the emails, eliminating duplicates, we will be left with p keywords in total. Note that p can be very large (≥ 10<sup>6</sup> ).

If we translate this into a mathematical problem, the standard setup for a supervised classification procedure is to consider a set of n training observations, x<sup>i</sup> , each of which is a p-dimensional vector of features. Each training observation has an associated class label, y<sup>i</sup> ∈ {−1, 1}. Hence we can think of n pairs of training observations (x<sup>i</sup> , yi) representing the features and class labels (keyword lists and spam/non-spam). In addition to the training observations we can provide test observations, x <sup>∗</sup> = (x ∗ 1 , ..., x<sup>∗</sup> p ) that are later used to test the performance of the classifiers. In our spam example, these test observations would be new emails that have not yet been seen.

Our goal is to develop a classifier based on provided training observations that will correctly classify subsequent test observations using only their feature values. This translates into being able to classify an email as spam or non-spam based solely on the keywords contained within it.

We will initially suppose that it is possible, via a means yet to be determined, to construct a hyperplane that separates training data perfectly according to their class labels (see Figure [19.3\)](#page-4-0). This would mean cleanly separating spam emails from non-spam emails using only specific keywords. The following diagram is only showing p = 2, while for keyword lists we may have p > 10<sup>6</sup> . Hence Figures [19.3](#page-4-0) are only representative of the problem.

![](_page_4_Figure_6.jpeg)

<span id="page-4-0"></span>Figure 19.3: Multiple separating hyperplanes; Perfect separation of class data

This translates into a mathematical separating property of:

$$\mathbf{b} \cdot \mathbf{x}_i + b_0 > 0, \text{ if } y_i = 1 \tag{19.6}$$

and

$$\mathbf{b} \cdot \mathbf{x}_i + b_0 < 0, \text{ if } y_i = -1 \tag{19.7}$$

This states that if each training observation is above or below the separating hyperplane, according to the geometric equation which defines the plane, then its associated class label will be +1 or −1. Thus we have developed a simple classification process. We assign a test observation to a class depending upon which side of the hyperplane it is located on.

This can be formalised by considering the following function f(x), with a test observation x <sup>∗</sup> = (x ∗ 1 , ..., x<sup>∗</sup> p ):

$$f(\mathbf{x}^*) = \mathbf{b} \cdot \mathbf{x}^* + b_0 \tag{19.8}$$

If f(x ∗ ) > 0 then y <sup>∗</sup> = +1, whereas if f(x ∗ ) < 0 then y <sup>∗</sup> = −1.

However this tells us nothing about how we go about finding the b<sup>j</sup> components of b, as well as b0, which are crucial in helping us determine the equation of the hyperplane separating the two regions. The next section discusses an approach for carrying this out. It also introduces the concept of the maximal margin hyperplane and a classifier built upon it known as the maximal margin classifier.

# 19.5 Deriving the Classifier

At this stage it is worth pointing out that separating hyperplanes are not unique since it is possible to slightly translate or rotate such a plane without touching any training observations (see Figures 19.3).

Not only do we need to know how to construct such a plane but we also need to determine the most optimal plane. This motivates the concept of the maximal margin hyperplane (MMH), which is the separating hyperplane furthest from any training observations and is thus "optimal".

How do we find the maximal margin hyperplane? Firstly, we compute the perpendicular distance from each training observation x<sup>i</sup> for a given separating hyperplane. The smallest perpendicular distance to a training observation from the hyperplane is known as the margin. The MMH is the separating hyperplane where the margin is the largest. This guarantees that it is the furthest minimum distance to a training observation.

The classification procedure is then just simply a case of determining which side a test observation falls on. This can be carried out using the above formula for f(x ∗ ). Such a classifier is known as a maximimal margin classifier (MMC). Note however that finding the particular values that lead to the MMH is purely based on the training observations. We still need to be aware of how the MMC performs on the test observations. We are implicitly making the assumption that a large margin in the training observations will provide a large margin on the test observations, but this may not be the case.

As always we must be careful to avoid overfitting when the number of feature dimensions is large. This often occurs in Natural Language Processing applications such as email spam classification. Overfitting means that the MMH is a very good fit for the training data but can perform quite poorly when exposed to testing data. I discuss this issue at length in the chapter on Model Selection and Cross Validation, under the Bias-Variance Tradeoff section.

To reiterate, our goal now becomes finding an algorithm that can produce the b<sup>j</sup> values, which will fix the geometry of the hyperplane and hence allow determination of f(x ∗ ) for any test observation.

If we consider Figure [19.4,](#page-6-0) we can see that the MMH is the mid-line of the widest "block" that we can insert between the two classes such that they are perfectly separated.

![](_page_6_Figure_3.jpeg)

<span id="page-6-0"></span>Figure 19.4: Maximal margin hyperplane with support vectors (A, B and C)

One of the key features of the MMC (and subsequently SVC and SVM) is that the location of the MMH only depends on the support vectors, which are the training observations lying directly on the margin, but not hyperplane, boundary. See points A, B and C in Figure [19.4.](#page-6-0) This means that the location of the MMH is not dependent upon any other training observations.

Thus it can be immediately seen that a potential drawback of the MMC is that its MMH, and thus its classification performance, can be extremely sensitive to the support vector locations. However it is also partially this feature that makes the SVM an attractive computational tool, as we only need to store the support vectors in memory once it has been "trained" (when the b<sup>j</sup> values have been fixed).

# 19.6 Constructing the Maximal Margin Classifier

I feel it is instructive to fully outline the optimisation problem that needs to be solved in order to create the MMH and thus the MMC itself. While I will outline the constraints of the optimisation problem its algorithmic solution is beyond the scope of the book. Thankfully these optimisation routines are implemented in Scikit-Learn via the LIBSVM library[33]. If you wish to read more about the solution to these algorithmic problems take a look at Hastie et al (2009)[51] and the Scikit-Learn page on Support Vector Machines[12].

The procedure for determining a maximal margin hyperplane for a maximal margin classifier is as follows. Given n training observations x1, ..., x<sup>n</sup> ∈ R <sup>p</sup> and n class labels y1, ..., y<sup>n</sup> ∈ {−1, 1}, the MMH is the solution to the following optimisation procedure:

Maximise M ∈ R, by varying b1, ..., b<sup>p</sup> ∈ R such that:

$$\sum_{j=1}^{p} b_j^2 = \mathbf{b} \cdot \mathbf{b} = 1 \tag{19.9}$$

and

$$y_i \left( \mathbf{b} \cdot \mathbf{x} + b_0 \right) \ge M, \quad \forall i = 1, ..., n \tag{19.10}$$

Despite the complex looking constraints, they actually state that each observation must be on the correct side of the hyperplane and at least a distance M from it. Since the goal of the procedure is to maximise M, this is precisely the condition we need to create the MMC.

Clearly the case of perfect separability is an ideal one. Most "real world" datasets will not have such perfect separability via a linear hyperplane (see Figure [19.5\)](#page-7-0). However, if there is no separability then we are unable to construct a MMC by the optimisation procedure above. So, how do we create a form of separating hyperplane?

![](_page_7_Figure_6.jpeg)

<span id="page-7-0"></span>Figure 19.5: No possibility of a true separating hyperplane

Essentially we have to relax the requirement that a separating hyperplane will perfectly separate every training observation on the correct side of the plane. To achieve this we use what is called a soft margin. This motivates the concept of a support vector classifier (SVC).

# 19.7 Support Vector Classifiers

As we alluded to above, one of the problems with MMC is that they can be extremely sensitive to the addition of new training observations. Consider Figure 19.6. In the left panel it can be seen that there exists a MMH perfectly separating the two classes. However, in the right panel if we add one point to the +1 class we see that the location of the MMH changes substantially. Hence in this situation the MMH has clearly been overfit:

![](_page_8_Figure_0.jpeg)

Figure 19.6: Addition of a single point dramatically changes the MMH line

Consider a classifier based on a separating hyperplane that does not perfectly separate the two classes. This would have a greater robustness to the addition of new invididual observations and a better classification on most of the training observations. This comes at the expense of some misclassification of a few training observations.

This is how a support vector classifier or soft margin classifier works. A SVC allows some observations to be on the incorrect side of the margin (or hyperplane), providing a "soft" separation. Figure [19.7](#page-8-0) demonstrates observations being on the wrong side of the margin and the wrong side of the hyperplane respectively.

![](_page_8_Figure_4.jpeg)

<span id="page-8-0"></span>Figure 19.7: Observations on the wrong side of the margin and hyperplane, respectively

An observation is still classified depending upon which side of the separating hyperplane it lies on but some points may be misclassified.

It is instructive to see how the optimisation procedure differs from that described above for the MMC. We need to introduce new parameters, namely n <sup>i</sup> values (known as the slack values) and a non-negative parameter C ∈ R <sup>+</sup> ∪ 0, known as the budget. We wish to maximise M ∈ R, across b1, ..., bp, 1, .., <sup>n</sup> ∈ R such that:

$$\sum_{j=1}^{p} b_j^2 = \mathbf{b} \cdot \mathbf{b} = 1 \tag{19.11}$$

and

$$y_i \left( \mathbf{b} \cdot \mathbf{x} + b_0 \right) \ge M(1 - \epsilon_i), \quad \forall i = 1, ..., n \tag{19.12}$$

and

$$\epsilon_i \ge 0, \quad \sum_{i=1}^n \epsilon_i \le C \tag{19.13}$$

Where C, the budget, is a non-negative "tuning" parameter. M still represents the margin and the slack variables <sup>i</sup> allow the individual observations to be on the wrong side of the margin or hyperplane.

In essence the <sup>i</sup> tell us where the ith observation is located relative to the margin and hyperplane. For <sup>i</sup> = 0 it states that the x<sup>i</sup> training observation is on the correct side of the margin. For <sup>i</sup> > 0 we have that x<sup>i</sup> is on the wrong side of the margin, while for <sup>i</sup> > 1 we have that x<sup>i</sup> is on the wrong side of the hyperplane.

C collectively controls how much the individual <sup>i</sup> can be modified to violate the margin. C = 0 implies that <sup>i</sup> = 0, ∀i and thus no violation of the margin is possible, in which case (for separable classes) we have the MMC situation.

For C > 0 it means that no more than C observations can violate the hyperplane. As C increases the margin will widen. See Figure [19.8](#page-9-0) for two differing values of C:

![](_page_9_Figure_8.jpeg)

<span id="page-9-0"></span>Figure 19.8: Different values of the tuning parameter C

How do we choose C in practice? Generally this is done via cross-validation. In essence C is the parameter that governs the bias-variance trade-off for the SVC. A small value of C means a low bias, high variance situation. A large value of C means a high bias, low variance situation.

As before, to classify a new test observation x <sup>∗</sup> we simply calculate the sign of f(x ∗ ) = b · x <sup>∗</sup> + b0.

This works well for classes that are linearly, or nearly linearly, separated. What about nonlinear separation boundaries? How do we deal with those situations? This is where we can extend the concept of support vector classifiers to support vector machines.

# 19.8 Support Vector Machines

The motivation behind the extension of a SVC is to allow non-linear decision boundaries. This is the domain of the support vector machine (SVM). Consider the following Figure [19.9.](#page-10-0) In such a situation a purely linear SVC will have extremely poor performance, simply because the data has no clear linear separation:

![](_page_10_Figure_2.jpeg)

<span id="page-10-0"></span>Figure 19.9: No clear linear separation between classes and thus poor SVC performance

Hence SVCs can be useless in highly non-linear class boundary problems.

In order to motivate how an SVM works we can use a standard "trick" that was mentioned in the chapter on linear regression when considering non-linear situations. In particular a set of p features x1, ..., x<sup>p</sup> can be transformed, say, into a set of 2p features x1, x<sup>2</sup> 1 , ..., xp, x<sup>2</sup> p . This allows us to apply a linear technique to a set of non-linear features.

While the decision boundary is linear in the new 2p-dimensional feature space it is non-linear in the original p-dimensional space. We end up with a decision boundary given by q(x) = 0 where q is a quadratic polynomial function of the original features and hence is a non-linear solution.

Clearly this is not restricted to quadratic polynomial transformations. Higher-dimensional polynomials, interaction terms and other functional forms can all be considered. The drawback with this approach is that it dramatically increases the dimension of the feature space making some algorithms computationally intractable.

The major advantage of SVMs is that they allow a non-linear enlargening of the feature space, while still retaining a significant computational efficiency, using a process known as the "kernel trick", which will be outlined below shortly.

So what are SVMs? In essence they are an extension of SVCs that results from enlargening the feature space through the use of functions known as kernels. In order to understand kernels, we need to briefly discuss some aspects of the solution to the SVC optimisation problem outlined above.

While calculating the solution to the SVC optimisation problem the algorithm only needs to make use of inner products between the observations and not the observations themselves. Recall that an inner product is defined for two p-dimensional vectors u, v as:

$$\langle \mathbf{u}, \mathbf{v} \rangle = \sum_{j=1}^{p} u_j v_j \tag{19.14}$$

Hence for two observations an inner product is defined as:

$$\langle \mathbf{x}_i, \mathbf{x}_k \rangle = \sum_{j=1}^p x_{ij} x_{kj} \tag{19.15}$$

We will not dwell on the details since they are beyond the scope of this book, however it is possible to show that a linear support vector classifier for a particular observation x can be represented as a linear combination of inner products:

$$f(\mathbf{x}) = b_0 + \sum_{i=1}^n a_i \langle \mathbf{x}, \mathbf{x}_i \rangle \tag{19.16}$$

With n a<sup>i</sup> coefficients, one for each of the training observations.

To estimate the b<sup>0</sup> and a<sup>i</sup> coefficients we only need to calculate <sup>n</sup> 2 = n(n − 1)/2 inner products between all pairs of training observations. In fact, we really only need to calculate the inner products for the subset of training observations that represent the support vectors. I will call this subset S . This means that:

$$a_i = 0 \text{ if } \mathbf{x}_i \notin \mathscr{S} \tag{19.17}$$

Hence we can rewrite the representation formula as:

$$f(\mathbf{x}) = b_0 + \sum_{i \in \mathscr{S}} a_i \langle \mathbf{x}, \mathbf{x}_i \rangle \tag{19.18}$$

It turns out that this is a major advantage for computational efficiency.

This now motivates the extension to SVMs. If we consider the inner product hx<sup>i</sup> , xki and replace it with a more general inner product "kernel" function K = K(x<sup>i</sup> , xk), we can modify the SVC representation to use non-linear kernel functions. Hence we can adjust how we calculate "similarity" between two observations. For instance, to recover the SVC we just take K to be as follows:

$$K(\mathbf{x}_i, \mathbf{x}_k) = \sum_{j=1}^p x_{ij} x_{kj}$$
(19.19)

Since this kernel is linear in its features the SVC is known as the linear SVC. We can also consider polynomial kernels, of degree d:

$$K(\mathbf{x}_i, \mathbf{x}_k) = (1 + \sum_{j=1}^p x_{ij} x_{kj})^d$$
(19.20)

This provides a significantly more flexible decision boundary and essentially amounts to fitting a SVC in a higher-dimensional feature space involving d-degree polynomials of the features (see Figure [19.10\)](#page-12-0).

![](_page_12_Figure_2.jpeg)

<span id="page-12-0"></span>Figure 19.10: A d-degree polynomial kernel; A radial kernel

Hence, the definition of a support vector machine is a support vector classifier with a nonlinear kernel function.

We can also consider the popular radial kernel (see Figure [19.10\)](#page-12-0):

$$K(\mathbf{x}_i, \mathbf{x}_k) = \exp\left(-\gamma \sum_{j=1}^p (x_{ij} - x_{kj})^2\right), \quad \gamma > 0 \tag{19.21}$$

So how do radial kernels work? They clearly differ from polynomial kernels. Essentially if our test observation x ∗ is far from a training observation x<sup>i</sup> in standard Euclidean distance then the sum P<sup>p</sup> <sup>j</sup>=1(x ∗ <sup>j</sup> − xij ) <sup>2</sup> will be large and thus K(x ∗ , xi) will be very small. Hence this particular training observation x<sup>i</sup> will have almost no effect on where the test observation x ∗ is placed, via f(x ∗ ).

Thus the radial kernel has extremely localised behaviour and only nearby training observations to x <sup>∗</sup> will have an impact on its class label.

#### 19.8.1 Biblographic Notes

Originally, SVMs were invented by Vapnik[98], while the current standard "soft margin" approach is due to Cortes[34]. My treatment of the material follows, and is strongly influenced by, the excellent statistical machine learning texts of James et al[59] and Hastie et al[51].
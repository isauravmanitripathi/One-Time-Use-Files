and the testing is run only on the one configuration chosen in the validation phase. In what case does this procedure still fail?

3. What is the key to avoiding selection bias?

# **Bibliography**

1. Bharat Rao, R., G. Fung, and R. Rosales (2008): "On the dangers of crossvalidation: An experimental evaluation." White paper, IKM CKS Siemens Medical Solutions USA. Available at [http://people.csail.mit.edu/romer/papers/CrossVal\\_SDM08.pdf](http://people.csail.mit.edu/romer/papers/CrossVal_SDM08.pdf) .

2. Bishop, C. (1995): *Neural Networks for Pattern Recognition* , 1st ed. Oxford University Press.

- 3. Breiman, L. and P. Spector (1992): "Submodel selection and evaluation in regression: The X-random case." White paper, Department of Statistics, University of California, Berkeley. Available at <http://digitalassets.lib.berkeley.edu/sdtr/ucb/text/197.pdf> .
- 4. Hastie, T., R. Tibshirani, and J. Friedman (2009): *The Elements of Statistical Learning* , 1st ed. Springer.
- 5. James, G., D. Witten, T. Hastie and R. Tibshirani (2013): *An Introduction to Statistical Learning* , 1st ed. Springer.
- 6. Kohavi, R. (1995): "A study of cross-validation and bootstrap for accuracy estimation and model selection." International Joint Conference [on Artificial Intelligence. Available at http://web.cs.iastate.edu/](http://web.cs.iastate.edu/~jtian/cs573/Papers/Kohavi-IJCAI-95.pdf) ∼jtian/cs573/Papers/Kohavi-IJCAI-95.pdf .
- 7. Ripley, B. (1996): *Pattern Recognition and Neural Networks* , 1st ed. Cambridge University Press.

# **CHAPTER 8**

# **Feature Importance**

# **8.1 Motivation**

One of the most pervasive mistakes in financial research is to take some data, run it through an ML algorithm, backtest the predictions, and repeat the sequence until a nice-looking backtest shows up. Academic journals are filled with such pseudo-discoveries, and even large hedge funds constantly fall into this trap. It does not matter if the backtest is a walk-forward out-of-sample. The fact that we are repeating a test over and over on the same data will likely lead to a false discovery. This methodological error is so notorious among statisticians that they consider it scientific fraud, and the American Statistical Association warns against it in its ethical guidelines (American Statistical Association [2016], Discussion #4). It typically takes about 20 such iterations to discover a (false) investment strategy subject to the standard significance level (false positive rate) of 5%. In this chapter we will explore why such an approach is a waste of time and money, and how feature importance offers an alternative.

## **8.2 The Importance of Feature Importance**

A striking facet of the financial industry is that so many very seasoned portfolio managers (including many with a quantitative background) do not realize how easy it is to overfit a backtest. How to backtest properly is not the subject of this chapter; we will address that extremely important topic in Chapters 11–15. The goal of this chapter is to explain one of the analyses that must be performed *before* any backtest is carried out.

Suppose that you are given a pair of matrices ( *X* , *y* ), that respectively contain features and labels for a particular financial instrument. We can fit a classifier on ( *X* , *y* ) and evaluate the generalization error through a purged k-fold crossvalidation (CV), as we saw in Chapter 7. Suppose that we achieve good performance. The next natural question is to try to understand what features contributed to that performance. Maybe we could add some features that strengthen the signal responsible for the classifier's predictive power. Maybe we could eliminate some of the features that are only adding noise to the system. Notably, understanding feature importance opens up the proverbial black box. We can gain insight into the patterns identified by the classifier if we understand what source of information is indispensable to it. This is one of the reasons why the black box mantra is somewhat overplayed by the ML skeptics. Yes, the algorithm has learned without us directing the process (that is the whole point of ML!) in a black box, but that does not mean that we cannot (or should not) take a look at what the algorithm has found. Hunters do not blindly eat everything their smart dogs retrieve for them, do they?

Once we have found what features are important, we can learn more by conducting a number of experiments. Are these features important all the time, or only in some specific environments? What triggers a change in importance

over time? Can those regime switches be predicted? Are those important features also relevant to other related financial instruments? Are they relevant to other asset classes? What are the most relevant features across all financial instruments? What is the subset of features with the highest rank correlation across the entire investment universe? This is a much better way of researching strategies than the foolish backtest cycle. Let me state this maxim as one of the most critical lessons I hope you learn from this book:

## **Snippet 8.1 Marcos' First Law of Backtesting—Ignore at your own peril**

"Backtesting is not a research tool. Feature importance is."

Marcos López de Prado *Advances in Financial Machine Learning* (2018)

# **8.3 Feature Importance with Substitution Effects**

I find it useful to distinguish between feature importance methods based on whether they are impacted by substitution effects. In this context, a substitution effect takes place when the estimated importance of one feature is reduced by the presence of other related features. Substitution effects are the ML analogue of what the statistics and econometrics literature calls "multi-collinearity." One way to address linear substitution effects is to apply PCA on the raw features, and then perform the feature importance analysis on the orthogonal features. See Belsley et al. [1980], Goldberger [1991, pp. 245–253], and Hill et al. [2001] for further details.

# **8.3.1 Mean Decrease Impurity**

Mean decrease impurity (MDI) is a fast, explanatory-importance (in-sample, IS) method specific to tree-based classifiers, like RF. At each node of each decision tree, the selected feature splits the subset it received in such a way that impurity is decreased. Therefore, we can derive for each decision tree how much of the overall impurity decrease can be assigned to each feature. And given that we have a forest of trees, we can average those values across all estimators and rank the features accordingly. See Louppe et al. [2013] for a detailed description. There are some important considerations you must keep in mind when working with MDI:

- 1. Masking effects take place when some features are systematically ignored by tree-based classifiers in favor of others. In order to avoid them, set max\_features=int(1) when using sklearn's RF class. In this way, only one random feature is considered per level.
  - 1. Every feature is given a chance (at some random levels of some random trees) to reduce impurity.
  - 2. Make sure that features with zero importance are not averaged, since the only reason for a 0 is that the feature was not randomly chosen. Replace those values with np.nan .
- 2. The procedure is obviously IS. Every feature will have some importance, even if they have no predictive power whatsoever.
- 3. MDI cannot be generalized to other non-tree based classifiers.
- 4. By construction, MDI has the nice property that feature importances add up to 1, and every feature importance is bounded between 0 and 1.
- 5. The method does not address substitution effects in the presence of correlated features. MDI dilutes the importance of substitute features, because of their interchangeability: The importance of two identical features will be halved, as they are randomly chosen with equal probability.
- 6. Strobl et al. [2007] show experimentally that MDI is biased towards some predictor variables. White and Liu [1994] argue that, in case of single decision trees, this bias is due to an unfair advantage given by popular impurity functions toward predictors with a large number of categories.

Sklearn's RandomForest class implements MDI as the default feature importance score. This choice is likely motivated by the ability to compute MDI on the fly, with minimum computational cost. <sup>1</sup> Snippet 8.2 illustrates an implementation of MDI, incorporating the considerations listed earlier.

### **SNIPPET 8.2 MDI FEATURE IMPORTANCE**

# **8.3.2 Mean Decrease Accuracy**

Mean decrease accuracy (MDA) is a slow, predictive-importance (out-ofsample, OOS) method. First, it fits a classifier; second, it derives its performance OOS according to some performance score (accuracy, negative log-loss, etc.); third, it permutates each column of the features matrix ( *X* ), one column at a time, deriving the performance OOS after each column's permutation. The importance of a feature is a function of the loss in performance caused by its column's permutation. Some relevant considerations include:

- 1. This method can be applied to any classifier, not only tree-based classifiers.
- 2. MDA is not limited to accuracy as the sole performance score. For example, in the context of meta-labeling applications, we may prefer to score a classifier with F1 rather than accuracy (see Chapter 14, Section 14.8 for an explanation). That is one reason a better descriptive name would have been "permutation importance." When the scoring function does not correspond to a metric space, MDA results should be used as a ranking.
- 3. Like MDI, the procedure is also susceptible to substitution effects in the presence of correlated features. Given two identical features, MDA always considers one to be redundant to the other. Unfortunately, MDA will make both features appear to be outright irrelevant, even if they are critical.
- 4. Unlike MDI, it is possible that MDA concludes that all features are unimportant. That is because MDA is based on OOS performance.

5. The CV must be purged and embargoed, for the reasons explained in Chapter 7.

Snippet 8.3 implements MDA feature importance with sample weights, with purged k-fold CV, and with scoring by negative log-loss or accuracy. It measures MDA importance as a function of the improvement (from permutating to not permutating the feature), relative to the maximum possible score (negative log-loss of 0, or accuracy of 1). Note that, in some cases, the improvement may be negative, meaning that the feature is actually detrimental to the forecasting power of the ML algorithm.

#### **SNIPPET 8.3 MDA FEATURE IMPORTANCE**

```
<pre>def featImpMDA(clf,X,y,cv,sample weight,t1,pctEmbargo,scoring='neg log loss'):</pre>
# feat importance based on OOS score reduction
if scoring not in ['neg log loss', 'accuracy']:
    raise Exception('wrong scoring method.')
from sklearn.metrics import log loss, accuracy score
cvGen=PurgedKFold(n splits=cv,t1=t1,pctEmbargo=pctEmbargo) # purged cv
scr0, scr1=pd.Series(), pd.DataFrame(columns=X.columns)
for i, (train, test) in enumerate(cvGen.split(X=X)):
    <pre>X0, y0, w0=X.iloc[train, :], y.iloc[train], sample weight.iloc[train]</pre>
    <pre>X1,y1,w1=X.iloc[test,:],y.iloc[test],sample weight.iloc[test]</pre>
    fit=clf.fit(X=X0, y=y0, sample weight=w0.values)if scoring=='neg log loss':
        prob=fit.predict proba(X1)
         scr0.loc[i] = -log loss(y1,prob,sample weight=w1.values,
                                labels=clf.classes )
    else:
        pred=fit.predict(X1)
         scr0.loc[i]=accuracy score(y1,pred,sample weight=w1.values)
    for j in X.columns:
        X1 = X1.\text{copy (deep=True)}np.random.shuffle(X1 [j].values) # permutation of a single column
        if scoring=='neg log loss':
             prob=fit.predict proba(X1 )
             scr1.loc[i,j]=-log_loss(y1,prob,sample_weight=w1.values,
                                       labels=clf.classes )
        else:
             pred=fit.predict(X1)
             scr1.loc[i,j]=accuracy score(y1,pred,sample weight=w1.values)
\text{imp} = (-\text{scr1}) \cdot \text{add}(\text{scr0}, \text{axis} = 0)if scoring=='neg log loss':imp=imp/-scr1
else:imp=imp/(1.-scr1)imp=pd.concat({'mean':imp.mean(),'std':imp.std()*imp.shape[0]**-.5},axis=1)
return imp, scr0.mean()
```

## **8.4 Feature Importance without Substitution Effects**

Substitution effects can lead us to discard important features that happen to be redundant. This is not generally a problem in the context of prediction, but it could lead us to wrong conclusions when we are trying to understand, improve, or simplify a model. For this reason, the following single feature importance method can be a good complement to MDI and MDA.

## **8.4.1 Single Feature Importance**

Single feature importance (SFI) is a cross-section predictive-importance (outof-sample) method. It computes the OOS performance score of each feature in isolation. A few considerations:

- 1. This method can be applied to any classifier, not only tree-based classifiers.
- 2. SFI is not limited to accuracy as the sole performance score.
- 3. Unlike MDI and MDA, no substitution effects take place, since only one feature is taken into consideration at a time.
- 4. Like MDA, it can conclude that all features are unimportant, because performance is evaluated via OOS CV.

The main limitation of SFI is that a classifier with two features can perform better than the bagging of two single-feature classifiers. For example, (1) feature B may be useful only in combination with feature A; or (2) feature B may be useful in explaining the splits from feature A, even if feature B alone is inaccurate. In other words, joint effects and hierarchical importance are lost in SFI. One alternative would be to compute the OOS performance score from subsets of features, but that calculation will become intractable as more features are considered. Snippet 8.4 demonstrates one possible implementation of the SFI method. A discussion of the function cvScore can be found in Chapter 7.

#### **SNIPPET 8.4 IMPLEMENTATION OF SFI**

## **8.4.2 Orthogonal Features**

As argued in Section 8.3, substitution effects dilute the importance of features measured by MDI, and significantly underestimate the importance of features measured by MDA. A partial solution is to orthogonalize the features before applying MDI and MDA. An orthogonalization procedure such as principal components analysis (PCA) does not prevent all substitution effects, but at least it should alleviate the impact of linear substitution effects.

Consider a matrix { *X <sup>t</sup> , <sup>n</sup>* } of stationary features, with observations *t* = 1, …, *T* and variables *n* = 1, …, *N* . First, we compute the standardized features matrix *Z* , such that *Z <sup>t</sup> , <sup>n</sup>* = σ <sup>−</sup> <sup>1</sup> *n* ( *X <sup>t</sup> , <sup>n</sup>* − μ *<sup>n</sup>* ), where μ *<sup>n</sup>* is the mean of { *X <sup>t</sup> , <sup>n</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* and σ *<sup>n</sup>* is the standard deviation of { *X <sup>t</sup> , <sup>n</sup>* } *<sup>t</sup>* <sup>=</sup> 1, …, *<sup>T</sup>* . Second, we compute the eigenvalues Λ and eigenvectors *W* such that *Z* ' *ZW* = *W* Λ, where Λ is an *NxN* diagonal matrix with main entries sorted in descending order, and *W* is an *NxN* orthonormal matrix. Third, we derive the orthogonal features as *P* = *ZW* . We can verify the orthogonality of the features by noting that *P* ' *P* = *W* ' *Z* ' *ZW* = *W* ' *W* Λ *W* ' *W* = Λ.

The diagonalization is done on *Z* rather than *X* , for two reasons: (1) centering the data ensures that the first principal component is correctly oriented in the main direction of the observations. It is equivalent to adding an intercept in a linear regression; (2) re-scaling the data makes PCA focus on explaining correlations rather than variances. Without re-scaling, the first principal components would be dominated by the columns of *X* with highest variance, and we would not learn much about the structure or relationship between the variables.

Snippet 8.5 computes the smallest number of orthogonal features that explain at least 95% of the variance of *Z* .

#### **SNIPPET 8.5 COMPUTATION OF ORTHOGONAL FEATURES**

Besides addressing substitution effects, working with orthogonal features provides two additional benefits: (1) orthogonalization can also be used to reduce the dimensionality of the features matrix *X* , by dropping features associated with small eigenvalues. This usually speeds up the convergence of ML algorithms; (2) the analysis is conducted on features designed to explain the structure of the data.

Let me stress this latter point. An ubiquitous concern throughout the book is the risk of overfitting. ML algorithms will always find a pattern, even if that pattern is a statistical fluke. You should always be skeptical about the purportedly important features identified by any method, including MDI, MDA, and SFI. Now, suppose that you derive orthogonal features using PCA. Your PCA analysis has determined that some features are more "principal" than others, without any knowledge of the labels (unsupervised learning). That is, PCA has ranked features without any possible overfitting in a classification sense. When your MDI, MDA, or SFI analysis selects as most important (using label information) the same features that PCA chose as principal (ignoring label information), this constitutes confirmatory evidence that the pattern identified by the ML algorithm is not entirely overfit. If the features were entirely random, the PCA ranking would have no correspondance with the feature importance ranking. Figure 8.1 displays the scatter plot of eigenvalues associated with an eigenvector (x-axis) paired with MDI of the feature associated with an engenvector (y-axis). The Pearson correlation is 0.8491 (pvalue below 1E-150), evidencing that PCA identified informative features and ranked them correctly without overfitting.

![](_page_11_Figure_0.jpeg)

<span id="page-11-0"></span>**Figure 8.1** Scatter plot of eigenvalues (x-axis) and MDI levels (y-axis) in loglog scale

I find it useful to compute the weighted Kendall's tau between the feature importances and their associated eigenvalues (or equivalently, their inverse PCA rank). The closer this value is to 1, the stronger is the consistency between PCA ranking and feature importance ranking. One argument for preferring a weighted Kendall's tau over the standard Kendall is that we want to prioritize rank concordance among the most importance features. We do not care so much about rank concordance among irrelevant (likely noisy) features. The hyperbolic-weighted Kendall's tau for the sample in [Figure 8.1](#page-11-0) is 0.8206.

Snippet 8.6 shows how to compute this correlation using Scipy. In this example, sorting the features in descending importance gives us a PCA rank sequence very close to an ascending list. Because the weightedtau function gives higher weight to higher values, we compute the correlation on the inverse PCA ranking, pcRank\*\*-1 . The resulting weighted Kendall's tau is relatively high, at 0.8133.

#### **SNIPPET 8.6 COMPUTATION OF WEIGHTED KENDALL'S TAU BETWEEN FEATURE IMPORTANCE AND INVERSE PCA RANKING**

## **8.5 Parallelized vs. Stacked Feature Importance**

There are at least two research approaches to feature importance. First, for each security *i* in an investment universe *i* = 1, …, *I* , we form a dataset ( *X <sup>i</sup>* , *y <sup>i</sup>* ), and derive the feature importance in parallel. For example, let us denote λ *<sup>i</sup>* , *<sup>j</sup>* , *<sup>k</sup>* the importance of feature *j* on instrument *i* according to criterion *k.* Then we can aggregate all results across the entire universe to derive a combined Λ *<sup>j</sup>* , *<sup>k</sup>* importance of feature *j* according to criterion *k.* Features that are important across a wide variety of instruments are more likely to be associated with an underlying phenomenon, particularly when these feature importances exhibit high rank correlation across the criteria. It may be worth studying in-depth the theoretical mechanism that makes these features predictive. The main advantage of this approach is that it is computationally fast, as it can be parallelized. A disadvantage is that, due to substitution effects, important features may swap their ranks across instruments, increasing the variance of the estimated λ *<sup>i</sup>* , *<sup>j</sup>* , *<sup>k</sup>* . This disadvantage becomes relatively minor if we average λ *<sup>i</sup>* , *<sup>j</sup>* , *<sup>k</sup>* across instruments for a sufficiently large investment universe.

A second alternative is what I call "features stacking." It consists in stacking all datasets into a single combined dataset ( *X* , *y* ), where is a transformed instance of *X <sup>i</sup>* (e.g., standardized on a rolling trailing window). The purpose of this transformation is to ensure some distributional homogeneity, . Under this approach, the classifier must learn what features are more important across all instruments simultaneously, as if the

entire investment universe were in fact a single instrument. Features stacking presents some advantages: (1) The classifier will be fit on a much larger dataset than the one used with the parallelized (first) approach; (2) the importance is derived directly, and no weighting scheme is required for combining the results; (3) conclusions are more general and less biased by outliers or overfitting; and (4) because importance scores are not averaged across instruments, substitution effects do not cause the dampening of those scores.

I usually prefer features stacking, not only for features importance but whenever a classifier can be fit on a set of instruments, including for the purpose of model prediction. That reduces the likelihood of overfitting an estimator to a particular instrument or small dataset. The main disadvantage of stacking is that it may consume a lot of memory and resources, however that is where a sound knowledge of HPC techniques will come in handy (Chapters 20–22).

# **8.6 Experiments with Synthetic Data**

In this section, we are going to test how these feature importance methods respond to synthetic data. We are going to generate a dataset ( *X* , *y* ) composed on three kinds of features:

- 1. Informative: These are features that are used to determine the label.
- 2. Redundant: These are random linear combinations of the informative features. They will cause substitution effects.
- 3. Noise: These are features that have no bearing on determining the observation's label.

Snippet 8.7 shows how we can generate a synthetic dataset of 40 features where 10 are informative, 10 are redundant, and 20 are noise, on 10,000 observations. For details on how sklearn generates synthetic datasets, visit: http://scikit-

[learn.org/stable/modules/generated/sklearn.datasets.make\\_classification.html](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html) .

## **SNIPPET 8.7 CREATING A SYNTHETIC DATASET**

Given that we know for certain what feature belongs to each class, we can evaluate whether these three feature importance methods perform as designed. Now we need a function that can carry out each analysis on the same dataset. Snippet 8.8 accomplishes that, using bagged decision trees as default classifier (Chapter 6).

#### **SNIPPET 8.8 CALLING FEATURE IMPORTANCE FOR ANY METHOD**

Finally, we need a main function to call all components, from data generation to feature importance analysis to collection and processing of output. These tasks are performed by Snippet 8.9.

#### **SNIPPET 8.9 CALLING ALL COMPONENTS**

For the aesthetically inclined, Snippet 8.10 provides a nice layout for plotting feature importances.

#### **SNIPPET 8.10 FEATURE IMPORTANCE PLOTTING FUNCTION**

Figure 8.2 shows results for MDI. For each feature, the horizontal bar indicates the mean MDI value across all the decision trees, and the horizontal line is the standard deviation of that mean. Since MDI importances add up to 1, if all features were equally important, each importance would have a value of 1/40. The vertical dotted line marks that 1/40 threshold, separating features whose importance exceeds what would be expected from undistinguishable features. As you can see, MDI does a very good job in terms of placing all informative and redundant features above the red dotted line, with the exception of R\_5, which did not make the cut by a small margin. Substitution effects cause some informative or redundant features to rank better than others, which was expected.

![](_page_18_Figure_0.jpeg)

**Figure 8.2** MDI feature importance computed on a synthetic dataset

Figure 8.3 shows that MDA also did a good job. Results are consistent with those from MDI's in the sense that all the informed and redundant features rank better than the noise feature, with the exception of R\_6, likely due to a substitution effect. One not so positive aspect of MDA is that the standard deviation of the means are somewhat higher, although that could be addressed by increasing the number of partitions in the purged k-fold CV, from, say, 10 to 100 (at the cost of 10 × the computation time without parallelization).

![](_page_19_Figure_0.jpeg)

**Figure 8.3** MDA feature importance computed on a synthetic dataset

Figure 8.4 shows that SFI also does a decent job; however, a few important features rank worse than noise (I\_6, I\_2, I\_9, I\_1, I\_3, R\_5), likely due to joint effects.

The labels are a function of a combination of features, and trying to forecast them independently misses the joint effects. Still, SFI is useful as a complement to MDI and MDA, precisely because both types of analyses are affected by different kinds of problems.

|               | $\begin{array}{c} \text{R} \text{1} \\ \text{R} \text{3} \\ \text{14} \\ \text{R} \text{7} \\ \text{R} \end{array}$<br>15<br>R 6<br>R 4<br>I 8<br>I 7 |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|---------------|--|--|--|------------------|--|--|--|--|--|--|
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     | -             |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       | -                                                                                   |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       | $\sim$                                                                              |               |  |  |  |                  |  |  |  |  |  |  |
| R 8 9 2 0 3 8 |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       | $\hat{=}$<br>$\sim$<br>-<br>$\overline{a}$<br>-<br>$\overline{m}$<br>$\overline{ }$ |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  | -                |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  | -                |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  | -<br>-           |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  | -<br>-<br>-<br>- |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     |               |  |  |  |                  |  |  |  |  |  |  |
|               |                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                       |                                                                                     | 0.5           |  |  |  |                  |  |  |  |  |  |  |
|               | 0.1                                                                                                                                                   | N 8 5<br>N 8 13<br>N 19<br>N 19<br>$\begin{array}{c} \begin{array}{c} \text{N} \ 14 \\ \text{N} \ 6 \\ \text{N} \ 15 \\ \text{N} \ 10 \\ \text{N} \ 12 \\ \text{N} \ 9 \\ \text{N} \ 18 \\ \text{N} \ 4 \\ \text{N} \ 17 \\ \text{N} \ 2 \\ \text{1} \ 9 \\ \text{N} \ 17 \\ \text{N} \ 2 \\ \text{1} \ 5 \\ \text{1} \ 5 \\ \end{array} \end{array}$ | 0.2<br>0.3                                                                          | 1<br>L<br>0.4 |  |  |  |                  |  |  |  |  |  |  |

**Figure 8.4** SFI feature importance computed on a synthetic dataset

#### **Exercises**

- 1. Using the code presented in Section 8.6:
  - 1. Generate a dataset (*X* , *y* ).
  - 2. Apply a PCA transformation on *X* , which we denote .
  - 3. Compute MDI, MDA, and SFI feature importance on , where the base estimator is RF.
  - 4. Do the three methods agree on what features are important? Why?
- 2. From exercise 1, generate a new dataset , where is a feature union of *X* and .
  - 1. Compute MDI, MDA, and SFI feature importance on , where the base estimator is RF.

- 2. Do the three methods agree on the important features? Why?
- 3. Take the results from exercise 2:
  - 1. Drop the most important features according to each method, resulting in a features matrix .
  - 2. Compute MDI, MDA, and SFI feature importance on , where the base estimator is RF.
  - 3. Do you appreciate significant changes in the rankings of important features, relative to the results from exercise 2?
- 4. Using the code presented in Section 8.6:
  - 1. Generate a dataset (*X* , *y* ) of 1E6 observations, where 5 features are informative, 5 are redundant and 10 are noise.
  - 2. Split (*X* , *y* ) into 10 datasets {(*X <sup>i</sup>* , *y <sup>i</sup>* )} *<sup>i</sup>* <sup>=</sup> 1, …, <sup>10</sup> , each of 1E5 observations.
  - 3. Compute the parallelized feature importance (Section 8.5), on each of the 10 datasets, {(*X <sup>i</sup>* , *y <sup>i</sup>* )} *<sup>i</sup>* <sup>=</sup> 1, …, <sup>10</sup> .
  - 4. Compute the stacked feature importance on the combined dataset (*X* , *y* ).
  - 5. What causes the discrepancy between the two? Which one is more reliable?
- 5. Repeat all MDI calculations from exercises 1–4, but this time allow for masking effects. That means, do not set max\_features=int(1) in Snippet 8.2. How do results differ as a consequence of this change? Why?

### **References**

- 1. American Statistical Association (2016): "Ethical guidelines for statistical practice." Committee on Professional Ethics of the American Statistical Association (April). Available at <http://www.amstat.org/asa/files/pdfs/EthicalGuidelines.pdf> .
- 2. Belsley, D., E. Kuh, and R. Welsch (1980): *Regression Diagnostics: Identifying Influential Data and Sources of Collinearity* , 1st ed. John Wiley & Sons.
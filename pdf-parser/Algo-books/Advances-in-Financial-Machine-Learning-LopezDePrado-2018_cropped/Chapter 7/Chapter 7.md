- 2. Kearns, M. and L. Valiant (1989): "Cryptographic limitations on learning Boolean formulae and finite automata." In Proceedings of the 21st Annual ACM Symposium on Theory of Computing, pp. 433–444, New York. Association for Computing Machinery.
- 3. Schapire, R. (1990): "The strength of weak learnability." *Machine Learning* . Kluwer Academic Publishers. Vol. 5 No. 2, pp. 197–227.

# **Bibliography**

- 1. Gareth, J., D. Witten, T. Hastie, and R. Tibshirani (2013): *An Introduction to Statistical Learning: With Applications in R* , 1st ed. Springer-Verlag.
- 2. Hackeling, G. (2014): *Mastering Machine Learning with Scikit-Learn* , 1st ed. Packt Publishing.
- 3. Hastie, T., R. Tibshirani and J. Friedman (2016): *The Elements of Statistical Learning* , 2nd ed. Springer-Verlag.
- 4. Hauck, T. (2014): *Scikit-Learn Cookbook* , 1st ed. Packt Publishing.
- 5. Raschka, S. (2015): *Python Machine Learning* , 1st ed. Packt Publishing.

### **Notes**

1  [For an introduction to ensemble methods, please visit: http://scikit](http://scikit-learn.org/stable/modules/ensemble.html.)learn.org/stable/modules/ ensemble.html.

2 I would not typically cite Wikipedia, however, on this subject the user may find some of the illustrations in this article useful: [https://en.wikipedia.org/wiki/Bias%E2%80%93variance\\_tradeoff.](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff.)

3 For an intuitive explanation of Random Forest, visit the following link: [https://quantdare.com/random -forest-many-is-better-than-one/.](https://quantdare.com/random-forest-many-is-better-than-one/)

4 For a visual explanation of the difference between bagging and boosting, [visit: https://quantdare.com/ what-is-the-difference-between-bagging-and](https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/)boosting/.

# **CHAPTER 7**

# **Cross-Validation in Finance**

## **7.1 Motivation**

The purpose of cross-validation (CV) is to determine the generalization error of an ML algorithm, so as to prevent overfitting. CV is yet another instance where standard ML techniques fail when applied to financial problems. Overfitting will take place, and CV will not be able to detect it. In fact, CV will contribute to overfitting through hyper-parameter tuning. In this chapter we will learn why standard CV fails in finance, and what can be done about it.

# **7.2 The Goal of Cross-Validation**

One of the purposes of ML is to learn the general structure of the data, so that we can produce predictions on future, unseen features. When we test an ML algorithm on the same dataset as was used for training, not surprisingly, we achieve spectacular results. When ML algorithms are misused that way, they are no different from file lossy-compression algorithms: They can summarize the data with extreme fidelity, yet with zero forecasting power.

CV splits observations drawn from an IID process into two sets: the *training* set and the *testing* set. Each observation in the complete dataset belongs to one, and only one, set. This is done as to prevent leakage from one set into the other, since that would defeat the purpose of testing on unseen data. Further details can be found in the books and articles listed in the references section.

There are many alternative CV schemes, of which one of the most popular is kfold CV. Figure 7.1 illustrates the *k* train/test splits carried out by a k-fold CV, where *k* = 5. In this scheme:

- 1. The dataset is partitioned into *k* subsets.
- 2. For *i = 1,…,k*
  - 1. The ML algorithm is trained on all subsets excluding *i.*
  - 2. The fitted ML algorithm is tested on *i.*

![](_page_2_Figure_0.jpeg)

#### **Figure 7.1** Train/test splits in a 5-fold CV scheme

The outcome from k-fold CV is a *kx1* array of cross-validated performance metrics. For example, in a binary classifier, the model is deemed to have learned something if the cross-validated accuracy is over 1/2, since that is the accuracy we would achieve by tossing a fair coin.

In finance, CV is typically used in two settings: model development (like hyper-parameter tuning) and backtesting. Backtesting is a complex subject that we will discuss thoroughly in Chapters 10–16. In this chapter, we will focus on CV for model development.

### **7.3 Why K-Fold CV Fails in Finance**

By now you may have read quite a few papers in finance that present k-fold CV evidence that an ML algorithm performs well. Unfortunately, it is almost certain that those results are wrong. One reason k-fold CV fails in finance is because observations cannot be assumed to be drawn from an IID process. A second reason for CV's failure is that the testing set is used multiple times in the process of developing a model, leading to multiple testing and selection bias. We will revisit this second cause of failure in Chapters 11–13. For the time being, let us concern ourselves exclusively with the first cause of failure. Leakage takes place when the training set contains information that also appears in the testing set. Consider a serially correlated feature  $X$  that is associated with labels  $Y$  that are formed on overlapping data:

- Because of the serial correlation,  $X_t \approx X_{t+1}$ .
- Because labels are derived from overlapping datapoints,  $Y_t \approx Y_{t+1}$ .

By placing  $t$  and  $t + 1$  in different sets, information is leaked. When a classifier is first trained on  $(X_t, Y_t)$ , and then it is asked to predict  $E[Y_{t+1} | X_{t+1}]$ based on an observed  $X_{t+1}$ , this classifier is more likely to achieve  $Y_{t+1} = E$ [  $Y_{t+1} | X_{t+1}$  even if *X* is an irrelevant feature.

If *X* is a predictive feature, leakage will enhance the performance of an already valuable strategy. The problem is leakage in the presence of irrelevant features, as this leads to false discoveries. There are at least two ways to reduce the likelihood of leakage:

- 1. Drop from the training set any observation  $i$  where  $Y_i$  is a function of information used to determine  $Y_j$ , and  $j$  belongs to the testing set.
  - 1. For example,  $Y_i$  and  $Y_i$  should not span overlapping periods (see Chapter 4 for a discussion of sample uniqueness).
- 2. Avoid overfitting the classifier. In this way, even if some leakage occurs, the classifier will not be able to profit from it. Use:
  - 1. Early stopping of the base estimators (see Chapter 6).
  - 2. Bagging of classifiers, while controlling for oversampling on redundant examples, so that the individual classifiers are as diverse as possible.
    - $1.$  Set max\_samples to the average uniqueness.
    - 2. Apply sequential bootstrap (Chapter 4).

Consider the case where  $X_i$  and  $X_j$  are formed on overlapping information, where  $i$  belongs to the training set and  $j$  belongs to the testing set. Is this a case of informational leakage? Not necessarily, as long as  $Y_i$  and  $Y_i$  are independent. For leakage to take place, it must occur that ( $X_i$ ,  $Y_i$ )  $\approx$  ( $X_j$ ,  $Y_j$ ), and it does not suffice that  $X_i \approx X_j$  or even  $Y_i \approx Y_j$ .

# 7.4 A Solution: Purged K-Fold CV

One way to reduce leakage is to purge from the training set all observations whose labels overlapped in time with those labels included in the testing set. I call this process "purging." In addition, since financial features often incorporate series that exhibit serial correlation (like ARMA processes), we should eliminate from the training set observations that immediately follow an observation in the testing set. I call this process "embargo."

# **7.4.1 Purging the Training Set**

Suppose a testing observation whose label *Y <sup>j</sup>* is decided based on the information set Φ *<sup>j</sup>* . In order to prevent the type of leakage described in the previous section, we would like to purge from the training set any observation whose label *Y <sup>i</sup>* is decided based on the information set Φ *<sup>i</sup>* , such that Φ *<sup>i</sup>* ∩Φ *<sup>j</sup>* = ∅ *.*

In particular, we will determine that there is informational overlap between two observations *i* and *j* whenever *Y <sup>i</sup>* and *Y <sup>j</sup>* are concurrent (see Chapter 4, Section 4.3), in the sense that both labels are contingent on at least one common random draw. For example, consider a label *Y <sup>j</sup>* that is a function of observations in the closed range *t* ∈ [ *t j , 0* , *t j , 1* ], *Y <sup>j</sup>* = *f* [[ *t j , 0* , *t j , 1* ]] (with some abuse of notation). For example, in the context of the triple-barrier labeling method (Chapter 3), it means that the label is the sign of the return spanning between price bars with indices *t <sup>j</sup> , <sup>0</sup>* and *t j , 1* , that is . A label *Y <sup>i</sup>* = *f* [[ *t i , 0* , *t i , 1* ]] overlaps with *Y <sup>j</sup>* if any of the three sufficient conditions is met:

1. *t <sup>j</sup> , <sup>0</sup>* ≤ *t <sup>i</sup> , <sup>0</sup>* ≤ *t j , 1* 2. *t <sup>j</sup> , <sup>0</sup>* ≤ *t <sup>i</sup> , <sup>1</sup>* ≤ *t j , 1* 3. *t <sup>i</sup> , <sup>0</sup>* ≤ *t <sup>j</sup> , <sup>0</sup>* ≤ *t <sup>j</sup> , <sup>1</sup>* ≤ *t i , 1*

Snippet 7.1 implements this purging of observations from the training set. If the testing set is contiguous, in the sense that no training observations occur between the first and last testing observation, then purging can be accelerated: The object testTimes can be a pandas series with a single item, spanning the entire testing set.

#### **SNIPPET 7.1 PURGING OBSERVATION IN THE TRAINING SET**

When leakage takes place, performance improves merely by increasing *k* → *T* , where *T* is the number of bars. The reason is that the larger the number of testing splits, the greater the number of overlapping observations in the training set. In many cases, purging suffices to prevent leakage: Performance will improve as we increase *k* , because we allow the model to recalibrate more often. But beyond a certain value *k* \*, performance will not improve, indicating that the backtest is not profiting from leaks. Figure 7.2 plots one partition of the k-fold CV. The test set is surrounded by two train sets, generating two overlaps that must be purged to prevent leakage.

![](_page_6_Figure_0.jpeg)

**Figure 7.2** Purging overlap in the training set

#### **7.4.2 Embargo**

For those cases where purging is not able to prevent all leakage, we can impose an embargo on training observations *after* every test set. The embargo does not need to affect training observations prior to a test set, because training labels *Y <sup>i</sup>* = *f* [[ *t i , 0* , *t i , 1* ]], where *t <sup>i</sup> , <sup>1</sup>* < *t j , 0* (training ends before testing begins), contain information that was available at the testing time *t j , 0* . In other words, we are only concerned with training labels *Y <sup>i</sup>* = *f* [[ *t i , 0* , *t i , 1* ]] that take place immediately after the test, *t <sup>j</sup> , <sup>1</sup>* ≤ *t <sup>i</sup> , <sup>0</sup>* ≤ *t <sup>j</sup> , <sup>1</sup>* + *h.* We can implement this embargo period *h* by setting *Y <sup>j</sup>* = *f* [[ *t j , 0* , *t <sup>j</sup> , <sup>1</sup>* + *h* ]] before purging. A small value *h* ≈ .01 *T* often suffices to prevent all leakage, as can be confirmed by testing that performance does not improve indefinitely by increasing *k* → *T* . Figure 7.3 illustrates the embargoing of train observations immediately after the testing set. Snippet 7.2 implements the embargo logic.

![](_page_7_Figure_0.jpeg)

**Figure 7.3** Embargo of post-test train observations

#### **SNIPPET 7.2 EMBARGO ON TRAINING OBSERVATIONS**

**7.4.3 The Purged K-Fold Class**

In the previous sections we have discussed how to produce training/testing splits when labels overlap. That introduced the notion of purging and embargoing, in the particular context of model development. In general, we need to purge and embargo overlapping training observations whenever we produce a train/test split, whether it is for hyper-parameter fitting, backtesting, or performance evaluation. Snippet 7.3 extends scikit-learn's KFold class to account for the possibility of leakages of testing information into the training set.

#### **SNIPPET 7.3 CROSS-VALIDATION CLASS WHEN OBSERVATIONS OVERLAP**

### **7.5 Bugs in Sklearn's Cross-Validation**

You would think that something as critical as cross-validation would be perfectly implemented in one of the most popular ML libraries. Unfortunately that is not the case, and this is one of the reasons you must always read all the code you run, and a strong point in favor of open source. One of the many upsides of open-source code is that you can verify everything and adjust it to your needs. Snippet 7.4 addresses two known sklearn bugs:

- 1. Scoring functions do not know classes\_ , as a consequence of sklearn's reliance on numpy arrays rather than pandas series: <https://github.com/scikit-learn/scikit-learn/issues/6231>
- 2. cross\_val\_score will give different results because it passes weights to the fit method, but not to the log\_loss [method: https://github.com/scikit](https://github.com/scikit-learn/scikit-learn/issues/9144)learn/scikit-learn/issues/9144

### **SNIPPET 7.4 USING THE PURGEDKFOLD CLASS**

Please understand that it may take a long time until a fix for these bugs is agreed upon, implemented, tested, and released. Until then, you should use cvScore in Snippet 7.4, and avoid running the function cross\_val\_score .

### **Exercises**

- 1. Why is shuffling a dataset before conducting k-fold CV generally a bad idea in finance? What is the purpose of shuffling? Why does shuffling defeat the purpose of k-fold CV in financial datasets?
- 2. Take a pair of matrices ( *X* , *y* ), representing observed features and labels. These could be one of the datasets derived from the exercises in Chapter 3.
  - 1. Derive the performance from a 10-fold CV of an RF classifier on (*X* , *y* ), without shuffling.
  - 2. Derive the performance from a 10-fold CV of an RF on (*X* , *y* ), with shuffling.
  - 3. Why are both results so different?
  - 4. How does shuffling leak information?
- 3. Take the same pair of matrices ( *X* , *y* ) you used in exercise 2.
  - 1. Derive the performance from a 10-fold purged CV of an RF on (*X* , *y* ), with 1% embargo.
  - 2. Why is the performance lower?
  - 3. Why is this result more realistic?
- 4. In this chapter we have focused on one reason why k-fold CV fails in financial applications, namely the fact that some information from the testing set leaks into the training set. Can you think of a second reason for CV's failure?
- 5. Suppose you try one thousand configurations of the same investment strategy, and perform a CV on each of them. Some results are guaranteed to look good, just by sheer luck. If you only publish those positive results, and hide the rest, your audience will not be able to deduce that these results are false positives, a statistical fluke. This phenomenon is called "selection bias."
  - 1. Can you imagine one procedure to prevent this?
  - 2. What if we split the dataset in three sets: training, validation, and testing? The validation set is used to evaluate the trained parameters,
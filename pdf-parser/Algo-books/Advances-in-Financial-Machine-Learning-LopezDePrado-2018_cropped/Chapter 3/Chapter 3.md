- 1. Sample bars using the CUSUM filter, where {*y <sup>t</sup>* } are absolute returns and *h* = 0.05*.*
- 2. Compute the rolling standard deviation of the sampled bars.
- 3. Compare this result with the results from exercise 4. What procedure delivered the least heteroscedastic sample? Why?

#### **References**

- 1. Ané, T. and H. Geman (2000): "Order flow, transaction clock and normality of asset returns." *Journal of Finance* , Vol. 55, pp. 2259–2284.
- 2. Bailey, David H., and M. López de Prado (2012): "Balanced baskets: A new approach to trading and hedging risks." *Journal of Investment Strategies (Risk Journals)* , Vol. 1, No. 4 (Fall), pp. 21–62.
- 3. Clark, P. K. (1973): "A subordinated stochastic process model with finite variance for speculative prices." *Econometrica* , Vol. 41, pp. 135–155.
- 4. Easley, D., M. López de Prado, and M. O'Hara (2011): "The volume clock: Insights into the high frequency paradigm." *Journal of Portfolio Management* , Vol. 37, No. 2, pp. 118–128.
- 5. Easley, D., M. López de Prado, and M. O'Hara (2012): "Flow toxicity and liquidity in a high frequency world." *Review of Financial Studies* , Vol. 25, No. 5, pp. 1457–1493.
- 6. Fama, E. and M. Blume (1966): "Filter rules and stock market trading." *Journal of Business* , Vol. 40, pp. 226–241.
- 7. Kolanovic, M. and R. Krishnamachari (2017): "Big data and AI strategies: Machine learning and alternative data approach to investing." White paper, JP Morgan, Quantitative and Derivatives Strategy. May 18.
- 8. Lam, K. and H. Yam (1997): "CUSUM techniques for technical trading in financial markets." *Financial Engineering and the Japanese Markets* , Vol. 4, pp. 257–274.
- 9. López de Prado, M. and D. Leinweber (2012): "Advances in cointegration and subset correlation hedging methods." *Journal of Investment Strategies (Risk Journals)* , Vol. 1, No. 2 (Spring), pp. 67–115.
- 10. Mandelbrot, B. and M. Taylor (1967): "On the distribution of stock price differences." *Operations Research* , Vol. 15, No. 5, pp. 1057–1062.

# **CHAPTER 3**

# **Labeling**

#### **3.1 Motivation**

In Chapter 2 we discussed how to produce a matrix *X* of financial features out of an unstructured dataset. Unsupervised learning algorithms can learn the patterns from that matrix *X* , for example whether it contains hierarchical clusters. On the other hand, supervised learning algorithms require that the rows in *X* are associated with an array of labels or values *y* , so that those labels or values can be predicted on unseen features samples. In this chapter we will discuss ways to label financial data.

#### **3.2 The Fixed-Time Horizon Method**

As it relates to finance, virtually all ML papers label observations using the fixed-time horizon method. This method can be described as follows. Consider a features matrix *X* with *I* rows, { *X <sup>i</sup>* } *<sup>i</sup>* <sup>=</sup> 1, …, *<sup>I</sup>* , drawn from some bars with index *t* = 1, …, *T* , where *I* ≤ *T* . Chapter 2, Section 2.5 discussed sampling methods that produce the set of features { *X <sup>i</sup>* } *<sup>i</sup>* = 1, …, *I* . An observation *X <sup>i</sup>* is assigned a label *y <sup>i</sup>* ∈ { − 1, 0, 1},

$$y_i = \begin{cases} -1 & \text{if } r_{t_{i,0},t_{i,0}+h} < -\tau \\ 0 & \text{if } |r_{t_{i,0},t_{i,0}+h}| \le \tau \\ 1 & \text{if } r_{t_{i,0},t_{i,0}+h} > \tau \end{cases}$$

where τ is a pre-defined constant threshold, *t i , 0* is the index of the bar immediately after *X <sup>i</sup>* takes place, *t <sup>i</sup> , <sup>0</sup>* + *h* is the index of the *h* -th bar after *t i , 0* , and is the price return over a bar horizon *h* ,

$$r_{t_{i,0},t_{i,0}+h} = \frac{p_{t_{i,0}+h}}{p_{t_{i,0}}} - 1$$

Because the literature almost always works with time bars, *h* implies a fixed-time horizon. The bibliography section lists multiple ML studies, of which Dixon et al. [2016] is a recent example of this labeling method. Despite its popularity, there are several reasons to avoid this approach in most cases. First, as we saw in Chapter 2, time bars do not exhibit good statistical properties. Second, the same threshold τ is applied regardless of the observed volatility. Suppose that τ = 1 *E* − 2, where sometimes we label an observation as *y <sup>i</sup>* = 1 subject to a realized bar volatility of (e.g., during the night session), and sometimes (e.g., around the open). The large majority of labels will be 0, even if return was predictable and statistically significant.

In other words, it is a very common error to label observations according to a fixed threshold on time bars. Here are a couple of better alternatives. First, label per a varying threshold , estimated using a rolling exponentially weighted standard deviation of returns. Second, use volume or dollar bars, as their volatilities are much closer to constant (homoscedasticity). But even these two improvements miss a key flaw of the fixed-time horizon method: the path followed by prices. Every investment strategy has stop-loss limits, whether they are self-imposed by the portfolio manager, enforced by the risk department, or triggered by a margin call. It is simply unrealistic to build a strategy that profits from positions that would have been stopped-out by the exchange. That virtually no publication accounts for that when labeling observations tells you something about the current state of the investment literature.

#### **3.3 Computing Dynamic Thresholds**

As argued in the previous section, in practice we want to set profit taking and stop-loss limits that are a function of the risks involved in a bet. Otherwise, sometimes we will be aiming too high ( ), and sometimes too low ( ), considering the prevailing volatility.

Snippet 3.1 computes the daily volatility at intraday estimation points, applying a span of span0 days to an exponentially weighted moving standard deviation. See the pandas documentation for details on the pandas.Series.ewm function.

#### **SNIPPET 3.1 DAILY VOLATILITY ESTIMATES**

We can use the output of this function to set default profit taking and stop-loss limits throughout the rest of this chapter.

#### **3.4 The Triple-Barrier Method**

Here I will introduce an alternative labeling method that I have not found in the literature. If you are an investment professional, I think you will agree that it makes more sense. I call it the triple-barrier method because it labels an observation according to the first barrier touched out of three barriers. First, we set two horizontal barriers and one vertical barrier. The two horizontal barriers are defined by profit-taking and stop-loss limits, which are a dynamic function of estimated volatility (whether realized or implied). The third barrier is defined in terms of number of bars elapsed since the position was taken (an expiration limit). If the upper barrier is touched first, we label the observation as a 1. If the lower barrier is touched first, we label the observation as a −1. If the vertical barrier is touched first, we have two choices: the sign of the return, or a 0. I personally prefer the former as a matter of realizing a profit or loss within limits, but you should explore whether a 0 works better in your particular problems.

You may have noticed that the triple-barrier method is path-dependent. In order to label an observation, we must take into account the entire path spanning [ *t i , 0* , *t <sup>i</sup> , <sup>0</sup>* + *h* ], where *h*

defines the vertical barrier (the expiration limit). We will denote *t i , 1* the time of the first barrier touch, and the return associated with the observed feature is . For the sake of clarity, *t <sup>i</sup> , <sup>1</sup>* ≤ *t <sup>i</sup> , <sup>0</sup>* + *h* and the horizontal barriers are not necessarily symmetric.

Snippet 3.2 implements the triple-barrier method. The function receives four arguments:

- close : A pandas series of prices.
- events : A pandas dataframe, with columns,
  - t1 : The timestamp of vertical barrier. When the value is np.nan , there will not be a vertical barrier.
  - trgt : The unit width of the horizontal barriers.
- ptSl : A list of two non-negative float values:
  - ptSl[0] : The factor that multiplies trgt to set the width of the upper barrier. If 0, there will not be an upper barrier.
  - ptSl[1] : The factor that multiplies trgt to set the width of the lower barrier. If 0, there will not be a lower barrier.
- molecule : A list with the subset of event indices that will be processed by a single thread. Its use will become clear later on in the chapter.

#### **SNIPPET 3.2 TRIPLE-BARRIER LABELING METHOD**

The output from this function is a pandas dataframe containing the timestamps (if any) at which each barrier was touched. As you can see from the previous description, the method considers the possibility that each of the three barriers may be disabled. Let us denote a barrier configuration by the triplet [ pt,sl,t1 ], where a 0 means that the barrier is inactive and a 1 means that the barrier is active. The possible eight configurations are:

Three useful configurations:

- [1,1,1]: This is the standard setup, where we define three barrier exit conditions. We would like to realize a profit, but we have a maximum tolerance for losses and a holding period.
- [0,1,1]: In this setup, we would like to exit after a number of bars, unless we are stopped-out.
- [1,1,0]: Here we would like to take a profit as long as we are not stopped-out. This is somewhat unrealistic in that we are willing to hold the position for as long as it takes.
- Three less realistic configurations:
  - [0,0,1]: This is equivalent to the fixed-time horizon method. It may still be useful when applied to volume-, dollar-, or information-driven bars, and multiple forecasts are updated within the horizon.
  - [1,0,1]: A position is held until a profit is made or the maximum holding period is exceeded, without regard for the intermediate unrealized losses.
  - [1,0,0]: A position is held until a profit is made. It could mean being locked on a losing position for years.
- Two illogical configurations:
  - [0,1,0]: This is an aimless configuration, where we hold a position until we are stopped-out.
  - [0,0,0]: There are no barriers. The position is locked forever, and no label is generated.

Figure 3.1 shows two alternative configurations of the triple-barrier method. On the left, the configuration is [1,1,0], where the first barrier touched is the lower horizontal one. On the right, the configuration is [1,1,1], where the first barrier touched is the vertical one.

![](_page_5_Figure_0.jpeg)

**Figure 3.1** Two alternative configurations of the triple-barrier method

## **3.5 Learning Side and Size**

In this section we will discuss how to label examples so that an ML algorithm can learn both the side and the size of a bet. We are interested in learning the side of a bet when we do not have an underlying model to set the sign of our position (long or short). Under such circumstance, we cannot differentiate between a profit-taking barrier and a stop-loss barrier, since that requires knowledge of the side. Learning the side implies that either there are no horizontal barriers or that the horizontal barriers must be symmetric.

Snippet 3.3 implements the function getEvents , which finds the time of the first barrier touch. The function receives the following arguments:

- close : A pandas series of prices.
- tEvents : The pandas timeindex containing the timestamps that will seed every triple barrier. These are the timestamps selected by the sampling procedures discussed in Chapter 2, Section 2.5.
- ptSl : A non-negative float that sets the width of the two barriers. A 0 value means that the respective horizontal barrier (profit taking and/or stop loss) will be disabled.
- t1 : A pandas series with the timestamps of the vertical barriers. We pass a False when we want to disable vertical barriers.
- trgt : A pandas series of targets, expressed in terms of absolute returns.
- minRet : The minimum target return required for running a triple barrier search.
- numThreads : The number of threads concurrently used by the function.

### **SNIPPET 3.3 GETTING THE TIME OF FIRST TOUCH**

Suppose that *I* = 1 *E* 6 and *h* = 1 *E* 3, then the number of conditions to evaluate is up to one billion on a single instrument. Many ML tasks are computationally expensive unless you are familiar with multi-threading, and this is one of them. Here is where parallel computing comes into play. Chapter 20 discusses a few multiprocessing functions that we will use throughout the book.

Function mpPandasObj calls a multiprocessing engine, which is explained in depth in Chapter 20. For the moment, you simply need to know that this function will execute applyPtSlOnT1 in parallel. Function applyPtSlOnT1 returns the timestamps at which each barrier is touched (if any). Then, the time of the first touch is the earliest time among the three returned by applyPtSlOnT1 . Because we must learn the side of the bet, we have passed ptSl = [ptSl,ptSl] as argument, and we arbitrarily set the side to be always long (the horizontal barriers are symmetric, so the side is irrelevant to determining the time of the first touch). The output from this function is a pandas dataframe with columns:

- t1 : The timestamp at which the first barrier is touched.
- trgt : The target that was used to generate the horizontal barriers.

Snippet 3.4 shows one way to define a vertical barrier. For each index in tEvents , it finds the timestamp of the next price bar at or immediately after a number of days numDays . This vertical barrier can be passed as optional argument t1 in getEvents .

### **SNIPPET 3.4 ADDING A VERTICAL BARRIER**

Finally, we can label the observations using the getBins function defined in Snippet 3.5. The arguments are the events dataframe we just discussed, and the close pandas series of prices. The output is a dataframe with columns:

- ret : The return realized at the time of the first touched barrier.
- bin : The label, { − 1, 0, 1}, as a function of the sign of the outcome. The function can be easily adjusted to label as 0 those events when the vertical barrier was touched first, which we leave as an exercise.

### **SNIPPET 3.5 LABELING FOR SIDE AND SIZE**

# **3.6 Meta-Labeling**

Suppose that you have a model for setting the side of the bet (long or short). You just need to learn the size of that bet, which includes the possibility of no bet at all (zero size). This is a situation that practitioners face regularly. We

often know whether we want to buy or sell a product, and the only remaining question is how much money we should risk in such a bet. We do not want the ML algorithm to learn the side, just to tell us what is the appropriate size. At this point, it probably does not surprise you to hear that no book or paper has so far discussed this common problem. Thankfully, that misery ends here. I call this problem meta-labeling because we want to build a secondary ML model that learns how to use a primary exogenous model.

Rather than writing an entirely new getEvents function, we will make some adjustments to the previous code, in order to handle meta-labeling. First, we accept a new side optional argument (with default None ), which contains the side of our bets as decided by the primary model. When side is not None , the function understands that meta-labeling is in play. Second, because now we know the side, we can effectively discriminate between profit taking and stop loss. The horizontal barriers do not need to be symmetric, as in Section 3.5. Argument ptSl is a list of two non-negative float values, where ptSl[0] is the factor that multiplies trgt to set the width of the upper barrier, and ptSl[1] is the factor that multiplies trgt to set the width of the lower barrier. When either is 0, the respective barrier is disabled. Snippet 3.6 implements these enhancements.

#### **SNIPPET 3.6 EXPANDING GETEVENTS TO INCORPORATE META-LABELING**

Likewise, we need to expand the getBins function, so that it handles metalabeling. Snippet 3.7 implements the necessary changes.

#### **SNIPPET 3.7 EXPANDING GETBINS TO INCORPORATE META-LABELING**

Now the possible values for labels in out['bin'] are {0,1}, as opposed to the previous feasible values {−1,0,1}. The ML algorithm will be trained to decide whether to take the bet or pass, a purely binary prediction. When the predicted label is 1, we can use the probability of this secondary prediction to derive the size of the bet, where the side (sign) of the position has been set by the primary model.

### **3.7 How to Use Meta-Labeling**

Binary classification problems present a trade-off between type-I errors (false positives) and type-II errors (false negatives). In general, increasing the true positive rate of a binary classifier will tend to increase its false positive rate. The receiver operating characteristic (ROC) curve of a binary classifier

measures the cost of increasing the true positive rate, in terms of accepting higher false positive rates.

Figure 3.2 illustrates the so-called "confusion matrix." On a set of observations, there are items that exhibit a condition (positives, left rectangle), and items that do not exhibit a condition (negative, right rectangle). A binary classifier predicts that some items exhibit the condition (ellipse), where the TP area contains the true positives and the TN area contains the true negatives. This leads to two kinds of errors: false positives (FP) and false negatives (FN). "Precision" is the ratio between the TP area and the area in the ellipse. "Recall" is the ratio between the TP area and the area in the left rectangle. This notion of recall (aka true positive rate) is in the context of classification problems, the analogous to "power" in the context of hypothesis testing. "Accuracy" is the sum of the TP and TN areas divided by the overall set of items (square). In general, decreasing the FP area comes at a cost of increasing the FN area, because higher precision typically means fewer calls, hence lower recall. Still, there is some combination of precision and recall that maximizes the overall efficiency of the classifier. The F1-score measures the efficiency of a classifier as the harmonic average between precision and recall (more on this in Chapter 14).

![](_page_13_Figure_2.jpeg)

**Figure 3.2** A visualization of the "confusion matrix"

Meta-labeling is particularly helpful when you want to achieve higher F1 scores. First, we build a model that achieves high recall, even if the precision is not particularly high. Second, we correct for the low precision by applying meta-labeling to the positives predicted by the primary model.

Meta-labeling will increase your F1-score by filtering out the false positives, where the majority of positives have already been identified by the primary model. Stated differently, the role of the secondary ML algorithm is to determine whether a positive from the primary (exogenous) model is true or false. It is *not* its purpose to come up with a betting opportunity. Its purpose is to determine whether we should act or pass on the opportunity that has been presented.

Meta-labeling is a very powerful tool to have in your arsenal, for four additional reasons. First, ML algorithms are often criticized as black boxes (see Chapter 1). Meta-labeling allows you to build an ML system on top of a white box (like a fundamental model founded on economic theory). This ability to transform a fundamental model into an ML model should make meta-labeling particularly useful to "quantamental" firms. Second, the effects of overfitting are limited when you apply meta-labeling, because ML will not decide the side of your bet, only the size. Third, by decoupling the side prediction from the size prediction, meta-labeling enables sophisticated strategy structures. For instance, consider that the features driving a rally may differ from the features driving a sell-off. In that case, you may want to develop an ML strategy exclusively for long positions, based on the buy recommendations of a primary model, and an ML strategy exclusively for short positions, based on the sell recommendations of an entirely different primary model. Fourth, achieving high accuracy on small bets and low accuracy on large bets will ruin you. As important as identifying good opportunities is to size them properly, so it makes sense to develop an ML algorithm solely focused on getting that critical decision (sizing) right. We will retake this fourth point in Chapter 10. In my experience, meta-labeling ML models can deliver more robust and reliable outcomes than standard labeling models.

## **3.8 The Quantamental Way**

You may have read in the press that many hedge funds are embracing the quantamental approach. A simple Google search will show reports that many hedge funds, including some of the most traditional ones, are investing tens of millions of dollars in technologies designed to combine human expertise with quantitative methods. It turns out, meta-labeling is exactly what these people have been waiting for. Let us see why.

Suppose that you have a series of features that you believe can forecast some prices, you just do not know how. Since you do not have a model to determine the side of each bet, you need to learn both side and size. You apply what you have learned in Section 3.5, and produce some labels based on the triple-barrier method with symmetric horizontal barriers. Now you are ready to fit your

algorithm on a training set, and evaluate the accuracy of your forecasts on a testing set. Alternatively, you could do the following:

- 1. Use your forecasts from the primary model, and generate meta-labels. Remember, horizontal barriers do not need to be symmetric in this case.
- 2. Fit your model again on the same training set, but this time using the meta-labels you just generated.
- 3. Combine the "sides" from the first ML model with the "sizes" from the second ML model.

You can always add a meta-labeling layer to any primary model, whether that is an ML algorithm, an econometric equation, a technical trading rule, a fundamental analysis, etc. That includes forecasts generated by a human, solely based on his intuition. In that case, meta-labeling will help us figure out when we should pursue or dismiss a discretionary PM's call. The features used by such meta-labeling ML algorithm could range from market information to biometric statistics to psychological assessments. For example, the metalabeling ML algorithm could find that discretionary PMs tend to make particularly good calls when there is a structural break (Chapter 17), as they may be quicker to grasp a change in the market regime. Conversely, it may find that PMs under stress, as evidenced by fewer hours of sleep, fatigue, change in weight, etc. tend to make inaccurate predictions. <sup>1</sup> Many professions require regular psychological exams, and an ML meta-labeling algorithm may find that those scores are also relevant to assess our current degree of confidence on a PM's predictions. Perhaps none of these factors affect discretionary PMs, and their brains operate independently from their emotional being, like cold calculating machines. My guess is that this is not the case, and therefore metalabeling should become an essential ML technique for every discretionary hedge fund. In the near future, every discretionary hedge fund will become a quantamental firm, and meta-labeling offers them a clear path to make that transition.

## **3.9 Dropping Unnecessary Labels**

Some ML classifiers do not perform well when classes are too imbalanced. In those circumstances, it is preferable to drop extremely rare labels and focus on the more common outcomes. Snippet 3.8 presents a procedure that recursively drops observations associated with extremely rare labels. Function dropLabels recursively eliminates those observations associated with classes that appear less than a fraction minPct of cases, unless there are only two classes left.

### **SNIPPET 3.8 DROPPING UNDER-POPULATED LABELS**

Incidentally, another reason you may want to drop unnecessary labels is this known sklearn bug: <https://github.com/scikit-learn/scikit-learn/issues/8566> . This sort of bug is a consequence of very fundamental assumptions in sklearn implementation, and resolving them is far from trivial. In this particular instance, the error stems from sklearn's decision to operate with standard numpy arrays rather than structured arrays or pandas objects. It is unlikely that there will be a fix by the time you are reading this chapter, or in the near future. In later chapters, we will study ways to circumvent these sorts of implementation errors, by building your own classes and expanding sklearn's functionality.

## **Exercises**

- 1. Form dollar bars for E-mini S&P 500 futures:
  - 1. Apply a symmetric CUSUM filter (Chapter 2, Section 2.5.2.1) where the threshold is the standard deviation of daily returns (Snippet 3.1).
  - 2. Use Snippet 3.4 on a pandas series t1 , where numDays = 1 .
  - 3. On those sampled features, apply the triple-barrier method, where ptSl = [1,1] and t1 is the series you created in point 1.b.
  - 4. Apply getBins to generate the labels.
- 2. From exercise 1, use Snippet 3.8 to drop rare labels.

- 3. Adjust the getBins function (Snippet 3.5) to return a 0 whenever the vertical barrier is the one touched first.
- 4. Develop a trend-following strategy based on a popular technical analysis statistic (e.g., crossing moving averages). For each observation, the model suggests a side, but not a size of the bet.
  - 1. Derive meta-labels for ptSl = [1,2] and t1 where numDays = 1 . Use as trgt the daily standard deviation as computed by Snippet 3.1.
  - 2. Train a random forest to decide whether to trade or not. Note: The decision is whether to trade or not, {0,1}, since the underlying model (the crossing moving average) has decided the side, {−1,1}.
- 5. Develop a mean-reverting strategy based on Bollinger bands. For each observation, the model suggests a side, but not a size of the bet.
  - 1. Derive meta-labels for ptSl = [0,2] and t1 where numDays = 1 . Use as trgt the daily standard deviation as computed by Snippet 3.1.
  - 2. Train a random forest to decide whether to trade or not. Use as features: volatility, serial correlation, and the crossing moving averages from exercise 2.
  - 3. What is the accuracy of predictions from the primary model (i.e., if the secondary model does not filter the bets)? What are the precision, recall, and F1-scores?
  - 4. What is the accuracy of predictions from the secondary model? What are the precision, recall, and F1-scores?

### **Bibliography**

- 1. Ahmed, N., A. Atiya, N. Gayar, and H. El-Shishiny (2010): "An empirical comparison of machine learning models for time series forecasting." *Econometric Reviews* , Vol. 29, No. 5–6, pp. 594–621.
- 2. Ballings, M., D. van den Poel, N. Hespeels, and R. Gryp (2015): "Evaluating multiple classifiers for stock price direction prediction." *Expert Systems with Applications* , Vol. 42, No. 20, pp. 7046–7056.
- 3. Bontempi, G., S. Taieb, and Y. Le Borgne (2012): "Machine learning strategies for time series forecasting." *Lecture Notes in Business Information Processing* , Vol. 138, No. 1, pp. 62–77.
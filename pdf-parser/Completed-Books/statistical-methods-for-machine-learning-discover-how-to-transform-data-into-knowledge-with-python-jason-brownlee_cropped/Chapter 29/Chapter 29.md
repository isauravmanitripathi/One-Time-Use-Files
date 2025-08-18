# Chapter 29

## Independence Test

A common problem in applied machine learning is determining whether input features are relevant to the outcome to be predicted. This is the problem of feature selection. In the case of classification problems where input variables are also categorical, we can use statistical tests to determine whether the output variable is dependent or independent of the input variables. If independent, then the input variable is a candidate for a feature that may be irrelevant to the problem and removed from the dataset.

The Pearson's Chi-Squared statistical hypothesis is an example of a test for independence between categorical variables. In this tutorial, you will discover the Chi-Squared statistical hypothesis test for quantifying the independence of pairs of categorical variables. After completing this tutorial, you will know:

- Pairs of categorical variables can be summarized using a contingency table.
- The Chi-Squared test can compare an observed contingency table to an expected table and determine if the categorical variables are independent.
- How to calculate and interpret the Chi-Squared test for categorical variables in Python.

Let's get started.

### 29.1 Tutorial Overview

This tutorial is divided into 3 parts; they are:

- 1. Contingency Table
- 2. Pearson's Chi-Squared Test
- 3. Example Chi-Squared Test

### 29.2 Contingency Table

A categorical variable is a variable that may take on one of a set of labels. An example might be sex, which may be summarized as male or female. The variable is sex and the labels or factors of the variable are male and female in this case. We may wish to look at a summary of a categorical variable as it pertains to another categorical variable. For example, sex and interest, where interest may have the labels science, math, or art. We can collect observations from people collected with regard to these two categorical variables; for example:

Sex, Interest Male, Art Female, Math Male, Science Male, Math ...

Listing 29.1: Example of a small categorical dataset.

We can summarize the collected observations in a table with one variable corresponding to columns and another variable corresponding to rows. Each cell in the table corresponds to the count or frequency of observations that correspond to the row and column categories. Historically, a table summarization of two categorical variables in this form is called a contingency table. For example, the Sex=rows and Interest=columns table with contrived counts might look as follows:

|        | Science, | Math, | Art |
|--------|----------|-------|-----|
| Male   | 20,      | 30,   | 15  |
| Female | 20,      | 15,   | 30  |

Listing 29.2: Example of a contingency table.

The table was called a contingency table, by Karl Pearson, because the intent is to help determine whether one variable is contingent upon or depends upon the other variable. For example, does an interest in math or science depend on gender, or are they independent? This is challenging to determine from the table alone; instead, we can use a statistical method called the Pearson's Chi-Squared test.

## 29.3 Pearson's Chi-Squared Test

The Pearson's Chi-Squared test, or just Chi-Squared test for short, is named for Karl Pearson, although there are variations on the test. The Chi-Squared test is a statistical hypothesis test that assumes (the null hypothesis) that the observed frequencies for a categorical variable match the expected frequencies for the categorical variable. The test calculates a statistic that has a Chi-Squared distribution, named for the Greek lowercase letter chi (χ) pronounced "ki" as in "kite".

Given the Sex/Interest example above, the number of observations for a category (such as male and female) may or may not be the same. Nevertheless, we can calculate the expected frequency of observations in each Interest group and see whether the partitioning of interests by Sex results in similar or different frequencies. The Chi-Squared test does this for a contingency table, first calculating the expected frequencies for the groups, then determining whether the division of the groups, called the observed frequencies, matches the expected frequencies. The result of the test is a test statistic that has a Chi-Squared distribution and can be interpreted to reject or fail to reject the assumption or null hypothesis that the observed and expected frequencies are the same, that the variables are independent of each other.

When observed frequency is far from the expected frequency, the corresponding term in the sum is large; when the two are close, this term is small. Large values of χ 2 indicate that observed and expected frequencies are far apart. Small values of χ 2 mean the opposite: observeds are close to expecteds. So χ <sup>2</sup> does give a measure of the distance between observed and expected frequencies.

— Page 525, Statistics, Fourth Edition, 2007.

The variables are considered independent if the observed and expected frequencies are similar, that the levels of the variables do not interact, are not dependent.

The chi-square test of independence works by comparing the categorically coded data that you have collected (known as the observed frequencies) with the frequencies that you would expect to get in each cell of a table by chance alone (known as the expected frequencies).

— Page 162, Statistics in Plain English, Third Edition, 2010.

We can interpret the test statistic in the context of the Chi-Squared distribution with the requisite number of degrees of freedom as follows:

- Test Statistic ≥ Critical Value: significant result, reject null hypothesis, dependent (H1).
- Test Statistic < Critical Value: not significant result, fail to reject null hypothesis, independent (H0).

The degrees of freedom for the Chi-Squared distribution is calculated based on the size of the contingency table as:

$$degrees of freedom = (rows - 1) \times (cols - 1)$$
(29.1)

In terms of a p-value and a chosen significance level (alpha), the test can be interpreted as follows:

- p-value ≤ alpha: significant result, reject null hypothesis, dependent (H1).
- p-value > alpha: not significant result, fail to reject null hypothesis, independent (H0).

For the test to be effective, at least five observations are required in each cell of the contingency table. Next, let's look at how we can calculate the Chi-Squared test.

## 29.4 Example Chi-Squared Test

The Pearson's Chi-Squared test for independence can be calculated in Python using the chi2 contingency() SciPy function. The function takes an array as input representing the contingency table for the two categorical variables. It returns the calculated statistic and p-value for interpretation as well as the calculated degrees of freedom and table of expected frequencies. ... # calculate Chi-Squared test stat, p, dof, expected = chi2\_contingency(table)

Listing 29.3: Example of calculating the Chi-Squared test.

We can interpret the statistic by retrieving the critical value from the Chi-Squared distribution for the probability and number of degrees of freedom. For example, a probability of 95% can be used, suggesting that the finding of the test is quite likely given the assumption of the test that the variables are independent. If the statistic is less than or equal to the critical value, we can fail to reject this assumption, otherwise it can be rejected.

```
...
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
if abs(stat) >= critical:
 print('Dependent (reject H0)')
else:
 print('Independent (fail to reject H0)')
```

Listing 29.4: Example of interpreting the Chi-Squared test statistic.

We can also interpret the p-value by comparing it to a chosen significance level, which would be 5%, calculated by inverting the 95% probability used in the critical value interpretation.

```
...
# interpret p-value
alpha = 1.0 - prob
if p <= alpha:
 print('Dependent (reject H0)')
else:
 print('Independent (fail to reject H0)')
```

Listing 29.5: Example of interpreting the Chi-Squared p-value.

We can tie all of this together and demonstrate the Chi-Squared significance test using a contrived contingency table. A contingency table is defined below that has a different number of observations for each population (row), but a similar proportion across each group (column). Given the similar proportions, we would expect the test to find that the groups are similar and that the variables are independent (fail to reject the null hypothesis, or H0).

```
...
# contingency table
table = [ [10, 20, 30],
     [6, 9, 17]]
```

Listing 29.6: Example of a contingency table.

The complete example is listed below.

```
# chi-squared test with similar proportions
from scipy.stats import chi2_contingency
from scipy.stats import chi2
# contingency table
table = [ [10, 20, 30],
```

```
[6, 9, 17]]
print(table)
stat, p, dof, expected = chi2_contingency(table)
print('dof=%d' % dof)
print(expected)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
 print('Dependent (reject H0)')
else:
 print('Independent (fail to reject H0)')
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
 print('Dependent (reject H0)')
else:
 print('Independent (fail to reject H0)')
```

Listing 29.7: Example of calculating the Chi-Squared test on the contingency table.

Running the example first prints the contingency table. The test is calculated and the degrees of freedom (dof) is reported as 2, which makes sense given:

$$\begin{aligned} dof &= (rows - 1) \times (cols - 1) \\ &= (2 - 1) \times (3 - 1) \\ &= 1 \times 2 \\ &= 2 \end{aligned} \tag{29.2}$$

Next, the calculated expected frequency table is printed and we can see that indeed the observed contingency table does appear to match via an eyeball check of the numbers. The critical value is calculated and interpreted, finding that indeed the variables are independent (fail to reject H0). The interpretation of the p-value makes the same finding.

```
[[10, 20, 30], [6, 9, 17]]
dof=2
[[10.43478261 18.91304348 30.65217391]
[ 5.56521739 10.08695652 16.34782609]]
probability=0.950, critical=5.991, stat=0.272
Independent (fail to reject H0)
significance=0.050, p=0.873
Independent (fail to reject H0)
```

Listing 29.8: Example output from calculating the Chi-Squared test on the contingency table.

### 29.5 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Update the Chi-Squared test to use your own contingency table.
- Write a function to report on the independence given observations from two categorical variables
- Load a standard machine learning dataset containing categorical variables and report on the independence of each.

If you explore any of these extensions, I'd love to know.

### 29.6 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

#### 29.6.1 Books

- Statistics in Plain English, Third Edition, 2010. <http://amzn.to/2IFyS4P>
- Statistics, Fourth Edition, 2007. <http://amzn.to/2u44zll>

#### 29.6.2 API

- scipy.stats.chisquare API. [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html). [html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- scipy.stats.chi2 contingency API. [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2\\_cont](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)ingency. [html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
- sklearn.feature selection.chi2 API. [http://scikit-learn.org/stable/modules/generated/sklearn.feature\\_selection](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html). [chi2.html](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html)

#### 29.6.3 Articles

- Chi-Squared test on Wikipedia. [https://en.wikipedia.org/wiki/Chi-squared\\_test](https://en.wikipedia.org/wiki/Chi-squared_test)
- Pearson's Chi-Squared test on Wikipedia. [https://en.wikipedia.org/wiki/Pearson%27s\\_chi-squared\\_test](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test)
- Contingency table on Wikipedia. [https://en.wikipedia.org/wiki/Contingency\\_table](https://en.wikipedia.org/wiki/Contingency_table)
- How is chi test used for feature selection in machine learning? on Quora. <https://www.quora.com/How-is-chi-test-used-for-feature-selection-in-machine-learning>

## 29.7 Summary

In this tutorial, you discovered the Chi-Squared statistical hypothesis test for quantifying the independence of pairs of categorical variables. Specifically, you learned:

- Pairs of categorical variables can be summarized using a contingency table.
- The Chi-Squared test can compare an observed contingency table to an expected table and determine if the categorical variables are independent.
- How to calculate and interpret the Chi-Squared test for categorical variables in Python.

#### 29.7.1 Next

This is the end of part VII, in the next part you will discover additional resources to help you on your journey with statistical methods.
# Chapter 8

# Central Limit Theorem

The central limit theorem is an often quoted, but misunderstood pillar from statistics and machine learning. It is often confused with the law of large numbers. Although the theorem may seem esoteric to beginners, it has important implications about how and why we can make inferences about the skill of machine learning models, such as whether one model is statistically better than another and confidence intervals on models skill. In this tutorial, you will discover the central limit theorem and the implications of this important pillar of statistics and probability on applied machine learning. After completing this tutorial, you will know:

- The central limit theorem describes the shape of the distribution of sample means as a Gaussian, which is a distribution that statistics knows a lot about.
- How to develop an example of simulated dice rolls in Python to demonstrate the central limit theorem.
- How the central limit theorem and knowledge of the Gaussian distribution is used to make inferences about model performance in applied machine learning.

Let's get started.

## 8.1 Tutorial Overview

This tutorial is divided into 3 parts; they are:

- 1. Central Limit Theorem
- 2. Worked Example with Dice
- 3. Impact on Machine Learning

## 8.2 Central Limit Theorem

The Central Limit Theorem, or CLT for short, is an important finding and pillar in the fields of statistics and probability. It may seem a little esoteric at first, so hang in there. It turns out that the finding is critically important for making inferences in applied machine learning. The theorem states that as the size of the sample increases, the distribution of the mean across multiple samples will approximate a Gaussian distribution. Let's break this down.

We can imagine performing a trial and getting a result or an observation. We can repeat the trial again and get a new independent observation. Collected together, multiple observations represents a sample of observations. A sample is a group of observations from a broader population of all possible observations that could be made given trials.

- Observation: Result from one trial of an experiment.
- Sample: Group of results gathered from separate independent trials.
- Population: Space of all possible observations that could be seen from a trial.

If we calculate the mean of a sample, it will be an estimate of the mean of the population distribution. But, like any estimate, it will be wrong and will contain some error. If we draw multiple independent samples, and calculate their means, the distribution of those means will form a Gaussian distribution. It is important that each trial that results in an observation be independent and performed in the same way. This is to ensure that the sample is drawing from the same underlying population distribution. More formally, this expectation is referred to as independent and identically distributed, or iid.

Firstly, the central limit theorem is impressive, especially as this will occur no matter the shape of the population distribution from which we are drawing samples. It demonstrates that the distribution of errors from estimating the population mean fit a distribution that the field of statistics knows a lot about. Secondly, this estimate of the Gaussian distribution will be more accurate as the size of the samples drawn from the population is increased. This means that if we use our knowledge of the Gaussian distribution in general to start making inferences about the means of samples drawn from a population, that these inferences will become more useful as we increase our sample size.

One interesting implication of the central limit theorem mentioned to me one time by a very clever scientist is that you can use it to generate Gaussian random numbers. You can generate uniformly random integers, sum groups of them together, and the results of the sums will be Gaussian. Remember that the mean is just the normalized sum of the sample. It's a slower method for generating random Gaussian variables than other methods (like the Box-Muller method), but a clear (and clever) application of the theorem.

### 8.2.1 Law of Large Numbers

The central limit theorem is often confused with the law of large numbers by beginners. The law of large numbers is another different theorem from statistics. It is simpler in that it states that as the size of a sample is increased, the more accurate of an estimate the sample mean will be of the population mean. The central limit theorem does not state anything about a single sample mean; instead, it is broader and states something about the shape or the distribution of sample means.

The law of large numbers is intuitive. It is why we think that collecting more data will lead to a more representative sample of observations from the domain. The theorem supports this intuition. The central limit theorem is not intuitive. Instead, it is a finding that we can exploit in order to make claims about sample means.

#### Worked Example with Dice $8.3$

We can make the central limit theorem concrete with a worked example involving the rolling of die. Remember that a die is a cube with a different number on each side from 1-to-6. Each number has a 1-in-6 likelihood to turn up from a roll. The distribution of the numbers that turn up from a dice roll is uniform given the equal likelihood. We can use the randint() NumPy function to generate a specific number of random dice rolls (e.g.  $50$ ) between 1 and 6.

```
# generate a sample of die rolls
rolls = randint(1, 7, 50)
```

. . .

Listing 8.1: Example of how to simulate dice rolls.

The complete example is listed below.

```
# generate random dice rolls
from numpy.random import seed
from numpy.random import randint
from numpy import mean
# seed the random number generator
seed(1)# generate a sample of die rolls
rolls = randint(1, 7, 50)<pre>print(rolls)</pre>
<pre>print(mean(rolls))</pre>
```

Listing 8.2: Example calculating the average of simulated dice rolls.

Running the example generates and prints the sample of 50 die rolls and the mean value of the sample. We know that the mean value of the distribution is 3.5 calculated as  $\frac{1+2+3+4+5+6}{6}$  or  $\frac{21}{6}$ . We can see that the mean of the sample is slightly wrong, which is to be expected because it is an estimate of the population mean.

```
[6 4 5 1 2 4 6 1 1 2 5 6 5 2 3 5 6 3 5 4 5 3 5 6 3 5 2 2 1 6 2 2 6 2 2 1 5
2 1 1 6 4 3 2 1 4 6 2 2 4
3.44
```

Listing 8.3: Sample output from simulated dice rolls.

This is the result of rolling the simulated die 50 times. We can then repeat this process multiple times, such as  $1,000$ . This will give us a result of  $1,000$  sample means. According to the central limit theorem, the distribution of these sample means will be Gaussian. The example below performs this experiment and plots the resulting distribution of sample means.

```
# demonstration of the central limit theorem
<pre>from numpy.random import seed</pre>
<pre>from numpy.random import randint</pre>
from numpy import mean
from matplotlib import pyplot
# seed the random number generator
seed(1)# calculate the mean of 50 dice rolls 1000 times
means = [mean(randint(1, 7, 50)) for _ in range(1000)]# plot the distribution of sample means
<pre>pyplot.hist(means)</pre>
```

#### pyplot.show()

Listing 8.4: Example of calculating the average of multiple simulations of dice rolls.

Running the example creates a histogram plot of the sample means. We can tell from the shape of the distribution that the distribution is Gaussian. It's interesting to note the amount of error in the sample mean that we can see in 1,000 trials of 50 dice rolls. Further, the central limit theorem also states that as the size of each sample, in this case 50, is increased, then the better the sample means will approximate a Gaussian distribution.

![](_page_3_Figure_4.jpeg)

Figure 8.1: Histogram plot of sample means from dice roll simulations.

## 8.4 Impact on Machine Learning

The central limit theorem has important implications in applied machine learning. The theorem does inform the solution to linear algorithms such as linear regression, but not exotic methods like artificial neural networks that are solved using numerical optimization methods. Instead, we must use experiments to observe and record the behavior of the algorithms and use statistical methods to interpret their results. Let's look at two important examples.

### 8.4.1 Significance Tests

In order to make inferences about the skill of a model compared to the skill of another model, we must use tools such as statistical significance tests. These tools estimate the likelihood that the two samples of model skill scores were drawn from the same or a different unknown underlying distribution of model skill scores. If it looks like the samples were drawn from the same population, then no difference between the models skill is assumed, and any actual differences are due to statistical noise.

The ability to make inference claims like this is due to the central limit theorem and our knowledge of the Gaussian distribution and how likely the two sample means are to be a part of the same Gaussian distribution of sample means.

### 8.4.2 Confidence Intervals

Once we have trained a final model, we may wish to make an inference about how skillful the model is expected to be in practice. The presentation of this uncertainty is called a confidence interval. We can develop multiple independent (or close to independent) evaluations of a model accuracy to result in a population of candidate skill estimates. The mean of these skill estimates will be an estimate (with error) of the true underlying estimate of the model skill on the problem.

With knowledge that the sample mean will be a part of a Gaussian distribution from the central limit theorem, we can use knowledge of the Gaussian distribution to estimate the likelihood of the sample mean based on the sample size and calculate an interval of desired confidence around the skill of the model.

## 8.5 Extensions

This section lists some ideas for extending the tutorial that you may wish to explore.

- Suggest two additional areas in an applied machine learning where the central limit theorem may be relevant.
- Implement a function for generating random Gaussian numbers exploiting the central limit theorem and numbers drawn from a uniform distribution.
- Update the demonstration of dice rolls to demonstrate the relationship between sample size and the fidelity of the Gaussian distribution of the sample means.

If you explore any of these extensions, I'd love to know.

## 8.6 Further Reading

This section provides more resources on the topic if you are looking to go deeper.

## 8.6.1 API

- numpy.random.seed API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html>
- numpy.random.randint API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html>
- numpy.mean API. <https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html>

## 8.6.2 Articles

- Central limit theorem on Wikipedia. [https://en.wikipedia.org/wiki/Central\\_limit\\_theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- Illustration of the central limit theorem on Wikipedia. [https://en.wikipedia.org/wiki/Illustration\\_of\\_the\\_central\\_limit\\_theorem](https://en.wikipedia.org/wiki/Illustration_of_the_central_limit_theorem)
- Law of large numbers on Wikipedia. [https://en.wikipedia.org/wiki/Law\\_of\\_large\\_numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## 8.7 Summary

In this tutorial, you discovered the central limit theorem and the implications of this important pillar of statistics and probability on applied machine learning. Specifically, you learned:

- The central limit theorem describes the shape of the distribution of sample means as a Gaussian, which is a distribution that statistics knows a lot about.
- How to develop an example of simulated dice rolls in Python to demonstrate the central limit theorem.
- How the central limit theorem and knowledge of the Gaussian distribution are used to make inferences about model performance in applied machine learning.

## 8.7.1 Next

This is the end of part III, in the next part you will discover statistical hypothesis testing.
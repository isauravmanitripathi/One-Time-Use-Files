## Chapter 2

# Introduction to Bayesian Statistics

The first part of Advanced Algorithmic Trading is concerned with a detailed look at Bayesian Statistics. As I mentioned in the introduction, Bayesian methods underpin many of the techniques in Time Series Analysis and Machine Learning, so it is essential that we gain an understanding of the "philosophy" of the Bayesian approach and how to apply it to real world quantitative finance problems.

This chapter has been written to help you understand the basic ideas of Bayesian Statistics, and in particular, Bayes' Theorem (also known as Bayes' Rule). We will see how the Bayesian approach compares to the more traditional Classical, or Frequentist, approach to statistics and the potential applications in both quantitative trading and risk management.

In the chapter we will:

- Define Bayesian statistics and Bayesian inference
- Compare Classical/Frequentist statistics and Bayesian statistics
- Derive the famous Bayes' Rule, an essential tool for Bayesian inference
- Interpret and apply Bayes' Rule for carrying out Bayesian inference
- Carry out a concrete probability coin-flip example of Bayesian inference

## 2.1 What is Bayesian Statistics?

Bayesian statistics is a particular approach to applying probability to statistical problems. It provides us with mathematical tools to update our beliefs about random events in light of seeing new data or evidence about those events.

In particular Bayesian inference interprets probability as a measure of believability or confidence that an individual may possess about the occurance of a particular event.

We may have a prior belief about an event, but our beliefs are likely to change when new evidence is brought to light. Bayesian statistics gives us a solid mathematical means of incorporating our prior beliefs, and evidence, to produce new posterior beliefs.

Bayesian statistics provides us with mathematical tools to rationally update our subjective beliefs in light of new data or evidence.

This is in contrast to another form of statistical inference, known as Classical or Frequentist statistics, which assumes that probabilities are the frequency of particular random events occuring in a long run of repeated trials.

For example, as we roll a fair unweighted six-sided die repeatedly, we would see that each number on the die tends to come up 1/6th of the time.

Frequentist statistics assumes that probabilities are the long-run frequency of random events in repeated trials.

When carrying out statistical inference, that is, inferring statistical information from probabilistic systems, the two approaches–Frequentist and Bayesian–have very different philosophies.

Frequentist statistics tries to eliminate uncertainty by providing estimates. Bayesian statistics tries to preserve and refine uncertainty by adjusting individual beliefs in light of new evidence.

#### 2.1.1 Frequentist vs Bayesian Examples

In order to make clear the distinction between these differing statistical philosophies, we will consider two examples of probabilistic systems:

- Coin flips What is the probability of an unfair coin coming up heads?
- Election of a particular candidate for UK Prime Minister What is the probability of seeing an individual candidate winning, who has not stood before?

Table 2.1.1 describes the alternative philosophies of the frequentist and Bayesian approaches. In the Bayesian interpretation probability is a summary of an individual's opinion. A key point is that various rational, intelligent individuals can have different opinions and thus form alternative prior beliefs. They have varying levels of access to data and ways of interpreting it. As time progresses information will diffuse as new data comes to light. Hence their potentially differing prior beliefs will lead to posterior beliefs that converge towards each other, under the rational updating procedure of Bayesian inference.

In the Bayesian framework an individual would apply a probability of 0 when they believe there is no chance of an event occuring, while they would apply a probability of 1 when they are absolutely certain of an event occuring. Assigning a probability between 0 and 1 allows weighted confidence in other potential outcomes.

In order to carry out Bayesian inference, we need to utilise a famous theorem in probability known as Bayes' rule and interpret it in the correct fashion. In the next section Bayes' rule is derived using the definition of conditional probability. However, it isn't essential to follow the derivation in order to use Bayesian methods, so feel free to skip the following section if you wish to jump straight into learning how to use Bayes' rule.

Note that due to the presence of cognitive biases many individuals mistakenly equate highly improbable events with events that have no chance of happening. This manifests in common vernacular when individuals state that certain tasks are "impossible", when in fact they may be merely very difficult. In quantitative finance this is extremely dangerous thinking, as it ignores the ever-present issue of tail-risk. Consider the failures of Barings Bank in 1995, Long-Term Capital Management in 1998 or Lehman Brothers in 2008. In Bayesian probability this usually translates as applying very low probability in priors to "impossible" chances, rather than zero.

| Example               | Frequentist Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Bayesian Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfair Coin Flip      | The probability of seeing a head<br>when<br>the<br>unfair<br>coin<br>is<br>flipped<br>long-run relative frequency<br>is the<br>of seeing a head when repeated<br>flips of the coin are carried out.<br>That<br>is,<br>as<br>we<br>carry<br>out<br>more<br>coin<br>flips<br>the<br>number<br>of<br>heads<br>obtained as a proportion of the<br>total flips tends to the "true" or<br>"physical" probability of the coin<br>coming up as heads.<br>In partic<br>ular<br>the<br>individual<br>running<br>the<br>experiment<br>does not<br>incorporate<br>their own beliefs about the fair<br>ness of other coins. | Prior to any flips of the coin an<br>individual<br>may<br>believe<br>that<br>the<br>coin is fair.<br>After a few flips the<br>coin continually comes up heads.<br>prior<br>Thus the<br>belief about fair<br>ness<br>of<br>the<br>coin<br>is<br>modified<br>to<br>account<br>for<br>the<br>fact<br>that<br>three<br>heads have come up in a row and<br>thus the coin might not be fair.<br>After 500 flips, with 400 heads,<br>the individual believes that the<br>coin is very unlikely to be fair.<br>The<br>posterior<br>belief<br>is<br>heavily<br>modified from the<br>prior<br>belief of<br>a fair coin. |
| Election of Candidate | The candidate only ever stands<br>once<br>for<br>this<br>particular<br>election<br>and<br>so<br>we<br>cannot<br>perform<br>"re<br>peated<br>trials".<br>In<br>a<br>frequen<br>tist<br>setting<br>we<br>construct<br>"vir<br>tual"<br>trials<br>of<br>the<br>election<br>pro<br>cess. The probability of the can<br>didate winning is defined as the<br>relative<br>frequency<br>of<br>the<br>candi<br>date winning in the "virtual" tri<br>als as a fraction of all trials.                                                                                                                                    | An<br>individual<br>has a<br>prior<br>belief<br>of a candidate's chances of win<br>ning<br>an<br>election<br>and<br>their<br>con<br>fidence<br>can<br>be<br>quantified<br>as<br>a<br>probability. However another in<br>dividual could also have a sepa<br>rate<br>differing<br>prior<br>belief<br>about<br>the<br>same<br>candidate's<br>chances.<br>As new data arrives, both beliefs<br>are (rationally) updated by the<br>Bayesian procedure.                                                                                                                                                             |

#### Deriving Bayes' Rule

We begin by considering the definition of conditional probability, which gives us a rule for determining the probability of an event A, given the occurance of another event B. An example question in this vein might be "What is the probability of rain occuring given that there are clouds in the sky?"

The mathematical definition of conditional probability is as follows:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
(2.1)

This simply states that the probability of A occuring given that B has occured is equal to the probability that they have both occured, relative to the probability that B has occured.

Or in the language of the example above: The probability of rain given that we have seen clouds is equal to the probability of rain and clouds occuring together, relative to the probability of seeing clouds at all.

If we multiply both sides of this equation by P(B) we get:

$$P(B)P(A|B) = P(A \cap B) \tag{2.2}$$

But, we can simply make the same statement about  $P(B|A)$ , which is akin to asking "What is the probability of seeing clouds, given that it is raining?":

$$P(B|A) = \frac{P(B \cap A)}{P(A)}$$
(2.3)

Note that  $P(A \cap B) = P(B \cap A)$  and so by substituting the above and multiplying by  $P(A)$ , we get:

$$P(A)P(B|A) = P(A \cap B) \tag{2.4}$$

We are now able to set the two expressions for  $P(A \cap B)$  equal to each other:

$$P(B)P(A|B) = P(A)P(B|A) \tag{2.5}$$

If we now divide both sides by  $P(B)$  we arrive at the celebrated Bayes' rule:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
(2.6)

However, it will be helpful for later usage of Bayes' rule to modify the denominator,  $P(B)$ on the right hand side of the above relation to be written in terms of  $P(B|A)$ . We can actually write:

$$P(B) = \sum_{a \in A} P(B \cap A) \tag{2.7}$$

This is possible because the events  $A$  are an exhaustive partition of the sample space. So that by substituting the definition of conditional probability we get:

$$P(B) = \sum_{a \in A} P(B \cap A) = \sum_{a \in A} P(B|A)P(A) \tag{2.8}$$

Finally, we can substitute this into Bayes' rule from above to obtain an alternative version of Bayes' rule, which is used heavily in Bayesian inference:

$$P(A|B) = \frac{P(B|A)P(A)}{\sum_{a \in A} P(B|A)P(A)}$$
(2.9)

Now that we have derived Bayes' rule we are able to apply it to statistical inference.

## 2.2 Applying Bayes' Rule for Bayesian Inference

As we stated at the start of this chapter the basic idea of Bayesian inference is to continually update our prior beliefs about events as new evidence is presented. This is a very natural way to think about probabilistic events. As more and more evidence is accumulated our prior beliefs are steadily "washed out" by any new data.

Consider a (rather nonsensical) prior belief that the Moon is going to collide with the Earth. For every night that passes, the application of Bayesian inference will tend to correct our prior belief to a posterior belief that the Moon is less and less likely to collide with the Earth, since it remains in orbit.

In order to demonstrate a concrete numerical example of Bayesian inference it is necessary to introduce some new notation.

Firstly, we need to consider the concept of parameters and models. A parameter could be the weighting of an unfair coin, which we could label as θ. Thus θ = P(H) would describe the probability distribution of our beliefs that the coin will come up as heads when flipped. The model is the actual means of encoding this flip mathematically. In this instance, the coin flip can be modelled as a Bernoulli trial.

#### Bernoulli Trial

A Bernoulli trial is a random experiment with only two outcomes, usually labelled as "success" or "failure", in which the probability of the success is exactly the same every time the trial is carried out. The probability of the success is given by θ, which is a number between 0 and 1. Thus θ ∈ [0, 1].

Over the course of carrying out some coin flip experiments (repeated Bernoulli trials) we will generate some data, D, about heads or tails.

A natural example question to ask is "What is the probability of seeing 3 heads in 8 flips (8 Bernoulli trials), given a fair coin (θ = 0.5)?".

A model helps us to ascertain the probability of seeing this data, D, given a value of the parameter θ. The probability of seeing data D under a particular value of θ is given by the following notation: P(D|θ).

However, if you consider it for a moment, we are actually interested in the alternative question - "What is the probability that the coin is fair (or unfair), given that I have seen a particular sequence of heads and tails?".

Thus we are interested in the probability distribution which reflects our belief about different possible values of θ, given that we have observed some data D. This is denoted by P(θ|D). Notice that this is the converse of P(D|θ). So how do we get between these two probabilities? It turns out that Bayes' rule is the link that allows us to go between the two situations.

#### Bayes' Rule for Bayesian Inference

$$P(\theta|D) = P(D|\theta) P(\theta) / P(D)$$
(2.10)

Where:

• P(θ) is the prior. This is the strength in our belief of θ without considering the evidence D. Our prior view on the probability of how fair the coin is.

- P(θ|D) is the posterior. This is the (refined) strength of our belief of θ once the evidence D has been taken into account. After seeing 4 heads out of 8 flips, say, this is our updated view on the fairness of the coin.
- P(D|θ) is the likelihood. This is the probability of seeing the data D as generated by a model with parameter θ. If we knew the coin was fair, this tells us the probability of seeing a number of heads in a particular number of flips.
- P(D) is the evidence. This is the probability of the data as determined by summing (or integrating) across all possible values of θ, weighted by how strongly we believe in those particular values of θ. If we had multiple views of what the fairness of the coin is (but didn't know for sure), then this tells us the probability of seeing a certain sequence of flips for all possibilities of our belief in the coin's fairness.

The entire goal of Bayesian inference is to provide us with a rational and mathematically sound procedure for incorporating our prior beliefs, with any evidence at hand, in order to produce an updated posterior belief. What makes it such a valuable technique is that posterior beliefs can themselves be used as prior beliefs under the generation of new data. Hence Bayesian inference allows us to continually adjust our beliefs under new data by repeatedly applying Bayes' rule.

There was a lot of theory to take in within the previous two sections, so I'm now going to provide a concrete example using the age-old tool of statisticians: the coin-flip.

## 2.3 Coin-Flipping Example

In this example we are going to consider multiple coin-flips of a coin with unknown fairness. We will use Bayesian inference to update our beliefs on the fairness of the coin as more data (i.e. more coin flips) becomes available. The coin will actually be fair, but we won't learn this until the trials are carried out. At the start we have no prior belief on the fairness of the coin, that is, we can say that any level of fairness is equally likely.

In statistical language we are going to perform N repeated Bernoulli trials with θ = 0.5. We will use a uniform probability distribution as a means of characterising our prior belief that we are unsure about the fairness. This states that we consider each level of fairness (or each value of θ) to be equally likely.

We are going to use a Bayesian updating procedure to go from our prior beliefs to posterior beliefs as we observe new coin flips. This is carried out using a particularly mathematically succinct procedure known as conjugate priors. We won't go into any detail on conjugate priors within this chapter, as it will form the basis of the next chapter on Bayesian inference. It will however provide us with the means of explaining how the coin flip example is carried out in practice.

The uniform distribution is actually a more specific case of another probability distribution, known as a Beta distribution. Conveniently, under the binomial model, if we use a Beta distribution for our prior beliefs it leads to a Beta distribution for our posterior beliefs. This is an extremely useful mathematical result, as Beta distributions are quite flexible in modelling beliefs. However, I don't want to dwell on the details of this too much here, since we will discuss it in the next chapter. At this stage, it just allows us to easily create some visualisations below that emphasise the Bayesian procedure!

In the following figure we can see 6 particular points at which we have carried out a number of Bernoulli trials (coin flips). In the first sub-plot we have carried out no trials and hence our probability density function (in this case our prior density) is the uniform distribution. It states that we have equal belief in all values of θ representing the fairness of the coin.

The next panel shows 2 trials carried out and they both come up heads. Our Bayesian procedure using the conjugate Beta distributions now allows us to update to a posterior density. Notice how the weight of the density is now shifted to the right hand side of the chart. This indicates that our prior belief of equal likelihood of fairness of the coin, coupled with 2 new data points, leads us to believe that the coin is more likely to be unfair (biased towards heads) than it is tails.

The following two panels show 10 and 20 trials respectively. Notice that even though we have seen 2 tails in 10 trials we are still of the belief that the coin is likely to be unfair and biased towards heads. After 20 trials, we have seen a few more tails appear. The density of the probability has now shifted closer to θ = P(H) = 0.5. Hence we are now starting to believe that the coin is possibly fair.

After 50 and 500 trials respectively, we are now beginning to believe that the fairness of the coin is very likely to be around θ = 0.5. This is indicated by the shrinking width of the probability density, which is now constrained tightly around θ = 0.46 in the final panel. Were we to carry out another 500 trials (since the coin is actually fair) we would see this probability density become even tighter and centred closer to θ = 0.5.

![](_page_6_Figure_5.jpeg)

Figure 2.1: Bayesian update procedure using the Beta-Binomial Model

Thus it can be seen that Bayesian inference gives us a rational procedure to go from an uncertain situation with limited information to a more certain situation with significant amounts of data. In the next chapter we will discuss the notion of conjugate priors in more depth, which heavily simplify the mathematics of carrying out Bayesian inference in this example.

For completeness, I've provided the Python code (heavily commented) for producing this plot. It makes use of SciPy's statistics model, in particular, the Beta distribution:

```
# beta_binomial.py
```

```
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
```

**if** \_\_name\_\_ == "\_\_main\_\_":

```
# Create a list of the number of coin tosses ("Bernoulli trials")
number_of_trials = [0, 2, 10, 20, 50, 500]
```

# Conduct 500 coin tosses and output into a list of 0s and 1s # where 0 represents a tail and 1 represents a head data = stats.bernoulli.rvs(0.5, size=number\_of\_trials[-1])

```
# Discretise the x-axis into 100 separate plotting points
x = np.linspace(0, 1, 100)
```

```
# Loops over the number_of_trials list to continually add
# more coin toss data. For each new set of data, we update
# our (current) prior belief to be a new posterior. This is
# carried out using what is known as the Beta-Binomial model.
# For the time being, we won't worry about this too much.
for i, N in enumerate(number_of_trials):
```

```
# Accumulate the total number of heads for this
# particular Bayesian update
heads = data[:N].sum()
```

```
# Create an axes subplot for each update
ax = plt.subplot(len(number_of_trials) / 2, 2, i + 1)
ax.set_title("%s trials, %s heads" % (N, heads))
```

```
# Add labels to both axes and hide labels on y-axis
plt.xlabel("$P(H)$, Probability of Heads")
plt.ylabel("Density")
if i == 0:
    plt.ylim([0.0, 2.0])
```

```
plt.setp(ax.get_yticklabels(), visible=False)
```

```
# Create and plot a Beta distribution to represent the
    # posterior belief in fairness of the coin.
    y = stats.beta.pdf(x, 1 + heads, 1 + N - heads)
    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
    plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)
# Expand plot to cover full width/height and show it
plt.tight_layout()
plt.show()
```
✖

# **4 Utility Theory**

Economic behavior is mainly considered a particular kind of rational decision making. To be more precise, it is assumed that agents maximize their personal felicity, with respect to economic variables like consumption or wealth, in a consistent and predictable manner. The purpose of utility theory is to provide a mathematical framework, in which rational behavior can be analyzed and consistently explained.

## **4.1 Lotteries**

The term lottery refers to the roots of game theory, to gambling. In the modern language of probability theory, it is a concept that collects information about a random variable and a specific probability distribution function, attached to it. Consider a discrete random variable *W* : Ω →W that assigns to every possible state of the world a specific wealth, *W*(ω*n*) = *wn*, measured in monetary units. A lottery is a list of all probability masses associated with the different realizations *w<sup>n</sup>* of the random variable *W*,

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$L(W) = (f(w_1), \dots, f(w_N)). \tag{4.1}$$

Because the probability mass function *f*(*wn*) is in one-to-one correspondence with the probability measure *P* of the underlying probability space (Ω,F ,*P*), it is customary to simplify the notation to

$$L = (p_1, \dots, p_N), \tag{4.2}$$

where we also suppressed the reference to the random variable. This concept is more versatile than it looks at first sight.

## **Example 4.1**

Suppose you want to grant a credit to only one of two customers. You expect different redemption profiles:

Customer 1:

- Full repayment of \$16 with *p* = 1 2
- Complete default with 1 − *p* = 1 2

Customer 2:

- Full repayment of \$16 with *q* = 1 10
- Partial recovery of \$4 with 1 − *q* = 9 10

Which lotteries correspond to the two alternatives?

## Solution

First of all, there are three states of the world: "default," "partial recovery," and "full repayment." These are mapped by *W* onto W= { 0, 4, 16} . The two lotteries then correspond to the different probability measures *P* and *Q*

$$L_1 = \left(\frac{1}{2}, 0, \frac{1}{2}\right)$$
 and  $L_2 = \left(0, \frac{9}{10}, \frac{1}{10}\right)$ .

........................................................................................................................

There is also a notion of compound lotteries. Let *L*<sup>1</sup> and *L*<sup>2</sup> be two lotteries, with respect to the random variable *W*, and π a probability, associated with another random variable *X*. The new lottery

$$L = \pi L_1 + (1 - \pi)L_2 \quad \text{with} \quad \pi_n = \pi p_n + (1 - \pi)q_n \tag{4.3}$$

is called a compound lottery. Compound lotteries are based on the independence of *W* and *X*. This is why the probabilities multiply.

**Quick calculation 4.1** Assume you decide the credit assignment in Example 4.1 by tossing a fair coin. What is the compound lottery?

## **4.2 Preference Relations and Expected Utility**

Given several risky alternatives, you might prefer one over another or you might be indifferent between two lotteries. The personal attitude of an agent towards any such pair of lotteries is described by so-called preference relations:

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

*L*<sup>1</sup> ≻ *L*<sup>2</sup> ↔ *L*<sup>1</sup> is better then *L*2, *L*<sup>1</sup> ≽ *L*<sup>2</sup> ↔ *L*<sup>1</sup> is at least as good as *L*2, *L*<sup>1</sup> ∼ *L*<sup>2</sup> ↔ indifference between *L*<sup>1</sup> and *L*2. (4.4)

Note that *L*<sup>1</sup> ≽ *L*<sup>2</sup> and simultaneously *L*<sup>1</sup> ≼ *L*<sup>2</sup> implies *L*<sup>1</sup> ∼*L*2. Preference relations provide access to an ordering of different lotteries, but realize that not every such order would qualify as rational.

## **Example 4.2**

Imagine you witness a common decision problem in a shoe shop. A customer has difficulties in deciding between a black pair of shoes, a red pair, and a brown pair.

After observing the scene for a while, you arrive at the conclusion that the preference relations of the poor soul have to be

```
"black" ≻ "red" and "brown" ≻ "black" and "red" ≻ "brown".
```

You see the problem?

Explanation

Such a case of circular preferences is called non-transitive. A non-transitive preference structure surely renders any kind of rational ordering impossible. Remarkably, rumor has it that about 50% of all shoe shop customers seem to face this kind of decision problem. ........................................................................................................................

So the natural question arises under which conditions can a rational preference order be achieved. Or put another way, is there a set of rules, such that a preference order, if obeying these rules, can be called rational in a sensible way? The answer is yes, and such a set of rules was stipulated by John von Neumann and Oskar Morgenstern, two great pioneers of game theory. They postulated four conditions, known as the axioms of expected utility theory:

| Axiom 1: | Completeness                                                              |       |
|----------|---------------------------------------------------------------------------|-------|
|          | ≽<br>≼<br>∼<br>L2,<br>L2,<br>L2).<br>(L1<br>Either<br>L1<br>L1<br>or both |       |
| Axiom 2: | Transitivity                                                              |       |
|          | ≽L<br>≽L2,<br>≽L2.<br>If<br>L1<br>and<br>L<br>then<br>L1                  |       |
| Axiom 3: | Continuity                                                                | (4.5) |
|          | ≽L<br>≽<br>π,<br>For<br>L1<br>L2<br>and some probability                  |       |
|          | ∼<br>−<br>πL1<br>(1<br>π)L2<br>L<br>+<br>holds.                           |       |
| Axiom 4: | Independence                                                              |       |
|          | ∼L2<br>π,<br>For<br>L1<br>and any probability                             |       |
|          | −<br>π)L∼<br>−<br>πL1<br>πL2<br>π)L<br>+<br>(1<br>+<br>(1<br>holds.       |       |

Axiom 1 ensures that every two lotteries can be pairwise related to each other. This is an obvious requirement. Axiom 2 rules out circular preferences as in Example 4.2. The true meaning of Axiom 3 is not immediately evident; it rules out lexicographical preferences. This is a highly technical issue, just think of it as a mechanism for adding linear and smooth transitions between different preference levels. Axiom 4 prevents any preference relation from bias due to mixing with another lottery. The last axiom has been subject to intense discussion. A slight modification leads to Yaari's dual theory of choice (Yaari, 1987), which is an alternative decision system that is very popular in actuarial science.

Von Neumann and Morgenstern were able to prove a remarkable fact: If the axioms (4.5) hold, then there exists a real function *u* :W → R, such that for *L*<sup>1</sup> and *L*<sup>2</sup> the equivalence

$$L_1 \gtrsim L_2 \quad \Leftrightarrow \quad \sum_{n=1}^N u(w_n) p_n \ge \sum_{n=1}^N u(w_n) q_n \tag{4.6}$$

holds. *u*(*w*) is called the utility function. The functional

$$U[L] = E[u(W)] = \sum_{n=1}^{N} u(w_n) p_n \tag{4.7}$$

is called the *von Neumann–Morgenstern*-utility or expected utility. It is indeed a functional, because it is the expectation value of a function of *W*.

With expected utility we are now in a position to compare whole lotteries in a quantitative way. This is progress, because we no longer need an extensive list of pairwise preference relations of an agent. Instead a neat table of numbers, one for each lottery, suffices. But keep in mind that expected utility is not a global entity. Every rational agent comes with her own utility function *u*(*w*), which is a kind of utility kernel of the *von Neumann–Morgenstern*-functional *U*[*L*]. Furthermore, there is an ambiguity in the utility function. Take the affine transformation

$$v(w) = au(w) + b,\t(4.8)$$

with *a*, *b* ∈ R and *a* > 0. Then the preference order, generated by *U*[*L*] and *V*[*L*] is identical. For all practical purposes this ambiguity is an advantage, because it creates additional degrees of freedom in scaling and translation of *u*(*w*).

# **Example 4.3**

Stick to the credit alternatives in Example 4.1. If you had the utility function *u*(*w*) = *w*, how would you decide?

## Solution

Calculating the expected utility yields

$$U[L_1] = 0 \cdot \frac{1}{2} + 2 \cdot 0 + 4 \cdot \frac{1}{2} = 2$$
  
$$U[L_2] = 0 \cdot 0 + 2 \cdot \frac{9}{10} + 4 \cdot \frac{1}{10} = \frac{11}{5}.$$

Thus, you would prefer to give the loan to customer two. ........................................................................................................................

## **4.3 Risk Aversion**

Let's consider a rather extreme situation. Imagine, someone offers you participation in a one shot coin flip game for your whole wealth. Call the sum of all your

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

possessions *V*, then the alternatives of participating and not participating in the game can be summarized by W= { 0, *V*, 2*V* } , and the lotteries

$$L_1 = \left(\frac{1}{2}, 0, \frac{1}{2}\right)$$
 and  $L_2 = (0, 1, 0).$  (4.9)

Would you consider participation in that game? I suppose not. The reason is that agents are usually risk averse. The consequences of losing everything you own are far more shocking than doubling your wealth would be beneficial. Let's ask a somewhat strange question. What if you were solely interested in terminal wealth, no matter what risks are associated with a specific lottery, which means *U*[*L*] = *E*[*W*]? In this case, we can immediately conclude

$$U[L_1] = 0 \cdot \frac{1}{2} + 2V \cdot \frac{1}{2} = V \cdot 1 = U[L_2] \quad \Leftrightarrow \quad L_1 \sim L_2. \tag{4.10}$$

You would be indifferent between participating and not participating in the coin flip game. But this is a special case of expected utility (4.7) with utility function *u*(*w*) =*w*, see Figure 4.1 left.

**Quick calculation 4.2** Convince yourself that the last statement is true.

Because the risk dimension is completely ignored, the utility function *u*(*w*) = *w* is said to belong to a risk-neutral agent. We can reverse the logic of this conclusion to conjecture that risk attitude has to be encoded in the shape of the utility function. Let's push this idea a little bit further and ask, what sensible shape should a generic utility function have? First of all, more is better than less and thus the slope of *u*(*w*) should be positive. But what about the marginal utility? Does \$1000 increase your utility if you already own \$10 million in the same way as if you own \$200? Suppose not, at least you should not draw more utility from the additional \$1000 if you are a

![](_page_4_Figure_8.jpeg)

**Fig. 4.1** Risk-neutral utility function *u*(*w*) = *w* (left) and concave utility function *u*(*w*) = 2*w* 1+2*w* (right)

millionaire already. That is to say that the increase in marginal utility should not be positive. We can summarize these requirements formally

$$\frac{du}{dw} > 0 \quad \text{and} \quad \frac{d^2u}{dw^2} \le 0. \tag{4.11}$$

If a utility function obeys  $(4.11)$ , it is called concave. If the second inequality holds strictly, it is called strictly concave. A risk-averse agent has a strictly concave utility function. Let's see if we can build some intuition for the last claim. Figure 4.1 right shows such a concave utility function. It is easy to see that in this case the condition

$$u(E[W]) \ge E[u(W)] \tag{4.12}$$

holds strictly. Equation  $(4.12)$  is known as Jensen's inequality for concave functions. If  $u(w)$  is strictly concave, the inequality also holds strictly. Jensen's inequality merely describes what we loosely defined as risk aversion, namely the asymmetric gain or loss in utility of a symmetric gain or loss in wealth.

**Quick calculation 4.3** Verify that for  $u(w) = w$  equality has to hold in (4.12).

We can now understand better, why we were reluctant about participating in the coin flip game. The gain in utility from winning is not as high as the loss of utility, if the unfavorable outcome occurs. Thus, the expected utility over all outcomes of the game is lower than our current utility. We therefore refuse participation and call the reason risk aversion.

## 4.4

## Measures of Risk Aversion

There is a useful measure of the degree of risk aversion an agent exhibits. It was suggested independently by John Pratt (1964) and Kenneth Arrow (1965), and it is called the absolute risk aversion  $(ARA)$ 

$$ARA(w) = -\frac{u''(w)}{u'(w)},$$
(4.13)

where we have used  $u'$  and  $u''$  as shorthand for the first and second derivative of u with respect to its argument. For concave utility functions, the restriction  $u''(w) \le 0 < u'(w)$ holds and thus  $ARA(w) \ge 0$ , where equality holds for the risk-neutral agent.

There is another version of the *Pratt–Arrow*-measure, scaling risk aversion by the current level of wealth of an individual agent. It is called relative risk aversion (RRA)

$$\text{RRA}(w) = -\frac{w \cdot u''(w)}{u'(w)}.\tag{4.14}$$

For *w*> 0, the condition RRA(*w*) ≥ 0 is also satisfied for concave utility functions. Both coefficients sum up the properties of a given utility function in a neat way.

**Example 4.4**

Consider Bernoulli's utility function

*u*(*w*) = log*w*.

What are the *Pratt–Arrow*-coefficients and what do they mean?

Solution

Calculating the derivatives of log*w* yields

$$ARA(w) = \frac{1}{w}$$
 and  $RRA(w) = 1$ .

Obviously, absolute risk aversion decreases with increasing levels of wealth. This is intuitively sensible; think of gaining or losing \$1000 if you are either poor or already a millionaire. Relative risk aversion tells us that absolute risk aversion decreases proportionally to the increase in wealth, with a constant proportionality factor of one. ........................................................................................................................

## **4.5 Certainty Equivalent and Risk Premium**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • Let's ask the following question: Offered the participation in our coin flip lottery, is there a particular wealth level *w* ∗ , such that

$$E[u(W)] = u(w^*)?$$
 (4.15)

In fact there is and its existence is an immediate consequence of the continuity axiom.

**Quick calculation 4.4** Can you see why?

The wealth level *w* ∗ is called the certainty equivalent for obvious reasons. Let's try to find out a bit more about it. For a risk-averse agent, we have from Jensen's inequality and (4.15)

$$u(E[W]) > E[u(W)] = u(w^*). \tag{4.16}$$

Furthermore, because the utility function is strictly monotonic increasing in its argument,

$$E[W] > w^* \tag{4.17}$$

has to hold. In other words, the certainty equivalent wealth level is lower than the expected wealth of the lottery. The risk-averse agent is willing to give up some wealth to avoid uncertainty. The difference between expected wealth and the certainty equivalent is called the risk premium π,

$$E[W] = w^* + \pi. \tag{4.18}$$

Figure 4.2 illustrates the certainty equivalent and the risk premium for the coin flip example. Of course both concepts are not limited to symmetric lotteries with only two random outcomes, but are completely general.

It is often the case that random fluctuations are rather small and the random variable can be expressed in terms of its expectation value, plus a small random error,

$$W = \mu + \epsilon,\tag{4.19}$$

with *E*[ϵ] = 0 and Var[ϵ] =σ 2 . If the random error ϵ is small compared to the expectation value µ, then the risk premium will also be small, and we can use the approximation

$$\pi \approx \frac{1}{2} \text{ARA}(\mu) \sigma^2. \tag{4.20}$$

It is a nice exercise to prove (4.20). From the definition of the risk premium and the certainty equivalent, we have *w* <sup>∗</sup> = µ − π and

$$E[u(W)] = u(w^*) = u(\mu - \pi). \tag{4.21}$$

![](_page_7_Figure_12.jpeg)

**Fig. 4.2** Risk-averse utility function – Certainty equivalent and risk premium

We will now *Taylor*-expand both sides of (4.21) around µ and equate the results. Let's start with the left hand side

$$E[u(W)] = u(\mu) + u'(\mu)E[\epsilon] + \frac{1}{2}u''(\mu)E[\epsilon^2] + O(\epsilon^3)$$
  
 
$$\approx u(\mu) + \frac{1}{2}u''(\mu)\sigma^2.$$
 (4.22)

Note that if ϵ is distributed symmetrically, then *E* [ ϵ 3 ] = 0 and the approximation is exact up to order O ( ϵ 4 ) .

**Quick calculation 4.5** What is the fourth order expansion term if ϵ ∼ *N*(0, σ<sup>2</sup> )?

Expanding the right hand side of (4.21), we restrict ourselves to a linear approximation, because π is expected to be small so that terms of order O ( π 2 ) can be neglected. We obtain

$$u(\mu - \pi) \approx u(\mu) - u'(\mu)\pi.$$
 (4.23)

Equating (4.22) and (4.23), and solving for π yields

$$\pi \approx -\frac{1}{2} \frac{u''(\mu)}{u'(\mu)} \sigma^2 = \frac{1}{2} \text{ARA}(\mu) \sigma^2, \tag{4.24}$$

which is the desired result.

# **4.6 Classes of Utility Functions**

There are several standard classes of utility functions we will briefly discuss in this section, along with some of their characteristic properties. Often utility functions are categorized by their relation to the *Pratt–Arrow*-measure of risk aversion.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

## **4.6.1 Constant Absolute Risk Aversion (CARA)**

There is one class of utility functions, also referred to as exponential utility, that experiences no shift in absolute risk aversion, no matter how small or large the wealth *w* becomes. It has the generic form

$$u(w) = -e^{-\alpha w}.\tag{4.25}$$

Remember that utility functions are only uniquely determined up to an affine transformation. Thus, scaling or translating (4.25) makes no difference and we omit the additional parameters. Exponential utility is very pleasant from a mathematical point of view. For example, realize that the *n*-th derivative of (4.25) is

$$u^{(n)}(w) = (-\alpha)^n u(w). \tag{4.26}$$

Thus, the *Pratt–Arrow*-coefficients can be computed easily,

$$ARA(w) = \frac{\alpha^2 u(w)}{\alpha u(w)} = \alpha \quad \text{and} \quad RRA(w) = \alpha w. \tag{4.27}$$

Now the name of this class of utility functions makes perfect sense. Observe that we pay for the simple analytic form in terms of questionable economic implications. In Example 4.4 we advanced the sensible economic argument that absolute risk aversion should decrease with increasing wealth. The CARA-class fails in this regard. Nevertheless, it may be a good local approximation of the true utility function.

## **4.6.2 Hyperbolic Absolute Risk Aversion (HARA)**

A utility function belongs to the HARA-class, if its absolute risk aversion has the form

$$ARA(w) = -\frac{u''(w)}{u'(w)} = \frac{1}{aw+b},$$
(4.28)

for *a*, *b* ∈ R and *a* > 0. Equation (4.28) is a second order differential equation in *u*(*w*). Thus, we can expect the general solution to have two arbitrary constants, corresponding to the freedom of scaling and translation. A particular solution to the problem is

$$u(w) = \frac{(w+\beta)^{1-\gamma} - 1}{1-\gamma}.$$
 (4.29)

**Quick calculation 4.6** Verify that this solution fulfills (4.28) with *a* = 1 γ and *b* = β γ .

Computing the derivatives of (4.29) with respect to *w*, one obtains

$$\text{ARA}(w) = \frac{\gamma}{w + \beta} \quad \text{and} \quad \text{RRA}(w) = \frac{\gamma w}{w + \beta}.$$
 (4.30)

**Quick calculation 4.7** Convince yourself that (4.30) is consistent with our economic intuition.

There is a special case, when β = 0, that is often called constant relative risk aversion (CRRA), because the *Pratt–Arrow*-coefficient becomes

$$\mathbf{RRA}(w) = \gamma. \tag{4.31}$$

HARA-utility is the dominant paradigm in economics. It is on the one hand flexible enough to accommodate many standard assumptions, and on the other hand sufficiently tractable, to allow analytical solutions for a large number of problems.

## **4.6.3 Quadratic Utility**

Quadratic utility is really only a local approximation to the true, but most of the time unknown utility function. It has the simple form

$$u(w) = -(\eta - w)^2, \tag{4.32}$$

where η is called the bliss point, and (4.32) does only make sense for *w*< η.

## **Quick calculation 4.8** Can you see why?

The *Pratt–Arrow*-measures are easily computed as

$$ARA(w) = \frac{1}{\eta - w} \quad \text{and} \quad RRA(w) = \frac{w}{\eta - w}.$$
 (4.33)

Because absolute risk aversion increases as wealth increases towards the bliss point, we can conclude that quadratic utility has a false built-in economic mechanism. However, it tells us something about the attitude of economic agents towards expected wealth and uncertainty; see Problem 4.6 at the end of this chapter.

## **4.7 Constrained Optimization**

Frequently, we have to optimize an objective function, like for example a utility function, with respect to some restrictions, like budget constraints or something similar. This is usually done with Lagrange's method, which is an ingenious trick to translate a constrained optimization problem in given dimensions into a higher-dimensional unconstrained problem. This is profound progress, because dimensionality is much easier to handle than constraints.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Suppose there are two different consumer goods and we want to maximize our utility function *u*(*c*1, *c*2), where *c*<sup>1</sup> and *c*<sup>2</sup> are the quantities of both commodities to be consumed. Because we do not have unlimited funds, we are subject to a budget constraint *h*(*c*1, *c*2) of some kind. If our current wealth is *w*, we have to solve the problem

$$\max_{c_1, c_2} u(c_1, c_2) \quad \text{subject to} \quad h(c_1, c_2) = w. \tag{4.34}$$

Lagrange's trick is to invent a new function, the *Lagrange*-function

$$\mathcal{L}(c_1, c_2, \lambda) = u(c_1, c_2) + \lambda(w - h(c_1, c_2)), \tag{4.35}$$

that can instead be analyzed without constraints. The only price to pay is that we have an additional variable λ, called the *Lagrange*-multiplier. So let's see if we can understand why this marvelous trick works.

First of all, let's be a little more specific about the utility function and the budget constraint. Suppose we have

$$u(c_1, c_2) = \sqrt{c_1 c_2}$$
 and  $h(c_1, c_2) = p_1 c_1 + p_2 c_2,$  (4.36)

with commodity prices *p*<sup>1</sup> and *p*2.

**Quick calculation 4.9** Verify that the utility function is of the HARA-type.

![](_page_11_Figure_1.jpeg)

**Fig. 4.3** 3D Utility maximization problem with different budget constraint slices

The linear budget constraint in (4.36) is typical for economic problems. What it says is that we have no volume discount of any kind. Figure 4.3 illustrates this optimization problem for different budget constraint slices. Lagrange's method is by no means limited to linear constraints. Indeed it can easily deal with several nonlinear constraints, but for every additional one, we get another *Lagrange*-multiplier. The key in understanding the *Lagrange*-formalism is the gradient. For an arbitrary function *f*(*x*1, . . . , *xN*) it is defined by

$$\nabla f = \left(\frac{\partial f}{\partial x_1} \dots \frac{\partial f}{\partial x_N}\right). \tag{4.37}$$

In differential geometry, the gradient is the archetypical form (co-vector). You should recognize that this expression is identical with the functional derivative with respect to a vector. In this case, the utility function would represent a nonlinear functional of the consumption vector |*c*⟩. But on the other hand, we could understand the budget constraint as linear functional

$$h[|c\rangle] = \langle p|c\rangle. \tag{4.38}$$

Therefore, we can immediately conclude that ∇*h* = ⟨*p*|. Figure 4.4 shows a curve of constant utility and the budged constraint for the functions (4.36). Furthermore, the gradients of *u*(*c*1, *c*2) at the specific intersection points are indicated. Utility increases the more we proceed to the top right corner. That is why the situation in the left illustration is not optimal. A higher level of utility can still be attained without leaving the budget constraint. In Figure 4.4 right, the utility maximum is realized, because we cannot shift the utility curve any further in the "north-east" direction, without detaching it from the budget constraint. To declutter the illustration, we have not indicated the gradient of *h*(*c*1, *c*2), but its corresponding vector |*p*⟩ instead. The information contained in it, with respect to direction and magnitude, is the same, only the graphical representation changes. There is one crucial and by no means accidental fact to be observed: In the optimum, both gradients point exactly in the same direction. To make this observation even more precise: The gradients are perfectly aligned at the optimum, but they do

![](_page_12_Figure_1.jpeg)

**Fig. 4.4** Utility isoquants (gray) and budget constraint (black) – Suboptimal solution with misaligned gradients (left) and utility maximum with aligned gradients (right)

not necessarily have the same magnitude. This is a necessary first order condition for an optimum in the constrained problem (4.34). In our specific case (4.36), it is quite obvious from Figure 4.3 that this condition is also sufficient, because there are no minima or saddle points to worry about in each particular budget constraint slice.

Let's return to the *Lagrange*-function and analyze its first order conditions a little bit. For an unconstrained optimization problem, it is necessary that the gradient in the optimum vanishes. This is the analogue of a vanishing derivative for functions of one variable. So let's see what we get componentwise

$$\frac{\partial \mathcal{L}}{\partial c_n} = \frac{\partial u}{\partial c_n} - \lambda \frac{\partial h}{\partial c_n} \stackrel{!}{=} 0,\tag{4.39}$$

for *n* = 1, 2. If we rearrange and accumulate the components into a form, we get

$$\nabla u \stackrel{!}{=} \lambda \cdot \nabla h. \tag{4.40}$$

This is precisely the necessary condition we observed earlier, namely that the gradients have to coincide, up to a scale factor. This scale factor is the *Lagrange*-multiplier λ.

**Quick calculation 4.10** Compute the specific form of ∇*u* for (4.36).

But we still have one more condition from the *Lagrange*-function

$$\frac{\partial \mathcal{L}}{\partial \lambda} = w - h(c_1, c_2) \stackrel{!}{=} 0. \tag{4.41}$$

Obviously, this one reproduces the original constraint as necessary condition for an admissible optimum

$$h(c_1, c_2) \stackrel{!}{=} w. \tag{4.42}$$

![](_page_13_Figure_1.jpeg)

**Fig. 4.5** 3D *Lagrange*ian contour shells with four-dimensional saddlepoint in the mid shell

Now we can see exactly why Lagrange's trick works. The function L(*c*1, *c*2, λ) is chosen in such a way that

$$\nabla \mathcal{L} \stackrel{!}{=} \langle 0| \tag{4.43}$$

reproduces all necessary conditions for an optimum in the original constrained problem. To emphasize it once more, even though we focused on a rather simple example to explain the *Lagrange*-formalism, the method is completely general and all arguments carry over to such general situations.

There is however one important subtlety. The first order condition (4.43) does not correspond to an optimum in the *Lagrange*-function, but to a saddlepoint. In our toy example (4.36), this is easily seen for vanishing commodity inputs

$$\mathcal{L}(0,0,\lambda) = \lambda w. \tag{4.44}$$

For *w*> 0, the *Lagrange*-function is not bounded, but there are stationary points, where the gradient vanishes. The situation is illustrated in Figure 4.5 for *p*<sup>1</sup> = 1, *p*<sup>2</sup> = 2, and *w* = 2. Because a four-dimensional graph cannot be plotted directly, different surface shells of constant function value are drawn, where the *Lagrange*-function increases in going from the outer to the inner shells. The saddlepoint is located on the mid shell, where the entire surface contracts to a single point. To decide whether or not this point constitutes a minimum or maximum in the original constrained optimization problem, one may analyze the bordered *Hess*ian of the *Lagrange*-problem (for details see Chiang and Wainwright, 2004, sect. 12.3). Fortunately, the structure of common problems in economics and finance often determines the nature of the stationary point beforehand. In our example it was immediately obvious that the first order conditions can only be associated with a maximum in the utility function, because *u*(*c*1, *c*2) is monotonically increasing in both arguments, and solely limited by the budget constraint.

# **4.8 Further Reading**

The classical reference to this subject is von Neumann and Morgenstern (1953). A comprehensive introduction is provided in Resnik (1987). Alternative decision theories have been advanced among others by Kahneman and Tversky (1979); Machina (1982); Quiggin (1982), and Yaari (1987). Measures of risk aversion were introduced by Pratt (1964) and Arrow (1965). For known paradoxes of expected utility, see for example Allais (1953); Ellsberg (1961), or Rabin (2000). A comprehensive introduction to optimization techniques in economics and finance is Chiang and Wainwright (2004).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

# **4.9 Problems**

**4.1** The St. Petersburg paradox is a coin flip game, where a fair coin is tossed successively, until heads occurs. If the first toss is heads, you win \$1. If the first one is tails and the second one is heads, you win \$2. If the first heads occurs in the third toss, you win \$4 and so forth. The amount of money you win is doubled with each coin flip you survive. In the eighteenth century it was believed that the fair price for participating in such a game would be the expected wealth you gain. Show that the expectation value of the St. Petersburg game is infinite.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

**4.2** Daniel Bernoulli was the first to suggest a kind of expected utility of wealth as a solution to the St. Petersburg paradox of Problem 4.1. He used logarithmic utility

$$u(w) = \log w.$$

Show that the expected utility of the St. Petersburg game is indeed finite and that the certainty equivalent is *w* <sup>∗</sup> = \$2. Use that

$$\sum_{n=0}^{\infty} \frac{n}{2^n} = 2.$$

- **4.3** Suppose you own wealth *w* and you are facing a potential loss *l* that may occur with probability *p*. There is an insurance company that offers protection against an arbitrary loss η at an actuarial fair price *p*η. Assume you are risk averse; which amount η <sup>∗</sup> would you insure under expected utility maximization?
- **4.4** For the special class of utility functions *u*(*w*) = *w* − *be*<sup>−</sup>*aw*, with *a*, *b* > 0, Bell (1988) suggested another measure of risk aversion. For this class, expected utility takes the form

$$E[u(W)] = E[W] - bE[e^{-aw}]$$
  
= 
$$E[W] - be^{-aE[W]} \cdot E[e^{-a(W - E[W])}],$$

where the product on the right hand side contains a scaling factor *be*<sup>−</sup>*aE*[*W*] and Bell's risk aversion term. Show that

$$E\left[e^{-a(W-E[W])}\right]$$

does not only take the variance into account, but all higher central moments *M<sup>k</sup>* of the probability distribution of *W*.

- **4.5** Show that hyperbolic absolute risk aversion with β = 0, in the limit γ → 1 specializes to Bernoulli's logarithmic utility.
- **4.6** Assume the random variable *W* has expectation value *E*[*W*] = µ and variance Var[*W*] =σ 2 . Mean variance analysis postulates that expected utility increases with increasing µ, and decreases with increasing σ 2 . Show that quadratic utility coincides with these postulates.
- **4.7** Assume that the commodity prices in the optimization problem (4.34) with (4.36) are *p*<sup>1</sup> = 1 and *p*<sup>2</sup> = 2. Show that in the optimum *u*(*c* ∗ 1 , *c* ∗ 2 ) = *w*√ 8 holds.
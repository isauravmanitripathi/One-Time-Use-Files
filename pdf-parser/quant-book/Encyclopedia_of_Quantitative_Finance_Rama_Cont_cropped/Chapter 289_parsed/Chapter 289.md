# **Behavioral Portfolio Selection**

Behavioral portfolio selection is the study of how psychology impacts investors' portfolio choices. These choices pertain to the manner in which investors structure the risk-return composition of their portfolios and modify their portfolios over time through the buying and selling of securities.

The key behavioral features about portfolios include a dual emphasis on very safe and very risky securities, a lack of full diversification, excessive trading, the salience of securities that are purchased for the portfolio, and the disposition to sell winners too early but ride losers too long.

The theoretical framework underlying behavioral portfolio selection draws on the following four elements in the literature in behavioral decision making: (i) *SP/A* theory; (ii) prospect theory; (iii) regret and self-control; and (iv) heuristics and biases. Notably, the first three elements pertain to risk preferences, while the fourth deals with erroneous judgments about risk.

All four elements involve departures from the neoclassical mean-variance approach to portfolio selection. In the neoclassical approach, investors are rational in two senses. First, their preferences conform to the axioms of expected utility, where utility is defined over total return (or wealth) and risk is measured in terms of return standard deviation. Second, their judgments about risk and return are free of error. By way of contrast, in the behavioral approach, preferences typically violate the axioms of expected utility, investors attach importance to other variables besides total return (or wealth), investors do not measure risk in terms of return standard deviation, and investors make erroneous judgments about the risks they face.

In the mean-variance approach, investors hold well-diversified portfolios that feature risk and return being rationally balanced against each other. In the behavioral approach, investors are imperfectly rational, and in the course of attempting to make the best portfolio decisions they can, they adopt piecemeal approaches to portfolio selection that leave them holding undiversified portfolios.

## **Theoretical Foundations**

#### *SP/A Theory*

Lopes [9] developed a psychologically based approach known as *SP/A theory* to explain choice among risky alternatives. She titled her 1987 article "The Psychology of Risk: Between Hope and Fear" to capture the idea that the emotions of hope and fear play key roles in choice among risky alternatives. In this respect, the letters that make up *SP/A* refer to specific concepts that measure or impact the degree of fear or hope experienced by a decision maker. Notably, *S* stands for security, *P* stands for potential, and A stands for aspiration.

In order to describe Lopes' formal framework, consider some notation. Denote the set of possible outcomes by a finite set of real numbers *X* = {*x*1*,...,xn*}, ordered from the lowest outcome *x*<sup>1</sup> to the highest *xn*. Formally, a risky alternative or prospect is a random variable that takes on values in *X*. One way to describe the probabilities attached to a random variable is to use a decumulative distribution function *D*, where *D(x)* is the probability that the outcome payoff is at least *x*. The same probabilistic information is also conveyed by the cumulative distribution function, which measures the probability that the outcome payoff is no greater than *x*, or the probability density function, which measures the probability that the outcome payoff is exactly *x*.

In a typical decision task, a decision maker chooses a best alternative from a menu {*D*} of risky alternatives. The role of the theory is to describe the criteria leading to the choice. In *SP/A* theory, risky alternatives are evaluated using an objective function whose arguments reflect security *S*, potential *P*, and aspiration *A*.

Roughly speaking, increased fear stems from reduced security and reduced security corresponds to an increase in the probability attached to the occurrence of some unfavorable event. Suppose we consider two decision makers who face an identical risk, or prospect *D*, but experience different degrees of fear. Intuitively, the decision maker who experiences more fear attaches greater importance to the probability associated with unfavorable events than the decision maker who experiences less fear.

Formally, Lopes uses rank-dependent utility to capture the effects of fear. In rank-dependent utility, a decision maker who faces a risky prospect *D*

acts as if the decumulative density function is the transform *h(D)* rather than *D* itself. In *SP/A* theory, fear operates on the probabilities associated with unfavorable events. Because *D* is a decumulative distribution function, the probability attached to the least favorable event *x*<sup>1</sup> is given by Prob{*x*1} = *D(x*1*)* − *D(x*2*)*.

Under the transform *h(D)*, the probability attached to the least favorable event *x*<sup>1</sup> is given by Prob{*x*1} = *h(D(x*1*))* − *h(D(x*2*))*. In Lopes' framework, a decision maker who is fearful about exposure to event *x*<sup>1</sup> overweights the probability attached to *x*1. That is, the fearful decision maker employs a transform *h* that satisfies

$$h(D(x_1)) - h(D(x_2)) > D(x_1) - D(x_2) \tag{1}$$

Because *x*<sup>1</sup> is the least favorable outcome, the probability that the actual outcome turns out to be *x*<sup>1</sup> or higher is 1. In other words, *D(x*1*)* = 1. What equation (3) effectively states is that increased fear leads to an increase in the slope of the *h*-function in the neighborhood of 1.

Rank-dependent utility also captures the manner in which the decision maker experiences hope. Hope is associated with upside potential, or potential for short. Hope induces a decision maker to attach greater weight to the most favorable events. Because *D* is a decumulative distribution function, the probability attached to the most favorable event *xn* is given by Prob{*xn*} = *D(xn)*. Therefore, the emotion of hope leads a decision maker to employ a transform *h* that satisfies *h(D(xn)) > D(xn)*. For the second most favorable outcome, the corresponding inequality would read as

$$h(D(x_n)) - h(D(x_{n-1})) > D(x_n) - D(x_{n-1}) \quad (2)$$

This inequality indicates that increased hope leads to an increase in the slope of the *h*-function in the neighborhood of 0.

In Lopes' framework, a person who neither experiences fear nor hope is associated with an *h*-function that is the identify function: *h(D)* = *D*. A decision maker who experiences only fear, but not hope, is associated with an *h*-function that is strictly convex in *D*: it is steep in the neighborhood of 1 and flat in the neighborhood of 0. Formally, Lopes uses a power function *hS (D)* = *D<sup>q</sup>* , *q >* 1 for this case. A decision maker who experiences only hope is associated with an *h*-function that is strictly concave in *D*. Formally, Lopes uses a power function *hP (D)* = 1 − *(*1 − *D)p*, *p >* 1 for this case. A person who experiences both fear and hope is associated with an *h*-function that has an inverse-S shape. It is concave in the neighborhood of the origin and convex in the neighborhood of 1. Formally, Lopes uses a convex combination of the power functions *hS* and *hP* to capture this case.

In *SP/A* theory, the degree to which fear and hope are experienced depends on the degree to which risky prospects offer security *S* and potential *P*. To capture the impact of both security and potential, Lopes uses an expected utility function with probabilities derived from the *h*-transform. She calls the function *SP* for security–potential, and it has the form

$$SP = \sum_{i=1}^{n} (h(D_i) - h(D_{i+1}))u(X_i) \qquad (3)$$

In equation (1), *u* is a utility function whose argument is outcome *x*. Although Lopes uses the assumption *u(x)* = *x* in most of her analysis, Lopes and Oden [10] comment that, in practice, *u* might display a bit of concavity.

The *A* in *SP/A* denotes aspiration. Aspiration pertains to a target value *α* (or range) to which the decision maker aspires. Aspiration points reflect different types of goals. For example, a decision maker might wish to generate an outcome that would allow the purchase of a particular good or service. Alternatively, the aspiration point might reflect a status quo position that corresponds to the notion of no gain or loss. In Lopes' framework, aspiration risk is measured as the probability 1-A where *A* = Prob{*x* ≥ *α*} that the random outcome *x* meets or exceeds the aspiration level *α*.

In *SP/A* theory, the decision maker maximizes an objective function *V* (*SP*,*A*) in deciding which alternative *D* to choose from the menu of available prospects. *V* is strictly monotone increasing in both of its arguments. Therefore, there are situations in which a decision maker is willing to trade off some *SP* in exchange for a higher value of *A*.

#### *Prospect Theory*

Prospect theory is a theory of choice developed by psychologists Kahneman and Tversky [5]. Prospect theory has four distinctive features.

First, the carriers of utility are changes, meaning gains and losses relative to a reference point, not the final position.

Second, the utility function (known as a *value function* in prospect theory) is concave in gains and convex in losses, with a point of nondifferentiability at the origin so that the function is more steeply sloped for losses (to the left of the origin) than for gains (to the right of the origin). Hence, the utility function is S-shaped with a kink at the origin. Tversky and Kahneman [16] suggest using a utility function *u(x)* with the form *x<sup>α</sup>* in the domain of gains (*x* ≥ 0) and −*λ(*−*x)β* in the domain of losses (*x* ≤ 0).

Third, probabilities are weighted (or distorted) when prospects are evaluated. In the original 1979 version of prospect theory (original prospect theory OPT), the weighting function *π* has probability density *p* as its argument. The *π*-function in OPT is convex, with *π(p) > p* for small positive values of *p* and *π(p) < p* for high values of *p* less than 1. In 1992, Tversky and Kahneman [16] proposed a cumulative version of prospect theory (cumulative prospect theory CPT) that uses rank-dependent utility. Unlike OPT, where probability weights depend only on probability density, the weights in CPT depend on outcome rank.

Tversky and Kahneman [16] use two weighting functions, one function for gains and one function for losses. Both functions take decumulative probabilities as their arguments, where the decumulative distribution pertains to the absolute value of the gain or loss, respectively. The weighting function is similar to the *h*-transform used by Lopes. It features an inverse S-shape, which Tversky–Kahneman generate using the ratio of a power function to a Holder aver- ¨ age; that is, *p<sup>γ</sup>* /*(p<sup>γ</sup>* + *(*1 − *p)γ )*<sup>1</sup>*/γ* . As a result, in CPT, it is the probabilities of extreme outcomes that are overweighted (very large losses and very large gains).

Both the S-shape of the utility function and the inverse S-shape of the weighting functions reflect psychophysics, meaning the diminished sensitivity to successive changes. For the utility function, the changes pertain to differences relative to the reference point. For the weighting function, the changes pertain to differences relative to the endpoints 0 and 1.

Fourth, decision makers engage in editing or framing before formally evaluating risky prospects. There are several types of editing issues. Perhaps the simplest editing issue is the choice of reference point. Kahneman and Tversky illustrate this issue by describing a medical task in which the data can be presented, or framed, in one of two ways. The first way is in terms of lives saved, while the second way is in terms of lives lost. The "lives saved" frame implicitly sets the reference point at 100% fatalities. The "lives lost" frame implicitly sets the reference point at 0% fatalities. Although the data underlying the two frames is identical, physicians tend to act as if they are more risk averse when presented with the data framed in terms of "lives saved" than when the data is framed in terms of "lives lost". This choice pattern is consistent with the S-shaped utility function.

A more complex framing issue is the segmentation of a complicated decision task into a series of subtasks. The structure of each subtask is called a *mental account* and the segmentation process is known as *narrow framing*. Because narrow framing tends to overlook interdependencies between mental accounting structures, the segmentation process is often suboptimal. Tversky and Kahneman present examples in which narrow framing leads to the selection of stochastically dominated choices.

Prospect theory is a descriptive framework, not a normative framework. People who choose stochastically dominated alternatives do so because they do not always grasp the complete structure of the decision tasks they confront. The complete structure is typically opaque, not transparent, and people lack the ability to frame complex decision tasks transparently.

#### *Regret and Self-control*

In the early development of prospect theory, Kahneman and Tversky focused on the role of regret. Regret is the psychological pain associated with recognizing after the fact that taking a different decision would have produced a better outcome. Kahneman *et al.* [7] eventually built prospect theory using the S-shaped value function, but in their 1982 work they continued to emphasize the importance of regret. They pointed out that regret will be magnified by the ease with which a person can imagine taking a different decision.

Self-control refers to situations when a person is conflicted, and *thinks* he or she should take one decision, but emotionally *feels* like taking a different decision. Studies of self-control in financial economics tend to emphasize the difficulty in delaying gratification. However, self-control applies more broadly, and in particular applies when the emotion of regret prevents a person from taking a decision that he or she "thinks" is appropriate.

#### *Heuristics and Biases*

The weighting functions in *SP/A* theory and prospect theory reflect the way that people process known probabilistic information. In these theories, people weight probabilities as they do because of emotion (as in *SP/A* theory) or psychophysics (as in prospect theory). In contrast, heuristics and biases involve errors in judgments about the probabilities themselves. A person might know the true probability of winning the lottery but because of hope overweights its value psychologically when deciding whether or not to purchase a lottery ticket. On the other hand, a person who is unrealistically optimistic would tend to overestimate the probability of winning the lottery.

The volume edited by Kahneman *et al.* [6] contains the foundation contributions to the heuristics and biases literature. A heuristic is a crude rule of thumb for making judgments about probabilities, statistics, future outcomes, and so on. A bias is a predisposition toward making a particular judgmental error. The heuristics and biases approach studies the heuristics upon which people rely to form judgments, and the associated biases in those judgments.

Some biases are associated with specific heuristics. Examples of these biases relate to such heuristic principles as availability, anchoring, and representativeness.

Availability is the tendency to form judgments based on information that is readily available, but to underweight information because it is not readily available. For example, a person might underestimate the danger from riptides and overestimate the danger from shark attacks because media stories tend to report most shark attacks but rarely report less dramatic incidents involving riptides. Heuristics and biases associated with availability reflect the importance of salience and attention.

Anchoring is the tendency to formulate an estimate by using a process that begins with an initial number (the anchor) and then making adjustments relative to the anchor. Anchoring bias is the tendency for the associated adjustments to be too small.

Representativeness is the tendency to rely on stereotypes to make a judgment. For example, a person who relies on representativeness might be especially bold in predicting that the future return of a particular stock will be very favorable because its past long-term performance has been very favorable. This is because they form the judgment that favorable past performance is representative of good stocks. However, representativeness leads such predictions to be overly bold, because of insufficient attention to factors that induce regression to the mean.

Although some biases relate directly to specific heuristics, other biases stem from a variety of factors. For example, people tend to be overconfident about both their abilities and their knowledge. People who are overconfident about their abilities overestimate those abilities. People who are overconfident about their knowledge tend to think they know more than they actually do. In particular, people who are overconfident about their knowledge tend to set confidence intervals around their estimates that are too narrow. As a result, they wind up being surprised at their mistakes more often than they anticipate.

Other examples of biases that do not stem directly from specific heuristics are unrealistic optimism and the illusion of control. Unrealistic optimism involves overestimating the probabilities of favorable events and underestimating the probabilities of unfavorable events. The illusion of control is overestimating the role of skill relative to luck in the determination of outcomes.

## **Implications for Portfolio Selection**

#### *SP/A Theory and Portfolio Selection*

Shefrin and Statman [15] use the *SP/A* framework as the basis of behavioral portfolio theory. They develop a model with two dates, *t* = 0 and *t* = 1, in which an investor with initial wealth *W* = 1 chooses a portfolio at *t* = 0. The model is structured so that at *t* = 1 one of *n* possible states will occur, and the subjective probability (density) associated with the occurrence of state *i* is *pi*. The model also features a complete market, meaning that securities are priced in accordance with state prices *υ*1*,...,υn*, where *υi* is the price associated with the delivery of 1 unit of consumption in state *i*.

A portfolio return configuration is given by *x*1*,...,xn* where *xi* denotes the number of units of consumption paid if state *i* occurs. Notice that because *W* = 1*, x*1*,...,xn* are indeed gross rates of return, which are assumed to be nonnegative.

The decision task for investor with *SP/A* preferences is to choose a portfolio return configuration *x*1*,...,xn* to maximize the objective function *V* (*SP*,*A*) subject to the constraint

$$\sum_{i=1}^{n} v_i x_i = 1 \tag{4}$$

The maximization of *V* (*SP*,*A*) for fixed *A* is formally equivalent to a constrained expected utility maximization problem, where the decision weights derived from the *h*-transform are treated like probabilities. The associated constraint is *A* = Prob{*x* ≥ *α*}. The effect of this constraint, when active, is to introduce a flat region *iL* ≤ *i* ≤ *iU* for which *xi* = *α*. Notably, the investor meets the *A*-constraint by fulfilling this constraint from the favorable states down. This can result in three regions: *xn > α*, *xi* = *α* for *iL* ≤ *i* ≤ *iU* , and *xi < α* for *i<iL*, and when *u* is linear *xi* = 0 for *i<iL*. In effect, an *SP/A* portfolio can be thought of as the combination of a risky bond and a call option on a neoclassical portfolio with a high exercise price.

There are two key questions associated with *SP/A* portfolios. First, how do the *h*-function and curvature of the utility function *u(x)* impact the choice of portfolio payoff configuration? Second, how is the return configuration impacted by the values of *α* and *A*?

Lopes suggests that the utility function *u(x)* is mildly concave, although for purposes of exposition she treats it as linear in her discussions. Notably, linearity encourages an investor to concentrate as much wealth as possible on purchasing claims associated with the state featuring the lowest state price per unit probability. This will lead to a lottery property, meaning the small probability of a very large payoff. Concavity in the utility function will dampen the lottery property.

The impact of fear and hope occurs through the *SP* function, where the probabilities associated with the least favorable states and the most favorable states are overweighted. Such overweighting leads to higher returns in extreme states than would occur otherwise, and therefore lower returns in intermediate states.

It is the impact of the *A* variable that makes *SP/A* theory distinct from other psychologically based theories of risk. It should be kept in mind that the investor tends to fulfill the *A*-constraint from the most favorable state down. Increasing the value of *A* leads to a shift in returns from both the most unfavorable states and the most favorable states, where *xi* = *α*, to expand the middle region where *xi* = *α*. If an investor increases the value of *α*, then she also shifts return from the extremes to the middle, but with the purpose of raising the level of the middle region.

*SP/A* theory implies that investors will choose portfolios whose return patterns can be generated by combining a risky bond and a call option on a neoclassical portfolio associated with unconstrained *SP*-maximization.

#### *Prospect Theory and Portfolio Selection*

Two features of prospect theory are particularly germane to portfolio selection, and both involve the manner in which the information underlying the selection task is framed. The first feature is the simplification of the selection task through the use of mental accounts. The second feature is the reference point used to define gains and losses.

The use of mental accounting leads investors to evaluate decisions about securities with little or no reference to other securities in the portfolio. This is in sharp contrast to neoclassical theory, where the value of a security to an investor very much depends on the return covariance of that security with other securities in the portfolio. Mental accounting implies that investors make little if any direct use of the return variance–covariance matrix.

Shefrin and Statman [14] suggest that the most natural reference point for the mental account associated with an individual security is original purchase price. As discussed earlier, the location of a reference point is important because people's attitude toward risk depends critically on whether they view the set of possible outcomes as gains, losses, or a mixture of gains and losses. This feature was first highlighted by Kahneman and Tversky [5], and is shared by *SP/A* theory.

Mental accounting is also associated with investors having a multitude of different goals. In this case, the investor associates a mental account or portfolio layer to a specific goal *α* and associated probability *A*. Downside protection is associated with a low *α* and high probability *A*. Upside potential is associated with a high *α* and associated probability *A* that is as high as feasibility allows.

#### *Regret, Self-control, and Portfolio Selection*

People experience regret when they admit to having made a decision that turned out poorly. When an investor purchases a stock that subsequently performs poorly, the investor is prone to experiencing regret. Shefrin and Statman [14] suggest that the degree of regret is especially high when an investor sells a stock at a loss.

Because there are tax benefits from selling stocks at a loss, many investors who delay tax-loss selling forego potential benefits. In doing so, they pay a price to defer the pain of regret, hoping that the stock will bounce back so that they can avoid selling at a loss. On the flip side, selling a stock for a gain can be a source of pride, even if there is a tax penalty for doing so. In this respect, imperfect self-control can lead investors to sell stocks before their gains become long-term, thereby leading to a higher tax liability. Therefore, regret and imperfect self-control predispose investors to sell winners too early and ride losers too long, a phenomenon that Shefrin and Statman [14] call *the disposition effect*.

The S-shaped utility function in prospect theory implies that decision makers are prone to be risk averse in the domain of gains but risk seeking in the domain of losses. For this reason, prospect theory is the natural starting point for discussing the disposition effect. However, prospect theory does not explain why an investor would knowingly incur an unnecessary tax penalty.

#### *Heuristics, Biases, and Portfolio Selection*

Few, if any, investors have objectively correct knowledge of return distributions. Most investors formulate their beliefs by applying heuristics to the information at their disposal. As such, they are vulnerable to forming biased beliefs.

Biases take many forms. Barber and Odean [2] point out that because of reliance on the availability heuristic, investors tend to place undue stress on stocks that have attracted their attention. They call this phenomenon *the attention hypothesis*. De Bondt and Thaler [3] suggest that individual investors who rely on representativeness are prone to extrapolate past performance with undue weight on the recent past. They call this phenomenon *the overreaction effect*. Shefrin [13] suggests that professional investors who rely on representativeness apply it differently than individual investors and are prone to attach too high a probability to reversals. Odean [11] suggests that overconfidence leads all investors to be overconfident in their beliefs, thereby trading with excessive frequency on unwarranted convictions.

## **Empirical Evidence**

Much of the literature pertaining to behavioral portfolio selection involves the development of hypotheses in theoretical papers followed by other papers which tested these hypotheses.

Polkovnichenko [12] and Kumar [8] provide evidence that supports hypotheses stemming from *SP/A*based portfolio theory. Kumar's work documents that the portfolios of individual investors overweight high-risk stocks, which he calls *lottery stocks*, while the portfolios of professional investors underweight lottery stocks. Polkovnichenko's work characterizes the degree to which the portfolios of individual investors are driven by fear, as reflected in their unwillingness to hold equities. His work also highlights the lack of diversification in most investors' portfolios. Odean [11] documents the degree to which individual investors are prone to the disposition effect, and Frazzini [4] shows that professional investors are also prone. Barber and Odean [2] provide evidence that individual investors purchase stocks by relying on the availability heuristic more so than professional investors. Barber and Odean [1] provide evidence that excessive trading by individual investors harms performance.

## **References**

- [1] Barber, B. & Odean, T. (2000). Trading is hazardous to your wealth: the common stock investment performance of individual investors with Brad Barber, *Journal of Finance* **LV**(2), 773–806.
- [2] Barber, B. & Odean, T. (2008). All that glitters: the effect of attention and news on the buying behavior of individual and institutional investors, *The Review of Financial Studies* **21**(2), 785–818.
- [3] De Bondt, W. & Thaler, R. (1985). Does the stock market overreact? *Journal of Finance* **40**, 793–805.
- [4] Frazzini, A. (2006). The disposition effect and underreaction to news, *Journal of Finance* **41**(6), 2017–2046.

- [5] Kahneman, D. & Tversky, A. (1979). Prospect theory: an analysis of decision making under risk, *Econometrica* **47**(2), 263–291.
- [6] Kahneman, D., Slovic, P. & Tversky, A. (1982). The psychology of preferences, *Scientific American* **246**, 160–173.
- [7] Kahneman, D., Slovic, P. & Tversky, A. (1982). *Judgment Under Uncertainty: Heuristics and Biases*, Cambridge University Press, Cambridge.
- [8] Kumar, A. (2007). *Who Gambles in the Stock Market?* Working paper, University of Texas.
- [9] Lopes, L. (1987). Between hope and fear: the psychology of risk, *Advances in Expermintal Social Psychology* **20**, 255–295.
- [10] Lopes, L.L. & Oden, G.C. (1999). The role of aspiration level in risk choice: a comparison of cumulative prospect theory and *SP/A* theory, *Journal of Mathematical Psychology* **43**, 286–313.
- [11] Odean, T. (1998). Are investors reluctant to realize their losses? *Journal of Finance* **53**(5), 1775–1798.

- [12] Polkovnichenko, V. (2005). Household portfolio diversification: a case for rank-dependent preferences, *The Review of Financial Studies* **18**(4), 1467–1501.
- [13] Shefrin, H. (2005). *A Behavioral Approach to Asset Pricing*, Elsevier Academic Press, Boston.
- [14] Shefrin, H. & Statman, M. (1985). The disposition to sell winners too early and ride losers too long: theory and evidence, *Journal of Finance* **40**(3), 777–790.
- [15] Shefrin, H. & Statman, M. (2000). Behavioral portfolio theory *Journal of Financial and Quantitative Analysis* **35**, 127–151.
- [16] Tversky, A. & Kahneman, D. (1992). Advances in prospect theory: cumulative representation of uncertainty, *Journal of Risk and Uncertainty* **5**, 297–323.

## **Related Articles**

**Ambiguity**; **Expectations Hypothesis**; **Modern Portfolio Theory**; **Risk Aversion**; **Utility Function**.

HERSH SHEFRIN
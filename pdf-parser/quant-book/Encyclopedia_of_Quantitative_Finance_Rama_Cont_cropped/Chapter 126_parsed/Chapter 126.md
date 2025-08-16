# **Altiplano Option**

In the late 1990s, Societe Generale introduced a series of options on baskets of assets that are now commonly referred to as *Mountain Range* options [2]. They were introduced in part to replicate certain portfolio strategies and in part to extend single-name options to portfolios. What these options share is a strong dependence on the correlation structure of the assets, brought about by their nonlinear and pathdependent payoffs. But beyond this similarity, each type has its own distinct payoff tailored to its own risk profile and use, making each deserving of its own study. In this last of three articles on Mountain Range options, we look at the Altiplano option, which can be thought of as an extension of barrier options to baskets.

This article is organized as follows. We first provide a description of the Altiplano option and discuss the financial motivations for and strategies of its usage. We then discuss modeling, valuation, and risk issues that Altiplano options share with all Mountain Range options, and conclude with a brief analysis of the risk profile that is unique to it. We remark that although the following discussion holds for a wide class of assets, such as foreign exchange (FX) and commodities, these options are traded mostly on baskets of stocks.

## **Contract Description**

Like single-name barrier options, Altiplano options have two components—a vanilla-type payoff if a barrier event occurs, and a coupon payoff if it does not. Usually the barrier event is to have at least one stock reach a predetermined barrier.

More precisely, given a portfolio, or a basket of *n* stocks, let *Si(t)* be the price of the stock *i* = 1*,...,n* at time *t*, with 0 being the start of the option and *T* its maturity. The payoff is

$$\max\left(\sum_{i=1}^{n} \frac{S_i(T)}{S_i(0)} - K, 0\right) I_B + (1 - I_B)C \qquad (1)$$

where *IB* is 1 if a barrier event in relation to barrier level *B* occurs, and is 0 if it does not, in which case the option would pay a coupon *C*. Here we have used a call option, but, in principle, we could use any option. As in single-name barriers, there are many possible wrinkles for the barrier event, such as the Parisian type (*see* **Parisian Option**). But unlike a simple extension from the single-name case where the barrier is triggered by the sum of the portfolio, individual assets can trigger the barriers by themselves. In the example above, all it takes is for one asset to activate a barrier, independently of the level of other assets at the time. This makes the Altiplano sensitive to individual asset moves, rather than the collective sum.

As in single-name barriers, since *IB* is always less than 1, the payoff, and thus the risk, are lower than for standard options on baskets, which makes their premiums lower as well (assuming *C* is small or zero). The lower premium makes it more attractive when used as a hedge, for example.

## **Modeling**

In the simplest of implementations, as in single-name options, the asset price processes are modeled as lognormal processes but with a correlation matrix. In more advanced implementations, to account for the volatility smile, some versions of stochastic volatility models are often used. One may even include some form of default component. However, in these more complex models, the modeling of correlation and its estimation become more complex as well.

## **Valuation and Risk**

The number of assets in Mountain Range options generally ranges from a low of 4 or 5 to a high of about 20. Owing to their complex payoff and path-dependency, idiosyncratic characteristics of each asset need to be taken into account. Hence one cannot assume homogeneity of assets for either small or large baskets, making any closed-form approximation (especially in light of path dependence) intractable. As a result, Mountain Range options, specially the path-dependent varieties such as the Altiplano, are calculated using Monte Carlo simulation [1]. Monte Carlo methods, especially for high-dimensional payoffs with large number of assets and time points, are slow to converge, and usually one or more variancereduction techniques are employed. Additionally, since the barrier event is binary, the number of simulation paths needed is even greater than those with continuous payoffs, making first- and second- order Greeks calculations even more noisy. This makes use of variance-reduction methods even more critical.

The other challenge posed by these options is the correlation. Even in the simple lognormal model, the sheer size of the correlation matrix can become a challenge. Since for *n* assets, there can be *n(n* − 1*)/*2 distinct correlations, even for a modest basket of 10 assets, 45 distinct correlations are possible. Moreover, it is not clear how one can obtain the pairwise correlations themselves. If, theoretically speaking, there existed *n(n* − 1*)/*2 traded spread options on each pair, their implied correlations could be used with the spread options as hedges. However, it is unlikely that every pair of assets in a basket would have a traded spread option. Even if they did, their sheer number would make transaction costs prohibitive, even for moderate bid–ask spreads. Hence historical correlations are more often used, even though as with all historical estimates, they are hard to hedge and can change with macro- and microeconomic shifts. When all assets belong to the same sector, a single correlation number is commonly used. This high amount of asset interdependence makes cross-gammas important, adding further to the hedging complexity.

## **Risk Profile**

As in single-asset barrier options, the payoff of an Alitplano option is determined by two competing terms—the option term and the barrier term. Again, for ease of analysis, we look at a homogeneous portfolio with identical pairwise correlations given by a single number in the simple lognormal model with no coupon payout. For a simple call option on a basket, it is known that high correlation and volatility increase its price. For the barrier event, it depends on the type. If it takes only one asset to hit a barrier, then low correlation and high volatility increase the probability of hitting it. Moreover, depending on the barrier, the paths that lead to higher option prices may make the barrier even more or less likely, leading to possible nonmonotonous behavior. So even in this simple homogeneous case with a single correlation, the behavior is rather complex.

## **References**

- [1] Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*, Springer, New York.
- [2] *Mountain Range Options*, document downloadable from global-derivatives.com

## **Related Articles**

**Atlas Option**; **Basket Options**; **Correlation Risk**; **Himalayan Option**.

REZA K. GHARAVI
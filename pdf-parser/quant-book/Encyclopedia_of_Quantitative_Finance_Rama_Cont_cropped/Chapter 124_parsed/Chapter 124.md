# **Atlas Option**

In late 1990s, Societe Generale introduced a series of options on baskets of assets which are now commonly referred to as "Mountain Range" options [2]. They were introduced in part to replicate certain portfolio strategies and in part to extend single-name options to portfolios. What these options share is a strong dependence on the correlation structure of the assets, brought about by their nonlinear and path-dependent payoffs. But beyond this similarity, each type has its own distinct payoff tailored to its own risk profile and usage, making each deserving a study of its own. In a series of three articles, we look at the three commonly traded types of Mountain Range options—the Atlas option, the Himalayan option, and the Altiplano option.

We start with the Atlas option, which being the only non-path-dependent option in this group, is somewhat easier to analyze than the other two. This article is organized as follows. We first provide a description of the Atlas option and discuss the financial motivations for and strategies of its usage. We then discuss modeling, valuation, and risk issues that Atlas options share with all Mountain Range options, and conclude with a brief analysis of the risk profile that is unique to it. We remark that although the following discussion holds for a wide class of assets, such as foreign exchange (FX) and commodities, these options are traded mostly on baskets of stocks.

## **Contract Description**

The payoff of the Atlas option is simply a call (or a put) option on the performance of a portfolio at maturity with the best and worst performing names removed. More precisely, given a portfolio, or basket of *n* stocks, let *Si(t)* be the price of the stock *i* = 1*,...,n* at time *t*, with 0 being the start of the option and *T* its maturity. Furthermore, assume that the indices are such that *S*1*(T )/S*1*(*0*), . . . , Sn(T )/Sn(*0*)*, that is, the performance of the stocks is in increasing order. Given a strike *K*, the number of underperforming assets *w* and outperforming ones *b* to be removed, the payoff of the Atlas option is

$$\max\left(\frac{1}{n - (w+b)}\sum_{i=1+w}^{n-b} \frac{S_i(T)}{S_i(0)} - K, 0\right) \tag{1}$$

with the obvious condition that *b* + *w<n*.

If *b<w*, with *b* possibly 0, or if *b>w* with *w* possibly 0, then this option becomes the best of or worst of option, respectively. On the other hand, if *b* = *w*, with equal number of underperforming and outperforming stocks removed, this option becomes, in effect, a "middle of the road" or an "average of averages" option. By removing the outliers, we are removing extreme risk and lowering the premium, while making it more favorable to risk-averse customers. For example, it can provide protection against defaults for the price of missing out on top performers.

## **Modeling**

In the simplest of implementations, as in single-name options, the asset price processes are modeled as lognormal processes but with a correlation matrix. In more advanced implementations, to account for the volatility smile, some versions of stochastic volatility models are often used. One may even model some form of default component. However, in these more complex models, the modeling of correlation and its estimation become more complex as well.

## **Valuation and Risk**

The number of assets in Mountain Range options generally ranges from a low of 4 or 5 to a high of about 20. Owing to their complex payoff and path-dependency, idiosyncratic characteristics of each asset need to be taken into account. Hence one cannot assume homogeneity of assets for neither small nor large baskets, making any closed-form approximation (especially in light of path dependence) intractable. Consequently, Mountain Range options, even the non-path-dependent Atlas options, are calculated using Monte Carlo simulation [1]. Monte Carlo methods, especially for high-dimensional payoffs with large number of assets, are slow to converge, and usually one or more variance-reduction techniques are employed. This problem is exacerbated further when calculating first and second order Greeks.

But even in the simple lognormal model, the sheer size of the correlation matrix can become a challenge. Since for *n* assets there can be *n(n* − 1*)/*2 distinct correlations, even for a modest basket of 10 assets, 45 different correlations are possible. Moreover, it is not clear how one can obtain the correlation numbers themselves. If, theoretically speaking, there existed *n(n* − 1*)/*2 traded spread options on each pair, their implied correlations could be used with the spread options as hedges. However, it is unlikely that every pair of assets in a basket would have a traded spread option. Even if they did, their sheer number would make transaction costs prohibitive, even for moderate bid–ask spreads. Hence historical correlations are more often used, even though as with all historical estimates, they are hard to hedge and can change with macro- and microeconomic shifts. When all assets belong to the same sector, a single correlation number is commonly used. This high amount of asset interdependence makes cross-gammas (*see* **Gamma Hedging**) important, adding further to the hedging complexity.

## **Risk Profile**

When *w* = *b* = 0, the Atlas option is simply a call option on the average performance of a basket. As in a vanilla call on a single stock, the higher the volatility, the higher the price. But the analysis gets more interesting when we start removing good and bad performers at maturity.

For simplicity, we look at a homogeneous portfolio with identical pairwise correlations given by a single number in a simple lognormal model. For very high correlations, the basket behaves as a single asset—thus removing assets has a small effect on the option payoff. Since it behaves as a single asset, as in single-asset calls, the option's payoff generally increases with volatility.

For low correlations, on the other hand, the basket has a high dispersion at maturity—on average, a few stocks will have a high price and the rest low—and higher the volatility, the higher the dispersion. Since the expectation of the sum of asset prices at maturity is independent of both volatility and correlation, having a few high asset prices implies that many others are very low in most paths. But it is precisely these high-contribution assets that are removed from the basket, leaving the basket with low-priced assets, thus reducing the price of the option. So for low correlation, with *b* = 0, increasing volatility does not necessarily increase the price. We remind the reader that this simple analysis applies to a homogeneous basket. Individual volatilities, dividends, and a nonconstant correlation can affect the payoff in ways not always easily explained.

## **References**

- [1] Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*, Springer, New York.
- [2] Mountain Range Options, document downloadable from global-derivatives.com

## **Related Articles**

**Altiplano Option**; **Basket Options**; **Correlation Risk**; **Himalayan Option**.

REZA K. GHARAVI
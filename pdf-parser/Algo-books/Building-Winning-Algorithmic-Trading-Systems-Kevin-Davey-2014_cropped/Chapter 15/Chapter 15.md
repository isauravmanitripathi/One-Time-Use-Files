# Diversification

s you progress through the trading system development process numerous  $\boldsymbol{\Lambda}$ times, you'll start to realize that you have an algorithmic strategy factory on your hands. Raw material comes in the door as strategy ideas for entry and exit. Machines, such as limited testing, walk-forward testing, and Monte Carlo simulation, work on your ideas and either shape it into a better product, or tear it to shreds. At the end of your factory, you end up with trading systems you can trade or garbage destined for the scrap heap. If you do this over and over, you'll create a lot of garbage, but you'll also have a stack of strategies to trade. That's where diversification can be a big contributor.

I'm sure you've heard the old saw, "Put your eggs in one basket, then watch that basket!" In trading, this would be analogous to finding one trading system (the basket) and then putting all your money (eggs) into it. That is great if it works. I'm sure there are traders out there who concentrate on trading one system. I'm not one of them, though, and I do not recommend that you try to be one either. Why not? Well, the simple fact is that trading systems fail, and very few, if any, trading systems last forever. In addition, all trading systems go through drawdowns, and sometimes they recover and sometimes they don't. Do you really want your money tied to the fortunes (or misfortunes) of one trading strategy? I sure don't!

To get around this issue, I take the opposite approach and use diversification. Instead of one basket (trading system), I spread my capital among numerous, uncorrelated trading systems. In effect, I have many baskets, and although it takes more effort to watch and track each basket, the benefits are clear:

Less worry about a system's failing. When you trade one system, you are at the mercy of that system or the approach behind the system. If you have a trend-following approach and the market goes flat for a few years, you will be in drawdown until

the market starts to trend. When you trade multiple systems with diff erent styles, it is very likely that your countertrend systems will do good when your trend systems do bad, and vice versa.

- *Fewer fi ll issues.* In trading one system, as your capital grows, so will your trading size. Eventually, your size will become large enough to aff ect your fi lls. Even trading 10 contracts in gold, for example, is enough that any stop‐loss orders you have will likely experience a few extra ticks of slippage as your 10 lot gets filled. However, if you trade numerous systems, your size on any one trade will be smaller, making fills less of an issue.
- *Smoother equity curve.* When you diversify correctly, you will have diff erent styles, diff erent markets, and diff erent time frames with your trading systems. These differences come together to produce a smoother equity curve, many times reducing drawdown, and almost always reducing overall volatility.

 Diversifi cation, done properly, is probably the closest thing I've ever seen to the so‐called trading "Holy Grail." The tricks behind diversifi cation are then (1) how to design systems with diversifi cation in mind and (2) how to measure that you actually have diversifi cation. I'll discuss each of these topics in this chapter.

## ■ **Designing with Diversifi cation in Mind**

 In the next section, I describe simple ways to measure diversification, but I use these measures after the fact, not during the design process. This is because it is difficult to look at a trading system, identify its weak points, and then design a second complementary system to smooth the first one. It can be done, but I think that is the tough way. I take a much simpler approach, and it seems to work quite well.

 If you look back at the initial stages of strategy development, you'll recall that we identify certain characteristics of the system we are trading:

- Market
- Bar type/size
- Any custom time sessions
- Entry
- Exit

 As it turns out, taking an initial strategy and varying a couple of these strategy characteristics will likely produce an uncorrelated system. It becomes as simple as doing something diff erent with your trading idea!

 A good example of this is with the two euro futures strategies I design in Part IV of this book. Although the market traded is exactly the same, I altered the bar size (105‐minute bars versus 60-minute bars), the time session (one strategy trades at night, the other during the day), the entries (completely different entries for each strategy) and exits (different exits, where one system strives for small profits, and the other goes for outsized gains). These change cause completely different system behavior, leading to different results, and consequently diversification.

### ■ **Measuring Diversifi cation**

 Once we have two or more systems, how do we check that trading these two systems actually increase diversifi cation? I generally use four methods to check.

#### **Daily Return Correlation**

 With this method, you simply run a correlation analysis in Excel on the daily returns of each system. For intraday systems, you could run the analysis on shorter time period bars, such as hourly. When I use daily results, I generally check the correlation over the entire history, and then over six‐month to one‐year periods. This analysis can easily be performed in Excel. I take the daily strategy results for each strategy, plot one as X and one as Y, and calculate the R2 correlation coeffi cient. The lower the correlation coeffi cient, the better the diversifi cation. If in all cases the correlation is much less than 1.0, I can safely assume the correlation is low, and therefore the diversifi cation is high. One caveat, though: because of the fact that the longer term correlation is low does not mean that the systems will never be correlated. There could be weeks or months where the results are highly correlated. If you are aggressive with position sizing, you need to be extra careful—strategies that you assume are not correlated can suddenly become correlated and, instead of reducing your risk, may actually amplify it. A good example of this occurred during the fi nancial crisis of 2008, where heretofore uncorrelated markets and approaches suddenly all moved in lockstep. Diversifi cation might not help you much in periods of crisis.

| TABLE 15.1       | Using Correlation Measures for<br>Diversification Check |  |
|------------------|---------------------------------------------------------|--|
| Strategy         | R 2<br>Correlation<br>Coefficient                       |  |
| Euro night       | 0.9370                                                  |  |
| Euro day         | 0.9745                                                  |  |
| Euro day + night | 0.9817                                                  |  |

#### **Linearity of Equity Curve**

 As I have stated previously, a perfectly linear equity curve is the ideal curve for a trading system. It is also a terrifi c way to measure the diversifi cation eff ect. All you have to do is take the strategy's equity curve, run a linear regression on it (which can be done in Excel), and report the correlation coeffi cient R 2 value. An R 2 value of 1 is ideal, as it represents a perfectly linear equity curve. An example of this measurement is shown in Table 15.1 for the euro systems, which are discussed in later chapters. As you can see, the R2 value for the combined equity is better than the R 2 for each of the pieces. Thus, combining these strategies into one system provides diversifi cation, resulting in a smoother equity curve.

#### **Maximum Drawdown**

 Another way to measure the impact of diversifi cation is through the maximum drawdown. Although trading multiple systems might not always lead to a reduced maximum drawdown, especially on an absolute basis, many times it does. This is easy to check if you have the equity curve for each system and the combined system. This is shown in Table 15.2 for the euro systems.

 In this case, the drawdown for the combined system is in between that of the euro day and euro night systems. This makes it a bit unclear as to whether diversifi cation is occurring. But once we look at reward relative to risk, the answer is clear.

#### **Monte Carlo, Return/Drawdown**

 Since measuring the drawdown by itself doesn't always give a clear answer, I use Monte Carlo analysis to see whether the combined system is better on a risk‐adjusted basis. I measure this by looking at the annual percentage return divided by the max percentage drawdown. Higher values mean that I am getting more reward for my risk. I also look at the probability of making money in a year for confi rmation. When I run this analysis, the results are clear (see Table 15.3 ).

 When looking at all the analysis results, note that the conclusion is pretty obvious: combining the two systems produces a smoother equity curve, smaller drawdown

| TABLE 15.2       | Utilizing Drawdown for Diversification<br>Check |  |
|------------------|-------------------------------------------------|--|
| Strategy         | Maximum Drawdown                                |  |
| Euro night       | \$3,008                                         |  |
| Euro day         | \$3,523                                         |  |
| Euro day + night | \$3,265                                         |  |

|                  | Diversification Check |                                   |  |
|------------------|-----------------------|-----------------------------------|--|
| Strategy         | Return/Drawdown       | Probability of Profit in One Year |  |
| Euro night       | 2.2                   | 89%                               |  |
| Euro day         | 5.2                   | 97%                               |  |
| Euro day + night | 6.7                   | 98%                               |  |

 **TABLE 15.3 Using Return/Drawdown and Probability of Profit for** 

than the worst system by itself, a better return‐to‐risk ratio, and increased probability of profi t. Clearly, diversifi cation made the combined system better than each of its parts.

 The really nice thing about this diversifi cation technique is that it did not take any real mathematical eff ort to ensure that the systems were diversifi ed. By simply taking care to make the strategies diff erent, by some combination of diff erent entries, exits, and other general parameters, diversifi cation was practically ensured. This might not always be the case, but this is true enough of the time to make it a useful and simple technique.

 One fi nal benefi t of diversifi cation will help you increase the output of your strategy development factory. As I have shown, two good systems became a lot better by trading them together. Thus, it might mean that your individual system performance goals can be relaxed a bit, since diversifi cation will later improve the performance. In this manner, you might be more successful creating many "decent" or "just good enough" strategies, rather than one "super‐terrifi c" strategy. Since it is much, much easier to create good, but not great systems, you might get to your overall goal much more quickly by employing diversifi cation.
### **Financial Risk**

Financial risk is about potential value variation per unit of time.

That sentence is of sufficient importance to deserve its own paragraph. This is a very basic concept and one that's absolutely clear to anyone working in the financial industry. If you have a university degree in finance or if you have spent time on the professional side of the industry, this should already be very obvious to you.

However, unfortunate as it is, the concept of risk is often very much misunderstood and misused in the hobby trading segment. A large quantity of books and websites targeting hobby traders has muddled the concept of risk and continue to misuse the term and promote methodologies based on gambling, numerology and pseudoscience.

In this chapter, I will attempt to explain what risk means in a financial context, how it can be measured and used for systematic trading models, as well as explain the common ways that the term is misused and the dangers it poses. But first, take a look at that key sentence again.

Financial risk is about potential value variation per unit of time.

## **Quantifying Risk**

The most common way to quantify risk is about measuring past volatility. The term volatility has to do with how much an asset tends to fluctuate, move up or down, in a given time period. You may for instance conclude that while Microsoft tends to fluctuate by about half a percent per day on average for the past few months, Tesla shows daily changes of double that.

That would mean that Tesla is more volatile than Microsoft, but whether or not it's more risky depends on how much you invest in it. If the volatility is exactly half in Microsoft, you would theoretically achieve the same risk level if you invest twice as much as in Tesla. You would, again theoretically, see the same value variation in each stock per day going forward.

That's in a nutshell how to think about financial risk.

Before I offend actual financial risk professionals too much, in particular as I'm married to one, I should point out that financial risk can be an extremely complex topic. If you are a risk manager or risk controller of a larger portfolio, of a number of portfolios or something as complex as a whole bank, risk can be very mathematically intensive. But that's not what this book covers. This book covers risk as it pertains to trading a single, or at least a small number of portfolios.

The most important part to understand from that perspective is that risk, just like return, always has a time component. If you are offered a ten percent return, you can't possibly say if that's good or bad without knowing about the time frame. Ten percent in a month, ten percent in a year, or ten percent in ten years are all very different situations.

The same naturally goes for the risk side. Risking a loss of two percent in a day is not the same as risking a loss of two percent in a year. This is why we use historical volatility of assets, measuring how much they move up or down per day, to calculate risk exposure.

If you understand this concept alone, that risk has to do with potential value variation per unit of time, you have come a long way from the hobby trading way of thinking.

As always, there are of course potentially complicating factors to this otherwise simple concept. While I will refrain from going into these in great detail, as they could easily warrant a book on by themselves, I will briefly explain what it's about.

The first issue has to do with correlation. This should be considered when you have multiple positions open, and has to do with how they relate to each other. If you hold two positions in two similar stocks, with a high correlation to each other, you are adding to the same or a similar risk factor.

If on the other hand, you hold a stock and a commodity, they could potentially be completely unrelated, and holding them both could be lower overall risk than only holding one of them. No need to worry if this seems overly complicated to you. For the purposes of this book I will keep things simple and not dive into the fun sounding topic of covariance matrix analysis.

The other issue with using recent volatility as a forecast for future volatility is that this relationship does not always work out. Meaning, that sometimes future volatility can be quite different from the past. Or in plain English, sometimes things change.

But on the whole, using past volatility to estimate future volatility is better than not doing so.

This concept of volatility can also be applied to the past, which things are bit less in in a state of flux than in the future. If you evaluating the past performance of trading portfolios as an example. It's not enough to see that Portfolio A showed a higher performance than Portfolio B. You need to put it into context of what risk they took to get there. How high the volatility of returns were.

This is why the Sharpe Ratio remains one of the most commonly used comparison measurements. This ratio takes the overall returns, deducts risk free interest for the same period, and divides this by the standard deviation.

### **Mark to Market**

The term mark to market is a principle of valuing something at

the most recent market price, taking all known factors into account. This may seem like an obvious concept, but is often overlooked by those lacking financial education or market experience.

Your holdings as well as your overall portfolio should always be valued at their current mark to market valuation. That's not anywhere near as complicated as it may seem. It's best explained by an example of someone breaking this rule.

People seem to like gambling analogies. A guy walks into a casino and puts down a hundred dollars in chips on the black jack table. After a good run, he now has two hundred dollars in chips in front of him. In his mind, he is now playing with the bank's money. He could lose a hundred dollars before risking anything.

That's now how it works though. After he doubled his money, his mark to market portfolio is \$200. If he now loses ten dollars before leaving the table, he walks away with \$190. That's a gain from when he sat down, but a loss from his peak mark to market valuation.

Now look at the trading equivalent. Someone buys 500 Initech shares at \$20, with a plan to lose at most \$1,000 on this trade. The share takes off right away, and moves up to \$30. Now your initial position value of \$10,000 is up to \$15,000. Then the price starts moving down for a while. Finally it hits \$18, and he stops out with a portfolio value of \$9,000, for a loss of \$1,000.

But that's again not how it works. The position was at one point worth \$15,000, so he lost \$6,000 from there.

From a valuation perspective, it does not matter if you have closed your position or not. The value of your position, and in extension of your portfolio, is not affected by whether or not you still have an open exposure. The current value is what counts, and the current value is based on the last known market price of the shares, if the position is open, or the cash proceeds if it was closed.

To understand mark to market, you need to think in terms of

state. Consider the current state of your portfolio. What it's worth right now, at this moment.

#### **Common Risk Fallacies**

It was no accident that I used a gambling analogy in the previous section. Gambling analogies are very common in hobby trading literature and unfortunately so are gambling approaches to risk. Such approaches can not only be very dangerous, they also tend to be quite nonsensical and disregard basic economics.

These methods are usually collected under the umbrella term Money Management. This is a term that you won't likely hear in the financial industry, but which seems quite common in the hobby segment.

A popular idea in this space is to apply what is called position size pyramiding. This premise is that you increase a position upon success, as you are now playing with the bank's money, and thereby your risk is lower.

But as you saw earlier, this defies the most basic idea of what risk is and what it means. I will also demonstrate here why it just does not make any sense.

A trader buys 1,000 shares of Pierce & Pierce at \$10. A few days later, the price has moved up nicely and is now trading at 20. At that point, our fearless trader decides to double his position, and buy another 1,000 shares. The price moves up and down a bit, but some days later the trader finds the stock at \$25, and he buys another 1,000 lots.

This is the general idea of pyramiding. To increase position on success. And it also makes no sense.

![](_page_5_Figure_0.jpeg)

*Figure 4*‑*1 Pyramiding*

In this simple example, we don't really know why the trader decided to buy exactly 1,000 shares, but that was the starting position. A few days later, he doubled his risk, simply because the first entry point turned out to be favorable.

The problem with that is that your past trades lack a magical ability to impact the future. The fact that you bought at 10 does not in any way affect the probabilities of prices moving up or down from here. Yet the trader decided to double his position.

Ask yourself what you would have done if you missed that first entry at 10 for some reason. When you came back to see the screens, the price was already at 20. What now? Would you buy 1,000 shares? 2,000 shares? Or pass on the trade?

That's an important question. This goes back to the importance of thinking about states, and your answer to that question will show if you follow financial logic yet or not.

If you had taken that first trade at 10 and now doubled, as per

the original plan, you would now hold 2,000 shares. From a logical point of view, if you missed the first trade, you should now buy the full 2,000 shares. That's the only way that you end up with the same portfolio state as originally intended.

If your answer is that you should only buy 1,000 or skip the trade, then you seem to believe that your own past trades can magically impact the future. And there really lay the problem with pyramiding, and with most other so called "money management strategies". They are based on common gambling fallacies that have no grounding in logic, mathematics or finance.

A similar idea is the concept of *Risk per Trade* . The first time I was asked how much I risk per trade, I was quite puzzled. I couldn't figure out what that question meant. Risk per trade and day?

This is again a dangerous fallacy. Risk per trade is the notion of risk being how much money you would lose if an imaginary stop loss point is hit at some time in the unspecified future. That way of thinking about risk is just plain wrong. There is really no other way to look at it. This way of defining risk is simply a misunderstanding of what the word means in a financial context.

Take two portfolios as an example, each with a million dollars to start out with. We are going to buy IBM shares, and only IBM shares and those are right now trading at \$180. For Portfolio 1 we are buying 4,000 shares, for a total notional exposure of \$720.000. With Portfolio 2, we only buy 2,000, and thereby have half of the exposure, \$360,000.

We set our stop loss point for Portfolio 1 at 170, and the stop loss point for Portfolio 2 at 155. Which portfolio is more risky?

|                |                    |                |                 |               | "Risk<br>per |
|----------------|--------------------|----------------|-----------------|---------------|--------------|
|                | Portfolio<br>Value | Shares<br>Held | Shares<br>Value | Stop<br>Point | Trade"       |
| Portfolio<br>1 | 1,000,000          | 4,000          | 720,000         | 170           | 40,000       |
| Portfolio<br>2 | 1,000,000          | 2,000          | 360,000         | 155           | 50,000       |

*Table 4.1 "Risk per Trade"*

If your answer was Portfolio 2, you need to rethink how you view risk. This is a very important issue, and it's really a problem in how hobby trading literature is obscuring the subject.

According to this odd risk-per-trade way of reasoning, Portfolio 1 can lose up to \$40,000 if the stop loss point of 170 is hit, while Portfolio 2 can lose up to \$50,000 if the stop at 155 is hit. But this is not what risk is. Obviously, Portfolio 1 is twice as risky as portfolio 2.

If IBM falls by one dollar tomorrow, Portfolio 1 will lose \$4,000 while Portfolio 2 will lose \$2,000. Risk always has a time component to it. Just like return does.

# **Risk as Currency to Buy Performance**

Performance always has to be put into the context of risk taken. The game is never about who has the highest return in a year. It's about who has the highest return per unit of risk. A gambler putting his entire fortune on number 17, spinning the roulette wheel and winning, made a lot of money. The risk however was rather extreme.

One of the most important steps to becoming a professional trader is to understand what is possible and what is not. Many people entering the field have a belief in seemingly magical return numbers at little to no risk. Unfortunately, there is a thriving industry of con men who are happy to help sell such dreams. They all have colorful stories of how they made millions in short periods of time and how they figured out the secrets of the market. And then they decided to go into the business of mentoring or system selling.

If you are aiming for triple digit yearly returns, you are in the

wrong field. It just does not work like that. Nobody has done that. You will not succeed.

In a single year, anything can happen. Anyone can have an extremely good year now and then. But to expect to compound at triple digit numbers over time is the equivalent of attempting a hundred meter dash in two seconds.

Imagine for a moment that the con men are correct. That if you pay them for their trading systems and mentoring, you can achieve 100% consistent return per year. What would that mean? The math is quite simple. Sell your car and put \$10,000 to work. In a year, you will have 20k. In two years you have 40k. In ten years, you will have ten million dollars. Twenty years after you started, you will be the proud owner of ten billion dollars and you would see your first trillion in year 26. It would be nice if such fantasies worked, but as it turns out, magic is not real and, spoiler, neither is Santa.

Anyone aiming at achieving triple digit yearly returns will, with mathematical certainty, lose all of their money if they remain at the table. In such a game, the longer you play, the more your probability of ruin approaches 1.

To put things into context, some of the very best hedge funds in the world show real world compound returns of around 20% per year. And those are the best of the best. This is the league that Buffett and Soros are playing in.

So what can we expect?

The first thing to understand is that the higher risk you are willing to take, the higher will your possible returns be. Just like the guy at the roulette table, you can make enormous gains if you don't mind having a very high probability of losing all of it.

Knowledge, hard work and skill can improve your results but it can't accomplish the impossible.

The bad news is that your returns are likely to be less than 15%

p.a. in reality over longer time periods. The good news is that if you can achieve that, you can make a lot of money in this business. But of course, performance need to be paid for, with volatility.

Nobody likes volatility. It would be great if we could get a small gain every single day, and move up in a straight line. But unfortunately, volatility is required to create returns. What we try to achieve is to use as little volatility as we can to pay for the performance. And that's what a Sharpe Ratio measures.

Sharpe Ratio is probably the most widely used and most wellknown performance metrics. It can be a very useful analytic and it gives you a general idea of the risk adjusted performance of a strategy. Naturally you need to go deeper and analyze the details for a proper strategy evaluation, but the Sharpe will give you a good overview to start off with.

The calculation of the Sharpe Ratio is quite simple. You take the annualized return, deduct risk free interest and divide by annualized standard deviation of returns.

$$\text{Sharpe} = \frac{\text{AnnualizedReturn - RiskFree}}{\text{AnnualizedStandardDeviation}}$$

The part of this formula which tends to raise the most questions is the risk free rate. The proper way to do it, at least in this author's view, would be to use a shorter money market or treasury yields. That is, a time series of yields, deducting the daily yields from the daily strategy returns, and not just a fixed value.

But this is a practical book, and I will give you a practical advice. For most readers of this book, the risk free rate aspect may seem like an unnecessary complication. If your purpose is simply to compare strategies against each other, you might want to take the shortcut of using zero as the risk free rate.

Given the formula, we clearly want to see a high Sharpe Ratio rather than a low one. We want a high return at a low volatility. But you need to be realistic here. What you will find is that Sharpe Ratios

over 1.0 are rare, and that's not necessarily a problem.

Some strategies can be highly successful and very profitable, while still showing a Sharpe of 0.7 or 0.8. A realized Sharpe of above 1.0 is possible, but exceptional. It's in this type of range that is makes sense to aim.

Strategies with Sharpe of 3 or even 5 do exist, but they tend to be of the so called negative skew variety. That expression, referring to the shape of the return distribution, means that you win small most of the time, until you suddenly get hit with a big loss. For such strategies, you may see long periods of constant winning, only to suffer a sudden and sometimes catastrophic loss.

A Sharpe Ratio does not tell the whole story, and by itself it shouldn't be used to evaluate, select or discard a strategy. It does make sense to use in combination with other analytics and a detailed analysis.

What makes the Sharpe Ratio so useful is that it directly reflects the core concept that this chapter is trying to instill. The concept that returns always have to be put in context of volatility. By understanding the logic of the Sharpe Ratio, you will gain an understanding of the concept of financial risk.
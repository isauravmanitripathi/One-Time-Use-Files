## Chapter 5

# Sourcing Strategy Ideas

In this chapter I want to introduce you to the methods by which I myself identify protable algorithmic trading strategies. We will discuss how to nd, evaluate and select such systems. I'll explain how identifying strategies is as much about personal preference as it is about strategy performance, how to determine the type and quantity of historical data for testing, how to dispassionately evaluate a trading strategy and nally how to proceed towards the backtesting phase and strategy implementation.

## 5.1 Identifying Your Own Personal Preferences for Trading

In order to be a successful trader - either discretionally or algorithmically - it is necessary to ask yourself some honest questions. Trading provides you with the ability to lose money at an alarming rate, so it is necessary to "know thyself" as much as it is necessary to understand your chosen strategy.

I would say the most important consideration in trading is being aware of your own personality. Trading, and algorithmic trading in particular, requires a signicant degree of discipline, patience and emotional detachment. Since you are letting an algorithm perform your trading for you, it is necessary to be resolved not to interfere with the strategy when it is being executed. This can be extremely dicult, especially in periods of extended drawdown. However, many strategies that have been shown to be highly protable in a backtest can be ruined by simple interference. Understand that if you wish to enter the world of algorithmic trading you will be emotionally tested and that in order to be successful, it is necessary to work through these diculties!

The next consideration is one of time. Do you have a full time job? Do you work part time? Do you work from home or have a long commute each day? These questions will help determine the frequency of the strategy that you should seek. For those of you in full time employment, an intraday futures strategy may not be appropriate (at least until it is fully automated!). Your time constraints will also dictate the methodology of the strategy. If your strategy is frequently traded and reliant on expensive news feeds (such as a Bloomberg terminal) you will clearly have to be realistic about your ability to successfully run this while at the oce! For those of you with a lot of time, or the skills to automate your strategy, you may wish to look into a more technical high-frequency trading (HFT) strategy.

My belief is that it is necessary to carry out continual research into your trading strategies to maintain a consistently protable portfolio. Few strategies stay "under the radar" forever. Hence a signicant portion of the time allocated to trading will be in carrying out ongoing research. Ask yourself whether you are prepared to do this, as it can be the dierence between strong protability or a slow decline towards losses.

You also need to consider your trading capital. The generally accepted ideal minimum amount for a quantitative strategy is 50,000 USD (approximately ¿35,000 for us in the UK). If I was starting again, I would begin with a larger amount, probably nearer 100,000 USD (approximately ¿70,000). This is because transaction costs can be extremely expensive for midto high-frequency strategies and it is necessary to have sucient capital to absorb them in times of drawdown. If you are considering beginning with less than 10,000 USD then you will need to restrict yourself to low-frequency strategies, trading in one or two assets, as transaction costs will rapidly eat into your returns. Interactive Brokers, which is one of the friendliest brokers to those with programming skills, due to its API, has a retail account minimum of 10,000 USD.

Programming skill is an important factor in creating an automated algorithmic trading strategy. Being knowledgeable in a programming language such as C++, Java, C#, Python or R will enable you to create the end-to-end data storage, backtest engine and execution system yourself. This has a number of advantages, chief of which is the ability to be completely aware of all aspects of the trading infrastructure. It also allows you to explore the higher frequency strategies as you will be in full control of your "technology stack". While this means that you can test your own software and eliminate bugs, it also means more time spent coding up infrastructure and less on implementing strategies, at least in the earlier part of your algo trading career. You may nd that you are comfortable trading in Excel or MATLAB and can outsource the development of other components. I would not recommend this however, particularly for those trading at high frequency.

You need to ask yourself what you hope to achieve by algorithmic trading. Are you interested in a regular income, whereby you hope to draw earnings from your trading account? Or, are you interested in a long-term capital gain and can aord to trade without the need to drawdown funds? Income dependence will dictate the frequency of your strategy. More regular income withdrawals will require a higher frequency trading strategy with less volatility (i.e. a higher Sharpe ratio). Long-term traders can aord a more sedate trading frequency.

Finally, do not be deluded by the notion of becoming extremely wealthy in a short space of time! Algo trading is NOT a get-rich-quick scheme - if anything it can be a become-poorquick scheme. It takes signicant discipline, research, diligence and patience to be successful at algorithmic trading. It can take months, if not years, to generate consistent protability.

## 5.2 Sourcing Algorithmic Trading Ideas

Despite common perceptions to the contrary, it is actually quite straightforward to locate profitable trading strategies in the public domain. Never have trading ideas been more readily available than they are today. Academic nance journals, pre-print servers, trading blogs, trading forums, weekly trading magazines and specialist texts provide thousands of trading strategies with which to base your ideas upon.

Our goal as quantitative trading researchers is to establish a strategy pipeline that will provide us with a stream of ongoing trading ideas. Ideally we want to create a methodical approach to sourcing, evaluating and implementing strategies that we come across. The aims of the pipeline are to generate a consistent quantity of new ideas and to provide us with a framework for rejecting the majority of these ideas with the minimum of emotional consideration.

We must be extremely careful not to let cognitive biases inuence our decision making methodology. This could be as simple as having a preference for one asset class over another (gold and other precious metals come to mind) because they are perceived as more exotic. Our goal should always be to nd consistently protable strategies, with positive expectation. The choice of asset class should be based on other considerations, such as trading capital constraints, brokerage fees and leverage capabilities.

#### 5.2.1 Textbooks

If you are completely unfamiliar with the concept of a trading strategy and nancial markets in general then the rst place to look is with established textbooks. Classic texts provide a wide range of simpler, more straightforward ideas, with which to familiarise yourself with quantitative trading. Here is a selection that I recommend for those who are new to quantitative trading, which gradually become more sophisticated as you work through the list.

#### Financial Markets and Participants

The following list details books that outline how capital markets work and describe modern electronic trading.

- Financial Times Guide to the Financial Markets by Glen Arnold[1] - This book is designed for the novice to the nancial markets and is extremely useful for gaining insight into all of the market participants. For our purposes, it provides us with a list of markets on which we might later form algorithmic trading strategies.
- Trading and Exchanges: Market Microstructure for Practitioners by Larry Harris[7] - This is an extremely informative book on the participants of nancial markets and how they operate. It provides signicant detail in how trades are carried out, the various motives of the players and how markets are regulated. While some may consider it "dry reading" I believe it is absolutely essential to understand these concepts to be a good algorithmic trader.
- Algorithmic Trading and DMA: An introduction to direct access trading strategies by Barry Johnson[10] - Johnson's book is geared more towards the technological side of markets. It discusses order types, optimal execution algorithms, the types of exchanges that accept algorithmic trading as well as more sophisticated strategies. As with Harris' book above, it explains in detail how electronic trading markets work, the knowledge of which I also believe is an essential prerequisite for carrying out systematic strategies.

#### Quantitative Trading

The next set of books are about algorithmic/quantitative trading directly. They outline some of the basic concepts and describe particular strategies that can be implemented.

- Quantitative Trading: How to Build Your Own Algorithmic Trading Business by Ernest Chan[5] - Ernest Chan's rst book is a beginner's guide to quantitative trading strategies. While it is not heavy on strategy ideas, it does present a framework for how to setup a trading business, with risk management ideas and implementation tools. This is a great book if you are completely new to algorithmic trading. The book makes use of MATLAB.
- Algorithmic Trading: Winning Strategies and Their Rationale by Ernest Chan[6] - Chan's second book is very heavy on strategy ideas. It essentially begins where the previous book left o and is updated to reect current market conditions. The book discusses mean reversion and momentum based strategies at the interday and intraday frequencies. it also briey touches on high-frequency trading. As with the prior book it makes extensive use of MATLAB code.
- Inside The Black Box: The Simple Truth About Quantitative and High-Frequency Trading, 2nd Ed by Rishi Narang[12] - Narang's book provides an overview of the components of a trading system employed by a quantitative hedge fund, including alpha generators, risk management, portfolio optimisation and transaction costs. The second edition goes into signicant detail on high-frequency trading techniques.
- Volatility Trading by Euan Sinclair[16] - Sinclair's book concentrates solely on volatility modelling/forecasting and options strategies designed to take advantage of these models. If you plan to trade options in a quantitative fashion then this book will provide many research ideas.

#### 5.2.2 The Internet

After gaining a grounding in the process of algorithmic trading via the classic texts, additional strategy ideas can be sourced from the internet. Quantitative nance blogs, link aggregators and trading forums all provide rich sources of ideas to test.

However, a note of caution: Many internet trading resources rely on the concept of technical analysis. Technical analysis involves utilising basic signals analysis indicators and behavioural psychology to determine trends or reversal patterns in asset prices.

Despite being extremely popular in the overall trading space, technical analysis is considered somewhat controversial in the quantitative nance community. Some have suggested that it is no better than reading a horoscope or studying tea leaves in terms of its predictive power! In reality there are successful individuals making extensive use of technical analysis in their trading.

As quants with a more sophisticated mathematical and statistical toolbox at our disposal, we can easily evaluate the eectiveness of such "TA-based" strategies. This allows us to make decisions driven by data analysis and hypothesis testing, rather than base such decisions on emotional considerations or preconceptions.

#### Quant Blogs

I recommend the following quant blogs for good trading ideas and concepts about algorithmic trading in general:

- MATLAB Trading - http://matlab-trading.blogspot.co.uk/
- Quantitative Trading (Ernest Chan) - http://epchan.blogspot.com
- Quantivity - http://quantivity.wordpress.com
- Quantopian - http://blog.quantopian.com
- Quantpedia - http://quantpedia.com

#### Aggregators

It has become fashionable in the last few years for topical links to be aggregated and then discussed. I read the following aggregators:

- Quantocracy - http://www.quantocracy.com
- Quant News - http://www.quantnews.com
- Algo Trading Sub-Reddit - http://www.reddit.com/r/algotrading

#### Forums

The next place to nd additional strategy ideas is with trading forums. Do not be put o by more "technical analysis" oriented strategies. These strategies often provide good ideas that can be statistically tested:

- Elite Trader Forums - http://www.elitetrader.com
- Nuclear Phynance - http://www.nuclearphynance.com
- QuantNet - http://www.quantnet.com
- Wealth Lab - http://www.wealth-lab.com/Forum
- Wilmott Forums - http://www.wilmott.com

#### 5.2.3 Journal Literature

Once you have had some experience at evaluating simpler strategies, it is time to look at the more sophisticated academic oerings. Some academic journals will be dicult to access, without high subscriptions or one-o costs. If you are a member or alumnus of a university, you should be able to obtain access to some of these nancial journals. Otherwise, you can look at pre-print servers, which are internet repositories of late drafts of academic papers that are undergoing peer review. Since we are only interested in strategies that we can successfully replicate, backtest and obtain protability for, a peer review is of less importance to us.

The major downside of academic strategies is that they can often either be out of date, require obscure and expensive historical data, trade in illiquid asset classes or do not factor in fees, slippage or spread. It can also be unclear whether the trading strategy is to be carried out with market orders, limit orders or whether it contains stop losses etc. Thus it is absolutely essential to replicate the strategy yourself as best you can, backtest it and add in realistic transaction costs that include as many aspects of the asset classes that you wish to trade in.

Here is a list of the more popular pre-print servers and nancial journals that you can source ideas from:

- arXiv - http://arxiv.org/archive/q-n
- SSRN - http://www.ssrn.com
- Journal of Investment Strategies - http://www.risk.net/type/journal/source/journalof-investment-strategies
- Journal of Computational Finance - http://www.risk.net/type/journal/source/journalof-computational-nance
- Mathematical Finance - http://onlinelibrary.wiley.com/journal/10.1111/%28ISSN%291467- 9965

#### 5.2.4 Independent Research

What about forming your own quantitative strategies? This generally requires (but is not limited to) expertise in one or more of the following categories:

- Market microstructure - For higher frequency strategies in particular, one can make use of market microstructure, i.e. understanding of the order book dynamics in order to generate protability. Dierent markets will have various technology limitations, regulations, market participants and constraints that are all open to exploitation via specic strategies. This is a very sophisticated area and retail practitioners will nd it hard to be competitive in this space, particularly as the competition includes large, well-capitalised quantitative hedge funds with strong technological capabilities.
- Fund structure - Pooled investment funds, such as pension funds, private investment partnerships (hedge funds), commodity trading advisors and mutual funds are constrained both by heavy regulation and their large capital reserves. Thus certain consistent behaviours can be exploited with those who are more nimble. For instance, large funds are subject to capacity constraints due to their size. Thus if they need to rapidly ooad (sell) a quantity of securities, they will have to stagger it in order to avoid "moving the market". Sophisticated algorithms can take advantage of this, and other idiosyncrasies, in a general process known as fund structure arbitrage.
- Machine learning/articial intelligence - Machine learning algorithms have become more prevalent in recent years in nancial markets. Classiers (such as Naive-Bayes, et al.) non-linear function matchers (neural networks) and optimisation routines (genetic algorithms) have all been used to predict asset paths or optimise trading strategies. If you have a background in this area you may have some insight into how particular algorithms might be applied to certain markets.

By continuing to monitor the above sources on a weekly, or even daily, basis you are setting yourself up to receive a consistent list of strategies from a diverse range of sources. The next step is to determine how to reject a large subset of these strategies in order to minimise wasting your time and backtesting resources on strategies that are likely to be unprotable.

## 5.3 Evaluating Trading Strategies

The rst, and arguably most obvious consideration is whether you actually understand the strategy. Would you be able to explain the strategy concisely or does it require a string of caveats and endless parameter lists? In addition, does the strategy have a good, solid basis in reality? For instance, could you point to some behavioural rationale or fund structure constraint that might be causing the pattern(s) you are attempting to exploit? Would this constraint hold up to a regime change, such as a dramatic regulatory environment disruption? Does the strategy rely on complex statistical or mathematical rules? Does it apply to any nancial time series or is it specic to the asset class that it is claimed to be protable on? You should constantly be thinking about these factors when evaluating new trading methods, otherwise you may waste a signicant amount of time attempting to backtest and optimise unprotable strategies.

Once you have determined that you understand the basic principles of the strategy you need to decide whether it ts with your aforementioned personality prole. This is not as vague a consideration as it sounds! Strategies will dier substantially in their performance characteristics. There are certain personality types that can handle more signicant periods of drawdown, or are willing to accept greater risk for larger return. Despite the fact that we, as quants, try and eliminate as much cognitive bias as possible and should be able to evaluate a strategy dispassionately, biases will always creep in. Thus we need a consistent, unemotional means through which to assess the performance of strategies. Here is the list of criteria that I judge a potential new strategy by:

- Methodology - Is the strategy momentum based, mean-reverting, market-neutral, directional? Does the strategy rely on sophisticated (or complex!) statistical or machine learning techniques that are hard to understand and require a PhD in statistics to grasp? Do these techniques introduce a signicant quantity of parameters, which might lead to optimisation bias? Is the strategy likely to withstand a regime change (i.e. potential new regulation of nancial markets)?
- Sharpe Ratio - The Sharpe ratio heuristically characterises the reward/risk ratio of the strategy. It quanties how much return you can achieve for the level of volatility endured by the equity curve. Naturally, we need to determine the period and frequency that these returns and volatility (i.e. standard deviation) are measured over. A higher frequency strategy will require greater sampling rate of standard deviation, but a shorter overall time period of measurement, for instance.
- Leverage - Does the strategy require signicant leverage in order to be protable? Does the strategy necessitate the use of leveraged derivatives contracts (futures, options, swaps) in order to make a return? These leveraged contracts can have heavy volatility characterises and thus can easily lead to margin calls. Do you have the trading capital and the temperament for such volatility?
- Frequency - The frequency of the strategy is intimately linked to your technology stack (and thus technological expertise), the Sharpe ratio and overall level of transaction costs. All other issues considered, higher frequency strategies require more capital, are more sophisticated and harder to implement. However, assuming your backtesting engine is sophisticated and bug-free, they will often have far higher Sharpe ratios.
- Volatility - Volatility is related strongly to the "risk" of the strategy. The Sharpe ratio characterises this. Higher volatility of the underlying asset classes, if unhedged, often leads to higher volatility in the equity curve and thus smaller Sharpe ratios. I am of course assuming that the positive volatility is approximately equal to the negative volatility. Some strategies may have greater downside volatility. You need to be aware of these attributes.

- Win/Loss, Average Prot/Loss - Strategies will dier in their win/loss and average prot/loss characteristics. One can have a very protable strategy, even if the number of losing trades exceed the number of winning trades. Momentum strategies tend to have this pattern as they rely on a small number of "big hits" in order to be protable. Meanreversion strategies tend to have opposing proles where more of the trades are "winners", but the losing trades can be quite severe.
- Maximum Drawdown - The maximum drawdown is the largest overall peak-to-trough percentage drop on the equity curve of the strategy. Momentum strategies are well known to suer from periods of extended drawdowns (due to a string of many incremental losing trades). Many traders will give up in periods of extended drawdown, even if historical testing has suggested this is "business as usual" for the strategy. You will need to determine what percentage of drawdown (and over what time period) you can accept before you cease trading your strategy. This is a highly personal decision and thus must be considered carefully.
- Capacity/Liquidity - At the retail level, unless you are trading in a highly illiquid instrument (like a small-cap stock), you will not have to concern yourself greatly with strategy capacity. Capacity determines the scalability of the strategy to further capital. Many of the larger hedge funds suer from signicant capacity problems as their strategies increase in capital allocation.
- Parameters - Certain strategies (especially those found in the machine learning community) require a large quantity of parameters. Every extra parameter that a strategy requires leaves it more vulnerable to optimisation bias (also known as "curve-tting"). You should try and target strategies with as few parameters as possible or make sure you have sucient quantities of data with which to test your strategies on.
- Benchmark - Nearly all strategies (unless characterised as "absolute return") are measured against some performance benchmark. The benchmark is usually an index that characterises a large sample of the underlying asset class that the strategy trades in. If the strategy trades large-cap US equities, then the S&P500 would be a natural benchmark to measure your strategy against. You will hear the terms "alpha" and "beta", applied to strategies of this type.

Notice that we have not discussed the actual returns of the strategy. Why is this? In isolation, the returns actually provide us with limited information as to the eectiveness of the strategy. They don't give you an insight into leverage, volatility, benchmarks or capital requirements. Thus strategies are rarely judged on their returns alone. Always consider the risk attributes of a strategy before looking at the returns.

At this stage many of the strategies found from your pipeline will be rejected out of hand, since they won't meet your capital requirements, leverage constraints, maximum drawdown tolerance or volatility preferences. The strategies that do remain can now be considered for backtesting. However, before this is possible, it is necessary to consider one nal rejection criteria - that of available historical data on which to test these strategies.

## 5.4 Obtaining Historical Data

Nowadays, the breadth of the technical requirements across asset classes for historical data storage is substantial. In order to remain competitive, both the buy-side (funds, prop-desks) and sell-side (broker/dealers) invest heavily in their technical infrastructure. It is imperative to consider its importance. In particular, we are interested in timeliness, accuracy and storage requirements. We will be discussing data storage in later chapters of the book.

In the previous section we had set up a strategy pipeline that allowed us to reject certain strategies based on our own personal rejection criteria. In this section we will lter more strategies based on our own preferences for obtaining historical data. The chief considerations (especially at retail practitioner level) are the costs of the data, the storage requirements and your level of technical expertise. We also need to discuss the dierent types of available data and the dierent considerations that each type of data will impose on us.

Let's begin by discussing the types of data available and the key issues we will need to think about, with the understanding that we will explore these issues in signicant depth in the remainder of the book:

- Fundamental Data - This includes data about macroeconomic trends, such as interest rates, ination gures, corporate actions (dividends, stock-splits), SEC lings, corporate accounts, earnings gures, crop reports, meteorological data etc. This data is often used to value companies or other assets on a fundamental basis, i.e. via some means of expected future cash ows. It does not include stock price series. Some fundamental data is freely available from government websites. Other long-term historical fundamental data can be extremely expensive. Storage requirements are often not particularly large, unless thousands of companies are being studied at once.
- News Data - News data is often qualitative in nature. It consists of articles, blog posts, microblog posts ("tweets") and editorial. Machine learning techniques such as classiers are often used to interpret sentiment. This data is also often freely available or cheap, via subscription to media outlets. The newer "NoSQL" document storage databases are designed to store this type of unstructured, qualitative data.
- Asset Price Data - This is the traditional data domain of the quant. It consists of time series of asset prices. Equities (stocks), xed income products (bonds), commodities and foreign exchange prices all sit within this class. Daily historical data is often straightforward to obtain for the simpler asset classes, such as equities. However, once accuracy and cleanliness are included and statistical biases removed, the data can become expensive. In addition, time series data often possesses signicant storage requirements especially when intraday data is considered.
- Financial Instruments - Equities, bonds, futures and the more exotic derivative options have very dierent characteristics and parameters. Thus there is no "one size ts all" database structure that can accommodate them. Signicant care must be given to the design and implementation of database structures for various nancial instruments.
- Frequency - The higher the frequency of the data, the greater the costs and storage requirements. For low-frequency strategies, daily data is often sucient. For high frequency strategies, it might be necessary to obtain tick-level data and even historical copies of particular trading exchange order book data. Implementing a storage engine for this type of data is very technologically intensive and only suitable for those with a strong programming/technical background.
- Benchmarks - The strategies described above will often be compared to a benchmark. This usually manifests itself as an additional nancial time series. For equities, this is often a national stock benchmark, such as the S&P500 index (US) or FTSE100 (UK). For a xed income fund, it is useful to compare against a basket of bonds or xed income products. The "risk-free rate" (i.e. appropriate interest rate) is also another widely accepted benchmark. All asset class categories possess a favoured benchmark, so it will be necessary to research this based on your particular strategy, if you wish to gain interest in your strategy externally.
- Technology - The technology stacks behind a nancial data storage centre are complex. However, it does generally centre around a database cluster engine, such as a Relational Database Management System (RDBMS), such as MySQL, SQL Server, Oracle or a Document Storage Engine (i.e. "NoSQL"). This is accessed via "business logic" application code that queries the database and provides access to external tools, such as MATLAB, R or Excel. Often this business logic is written in C++, Java or Python. You will also need to host this data somewhere, either on your own personal computer, or remotely via internet servers. Products such as Amazon Web Services have made this simpler and cheaper in

recent years, but it will still require signicant technical expertise to achieve in a robust manner.

As can be seen, once a strategy has been identied via the pipeline it will be necessary to evaluate the availability, costs, complexity and implementation details of a particular set of historical data. You may nd it is necessary to reject a strategy based solely on historical data considerations. This is a big area and teams of PhDs work at large funds making sure pricing is accurate and timely. Do not underestimate the diculties of creating a robust data centre for your backtesting purposes!

I do want to say, however, that many backtesting platforms can provide this data for you automatically - at a cost. Thus it will take much of the implementation pain away from you, and you can concentrate purely on strategy implementation and optimisation. Tools like TradeStation possess this capability. However, my personal view is to implement as much as possible internally and avoid outsourcing parts of the stack to software vendors. I prefer higher frequency strategies due to their more attractive Sharpe ratios, but they are often tightly coupled to the technology stack, where advanced optimisation is critical.
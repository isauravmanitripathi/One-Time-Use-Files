## Chapter 2

# What Is Algorithmic Trading?

Algorithmic trading, as dened here, is the use of an automated system for carrying out trades, which are executed in a pre-determined manner via an algorithm specically without any human intervention. The latter emphasis is important. Algorithmic strategies are designed prior to the commencement of trading and are executed without discretionary input from human traders.

In this book algorithmic trading refers to the retail practice of automated, systematic and quantitative trading, which will all be treated as synonyms for the purpose of this text. In the nancial industry algorithmic trading generally refers to a class of execution algorithms (such as Volume Weighted Average Price, VWAP) used to optimise the costs of larger trading orders.

## 2.1 Overview

Algorithmic trading diers substantially from discretionary trading. In this section the benets and drawbacks of a systematic approach will be outlined.

#### 2.1.1 Advantages

Algorithmic trading possesses numerous advantages over discretionary methods.

#### Historical Assessment

The most important advantage in creating an automated strategy is that its performance can be ascertained on historical market data, which is (hopefully) representative of future market data. This process is known as backtesting and will be discussed in signicant depth within this book. Backtesting allows the (prior) statistical properties of the strategy to be determined, providing insight into whether a strategy is likely to be protable in the future.

#### Eciency

Algorithmic trading is substantially more ecient than a discretionary approach. With a fully automated system there is no need for an individual or team to be constantly monitoring the markets for price action or news input. This frees up time for the developer(s) of the trading strategy to carry out more research and thus, depending upon capital constraints, deploy more strategies into a portfolio.

Furthermore by automating the risk management and position sizing process, by considering a stable of systematic strategies, it is necessary to automatically adjust leverage and risk factors dynamically, directly responding to market dynamics in real-time. This is not possible in a discretionary world, as a trader is unable to continuously compute risk and must take occasional breaks from monitoring the market.

#### No Discretionary Input

One of the primary advantages of an automated trading system is that there is (theoretically) no subsequent discretionary input. This refers to modication of trades at the point of execution or while in a position. Fear and greed can be overwhelming motivators when carrying out discretionary trading. In the context of systematic trading it is rare that discretionary input improves the performance of a strategy.

That being said, it is certainly possible for systematic strategies to stop being protable due to regime shifts or other external factors. In this instance judgement is required to modify parameters of the strategy or to retire it. Note that this process is still devoid of interfering with individual trades.

#### Comparison

Systematic strategies provide statistical information on both historical and current performance. In particular it is possible to determine equity growth, risk (in various forms), trading frequency and a myriad of other metrics. This allows an "apples to apples" comparison between various strategies such that capital can be allocated optimally. This is in contrast to the case where only prot & loss (P&L) information is tracked in a discretionary setting, since it masks potential drawdown risk.

#### Higher Frequencies

This is a corollary of the eciency advantage discussed above. Strategies that operate at higher frequencies over many markets become possible in an automated setting. Indeed, some of the most protable trading strategies operate at the ultra-high frequency domain on limit order book data. These strategies are simply impossible for a human to carry out.

#### 2.1.2 Disadvantages

While the advantages of algorithmic trading are numerous there are some disadvantages.

#### Capital Requirements

Algorithmic trading generally requires a far larger capital base than would be utilised for retail discretionary trading, this is simply due to the fact that there are few brokers who support automated trade execution that do not also require large account minimums. The most prolic brokerage in the retail automated space is Interactive Brokers, who require an account balance of \$10,000. The situation is slowly changing, especially as other brokerages are allowing direct connection via the FIX protocol. Further, the Pattern Day Trader requirements as dened by the Securities and Exchange Commission require a minimum of \$25,000 in account equity to be maintained at all times, in certain margin situations. These issues will be discussed at length in the section on Execution.

In addition, obtaining data feeds for intraday quantitative strategies, particularly if using futures contracts, is not cheap for the retail trader. Common retail intraday feeds are often priced in the \$300-\$500 per month range, with commercial feeds an order of magnitude beyond that. Depending upon your latency needs it may be necessary to co-locate a server in an exchange, which increases the monthly costs. For the interday retail trader this is not necessarily an issue, but it is worth considering. There are also ancillaries such as a more robust internet connection and powerful (and thus expensive) desktop machines to be purchased.

#### Programming/Scientic Expertise

While certain systematic trading platforms exist, such as Quantopian, QuantConnect and TradeStation, that alleviate the majority of the programming diculty, some do not yet (as of the time of writing) support live execution. TradeStation is clearly an exception in this case. Thus it is a requirement for the algorithmic trader to be relatively procient both in programming and scientic modelling.

I have attempted to demonstrate a wide variety of strategies, the basis of which are nearly always grounded in a manner that is straightforward to understand. However, if you do possess numerical modelling skills then you will likely nd it easier to make use of the statistical time series methods present in the Modelling section. The majority of the techniques demonstrated have already been implemented in external Python libraries, which saves us a substantial amount of development work. Thus we are reduced to tying together our data analysis and execution libraries to produce an algorithmic trading system.

## 2.2 Scientic Method

The design of trading strategies within this book is based solely on the principles of the scientic method. The process of the scientic method begins with the formulation of a question, based on observations. In the context of trading an example would be "Is there a relationship between the SPDR Gold Shares ETF (GLD) and the Market Vectors Gold Miners ETF (GDX)?". This allows a hypothesis to be formed that may explain the observed behaviour. In this instance a hypothesis may be "Does the spread between GLD and GDX have mean-reverting behaviour?". The null hypothesis is that there is no mean-reverting behaviour, i.e. the price spread is a random walk.

After formulation of a hypothesis it is up to the scientist to disprove the null hypothesis and demonstrate that there is indeed mean reverting behaviour. To carry this out a prediction must be dened. Returning to the GLD-GDX example the prediction is that the time series representing the spread of the two ETFs is stationary. In order to prove or disprove the hypothesis the prediction is subject to testing. In the case of GLD-GDX this means applying statistical stationarity tests such as the Augmented Dickey-Fuller, Hurst Exponent and Variance-Ratio Tests (described in detail in subsequent chapters).

The results of the testing procedure will provide a statistical answer upon whether the null hypothesis can be rejected at a certain level of condence. If the null hypothesis is unable to be rejected, which implies that there was no discernible relationship between the two ETFs, it is still possible that the hypothesis is (partially) true. A larger set of data, incorporation of additional information (such as a third ETF aecting the price) can also be tested. This is the process of analysis. It often leads to rejection of the null hypothesis, after renement.

The primary advantage of using the scientic method for trading strategy design is that if the strategy "breaks down" after a prior period of protability, it is possible to revisit the initial hypothesis and re-evaluate it, potentially leading to a new hypothesis that leads to regained protability for a strategy.

This is in direct contrast to the data mining or black box approach where a large quantity of parameters or "indicators" are applied to a time series. If such a "strategy" is initially protable and then performance deteriorates it is dicult (if not impossible) to determine why. It often leads to arbitrary application of new information, indicators or parameters that may temporarily lead to protability but subsequently lead to further performance degradation. In this instance the strategy is usually discarded and the process of "research" continues again.

In this book all trading strategies will be developed with an observation-hypothesis approach.

## 2.3 Why Python?

The above sections have outlined the benets of algorithmic trading and the scientic method. It is now time to turn attention to the language of implementation for our trading systems. For this book I have chosen [Python.](http://python.org/) Python is a high-level language designed for speed of development. It possesses a wide array of libraries for nearly any computational task imaginable. It is also gaining wider adoption in the the asset management and investment bank communities.

Here are the reasons why I have chosen Python as a language for trading system research and implementation:

 Learning - Python is extremely easy to learn compared to other languages such as C++. You can be extremely productive in Python after only a few weeks (some say days!) of usage.

- Libraries - The main reason to use Python is that it comes with a staggering array of libraries, which signicantly reduce time to implementation and the chance of introducing bugs into our code. In particular, we will make use of NumPy (vectorised operations), SciPy (optimisation algorithms), pandas (time series analysis), statsmodel (statistical modelling), scikit-learn (statistical/machine learning), IPython (interactive development) and matplotlib (visualisation).
- Speed of Development - Python excels at development speed to the extent that some have commented that it is like writing in pseudocode. The interactive nature of tools like IPython make strategy research extremely rapid, without sacricing robustness.
- Speed of Execution - While not quite as fast as C++, Python provides scientic computing components which are heavily optimised (via vectorisation). If speed of execution becomes an issue one can utilise Cython and obtain execution speeds similar to C, for a small increase in code complexity.
- Trade Execution - Python plugins exist for larger brokers, such as Interactive Brokers (IBypy). In addition Python can easily make use of the FIX protocol where necessary.
- Cost/License - Python is free, open source and cross-platform. It will run happily on Windows, Mac OSX or Linux.

While Python is extremely applicable to nearly all forms of algorithmic trading, it cannot compete with C (or lower level languages) in the Ultra-High Frequency Trading (UHFT) realm. However, these types of strategies are well outside the scope of this book!

## 2.4 Can Retail Traders Still Compete?

It is common, as a beginning algorithmic trader practising at retail level, to question whether it is still possible to compete with the large institutional quant funds. In this section it will be argued that due to the nature of the institutional regulatory environment, the organisational structure and a need to maintain investor relations, that funds suer from certain disadvantages that do not concern retail algorithmic traders.

The capital and regulatory constraints imposed on funds lead to certain predictable behaviours, which are able to be exploited by a retail trader. "Big money" moves the markets, and as such one can dream up many strategies to take advantage of such movements. Some of these strategies will be discussed in later chapters. The comparative advantages enjoyed by the algorithmic trader over many larger funds will now be outlined.

#### 2.4.1 Trading Advantages

There are many ways in which a retail algo trader can compete with a fund on their trading process alone, but there are also some disadvantages:

- Capacity - A retail trader has greater freedom to play in smaller markets. They can generate signicant returns in these spaces, even while institutional funds can't.
- Crowding the trade - Funds suer from "technology transfer", as sta turnover can be high. Non-Disclosure Agreements and Non-Compete Agreements mitigate the issue, but it still leads to many quant funds "chasing the same trade". Whimsical investor sentiment and the "next hot thing" exacerbate the issue. Retail traders are not constrained to follow the same strategies and so can remain uncorrelated to the larger funds.
- Market impact - When playing in highly liquid, non-OTC markets, the low capital base of retail accounts reduces market impact substantially.

- Leverage - A retail trader, depending upon their legal setup, is constrained by margin/leverage regulations. Private investment funds do not suer from the same disadvantage, although they are equally constrained from a risk management perspective.
- Liquidity - Having access to a prime brokerage is out of reach of the average retail algo trader. They have to "make do" with a retail brokerage such as Interactive Brokers. Hence there is reduced access to liquidity in certain instruments. Trade order-routing is also less clear and is one way in which strategy performance can diverge from backtests.
- Client news ow - Potentially the most important disadvantage for the retail trader is lack of access to client news ow from their prime brokerage or credit-providing institution. Retail traders have to make use of non-traditional sources such as meet-up groups, blogs, forums and open-access nancial journals.

#### 2.4.2 Risk Management

Retail algo traders often take a dierent approach to risk management than the larger quant funds. It is often advantageous to be "small and nimble" in the context of risk.

Crucially, there is no risk management budget imposed on the trader beyond that which they impose themselves, nor is there a compliance or risk management department enforcing oversight. This allows the retail trader to deploy custom or preferred risk modelling methodologies, without the need to follow "industry standards" (an implicit investor requirement).

However, the alternative argument is that this exibility can lead to retail traders to becoming "sloppy" with risk management. Risk concerns may be built-in to the backtest and execution process, without external consideration given to portfolio risk as a whole. Although "deep thought" might be applied to the alpha model (strategy), risk management might not achieve a similar level of consideration.

#### 2.4.3 Investor Relations

Outside investors are the key dierence between retail shops and large funds. This drives all manner of incentives for the larger fund - issues which the retail trader need not concern themselves with:

- Compensation structure - In the retail environment the trader is concerned only with absolute return. There are no high-water marks to be met and no capital deployment rules to follow. Retail traders are also able to suer more volatile equity curves since nobody is watching their performance who might be capable of redeeming capital from their fund.
- Regulations and reporting - Beyond taxation there is little in the way of regulatory reporting constraints for the retail trader. Further, there is no need to provide monthly performance reports or "dress up" a portfolio prior to a client newsletter being sent. This is a big time-saver.
- Benchmark comparison - Funds are not only compared with their peers, but also "industry benchmarks". For a long-only US equities fund, investors will want to see returns in excess of the S&P500, for example. Retail traders are not enforced in the same way to compare their strategies to a benchmark.
- Performance fees - The downside to running your own portfolio as a retail trader are the lack of management and performance fees enjoyed by the successful quant funds. There is no "2 and 20" to be had at the retail level!

#### 2.4.4 Technology

One area where the retail trader is at a signicant advantage is in the choice of technology stack for the trading system. Not only can the trader pick the "best tools for the job" as they see t, but there are no concerns about legacy systems integration or rm-wide IT policies. Newer languages such as Python or R now possess packages to construct an end-to-end backtesting, execution, risk and portfolio management system with far fewer lines-of-code (LOC) than may be needed in a more verbose language such as C++.

However, this exibility comes at a price. One either has to build the stack themselves or outsource all or part of it to vendors. This is expensive in terms of time, capital or both. Further, a trader must debug all aspects of the trading system - a long and potentially painstaking process. All desktop research machines and any co-located servers must be paid for directly out of trading prots as there are no management fees to cover expenses.

In conclusion, it can be seen that retail traders possess signicant comparative advantages over the larger quant funds. Potentially, there are many ways in which these advantages can be exploited. Later chapters will discuss some strategies that make use of these dierences.
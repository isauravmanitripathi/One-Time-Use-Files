# CHAPTER 3 Overview of the **Business of High-Frequency** Trading

ccording to the Technology and High-Frequency Trading Survey conducted by FINalternatives.com, a leading hedge fund publication, in June 2009, 90 percent of the 201 asset managers surveyed thought that high-frequency trading had a bright future. In comparison, only  $50$  percent believed that the investment management industry has favorable prospects, and only 42 percent considered the U.S. economy as having a positive outlook.

The same respondents identified the following key characteristics of high-frequency trading:

- Tick-by-tick data processing
- High capital turnover
- Intra-day entry and exit of positions
- Algorithmic trading

Tick-by-tick data processing and high capital turnover define much of high-frequency trading. Identification of small changes in the quote stream sends rapid-fire signals to open and close positions. The term "highfrequency" itself refers to fast entry and exit of trading positions. An overwhelming 86 percent of respondents in the FINalternatives survey thought that the term "high-frequency trading" referred strictly to holding periods of one day or less. (See Figure  $3.1$ .)

Intra-day position management deployed in high-frequency trading results in considerable savings of overnight position carrying costs. The carry is the cost of holding a margined position through the night; it is usually

![](_page_1_Figure_1.jpeg)

**Position-Holding Time Qualifying as High-Frequency Trading**

**FIGURE 3.1** Details of the FINalternatives July 2009 Technology and Trading Survey responses to the question "What position-holding time qualifies as highfrequency trading?"

computed on the margin portion of account holdings after the close of the North American trading sessions. Overnight carry charges can substantially cut into the trading bottom line in periods of tight lending or high interest rates.

Closing down positions at the end of each trading day also reduces the risk exposure resulting from the passive overnight positions. Smaller risk exposure again results in considerable risk-adjusted savings.

Finally, algorithmic trading is a necessary component of highfrequency trading platforms. Evaluating every tick of data separated by milliseconds, processing market information, and making trading decisions in a consistent continuous manner is not well suited for a human brain. Affordable algorithms, on the other hand, can make fast, efficient, and emotionless decisions, making algorithmic trading a requirement in highfrequency operations.

## **COMPARISON WITH TRADITIONAL APPROACHES TO TRADING**

High-frequency trading is a relatively novel approach to investing. As a result, confusion and questions often arise as to how high-frequency trading relates to other, older investment styles. This section addresses these issues.

#### **Technical, Fundamental, or Quant?**

As discussed in Chapter 2, technical trading is based on technical analysis, the objective of which is to identify persistent price change patterns. Technical analysis may suggest that a price is too high or too low given its past trajectory. Technical trading would then imply buying a security the price of which was deemed too low in technical analysis, and selling a security the price of which was deemed too high. Technical analysis can be applied at any frequency and can be perfectly suitable in high-frequency trading models.

Fundamental trading is based on fundamental analysis. Fundamental analysis derives the equilibrium price levels, given available information and economic equilibrium theories. As with technical trading, fundamental trading entails buying a security the price of which was deemed too low relative to its analytically determined fundamental value and selling a security the price of which is considered too high. Like technical trading, fundamental trading can also be applied at any frequency, although price formation or microstructure effects may result in price anomalies at ultrahigh frequencies.

Finally, *quant* (short for quantitative) trading refers to making portfolio allocation decisions based on scientific principles. These principles may be fundamental or technical or can be based on simple statistical relationships. The main difference between quant analyses and technical or fundamental styles is that quants use little or no discretionary judgments, whereas fundamental analysts may exercise discretion in rating the management of the company, for example, and technical analysts may "see" various shapes appearing in the charts. Given the availability of data, quant analysis can be run in high-frequency settings.

Quant frameworks are best suited to high-frequency trading for one simple reason: high-frequency generation of orders leaves little time for traders to make subjective nonquantitative decisions and input them into the system. Aside from their inability to incorporate discretionary inputs, high-frequency trading systems can run on quant analyses based on both technical and fundamental models.

## **Algorithmic, Systematic, Electronic, or Low-Latency?**

Much confusion exists among the terms "high-frequency trading" and "algorithmic," "systematic," "electronic," and "low-latency" trading.

High-frequency trading refers to fast reallocation or turnover of trading capital. To ensure that such reallocation is feasible, most high-frequency trading systems are built as algorithmic trading systems that use complex computer algorithms to analyze quote data, make trading decisions, and optimize trade execution. All algorithms are run electronically and, therefore, automatically fall into the "electronic trading" subset.

While all algorithmic trading qualifies as electronic trading, the reverse does not have to be the case; many electronic trading systems only route orders that may or may not be placed algorithmically. Similarly, while most high-frequency trading systems are algorithmic, many algorithms are not high-frequency.

"Low-latency trading" is another term that gets confused with "highfrequency trading." In practice, "low-latency" refers to the speed of executing an order that may or may not have been placed by a high-frequency system; "low-latency trading" refers to the ability to quickly route and execute orders irrespective of their position-holding time. High-frequency, on the other hand, refers to the fast turnover of capital that may require lowlatency execution capability. Low-latency can be a trading strategy in its own right when the high speed of execution is used to arbitrage instantaneous price differences on the same security at different exchanges.

# **MARKET PARTICIPANTS**

#### **Competitors**

High-frequency trading firms compete with other investment management firms for quick access to market inefficiencies, for access to trading and operations capital, and for recruiting of talented trading strategists. Competitive investment management firms may be proprietary trading divisions of investment banks, hedge funds, and independent proprietary trading operations. The largest independent firms deploying high-frequency strategies are DE Shaw, Tower Research Capital, and Renaissance Technologies.

#### **Investors**

Investors in high-frequency trading include fund of funds aiming to diversify their portfolios, hedge funds eager to add new strategies to their existing mix, and private equity firms seeing a sustainable opportunity to create wealth. Most investment banks offer leverage through their "prime" services.

#### **Services and Technology Providers**

Like any business, a high-frequency trading operation requires specific support services. This section identifies the most common and, in many cases, critical providers to the high-frequency business community.

**Electronic Execution** High-frequency trading practitioners rely on their executing brokers and electronic communication networks (ECNs) to quickly route and execute their trades. Goldman Sachs and Credit Suisse are often cited as broker-dealers dominating electronic execution. Today's major ECN players are ICAP and Thomson/Reuters, along with several others.

**Custody and Clearing** In addition to providing connectivity to exchanges, broker-dealers typically offer special "prime" services that include safekeeping of trading capital (known as custody) and trade reconciliation (known as clearing). Both custody and clearing involve a certain degree of risk. In a custody arrangement, the broker-dealer takes the responsibility for the assets, whereas in clearing, the broker-dealer may act as insurance against the default of trading counterparties. Transaction cost mark-ups compensate broker-dealers for their custody and clearing efforts and risk.

**Software** High-frequency trading operations deploy the following software that may or may not be built in-house:

- Computerized generation of trading signals refers to the core functionality of a high-frequency trading system; the generator accepts and processes tick data, generates portfolio allocations and trade signals, and records profit and loss (P&L).
- Computer-aided analysis represents financial modeling software deployed by high-frequency trading operations to build new trading models. MatLab and R have emerged as the industry's most popular quantitative modeling choices.
- Internet-wide information-gathering software facilitates highfrequency fundamental pricing of securities. Promptly capturing rumors and news announcements enhances forecasts of short-term price moves. Thomson/Reuters has a range of products that deliver real-time news in a machine-readable format.
- Trading software incorporates optimal execution algorithms for achieving the best execution price within a given time interval through timing of trades, decisions on market aggressiveness, and sizing orders into optimal lots. New York–based MarketFactory provides a suite of software tools to help automated traders get an extra edge in the market, help their models scale, increase their fill ratios, reduce slippage, and thereby improve profitability (P&L). Chapter 18 discusses optimization of execution.
- Run-time risk management applications ensure that the system stays within prespecified behavioral and P&L bounds. Such applications may also be known as system-monitoring and fault-tolerance software.

- Mobile applications suitable for monitoring performance of highfrequency trading systems alert administration of any issues.
- Real-time third-party research can stream advanced information and forecasts.

**Legal, Accounting, and Other Professional Services** Like any business in the financial sector, high-frequency trading needs to make sure that "all i's are dotted and all t's are crossed" in the legal and accounting departments. Qualified legal and accounting assistance is therefore indispensable for building a capable operation.

# **Government**

In terms of government regulation, high-frequency trading falls under the same umbrella as day trading. As such, the industry has to abide by common trading rules—for example, no insider trading is allowed. An unsuccessful attempt to introduce additional regulation through a surcharge on transaction costs was made in February 2009.

# **OPERATING MODEL**

# **Overview**

Surprisingly little has been published on the best practices to implement high-frequency trading systems. This chapter presents an overview of the business of high-frequency trading, complete with information on planning the rollout of the system and the capital required to develop and deploy a profitable operation.

Three main components, shown in Figure 3.2, make up the business cycle:

- Highly quantitative, econometric models that forecast short-term price moves based on contemporary market conditions
- Advanced computer systems built to quickly execute the complex econometric models
- Capital applied and monitored within risk and cost-management frameworks that are cautious and precise

The main difference between traditional investment management and high-frequency trading is that the increased frequency of opening and closing positions in various securities allows the trading systems to profitably

![](_page_6_Figure_1.jpeg)

**FIGURE 3.2** Overview of the development cycle of a high-frequency trading process.

capture small deviations in securities prices. When small gains are booked repeatedly throughout the day, the end-of-day result is a reasonable gain.

Developing a high-frequency trading business follows a process unusual for most traditional financial institutions. Designing new highfrequency trading strategies is very costly; executing and monitoring finished high-frequency products costs close to nothing. By contrast, traditional proprietary trading businesses incur fixed costs from the moment an experienced senior trader with a proven track record begins running the trading desk and training promising young apprentices, through the time when the trained apprentices replace their masters.

Figure 3.3 illustrates the cost curves for rolling out computerized and traditional trading systems. The cost of traditional trading remains fairly constant through time. With the exception of trader "burn-outs" necessitating hiring and training new trader staff, costs of staffing the traditional trading desk do not change. Developing computerized trading systems, however, requires an up-front investment that is costly in terms of labor and time. One successful trading system takes on average 18 months to develop. The costs of computerized trading decline as the system moves into production, ultimately requiring a small support staff that typically includes a dedicated systems engineer and a performance monitoring agent. Both the systems engineer and a monitoring agent can be responsible for several trading systems simultaneously, driving the costs closer to zero.

![](_page_7_Figure_1.jpeg)

Time in development and use

**FIGURE 3.3** The economics of high-frequency versus traditional trading businesses.

#### **Model Development**

The development of a high-frequency trading business begins with the development of the econometric models that document persistent relationships among securities. These relationships are then tested on lengthy spans of tick-by-tick data to verify the forecasting validity in various market situations. This process of model verification is referred to as "backtesting." Standard back-testing practices require that the tests be run on data of at least two years in duration. The typical modeling process is illustrated in Figure 3.4.

#### **System Implementation**

The models are often built in computer languages such as MatLab that provide a wide range of modeling tools but may not be suited perfectly for high-speed applications. Thus, once the econometric relationships are ascertained, the relationships are programmed for execution in a fast computer language such as C++. Subsequently, the systems are tested in "paper-trading" with make-believe capital to ensure that the systems work as intended and any problems (known as "bugs") are identified and fixed. Once the systems are indeed performing as expected, they are switched to live capital, where they are closely monitored to ensure proper execution and profitability.

High-frequency execution systems tend to be complex entities that detect and react to a variety of market conditions. Figure 3.5 documents the standard workflow of a high-frequency trading system operating on live capital.

![](_page_8_Figure_1.jpeg)

**FIGURE 3.4** The process for development of econometric models for highfrequency trading.

As Figure 3.5 shows, a typical high-frequency trading system in production encompasses six major tasks, all of which are interrelated and operate in unison.

- Block A receives and archives real-time tick data on securities of interest.
- Block B applies back-tested econometric models to the tick data obtained in Block A.

![](_page_8_Figure_6.jpeg)

**FIGURE 3.5** Run-time and post-trade workflows of a typical high-frequency operation.

- Block C sends orders and keeps track of open positions and P&L values.
- Block D monitors run-time trading behavior, compares it with predefined parameters, and uses the observations to manage the run-time trading risk.
- Block E evaluates trading performance relative to a host of predetermined benchmarks.
- Block F ensures that the trading costs incurred during execution are within acceptable ranges.

Each of the six functional blocks is built with an independent alert system that notifies the monitoring personnel of any problems or other unusual patterns, including unforeseen market behavior, disruptions in the market data process, unexpectedly high trading costs, failure to transmit orders or to receive acknowledgments, and the like.

Given the complexity of the execution process, the development of the six tasks is hardly trivial. It is most successfully approached using a continuous iterative implementation cycle whereby the execution capability is gradually expanded in scope. Figure 3.6 illustrates a

![](_page_9_Figure_7.jpeg)

**FIGURE 3.6** A typical implementation process of run-time high-frequency trading systems.

standard approach for designing and implementing high-frequency trading systems.

The implementation of the run-time components of the high-frequency trading systems begins with careful planning that establishes core functionalities and budgets for the system. Once the planning phase is complete, the process moves into the analysis phase, where the scope of the initial iteration of the project is determined, feedback from all the relevant stakeholders is aggregated, and senior management signs off on the high-level project specifications. The next stage—the design—breaks the system into manageable modules, outlines the functionality of each module, and specifies the desired behavior. In the following stage (known as the implementation stage) the modules are programmed by teams of dedicated software engineers and are tested against specifications determined in the design stage. Once behavior is found to be satisfactory, the project moves into the production and maintenance phase, where deviations from the desired behavior are addressed. When the project is considered stable, a new iteration of planning begins to incorporate enhancements and other desired features into the project. See Chapter 16 for the details of best practices in design and implementation of the high-frequency trading systems.

#### **Trading Platform**

Most high-frequency trading systems today are built to be "platformindependent"—that is, to incorporate flexible interfaces to multiple brokerdealers, ECNs, and even exchanges. The independence is accomplished through the use of FIX language, a special sequence of codes optimized for exchange of financial trading data. With FIX, at a flip of a switch the trading routing can be changed from one executing broker to another or to several brokers simultaneously.

### **Risk Management**

Competent risk management is key to the success of any high-frequency trading system. A seemingly harmless glitch in the code, market data, market conditions, or the like can throw off the trading dynamic and result in large losses. The objective of risk management is to assess the extent of potential damages and to create infrastructure to mitigate damaging conditions during the system run-time. Risk management is discussed in detail in Chapter 17.

#### **ECONOMICS**

## **Revenue Driven by Leverage and the Sharpe Ratio**

For the business to remain viable, revenues must be sufficient to cover expenses of running the business. The business of high-frequency trading is no exception. Accounting for trading costs, a portion of revenues (80 percent on average) is paid out to investors in the trading operation, leaving the management with "performance fees." In addition, the management may collect "management fees," which are a fixed percentage of assets designated to cover administrative expenses of the trading business regardless of performance.

Even the most cost-effective high-frequency trading operation has employee salaries, administrative services, and trading costs, as well as legal and compliance expenses. The expenses easily run \$100,000 per average employee in base salaries and benefits, not considering a negotiated incentive structure; this is in addition to the fixed cost overhead of office space and related expenses.

To compensate for these expenses, what is the minimum level of return on capital that a high-frequency manager should generate each year to remain a going concern? The answer depends on the leverage of the trading platform. Consider a trading operation with five employees. Fixed expenses of such a business may total \$600,000 per year, including salaries and office expenses. Suppose further that the business charges a 0.5 percent management fee on its capital equity and a 20 percent incentive fee on returns it produces above the previous high value, or "watermark." The minimum capital/return conditions for breaking even for such a trading business under different leverage situations are shown in Figure 3.7. As illustrated there, a \$20 million unlevered fund with five employees needs to generate at least a 12 percent return per year in order to break even, while the same fund levered 500 percent (borrowing four times its investment equity) needs to generate just 3 percent per year to survive.

Conventional wisdom, however, tells us that leverage increases the risk of losses. To evaluate the risk associated with higher leverage, we next consider the risks of losing at least 20 percent of the capital equity of the business. As shown in Figures 3.7 and 3.8, the probability of severe losses is much more dependent on the aggregate Sharpe ratio of the trading strategies than it is on the leverage used by the hedge fund.

The Sharpe ratio of a high-frequency trading strategy, discussed in detail in Chapter 5, is the ratio of the average annualized return of the strategy to the annualized standard deviation of the strategy's returns. The higher the Sharpe ratio, the lower the probability of severe losses. As Figure 3.8

![](_page_12_Figure_1.jpeg)

**Sample Break-Even Conditions for Different Leverage Values**

**FIGURE 3.7** Sample break-even conditions for a high-frequency trading business employing five workers.

shows, an annualized Sharpe ratio of 0.5 for an unlevered trading operation expecting to make 20 percent per year translates into a 15 percent risk of losing at least one-fifth of the fund's equity capital. Levering the same fund nine-fold only doubles the risk of losing at least one-fifth of equity. In comparison, the annualized Sharpe ratio of 2.0 for an unlevered trading business expecting to make 20 percent per year translates into a miniscule 0.1 percent risk of losing at least one-fifth of the equity capital, and levering the same trading business only increases the risk of losing at least one-fifth of the fund to 1.5 percent, as shown in Figure 3.9.

Furthermore, as Figures 3.8 and 3.9 show, for any given Sharpe ratio, the likelihood of severe losses actually increases with increasing expected returns, reflecting the wider dispersion of returns. From an investor's perspective, a 5 percent expected return with a Sharpe over 2 is much preferable to a 35 percent expected return with a low Sharpe of, say, 0.5.

![](_page_12_Figure_6.jpeg)

**FIGURE 3.8** Probability of losing 20 percent or more of the investment capital equity running strategies with Sharpe ratio of 0.5.

![](_page_13_Figure_1.jpeg)

**FIGURE 3.9** Probability of losing 20 percent or more of the investment capital equity running strategies with Sharpe ratio of 2.

In summary, a high-frequency trading operation is more likely to survive and prosper if it has leverage and high Sharpe ratios. High leverage increases the likelihood of covering costs, and the high Sharpe ratio reduces the risk of a catastrophic loss.

#### **Transparent and Latent Costs**

Understanding the cost structure of trading becomes especially important in high-frequency settings, where the sheer number of transactions can eliminate gains. As Chapter 19 notes, in addition to readily available or transparent costs of trading, high-frequency operations should account for a wide range of unobservable, or latent, costs. For details on various cost types, please see Chapter 19.

#### **Staffing**

Initial development of high-frequency systems is both risky and pricey, and the staff required to design trading models should understand PhD-level quantitative research in finance and econometrics. In addition, programming staff should be experienced enough to handle complex issues of system inter-operability, computer security, and algorithmic efficiency.

# **CAPITALIZING A HIGH-FREQUENCY TRADING BUSINESS**

Capital used for trading in high-frequency operations comprises equity and leverage. The equity normally comprises contributions from the founders of the firm, private equity capital, investor capital, or capital of the parent company. Leverage is debt that can be obtained through a simple bank loan or margin lending or through other loans offered by broker-dealers.

## **CONCLUSION**

Developing a high-frequency business involves challenges that include issues surrounding the "gray box" or "black box" nature of many systems. The low transparency of fast and complex algorithm decisions may frustrate human traders accustomed to having a thorough understanding of decisions prior to placing trades. High trading frequency may make it difficult to spot a malfunction with the algorithm. And we will not even go into the whole issue of computer security!

Despite the complexity of successfully implementing high-frequency operations, the end results make it all worthwhile. The deployment and execution costs decrease considerably with time, leaving the profitgenerating engines operating consistently, with no emotion, sickness, or other human factors. High-frequency trading is particularly well suited for markets where traditional long-term investment strategies may not work at all; high geopolitical and economic uncertainty may render many such traditional investing venues unprofitable. Well-designed and -executed high-frequency systems, capitalizing on multiple short-term moves of security prices, are capable of generating solid profitability in highly uncertain markets.
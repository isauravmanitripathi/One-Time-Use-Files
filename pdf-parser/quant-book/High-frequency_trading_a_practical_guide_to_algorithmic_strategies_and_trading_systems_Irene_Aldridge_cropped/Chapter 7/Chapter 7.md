# The Business of High-Frequency Trading

 $\bullet$ ontrary to popular belief, the business of high-frequency trading (HFT) is not  $\checkmark$ entirely the business of trading, nor is it a business of pure research. Instead, most of HFT is the business of technology. As such, the economics of building an HFT operation differ considerably from those of a traditional trading floor. This chapter explains the economic nuts and bolts of a successful HFT organization.

#### Key Processes of HFT

The central value proposition of HFT is enabled by tick-by-tick data processing and high capital turnover. The technology behind identifying small changes in the quote stream is what differentiates this business and enables a trader to send rapid-fire signals to open and close positions.

Processing every tick of data on multiple financial instruments is possible only via automated trading. Evaluating data separated by microseconds, interpreting reams of market information, and making trading decisions in a consistent continuous manner is too complex a task for a human brain. Affordable fully automated HFT systems, however, can make fast, efficient, and emotionless decisions.

Figure 7.1 illustrates a sample deceivingly simple process used to develop HFT systems. Just like any software development activity, the HFT process begins with a concept of the final product: a trading idea that becomes a quantitative model. The concept, or a prototype, may be a 20-line piece of code written in a modeling language, such as MatLab, and shown to produce hypothetical profitability on a selection of data.

117

![](_page_1_Figure_0.jpeg)

**FIGURE 7.1** Algorithm design and reevaluation Process

The next step is a back-test: a process whereby the concept is tested on a large volume of tick data. Two years is generally considered a suffi cient amount of tick data to ascertain validity of the concept. Back-test best practices are discussed in Chapter 16 of this book. The model is tested on "out-of-sample" or "clean" swath of data, a series of quotes and trades unused in the initial proof of concept activity. If the model performs satisfactorily out-of-sample, the model is moved into paper trading. Models that fail the back-test are generally discarded.

Following a successful back-test, the models are moved into the preproduction or paper-trading phase. Paper trading emulates real-time trading activity without placing actual orders, but keeps track of the orders in a program-generated log. Except for the order-placement functionality, the paper-trading phase is typically a fully programmed HFT system. As such, the paper-trading stage is a perfect "sandbox" for testing all other aspects of the HFT system: data receipt and processing, runtime generation of trading signals, position accounting, archiving of data, and risk management. To ascertain the correctness of the paper HFT system, the back-test algorithm is typically run at the end of each trading day on data collected in paper trading—any deviations observed between the back-test and paper trading are noted and investigated.

When paper trading and the back-test are properly programmed, both should deliver identical results. A month of clean paper trading fully reconciled with back-test results is usually considered to be suffi cient to move the system into a low-amount live trading or "production."

The transition to production is often loaded with its own set of challenges, described in detail in Chapter 16. Trade execution and real-time portfolio accounting can be complex coding exercises, and have to be executed perfectly to avoid unexpected malfunctions and losses. Extended production runs with little capital at stake help iron out various code issues and ensure a smooth and eff ective trading functionality.

■ Quant HFT model development/proof of concept including back-tests: 15 percent Quant HFT models, the core examples of which are described in Chapters 8 through 11 of this book, are the road maps for trading. The output of quant models is a set of persistent indicators built to identify trading opportunities.

■ Risk management principles, model validation and policy development: 10 percent Competent risk management, discussed in Chapter 14, prevents seemingly harmless glitches in the code, market data, market conditions, or the like from throwing off trading dynamics and causing large losses. The objective of risk management is to assess the extent of potential damages and to create infrastructure to mitigate damaging conditions during run-time, and to build a system of warnings, failure breaks, and processes with the goal to eliminate or limit the potential damage. Some risk management processes may be built into the code, while others require a human presence to ensure a failure-safe operation.

■ Coding of trading and risk-management infrastructure: 40 percent

Coding trading and risk-management signals comprises the primary focus of HFT development. High-frequency execution systems tend to be complex entities that detect and react to a variety of market conditions. Most HFT systems today are built to be "platform independent"—that is, to incorporate flexible interfaces to multiple broker-dealers, electronic communication networks (ECNs), and exchanges. This independence is accomplished through the use of the Financial Information eXchange (FIX) language, a special sequence of codes optimized for financial trading data. With FIX, at the flip of a switch the routing can be changed from one executing broker to another or to several brokers simultaneously. Best coding practices are described in Chapter 16.

FIX can be quite cumbersome, as discussed in Chapter 2. To counteract the delay in speed induced by the complexities of FIX, several providers have rolled out proprietary communication protocols and application programming interfaces (APIs). The proprietary structures also have the effect of making it difficult for traders to switch platforms, thus capturing the audience. The extent of work required to adapt to a given platform can be extensive, however, and some providers even offer monetary incentives for traders interested in building out connectivity. Some divisions of Deutsche Börse, for example, may offer as much as \$65,000 to prospective traders to defray the interface implementation costs.

■ System testing: 20 percent

System testing is another critical component, discussed in detail in Chapter 16. To ensure thorough testing, the system is run through various scenarios, or "scripts." Professional software testers are typically deployed to examine each block of code, to compare its performance with its stated mandate, and to document all discrepancies, known as "bugs." Testers are often compensated about one third as much as coders. Separating coding and testing duties also ensures proper testing, free of face-saving whitewashing gaffes that can ultimately cost the business significant money.

■ run-time monitoring: 5 percent

run-time monitoring is another HFT task requiring personnel. The task of monitoring a well-defi ned HFT system with clear risk management parameters and escalation procedures is not particularly involved, but requires close attention to detail. separate personnel are typically tasked with the duty of watching the systems and ensuring that run-time performance remains within acceptable limits. Best practices for HFT monitoring are discussed in Chapter 16.

■ Compliance and other administrativia: 10 percent

Compliance and other administrative tasks are a function of all trading businesses. Keeping track of regulatory guidelines, documentation, and all other related activities is a full-time job.

The proportion of time spent on each task outlined here varies with the stage of HFT business development, as shown in Figure 7.2. In the start-up phase, HFT businesses tend to be data and programming centered. In the ramp-up stage, testing, risk management, and monitoring take the majority of eff ort. Finally, in steady-state production, it is monitoring, compliance, and other administrative tasks that take the majority of time.

In the traditional broker-dealer world, where the word *technology* is often associated only with new shiny gadgets provided by technology teams far removed from business, tasks such as system testing and policy development may seem like an unnecessary expense. By separating technology from the business, the management creates an impression that traders need not feel accountable for the systems they are using. real-life examples, such as the Knight Capital fi asco that occurred in the summer of 2012, have shown that thorough testing, compliance, and monitoring of HFT systems are key to the long-term profi tability of the business. These functions follow directly from the best practices of software development, discussed in detail in Chapter 16.

As Figure 7.2 illustrates, development of an HFT business follows a process unusual for most traditional trading desks. designing new HFT strategies is costly; executing and monitoring fi nished high-frequency products costs close to nothing. By contrast, a traditional proprietary trading businesses incurs fi xed costs from the

![](_page_3_Figure_7.jpeg)

**FIGURE 7.2** Allocation of Man-Hours during diff erent Phases of HFT development

![](_page_4_Figure_0.jpeg)

**FIGURE 7.3** The Economics of High-Frequency versus Traditional Trading Businesses

moment an experienced senior trader with a proven track record begins running the trading desk and training promising young apprentices, through the time when the trained apprentices replace their masters.

Figure 7.3 illustrates the cost curves for rolling out computerized and traditional trading systems. The cost of traditional trading remains fairly constant through time. With the exception of trader "burnouts" necessitating hiring and training new trader staff , costs of staffi ng the traditional trading desk do not change. developing computerized trading systems, however, requires an up-front investment that is costly in terms of labor and time. one successful trading system takes on average 36 months to develop. The costs of computerized trading decline as the system moves into production, ultimately requiring a small support staff that typically includes a dedicated systems engineer and a performance-monitoring agent. Both the systems engineer and a monitoring agent can be responsible for several trading systems simultaneously, driving the costs closer to zero.

#### ■ **Financial Markets Suitable for HFT**

A wide range of securities and market conditions fi t the profi le for trading at high frequencies. some securities markets, however, are more appropriate than others.

To be appropriate for this type of trading, two requirements must be met: the ability to quickly move in and out of positions and suffi cient market volatility to ensure that changes in prices exceed transaction costs. The volatilities of diff erent markets have been shown to be highly interrelated and dependent on the volume of macroeconomic news reaching the markets. The ability to quickly enter into positions as well as to close them is in turn determined by two factors: market liquidity and availability of electronic execution.

Liquid assets are characterized by readily available supply and demand. Liquid securities such as major foreign exchange pairs are traded 24 hours a day, 5 days a week. Less liquid securities, such as penny stocks, may trade only once every few days. Between trades, the prices of illiquid assets may change substantially, making less liquid securities more risky as compared with more liquid assets.

High-frequency strategies focus on the most liquid securities; a security requiring a holding period of 10 minutes may not be able to find a timely reasonably-priced counterparty in illiquid markets. While longer-horizon investors can work with either liquid or illiquid securities, Amihud and Mendelson (1986) show that longerhorizon investors optimally hold less liquid assets. According to these authors, the key issue is the risk/return consideration; longer-term investors (already impervious to the adverse short-term market moves) will obtain higher average gains by taking on more risk in less liquid investments.

A perfectly liquid market is the one where the quoted bid or ask price can be achieved irrespective of the quantities traded (see Bervas, 2006, for detailed treatment of the subject). Market liquidity depends on the presence of limit-order traders in the market, as well as the counterparties' willingness to trade. The market participants' willingness to trade in turn depends on their risk aversions and expectations of impending price movements, along with other market information.

One way to compare the liquidity of different securities is to use the average daily volume of each security as the measure of liquidity. In terms of daily average trading volume, foreign exchange is the most liquid market, followed by recently issued U.S. Treasury securities, then equities, options, commodities, and futures. Swaps, traditionally traded over the counter (OTC), but entering the electronic era under the Dodd-Frank Act, are on their way to become the most liquid and optimal market for HFT.

#### ■ **Economics of HFT**

# **Costs of Doing HFT Business**

The cost drivers in an HFT business are data, labor, equipment and software, trading costs, administrative and legal costs, and, most important, trading losses. Effective risk management, monitoring, and compliance frameworks, discussed in Chapters 14 and 16 are required to limit the latter. This section describes the costs of doing business that are not attributable to risk.

# **Costs of Data**

Data tend to be either very expensive or entirely free. Multiple companies, like Reuters and Bloomberg, offer tick data for sale for a significant premium. Brokerdealers and trading venues may offer quality tick data free of charge to prospective traders. Start-up HFT firms will need to obtain at least two years of historical data in the instrument of choice to generate initial trading models.

Hardware As discussed in Chapter 2, hardware costs are the least prominent component of HFT operating expenses. The most basic, yet effective, HFT setup involves computers commonly available at retail stores. A professional operating system, like Windows 7 or Red Hat Linux, is necessary for thorough configuration and remote access. It is wise to purchase separate machines for development, testing, and production, to minimize incidents of unintentional code manipulation and overloads of processing power.

Connectivity Connectivity is important for any successful HFT operation: a fast connection with a sufficient bandwidth ensures that the trading operation receives the fullest set of quotes and trades: as described in Chapter 2, quotes in particular can be lost in cyberspace congestion. Connectivity options involve

- Co-location
- Proximity
- Run-of-the-mill connections

Co-location or "colo" is offered by exchanges and other trading venues in their dedicated facilities, and typically includes a secure "cage" for the HFT server, a power source, and an actual network "wire" connecting the HFT and the exchange servers, most often via a dedicated line. High-frequency traders are free to configure the server anyway they like, and may include remote accessibility.

Proximity services are similar to co-location, except they are run by third-party companies with access to facilities located close to trading venues, but not in the same facility as trading venues. Like co-location, proximity offers a cage for servers, a power source, and a fast wire (typically, a fiber-optic hookup). The wire, however, connects to the exchange via the general Internet, making proximity less secure than co-location.

Finally, a shoestring HFT start-up can survive on a premium cable network as well until its systems become consistently profitable. The common network, however, is subject to extreme congestion, resulting in serial quote losses and information and trading delays.

Software HFT operations deploy the following software that may or may not be built in-house:

- Computerized generation of trading signals is the core functionality of an HFT system. The generator accepts and processes tick data, generates portfolio allocations and trade signals, and records profit and loss (P&L). Generators are most often built in-house and kept in utmost secrecy. The secrecy requirement stems from purely competitive business considerations: every investment strategy has a finite capacity, and a competitor armed with a generator code is bound to significantly diminish or outright destroy profitability of an HFT strategy.
- Computer-aided analysis is done with financial modeling software deployed by HFT operations to build new trading models. MatLab and R have emerged as the industry's most popular quantitative modeling choices. MatLab can be pricey, but is well known in the industry. R, however, is free: it is an open-source software that is efficient, and, best of all, can be extended with proprietary libraries. Citigroup, for example, now runs almost all of its modeling in R.

- Internet-wide information-gathering software facilitates high-frequency fundamental pricing of securities. Promptly capturing rumors and news announcements enhances forecasts of short-term price moves. Thomson Reuters, Dow Jones, and newcomers like RavenPack, SemLab and AbleMarkets.com offer a range of products that deliver real-time news in a machine-readable format.
- Trading software incorporates optimal execution algorithms for achieving the best execution price within a given time interval. This software enables traders to time trades, decide on market aggressiveness, and size orders into optimal lots. Development and per-trade licensing of best execution algorithms is now the bread and butter of many broker-dealers. Yet independent companies have sprung up to help investors distribute their orders in the most efficient manner. For example, the New York–based MarketFactory provides a suite of software tools to help automated traders get an extra edge in the foreign exchange market. Furthermore, an increasing number of traditional buy-side investors, like large pension funds and hedge funds, have developed their own suites of best execution algorithms in a bid to bypass broker-dealers altogether. Chapter 15 discusses the latest developments in best execution.
- Run-time risk management applications ensure that the system stays within pre-specified behavioral and P&L bounds, as discussed in detail in Chapter 14. Such applications may also be known as system-monitoring and faulttolerance software and are often built in-house, but are generic enough to buy off the shelf. The advantage of buying third-party risk software is the reliability of the modules. The third-party software undergoes diligent review by multiple customers and, as a result, may be more sound than anything built in-house.
- Desktop and mobile applications designed for monitoring performance of HFT systems are a must for all modern HFT organizations. Any issues, breaches of risk limits, power outages, or any other problems should be immediately related to responsible parties. Like risk-management systems, performance monitoring and compliance systems tend to be generic enough to warrant purchasing well-tested third-party software.
- Real-time third-party research can stream advanced information and forecasts. Sometimes, these forecasts can be incorporated into a trading system in a useful manner. For example, a forecast that warns of an imminent crash can be used to enhance a liquidity provision HFT system. AbleMarkets.com and HFTindex.com provide this kind of information.

Electronic Execution HFT practitioners may rely on their executing brokers and ECNs to quickly route and execute their trades. Goldman Sachs and Credit Suisse are often cited as broker-dealers dominating electronic execution. UBS, Barclays and Quantitative Brokers have been the go-to venues for foreign exchange and fixed income.

Execution providers typically charge a per-trade fee, known in advance. The total costs may, however, include other unobservable components that vary from broker to broker, as Chapter 5 describes in detail. Understanding the cost structure of execution is especially important in high-frequency settings where the sheer number of transactions can eliminate gains.

Custody and Clearing In addition to providing connectivity to exchanges, broker-dealers typically offer special "prime" services that include safekeeping of trading capital (known as *custody*) and trade reconciliation (known as *clearing*). Both custody and clearing involve a certain degree of risk. In a custody arrangement, the broker-dealer takes the responsibility for the assets, whereas in clearing, the broker-dealer may act as insurance against the default of trading counterparties. Broker-dealers and trading venues charge custody and clearing fees.

Staffing Costs Initial development of high-frequency systems is both risky and pricey, and the staff required to design trading models needs to understand PhD-level quantitative research in finance and econometrics. In addition, programming staff should be experienced enough to handle complex issues of system interoperability, computer security, and algorithmic efficiency.

Administrative and Legal Costs Like any business in the financial sector, highfrequency traders need to make sure that "all i's are dotted and all t's are crossed" in legal and accounting departments. Qualified legal and accounting assistance is therefore indispensable for building a capable operation.

# **Capitalization of HFT**

As with any other form of trading, an HFT firm can be capitalized with equity and leverage. The initial equity normally comprises contributions from the founders of the firm, private equity capital, private investor capital, or capital of the parent company. The amount of the initial equity required depends on many factors, but can be approximated using the following variables:

- Profitability of the HFT strategy to be traded with live capital.
- Cost structure of the trading operation.
- Sharpe ratio of the strategy.
- Maximum drawdown of the strategy.

The profitability of the HFT strategy describes the "gross" return on every dollar invested. The gross return does not account for trading costs and presents a high-level picture of potential profitability. During the earliest stages of investment, back-test performance can be used as potential future performance. Great caution, however, should be used: back-tests often fail to account for basic costs and market impact of the strategy itself, reducing production profitability. Worst of all, back-tests can be simply wrong, either due to unrealistic assumptions or coding mistakes that may not be exposed until the code is transferred into production.

Strategies that do well in gross performance terms are subject to significant costs. In high-frequency settings, per-trade gains are typically small compared to the transaction costs, which can easily annihilate any semblance of profitability. This is particularly true in the start-up phases of operation, when the traded notional is often small. As described in Chapter 5, trading costs are often larger when the traded amount is small and vice versa. For example, a common retail brokerage charges \$20 per every leg of the trade with notional of \$40,000 and less, or more than 0.05 percent of the notional. And every trade has two legs: one to open a position, and one to close, emptying a retail trader of 0.1 percent per every round-trip trade. At the same time, a large institution faces costs of as little as \$3 or \$5 for every \$1 million traded—just 0.0005 percent of the notional, a cost 100 times smaller than the one offered to the retail investors.

When the available capital is small, it often can be "levered." Leverage most often refers to borrowed funds collateralized by the traded financial instruments. Thus, with a 1:9 leverage, a \$100,000 investment becomes \$1 million trading notional, possibly obtaining lower transaction costs and retaining better profitability. In addition, leverage helps multiply gains of the strategy. A 0.1 percent return on \$100,000 is \$100 without leverage. When the strategy is traded with a 1:9 leverage, the \$0.1 percent return becomes a \$1 million × 0.1 percent = \$1,000 or 1 percent return on the \$100,000 investment, a significant improvement. Of course, when the strategy loses money, its losses are also multiplied accordingly: what is a \$100 loss in an unlevered \$100,000 notional extends to a \$1,000 loss with a 1:9 leverage.

Broker-dealers are the most natural providers of leverage: they can observe the trader's positions in real time and ensure return of their capital by liquidating said trader's positions. Liquidation happens when the trader's account value falls below a safety collateral value known as *margin.* Margin requirements vary from broker to broker, but typically designate a certain percentage of the traded notional to be in the account at all times. Margin requirements are not, however, written in stone and can be negotiated on an account-by-account and even situation-by-situation basis.

To avoid liquidation, traders can optimize the leverage that works best for each strategy. Maximum drawdown and Sharpe ratio metrics help traders determine how much leverage the trader can afford given the volatility of his strategy and the maximum downside recorded in historical data.

In addition to leverage, later-stage equity can be a source of trading capital, and it can be obtained from established institutions, such as bank asset management divisions, fund-of-funds, pension funds, large hedge funds interested in boosting their performance, and the like.

From the perspective of a large institutional investor, possibly looking to invest into a high-frequency operation, most HFT tends to fall into the category of "alternative" investments. The term *alternative investments* describes most strategies under a broader hedge fund umbrella; the term is used to distinguish strategies from "traditional" investments, such as long-only mutual funds and bond portfolios. As a result of its alternative status, HFT strategies are candidates for inclusion in larger institutional portfolios. To qualify for institutional investment, HFT managers need to deliver a one- to three-year auditable performance track record of 8 to 12 percent per annum, with as little volatility as possible.

The compensation of HFTs then follows the hedge fund model: HFT managers are paid management and performance fees. Management fees are typically fixed percentages of the notional amount invested. The performance fees are percentages of the gain above the previous highest value of the fund shares, known as high water *mark.* Just as with any other hedge fund manager, the performance fee is paid to a high-frequency manager only when the manager increases (or has increased) the value of the fund shares, creating an incentive to outperform.

Due to its relative novelty, HFT is often treated as an "emerging manager" business. The "emerging" label typically results in higher perceived risk as far as strategy longevity is concerned, from the institutional investor's point of view. This, in turn, translates into higher performance, but lower management fees. Where an arbitrary hedge fund may command 2 percent management fee and 20 percent performance fee (the classic "2-and-20" model), high-frequency traders often offer a "1-and-30" model, with 1 percent of all assets under management serving as a compensation for administrative activity, and 30 percent of above-the-highest-water mark gains paid as a performance incentive.

#### Leverage of HFT

How much leverage can an HFT business sustain and remain viable? The quick answer to this question depends on two performance variables characteristic to each HFT strategy: Sharpe ratio and maximum drawdown. The beauty of the Sharpe ratio lies in its invariance with respect to leverage: a Sharpe ratio of an unlevered HFT strategy is exactly the same as the Sharpe ratio of an HFT strategy levered 100 times. This is due to the structure of the high-frequency Sharpe ratio: no levered HFT positions are held overnight, so the HFT Sharpe ratio does not include the risk-free rate in the numerator, as pointed out in Chapter 6. When the Sharpe ratio increases, the expected return in the numerator and the volatility in the denominator of the ratio increase proportionally by the amount of leverage,  $L$ :

$$SR^{HFT} = \frac{\mathbb{E}\left[R_{annualized}\right]}{\sigma\left[R_{annualized}\right]} = \frac{\mathbb{E}\left[R_{annualized}\right] \cdot L}{\sigma\left[R_{annualized}\right] \cdot L} \tag{1}$$

The expected return of the high-frequency operation must take into account the costs of doing business, so the Sharpe ratio of an HFT business is adjusted for expenses:

$$SR^{HFT\,Ops} = \frac{\mathbb{E}\left[R_{annualized}\right] \times L \times (Capital) - (Annualized Expenses)}{\sigma\left[R_{annualized}\right] \times L \times (Capital)}$$
(2)

or, using daily data, and assuming 250 trading days per year:

$$SR^{HFT\,Ops} = \frac{\mathbb{E}\left[R_{daily}\right] \times L \times (Capital) - (Daily\,Expenses)}{\sigma \left[R_{daily}\right] \times L \times (Capital)} \sqrt{250} \tag{3}$$

Expressions in equations (2) and (3) have to be positive for a profitable business, yet the leverage value  $L$  cannot be increased infinitely. Annualized volatility is only the average measure of return variability. The actual realizations of losses can be much more severe. To determine the minimum Sharpe ratio  $SR^{HFT \;Ops}$ required for a stable operation, a maximum drawdown comes in as a convenient metric.

Assuming that the historical maximum drawdown can occur in 10 percent of worst-case scenarios, the required Sharpe ratio  $SR^{HFT \textit{Ops}}$  is related to the number of standard deviations the historical maximum drawdown lies away from the mean of returns:

$$\frac{\text{Max}\$\text{Drawdown}}{\text{Capital}} > \text{SR}^{\text{HFTOps}} \times \sigma\left[R_{\text{annualized}}\right] \times L - 1.645 \times \cdot \sigma\left[R_{\text{annualized}}\right] \times L \quad (4)$$

from where the minimum  $SR^{HFT \,Ops}$  can be obtained as

$$SR^{HFT\,Ops}_{min} = \frac{Max\$\nDrawdown/Capital + 1.96 \cdot \sigma[R_{annualized}] \cdot L}{\sigma[R_{annualized}] \cdot L}$$
(5)

For a levered strategy to remain solvent, the Sharpe ratio takes into account operating costs  $SR^{HFT \textit{Ops}}$  that have to exceed  $SR^{HFT \textit{Ops}}_{\textit{min}}$  determined by equation (5). Figure 7.4 presents gross cumulative performance of a sample high-frequency strategy. The strategy delivers a gross Sharpe ratio of 2.78 with a maximum drawdown of 0.93 percent incurred in July 2012, and daily volatility of 0.15 percent computed over the sample history of the strategy. The minimum operational Sharpe ratio  $SR^{HFT \,Ops}$  this strategy delivers when levered has to exceed  $SR^{HFT \,Ops}_{min}$  of equation (5), computed to be 1.41. If this particular strategy is allocated \$10 million in capital and allowed a nine-to-one leverage,  $L = 10$ , then the maximum daily spending of the operation cannot exceed \$13,730, or \$3,432,729 for 250 trading days per year. This number is considerably smaller than the number computed from the daily average return: if the risk of going bankrupt via maximum drawdown is ignored completely, then the expected levered performance is computed as the annualized average daily return multiplied by capital and leverage:

$$E\left[Gain_{naive}\right] = E\left[R_{\text{daily}}\right] \times 250 \times Capital \times Leverage \tag{6}$$

If computed using equation (6), the naïve gain works out to be nearly \$6,959,034-a misleading number to spend when the risk of drawdown is taken into account.

If a stricter performance measure is required, whereby the observed maximum drawdown occurs in less than 5 percent of all cases, equation (5) can be rewritten as

$$SR^{HFT\,Ops}_{min} = \frac{MaxDrawdown/Capital + 1.96 \cdot \sigma[R_{annualized}] \cdot L}{\sigma[R_{annualized}] \cdot L}$$
(7)

where number of standard deviations where maximum drawdown is located has changed from 1 to 3. For the \$10 million capital deployed in strategy with the

![](_page_12_Figure_0.jpeg)

**FIGURE 7.4** HFT Industry Participants

minimum operational sharpe ratio of 2.41, for example, the maximum allowable annual expense is \$931,801.

An HFT operation is more likely to survive and prosper if it has leverage and high sharpe ratios. High leverage increases the likelihood of covering costs, and the high sharpe ratio reduces the risk of a catastrophic loss.

#### ■ **Market Participants**

Like any other industry, HFT is subject to outside forces and infl uences. Figure 7.4 summarizes the playing fi eld of HFT. The remainder of the section discusses market participants in detail.

# **Competitors**

HFT fi rms compete with other, more traditional, investment management fi rms, as well as market-making broker-dealers. The competition with traditional mutual and hedge funds centers on attracting investment. The rivalry with quantitative hedge funds and other high-frequency trading fi rms also includes recruitment of talented and experienced strategists and technologists, as well as direct contest for market ineffi ciencies. Likewise, the battle with traditional non-HFT broker-dealers involves turf wars over "fi rst dibs" access to profi t opportunities in the traditional market-making arena.

# **Investors**

Investors in HFT include funds-of-funds aiming to diversify their portfolios, hedge funds eager to add new strategies to their existing mix, and private equity fi rms seeing a sustainable opportunity to create wealth. Most investment banks off er leverage through their "prime" services.

# **Services and Technology Providers**

Like any business, a high-frequency trading operation requires specific support services. Most common and, in many cases, critical providers to the high-frequency business community include providers of data, hardware, connectivity, software, execution, custody, clearing, staffing, and administrative and legal services, described in more detail earlier in this chapter.

# **Government**

Several regulatory initiatives were under way around the world at the time this book was written. Chapter 13 summarizes the latest regulatory thought.

#### ■ **Summary**

Developing a high-frequency business involves challenges that include issues surrounding the "gray box" or "black box" nature of many systems. The low transparency of fast and complex algorithm decisions requires diligent risk management and monitoring processes, and constant human supervision. The deployment and execution costs decrease considerably with time, leaving the profit-generating engines operating consistently, with no emotion, sickness, or other human factors. Well-designed and -executed high-frequency systems, capitalizing on multiple short-term moves of security prices, are capable of generating solid profitability in all types of electronic markets.

#### ■ **End-of-Chapter Questions**

- 1. What are the key steps in algorithm development?
- 2. How much time is spent on monitoring in a stable HFT operation?
- 3. What kind of operational costs can an HFT with \$100 million in capital and a net (after transaction costs) Sharpe ratio of 1.5 carry?
- 4. What is the minimum capital needed for a breakeven of an HFT with the following characteristics:
  - a. Net (after transaction costs) Sharpe ratio of 2.8
  - b. Three full-time officers earning \$150,000 per year each
  - c. Office overhead (office space, networking and computer expenses) of \$72,000 per year
  - d. Co-location of \$36,000 per year
- 5. Who are the HFT industry participants?
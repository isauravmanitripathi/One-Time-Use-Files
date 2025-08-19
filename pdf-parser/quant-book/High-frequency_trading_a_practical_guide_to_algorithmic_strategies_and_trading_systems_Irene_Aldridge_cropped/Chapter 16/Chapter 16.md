# Implementation<br>of HFT Systems

 $\mathbf{T}$ igh-frequency trading (HFT) systems tend to be "mission-critical applications,"  $\blacksquare$  comparable with software piloting NASA shuttle launches and having little room for error. This chapter describes best practices of implementing accurate and reliable HFT systems.

#### Model Development Life Cycle

HFT systems, by their nature, require rapid hesitation-free decision making and execution. Properly programmed computer systems typically outperform human traders in these "mission-critical" trading tasks, particularly under treacherous market conditions—see Aldridge (2009b), for example. As a result, computer trading systems are rapidly replacing traditional human traders on trading desks around the world.

The development of a fully automated trading system follows a path similar to that of the standard software development process. The typical life cycle of a development process is illustrated in Figure 16.1.

A sound development process normally consists of the following five phases:

- 1. Planning
- 2. Analysis
- 3. Design
- 4. Implementation
- 5. Maintenance

The circular nature of the process illustrates the continuous quality of system development. When a version of the system appears to be complete, new issues demand advanced modifications and enhancements that lead to a new development cycle.

The purpose of the planning phase is to determine the goals of the project as well as to generate a high-level view of what the completed project may look like. The

![](_page_1_Figure_0.jpeg)

**FIGURE 16.1** Typical Development Cycle of a Trading System

planning is accompanied by a feasibility study that evaluates the project in terms of its economics, operating model, and technical requirements. The economical considerations explore whether the project has a suffi cient profi t-and-loss (P&l) potential, whereas operational and technical issues address the feasibility of the project from the compliance, human resources, and other day-to-day points of view. The outputs of the planning phase include concrete goals and targets set for the project, established schedules, and estimated budgets for the entire system.

During the analysis stage of the process, the team aggregates requirements for system functionality, determines the scope of the project (which features are in and which features are out of the current release), and solicits initial feedback from users and management. The analysis stage is arguably the most critical stage in the development process, because it is here that stakeholders have the ultimate ability to shape the functionality of the system given the allocated budget.

The design phase incorporates detailed specifi cations of functionality, including process diagrams, business rules, and screenshots, along with other output formats such as those of daily reports and other documents. An objective of the design stage is to separate the whole project into discrete components subsequently assigned to teams of software developers; the discrete components will have well-specifi ed interfaces that can lock in seamlessly with other components designed by diff erent teams of software developers. Such early specifi cation of software packaging of internal computer modules streamlines future communication among diff erent software development teams and enables smooth operation of the project going forward. The design phase also outlines test cases—that is, the functionality paths that are later used as blueprints to verify the correctness of the completed code.

The implementation phase, fi nally, involves actual programming; the software teams or individual programmers develop software modules according to the specifi cations defi ned in the design stage. The individual modules are then tested by the development teams themselves against the predefi ned test cases. When the project management is satisfi ed that the individual modules have been developed according to the specifi cations, the project integration work begins. Integration, as its name implies, refers to putting together the individual modules to create a functional system.

While successfully planned projects encounter little variance or problems in the integration stage, some work still remains. Scripts may have to be written to ensure proper communication among various system components, installation wrappers may have to be developed, and, most important, the system has to be comprehensively tested to ensure proper operation. The test process usually involves dedicated personnel other than the people who developed the code. The test staff diligently monitors the execution of each functionality according to testing procedures defi ned in the design stage. The test personnel then documents any "bugs"—that is, discrepancies between the prespecifi ed test case performance and observed performance. The bugs are then sent back over to the development team for resolution and are subsequently returned to the testing teams.

Successful implementation is followed by the deployment and subsequent maintenance phase of the system. The maintenance phase addresses system-wide deviations from planned performance, such as troubleshooting newly discovered bugs.

#### ■ **System Implementation**

# **Key Steps in Implementation of high-Frequency Systems**

Most systematic trading platforms are organized as shown in Figure 16.2. This section discusses each component of the process in detail.

![](_page_2_Figure_5.jpeg)

**FIGURE 16.2** Typical High-Frequency Process

Step 1: The Core Engine The core engine is composed of one or several run-time processors that contain the core logic of the trading mechanism and perform the following functions:

- Receive, evaluate, and archive incoming quotes.
- Perform run-time econometric analysis.
- Implement run-time portfolio management.
- Initiate and transmit buy and sell trading signals.
- Listen for and receive confirmation of execution.
- Calculate run-time P&L.
- Dynamically manage risk based on current portfolio allocations and market conditions.

Most of the high-frequency production-bound systems are written in C++, although some high-frequency trading firms are known to use Java and Q, a commercial hybrid of language syntax and database organization distributed by Kx Systems. The matching engine of Nasdaq OMX, for example, is said to be written in Java, yet the code disables "garbage collection," a core functionality of Java that distinguishes it from C++, but also slows down the systems. C++ is often considered to be "lighter" and "faster" than Java, meaning that C++ programs do not have the processing power overhead required by Java; as a result, C++ systems often work faster than Java-based systems.

The core engine and the portfolio management framework then initiate and transmit orders to the broker-dealer. Upon receiving and executing an order, the broker-dealer sends back the order status and order-filling price and size to the client. The system then calculates the P&L and assesses risk management parameters that feed back into the portfolio management piece.

The design and implementation of run-time portfolio management reflects the core econometric engine. In addition to the raw quote inputs, the portfolio management framework incorporates inputs from the econometric model, current position sizes, and other information relevant to portfolio diversification and maximization of portfolio returns, while minimizing portfolio risk.

Incoming quotes, along with outgoing orders and any other communication between a broker-dealer and a client or an exchange, are most often transmitted via the Financial Information eXchange (FIX) protocol specifically designed for transmission of real-time financial inform[ation. Other protocols,](http://www.fixprotocol.org) like FAST and Nasdaq's proprietary ITCH and OUCH, are also used.

According to the FIX industry web site (www.fixprotocol.org), FIX emerged in 1992 as a bilateral communications framework for equity trading between Fidelity Investments and Salomon Brothers. It has since become the dominant communication method among various broker-dealers, exchanges, and transacting customers. In fact, according to a survey conducted by fixprotocol.org, FIX was used for systematic trading by 75 percent of buy-side firms, 80 percent of sell-side firms, and over 75 percent of exchanges in 2006.

FIX is best described as a programming language that is overseen by a global steering committee, consisting of representatives from banks, broker-dealers, exchanges, industry utilities and associations, institutional investors, and information technology providers from around the world. Its standard is open and free. Implementation of a communication process via FIX, however, requires careful planning and dedicated resources and may demand significant expense, much like any other system development process.

A typical FIX message is composed of a header, a body, and a trailer. The header always contains the following three fields: a string identifying the beginning of a message (FIX field # 8), the number of characters in the body of the message to follow the message header (FIX field # 9), and the type of the message (FIX field # 35). Among many message types are quotation and order execution directives and acknowledgments as well as housekeeping messages designed to ensure that the system remains up and running.

For example, MsgType = 0 is the "Heartbeat" message—a message is sent to the other communication party to ensure that the communication connection remains operational and has not been lost as a result of any unforeseen technical problems. The heartbeat message is typically sent after a prespecified number of seconds of inactivity. If either communication party has not received a heartbeat message from the other party, it sends a TestRequest message (MsgType = 1) to "poll" the other communication party. If no heartbeat message is received following a TestRequest message, the connection is considered lost and steps are taken to restart it.

MsgType = 6 is known as "Indication of Interest." Exchanges and broker-dealers use Indication of Interest messages to transmit their interest in either buying or selling in either a proprietary or an agency capacity. MsgType = R indicates a "Quote Request" message with which a client of a broker-dealer requests a quote stream. Under normal circumstances, the broker-dealer responds to the Quote Request message with a continuous stream of Quote messages (MsgType = S) that carry actual quote information, such as bid or ask prices.

Other message types include orders such as single-name orders, list orders, day limit orders, multiday orders, various cancellation requests, and acknowledgments. All fields in the body are included in the following format:

[Field #] = [data]

For example, to communicate that the message carries the status of an order, the following sequence is used:

35 = 8|

All field sequences are terminated with a special character that has a computer value of 0x01. The character looks like "|" when seen on-screen.

The body of the message contains the details of the message, whether it is a quote request, a quote itself, or order and trade information. The message body further specifies the exchange of interest, a timestamp that includes milliseconds, a security symbol, and other necessary transaction data. Like the header, all fields in the body are included in the following format:

[Field #] = [data]

and each field sequence is terminated by a special computer character 0x01.

Finally, at the end of the body of every message is the "checksum"—a sum of digital values of all the characters in the message included as a verification of whether the message has arrived in full. An example of a FIX message is shown in Chapter 2 of this book.

The risk management functionality can include the following components: tracking the basic components of the system performance and generating warning messages should the performance limits be breached. Appropriate risk management parameters may include message count limits per unit time, P&L parameters, and other variables discussed in detail later in this chapter.

Step 2: Quote Archival Most quotes are accepted and archived using proprietary FIX engines that are tested with various message scenarios. The quotes are next archived for reconciliation and simulation purposes.

As discussed in Chapter 2, quote delivery over the public networks can be unreliable: the User Datagram Protocol (UDP) over which some quotes are broadcast does not guarantee point-to-point delivery. As a result, an HFT without co-location may lose quotes. Furthermore, variations in quote-receiving technology from one entity to the next do not guarantee that each entity's recorded datastream will be identical to that of the next entity. In some cases, purchased tick data may not be completely representative of the quote process archived by the data buyer from his own quote interface. While purchased historical data fills an important informational void when a researcher has no data, best practices suggest that each trading entity will benefit most from the internally archived data as such data will be most representative of the data received by the system during production.

Most firms with serious HFT needs archive all received and sent messages in text or binary file formats. The text file, known as a *flat file* in the industry, is the simplest form of storage. The flat file is readable by humans without special translation. The fields in the file can be comma or tab separated, and can be easily loaded into Excel or opened with Notepad on PCs or plain text editors on LINUX. Binary files, commonly referred to as *Large Binary OBjects*, or *BLOBs*, are recorded in hexadecimal (Hex) characters readable by machines. At the expense of readability, BLOBs are faster and much more compact than flat files. Interdealer broker ICAP's foreign exchange matching engine, for example, records all ticks in a continuous weekly BLOB. Along with foreign exchange markets, each ICAP's BLOB begins on Sunday night and ends on Friday night, New York time. Each such BLOB can occupy as much as a terabyte of storage space. Such storage requirements could have been prohibitively expensive just 10 years ago, yet today such storage is very reasonable. Various incarnations of Storage Area Networks (SANs) allow seamless access to stored data.

Many databases have attempted to crack the market for archiving real-time highfrequency data, and replace flat files with their products. Most databases are unsuitable to HFT because in HFT the most time-sensitive functionality is data archival. Slow input/output operation delays execution of the trading engine, compromising performance of the HFT system. Retrieval of tick data occurs only at the simulation level where execution time is not a critical parameter. Most databases, however, are optimized to efficiently retrieve data, and not to enter it into the system. KDB, Step 3: Posttrade Analytics The best HFT systems do not stop there. A posttrade analysis engine reconciles production results with simulation results run with the same code on the same data and updates distributions of returns, trading costs, and risk management parameters to be fed back into the main processing engine, portfolio optimization, and risk management components.

Step 4: Simulation *Simulation* refers to a make-belief execution of a trading strategy. Simulation is important for one key reason: it allows researchers to test a strategy within a short time span, without risking actual capital. A strategy that works well in simulation has a chance on actual money, in "production." Conversely, a strategy that fails in simulation will be hard-pressed to deliver positive results in a real trading environment.

The simulation engine is an independent module that tests new trading ideas on past and run-time data without actually executing the trades. Unlike ideas that are still in the early stages of development that are often coded in MatLab or even Excel, ideas tested in the simulation engine are typically coded in the production language (C++ or Java).

Simulation produces an approximation of real-life trading, and only if the execution part of simulation is programmed correctly. Specifically, execution of market and limit orders requires different treatment. A market order submitted in simulation can be assumed to be executed at the prevailing quote at the time the market order is submitted. Thus, a market buy order can be assumed to be filled at the best ask, providing that the size of the market order is smaller than the size of the best ask queue. Similarly, a small market sell order can be assumed to be executed at the best bid.

The best-quote assumptions about execution of market orders, however, will most of the time overstate performance of the trading system. In live trading, market orders will incur MI or slippage, resulting in worse prices than predicted by the best bid and best offer (for more details on market impact, please see Chapter 5). To better approximate the live trading results, the HFT researcher can estimate the average MI per unit trade size, and then adjust the best quotes by the estimated values of the MI. The market buy orders will then be considered executed at the prevailing ask plus the expected size-dependent MI, closer reflecting real-market conditions and applying a great degree of conservatism to simulation. Similarly, the market sell orders will be expected to execute at the best bid less MI estimation.

Simulation of execution of limit orders is also complex. A limit order can be considered to be executed only when the market price "crosses" the order price, as shown in Figure 10.1. When the market price equals the limit order price, the limit order may or may not to be executed in live trading. As a result, simulations of limit order trading generally consider a limit order to be executed when the market price drops below the price of the buy limit order, or when the market price rises above the price of the limit sell order, and the limit order execution is guaranteed.

Simulation of strategies can be performed in-sample and out-of-sample. In-sample simulation runs the strategy on the same sample of data on which the strategy was first developed. Natural issues dog the in-sample process: the data can be overfitted, and the results may not hold up in normal market conditions.

To make sure that the strategy has a chance in real-life trading, the strategy needs to be tested out-of-sample. Out-of-sample testing involves running the strategy on a copious amount of previously unused data. The out-of-sample testing is usually performed in the following order:

- 1. Back-test
- 2. Paper trading
- 3. Production

*Back-Test* A strategy run on historical data is called a *back-test*. The back-test typically utilizes at least two years of most recent tick data. The two-year minimum for the test is likely an overhang from low-frequency monthly performance evaluation days: 24 months provides a number of monthly observations nearly sufficient for making statistically significant inferences under the central limit theorem in statistics.

In theory, the minimum number of days sufficient to prove the performance of a strategy is determined by the Sharpe ratio it is thought to produce, as discussed in Chapter 6. In practice, however, a larger number of observations is preferred to the smaller set because the larger the number of observations, the more opportunities to evaluate the strategy performance, and the more confidence in the strategy results.

A large reserve of historical data (at least two years of continuous tick data) also ensures that the model minimizes the data-snooping bias, a condition that occurs when the model overfits to a nonrecurring aberration in the data. Running the backtest on a fresh set of historical data unused in the model development is known as making *out-of-sample inferences*.

A back-test is also useful in estimation of risk of a given trading system. The preferred distributions of returns used as inputs into HFT risk quantification models are obtained from running the system on live capital. Still, a back-test distribution of trade returns obtained from running the model over at least two years of tick data can also be used in risk management applications, even though the back-test distribution may generate misleading results: back-tests may fail to account for all the extreme returns and hidden costs that occur when the system is trading live.

To mitigate the unexpected and low probability extreme returns, known as *black swans* (Taleb, 2007), the HFT researcher may consider running the HFT code through historical or simulated data representing made-up "stress-test scenarios." The data surrounding the flash crash of May 6, 2010, represents a historical example of a stress event. However, data corresponding to some hypothetical simultaneous failure of global financial markets can be simulated.

The out-of-sample back-test results need to be evaluated. At a minimum, the evaluation process should compute basic statistical parameters of the trading idea's performance: cumulative and average returns, Sharpe ratio, and maximum drawdown, as explained in Chapter 6.

Once a strategy is determined to perform satisfactorily in the back-test, the strategy is moved into paper trading, discussed next.

*Paper Trading* A strategy run in real time on live data, but without placing the actual trades, is known as paper trading. The *paper-trading* stage records all orders in a text file. The orders and trades records at a minimum should include:

- A granular timestamp of the order, with a minimum of 1 ms or finer precision.
- A code of the traded financial instrument.
- Last observed best bid price, best bid size, best ask price, and best ask size, for end-of-day reconciliation of orders and data.
- Order quantity.
- Assumed execution price.

The main difference between the live trading model and the back-test model should be the origin of the quote data; the back-test system includes a historical quote-streaming module that reads historical tick data from archives and feeds it sequentially to the module that has the main functionality. In the paper trading system, a different quote module receives real-time tick data from trading venues and broker-dealers.

Except for differences in receiving quotes, paper-trading and back-test systems should be identical; they can be built simultaneously and use the same code for core functionality. This chapter reviews the systems implementation process under the assumption that both back-testing and paper-trading engines are built and tested in parallel. The following sections summarize key steps in the process of developing high-frequency systems, detail the system development process, including common pitfalls,as well as discuss the best practices for testing developed trading systems.

*Production* A strategy running in real time on live capital is usually referred to live trading or as *production*. Production orders are sent to live trading venues via FIX or other messaging protocols. An HFT system running in production will still need to locally archive all orders, as for the paper trading discussed above. The paper trading records and the live trading records will help generate order fulfillment and reconciliation analysis, as well as assess executional performance of the strategy.

The difference in performance of the live strategy and paper trading is formally known as *implementation shortfall*. Implementation shortfall provides the most reliable measures of slippage and other latent costs by allowing direct observation of prices obtained in real markets and their simulated counterparts.

Step 5: Human Supervision Continuous human supervision of the system is required to ensure that the system does not fall victim to some malicious activity such as a computer virus or a market event unaccounted for in the model itself. The role of the human trader, however, should normally be limited to making sure that the performance of the system falls within specific bounds. Once the bounds are breached, the human trader should have the authority to shut down trading for the day or until the conditions causing the breach have been resolved.

# **Common Pitfalls in Systems Implementation**

Message Acknowledgment Loops A market order communication process includes the following steps:

- The client sends a market order to the broker or a trading venue.
- The venue receives the order/the broker forwards the order to the exchange.
- The trading venue sends out an order acknowledgment.
- The client receives the order acknowledgment.
- The order is executed.
- The trading venue sends out the execution acknowledgment.
- The client receives the execution acknowledgment.

Time elapses from the instance the client sends an order to the moment the client receives an order execution acknowledgment. In the United States, the round-trip execution speed of a market order is 10 ms or less; in Europe, this number may grow to 50 to 100 ms, and in Asia the round-trip time may still take a whole minute or two. Regardless of the speed of the execution process, the finite time that elapses between the order origination and confirmation of execution is sufficient to produce wildly runaway algos.

A frequent rookie cause for the runaway condition is an ill-programmed position counter. Consider the following logic: a trading algorithm sends out orders in response to specific market conditions and until the total portfolio reaches a certain position limit. When the position counter is adjusted only upon receiving execution acknowledgments, the system keeps spewing out orders during the time the order is being executed, potentially resulting in an extreme quantity of executions, well above the set position limit. The mistake is common and is easy to fix. One solution involves keeping two position counters: one for sent-in orders, and the other for executed positions. The idea, however, does not occur easily to someone lacking HFT experience.

Time Distortion The simulation runs in its own time using quotes collected and stored during a run time of another process. The frequency of the quotes recorded by the process that collected the data that is now historical data can vary greatly, mostly because of the following two factors:

- 1. The number of financial instruments for which the original process collected quotes.
- 2. The speed of the computer system on which the original process ran.

Their impact is due to the nature of the quote process and its realization in most trading systems. Most systems comprise a client (the quote collecting and/or trading application) that is geared to receive quotes and the server (a broker-dealer application supplying the quotes). The client is most often a "local" application that runs "locally": on computer hardware over which the trader has full control. The broker-dealer server is almost always a remote application, meaning that the client has to communicate with the server over a remote connection, such as the Internet. To receive quotes, the client application usually has to perform the following communication with the server process:

- 1. The client sends the server a message or a series of messages with the following information:
  - a. Client identification (given to the client by the broker-dealer that houses the server).
  - b. Names of financial securities for which the quotes are requested.
- 2. The server will respond, acknowledging the client's message. The server's response will also indicate whether the client is not allowed to receive any of the quotes requested for any reason.
- 3. The server will begin to stream the quotes to the client. The quotes are typically streamed in an "asynchronous" manner—that is, the server will send a quote to the client as soon as a new quote becomes available. Some securities have higher-frequency quotes than others. For example, during high-volatility times surrounding economic announcements, it is not unusual for the EUR/USD exchange rate to be accompanied by as many as 300 quotes per second. At the same time, some obscure option may generate only one quote per trading day. It is important to keep in mind the expected frequency of quotes while designing the quote-receiving part of the application.
- 4. Quote distortion often happens next. It is the responsibility of the client to collect and process all the quotes as soon as they arrive at the client's computer. Here, several issues can occur. On the client's machine, all incoming quotes are placed into a queue in the order of their arrival, with the earliest quotes located closest to the processor. This queue can be thought of as a line for airport checkin. Unlike the airport line, however, the queue often has a finite length or capacity; therefore, any quote arrivals that find the queue full are discarded, hence the first issue: quote time series may vary from client to client if the client systems have queues of varying lengths, all other system characteristics being equal.

Once the quotes are in the queue, the system picks the earliest quote arrival from the queue for processing; then all the quotes in the queue are shifted closer to the processing engine. As noted previously, the quotes may arrive faster than the client is able to process them, filling up the queue and leading the system to discard new quote arrivals until the older quotes are processed. Even a seemingly simple operation such as copying a quote to a file or a database stored on the computer system takes computer time. While the quote-storing time may be a tiny fraction of a second and thus negligible by human time standards, the time can be significant by computer clock and slow down the processing of incoming quotes.

A client system may assign the quote an arrival time on taking the quote from its arrival queue. The timestamp may therefore differ from the timestamp given to the quote by the server. Depending on the number of securities for which the quotes are collected and the market's volatility at any given time of day, the timestamp distortion may differ significantly as a result of the quote-processing delay alone. If the quotes are further mathematically manipulated to generate trading signals, the distortions in timestamps may be even more considerable.

- 5. Naturally, systems running on computers with slower processing power will encounter more timestamp distortion than systems running on faster machines. Faster machines are quicker at processing sequential quotes and drop fewer quotes as a result. Even the slightest differences in system power can result in different quote streams that in turn may produce different trading signals. The reliability of quote delivery can be improved in the following four ways:
- 1. Time-stamping quotes immediately when each quote arrives before putting the quote into the queue.
- 2. Increasing the size of the quote queue.
- 3. Increasing system memory to the largest size feasible given a cost/benefit analysis.
- 4. Reducing the number of securities for which the quotes are collected on any given client.

These four steps toward establishing greater quote reliability are fairly easy to implement when the client application is designed and built from scratch, and in particular when using the FIX protocol for quote delivery. However, many off-the shelf clients, including those distributed by executing brokers, may be difficult or impossible to customize. For firms planning to use an off-the-shelf client, it may be prudent to ask the software manufacturer how the preceding issues can be addressed in the client.

Speed of Execution Duration of execution can make or break HFT models. Most strategies for arbitraging temporary market mispricings, for example, depend on the ability to get the orders posted with lightning speed. Whoever detects the mispricing and gets his order posted on the exchange first is likely to generate the most profit.

Speed of execution is controlled by the following components of trading platforms:

- The speed of applications generating trading signals.
- The proximity of applications generating trading signals to the executing broker.
- The speed of the executing broker's platform in routing execution requests.
- The proximity of the executing broker to the exchange.
- The speed of the exchange in processing the execution orders.

Figure 16.3 illustrates the time-dependent flow of execution process.

To enhance message security and to alleviate delays due to the physical transmission of trading signals between clients and the broker or the exchange, clients dependent on the speed of execution often choose to co-locate or house their servers in proximity centers. Co-location and proximity hosting services typically employ systems administration staff that are capable of providing recovery services in case of systems or power failure, making sure that the client applications work at least 99.999 percent of the time. Co-location and proximity hosting are discussed in detail in Chapter 2 of the book.

![](_page_12_Figure_0.jpeg)

**FIGURE 16.3** execution Process

#### ■ **Testing Trading Systems**

The costs of rolling out a system that contains programmatic errors, or bugs, can be substantial. Thorough testing of the system, therefore, is essential prior to wide rollout of the model. Testing has the following stages:

- Data set testing
- Unit testing
- System testing
- Integration testing
- Regression testing
- Automation testing

# **Data Set testing**

Data set testing refers to testing the validity of the data, whether historical data used in a back-test or real-time data obtained from a streaming data provider. The objective of data testing is to ascertain that the system minimizes undesirable infl uences and distortions in the data and to ensure that the run-time analysis and trading signal generation work smoothly.

Data set testing is built on the premise that all data received for a particular security should fall into a statistical distribution that is consistent throughout time. The data should also exhibit consistent distributional properties when sampled at different frequencies: one-minute data for USD/CAD, for example, should be consistent with historical one-minute data distribution for USD/CAD observed for the past year. Naturally, data set testing should allow for distributions to change with time, but the observed changes should not be drastic, unless they are caused by a large-scale market disruption.

A popular procedure for testing data is based on testing for consistency of autocorrelations. It is implemented as follows:

- 1. A data set is sampled at a given frequency—say, 10-second intervals.
- 2. Autocorrelations are estimated for a moving window of 30 to 1,000 observations.
- 3. The obtained autocorrelations are then mapped into a distribution; outliers are identified, and their origin is examined. The distributional properties can be analyzed further to answer the following questions:
  - Have the properties of the distribution changed during the past month, quarter, or year?
  - Are these changes due to the version of the code or to the addition or removal of programs on the production box?

The testing should be repeated at different sampling frequencies to ensure that no systemic deviations occur.

# **Unit Testing**

Unit testing verifies that each individual software component of the system works properly. A unit is a testable part of an application; the definition of a unit can range from the code for the lowest function or method to the functionality of a mediumlevel component—for example, a latency measurement component of the posttrade analysis engine. Testing code in small blocks from the ground up ensures that any errors are caught early in the integration process, avoiding expensive system disruptions at later stages.

# **Integration Testing**

Integration testing follows unit testing. As its name implies, integration testing is a test of the interoperability of code components; the test is administered to increasingly larger aggregates of code as the system is being built up from modular pieces to its completed state. Testing modular interoperability once again ensures any that code defects are caught and fixed early.

# **System Testing**

System testing is a postintegration test of the system as a whole. The system testing incorporates several testing processes described as follows.

Graphical user interface (GUI) software testing ensures that the human interface of the system enables the user (e.g., the person responsible for monitoring trading activity) to perform her tasks. GUI testing typically ensures that all the buttons and displays that appear on screen are connected with the proper functionality according to the specifications developed during the design phase of the development process.

Usability and performance testing is similar in nature to GUI testing but is not limited to GUIs and may include such concerns as the speed of a particular functionality. For example, how long does the system take to process a "system shutdown" request? Is the timing acceptable from a risk management perspective?

Stress testing is a critical component of the testing of high-frequency trading systems. A stress-testing process attempts to document and, subsequently, quantify the impact of extreme hypothetical scenarios on the system's performance. For example, how does the system react if the price of a particular security drops 10 percent within a very short time? What if an act of God occurs that shuts down the exchange, leaving the system holding its positions? What other worst-case scenarios are there, and how will they affect the performance of the system and the subsequent P&L?

Security testing is another indispensable component of the testing process that is often overlooked by organizations. Security testing is designed to identify possible security breaches and to either provide a software solution for overcoming the breaches or create a breach-detection mechanism and a contingency plan in the event a breach occurs. HFT systems can be vulnerable to security threats coming from the Internet, where unscrupulous users may attempt to hijack account numbers, passwords, and other confidential information in an attempt to steal trading capital. However, intraorganizational threats should not be underestimated; employees with malicious intent or disgruntled workers having improper access to the trading system can wreak considerable and costly havoc. All such possibilities must be tested and taken into account.

Scalability testing refers to testing the capacity of the system. How many securities can the system profitably process at the same time without incurring significant performance impact? The answer to this question may appear trivial, but the matter is anything but trivial in reality. Every incremental security measure added to the system requires an allocation of computer power and Internet bandwidth. A large number of securities processed simultaneously on the same machine may considerably slow down system performance, distorting quotes, trading signals, and the P&L as a result. A determination of the maximum permissible number of securities will be based on the characteristics of each trading platform, including available computing power.

Reliability testing determines the probable rate of failure of the system. Reliability testing seeks to answer the following questions: What are the conditions under which the system fails? How often can we expect these conditions to occur? The failure conditions may include unexpected system crashes, shutdowns due to insufficient memory space, and anything else that leads the system to stop operating. The failure rate for any well-designed high-frequency trading system should not exceed 0.01 percent (i.e., the system should be guaranteed to remain operational 99.99 percent of time).

Recovery testing refers to verification that in an adverse event, whether an act of God or a system crash, the documented recovery process ensures that the system's integrity is restored and it is operational within a prespecified time. The recovery testing also ensures that data integrity is maintained through unexpected terminations of the system. Recovery testing should include the following scenarios: When the application is running and the computer system is suddenly restarted, the application should have valid data upon restart. Similarly, the application should continue operating normally if the network cable should be unexpectedly unplugged and then plugged back in.

# **Use-Case Testing**

The term *use-case testing* refers to the process of testing the system according to the system performance guidelines defined during the design stage of the system development. In use-case testing, a dedicated tester follows the steps of using the system and documents any discrepancies between the observed behavior and the behavior that is supposed to occur. Use-case testing ensures that the system is operating within its parameters.

Use-case testing is typically performed by professional software testers, not the programmers who coded the system. The deployment of testers is important for several reasons:

- Testers are trained to document discrepancies between a given scenario and actual performance of the system module.
- Testers are not emotionally involved in code development and are impartial to found errors.
- Testers' labor is considerably less expensive than that of programmers, resulting in savings for the organization.

Discrepancies or "bugs" reported by testers usually span three levels: critical, moderate, and inconsequential. Critical bugs significantly impair intended system performance and need to be addressed with the highest priority. Moderate bugs are considerable issues and need to be addressed following the bugs in the critical functionality. Inconsequential bugs are more of a cosmetic variety and may not need to be addressed until a downtime occurs within the ranks of coders.

#### ■ **Summary**

Implementation of high-frequency systems is a time-consuming process, in which mistakes can be very costly. Outsourcing noncritical components of the system may be a prudent strategy. Testing, however, is the paramount activity that has to be conducted according to best practices established for software development.

# ■ **End-of-Chapter Questions**

- 1. What are the stages in development of high-frequency trading systems? What are the stages in HFT implementation?
- 2. What is a back-test? What are the peculiarities of back-testing?
- 3. Suppose the back-testing system is placing a limit buy order at 125.13 when the market price is 125.14. At what market price level can the researcher assume that the limit order was executed?
- 4. Suppose a system produces a Sharpe ratio of 12 in the back-test. How much paper-trading testing does this system need to ascertain its performance?
- 5. What methodologies can be deployed in data testing?
- 6. What is use-case testing? Why is it valuable?
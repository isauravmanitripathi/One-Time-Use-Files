#### CHAPTER 16

# Implementing **High-Frequency**<br>**Trading Systems**

nce high-frequency trading models have been identified, the models are back-tested to ensure their viability. The back-testing software should be a "paper"-based prototype of the eventual live system. The same code should be used in both, and the back-testing engine should run on tick-by-tick data to reenact past market conditions. The main functionality code from the back-testing modules should then be reused in the live system.

To ensure statistically significant inferences, the model "training" period  $T$  should be sufficiently large; according to the central limit theorem  $(CLT)$ , 30 observations is the bare minimum for any statistical significance, and 200 observations is considered a reasonable number. Given strong seasonality in intra-day data (recurrent price and volatility changes at specific times throughout the day), benchmark high-frequency models are backtested on several years of tick-by-tick data.

The main difference between the live trading model and the back-test model should be the origin of the quote data; the back-test system includes a historical quote-streaming module that reads historical tick data from archives and feeds it sequentially to the module that has the main functionality. In the live trading system, a different quote module receives real-time tick data originating at the broker-dealers.

Except for differences in receiving quotes, both live and back-test systems should be identical; they can be built simultaneously and, ideally, can use the same code samples for core functionality. This chapter reviews the systems implementation process under the assumption that both backtesting and live engines are built and tested in parallel.

#### **MODEL DEVELOPMENT LIFE CYCLE**

High-frequency trading systems, by their nature, require rapid hesitationfree decision making and execution. Properly programmed computer systems typically outperform human traders in these "mission-critical" trading tasks, particularly under treacherous market conditions—see Aldridge (2009), for example. As a result, computer trading systems are rapidly replacing traditional human traders on trading desks around the world.

The development of a fully automated trading system follows a path similar to that of the standard software development process. The typical life cycle of a development process is illustrated in Figure 16.1.

A sound development process normally consists of the following five phases:

- **1.** Planning
- **2.** Analysis
- **3.** Design
- **4.** Implementation
- **5.** Maintenance

![](_page_1_Figure_11.jpeg)

**FIGURE 16.1** Typical development cycle of a trading system.

The circular nature of the process illustrates the continuous quality of system development. When a version of the system appears to be complete, new issues demand advanced modifications and enhancements that lead to a new development cycle.

The purpose of the planning phase is to determine the goals of the project as well as to generate a high-level view of what the completed project may look like. The planning is accompanied by a feasibility study that evaluates the project in terms of its economics, operating model, and technical requirements. The economical considerations explore whether the project has a sufficient profit and loss (P&L) potential, whereas operational and technical issues address the feasibility of the project from the compliance, human resources, and other day-to-day points of view. The outputs of the planning phase include concrete goals and targets set for the project, established schedules, and estimated budgets for the entire system.

During the analysis stage of the process, the team aggregates requirements for system functionality, determines the scope of the project (which features are in and which features are out of the current release), and solicits initial feedback from users and management. The analysis stage is arguably the most critical stage in the development process, because it is here that stakeholders have the ultimate ability to shape the functionality of the system given the allocated budget.

The design phase incorporates detailed specifications of functionality, including process diagrams, business rules, and screenshots, along with other output formats such as those of daily reports and other documents. An objective of the design stage is to separate the whole project into discrete components subsequently assigned to teams of software developers; the discrete components will have well-specified interfaces that can lock in seamlessly with other components designed by different teams of software developers. Such early specification of software packaging of internal computer modules streamlines future communication among different software development teams and enables smooth operation of the project going forward. The design phase also outlines test cases—that is, the functionality paths that are later used as blueprints to verify the correctness of the completed code.

The implementation phase, finally, involves actual programming; the software teams or individual programmers develop software modules according to the specifications defined in the design stage. The individual modules are then tested by the development teams themselves against the predefined test cases. When the project management is satisfied that the individual modules have been developed according to the specifications, the project integration work begins. Integration, as its name implies, refers to putting together the individual modules to create a functional system.

While successfully planned projects encounter little variance or problems in the integration stage, some work still remains. Scripts may have to be written to ensure proper communication among various system components, installation wrappers may have to be developed, and, most importantly, the system has to be comprehensively tested to ensure proper operation. The test process usually involves dedicated personnel other than the people who developed the code. The test staff diligently monitors the execution of each functionality according to testing procedures defined in the design stage. The test personnel then documents any "bugs"—that is, discrepancies between the prespecified test case performance and observed performance. The bugs are then sent back over to the development team for resolution and are subsequently returned to the testing teams.

Successful implementation is followed by the deployment and subsequent maintenance phase of the system. The maintenance phase addresses system-wide deviations from planned performance, such as troubleshooting newly discovered bugs.

## SYSTEM IMPLEMENTATION

#### **Key Steps in Implementation** of High-Frequency Systems

Most systematic trading platforms are organized as shown in Figure 16.2. One or several run-time processors contain the core logic of the trading mechanism and perform the following functions:

- Receive, evaluate, and archive incoming quotes
- Perform run-time econometric analysis
- Implement run-time portfolio management
- Initiate and transmit buy and sell trading signals
- Listen for and receive confirmation of execution
- Calculate run-time P&L
- Dynamically manage risk based on current portfolio allocations and market conditions

A successful high-frequency trading system adapts itself easily to contemporary market conditions. As a result, most high-frequency systems accept, process, and archive volumes of quotes and other market data delivered at real-time frequency. Some systems may convert streaming realtime data into equally spaced data intervals, such as seconds or minutes, for use in their internal econometric analyses. Other systems may run on the raw, irregularly spaced quotes. The decision whether to convert the data should be based on the requirements of the run-time econometric analysis.

![](_page_4_Figure_0.jpeg)

![](_page_4_Figure_1.jpeg)

The run-time econometric analysis is a computer program that performs the following three functions:

- **1.** Accepts quotes and order acknowledgments
- **2.** Uses the quotes as input to the core analysis engine
- **3.** Outputs trading signals

The core analysis engine is typically based on the historical analysis identified to generate consistent positive returns over a significant period of time during the simulation and back-testing process. The development of the core engine usually proceeds as follows. First, a quantitative analyst identifies a mispriced security, a market inefficiency, or a persistent deviation from equilibrium. This first modeling step is often done using the MatLab or R programming languages, which are designed to facilitate mathematical operations.

Next, the quantitative analyst, usually in conjunction with technical specialists, back-tests the model on several years of data. A back test of several years (two at the very minimum) should produce a sample distribution of returns that is numerous enough to be close to the true distribution of returns characterizing both past and future performance. If the model delivers consistently positive results in the back test over several years, the model is then programmed into its production state.

Most of the high-frequency production-bound systems are written in C++, although some hedge funds and other investment management firms are known to use Java. C++ is often considered to be "lighter" and "faster" than Java, meaning that C++ programs do not have the processing power overhead required by Java; as a result, C++ systems often work faster than Java-based systems. C++ programmers, however, must be careful in their utilization of the system's run-time memory, whereas Java is designed to take care of all run-time memory issues whether or not the programmer remembers to do so.

The design and implementation of run-time portfolio management reflects the core econometric engine. In addition to the raw quote inputs, the portfolio management framework incorporates inputs from the econometric model, current position sizes, and other information relevant to portfolio diversification and maximization of portfolio returns, while minimizing portfolio risk.

The core engine and the portfolio management framework then initiate and transmit orders to the broker-dealer. Upon receiving and executing an order, the broker-dealer sends back the order status and order-filling price and size to the client. The system then calculates the P&L and assesses risk management parameters that feed back into the portfolio management piece.

Incoming quotes, along with outgoing orders and any other communication between a broker-dealer and a client or an exchange, are most often transmitted via a Financial Information eXchange (FIX) protocol specifically designed for transmission of real-time financial information. According to the FIX industry website (http://www.fixprotocol.org), FIX emerged in 1992 as a bilateral communications framework for equity trading between Fidelity Investments and Salomon Brothers. It has since become the dominant communication method among various broker-dealers, exchanges, and transacting customers. In fact, according to a survey conducted by fixprotocol.org, FIX was used for systematic trading by 75 percent of buy-side firms, 80 percent of sell-side firms, and over 75 percent of exchanges in 2006.

FIX is best described as a programming language that is overseen by a global steering committee, consisting of representatives from banks, broker-dealers, exchanges, industry utilities and associations, institutional investors, and information technology providers from around the world. Its standard is open and free. Implementation of communication process via FIX, however, requires careful planning and dedicated resources and may demand significant expense, much like any other system development process.

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

Finally, at the end of the body of every message is the "checksum"—a sum of digital values of all the characters in the message included as a verification of whether the message has arrived in full.

For example, a message carrying a quote for USD/CAD at 15:25:20 GMT on July 31, 2007 looked like this:

```
8=FIX.4.2 | 9=309 | 35=S | 49=ML-FIX-FX |
56=ECHO2-QTS-TEST | 34=5015 | 52=20070731-15:25:20 |
131=1185895365 | 117=ECHO2-QTS-
TEST.00043690C8A8D6B9.00043690D14044C6 | 301=0 |
55=USD/CAD | 167=FOR | 15=USD | 132=1.065450 |
133=1.065850 | 134=5000000.0 | 135=5000000.0 |
647=2000001.0 | 648=2000001.0 | 188=1.06545 |
190=1.06585 | 60=20070731-15:25:20 | 40=H | 64=20070801
| 10=178
```

Dissecting the message, we note the following fields:

8=FIX.4.2: Version of the FIX protocol used. 9=309: The body of the message is 309 characters long. 35=S: This message is carrying a quote.

49=ML-FIX-FX: internal identification of the sender of the message; in this case, the sender is Merrill Lynch FX desk.

56=ECHO2-QTS-TEST: internal identification of the message recipient.

- 34=5015: sequential message number; this number is used to track all the messages sent. Message sequencing makes it easy for the recipient of the message to identify whether the recipient has received all of the messages and whether they were received in order. Message sequencing may help pinpoint problems with the communication link or message transmission and reception.
- 52=20070731-15:25:20: timestamp corresponding to the time transmission originated. The timestamp consists of the date (yyyymmdd) and time (hh:mm:dd). The time is usually quoted in GMT.
- 131=1185895365: unique identifier corresponding to a message containing an original quote request for a given security.
- 117=ECHO2-QTS-TEST.00043690C8A8D6B9.00043690D14044C6: unique identifier for the quote. Note that the identifier contains the recipient's identification, making it possible for broker-dealers to stream different quotes to clients with different profiles. For example, the broker-dealer may increase spreads for a persistently successful client.
- 301=0: level of response requested from recipient of the quote message; valid responses are 0 = No Acknowledgment (default), 1 = Acknowledge only negative or erroneous quotes, and 2 = Acknowledge each quote message. In our example, Merrill Lynch does not expect any acknowledgment upon receipt of the quote.
- 55=USD/CAD: the ticker symbol of the quoted instrument.
- 167=FOR: the type of the security quoted. Valid values include ABS = Asset-backed Securities, BN = Bank Notes, FUT = Future, and OPT = Option, among many others.

15=USD: based currency used for price.

- 132=1.065450: bid price.
- 133=1.065850: offer or ask price.
- 134=5000000.0: bid quantity.
- 135=5000000.0: offer quantity.
- 647=2000001.0: minimum quantity for a bid.
- 648=2000001.0: minimum quantity for an offer.
- 188=1.06545: bid FX spot rate.
- 190=1.06585: offer FX spot rate.
- 60=20070731-15:25:20: timestamp of the quote creation.

40=H: available order types.

Order types may assume one of the following values: 1 = Market, 2 = Limit, 3 = Stop/Stop Loss, 4 = Stop Limit, 5 = Market On Close (No longer used), 6 = With Or Without, 7 = Limit Or Better, 8 = Limit With Or Without, 9 = On Basis, A = On Close (No longer used), B = Limit On Close (No longer used), C = Forex Market (No longer used), D = Previously Quoted, E = Previously Indicated, F = Forex Limit (No longer used), G = Forex Swap, H = Forex Previously Quoted (No longer used), I = Funari (Limit day order with unexecuted portion handles as Market On Close, e.g., Japan), J = Market If Touched (MIT), K = Market With Left Over as Limit (market order with unexecuted quantity becoming limit order at last price), L = Previous Fund Valuation Point (Historic pricing; for CIV), M = Next Fund Valuation Point (Forward pricing; for CIV), P = Pegged, Q = Counter-order selection.

- 64=20070801: trade settlement date. If the order were to be executed on July 31, 2007, the trade would be settled on 8/1/2007.
- 10=178: checksum, a sum of computer codes of all characters in the message. The checksum is used to verify that the message arrived intact.

The best high-frequency trading systems do not stop there. A posttrade analysis engine reconciles production results with simulation results run with the same code on the same data and updates distributions of returns, trading costs, and risk management parameters to be fed back into the main processing engine, portfolio optimization, and risk management components.

The simulation engine is an independent module that tests new trading ideas on past and run-time data without actually executing the trades. Unlike ideas that are still in early stages of development that are often coded in MatLab or Excel, ideas tested in the simulation engine are typically coded in the production language (C++ or Java). Once coded for production setup, the simulation engine is first run on a long sample of historical data in a process known as back-testing. At this point, the simulation engine can be refined to incorporate any system tweaks and bug fixes. Once the back test performs satisfactorily, the system is switched to run on real-time data, the same data that feeds into the production system. At this point, however, the system is still in the testing phase and the system's ability to send production orders is disabled. Instead, all orders that would be sent to the broker-dealer are recorded in a text file. This testing phase of the system on the real-time data is referred to as "paper-trading."

Once paper-trading performance is satisfactory and comparable to that of the back test, paper-trading is moved into production. Continuous human supervision of the system is required to ensure that the system does not fall victim to some malicious activity such as a computer virus or a market event unaccounted for in the model itself. The role of the human trader, however, should normally be limited to making sure that the performance of the system falls within specific bounds. Once the bounds are breached, the human trader should have the authority to shut down trading for the day or until the conditions causing the breach have been resolved.

# **Common Pitfalls in Systems Implementation**

**Time Distortion** The simulation runs in its own time using quotes collected and stored during a run-time of another process. The frequency of the quotes recorded by the process that collected the data that is now historical data can vary greatly, mostly because of the following two factors:

- **1.** The number of financial instruments for which the original process collected quotes
- **2.** The speed of the computer system on which the original process ran

Their impact is due to the nature of the quote process and its realization in most trading systems. Most systems comprise a client (the quote collecting and/or trading application) that is geared to receive quotes and the server (a broker-dealer application supplying the quotes). The client is most often a "local" application that runs "locally": on computer hardware over which the trader has full control. The broker-dealer server is almost always a remote application, meaning that the client has to communicate with the server over a remote connection, such as the Internet. To receive quotes, the client application usually has to perform the following communication with the server process:

- **1.** The client sends the server a message or a series of messages with the following information:
  - **a.** Client identification (given to the client by the broker-dealer that houses the server)
  - **b.** Names of financial securities for which the quotes are requested
- **2.** The server will respond, acknowledging the client's message. The server's response will also indicate whether the client is not allowed to receive any of the quotes requested for any reason.
- **3.** The server will begin to stream the quotes to the client. The quotes are typically streamed in an "asynchronous" manner—that is, the server will send a quote to the client as soon as a new quote becomes available. Some securities have higher-frequency quotes than others. For example, during high-volatility times surrounding economic announcements, it is not unusual for the EUR/USD exchange rate to be accompanied by as many as 30 quotes per second. At the same time, some obscure stock may generate only one quote per trading day. It is important to keep in mind the expected frequency of quotes while designing the quote-receiving part of the application.

**4.** Quote distortion often happens next. It is the responsibility of the client to collect and process all the quotes as soon as they arrive at the client's computer. Here, several issues can occur. On the client's machine, all incoming quotes are placed into a queue in the order of their arrival, with the earliest quotes located closest to the processor. This queue can be thought of as a line for airport check-in. Unlike the airport line, however, the queue often has a finite length or capacity; therefore, any quote arrivals that find the queue full are discarded. Hence the first issue: Quote time series may vary from client to client if the client systems have queues of varying lengths, all other system characteristics being equal.

Once the quotes are in the queue, the system picks the earliest quote arrival from the queue for processing; then all the quotes in the queue are shifted closer to the processing engine. As noted previously, the quotes may arrive faster than the client is able to process them, filling up the queue and leading the system to discard new quote arrivals until the older quotes are processed. Even a seemingly simple operation such as copying a quote to a file or a database stored on the computer system takes computer time. While the quote-storing time may be a tiny fraction of a second and thus negligible by human time standards, the time can be significant by computer clock, and slow down the processing of incoming quotes.

A client system may assign the quote an arrival time on taking the quote from its arrival queue. The timestamp may therefore differ from the timestamp given to the quote by the server. Depending on the number of securities for which the quotes are collected and the market's volatility at any given time of day, the timestamp distortion may differ significantly as a result of the quote-processing delay alone. If the quotes are further mathematically manipulated to generate trading signals, the distortions in timestamps may be even more considerable.

**5.** Naturally, systems running on computers with slower processing power will encounter more timestamp distortion than systems running on faster machines. Faster machines are quicker at processing sequential quotes and drop fewer quotes as a result. Even the slightest differences in system power can result in different quote streams that in turn may produce different trading signals.

The reliability of quote delivery can be improved in the following four ways:

- **1.** Timestamping quotes immediately when each quote arrives before putting the quote into the queue
- **2.** Increasing the size of the quote queue

- 3. Increasing system memory to the largest size feasible given a cost/ benefit analysis
- 4. Reducing the number of securities for which the quotes are collected on any given client

These four steps toward establishing greater quote reliability are fairly easy to implement when the client application is designed and built from scratch, and in particular when using the FIX protocol for quote delivery. On the other hand, many off-the shelf clients, including those distributed by executing brokers, may be difficult or impossible to customize. For firms planning to use an off-the-shelf client, it may be prudent to ask the software manufacturer how the preceding issues can be addressed in the client.

**Speed of Execution** Duration of execution can make or break highfrequency trading models. Most strategies for arbitraging temporary market mispricings, for example, depend on the ability to get the orders posted with lightning speed. Whoever detects the mispricing and gets his order posted on the exchange first is likely to generate the most profit.

Speed of execution is controlled by the following components of trading platforms:

- The speed of applications generating trading signals
- The proximity of applications generating trading signals to the executing broker
- The speed of the executing broker's platform in routing execution requests
- The proximity of the executing broker to the exchange
- The speed of the exchange in processing the execution orders

Figure 16.3 illustrates the time-dependent flow of execution process.

To alleviate delays due to the physical transmission of trading signals between clients and the broker and, again, between the broker and the exchange, clients dependent on the speed of execution often choose to locate their systems as close to the broker and the exchange as possible. This practice of placing client computer systems next to the broker and the exchange is known as "co-location." Co-location does not require clients to move their offices; instead, co-location can be achieved through a set of production machines managed in a secure warehouse by an experienced third-party administrator, with the client having a full remote, or "virtual," access to the production machines. Co-location services typically employ systems administration staff that is capable of providing recovery services in case of systems or power failure, making sure that the client applications work at least 99.9 percent of time.

![](_page_13_Figure_1.jpeg)

**FIGURE 16.3** Execution process.

# TESTING TRADING SYSTEMS

The costs of rolling out a system that contains programmatic errors, or bugs, can be substantial. Thorough testing of the system, therefore, is essential prior to wide roll-out of the model. Testing has the following stages:

- Data set testing
- Unit testing
- Integration testing
- System testing
- Regression testing
- Use case testing

## **Data Set Testing**

Data set testing refers to testing the validity of the data, whether historical data used in a back test or real-time data obtained from a streaming data provider. The objective of data testing is to ascertain that the system minimizes undesirable influences and distortions in the data and to ensure that the run-time analysis and trading signal generation work smoothly.

Data set testing is built on the premise that all data received for a particular security should fall into a statistical distribution that is consistent throughout time. The data should also exhibit consistent distributional properties when sampled at different frequencies: 1-minute data for USD/CAD, for example, should be consistent with historical 1-minute data distribution for USD/CAD observed for the past year. Naturally, data set testing should allow for distributions to change with time, but the observed changes should not be drastic, unless they are caused by a largescale market disruption.

A popular procedure for testing data is based on testing for consistency of autocorrelations. It is implemented as follows:

- **1.** A data set is sampled at a given frequency—say, 10-second intervals.
- **2.** Autocorrelations are estimated for a moving window of 30 to 1,000 observations.
- **3.** The obtained autocorrelations are then mapped into a distribution; outliers are identified, and their origin is examined. The distributional properties can be analyzed further to answer the following questions:
  - Have the properties of the distribution changed during the past month, quarter, or year?
  - Are these changes due to the version of the code or to the addition or removal of programs on the production box?

The testing should be repeated at different sampling frequencies to ensure that no systemic deviations occur.

# **Unit Testing**

Unit testing verifies that each individual software component of the system works properly. A unit is a testable part of an application; the definition of a unit can range from the code for the lowest function or method to the functionality of a medium-level component—for example, a latency measurement component of the post-trade analysis engine. Testing code in small blocks from the ground up ensures that any errors are caught early in the integration process, avoiding expensive system disruptions at later stages.

# **Integration Testing**

Integration testing follows unit testing. As its name implies, integration testing is a test of the interoperability of code components; the test is administered to increasingly larger aggregates of code as the system is being built up from modular pieces to its completed state. Testing modular interoperability once again ensures that any code defects are caught and fixed early.

#### **System Testing**

System testing is a post-integration test of the system as a whole. The system testing incorporates several testing processes described as follows.

Graphical user interface (GUI) software testing ensures that the human interface of the system enables the user (e.g., the person responsible for monitoring trading activity) to perform her tasks. GUI testing typically ensures that all the buttons and displays that appear on screen are connected with the proper functionality according to the specifications developed during the design phase of the development process.

Usability and performance testing is similar in nature to GUI testing but is not limited to graphical user interfaces and may include such concerns as the speed of a particular functionality. For example, how long does the system take to process a "system shutdown" request? Is the timing acceptable from a risk management perspective?

Stress testing is a critical component of the testing of high-frequency trading systems. A stress-testing process attempts to document and, subsequently, quantify the impact of extreme hypothetical scenarios on the system's performance. For example, how does the system react if the price of a particular security drops 10 percent within a very short time? What if an act of God occurs that shuts down the exchange, leaving the system holding its positions? What other worst-case scenarios are there and how will they affect the performance of the system and the subsequent P&L?

Security testing is another indispensable component of the testing process that is often overlooked by organizations. Security testing is designed to identify possible security breaches and to either provide a software solution for overcoming the breaches or create a breach-detection mechanism and a contingency plan in the event a breach occurs. High-frequency trading systems can be vulnerable to security threats coming from the Internet, where unscrupulous users may attempt to hijack account numbers, passwords, and other confidential information in an attempt to steal trading capital. However, intra-organizational threats should not be underestimated; employees with malicious intent or disgruntled workers having improper access to the trading system can wreak considerable and costly havoc. All such possibilities must be tested and taken into account.

Scalability testing refers to testing the capacity of the system. How many securities can the system profitably process at the same time without incurring significant performance impact? The answer to this question may appear trivial, but the matter is anything but trivial in reality. Every incremental security measure added to the system requires an allocation of computer power and Internet bandwidth. A large number of securities processed simultaneously on the same machine may considerably slow down system performance, distorting quotes, trading signals, and the P&L as a result. A determination of the maximum permissible number of securities will be based on the characteristics of each trading platform, including available computing power.

Reliability testing determines the probable rate of failure of the system. Reliability testing seeks to answer the following questions: What are the conditions under which the system fails? How often can we expect these conditions to occur? The failure conditions may include unexpected system crashes, shutdowns due to insufficient memory space, and anything else that leads the system to stop operating. The failure rate for any welldesigned high-frequency trading system should not exceed 0.01 percent (i.e., the system should be guaranteed to remain operational 99.99 percent of the time).

Recovery testing refers to verification that in an adverse event, whether an act of God or a system crash, the documented recovery process ensures that the system's integrity is restored and it is operational within a prespecified time. The recovery testing also ensures that data integrity is maintained through unexpected terminations of the system. Recovery testing should include the following scenarios: When the application is running and the computer system is suddenly restarted, the application should have valid data upon restart. Similarly, the application should continue operating normally if the network cable should be unexpectedly unplugged and then plugged back in.

## **Use Case Testing**

The term *use case testing* refers to the process of testing the system according to the system performance guidelines defined during the design stage of the system development. In use case testing, a dedicated tester follows the steps of using the system and documents any discrepancies between the observed behavior and the behavior that is supposed to occur. Use case testing ensures that the system is operating within its parameters.

# **CONCLUSION**

Implementation of high-frequency systems is a critical process, one in which mistakes can be very costly. Outsourcing noncritical components of the system may be a prudent strategy. However, code that implements proprietary econometric models should be developed internally to ensure maximum strategy capacity.
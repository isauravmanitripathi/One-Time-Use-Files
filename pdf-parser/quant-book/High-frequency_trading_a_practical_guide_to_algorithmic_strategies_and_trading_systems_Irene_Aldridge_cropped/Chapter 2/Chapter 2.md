# Technological Innovations, Systems, and HFT

 $\bullet$ echnological innovation leaves the most persistent mark on the operations of financial markets. While the introduction of new financial instruments, such as EUR/USD in 1999, created large-scale one-time disruptions in market routines, technological changes have a subtle and continuous impact on the markets. Over the years, technology has improved the way news is disseminated, the quality of financial analysis, and the speed of communication. The adoption of technology in financial services, however, was greatly aided by the ever-plummeting costs of technological improvements. This chapter examines the key developments that have occurred in technology over the past several decades in the context of enabling modern financial landscape.

#### A Brief History of Hardware

Trading was institutionalized during the Roman Empire, when the first exchange in currency in designated locations can be noted (benches or "bancas" were the direct precursors of today's banks). Gradual change guided the operations of trading firms until the technological revolution of the twentieth century enabled the current state of trading with rapid exchanges of information. As Figure 2.1 illustrates, over the past 100 years or so the computational speed available to traders has increased exponentially, while the cost of computing has been falling steadily since the 1980s, after reaching its peak.

The price decline in computer technology has been spectacular over the past 20 years. A computer system with 2 gigabytes of memory (RAM), 300 gigabytes of hard drive space, and a 2-gigahertz processor cost several million dollars in 1995, and was big enough to require its own room. In 2012, a computer with identical specifi cations not only fi ts in a standard desktop case, it can also be found for as little as \$400 in any neighborhood Best Buy or other computer store.

The decline in the cost of computing can be largely traced to the effi ciency of scale in production of computer chips overseas. The demand for the increasingly accessible and cheaper technology has, surprisingly, been driven not by the fi nancial services practitioners, but rather by more casual users of computer technology with considerably thinner wallets. Over the past two decades, the latter demanders for cost-effi cient technology happened to be video game players, whose sheer scale and desire for lifelike graphics has fueled the surge in mass production and plummeting prices of fast technology. Financial fi rms have reaped the benefi ts of innovation and cost effi ciencies created by the activity of the video gaming industry.

![](_page_1_Figure_2.jpeg)

**FIGURE 2.1** Evolution of Speed and costs of Technology over the Twentieth century

As shown in Figure 2.1, today's advanced technologies comprise multicore central processing units (cPUs), fi eld programmable gate arrays (FPGAs), graphics processing units (GPUs), and the so-called massively parallel architecture chips. A cPU is the brain of the computer and decides how to store information in memory. Multicore cPUs use a shared memory for fast inter-cPU communication, while each individual cPU schedules tasks and performs computations on a given process branch or "thread." Sample architecture of a multicore cPU is shown in Figure 2.2. At the time this book was written, a multicore cPU could cost \$100 and higher.

Unlike cPUs, where the majority of the space on the chip is occupied by memory and scheduler functions, the space on a sample GPU is largely devoted to the computational operations, performed in the so-called arithmetic logic units (AlUs). To further maximize effi ciency of each chip, process threads are executed in parallel batches of identical size. These batches of threads are called *warps.* To minimize

![](_page_2_Figure_0.jpeg)

FIGURE 2.2 Architecture of a Sample Multicore CPU *Source:* Thomas, Howes and Luk (2009)

latency, however, care should be taken to ensure that the threads of the process are similar in terms of the number of loops and conditional exits. In other words, programming expertise is required to ensure that GPUs are deployed with maximum efficiency. Figure 2.3 illustrates sample architecture of the GPU. A popular model of a GPU is Nvidia GTX series, which can retail for \$100 to \$700 per card.

FPGAs are an entirely different class of chips that do not have any fixed instruction set architecture. Instead, an FPGA provides a blank slate of bitwise functional units that can be programmed to create any desired circuit or processor. Some FPGAs

![](_page_2_Figure_4.jpeg)

FIGURE 2.3 Architecture of a Sample GPU Source: Thomas, Howes and Luk (2009)

contain a number of dedicated functional units, such as multipliers and memory blocks. Most of the area of an FPGA, however, is dedicated to the routing infrastructure the run-time connectivity of the FPGA's functional units. Figure 2.4 shows the architecture of a sample FPGA chip.

![](_page_3_Figure_1.jpeg)

**FIGURE 2.4** Architecture of a Sample FPGA chip *Source:* Thomas, Howes and luk (2009)

The main distinction of FPGAs is that the programming code is written directly onto the chip from the outset. FPGAs are programmed using special programming languages, such as verilog or vHDl. The languages are similar to c programming language and are easy to learn. A special FPGA programming device translates verilog or vHDl into Assembly language understood by the FPGA chips. In the absence of FPGAs, trading programs need to be compiled and translated to the computer chips like cPUs during program run time, requiring additional computer operations and eating into the latency. The process of programming an FPGA is rather straightforward and inexpensive. While there exists a signifi cant variation in costs of blank FPGA chips and verilog or vHDl compilers and simulators, quality inexpensive options are commonly available, once again produced to satisfy demand of video gamers. A blank FPGA chip may cost anywhere from \$4 to \$5,000. The verilog software and simulators may be free ("open-source") or \$20,000. The software is then downloaded onto the chip, using the process specifi c to the chip manufacturer. Programming of FPGA chips is often taught in undergraduate electrical engineering programs, and tends to be easy to learn. However, achieving a state-of-the-art FPGA system may require arranging FPGAs in a format known as *massively parallel processor array confi guration,*  demanding advanced understanding of hardware and software optimization.

Performance-wise, FPGAs tend to be superior to GPUs and cPUs, particularly when used to simultaneously process a limited number of time series. Figure 2.5 shows a graphical comparison of effi ciency of key hardware models. The horizontal axis of the fi gure shows the "input" size, or the number of independent variables simultaneously fed into the algorithm. The vertical axis shows the number of computer "cycles" required to perform an operation involving the given number of inputs. As Figure 2.5 illustrates, an FPGA posts best results when the number of inputs is less than 2,000. When the number of inputs exceeds this threshold, the speed of an FPGA becomes comparable to that of a GPU.

![](_page_4_Figure_1.jpeg)

**FIGURE 2.5** comparative Performance of FPGA, GPU, Single cPU, and Quad cPU Architectures *Source:* Thomas, Howes and luk (2009)

The choice of a chip itself is not the single determinant of the speed of the computer program. The speed of each computer cycle is determined by the so-called oscillator crystal within each machine and, most important, organization of the program's algorithm.

## ■ **Messaging**

Hardware is just one of many components of computer technology necessary for achieving successful trading. Another crucial component is messaging, enabling communication among hardware and software modules of various market participants. Just as speed is important in hardware, it is also important in messaging. In fact, it is the speed of messaging that presents a hurdle or a bottleneck for trading communication.

# **Messaging protocols**

Trading messaging is comprised of three levels of protocols, shown in Figure 2.6. The most basic level of communication enables data streaming and is known as the User Datagram Protocol (UDP). UDP is the "bare bones" data communication protocol, lean in its implementation, and utilizing the fewest number of bytes and messages to identify and deliver the stream of data. As a result, UDP is very fast, but does not guarantee delivery of sent data. UDP is the same technology as the one used to stream games and movies over the Internet, where loss of one packet here and there does not signifi cantly impact the viewer's experience. In trading, UDP is sometimes used to transmit quotes, the data that are refreshed continuously, and are, therefore, not very sensitive to lost information. If a particular quote sent from an exchange fails to reach a trader, the resulting impact may be deemed minimal: a new revised quote is already on the way, retiring the lost quote upon hitting the trader's account.

![](_page_5_Figure_2.jpeg)

**FIGURE 2.6** Three levels of complexity of communication Protocols Used in Trading

The integrity of the quote process, however, can matter in trading model development. A trading algorithm developer may rely on the quote stream idiosyncrasies to generate predictive signals about impending market movements. If the structure of the historical quote stream used in model development diff ers signifi cantly from that of the quote stream encountered by the trader "in production" environment, the calculated forecasts may cease working. care should be taken to ensure that the data used in simulation and back-test of the algorithms is structurally compatible to the data received in production environment. At a minimum, the algorithm designer should ascertain that the frequency of quotes received in production matches that in the historical data used in the back-test. More complicated data tests can also be performed. For example, a rolling autocorrelation metric can be computed on the two sets of data, and the distribution of the resulting metrics should be comparable for successful algorithm design and implementation.

The next level of complexity in communication protocols is Transmission control Protocol/Internet Protocol (TcP/IP). TcP/IP is another standard Internet communication protocol, presently used in most e-mail and Web-browsing communication. Unlike the UDP, where individual packets of information do not carry any identifying monikers, all packets of a TcP/IP transmission are sequentially numbered, the total number of bytes within each packet is counted, and undelivered or corrupt data is re-sent. As a result, TcP/IP provides a more secure framework for information delivery, and is used to transmit orders, order acknowledgments, execution acknowledgments, order cancellations, and similarly important information. As a trade-off , TcP/IP tends to be three times slower than UDP. Figure 2.7 summarizes common usage of UDP, TcP/IP and FIX in trading communication.

![](_page_6_Figure_1.jpeg)

**FIGURE 2.7** common Use of Protocols in Trading communication

Both the UDP and TcP/IP, however, require an additional layer of communication to standardize messages of the trading process. Protocols like Financial Information eXchange (FIX), ITcH, OUcH, and FAST are used on top of UDP and TcP to transmit data in a standardized machine-readable format. FIX protocol is a free XMl-based text specifi cation for quote, order, trade and related message transmission. The FIX protocol comprises data fi eld defi nitions, enumerations, and various components, forming messages. Each message is then populated with the user-generated data. Each fi eld of the message, including the version of FIX used, the time stamp, and other information, is separated from the following fi eld by binary 1.

```
8=FIX.4.2 | 9=309 | 35=S | 34=5015 | 52=20070731-15:25:20 | 
131=1185895365 | 301=0 | 55=USD/cAD | 167=FOR | 15=USD | 
132=1.065450 | 133=1.065850 | 134=5000000.0 | 135=5000000.0 | 
647=2000001.0 | 648=2000001.0 | 188=1.06545 | 190=1.06585 | 
60=20070731-15:25:20 | 40=H | 64=20070801 | 10=178
```

#### **FIGURE 2.8** Sample FIX Message

Figure 2.8 illustrates a sample FIX message, transmitting a quote for USD/cAD exchange rate. The shown quote contains the following information:

- Version of FIX, "FIX.4.2" (field number 8)
- The time stamp of the message, "20070731-15:25:20" (field number 52)
- Security identifier, "USD/CAD" (field number 55)
- Security type, "FOR" for foreign exchange (field number 167)
- Base currency, "USD" for U.S.\$ (field number 15)
- Best bid and best ask (fields 132 and 133, respectively)
- Sizes at the best bid and best ask (fields 134 and 135)

Transmission speed of communication messages depends on several factors:

- Size of message
- Connection bandwidth
- TCP/IP and UDP "window" sizes, specifying how many bytes market participants are willing to send and receive at per message "slice." Once the system of one market participant sends out a message, the message is sliced into the individual parcels of a specified window length, a message header is attached to each parcel, and the messages are sent out on their route. The UDP message header typically identifies the destination, and consists of just 8 bytes. The TCP/IP message header includes the sender and destination identifications, parcel sequence number, and the total number of parcels comprising the message, among other variables. The standard TCP/IP header is 20 bytes. The FIX header can be much more elaborate, and is often in excess of 100 bytes.

While FIX is widely used, it is slow in comparison with Nasdaq's protocols known as ITCH and OUCH. The binary nature of ITCH and OUCH ensures that the messages arrive in the machine-readable format, using no processing time to convert them from text to binary and back. In addition to the binary format, ITCH and OUCH messages have a fixed message length, enabling faster transmission. OUCH is the order entry protocol, while ITCH is the outbound quote and trade-data dissemination specification. Yet ITCH and OUCH support only a limited number of messages. OUCH provides the platform for:

- Order entry.
- Replacement and cancellations.
- Receipt of execution acknowledgements.

ITCH is built for fast and lean quote and past trade data dissemination, and is able to transmit:

- Order-level data.
- Trade messages.
- Net order imbalance data.

- Administrative messages.
- Event controls, such as start of day, end of day, and emergency market halt/resume.

For more complex messages, ITcH- and OUcH-enabled market participants are often required to use FIX.

# **Core Message architecture**

Tick information is transmitted among market participants using one or several quote messaging specifi cations. FIX, ITcH, OUcH, and FAST are just a few message languages enabling transmission of critical trading information. Despite their complicated acronyms, messaging is built around strikingly simple architecture, as illustrated in Figure 2.9.

![](_page_8_Figure_5.jpeg)

**FIGURE 2.9** core Message Architecture in Trading

As shown in Figure 2.9, every stream of quote and trade communication includes the following key messages:

- 1. *Session start* is the message sent in the beginning of every communication session, sometimes only once a day. The session start message notifi es relevant market participants that the entity is open for trading and desires to establish a communication stream.
- 2. *Heartbeat* is a recurrent message that notifi es the participant's communication parties that the participant is online, in a state of good technological health, and open for business. Parties that fail to receive their communication partners'

heartbeat messages for a preconfigured period of time often shut down the communication channel. The communication channel may then be reinstated using the "session start" sequence.

- 3. *Quote* message is a message carrying quote information, such as best bid and ask prices and sizes. Level II data, like the depth of the order book behind the best bid and ask quotes, may also be transmitted using quote messages.
- 4. *Order* message is used to transmit actual order information. A typical order message includes a buy or sell identifier, an order type—a market, limit or other specification, order size, and a desired execution price and validity period (day, good-till-canceled) in the case of limit orders.
- 5. *Order cancellation* message includes the unique identifier of the previously placed order that now needs to be canceled.
- 6. *Order acknowledgment* and *order cancellation acknowledgment* messages include confirmations of order placement or order cancellation, respectively.
- 7. *Execution acknowledgment* messages specify the details of execution: time of execution, obtained price, and execute quantity.
- 8. *Session end* message informs parties that a given trading entity has stopped trading and quoting for the day.

The resulting trade messaging flow comprises intuitive methodology to deliver effective, reliable, and traceable communication. Most trading outfits log their daily communication for easy reconciliation and fast identification of potential issues, such as network connectivity problems, algorithm errors, and the like.

# **Speed and Security**

Neither TCP/IP nor UDP incorporate encryption. In other words, most TCP/IP and UDP messages are sent via Internet networks in plain text. FIX provides optional encryption at a considerable latency. While ITCH and OUCH send messages in a binary format, most Nasdaq OMX messages are still sent unencrypted over the Internet networks.

What kind of risk do market participants face by sending unencrypted messages? To answer this question, one needs to consider the current layout and flow of the Internet traffic. Today, most Internet traffic in the world flows through about 80 "core" nodes. These nodes, such as major Internet service providers (ISPs) like Verizon, have some security measures in place, limiting the incidence of spying activity at these nodes. At the same time, nodes can be quite congested, slowing down messaging traffic without consideration to its urgency.

If the core nodes were to fail, 70 percent of Internet traffic would flow through peer-to-peer networks, redundant backup structures in which the traffic would hop from one local user to another, in a distributed fashion. While the peer-to-peer network configuration can allow the network participants to observe each other's traffic and read unencrypted messages in full, the peer-to-peer communication is sufficiently randomized to prevent any peer party to accumulate the entire message flow. Still, peer-to-peer networks may be vulnerable to malicious intent, and the resulting potential hijacking of the order flow could destroy markets and cause tremendous losses for all market participants.

![](_page_10_Figure_0.jpeg)

**FIGURE 2.10** Messaging Architecture in client-Server, Peer-to-Peer, and co-location Models

Figure 2.10 describes three common Internet communication models prevalent in trading, including the so-called co-location model. In the co-location model, traders' servers are housed in the same secure facility as the exchange's matching servers. In the co-location scenario, trading servers have dedicated network access to the exchange servers. The dedicated network access comprises a private secure communication line from the trading servers directly to the exchange, minimizing the risk of malicious intervention and ensuring a safe environment for all market participants. co-location also provides such benefi ts as speed advantage: the servers of a chicago trader co-located with nasdaq, for example, would allow the trader to shave anywhere from 17 to 22 milliseconds in a round-trip order latency due to the physical distance between new york and chicago, all in addition to the immeasurable savings resulting from the security of the co-located trading connection. Figure 2.11 summarizes latency among selected co-location centers worldwide.

|                   | New<br>York, NY | Washington,<br>DC | toronto,<br>Canada | Chicago,<br>IL | London,<br>U.K. | Frankfurt,<br>Germany | Sao paolo,<br>Brazil | tokyo,<br>Japan |
|-------------------|-----------------|-------------------|--------------------|----------------|-----------------|-----------------------|----------------------|-----------------|
| newark, nJ        | 0.314           | 3.400             | 9.470              | 15.175         | 65.763          | 74.383                | 109.414              | 141.640         |
| new york, ny      |                 | 4.057             | 9.784              | 15.291         | 65.533          | 74.153                | 109.100              | 141.756         |
| Washington, Dc    |                 |                   | 13.270             | 14.175         | 69.083          | 78.164                | 111.960              | 140.640         |
| Toronto, On       |                 |                   |                    | 10.795         | 75.233          | 83.853                | 118.884              | 136.910         |
| chicago, Il       |                 |                   |                    |                | 80.740          | 89.360                | 123.485              | 127.595         |
| london, U.K.      |                 |                   |                    |                |                 | 8.620                 | 183.253              | 215.825         |
| Frankfurt,        |                 |                   |                    |                |                 |                       | 183.253              | 215.825         |
| Germany           |                 |                   |                    |                |                 |                       |                      |                 |
| Sao Paolo, Brazil |                 |                   |                    |                |                 |                       |                      | 249.950         |

**FIGURE 2.11** latency Incurred by Electronic Signals Traveling over Optical Fiber networks between Pairs of locations

Within most co-location data centers, servers are positioned at various distances from the exchange server itself, raising natural concerns about "fairness" of connections of all traders co-located in a given facility. A physical distance difference of as little as 100 feet may result in one microsecond (one millionth of a second) time delay on every message sent and received, giving traders co-located near the exchange servers a potential advantage. To address such issues, the Nasdaq co-location center guarantees an equidistant length of fiber-optic cable from the servers to the exchange to the servers of each trader co-located in the Nasdaq's facility. The cable lengths are identical down to the millimeter, and can be seen coiled near the servers of traders physically close to servers of the exchange.

Although some market participants believe co-location to be unaffordably expensive, the real numbers point to the opposite. At a data center in Secaucus, New Jersey, for example, a private company, Equinix, offers co-location-equivalent proximity services with the minimum monthly charges broken down as follows:

- A cabinet for the trader's hardware equipped with biometric security scanners and air-conditioning runs \$1,500 per month.
- A 20-amp 120-volt primary power source costs \$350 per month.
- An additional 20-amp 120-volt power source designed for redundancy costs an additional \$175 per month.
- Finally, a connection to the ultra-fast communication network linking various data centers around the world runs an additional \$325 per month.

The grand total of the proximity setup adds up to just \$2,350 per month, a negligible cost for any serious investor.

# **Network Throughput**

The messaging architecture is a resource available to all market participants, yet it is not free to all. Exchanges, for example, have to continuously enhance their infrastructure to ensure that the bandwidth of their connections is broad enough to allow uninhibited message traffic among all interested traders. Perhaps the biggest challenge to exchanges and other order-matching venues is the sheer volume of order cancellations. According to Hautsch and Huang (2011), on Nasdaq, 95 percent of all limit orders are canceled within one minute from the time the orders are placed. Hasbrouck and Saar (2011) report similar activity grouped into brisk order placement and cancellation "runs." While this activity may seem malicious to an uninitiated observer, the explanation for such behavior is quite simple: as described in detail in Chapters 10, automated market makers need to quote close to the market price—"stay on top of the book"—in order to be successfully and promptly matched, thus ensuring a steady revenue stream. Once the market moves away from the quotes of the market maker, it is in the best interests of the market maker to cancel the orders and to resubmit them at the new best bid and best offer prices. In addition, as explained in Chapter 12, on exchanges with time-price priority of limit order books, market participants may place and then innocuously cancel excessive numbers limit orders to secure their execution priority, in a practice known as "layering."

In such dynamics, many trading venues are caught within a vicious circle: on the one hand, they are competing to attract the market makers, but on the other, many order-cancelling market makers are eroding network resources, resulting in missed quotes and other delays for all market participants. Even the co-location does not help fully navigate the bandwidth issue, as co-location space also faces capacity constraints: nasdaq has seen so much demand in its co-location hangar in Mahwah, new Jersey, that it is reportedly running out of space to off er to the parties interested in co-locating there. As discussed in chapters 3 and 12, a promising solution to the network bandwidth issue, known as *pro-rata execution*, has been developed and implemented at selected exchanges.

#### ■ **Software**

High-frequency trading systems are ultimately software applications deployed over hardware and messaging described above. As with any software system, an HFT system begins with an idea, known as an *algorithm* in computer-science lingo, that is subsequently coded in a chosen computer language into a full-blown software program. The term *algorithm* is properly defi ned as logic, or a sequence of high-level actions, developed to explain to a computer how to implement a given task at hand. The algorithm does not delve into the details of actual coding or programming the system, but may still take into account the idiosyncrasies of the hardware and messaging structure on which the algorithm will be ultimately implemented. Algorithms are often visualized in diagrams. The key elements of the algorithm diagrams are summarized in Figure 2.12.

The algorithm elements shown in Figure 2.12 will be used throughout the book to explain algorithm designs of common HFT strategies. Figure 2.13 illustrates the step-by-step process of the following simple market-making algorithm:

- 1. Begin program.
- 2. check market conditions: Are market conditions suitable for market making?
- 3. If yes, start market making.
- 4. If no, wait one minute.
- 5. Repeat step 2.

The algorithm presented in Figure 2.13 is "nested," or comprises two additional algorithms marked in Figure 2.13 only as "check market conditions" and "Start market making." The nested tasks can be the critical "secret sauce" that distinguishes good HFT systems from bad ones. Usually, the tasks are designed on the basis of advanced research, where the task is selected among several competing ideas given

![](_page_12_Figure_10.jpeg)

positive results of rigorous testing. The two nested tasks shown in Figure 2.13 are explained in detail in chapter 15.

![](_page_13_Figure_1.jpeg)

**FIGURE 2.13** Sample Market-Making Algorithm

The term *algorithm* is often used synonymously with the terms *high-frequency trading, systematic trading, electronic trading,* and *low-latency trading.* The distinctions among the terms, however, are signifi cant enough to warrant some explanation. A *system* usually refers to a highly methodical approach to a process. Systematic trading, therefore, is following some rigid frameworks, but does not have to be fully automated. A trader can be considered systematic if he manually places trades when certain indicators form a specifi c pattern. The term *systematic* was coined to distinguish traders practicing methodical allocations from traders using their intuition or discretion, and hence known as *discretionary* traders. All high-frequency and algorithmic traders are also systematic.

The term *electronic* describes the execution preferences of the trader: whether he chooses to place orders electronically or, perhaps, over the telephone. All high-frequency trading, algorithmic trading, and low-latency trading are necessarily electronic, but systematic trading may involve nonelectronic components. The reverse, however, does not have to be the case; many electronic trading systems route only orders that may or may not be placed algorithmically. As most markets and traders are moving on to electronic platforms, however, the term *electronic trading* is becoming implicit and obsolete.

*Low-latency* trading refers to trading that utilizes fast connectivity between traders and exchanges. As described in the previous section, latency measures the time distance between the trader and the exchange. Most latency measurements are currently recorded in microseconds. High-frequency trading systems often also happen to be low-latency, but the reverse does not have to hold: low-latency systems are often deployed by low-frequency traders to obtain better prices on trades.

Once an algorithm is designed, it is broken down into components and coded in a language understood by computers. The goal of coding is to accurately translate the logic of the algorithm into computer "speak" and, in the process, to create as little delay as possible during "run time," when the computer will read and interpret the code. The code written directly to FPGA chips is presently the fastest. Still, many high-frequency traders deploy standard non-FPGA architecture and rely on languages such as C++ and Java to code their systems. While C++ remains the fastest computer language easily understood by humans, many systems are coded in Java with workarounds of its slowest components. Thus, for example, the famed Nasdaq OMX system is reportedly coded in Java with Java garbage collection disabled and replaced with C++-like direct memory access for increased speed. Chapter 16 describes best practices of coding implementation.

The code outlining the actual trading logic of an algorithm tends to be quite short. In many successful cases, the trading logic comprises as few as 50 lines of code. In addition to the actual decisions to buy and sell, however, every HFT system incorporates supporting quote data retrieval functionality that may number in 10,000+ lines of code, as well as the trade send-off and acknowledgment receipt applications that can also take as much as 5,000 lines of code. Perhaps the most lengthy, yet mandatory, component of each HFT system is its risk management checks and balances, which can total 50,000+ lines of code. Risk management of HFT is discussed in detail in Chapter 14 of this book.

### ■ **Summary**

Algorithmic execution is inseparable from today's markets. It is a necessary function that delivers considerable value to all investors, large and small. With plummeting technology costs, most investors today can afford to build and use advanced algos, including algos designed for high-frequency trading, previously available only to a select few market participants. Services such as co-location provide added benefits of security and speed.

#### ■ **End-of-Chapter Questions**

- 1. Would you encrypt your trading orders before transmitting them to the execution venue over the Internet? Explain.
- 2. Mr. Smith has read about the "arms race" of computer technology in the financial services industry and decides to invest into the latest super computer to increase the odds of fast order transmission. Is Mr. Smith's investment justified? Where does most message congestion occur in the cyber-universe today?
- 3. What is co-location?
- 4. On average, how much slower is the transmission of trade order messages in comparison with quote messages?
- 5. What is a heartbeat?
- 6. The best offer on exchange A contains 300 units of instrument X, the best offer on exchange B contains 500 units, and the best offer on exchange C contains just 100 units. Your customer wants you to buy 550 units on his behalf. How would you break up the customer's order and send them to exchanges under the minimal impact algorithm?
## CHAPTER 1

## Introduction

igh-frequency trading has been taking Wall Street by storm, and for a good reason: its immense profitability. According to  $\Lambda lpha$  $\mathsf{L}$  magazine, the highest earning investment manager of 2008 was Jim Simons of Renaissance Technologies Corp., a long-standing proponent of high-frequency strategies. Dr. Simons reportedly earned \$2.5 billion in 2008 alone. While no institution was thoroughly tracking performance of highfrequency funds when this book was written, colloquial evidence suggests that the majority of high-frequency managers delivered positive returns in 2008, whereas 70 percent of low-frequency practitioners lost money, according to the *New York Times*. The profitability of high-frequency enterprises is further corroborated by the exponential growth of the industry. According to a February 2009 report from Aite Group, high-frequency trading now accounts for over 60 percent of trading volume coming through the financial exchanges. High-frequency trading professionals are increasingly in demand and reap top-dollar compensation. Even in the worst months of the 2008 crisis, 50 percent of all open positions in finance involved expertise in high-frequency trading (Aldridge, 2008). Despite the demand for information on this topic, little has been published to help investors understand and implement high-frequency trading systems.

So what is high-frequency trading, and what is its allure? The main innovation that separates high-frequency from low-frequency trading is a high turnover of capital in rapid computer-driven responses to changing market conditions. High-frequency trading strategies are characterized by a higher number of trades and a lower average gain per trade. Many traditional money managers hold their trading positions for weeks or even months, generating a few percentage points in return per trade. By comparison, high-frequency money managers execute multiple trades each day, gaining a fraction of a percent return per trade, with few, if any, positions carried overnight. The absence of overnight positions is important to investors and portfolio managers for three reasons:

- 1. The continuing globalization of capital markets extends most of the trading activity to 24-hour cycles, and with the current volatility in the markets, overnight positions can become particularly risky. Highfrequency strategies do away with overnight risk.
- 2. High-frequency strategies allow for full transparency of account holdings and eliminate the need for capital lock-ups.
- 3. Overnight positions taken out on margin have to be paid for at the interest rate referred to as an overnight carry rate. The overnight carry rate is typically slightly above LIBOR. With volatility in LIBOR and hyperinflation around the corner, however, overnight positions can become increasingly expensive and therefore unprofitable for many money managers. High-frequency strategies avoid the overnight carry, creating considerable savings for investors in tight lending conditions and in high-interest environments.

High-frequency trading has additional advantages. High-frequency strategies have little or no correlation with traditional long-term buy and hold strategies, making high-frequency strategies valuable diversification tools for long-term portfolios. High-frequency strategies also require shorter evaluation periods because of their statistical properties, which are discussed in depth further along in this book. If an average monthly strategy requires six months to two years of observation to establish the strategy's credibility, the performance of many high-frequency strategies can be statistically ascertained within a month.

In addition to the investment benefits already listed, high-frequency trading provides operational savings and numerous benefits to society. From the operational perspective, the automated nature of high-frequency trading delivers savings through reduced staff headcount as well as a lower incidence of errors due to human hesitation and emotion.

Among the top societal benefits of high-frequency strategies are the following:

- Increased market efficiency
- Added liquidity
- Innovation in computer technology
- Stabilization of market systems

High-frequency strategies identify and trade away temporary market inefficiencies and impound information into prices more quickly. Many high-frequency strategies provide significant liquidity to the markets, making the markets work more smoothly and with fewer frictional costs for all investors. High-frequency traders encourage innovation in computer technology and facilitate new solutions to relieve Internet communication bottlenecks. They also stimulate the invention of new processors that speed up computation and digital communication. Finally, high-frequency trading stabilizes market systems by flushing out toxic mispricing.

A fit analogy was developed by Richard Olsen, CEO of Oanda, Inc. At a March 2009 FXWeek conference, Dr. Olsen suggested that if financial markets can be compared to a human body, then high-frequency trading is analogous to human blood that circulates throughout the body several times a day flushing out toxins, healing wounds, and regulating temperature. Lowfrequency investment decisions, on the other hand, can be thought of as actions that destabilize the circulatory system by reacting too slowly. Even a simple decision to take a walk in the park exposes the body to infection and other dangers, such as slips and falls. It is high-frequency trading that provides quick reactions, such as a person rebalancing his footing, that can stabilize markets' reactions to shocks.

Many successful high-frequency strategies run on foreign exchange, equities, futures, and derivatives. By its nature, high-frequency trading can be applied to any sufficiently liquid financial instrument. (A "liquid instrument" can be a financial security that has enough buyers and sellers to trade at any time of the trading day.)

High-frequency trading strategies can be executed around the clock. Electronic foreign exchange markets are open 24 hours, 5 days a week. U.S. equities can now be traded "outside regular trading hours," from 4 A.M. EST to midnight EST every business day. Twenty-four-hour trading is also being developed for selected futures and options.

Many high-frequency firms are based in New York, Connecticut, London, Singapore, and Chicago. Many Chicago firms use their proximity to the Chicago Mercantile Exchange to develop fast trading strategies for futures, options, and commodities. New York and Connecticut firms tend to be generalist, with a preference toward U.S. equities. European time zones give Londoners an advantage in trading currencies, and Singapore firms tend to specialize in Asian markets. While high-frequency strategies can be run from any corner of the world at any time of day, natural affiliations and talent clusters emerge at places most conducive to specific types of financial securities.

The largest high-frequency names worldwide include Millennium, DE Shaw, Worldquant, and Renaissance Technologies. Most of the highfrequency firms are hedge funds or other proprietary investment vehicles

| Strategy                         | Description                                                                                             | Typical<br>Holding Period |
|----------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------|
| Automated liquidity<br>provision | Quantitative algorithms for optimal<br>pricing and execution of<br>market-making positions              | <1 minute                 |
| Market microstructure<br>trading | Identifying trading party order flow<br>through reverse engineering of<br>observed quotes               | <10 minutes               |
| Event trading                    | Short-term trading on macro events                                                                      | <1 hour                   |
| Deviations arbitrage             | Statistical arbitrage of deviations<br>from equilibrium: triangle trades,<br>basis trades, and the like | <1 day                    |

## **TABLE 1.1** Classification of High-Frequency Strategies

that fly under the radar of many market participants. Proprietary trading desks of major banks, too, dabble in high-frequency products, but often get spun out into hedge fund structures once they are successful.

Currently, four classes of trading strategies are most popular in the high-frequency category: automated liquidity provision, market microstructure trading, event trading, and deviations arbitrage. Table 1.1 summarizes key properties of each type.

Developing high-frequency trading presents a set of challenges previously unknown to most money managers. The first is dealing with large volumes of intra-day data. Unlike the daily data used in many traditional investment analyses, intra-day data is much more voluminous and can be irregularly spaced, requiring new tools and methodologies. As always, most prudent money managers require any trading system to have at least two years worth of back testing before they put money behind it. Working with two or more years of intra-day data can already be a great challenge for many. Credible systems usually require four or more years of data to allow for full examination of potential pitfalls.

The second challenge is the precision of signals. Since gains may quickly turn to losses if signals are misaligned, a signal must be precise enough to trigger trades in a fraction of a second.

Speed of execution is the third challenge. Traditional phone-in orders are not sustainable within the high-frequency framework. The only reliable way to achieve the required speed and precision is computer automation of order generation and execution. Programming high-frequency computer systems requires advanced skills in software development. Run-time mistakes can be very costly; therefore, human supervision of trading in production remains essential to ensure that the system is running within prespecified risk boundaries. Such discretion is embedded in human supervision. However, the intervention of the trader is limited to one decision only: whether the system is performing within prespecified bounds, and if it is not, whether it is the right time to pull the plug.

From the operational perspective, the high speed and low transparency of computer-driven decisions requires a particular comfort level with computer-driven execution. This comfort level may be further tested by threats from Internet viruses and other computer security challenges that could leave a system paralyzed.

Finally, just staying in the high-frequency game requires ongoing maintenance and upgrades to keep up with the "arms race" of information technology (IT) expenditures by banks and other financial institutions that are allotted for developing the fastest computer hardware and execution engines in the world.

Overall, high-frequency trading is a difficult but profitable endeavor that can generate stable profits under various market conditions. Solid footing in both theory and practice of finance and computer science are the normal prerequisites for successful implementation of high-frequency environments. Although past performance is never a guarantee of future returns, solid investment management metrics delivered on auditable returns net of transaction costs are likely to give investors a good indication of a high-frequency manager's abilities.

This book offers the first applied "how to do it" manual for building high-frequency systems, covering the topic in sufficient depth to thoroughly pinpoint the issues at hand, yet leaving mathematical complexities to their original publications, referenced throughout the book.

The following professions will find the book useful:

- Senior management in investment and broker-dealer functions seeking to familiarize themselves with the business of high-frequency trading
- Institutional investors, such as pension funds and funds of funds, desiring to better understand high-frequency operations, returns, and risk
- Quantitative analysts looking for a synthesized guide to contemporary academic literature and its applications to high-frequency trading
- IT staff tasked with supporting a high-frequency operation
- Academics and business students interested in high-frequency trading
- Individual investors looking for a new way to trade
- Aspiring high-frequency traders, risk managers, and government regulators

The book has five parts. The first part describes the history and business environment of high-frequency trading systems. The second part reviews the statistical and econometric foundations of the common types of high-frequency strategies. The third part addresses the details of modeling high-frequency trading strategies. The fourth part describes the steps required to build a quality high-frequency trading system. The fifth and last part addresses the issues of running, monitoring, and benchmarking highfrequency trading systems.

The book includes numerous quantitative trading strategies with references to the studies that first documented the ideas. The trading strategies discussed illustrate practical considerations behind high-frequency trading. Chapter 10 considers strategies of the highest frequency, with position-holding periods of one minute or less. Chapter 11 looks into a class of high-frequency strategies known as the market microstructure models, with typical holding periods seldom exceeding 10 minutes. Chapter 12 details strategies capturing abnormal returns around ad hoc events such as announcements of economic figures. Such strategies, known as "event arbitrage" strategies, work best with positions held from 30 minutes to 1 hour. Chapter 13 addresses a gamut of other strategies collectively known as "statistical arbitrage" with positions often held up to one trading day. Chapter 14 discusses the latest scientific thought in creating multistrategy portfolios.

The strategies presented are based on published academic research and can be readily implemented by trading professionals. It is worth keeping in mind, however, that strategies made public soon become obsolete, as many people rush in to trade upon them, erasing the margin potential in the process. As a consequence, the best-performing strategies are the ones that are kept in the strictest of confidence and seldom find their way into the press, this book being no exception. The main purpose of this book is to illustrate how established academic research can be applied to capture market inefficiencies with the goal of stimulating readers' own innovations in the development of new, profitable trading strategies.
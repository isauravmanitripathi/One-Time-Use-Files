## Chapter 24

# Introduction to QSTrader

In this chapter the freely-available open-source backtesting engine–QSTrader–will be introduced. This software is used for nearly all of the trading strategy simulations within this book.

QSTrader is a full portfolio and order management system (OMS) containing modules for data ingestion, event-driven backtesting, portfolio construction, position tracking, position sizing, risk management, execution simulation and simulated brokerage connection.

The project homepage is currently hosted on GitHub at [https://github.com/mhallsmoore/](https://github.com/mhallsmoore/qstrader) [qstrader](https://github.com/mhallsmoore/qstrader). Please visit it for the latest project news.

### 24.1 Motivation for QSTrader

One of the most important moments in the development of a quantitative trading strategy occurs when a backtested strategy is finally set to trade live. This usually involves a complex transition from "research style" code (commonly written without proper software engineering methodology) to deployment in a production environment, often on a remote server.

Unfortunately the actual performance of the deployed strategy can be significantly worse than that of the same backtested system. There are many reasons for this:

- Overfit Models The trading strategy was fit too heavily to historical data and was not sufficiently validated.
- Transaction costs These include spread, fees, slippage and market impact.
- Latency to liquidity provider This is the time taken between issuing an order to a brokerage and the brokerage executing it.
- Market regime change A strategy or portfolio might have behaved well in previous market conditions but fundamental changes to the market, such as a new regulatory environment reduce the performance of the strategy.
- Strategy decay The strategy eventually ends up being replicated by too many traders and thus becomes "arbitraged away".

The most common reason for significant underperformance compared to a backtest, apart from overfit models, is incomplete transaction cost handling in the simulation. Spread, slippage, fees and market impact all contribute to reduced profitability when a strategy is traded live.

While vectorised backtests are simple to code they are often severely lacking in respect of proper implementation details. Transaction costs are usually ignored and "nitty gritty" implementation details are idealised in order to minimise code complexity.

This motivated the philosophy and subsequent development of QSTrader. QSTrader has been designed to provide a realistic simulation environment that attempts to mirror the live deployment of a trading strategy as much as possible. For instance, realistic brokerage fees are turned on by default–an unusual design choice compared to many other backtesting systems.

It is the author's wish that the presented backtests of trading strategies within this book are as realistic as possible. This provides readers with a detailed insight into their real-world performance before deciding to trade them live.

Another motivating goal for QSTrader was to ensure that it was freely available by releasing it under a permissive open source license (the [MIT license\)](https://github.com/mhallsmoore/qstrader/blob/master/LICENSE). This was to encourage contributions from the wider community. It has been developed and tested in Python 2.7.x, 3.4.x and 3.5.x to allow straightforward cross-platform compatibility.

In the twelve months since development began QSTrader has attracted more than a dozen volunteer developers, of which five have made significant contributions, with three in particular having provided exceptional contributions to the project. The author would like to personally thank [Ryan Kennedy,](https://github.com/ryankennedyio) [Femto Trader](https://github.com/femtotrader) and [Nick Willemse](https://github.com/nwillemse) for their extensive generosity and fantastic contributions to the QSTrader project.

QSTrader is strongly influenced by another QuantStart project–QSForex–also available under a permissive open-source license. QSForex only supports one brokerage–OANDA–via their RESTful API. QSTrader, however, is being developed to connect to the newly released Interactive Brokers Python API, which was released very close to the publication date of this book. The eventual goal is to allow equities, ETFs and forex to all be traded under the same portfolio framework.

The project page of QSTrader will always be available on Github at [https://github.com/](https://github.com/mhallsmoore/qstrader) [mhallsmoore/qstrader](https://github.com/mhallsmoore/qstrader). Please head there in order to study the most recent installation instructions and documentation.

Ultimately, QSTrader will be used for all of the trading strategies within this book. At this stage however it is under active development both by the author and the community. As new modules are released the book, strategies and their performance will be updated.

### 24.2 Design Considerations

The design of QSTrader is equivalent to the type of bespoke algorithmic trading infrastructure stack that might be found in a small quantitative hedge fund manager. Thus, the author considers the end goal of this project to be a fully open-source institutional grade production-ready portfolio and order management system, with risk management layers across positions, portfolios and the infrastructure as a whole.

QSTrader will eventually allow end-to-end automation, meaning that minimal human intervention is required for the system to trade once it is set "live". It is of course impossible to completely eliminate human involvement, especially where input data quality is concerned as with erroneous ticks from data vendors. However it is certainly possible to have the system running in an automated fashion for the majority of the time.

The design calls for the infrastructure to mirror that which might be found in a small quant fund or family office quant arm. The functionality within QSTrader is highly modular and loosely coupled.

The main components are the PriceHandler, Strategy, PortfolioHandler, PositionSizer, RiskManager and ExecutionHandler. They handle portfolio/order management system and brokerage connection functionality.

The system is event-driven and communicates via an events queue using subclassed Event objects. The full list of components is as follows:

- Event All "messages" of data within the system are encapsulated in an Event object. The various events include TickEvent, BarEvent, SignalEvent, SentimentEvent, OrderEvent and FillEvent.
- Position This class encapsulates all data associated with an open position in an asset. That is, it tracks the realised and unrealised profit and loss (PnL) by averaging the multiple "legs" of the transaction, inclusive of transaction costs.
- Portfolio The Portfolio class encapsulates a list of Positions, as well as a cash balance, equity and PnL. This object is used by the PositionSizer and RiskManager objects for portfolio construction and risk management purposes.
- PortfolioHandler The PortfolioHandler class is responsible for the management of the current Portfolio, interacting with the RiskManager and PositionSizer as well as submitting orders to be executed by an ExecutionHandler.
- PriceHandler The PriceHandler and derived subclasses are used to ingest financial asset pricing data from various sources. In particular, there are separate class hierarchies for bar and tick data.
- Strategy The Strategy object and subclasses contain the "alpha generation" code for creating trading signals.
- PositionSizer The PositionSizer class provides the PortfolioHandler with guidance on how to size positions once a strategy signal is received. For instance the PositionSizer could incorporate a Kelly Criterion approach or carry out monthly rebalancing of a fixedweight portfolio.
- RiskManager The RiskManager is used by the PortfolioHandler to verify, modify or veto any suggested trades that pass through from the PositionSizer, based on the current composition of the portfolio and external risk considerations (such as correlation to indices or volatility).
- ExecutionHandler This object is tasked with sending orders to brokerages and receiving "fills". For backtesting this behaviour is simulated, with realistic fees taken into account.
- Statistics This is used to produce performance reports from backtests. A "tearsheet" capability has recently been added providing detailed statistics on equity curve performance, with benchmark comparison.

• Backtest - Encapsulates the event-driven behaviour of the system, including the handling of the events queue. Requires knowledge of all other components in order to simulate a full backtest.

This list is not exhaustive. It is however extremely modular and flexible, allowing significant customisation for particular trading styles and frequencies.

### 24.3 Installation

At this stage QSTrader is still being actively developed and the installation instructions continue to evolve. However, you can find the latest installation process at the following URL: [https:](https://github.com/mhallsmoore/qstrader) [//github.com/mhallsmoore/qstrader](https://github.com/mhallsmoore/qstrader).

Usage will be demonstrated via the examples throughout the remainder of the book.
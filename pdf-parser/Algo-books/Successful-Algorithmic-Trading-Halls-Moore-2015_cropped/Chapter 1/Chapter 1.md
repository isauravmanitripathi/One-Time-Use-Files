## Chapter 1

# Introduction to the Book

### 1.1 Introduction to QuantStart

QuantStart was founded by Michael Halls-Moore, in 2010, to help junior quantitative analysts (QAs) nd jobs in the tough economic climate. Since then the site has evolved to become a substantial resource for quantitative nance. The site now concentrates on algorithmic trading, but also discusses quantitative development, in both Python and C++.

Since March 2010, QuantStart has helped over 200,000 visitors improve their quantitative nance skills. You can always contact QuantStart by sending an email to [mike@quantstart.com.](mailto:mike@quantstart.com)

#### 1.2 What is this Book?

Successful Algorithmic Trading has been written to teach retail discretionary traders and trading professionals, with basic programming skills, how to create fully automated protable and robust algorithmic trading systems using the Python programming language. The book describes the nature of an algorithmic trading system, how to obtain and organise nancial data, the concept of backtesting and how to implement an execution system. The book is designed to be extremely practical, with liberal examples of Python code throughout the book to demonstrate the principles and practice of algorithmic trading.

#### 1.3 Who is this Book For?

This book has been written for both retail traders and professional quants who have some basic exposure to programming and wish to learn how to apply modern languages and libraries to algorithmic trading. It is designed for those who enjoy self-study and can learn by example. The book is aimed at individuals interested in actual programming and implementation, as I believe that real success in algorithmic trading comes from fully understanding the implementation details.

Professional quantitative traders will also nd the content useful. Exposure to new libraries and implementation methods may lead to more optimal execution or more accurate backtesting.

#### 1.4 What are the Prerequisites?

The book is relatively self-contained, but does assume a familiarity with the basics of trading in a discretionary setting. The book does not require an extensive programming background, but basic familiarity with a programming language is assumed. You should be aware of elementary programming concepts such as variable declaration, ow-control (if-else) and looping (for/while).

Some of the trading strategies make use of statistical machine learning techniques. In addition, the portfolio/strategy optimisation sections make extensive use of search and optimisation algorithms. While a deep understanding of mathematics is not absolutely necessary, it will make it easy to understand how these algorithms work on a conceptual level.

If you are rusty on this material, or it is new to you, have a look at the [QuantStart reading](http://www.quantstart.com/articles/Quantitative-Finance-Reading-List) [list.](http://www.quantstart.com/articles/Quantitative-Finance-Reading-List)

#### 1.5 Software/Hardware Requirements

Quantitative trading applications in Python can be developed in Windows, Mac OSX or Linux. This book is agnostic to the operating system so it is best to use whatever system you are comfortable with. I do however recommend Mac OSX or Linux (I use Ubuntu), as I have found installation and data management to be far more straightforward.

In order to write Python programs you simply need access to a text editor (preferably with syntax highlighting). On Windows I tend to use [Notepad++.](http://notepad-plus-plus.org/) On Mac OSX I make use of [SublimeText.](http://www.sublimetext.com/) On Ubuntu I tend to use emacs, but of course, you can use vim.

The code in this book will run under both Python version 2.7.x (specically 2.7.6 on my Ubuntu 14.04 machine) and Python 3.4.x (specically 3.4.0 on my Ubuntu 14.04 machine).

In terms of hardware, you will probably want at least 1GB RAM, but more is always better. You'll also want to use a relatively new CPU and plenty of hard disk storage for historical data, depending upon the frequency you intend to trade at. A 200Gb hard disk should be sucient for smaller data, while 1TB is useful for a wide symbol universe of tick data.

#### 1.6 Book Structure

The book is designed to create a set of algorithmic trading strategies from idea to automated execution. The process followed is outlined below.

- Why Algorithmic Trading? - The benets of using a systematic/algorithmic approach to trading are discussed as opposed to a discretionary methodology. In addition the dierent approaches taken to algorithmic trading are shown.
- Trading System Development - The process of developing an algorithmic trading system is covered, from hypothesis through to live trading and continual assessment.
- Trading System Design - The actual components forming an algorithmic trading system are covered. In particular, signal generation, risk management, performance measurement, position sizing/leverage, portfolio optimisation and execution.
- Trading System Environment - The installation procedure of all Python software is carried out and historical data is obtained, cleaned and stored in a local database system.
- Time Series Analysis - Various time series methods are used for forecasting, meanreversion, momentum and volatility identication. These statistical methods later form the basis of trading strategies.
- Optimisation - Optimisation/search algorithms are discussed and examples of how they apply to strategy optimisation are considered.
- Performance Measurement - Implementations for various measures of risk/reward and other performance metrics are described in detail.
- Risk Management - Various sources of risk aecting an algorithmic trading system are outlined and methods for mitigating this risk are provided.
- Trading Strategy Implementation - Examples of trading strategies based o statistical measures and technical indicators are provided, along with details of how to optimise a portfolio of such strategies.
- Execution - Connecting to a brokerage, creating an automated event-based trading infrastructure and monitoring/resilience tools are all discussed.

#### 1.7 What the Book does not Cover

This is not a beginner book on discretionary trading, nor a book lled with technical analysis trading strategies. If you have not carried out any trading (discretionary or otherwise), I would suggest reading some of the books on the [QuantStart reading list.](http://www.quantstart.com/articles/Quantitative-Finance-Reading-List)

It is also not a Python tutorial book, although once again the QuantStart reading list can be consulted. While every eort has been made to introduce the Python code as each example warrants it, a certain familiarity with Python will be extremely helpful.

#### 1.8 Where to Get Help

The best place to look for help is the articles list on [QuantStart.com,](http://www.quantstart.com) found at [QuantStart.com/articles](http://www.quantstart.com/articles) or by contacting me at [mike@quantstart.com.](mailto:mike@quantstart.com) I've written over 140 articles about quantitative nance (and algorithmic trading in particular), so you can brush up by reading some of these.

I also want to say thank you for purchasing the book and helping to support me while I write more content - it is very much appreciated. Good luck with your algorithmic strategies! Now onto some trading...
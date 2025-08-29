# Chapter 1

# Introduction To Advanced Algorithmic Trading

## 1.1 The Hunt for Alpha

The goal of the quantitative trading researcher is to seek out what is termed alpha–new streams of uncorrelated risk-adjusted returns–and then exploit these returns via a systematic trading model and execution infrastructure.

Alpha is difficult to find, as by definition once it is well-known it decays and seeks to be an uncorrelated source of returns. Instead it gradually becomes a risk factor and thus loses its risk-adjusted profitability.

This book concentrates on three major areas of mathematical modelling–Bayesian Statistics, Time Series Analysis and Machine Learning–that will augment your quantitative trading research process in order to help you discover sources of alpha.

Many of these techniques are in use at some of the largest global asset managers and quantitative hedge funds. In the following chapters these techniques will be described and applied to financial data in order to develop testable systematic trading strategies.

# 1.2 Why Time Series Analysis, Bayesian Statistics and Machine Learning?

In the last few years there has been a significant increase in the availability of software for carrying out statistical analysis at large scales–the so called "big data" era.

Much of this software is completely free, open source, extremely well-tested and straightforward to use. The prevalence of free software coupled to the availability of financial data, as provided by services such as Yahoo Finance, Google Finance, Quandl and DTN IQ Feed, has lead to a sharp increase in individuals deciding to become quant traders.

Unfortunately many of these individuals never get past learning basic "technical analysis". They avoid important topics such as risk management, portfolio construction and algorithmic execution–topics given significant attention in institutional environments. In addition "retail" traders often neglect more effective means of generating alpha, such as can be provided via detailed statistical analysis.

The aim of this book is to provide the "next step" for those who have already begun their quantitative trading career or are looking to try more advanced methods. In particular the book will discuss techniques that are currently in deployment at some of the large quantitative hedge funds and asset management firms.

Our main area of study will be that of rigourous statistical analysis. This may sound like a dry topic, but rest assured that it is not only extremely interesting when applied to real world data, but also provides a solid "mental framework" for how to think about future trading methods and approaches.

Statistical analysis is a huge field of academic interest and only a fraction of the field can be considered within this book. Trying to distill the topics important for quantitative trading is difficult. However three main areas have been chosen for discussion:

- Bayesian Statistics
- Time Series Analysis
- Machine Learning

Each of these three areas is extremely useful for quantitative trading research.

#### 1.2.1 Bayesian Statistics

Bayesian Statistics is an alternative way of thinking about probability. The more traditional "frequentist" approach considers probabilities as the end result of many trials, for instance, the fairness of a coin being flipped many times. Bayesian Statistics takes a different approach and instead considers probability as a measure of belief. That is, opinions are used to create probability distributions from which the fairness of the coin might be based on.

While this may sound highly subjective it is often an extremely effective method in practice. As new data arrives beliefs can be updated in a rational manner using the famous Bayes' Rule. Bayesian Statistics has found uses in many fields, including engineering reliability, searching for lost nuclear submarines and controlling spacecraft orientation. However, it is also extremely applicable to quantitative trading problems.

Bayesian Inference is the application of Bayesian Statistics to making inference and predictions about data. Within this book the main goal will be to study financial asset prices in order to predict future values or understand why they change. The Bayesian framework provides a modern, sophisticated mathematical toolkit with which to carry this out.

Time Series Analysis and Machine Learning make heavy use of Bayesian Inference for the design of some of their algorithms. Hence it is essential that the basics of how Bayesian Statistics is carried out are discussed first.

To carry out Bayesian Inference in this book a "probabilistic programming" tool written in Python will be used, called [PyMC3.](https://github.com/pymc-devs/pymc3)

#### 1.2.2 Time Series Analysis

Time Series Analysis provides a set of "workhorse" techniques for analysing financial time series. Most professional quants will begin their analysis of financial data using basic time series methods. By applying the tools in time series analysis it is possible to make elementary assessments of financial asset behaviour.

The main idea in Time Series Analysis is that of serial correlation. Briefly, in terms of daily trading prices, serial correlation describes how much of today's asset prices are correlated to previous days' prices. Understanding the structure of this correlation helps us to build sophisticated models that can help us interpret the data and predict future values. The concept of asset momentum–and trading strategies derived from it–is based on positive serial correlation of asset returns.

Time Series Analysis can be thought of as a more rigourous approach to understanding the behaviour of financial asset prices than is provided via "technical analysis".

While technical analysis has basic "indicators" for trends, mean reverting behaviour and volatility determination, Time Series Analysis brings with it the full power of statistical inference.

This includes hypothesis testing, goodness-of-fit tests and model selection, all of which serve to help rigourously determine asset behaviour and thus eventually increase profitability of systematic strategies. Trends, seasonality, long-memory effects and volatility clustering can all be understood in much more detail.

To carry out Time Series Analysis in this book the R statistical programming environment, along with its many external libraries, will be utilised.

#### 1.2.3 Machine Learning

Machine Learning is another subset of statistical learning that applies modern statistical models to vast data sets, whether they have a temporal component or not. Machine Learning is part of the broader "data science" and quant ecosystem. In essence it is a fusion of computational methods–mainly optimisation techniques–within a rigourous probabilistic framework. It provides the ability to "learn a model from data".

Machine Learning is generally subdivided into three separate categories: Supervised Learning, Unsupervised Learning and Reinforcement Learning.

Supervised Learning makes use of "training data" to train, or supervise, an algorithm to detect patterns in data. Unsupervised Learning differs in that there is no concept of training (hence the "unsupervised"). Unsupervised algorithms act solely on the data without being penalised or rewarded for correct answers. This makes it a far harder problem. Both of these techniques will be studied at length in this book and applied to quant trading strategies.

Reinforcement Learning has gained significant popularity over the last few years due to the famous results of firms such as Google DeepMind[3], including their work on Atari 2600 videogames[70] and the AlphaGo contest[4]. Unfortunately Reinforcement Learning is a vast area of academic research and as such is outside the scope of the book.

In this book Machine Learning techniques such as Support Vector Machines and Random Forests will be used to find more complicated relationships between differing sets of financial data. If these patterns can be successfully validated then they can be used to infer structure in the data and thus make predictions about future data points. Such tools are highly useful in alpha generation and risk management.

To carry out Machine Learning in this book the Python [Scikit-Learn](http://scikit-learn.org/stable/) and [Pandas](http://pandas.pydata.org/) libraries will be utilised.

# 1.3 How Is The Book Laid Out?

The book is broadly laid out in four sections. The first three are theoretical in nature and teach the basics of Bayesian Statistics, Time Series Analysis and Machine Learning, with many references presented for further research. The fourth section applies all of the previous theory to the backtesting of quantitative trading strategies using the [QSTrader](https://github.com/mhallsmoore/qstrader) open-source backtesting engine.

The book begins with a discussion on the Bayesian philosophy of statistics. The binomial model is presented as a simple example with which to apply Bayesian concepts such as conjugate priors and posterior sampling via Markov Chain Monte Carlo.

It then explores Bayesian statistics as related to quantitative finance, discussing a Bayesian approach to stochastic volatility. Such a model is eligible for use within a regime detection mechanism in a risk management setting.

In Time Series Analysis the discussion begins with the concept of serial correlation, applying it to simple models such as White Noise and the Random Walk. From these two models more sophisticated linear approaches can be built up to explain serial correlation, culminating in the Autoregressive Integrated Moving Average (ARIMA) family of models.

The book then considers volatility clustering, or conditional heteroskedasticity, motivating the famous Generalised Autoregressive Conditional Heteroskedastic (GARCH) family of models.

Subsequent to ARIMA and GARCH the book introduces the concept of cointegration (used heavily in pairs trading) and introduces state space models including Hidden Markov Models and Kalman Filters.

These time series methods are all applied to current financial data as they are introduced. Their inferential and predictive performance is also assessed.

In the Machine Learning section a rigourous definition of supervised and unsupervised learning is presented utilising the notation and methodology of statistical machine learning. The humble linear regression will be presented in a probabilistic fashion, which allows introduction of machine learning ideas in a familiar setting.

The book then introduces the more advanced non-linear methods such as Decision Trees, Support Vector Machines and Random Forests. It then discusses unsupervised techniques such as K-Means Clustering.

Many of the above mentioned techniques are applied to asset price prediction, natural language processing and sentiment analysis. Subsequently full code is provided for systematic strategy backtesting implementations within QSTrader.

The book provides plenty of references on where to head next. There are many potential academic topics of interest to pursue subsequent to this book, including Non-Linear Time Series Methods, Bayesian Nonparametrics and Deep Learning using Neural Networks. Unfortunately, these exciting methods will need to wait for an additional book to be given the proper treatment they deserve!

# 1.4 Required Technical Background

Advanced Algorithmic Trading is a definite step up in complexity from the previous QuantStart book Successful Algorithmic Trading. Unfortunately it is difficult to carry out any statistical inference without utilising some mathematics and programming.

#### 1.4.1 Mathematics

To get the most out of this book it will be necessary to have taken introductory undergraduate classes in Mathematical Foundations, Calculus, Linear Algebra and Probability, which are often taught in university degrees of Mathematics, Physics, Engineering, Economics, Computer Science or similar.

Thankfully it is unnecessary to have completed a university education in order to make good use of this book. There are plenty of fantastic resources for learning these topics on the internet. Some useful suggestions include:

- Khan Academy https://www.khanacademy.org
- MIT Open Courseware http://ocw.mit.edu/index.htm
- Coursera https://www.coursera.org
- Udemy https://www.udemy.com

However, it should be well noted that Bayesian Statistics, Time Series Analysis and Machine Learning are quantitative subjects. There is no avoiding the fact that some intermediate level mathematics will be needed to quantify our ideas.

The following courses are extremely useful for getting up to speed with the required mathematics:

- Linear Algebra by Gilbert Strang http://ocw.mit.edu/courses/mathematics/18-06sclinear-algebra-fall-2011/index.htm
- Single Variable Calculus by David Jerison http://ocw.mit.edu/courses/mathematics/18- 01-single-variable-calculus-fall-2006
- Multivariable Calculus by Denis Auroux http://ocw.mit.edu/courses/mathematics/18- 02-multivariable-calculus-fall-2007
- Probability by Santosh Venkatesh https://www.coursera.org/course/probability

#### 1.4.2 Programming

Since this book is fundamentally about programming quantitative trading strategies, it will be necessary to have some exposure to programming languages.

While it is not necessary to be an expert programmer or software developer, it is helpful to have used a language similar to C++, C#, Java, Python, R or MatLab.

Many will have likely have programmed in VB Script or VB.NET through Excel. However, taking an introductory Python or R programming course is strongly recommended. There are many such courses available online:

- Programming for Everybody https://www.coursera.org/learn/python
- R Programming https://www.coursera.org/course/rprog

# 1.5 How Does This Book Differ From "Successful Algorithmic Trading"?

Successful Algorithmic Trading was written primarily to help readers think in rigourous quantitative terms about their trading. It introduces the concepts of hypothesis testing and backtesting trading strategies. It also outlined the available software that can be used to build backtesting systems.

It discusses the means of storing financial data, measuring quantitative strategy performance, how to assess risk in quantitative strategies and how to optimise strategy performance. Finally, it provides a template event-driven backtesting engine on which to base further, more sophisticated, trading systems.

It is not a book that provides many trading strategies. The emphasis is primarily on how to think in a quantitative fashion and how to get started.

Advanced Algorithmic Trading has a different focus. In this book the main topics are Time Series Analysis, Machine Learning and Bayesian Statistics as applied to rigourous quantitative trading strategies.

Hence this book is largely theoretical for the first three sections and then highly practical for the fourth, which discusses the implementation of actual trading strategies in a sophisticated, but freely-available backtesting engine.

More strategies have been added to this book than in the previous version. However, the main goal is to motivate continued research into strategy development and to provide a framework for achieving improvement, rather than presenting specific "technical analysis"-style prescriptions.

This book is not a book that covers extensions of the event-driven backtester presented in Successful Algorithmic Trading, nor does it dwell on software-specific testing methodology or how to build an institutional-grade infrastructure system. It is primarily about mathematical modelling and how this can be applied to quantitative trading strategy development.

# 1.6 Software Installation

Over the last few years it has become significantly easier to get both Python and R environments installed on Windows, Mac OS X and Linux. This section will describe how to easily install Python and R in a platform-independent manner.

#### 1.6.1 Installing Python

In order to follow the code for the Bayesian Statistics and Machine Learning chapters (as well as one chapter in the Time Series Analysis section) it is necessary to install a Python environment.

The most straightforward way to achieve this is to download and install the free Anaconda distribution from Continuum Analytics at <https://www.continuum.io/downloads>.

The installation instructions are provided at the link above and come with nearly all of the necessary libraries needed to get started with the code in this book. Other libraries can be easily installed using the "pip" command-line tool.

Anaconda is bundled with the Spyder Integrated Development Environment (IDE), which provides a Python syntax-highlighting text editor, an IPython console for interactive workflow/visualisation and an object/variable explorer for debugging.

All of the code in the Python sections of this book have been designed to be run using Anaconda/Spyder for Python 2.7.x, 3.4.x and 3.5.x. However, many seasoned developers prefer to work outside of the Anaconda environment, e.g. by using [virtualenv.](https://virtualenv.pypa.io/en/stable/) The code in this book will also happily work in such virtual environments once the necessary libraries have been installed.

If there are any questions about Python installation or the code in this book then please email [support@quantstart.com.](mailto:support@quantstart.com)

#### 1.6.2 Installing R

R is a little bit trickier to install than Anaconda but not hugely so. RStudio is an IDE for R that provides a similar interface to R as Spyder does for Python. RStudio has an R syntax-highlighting console and visualisation tools all in the same document interface.

RStudio requires the underlying R software itself. R must first be downloaded prior to usage of RStudio. This can be done for Windows, Mac OS X or Linux from the following link: <https://cran.rstudio.com/>

It is necessary to select the pre-compiled binary from the top of the page that fits the particular operating system being utilised.

Once R is successfully installed the next step is to download RStudio: [https://www.rstudio.](https://www.rstudio.com/products/rstudio/download/) [com/products/rstudio/download/](https://www.rstudio.com/products/rstudio/download/)

Once again the version will need to be selected for the particular platform and operating system type (32/64-bit) in use. It is necessary to select one of the links under "Installers for Supported Platforms".

All of the code snippets in the R sections of this book have been designed to run on "vanilla" R and/or R Studio.

If there are any questions about R installation or the code in this book then please email [support@quantstart.com.](mailto:support@quantstart.com)

## 1.7 QSTrader Backtesting Simulation Software

There is now a vast array of freely available tools for carrying out quantitative trading strategy backtests. New software (both open source and proprietary) appears every month.

In this book extensive use will be made of QSTrader–QuantStart's own open-source backtesting engine. The project has a GitHub page here: [https://github.com/mhallsmoore/](https://github.com/mhallsmoore/qstrader) [qstrader](https://github.com/mhallsmoore/qstrader).

QSTrader's "philosophy" is to be highly modular with first-class status given to risk management, position-sizing, portfolio construction and execution. Brokerage fees and bid/ask spread (assuming available data) are turned on by default in all backtests. This provides a more realistic assessment of how a strategy is likely to perform under real trading conditions.

QSTrader is currently under active development by a team of dedicated volunteers, including myself. The software remains in "alpha" mode, which means it is not ready for live-trading deployment yet. However it is sufficiently mature to allow comprehensive backtesting simulation.

The majority of the quantitative trading strategies in this book have been implemented using QSTrader, with full code provided within each respective chapter.

More information about the software can be found in the chapter Introduction To QSTrader in the final section of this book.

#### 1.7.1 Alternatives

There are many alternative backtesting environments available, some of which are listed below:

- Quantopian A well-regarded web-based backtesting and trading engine for equities markets: <https://www.quantopian.com>
- Zipline An open source backtesting library that powers the Quantopian web-based backtester: <https://github.com/quantopian/zipline>
- PySystemTrade Rob Carver's futures backtesting system: [https://github.com/robcarv](https://github.com/robcarver17/pysystemtrade)er17/ [pysystemtrade](https://github.com/robcarver17/pysystemtrade)

## 1.8 Where to Get Help

The best place to look for help is the articles list on [QuantStart.com](http://www.quantstart.com) found at [QuantStart.com/articles.](http://www.quantstart.com/articles) Over 200 articles about quantitative finance and algorithmic trading have been written to date on the site.

If you have a question that you feel is not answered by one of the current articles an alternative is to contact QuantStart Support at [support@quantstart.com.](mailto:support@quantstart.com)
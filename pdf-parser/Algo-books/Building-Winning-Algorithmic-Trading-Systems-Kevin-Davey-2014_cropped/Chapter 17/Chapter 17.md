# Documenting the Process

s you can imagine, keeping track of all the strategies you create and run through  $\boldsymbol{\Lambda}$  this development process can quickly become a nightmare. Proper documentation is the key to successfully managing this effort. Currently, I use an Excel spreadsheet to manage my strategies. This is available on the book resource web site (www.wiley.com/ go/algotradingsystems) for you to download and use, and is also shown in Figures 17.1 and 17.2. I have set it up to identify the items I feel are the most important. Of course, as you progress in system development, you will likely have different items you want to track. In that case, simply edit the spreadsheet to fit your own needs.

The items I track with the spreadsheet will be discussed in this chapter.

#### **Trading Goals**

I list all my goals for profit, drawdown, rate of return, number of trades, and so on. I find it much more difficult to accept systems that do not meet my goals when the goals are clearly written at the start!

#### Trading Idea

Here I list all the particulars of the strategy I am testing.

Strategy name. Sounds simple, but having a unique name for every strategy helps you keep track of things. I use a standard naming convention, which allows me to easily find it in my trading software's list of strategies.

KJD2013-10 BrkOut A

| System Development Process Checklist |          |                 |  |  |
|--------------------------------------|----------|-----------------|--|--|
| Trading Goals                        | Criteria | Completion Date |  |  |
| List All Goals                       |          |                 |  |  |
|                                      |          |                 |  |  |
|                                      |          |                 |  |  |
| Trading Idea                         |          | Completion Date |  |  |
| Strategy Name                        |          |                 |  |  |
| Strategy—Gen Description             |          |                 |  |  |
| Edge                                 |          |                 |  |  |
| Markets to Test                      |          |                 |  |  |
| Bar Size                             |          |                 |  |  |
| Historical Test Period               |          |                 |  |  |
| Market Data Streams                  |          |                 |  |  |
| Market Data Customization            |          |                 |  |  |
|                                      |          |                 |  |  |
| Entry Rules                          |          |                 |  |  |
|                                      |          |                 |  |  |
|                                      |          |                 |  |  |
| Exit Rules                           |          |                 |  |  |
|                                      |          |                 |  |  |
|                                      |          |                 |  |  |
|                                      |          |                 |  |  |
| Limited Testing                      | Results  | Completion Date |  |  |
| Test Period                          |          |                 |  |  |
| Entry Testing                        |          |                 |  |  |
| Fixed Stop, Fixed Target             |          |                 |  |  |
| Fixed Bar                            |          |                 |  |  |
| Exit Testing                         |          |                 |  |  |
| Similar Approach Entry               |          |                 |  |  |
| Core System Test                     |          |                 |  |  |
| Monkey Testing                       |          |                 |  |  |
| Random Entry                         |          |                 |  |  |
| Random Exit                          |          |                 |  |  |
| Random Entry & Exit                  |          |                 |  |  |
|                                      |          |                 |  |  |
| Limited Testing—Overall              | Pass     | Fail            |  |  |

**FIGURE 17.1** Documenting the Development Process

|                                          | System Development Process Checklist |      |                 |
|------------------------------------------|--------------------------------------|------|-----------------|
| Walk-forward Testing                     | Results                              |      | Completion Date |
| In Period                                |                                      |      |                 |
| Out Period                               |                                      |      |                 |
| Fitness Function                         |                                      |      |                 |
| Anchored/Unanchored                      |                                      |      |                 |
| Optimum In/Out (if applicable)           |                                      |      |                 |
| Walk-forward Historical Strategy Created |                                      |      |                 |
| Walk-forward Testing—Overall             |                                      | Pass | Fail            |
| Monte Carlo Analysis                     | Results                              |      | Completion Date |
|                                          |                                      |      |                 |
| Start Equity<br>Quit Equity              |                                      |      |                 |
|                                          |                                      |      |                 |
| Number Trades, 1 Year                    |                                      |      |                 |
| Return/DD Ratio                          |                                      |      |                 |
| Monte Carlo—Overall                      |                                      | Pass | Fail            |
|                                          |                                      |      |                 |
| Incubation                               | Results                              |      | Completion Date |
| Meets Goals                              |                                      | Pass | Fail            |
| Diversification                          |                                      |      |                 |
| Meets Goals                              |                                      | Pass | Fail            |
| Position Sizing                          |                                      |      |                 |
| Meets Goals                              |                                      | Pass | Fail            |
| Final Notes                              |                                      |      | Completion Date |
|                                          |                                      |      |                 |

 **FIGURE 17.2** Documenting the Development Process (cont'd)

where:

- KJD = My initials—in a list of 1,000 strategies, you want to easily fi nd the ones you wrote.
- 2013‐10 = Year, followed by two‐digit month. I created this strategy in October 2013.
- BrkOut = A simple description of the strategy. This example would be a breakout strategy.
  - A = Version of strategy. If I later change or add rules, the next version would be "B." This serves a couple of purposes. First, it helps you keep track of how the strategy changed over time. Second, it reminds you how many changes you made to the strategy. If you consistently fi nd yourself testing up to version "M," for example, you are probably spending too much time revising your strategy. Remember, the risk of overfi tting goes up with each version.

 As part of this naming, I will also add a "W" to the end if the walk‐forward version has a diff erent code than the baseline version, and I will use "H" at the end to signify a historical walk‐forward version of the strategy.

*Strategy—general description.* In simple words, I will describe my strategy. *Edge.* What do I think my edge is? Enter it here. This is a good warning sign—if

you do not have a clue what your edge is, you probably do not have one!

*Markets to test.* List the market or markets you plan to examine.

*Bar size.* Enter the type of bar you are testing with.

*Historical test period.* List the start and end dates for your analysis.

*Market data streams.* List the data identifi er you are using. For example, if I wanted to test the continuous gold contract, in TradeStation I would use "@GC."

*Market data customization.* If you use any special session times or anything else unique, enter it here.

*Entry rules.* Describe your entry rules. You can use plain English, pseudo code, or actual code. The idea is to archive the entry method for later reference.

*Exit rules.* Describe your exit rules in the same manner as your entry rules.

## ■ **Limited Testing**

Here I list all the particulars of the limited testing phase:

- *Test period.* The one or two‐year sample of historical data that I am using to perform the limited testing.
- *Entry testing.* Here, I will record the general results (e.g., excellent, good, poor) for the entry testing (fi xed stop, fi xed target, and/or fi xed bar).

TING

THE PROCESS

*Exit testing.* Here, I will record the general results (e.g., excellent, good, poor) for the exit testing (similar‐approach entry).

*Core system testing.* General results of the whole system.

*Monkey testing.* If I perform any random "monkey" testing, I will record the results here. *Limited testing—overall.* Based on all the limited tests run, does the system pass or fail?

## ■ **Walk-Forward Testing**

 Assuming the strategy passes the limited testing phase, I now move on to the walk‐ forward testing step.

*In period.* The number of trading days in the in‐sample periods.

*Out period.* The number of trading days in the out‐sample periods.

*Fitness function.* List the fi tness function used.

- *Anchored/Unanchored.* Identify whether you are using anchored testing or unanchored testing.
- *Optimum in/out.* If you optimize the in/out periods, identify that here, and also provide information on the true out‐of‐sample date range.
- *Walk‐forward historical strategy created.* If you create a strategy version specifi cally with walk‐forward history, identify it here. I signify this by putting the letter "H" on the end of the strategy.
- *Walk‐forward testing—overall.* Based on all the walk‐forward testing, does the system pass or fail?

## ■ **Monte Carlo Testing**

 Assuming the strategy passes the walk‐forward testing phase, I now move on to the Monte Carlo testing step:

*Start equity.* Enter the starting equity you are using for the simulation.

*Quit equity.* Enter the equity level below which you will quit trading the strategy.

*Number trades, 1 year.* Number of trades in one year of trading.

*Return/DD ratio.* Enter this result from the Monte Carlo simulation.

*Monte Carlo testing—overall.* Based on all the Monte Carlo testing, does the system pass or fail?

## ■ **Incubation Testing**

 Assuming the strategy passes the Monte Carlo phase, I now move on to the incubation testing step:

*Meets goals.* Did the strategy pass or fail incubation?

#### ■ **Diversification Check**

 Applicable only to strategies that you plan to trade with other strategies. Was the current strategy developed with diversifi cation in mind?

*Meets goals.* Did the strategy pass or fail diversifi cation?

## ■ **Position-Sizing Check**

 Since I usually test a strategy with "one trade per contract" rules, this is an easy check. If, however, I used a particular position sizing during development, it should not be the outcome of optimization and should be identifi ed here (especially if it will be traded with other systems).

*Meets goals.* Was the strategy developed using one contract per trade, or some other position-sizing technique that did *not* involve optimization?

#### ■ **Final Notes**

 After testing and development is completed, enter any information you feel is appropriate. For example, you could list the date you started trading. If the strategy does not pass but you like the entry or exit rules, you could always identify that fact here. I have had strategies that failed, but I still liked a particular aspect of it. With the notes at the end, you can always refer to it later and easily remember, "Oh yes, I wanted to test this entry with soybeans, due to its high volatility."

#### ■ **One Final List**

 The individual sheets provide an excellent way to manage each strategy. In addition, I also keep a list of entry and exit ideas. These might not be fully formed strategies, but they are ideas I can take and later use in a strategy. For example, if I see an intriguing entry idea in a book or trading magazine, and I cannot immediately test it, I'll just add it to my entry list. This list serves two purposes. First, it functions as an idea manager, saving any idea you have for future testing. Second, having this list means you will never run out of ideas to test. Trust me, the list will grow far faster than you can test!
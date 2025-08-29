# **Systematic Trading**

This book is about systematic trading. That is, the use of computers to model, test and implement mathematical rules for how to trade. This way of working is by no means a shortcut, as it may unfortunately appear to some newcomers in the field. Building solid mathematical models with predictive value going forward can be a daunting task. It takes hard work and research. But on the other hand, this way of working allows you to test what you believe about the market, and even more importantly to test how your ideas about trading would have performed in the past.

# **Trading Approach Validation**

A good reason to enter the space of systematic trading and quantitative modelling is to validate your ideas, or others' ideas for that matter. You have probably read books or websites telling you to buy when some indicator hits some value, on lines crossing or something similar. Perhaps that's a valid approach, and perhaps not. You could find out by taking a bet on these rules, or you could formulate them into a trading model and test them.

When you first starting testing ideas in this way, it can be an eye opener. The first thing you will likely realize is that most such advice represent only a small part of the puzzle, or that they can be difficult or even impossible to turn into firm trading rules.

Whether or not you want to go the full mile and implement completely systematic trading rules, the ability to test and validate ideas is very valuable. Many market participants rely on old platitudes and so called common knowledge about how the markets work, without ever bothering to validate these ideas.

Take something as common as the saying "Sell in May and go

away", which refers to the common belief that markets perform best during the winter. It does not take any deeper understanding of systematic trading to find out if there is a value in such an approach.

Other wisdoms you may have heard would include how you should hold 70% stocks and 30% bonds in the long run, how you should never hold stocks in October or similar. After reading this book, you should have a sufficient toolkit at your disposal to try out any such ideas you may hear.

Having this ability to test ideas also tends to aid critical thinking. Once you understand what is required to test an idea, the logical parts that make up a complete trading model and the details that you need to sort out, you will quickly see if a proposed method of trading is possible to model or not. This will help you understand if what is being suggested is a complete method, or just a small part of it.

Once you start thinking in this manner and look for ways to convert someone's text into trading rules, you will start to apply more critical thinking to claims surrounding various approaches to the markets. Many seemingly mathematical approaches to the market are not in any way quantifiable, once you start trying to construct a model around them. Try to implement Fibonacci or Elliot Wave ideas into a testable approach, and you will find yourself in a bottomless logical pit with a china teapot floating in the middle.

### **Scientific Approach**

Systematic trading aims for a scientific approach. I would say aims for, as a most systematic traders take shortcuts which an academic researcher would take issue with. As practitioners, systematic traders are not in the business of seeking truth, but rather in the business of making money. At times, this can mean that some scientific principles may be cut short, but it's important to keep the principles intact.

In science, hypotheses are formulated and tests for them are devised. The default assumption is always that any given hypothesis you may have is false, and if the tests attempt to demonstrate this. If the tests fail to show validity of our hypothesis, it's rejected.

This is the key difference between gut feeling trading and a somewhat scientific approach. The willingness to throw away your ideas and reevaluate your beliefs if they can't demonstrate real world results.

In order to do this, you first need for formulate every aspect of your hypothesis into firm rules. This in itself is a valuable skill to have, to be able to break down your ideas into logical components.

The next step is to construct a test for these rules. For that, you need a backtesting environment capable of testing your rules. You also need relevant data, and to make sure that this data is correct, clean and properly suitable for testing your ideas. Depending on your choice of asset class, time frame and complication, this might be relatively simple and cheap, or it may get a little tricky.

When constructing and executing your tests, the so called backtests, you should always have a skeptical mindset. Your default way of thinking should be to find ways to reject the rules. To show that they fail to add value and should be discarded. That you need to start over.

The other way of working, to find ways to show the value of your rules, is easy. If you purposely try to construct tests to show how clever your rules are, your own confirmation bias will push you to accept ideas which are unlikely to have predictive value going forward.

Backtesting is the process of applying a set of trading rules on historical price series, to investigate what would theoretically have happened if you had traded them in the past. This book will go into details on how you can use Python to set up such a backtesting environment and how to write code to test historical performance.

This book will not however go into any level of depth on applying scientific principles to the various aspects of constructing trading models. That's a vast subject which would require a book all by itself. Luckily, a good such book already exists (Carver, Systematic Trading, 2015).

### **Consistent Methodology**

Trading can often be emotionally exhausting. Discretionary trading requires a constant focus and can be greatly dependent on your mental and emotional state on any given day. External factors can easily affect your trading performance. If you are having relationship issues, if a loved one has a health situation or even if your favorite football team just lost an important game, you may find that your temper or lack of focus can greatly impact your performance.

It can also be factors directly related to your trading that clouds your mind. If you just took a big loss for instance, you may find yourself trying to make the market give you your money back, or to prove yourself and your abilities by trading more aggressively. Depending on your personality, a loss might also make you gun shy and have you trade more defensively, or not at all.

During times of market distress, this phenomenon impacts most of us. When there are big headlines on the news ticker, making prices crash and showing wild intraday swings, most people lose money. And most people spend their days being upset, scared or with high adrenaline. That's not a great state of mind for most people to make important decisions.

While some personality types thrive in the high pressure environments that market crises cause, most people make very poor decisions in such situations.

This is where systematic trading really shines. It will remove this emotional aspect of trading, by providing clear cut rules. If you

have done your job well and constructed solid trading rules, you simply let them do their thing.

When the market crashes and everyone around you is in panic, you can calmly continue to follow the rules, in the knowledge that they have been tested for this type of market climate and you know what to expect. There is no need to make rash decisions under fire. Just follow your rules.

Even during more normal market circumstances, you can achieve a more consistent and more predictable performance with a rule bound, systematic approach. Whether you can achieve higher returns or not is of course a wholly unrelated question.

### **Time Management**

Most systematic traders don't have a need to sit by the screens and watch the markets all day. That does not necessarily mean that they can spend all day at the beach, but they are generally freer to plan their day.

Staring at tick charts all day can be quite addictive. If you trade on a shorter time frame and make your decisions based on what you see in the market, you probably do need to sit in front of your Bloomberg or Reuters all day. Given the global market trading and exchange opening hours, this might mean that you will never really be off duty.

Many systematic traders work hard and long hours, but you do have a much greater degree of flexibility. If your purpose is to trade your own personal account, you could develop rules that trade daily, weekly or even monthly. This would allow you to trade as a hobby and keep your regular day job. You can develop rules that fit your schedule.

Most systematic traders execute their trades manually, in

particular in the hobby segment. That is, even if the rules are exact and all trading signals are followed, the task of entering the trades is still yours. There is really nothing wrong with working in this manner, as long as you can keep yourself from overriding and trying to outsmart your tested rules.

You might for instance have a trading model which trades at the opening of the exchange every day. Your trading model generates daily lists of trades for the day, and you enter them in the market before work each day. That's a common approach to longer term trading models for hobby traders.

As you get more advanced, you might even automate your trades, and have your code send the orders straight to the broker. This can be very convenient and allow you to trade faster, but it also comes with the added danger of bugs in your code. A decimal point wrong, and you end up with ten times exposure, which can make or break your day real fast. Don't go the automated route before you really know what you are doing.

An important point to understand in this context is that even if your model is automated, it should never be unsupervised. It's a seductive idea to just train an algo to trade for you and go on vacation, and then to return to find a few more millions on your account.

Leaving a trading model to its own devices, letting it trade unsupervised without someone constantly watching is not a great idea. Computers are only as smart as the person programming it, and usually not even that smart. Constantly monitor automatic trading models.
# **Backtesting Trading Strategies**

In this chapter, we will take a look at how backtesting in Python works. As we saw in chapter 4, it's extremely easy to perform simple ad-hoc tests. But that's not what we are going for in this book. We are going to do things properly.

When I started writing my first book, I decided to make sure that readers can replicate and verify everything I write. Most companies in my business spend a lot of money on software, data and quants. I did not want to write books that only firms with large budgets could make use of. If I make claims that can't be verified, they are of little use. I wouldn't trust a book that does not show all the details and allow for replication, and it would be unreasonable for me to expect anyone else to do so.

The first thing I did was to research cheap tools that are good enough for the purpose. I did not want to tell people to go out and spend thousands of dollars a month just on market data. If you have the budget for that, fine. Knock yourself out. But it's a fair assumption that most of my readers don't.

What I ended up doing was to construct a budget quant environment and use that and only that for the purpose of my books. For my first book, *Following the Trend* (Clenow, Following the Trend, 2013), I used software that cost around 500 dollars and market data that cost a hundred or so per month. That's dirt cheap in this business. But I was surprised that quality tools can be found on the cheap with a little research.

That being said, most backtesting platforms used by retail traders are really bad. No, I won't single anyone in particular out, but I dare to say that an overwhelming majority of what non-professionals use is horrible.

The environment I ended up using for my first book was based

on **RightEdge** . It's a solid piece of software that I still use and recommend. Based on C#, it's fast and reliable, but requires quite a bit of programming knowledge to get started. C# is a great language to work in, once you get to know it. Easier than C++, it's a fast and robust language that can do just about anything you need. It's hard to proclaim any software *The Best* , and the choice often comes down to purpose and preference. It's easier to discard the bad ones until only a few good-enough remain.

I still like **RightEdge** , even though it's barely updated in a decade, and I kept using it heavily over the years and spent much time modifying it to my needs. I relied on that same platform for the research in my second book, Stocks on the Move.

For *Following the Trend* , I used futures data from **CSI Data** , and in *Stocks on the Move* , I used data from **QuantQuote** and **Norgate Data** .

I'm sure some are wondering why I mention this, and how much money these companies are paying for it. Well, once again not getting paid for mentioning them. I simply want to be up front with what I used. Are these firms the best? I don't know, but it seems unlikely that I happened to find the very best, whatever that might mean in this context. I found these solutions to be good enough for the purpose. They also fit my requirement of low cost solutions, to allow readers to replicate the work.

I ended up needing a budget of a couple of thousand a year for the tools needed to replicate the research in those books. That seems like a good deal to me.

In Python world, you will find that practically all software is free. It won't be as polished, or even as finished as most of us will be used to. Most Python software requires you to do a lot of work in installing, adapting and configuring before you can really use them. But free is free.

Data however tends not to be free. There are some free data

sources out there, but unfortunately the trend is that they all go premium. One by one, they either cut or limit access, and offer a pay service.

You can find some basic stock data to play with, but if you want proper data that you can rely on, unfortunately free does not seem to be a robust option.

For this book, I used two data sources. For stocks, I relied on **Norgate Data** and for futures I have used **CSI Data** . Both are low cost services, with good enough quality for most daily algo modeling and they are well priced for retail traders.

#### **Python Backtesting Engines**

The first thing that you need to understand is that there is no single way to run financial backtests in Python. Just like there is no single way to do it in C++, or other languages. A programming language is just that; a language. To use it for backtesting, we either need to construct an engine, which deals with all the details for us, or install and use an engine that someone else already made.

After all, that's what happens if you buy an off the shelf software package, such as **AmiBroker** , **RightEdge** , **TradeStation** , **NinjaTrader** , **MultiCharts** etc. The main difference in the Python world is that you are generally expected to do more work yourself. You won't get as finished, polished, visual software.

On the other hand, the flexibility and potential is much greater using Python than with most of these kind of off-the-shelf packages. Once you get into Python, you will see the benefits of being able to do just about anything with it. And again, it's free.

Python backtesting is still in its early days. It has not yet reached mass appeal, and that can sometimes be painfully clear in terms of usability and documentation. So far, it's mostly data

scientists, quant professionals and early adopters using it. But what we are seeing is that the user base is growing and, more importantly, broadening. As this continues, usability and documentation are likely to improve.

Don't expect to download an installation file, get a graphical installation program which takes care of every detail, installing a shiny Windows application where you point and click, change a few settings, run a backtest and get some colorful analysis page showing you all the details. That's not the Python way. At least not yet.

On the other hand, Python backtesting engines tend to be not only totally free, but also open source. Yes, you can get the software without paying a penny, and you will get the full source code so that you can make any modifications that you see fit.

When you start looking for a backtesting engine for Python, you will find that there are many to choose from. It may seem overwhelming even. As you dig deeper, you will find that they are all quite different, often with their own unique strengths and weaknesses.

When I first started digging into these details, I asked friends in the financial industry who had been working with Python backtesting much longer than I had. More often than not, it was suggested that I simply build my own engine.

I can see how that makes sense for some. But I'm not looking to reinvent the wheel here. When I need to use a spreadsheet application, I simply open Excel. I don't start over, building my own spread sheet application, even though I don't necessarily agree with all the design choices that Microsoft made.

I prefer to use something that's already built. Preferably something that I can then modify, changing things that I don't like, adding things that I see as missing. But still using the core functionality of an existing solution.

The question is then which of the many available Python

backtesters to use. In this book, I'm only going to use one. I don't want to go over each and every possible Python backtester, showing code examples from all of them and leave everyone utterly confused.

Instead, I will pick a single backtesting engine and use it for all examples in this book. That way, you have a fighting chance to replicate everything from this book on your local computer, and build upon that to make your very own backtesting environment.

# **Zipline and Quantopian**

The backtesting engine that I will use for this book is **Zipline** , developed by Quantopian. The **Zipline** package is probably the most mature of all the currently available choices. It has a richer functionality and it scales very well to large amounts of data. The reason for this requires a brief background on the company that built it.

Quantopian is a Boston based tech and asset management firm which among other things runs a website of the same name. On that website, you'll find a totally free backtesting environment, where you can run advanced backtests on minute level data for American stocks and futures. It's all hosted, running on their servers and provides you with rich functionality and minute level data, all totally free.

At the core, Quantopian is an investment firm, albeit a little different type of investment firm. They are aiming to find untapped talent among the users who develop trading strategies on their website. If you have built something that you think is really valuable, you can submit it to their competition. If you are selected, they will allocate money to your strategy and pay you based on performance.

It's a novel concept, and the jury is still out on this business model. Some readers may have noticed that I have appeared quite a few times as a speaker at Quantopian's conferences, QuantCon, around the world. So clearly you are now wondering just how much

they are paying me to plug their company here.

I hate to disappoint but I'm not getting paid, for speaking at their conferences or for mentioning them here. Their conferences are some of the best in the field, and I show up and speak there because I enjoy it. Regarding getting paid for putting them in the book, I doubt that this publicity is worth enough to bribe an author. Don't get me wrong of course. I do work in the hedge fund field, and claiming to be morally outraged by the idea would be silly. But I sincerely question the economic value of plugging a substandard solution for a few bucks extra. Especially a free, open source solution.

If however you have a product you would want to bribe me to plug in an upcoming book, you should know that I'm partial to gold bars and Patek watches.

The Quantopian website uses the backtesting engine **Zipline** , developed and maintained by the same company. **Zipline** can also be downloaded and installed locally.

There are some important differences between using the Quantopian website and installing **Zipline** locally. Clearly, using the website is far easier. Everything is installed and set up for you. Even more importantly, you get free access to minute level data for stocks and futures. You get a nice graphical environment to work in, where you can point and click to get things done, as most people would expect these days.

Most of the trading strategies and code in this book should work just fine on the Quantopian website. But it seems like a bit of cheating, if I write a whole book around a website. In the long run, and if you are really serious about quantitative modelling and systematic trading, you probably need a robust, local environment.

Most of the knowledge from this book can be used on the Quantopian site and for those looking to monetize their trading hobby at low risk, you may want to look closer at what they have to offer.

But going forward in this book, I will use the **Zipline** library as a teaching tool, installed locally on your own computer. Once you feel confident enough to go on your own, feel free to try other backtesting libraries and discover differences and similarities.

Having a local setup is naturally a little bit more complex. It also does not come with the aforementioned minute level free data, like the Quantopian website does. They obviously can't just give you that data to use on your local machine. Their licensing agreements with their data providers forces them to ensure that all that data stays on their server.

A result of this is that everything you do on their website needs to stay on their website. They don't allow for saving and downloading equity curves from a trading strategy for example, among other things. If they did, then someone would quickly figure out that you can use that to siphon data out.

For a local setup, we therefore have to improvise a bit on the data side. That's actually the most complex task we have to solve. The easy solution, though hardly the best, is to use free data from a source like Quandl. Such functionality is built into the Zipline package and you can be up and running with that in minutes.

But naturally, a free internet data source is not suitable for proper backtesting. We will use Quandl data for some basic models and testing first, and later in this book we will look closer at proper data and how to hook it up.

#### **Pros and Cons**

Setting up a proper simulation environment based on Zipline without a guide can be quite painful. It may require a bit of work to get all the pieces in place, get the right libraries installed, setting up your own data source and such. I will do my best to guide you through these parts here in this book. It could of course be argued that this

issue is not necessarily a Zipline issue, but rather a larger Python issue.

The Python user base is expanding, but most code and documentation are aimed at data scientists with a strong programming background. Generally speaking, documentation in the Python community is poor. But this is likely to change as more and more people join this field.

The Zipline documentation is no exception. As far as Python documentation goes, it's not bad. But compared to what you might be used to, it's quite lackluster.

Connecting your own data source to Zipline is not entirely trivial. The documentation is near non-existing and it can be a little frustrating to get everything working. Again, this is something that I hope to help you with in this book, and you will find full source code and samples in later chapters.

But one of the most severe downsides with Zipline is that it's only aware of a single world currency. That is, it's unaware that securities may be denominated in multiple currencies. If you only trade American stocks, that shouldn't matter. But if you trade international stocks, or global futures markets, that's a bit of a problem.

There are many great things with Zipline as well. A key point here is that, as opposed to alternative backtesting libraries, this one has a paid staff of full time developers working on it. That certainly helps drive improvements and bug fixes, and this is why Zipline has grown to such a rich set of functionality.

Compared to most current alternatives, Zipline can do more realistic simulations, handle much larger amounts of data and it's really quite fast. It also has a fairly large online community of users, and that means that it's easier to find answers to questions when you get stuck.

Zipline works with both equities and futures, and it has some very clever features in both those areas that we will look closer at later on.

When writing a book like this, there is always a risk that something important changes after you go to print. Depending on when you read this, perhaps there is some other backtesting engine which has surpassed Zipline or perhaps something major changed with Zipline. To mitigate this risk, I will try to keep everything in this book general enough that you should be able to figure out how to apply it on a different environment as well, with as few modifications as possible.

The important point here is learning methodology. Not the exact interfaces for a specific backtesting engine.

### **Installing Zipline**

Remember that Zipline is just another Python library. It's not a stand-alone application, where you download some exe file and get a graphical installation program guiding you through the process. That's not how Python generally works.

If you are new to Python before this book, it might take you a little while to get used to how things are done here. Bear with me, and I will walk you through a typical Zipline installation process.

While there may be new versions of Zipline released by the time you read this, all sample code in this book assumes that you are using Zipline version 1.3. As of writing, that's the most up to date version.

First off, Zipline is designed to work either on Python 2.7 or Python 3.5. As of writing this, the most current version of Python is 3.7, and as of this date Zipline does not install on that version. Remember that in chapter 4 we discussed installing Python, and how

you should install version 3.7. That's likely what you are now running by default on your computer. But fear not. There is a relatively simple way around this.

The solution is in Python's ability to have multiple **environments** on a single computer. Think of an environment as a virtual computer, running on your actual computer. You can set up as many environments as you like, and they are completely independent of each other in every regard. They can run on different versions of Python and have different libraries installed and running.

Setting up separate environments for separate tasks is a good idea. A complex library such as Zipline, or other backtesting engines, may have very specific requirements for which versions of other libraries it needs to have installed. Perhaps it requires a specific version of Pandas, for instance.

Then imagine if you would like to try another backtesting engine. Or perhaps you want to build something completely different by yourself, where you would like the latest versions of all libraries. Now you have a conflict.

And that's why you should set up a new and separate environment for each type of activity. A backtester like Zipline should have its own environment, so that everything can be installed and set up according to what it needs, without interfering with anything else you would like to do with Python on your computer.

Therefore, the first step here is to set up a brand new Python environment for Zipline, running on Python version 3.5. For most of this book, we are going to use this environment.

As always in Python world, there are many ways to accomplish the same thing. I won't go over every possible way, but simply pick one which I think could be easiest for beginners. If you know of other ways, feel free to use them. But I will primarily use the **Anaconda** way, using as much graphical user interface methods as I can.

Go back to **Anaconda Navigator** . We are going to use it to create a new Python environment. Click on the Environments menu on the left. Depending on your exact installation, you will likely just see one environment called root or base. At the bottom, you see some buttons to create, clone, import and remove environments. Click create.

We are going to call this new environment zip3 5 , so that we remember what it's for and which version it's running. Be sure to select Python version 3.5 in the dropdown, as in Figure 7‑1.

| root                   |               |        | Name<br>v T     |               |  |
|------------------------|---------------|--------|-----------------|---------------|--|
| Create new environment |               | X      | za              |               |  |
| Environment name       | zip35         |        | license         |               |  |
|                        | ☑ Python  ☐ R |        | nb_ext_conf     | $\mathcal{O}$ |  |
| Python version         | 3.5           | v      | r-mutex         |               |  |
|                        |               |        | r-xgboost-mutex | O             |  |
|                        | Cancel        | Create | ccelerate       |               |  |

*Figure 7*‑*1 Creating Zipline Environment*

Now you should see your new zip3 5 environment listed right there, under root. We are now ready to install the actual Zipline library.

In the previous chapter we saw how you can install libraries in **Anaconda Navigator** . You could install Zipline the same way, as long as you add the Quantopian channel. In Figure 7‑1 you can see the button for adding a channel. Think of a channel as a place where Python libraries can be downloaded from. In this case, Quantopian made their own channel.

Remember that you have to select the environment that you want to change before adding or removing any libraries. In this case,

we want to add Zipline to the zip3 5 environment, so you need to select that first to see the libraries available.

While you can install Zipline by just adding the Quantopian channel, finding Zipline and checking the Zipline library, you could also use the terminal if that's what you prefer. Most readers are probably happy to do things visually, but I want to mention this possibility so that you at least have heard of it.

The other way of installing a library would first involve opening the terminal window. The terminal is a text input, command line environment and thereby not the overly user friendly, but it can be useful to understand. You can open it by clicking that triangle next to the environment names, as you can see in Figure 7‑1.

If you click the button next to your newly created environment and select Open Terminal, you should get a terminal window, with the zip3 5 environment already activated for you. That means if we now give a command to install a Python library, it will install in that environment for us.

To install Zipline in the terminal, type the following command.

#### conda install -c Quantopian zipline

This tells the **conda** installation program to check the Quantopian channel for a library called Zipline, and install it.

The Zipline library comes with a list of dependences. That is, other libraries of specific versions that it relies upon to function. The **conda** installation program is aware of this, and will ask you if it's fine for you to go ahead and install all of those.

Once this process is finished, you now have Zipline installed on your computer. Of course, that's just one of several steps to actually get to the point of trying out a backtest.

## **Problems with Installing Zipline**

The instructions above for how to install the Zipline library have been tested by myself and a few others on different installations, operating systems and such. But with a complex library like this, there is always the potential for curveballs. If for some reason your Zipline installation did not work as planned and you got some sort of odd error message when attempting it, the best place to look for tips and help would be either Zipline's GitHub page, **<https://github.com/quantopian/zipline/issues>** , or the Google Groups forum, **<https://groups.google.com/forum/#!forum/zipline>** .

#### **Possible Version Issue**

After the first release of this book, a new version of Conda was released which broke some dependencies and refused to install Zipline. If you have Conda version 4.7 or higher and had trouble installing Zipline, you may want to try the workaround below.

```
conda config – allow_conda_downgrades true
conda install conda=4.6.11
```

# **Zipline Installation Issue**

A reader of the first edition of this book reported the following issue and solution.

Error:

Collecting package metadata (current\_repodata.json): done Solving environment: failed with current\_repodata.json, will retry with next repodata source.

#### Solution:

conda update – n base – c defaults conda

conda config – set restore\_free\_channel true

conda install – c Quantopian zipline

# **Patching the Framework**

Zipline, like most software in Python world is not only free, but open source. You can see and edit all the code as you like, and one big advantage of this is that we can make changes and even fix bugs when needed. You may wonder why you would ever want to go and edit someone else's code, but it can be very useful to have this possibility.

While writing this book, an interesting example of such a situation came up. One day, all the backtests suddenly stopped working, with an error message about failing to load benchmark data from some web address. As it turns out, there is a web call executed during backtests, where Zipline tries to pull data from an online source. This source, much like what happened to many other free data sources, suddenly stopped working without warning.

As of writing, this issue has not yet been addressed. But no worries, we can do it ourselves easily. We don't actually need this benchmark data for anything that we will do in this book, and the easiest fix is to simply remove the web call and just return empty data.

My version of Zipline is 1.3, and if you're working with the same version, you likely need to do this fix manually. It won't take long.

First locate a file called **benchmarks.py** , which should be in your Zipline installation folder. You can use the file system search tools to locate it. If you are on Windows, the path will probably be similar to this.

C:\ProgramData\Anaconda3\envs\zip35\Lib\site-packages\zipline\data

It's always a good idea to keep a backup of the original code, so rename this file to keep a copy. Then make a new file, with the name **benchmarks.py** , and put the following code in it before saving.

```
def get_benchmark_returns(symbol):
  cal = get_calendar('NYSE')
  first_date = datetime(1930,1,1)
  last_date = datetime(2030,1,1)
  dates = cal.sessions_in_range(first_date, last_date)
  data = pd.DataFrame(0.0, index=dates, columns=['close'])
  data = data['close']
  return data.sort_index().iloc[1:]
```

This code will simply return a data series from 1930 to 2030 with all zero values, which will effectively sidestep this web call issue, with no negative impact.

You may also need to bypass the cache in **loader.py** , in the same folder:

""" if data is not None: return data """

## **Zipline and Data**

As mentioned earlier, Zipline is the same backtesting engine used on the Quantopian website, but there are some pretty important differences. The most important being how you actually get financial data.

On the Quantopian site, minute level data for American stocks and futures is included for free. It's just there, ready to use. Not so with a local Zipline installation. It's fairly easy to get basic, free stock data hooked up. It's trickier to connect Zipline with high quality data from your source of choice.

In this book we are going to do both. To begin with, we will use freely available data off the internet. I will explain why this may be easy and convenient, but probably not a good idea for proper backtesting. Later in the book, we will look at how to get your own,

custom data working.

When it comes to Zipline and data, there are two words that need to be explained, which are core to this library's terminology; bundle and ingest. These are Zipline specific terms, and if you use other backtesting engines they are most likely not applicable.

A bundle is an interface to import data into Zipline. Zipline stores data in its own preferred format, and it has good reason for doing so. Zipline is able to read data incrementally, and only hold a part of it in memory at any given time.

If you run a backtest on a few stocks on daily data, that does not matter one bit. But if you are running it on a few hundred stocks on minute level, you are dealing with vast amounts of data. Reading it all and keeping in memory is not an option.

Zipline's solution is to import all data first, and store in this special format which allows for incremental reading. The bundle is the interface, which reads data from an actual data source and hands it over to Zipline for processing and storage.

Every data source needs its own bundle. There are some basic bundles included, but once you start getting really serious about backtesting, you probably want to write your own. We will get to that.

Then there is the second word, ingest. That word refers to the process of reading data with the help of a bundle, and storing in Zipline's own format. One needs to ingest a bundle before one can run a backtest. You do this from the terminal, running a command which tells Zipline to use a specific bundle to read data and store it so that it will be ready for use by a backtest.

The way that Zipline handles data is at the same time a core strength and a core weakness of this backtesting library. It's an advanced method, allowing for fast access to vast amount of data. It scales exceptionally well and you can run highly complex strategies on extremely large data sets. That's something which can't be said for

any alternative library that I have tried.

But on the other hand, this advanced functionality comes at a price. To make proper simulations, you need proper data. This is likely to entail a purchase of commercial data, and you will be left to your own devices to construct a bundle which can import to Zipline.

For now, it's only important that you understand what these two words mean. Later on, we will take a closer look at bundles and how to construct them.

# **Ingesting the Quandl Bundle**

How is that for a headline? In case you are standing in the book store, considering buying a trading book and flipped to this particular page, you would be understandably confused.

Quandl is a financial data provider, or perhaps aggregator is a better term, where you can download data off the internet. Some of their data is free, while much of it requires a subscription.

It used to be easier to get free, basic stock market data from the internet. If you pick up a book on the topic of financial modeling that was written before mid-2017, you likely see examples of how easy it is to get this data from Yahoo Finance, or perhaps Google Finance. Yes, this was indeed very easy and useful for all kinds of purposes. It was never considered high quality professional financial data, but that's beside the point. It was good enough for ad-hoc use.

But by mid-2017, the two companies which had been providing free of charge API access to financial data, suddenly and without warning stopped doing so. If they ever got around to explaining why, that explanation has still eluded me.

This little history of free online stock data is good to know, as you are likely to run into it again. Either if you read an older book, or if you go search the internet for examples. Everyone was using these

sources, up until they suddenly stopped working.

One source which still is free, at least for now, is the basic Quandl access. Zipline has an included (bundled?) bundle, which reads equity data from Quandl, and that's what we will use for our initial examples.

To be able to use the free Quandl data, you need to have register an account with them. No, it does not cost anything. Head over to Quandl.com and set up a free account. Once that's done, you can find your API key in your account settings. Copy that key out. We need it to be able to download data.

Next, go to the terminal for the zip3 5 environment. Remember that you can launch it from Anaconda, in the environments screen. Run the following command.

#### Set QUANDL\_API\_KEY=your\_own\_api\_key

Make sure to put your own key from the settings on **Quandl.com** . Setting this key only needs to be done once on your computer. After this, the setting is there and will be remembered. After this we are able to download data, and to do that we need to ingest the Quandl bundle.

zipline ingest – b quandl

This runs the ingest process, using the bundle called quandl to download free stocks data off the internet and store locally. You should see the progress bar moving, and it may take a few minutes to complete.

After this, you have access to daily equity prices to use for your backtests. Of course, this is a once off process, and it will not automatically update tomorrow. You will have to repeat this process when you want fresh data. Or figure out a way to automate it.

In case the Zipline command did not work and you were instead left with the less than helpful error message ' Failed to create proces

s ', there is an easy fix to this known bug. This is a bug that occurs on Windows environments only, and only if there are spaces in the path to your python.exe file. As of writing this it was not yet fixed. You need to locate a file called **zipline-script.py** , which is likely located either in your user profile or in the program data folder. The exact location depends on your local installation, but if you did get this particular error, search for the file and you will find it.

Open that in Notepad or similar, and put quotes around the path to python.exe.

If the top line of that file looked like this:

#!c:/path to/your/python interpreter/python.exe

Change it to this:

#!"c:/path to/your/python interpreter/python.exe"

## **Trouble Ingesting Quandl**

Feedback from the first edition shows that a small number of readers failed to ingest quandl with the following error:

"ValueError: Boolean array expected for the condition, not float64"

The same readers report that the issue was solved by downgrading Pandas to 0.18.1.

## **Installing Useful Libraries**

In chapter 4 we installed some very useful libraries, which can help get things done easier in Python World. When you install libraries, they will only install in one specific Python environment. Back then, we only had one environment; the default root

environment. Now, in this chapter, we have created a new environment specifically for Zipline. That means that the libraries we installed before, are not installed on our zip3 5 environment. We need to do that again.

You could do this exactly the same way as we did it in the previous chapter, and if you prefer that, go right ahead. But I will show you another, more visual way to install libraries for those who prefer that.

Go to **Anaconda Navigator** , click on Environments and then on the zip3 5 environment that we created. On the right side of the screen, you now see the installed libraries for this environment. But if you change that dropdown on the top to read *Not Installed* , you will see available but not yet installed libraries.

Do that and scroll down to **matplotlib** . Check the box, as in Figure 7‑2. Now do the same with **nb\_conda** . These were the libraries we installed in chapter 4. Once you have selected them, just hit the Apply button at the bottom, and they will be installed in your zip3 5 environment.

![](_page_19_Picture_4.jpeg)

## **Where to Write Backtest Algos**

As is often the case with Python, there's more than one way to do the same thing. While it's possible to use a variety of software solutions to write your Python backtests, I will stick to Jupyter Notebook, as we used in the previous chapters of this book.

Jupyter is very well suited for this type of tinkering, that backtest development usually entails. It's a great environment for testing code, and quickly getting the output and results in front of you.

One thing to keep in mind when working with Jupyter is to make sure that you have the correct environment active. After we installed the **nb\_conda** library in the previous section, this is easily done.

To launch Jupyter Notebook in the new zip3 5 environment, start by opening **Anaconda Navigator** , and go to the Environments view. Click the triangle next to the zip3 5 environment, as you can see in Figure 7‑2 and select Open with Jupyter Notebook.

Once you are in the Jupyter interface, you can make a new notebook with the zip35 environment by selecting it in the New dropdown, as in Figure 7‑3.

| 🗀 jupyter                                | Quit<br>Logout                     |  |  |
|------------------------------------------|------------------------------------|--|--|
| Files<br>Conda<br>Running<br>Clusters    |                                    |  |  |
| Select items to perform actions on them. | Upload<br>C<br>New -               |  |  |
| Bas /                                    | Notebook:                          |  |  |
| 0<br>-                                   | !e<br>Python [conda env:Anaconda3] |  |  |
| Chapter 6 - Intro                        | Python [conda env:zip35]           |  |  |
| Contacts                                 | Python [conda root]                |  |  |
|                                          | Python [default]                   |  |  |
| Desktop                                  | Other:                             |  |  |
| Documents                                | Text File<br>Folder                |  |  |
| Downloads                                |                                    |  |  |
|                                          | Terminal                           |  |  |
| Dropbox                                  |                                    |  |  |

*Figure 7*‑*3 Making a new notebook*

# **Your First Zipline Backtest**

For this first trading algorithm, we are not going to worry about realism or viability of the strategy. For now, we are merely looking at the basics of creating an algorithmic backtest.

The strategy we will create first will trade a single stock; Apple. We are going to be long Apple if the price closes over its 100 day moving average. If not, we will be in cash. The data will come from Quandl in this case, so we will be using the Quandl bundle, as discussed in the previous chapter.

The actual logic for this strategy is so simple that the bulk of the code we are going to write for it will be about showing the results, not computing the strategy. For showing the results, we will use a very similar approach to what was described in the previous chapter for how to make prettier graphs.

As with earlier, I will show code segments bit by bit as I describe them, and then show the complete code in one go after the explanations.

To begin with, as always, we need to import various libraries that we intend to use. Python alone, without importing libraries, is quite limited and to perform complex operations such as backtesting, we need a few additional things.

For a simple model like this, we don't need many import statements. Every time we run a Zipline backtest, we will need to import run\_algorith m . We will also need a few things from the zipline.ap i , but which exact things we need from there may vary depending on what we want to do in the backtest. In this case, we need the ability to place trading orders in terms of target percent, as well as the ability to look up stock symbols based on the ticker. The methods order\_target\_percen t and symbo l can do that for us. Later on, you will see many more methods that we can get from this library.

# Import Zipline functions that we need from zipline import run\_algorithm from zipline.api import order\_target\_percent, symbol

We also import the datetim e functionality as well as pyt z which lets us define time zones. Both of which are needed when we tell Zipline when exactly to start and end the backtest.

# Import date and time zone libraries from datetime import datetime import pytz

The final import statement is for matplotli b , so that we can draw some graphs based on the results of the backtest.

# Import visualization import matplotlib.pyplot as plt

There are three functions in the code for this algorithm, and you will see the same set of three functions many more times in this book. These are the functions initializ e , handle\_dat a and analyz e .

The function initializ e will be executed before the backtest starts and this is where we will set parameters and prepare what needs to be prepared before the run. In this section, as you see in the code segment just below, we do two things. We set the stock that we want trade and

we set the moving average window that we want to use. Those are the only two settings that we need for this backtest.

You can see in the code below how we look up the stock symbol based on the ticker, using the function symbo l , which we imported just now.

```
def initialize(context):
  # Which stock to trade
  context.stock = symbol('AAPL')
```

# Moving average window context.index\_average\_window = 100

The next function is handle\_dat a , which is executed for each new data point. As we are dealing with daily data here, this function will be called once per day. This is where the trading logic goes. The rules for when to buy, when to sell, and how much. It's all done right here, in handle\_dat a .

The first thing that we do here in handle\_dat a is to pull time series history. This is an important concept, as you will almost always need to do this for your backtests.

```
def handle_data(context, data):
  # Request history for the stock
  equities_hist = data.history(context.stock, "close",
                    context.index_average_window, "1d")
```

As you can see in the code above, we can use a function called histor y , which is part of the dat a object that was passed to us in the function definition. This function can pull history for a single symbol or for many at the same time. In this case, we are supplying just a single stock, but we could have provided a whole list of stocks as the first argument if that's what we were interested in.

As the second argument to the function history, we here supply the string "close " . That's because all we need for this model is a single field, the last closing price. Again here, we could have supplied a list of strings, such as ['open','high','low','close' ] if we wanted to.

Next in the same history function, we specify how many data points we want. Well, all we need to do with the data in this model is to calculate a moving average. And we already know how many periods that moving average window is, don't we? Remember that we stored that value in the variable context.index\_average\_windo w .

Lastly, we supply the string "1d " to tell the history function that we are looking for daily frequency, one day interval.

Now that we have the historical data available, it's time for the trading logic. Do you still remember the rules? We want to be long if the price is above the moving average, else flat. That's it.

```
# Check if price is above moving average
if equities_hist[-1] > equities_hist.mean():
  stock_weight = 1.0
else:
  stock_weight = 0.0
```

This code segment uses the i f statement, checking whether the price is above the average price for the requested time series history. As we requested the same amount of data points as the moving average period, all we need to do is to calculate the mean of those prices. No need to actually "move" the average, is there. Also remember the importance of indentation, and how we need that initial tab after the i f and after the els e .

In that segment, we don't actually trade. Not yet. We just set the value of the variable target\_weigh t .

The trading is next, in the final row of handle\_dat a .

order\_target\_percent(context.stock, stock\_weight)

We are using an order method here called order\_target\_percen t . This is a handy method if you want to automatically target a certain percent exposure. You could also calculate number of shares desired, and use the method order\_targe t if you so prefer, which would then need to be imported at the top as well, just like order\_target\_percen t is now.

Finally, there is the function analyz e . This function will be called after the backtest is all done, and this is where we will calculate analytics and visualize results. When this function runs, we are passed the objects contex t and per f , which will contain all the information we need about the backtest results. In the next chapter we will look in more detail on what can be done with these.

At the bottom of the code sample, we set the start and end date, before starting the backtest off. Note the input parameters used when starting the backtest run.

```
# Set start and end date
start_date = datetime(1996, 1, 1, tzinfo=pytz.UTC)
end_date = datetime(2018, 12, 31, tzinfo=pytz.UTC)
# Fire off the backtest
results = run_algorithm(
  start=start_date,
  end=end_date,
  initialize=initialize,
  analyze=analyze,
  handle_data=handle_data,
  capital_base=10000,
  data_frequency = 'daily', bundle='quandl'
)
```

This is where we tell the Zipline engine when to start and when to end the backtest. We tell it which functions to run before, during and after the backtest and how much capital to start off with. Finally we also define the data frequency as well as which data bundle to use.

Here is the complete source code for this first Zipline backtest. As with all source code in this book, you can also download it from the book website.

# This ensures that our graphs will be shown properly in the notebook. %matplotlib inline

# Import Zipline functions that we need from zipline import run\_algorithm from zipline.api import order\_target\_percent, symbol

# Import date and time zone libraries from datetime import datetime

import pytz

# Import visualization import matplotlib.pyplot as plt def initialize(context): # Which stock to trade context.stock = symbol('AAPL')

# Moving average window context.index\_average\_window = 100

def handle\_data(context, data): # Request history for the stock equities\_hist = data.history(context.stock, "close", context.index\_average\_window, "1d")

```
# Check if price is above moving average
if equities_hist[-1] > equities_hist.mean():
  stock_weight = 1.0
else:
  stock_weight = 0.0
```

```
# Place order
order_target_percent(context.stock, stock_weight)
```

def analyze(context, perf): fig = plt.figure(figsize=(12, 8))

```
# First chart
ax = fig.add_subplot(311)
ax.set_title('Strategy Results')
ax.semilogy(perf['portfolio_value'], linestyle='-',
       label='Equity Curve', linewidth=3.0)
ax.legend()
ax.grid(False)
```

```
# Second chart
ax = fig.add_subplot(312)
ax.plot(perf['gross_leverage'],
     label='Exposure', linestyle='-', linewidth=1.0)
ax.legend()
ax.grid(True)
```

```
# Third chart
```

```
ax = fig.add_subplot(313)
  ax.plot(perf['returns'], label='Returns', linestyle='-.', linewidth=1.0)
  ax.legend()
  ax.grid(True)
# Set start and end date
start_date = datetime(1996, 1, 1, tzinfo=pytz.UTC)
end_date = datetime(2018, 12, 31, tzinfo=pytz.UTC)
# Fire off the backtest
results = run_algorithm(
  start=start_date,
  end=end_date,
  initialize=initialize,
  analyze=analyze,
  handle_data=handle_data,
  capital_base=10000,
  data_frequency = 'daily', bundle='quandl'
)
```

Once you execute this code, it might take a minute or so, and then you should get the results popping up below, in the shape of three charts. In the code segment, you should be able to see how we create the three charts one by one. The first one shows the equity curve, the value development of our fictive portfolio.

The second chart shows the exposure, which the Zipline API prefers to call leverage. Lastly, the third chart shows the daily percentage returns.

You should now see a figure such as

Figure 7‑4. Some basic outputs, showing us roughly what this simple algorithm would have done for us, in theory of course.

In case you are underwhelmed at this point by the details of the output, fear not. A key strength of Python is in analyzing time series, and once the backtest is done, that's what this is all about. Analyzing the output time series. From here, we have plenty of options on how to slice, dice and display the data.

![](_page_28_Figure_0.jpeg)

*Figure 7*‑*4 First Backtest Output*

### **Portfolio Backtest**

In the previous backtest, we used a very simple strategy on a single instrument. That's probably not how most of you tend to operate. There used to be a clear divide between the hobby segment and industry participants in that the former tended to focus on single model, single asset strategies. That's not necessarily the case anymore, as increasingly more advanced tools have become available to the general public.

Not long ago, the only tools available to the public were either exclusively single asset strategy platforms, or had some rather shoddy after market portfolio extension slapped on top of it as an afterthought.

The core problem with single market strategies is that there is no diversification possible. They become pure market timing models,

and such things rarely work out in real life. Diversification is absolutely key to professional trading.

Another issue with single market strategies is the selection of that single market. Your trading rules may be systematic, but your selection of a single stock or other asset to trade is clearly discretionary. Picking that one asset is the single largest design choice of your entire strategy.

After all, the only reason why I picked Apple for the previous example is that I know that it would show great results. A long only trend following logic on a stock which has had a tremendous bull run all but ensures a great looking backtest. But that does not necessarily have any predictive value.

When constructing equity models, it's of vital importance to properly deal with instrument universe selection. That is, you need to consider carefully which stocks your algorithm will include. To have a fighting chance of showing some predictive value, your instrument selection needs to be realistic. If you test a strategy ten years back in time, the instrument selection ten years ago in your backtest need to resemble what you would have reasonably selected in reality back then.

The worst possible way to select stocks for a backtest is to pick those that are hot right now. They are of course hot now because they had great performance, and that means that your backtest is severely distorted before it even started.

In chapter 11 we will start using realistic investment universes, which aim to minimize the risk of bias. But before we get there, we are going to construct a portfolio backtest, just to get a feel for the mechanics of working with multiple markets.

In fact, what we are about to do here will have a serious logical flaw, quite on purpose. But let's just get on with it, and see if you can spot the logical error before I explain it.

Our first portfolio simulation will trade the index constituents of the Dow Jones Industrial Average. For each of the 30 member stocks, we'll check each day if the price is above or below its respective 100 day moving average.

If the price is above the moving average, we will be long with a notional allocation of 1/30, or about 3.33%. That means that in a perfect bull market, if all 30 stocks are above their respective moving averages, we will have an overall portfolio exposure of 100 percent, but most of the time it will be below that.

In this example, we are going to define the stocks that we want to consider for trading, our investment universe, in the initializ e function. As you see here, we again use the contex t object and attach a list of items to it, to be read later. Some readers who are familiar with programming may ask if we couldn't just use global variables for this, and that would be fine as well if you so prefer.

As we have seen in the previous example, Zipline makes a difference between the symbol object and the ticker string. What we need is a list of the symbols, but to make the code easier to read and edit, I first listed the symbol strings, and then in a single row I made a new list of all the corresponding symbol objects.

| def<br>initialize(context):        |  |
|------------------------------------|--|
| #<br>Which<br>stock<br>to<br>trade |  |
| dji<br>=<br>[                      |  |
| "AAPL",                            |  |
| "AXP",                             |  |
| "BA",                              |  |
| "CAT",                             |  |
| "CSCO",                            |  |
| "CVX",                             |  |
| "DIS",                             |  |
| "DWDP",                            |  |
| "GS",                              |  |
| "HD",                              |  |
| "IBM",                             |  |
| "INTC",                            |  |
| "JNJ",                             |  |
| "JPM",                             |  |
| "KO",                              |  |
| "MCD",                             |  |

```
"MMM",
  "MRK",
  "MSFT",
  "NKE",
  "PFE",
  "PG",
  "TRV",
  "UNH",
  "UTX",
  "V",
  "VZ",
  "WBA",
  "WMT",
  "XOM",
]
```

# Make a list of symbols from the list of tickers context.dji\_symbols = [symbol(s) for s in dji]

In the handle\_dat a function, we're going to make use of some Pandas tricks to get the logic done easily. First we need to fetch the historical data, and we have seen this before. This time however, we are getting history for all the stocks at once.

# Get history for all the stocks stock\_hist = data.history(context.dji\_symbols, "close", context.index\_average\_window, "1d")

Next we'll do some **Pandas** voodoo. What I plan to do here is to make a **DataFrame** with a column to tell us if a stock is above or below the average, and a column for what percentage weight of the stock that we want to hold. I'm doing it this way to teach you how this can be done with Pandas.

First we create a new **DataFrame** and then we make a column called above\_mea n , which will be set to **True** if the stock is above, and otherwise it will be **False** . Note how this logic is done in a single, clean row below. We are comparing the last price with the mean price, and we can find the last price with the ilo c function, which can locate lows in a **DataFrame** based on their numerical position. Minus one in this case means the last one, i.e. the latest point.

```
# Make an empty DataFrame to start with
stock_analytics = pd.DataFrame()
```

We continue to use the same **DataFrame** that we just created, and add a column called weigh t . Now here is an interesting trick to pay attention to. This time we are using the function lo c which can locate rows in a **DataFrame** based on a logical criterion.

That first row below does the following. It locates rows where the column above\_mea n is **True** , and for those rows, it sets the column weigh t . As we said before, we want the weight to be 1 divided by total index stocks. This way of locating rows and setting a value can get things done quickly and easily. Consider the alternative of looping through all the rows one by one.

We do the exact same thing for rows where the price is below the average, and set the weight to zero.

```
# Set weight for stocks to buy
  stock_analytics.loc[stock_analytics['above_mean'] == True, 'weight'] =
1/len(context.dji_symbols)
```

# Set weight to zero for the rest stock\_analytics.loc[stock\_analytics['above\_mean'] == False, 'weight'] = 0.0

Now we know which stocks to be long and which to be flat, and we know the weights. Now we can loop and make the trades, one by one. We can use the .iterrrows( ) to get the index and corresponding **DataFrame** row, one at a time.

As a safety, I added a check for if the stock can be traded at this time.

```
# Iterate each row and place trades
for stock, analytics in stock_analytics.iterrows():
  # Check if the stock can be traded
  if data.can_trade(stock):
     # Place the trade
     order_target_percent(stock, analytics['weight'])
```

This is really not that many actual lines of code. As you see, the trading logic could be done in just a few simple statements. This is

exactly what you want with a backtesting environment. You want to focus on what's important. You want to spend your time testing your trading ideas, not writing page after page of code just to get simple stuff done. Python, with some help from Zipline and Pandas can achieve this for you.

# This ensures that our graphs will be shown properly in the notebook. %matplotlib inline

# Import a few libraries we need from zipline import run\_algorithm

from zipline.api import order\_target\_percent, record, symbol from datetime import datetime import pytz import matplotlib.pyplot as plt import pandas as pd

def initialize(context):

# Which stock to trade dji = [ "AAPL", "AXP", "BA", "CAT", "CSCO", "CVX", "DIS", "DWDP", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK", "MSFT", "NKE", "PFE", "PG", "TRV", "UNH", "UTX", "V", "VZ",

"WBA", "WMT", "XOM",

]

# Make a list of symbols from the list of tickers context.dji\_symbols = [symbol(s) for s in dji]

# Moving average window context.index\_average\_window = 100

def handle\_data(context, data): # Get history for all the stocks stock\_hist = data.history(context.dji\_symbols, "close", context.index\_average\_window, "1d")

# Make an empty DataFrame to start with stock\_analytics = pd.DataFrame()

# Add column for above or below average stock\_analytics['above\_mean'] = stock\_hist.iloc[-1] > stock\_hist.mean()

# Set weight for stocks to buy stock\_analytics.loc[stock\_analytics['above\_mean'] == True, 'weight'] = 1/len(context.dji\_symbols)

# Set weight to zero for the rest stock\_analytics.loc[stock\_analytics['above\_mean'] == False, 'weight'] = 0.0

```
# Iterate each row and place trades
for stock, analytics in stock_analytics.iterrows():
  # Check if the stock can be traded
  if data.can_trade(stock):
     # Place the trade
     order_target_percent(stock, analytics['weight'])
```

```
def analyze(context, perf):
  fig = plt.figure(figsize=(12, 8))
```

# First chart ax = fig.add\_subplot(311) ax.set\_title('Strategy Results') ax.plot(perf['portfolio\_value'], linestyle='-', label='Equity Curve', linewidth=3.0) ax.legend() ax.grid(False)

```
# Second chart
  ax = fig.add_subplot(312)
  ax.plot(perf['gross_leverage'],
       label='Exposure', linestyle='-', linewidth=1.0)
  ax.legend()
  ax.grid(True)
  # Third chart
  ax = fig.add_subplot(313)
  ax.plot(perf['returns'], label='Returns', linestyle='-.', linewidth=1.0)
  ax.legend()
  ax.grid(True)
# Set start and end date
start = datetime(2003, 1, 1, tzinfo=pytz.UTC)
end = datetime(2017, 12, 31, tzinfo=pytz.UTC)
# Fire off the backtest
results = run_algorithm(start=start, end=end,
                    initialize=initialize, analyze=analyze,
                    handle_data=handle_data,
                    capital_base=10000,
```

After running this code, you should have an output showing you something similar as Figure 7‑5.

data\_frequency = 'daily', bundle='quandl' )

![](_page_36_Figure_0.jpeg)

Now I told you before that there is some sort of an issue with this backtest, and I suspect most readers have already picked up on that. If you did not spot it yet, go back and look at the code a moment.

I'm not referring to the fact that we have no trading costs, no slippage, or even to the viability of the strategy as such. It's not even that we started the backtest in 2003 just to make it look better, or that we magically trade instantly on the same close price that we use for the calculation. No, there is a much more fundamental issue.

What we did here, albeit on purpose, was to commit a very common but equally serious offence. We specifically set the investment universe to the current constituents of the Dow Jones Index. The index did not have the same members back in 2003 when this simulation starts.

Why does that matter? Consider why these stocks are in the index in the first place. Like for any index, the stocks that are in the

index are only there because they performed well in the past. Of course a strategy which relies on buying stocks will perform better if you run it on stocks which we already know had large gains in the past.

This is a very important issue, and we will return to it again in this book.

#### **Data Used for this Book**

To be able to build proper backtests and experiment with your trading ideas, you first need to obtain financial data of sufficient quality and import it so that your backtesting software can read it. This can be a non-trivial task, but it's something that has to be taken seriously. In the interest of maintaining the flow of this book, and to trick you into reading the more interesting parts first, I will explain data handling in more detail in chapters 23 and 24.

There you will be able to read in more detail about how to make Zipline function with your own data, and you will find source code and explanations. I suspect that most readers will want to read through the book first, before constructing the full scale backtesting environment and trying out all the source code. But I will show you all the code that you need.

For this book, I used equity data from **Norgate Data** and futures data from **CSI Data** . I picked those two because I know that they are good, and they are both priced in a range accessible to hobby traders and beginners.
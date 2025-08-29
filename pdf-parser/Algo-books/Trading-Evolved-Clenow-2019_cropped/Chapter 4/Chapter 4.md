## **Introduction to Python**

So here you are. You bought a trading book written by that guy who tends to keep things simple. You got sucked in by his last two books. They both followed a simple formula, explaining a single strategy each. One simple concept, slowly explained in detail over a few hundred pages in a way that anyone can understand. And now you are starting to realize that you got tricked into buying a programming book and it's far too late to ask for your money back.

Well, now that you already paid for the book, you might as well stick around and learn something. Yes, I'm going to teach you some programming in this book. No, it's not going to hurt. Much. It won't even be all that difficult. Strap in and make yourself comfortable. You are in for a long ride.

## **Some Assembly Required**

I have been using computers since before many of you readers were born. And that's a painful thing to say. Back in the 80's, computers were mostly dismissed as useless toys. In all fairness, they were pretty fun toys. Even in the early 90's, nobody would take computers seriously. These were the days when nerdy Scandinavian kids like me would program little 'demos', with jumping and blinking text that proclaims how smart we are in the coolest American street slang as we could muster, saving it on 5.25" floppy disks along with perfectly legal copies of computer games, put them in paper envelopes and mail them around the world to like-minded individuals. It was a strange time.

The seismic shift happened in late 1995. It was actually quite painful to watch for us computer guys. At the time, I was a member of both the university computer club, and the main party frat. That was

not how things normally worked, and I was careful in keeping the two as separate as possible. But when the president of the frat came up to me in late 1995 and asked if it's worth upgrading his 9600 bps modem to a new 14.4k, that's when I knew that our world was over. The barbarians were at the gate and there was nothing we could do to hold them back.

My premonition turned out all too true, and much like Cassandra I was helpless to change it. Suddenly everybody and his literal grandmother thought computers were the coolest thing ever. In 1994 email was something for a small group of computer enthusiasts. In 1996 your grandmother had a home page. It was a traumatic experience.

But it was not all bad. Suddenly even the most elementary computer skills became negotiable assets. Computers now became an integral part of almost any profession. You just couldn't get by without being able to use email, Word or Excel. It's almost hard to imagine now, but in 1994 few people in the world had any idea of the concept of files and folders (though we called them directories back then).

I'm sure you are all wondering if there is a point to this walk down memory lane or if I simply got old enough to rant on. Believe it or not, there actually is a point here.

Most people today view programming as some sort of specialized task for propeller heads. Programming is for programmers. The kind of people who do nothing but program all day.

Very much like how people once saw typing as a difficult and menial task, reserved for secretaries. Or how the idea of learning about file systems seemed outlandish to people in 1994. Yet today, you would have a severe disadvantage in most skilled professions if you are unable to type at reasonable speed and even more so if you don't understand basic computer usage.

You don't have to become a programmer. There will always be

people who are much better than you at programming. But that does not mean that you should stay ignorant on the subject.

Programming is not as difficult as most people would think. Once you start learning, it can be incredibly gratifying to see the results on the screen. And you don't need to go into any real depth.

Once you learn some elementary programming, you can get things done by yourself. You no longer have to rely on specialists to do these things for you. Just like how you don't need to dictate a letter for your secretary to type anymore.

So if we are over the technophobia now, let's move on.

## **Python Emerges as the Logical Choice**

From a finance and trading point of view, Python as a programming language is objectively special. It's not just yet another language with some different syntax and minor differences. It's a potential game changer and something you should really pay attention to.

Python is very easy to learn. Whether you are new to programming or a seasoned C++ coder, you can get into Python very quickly. The syntax is deliberately very easy to read. If you know nothing about Python and are shown a bit of code, you will right away see what it does. That's not true for most programming languages.

Python is to a large extent purpose built for finance. There are tools available which are designed by hedge fund quants and made available to everyone for free. Tasks which would take a lot of programming in a C style language can often be done in a single line of code. Having programmed in many different languages for the past 30 years, I have never seen a language where you can get things done

as quickly and easily as in Python.

Python is an interpreted language. That means that you don't compile your code into binary files. If those sentences don't mean anything to you, there is no need to worry. It's not important.

The **exe** and **dll** files that you see on your computer, should you be using Windows, are compiled. If you open them in a text editor, you get seemingly random garbage displayed. Compiled code is faster than interpreted code but not as easy to build and maintain. The interpreted code on the other hand is just a text file. It's translated on the fly, as it's being executed.

In the past few years, Python has emerged as the quant's language of choice. This has resulted in a substantial community and a large amount of open source tools. For people working in finance, the quant community are surprisingly open to sharing stuff.

There are some clear issues with Python of course. Given that most people using Python at the moment are hard core quants, documentation tends to assume that you already know everything and there is a clear aversion to anything user friendly. For someone entering this space, the first barrier to overcome is what at times look like a certain techno arrogance.

Most people working with Python do almost everything at a text prompt, occasionally spitting out a simplistic graph but mostly just text. There is really no technical reason for the lack of graphical environments, but it's rather a cultural thing.

With this book, I hope to make Python more accessible for traders. It really is a great tool. Don't let them scare you away.

#### **Programming Teaching Approach**

As opposed to most actual programming books, I won't start off by going over all data types, control structures and such. You will

get the hang of that later on anyhow, and it's not terribly important from the very start. In fact, I think that the usual way that programming books are structured tend to scare off, or bore off, a lot of readers. Besides, there are already plenty of such books out there which are written by people far more competent than I in explaining the in-depth technical aspects.

I will instead take a little different tack. I'm going to just drop you in it and let you swim. This is a practical, hands on book and my aim here is to get you up and running as quickly as possible. Learning about the specific differences between a tuple and a set is not important from the get go, and as we move along in this book you will pick up sufficient knowledge to get the important tasks done.

That also means that I won't explain every different possible way of doing something. I will pick one which I think will be helpful for you at the moment. Most of the time, there are multiple ways, methods, libraries or tools that can be used. I won't explain them all in this book. I will show you one path of getting things done, and once you feel confident enough to explore, you will see that the same task could be done in many different ways.

I will start by showing you how to install and set up Python on your computer. Then we will play a bit with Python, trying some code out and getting a feel for how things work.

After this, we are going to install a Python based backtesting engine. That's what we will use to run the simulations in this book. At first, we are going to do some basic, simple simulations. As the book progresses, we will get to increasingly complex and realistic modeling, and my aim is that you will get more and more comfortable with working with Python backtesting over the course of this book.

Working with a language environment like this, there is always a risk that something will change. That new versions are being released after this book, and that some parts simply don't work as they should anymore. I will do my best to reduce such risks, but it can't be avoided all together. Should such issues come up, take a look at my

website for updates and explanations.

## **Installing Python on your Computer**

Python can be run on many types of computers. It can even be run via some websites, where all is managed on a server by someone else. That can be a good idea for some things, but in this book we are going to run everything locally on your own machine. That way, you will have full control of your code, your data and your environment.

For the purpose of this book, it does not matter if you have a Windows based computer, Apple or Linux. I'm using Windows, and that means that screenshots will be from that environment, and there may be minor differences here and there in case you are on a different operating system. But it shouldn't matter much.

I don't see a reason to proclaim any of these operating systems somehow better or more suited than another. I use Windows as some financial software on my machines are only available for Windows, and because I prefer to work with Windows. In the end, it's just a tool. It would be silly to have emotional reasons for picking a tool. Pick one that gets the job done.

An enormously helpful software package for Python is **Anaconda** . That's what we will use for much of this book. It's a free software package and it's available for **Windows** , **MacOS** and **Linux** .

**Anaconda** is the de facto industry standard software package for developing and testing with Python. It's actually a collection of programs which are all installed when you download the main **Anaconda** package.

With **Anaconda** , you will get some nice graphical tools to work with, so that we don't have to do everything at a command prompt. It just makes Python life easier.

Head on over to the **Anaconda** website, (

**<https://www.anaconda.com/download/>** ) and download the latest package for your operating system. You will see that they give you a choice of downloading Python version 3 or 2. Go with the former.

Python 2 is now quite old, and there is very little reason to use it. Unless you have a really good reason to pick that one, go with version 3.

## **Let's Run Some Code**

There are a multitude of different applications and environments where you could write and run your Python code. Two of the most common are already installed on your computer at this point, as they are prepackaged with the **Anaconda** installation.

I want to briefly mention the useful but annoyingly spelled application **Spyder** , before moving into more detail about the equally annoyingly spelled **Jupyter Notebook** environment which we will be using for almost the entire remainder of this book.

**Spyder** looks and behaves very similar to what most would expect from a programming environment. If you have prior experience with writing code, you would likely feel quite at home here.

The **Spyder** environment is great for working with multiple source files, creating or editing Python files and building libraries of code. As you get more comfortable with Python, I very much encourage you to look closer at this environment. I find **Spyder** to be a useful tool and it complements the Jupyter environment well.

The only reason that this book is not using **Spyder** is that many readers are likely brand new to both Python and programming, and I would like to avoid the additional confusion of having two separate applications with different behavior to worry about.

For the purposes of modeling trading strategies, I find the **Jupyter Notebook** superior. In a generalization that I'm sure some

experienced coders will take issue with, I would say that **Spyder** is great for serious programming while **Jupyter** is great for tinkering and testing stuff.

Since building trading models is very much a process of tinkering and testing stuff, we will be using Jupyter exclusively in this book.

When you installed **Anaconda** , a few different programs were actually installed at the same time, all part of the **Anaconda** package. Open up the program **Anaconda Navigator** . This is the hub, the main control center for all your new Python tools. We will be using this program more in this book and I'm sure you'll find it quite useful.

When you open up **Anaconda Navigator** , you should see something similar to Figure 5‑1, where a few applications in the **Anaconda** package are shown. As you see, both **Jupyter** and **Spyder** are listed here, among others.

![](_page_8_Figure_0.jpeg)

*Figure 5*‑*1 Anaconda Navigator*

Click the launch button for **Jupyter** and see what happens. You might be surprised to see that a web browser is launched, and that you now have a web page in front of you, listing the files and folders of your user folder. What you will see is something very similar to Figure 5‑2.

Believe it or not, this seemingly odd web page is actually a powerful tool which we will use to build and test serious trading models in this book.

| 💭 jupyter                                |             | Quit          | Logout    |   |  |
|------------------------------------------|-------------|---------------|-----------|---|--|
| Files<br>Running<br>Clusters             |             |               |           |   |  |
| Select items to perform actions on them. |             | Upload        | New ▾     | 3 |  |
| lin /<br>6<br>0<br>-                     | Name 🔸      | Last Modified | File size |   |  |
| Contacts                                 |             | 2 days ago    |           |   |  |
| Desktop                                  | 2 days ago  |               |           |   |  |
| Documents                                | 2 days ago  |               |           |   |  |
| Downloads<br>0                           | 2 days ago  |               |           |   |  |
| ☐ Dropbox<br>$\Box$                      | 6 years ago |               |           |   |  |
| Favorites                                | 2 days ago  |               |           |   |  |
| Google Drive<br>$\Box$                   |             | 6 years ago   |           |   |  |
| C Links                                  | 2 days ago  |               |           |   |  |

#### *Figure 5*‑*2 Jupyter Notebook*

We are going to create a new file where we will write our first code. To keep things neat and organized, you may want to create a new folder for it first. You can create both a folder and a new Python file through that dropdown on the right side, which you can see in Figure 5‑2.

After you make a new file, you will be met by a new web page, which likely looks like Figure 5‑3. That text box there, just after the text In [ ] : is called a cell. In a notebook like this, you write code in cells before executing, or running the code. As we have not yet named this notebook, the text Untitled can be seen at the top. You can click on that and rename your notebook if you like, and its file name will update automatically.

| File<br>Edit | View                                   | Insert | Cell      | Kernel | Widgets   | Help |        | Trusted | Python 3 O |
|--------------|----------------------------------------|--------|-----------|--------|-----------|------|--------|---------|------------|
| B<br>86      | B<br>0                                 |        | N Run 🔳 C |        | *<br>Code |      | $\sim$ |         |            |
|              |                                        |        |           |        |           |      |        |         |            |
|              | A------------------------------------- |        |           |        |           |      |        |         |            |
|              |                                        |        |           |        |           |      |        |         |            |
|              |                                        |        |           |        |           |      |        |         |            |

*Figure 5*‑*3 Empty Jupyter Notebook*

It's time to write and run your first piece of Python code. This is a simple piece of code, designed to teach a few important concepts about this particular language.

Click in the cell in your new notebook, and enter the following code.

```
people = ['Tom','Dick',"Harry"]
for person in people:
  print("There's a person called " + person)
```

Now run the code. You can run it directly inside the notebook, either by clicking the run button in the toolbar, or simply hitting **ctrlenter** or the equivalent if you not on a Windows platform. The code will run right away, and the result output will be shown just below your cell, just like in Figure 5‑4.

The output from this should, somewhat predictably, look like this.

There's a person called Tom There's a person called Dick There's a person called Harry

As you see, it's quite easy to look at a piece of Python code and immediately see what it does. That's one of the really great parts of this language, how easy it is to read. But now look closer at this little code snippet and see what it really does.

The first row, people = ['Tom','Dick',"Harry" ] , defines a list. Lists are pretty much what other languages would call arrays; simply a list of stuff. Note that we don't need to tell Python what kind of variable type to create. In case you are used to other languages, you may notice that there is no need to declare variable and type. Another great help, and one less headache less to worry about.

![](_page_11_Picture_0.jpeg)

*Figure 5*‑*4 Your first Python Code*

In the second row, for person in people : , we initiate a loop. This is also much easier than in most other languages. We just tell the code to loop through all the items in the list peopl e . First note the colon at the end of that row. This means that we are about to supply a block of code, in this case to be looped through. The colon introduces a block of code.

Think of it as a way of saying, "Now do the stuff that I'm about to tell you about below". What follows below is a block of code. The instructions of what to do in this loop. You will see a very similar syntax later when making conditions, such as telling that code that if something is equal to something else, then run a block of code.

The next important point is how a block of code is defined in Python. This is a very important concept in Python. Note the indentation.

Many languages group blocks of code by using curly braces. Python does not do that. Here, a block of code is defined by the level of indentation. That is, the amount of blank space there is to the left of the text. Text on the same level, with the same distance to the left edge, are a group.

So the tab in on the row that starts with prin t , is absolutely necessary. That shows that this is a different block of code, subordinated to the previous one. You will see this concept all the

time, throughout this book.

In this simple example, we had only one operation that we wanted to loop. The printing of a few rows of text. If we wanted to do more things, we could just add further instructions, more rows below the print statement, on the same level of indentation.

You may have noticed that I seem to have a weird mix of single quotes and double quotes in that first row of code, people = ['Tom','Dick',"Harry" ] . Unless of course my copy editor decided to clean that up. I purposely used a really ugly syntax, where some strings are enclosed in single quotes, while one is in double quotes. I did that to show that it does not matter. You can use either single or double quotes.

But the reason I mixed the type of quotes in the print statement, print("There's a person called " + person ) is to demonstrate something else. As you see there, I'm trying to print out a single quote that is part of the sentence. In that case, the easiest solution is to simply enclose the entire sentence in double quotes.

The prin t statement concatenates a text string with the name of each person and outputs to console. So from this little silly code sample, you have now learned about lists, loops, indentions, quotes and console printing.

If this in any way seemed complicated to you, then take a moment and try this code out. Change it a bit. Make different types of lists, print different things. The best way to get a hang of it, is to just try it out for yourself.

## **Working with Jupyter Notebook**

You saw in the previous example that in a Jupyter Notebook, we write the code in a cell, and that when it is executed, the result is shown right below that cell. A notebook can have many cells, each with its own code. Sometimes it can be very useful to break the code up into a few different cells, to make it easier to keep track of, and avoid having to re-run all of the code if you change a small part. It makes tinkering easier.

What's important to understand is that the cells in a notebook share a common name space. What that means is just that each cell is aware of the results of the others. Once you have executed a code in one cell, you can refer to variables from that in other cells.

To test this concept out, make a new cell in the same notebook, below the one where we played with the list before. You can just press the plus sign in the toolbar and you will get a brand new cell.

In this new cell, write this code.

```
print("The first person is " + people[0])
```

With this row, I want to show two things. The first thing is that this second cell is aware of the variable peopl e which we created in the first cell. And as a second point to learn here is that lists are zero based. That is, we are grabbing the first element of this list with the syntax people[0 ] . As the list is zero based, the first element is 0, the second element is 1 and so on.

Figure 5‑5 demonstrates how this should look, and how the code output would appear. The idea of working with cells like this, writing and executing code segments in the cells, is something that you will have great use for when tinkering with Python.

|        | Insert<br>Cell<br>Kernel<br>Help<br>View<br>Widgets                                          | Python 3 O |
|--------|----------------------------------------------------------------------------------------------|------------|
| B<br>8 | CellToolbar<br>B<br>H<br>2<br>C<br>Code<br>$\sim$                                            |            |
|        | for person in people:<br><pre>print("There's a person called " + person)</pre>               |            |
|        | There's a person called Tom<br>There's a person called Dick<br>There's a person called Harry |            |
|        |                                                                                              |            |

*Figure 5*‑*5 Working with Cells*

## **Dictionary Lookup**

Two very closely related concepts that you will come across all the time are lists and dictionaries. In the previous section, you saw an example of how lists work. Lists are just what they sound like. Lists of just about anything. A dictionary on the other hand, is a lookup table which matches two items with each other. Just like, well, an actual dictionary.

As you just saw above, a list is defined using square brackets, like this [one, two three ] . A dictionary on the other hand uses curly braces. This makes it easy to tell in the code if you are dealing with a list or a dictionary.

Giving you a feel for what a dictionary is and how it works, let's try a brief example. We can create a new dictionary using curly braces, like the list of tickers and matching company names below.

```
stocks = {
```

"CAKE":"Cheesecake Factory", "PZZA":"Papa John's Pizza",

"FUN":"Cedar Fair", "CAR": "Avis Budget Group", }

The code above, defining the dictionary, is just one line of code. As you see, it's possible to break the line up to make it easier to read, as I have done here. A dictionary defines pairs of items, separated by a colon, in this case a ticker followed by a name after the colon.

Another thing you might notice is that I left the comma after the last item set. Clearly that's not needed, as nothing comes after it. I left it there to show that it doesn't matter. As opposed to most other programming languages, Python won't complain about this. Just another way that Python is easier and simpler.

We can now look up values in this dictionary, or we can loop through and get all the items one by one. To look up the company name behind ticker PZZA we just write stocks["PZZA" ] .

```
print(stocks["PZZA"])
```

Or if we want to iterate the items and print them all, we can use this kind of logic below.

```
for ticker, name in stocks.items():
  print("{} has ticker {}".format(name, ticker))
```

This is a clever thing in Python that you will see more of. We can unpack the item pairs, and get both the ticker and the name each loop through.

|              | ☐ Jupyter Elementary Python (autosaved)                                                                                                                     | Logout     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| File<br>Edit | Cell<br>View<br>Insert<br>Kernel<br>Widgets<br>Help                                                                                                         | Python 3 O |
| B<br>0<br>80 | CellToolbar<br>B<br>Code<br>C<br>$-1$                                                                                                                       |            |
|              |                                                                                                                                                             |            |
| In [2]:      | stocks = {<br>"CAKE": "Cheesecake Factory",<br>"PZZA": "Papa John's Pizza",<br>"FUN": "Cedar Fair",<br>"CAR": "Avis Budget Group",<br>print(stocks["PZZA"]) |            |
|              | Papa John's Pizza                                                                                                                                           |            |
| In [3]:      | for ticker, name in stocks.items():<br><pre>print("{} has ticker {}".format(name, ticker))</pre>                                                            |            |
|              | Cheesecake Factory has ticker CAKE<br>Papa John's Pizza has ticker PZZA                                                                                     |            |

*Figure 5*‑*6 Working with Dictionaries*

I also used a useful Python way of constructing a text string here. Previously we simply used plus signs to construct strings, but this way is so much easier. Using plus signs, we could have concatenated the string like this:

name + " has ticker " + ticker

That works just fine, but it's much more convenient to just write the entire string first, and then have the variable values inserted into it at the right spots. This way also has the advantage of allowing us to make formatting choices, for number values for instance, which we will do later on.

```
"{} has ticker {}".format(name, ticker)
```

That will result in the same string, but will be easier to manage. The curly braces in the text string show where we want variables to be inserted, and the function format( ) will handle it for us. We can insert as many or as few variables as we like into a text string this way.

## **Possible Issue Starting Jupyter**

Based on the first edition of this book, a reader reported issues trying to start Jupyter on his local machine. The issue was solved by downgrading the Python package **tornado** from 5.1.1 to 4.5.3. On my own development machine for this book project, I have version 5.0.2 installed without issues.

# **Conditional Logic**

The next basic concept that you need to be aware of is how to make conditional statements. For example, to tell the code that if some value is above another value, then perform some action. Think of a trading logic where you want to buy if the price is above a moving average or similar, which of course we will be doing later in this book.

A conditional statement works in a similar way as the loops we just saw. We use the word i f to show that we want to make a conditional statement, we need to end that statement with a colon, just as we did for the loops, and we need the indentation for the for following.

Building on the knowledge we just acquired using lists, take a moment to look at the following code.

```
bunch_of_numbers = [
    1, 7, 3, 6, 12, 9, 18
    ]
for number in bunch_of_numbers:
  if number == 3:
    print("The number three!")
  elif number < 10:
    print("{} is below ten.".format(number))
  else:
    print("Number {} is above ten.".format(number))
```

There are a few important points to learn in that brief code

segment. The first row should be familiar by now. We're starting by creating a list, this time of a bunch of numbers. After that, we start a loop, iterating through all those numbers, just like we did earlier in this chapter. Nothing new so far.

But then there is that first conditional statement. Take note of the double equal signs. That's not a typo. In Python, just like in most other programming languages, a single equal sign is used to assign a value, while double equal signs are used for comparison. In this case, we are saying "if the current number is equal to three, then do the following".

Also take note here of the nested indentations. After the loop is initiated, there is an indentation for the next block of code. After that, we have the i f statement, which requires its own indentation to show which code block should be run if the condition is met.

After the i f statement, you see a like which may at first not be so obvious. A new strange word, called eli f . This is just short for "else if". If the number was 3, the first condition was met and we will not reach the eli f row. This is only evaluated if the number was not three, and we did not meet the first condition.

The eli f statement checks if the number is below ten. If so, print out a line of text, and move to next number.

Finally, if neither of the conditions were met, the els e condition will be met. In this case, we know that the number was not 3 and that it was above 10.

#### **Common Mistakes**

At this point, it's probably a good idea to bring up some of the most common sources of errors early on. When first starting out with Python, I recall that the thing that kept getting me snagged was the indentation logic.

Remember that Python groups blocks of code based on how far from the left edge they are. Most of the time, this indentation is done automatically by the editor. When you end a row with a colon, for example, most Python editors will automatically start you off one tab further to the left when you press enter. It knows that you are about to make a new code block.

But that doesn't prevent the occasional error. If you for instance leave an accidental space at the start of a row, your code will fail to run. The code below is the same as we used earlier to demonstrate conditional statements, but there is a deliberate error in it. See if you can spot it.

```
bunch_of_numbers = [
    1, 7, 3, 6, 12, 9, 18
    ]
for number in bunch_of_numbers:
  if number == 3:
    print("The number three!")
   elif number < 10:
    print("{} is below ten.".format(number))
  else:
    print("Number {} is above ten.".format(number))
```

It's not that easy to see in the code segment above. The row starting with eli f now has an additional space in front of it, making it misaligned with the i f and the else statement. If you try to run this code, you will get a message about " IndendationErro r ". You can see this demonstrated in Figure 5‑7. This book is in black and white, but if you try this in a notebook, you will see that the word eli f in the code will be automatically highlighted in red, to show that something is wrong here. Look closely, if you don't spot it right away. The row with eli f is not aligned with the i f statement above it.

#### *Figure 5*‑*7 Indentation Error*

Sometimes Python error messages are friendly and helpful, and sometimes they can be rude and confusing. A good example of a nice and friendly error message is when you forget the parenthesis for a print statement. That's a very common mistake, as previous versions of Python did not require such a parentheses.

In Figure 5‑8 you can see the same code again, with missing parentheses on row 7. In the console you can see how the error message figured out what you did wrong and suggests a fix.

```
In [6]: # There's a deliberate error in this cell
         <pre>bunch_of_numbers = [</pre>
                 1, 7, 3, 6, 12, 9, 18
                 1
         for number in bunch_of_numbers:
            if number == 3:
                print "The number three!"
             elif number < 10:
                <pre>print("{} is below ten.".format(number))</pre>
             else:
                 <pre>print("Number {} is above ten.".format(number))</pre>
          File "<ipython-input-6-9c419f40eebe>", line 8
            print "The number three!"
        SyntaxError: Missing parentheses in call to 'print'. Did you mean print("The nu
         mber three!")?
```

*Figure 5-8 Missing Parentheses* 

#### **Installing Libraries**

Installation of Python libraries is usually done at the terminal. The terminal can run commands and programs for you, just like the good old command prompt. In fact, it would be possible to do this in the normal command prompt, but the way I will show you here is easier.

At this point, I merely mention the command line installation as you're likely to run into this when reading other books or online articles on the topic. While it is quite common to use text commands to deal with installations, you can avoid this additional hassle for now.

I'm guessing it's a fair assumption that most readers of this particular book would prefer to avoid text commands wherever possible, so instead I will show you a visual way of accomplishing the same task.

When you installed the **Anaconda** package, as discussed earlier in this chapter, one of the applications installed was **Anaconda Navigator** . Find it, and open it. This application can help simplify a lot of common Python tasks, and you will likely be using it quite a lot.

When you open **Anaconda Navigator** , you should see a sidebar menu on the left. One of these menu items is Environments. Go there. We will go into environments a bit more later on, as we will soon create a new one. The ability to have multiple environments is great, as we can install environments with specific libraries and versions for specific purposes.

For now, if you just made a fresh installation of **Anaconda** , you will probably only have one item here, which is likely called root or base.

Select the root environment, and the right side of the screen

will update to show you exactly which libraries are installed in this environment. As you can see in Figure 5‑9, there is also a dropdown where you can select if you want to see libraries that are already installed or those available but not yet installed.

![](_page_23_Picture_1.jpeg)

*Figure 5*‑*9 Anaconda Libraries*

The simplest way to install a new Python library is to go here and select Not Installed in that dropdown, so that you see libraries available for installation. Find the library that you need, check it, and hit the Apply button at the bottom. That's it.

At this point, you're wondering what libraries you need to install, and why. Well, I mention how to install libraries early on, because from time to time you will run into code samples which use libraries which you don't yet have installed. When you do need it, it's better to know in advance what to do.

We will need some quite common libraries early on in this book, so before moving on to next chapter, make sure that you've got them installed. Depending on your installation, you may already have

them installed, but let's check.

Select to view all libraries in that dropdown, the one that you can see in Figure 5‑9, and then find **Pandas** . You can use the search field on top to find it faster. If there is a check mark next to this library, it's already installed and you're all good. Next verify that **MatPlotLib** is installed, the same way. It if's not installed, click the check box next to it and apply changes.

These are two very common libraries which we will use in practically all sample code from here on in this book. The first library revolutionizes time series processing and is the number one reason for the rise of Python in financial modeling, and the second library is for visualizing data.

It's important to remember that if you are using multiple environments, which we will do soon in this book, the library you just installed did not install into all of them. Just the one that you had selected, in this case the root or base environment.

Some more complex libraries may be dependent on other libraries. In that case, they will automatically make sure that all dependencies are installed as well. Most backtesting libraries, for instance, will require a set of other libraries to be installed. When we install those backtesting libraries, they will take care of installing all these other required libraries for us.
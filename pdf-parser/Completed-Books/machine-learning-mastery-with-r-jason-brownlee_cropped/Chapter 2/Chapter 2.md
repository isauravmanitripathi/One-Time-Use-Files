## Chapter 2

# The R Platform

R is one of the most powerful machine learning platforms and is used by the top data scientists in the world. In this Chapter you will get an introduction to R and why you should use R for machine learning.

### 2.1 Why Use R

There are five reasons why you should use R for your predictive modeling machine learning problems:

- R is used by the best data scientists in the world. In surveys on Kaggle (the competitive machine learning platform), R is by far the most used machine learning tool<sup>1</sup> When professional machine learning practitioners were surveyed in 2015, again the most popular machine learning tool was R<sup>2</sup> .
- R is powerful because of the breadth of techniques it offers in third-party packages. Any techniques that you can think of for data analysis, visualization, data sampling, supervised learning and model evaluation are provided in R. The platform has more techniques than any other that you will come across.
- R is state-of-the-art because it is used by academics. One of the reasons why R has so many techniques is because academics who develop new algorithms are developing them in R and releasing them as R packages. This means that you can get access to state-of-the-art algorithms in R before other platforms. It also means that you can only access some algorithms in R until someone ports them to other platforms.
- R is free because it is open source software. You can download it right now for free and it runs on any workstation platform you are likely to use.
- R is a lot of fun. I think the fun comes from the sense of exploration (you're always finding out about some new amazing technique) and because of the results you get (you can run very powerful methods on your data in a few lines of code). I use other platforms, but I always come back to R when I've got serious work to do.

Convinced?

<sup>1</sup><http://blog.kaggle.com/2011/11/27/kagglers-favorite-tools>

<sup>2</sup><http://www.kdnuggets.com/2015/05/poll-r-rapidminer-python-big-data-spark.html>

### 2.2 What Is R

R is a language, an interpreter and a platform.

- R is a computer language . It can be difficult to learn but is familiar and you will figure it out quickly if you have used other scripting languages like Python, Ruby or BASH.
- R is an interpreter . You can write scripts and save them as files. Like other scripting languages, you can then use the interpreter to run those scripts any time. R also provides a REPL environment where you can type in commands and see the output immediately.
- R is also a platform . You can use it to create and display graphics, to save and load state and to interface with other systems. You can do all of your exploration and development in the REPL (read-evaluate-print loop) environment if you so wish.

#### 2.2.1 Where R Came From

R was created by Ross Ihaka and Robert Gentleman at the University of Auckland, New Zealand as an implementation of the S programming language. Development started in 1993. A version was made available on FTP released under the GNU GPL in 1995. The larger core group and open source project was setup in 1997.

It started as an experiment by the authors to implement a statistical test bed in Lisp using a syntax like that provided in S. As it developed, it took on more of the syntax and features of S, eventually surpassing it in capability and scope.

#### 2.2.2 Power In The Packages

R itself is very simple. It provides built in commands for basic statistics and data handing. The machine learning features of R that you will use come from third party packages. Packages are plug-ins to the R platform. You can search for, download and install them within the R environment.

Because packages are created by third parties, their quality can vary. It is a good idea to search for the best-of-breed packages that provide a specific technique you want to use. Packages provide documentation in the form of help for each package function and often vignettes that demonstrate how to use the package.

Before you write a line of code, always search to see if there is a package that can do what you need. You can search for packages on the Comprehensive R Archive Network or CRAN for short<sup>3</sup> .

#### 2.2.3 Not For Production

R is probably not the best solution for building a production model. The techniques may be state-of-the-art but they may not use the best software engineering principles, have tests or be scalable to the size of the datasets that you may need to work with.

That being said, R may be the best solution to discover what model to actually use in production. The landscape is changing and people are writing R scripts to run operationally and services are emerging to support larger datasets.

<sup>3</sup><https://cran.r-project.org>

## 2.3 Summary

This chapter provided an introduction to R. You discovered:

- 5 Good reasons why you should be using R for machine learning, not least because it used by some of the best data scientists in the world.
- That R is 3 things, a programming language, interpreter and platform.
- That the power of R comes from the free third-party packages that you can download.
- That R is excellent for R&D and one-off projects, but probably inappropriate for running production models.

#### 2.3.1 Next Step

Next is Part II where you will begin working through the lessons, the main body of this book. The first lesson is quick and will assist you in installing R and running it for the first time.
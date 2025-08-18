# Chapter 3

# Installing and Starting R

You may not have R installed and you may have never used the R environment before. This lesson will teach you:

- 1. How to download and install R.
- 2. How to start the R interactive environment.
- 3. How to run an R script.

If you have R installed, know how to start and use R, you can probably skip this lesson.

### 3.1 Download and Install R

You need R installed if you are going to learn how to work through predictive modeling machine learning problems using the platform. As a developer, you are already familiar with how to download and install software on your computer. So I don't need to go into too much detail. Let's download and install R:

- 1. Start off by visiting the R Project home page at: <https://www.r-project.org>. You will notice that there is no direct download link, instead you are directed to a list of international mirrors websites from which you can download R: <https://cran.r-project.org/mirrors.html>.
- 2. Select a mirror and click the link, for example the Berkley mirror: <http://cran.cnr.berkeley.edu/>.
- 3. You are now presented with a list of R downloads for Linux, Mac (OS X) and Windows. Each platform has it's own webpage. For Linux, you can choose the appropriate platform and you will be directed to use the package manager to install R. Mac provides binaries for modern versions of the operating system, download the package. Windows provides an executable that you can download.
- 4. Once you have downloaded the binary package suitable for your environment, go ahead and install it. Depending on your platform, you may or may not require administration rights.

#### 3.1. Download and Install R 13

Figure 3.1: Screenshot the R download webpage.

Which version of R should you download? Always download the latest version. The examples in this book require least version 3.2 of R. If you are having trouble, each platform has specific installation instructions and frequently asked that you may find useful. A good general place to start is the How can R be installed? part of the general R FAQ<sup>1</sup> . Another helpful guide is: R Installation and Administration<sup>2</sup> .

### 3.2 R Interactive Environment

You can start R from whatever menu system you use on your operating system. This will load the R interactive environment. For example, below is a screenshot of the R interactive environment on my system.

![](_page_2_Picture_4.jpeg)

Figure 3.2: Screenshot of the R interactive environment launched from a menu.

In practice, I prefer the command line. It works everywhere and looks the same everywhere. Open your command line, change (or create) to your project directory and start R by typing:

R

Listing 3.1: The R command on the command line.

You should see something like the screenshot below either in your terminal.

<sup>1</sup><https://cran.r-project.org/doc/FAQ/R-FAQ.html>

<sup>2</sup><https://cran.r-project.org/doc/manuals/r-release/R-admin.html>

Figure 3.3: Screenshot of the R interactive environment at the command line.

You can close the interactive environment by calling the quit function q(). The R interactive environment is very useful for exploring and learning how to use packages and functions. You should spend a lot of time in the interactive environment when you are just starting out. The environment is also very good if you are exploring a new problem and trying what-if scenarios. It is also great if you want to use a systematic process and come up with a prototype model very quickly without the full rigmarole. I recommend that you use the R interactive environment while working through all of the lessons in this book.

#### 3.3 R Scripts

You can save your R commands into a file with a .R extension. These are called R scripts. R scripts can be run from the command line, called from shell scripts and (my personal favorite) called from targets in a Makefile.

Below is an R script. Type this or copy-and-paste it into a new file and save it into your working directory as your script.R. This simple script loads a standard machine learning dataset called iris (the iris flowers dataset) and summarizes all of the attributes. You will learn a lot more about these commands in later lessons.

| data(iris)    |  |
|---------------|--|
| summary(iris) |  |

Listing 3.2: Sample content for your custom R script.

Open your terminal (command line) and change directory to wherever you saved the your script.R file. Type the following command:

|  |  |  |  |  |  | R CMD BATCH your_script.R your_script.log |
|--|--|--|--|--|--|-------------------------------------------|
|--|--|--|--|--|--|-------------------------------------------|

Listing 3.3: Example of running your R script from the command line.

This command runs the script file your script.R using R in a batch mode (non-iteratively) and saves any results in the file your script.log. Take a look in the log file your script.log and you will see the output of the two commands from your script, as well as some executing timing information (shown below).

```
> data(iris)
> summary(iris)
 Sepal.Length Sepal.Width Petal.Length Petal.Width
Min. :4.300 Min. :2.000 Min. :1.000 Min. :0.100
1st Qu.:5.100 1st Qu.:2.800 1st Qu.:1.600 1st Qu.:0.300
Median :5.800 Median :3.000 Median :4.350 Median :1.300
Mean :5.843 Mean :3.057 Mean :3.758 Mean :1.199
3rd Qu.:6.400 3rd Qu.:3.300 3rd Qu.:5.100 3rd Qu.:1.800
Max. :7.900 Max. :4.400 Max. :6.900 Max. :2.500
      Species
setosa :50
versicolor:50
virginica :50
> proc.time()
  user system elapsed
 3.255 0.117 3.364
```

Listing 3.4: Output from running your R script.

I recommend that if you have a large machine learning project that you develop scripts. I do not recommend that you use scripts to work through the lessons in this book. Each task in your project could be described in a new script which can be documented, updated and tracked in revision control. I would also recommend using make with a Makefile (or similar build system) and create targets to call each of your scripts. This will ensure that the steps of your project are independent, repeatable, and reusable on future projects.

#### 3.4 Summary

This lesson gave you a crash course in how to install and start R, just in case you are completely new to the platform. In this lesson you learned:

- 1. How to download and install R.
- 2. How to start the R interactive environment.
- 3. How to run an R script.

#### 3.4.1 Next Step

In the next lesson you will get a crash course in the R programming language, designed specifically to get a developer like you up to speed with R very fast.
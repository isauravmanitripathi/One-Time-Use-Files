# Chapter 1

## Welcome

Welcome to Machine Learning Mastery with R. This book is your guide to applied machine learning with R. You will discover the step-by-step process that you can use to get started and become good at machine learning for predictive modeling on the R platform.

## 1.1 Learn R The Wrong Way

Here is what you should NOT do when you start studying machine learning in R.

- 1. Get really good at R programming and R syntax.
- 2. Deeply study the underlying theory and parameters for machine learning algorithms in R.
- 3. Avoid or lightly touch on all of the other tasks needed to complete a real project.

I think that this approach can work for some people, but it is a really slow and a roundabout way of getting to your goal. It teaches you that you need to spend all your time learning how to use individual machine learning algorithms. It also does not teach you the process of building predictive machine learning models in R that you can actually use to make predictions. Sadly, this is the approach used to teach machine learning that I see in almost all books and online courses on the topic.

## 1.2 Machine Learning in R

This book focuses on a specific sub-field of machine learning called predictive modeling. This is the field of machine learning that is the most useful in industry and the type of machine learning that the R platform excels at facilitating. Unlike statistics, where models are used to understand data, predictive modeling is laser focused on developing models that make the most accurate predictions at the expense of explaining why predictions are made. Unlike the broader field of machine learning that could feasibly be used with data in any format, predictive modeling is primarily focused on tabular data (e.g. tables of numbers like a spreadsheet).

This book was written around three themes designed to get you started and using R for applied machine learning effectively and quickly. These three parts are as follows:

- Lessons : Learn how the sub-tasks of a machine learning project map onto R and the best practice way of working through each task.
- Projects : Tie together all of the knowledge from the lessons by working through case study predictive modeling problems.
- Recipes : Apply machine learning with a catalog of standalone recipes in R that you can copy-and-paste as a starting point for new projects.

#### 1.2.1 Lessons

You need to know how to complete the specific subtasks of a machine learning project on the R platform. Once you know how to complete a discrete task using the platform and get a result reliably, you can do it again and again on project after project. Let's start with an overview of the common tasks in a machine learning project. A predictive modeling machine learning project can be broken down into 6 top-level tasks:

- 1. Define Problem: Investigate and characterize the problem in order to better understand the goals of the project.
- 2. Analyze Data: Use descriptive statistics and visualization to better understand the data you have available.
- 3. Prepare Data: Use data transforms in order to better expose the structure of the prediction problem to modeling algorithms.
- 4. Evaluate Algorithms: Design a test harness to evaluate a number of standard algorithms on the data and select the top few to investigate further.
- 5. Improve Results: Use algorithm tuning and ensemble methods to get the most out of well-performing algorithms on your data.
- 6. Present Results: Finalize the model, make predictions and present results.

A blessing and a curse with R is that there are so many techniques and so many ways to do something with the platform. In part II of this book you will discover one easy or best practice way to complete each subtask of a general machine learning project. Below is a summary of the Lessons from Part II and the sub-tasks that you will learn about.

- Lesson 1: Install and Start R.
- Lesson 2: R Language Crash Course.
- Lesson 3: Load Standard Datasets.
- Lesson 4: Load Custom Data. (Analyze Data)
- Lesson 5: Understand Data With Descriptive Statistics. (Analyze Data)
- Lesson 6: Understand Data With Visualization. (Analyze Data)

- Lesson 7: Pre-Process Data. (Prepare Data)
- Lesson 8: Resampling Methods. (Evaluate Algorithms)
- Lesson 9: Algorithm Evaluation Metrics. (Evaluate Algorithms)
- Lesson 10: Spot-Check Algorithms. (Evaluate Algorithms)
- Lesson 11: Model Selection. (Evaluate Algorithms)
- Lesson 12: Algorithm Parameter Tuning. (Improve Results)
- Lesson 13: Ensemble Methods. (Improve Results)
- Lesson 14: Finalize Model. (Present Results)

These lessons are are intended to be read from beginning to end in order, showing you exactly how to complete each task in a predictive modeling machine learning project. Of course, you can dip into specific lessons again later to refresh yourself. Some lessons are demonstrative, showing you how to use specific techniques for a common machine learning task (e.g. data loading and data pre-processing). Others are in a tutorial format, building throughout the lesson to culminate in a final result (e.g. algorithm tuning and ensemble methods). Each lesson was designed to be completed in under 30 minutes (depending on your level of skill and enthusiasm). It is possible to work through the entire book in one weekend. It also works if you want to dip into specific sections and use the book as a reference.

#### 1.2.2 Projects

Recipes for common predictive modeling tasks are critically important, but they are also just the starting point. This is where most books and courses stop.

You need to piece the recipes together into end-to-end projects. This will show you how to actually deliver a model or make predictions on new data using R. This book uses small well-understood machine learning datasets from the UCI Machine learning repository<sup>1</sup> in both the lessons and in the example projects. These datasets are available for free as CSV downloads, and most are available directly in R by loading third party packages. These datasets are excellent for practicing applied machine learning because:

- They are small, meaning they fit into memory and algorithms can model them in reasonable time.
- They are well behaved, meaning you often don't need to do a lot of feature engineering to get a good result.
- They are benchmarks, meaning that many people have used them before and you can get ideas of good algorithms to try and accuracy levels you should expect.

In Part III you will work through three projects:

<sup>1</sup><http://archive.ics.uci.edu/ml>

- Hello World Project (Iris flowers dataset) : This is a quick pass through the project steps without much tuning or optimizing on a dataset that is widely used as the hello world of machine learning.
- Regression (Boston House Price dataset) : Work through each step of the project process with a regression problem.
- Binary Classification (Wisconsin Breast Cancer dataset) : Work through each step of the project process using all of the methods on a binary classification problem.

These projects unify all of the lessons from Part II. They also give you insight into the process for working through predictive modeling machine learning problems which is invaluable when you are trying to get a feeling for how to do this in practice. Also included in this section is a template for working through predictive modeling machine learning problems which you can use as a starting point for current and future projects. I find this useful myself to set the direction and set up important tasks (which are easy to forget) on new projects, and I'm sure you will too.

#### 1.2.3 Recipes

Recipes are small code snippets in R that show you how to do one specific thing and get a result. For example, you could have a recipe that demonstrates how to use Random Forest algorithm for classification. You could have another for normalizing the attributes of a dataset.

Recipes make the difference between a beginner who is having trouble and a fast learner capable of making accurate predictions quickly on any new project. A catalog of recipes provides a repertoire of skills that you can draw from when starting a new project. More formally, recipes are defined as follows:

- Recipes are code snippets not tutorials.
- Recipes provide just enough code to work.
- Recipes are demonstrative not exhaustive.
- Recipes run as-is and produce a result.
- Recipes assume that required packages are installed.
- Recipes use built-in datasets or datasets provided in specific packages.

You are starting your journey into machine learning with R with my personal catalog of machine learning recipes provided with this book. All of the code from the lessons in Part II are available in your R recipe catalog. There are also recipes for techniques not covered in this book, including usage of a very large number of algorithms and many additional case studies. Recipes are divided into directories according to the common tasks of a machine learning project as listed above. The list below provides a summary of the recipes available.

 Analyze Data: Recipes to load, summarize and visualize data, including visualizations using univariate plots, multivariate plots and projection methods.

- Prepare Data: Recipes for data preparation including data cleaning, feature selection and data transforms.
- Algorithms: Recipes for using a large number of machine learning algorithms both standalone and within the popular R package caret, including linear, non-linear, trees, ensembles for classification and regression.
- Evaluate Algorithms: Recipes for re-sampling methods, algorithm evaluation metrics and model selection.
- Improve Results: Recipes for algorithm tuning and ensemble methods.
- Finalize Model: Recipes to make final predictions, to finalize the model and save and load models to disk.
- Other: Recipes for managing packages and getting started with R syntax.
- Case Studies: Case studies for binary classification, multi-class classification and regression problems.

This is an invaluable resource that you can use to jump-start your current and future machine learning projects. You can also build upon this recipe catalog as you discover new techniques.

#### 1.2.4 Your Outcomes From This Process

This book will lead you from being a developer who is interested in machine learning with R to a developer who has the resources and capability to work through a new dataset end-to-end using R and develop accurate predictive models. Specifically, you will know:

- How to work through a small to medium sized dataset end-to-end.
- How to deliver a model that can make accurate predictions on new unseen data.
- How to complete all subtasks of a predictive modeling problem with R.
- How to learn new and different techniques in R.
- How to get help with R.

From here you can start to dive into the specifics of the functions, techniques and algorithms used with the goal of learning how to use them better in order to deliver more accurate predictive models, more reliably in less time.

## 1.3 What This Book is Not

This book was written for professional developers who want to know how to build reliable and accurate machine learning models in R.

 This is not a machine learning textbook. We will not be getting into the basic theory of machine learning (e.g. induction, bias-variance trade-off, etc.). You are expected to have some familiarity with machine learning basics, or be able to pick them up yourself.

- This is not an algorithm book. We will not be working through the details of how specific machine learning algorithms work (e.g. random forest). You are expected to have some basic knowledge of machine learning algorithms or how to pick up this knowledge yourself.
- This is not an R programming book. We will not be spending a lot of time on R syntax and programming (e.g. basic programming tasks in R). You are expected to be a developer who can pick up a new C-like language relatively quickly.

You can still get a lot out of this book of you are weak in one or two of these areas, but you may struggle picking up the language or require some more explanation of the techniques. If this is the case, see the Resources Chapter at the end of the book and seek out a good companion reference text.

## 1.4 Summary

I hope you are as excited as me to get started. In this introduction chapter you learned that this book is unconventional. Unlike other books and courses that focus heavily on machine learning algorithms in R and focus on little else, this book will walk you through each step of a predictive modeling machine learning project.

- Part II of this book provides standalone lessons including a mixture of recipes and tutorials to build up your basic working skills and confidence in R.
- Part III of this book will introduce a machine learning project template that you can use as a starting point on your own projects and walks you through three end-to-end projects.
- The recipes companion to this book provides a catalog of more than 150 machine learning recipes in R. You can browse this invaluable resource, find useful recipes and copy-and-paste them into your current and future machine learning projects.
- Part IV will finish out the book. It will look back at how far you have come in developing your new found skills in applied machine learning with R. You will also discover resources that you can use to get help if and when you have any questions about R or the platform.

### 1.4.1 Next Step

In the next Chapter you will take a closer look at R. You will discover what R is, why it is so powerful as a platform for machine learning and the different ways you should and should not use the platform.
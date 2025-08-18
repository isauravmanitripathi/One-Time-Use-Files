## Chapter 3

# Examples of Statistics in Machine Learning

Statistics and machine learning are two very closely related fields. In fact, the line between the two can be very fuzzy at times. Nevertheless, there are methods that clearly belong to the field of statistics that are not only useful, but invaluable when working on a machine learning project. It would be fair to say that statistical methods are required to effectively work through a machine learning predictive modeling project. In this chapter, you will discover specific examples of statistical methods that are useful and required at key steps in a predictive modeling problem. After completing this chapter, you will know:

- Exploratory data analysis, data summarization, and data visualizations can be used to help frame your predictive modeling problem and better understand the data.
- That statistical methods can be used to clean and prepare data ready for modeling.
- That statistical hypothesis tests and estimation statistics can aid in model selection and in presenting the skill and predictions from final models.

Let's get started.

#### 3.1 Overview

In this chapter, we are going to look at 10 examples of where statistical methods are used in an applied machine learning project. This will demonstrate that a working knowledge of statistics is essential for successfully working through a predictive modeling problem.

- 1. Problem Framing
- 2. Data Understanding
- 3. Data Cleaning
- 4. Data Selection
- 5. Data Preparation

- 6. Model Evaluation
- 7. Model Configuration
- 8. Model Selection
- 9. Model Presentation
- 10. Model Predictions

#### 3.2 Problem Framing

Perhaps the point of biggest leverage in a predictive modeling problem is the framing of the problem. This is the selection of the type of problem, e.g. regression or classification, and perhaps the structure and types of the inputs and outputs for the problem. The framing of the problem is not always obvious. For newcomers to a domain, it may require significant exploration of the observations in the domain.

For domain experts that may be stuck seeing the issues from a conventional perspective, they too may benefit from considering the data from multiple perspectives. Statistical methods that can aid in the exploration of the data during the framing of a problem include:

- Exploratory Data Analysis. Summarization and visualization in order to explore ad hoc views of the data.
- Data Mining. Automatic discovery of structured relationships and patterns in the data.

#### 3.3 Data Understanding

Data understanding means having an intimate grasp of both the distributions of variables and the relationships between variables. Some of this knowledge may come from domain expertise, or require domain expertise in order to interpret. Nevertheless, both experts and novices to a field of study will benefit from actually handling real observations form the domain. Two large branches of statistical methods are used to aid in understanding data; they are:

- Summary Statistics. Methods used to summarize the distribution and relationships between variables using statistical quantities.
- Data Visualizations. Methods used to summarize the distribution and relationships between variables using visualizations such as charts, plots, and graphs.

#### 3.4 Data Cleaning

Observations from a domain are often not pristine. Although the data is digital, it may be subjected to processes that can damage the fidelity of the data, and in turn any downstream processes or models that make use of the data. Some examples include:

Data corruption.

- Data errors.
- Data loss.

The process of identifying and repairing issues with the data is called data cleaning Statistical methods are used for data cleaning; for example:

- Outlier detection. Methods for identifying observations that are far from the expected value in a distribution.
- Imputation. Methods for repairing or filling in corrupt or missing values in observations.

## 3.5 Data Selection

Not all observations or all variables may be relevant when modeling. The process of reducing the scope of data to those elements that are most useful for making predictions is called data selection. Two types of statistical methods that are used for data selection include:

- Data Sample. Methods to systematically create smaller representative samples from larger datasets.
- Feature Selection. Methods to automatically identify those variables that are most relevant to the outcome variable.

#### 3.6 Data Preparation

Data can often not be used directly for modeling. Some transformation is often required in order to change the shape or structure of the data to make it more suitable for the chosen framing of the problem or learning algorithms. Data preparation is performed using statistical methods. Some common examples include:

- Scaling. Methods such as standardization and normalization.
- Encoding. Methods such as integer encoding and one hot encoding.
- Transforms. Methods such as power transforms like the Box-Cox method.

#### 3.7 Model Evaluation

A crucial part of a predictive modeling problem is evaluating a learning method. This often requires the estimation of the skill of the model when making predictions on data not seen during the training of the model. Generally, the planning of this process of training and evaluating a predictive model is called experimental design. This is a whole subfield of statistical methods.

 Experimental Design. Methods to design systematic experiments to compare the effect of independent variables on an outcome, such as the choice of a machine learning algorithm on prediction accuracy.

As part of implementing an experimental design, methods are used to resample a dataset in order to make economic use of available data in order to estimate the skill of the model. These methods are another subfield of statistical methods.

 Resampling Methods. Methods for systematically splitting a dataset into subsets for the purposes of training and evaluating a predictive model.

## 3.8 Model Configuration

A given machine learning algorithm often has a suite of hyperparameters that allow the learning method to be tailored to a specific problem. The configuration of the hyperparameters is often empirical in nature, rather than analytical, requiring large suites of experiments in order to evaluate the effect of different hyperparameter values on the skill of the model. The interpretation and comparison of the results between different hyperparameter configurations is made using one of two subfields of statistics, namely:

- Statistical Hypothesis Tests. Methods that quantify the likelihood of observing the result given an assumption or expectation about the result (presented using critical values and p-values).
- Estimation Statistics. Methods that quantify the uncertainty of a result using confidence intervals.

## 3.9 Model Selection

One among many machine learning algorithms may be appropriate for a given predictive modeling problem. The process of selecting one method as the solution is called model selection. This may involve a suite of criteria both from stakeholders in the project and the careful interpretation of the estimated skill of the methods evaluated for the problem. As with model configuration, two classes of statistical methods can be used to interpret the estimated skill of different models for the purposes of model selection. They are:

- Statistical Hypothesis Tests. Methods that quantify the likelihood of observing the result given an assumption or expectation about the result (presented using critical values and p-values).
- Estimation Statistics. Methods that quantify the uncertainty of a result using confidence intervals.

## 3.10 Model Presentation

Once a final model has been trained, it can be presented to stakeholders prior to being used or deployed to make actual predictions on real data. A part of presenting a final model involves presenting the estimated skill of the model. Methods from the field of estimation statistics can be used to quantify the uncertainty in the estimated skill of the machine learning model through the use of tolerance intervals and confidence intervals.

 Estimation Statistics. Methods that quantify the uncertainty in the skill of a model via confidence intervals.

## 3.11 Model Predictions

Finally, it will come time to start using a final model to make predictions for new data where we do not know the real outcome. As part of making predictions, it is important to quantify the confidence of the prediction. Just like with the process of model presentation, we can use methods from the field of estimation statistics to quantify this uncertainty, such as confidence intervals and prediction intervals.

 Estimation Statistics. Methods that quantify the uncertainty for a prediction via prediction intervals.

## 3.12 Summary

In this tutorial, you discovered the importance of statistical methods throughout the process of working through a predictive modeling project. Specifically, you learned:

- Exploratory data analysis, data summarization, and data visualizations can be used to help frame your predictive modeling problem and better understand the data.
- That statistical methods can be used to clean and prepare data ready for modeling.
- That statistical hypothesis tests and estimation statistics can aid in model selection and in presenting the skill and predictions from final models.

#### 3.12.1 Next

This is the end of part II, in the next part you will discover the foundations you need to know in statistics, starting with how to summarize the Gaussian distribution.
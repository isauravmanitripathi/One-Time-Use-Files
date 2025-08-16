# **Credit Scoring**

Credit scoring models play a fundamental role in the risk management practice at most banks. Commercial banks' primary business activity is related to extending credit to borrowers and generating loans and credit assets. A significant component of a bank's risk, therefore, lies in the quality of its assets that needs to be in line with the bank's risk appetite.a To manage risk efficiently, quantifying it with the most appropriate and advanced tools is an extremely important factor in determining the bank's success.

Credit risk models are used to quantify credit risk at counterparty or transaction level and they differ significantly by the nature of the counterparty (e.g., corporate, small business, private individual). Rating models have a long-term view (through the cycle) and have been always associated with corporate clients, financial institutions, and public sector (*see* **Credit Rating**; **Counterparty Credit Risk**). Scoring models, instead, focus more on the short term (point in time) and have been mainly applied to private individuals and, more recently, extended to small- and medium-sized enterprises (SMEs).b In this article, we focus on credit scoring models, giving an overview of their assessment, implementation, and usage.

Since 1960s, larger organizations have been utilizing credit scoring to quickly and accurately assess the risk level of their prospects, applicants, and existing customers mainly in the consumer-lending business. Increasingly, midsize and smaller organizations are appreciating the benefits of credit scoring as well. The credit score is reflected in a number or letter(s) that summarizes the overall risk utilizing available information on the customer. Credit scoring models predict the probability that an applicant or existing borrower will default or become delinquent over a fixed time horizon.c The credit score empowers users to make quick decisions or even to automate decisions, and this is extremely desirable when banks are dealing with large volumes of clients and relatively small margin of profits at individual transaction level.

Credit scoring models can be classified into three main categories: application, behavioral, and collection models, depending on the stage of the consumer credit cycle in which they are used. The main difference between them lies in the set of variables that are available to estimate the client's creditworthiness, that is, the earlier the stage in the credit cycle, the lower the number of specific client information available to the bank. This generally means that application models have a lower prediction power than behavioral and collection models.

Over the last 50 years, several statistical methodologies have been used to build credit scoring models. The very simplistic univariate analysis applied at the beginning (late 1950s) was replaced as soon as academic research started to focus on credit scoring modeling techniques (late 1960s). The seminal works, in this field, of Beaver [10] and Altman [1] introduced the multivariate discriminant analysis (MDA) that became the most popular statistical methodology used to estimate credit scoring models until Ohlson [26], for the first time, applied the conditional logit model to the default prediction's study. Since Ohlson's research (early 1980s), several other statistical techniques have been utilized to improve the prediction power of credit scoring models (e.g., linear regression, probit analysis, Bayesian methods, neural network, etc.), but the logistic regression still remains the most popular method.

Lately, credit scoring has gained new importance with the new Basel Capital Accord. The so-called Basel II replaces the current 1988 capital accord and focuses on techniques that allow banks and supervisors to properly evaluate the various risks that banks face (*see* **Internal-ratings-based Approach**; **Regulatory Capital**). Since credit scoring contributes broadly to the internal risk assessment process of an institution, regulators have enforced more strict rules about model development, implementation, and validation to be followed by banks that wish to use their internal models in order to estimate capital requirements.

The remainder of the article is structured as follows. In the second section, we review some of the most relevant research related to credit scoring modeling methodologies. In the third section, following the model lifecycle structure, we analyze the main steps related to the model assessment, implementation, and validation process.

The statistical techniques used for credit scoring are based on the idea of discrimination between several groups in a data sample. These procedures originated in the 1930s and 1940s of the previous century [18]. At that time, some of the finance houses and mail order firms were having difficulties with their credit management. Decision whether to give loans or send merchandise to the applicants was made judgmentally by credit analysts. The decision procedure was nonuniform, subjective, and opaque; it depended on the rules of each financial house and on the personal and empirical knowledge of each single clerk. With the rising number of people applying for a credit card, it was impossible to rely only on credit analysts; an automated system was necessary. The first consultancy was formed in San Francisco by Bill Fair and Earl Isaac in the late 1950s.

After the first empirical solutions, academic interest on the topic rose and, given the lack of consumerlending figures, researchers focused their attention on small business clients. The seminal works in this field were Beaver [10] and Altman [1], who developed univariate and multivariate models, applying an MDA technique to predict business failures using a set of financial ratios.d

For many years thereafter, MDA was the prevalent statistical technique applied to the default prediction models and it was used by many authors [2, 3, 13, 15, 16, 24, 29]. However, in most of these studies, authors pointed out that two basic assumptions of MDA are often violated when applied to the default prediction problems.e Moreover, in MDA models, the standardized coefficients cannot be interpreted such as the slopes of a regression equation and, hence, do not indicate the relative importance of the different variables. Considering these MDA's problems, Ohlson [26], for the first time, applied the conditional logit model to the default prediction's study.f The practical benefits of the logit methodology are that it does not require the restrictive assumptions of MDA and allows working with disproportional samples. The performance of his models, in terms of classification accuracy, was lower than the one reported in the previous studies based on MDA, but he pointed out some reasons to prefer the logistic analysis.

From a statistical point of view, logit regression seems to fit well the characteristics of the default prediction problem, where the dependent variable is binary (default/nondefault) and with the groups being discrete, nonoverlapping, and identifiable. The logit model yields a score between 0 and 1, which conveniently can be transformed in the probability of default (PD) of the client. Lastly, the estimated coefficients can be interpreted separately as the importance or significance of each of the independent variables in the explanation of the estimated PD. After the work of Ohlson [26], most of the academic literature [5, 11, 19, 27, 30] used logit models to predict default.

Several other statistical techniques have been tested to improve the prediction accuracy of credit scoring models (e.g., linear regression, probit analysis, Bayesian methods, neural network, etc.), but the empirical results have never shown really significant benefits.

## **Credit Scoring Models Lifecycle**

As already mentioned, banks that want to implement the most advanced approach to calculate their minimum capital requirements (i.e., advanced internal rating based approach, A-IRB) are subject to more strict and common rules regarding how their internal models should be developed, implemented, and validated.g A standard model lifecycle has been designed to be followed by the financial institutions that will want to implement the A-IRB approach. The lifecycle of every model is divided into several phases (assessment, implementation, validation) and regulators have published specific requirements for each one of them. In this section, we describe the key aspects of each model's lifecycle phase.

#### *Model Assessment*

Credit scoring models are used to risk rank new or existing clients on the basis of the assumption that the future will be similar to the past. If an applicant or an existing client had a certain behavior in the past (e.g., paid back his debt or not), it is likely that a new applicant or client, with similar characteristics, will show the same behavior. As such, to develop a credit scoring model, we need a sample of past applicants or clients' data related to the same product as the one we want to use our scoring model for. If historical data from the bank are available, an empirical model can be developed. When banks do not have data or do not have a sufficient amount of data to develop an empirical model, an expert or a generic model is the most popular solution.h

When a data sample covering the time horizon necessary for the statistical analysis (usually at least 1 year) is available, the performance of the clients inside the sample can be observed. We define performance as the default or nondefault event associated with each client.i This binary variable is the dependent variable used to run the regression analysis. The characteristics of the client at the beginning of the selected period are the predictors.

Following the literature discussed in the second section, a conditional probability model, logit model, is commonly used by most banks to estimate the 1-year score through a range of variables by maximizing the log-likelihood function. This procedure is used to obtain the estimates of the parameters of the following logit model [20, 21]:

$$P_1(Xi) = \frac{1}{[1 + e^{-(B0 + B1Xi1 + B2Xi2 + \dots + BnXin)}]}$$
$$= \frac{1}{[1 + e^{-(Di)}]}$$
(1)

where *P*1*(Xi)* is the score given the vector of attributes *Xi*; *Bj* is the coefficient of attribute *j* (with *j* = 1*,...,n*); *B*<sup>0</sup> is the intercept; *Xij* is the value of the attribute *j* (with *j* = 1*,...,n*) for customer *I* ; and *Di* is the logit for customer *i*.

The logistic function implies that the logit score *P*<sup>1</sup> has a value in [0,1] interval and is increasing in *Di*. If *Di* approaches minus infinity, *P*<sup>1</sup> will be zero and if *Di* approaches plus infinity, *P*<sup>1</sup> will be one.

The set of attributes that are used in the regression depends on the type of model that is going to be developed. Application models, employed to decide whether to accept or reject an applicant, typically rely only on personal information about the applicant, given the fact that this is usually the only information available to the bank at that stage.j Behavioral and collection models include variables describing the status of the relationship between the client and the bank that may add significant prediction power to the model.k

Once the model is developed, it needs to be tested on a test sample to confirm the soundness of its results. When enough data are available, part of the development sample (hold-out sample) is usually kept for the final test of the model. However, an optimal test of the model would require investigating its performance also on an out-of-time and out-ofuniverse sample.

#### *Model Implementation*

The main advantage of scoring models is to allow banks to implement automated decision systems to manage their retail clients (private individuals and SMEs). When a large amount of applicants or clients is manually referred to credit analysts to check their information and apply policy rules, most of the benefits associated with the use of scoring models are lost. On the other hand, any scoring model has a "gray" area where it is not able to separate with an acceptable level of confidence between expected "good" clients and expected "bad" ones.l The main challenge for credit risk managers is to define the most appropriate and efficient thresholds (cutoff) for each scoring model.

In order to maximize the benefits of a scoring model, the optimal cutoff should be set taking into account the misclassification costs related to the type I and type II error rates as Altman *et al.* [2], Taffler [29], and Koh [23] point out. Moreover, we believe that the optimum cutoff value cannot be found without a careful consideration of each particular bank peculiarities (e.g., tolerance for risk, profit–loss objectives, recovery process costs and efficiency, possible marketing strategies). Today, the most advanced banks set cutoffs using profitability analyses at account level.

The availability of sophisticated IT systems has significantly broadened the number of strategies that can be implemented using credit scoring models. The most efficient banks are able to follow the lifecycle of any client, from the application to the end of the relationship, with monthly updated scores calculated by different scorecards related to the phase of the credit cycle where the client is located (e.g., origination, account maintenance, collection, write off). Marketing campaigns (e.g., cross-selling, up-selling), automated limit changes, early collection strategies, and shadow limit management are some of the activities that are fully driven by the output of scoring models in most banks.

#### *Model Validation*

Banks that have adopted or are willing to adopt the Basel II IRB-advanced approach are required to put in place a regular cycle of model validation that should include at least monitoring of the model performance and stability, reviewing of the model relationships, and testing of model outputs against outcomes (i.e., backtesting).m

Considering the relatively short lifecycle of credit scoring models due to the high volatility of retail markets, their validation has always been completed by banks. Basel II has only given to it a more official shape, prescribing that the validation should be undertaken by a team independent from the one that has developed the models.

Stability and performance (i.e., prediction accuracy) are extremely important information about the quality of the scoring models. As such, they should be tracked and analyzed at least monthly by banks, regardless of the validation exercise. As we have discussed above, often scoring models are used to generate a considerable amount of automated decisions that may have a significant impact on the banking business. Even small changes in the population's characteristics can substantially affect the quality of the models, creating undesired selection bias.

In the literature, we have found several indexes that have been used to assess the performance of the models. The simple type I and type II error rates that quantify the accuracy of each model in correctly classifying defaulted and nondefaulted observations have been the first measures to be applied to scoring models. More recently, the accuracy ratio (AR) and the Gini index have become the most popular measures (see [17] for further details).

Backtesting and benchmarking are an essential part of the scoring models' validation. With the backtesting, we evaluate the calibration and discrimination of a scoring model. Calibration refers to the mapping of a score to a quantitative risk measure (e.g., PD). A scoring model is considered well calibrated if the (*ex ante*) estimated risk measures (PD) deviate only marginally from what has been observed *ex post* (actual default rate per score band). Discrimination measures how well the scoring model provides an ordinal ranking of the risk profile of the observations in the sample; for example, in the credit risk context, discrimination measures to what extent defaulters were assigned low scores and nondefaulters high scores.

Benchmarking is another quantitative validation method that aims at assessing the consistency of the estimated scoring models with those obtained using other estimation techniques and potentially using other data sources. This analysis may be quite difficult to perform for retail portfolios, given the lack of generic benchmarks in the market.<sup>n</sup>

Lastly, we would like to point out that Basel II specifically requires senior management to be fully involved and aware of the quality and performance of all the scoring models utilized in the daily business (see [9], par. 438, 439, 660, 718 (LXXVI), 728).

## **End Notes**

a*.* Risk appetite is defined as the maximum risk the bank is willing to accept in executing its chosen business strategy, to protect itself against events that may have an adverse impact on its profitability, the capital base, or share price (*see* **Economic Capital Allocation**; **Economic Capital**).

b*.* Recently, several studies [4, 12] have shown the importance for banks of classifying SMEs as retail clients and applying credit scoring models developed specifically for them.

c*.* The default definition may be significantly different by bank and type of client. The new Basel Capital Accord [9] (par.452) has given a common definition of default (i.e., 90 days past due over 1-year horizon) that is consistently used by most banks today.

d*.* The original *Z*-score model Altman [1] used five ratios: working capital/total assets, retained earnings/total assets, EBIT/total assets, market value equity/BV of total debt, and sales/total assets.

e*.* MDA is based on two restrictive assumptions: (i) the independent variables included in the model are multivariate normally distributed and (ii) the group dispersion matrices (or variance–covariance matrices) are equal across the failing and the nonfailing group. See [6, 22, 25] for further discussions about this topic.

f*.* Zmijewski [31] was the pioneer in applying probit analysis to predict default, but, until now, logit analysis has given better results in this field.

g*.* The new Basel Capital Accord offers financial institutions the possibility to choose between the standardized and the advanced approach to calculate their capital requirements. Only the latter requires banks to use their own internal risk assessment tools to quantify the inputs of the capital requirements formulas (i.e., PD and loss given default).

h*.* Expert scorecards are based on subjective weights assigned by an analyst, whereas generic scorecards are developed on pooled data from other banks operating in the same market. For a more detailed analysis of the possible solutions that banks can consider when not enough historical data is available, see [28].

i*.* See end note (b).

j*.* The most common application variables used are sociodemographic information about the applicants (e.g., marital status, residence type, time at current address, type of work, time at current work, flag phone, number of children, installment on income, etc.). When a credit bureau is available in the market, the information that can be obtained related to the behavior of the applicant with other financial institutions is an extremely powerful variable to be used in application models.

k*.* Variables used in behavioral and collection scoring models are calculated and updated at least monthly. As such, the correlation between these variables and the default event is significantly high. Examples of behavioral variables are as follows: the number of missed installments (current, max last 3/6/12 months, or ever), number of days in excess (current, max last 3/6/12 months, or ever), outstanding on limit, and so on. Behavioral score can be calculated at facility and customer level (when several facilities are related to the same client).

l*.* Depending on the chosen binary-dependent variable, "good" and "bad" will have different meanings. For credit risk models, these terms are usually associated with nondefaulted and defaulted clients, respectively.

m*.* See par. 417 and 718 (XCix) of the new Basel Capital Accord [7–9] (*see also* **Model Validation**; **Backtesting**). n*.* Recently, rating agencies (e.g., Standard & Poor's and Moody's) and credit bureau providers (e.g., Fair Isaac and Experian) have started to offer services of benchmarking for retail scoring models. For more details about backtesting and benchmarking techniques, see [14].

## **References**

- [1] Altman, E.I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, *Journal of Finance* **23**(4), 589–611.
- [2] Altman, E.I., Haldeman, R.G. & Narayanan, P. (1977). Zeta-analysis. A new model to identify bankruptcy risk of corporations, *Journal of Banking and Finance* **1**, 29–54.
- [3] Altman, E.I., Hartzell, J. & Peck, M. (1995). *A Scoring System for Emerging Market Corporate Debt*. Salomon Brothers Emerging Markets Bond Research, May 15.
- [4] Altman, E.I. & Sabato, G. (2005). Effects of the new Basel capital accord on bank capital requirements for SMEs, *Journal of Financial Services Research* **28**(1/3), 15–42.
- [5] Aziz, A., Emanuel, D.C. & Lawson, G.H. (1988). Bankruptcy prediction – an investigation of cash flow based models, *Journal of Management Studies* **25**(5), 419–437.
- [6] Barnes, P. (1982). Methodological implications of nonnormality distributed financial ratios, *Journal of Business Finance and Accounting* **9**(1), 51–62.
- [7] Basel Committee on Banking Supervision (2005). *Studies on the Validation of Internal Rating Systems*. Working paper 14, www.bis.org.
- [8] Basel Committee on Banking Supervision (2005). *Update on Work of the Accord Implementation Group Related to Validation Under the Basel II Framework* . Newsletter 4, www.bis.org.
- [9] Basel Committee on Banking Supervision (2006). *International Convergence of Capital Measurement and Capital Standards*. www.bis.org.
- [10] Beaver, W. (1967). Financial ratios predictors of failure, *Journal of Accounting Research* **4**, 71–111.

- [11] Becchetti, L. & Sierra, J. (2003). Bankruptcy risk and productive efficiency in manufacturing firms, *Journal of Banking and Finance* **27**(11), 2099–2120.
- [12] Berger, A.N. & Frame, S.W. (2007). Small business credit scoring and credit availability, *Journal of Small Business Management* **45**(1), 5–22.
- [13] Blum, M. (1974). Failing company discriminant analysis, *Journal of Accounting Research* **12**(1), 1–25.
- [14] Castermans, G., Martens, D., Van Gestel, T., Hamers, B. & Baesens, B. (2007). An overview and framework for PD backtesting and benchmarking, *Proceedings of Credit Scoring and Credit Control X*, Edinburgh, Scotland.
- [15] Deakin, E. (1972). A discriminant analysis of predictors of business failure, *Journal of Accounting Research* **10**(1), 167–179.
- [16] Edmister, R. (1972). An empirical test of financial ratio analysis for small business failure prediction, *Journal of Financial and Quantitative Analysis* **7**(2), 1477–1493.
- [17] Engelmann, B., Hayden, E. & Tasche, D. (2003). Testing rating accuracy, *Risk* **16**(1), 82–86.
- [18] Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems, *Annals of Eugenic* **7**, 179–188.
- [19] Gentry, J.A., Newbold, P. & Whitford, D.T. (1985). Classifying bankrupt firms with funds flow components, *Journal of Accounting Research* **23**(1), 146–160.
- [20] Gujarati, N.D. (2003). *Basic Econometrics*, 4th Edition, McGraw-Hill, London.
- [21] Hosmer, D.W. & Lemeshow, S. (2000). *Applied Logistic Regression*, 2nd Edition, John Wiley & Sons, New York.
- [22] Karels, G.V. & Prakash, A.J. (1987). Multivariate normality and forecasting of business bankruptcy, *Journal of Business Finance & Accounting* **14**(4), 573–593.
- [23] Koh, H.C. (1992). The sensitivity of optimal cutoff points to misclassification costs of Type I and Type II errors in the going-concern prediction context, *Journal of Business Finance & Accounting* **19**(2), 187–197.
- [24] Lussier, R.N. (1995). A non-financial business success versus failure prediction model for young firms, *Journal of Small Business Management* **33**(1), 8–20.
- [25] Mc Leay, S. & Omar, A. (2000). The sensitivity of prediction models tot the non-normality of bounded an unbounded financial ratios, *British Accounting Review* **32**, 213–230.
- [26] Ohlson, J. (1980). Financial ratios and the probabilistic prediction of bankruptcy, *Journal of Accounting Research* **18**(1), 109–131.
- [27] Platt, H.D. & Platt, M.B. (1990). Development of a class of stable predictive variables: the case of bankruptcy prediction, *Journal of Business Finance & Accounting* **17**(1), 31–51.
- [28] Sabato, G. (2008). Managing credit risk for retail lowdefault portfolios, in *Credit Risk: Models, Derivatives and Management*, N. Wagner, ed., Financial Mathematics Series, Chapman & Hall/CRC.
- [29] Taffler, R.J. & Tisshaw, H. (1977). Going, going, gone – four factors which predict, *Accountancy* **88**(1083), 50–54.

- [30] Zavgren, C. (1983). The prediction of corporate failure: the state of the art, *Journal of Accounting Literature* **2**, 1–37.
- [31] Zmijewski, M.E. (1984). Methodological issues related to the estimation of financial distress prediction models, *Journal of Accounting Research* **22**, 59–86.

## **Further Reading**

Taffler, R.J. (1982). Forecasting company failure in the UK using discriminant analysis and financial ratio data, *Journal of the Royal Statistical Society* **145**(3), 342–358.

**Related Articles**

**Backtesting**; **Credit Rating**; **Credit Risk**; **Internalratings-based Approach**; **Model Validation**.

GABRIELE SABATO
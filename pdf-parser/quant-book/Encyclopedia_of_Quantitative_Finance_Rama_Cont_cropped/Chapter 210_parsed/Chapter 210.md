# **Structured Finance Rating Methodologies**

Rating agencies are among the most important players in the securitization market and they have contributed significantly in the development of the market. Rating agencies have the expertise and access to necessary information to rate the multiple tranches of structured finance transactions. Their ratings are independent assessments of the credit and noncredit risks in a transaction. Investors who do not have the expertise and the required information to assess the credit quality of the issued structured finance products can use the ratings in their investment decision process. In addition, rating agencies provide transparency and increase the effectiveness in the securitization market. Finally, rating agencies have contributed significantly to the rapid development of the securitization market in the recent years.

Rating agencies have developed methodologies for structured finance ratings, which are significantly more complex than those they use to rate traditional instruments. Quantitative modeling is essential for rating structured finance securities. All three major agencies use a three-step rating process to model the assets and liabilities of a transaction. Although the rating methodologies across asset classes share the same basic principles, the modeling differs across asset classes and jurisdictions.

We examine the asset-backed securities (ABS) (*see* **Securitization**) and collateralized debt obligation (CDO) (*see* **Collateralized Debt Obligations (CDO)**) rating methodologies applied in the securitization market ([5, 6] for an introduction to securitization process). We focus on the quantitative aspects of the modeling that the major rating agencies apply in order to rate ABS and CDO tranches with a discussion on the importance and uses of the ratings in the securitization market.

## **Rating Methodologies**

Rating agencies update their rating methodologies regularly to increase the accuracy and to incorporate new structures that appear in the market. For previous reviews on rating methodologies, see [1, 7]. Although the rating methodologies differ across rating agencies, all three major agencies, that is, Fitch, Moody's, and Standard & Poor's follow a threestep rating approach. The basic principles of this three-step approach are applied to structured finance transactions. In general, the three steps of a rating process are the following:

- 1. calculation of the default/loss distribution of the portfolio of assets;
- 2. generation of the asset cash flows using the portfolio loss characteristics; and
- 3. generation of the liability cash flows using the asset cash flows.

However, the modeling of each of the above steps can be very different depending on the type of structure (synthetic or cash) or the type of collateral (such as auto loans, mortgages, bonds, or others). The first two steps focus on the asset side and the third step on the liabilities side of the transaction. The next two sections discuss the basic principles of the assets and liabilities modeling that the agencies use to determine structured finance ratings.

#### *Asset Side Modeling*

In the first step of their respective methodologies, the agencies assess the credit risk in the underlying asset portfolio. They do so by modeling the default/loss distribution of the portfolio. The three main inputs driving these models are the following:

- 1. *Term structure of probabilities of default* (PDs) of each individual obligor in the portfolio across the life of the transaction.
- 2. *Recovery rates* (or losses-given-default (LGD), which is equal to one minus the recovery rate in the event of default).
- 3. *Asset correlations* within the portfolio, which determine default correlations and thus the likelihood of occurrence of joint defaults in a given period.

The main outputs of the credit risk assessment models are the loss characteristics of the portfolio, that is, the portfolio loss and default distributions.

Typical ABS portfolios usually contain large, granular, and homogeneous pools of assets. Hence, the systematic risk factors are typically the primary drivers of the default distribution of the ABS portfolios. Moreover, model inputs, such as the default probabilities, the recovery rates, and the correlation assumptions, are usually estimated on a portfolio level. On the other hand, CDOs are typically nongranular portfolios of a small number of assets. Thus, the idiosyncratic risk is much more important in CDOs than the ABS portfolios. As a result of this, one has to carefully consider each obligor's individual probability of default and recovery rates.

As of February 2008, for rating CDO transactions, Standard and Poor's [10, 20] and Fitch [11, 14, 18] use very similar Monte Carlo simulation methodologies to calculate the loss/default distribution of CDO portfolios. Both the agencies use structural form models, where an obligor defaults if its assets value falls below its liabilities (also referred to as *default threshold*); see [16]. In these models, copulas are used to model the joint defaults of the obligors in the portfolio. In February 2007, Moody's introduced a Monte Carlo simulation approach [15] similar to the other agencies' methodologies to compute the expected loss for static synthetic CDOs and CDOs-squared. As of February 2008, Moody's continues to use the binomial expansion technique (BET) [3, 8, 21] for assessing the credit risk of other types of CDOs. For a comparison of the BET against the copula models, see [9]. In spite of the similarities in the agencies' methodologies, there are also some disparities in their approaches. Specifically, there are differences in the correlation structures and the recovery assumptions that the rating agencies employ.

The approaches that the rating agencies apply to all the other ABS transactions differ across asset classes and jurisdictions. These approaches are described next as of February 2008. Fitch uses a simulation-based methodology [2] appropriate for large, granular ABS portfolios composed of consumer and auto loans or leases for the European transactions, whereas it employs an actuarial approach to rate US ABS transactions; for example, it uses historical default rates to specify the credit risk of such portfolios. The key difference between the CDO and ABS simulation approaches is that the default probabilities inputs in the latter are specified at a pool level and not at an asset level. Fitch uses similar simulationbased methodology to the one that is used for CDOs in order to calculate the loss distributions of commercial mortgage-backed securities (CMBS) portfolios [4]. Fitch rates residential mortgage-backed securities

(RMBS) transactions by applying standard criteria at a country level. Historical information on a loan-byloan level as well as on the level of the originator is used to arrive at probability defaults at a loan-byloan level before aggregating to pool level. Moody's applies an actuarial approach to calculate the loss distribution in most ABS transactions. It analyzes historical data on pools of loans provided by the originators to calculate the expected loss and the volatility of the losses for the underlying asset portfolio. Once expected losses and volatility have been estimated, a lognormal distribution is used to approximate the loss distribution of the portfolio [13]. Standard and Poor's also estimates the default probability of ABS portfolio using historical default rates provided by the originator. Standard and Poor's estimates the probability of default of an RMBS portfolio at a country level [12]. More specifically, the agency estimates the defaults in a portfolio and the loss severity in a portfolio by calculating the weighted average foreclosure frequency and the weighed average loss severity. These estimates increase for the higher stressed ratings scenarios.

The loss characteristics of the asset portfolio along with the recovery rate and interest rate movement assumptions are the main inputs in the model, which generates the cash flows of the assets. In this second step, cash flows of the underlying assets are generated for different stress scenarios, which correspond to different ratings. Note that for many synthetic CDOs usually there is no need to measure any impact on the credit enhancement levels *via* the cash flow model. For these CDOs, the credit enhancement levels can be directly determined from the loss distribution of the underlying credit portfolio [14].

#### *Liabilities Side Modeling*

The asset cash flows and the default assumptions that have been determined in the first two steps of the rating process are the key inputs to the liabilities cash flow model. The purpose of the cash flow model is to determine whether the various tranches of the liabilities receive the principal and interest payments in accordance with the terms of the transaction. In order to achieve this aim, the cash flow modeling usually takes into account the following noncredit risk factors [1, 19], which are known to affect the performance of the transaction:

- 1. *Capital structure of the transaction, principal, and interest waterfall triggers*, for example, the mechanics through which the assets cash flows are allocated to pay the tranches and all the other transaction fees and expenses.
- 2. *Market risks* such as prepayment, interest rate, currency, and potential basis risks.
- 3. *Operational and administrative risks*, that is, the performance risks which are related to the participants in the transaction such as asset managers and servicers.
- 4. *Counterparty risk*, that is, the performance risks of credit enhancement providers and hedge counterparties.
- 5. *Legal and regulatory risks* that may rise from imperfect isolation of the securitized assets from the bankruptcy risk of the special purpose vehicle (SPV) under the applicable legal and regulatory framework.

The cash flow modeling procedures differ across the asset classes. Also, cash flow modeling is based heavily on the distinct characteristics of each specific transaction. Thus, in many instances, agencies apply deal-specific cash flow modeling. Usually, the ABS structures are more complicated than those of CDOs and thus cash flow modeling is, in general, the most important part of the ABS rating process. For more technical details on cash flow modeling, refer to [17].

## **References**

- [1] BIS (2005). *The Role of Ratings in Structured Finance Issues and Implications*, Committee on the Global Financial System.
- [2] Bund, S., Dyke, H., Holter, M., Weintraub, H., ¨ Akhavein, J., Ramachandran, B. & Cipolla, A. (2006). *European Consumer ABS Rating Criteria*, Fitch Ratings, 11 October.
- [3] Cifuentes, A. & O'Connor, G. (1996). *The Binomial Expansion Method Applied to CBO/CLO Analysis*. Moody's Special Report, 13 December.
- [4] Dominedo, G. & Currie, A. (2007). *Criteria for European CMBS Analysis*, Fitch Ratings, 12 September.
- [5] Fabozzi, F. & Choudry, M. (2004). *The Handbook of European Structured Financial Products*, Fabozzi Series, Wiley Finance.
- [6] Fabozzi, F., Davis, H. & Choundry, M. (2006). *Introduction to Structured Finance*, Frank J. Fabozzi Series, Wiley.

- [7] Fender, I. & Kiff, J. (2004). *CDO Rating Methodology: Some Thoughts on Model Risk and its Implications*. BIS Working paper, November.
- [8] Garcia, J., Dewyspelaere, T., Langendries, R., Leonard, L. & Van Gestel, T. (2003). *On Rating Cash Flow CDO's using BET Technique*, Dexia Group. Working paper version April 17th.
- [9] Garcia, J., Dwyspelaere, T., Leonard, L., Alderweireld, T. & Van Gestel, T. (2005). *Comparing BET and Copulas for Cash Flows CDO's*, Dexia Group, available in www.defaultrisk.com January 31.
- [10] Gikes, K., Jobst, N. & Watson, B. (2005). *CDO Evaluator Version 3.0: Technical Document*, 19-December-2005.
- [11] Jebjerg, L., Carter, J., Linden, A., Hrvatin, R., Zelter, J., Cunningham, T., Carroll, D. & Hardee, R. (2006). *Global Rating Criteria for Portfolio Credit Derivatives (Synthetic CDOs)*. FitchRatings, 11 October.
- [12] Johnstone, V., McCabe, S. & Kane, B. (2003). *Cash Flow Criteria for RMBS Transactions*. 20-November-2003.
- [13] Kanthan, K., DiRienz, M., Eisbruck, J., Stesney, L., Weill, N. & Hemmerling, B. (2007). *Moody's Approach to Rating US Auto Loan-Backed Securities*. Moody's, 29 June.
- [14] Koo, M., Cromartie, J. & Vedova, P. (2006). *Global Rating Criteria for Collateralised Debt Obligations*, FitchRatings. 18 October 2006.
- [15] Marjolin, B., Lassalvy, L. & Sieler, J. (2007). *Moody's Approach to Modelling Exotic Synthetic CDOs with CDOROM* . Moody's, 1 February.
- [16] Merton, R. (1974). On the pricing of corporate debt: the risk structure of interest rates, *Journal of Finance* **29**, 449–470.
- [17] Tick, E. (2007). *Structure Finance Modeling with Object-oriented VBA*, Wiley Finance.
- [18] Wilgen, A. (2006). *Global Rating Criteria for Cash Flow Collateralised Debt Obligations*, FitchRatings. October.
- [19] Wong, C., Gills, T. & Michaux, F. (2007). *Criteria: Principles-based Rating Methodology for Global Structured Finance Securities*, Standard & Poor's. 29-May.
- [20] Xie, M. & Witt, G. (2002). *Global Cash Flow and Synthetic CDO Criteria*, Standard & Poor's. 21-March.
- [21] Xie, M. & Witt, G. (2005). *Moody's Modeling Approach to Rating Structured Finance Cash Flow CDO Transactions*. 26 September.

## **Related Articles**

**ABS Indices**; **CDO Square**; **Collateralized Debt Obligations (CDO)**; **Credit Risk**; **Rating Transition Matrices**; **Securitization**.

> AHMET E. KOCAGIL & VASILEIOS PAPATHEODOROU
![](_page_0_Picture_0.jpeg)

 $\bullet$  ffective risk management in a trading operation is as important as the signals that motivate the trades. A well-designed and executed  $\bullet$  risk management function is key to sustainable profitability in all organizations. This chapter presents the leading approaches for managing risk in high-frequency trading operations that are compliant with Basel II risk management standards. $^{1}$ 

As with any business decision, the process of building a risk management system involves several distinct steps:

- 1. First, the overall organization-wide goals of risk management should be clearly defined.
- 2. Next, potential risk exposure should be measured for each proposed trading strategy and the overall portfolio of the trading operation.
- 3. Based on the goals and risk parameters determined in the two preceding steps, a risk management system is put in place to detect abnormal risk levels and to dynamically manage risk exposure.

The following sections in turn address each of these steps.

<sup>&</sup>lt;sup>1</sup>Basel II is the set of recommendations on risk management in financial services issued by the Basel Committee on Banking Supervision in June 2004 with the goal of promoting economic stability.

## DETERMINING RISK MANAGEMENT GOALS

The primary objective of risk management is to limit potential losses. Competent and thorough risk management in a high-frequency setting is especially important, given that large-scale losses can mount quickly at the slightest shift in behavior of trading strategies. The losses may be due to a wide range of events, such as unforeseen trading model shortcomings, market disruptions, acts of God (earthquakes, fire, etc.), compliance breaches, and similar adverse conditions.

Determining organizational goals for risk management is hardly a trivial endeavor. To effectively manage risk, an organization first needs to create clear and effective processes for measuring risk. The risk management goals, therefore, should set concrete risk measurement methodologies and quantitative benchmarks for risk tolerance associated with different trading strategies as well as with the organization as a whole. Expressing the maximum allowable risk in numbers is difficult, and obtaining organization-wide agreement on the subject is even more challenging, but the process pays off over time through quick and efficient daily decisions and the resulting low risk.

A thorough goal-setting exercise should achieve senior management consensus with respect to the following questions:

- What are the sources of risk the organization faces?
- What is the extent of risk the organization is willing to undertake? What risk/reward ratio should the organization target? What is the minimum acceptable risk/reward ratio?
- What procedures should be followed if the acceptable risk thresholds are breached?

The sources of risk should include the risk of trading losses, as well as credit and counterparty risk, liquidity risk, operational risk, and legal risk. The risk of trading losses, known as market risk, is the risk induced by price movements of all market securities; credit and counterparty risk addresses the ability and intent of trading counterparties to uphold their obligations; liquidity risk measures the ability of the trading operation to quickly unwind positions; operational risk enumerates possible financial losses embedded in daily trading operations; and legal risk refers to all types of contract frustration. A successful risk management practice identifies risks pertaining to each of these risk categories.

Every introductory finance textbook notes that higher returns, on average, are obtained with higher risk. Yet, while riskier returns are on average higher across the entire investing population, some operations with risky exposures obtain high gains and others suffer severe losses. A successful risk management process should establish the risk budget that the operation is willing to take in the event that the operation ends up on the losing side of the equation. The risks should be quantified as worst-case scenario losses tolerable per day, week, month, and year and should include operational costs, such as overhead and personnel costs. Examples of the worstcase losses to be tolerated may be 10 percent of organizational equity per month or a hard dollar amount—for example, \$150 million per fiscal year.

Once senior management has agreed to the goals of risk management, it becomes necessary to translate the goals into risk processes and organizational structures. Processes include development of a standardized approach for review of individual trading strategies and the trading portfolio as a whole. Structures include a risk committee that meets regularly, reviews trading performance, and discusses the firm's potential exposure to risks from new products and market developments.

The procedures for dealing with breaches of established risk management parameters should clearly document step-by-step actions. Corporate officers should be appointed as designated risk supervisors responsible to follow risk procedures. The procedures should be written for dealing with situations not if, but when a risk breach occurs. Documented step-bystep action guidelines are critical; academic research has shown that the behavior of investment managers becomes even riskier when investment managers are incurring losses. See, for example, Kahneman and Teversky (1979), Kouwenberg and Ziemba (2007), and Carpenter (2000). Previously agreed-on risk management procedures eliminate organizational conflicts in times of crisis, when unified and speedy action is most necessary.

The following sections detail the quantification of risk exposure for different types of risk and document the best practices for ongoing oversight of risk exposure.

## **MEASURING RISK**

While all risk is quantifiable, the methodology for measuring risk depends on the type of risk under consideration. The Basel Committee on Banking Supervision2, an authority on risk management in financial services, identifies the following types of risk affecting financial securities:

- **1.** Market risk—induced by price movements of market securities
- **2.** Credit and counterparty risk—addresses the ability and intent of trading counterparties to uphold their obligations

<sup>2</sup>More information on the Basel Committee for Banking Supervision can be found by visiting http://www.bis.org/bcbs/ on the Internet.

- 3. Liquidity risk—the ability of the trading operation to quickly unwind positions
- 4. Operational risk—the risk of financial losses embedded in daily trading operations
- 5. Legal risk—the risk of litigation expenses

All current risk measurement approaches fall into four categories:

- Statistical models
- Scalar models
- Scenario analysis
- Causal modeling

Statistical models generate predictions about worst-case future conditions based on past information. The Value-at-Risk (VaR) methodology is the most common statistical risk measurement tool, discussed in detail in the sections that focus on market and liquidity risk estimation. Statistical models are the preferred methodology of risk estimation whenever statistical modeling is feasible.

Scalar models establish the maximum foreseeable loss levels as percentages of business parameters, such as revenues, operating costs, and the like. The parameters can be computed as averages of several days, weeks, months, or even years of a particular business variable, depending on the time frame most suitable for each parameter. Scalar models are frequently used to estimate operational risk.

Scenario analysis determines the base, best, and worst cases for the key risk indicators (KRIs). The values of KRIs for each scenario are determined as hard dollar quantities and are used to quantify all types of risk. Scenario analysis is often referred to as the "stress test."

Causal modeling involves identification of causes and effects of potential losses. A dynamic simulation model incorporating relevant causal drivers is developed based on expert opinions. The simulation model can then be used to measure and manage credit and counterparty risk, as well as operational and legal risks. The following sections discuss the measurement of different types of risk.

## **Measuring Market Risk**

Market risk refers to the probability of and the expected value of a decrease in market value due to market movements. Market risk is present in every trading system and must be competently and thoroughly estimated.

Market risk is the risk of loss of capital due to an adverse price movement in any securities—equities, interest rates, or foreign exchange. Many securities can be affected by changes in prices of other, seemingly unrelated, securities. The capital invested in equity futures, for example, will be affected by price changes in equities underlying the futures as well as by the changes in interest rates used to value the time component of the futures price. If the capital originates and is settled in EUR, but the investment is placed into equity futures in the U.S. market, then EUR/USD price changes will also affect the value of the portfolio.

To accurately estimate the risk of a given trading system, it is necessary to have a reasonably complete idea of the returns generated by the trading system. The returns are normally described in terms of distributions. The preferred distributions of returns are obtained from running the system on live capital. The back test obtained from running the model over at least two years of tick data can also be used as a sample distribution of trade returns. However, the back-test distribution alone may be misleading, because it may fail to account for all the extreme returns and hidden costs that occur when the system is trading live. Once the return distributions have been obtained, the risk metrics are most often estimated using statistical models and VaR in particular.

The concept of Value-at-Risk (VaR) has by now emerged as the dominant metric in market risk management estimation. The VaR framework spans two principal measures—VaR itself and the expected shortfall (ES). VaR is the value of loss in case a negative scenario with the specified probability should occur. The probability of the scenario is determined as a percentile of the distribution of historical scenarios that can be strategy or portfolio returns. For example, if the scenarios are returns from a particular strategy and all the returns are arranged by their realized value in ascending order from the worst to the best, then the 95 percent VaR corresponds to the cutoff return at the lowest fifth percentile. In other words, if 100 sample observations are arranged from the lowest to the highest, then VaR corresponds to the value of the fifth lowest observation.

The expected shortfall (ES) measure determines the average worstcase scenario among all scenarios at or below the prespecified threshold. For example, a 95 percent ES is the average return among all returns at the 5 percent or lower percentile. If 100 sample observations are arranged from the lowest to the highest, the ES is the average of observations 1 through 5. Figure 17.1 illustrates the concepts of VaR and ES.

An analytical approximation to true VaR can be found by parameterizing the sample distribution. The parametric VaR assumes that the observations are distributed in a normal fashion. Specifically, the parametric VaR assumes that the 5 percent in the left tail of the observations fall at µ − 1.65σof the distribution, where µ and σ represent the mean and standard deviation of the observations, respectively. The 95 percent parametric VaR is then computed as µ − 1.65σ, while the 95 percent parametric ES is

![](_page_5_Figure_1.jpeg)

**FIGURE 17.1** The 99 percent VaR (α = 1 percent) and 95 percent VaR (α = 5 percent) computed on the sample return population.

computed as the average of all distribution values from –∞ to µ − 1.65σ. The average can be computed as an integral of the distribution function. Similarly, the 99 percent parametric VaR is computed as µ − 2.33σ, while the 99 percent parametric ES is computed as the average of all distribution values from −∞ to µ − 1.65σ. The parametric VaR is an approximation of the true VaR; the applicability of the parametric VaR depends on how close the sample distribution resembles the normal distribution. Figure 17.2 illustrates this idea.

While the VaR and ES metrics summarize the location and the average of many worst-case scenarios, neither measure indicates the absolute worst scenario that can destroy entire trading operations, banks, and markets. Most financial return distributions have fat tails, meaning that the very extreme events lie beyond normal distribution bounds and can be truly catastrophic.

The limitations of VaR methodology have hardly been a secret. In a *New York Times* article published on January 2, 2009, David Einhorn, the

![](_page_5_Figure_6.jpeg)

**FIGURE 17.2** The 95 percent parametric VaR corresponds to µ−1.65σ of the distribution, while the 99 percent parametric VaR corresponds to µ−2.33σ of the distribution.

founder of the hedge fund Greenlight Capital, stated that VaR was "relatively useless as a risk-management tool and potentially catastrophic when its use creates a false sense of security among senior managers and watchdogs. This is like an air bag that works all the time, except when you have a car accident." The article also quoted Nassim Nicholas Taleb, the bestselling author of *The Black Swan*, as calling VaR metrics "a fraud." Jorion (2000) points out that the VaR approach both presents a faulty measure of risk and actively pushes strategists to bet on extreme events. Despite all the criticism, VaR and ES have been mainstays of corporate risk management for years, where they present convenient reporting numbers.

To alleviate the shortcomings of the VaR, many quantitative outfits began to parameterize extreme tail distributions to develop fuller pictures of extreme losses. Once the tail is parameterized based on the available data, the worst-case extreme events can be determined analytically from distributional functions, even though no extreme events of comparable severity were ever observed in the sample data.

The parameterization of the tails is performed using the extreme value theory (EVT). EVT is an umbrella term spanning a range of tail modeling functions. Dacorogna et al. (2001) note that all fat-tailed distributions belong to the family of Pareto distributions. A Pareto distribution family is described as follows:

$$G(x) = \begin{cases} 0 & x \le 0\\ \exp(-x^{-\alpha}) & x > 0, \alpha > 0 \end{cases}$$
(17.1)

where the tail index α is the parameter that needs to be estimated from the return data. For raw security returns, the tail index varies from financial security to financial security. Even for raw returns of the same financial security, the tail index can vary from one quoting institution to another, especially for really high-frequency estimations.

When the tail index α is determined, we can estimate the magnitude and probability of all the extreme events that may occur, given the extreme events that did occur in the sample. Figure 17.3 illustrates the process of using tail parameterization:

- **1.** Sample return observations obtained from either a back test or live results are arranged in ascending order.
- **2.** The tail index value is estimated on the bottom 5 percentile of the sample return distribution.
- **3.** Using the distribution function obtained with the tail index, the probabilities of observing the extreme events are estimated. According to the tail index distribution function, a –7 percent return would occur with a probability of 0.5 percent, while a return of –11 percent would register with a probability of 0.001 percent.

![](_page_7_Figure_1.jpeg)

**FIGURE 17.3** Using tail index parameterization to predict extreme events.

The tail index approach allows us to deduce the unobserved return distributions from the sample distributions of observed returns. Although the tail index approach is useful, it has its limitations. For one, the tail index approach "fills in" the data for the observed returns with theoretical observations; if the sample tail distribution is sparse (and it usually is), the tail index distribution function may not be representative of the actual extreme returns. In such cases, a procedure known as "parametric bootstrapping" may be applicable.

Parametric bootstrap simulates observations based on the properties of the sample distribution. The technique "fills in" unobserved returns based on observed sample returns. The parametric bootstrap process works as follows:

- **1.** The sample distribution of observed returns delivered by the manager is decomposed into three components using a basic market model:
  - **a.** The manager's skill, or alpha
  - **b.** The manager's return due to the manager's portfolio correlation with the benchmark
  - **c.** The manager's idiosyncratic error

The decomposition is performed using the standard market model regression:

$$R_{i,t} = \alpha_i + \beta_{i,x} R_{x,t} + \varepsilon_t \tag{17.2}$$

where *Ri,t* is the manager's raw return in period *t*, *Rx,t* is the raw return on the chosen benchmark in period *t*, α*<sup>i</sup>* is the measure of the manager's money management skill or alpha, and β*i,x* is a measure of the dependency of the manager's raw returns on the benchmark returns.

| Observation<br>No. | $R_{i,t}$ | $\mathbf{R}_{x,t}$ | ^<br>$\alpha_i$ | $\hat{\beta}_{i,x} R_{x,t}$ | $\varepsilon_{i,t}$ |
|--------------------|-----------|--------------------|-----------------|-----------------------------|---------------------|
|                    | 0.015     | $-0.001$           | 0.002           | 0.00005                     | 0.01295             |
| 2                  | 0.0062    | 0.0034             | 0.002           | -0.00017                    | 0.00403             |

**Examples of Generated Bootstrap Components TABLE 17.1** 

- **2.** Once parameters  $\hat{\alpha}_i$  and  $\hat{\beta}_{i,x}$  are estimated using equation (17.2), three pools of data are generated: one for  $\hat{\alpha}_i$  (constant for given manager, benchmark, and return sample),  $\hat{\beta}_{i,x}R_{x,t}$ , and  $\varepsilon_{i,t}$ .<sup>3</sup> For example, if  $\hat{\alpha}_i$ and  $\hat{\beta}_{i,x}$  were estimated to be 0.002 and -0.05, respectively, then the component pools for a sample of raw returns and benchmarked returns may look as shown in Table  $17.1$ .
- 3. Next, the data is resampled as follows:
  - **a.** A value  $\varepsilon_{i,t}^S$  is drawn at random from the pool of idiosyncratic errors,  $\{\varepsilon_{i\,t}\}.$
  - **b.** Similarly, a value  $\hat{\beta}_{i,x}R_{r,t}^S$  is drawn at random from the pool of  $\{\beta_{i} R_{x t}\}.$
  - **c.** A new sample value is created as follows:

$$\hat{R}_{i,t}^S = \hat{\alpha}_i + \hat{\beta}_{i,x} R_{x,t}^S + \varepsilon_t^S \tag{17.3}$$

**d.** The sampled variables  $\varepsilon_t^S$  and  $\hat{\beta}_{i,x}R_{x,t}^S$  are returned to their pools (not eliminated from the sample).

The resampling process outlined in steps a-d above is then repeated a large number of times deemed sufficient to gain a better perspective on the distribution of tails. As a rule of thumb, the resampling process should be repeated at least as many times as there were observations in the original sample. It is not uncommon for the bootstrap process to be repeated thousands of times. The resampled values  $\hat{R}_{i\,t}^S$  can differ from the observed sample distribution, thus expanding the sample data set with extra observations conforming to the properties of the original sample.

4. The new distribution values obtained through the parametric process are now treated as were other sample values and are incorporated into the tail index, VaR, and other risk management calculations.

<sup>&</sup>lt;sup>3</sup>The "hat" notation on variables, as in  $\hat{\alpha}_i$  and  $\hat{\beta}_{i,x}$ , denotes that the parameters were estimated from a sample distribution, as opposed to comprising the true distribution values.

The parametric bootstrap relies on the assumption that the raw returns' dependence on a benchmark as well as the manager's alpha remain constant through time. This does not have to be the case. Managers with dynamic strategies spanning different asset classes are likely to have timevarying dependencies on several benchmarks. Despite this shortcoming, the parametric bootstrap allows risk managers to glean a fuller notion of the true distribution of returns given the distribution of returns observed in the sample.

To incorporate portfolio managers' benchmarks into the VaR framework, Suleiman, Shapiro, and Tepla (2005) propose analyzing the "tracking error" of the manager's return in excess of his benchmark. Suleiman, Shapiro, and Tepla (2005) define tracking error as a contemporaneous difference between the manager's return and the return on the manager's benchmark index:

$$TE_{t} = \ln(R_{i,t}) - \ln(R_{X,t}) \tag{17.4}$$

where *Ri,t* is the manager's return at time *t* and *Rx,t* is return on the manager's benchmark, also at time *t*. The VaR parameters are then estimated on the tracking error observations.

In addition to VaR, statistical models may include Monte Carlo simulation–based methods to estimate future market values of capital at risk. The Monte Carlo simulations are often used in determining derivatives exposure. Scenario analyses and causal models can be used to estimate market risk as well. These auxiliary types of market risk estimation, however, rely excessively on qualitative assessment and can, as a result, be misleading in comparison with VaR estimates, which are based on realized historical performance.

### **Measuring Credit and Counterparty Risk**

The credit and counterparty risk reflects the probability of financial loss should one party in the trading equation not live up to its obligations. An example of losses due to a counterparty failure is a situation in which a fund's money is custodied with a broker-dealer, and the broker-dealer goes bankrupt. The collapse of Lehman Brothers in October 2008 was the most spectacular counterparty failure in recent memory. According to Reuters, close to \$300 billion was frozen in bankruptcy proceedings as a result of the bank's collapse, pushing many prominent hedge funds to the brink of insolvency. Credit risk is manifest in decisions to extend lines of credit or margins. Credit risk determines the likelihood that creditors will default on their margin calls, should they encounter any. In structured products, credit risk measures the likelihood and the impact of default of the product underwriter, called the reference entity.

Until recently, the measurement of credit and counterparty risk was delegated to dedicated third-party agencies that used statistical analysis overlaid with scenario and causal modeling. The most prominent of these agencies, Standard & Poor's and Moody's, came under fire during the credit crisis of 2007–2008 because their ratings may have failed to capture the true credit and counterparty risk, and it was revealed that in many instances the rating agencies had cozy relationships with the firms they rated. As credit and counterparty data becomes increasingly available, it may make good sense for firms to statistically rate their counterparties internally. The remainder of this section describes common techniques for measuring credit and counterparty risk.

Entities with publicly traded debt are the easiest counterparties to rank. The lower the creditworthiness of the entity, the lower the market price on the senior debt issued by the entity and the higher the yield the entity has to pay out to attract investors. The spread, or the difference between the yield on the debt of the entity under consideration and the yield on the government debt with comparable maturity, is a solid indicator of the creditworthiness of the counterparty. The higher the spread, the lower the creditworthiness of the counterparty. Because yields and spreads are inversely related to the prices of the bonds, the creditworthiness of a counterparty can also be measured on the basis of the relative bond price of the firm: the lower the bond price, the higher the yield and the lower the creditworthiness. Market prices of corporate debt provide objective information about the issuer's creditworthiness. The prices are determined by numerous market participants analyzing the firms' strategies and financial prospects and arriving at their respective valuations.

Table 17.2 shows senior bond prices for selected firms and their relative creditworthiness rankings on May 15, 2009. A creditworthiness of 100 indicates solid ability to repay the debt, while a creditworthiness of 0 indicates the imminence of default. From the perspective of a fund deciding on May 15, 2009 whether to use Morgan Stanley or Wells Fargo & Co. as its prime broker, for example, Morgan Stanley may be a better choice in that the firm shows higher creditworthiness and lower counterparty risk. As discussed in the section on implementation of risk management frameworks that follows, a diversification of counterparties is the best way to protect the operation from credit and counterparty risk.

The creditworthiness of private entities with unobservable market values of obligations can be approximated as that of a public firm with matching factors. The matching factors should include the industry, geographic location, annual earnings of the firms to proxy for the firms' sizes, and various accounting ratios, such as the quick ratio to assess short-term

| Firm                        | Bond Ticker<br>Symbol | Bond Price<br>at Close on<br>5/15/2009 | Relative<br>Creditworthiness<br>Rank |
|-----------------------------|-----------------------|----------------------------------------|--------------------------------------|
| Coca Cola Enterprises, Inc. | 191219AP9             | 131.07                                 | 80                                   |
| Morgan Stanley              | 617446HD4             | 103.25                                 | 55                                   |
| Wells Fargo & Co.           | 949746FS5             | 95.83                                  | 40                                   |
| Marriott Int'l, Inc. (New)  | 571903AF0             | 90.43                                  | 30                                   |
| American General Fin. Corp. | 02635PRT2             | 47.18                                  | 5                                    |

| TABLE 17.2 | Senior Bond Prices for Selected Firms and Their Relative |
|------------|----------------------------------------------------------|
|            | Creditworthiness Rank on May 15, 2009                    |

solvency. Once a close match with publicly traded debt is found for the private entity under evaluation, the spread on the senior debt of the publicly traded firm is used in place of that for the evaluated entity.

In addition to the relative creditworthiness score, the firms may need to obtain a VaR-like number to measure credit and counterparty risk. This number is obtained as an average of exposure to each counterparty weighted by the counterparty's relative probability of default:

$$\text{CCExposure} = \frac{1}{N} \sum_{i=1}^{N} \text{Exposure}_{i} \times \text{PD}_{i} \tag{17.5}$$

where CCExposure is the total credit and counterparty exposure of the organization, *N* is the total number of counterparties of the organization, Exposure*<sup>i</sup>* is the dollar exposure of the *i*th counterparty, and *PDi* is the probability of default of the *i*th counterparty:

$$\text{PD}_{i} = \frac{100 - (\text{Creditworthiness Rank})_{i}}{100} \% \tag{17.6}$$

The total credit and counterparty exposure is then normalized by the capital of the firm and added to the aggregate VaR number.

## **Measuring Liquidity Risk**

Liquidity risk measures the firm's potential inability to unwind or hedge positions in a timely manner at current market prices. The inability to close out positions is normally due to low levels of market liquidity relative to the position size. The lower the market liquidity available for a specific instrument, the higher the liquidity risk associated with that instrument. Levels of liquidity vary from instrument to instrument and depend on the number of market participants willing to transact in the instrument under consideration. Bervas (2006) further suggests the distinction between the trading liquidity risk and the balance sheet liquidity risk, the latter being the inability to finance the shortfall in the balance sheet either through liquidation or borrowing.

In mild cases, liquidity risk can result in minor price slippages due to the delay in trade execution and can cause collapses of market systems in its extreme. For example, the collapse of Long-Term Capital Management (LTCM) in 1998 can be attributed to the firm's inability to promptly offload its holdings. The credit crisis of 2008 was another vivid example of liquidity risk; as the credit crisis spread, seemingly high-quality debt instruments such as high-grade CDOs lost most of their value when the markets for these securities vanished. Many firms holding long positions in these securities suffered severe losses. Another, simpler, example of liquidity risk is provided by out-of-the-money options nearing expiration; the markets for out-of-the-money options about to become worthless disappear entirely.

The number of transacting parties usually depends on the potential profitability and degree of regulation in the trades of interest. No one is inclined to buy worthless options just before the options expire. In the case of CDOs in the fall of 2008, the absence of markets was largely due to regulation FAS 133 enacted in 2007. FAS 133 mandates that all securities be marked to their market prices. In the case of CDOs, for example, the market price is the last trade price recorded for the security by the firm holding CDOs in its portfolio. As a result of this regulation, the firms that held CDOs at 100 percent of their face value on the books refused to sell a portion of their CDOs at a lower price. The sale would result in devaluation of their remaining CDOs at the lower market price, which would trigger devaluation of the fund as a whole and would, in turn, result in increased investor redemptions. At the same time, potential buyers of the CDOs faced a similar problem: those already holding CDOs on their books at 100 percent of face value would face sharp devaluations of their entire funds if they chose to purchase new CDOs at significantly reduced prices. The recently proposed taxation scheme of charging transaction costs on trading as a tax may similarly destroy the liquidity of currently liquid instruments.

To properly assess the liquidity risk exposure of a portfolio, it is necessary to take into account all potential portfolio liquidation costs, including the opportunity costs associated with any delays in execution. While liquidation costs are stable and are easy to estimate during periods with little volatility, the liquidation costs can vary wildly during high-volatility regimes. Bangia et al. (1999), for example, document that liquidity risk accounted for 17 percent of the market risk in long USD/THB positions in May 1997, and Le Saout (2002) estimates that liquidity risk can reach over 50 percent of total risk on selected securities in CAC40 stocks.

Bervas (2006) proposes the following liquidity-adjusted VaR measure:

$$VaR^{L} = VaR + Liquidity \text{ }Adjustment = VaR - (\mu^{S} + z_{\alpha}\sigma^{S}) \tag{17.7}$$

where VaR is the market risk value-at-risk discussed previously in this chapter,  $\mu^S$  is the mean expected bid-ask spread,  $\sigma^S$  is the standard deviation of the bid-ask spread, and  $z_{\alpha}$  is the confidence coefficient corresponding to the desired  $\alpha$ – percent of the VaR estimation. Both  $\mu^S$  and  $\sigma^S$  can be estimated either from raw spread data or from the Roll (1984) model.

Using Kyle's  $\lambda$  measure, the VaR liquidity adjustment can be similarly computed through estimation of the mean and standard deviation of the trade volume:

$$VaR^{L} = VaR + Liquidity \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$$

where  $\hat{\alpha}$  and  $\hat{\lambda}$  are estimated using OLS regression following Kyle  $(1985)$ :

$$\Delta P_t = \alpha + \lambda NVOL_t + \varepsilon_t \tag{17.9}$$

 $\Delta P_t$  is the change in market price due to market impact of orders, and  $NVOL_t$  is the difference between the buy and sell market depths in period t.

Hasbrouck  $(2005)$  finds that the Amihud  $(2002)$  illiquidity measure best indicates the impact of volume on prices. Similar to Kyle's  $\lambda$  adjustment to  $VaR$ , the Amihud (2002) adjustment can be applied as follows:

$$VaR^{L} = VaR + Liquidity \text{ }Adjustment = VaR - (\mu^{\gamma} + z_{\alpha}\sigma^{\gamma}) \tag{17.10}$$

where  $\mu^{\gamma}$  and  $\sigma^{\gamma}$  are the mean and standard deviation of the Amihud (2002) illiquidity measure  $\gamma$ ,  $\gamma_t = \frac{1}{D_t} \sum_{d=1}^{D_t} \frac{|r_{d,t}|}{v_{d,t}}, D_t$  is the number of trades executed during time period  $t, r_{d,t}$  is the relative price change following trade d during trade period t, and  $v_{d,t}$  is the trade quantity executed within trade d.

#### **Measuring Operational Risk**

Operational risk is the risk of financial losses resulting from one or more of the following situations:

- Inadequate or failed internal controls, policies, or procedures
- Failure to comply with government regulations
- Systems failures
- Fraud
- Human error
- External catastrophes

Operational risk can affect the firm in many ways. For example, a risk of fraud can taint the reputation of the firm and will therefore become a "reputation risk." Systems failures may result in disrupted trading activity and lost opportunity costs for capital allocation.

The Basel Committee for Bank Supervision has issued the following examples of different types of operational risk:

- **Internal fraud**—misappropriation of assets, tax evasion, intentional mismarking of positions, and bribery
- **External fraud**—theft of information, hacking damage, third-party theft, and forgery
- Employment practices and workplace safety—discrimination, workers' compensation, employee health and safety
- Clients, products, and business practice—market manipulation, antitrust, improper trade, product defects, fiduciary breaches, account churning
- **Damage to physical assets**—natural disasters, terrorism, vandalism
- Business disruption and systems failures—utility disruptions, software failures, hardware failures
- Execution, delivery, and process management—data entry errors, accounting errors, failed mandatory reporting, negligent loss of client assets

Few statistical frameworks have been developed for measurement of operational risk; the risk is estimated using a combination of scalar and scenario analyses. Quantification of operational risk begins with the development of hypothetical scenarios of what can go wrong in the operation. Each scenario is then quantified in terms of the dollar impact the scenario will produce on the operation in the base, best, and worst cases. To align the results of scenario analysis with the VaR results obtained from estimates of other types of risk, the estimated worst-case dollar impact on operations is then normalized by the capitalization of the trading operation and added to the market VaR estimates

## **Measuring Legal Risk**

Legal risk measures the risk of breach of contractual obligations. Legal risk addresses all kinds of potential contract frustration, including contract formation, seniority of contractual agreements, and the like. An example of legal risk might be two banks transacting foreign exchange between the two of them, with one bank deciding that under its local laws, the signed contract is void

The estimation of legal risk is conducted by a legal expert affiliated with the firm, primarily using a causal framework. The causal analysis identifies the key risk indicators embedded in the current legal contracts of the firm and then works to quantify possible outcomes caused by changes in the key risk indicators. As with other types of risk, the output of legal risk analysis is a VaR number, a legal loss that has the potential to occur with just a 5 percent probability for a 95 percent VaR estimate.

## **MANAGING RISK**

Once market risk has been estimated, a market risk management framework can be established to minimize the adverse impact of the market risk on the trading operation. Most risk management systems work in the following two ways:

- **1.** Stop losses—stop current transaction(s) to prevent further losses
- **2.** Hedging—hedge risk exposure with complementary financial instruments

### **Stop Losses**

A stop loss is the crudest and most indispensable risk management technique to manage the risk of unexpected losses. In the case of market risk, a stop loss is a threshold price of a given security, which, if crossed by the market price, triggers liquidation of the current position. In credit and counterparty risk, a stop loss is a level of counterparty creditworthiness below which the trading operation makes a conscious decision to stop dealing with the deteriorating counterparty. In liquidity risk, the stop loss is the minimum level of liquidity that warrants opened positions in a given security. In operations risk, the stop loss is a set of conditions according to which a particular operational aspect is reviewed and terminated, if necessary. For example, compromised Internet security may mandate a complete shutdown of trading operations until the issue is resolved. Finally, a stop loss in legal risk can be a settlement when otherwise incurred legal expenses are on track to exceed the predetermined stop-loss level.

In market risk management, a simple stop loss defines a fixed level of the threshold price. For example, if at 12:00 P.M. EST we bought USD/CAD at 1.2000 and set a simple stop loss at 50 bps, the position will be liquidated whenever the level of USD/CAD drops below 1.1950, provided the position is not closed sooner for some other reason. Figure 17.4, panel (a) illustrates the idea. A simple stop loss does not take into account any price

![](_page_16_Figure_1.jpeg)

**FIGURE 17.4** The difference between simple (fixed) and trailing stop-loss thresholds.

movement from the time the position was open until the time the stop loss was triggered, resulting in a realized loss of 50 bps.

A trailing stop, on the other hand, takes into account the movements of the security's market price from the time the trading position was opened. As its name implies, the trailing stop "trails" the security's market price. Unlike the simple stop that defines a fixed price level at which to trigger a stop loss, the trailing stop defines a fixed stop-loss differential relative to the maximum gain attained in the position. For example, suppose we again bought USD/CAD at 12:00 P.M. EST at 1.2000 and set a trailing stop loss at 50 bps. Suppose further that by 12:15 P.M. EST the market price for USD/CAD rose to 1.2067, but by 13:30 P.M. EST the market price dropped down to 1.1940. The trailing stop loss would be triggered at 50 bps less the market price corresponding to the highest local maximum of the gain function. In our example, the local maximum of gain appeared at 1.2067 when the position gain was 1.2067−1.2000 = 0.0067. The corresponding trailing stop loss would be hit as soon as the market price for USD/CAD dipped below 1.2067 –50 bps = 1.2017, resulting in a realized profit of 17 bps, a big improvement over performance with a simple stop loss. Figure 17.4, panel (b) shows the process.

How does one determine the appropriate level of the stop-loss threshold? If the stop-loss threshold is too narrow, the position may be closed due to short-term variations in prices or even due to variation in the bid-ask spread. If the stop-loss threshold is too wide, the position may be closed too late, resulting in severe drawdowns. As a result, many trading practitioners calibrate the stop-loss thresholds to the intrinsic volatility of the traded security. For example, if a position is opened during high-volatility conditions with price bouncing wildly, a trader will set wide stop losses. At the same time, for positions opened during low-volatility conditions, narrow stop thresholds are required.

The actual determination of the stop-loss threshold based on market volatility of the traded security is typically calibrated with the following two factors in mind:

- **1.** Average gain of the trading system without stop losses in place, *E*[*G*]
- **2.** Average loss of the trading system without stop losses in place, *E*[*L*]

The probabilities of a particular position turning out positive also play a role in determining the optimal stop-loss threshold, but their role is a much smaller one than that of the averages. The main reason for the relative insignificance of probabilities of relative occurrence of gains and losses is that per the Gambler's Ruin Problem, the probability of a gain must always exceed the probability of a loss on any given trade; otherwise, the system faces the certainty of bankruptcy. Please refer to Chapter 10 for details.

The information on average upside and downside is typically determined from the system's back test. The back test normally spans at least two years of data and produces a sample return distribution with a number of observations sufficient to draw unbiased inferences about the distribution of the return population with the use of the techniques such as VaR, tail parameterization, or benchmarked performance measurement, discussed subsequently. Armed with distributional information about returns of the trading system, we can estimate the maximum (trailing) loss allowed that would keep our system consistently positive. The maximum trailing stop loss, *LM*, has to satisfy the following three conditions:

- **1.** In absolute terms, the maximum loss is always less than the average gain, |*LM* | < *E*[*G*]; otherwise, the system can produce negative cumulative results.
- **2.** Also in absolute terms, the maximum loss is always less than the average loss, |*LM* |≤|*E*[*L*]|; otherwise, the system can deliver almost identical results with no stop losses.
- **3.** After the introduction of stop losses, the probability of a gain still exceeds the probability of a loss in a back test.

Once the maximum stop loss is determined, the stop loss can be further refined to tighten dynamically in response to different volatility conditions. Dynamic calibration of stop losses to market volatility is more art than science. Dacorogna et al. (2001), for example, describe a moving average–based model with stop losses of low-volatility and high-volatility regimes. Dacorogna et al. (2001) use the absolute value of the gain or loss as a proxy for "volatility" and consider "volatility" to be low if the absolute gain or loss is less than 0.5 percent (50 bps). The model thresholds change in accordance with the volatility conditions. In Dacorogna et al. (2001), for example, the thresholds increase 10 times their low-volatility value when the "volatility" defined previously exceeds 0.5 percent. The low-volatility parameter is calibrated in the back test on the historical data.

The stop-loss thresholds in other types of risk are similarly determined based on the expected market gain and total maximum loss considerations presented previously.

## **Hedging Portfolio Exposure**

Hedging is closely related to portfolio optimization: the objective of any hedging operation is to create a portfolio that maximizes returns while minimizing risk—downside risk in particular. Hedging can also be thought of as a successful payoff matching: the negative payoffs of one security "neutralized" by positive payoffs of another.

Hedging can be passive or dynamic. Passive risk hedging is most akin to insurance. The manager enters into a position in a financial security with the risk characteristics that offset the long-term negative returns of the operation. For example, a manager whose main trading strategy involves finding fortuitous times for being long in USD/CAD may want to go short in the USD/CAD futures contract to offset his exposure to USD/CAD. As always, detailed analysis of the risk characteristics of the two securities is required to make such a decision.

Dynamic hedging is most often done through a series of short-term, potentially overlapping, insurance-like contracts. The objective of the shortterm insurance contracts is to manage the short-term characteristics of trading returns. In the case of market risk hedging, dynamic hedging may be developed for a particular set of recurring market conditions, when behaviors of the trading systems may repeat themselves. It may be possible to find a set of financial securities or trading strategies the returns of which would offset the downside of the primary trading strategy during these particular market conditions. For example, during a U.S. Fed announcement about the level of interest rates, the USD/CAD exchange rate is likely to rise following a rise in the U.S. interest rates, while U.S. bond prices are likely to fall following the same announcement. Depending upon return distributions for USD/CAD and U.S. bonds, it may make sense to trade the two together during the U.S. interest rate announcements in order to offset the negative tail risk in either. Mapping out extensive distributions of returns as described previously in this chapter would help in determining the details of such a dynamic hedging operation.

As with mean-variance portfolio construction, a successful hedging strategy solves the following optimization problem:

$$\begin{array}{l}\n\text{max } x \ E[R] - A \ x' V x \\
s.t. \ \sum x_i = 1\n\end{array} \tag{17.11}$$

where  $x_i$  is the portfolio weight of security  $i, i \in [1, \ldots, I], E[R]$  is a vector of expected returns of I securities, V is an  $I \times I$  variance-covariance matrix of returns, and  $A$  is the coefficient reflecting the risk aversion of the trading operation. A is commonly assumed to be  $0.5$  to simplify the solution. A dynamic state-dependent hedging would repeat the process outlined in equation  $(17.11)$ , but only for returns pertaining to a specific market state.

Like market risk, other types of risk can be diversified through portfolio risk management. The counterparty risk, for example, can be diversified through establishment of several ongoing broker-dealer relationships. Citi prime brokerage even markets itself as a secondary broker-dealer for funds already transacting, or "priming," with another broker-dealer.

Similarly, liquidity risk can be diversified away through using several liquidity providers. The American Academy of Actuaries (2000) provided the following guidance for companies seeking to diversify their liquidity exposure: "While a company is in good financial shape, it may wish to establish durable, ever-green (i.e., always available) liquidity lines of credit. The credit issuer should have an appropriately high credit rating to increase the chances that the resources will be there when needed." According to Bhaduri, Meissner, and Youn (2007), five derivative instruments can be specifically used for hedging liquidity risk:

- Withdrawal option is a put on the illiquid underlying asset.
- Bermudan-style return put option is a right to sell the underlying asset at a specified strike on specific dates.
- Return swap allows swapping the return on the underlying asset for LIBOR.
- Return swaption is an option to enter into the return swap.
- Liquidity option is a "knock-in" barrier option, where the barrier is a liquidity metric.

Regular process reviews ensure that the operations are running within predetermined guidelines on track to set goals, minimizing the probability of failure of oversight, regulatory breaches, and other internal functions. For example, the addition of new trading strategies into the trading portfolio should undergo rigid product review processes that analyze the return and risk profiles and other profitability and risk factors of proposed capital allocations, as described in Chapter 5. In addition to detailed process guidelines, operational risk can be hedged with insurance contracts offered by specialty insurance firms and by entirely outsourcing noncritical business processes to third-party vendors.

Legal risk is most effectively managed via the causal analysis used for its measurement. The key risk indicators are continuously monitored, and the effect of their changes is assessed according to the causal framework developed in the estimation of legal risk.

# **CONCLUSION**

This chapter has examined the best practices in risk management followed by successful high-frequency operations. While the process of identification, measurement, and management of risk can consume time and effort, the process pays off by delivering business longevity and stability.
### **Chapter 14**

#### **Risk Management of HFT**

Media coverage of risks accompanying high-frequency trading (HFT) tends to focus on and overstate the risks of market manipulation, as detailed in Chapter 12. However, little or no attention is paid to the real risks inherent in many HFT strategies and the ways to mitigate or minimize said risks. These risks include those incurred by high-frequency traders themselves and their trading venues and clearing parties. Chapters 14 through 16 describe the nature of such risks and existing strategy for dealing with them. Chapter 14 covers the risks facing high-frequency traders. Chapter 15 discusses mitigation of risks associated with market impact (MI) that can be used by both HFTs and other market participants, such as institutional investors. Chapter 16 covers best practices in development of HFT with specific consideration placed on minimizing risks embedded in technology implementation. Chapter 16 also discusses minimization of operational risks, and suggests best practices for execution of HFT.

# Measuring HFT Risk

As recent problems on Nasdaq and the Best Alternative Trading Systems (BATS) illustrate, the risks from poorly executed HFT systems alone may result in multimillion-dollar losses, incurred almost instantaneously. Understanding and management of risks embedded in HFT therefore is critical to ensuring operational success of HFT enterprises.

The following sections detail the quantification and management of risk exposure for different types of risk. Chapter 16 documents best practices for ongoing oversight of risk exposure. The methodology for measuring risk depends on the type of risk under consideration. All risk can be broken down into the following categories:

- Regulatory and legal risk
- Credit and counterparty risk
- Market risk
- Liquidity risk
- Operational risk

Regulatory and legal risk, credit and counterparty risk, market risk, and liquidity risks are discussed in the sections below. Chapter 15 describes mitigation of market impact. Chapter 16 focuses on operational risk.

### Regulatory and Legal Risk

Regulatory and legal risk comprises the demands of new legislations that may affect the operation of HFT systems. As discussed in Chapter 13, recent regulatory reforms strengthened risk controls surrounding HFT, and are therefore beneficial to both the markets and the HFTs themselves. As the latest U.S. Senate hearings indicate, however, the risks of adverse to HFT regulatory reform, such as the ill-thought-through idea of banning colocation, still exist. (As discussed in footnote 1 in Chapter 13, co-location is imperative for computer security and therefore stability of market systems.)

### Credit and Counterparty Risk

*Credit risk* specifies potential issues in a high-frequency trader's ability to secure leverage. Leverage refers to the trader's ability to borrow capital for his trading needs. HFTs generally have leverage abilities comparable to those of other traders. In equities, for example, HFTs can generally borrow and trade three or more times as much capital as the amount of cash available in their account, on a three-to-one or greater margin, at the discretion of the margin-advancing broker-dealer. Because most HFTs do not need to hold positions overnight, their leverage is considerably cheaper than that of long-term investors. From the broker-dealers' perspective, it is the typically unsupervised overnight changes in market value of long-term investors that are subject to blow-ups and defaults on broker's leverage. The intraday margin of HFTs is tightly monitored along with HFT positions by the responsible HFT oversight employee, at least in the best practices configurations. In futures markets, margin positions are automatically monitored and enforced by the exchanges in real time.

*Counterparty risk* reflects the probability of financial loss should the high-frequency trader's partners in the trading equation not live up to their obligations. An example of losses due to a counterparty failure is a situation in which a fund's money is custodied with a broker-dealer, and the brokerdealer goes bankrupt. The collapse of Lehman Brothers in October 2008 was the most spectacular counterparty failure in recent memory. According to Reuters, close to \$300 billion was frozen in bankruptcy proceedings as a result of the bank's collapse, pushing many prominent hedge funds to the brink of insolvency. The high-frequency traders may prevent similar conditions by tracking the creditworthiness of their brokers, as well as diversifying their exposure among different brokers and trading venues.

### Market Risk

*Market risk* is the risk of loss of capital due to an adverse price movement of the traded financial instrument. A long position in E-mini futures following a buy order at 1446.02 begins incurring market risk as soon as the order is executed. Even before any market movement takes place, instantaneous liquidation of the position will cost the trader money: to immediately close down the position, the trader or the trading system will need to pay the bid-ask spread.

The proliferation of automated trading has not changed the nature of market risk carried by market makers and other intraday trading strategies. However, on the per-trade basis and due to their ability to read every tick of market data and react in the matter of nanoseconds, high-frequency traders face considerably lower market risks than do their human counterparts.

The bulk of high-frequency market risk management focuses on the following four key aspects:

- 1. First order: Stop losses
- 2. Second order: Volatility cutouts
- 3. Third and fourth order: Short-term value-at-risk (VaR)
- 4. Higher order: Hedging with other instruments

The order of the risk management methodologies previously noted refers to the methodology relationship with the price of the traded financial instrument. Stop losses are linear in price, and are therefore "first-order" functions of price. Volatility is computed from squared price deviations and is referred to as a "second-order" metric. VaR takes into account skewness and kurtosis of the trading returns, the third- and fourth-order distributional parameters. Finally, hedging may be related to any functional shape of price, and is therefore "higher-order."

Each order of risk management is discussed in detail next.

### First-Order Risk Management: Stop Losses

Stop losses denote hard loss limits for each position and can be fixed or variable, absolute or trailing. Fixed stop losses outline the absolute maximum each position can potentially lose and are same for each trade

within a given trading strategy. Variable stop losses can be determined for each trade within a strategy and can be a strategy-specific function of market volatility and other related variables. Absolute stop losses specify the hard amount a strategy can afford to lose relative to the price level at which the position was opened. The trailing stop loss, however, stipulates the hard price an amount a strategy can lose relative to the price at which the strategy has achieved the highest gain after the position was opened. [Figure 14.1](#page-5-0) illustrates the difference between fixed and trailing stop losses.

<span id="page-5-1"></span><span id="page-5-0"></span>![](_page_5_Figure_1.jpeg)

![](_page_5_Figure_2.jpeg)

#### Determining Stop-Loss Parameters

The optimal stop-loss parameter should satisfy the following three requirements:

1. The stop loss should limit losing trades without affecting the winning trades.

2. A stop loss should not be triggered due to natural market volatility alone.

3. Stop losses should be executed immediately.

The preceding requirements translate into the following mathematical conditions for stop losses:

```
where E[Profit]
=E(Gain) * Pr(Gain) + E(Loss|Loss > StopLoss)
* Pr(Loss|Loss > StopLoss)
```

*+ E*(*Loss*|*Loss ≤ StopLoss*)

*\** Pr(*StopLoss*|*Loss ≤ StopLoss*)

Probability of gain, Pr(*Gain*), as well as the cumulative probability of loss, Pr(*Loss*|*Loss* > *StopLoss*) + Pr(*StopLoss*|*Loss* ≤ *StopLoss*), can be estimated from the simulation, as can be the average gain, *E*(*Gain*), and average losses above and below the stop loss values, *E*(*Loss*|*Loss* > *StopLoss*) and *E*(*Loss*|*Loss* ≤ *StopLoss*).

During periods of high volatility, natural oscillations of the market price may trigger "false" stop losses, adversely affecting performance of trading strategies. The simplest way to account for variable volatility is via the following analysis:

- In the in-sample back-test, estimate the volatility parameter over a rolling window. Within each time window, the volatility parameter can be estimated as a simple standard deviation, or (better) weighted toward later observations using a triangular or exponential weighting function. The duration of the window can match the average position holding time of the strategy.
- Distribution of the volatility parameters obtained in the previous step can be used to create a multiplier for the stop-loss parameter: higher volatility should result in larger absolute value of the stop loss.
- An out-of-sample back-test should confirm higher profitability of the stop-loss-enabled strategy.

## Second-Order Risk Management: Volatility Cutouts

*Volatility cutouts* refer to rules surrounding market conditions during which the HFT systems are halted. Some HFT strategies work better in highvolatility conditions, while others work best in low volatility. To optimize capital performance, volatility cutouts "pass through" orders of some strategies when one set of conditions takes place and allow orders of other strategies when a different state of the world is realized. Volatility "states of the world" can be determined empirically by computing a rolling volatility estimate, such as the standard deviation of short-term returns of the underlying asset or a market index over a certain past window of data. Such backward-looking volatility estimates are risky, as they are assuming that

the past volatility conditions will persist into the future (volatility tends to "cluster" or persist for long periods of time, so the assumption is plausible if not bulletproof). Alternatively, volatility cutouts can be tied to a variable measuring forward-looking volatility, such as the volatility index (VIX) or an implied volatility derived from the options on the traded security. Since volatility cutouts are tied to the squared changes in the value of the traded security, volatility cutouts can be considered a "second-order" risk metric.

### Determining Volatility Cutouts

Many trading strategies perform better in certain volatility conditions independent of the stop-loss parameters. To enhance performance of a strategy, it may be desirable to limit execution of such strategies in adverse volatility conditions. To determine the volatility conditions optimal for strategy execution, one may use the following technique:

1. In the in-sample back-test, estimate the volatility parameter over a rolling window. Within each time window, the volatility parameter can be estimated as a simple standard deviation, or (better) weighted toward later observations using triangular or exponential weighting function. The duration of the window can match the average position holding time of the strategy.

2. Regress strategy gains on the obtained volatility estimates using the following equation:

where *R<sup>t</sup>* represents the gain of the last completed round-trip trade realized at time *t*, and is the moving volatility estimate obtained in the previous step. Instead of realized strategy returns, the *R<sup>t</sup>* on the lefthand side of the regression can be mark-to-market strategy gain sampled at regular time intervals.

3. If the estimate of *β* is positive (negative) and statistically significant, the strategy performs better in high (low) volatility conditions. A median of volatility estimates obtained in step 1 above can be used as a turn-on/turn-off volatility switch for the strategy.

A successful risk management process should establish the risk budget that the operation is willing to take in the event that the operation ends up on the losing side of the equation. The risks should be quantified as worstcase scenario losses tolerable per day, week, month, and year and should include operational costs, such as overhead and personnel costs. Examples of the worst-case losses to be tolerated may be 10 percent of organizational equity per month or a hard dollar amount—for example, \$15 million per fiscal year.

#### Determining Volatility Cutouts Ex-Ante

Forecasting volatility is important in many trading applications. In addition to option-based strategies that directly arbitrage volatility, some spot and futures strategies may work better in some volatility conditions than in others. Many risk management models also call for volatility-dependent treatment of the strategies: stop losses may be "tighter" in low-volatility conditions and "looser" in high-volatility ones.

Forecasting volatility can be simple in principle. Volatility has been shown to "cluster" in time: volatility "builds up" into peaks and reverses into valleys gradually, resulting in clusters of high-volatility observations. As a result, volatility is straightforward to predict: high-volatility observations are usually followed by more or less high observations, while low-volatility cases are surrounded by similarly low volatility figures.

Popular tools for measuring volatility are quite simple: a standard deviation of returns (a simple average of square deviations from the mean) presents the most basic metric of volatility calculations. Since most recent observations can be more relevant than observations in the past, some researchers weigh later observations by computing a weighted average of square deviations from the mean. The weights can be either linear or exponential. Another popular metric of volatility is the average of squared intraperiod returns; it has been shown to be superior to standard deviation– based computations.

Given the tendency of volatility to cluster, it is reasonable to assume that the next period's volatility will be the same as the last period's volatility. Alternatively, one may calculate if the latest volatility observations form a trend, and then extrapolate the trend into the future. A popular trending volatility forecasting tool is called the generalized autoregressive conditional heteroskedasticity (GARCH) estimator and is built into many software packages.

Yet, when the key research question is whether the volatility is high or low, another technique, known as *Markov state dependency,* developed by Aldridge (2011), may work best. The Markov technique divides historical observations into high and low volatility states, and then assesses probabilities of transition from high to low probability and vice versa. Specifically, the technique can be used as follows:

1. Run a linear regression of price changes on past price changes.

2. Examine the distribution of error terms; separate them into two groups: low and high errors, based on the arbitrary yet appropriate cutoff point.

3. Estimate historical "transition probabilities" based on the sequential changes from low to high states and vice versa:

a. For each sequential error observation, determine whether the error was a change from low to high, a change from high to low, a stay in the low state, or a stay in the high-volatility state.

b. Count the totals and express them in a percentage probability form.

4. During run-time, assess whether the current volatility level is high or low. Given the probabilities of transition determined in step 3, assess the likelihood of a volatility change in the next period. Adjust the trading accordingly.

Markov switching models can be very fast and effective in HFT applications and many other models.

### Third- and Fourth-Order Risk Management: Valueat-Risk

Value-at-risk (VaR) is a probabilistic metric of potential loss that takes into consideration distributional properties of returns of the HFT. Intraday VaR is typically used in HFT applications to set the ceiling for the intraday market exposure and the floor for the intraday mark-to-market loss. If the strategy hits the intraday VaR threshold, the strategy is moved into paper trading for review of its stability until further notice. VaR considers the entire historical distribution of the traded security, including skewness and kurtosis of the security returns, the third and fourth moments of returns. As a result, VaR represents a "fourth-order" risk measure.

The concept of VaR has by now emerged as the dominant metric in market risk management estimation. The VaR framework spans two principal measures—VaR itself and the expected shortfall (ES). VaR is the value of loss in case a negative scenario with the specified probability should occur. The probability of the scenario is determined as a percentile

of the distribution of historical scenarios that can be strategy or portfolio returns. For example, if the scenarios are returns from a particular strategy and all the returns are arranged by their realized value in ascending order from the worst to the best, then the 95 percent VaR corresponds to the cutoff return at the lowest fifth percentile. In other words, if 100 sample observations are arranged from the lowest to the highest, then VaR corresponds to the value of the fifth lowest observation

The ES measure determines the average worst-case scenario among all scenarios at or below the prespecified threshold. For example, a 95 percent ES is the average return among all returns at the 5 percent or lower percentile. If 100 sample observations are arranged from the lowest to the highest, the ES is the average of observations 1 through 5. [Figure 14.2](#page-11-0) illustrates the concepts of VaR and ES.

<span id="page-11-0"></span>**[Figure 14.2](#page-11-1)** The 99 Percent VaR (α = 1 Percent) and 95 Percent VaR (α = 5 Percent) Computed on the Sample Return Population

<span id="page-11-1"></span>![](_page_11_Figure_3.jpeg)

To compute VaR, the trader or risk manager may use the following steps: 1. Compute daily net (after transaction costs) historical returns of the strategy either live or simulated (back-tested) returns.

2. Determine the cut-off corresponding to the worst 5 percent of strategy returns.

3. Set the shutdown threshold equivalent to the lowest 5 percentile of strategy returns, place the strategy "on probation" in paper trading until the cause of the low return is ascertained and the strategy is adjusted.

An analytical approximation to true VaR can be found by parameterizing the sample distribution. The parametric VaR assumes that the observations are distributed in a normal fashion. Specifically, the parametric VaR assumes that the 5 percent in the left tail of the observations fall at *μ*-1.65σ of the distribution, where m and s represent the mean and standard deviation of the observations, respectively. The 95 percent parametric VaR is then computed as *μ*-1.65σ, while the 95 percent parametric ES is computed as the average of all distribution values from –*∞* to *μ*-1.65σ. The average can be computed as an integral of the distribution function. Similarly, the 99 percent parametric VaR is computed as *μ*-2.33σ, while the 99 percent parametric ES is computed as the average of all distribution values from –*∞* to *μ*-2.33σ. The parametric VaR is an approximation of the true VaR; the applicability of the parametric VaR depends on how close the sample distribution resembles the normal distribution. [Figure 14.3](#page-12-0) illustrates this idea.

<span id="page-12-0"></span>**[Figure 14.3](#page-12-1)** The 95 Percent Parametric VaR Corresponds to μ – 1.65*σ* of the Distribution, While the 99 Percent Parametric VaR Corresponds to μ – 2.33*σ* of the Distribution

<span id="page-12-1"></span>![](_page_12_Figure_3.jpeg)

While the VaR and ES metrics summarize the location and the average of many worst-case scenarios, neither measure indicates the absolute worst scenario that can destroy entire trading operations, banks, and markets. Most financial return distributions have fat tails, meaning that the very

extreme events lie beyond normal distribution bounds and can be truly catastrophic.

The limitations of VaR methodology have hardly been a secret. In a *New York Times* article published on January 2, 2009, David Einhorn, the founder of the hedge fund Greenlight Capital, stated that VaR was "relatively useless as a risk-management tool and potentially catastrophic when its use creates a false sense of security among senior managers and watchdogs. This is like an air bag that works all the time, except when you have a car accident." The article also quoted Nassim Nicholas Taleb, the best-selling author of *The Black Swan*, as calling VaR metrics "a fraud." Jorion (2000) points out that the VaR approach both presents a faulty measure of risk and actively pushes strategists to bet on extreme events. Despite all the criticism, VaR and ES have been mainstays of corporate risk management for years Most recently, daily VaR has made forays into risk management of active trading, quickly becoming a tool of choice on many trading floors.

To alleviate the shortcomings of the VaR, many quantitative outfits began to parameterize extreme tail distributions to develop fuller pictures of extreme losses. Once the tail is parameterized based on the available data, the worst-case extreme events can be determined analytically from distributional functions, even though no extreme events of comparable severity were ever observed in the sample data.

The parameterization of the tails is performed using the extreme value theory (EVT). *EVT* is an umbrella term spanning a range of tail modeling functions. Dacorogna et al. (2001) note that all fat-tailed distributions belong to the family of Pareto distributions. A Pareto distribution family is described as follows:

(1) 
$$G(x) = \begin{cases} 0 & x \le 0 \\ \exp(-x^{-\alpha}) & x > 0, \alpha > 0 \end{cases}$$

where the tail index α is the parameter that needs to be estimated from the return data. For raw security returns, the tail index varies from financial security to financial security. Even for raw returns of the same financial security, the tail index can vary from one quoting institution to another, especially for really high-frequency estimations.

<span id="page-14-1"></span>When the tail index a is determined, we can estimate the magnitude and probability of all the extreme events that may occur, given the extreme events that did occur in the sample. [Figure 14.4](#page-14-0) illustrates the process of using tail parameterization:

<span id="page-14-0"></span>![](_page_14_Figure_1.jpeg)

1. Sample return observations obtained from either a back-test or live results are arranged in ascending order.

2. The tail index value is estimated on the bottom 5 percentile of the sample return distribution.

3. Using the distribution function obtained with the tail index, the probabilities of observing the extreme events are estimated. According to the tail index distribution function, a –7 percent return would occur with a probability of 0.5 percent while a return of –11 percent would register with a probability of 0.001 percent.

The tail index approach allows us to deduce the unobserved return distributions from the sample distributions of observed returns. Although the tail index approach is useful, it has its limitations. For one, the tail index approach "fills in" the data for the observed returns with theoretical observations; if the sample tail distribution is sparse (and it usually is), the tail index distribution function may not be representative of the actual extreme returns. In such cases, a procedure known as *parametric bootstrapping* may be applicable.

Parametric bootstrap simulates observations based on the properties of the sample distribution. The technique "fills in" unobserved returns based on

observed sample returns. The parametric bootstrap process works as follows:

The sample distribution of observed returns delivered by the manager is decomposed into three components using a basic market model:

1. The manager's skill, or alpha.

2. The manager's return due to the manager's portfolio correlation with the benchmark.

3. The manager's idiosyncratic error.

The decomposition is performed using the standard market model regression:

 $(2) R_{i,t} = \alpha_i + \beta_{i,x} R_{x,t} + \varepsilon_t$ 

where  $R_{\text{int}}$  is the manager's raw return in period *t*,  $R_{\text{int}}$  is the raw return on the chosen benchmark in period *t*,  $\alpha$  is the measure of the manager's money management skill or alpha, and  $\beta_{ix}$  is a measure of the dependency of the manager's raw returns on the benchmark returns.

4. Once parameters  $\hat{\alpha_i}$  and  $\hat{\beta_{i\ast}}$  are estimated using equation (2), three pools of data are generated: one for  $\hat{\alpha_i}$  (constant for given manager, benchmark, and return sample),  $\hat{\beta}_{i\star}R_{\star\star}$ , and  $\varepsilon_{i\star}^{-1}$  For example, if  $\hat{\alpha_i}$  and  $\hat{\beta}_{i\star}$ were estimated to be  $0.002$  and  $-0.05$ , respectively, then the component pools for a sample of raw returns and benchmarked returns may look as shown in Table 14.1.

5. Next, the data is resampled as follows:

<span id="page-15-1"></span>a. A value  $\varepsilon_{\text{it}}^{\text{s}}$  is drawn at random from the pool of idiosyncratic errors,  $\{\varepsilon_{i}\}.$ 

b. Similarly, a value  $\hat{\beta}_{i\kappa}R_{\kappa t}^{s}$  is drawn at random from the pool of  $\{\beta_{\nu}R_{\nu}\}\$ 

c. A new sample value is created as follows:

 $(3) \hat{R}_{i,t}^S = \hat{\alpha}_i + \hat{\beta}_{i,x} R_{x,t}^S + \varepsilon_t^S$ 

The sampled variables  $\varepsilon_{\text{it}}^{\text{s}}$  and  $\hat{\beta}_{\text{it}}$  are returned to their pools (not eliminated from the sample).

<span id="page-15-0"></span>**Table 14.1** Examples of Generated Bootstrap Components

| Observation No. | $R_{i,t}$ | $K_{x,t}$ | U.    | $\beta_{i,x}R_{x,t}$ | $\omega_{tt}$ |
|-----------------|-----------|-----------|-------|----------------------|---------------|
|                 | 0.015     | $-0.001$  | 0.002 | 0.00005              | 0.01295       |
|                 | 0.0062    | 0.0034    | 0.002 | $-0.00017$           | 0.00403       |

The resampling process outlined in steps a–c is then repeated a large number of times deemed sufficient to gain a better perspective on the distribution of tails. As a rule of thumb, the resampling process should be repeated at least as many times as there were observations in the original sample. It is not uncommon for the bootstrap process to be repeated thousands of times. The resampled values can differ from the observed sample distribution, thus expanding the sample data set with extra observations conforming to the properties of the original sample.

6. The new distribution values obtained through the parametric process are now treated as were other sample values and are incorporated into the tail index, VaR, and other risk management calculations.

The parametric bootstrap relies on the assumption that the raw returns' dependence on a benchmark as well as the manager's alpha remain constant through time. This does not have to be the case. Managers with dynamic strategies spanning different asset classes are likely to have time-varying dependencies on several benchmarks. Despite this shortcoming, the parametric bootstrap allows risk managers to glean a fuller notion of the true distribution of returns given the distribution of returns observed in the sample.

To incorporate portfolio managers' benchmarks into the VaR framework, Suleiman, Shapiro, and Tepla (2005) propose analyzing the "tracking error" of the manager's return in excess of his benchmark. Suleiman et al. (2005) define tracking error as a contemporaneous difference between the manager's return and the return on the manager's benchmark index:

(4)

where *Ri*,*<sup>t</sup>* is the manager's return at time *t* and *Rx,t* is return on the manager's benchmark, also at time *t*. The VaR parameters are then estimated on the tracking error observations.

In addition to VaR, statistical models may include Monte Carlo simulation–based methods to estimate future market values of capital at risk. The Monte Carlo simulations are often used in determining derivatives exposure. Scenario analyses and causal models can be used to estimate market risk as well. These auxiliary types of market risk estimation, however, rely excessively on qualitative assessment and can, as a result, be misleading in comparison with VaR estimates, which are based on realized historical performance.

### Higher-Order Risk Management: Hedging

The objective of hedging is to create a portfolio that maximizes returns while minimizing risk—downside risk in particular. Hedging can also be thought of as a successful payoff matching: the negative payoffs of one security "neutralized" by positive payoffs of another.

Hedging can be passive or dynamic. Passive risk hedging is most akin to insurance. The manager enters into a position in a financial security with the risk characteristics that offset the long-term negative returns of the operation. For example, a manager whose main trading strategy involves finding fortuitous times for being long in USD/CAD may want to go short the USD/CAD futures contract to offset his exposure to USD/CAD. As always, detailed analysis of the risk characteristics of the two securities is required to make such a decision.

Dynamic hedging is most often done through a series of short-term, potentially overlapping, insurance-like contracts. The objective of the short-term insurance contracts is to manage the short-term characteristics of trading returns. In the case of market risk hedging, dynamic hedging may be developed for a particular set of recurring market conditions, when behaviors of the trading systems may repeat themselves. It may be possible to find a set of financial instruments or trading strategies the returns of which would offset the downside of the primary trading strategy during these particular market conditions. For example, during a U.S. Fed announcement about the level of interest rates, the USD/CAD exchange rate is likely to rise following a rise in the U.S. interest rates, while U.S. bond prices are likely to fall following the same announcement. Depending upon return distributions

for USD/CAD and U.S. bonds, it may make sense to trade the two together during the U.S. interest rate announcements in order to offset the negative tail risk in either. Mapping out extensive distributions of returns as described previously in this chapter would help in determining the details of such a dynamic hedging operation.

High-frequency portfolio management can be applied to manage market risks of instruments used in HFT strategies as well as to extend capacity of strategies by carrying it over to other instruments.

Hedging can be further broken down into the following categories:

- Delta hedging
- Portfolio hedging

### Delta Hedging

In delta hedging HFT in a particular financial instrument, the portfolio system enters and closes positions in a liquid related instrument. The related instrument for a single stock or a spot commodity can be a nearterm futures contract written on that stock or commodity. Delta hedging instruments related to stocks, commodities or futures may be a liquid option. Most liquid options tend to be with near expiration dates and "at-the-money," with strike prices close to the present price of the underlying instrument.

In delta hedging, for every unit of the HF-traded instrument, the system purchases a specific quantity of the hedging instrument. This hedging quantity is determined by the average relative changes in the prices of the HF-traded instrument and the hedging instrument:

$$Q_{\text{hedging},t} = \frac{\Delta P_{\text{HFT},t}}{\Delta P_{\text{hedging},t}}$$

where Δ*PHFT,t* is the average return on the HF-traded instrument computed per chosen unit of time, and Δ*Phedging,t* represents the return on the selected hedging instrument computed over the same unit of time. To standardize the units of HF-traded and hedging instruments, both returns need to be time-based; the volume and tick clocks are inappropriate for the hedging application. In dynamic hedging, the quantity of the hedging instrument, *Q hedging,t* , needs to be recalculated continuously in the moving-window specification to ensure the average price changes are accurately captured.

In dynamic hedging, after the latest quantity of the hedging instrument, *Q hedging,t* , is estimated, a new challenge arises: executing the trades in the primary and the hedging instruments. The situation becomes particularly demanding in cases when the high-frequency trading strategy relies on limit orders, as the risk of non-execution in either instrument may compromise hedging activity altogether. A possible solution involves always trading the hedging instrument using market orders, and only after the trades in the principal instrument were

completely executed. Care should be taken to ensure that such solution does not destroy profitability of the HFT strategy.

### Portfolio Hedging

The main challenge of dynamic hedging of high-frequency strategies is speed: computation of risk-minimizing allocations takes time, during which the markets move and render the just-computed allocations stale. The hedging problem becomes a moving target in fast-paced markets, as illustrated in [Figure 14.5.](#page-21-0)

<span id="page-21-1"></span><span id="page-21-0"></span>![](_page_21_Figure_2.jpeg)

![](_page_21_Figure_3.jpeg)

To overcome the challenge described in [Figure 14.5,](#page-21-0) trading systems can deploy fast portfolio optimization algorithms discussed in detail below.

A classic portfolio hedging strategy, developed by Markowitz (1952), solves the following optimization problem:

(6)

where *x*<sup>i</sup> is the portfolio weight of security *i*, *i*∊[1,…,*I*], *E*[*R*] is a vector of expected returns of *I* securities, *V* is an *I×I* variance-covariance matrix of returns, and *A* is the coefficient reflecting the risk aversion of the trading operation. *A* is commonly assumed to be 0.5 to simplify the solution. A dynamic state-dependent hedging would repeat the process

outlined in equation (6), but only for returns pertaining to a specific market state.

The solution to equation (6) calls for an inversion of the variancecovariance matrix *V*, a computationally demanding operation the execution time of which has been shown to grow as a square of number of financial instruments considered.

Several classes of algorithms have been proposed to simplify and speed up setting the optimal portfolio weights:

- Simultaneous equations
- Nonlinear programming
- Critical-line optimizing algorithms
- Discrete pairwise (DPW) optimization
- Genetic algorithms

The following sections describe each of the algorithms in detail.

#### *Simultaneous Equations*

The *simultaneous equations* framework is the algorithm that directly follows the Markowitz (1952) specification. It has been shown to be inefficient for optimization if the portfolio exceeds 10 strategies, and it may produce highly erroneous forecasts when 20 or more assets are involved. The forecast errors are due to the estimation errors that occur when the average returns and variances are computed. The Bayesian error-correction framework, discussed later in this chapter, can be used to alleviate some of the input estimation errors. Still, in addition to the issues of forecast errors, the estimation time of this algorithm grows exponentially with the number of trading strategies involved, making this method hardly suitable for high-frequency trading of many assets. Tsagaris, Jasra, and Adams (2010) show that computational speed improvement can be improved by updating portfolio weights using eigenvalue decomposition, instead of recalculating portfolio weights afresh with each new tick of data.

### Nonlinear Programming

*Nonlinear programming* is a class of optimizers popular in commercial software. The nonlinear algorithms employ a variety of techniques with the objective of maximizing or minimizing the target portfolio optimization function given specified parameters such as portfolio allocation weights. Some of these algorithms employ a gradient technique whereby they analyze the slope of the objective function at any given point and select the fastest increasing or decreasing path to the target maximum or minimum, respectively. The nonlinear programming algorithms are equally sensitive to the estimation errors of the input means and variances of the returns. Most often, the algorithms are too computationally complex to be feasible in the highfrequency environments. A recent example of a nonlinear optimizer is provided by Steuer, Qi, and Hirschberger (2006).

### The Critical Line–Optimizing Algorithm

The *critical line–optimizing algorithm* was developed by Markowitz (1959) to facilitate the computation of his own portfolio theory. The algorithm is fast and comparatively easy to implement. Instead of providing point weights for each individual security considered in the portfolio allocation, the critical line optimizer delivers a set of portfolios on the efficient frontier, a drawback that has precluded many commercial companies from adapting this method. A recent algorithm by Markowitz and Todd (2000) addresses some of the issues. According to Niedermayer and Niedermayer (2007), the Markowitz and Todd (2000) algorithm outperforms the algorithm designed by Steuer, Qi, and Hirschberger (2006) by a factor of 10,000 when at least 2,000 assets considered simultaneously.

#### Discrete Pairwise (DPW) Optimization

The existing algorithms, whatever the complexity and accuracy of their portfolio allocation outputs, may not be perfectly suited to the highfrequency trading environment. First, in environments where a delay of one microsecond can result in a million-dollar loss, the optimization

algorithms in their current form still consume too much time and system power. Second, these algorithms ignore the liquidity considerations pertinent to the contemporary trading settings; most of the transactions occur in blocks or "clips" of a prespecified size. Trades of larger-than-normal sizes as well as trades of smaller blocks incur higher transaction costs that in the high-frequency environment can put a serious strain on the system's profitability.

A simple high-frequency alternative to the complex optimization solutions is a discrete pairwise (DPW) optimization developed by Aldridge (2010). The DPW algorithm is a fast compromise between the equally weighted portfolio setting and a full-fledged optimization machine that outputs portfolio weights in discrete clips of the prespecified sizes. No fractional weights are allowed. The algorithm works as follows:

1. Candidates for selection into the overall portfolio are ranked using Sharpe ratios and sorted from the highest Sharpe ratio to the lowest. This step of the estimation utilizes the fact that the Sharpe ratio itself is a measure of where each individual strategy lies on the efficient frontier.

2. An even number of strategies with the highest Sharpe ratios are selected for inclusion into the portfolio. Half of the selected strategies should have historically positive correlations with the market, and half should have historically negative correlations with the market.

3. After the universe of financial instruments is selected on the basis of the Sharpe ratio characteristics, all selected strategies are ranked according to their current liquidity. The current liquidity can be measured as the number of quotes or trades that have been recorded over the past fixed number of seconds or even minutes of trading activity.

4. After all the strategies have been ranked on the basis of their liquidity, the pairs are formed through the following process: the two strategies within each pair have opposite historical correlation with the market. Thus, strategies historically positively correlated with the market are matched with strategies historically negatively

correlated with the market. Furthermore, the matching should occur according to the strategy liquidity rank. The most liquid strategy positively correlated with the market should be matched with the most liquid strategy negatively correlated with the market, and so on until the least liquid strategy positively correlated with the market is matched with the least liquid strategy negatively correlated with the market. The liquidity-based matching ensures that the high-frequency dynamic captured by correlation is due to idiosyncratic movements of the strategy rather than the illiquidity conditions of one strategy.

5. Next, for each pair of strategies, the high-frequency volatility of a portfolio of just the two strategies is computed for discrete position sizes in either strategy. For example, in foreign exchange, where a common transactional clip is \$1 million, the discrete position sizes considered for the pairwise optimization may be –\$3 million, –\$2 million, –\$1 million, 0, \$1 million, \$2 million, and \$3 million, where the minus sign indicates the short position. Once the volatility for the various portfolio combinations is selected within each pair of strategies, the positions with the lowest portfolio volatility are selected.

6. The resulting pair portfolios are subsequently executed given the maximum allowable allocation constraints for each strategy. The maximum long and short allocation is predetermined and constrained as follows: the cumulative gross position in each strategy cannot exceed a certain size, and the cumulative net position cannot exceed another, separately set, limit that is smaller than the aggregate of the gross limits for all strategies. The smaller net position clause ensures a degree of market neutrality.

The DWP algorithm is particularly well suited to high-frequency environments because it has the following properties:

- The DPW algorithm avoids the brunt of the impact of input estimation errors by reducing the number of strategies in each portfolio allocation decision.
- The negative historical correlation of input securities ensures that within each pair of matched strategies, the minimum variance will

result in long positions in both strategies most of the time. Long positions in the strategies are shown to historically produce the highest returns per unit of risk, as is determined during the Sharpe ratio ranking phase. The times that the system results in short positions for one or more strategy are likely due to idiosyncratic market events.

- The algorithm is very fast in comparison with other portfolio optimization algorithms. The speed of the algorithm comes from the following "savings" in computational time:
  - If the total number of strategies selected in the Sharpe ratio ranking phase is 2*K*, the DPW algorithm computes only *K* correlations. Most other portfolio optimization algorithms compute correlation among every pair of strategies among the 2*K* securities, requiring 2*K*(*K−*1) correlation computations instead.
  - The grid search employed in seeking the optimal portfolio size for each strategy within each portfolio pair optimizes only between two strategies, or in two dimensions. A standard algorithm requires a 2*K*-dimensional optimization.
  - Finally, the grid search allows only a few discrete portfolio weight values. In the main example presented here, there are seven allowable portfolio weights: –\$3 MM, –\$2 MM, –\$1 MM, 0, \$1 MM, \$2 MM, and \$3 MM. This limits the number of iterations and resulting computations from, potentially, infinity, to 7<sup>2</sup> = 49.

Alexander (1999) notes that correlation and volatility are not sufficient to ensure long-term portfolio stability; both correlation and volatility are typically computed using short-term returns, which only partially reflect dynamics in prices and necessitate frequent portfolio rebalancing. Instead, Alexander (1999) suggests that in portfolio optimization more attention should be paid to cointegration of constituent strategies. Auxiliary securities, such as options and futures, can be added into the portfolio mix based on cointegration analysis to further strengthen the risk-return characteristics of the trading operation. The cointegration-enhanced portfolios can work particularly

well in trading operations that are tasked with outperforming specific financial benchmarks.

#### Genetic Algorithms

*Genetic algorithms* "learn" from past forecasts via the so-called Bayesian approach. Specifically, the Bayesian self-correction model compares the realized performance of portfolio with forecasted values, and adjusts future forecasts on the basis of errors retrieved from the comparison. Bayesian methodology continuously recalculates the trajectory of prices of portfolio instruments and updates the optimal portfolio weights. In many cases, genetic algorithms adjust, but do not fully recalculate portfolio weights, saving considerable computational time.

In the Bayesian approach, the average return estimate of a particular security is considered to be a random variable and is viewed probabilistically in the context of previously obtained information, or priors. All expectations are subsequently developed with respect to the distribution obtained for the estimate. Multiple priors, potentially representing multiple investors or analysts, increase the accuracy of the distribution for the estimate.

Under the Bayesian specification, all mean and variance-covariance estimates are associated with a confidence interval that measures the accuracy of the forecast. An accurate forecast has a tight confidence interval, while the inaccurate forecast has a wide confidence interval. After the accuracy of the previous forecast has been determined, the portfolio weight of a security is scaled depending on the width of the confidence intervals of these securities. The wider the confidence intervals for parameter estimates, the smaller is the portfolio weight for that security. When the confidence intervals approach zero, the weights are similar to those of the classic mean-variance optimization.

The traditional Bayesian approach, applied to mean-variance optimization by Jorion (1986), works as follows: both mean and variance estimates of a portfolio computed on a contemporary data sample are adjusted by lessons gleaned from historical (prior) observations.

The dispersion of the distributions of the true mean and variance of the distributions shrinks as more observations are collected and

analyzed with time. If *Rp,t* is the portfolio return following the meanvariance optimization of equation (7) from time *t –* 1 to time *t*, and is the average return estimate for security *i*, , the "Bayes-Stein shrinkage estimators" for expected return and variance of an individual security *i* to be used in the mean-variance optimization for the next period *t* + 1, are computed as follows:

$$E[R_{i,t+1}]_{BS} = (1 - \phi_{i,BS})\hat{E}[R_{i,t}] + \phi_{i,BS}R_{p,t}$$

$$V[R_{i,t+1}]_{BS} = V[R_{i,t}] \left[ 1 + \frac{1}{t+v} \right] + \frac{v}{t(t+1+v)} V[R_{i,t}]$$

where *v* is the precision of the mean estimates: ,

*N* is the number of observations in the sample at time *t*, and *BS* is the shrinkage

factor for the mean: . The case of zero precision (*v* = 0) corresponds to

completely diffuse estimates.

<span id="page-30-1"></span>Despite the computational complexities of high-frequency hedging, HFT hedging can be very effective due to the following feature of highfrequency data: low correlations between any two financial instruments. [Figure 14.6](#page-30-0) illustrates the point with empirical correlations observed on the S&P 500 ETF and iShares MSCI Index (EFA). Trade correlations are particularly low, just 3 percent when the data is sampled every 45 seconds, and decrease to zero as data sampling frequency increases to 200 ms. Quote correlations are much higher, around 30 percent when sampled every 45 seconds. The quote correlations also decrease dramatically with sampling frequency, to about 7 percent with 200-ms sampling. Relatively higher correlations of quote data may illuminate relative informativeness of tick data: quote data likely reflects market makers' information unavailable in trade data. The daily close correlation of the Standard & Poor's (S&P) 500 ETF and iShares MSCI Index (EFA) often reaches 65 percent.

<span id="page-30-0"></span>**[Figure 14.6](#page-30-1)** Correlations in High-Frequency Data. *Source: Aldridge (2010).*

![](_page_31_Figure_0.jpeg)

### Liquidity Risk

Liquidity risk may affect high-frequency traders during the normal intraday trading or during the end-of-day liquidation. Liquidity risk measures the firm's potential inability to unwind or hedge positions in a timely manner at current market prices. The inability to close out positions is normally due to low levels of market liquidity relative to the position size. The lower the market liquidity available for a specific instrument, the higher the liquidity risk associated with that instrument. Levels of liquidity vary from instrument to instrument and depend on the number of market participants willing to transact in the instrument under consideration. Bervas (2006) further suggests the distinction between the trading liquidity risk and the balance sheet liquidity risk, the latter being the inability to finance the shortfall in the balance sheet either through liquidation or borrowing.

In mild cases, liquidity risk can result in minor price slippages due to the delay in trade execution and can cause collapses of market systems in its extreme. For example, the collapse of Long-Term Capital Management (LTCM) in 1998 can be attributed to the firm's inability to promptly offload its holdings.

To properly assess the liquidity risk exposure of a portfolio, it is necessary to take into account all potential portfolio liquidation costs, including the opportunity costs associated with any delays in execution. While liquidation costs are stable and are easy to estimate during periods with little volatility, the liquidation costs can vary wildly during high-volatility regimes. Bangia et al. (1999), for example, document that liquidity risk accounted for 17 percent of the market risk in long USD/THB positions in May 1997, and Le Saout (2002) estimates that liquidity risk can reach over 50 percent of total risk on selected securities in CAC40 stocks.

Bervas (2006) proposes the following measure of liquidity risk:

(7)

where VaR is the market risk value-at-risk discussed previously in this chapter, *μ S* is the mean expected bid-ask spread, *<sup>S</sup>* is the standard deviation of the bid-ask spread, and *z*<sup>α</sup> is the confidence coefficient corresponding to

the desired α*–*percent of the VaR estimation. Both *μ <sup>S</sup>* and *<sup>S</sup>* can be estimated either from raw spread data or from the Roll (1984) model.

Using Kyle's λ measure, the VaR liquidity adjustment can be similarly computed through estimation of the mean and standard deviation of the trade volume:

(8)

where and are estimated using OLS regression following Kyle (1985):

(9)

*ΔP<sup>t</sup>* is the change in market price due to market impact of orders, and *NVOL<sup>t</sup>* is the difference between the buy and sell market depths in period *t*.

Hasbrouck (2005) finds that the Amihud (2002) illiquidity measure best indicates the impact of volume on prices. Similar to Kyle's *λ* adjustment to VaR, the Amihud (2002) adjustment can be applied as follows:

(10)

where μγ and *σγ* are the mean and standard deviation of the Amihud (2002)

illiquidity measure *γ*, , *D<sup>t</sup>* is the number of trades executed during time period *t*, *rd*,*<sup>t</sup>* is the relative price change following trade *d* during trade period *t*, and *vd*,*<sup>t</sup>* is the trade quantity executed within trade *d*.

The liquidity risk also applies in multiasset HFT upon entering positions. When the strategy calls for simultaneous acquisition of multiple instruments via limit orders, the less liquid instruments may compromise the strategy as they may be difficult to acquire. In such cases, the limit orders for the illiquid instruments are sent first; if executed, orders for the liquid instruments are placed.

## Summary

Competent risk management protects deployed capital, reduces risk and often enhances overall performance of high-frequency strategies. The risk management framework of HFT should take into account all aspects of HFT operation, including HFT suppliers and the government.

# End-of-Chapter Questions

1. What are the key types of risk faced by a high-frequency trading operation?

2. How to measure and mitigate market risk?

3. What is the credit and counterparty risk from a high-frequency trading perspective?

4. What are the key problems in high-frequency portfolio optimization?

5. What is liquidity risk? How to measure it?

<sup>1</sup> The "hat" notation on variables, as in and , denotes that the parameters were estimated from a sample distribution, as opposed to comprising the true distribution values.
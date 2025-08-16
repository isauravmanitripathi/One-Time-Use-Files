# **Asset–Liability Management**

Asset–liability management is a major concern for large financial institutions. Assets must be invested to achieve sufficient returns to pay liabilities and achieve goals subject to uncertainties, policy, taxes, and legal constraints. This article discusses asset and liability management with portfolio complexities, transaction costs, liquidity, taxes, investor preferences (including downside risk control, policy constraints, and other constraints), uncertain returns, and the timing of returns and commitments. Applications to the management of investment portfolios for large financial institutions, including pension funds and insurance companies, and for individual life-cycle planning are discussed. The approach recommended is discrete-time, multiperiod stochastic programming. For most practical purposes, such models provide a superior alternative to other approaches, such as mean–variance, simulation, control theory, and continuous-time finance. These models utilize investor preferences in a simple, understandable way. We present the Russell–Yasuda Kasai and the InnoALM models, both of which had a major impact on the practice of asset-liability management (ALM).

The use of scenario-based, stochastic programming optimization models in discrete time provides an approach to asset–liability modeling over time. The models provide a tool to think about, organize, and do calculations concerning how one should choose asset mixes over time to achieve goals and cover liabilities. Risk and return are balanced to achieve period-by-period goals and pay liabilities. The models force diversification and the consideration of extreme scenarios to protect investors from the effects of tail outcomes and also do well in normal times. They will not let individuals or institutions get into situations in which extreme, but plausible, scenarios would lead to truly disastrous consequences, such as losing half or more of one's assets. Because these models force consideration of all relevant scenarios, the common practice of assuming that low-probability scenarios will not occur is avoided. Hence, the disasters that frequently follow from this error are avoided.

In discrete-time, multiperiod stochastic programming models, one typically maximizes a concave, risk-averse utility function composed of the discounted expected wealth in the final period less a risk measure composed of a risk-aversion index times the sum of convex penalties for target violations relating to investor goals of various types in various periods. The convexity means that the larger the target violation, the larger the penalty cost. Hence, risk is measured as the nonattainment of investor goals, and this risk is traded off against expected returns. This approach is similar to a mean–variance preference structure, except that it is based on final wealth and the risks are downside risks that are measured across periods and investor goals. Discrete scenarios that represent the possible returns and other random parameter outcomes in various periods are generated from econometric and other models, such as those related to market dangers with increasing risk and from expert modeling. Mean-return estimation and the inclusion of extreme events are important for model success. The scenario approach has a number of advantages:

- Normality or lognormality, which is not an accurate representation of actual asset prices (*see* **Stylized Properties of Asset Returns**; **Heavy Tails**), especially for losses, need not be assumed.
- Tail events can be easily included; studies show that downside probabilities estimated from actual option prices are 10–1000 times fatter than lognormal (*see* **Heavy Tails**; **Stylized Properties of Asset Returns**).
- Scenario-dependent correlations between assets can be modeled and used in the decision-making process so that "normal" and "crisis" economic times (with higher and differing signed correlations) can be considered separately.
- The exact scenario that will occur and the probabilities and values of all the scenarios need not be accurately determined to provide model performance that is superior to that of other models and strategies, such as mean–variance or portfolio insurance.
- Most of the natural, practical aspects of asset–liability applications can be modeled well in the multiperiod stochastic programming approach. Model output is easy to understand by nonexperts such as pension fund trustees. The models can be tested *via* simulation and statistical methods and considerable independent evidence

demonstrates their superiority to other standard approaches and strategies.

- The approach protects investors from large market losses by considering the effects of extreme scenarios while accounting for other key aspects of the problem.
- Determining whether investment positions are truly diversified and of the right size across time is crucial to protect against extreme scenarios and ensure that the results will be good in normal times and avoid disasters.

## **Procedures for Scenario Generation**

There are many methods to estimate scenarios. Abaffy *et al.* [1, 10] survey scenario estimation and aggregation methods that represent a larger number of scenarios by a smaller number. See [31] for further references and discussion. Scenarios are a means to describe and approximate possible future economic environments. They are represented as discrete probabilities of specific events. Together, all the scenarios represent the possible evolution of the future world. The basic idea is to have a set of *T* period scenarios of the form *S<sup>T</sup>* = *(S*1*, S*2*,...,ST )*, where *st* ∈ *St* are the possible outcomes of all random problem elements and where *st* occurs in period *t* with probability *pt(st)*.

For asset–liability modeling, the most important parts of the distribution are the means and the left tail. The mean drives the returns and the left tail the losses. We cannot include all possible scenarios but rather focus on a discrete set that well approximates the possible important events that could happen. With *S<sup>T</sup>* total scenarios, we can include those we want. Once a scenario is included, the problem must react to what would be the consequences of that scenario. This important and flexible feature of stochastic programming modeling is not usually available in other approaches. The inclusion of such extreme scenarios means that the model must react to the possibility of that scenario occurring. This inclusion is one of the ways a stochastic programming overall model would have helped mitigate the 1998 losses and collapse of LTCM (*see* **Long-Term Capital Management**). The model would not have let them hold such large positions. We frequently aggregate scenarios to pick the best *N* out of the *S<sup>T</sup>* so that the modeling effort is manageable. The generation of good scenarios that well represent the future

evolution of the key parameters is crucial to the success of the modeling effort.

Among other things, scenarios should consider the following:

- mean reversion of asset prices;
- volatility clumping, in which a period of high volatility is followed by another period of high volatility;
- volatility increases when prices fall and decreases when they rise;
- trending of currency, interest rates, and bond prices;
- ways to estimate mean returns;
- ways to estimate fat tails; and
- ways to eliminate arbitrage opportunities or minimize their effects.

The true distribution *P* is approximated by a finite number of points *(w*<sup>1</sup>*,...,wS)* with positive probability *p<sup>s</sup>* for each scenario *s*. The sum of all scenario probabilities is 1.

Economic variables and actuarial predictions drive the liability side, whereas economic variables and sentiment drive financial markets and security prices. Hence, estimating scenarios for liabilities may be easier than for assets because there often are mortality tables, actuarial risks, legal requirements, such as pension or social security rules, well-established policies, and so on. Such scenarios may come from simulation models embedded into the optimization models that attempt to model the complex interaction between the economy, financial markets, and liability values. We can use the following classification:

- 1. There can be complete knowledge of the exact probability distribution. This knowledge usually comes from a theoretical model, but it is possible to use historical data or an expert's experience.
- 2. There can be a known parametric family based on a theoretical model whose parameters are estimated from available and possibly forecasted data.
- 3. Scenarios can be formed by sample-moment information that aggregates large numbers of scenarios into a smaller, easier set or generates scenarios from assumed probability distributions. This idea was used in the five-period Russell–Yasuda Kasai insurance model in 1989 [6]. Høyland and Wallace (HW) [17] have expanded and refined the idea for multiperiod

problems and they have generated scenarios that match some moments of the true distribution. Typically it is the first four moments.

- 4. The idea is to assume that the past will repeat in the sense that events that occurred with various probabilities will reoccur with the same probabilities but not necessarily in the same order. Despite missing fat tails, the method has had some success. This idea can be implemented by using the raw data or through procedures, such as vector autoregressive modeling or bootstrapping, that sample from the past data. Using subsets of past data is a viable scenario generation method. Grauer and Hakansson [13] have successfully used the idea in many asset-only studies. When no reliable data exist, one can use an expert's forecasts. Examples include [24, 28] or governmental regulations.
- 5. The Hochreiter and Pflug (HP) [16] approach generates scenario trees using a multidimensional facility location problem that minimizes a Wasserstein distance measure from the true distribution. Kolmogorov–Smirnov (KS) distance approximation is an alternative approach, but it does not take care of tails and higher moments. The HP method combines a good approximation of the moments and the tails.

Whatever method is used to generate the scenarios, in relying on the meshing of decision-maker subjective estimates, expert judgment, and empirical estimation, it is crucial to validate the estimated distributions and to make sure that the decision maker has not defined the range too narrowly. Perhaps reflecting on the distribution by asking what would make the value be outside the range and then assessing the probability would help expand the range and make the probability assessment more realistic.

## **Assessing Scenarios**

The philosophy proposed here for assessing scenarios is as follows. Markets are understandable most (over 95%) of the time, but real asset prices have fat tails because extreme events occur much more frequently than lognormal or normal distributions indicate. According to Keim and Ziemba [20], much of asset returns are *not* predictable. Hence, we must have ways to combine conventional models, options pricing, and so on, which are accurate most of the time with the irrational unexplainable aspects that occur once in a while. Whether the extreme events are predictable is not the key issue—what is *crucial* is that we consider that they can happen in various levels with various chances.

*Even apart from the instability due to speculation, there is the instability due to the characteristic of human nature that a large proportion of our positive activities depend on spontaneous optimism rather than mathematical expectations, whether moral or hedonistic or economic. Most, probably, of our decision to do something positive, the full consequences of which will be drawn out over many days to come, can only be taken as the result of animal spirits, a spontaneous urge to action rather than inaction, and not as the outcome of a weighted average of quantitative benefits multiplied by quantitative probabilities* [21].

*Human behavior is a main factor in how markets act. Indeed, sometimes markets act quickly, violently with little warning. Ultimately, history tells us that there will be a correction of some significant dimension. I have no doubt that human nature being what it is, that it is going to happen again and again* [14].

As a working background hypothesis, we assume that markets are basically efficient most of the time, so we have to deal with that plus the anomaly and behavioral finance departures from efficiency.

## **Dynamic and Liability Aspects**

Figure 1 shows the time flow of assets arriving and liability commitments leaving for institutions, such as insurance companies, pension funds, banks, and individuals.

![](_page_2_Figure_13.jpeg)

**Figure 1** Time flow of assets: (a) institutions and (b) individuals

(b)

College Retirement

Ziemba and Mulvey [32] suggest the following risk ladder with various levels of details, aggregation, and model decisions.

- *Rung 5* : Total integrated risk management.
- *Rung 4* : Dynamic asset and liability management.
- *Rung 3* : Dynamic asset-only.
- *Rung 2* : Static asset-only portfolios.
- *Rung 1:* Pricing single securities.

This article concerns mostly Rung 3 and, especially, Rung 4. Rung 5 represents overall companywide models that involve all aspects of a business; see [26].

The stochastic programming approach, which considers the following aspects, is ideally suited to analyze such problems. It is argued that it has the following elements.

- Multiple time periods; possible use of end effects—steady state after decision horizon adds one more decision period to the model; the tradeoff is to have either an end-effects period or a larger model with one less period. The Russell–Yasuda Kansai model uses end effects while the InnoALM model does not.
- The scenarios should be consistent with economic and financial theory for asset returns, interest rates, and bond prices with anomaly and behavioral finance scenarios included.
- Discrete scenarios for random elements—returns, liabilities, and currencies.
- Scenario-dependent correlation matrices so that correlations change for extreme scenarios. This was first implemented in the InnoALM model. Since bond prices rise during stock market crashes, these assets are negatively correlated then but they are positively correlated otherwise. Thus, capturing this effect with one correlation matrix will not work. One simply needs multiple correlation matrices for scenarios sets. The LTCM and October 27–28, 1997 crash examples discussed in [31] remind one of the importance of this.
- The use of various forecasting models that can handle fat tails.
- Institutional, legal, and policy constraints.
- Model derivatives and illiquid assets.
- Model the transaction costs.
- Use expressions of risk in terms understandable to decision makers item.

- Simple, easy-to-understand concave, piecewise linear, risk-averse utility functions that maximize long-run expected profits, net of expected discounted penalty costs for shortfalls, are suggested. One pays more penalty for shortfalls as they increase (highly preferable to Value-at-Risk (VaR)).
- Model as constraints or penalty costs for target violations in the objective function. This allows for multiple goals through targets within periods and across periods. However, one must be able to specify the relative importance of these targets within periods and across periods.
- Adequate reserves, cash levels, and regularity requirements must be maintained.
- Realistic multiperiod problems can now be solved on modern workstations and personal computers by using large-scale linear programming and stochastic programming algorithms.
- The model makes one diversify—the key for keeping out of trouble.

Some possible approaches to model situations with such events are as follows:

- Simulation models have very large output to understand but are very useful as a check. Stochastic programming (SP) models are useful because they can easily perform stress tests and what if calculations.
- Mean–variance models are static in nature and useful for such applications, but they are not very useful with liquidity or other constraints or for multiperiod problems or with liabilities, and so on.
- Expected log models yield very risky short-term strategies that do not diversify well; fractional Kelly with downside constraints is excellent for risky investment betting [23, 30].
- Many stochastic control models, although theoretically interesting, give hair-trigger and bang-bang policies in which one is 100% stocks and then 0% stocks one second later (*see* **Stochastic Control**; **Uncertain Volatility Model**). See, for example, the Brennan and Schwartz model [3] in [32] and the Rudolf and Ziemba model [27]. The question is how to constrain the asset weight changes to be practical. Possibly, the best work with this approach has been done by Campbell and Viceira [4], who used the approach successfully to analyze long-term asset-only allocation decisions in

which the power of the technique dominates the limitations of the model (which they acknowledge). Among other conclusions, they show the following:

- 1. The riskless asset for a long-term investor is not Treasury-bills; rather, it is an inflation-indexed bond since it delivers a predictable stream of real income.
- 2. A safe labor income stream is equivalent to a large position in the risk-free asset, allowing the investor to hold much more in risky assets; then, this is reversed to some extent. Fixed commitments are negative income.
- 3. Risky investments are extremely attractive to young households because they have large relatively safe human wealth relative to their financial wealth.
- 4. Business owners should have less equity exposure since their income stream is correlated with the stock market.
- 5. Wealthy investors should be more risk averse since more of their consumption stream depends on their financial success.
- 6. Since stocks are mean reverting, that is, they have lower risk over longer time horizons, investors can time the market over longer horizons; since the equity risk premium is time varying, the optimal strategic allocation mix changes over time. These are useful rules of thumb for many investors derived from a theoretically sound framework. The goal in SP-ALM models is to tailor the asset-allocation mix for the particular institution or investor given their consumption and other goals, taxes, preferences, uncertainties, transactions costs, liquidity, and so on.
- 7. Stochastic programming models with decision rules have policy prescriptions, such as fixed mix or buy and hold; the decision rules are intuitively appealing but are suboptimal and usually lead to nonconvex difficult optimization modeling.

## **Stochastic Programming is Superior** to Fixed Mix

Despite their good results, fixed-mix and buy-andhold strategies do not use new information from return outcomes in their asset allocation (see Fixed Mix Strategy). Indeed, their asset allocation is fixed independent of all new information. Hence, a stochastic programming model that reacts to such information should be superior. For an example of this, see [31].

Fleten *et al.* [11] compared two versions, namely, multistage stochastic linear programming and fixedmix, of a portfolio model for the Norwegian life insurance company Gjensidige NOR. They found that the multiperiod stochastic programming model dominated the fixed-mix approach. However, the degree of dominance was much smaller out of sample than in sample (Figure 2).

Why does the SP advantage decrease so much? The answer seems to be that out of sample, the random input data are structurally different from those in sample, so the stochastic programming model

![](_page_4_Figure_14.jpeg)

Figure 2 Advantage of stochastic programming over fixed-mix model: (a) in-sample results and (b) out-ofsample results [Reproduced from Fleten et al., 2002. © Elsevier.]

loses its advantage in optimally adapting to the information available in the scenario tree. In addition, the performance of the fixed-mix approach improves because the asset mix is updated at each stage through its volatility pumping procedure.

## **The Russell–Yasuda Kasai Model**

The Russell–Yasuda Kasai model was the first largescale multiperiod stochastic programming model implemented for a major financial institution (see [15]). The model was designed while the author was working as a consultant to the Frank Russell Company in Tacoma, Washington, from 1989 to 1991. Under the direction of Research Head Andy Turner, the team of David Carino, Taka Eguchi, David ˜ Myers, Celine Stacy, and Mike Sylvanus at Russell in Tacoma, Washington, implemented the model for the Yasuda Fire and Marine Insurance Company in Tokyo.

The Russell–Yasuda Kasai model was designed to satisfy the following need, as articulated by Kunihiko Sasamoto, director and deputy president of Yasuda Kasai:

*The liability structure of the property and casualty insurance business has become very complex, and the insurance industry has various restrictions in terms*

*of asset management. We concluded that existing models, such as Markowitz mean–variance, would not function well and that we needed to develop a new asset–liability management model.*

*The Russell-Yasuda Kasai model is now at the core of all asset–liability work for the firm. We can define our risks in concrete terms, rather than through an abstract, in business terms, measure like standard deviation. The model has provided an important side benefit by pushing the technology and efficiency of other models in Yasuda forward to complement it. The model has assisted Yasuda in determining when and how human judgment is best used in the asset–liability process* ([5], p. 49)

The full model is described in [6, 7]. Figure 3 shows the decision-making process. The Rusell–Yasuda Kasai model led to other Russell models (Table 1).

## **InnoALM: The Innovest Austrian Pension Fund Financial Planning Model**

Siemens Oesterreich, a part of the global Siemens Corporation, is the largest privately owned industrial company in Austria. Its businesses, with revenues of ¤2.4 billion in 1999, include information and communication networks, information and communication products, business services, energy and traveling technology, and medical equipment. Its pension fund,

![](_page_5_Figure_11.jpeg)

Note: UB, upper bound; LB, lower bound; CG, company growth.

**Figure 3** Yasuda Kasai's asset–liability decision-making process [Reproduced from Carino, 1994. ˜ INFORMS.]

established in 1998, is the largest corporate pension plan in Austria and is a DCP. More than 15 000 employees and 5000 pensioners are members of the pension plan, which had ¤510 million in assets under management as of December 1999.

Innovest Finanzdienstleistungs, the investment manager of the Siemens pension plan, was rated as the best plan in Austria. Various uncertain aspects, possible future economic scenarios, stocks, bonds, and other investments, transaction costs, liquidity, currency aspects, liability commitments over time, Austrian pension fund law, and company policy suggested that a good way to approach this asset–liability problem was *via* a multiperiod stochastic linear programming model. This model has innovative features, such as state-dependent correlation matrices, fat-tailed asset-return distributions, simple computational schemes, and output. InnoALM was developed in six months in 2000, with Geyer and Ziemba serving as consultants and with assistance from Herold and Kontriner from Innovest.

The liability side of the Siemens pension plan consists of employees for whom Siemens is contributing DCP payments and retired employees who receive pension payments. Contributions are based on a fixed fraction of salaries, which varies across employees. Active employees are assumed to be in steady state; thus, employees are replaced by a new employee with the same qualification and sex so that there are a constant number of similar employees. Newly employed staff start with less salary than retired staff, which implies that total contributions grow less rapidly than individual salaries.

The set of retired employees is modeled using Austrian mortality and marital tables. Widows receive 60% of the pension payments. Retired employees receive pension payments after reaching age 65 for men and 60 for women. Payments to retired employees are based on the individually accumulated contribution and the fund performance during active employment. The annual pension payments are based on a discount rate of 6% and the remaining life expectancy at the time of retirement. These annuities grow by 1.5% annually to compensate for inflation. Hence, the wealth of the pension fund must grow by 7.5% a year to match liability commitments. Another output of the computations is the expected annual net cash flow of plan contributions minus payments. Because the number of pensioners is rising faster than plan contributions, these cash flows are negative and the plan is declining in size.

The model determines the optimal purchases and sales for each of *N* assets in each of *T* planning periods. Typical asset classes used at Innovest are US, Pacific, European, and emerging market equities and US, UK, Japanese, and European bonds. The objective is to maximize the concave risk-averse utility function "expected terminal wealth" less convex penalty costs subject to various linear constraints. The effect of such constraints is evaluated in the examples that follow, including Austria's limits of 40% maximum in equities, 45% maximum in foreign securities, and 40% minimum in Eurobonds. The convex risk measure is approximated by a piecewise linear function, so the model is a multiperiod stochastic linear program. Typical targets that the model tries to achieve (and is penalized for if it does not) are for growth of 7.5% a year in wealth (the fund's assets) and for portfolio performance returns to exceed benchmarks. Excess wealth is placed into surplus reserves, and a portion of the excess is paid out in succeeding years.

| Table 1 |  |  | Russell business engineering models |  |
|---------|--|--|-------------------------------------|--|
|---------|--|--|-------------------------------------|--|

| Model                                   | Type of application             | Year<br>delivered | Number of<br>scenarios | Computer hardware                         |
|-----------------------------------------|---------------------------------|-------------------|------------------------|-------------------------------------------|
| Russell–Yasuch (Tokyo)                  | Property and casualty insurance | 1991              | 256                    | IBM RISC 6000                             |
| Mitsubishi Trust (Tokyo)                | Pension consulting              | 1994              | 2000                   | IBM RISC 6000 with<br>parallel processors |
| Swiss Bank Corp. (Basle)                | Pension consulting              | 1996              | 8000                   | IBM UNIX2                                 |
| Daido Life Insurance<br>Company (Tokyo) | Life insurance                  | 1997              | 25 600                 | IBM PC                                    |
| Banca Fideuram (Rome)                   | Assets only (personal)          | 1997              | 10 000                 | IBM UNIX2 and PC                          |
| Consulting Clients                      | Assets only (institutional)     | 1998              | Various                | IBM UNIX2 and PC                          |

![](_page_7_Figure_1.jpeg)

Figure 4 Elements of InnoALM [Reproduced from Geyer and Ziemba, 2008. © INFORMS.]

The elements of InnoALM are described in Figure 4. The interface to read in data and problem elements uses Excel. Statistical calculations use the program Gauss, and these data are fed into the IBM 0SL solver, which generates the optimal solution to the stochastic program. The output uses Gauss to generate various tables and graphs and retains key variables in memory to allow for future modeling calculations.

## Formulation of InnoALM as a Multistage **Stochastic Linear Programming Model**

The nonnegative decision variables are wealth (after transactions)  $W_{it}$ , and purchases  $P_{it}$  and sales  $S_{it}$  for each asset  $(i = 1, \ldots, N)$ . Purchases and sales are in periods  $t = 0, \ldots, T - 1$ . Purchases and sales are scenario dependent except for  $t = 0$ .

Wealth accumulates over time for a  $T$  period model according to

$$W_{i0} = W_i^{\text{init}} + P_{i0} - S_{i0}, \quad t = 0 \tag{1}$$

$$\tilde{W}_{i1} = \tilde{R}_{i1}W_{i0} + \tilde{P}_{i1} - \tilde{S}_{i1}, \quad t = 1 \tag{2}$$

$$\widetilde{W}_{it} = \widetilde{R}_{it}\widetilde{W}_{i,t-1} + \widetilde{P}_{it} - \widetilde{S}_{it}, \quad t = 2,\ldots,T-1$$
(3)

and

$$\tilde{W}_{iT} = \tilde{R}_{it}\,\tilde{W}_{i,T-1}, \quad t = T \tag{4}$$

where  $W_i^{\text{init}}$  is the prespecified initial value of asset *i*. There is no uncertainty in the initialization period  $t = 0$ . Tildes denote scenario-dependent random parameters or decision variables. Returns are associated with time intervals.  $R_{it}(t = 1, \ldots, T)$  are the (random) gross returns for asset *i* between  $t - 1$  and  $t$ . The scenario generation and statistical properties of returns are discussed below.

The budget constraints are

$$\sum_{i=1}^{N} P_{i0}(1 + tcp_i) = \sum_{i=1}^{N} S_{i0}(1 - tcs_i) + C_0 \ t = 0$$
(5)

and

$$\sum_{i=1}^{N} \tilde{P}_{it}(1 + tcp_i) = \sum_{i=1}^{N} \tilde{S}_{it}(1 - tcs_i) + C_t,$$
  
$$t = 1, \dots, T - 1 \tag{6}$$

where  $tcp_i$  and  $tcs_i$  denote asset-specific linear transaction costs for purchases and sales, and  $C_t$  is the fixed (nonrandom) net cashflow (inflow if positive).

Portfolio weights can be constrained over linear combinations (subsets) of assets or individual assets via ٠,

$$\sum_{i \in U} \tilde{W}_{it} - \theta_U \sum_{i=1}^N \tilde{W}_{it} \le 0 \tag{7}$$

and

$$-\sum_{i\in L}\tilde{W}_{it}+\theta_L\sum_{i=1}^N\tilde{W}_{it}\leq 0,\quad t=1,\ldots,T-1$$
(8)

where  $\theta_U$  is the maximum percentage and  $\theta_L$  is the minimum percentage of the subsets  $U$  and  $L$  of assets  $i = 1, \ldots, N$  included in the restrictions.  $\theta_U$ 's,  $\theta_L$ 's,  $U$ 's and  $L$ 's may be time dependent.

Risk is measured as a weighted discounted convex function of target violation shortfalls of various types in various periods. In a typical application, the deterministic wealth target  $\overline{W}_t$  is assumed to grow by 7.5% in each year. The wealth targets are modeled via

$$\sum_{i=1}^{N} (\tilde{W}_{it} - \tilde{P}_{it} + \tilde{S}_{it}) + \tilde{M}_{t}^{W} \geq \tilde{W}_{t}, \quad t+1, \ldots, T$$
(9)

where  $\tilde{M}^W_t$  are nonnegative wealth-target shortfall variables. The shortfall is penalized using a piecewise linear convex risk measure. Stochastic benchmark goals can also be set by the user and are similarly penalized for underachievement. The benchmark target  $\tilde{B}_t$  is scenario dependent. It is based on stochastic asset returns and fixed asset weights  $\alpha_i$  defining the benchmark portfolio

$$\tilde{B}_t = W_0 \sum_{j=1}^t \sum_{i=1}^N \alpha_i \tilde{R}_{ij} \tag{10}$$

The corresponding shortfall constraints are

$$\sum_{i=1}^{N} (\tilde{W}_{it} - \tilde{P}_{it} + \tilde{S}_{it}) + \tilde{M}_{t}^{B} \geq \tilde{B}_{t} \quad t = 1, \dots, T$$
(11)

where  $\tilde{M}_{t}^{B}$  is the benchmark-target shortfall. These shortfalls are also penalized with a piecewise linear convex risk measure. If total wealth exceeds the target, a fraction  $\gamma = 10\%$  of the exceeding amount is allocated to a reserve account and invested in the same way as other available funds. However, the wealth targets at future stages are adjusted. Additional nonnegative decision variables  $\tilde{D}_t$  are introduced and the wealth-target constraints become

$$\sum_{i=1}^{N} (\tilde{W}_{it} - \tilde{P}_{it} + \tilde{S}_{it}) - \tilde{D}_{t} + \tilde{M}_{t}^{W}$$
$$= \overline{W}_{t} + \sum_{j=1}^{t-1} \gamma \tilde{D}_{t-j}, \quad t = 1, \dots, T-1 \quad (12)$$

where  $\tilde{D}_1 = 0$ .

Since pension payments are based on wealth levels, increasing these levels increases pension payments. The reserves provide security for the pension plan's increase in pension payments at each future stage.

The pension plan's objective function is to maximize the expected discounted value of terminal wealth in period  $T$  net of the expected discounted penalty costs over the horizon from the convex risk measures  $c_k(\cdot)$  for the wealth- and benchmark-targets, respectively,

$$\operatorname{Max}E\left[d_{T}\sum_{i=1}^{N}\tilde{W}_{iT}-\lambda\sum_{t=1}^{T}d_{t}w_{t}\right.\left.\times\left(\sum_{k\in\{W,B\}}\nu_{k}c_{k}(\tilde{M}_{t}^{k})\right)\right]\tag{13}$$

Expectation is over  $T$  period scenarios  $S_T$ . The discount factors  $d_t$  are related to the interest rate r by  $d_t = (1 + r)^{-t}$ . Usually r is taken to be the threeor six-month Treasury-bill rate.  $v_k$ 's are weights for the wealth- and benchmark-shortfalls and the  $w_t$ 's are weights for the weighted sum of shortfalls at each stage normalized via

$$\sum_{k \in \{W, B\}} v_k = 1 \quad \text{and} \quad \sum_{t=1}^{I} w_t = T \tag{14}$$

Such concave objective functions with convex risk measures date back to 1986 [22], were used in the Russell-Yasuda model [7] and are justified in an axiomatic sense in [25]. Nontechnical decision makers find the increasing penalty for target violations a good approach and easy to understand. Allocations are based on optimizing the stochastic linear program.

### Applications

Geyer and Ziemba [12] consider four asset classes (European stocks, US stocks, European bonds, and US bonds) with five periods (six stages): twice 1 year, twice 2 years, and 4 years (10 years in total). They assumed discrete compounding, so the mean return for asset *i* in simulations is  $\mu_i = \exp(\overline{y}_i) - 1$ where  $\overline{y}_i$  is the mean, based on log returns. Using a  $100-5-5-2-2$  node structure, they generated  $10000$ 

scenarios. Initial wealth is equal to 100 units, and the wealth target is assumed to grow at an annual rate of 7.5%. They used a risk-aversion index of *RA* = 4, and the discount factor is equal to 5%, which roughly corresponds with a simple static mean–variance model to a standard 60/40 stock/bond pension fund mix [19].

Assumptions about the statistical properties of returns measured in nominal euros are based on a sample of monthly data from January 1970 for stocks and 1986 for bonds to September 2000. Summary statistics for monthly and annual log returns are shown in Table 2. The US and European equity means for the longer period 1970–2000 were much lower and slightly less volatile than those for the period 1986–2000. The monthly stock returns were nonnormal and negatively skewed. Monthly stock returns were fat tailed, whereas monthly bond returns were close to normal (the critical value of the Jarque–Bera test for *a* = 0*.*01 is 9.2).

For long-term planning models such as InnoALM, with its one-year review period, however, properties of monthly returns are less relevant. Table 2 shows statistics for annual returns. Although average returns and volatilities remained about the same, one year of data is lost when annual returns are computed and the distributional properties changed significantly. There was negative skewness, but no evidence existed for fat tails in annual returns, except for European stocks (1970–2000) and US bonds.

The mean returns from this sample are comparable to the 1900–2000 101-year mean returns estimated by Dimson [9]. Their estimate of the nominal mean equity return was 12.0% for the United States and 13.6% for Germany and the United Kingdom (the simple average of the two countries means). They estimated mean of bond returns of 5.1% for the United States and 5.4% for Germany and the United Kingdom.

Assumptions about means, standard deviations, and correlations for the applications of InnoALM are listed in Table 3 and are based on the sample statistics presented in Table 4. Projecting future rates of returns from past data is difficult. The equity means from the 1970 to 2000 period are used because the 1986–2000 period had an exceptionally high performance of stocks that is not assumed to prevail in the long run.

The correlation matrices in Table 3 for the three different regimes are based on the regression approach of Solnik *et al.* [29]. Moving average estimates of correlations among all assets are functions of standard deviations of US equity returns. The estimated regression equations are then used to predict the correlations in the three regimes shown in Table 3. Results for the estimated regression equations appear in Table 4. Three regimes are considered, and the assumption is that 10% of the time, equity markets are extremely volatile; 20% of the time, markets are characterized by high volatility; and 70% of the time, markets are normal. The 35% quantile of US equity return volatility defines "normal"

|                           | European stocks |           |           | US stocks | European bonds | US bonds  |  |
|---------------------------|-----------------|-----------|-----------|-----------|----------------|-----------|--|
| Returns                   | 1/70–9/00       | 1/86–9/00 | 1/70–9/00 | 1/86–9/00 | 1/86–9/00      | 1/86–9/00 |  |
| Monthly                   |                 |           |           |           |                |           |  |
| Mean (%)(a)               | 10.60           | 13.30     | 10.70     | 14.80     | 6.50           | 7.20      |  |
| Standard deviation (%)(a) | 16.10           | 17.40     | 19.0      | 20.200    | 3.70           | 11.3      |  |
| Skewness                  | −0.90           | −1.43     | −0.72     | −1.04     | −0.50          | 0.52      |  |
| Kurtosis                  | 7.05            | 8.43      | 5.79      | 7.09      | 3.25           | 3.30      |  |
| Jarque–Bera test          | 302.60          | 277.30    | 151.90    | 155.6     | 7.70           | 8.50      |  |
| Annual                    |                 |           |           |           |                |           |  |
| Mean (%)                  | 11.10           | 13.30     | 11.0      | 15.20     | 6.50           | 6.90      |  |
| Standard deviation (%)    | 17.20           | 16.20     | 20.10     | 18.40     | 4.80           | 12.10     |  |
| Skewness                  | −0.53           | −0.10     | −0.23     | −0.28     | −0.20          | −0.42     |  |
| Kurtosis                  | 3.23            | 2.28      | 2.56      | 2.45      | 2.25           | 2.26      |  |
| Jarque–Bera test          | 17.40           | 3.90      | 6.20      | 4.20      | 5.00           | 8.70      |  |

**Table 2** Statistical properties of asset returns

Reproduced from Geyer and Ziemba, 2008. INFORMS

*(*a*)* Annualized

| Asset class                       | European stocks | US stocks | European bonds | US bonds |  |
|-----------------------------------|-----------------|-----------|----------------|----------|--|
| Normal periods (70% of the time)  |                 |           |                |          |  |
| US stocks                         | 0.755           |           |                |          |  |
| European bonds                    | 0.334           | 0.286     |                |          |  |
| US bonds                          | 0.514           | 0.780     | 0.333          |          |  |
| Standard deviation                | 14.6%           | 17.3%     | 3.3%           | 10.9%    |  |
| High volatility (20% of the time) |                 |           |                |          |  |
| US stocks                         | 0.786           |           |                |          |  |
| European bonds                    | 0.171           | 0.100     |                |          |  |
| US bonds                          | 0.435           | 0.715     | 0.159          |          |  |
| Standard deviation                | 19.2%           | 21.1%     | 4.1%           | 12.4%    |  |
| Estreme periods (10% of the time) |                 |           |                |          |  |
| US stocks                         | 0.832           |           |                |          |  |
| European bonds                    | −0.075          | −0.182    |                |          |  |
| US bonds                          | 0.315           | 0.618     | −0.104         |          |  |
| Standard deviation                | 21.7%           | 27.1%     | 4.4%           | 12.9%    |  |
| Average period                    |                 |           |                |          |  |
| US stocks                         | 0.769           |           |                |          |  |
| European bonds                    | 0.261           | 0.202     |                |          |  |
| US bonds                          | 0.478           | 0.751     | 0.255          |          |  |
| Standard deviation                | 16.4%           | 19.3%     | 3.6%           | 11.4%    |  |
| All periods                       |                 |           |                |          |  |
| Mean                              | 10.6%           | 10.7%     | 6.5%           | 7.2%     |  |

**Table 3** Mean, standard deviation, and correlation assumptions

Reproduced from Geyer and Ziemba, 2008. INFORMS

| Table 4 |  |  |  |  |  |  |  | Regression equations relating asset correlations and US stock return volatility |  |
|---------|--|--|--|--|--|--|--|---------------------------------------------------------------------------------|--|
|---------|--|--|--|--|--|--|--|---------------------------------------------------------------------------------|--|

|                                |          | Slope with respect to |                      |      |
|--------------------------------|----------|-----------------------|----------------------|------|
| Correlation                    | Constant | US stock volatility   | t-Statistic of slope | R2   |
| European stocks–US stocks      | 0.62     | 2.7                   | 6.5                  | 0.23 |
| European stocks–European bonds | 1.05     | −14.4                 | −16.9                | 0.67 |
| European stocks–US bonds       | 0.86     | −7.0                  | −9.7                 | 0.40 |
| US stocks–European bonds       | 1.11     | −16.5                 | −25.2                | 0.82 |
| US stocks–US bonds             | 1.07     | −5.7                  | −11.2                | 0.48 |
| European bonds–US bonds        | 1.10     | −15.4                 | −12.8                | 0.54 |

Reproduced from Geyer and Ziemba, 2008. INFORMS

periods. "Highly volatile" periods are based on the 80% volatility quantile and "extreme" periods on the 95% quartile. The associated correlations reflect the return relationships that typically prevailed during those market conditions. The correlations show a distinct pattern across the three regimes. Correlations among stocks tend to increase as stock return volatility rises, whereas the correlations between stocks and bonds tend to decrease. European bonds may serve as a hedge for equities during extremely volatile periods because bond and stock returns, which are usually positively correlated, are then negatively correlated. This is a major reason using scenario-dependent correlation matrices is a major advance over the sensitivity of using one correlation matrix as is usually assumed.

Optimal portfolios were calculated for seven cases—with and without mixing of correlations and with normal, *t*-, and historical distributions. The "mixing" cases NM, TM, and HM use mixing correlations. Case NM assumes normal distributions for all assets. Case HM uses the historical distributions of each asset. Case TM assumes *t*-distributions with five degrees of freedom for stock returns, whereas bond returns are assumed to have normal

| Case                                                                               |       |      | European stocks US stocks European bonds US bonds |      |
|------------------------------------------------------------------------------------|-------|------|---------------------------------------------------|------|
| Single-period, mean-variance optimal weights (average<br>periods)                  | 34.8% | 9.6% | 55.6%                                             | 0.0% |
| NA: No-mixing (average periods) normal distributions                               | 27.2  | 10.5 | 62.3                                              | 0.0  |
| HA: No-mixing (average periods) historical distributions                           | 40.0  | 4.1  | 55.9                                              | 0.0  |
| TA: No-mixing (average periods) $t$ -distributions for stocks                      | 44.2  | 1.1  | 54.7                                              | 0.0  |
| NM: Mixing correlations normal distributions                                       | 47.0  | 27.6 | 25.4                                              | 0.0  |
| HM: Mixing correlations historical distributions                                   | 37.9  | 25.2 | 36.8                                              | 0.0  |
| TM: Mixing correlations $t$ -distributions for stocks                              | 53.4  | 11.1 | 35.5                                              | 0.0  |
| TMC: Mixing correlations historical distributions;<br>constraints on asset weights | 35.1  | 4.9  | 60.0                                              | 0.0  |

Table 5 Optimal initial asset weights at Stage 1 by case

Reproduced from Geyer and Ziemba, 2008. © INFORMS

distributions. The "average" cases NA, HA, and TA use the same distribution assumptions, with no mixing of correlation matrices. Instead, the correlations and standard deviations used in these cases correspond to an "average" period in which 10, 20, and 70% weights are used to compute the averages of correlations and standard deviations in the three different regimes. Comparisons of the average (A) cases and mixing (M) cases are mainly intended to investigate the effect of mixing correlations. TMC maintains all assumptions of case TM but uses Austria's constraints on asset weights (see Table 5). Eurobonds must be at least  $40\%$  and equity at most 40%, and these constraints are binding. Tables 5 and 6 exhibit a distinct pattern: the mixing-correlation cases initially assign a much lower weight to European bonds than the average-period cases. Single-period, mean-variance optimization, and average-period cases (NA, HA, and TA) suggest an approximate 45%/55% stock/bond mix. The mixing-correlation cases (NM, HM, and TM) imply a  $65\%/35\%$  stock/bond mix. Investing in US bonds is not optimal at Stage 1 in any of the cases, an apparent result of the relatively high volatility of US bonds.

Table 6 shows that the distinction between A and M cases becomes less pronounced over time. European equities, however, still have a consistently higher weight in the mixing cases than in the nomixing cases. This higher weight is mainly at the expense of Eurobonds. In general, the proportion of equities at the final stage is much higher than in the first stage. This result may be explained by the fact that the expected portfolio wealth at later stages is far above the target wealth level  $(206.1 \text{ at }$ Stage 6), and the higher risk associated with stocks is less important. The constraints in case TMC lead to lower expected portfolio wealth throughout the horizon and to a higher shortfall probability than in any other case. Calculations show that the initial wealth would have to be 35% higher to compensate for the loss in terminal expected wealth stemming from those constraints. In all cases, the optimal weight of equities is much higher than the historical  $4.1\%$  in Austria.

The expected terminal wealth levels and the shortfall probabilities at the final stage shown in Table 6 make the difference between mixing and no-mixing cases even clearer. The mixing-correlation cases yield higher levels of terminal wealth and lower shortfall probabilities.

If the level of portfolio wealth exceeds the target, the surplus,  $D_i$ , is allocated to a reserve account. The reserves in t are computed from  $\sum_{j=1}^{t} \tilde{D}_j$  and are shown in Table 6 for the final stage. These values are in monetary units given an initial wealth level of 100. They can be compared with the wealth target 206.1 at Stage 6. Expected reserves exceed the target level at the final stage by up to 16%. Depending on the scenario, the reserves can be as high as  $1800$ . Their standard deviation (across scenarios) ranges from 5 at the first stage to 200 at the final stage. The constraints in case TMC lead to a much lower level of reserves compared with the other cases, which implies, in fact, less security against future increases in pension payments.

Optimal allocations, expected wealth, and shortfall probabilities are mainly affected by considering mixing correlations, but the type of distribution chosen has a smaller impact. This distinction is primarily the result of the higher proportion allocated to equities,

| Table 6<br>Case | Final stage results |              |                   |             |                             |                                 |                                    |  |  |
|-----------------|---------------------|--------------|-------------------|-------------|-----------------------------|---------------------------------|------------------------------------|--|--|
|                 | European<br>stocks  | US<br>stocks | European<br>bonds | US<br>bonds | Expected<br>terminal wealth | Expected reserves<br>at Stage 6 | Probability of<br>target shortfall |  |  |
| NA              | 34.3%               | 49.6%        | 11.7%             | 4.4%        | 328.9                       | 202.8                           | 11.2%                              |  |  |
| HA              | 33.5                | 48.1         | 13.6              | 4.8         | 328.9                       | 205.2                           | 13.7                               |  |  |
| TA              | 35.5                | 50.2         | 11.4              | 2.9         | 327.9                       | 202.2                           | 10.9                               |  |  |
| NM              | 38.0                | 49.7         | 8.3               | 4.0         | 349.8                       | 240.1                           | 9.3                                |  |  |
| HM              | 39.3                | 46.9         | 10.1              | 3.7         | 349.1                       | 235.2                           | 10.0                               |  |  |
| TM              | 38.1                | 51.5         | 7.4               | 2.9         | 342.8                       | 226.6                           | 8.3                                |  |  |
| TMC             | 20.4                | 20.8         | 46.3              | 12.4        | 253.1                       | 86.9                            | 16.1                               |  |  |

Reproduced from Geyer and Ziemba, 2008. INFORMS

if different market conditions are taken into account by mixing correlations.

The results of any asset-allocation strategy crucially depend on the expected returns. Geyer and Ziemba investigated the effect by parameterizing the forecasted expected equity returns. Assume that an econometric model forecasts that the future return for US equities is between 5 and 15%. The mean of European equities is adjusted accordingly so that the ratio of equity means and the mean bond returns shown in Table 6 is maintained. Geyer and Ziemba retain all other assumptions of case NM (normal distribution and mixing correlations). As expected, the results are sensitive to the choice of the mean return; see [8] and [18, 19]. If the mean return for US stocks is assumed to equal the long-run mean of 12%, as estimated in [9], the model yields an optimal weight for equities of 100%. A mean return for US stocks of 9%, however, implies an optimal weight of less than 30% for equities.

Positive effects on the pension fund performance induced by the stochastic, multiperiod planning approach will be realized only if the portfolio is dynamically rebalanced, as implied by the optimal scenario tree [12]. Figure 5 compares the cumulated monthly returns obtained from the rebalancing strategy for the two cases with a buy-and-hold strategy that assumes that the portfolio weights on January 1992 were fixed at the optimal TM weights throughout the test period. In comparison to the buy-and-hold strategy or the performance using TA results, for which rebalancing does not account for different correlation and volatility regimes, rebalancing on the basis of the optimal TM scenario tree provided a substantial gain.

The model, developed in 2000, proved to be very useful. In 2006, Konrad Kontriner (Member of the Board) and Wolfgang Herold (Senior Risk Strategist) of Innovest stated:

*The InnoALM model... has become the only consistently implemented and fully integrated proprietary tool for assessing pension allocation issues within Siemens AG worldwide. [..] The key elements that make InnoALM superior to other consulting models are the flexibility to adopt individual constraints and target functions in combination with the broad and deep array of results, which allows to investigate individual, path dependent behavior of assets and liabilities as well as scenario based and Monte-Carlo like risk assessment of both sides. [..] The implementation of a scenario based asset allocation model will lead to more flexible allocation restraints that will allow for more risk tolerance and will ultimately result in better long term investment performance.*

# **Conclusions**

Some key points concerning the stochastic programming approach to asset-liability management are as follows:

- *Point 1* : Means are by far the most important part of the distribution of returns, especially the direction. One must estimate future means well or one can quickly travel in the wrong direction, which usually leads to losses or underperformance, or complete disaster if one is overlevered.
- *Point 2* : Mean–variance models are useful as a basic guideline when one is in an assets-only situation. Professionals adjust means using meanreversion, James–Stein, or truncated estimators and constrain output weights. Asset positions should not be changed unless the advantage of the change is significant. Mean–variance analysis should not be used with liabilities and other

![](_page_13_Figure_1.jpeg)

**Figure 5** Cumulative monthly returns for different strategies, 1992–2002 [Reproduced from Geyer and Ziemba, 2008. INFORMS.]

major market imperfections, except as a first test analysis.

- *Point 3* : Trouble arises when one overbets and a bad scenario occurs. Thus, overbetting should not be done when there is any possibility of a bad scenario occurring, unless the bet is protected by some type of hedge or stop loss.
- *Point 4* : Trouble is exacerbated when the expected diversification does not hold in the scenario that occurs. Thus, one must use scenario-dependent correlation matrices because simulations around historical correlation matrices are inadequate for extreme scenarios.
- *Point 5* : When a large decline in the stock market occurs, the positive correlation between stocks and bonds fails and they become negatively correlated. Thus, when the mean of the stock market is negative, bonds are more attractive, as is cash.
- *Point 6* : Stochastic programming scenario-based models are useful when one wants to look at aggregate overall decisions, with liabilities, liquidity, taxes, policy, legal, and other constraints, and have targets and goals one wants to achieve. It, thus, pays to make a complex stochastic programming model when a lot is at stake and the essential problem has many complications.
- *Point 7* : Other approaches, such as continuoustime finance, decision-rule-based stochastic programming, control theory, and so on, are useful

for problem insights and theoretical results. However in actual use, they may lead to disaster unless modified. Black and Scholes [2] option pricing theory infers that one can hedge perfectly with lognormal assets, which can lead to overbetting. Fat tails and jumps arise frequently and can occur without warning. Thus, one should be careful of the assumptions, including implicit ones, of theoretical models. The results should be used with caution no matter how complex and elegant the math or how smart or famous the author. Remember, one has to be very smart to lose millions and even smarter to lose billions.

• *Point 8* : One should not be concerned with getting all the scenarios exactly right when using stochastic programming models. Instead, one should worry about having the problem periods laid out reasonably and make sure the scenarios basically cover the means, the tails, and the chance of what could happen. If the current situation has never occurred before, use one that is similar to add scenarios. For a crisis in Brazil, use Russian crisis data, for example. The results of stochastic programming will give one good advice when times are normal and keep one out of severe trouble when times are bad. Those using stochastic programming models may lose 5, 10, or 15%, but they will not lose 50, 70, or 95%, as some investors and hedge funds have. Thus, if the scenarios are more or less accurate and the problem elements are reasonably modeled, stochastic programming will give good advice. One may slightly outperform in normal markets, but one will greatly outperform in bad markets when other approaches may blow up.

- *Point 9* : Advances in computing power and modeling expertise have made stochastic programming modeling much less expensive to implement. Such models, which are still complex and require approximately six months to develop and test, cost a couple of hundred thousand dollars. A small team can make a model for a complex organization quite quickly at fairly low cost compared with what is at stake.
- *Point 10* : Eventually, as more disasters occur and more successful stochastic programming models are built and used, they will become popular. Thus, the ultimate goal is to have them in regulations, such as VaR. Although VaR does more good than harm, its safety is questionable in many applications. Conditional VaR is an improvement, but for most people and organizations, the nonattainment of goals is more than proportional (i.e., convex) in the nonattainment.

# **References**

- [1] Abaffy, J., Bertocchi, M., Dupacov ˇ a, J. & Moriggia, V. ` (2000). On generating scenarios for bond portfolios, *Bulletin of the Czech Economic Society* February, 3–27.
- [2] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [3] Brennan, M.J. & Schwartz, E.S. (1998). The use of Treasury bill futures in strategies asset allocation program, in *Worldwide Asset and Liability Modeling*, W.T. Ziemba & J.M. Mulvey, eds, Cambridge University Press, pp. 205–228.
- [4] Campbell, J.Y. & Viceira, L.M. (2002). *Strategic Asset Allocation: Portfolio Choice for Long-term Investors*, Oxford University Press.
- [5] Carino, D.R., Kent, T., Myers, D.H., Stacy, C., Syl- ˜ vanus, M., Turner, A.L., Watanabe, K. & Ziemba, W.T. (1994). The Russell-Yasuda Kasai model: an asset/ liability model for a Japanese insurance company using multistage stochastic programming, *Interfaces* **24**, 29–49.
- [6] Carino, D., Myers, R. & Ziemba, W.T. (1998). Con- ˜ cepts, technical issues and uses of the Russell-Yasuda Kasai financial planning model, *Operations Research* **46**, 450–462.

- [7] Carino, D. & Ziemba, W.T. (1998). Formulation of ˜ Russell-Yasuda Kasai financial planning model, *Operations Research* **46**, 433–449.
- [8] Chopra, V.K. & Ziemba, W.T. (1993). The effect of errors in mean, variance and co-variance estimates on optimal portfolio choice, *Journal of Portfolio Management* **19**, 6–11.
- [9] Dimson, E., Marsh, P. & Staunton, M. (2002). *Triumph of the Optimists*. Princeton University Press.
- [10] Dupacov ˇ a, J., Consigli, G. & Wallace, S.W. (2000). ` Scenarios for multistage stochastic programs, *Annals of Operations Research* **100**, 25–53.
- [11] Fleten, S.-E., Høyland, K. & Wallace, S. (2002). The performance of stochastic dynamic and fixed mix portfolio models, *European Journal of Operational Research* **140**(1), 37–49.
- [12] Geyer, A. & Ziemba, W.T. (2008). The innovest Austrian pension fund financial planning model InnoALM, *Operations Research* **56**(4), 797–810.
- [13] Grauer, R.R. & Hakansson, N.H. (1998). On naive approaches to timing the market: the empirical probability assessment approach with an inflation adapter, in *World Wide Asset and Liability Modeling*, W.T. Ziemba, & J.M. Mulvey, eds, Cambridge University Press, pp. 149–181.
- [14] Greenspan, A. (1998). *Speech before the Committee on Banking and Social Services*, US House of Representatives.
- [15] Henriques, D.B. (1991). A better way to back your assets, *New York Times* March, Section 3 (Business), 11.
- [16] Hochreiter, R. & Pflug, G.C. (2003). *Scenario Generation for Stochastic Multi-stage Decision Processes as Facility Location Problems*, *Technical report*. Department of Statistics and Decision Support Systems, University of Vienna.
- [17] Høyland, K. & Wallace, S.W. (2001). Generating scenario trees for multistage decision problems, *Management Science* **47**, 295–307.
- [18] Kallberg, J.G. & Ziemba, W.T. (1981). Remarks on optimal portfolio selection, in *Methods of Operations Research*, G. Bamberg & O. Optiz, eds, Gunn and Hain, Oelgeschlager, Vol. 44, pp. 507–520.
- [19] Kallberg, J.G. & Ziemba, W.T. (1983). Comparison of alternative utility functions in portfolio selection problems, *Management Science* **29**, 1257–1276.
- [20] Keim, D. & Ziemba, W.T. (eds) (2000). *Security Market Imperfections in Worldwide Equity Markets*, Cambridge University Press.
- [21] Keynes, J.M. (1938). *Investment Policy Report on the Chest Fund*, Kings College, Cambridge, UK.
- [22] Kusy, M.I. & Ziemba, W.T. (1986). A bank asset and liability management model, *Operations Research* **34**(3), 356–376.
- [23] MacLean, L. & Ziemba, W.T. (2006). Capital growth theory and practice, in *Handbook of Asset and Liability Modeling*, S.A. Zenios & W.T. Ziemba, eds, On theory and methodology, North Holland, Amsterdam, Vol. 1, pp. 429–475.

- [24] Markowitz, H.M. & Perold, A. (1981). Portfolio analysis with factors and scenarios, *Journal of Finance* **36**, 871–877.
- [25] Rockafellar, T. & Ziemba, W.T. (2000). *Modified Risk Measures and Acceptance Sets*. Working Paper, University of Washington.
- [26] Rosen, D. & Zenios, S.A. (2006). Enterprise-wide asset and liability management: issues, institutions, and models, in *Theory and Methodology, Handbook of Asset and Liability Modeling*, S.A. Zenios & W.T. Ziemba, eds, North-Holland, Amsterdam, Vol. 1, pp. 1–23.
- [27] Rudolf, M. & Ziemba, W.T. (2004). Intertemporal surplus management, *Journal of Economic Dynamics and Control* **28**(4), 975–990.
- [28] Shapiro, J.F. (1988). Stochastic programming models for dedicated portfolio selection, in *Mathematical Models for Decision Support*, G.B. Mitra, ed., ASI Series, Springer-Verlag, Berlin, Vol. F48, pp. 587–611.
- [29] Solnik, B., Boucrelle, C. & Le Fur, Y. (1996). International market correlation and volatility, *Financial Analysts Journal* **52**, 17–34.
- [30] Thorp, E.O. (2006). The Kelly criterion in blackjack, sports betting and the stock market, in *Handbook of Asset and Liability Modeling*, S.A. Zenios & W.T. Ziemba, eds, On theory and methodology, North Holland, Amsterdam, Vol. 1, 385–428.
- [31] Ziemba, W.T. (2007). The Russell Yasuda Kasai, InnoALM and related models for pensions, insurance companies and high net worth individuals, in *Handbook of Asset and Liability Management*, S.A. Zenios & W.T.

Ziemba, eds, Applications and Case Studies, North Holland, Amsterdam, The Netherlands, Vol. 2, pp. 861–962.

[32] Ziemba, W.T. & Mulvey, J.M. (eds) (1998). *World Wide Asset and Liability Modeling*, Cambridge University Press.

# **Further Reading**

- Kallberg, J.G., White, R. & Ziemba, W.T. (1982). Short term financial planning under uncertainty. *Management Science* **XXVIII**, 670–682.
- Ziemba, W.T. (2003). *The Stochastic Programming Approach to Asset Liability and Wealth Management*, AIMR, Charlottesville, Virginia.
- Ziemba, R.E.S. & Ziemba, W.T. (2007). *Scenarios for Risk management and Global Investment Strategies*, John Wiley & Sons, Chichester, England.

# **Related Articles**

**Expected Shortfall**; **Fixed Mix Strategy**; **Kelly Problem**; **Mean–Variance Hedging**; **Mutual Funds**; **Performance Measures**; **Risk–Return Analysis**; **Stochastic Control**; **Stress Testing**; **Stylized Properties of Asset Returns**; **Value-at-Risk**.

WILLIAM T. ZIEMBA
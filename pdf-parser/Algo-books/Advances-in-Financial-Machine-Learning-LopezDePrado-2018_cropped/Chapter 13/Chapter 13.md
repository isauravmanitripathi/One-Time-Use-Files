# **CHAPTER 13**

# **Backtesting on Synthetic Data**

## **13.1 Motivation**

In this chapter we will study an alternative backtesting method, which uses history to generate a synthetic dataset with statistical characteristics estimated from the observed data. This will allow us to backtest a strategy on a large number of unseen, synthetic testing sets, hence reducing the likelihood that the strategy has been fit to a particular set of datapoints. <sup>1</sup> This is a very extensive subject, and in order to reach some depth we will focus on the backtesting of trading rules.

## **13.2 Trading Rules**

Investment strategies can be defined as algorithms that postulate the existence of a market inefficiency. Some strategies rely on econometric models to predict prices, using macroeconomic variables such as GDP or inflation; other strategies use fundamental and accounting information to price securities, or search for arbitrage-like opportunities in the pricing of derivatives products, etc. For instance, suppose that financial intermediaries tend to sell off-the-run bonds two days before U.S. Treasury auctions, in order to raise the cash needed for buying the new "paper." One could monetize on that knowledge by selling off-the-run bonds three days before auctions. But how? Each investment strategy requires an implementation tactic, often referred to as "trading rules."

There are dozens of hedge fund styles, each running dozens of unique investment strategies. While strategies can be very heterogeneous in nature, tactics are relatively homogeneous. Trading rules provide the algorithm that must be followed to enter and exit a position. For example, a position will be entered when the strategy's signal reaches a certain value. Conditions for exiting a position are often defined through thresholds for profit-taking and stop-losses. These entry and exit rules rely on parameters that are usually calibrated via historical simulations. This practice leads to the problem of *backtest overfitting* , because these parameters target specific observations insample, to the point that the investment strategy is so attached to the past that it becomes unfit for the future.

An important clarification is that we are interested in the exit corridor conditions that maximize performance. In other words, the position already exists, and the question is how to exit it optimally. This is the dilemma often faced by execution traders, and it should not be mistaken with the determination of entry and exit thresholds for investing in a security. For a study of that alternative question, see, for example, Bertram [2009].

Bailey et al. [2014, 2017] discuss the problem of backtest overfitting, and provide methods to determine to what extent a simulated performance may be inflated due to overfitting. While assessing the probability of backtest overfitting is a useful tool to discard superfluous investment strategies, it would be better to avoid the risk of overfitting, at least in the context of calibrating a trading rule. In theory this could be accomplished by deriving the optimal parameters for the trading rule directly from the stochastic process that generates the data, rather than engaging in historical simulations. This is the approach we take in this chapter. Using the entire historical sample, we will characterize the stochastic process that generates the observed stream of returns, and derive the optimal values for the trading rule's parameters without requiring a historical simulation.

## 13.3 The Problem

Suppose an investment strategy *S* invests in  $i = 1, \dots, I$  opportunities or bets. At each opportunity *i* , *S* takes a position of  $m_i$  units of security *X* , where  $m_i \in ($  $-\infty$ , ∞). The transaction that entered such opportunity was priced at a value  $m_i$  $P_{i,0}$ , where  $P_{i,0}$  is the average price per unit at which the  $m_i$  securities were transacted. As other market participants transact security  $X$ , we can mark-tomarket (MtM) the value of that opportunity *i* after *t* observed transactions as  $m_i$  $P_{i,t}$ . This represents the value of opportunity *i* if it were liquidated at the price observed in the market after *t* transactions. Accordingly, we can compute the MtM profit/loss of opportunity *i* after *t* transactions as  $\pi_{i,t} = m_i (P_{i,t} - P_{i,0})$ .

A standard trading rule provides the logic for exiting opportunity *i* at  $t = T_i$ . This occurs as soon as one of two conditions is verified:

- $\pi_{i,T_i} \geq \bar{\pi}$ , where  $\bar{\pi} > 0$  is the profit-taking threshold.
- $\pi_{i,T_i} \leq \underline{\pi}$ , where  $\underline{\pi} < 0$  is the stop-loss threshold.

These thresholds are equivalent to the horizontal barriers we discussed in the context of meta-labelling (Chapter 3). Because , one and only one of the two exit conditions can trigger the exit from opportunity *i.* Assuming that opportunity *i* can be exited at *T <sup>i</sup>* , its final profit/loss is . At the onset of each opportunity, the goal is to realize an expected profit , where is the forecasted price and *P <sup>i</sup> , <sup>0</sup>* is the entry level of opportunity *i.*

**Definition 1: Trading Rule:** A trading rule for strategy *S* is defined by the set of parameters .

One way to calibrate (by brute force) the trading rule is to:

- 1. Define a set of alternative values of *R* , Ω: ={*R* }.
- 2. Simulate historically (backtest) the performance of *S* under alternative values of *R* ∈ Ω.
- 3. Select the optimal *R* \*.

<span id="page-2-1"></span>More formally:

$$R^* = \arg\max_{R \in \Omega} \{SR_R\}$$
$$SR_R = \frac{\mathrm{E}[\pi_{i,T_i}|R]}{\sigma[\pi_{i,T_i}|R]}$$

<span id="page-2-0"></span>where E[.] and σ[.] are respectively the expected value and standard deviation of , conditional on trading rule *R* , over *i* = 1, … *I* . In other words, equation ( [13.1](#page-2-1) ) maximizes the Sharpe ratio of *S* on *I* opportunities over the space of alternative trading rules *R* (see Bailey and López de Prado [2012] for a definition and analysis of the Sharpe ratio). Because we count with two variables to maximize *SR <sup>R</sup>* over a sample of size *I* , it is easy to overfit *R.* A trivial overfit occurs when a pair targets a few outliers. Bailey et al. [2017] provide a rigorous definition of backtest overfitting, which can be applied to our study of trading rules as follows.

#### **Definition 2: Overfit Trading Rule:** *R* \* is overfit if

$$\mathrm{E}\left[\frac{E\left[\left.\pi_{j,T_{j}}\middle|R^{*}\right]\right]}{\sigma\left[\left.\pi_{j,T_{j}}\middle|R^{*}\right]\right]} < \mathrm{Me}_{\Omega}\left[\mathrm{E}\left[\frac{E\left[\left.\pi_{j,T_{j}}\middle|R\right]\right]}{\sigma\left[\left.\pi_{j,T_{j}}\middle|R\right]\right]}\right], \text{ where } j = I+1, \ldots J \text{ and } \mathrm{Me}_{\Omega}\left[.\right]$$

is the median.

Intuitively, an optimal in-sample (IS, *i* ∈ [1, *I* ]) trading rule *R* \* is overfit when it is expected to underperform the median of alternative trading rules *R* ∈ Ω out-of-sample (OOS, *j* ∈ [ *I* + 1, *J* ]). This is essentially the same definition we used in chapter 11 to derive PBO. Bailey et al. [2014] argue that it is hard not to overfit a backtest, particularly when there are free variables able to target specific observations IS, or the number of elements in Ω is large. A trading rule introduces such free variables, because *R* \* can be determined independently from *S.* The outcome is that the backtest profits from random noise IS, making *R* \* unfit for OOS opportunities. Those same authors show that overfitting leads to negative performance OOS when Δπ *<sup>i</sup>* , *<sup>t</sup>* exhibits serial dependence. While PBO provides a useful method to evaluate to what extent a backtest has been overfit, it would be convenient to avoid this problem in the first place. <sup>2</sup> To that aim we dedicate the following section.

## **13.4 Our Framework**

Until now we have not characterized the stochastic process from which observations π *<sup>i</sup>* , *<sup>t</sup>* are drawn. We are interested in finding an optimal trading rule (OTR) for those scenarios where overfitting would be most damaging, such as when π *<sup>i</sup>* , *<sup>t</sup>* exhibits serial correlation. In particular, suppose a discrete Ornstein-Uhlenbeck (O-U) process on prices

$$(13.2) P_{i,t} = (1 - \varphi) E_0[P_{i,T_i}] + \varphi P_{i,t-1} + \sigma \varepsilon_{i,t}$$

<span id="page-3-1"></span><span id="page-3-0"></span>such that the random shocks are IID distributed ϵ *<sup>i</sup>* , *<sup>t</sup>* ∼ *N* (0, 1). The seed value for this process is *P <sup>i</sup> , <sup>0</sup>* , the level targeted by opportunity *i* is , and φ determines the speed at which *P <sup>i</sup> , <sup>0</sup>* converges towards . Because π *<sup>i</sup>* , *<sup>t</sup>* = *m <sup>i</sup>* ( *P <sup>i</sup> , <sup>t</sup>* − *P <sup>i</sup> , <sup>0</sup>* ), equation ( [13.2](#page-3-1) ) implies that the performance of opportunity *i* is characterized by the process

$$(13.3)^{\frac{1}{m_{i}}}\pi_{i,t} = (1-\varphi)\mathbf{E}_{0}[P_{i,T_{i}}] - P_{i,0} + \varphi P_{i,t-1} + \sigma \varepsilon_{i,t}$$

From the proof to Proposition 4 in Bailey and López de Prado [2013], it can be shown that the distribution of the process specified in equation ( [13.2](#page-3-1) ) is Gaussian with parameters

$$\pi_{i,t} \sim N\left[m_i\left((1-\varphi)\,\mathcal{E}_0[P_{i,T_i}]\sum_{j=0}^{t-1}\varphi^j - P_{i,0}\right), m_i^2\sigma^2\sum_{j=0}^{t-1}\varphi^{2j}\right]$$
(13.4)

and a necessary and sufficient condition for its stationarity is that φ ∈ ( − 1, 1). Given a set of input parameters {σ, φ} and initial conditions associated with opportunity *i* , is there an OTR ? Similarly, should strategy *S* predict a profit target , can we compute the optimal stop-loss given the input values {σ, φ}? If the answer to these questions is affirmative, no backtest would be needed in order to determine *R* \*, thus avoiding the problem of overfitting the trading rule. In the next section we will show how to answer these questions experimentally.

#### **13.5 Numerical Determination of Optimal Trading Rules**

In the previous section we used an O-U specification to characterize the stochastic process generating the returns of strategy *S.* In this section we will present a procedure to numerically derive the OTR for any specification in general, and the O-U specification in particular.

#### **13.5.1 The Algorithm**

The algorithm consists of five sequential steps.

**Step 1** : We estimate the input parameters {σ, φ}, by linearizing equation ( 13.2 ) as:

$$(13.5)P_{i,t} = \mathbf{E}_0[P_{i,T_i}] + \varphi(P_{i,t-1} - \mathbf{E}_0[P_{i,T_i}]) + \xi_t$$

We can then form vectors *X* and *Y* by sequencing opportunities:

$$X = \begin{bmatrix} P_{0,0} - \mathcal{E}_{0}[P_{0,T_{0}}] \\ P_{0,1} - \mathcal{E}_{0}[P_{0,T_{0}}] \\ \dots \\ P_{0,T-1} - \mathcal{E}_{0}[P_{0,T_{0}}] \\ \dots \\ P_{I,0} - \mathcal{E}_{0}[P_{I,T_{I}}] \\ \dots \\ P_{I,T-1} - \mathcal{E}_{0}[P_{I,T_{I}}] \end{bmatrix}; \ Y = \begin{bmatrix} P_{0,1} \\ P_{0,2} \\ \dots \\ P_{0,T} \\ \dots \\ P_{I,1} \\ \dots \\ P_{I,1} \\ \dots \\ P_{I,T} \end{bmatrix}; \ Z = \begin{bmatrix} \mathcal{E}_{0}[P_{0,T_{0}}] \\ \mathcal{E}_{0}[P_{0,T_{0}}] \\ \dots \\ \mathcal{E}_{0}[P_{0,T_{0}}] \\ \dots \\ \mathcal{E}_{0}[P_{I,T_{I}}] \\ \dots \\ \mathcal{E}_{0}[P_{I,T_{I}}] \end{bmatrix}$$

$$(13.6)$$

Applying OLS on equation ( 13.5 ), we can estimate the original O-U parameters as,

$$\hat{\varphi} = \frac{\text{cov}[Y, X]}{\text{cov}[X, X]}$$
$$\hat{\xi}_t = Y - Z - \hat{\varphi}X$$
$$(13.7)^{\hat{\sigma}} = \sqrt{\text{cov}[\hat{\xi}_t, \hat{\xi}_t]}$$

where cov[ ·, ·] is the covariance operator.

- **Step 2** : We construct a mesh of stop-loss and profit-taking pairs, . For example, a Cartesian product of and give us 20 × 20 nodes, each constituting an alternative trading rule *R* ∈ Ω.
- **Step 3** : We generate a large number of paths (e.g., 100,000) for π *<sup>i</sup>* , *<sup>t</sup>* applying our estimates . As seed values, we use the observed initial conditions associated with an opportunity *i.* Because a position cannot be held for an unlimited period of time, we can impose a maximum holding period (e.g., 100 observations) at which point the position is exited even though . This maximum holding period is equivalent to the vertical bar of the triple-barrier method (Chapter 3). <sup>3</sup>
- **Step 4** : We apply the 100,000 paths generated in Step 3 on each node of the 20 × 20 mesh generated in Step 2. For each node, we apply the stop-loss and profit-taking logic, giving us 100,000 values of . Likewise, for each node we compute the Sharpe ratio associated with that trading rule as described in equation ( 13.1 ). See Bailey and López de Prado [2012] for a study of the confidence interval of the Sharpe ratio estimator. This result can be used in three different ways: Step 5a, Step 5b and Step 5c).
- **Step 5a** : We determine the pair within the mesh of trading rules that is optimal, given the input parameters and the observed initial conditions .
- **Step 5b** : If strategy *S* provides a profit target for a particular opportunity *i* , we can use that information in conjunction with the results in Step 4 to determine the optimal stop-loss, .

**Step 5c** : If the trader has a maximum stop-loss imposed by the fund's management for opportunity *i* , we can use that information in conjunction with the results in Step 4 to determine the optimal profit-taking within the range of stop-losses .

Bailey and López de Prado [2013] prove that the half-life of the process in equation ( 13.2 ) is , with the requirement that φ ∈ (0, 1). From that result, we can determine the value of φ associated with a certain half-life τ as .

## **13.5.2 Implementation**

Snippet 13.1 provides an implementation in Python of the experiments conducted in this chapter. Function main produces a Cartesian product of parameters , which characterize the stochastic process from equation ( 13.5 ). Without loss of generality, in all simulations we have used σ = 1. Then, for each pair , function batch computes the Sharpe ratios associated with various trading rules.

#### **SNIPPET 13.1 PYTHON CODE FOR THE DETERMINATION OF OPTIMAL TRADING RULES**

Snippet 13.2 computes a 20 × 20 mesh of Sharpe ratios, one for each trading rule , given a pair of parameters . There is a vertical barrier, as the maximum holding period is set at 100 ( maxHP = 100 ). We have fixed *P <sup>i</sup> , <sup>0</sup>* = 0, since it is the distance in equation ( 13.5 ) that drives the convergence, not particular absolute price levels. Once the first out of three barriers is touched, the exit price is stored, and the next iteration starts. After all iterations are completed (1E5), the Sharpe ratio can be computed for that pair , and the algorithm moves to the next pair. When all pairs of trading rules have been processed, results are reported back to main . This algorithm can be parallelized, similar to what we did for the triple-barrier method in Chapter 3. We leave that task as an exercise.

#### **SNIPPET 13.2 PYTHON CODE FOR THE DETERMINATION OF OPTIMAL TRADING RULES**

## **13.6 Experimental Results**

[Table 13.1](#page-8-0) lists the combinations analyzed in this study. Although different values for these input parameters would render different numerical results, the combinations applied allow us to analyze the most general cases. Column "Forecast" refers to ; column "Half-Life" refers to τ; column "Sigma" refers to σ; column "maxHP" stands for maximum holding period.

#### <span id="page-8-0"></span>**Table 13.1 Input Parameter Combinations Used in the Simulations**

| Figure | Forecast | Half-Life | Sigma | maxHP |
|--------|----------|-----------|-------|-------|
| 16.1   | 0        | 5         | 1     | 100   |
| 16.2   | 0        | 10        | 1     | 100   |
| 16.3   | 0        | 25        | 1     | 100   |
| 16.4   | 0        | 50        | 1     | 100   |
| 16.5   | 0        | 100       | 1     | 100   |
| 16.6   | 5        | 5         | 1     | 100   |
| 16.7   | 5        | 10        | 1     | 100   |
| 16.8   | 5        | 25        | 1     | 100   |
| 16.9   | 5        | 50        | 1     | 100   |

| 16.10 | 5    | 100 | 1 | 100 |
|-------|------|-----|---|-----|
| 16.11 | 10   | 5   | 1 | 100 |
| 16.12 | 10   | 10  | 1 | 100 |
| 16.13 | 10   | 25  | 1 | 100 |
| 16.14 | 10   | 50  | 1 | 100 |
| 16.15 | 10   | 100 | 1 | 100 |
| 16.16 | − 5  | 5   | 1 | 100 |
| 16.17 | − 5  | 10  | 1 | 100 |
| 16.18 | − 5  | 25  | 1 | 100 |
| 16.19 | − 5  | 50  | 1 | 100 |
| 16.20 | − 5  | 100 | 1 | 100 |
| 16.21 | − 10 | 5   | 1 | 100 |
| 16.22 | − 10 | 10  | 1 | 100 |

| 16.23 | − 10 | 25  | 1 | 100 |
|-------|------|-----|---|-----|
| 16.24 | − 10 | 50  | 1 | 100 |
| 16.25 | − 10 | 100 | 1 | 100 |

In the following figures, we have plotted the non-annualized Sharpe ratios that result from various combinations of profit-taking and stop-loss exit conditions. We have omitted the negative sign in the y-axis (stop-losses) for simplicity. Sharpe ratios are represented in grayscale (lighter indicating better performance; darker indicating worse performance), in a format known as a heat-map. Performance ( ) is computed per unit held ( *m <sup>i</sup>* = 1), since other values of *m <sup>i</sup>* would simply re-scale performance, with no impact on the Sharpe ratio. Transaction costs can be easily added, but for educational purposes it is better to plot results without them, so that you can appreciate the symmetry of the functions.

## **13.6.1 Cases with Zero Long-Run Equilibrium**

Cases with zero long-run equilibrium are consistent with the business of market-makers, who provide liquidity under the assumption that price deviations from current levels will correct themselves over time. The smaller τ, the smaller is the autoregressive coefficient ( ). A small autoregressive coefficient in conjunction with a zero expected profit has the effect that most of the pairs deliver a zero performance.

Figure 13.1 shows the heat-map for the parameter combination . The half-life is so small that performance is maximized in a narrow range of combinations of small profit-taking with large stop-losses. In other words, the optimal trading rule is to hold an inventory long enough until a small profit arises, even at the expense of experiencing some 5-fold or 7-fold unrealized losses. Sharpe ratios are high, reaching levels of around 3.2. This is in fact what many market-makers do in practice, and is consistent with the "asymmetric payoff dilemma" described in Easley et al.

[2011]. The worst possible trading rule in this setting would be to combine a short stop-loss with a large profit-taking threshold, a situation that marketmakers avoid in practice. Performance is closest to neutral in the diagonal of the mesh, where profit-taking and stop-losses are symmetric. You should keep this result in mind when labeling observations using the triple-barrier method (Chapter 3).

![](_page_11_Figure_1.jpeg)

**Figure 13.1** Heat-map for

Figure 13.2 shows that, if we increase τ from 5 to 10, the areas of highest and lowest performance spread over the mesh of pairs , while the Sharpe ratios decrease. This is because, as the half-life increases, so does the magnitude of the autoregressive coefficient (recall that ), thus bringing the process closer to a random walk.

![](_page_12_Figure_0.jpeg)

**Figure 13.2** Heat-map for

In Figure 13.3 , τ = 25, which again spreads the areas of highest and lowest performance while reducing the Sharpe ratio. Figure 13.4 (τ = 50) and Figure 13.5 (τ = 100) continue that progression. Eventually, as φ → 1, there are no recognizable areas where performance can be maximized.

![](_page_13_Figure_0.jpeg)

**Figure 13.3** Heat-map for

![](_page_14_Figure_0.jpeg)

**Figure 13.4** Heat-map for

![](_page_15_Figure_0.jpeg)

**Figure 13.5** Heat-map for

Calibrating a trading rule on a random walk through historical simulations would lead to backtest overfitting, because one random combination of profittaking and stop-loss that happened to maximize Sharpe ratio would be selected. This is why backtesting of synthetic data is so important: to avoid choosing a strategy because some statistical fluke took place in the past (a single random path). Our procedure prevents overfitting by recognizing that performance exhibits no consistent pattern, indicating that there is no optimal trading rule.

## **13.6.2 Cases with Positive Long-Run Equilibrium**

Cases with positive long-run equilibrium are consistent with the business of a position-taker, such as a hedge-fund or asset manager. Figure 13.6 shows the results for the parameter combination . Because positions tend to make money, the optimal profit-taking is higher than in the previous cases, centered around 6, with stop-losses that range between 4 and

10. The region of the optimal trading rule takes a characteristic rectangular shape, as a result of combining a wide stop-loss range with a narrower profittaking range. Performance is highest across all experiments, with Sharpe ratios of around 12.

![](_page_16_Figure_1.jpeg)

![](_page_16_Figure_2.jpeg)

![](_page_16_Figure_3.jpeg)

In Figure 13.7 , we have increased the half-life from τ = 5 to τ = 10 *.* Now the optimal performance is achieved at a profit-taking centered around 5, with stop-losses that range between 7 and 10. The range of optimal profit-taking is wider, while the range of optimal stop-losses narrows, shaping the former rectangular area closer to a square. Again, a larger half-life brings the process closer to a random walk, and therefore performance is now relatively lower than before, with Sharpe ratios of around 9.

![](_page_17_Figure_0.jpeg)

**Figure 13.7** Heat-map for

In Figure 13.8 , we have made τ = 25 *.* The optimal profit-taking is now centered around 3, while the optimal stop-losses range between 9 and 10. The previous squared area of optimal performance has given way to a semi-circle of small profit-taking with large stop-loss thresholds. Again we see a deterioration of performance, with Sharpe ratios of 2.7.

![](_page_18_Figure_0.jpeg)

**Figure 13.8** Heat-map for

In Figure 13.9 , the half-life is raised to τ = 50 *.* As a result, the region of optimal performance spreads, while Sharpe ratios continue to fall to 0.8. This is the same effect we observed in the case of zero long-run equilibrium (Section 13.6.1), with the difference that because now , there is no symmetric area of worst performance.

![](_page_19_Figure_0.jpeg)

**Figure 13.9** Heat-map for

In Figure 13.10 , we appreciate that τ = 100 leads to the natural conclusion of the trend described above. The process is now so close to a random walk that the maximum Sharpe ratio is a mere 0.32.

![](_page_20_Figure_0.jpeg)

**Figure 13.10** Heat-map for

We can observe a similar pattern in Figures 13.11 through 13.15, where and τ is progressively increased from 5 to 10, 25, 50, and 100, respectively.

![](_page_21_Figure_0.jpeg)

**Figure 13.11** Heat-map for

![](_page_22_Figure_0.jpeg)

**Figure 13.12** Heat-map for

![](_page_23_Figure_0.jpeg)

**Figure 13.13** Heat-map for

![](_page_24_Figure_0.jpeg)

**Figure 13.14** Heat-map for

![](_page_25_Figure_0.jpeg)

**Figure 13.15** Heat-map for

### **13.6.3 Cases with Negative Long-Run Equilibrium**

A rational market participant would not initiate a position under the assumption that a loss is the expected outcome. However, if a trader recognizes that losses are the expected outcome of a pre-existing position, she still needs a strategy to stop-out that position while minimizing such losses.

We have obtained Figure 13.16 as a result of applying parameters . If we compare Figure 13.16 with Figure 13.6 , it appears as if one is a rotated complementary of the other. Figure 13.6 resembles a rotated photographic negative of Figure 13.16 . The reason is that the profit in Figure 13.6 is translated into a loss in Figure 13.16 , and the loss in Figure 13.6 is translated into a profit in Figure 13.16 . One case is a reverse image of the other, just as a gambler's loss is the house's gain.

![](_page_26_Figure_0.jpeg)

**Figure 13.16** Heat-map for

As expected, Sharpe ratios are negative, with a worst performance region centered around the stop-loss of 6, and profit-taking thresholds that range between 4 and 10. Now the rectangular shape does not correspond to a region of best performance, but to a region of worst performance, with Sharpe ratios of around −12.

In Figure 13.17 , τ = 10, and now the proximity to a random walk plays in our favor. The region of worst performance spreads out, and the rectangular area becomes a square. Performance becomes less negative, with Sharpe ratios of about −9.

![](_page_27_Figure_0.jpeg)

**Figure 13.17** Heat-map for

This familiar progression can be appreciated in Figures 13.18 , 13.19 , and 13.20 , as τ is raised to 25, 50, and 100. Again, as the process approaches a random walk, performance flattens and optimizing the trading rule becomes a backtest-overfitting exercise.

![](_page_28_Figure_0.jpeg)

**Figure 13.18** Heat-map for

![](_page_29_Figure_0.jpeg)

**Figure 13.19** Heat-map for

![](_page_30_Figure_0.jpeg)

**Figure 13.20** Heat-map for

Figures 13.21 through 13.25 repeat the same process for and τ that is progressively increased from 5 to 10, 25, 50, and 100. The same pattern, a rotated complementary to the case of positive long-run equilibrium, arises.

![](_page_31_Figure_0.jpeg)

**Figure 13.21** Heat-map for

![](_page_32_Figure_0.jpeg)

**Figure 13.22** Heat-map for

![](_page_33_Figure_0.jpeg)

**Figure 13.23** Heat-map for

![](_page_34_Figure_0.jpeg)

**Figure 13.24** Heat-map for

![](_page_35_Figure_0.jpeg)

**Figure 13.25** Heat-map for

### **13.7 Conclusion**

In this chapter we have shown how to determine experimentally the optimal trading strategy associated with prices following a discrete O-U process. Because the derivation of such trading strategy is not the result of a historical simulation, our procedure avoids the risks associated with overfitting the backtest to a single path. Instead, the optimal trading rule is derived from the characteristics of the underlying stochastic process that drives prices. The same approach can be applied to processes other than O-U, and we have focused on this particular process only for educational purposes.

While we do not derive the closed-form solution to the optimal trading strategies problem in this chapter, our experimental results seem to support the following OTR conjecture:

**Conjecture:** Given a financial instrument's price characterized by a discrete O-U process, there is a unique optimal trading rule in terms of a combination of profit-taking and stop-loss that maximizes the rule's Sharpe ratio.

Given that these optimal trading rules can be derived numerically within a few seconds, there is little practical incentive to obtain a closed-form solution. As it is becoming more common in mathematical research, the experimental analysis of a conjecture can help us achieve a goal even in the absence of a proof. It could take years if not decades to prove the above conjecture, and yet all experiments conducted so far confirm it empirically. Let me put it this way: The probability that this conjecture is false is negligible relative to the probability that you will overfit your trading rule by disregarding the conjecture. Hence, the rational course of action is to assume that the conjecture is right, and determine the OTR through synthetic data. In the worst case, the trading rule will be suboptimal, but still it will almost surely outperform an overfit trading rule.

## **Exercises**

- 1. Suppose you are an execution trader. A client calls you with an order to cover a short position she entered at a price of 100. She gives you two exit conditions: profit-taking at 90 and stop-loss at 105.
  - 1. Assuming the client believes the price follows an O-U process, are these levels reasonable? For what parameters?
  - 2. Can you think of an alternative stochastic process under which these levels make sense?
- 2. Fit the time series of dollar bars of E-mini S&P 500 futures to an O-U process. Given those parameters:
  - 1. Produce a heat-map of Sharpe ratios for various profit-taking and stop-loss levels.
  - 2. What is the OTR?
- 3. Repeat exercise 2, this time on a time series of dollar bars of
  - 1. 10-year U.S. Treasure Notes futures
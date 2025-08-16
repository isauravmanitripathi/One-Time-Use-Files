# **Gamma Hedging**

## **Why Hedging Gamma?**

Gamma is defined as the second derivative of a derivative product with respect to the underlying price. To understand why gamma hedging is not just the issue of annihilating a second-order term in the Taylor expansion of a portfolio, we review the profit and loss  $(P\&L)^a$  explanation of a delta-hedged selffinancing portfolio for a monounderlying option and its link to the gamma.

Let us consider an economy described by the Black and Scholes framework, with a riskless interest rate  $r$ , a stock  $S$  with no repo or dividend whose volatility is  $\sigma$ , and an option O written on that stock.

Let  $\Pi$  be a self-financing portfolio composed at  $t$  of

- the option  $O_t$ ;
- its delta hedge:  $-\Delta_t S_t$  with  $\Delta_t = \frac{\partial O}{\partial S}$ ; and
- the corresponding financing cash amount  $-O_t$  +  $\Delta_t S_t$ .

We note  $\delta \Pi$  the P&L of the portfolio between t and  $t + \delta t$  and we set  $\delta S = S_{t+\delta t} - S_t$ . Directly, we have that the delta part of the portfolio P&L is  $-\Delta_t \delta S$  and that the P&L of the financing part is  $(-O_t + \Delta_t S_t) r \delta t$ . Regarding the option P&L,  $\delta O$ , we have, by a second-order expansion,

$$\delta O \approx \frac{\partial O}{\partial t} \delta t + \frac{\partial O}{\partial S} \delta S + \frac{1}{2} \frac{\partial^2 O}{\partial^2 S} (\delta S)^2 \tag{1}$$

Furthermore, the option satisfies the Black and Scholes equation (see Black-Scholes Formula):

$$\frac{\partial O}{\partial t} + rS\frac{\partial O}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 O}{\partial^2 S} = rO \qquad (2)$$

Combining these two equations and writing the P&L of the portfolio as the sum of the three terms, we get

$$\delta \Pi \approx \frac{1}{2} S^2 \frac{\partial^2 O}{\partial^2 S} \left( \left( \frac{\delta S}{S} \right)^2 - \sigma^2 \delta t \right) \tag{3}$$

where  $\partial^2 O/\partial^2 S$  is the gamma of the option part of the portfolio (in terms of definition,  $S^2(\partial^2 O/\partial^2 S)$ is called the *cash gamma* because it is expressed in currency and can be summed over several stock positions, whereas the direct gamma cannot).

As no condition was put on the relation of the volatility to time and space, equation  $(3)$  is easily extended to a local volatility setting (see Local Volatility Model). Practitioners call this equation the breakeven relation and  $\sigma\sqrt{\delta t}$  the breakeven for it represents the move in performance the stock has to make in the time  $\delta t$  to ensure a flat P&L (e.g., if we consider that a year is composed of 256 open days, a stock having an annualized volatility of 16% needs to make a move of 1%, at which the delta is rebalanced, to ensure a flat P&L between two consecutive days). Figure 1 shows the portfolio P&L for a position composed of an option with a positive gamma.

Equation (3) leads to two important remarks. First, it is a local relation, both in time and space, and the fact that the gamma is gearing the breakeven relation implies that the global P&L of a positive gamma position, hedged according to the Black and Scholes self-financing strategy, can very well be negative if a stock makes large moves in a region where the gamma is small and makes small moves in a region where the gamma is maximum, even if the realized variance of the stock is higher than the pricing variance  $\sigma^2$ . Secondly, in the long run, the realized variance is usually smaller than the implied variance, which can lead practitioners to build negative gamma positions. Yet, Figure 1 shows that a positive gamma position is of finite loss and possibly infinite gain, whereas it is the opposite for a negative gamma position. Practically, this is why traders tend naturally to a gamma neutral position.

A specific aspect of the equity market is the presence of dividends. One can wonder if, on the date the stock drops by the dividend amount, a positive gamma position is easier to carry than a negative gamma position. It is, of course, linked to the dividend representation chosen in the stock modeling. It can be shown that the only consistent way of representing the dividends is the one proposed in **Dividend Modeling**, where the stock is modeled as in Black and Scholes between two consecutive dividend dates. It is the only representation in which equation (3) stands (on the dividend date, the P&L term coming from the cash dividend part is offset by a term arising from the adapted Black and Scholes equation). In others, either the gamma carries a dividend part (dividend yield models) that leads to a

![](_page_1_Figure_1.jpeg)

**Figure 1** The P&L of a self-financing portfolio composed of an option with a positive gamma in the interval  $\delta t$ 

false breakeven on the dividend date or equation (3) is not associated with the stock but with the variable that is stochastic (model in which the stock is described as a capitalized exponential martingale minus a capitalized dividend term, for example). This is why practitioners use the model proposed in **Dividend Modeling** rather than any other. This is also why it is, indeed, a general framework we put ourselves in by excluding dividends and repo (which is usually represented by a drift term whose P&L impact is also offset by a term arising from the adapted Black and Scholes equation) in our analysis.

## **Practical Gamma Hedging**

We have seen why traders usually try to build a gamma-neutral portfolio. Yet, there is no pure gamma instrument in the market, and neutralizing the gamma exposure always brings a vega exposure to the portfolio. Without trying to be exhaustive, we briefly review here some natural gamma hedging instruments.

#### Hedging Gamma with Vanilla Options

European calls and puts have the same gamma (and the same vega). Hence, they are equivalent hedging instruments. Figure 2 shows the gamma of a European option for two different maturities and Figure 3 shows the compared evolutions with respect to the maturity of the gamma and of the vega.

These two figures show that, to efficiently hedge his or her gamma exposure, a trader would rather use a short-term option to avoid bringing too much vega to his or her position. Moreover, the gamma of an "atthe-money" option is increasing as one gets closer to the maturity, whereas the gamma of an "out-of-themoney" option is decreasing.

## The Put Ratio Temptation

As equation  $(3)$  shows, the gamma and the theta (first derivative of a derivative product with respect to time) of a portfolio are of opposite signs. Moreover, in the equity market, the implied volatility is usually described by a skew, meaning that if we consider two puts  $P_1$  and  $P_2$  for the same maturity T, having two strikes  $K_1$  and  $K_2$  with  $K_1 < K_2$ , we classically have  $\sigma_{K_1} > \sigma_{K_2}$ . If we now build a self financing portfolio  $\n\Pi\n$  that is composed of  $P_2 - \alpha P_1$  with  $\alpha = \Gamma_2/\Gamma_1$ , the ratio of the two gammas, we get from equation (3) that  $\delta \Pi \approx \frac{1}{2} S^2 \Gamma_2 (\sigma_{K_1}^2 - \sigma_{K_2}^2) \delta t > 0.$ 

This result is not in contradiction with arbitrage theory; it only demonstrates that equation  $(3)$  is strictly a local relation. As shown by Figure 2, to keep this relation through time, the trader would have to continuously sell the put  $P_2$ , as  $\alpha$  increases as time to maturity decreases, and, in case of a market drop down, he or she would find himself in a massive negative gamma situation. Still, practitioners commonly use put ratios to improve the breakeven of their position.

![](_page_2_Figure_1.jpeg)

**Figure 2** Gamma of a European call as a function of the spot for two maturities (strike is equal to 100)

![](_page_2_Figure_3.jpeg)

**Figure 3** Compared evolution of the gamma and vega of an at-the-money European call as a function of maturity (scales are different)

## *Hedging Gamma with a Variance Swap or a Gamma Swap*

As explained in **Variance Swap** a variance swap is equivalent to a log contract. Hence, its cash gamma is constant. It is therefore an efficient gamma hedging instrument for a portfolio whose gamma is not particularly localized (as opposed to a portfolio of vanilla options whose gamma is locally described by Figure 2). Gamma swaps (*see* **Gamma Swap**) have the same behavior. Their specificity is to have a constant gamma.

#### *Extending the Definition of Gamma*

In the market, the implied volatility changes with the spot moves (*see* **Implied Volatility Surface**). It is in contradiction with the use of a Black and Scholes model whose volatility is constant, but, to avoid the multiplicity of risk sources, and to keep them observable, traders tend to rely on that model, nonetheless (and therefore hedge their vega exposure). Nevertheless, to take this dynamics into consideration, some traders incorporate a "shadow" term into their sensitivities. The shadow gamma [1] is defined as

$$\frac{\partial^2 O}{\partial^2 S} + \frac{\partial}{\partial S} \left( \frac{\partial O}{\partial \sigma} \frac{\partial \sigma}{\partial S} \right) \tag{4}$$

The second term, the shadow term, depends on the chosen dynamics of the implied volatility.

The problem with the shadow approach is that we cannot rely anymore on a self-financing strategy in the Black and Scholes framework to define the breakeven. One solution, in order to build a selffinancing strategy that incorporates volatility surface into the dynamics, is to use a stochastic volatility model (see Heston Model) instead of a Black and Scholes model. For example, one can use the following model:

$$dS = rS dt + \sigma S dW_t^1$$
  
$$d\sigma = \mu dt + \nu dW_t^2$$
 (5)

$$d\langle W^1, W^2\rangle_t = \rho dt$$

Using the same arguments as in the Black and Scholes framework, the P&L of a delta-hedged selffinancing portfolio (now with a first-order hedge for the volatility factor using a volatility instrument like a straddle, for example) in this model is

$$\delta \Pi \approx \frac{1}{2} S^2 \frac{\partial^2 O}{\partial^2 S} \left( \left( \frac{\delta S}{S} \right)^2 - \sigma^2 \delta t \right)$$
$$+ \frac{1}{2} \frac{\partial^2 O}{\partial^2 \sigma} ((\delta \sigma)^2 - \nu^2 \delta t)$$
$$+ S \frac{\partial^2 O}{\partial S \partial \sigma} \left( \left( \frac{\delta S}{S} \right) \delta \sigma - \rho \sigma \nu \ \delta t \right) \quad (6)$$

Two other "gamma" terms appear in this equation, which proves that incorporating the dynamics of the volatility is not as simple as the addition of a shadow term in the Black and Scholes breakeven relation. It also shows that controlling the P&L leads to a more complex gamma hedge, as it is now necessary to annihilate two more terms (the second and third ones, for which natural hedging instruments are strangles and risk reversals).

Another popular way of integrating the volatility surface dynamics in the model is to use Levy processes (see Exponential Lévy Models). We do not give the P&L explanation in that case, but, like in the stochastic volatility framework, it is the sum of the term presented in equation (3), for the Brownian part, and of a term coming from the pure jump part. The hedge of the latter is very complex because it is not localized in space (one needs to use a strip of gap options, e.g., to control it).

Finally, a possible way of controlling the volatility surface dynamics is to make no assumption on the volatility except that it is bounded. This framework is known as *uncertain volatility modeling* and is presented in **Uncertain Volatility Model**. The analysis leads to the conclusion that instead of one breakeven volatility, there are, in fact, two: the upper bound for positive gamma regions and the lower bound for negative gamma ones. In that case, and supposing that the effective realized volatility stays locally between these two bounds, gamma hedging is not necessary, as the P&L of the delta-hedged self financing portfolio is naturally systematically positive.

#### **Multiunderlying Derivatives**

We consider a multidimensional Black and Scholes model of N stocks  $S_i$  with volatility  $\sigma_i$ .  $\rho_{ij}$  represents the correlation between the Brownian motions controlling the evolution of  $S_i$  and  $S_j$ . We do not discuss the issue of multicurrency (see Quanto Options) and, using the same mechanism as in the monounderlying framework, we can express the P&L of a deltahedged self-financing portfolio as

$$\delta \Pi \approx \frac{1}{2} \sum_{i=1}^{N} S_i^2 \frac{\partial^2 O}{\partial^2 S_i} \left( \left( \frac{\delta S_i}{S_i} \right)^2 - \sigma_i^2 \delta t \right)$$
$$+ \sum_{i < j} S_i S_j \frac{\partial^2 O}{\partial S_i \partial S_j} \left( \left( \frac{\delta S_i}{S_i} \right) \left( \frac{\delta S_j}{S_j} \right) - \rho_{ij} \sigma_i \sigma_j \delta t \right) \tag{7}$$

The first term can be controlled by the hedging instruments we have previously reviewed. The cross ones, which incorporate the "cross gammas", can also be controlled, using so-called correlation swaps (typically, a basket option minus the sum of the individual options).

### Conclusion

Controlling the gamma exposure of a position is one of the main concerns of traders. Hedging instruments are common options but it is not possible to simply hedge the gamma without modifying the vega exposure of the position. Also, integrating the volatility surface dynamics in the model leads to a more complex gamma-hedging issue than in a Black and Scholes model, but it still can be addressed. Moreover, we remark that although we have considered the equity market in our study, this analysis can easily be extended to other complete markets in which there is no arbitrage and where the price process is modeled by a Brownian motion of any dimension.

## **End Notes**

a*.* P&L stands for "profit and loss" and represents the evolution of the portfolio value between two dates due to time and to the market activity between these dates.

## **Reference**

[1] Taleb, N. (1996). *Dynamic Hedging: Managing Vanilla and Exotic Options*, John Wiley & Sons, pp. 138–146.

## **Related Articles**

**Correlation Swap**; **Delta Hedging**; **Exponential Levy Models ´** ; **Gamma Swap**; **Heston Model**; **Uncertain Volatility Model**; **Variance Swap**.

CHARLES-HENRI ROUBINET
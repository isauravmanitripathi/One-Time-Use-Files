# **Option Pricing: General** Principles

**Option contracts** are financial assets that involve an element of choice for the owner. Depending on an event, the holder of an option contract can exercise his/her options stated in the contract, that is, to undertake certain specified actions. The typical example of an option contract gives the holder the right to buy a specific stock at a contracted price and time in the future. The contracted price is called the *strike price*, whereas the exercise time is when the option may be executed. Such contracts are known as *call options*, and the event that triggers the execution of the option is that the underlying stock price is above the strike. There is a plethora of different options traded in today's modern financial markets, where the financial events may include credit, weather related situations, and so on. One usually refers to derivatives or claims as being financial assets whose values are dependent on other financial assets.

There are two fundamental questions that the option pricing theory tries to answer. First, what is the fair price of a claim, and second, how can one replicate the claim. The second question immediately implies the answer to the first, since if we can find an investment strategy in the market that replicates the claim, the cost of this replication should be the fair price. This replication strategy is frequently called the **hedging strategy** of the claim. The key financial concepts in pricing and replication are arbitrage (or rather the absence of such) and completeness. A mathematical concept related to these is the equivalent martingale measure, also known as the riskneutral probability.

## **Explaining the Basic Concepts**

To understand the concepts used, it is informative to consider a very simple (and highly unrealistic) oneperiod **binomial model**. Suppose that we have a stock with value \$100 today and two possible outcomes in one year. Either the stock price can increase to \$110 or it can remain unchanged. The interest rate earned on bank deposits is set to 5% yearly and considered the risk-free investment in the market

Suppose that we wish to find a fair price of a call option with strike \$105 in one year. This option will effectively pay out \$5 if the stock increases, whereas the holder will not exercise it if the stock value is \$100. Consider now an investment today in  $a = 0.5$  number of stocks and  $b = -\$50/1.05 \approx$  $-$47.62$  deposited in the bank. A simple calculation reveals that this investment yields exactly the same as holding the option. In fact, this is the only investment in the stock and bank that perfectly replicates the option payoff and we, therefore, call it the *replicating* strategy of the option. The cost of replication is  $P = \$50/21 \approx \$2.38.$ 

We argue that the fair price of the option should be the same as the costs  $P$  of buying the replicating strategy. If the price would be higher, say  $\widetilde{P} > P$ , then one could do the following. Sell  $n$  options for that price and buy  $n$  of the replicating strategy. At exercise, any claims from the options sold will be covered exactly by the replicating strategies bought. However, we have received the cash amount of  $n \times \widetilde{P}$ for selling the options and paid out the amount  $n \times P$ for replication, thus leaving us with a profit. There is no risk attached with this investment proposition, and we can make the profit arbitrarily high by simply increasing  $n$ . This is what is known as an **arbitrage** opportunity, and in efficient markets, this should not be possible (or at least be ruled out quickly). If  $P < P$ , we reverse the positions above to create an arbitrage. The definition of a fair price is the price for which no arbitrage possibility exists. Thus, the option price in our example must be  $P = $50/21 \approx $2.38$ .

We note that the probability of a stock price increase did not enter into our analysis. The fair price is unaffected by this probability, since the hedging strategy is the same no matter how likely the stock price is to increase to \$110. The price of the option does not depend on the expected return of the stock, but only on the spread in the two possible outcomes of the stock price at exercise time, or, in other words, the volatility.

One may ask if the price of an option can be stated as the present expected value of the payoff at exercise. From the above derivations, we see that this is, in general, not the case since the price is not a function of the probability of a stock price increase. Hence, a present value price of the option would lead to arbitrage possibilities. However, we may rephrase the question and ask whether *there exists* a probability  $q$  for price increase such that the fair price can be expressed as a present value? Letting  $q = 0.5$ , we can easily convince ourselves that

$$P = \frac{1}{1.05} \{q \times 5 + (1 - q) \times 0\}$$
$$= \frac{1}{1.05} \mathbb{E}_q[\text{option payoff}] \tag{1}$$

where  $\mathbb{E}_q$  is the expectation with respect to the probability  $q$ . This probability of a stock price increase is *not* the probability for a price increase observed in the market, but a *constructed* probability for which the option price can be expressed as a present expected value.

The probability  $q$  has an interesting property that actually defines it. The present expected value of the stock price is equal to today's value,

$$100 = \frac{1}{1.05} \mathbb{E}_q[\text{stock price}] \tag{2}$$

Hence, the discounted stock price is a **martingale** with respect to the probability  $q$ . Further, the return on an investment in the stock coincides with the riskfree rate under  $q$ , defending the name "risk-neutral probability" often assigned to  $q$ .

#### **Option Pricing in Continuous Time**

Our binomial one-period example basically contains the main concepts for pricing of options and claims in more general and realistic market models. Moving to a stock price that evolves dynamically in time with stochastic marginal changes, the principles of option pricing remain basically the same, however, introducing interesting technical challenges. We now look at the case when the stock price follows a **geometric Brownian motion** (GBM), that is,

$$\frac{\mathrm{d}S(t)}{S(t)} = \mu \,\mathrm{d}t + \sigma \,\mathrm{d}B(t) \tag{3}$$

defined on a probability space  $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ with the filtration  $\mathcal{F}_t$  generated by the Brownian motion modeling the information flow. The GBM model indicates that returns (or more precisely, logarithmic returns) are independent and normally distributed, with mean  $\mu$  dt and volatility  $\sigma\sqrt{dt}$ . The model was first proposed for stock price dynamics by Samuelson [7] and later used by Black and **Scholes** [1] and **Merton** [6] in their derivation of the

famous option pricing formula. We suppose that the market is frictionless in the sense that there are no transaction costs incurred when we trade in the stock or the bank, and there are no restrictions on short or long positions. Further, the interest rate is the same whether we borrow or lend money, and the market is perfectly liquid.

The main difference from the one-period model is that we can invest in the underlying stock at all times up to maturity of the claim. Obviously, we can also do the same with the bank deposit, which is now assumed to yield a continuously compounding interest rate  $r$ . An investment strategy will consist of  $a(t)$  shares of the stock and  $b(t)$  invested in the bank at time  $t$ . Since investors cannot foresee the future, the investment decisions at time  $t$  can only be based upon the available market information, which is contained in the filtration  $\mathcal{F}_t$ . The value at time  $t$  of the portfolio is

$$V(t) = a(t)S(t) + b(t)R(t) \tag{4}$$

where  $R(t) = \exp(rt)$ , the value of an initial bank deposit of 1. Further, since we are interested in creating strategies that are replicating an option, we wish to rule out any external funding or withdrawal of money in the portfolio we are setting up. This leads to the so-called **self-financing** hypothesis, saying that any change in portfolio value comes from a change in the underlying stock price and bank deposit. Mathematically, we can formulate this condition as

$$dV(t) = a(t) dS(t) + b(t) dR(t)$$
(5)

Note that **Itô's formula** implies a dynamics  $V(t)$ where the differentials of  $a(t)$  and  $b(t)$  appear. The self-financing hypothesis indicates that these differentials are zero.

For the one-period binomial model, we recall the existence of an **equivalent martingale measure** for which the discounted stock price is a martingale. Applying the Girsanov theorem, we find a probability measure  $\mathbb{Q}$  equivalent to the market probability  $\mathbb{P}$ , for which the process  $W(t)$  with differential

$$dW(t) = \frac{\mu - r}{\sigma} dt + dB(t) \tag{6}$$

is a Brownian motion. By a direct calculation, we find

$$d(e^{-rt}S(t)) = \sigma(e^{-rt}S(t)) dW(t)$$
(7)

which is a **martingale** under . Furthermore, by discounting the portfolio process *V (t)* and applying the self-financing hypothesis, we find

$$d(e^{-rt}V(t)) = \sigma a(t)(e^{-rt}S(t)) dW(t) \qquad (8)$$

Hence, the discounted portfolio process is also a martingale under .

Consider a claim with maturity at time *T* and a payoff represented by the random variable *X*, where F*<sup>T</sup>* is measurable and integrable with respect . The (for the moment unknown) price at time *t* of the claim is denoted by *P (t)*. Suppose that the discounted price of the claim is a martingale with respect to and that we have a self-financing portfolio consisting of investments in the stock, the bank notes, and the claim. Further, we construct the investment such that the initial price is zero. The discounted value process of this portfolio will then (by the same reasoning as above) give a martingale process under , and hence the expectation with respect to of the portfolio value at any future time must be the same as the initial investment, namely, zero. Thus, under , there is a positive probability of having a negative portfolio value, which implies by equivalence of with  that we cannot have any arbitrage opportunities in this market. On the other hand, if the market does not allow for any arbitrage, one can show that e<sup>−</sup>*rtP (t)* must be a -martingale. We refer to [3] for the connection between no-arbitrage and existence of equivalent martingale measures. It is a financially reasonable condition to assume that the market is arbitrage free.

By the **martingale representation theorem**, there exists an **adapted** stochastic process *φ(t)* such that

$$d(e^{-rt} P(t)) = \phi(t) dW(t)$$
(9)

whenever exp*(*−*rt)P (t)* is square-integrable with respect to . By defining *a(t)* =*φ(t)/σ* exp*(*−*rt)S(t)* and *b(t)* = exp*(*−*rt)(P (t)* − *a(t)S(t))*, the portfolio *V (t)* given by the investment strategy *(a, b)* is selffinancing. Moreover, *V (T )* = *P (T )* = *X*, implying that it is a replicating strategy for the claim. Furthermore the market becomes **complete**, meaning that there exists a replicating strategy for all claims, *X* being square-integrable with respect to .

Now, again appealing to the -martingale property of e<sup>−</sup>*rtP (t)*, we find by definition that

$$P(t) = e^{-r(T-t)} \mathbb{E}_{\mathbb{Q}} \left[ X \mid \mathcal{F}_t \right] \tag{10}$$

Thus, as a natural generalization of the binomial one-period model case, any claim has a price given as the expected present value, where the expectation is taken with respect to the risk-neutral probability. Note that *S* does not depend on its expected return *µ* under , and therefore the price *P (t)* is independent of this. The volatility *σ* is, however, a crucial parameter for the determination of price.

If we let *X* be the payoff of a call option written on *S*, one can calculate the conditional expectation in equation (10) to derive the famous **Black–Scholes formula**. Further, the process *φ(t)* is in this case explicitly known, and it turns out that the investment strategy *a(t)* is the derivative of the price *P (t)* with respect to *S(t)*. This derivative is known as the delta of the call option. Moreover, the strategy given by *a(t)* is called *delta-hedging*.

### **Option Pricing in Incomplete Markets**

Recall that we have assumed a frictionless market. In practice, transaction costs are normally incurred when buying and selling shares. Hence, since a deltahedging strategy *(a, b)* involves incessant trading, it will become infinitely costly if implemented. In addition, there are practical limits to how big a short position we can take (e.g., due to credit limits and collaterals). Theoretically, there exists only *one* replicating strategy since the martingale representation theorem prescribes a unique integrand process *φ(t)*. Introducing frictions such as transaction costs or short-selling limits in the market rules out the possibility to replicate claims in general, and the market is said to be **incomplete**. We remark that in an incomplete market, there still exists claims that can be replicated, and by the no-arbitrage principle, the price of these is characterized by the cost of replication, as we have argued above. However, a natural question arises: what can we say about pricing and hedging of claims where no replicating strategy exists?

One approach suggests to look at **super- and sub-replicating strategies**. A super(sub-)replicating strategy is a self-financing portfolio of stock and bank deposit, which at least(most) has the same value as the claim at maturity. Letting *P*max *(P*min*)* be the infimum (supremum) over all prices of such super(sub-)replicating strategies, it follows that any price *P* in the interval *(P*min*, P*max*)* is arbitrage free. Furthermore, any self-financing strategy that costs less than *P*max will always have a positive probability of having a value lower than the claim at maturity, and thus full replication is impossible. This leaves the issuer of the claim with some unhedgable risk. An acceptable or fair price of the claim will reflect the compensation the issuer demands for taking on this risk.

A change in the stock price dynamics gives another source of incompleteness in the market. The GBM model is rather unnatural from an empirical point of view, since observed stock price returns on the marketplace are frequently far from being normally distributed nor are they independent. Stock price models including **stochastic volatility** and/or stochastic drivers other than Brownian motion have been proposed. For instance, on the basis of empirics, the returns may be modeled by a heavy-tailed distribution, which gives rise to a **Levy process ´** in the geometric dynamics of the stock price. A consequence of such a seemingly innocent change in the structure is that there exists a continuum (in general) of **equivalent martingale measures** such that the discounted stock price is a martingale. The complicating implication of this is the absence of martingale representations when it becomes impossible to find an investment strategy replicating the claim. As for markets with frictions, we have no possibility of replication, but an interval of possible arbitragefree prices. In addition, in this case, the issuer of the claim needs to accept a certain unhedgable risk.

To price claims in incomplete markets, one must resort to methods that take into account the risk posed on the issuer. Popular approaches include minimalvariance hedging, where the strategy minimizing the variance (that is, the risk) is sought for. The price of the claim is the cost of buying the minimalvariance strategy [8] plus a compensation for the unhedged risk. Another possibility that has gained a lot of attention in the option pricing literature is **indifference pricing** (see also the seminal work of Hodges and Neuberger [5]). Here, one considers an investor who has two opportunities. Either he/she can invest his/her funds in the market, or he/she can sell a claim and invest his/her funds along with claim price. In the latter case, he/she has more funds for investment, but on the other hand, he/she faces a claim at maturity. By optimizing his/her expected utility from the two investment scenarios, the *indifference price* of the claim is defined as the price that makes one indifferent between the two opportunities. The choice of an exponential utility function leads to prices where the singular case of zero risk aversion coincides with the price defined by the **minimal entropy martingale measure** [4]. This price lends itself to the interpretation of being the price that is equally desirable for both the issuer and the buyer in the case when both parties have zero risk aversion. For all other risk aversions, the seller will charge higher prices, and the buyer will demand lower. The difference of the two optimal investment strategies obtained from utility maximization becomes the hedging strategy. This and other similar approaches have gained a lot of academic attention in the recent years.

Another path to pricing in incomplete markets is to try to complete the market by adding options. The required number of options to complete the market is closely linked to the number of sources of uncertainty and the number of assets. For example, considering a GBM with a stochastic volatility following the Heston model gives two random sources and one asset. Following the analysis in [2], one call option is sufficient to complete the market. In [2], the necessary and sufficient conditions to complete markets are given in the case when the filtration is spanned by more Brownian motions than there are traded assets.

### **References**

- [1] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**, 637–654.
- [2] Davis, M. & Obloj, J. (2008). Market completion using options, in *Advances in Mathematics of Finance*, L. Stettner, ed., Banach Center Publications, pp. 49–60, Vol. 43.
- [3] Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing, *Matematische Annalen* **300**, 463–520.
- [4] El Karoui, N. & Rouge, R. (2000). Pricing via utility maximization and entropy, *Mathematical Finance* **10**(2), 259–276.
- [5] Hodges, S. & Neuberger, A. (1989). Optimal replication of contingent claims under transaction costs, *Review of Futures Markets* **8**, 222–239.
- [6] Merton, R. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**, 141–183.

- [7] Samuelson, P.A. (1965). Proof that properly anticipating prices fluctuate randomly, *Industrial Management Reviews* **6**, 41–49.
- [8] Schweizer, M. (2001). A guided tour through quadratic hedging approaches, in *Option Pricing, Interest Rates, and Risk Management*, E. Jouini, J. Cvitanic & M. Musiela, eds, Cambridge University Press, pp. 538–574.

### **Related Articles**

**Binomial Tree**; **Black–Scholes Formula**; **Hedging**; **Option Pricing Theory: Historical Perspectives**.

FRED E. BENTH
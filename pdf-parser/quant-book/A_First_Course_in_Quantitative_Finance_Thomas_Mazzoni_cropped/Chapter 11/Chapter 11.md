✖

# **11 Forwards, Futures, and Options**

We are now entering the world of derivatives. Derivatives are contracts whose value depends on the value of other securities, commodities, rates, or even derivatives themselves; hence their name. They are nowadays traded as highly sophisticated risk transfer instruments in organized markets like the Chicago Board Options Exchange (CBOE) or in secondary over the counter markets (OTC). Valuation of derivatives is at the heart of quantitative finance, and can sometimes be a very challenging task. This chapter is only a gentle warm-up for the techniques to be discussed in the sequel.

# **11.1 Forward and Future Contracts**

Forwards and futures are contracts, which enable an agent to lock in a future price for an arbitrary underlying today. An underlying can be a security, a commodity, an exchange rate, or in principle everything that can be traded. The difference between forward and future contracts is the way they are traded and settled. Forwards are individually "over the counter" (OTC) brokered contracts. Settlement is at expiry or shortly after, usually but not necessarily in cash. A future is a standardized contract that is traded in an organized market. Both sides of the future can be contracted independently with a clearing house as counterparty. To reduce the default risk for the clearing house, the agent has to provide collateral and to agree to daily settlement payments via a margin account. By this procedure, the value of an open contract is reset every day. In a world where the risk-free interest rate is either constant, or a deterministic function of time, forward and future prices have to coincide. In reality, where interest rates themselves are stochastic, both prices diverge because of the different settlement policies. Until further notice, we will assume that the risk-free interest rate is deterministic.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Why would anyone enter into a forward or future contract at all? Let's look at the following example.

# **Example 11.1**

Assume A is a large food retail chain, say in Germany, and B is an agricultural producer in Spain. A would like to buy 50 tons of tomatoes from B next year. B is willing to sell the requested quantity to A, but both operate under a fair amount of risk and effort. The underlying commodity, the 50 tons of tomatoes, does not even exist today. They

have to be planted at the beginning of the next year, in order to be ready for harvesting shortly before the contracted delivery date. It is uncertain if there will be enough rain in Spain next year to prevent crop failures, which could drive up the market price of tomatoes or worse, rendering delivery of the full quantity impossible. Last but not least, 50 tons of tomatoes have to be shipped all the way across Europe, to get them from B to A.

#### Entering a forward contract

Imagine A and B agree to a cash settled forward contract, in which the delivery price and date are fixed. What happens at expiry of this contract? A will buy at the local market in Germany at the market price, prevailing at the delivery date. B will sell in Spain, also at the prevailing market price. Additionally, one party will compensate the other party for the difference between the contracted delivery price and the actual market price. There is no physical delivery, and hence no transportation costs, and no risk regarding the future market price of tomatoes. ........................................................................................................................

You see how efficient the forward contract is? It avoids costly physical delivery and completely removes the uncertainty of next year's price. Now you have a first glimpse of why modern economies vitally depend on a liquid and operational financial market.

There are two questions regarding such a forward contract, we have to answer. The first is, is there a rule to determine the delivery price, such that the contract is fair for both parties? And if there is, how should the delivery price be chosen? The second question is a little more subtle. Recall that the forward contract in Example 11.1 involves the right and the obligation to buy or sell the underlying at the delivery date at a predetermined price. This right can also be traded, and it thus should have a price itself. How can we determine its fair price? This is our first problem in derivative pricing.

# **11.2 Bank Account and Forward Price**

The concepts we will see in this section are some of the most powerful tools in derivative pricing, because they are completely model independent. As soon as a market is considered liquid enough to prevent arbitrage opportunities (at least on a large scale), these principles have to hold no matter what additional conditions we might have imposed.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Let's first talk about the time value of money. You might have learned already the golden rule of financial mathematics: Never compare two nominal payments at different times. What this means is that the value of money changes with time. How can that be? If you put \$100 under your pillow and come back tomorrow, you will still have \$100. But this is a particular property of your pillow. If you put \$100 into a bank account today and come back tomorrow, you have more than \$100, because you earned interest. In a liquid market, everyone puts her money into a bank account. If you find somebody preferring a pillow, offer him yours, then afterwards secretly put the money into your bank account and withdraw it the next day. So she gets her money back and you earn the interest. But that is an arbitrage, isn't it? The question is how

does the value of money evolve with time? Let's assume for the moment that interest rates are constant, and call the risk-free interest rate *r*. If you deposit a certain capital in a bank account *B*, its value changes proportional to the interest rate, the capital itself, and of course the time of your deposit. Let's write this for very short amounts of time,

$$dB(t) = rB(t)dt,\t(11.1)$$

and let's see what we can do with it. Without loss of generality, we can assume that the capital you put into your account at time *t* = 0 was *B*(0) = 1 unit of currency. If you put 100 units of currency there, think of it as 100 distinct accounts, it makes no difference. Next, divide both sides by *B*(*t*),

$$\frac{dB(t)}{B(t)} = d\log B(t) = rdt.$$
 (11.2)

We can integrate this differential equation easily to obtain

$$\int_0^t d\log B(s) = \log B(t) = rt = r \int_0^t ds.$$
 (11.3)

Exponentiating both sides of (11.3) yields

$$B(t) = e^{rt}.\t(11.4)$$

On the other hand, it is easy to see that a value of *K* at time *t* requires an initial deposit of *e* <sup>−</sup>*rtK*, or more precisely *e* <sup>−</sup>*rtK* standard bank accounts, because

$$e^{-rt}KB(t) = K. \t\t(11.5)$$

Here is a little more tricky question: What is the time *t* value of an amount *K* at *T* for 0 < *t* < *T*? By now you will agree that you initially need *e* <sup>−</sup>*rTK* standard accounts. But their value at time *t* is simply

$$e^{-rT}KB(t) = e^{-r(T-t)}K.$$
 (11.6)

**Quick calculation 11.1** What is the time *T* value of a time *t* deposit of one unit of currency for *t* < *T*?

Now let us return to our initial problem and answer the first question. How should the delivery price of a forward contract be chosen? Suppose the contract has an ordinary, non dividend paying stock *S* as underlying. When initiated, neither party should have to pay anything for contracting the delivery price *K* and delivery date *T*. Thus, at time *t* = 0 the forward contract has zero value, *F*0(*K*,*T*) = 0. Consider building the following hypothetical portfolio: Enter a forward contract as buyer, short one unit of the underlying, put the earnings from the short selling into your bank account. The position is summarized in Table 11.1. Obviously this portfolio does not cost anything at *t* = 0. But this means, it has to have zero price at *t* =*T*, too, otherwise we would have

| Table 11.1<br>Forward arbitrage portfolio |                      |                     |
|-------------------------------------------|----------------------|---------------------|
| Position                                  | Value at t = 0       | Value at t = T      |
| Forward                                   | 0                    | −<br>ST<br>K        |
| Stock                                     | −S0                  | −ST                 |
| Bank account                              | S0                   | rTS0<br>e           |
| Total sum                                 | −<br>= 0<br>S0<br>S0 | rTS0<br>−<br>e<br>K |

an arbitrage opportunity, either by holding this portfolio or by shorting it. To rule out such an arbitrage opportunity, the delivery price of the forward contract has to be chosen as

$$K = e^{rT} S_0. \t\t(11.7)$$

Except for a constant risk-free interest rate, this argument is completely free of modelbased assumptions. We only used a genuine arbitrage argument. Thus, this result is a very strong one and as long as interest rates are deterministic, it holds for the future contract as well.

The second question is, how should a running contract, initiated at some time in the past, be valued? To answer this question, we make use of another luxury the arbitrage free choice of the delivery price provides us with, we build ourselves a time machine. Note that the value of the forward contract at delivery is

$$F_T(K, T) = S_T - K, \t\t(11.8)$$

see Table 11.1. All quantities depend on time, even if this is not so obvious for the delivery price. To see this, let's write it in a slightly different form

$$K = e^{-rT} KB(T). \t(11.9)$$

**Quick calculation 11.2** Convince yourself that (11.9) is correct.

So the time *t* value of the delivery price *K* is

$$e^{-rT}KB(t) = e^{-r(T-t)}K.$$
(11.10)

Of course, what we discussed so thoroughly in terms of our standardized bank account is nothing else but continuous discounting. There is a deeper reason for going through it so rigorously. It has to do with a certain choice of numéraire we will encounter at a later point. At the moment, we simply take the value of the contract at expiry (11.8), and crank the dials of our time machine back to any desired time *t*. In doing so, we obtain

$$F_t(K,T) = S_t - e^{-r(T-t)}K.$$
 (11.11)

You have probably learned that something like a time machine cannot work in real life. So let's see if we can understand why our financial time machine works correctly. Fix an arbitrary time *t* = τ and assume that you already hold one forward contract, initiated at *t* = 0. Initiate another forward contract with identical delivery date *T* and delivery price K, and take the opposite side. By definition, entering this contract does not cost you anything and thus, the value of your position has not changed. At expiry of both contracts, your position has the value K − *K*. But this difference is only a positive or negative amount of currency with time τ value *e* −*r*(*T*−τ) (K − *K*). Now realize that you have to choose the delivery price

$$\mathcal{K} = e^{r(T-\tau)} S_{\tau} \tag{11.12}$$

in order to prevent arbitrage opportunities. Hence, the present value of your position at *t* = τ is

$$F_{\tau}(K,T) - 0 = S_{\tau} - e^{-r(T-\tau)}K.$$
(11.13)

Because τ is arbitrary, the substitution τ → *t* does the trick.

**Quick calculation 11.3** Sketch the arbitrage portfolio for the contract initiated at *t* = τ.

We can now see why our time machine worked for the forward contract. But the argument behind the derivation is far more general. Whenever the market is free of arbitrage opportunities and you can build a portfolio that costs nothing at one time, it cannot cost anything at any other time. This principle is at the heart of parity relations, which are the strongest conditions we can hope to find in pricing derivatives.

# **11.3 Options**

We learned that risk aversion is expressed in terms of a certain asymmetry in utility between losing or gaining a fixed amount of wealth. That usually holds also for the costs of precautionary measures.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Imagine you were employed at company A of Example 11.1, and you were the person in charge of the tomato deal with B. You are concerned that anything could go wrong and so you decide to enter a forward contract with B. Let's speculate what might happen. First think of the possibility that your precaution was well justified and tomato prices are considerably higher than expected, *S<sup>T</sup>* > *K*. In this case you can relax, because no matter what the price is, your forward contract will provide compensation of the difference between market price and delivery price, and everyone will praise you for your vigilance and your professional skills. But what happens if everything goes well and the tomatoes cost considerably less than expected, *S<sup>T</sup>* < *K*? Everyone will celebrate, because they hope for spectacular profits. Then you have to step in front of the CFO and explain, why your company has to pay *K* − *S<sup>T</sup>* from a forward contract you entered one year ago. You are lucky if you can keep your job.

![](_page_5_Figure_1.jpeg)

**Fig. 11.1** Payoff function of a call option (left) and a put option (right) from the holder's perspective (long position)

An option contract is designed to keep you out of such trouble, by certifying the right but not the obligation to buy (call) or sell (put) the underlying at an exercise price *K*. At expiry, the value of a call option for example is *S<sup>T</sup>* − *K*, if *S<sup>T</sup>* > *K*, and zero else. If the market price is higher than the contracted exercise price, you would of course exercise the option, because you can buy at *K* and immediately sell at *S<sup>T</sup>* at the market. Your riskless profit would be the difference *S<sup>T</sup>* − *K*, which is exactly the value of the option at expiry, if *S<sup>T</sup>* > *K*. If *S<sup>T</sup>* < *K*, you would not exercise the option at all, because you can buy cheaper at the market. Therefore, the contract expires worthlessly and its value at time *T* is zero. We can summarize these arguments by introducing the payoff function of the call option as its intrinsic value at expiry

$$C_T(S_T) = \max(S_T - K, 0) = (S_T - K)^+, \tag{11.14}$$

where we have written the terminal value as a function of the price of the underlying at time *T*. The right hand side is only a shorthand for the maximum function we will use frequently. Figure 11.1 left illustrates the payoff function from the perspective of the option holder. This position is also called the long position. The person who has written the option is said to be in the short position.

**Quick calculation 11.4** What is the payoff function of a forward contract?

If we are in the long position of a put option, then we have the right, but not the obligation, to sell the underlying at the contracted exercise price *K*. The writer of the option (short position) is under the obligation to buy the underlying from us, if we choose to exercise the option. If the market price of the underlying at expiry is less than the exercise price, *S<sup>T</sup>* < *K*, we can immediately buy in the market at *S<sup>T</sup>* and exercise the option to sell for *K* to the writer of the contract, providing an instantaneous profit of *K* − *ST*. If *S<sup>T</sup>* > *K*, we would of course not exercise the option, because we can earn more money by selling at the market price *ST*, rather than at the exercise price *K*. Thus, the payoff function of the put option has to be

$$P_T(S_T) = \max(K - S_T, 0) = (K - S_T)^+, \tag{11.15}$$

![](_page_6_Figure_1.jpeg)

**Fig. 11.2** Adding up the payoff functions of a long call and short put with identical exercise price *K* and expiry date *T*

where we have used the same shorthand for the maximum function as before. The payoff function is illustrated in Figure 11.1 right.

**Quick calculation 11.5** Sketch the payoff function for a short call and short put position.

Let's ask the following question: What payoff function do we get, if we hold one call option and short a put option with identical exercise price and time to expiry? The answer is illustrated in Figure 11.2. Adding both payoff functions results in an exact replication of the payoff function of a forward or future contract. This means that at time *T* we have

$$C_T - P_T = F_T. \tag{11.16}$$

But recognize that a portfolio of one long call, one short put, and one short forward of this kind has value zero at time *T*. This means that it must be zero at all times and we can again use our time machine. The resulting identity

$$C_t(K,T) - P_t(K,T) = F_t(K,T) = S_t - e^{-r(T-t)}K$$
(11.17)

is called put-call parity. It enables us to immediately find the value of a put option for example, if the corresponding call option is traded. As emphasized before, parity relations do not require model based assumptions, and are thus very powerful.

The most common types of options are called plain vanilla options after a very popular ice cream flavor in the USA. A position in plain vanilla options is characterized by the following features:

#### **Position**

- Long: Contract holder with the right to exercise the option.
- Short: Contract writer under the obligation to comply, if the holder exercises.

#### **Option type**

- Call: Right to buy the underlying from the writer at the contracted exercise price.
- Put: Right to sell the underlying to the writer at the contracted exercise price.

## **Exercise right**

- European: Option can only be exercised at expiry.
- American: Option can be exercised at any time until expiry.

Of course there is a multiverse of non-vanilla option contracts, called exotics, but vanillas are still the most liquidly traded derivatives in the market.

# **11.4 Compound Positions and Option Strategies**

Plain vanilla options are most versatile in that a desired payoff profile can be generated by combining long and short positions in calls and puts. Furthermore, they are appropriate for manipulating the downside risk or the return characteristics of a given position in the underlying. In this paragraph we will discuss some of the most basic strategies, frequently encountered in the market.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

# **11.4.1 Straddle**

A straddle position is often used to hedge against massive up- or downturns of the underlying. Imagine the underlying is a stock, and the respective company is about to report quarterly figures. Often the trading volume drops before such an event, because there are some opposing rumors, but nobody really knows what to expect. In this situation it is likely that the report triggers one of two possible events. Either the figures are good and the price moves up, due to temporal excess demand, or the report is disappointing for the investors and the price drops, because of increasing sales. Either way, a straddle position can provide insurance against the consequences of such an event. It is composed of a long call and a long put, both with identical exercise price *K* and expiry *T*,

$$\Pi_{\text{Straddle}} = C(K, T) + P(K, T). \n$$
(11.18)

The corresponding payoff function is illustrated in Figure 11.3 left. From the payoff it is obvious, why the straddle can provide insurance against both outcomes. Of course, such an insurance has its price; note that the straddle contains only long positions.

![](_page_7_Figure_11.jpeg)

**Fig. 11.3** Payoff function of a long straddle position (left) and a butterfly spread (right)

# **11.4.2 Butterfly Spread**

In a certain sense, the butterfly spread is an opposite position to the straddle. It pays off its maximum ∆*K*, if the price at expiry equals the exercise price *K*, see Figure 11.3 right. To establish a butterfly spread, one requires call options with three different exercise prices, *K*, and *K* ± ∆*K*, where ∆*K* > 0 is arbitrary. The structure of the entire position is

$$\Pi_{\text{Butterfly}} = C(K - \Delta K, T) - 2C(K, T) + C(K + \Delta K, T). \n$$
(11.19)

Because the butterfly spread contains two long and two short positions, it is relatively cheap to enter because

$$C_{t}(K - \Delta K, T) > C_{t}(K, T) > C_{t}(K + \Delta K, T)$$
(11.20)

has to hold for every *t* < *T*. Nevertheless, the butterfly spread has to cost a positive amount of money, Π*<sup>t</sup>* > 0, because it has a positive payoff in states of the world, in which *K* − ∆*K* < *S<sup>T</sup>* < *K* + ∆*K* holds. Otherwise we would have an arbitrage opportunity.

**Quick calculation 11.6** Sketch an arbitrage argument for the price of a butterfly spread to be bounded by 0 ≤ Π*<sup>t</sup>* ≤ *e* <sup>−</sup>*r*(*T*−*t*)∆*K* for *t* ≤*T*.

# **11.4.3 Bull and Bear Spreads**

Bull and bear spreads are limited risk positions with two options with the same expiry *T*, but with different exercise prices *K*<sup>2</sup> > *K*1. The difference between both positions is the direction in which the underlying has to evolve, in order to trigger a payoff at expiry. Imagine the current price of an underlying is *K*<sup>1</sup> < *S<sup>t</sup>* < *K*2. If it behaves bullish, which means its price rises, the payoff from the bull spread increases, see Figure 11.4 left. The position is established by the simple combination

$$\Pi_{\text{Bull}} = C(K_1, T) - C(K_2, T). \n$$
(11.21)

![](_page_8_Figure_11.jpeg)

**Fig. 11.4** Payoff function of a bull spread (left) and a bear spread (right)

Of course the price of a bull spread is bounded by 0 ≤ Π*<sup>t</sup>* ≤ *e* −*r*(*T*−*t*) (*K*<sup>2</sup> − *K*1) for *t* ≤*T*. Otherwise we would again have an arbitrage opportunity.

**Quick calculation 11.7** Confirm the above mentioned bounds for *S<sup>T</sup>* < *K*<sup>1</sup> and *S<sup>T</sup>* > *K*2.

The same holds true for the bear spread, because it is merely a mirror image of the bull spread, see Figure 11.4 right. It can be established by combining two put options,

$$\Pi_{\text{Bear}} = P(K_2, T) - P(K_1, T). \n$$
(11.22)

Of course, an investor would hold a bear spread, if she expects the price of the underlying to fall. Such a development is often called bearish, hence the name.

There is another spread strategy an investor can pursue, called a calendar spread. In this case the options involved have the same exercise price *K*, but different expiries, *T*<sup>1</sup> and *T*2. With this strategy, an investor usually does not speculate on rising or falling prices of the underlying, but on changes in implied volatility. Since we have not treated volatility concepts in detail so far, we will not discuss this position here.

# **11.4.4 Protective Put Buying**

Protective put buying is a strategy to limit the downside risk of a security or portfolio of securities, held by an investor. It works by establishing a so-called floor with the help of a long position in an appropriate put option. Imagine you hold a security with current price *S*0, and your investment horizon is *T*. You can limit the loss potential of this position by buying a put option with expiry *T* and exercise price *K* < *S*0. In case the price of the security falls below the floor, *S<sup>T</sup>* < *K*, the put option provides insurance by paying *K* − *S<sup>T</sup>* at expiry. Your potential loss from *S* is therefore bounded by *S*<sup>0</sup> − *K*. Of course this insurance does not come for free. At *t* = 0 you have to pay the option premium *P*0, reducing your expected profits from *S*. Assume that you have to borrow the money to buy the put option, then the value of your position at any time 0 ≤ *t* ≤ *T* is

$$\Pi_t = S_t + P_t(K, T) - e^{rt} P_0. \n$$
(11.23)

In particular at *t* = *T*, your portfolio is floored by Π*<sup>T</sup>* ≥ *K* − *e rTP*0. This is reassuring, but it comes at the cost of a reduced return, due to the long position in the put option. You can even increase the insurance level of this strategy for example by choosing an option with *K* = *S*0. You are then completely shielded from losses in your stock position, but such an at-the-money put option would be fairly expensive. Thus, your stock would have to perform extraordinarily well, just to break even.

# **11.4.5 Covered Call Writing**

Covered call writing is a strategy for manipulating the return profile of a position in a stock or a portfolio. It has no insurance character, but it earns a positive amount of money at the beginning of the investment period. Let's again consider an investment

horizon  $0 \le t \le T$ , and a long position in the stock S. Typically writing a call option is a delicate decision, because the potential loss is not bounded.

**Quick calculation 11.8** Sketch the payoff function of a short call position.

However, in this case shorting a call is noncritical, because we already own the underlying. If the option holder decides to exercise the option at expiry, we can hand over the stock and receive the exercise price. Of course, we obtain an option premium  $C_0$ at  $t = 0$ , which we deposit in our bank account in order to earn interest. The whole position at any time  $t$  is thus

$$\Pi_t = S_t - C_t(K, T) + e^{rt} C_0. \n$$
(11.24)

For this position to make sense, we have to choose an exercise price  $K > S_0$ , because eventually our gains are bounded by  $\Pi_T \leq K + e^{rT}C_0$  from above. Which means, we sell the possibility of extraordinary high returns for a fixed option premium at  $t = 0$ . This decision is advantageous in all cases, where  $S_T \leq K$ , because the option is not exercised. If  $S_T > K$  we do not participate further in any winnings, no matter how high they might be. We can decide how much of the potential gains to trade for the initial call premium; the lower K, the higher the premium, but the less we participate in potential gains.

#### 11.5 **Arbitrage Bounds on Options**

To determine the fair price of a plain vanilla European option, it is in general not sufficient to exploit arbitrage arguments. An exception is the theoretical possibility that the market contains a continuum of call options with all possible exercise prices at any given expiry; see Breeden and Litzenberger (1978). Nevertheless, they will carry us a good part of the way, so let's see what we can learn from them. Consider the problem of pricing a plain vanilla European call with exercise price K and expiry T today, at  $t = 0$ . We can apply three arbitrage arguments to bound its price from above and below:

- 1. The price of the call option  $C_0(K,T)$  can never exceed the price of the underlying  $S_0$ . To see this realize that for the payoff at expiry  $(S_T - K)^+ - S_T \le 0$  holds. Now crank the dials of the time machine back to  $t = 0$  to obtain  $C_0(K, T) - S_0 \le 0$ . The claim follows immediately.
- 2. The price of the call option can never be smaller than the price of a corresponding forward contract. To see this, again set up a portfolio of one call and short one forward contract. The payoff is  $(S_T - K)^+ - (S_T - K) \ge 0$ . Dialing back the time we obtain  $C_0(K, T) - S_0 + e^{-rT} K \ge 0$ , as required.
- 3. The price of the call option can never be negative. The argument for this is a fundamental one. The payoff of the call is nonnegative and positive for states of the world, in which  $S_T > K$ . Thus, the price at  $t = 0$  must not be negative by the very definition of an arbitrage opportunity.

Condensing all three arguments into one formula, we can make the following statement about the arbitrage bounds for a European call option

$$(S_0 - e^{-rT}K)^+ \le C_0(K,T) \le S_0. \tag{11.25}$$

Going through a similar set of arguments for a European plain vanilla put option, we arrive at the arbitrage bounds

$$(e^{-rT}K - S_0)^+ \le P_0(K, T) \le e^{-rT}K. \tag{11.26}$$

**Quick calculation 11.9** Apply the appropriate arbitrage arguments to confirm (11.26).

That is how far arbitrage considerations can carry us. Unfortunately those bounds are not very tight, which means we have to do much better.

# **11.6 Further Reading**

For the time value of money, see Capinski and Zastawniak (2003, sect. 2.1). Forward and future contracts are introduced very carefully in Hull (2009, chap. 5). In particular, a simple proof for the equality of forward and future prices for constant interest rates is provided in the appendix. For a deeper treatment of this subject, see Cox et al. (1981). A very good introduction to options, parity relations, and option strategies is provided in Hull (2009, chap. 8 & 10), and also in Wilmott (2006a, chap. 2). For arbitrage bounds on options see Hull (2009, chap. 9) and Cox (2010).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

# **11.7 Problems**

**11.1** Suppose a stock pays a fixed percentage dividend stream *q* that is continuously reinvested, such that an initial investment *S*<sup>0</sup> has time *T* value *e qTST*. Construct an arbitrage portfolio for a forward contract and find the delivery price, such that entering the contract does not cost anything.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

- **11.2** An option that pays off one unit of currency at expiry, in case of *S<sup>T</sup>* ≥ *K*, and zero else, is called a binary or digital call option. Likewise a binary put option pays one unit of currency, if *S<sup>T</sup>* < *K* holds, and nothing otherwise. Sketch the payoff function of a binary call and put.
- **11.3** Establish a parity relation for binary calls and puts by adding their payoff functions and derive a formula for 0 ≤ *t* ≤ *T*.

**11.4** Consider a modified butterfly position

$$\Pi_{\text{Butterfly}} = C(K_1, T) - a \cdot C(K_2, T) + C(K_3, T),$$

with *K*<sup>1</sup> < *K*<sup>2</sup> < *K*3, and *a* > 0. How is *a* to be chosen to guarantee a vanishing payoff for *S<sup>T</sup>* = *K*<sup>1</sup> and *S<sup>T</sup>* = *K*3?

**11.5** It is possible to generalize the butterfly position even more to the form

$$\Pi_{\text{Butterfly}} = C(K_1, T) - a \cdot C(K_2, T) + b \cdot C(K_3, T),$$

with *K*<sup>1</sup> < *K*<sup>2</sup> < *K*3, and *a*, *b* > 0 How are the coefficients *a* and *b* to be chosen, to generate a vanishing payoff for *S<sup>T</sup>* ≤ *K*<sup>1</sup> and *S<sup>T</sup>* ≥ *K*3?

- **11.6** Describe the position an investor holds, if she is long in a covered call and short in a protective put, with both options having the same exercise price and time to expiry.
- **11.7** Assume an investor holds long positions in a covered call and a protective put. Both options have identical expiries and exercise prices. What is the payoff of this combined position at expiry?
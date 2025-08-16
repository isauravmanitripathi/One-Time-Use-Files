# **Adverse Selection**

Adverse selection is potentially an important issue in a financial market whenever any trader has private information related to the value of an asset. An informed trader will strategically adjust his or her trade across states in a manner that reduces the payoff of an uninformed counterparty. The latter is subject to adverse selection: the likelihood of a transaction increases precisely in those states of the world in which the payoff from the transaction is lower.

## **Adverse Selection in Quote-driven** Markets

Consider a single-period binomial model for one stock. In standard fashion, at time 1, the value of the stock is  $v_h$  with probability  $\pi$  and  $v_\ell$  with probability  $(1 - \pi)$  (see Figure 1). Suppose the riskfree rate is normalized to zero. Then, at time 0, a risk-neutral agent is indifferent between buying and selling any quantity of the stock at the expected value  $v_0 = \pi v_h + (1 - \pi)v_\ell.$ 

Now, suppose our risk-neutral agent at time 0 is asked to trade with an omniscient "informed" counterparty who knows the time 1 value of the stock. If our "uninformed" agent trades at a price  $v_0 = \pi v_h + (1 - \pi)v_\ell$ , he or she will always lose money: the counterparty buys the asset only if the value will be  $v_h$  at time 1, and sells the asset only if the value will be  $v_{\ell}$  at time 1.

In equilibrium, of course, the uninformed trader rationally anticipates such adverse selection. Thus, if the informed counterparty wishes to buy the stock,

![](_page_0_Figure_6.jpeg)

Figure 1 Single-period binomial tree

the uninformed trader is only willing to sell it at  $v_h$ . Similarly, the uninformed trader is only willing to buy the stock at  $v_{\ell}$ . The possibility of adverse selection thus manifests itself as a spread between the ask price (the price at which he or she sells the stock) and the bid price (the price at which he or she buys the stock), thereby imposing a cost on all traders in the market.

The binomial example is perforce stark: we assumed that the counterparty was perfectly informed. More generally, suppose the counterparty is perfectly informed with some probability  $\gamma > 0$ , and uninformed with probability  $1 - \gamma$ . Then, we recover the essence of the Glosten and Milgrom [7] model (see Glosten-Milgrom Models). The bid-ask spread is easily seen to be increasing in  $\gamma$ .

To take the argument one step further, suppose there are a continuum of states at time 1, and the quantity an informed trader wishes to trade at time  $0$ is strictly increasing in value at time 1,  $v_1$ , holding fixed the price of the asset. Then, the uninformed agent should infer that  $v_1$  is higher when the net buy order is higher, so the bid-ask spread is naturally increasing in the quantity of shares traded. This intuition lies behind the Kyle [11] model (see Kyle Model).

### Adverse Selection in Limit Order Markets

There is no market-maker in a limit order market; rather, traders transact directly with each other by posting orders (or price-quantity pairs) in a limit order book, and accepting the orders of other traders. The passage of time since a limit order was submitted allows for new information to arrive at the market. Thus, as Copeland and Galai [3] demonstrate, a limit order is inherently subject to adverse selection.

Suppose  $v_s$ , the expected value of the asset at time  $t_s$ , given all information available to that time, follows some stochastic process. Two kinds of agents are willing to trade in the market: liquidity or noise traders, who are uninformed, and informed traders. Liquidity traders are motivated to trade by unmodeled hedging or portfolio considerations. Each liquidity buyer *i* has a reservation value  $v_i^b$ , which comes from some distribution  $F$ , and is willing to buy at any price less than  $v_i^b$ . Informed traders, on the other hand, will buy only at a price less than  $v_s$  and sell only at a price above  $v_s$ . Each arriving trader is a liquidity trader with probability  $q_{\ell}$  and an informed trader with probability  $1 - q_{\ell}$ .

Now, consider an agent who places a sell order at time  $t_0$ , at an ask price  $p_0 > v_0$ . Suppose a new trader arrives in the market at time  $t_1 > t_0$ . There are two possibilities: (i) The buyer is an uninformed trader. Then, with probability  $1 - F(p_0)$ , no trade occurs. A transaction occurs with probability  $F(p_0)$ , with the limit order seller earning a payoff  $p_0 - E(v_1)$  $v_0$ ). (ii) The buyer is an informed trader. Then, with probability  $Pr(v_1 < p_0)$ , no trade occurs. With probability  $Pr(v_1 \ge p_0)$ , a transaction occurs, and the payoff to the limit order seller is  $p_0 - E(v_1 \mid v_0, v_1 >$  $p_0) < 0.$ 

Adverse selection results in the overall transaction probability,  $q_{\ell}F(p_0) + (1-q_{\ell})\Pr(v_1 \geq p_0),$ being higher when  $v_1 > p_0$ . As Glosten [5] points out, the knowledge that the seller traded with an informed buyer raises the expected value of the asset from  $E(v_1 \mid v_0)$  to the upper tail expectation  $E(v_1 \mid v_0, v_1 > p_0).$ 

The price at which the sell limit order is posted,  $p_0$ , is chosen to maximize the submitter's overall expected payoff. Thus, even a relatively simple model of limit orders with asymmetric information involves a complicated decision on the part of a limit order submitter.

#### Informed Traders Submitting Limit Orders

To take this one step further, an informed trader may submit a limit order. Then, we have double-sided adverse selection: both the trader at  $t_0$  and the trader at  $t_1$  may find themselves trading with a counterparty who possesses better information about the asset's value.

In equilibrium in such a model, will an informed trader submit limit or market orders? This question is posed by Goettler et al. [8]. In their infinite horizon model, a Poisson process determines trader arrival. An uninformed trader observes  $v$  with a lag  $\Delta$ . Traders may reenter the market with some delay. Let  $\omega_s = \{L_s, (\hat{x}_s, \hat{p}_s), v_{s-\Delta}, v_s\}$  denote the state at time  $t_s$ ; the state includes the current limit order book  $L_s$ , whether the most recent transaction resulted from a market buy ( $\hat{x}_s = 1$ ) or sell ( $\hat{x}_s = -1$ ) order, the price  $\hat{p}_s$  at which the most recent transaction occurred, and the lagged  $(v_{s-\Delta})$  and current  $(v_s)$  expectations of asset value. An informed trader observes the state at the time he or she enters the market. An uninformed trader observes a subset of the state,  $\{L_s, (\hat{x}_s, \hat{p}_s), v_{s-\Delta}\}$ . A trader *i* who executes an order  $(x, p)$  when the asset value is v obtains a payoff  $x(\alpha_i + v - p)$ , where  $x = \pm 1$  denotes the direction of the order,  $p$  the price at which it is submitted, and  $\alpha_i$  is a private benefit to trade (in the absence of such a private benefit, a no-trade theorem applies, and no transactions occur). A limit order changes the book to  $L'_{s}$ , thus affecting the states viewed by future traders.

Let  $\phi(v, \tau \mid \omega, x, p)$  be the probability that a trader executes at time  $t_{s+\tau}$  when the value of the asset is  $v$ , if he or she takes action  $(x, p)$  in state  $\omega$ . For an informed trader, adverse selection is manifested in the  $\phi(\cdot)$  function, which, in equilibrium, is increasing in  $v$  for sell orders and decreasing in  $v$ for buy orders. In other words, sell orders are more likely to execute when the asset value has increased (so the sell price is too low) and buy orders when the asset value has decreased (so the buy price is too high). An uninformed trader must take a further expectation over the true state  $\omega$  and thus faces an added layer of adverse selection.

The model is solved numerically. Given the parameters chosen, in equilibrium, over 50% of the time, informed traders have limit orders at the best quotes, the exact proportion varying with asset characteristics. As a result, both the bid and ask prices and order depths from the limit order book are informative about the value of the asset. Uninformed traders therefore update their beliefs about value on observing the book, which mitigates adverse selection.

Thus, in a limit order market, we can expect both limit order submitters and market order submitters in a limit order market to face adverse selection. This result is consistent with the earlier analytic work of Chakravarty and Holden [2], who predict that an informed trader will use both market and limit orders. Bloomfield et al. [1] find that informed traders do use both market and limit orders in an experimental asset market.

## **Empirical Evidence**

Ouantitative estimates of the adverse selection component of the bid-ask spread vary by sample. Glosten and Harris [6] propose using the direction of trade to estimate the adverse selection component of the bid-ask spread in a quote-driven market. Their basic regression equation may be written as

$$\Delta P_t = c_0(Q_t - Q_{t-1}) + \alpha Q_t V_t + \epsilon_t \qquad (1)$$

where *Pt* is the change in transaction price from *t* − 1 to *t*, *Qt* is a trade direction indicator (+1 for a market buy and −1 for a market sell), *Vt* is the size of the order, and  *t* is the change in price due to public information. Here, *c*<sup>0</sup> + *α* equals the halfspread, with *c*<sup>0</sup> representing the transitory component due to market-maker costs of supplying liquidity and *α* the permanent component due to adverse selection. On a sample of 250 NYSE stocks over a 14-month period from December 1981 to January 1983, they estimate that the adverse selection component is on average about 18% of the bid–ask spread.

Madhavan *et al.* [12] extend the basic model to allow for *E*[*Qt* | *Qt*<sup>−</sup><sup>1</sup> = 1] = *ρ*, the first-order autocorrelation in order flow. The adverse selection component depends on the innovation in order flow. They use generalized method of moments to estimate the model on 274 NYSE stocks over the year 1990, and find that the spread and the adverse selection component both vary by time of day, being largest in the initial half-hour of trading. Estimates of the adverse selection component vary from 51% of the spread in the first half-hour to 35–36% over the latter half of the day. Gibson *et al.* [4] conduct a spread decomposition in the postdecimalization era, and find that although overall spreads are lower, the proportion due to adverse selection and inventory holding costs has increased to 55–59% of the total spread.

A different approach to determining the effect of information on prices is taken by Hasbrouck [9], who specifies a vector autoregression for trade direction and the midpoint of the bid and ask quotes. The permanent price impact of an innovation in the trade process then reflects the effect of information in the market. He finds that the full price impact occurs with a protracted lag, suggesting that information is revealed slowly in the market.

Empirical work on adverse selection in limit order markets is based on Glosten's [5] model of an electronic limit order book. de Jong *et al.* [10] find that adverse selection accounts for 25% (small orders) to 60% (large orders) of the spread on the Paris Bourse over a 44-day period in 1991. Sandas [13] conducts a structural test of the model's ˚ restriction that bid prices be equal to the lower tail expectation of asset value given the order size, and ask prices be equal to the corresponding upper tail expectation. The model is rejected, with the slope of the limit order book being too steep. This finding, interestingly, is consistent with noncompetitive limit order submission, suggesting that informed traders submit some proportion of limit orders.

## **Conclusion**

Adverse selection is important to asset pricing for two reasons. First, in a frictionless market, the bid–ask spread should be zero, with all trades occurring at the price *v*0. However, because of the potential asymmetric information between traders, there is now a cost associated with changing a position in the asset. Indeed, if the adverse selection problem is sufficiently severe, the market may even close down.

Second, adverse selection represents a dimension of counterparty risk that is unhedgeable: one cannot directly trade on the event that the counterparty is informed, since such information is typically unverifiable in a court. Thus, we cannot create a replicating portfolio to hedge this risk, so that asymmetric information across traders implies that markets are fundamentally incomplete. This incompleteness may directly affect traders' valuation for an asset and therefore the risk-neutral probabilities themselves.

## **References**

- [1] Bloomfield, R., O' Hara, M. & Saar, G. (2005). The 'make or take' decision in an electronic market: evidence on the evolution of liquidity, *Journal of Financial Economics* **75**, 165–199.
- [2] Chakravarty, S. & Holden, C. (1995). An integrated model of market and limit orders, *Journal of Financial Intermediation* **4**, 213–241.
- [3] Copeland, T. & Galai, D. (1983). Information effects on the bid-ask spread, *Journal of Finance* **38**(5), 1457–1469.
- [4] de Jong, F., Nijman, T. & Roell, A. (1996). Price effects ¨ of trading and components of the bid-ask spread on the Paris Bourse, *Journal of Empirical Finance* **3**(2), 193–213.
- [5] Gibson, S., Singh, R. & Yerramilli, V. (2003). The effects of decimalization on the components of the bid-ask spread, *Journal of Financial Intermediation* **12**, 121–148.
- [6] Glosten, L. (1994). Is the electronic limit order book inevitable? *Journal of Finance* **49**, 1127–1161.

- [7] Glosten, L. & Harris, L. (1988). Estimating the components of the bid/ask spread, *Journal of Financial Economics* **21**(1), 123–142.
- [8] Glosten, L. & Milgrom, P. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders, *Journal of Financial Economics* **14**, 71–100.
- [9] Goettler, R., Parlour, C. & Rajan, U. (2008). Informed traders and limit order markets, *Journal of Financial Economics*. Forthcoming.
- [10] Hasbrouck, J. (1991). Measuring the information content of stock trades, *Journal of Finance* **46**(1), 179–207.

- [11] Kyle, A. (1985). Continuous auctions and insider trading, *Econometrica* **53**, 1315–1335.
- [12] Madhavan, A., Richardson, M. & Roomans, M. (1997). Why do security prices change? A transaction-level analysis of NYSE stocks, *Review of Financial Studies* **10**(4), 1035–1064.
- [13] Sandas, P. (2001). Adverse selection and competitive ˚ market-making: empirical evidence from a limit order market, *Review of Financial Studies* **14**, 705–734.

CHRISTINE A. PARLOUR & UDAY RAJAN
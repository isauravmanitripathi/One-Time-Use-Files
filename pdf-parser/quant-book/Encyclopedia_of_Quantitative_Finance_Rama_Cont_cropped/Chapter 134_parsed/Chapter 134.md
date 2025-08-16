# **Put–Call Parity**

Put-call parity means that one may switch between call and put positions by selling or buying the underlying forward: "long call, short put is long forward contract" or  $\mathbf{c} - \mathbf{p} \equiv \mathbf{f}$ . In other words, one may replicate a put contract by buying a call of identical characteristics (underlying asset, strike, maturity) and selling the underlying asset forward  $(\mathbf{p} \equiv \mathbf{c} - \mathbf{f})$ , and one may replicate a call by buying a put and the underlying forward ( $\mathbf{c} \equiv \mathbf{p} + \mathbf{f}$ ). This is shown in the three payoff diagrams (Figures  $1-3$ ).

A logical proof of the third instance  $(c \equiv p + f)$ is as follows: a rational investor will exercise a call option whenever the asset price  $S$  at maturity is above the strike  $K$ ; this is equivalent to promising to buy the asset at  $K$  and having the option to sell it at that level, which a rational investor will exercise whenever  $S$ falls below  $K$ 

Put-call parity is often referred to as *option syn*thetics by practitioners and holds only for European options.<sup>a</sup> It does not require any assumption other than the ability to buy or sell the asset forward, but it is worth noting that this may not always be the case: to sell forward, either a futures market must exist or one must be able to short-sell the asset.

Put-call parity must not be confused with "put-call symmetry" (see Foreign Exchange Symmetries) in foreign exchange, which states that a call struck at  $K$  on a given exchange rate  $S$  (e.g., dollars per leuro) is identical to a put struck at  $1/K$  on the reverse rate  $1/S$  (euros per 1 dollar), after the *ad hoc* numeraire conversions:  $c(S, K)/S \equiv$  $K \ p(1/S, 1/K).$ 

#### **Price Relationship**

Assuming no arbitrage, the synthetic relationship immediately translates into the well-known price relationship: "call minus put equals forward" or  $c_t - p_t = f_t$ . Note that here  $f_t$  denotes the price of a forward contract struck at  $K$ , that is, the present value (p.v.) of the gap between the forward price  $F_t$ and the strike price  $K$  (see Forwards and Futures). Denoting the price of the zero-coupon bond maturing

at T by  $B_t$  and rearranging terms, we have

$$\text{call} + \text{p.v. of strike price}$$

 $=$  put  $+$  p.v. of forward price (1)

$$c_t + K \cdot B_t = p_t + F_t \cdot B_t \tag{2}$$

For all investment assets where short selling is feasible, the forward price can be further expressed as a function of the spot price  $S_t$  and the revenue or cost of carry until maturity  $T$  (see Forwards and **Futures**). For example, the forward price of a stock with continuous dividend rate q satisfies  $F_t = S_t/B_t$ .  $\exp(-q(T-t))$ , and put-call parity simplifies to

$$c_t + K \cdot B_t = p_t + S_t \cdot e^{-q(T-t)} \tag{3}$$

In practice, Kamara and Miller [5] give empirical evidence that while put-call parity has many small violations, almost half of the arbitrages would result in a loss when execution delays are accounted for.

#### **Basic Implications**

or

- For trading purposes, puts and calls are identical instruments (up to a directional position in the underlying asset).
- . At-the-money-forward calls and puts must have the same value. (An at-the-money-forward option has its strike set at the forward price of the underlying asset.)
- In the absence of revenue or cost of carry, . the deltas (see Black-Scholes Formula; Delta **Hedging**) of a call and put must add up to 1 (in absolute value).
- Puts and calls must have the same gamma and vega (see Black-Scholes Formula; Gamma Hedging).

In volatility modeling, put-call parity implies that calls and puts of identical characteristics must have the same **implied volatility**.

In exotic option pricing, Carr and Lee [1] put forward the idea of a generalized American option that may be indefinitely exercised until maturity to lock-in the intrinsic value and switch between call and put styles. The authors show that this option may be replicated by holding onto a European

![](_page_1_Figure_1.jpeg)

![](_page_1_Figure_2.jpeg)

**Figure 1 c − p ≡ f**

![](_page_1_Figure_4.jpeg)

**Figure 2 p ≡ c − f**

vanilla call and subsequently selling and buying the forward contract at every exercise. This strategy is a straightforward illustration of how put–call parity may be exploited to alternate between call and put positions by only trading in the forward contract.

![](_page_1_Figure_7.jpeg)

## **History**

Haug [3] traces put–call parity as far back as the seventeenth century, but its formulation was then "diffuse". According to the author, an early formulation of put–call parity "as we know it" can be found in the work by Higgins [4], who wrote in 1902:

It can be shown that the adroit dealer in options can convert a 'put' into a 'call', a 'call' into a 'put' [*...*] by dealing against it in the stock.

Derman and Taleb [2] argue that the Black–Scholes– Merton formulas could have been established earlier than 1973 *via* put–call parity instead of the dynamic replication argument. Specifically, the authors cite similar formulas published in the 1960s, all of which "involved unknown risk premiums that would have been determined to be zero had [*...*] the put–call replication argument" been used.

Put–call parity can fail when there are restrictions on short selling, when the underlying asset is hard to borrow or illiquid, or in the case of corporate events such as leveraged buyouts.

## **End Notes**

a*.* The reason put–call parity fails with American options is best seen in the first instance (**c − p ≡ f**), whereby an agent attempts to replicate a forward contract by buying a call and selling a put. If the put is American, it may be exercised against the agent before maturity, thus breaking the replication strategy.

## **References**

- [1] Carr, P. & Lee, R. (2002). *Hyper Options*. Working paper, Courant Institute and Stanford University, December 2002.
- [2] Derman, E. & Taleb, N.N. (2005). The illusions of dynamic replication, *Quantitative Finance* **5**(4), 323–326.
- [3] Haug, E. (2007). *Derivatives: Models on Models*. Wiley.

- [4] Higgins, L.R. (1902). *The Put-and-Call*. E. Wilson, London.
- [5] Kamara, A. & Miller, T.W. (1995). Daily and intradaily tests of European put-call parity, *Journal of Financial and Quantitative Analysis* **30**, 519–539.

## **Related Articles**

**Black–Scholes Formula**; **Call Options**; **Forwards and Futures**; **Option Pricing: General Principles**; **Options: Basic Definitions**.

SEBASTIEN ´ BOSSU
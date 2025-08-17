# **Forwards and Futures**

Futures and forwards are financial contracts that make it possible to reduce the price risk that arises from the intention to buy or sell certain assets at a later date. A forward contract specifies in advance the price that will be paid at such a later date for the delivery of the asset. This obviously reduces the price risk for that transaction to zero for all parties involved. A futures contract, on the other hand, guarantees that changes in the asset's price that occur before the delivery date will be compensated for immediately when they arise. This compensation is achieved by offsetting payments into a bank account that is called the *margin account*. This significantly reduces the price risk associated with the futures transaction, since the only possible remaining source of uncertainty is now due to the interest rate used for the margin account.

The assets that are bought or sold at the delivery date can be storable commodities (such as gold, oil, and agricultural products), nonstorable commodities (such as electricity), or other financial assets (such as stocks, bonds, options, or currencies). Forward contracts are also used by parties to agree in advance on an interest rate that will be paid or charged during a later time period, in so-called forward rate agreements (FRAs). Similarly, one can buy and sell futures on the value of money deposited in a bank account. For such interest rate futures, which include the very popular eurodollar and euribor contracts, there is no actual delivery but the contract is fulfilled by cash settlement instead.

Here, we discuss only the general pricing principles for forwards and futures. We refer to other articles in the encyclopedia for detailed information concerning the delivery procedures and methods to quote prices for specific futures and forward contracts, such as eurodollar futures (*see* **Eurodollar Futures and Options**), forward rate agreements (*see* **LIBOR Rate**), electricity (*see* **Electricity Forward Contracts**), commodity (*see* **Commodity Forward Curve Modeling**), and foreign exchange forwards (*see* **Currency Forward Contracts**).

# **Using Futures and Forwards**

Forward contracts are usually agreed upon by two parties who directly negotiate the terms of such contracts, which can therefore be very flexible. The two parties need to agree on the specific asset (often called *the underlying asset*) and on the precise quantities that are bought or sold, on the exact date when the transactions take place (the *delivery date*), and the price that will be charged on that date (the *forward price*). Usually the forward price is chosen in such a way that both parties agree to sign the contract without any money changing hands before the delivery date. This implies that the forward contract starts with having zero market value, since both parties are willing to sign it without receiving or paying any money for it. Later on, the contract may have a positive or negative market value, since every change in the market price of the underlying asset will make the existing agreement as written in the contract more beneficial to one of the parties and less beneficial to the other one. The forward contract may, therefore, become a serious liability for one of the two parties involved, so there is the risk that this party is no longer willing or able to honor the terms of the contract on the delivery date. This counterparty risk problem can be avoided by the use of futures contracts.

Futures are standardized contracts that are traded on futures exchanges. When entering a futures contract, a margin account on the futures exchange is opened and a payment into that account is required, to make it possible for the exchange to withdraw money when appropriate. The exchange publishes a *futures price* for every contract, which is updated regularly to reflect price changes in the underlying. Whenever a new futures price is announced, an amount of cash that is equal to the difference between the new futures price and the previous one is paid into or withdrawn from the margin account, depending on whether one is *short* the contract or *long* the contract. Parties that intend to buy the underlying are long the contract, and they, therefore, receive money if the futures price goes up and pay when it goes down. Parties that intend to sell are short the contract, and they, therefore, pay money if the futures price goes down and receive money when it goes up. This procedure is known as *marking to market*. Since on the delivery date the futures price is always equal to the underlying asset price, a possible difference between the initial futures price and the current asset price has been compensated for by the intermediate payments into the margin account.

Parties with opposite positions in the futures market deal only with the exchange instead of with each other, which explains the need for standardized contracts and the significant reduction in counterparty risk. Since no cash is needed to enter into a new (long or short) futures contract as long as there is enough money left in the margin account, it is easy to change a position in futures once such an account has been established. One can terminate existing long contracts by simply taking a position in offsetting short contracts or *vice versa*, and many parties close their position just before the delivery date if they are only interested in compensation for price changes and not in the actual delivery. This makes futures very convenient to use for hedging purposes (see **Hedging**) and for speculation on an underlying's price movements. Likewise, it is quite easy for the exchange to close the futures position of a party who refuses to put more money in their margin account when asked to do so in the so-called margin call.

These characteristics have made futures very popular financial instruments and the market for them is huge. In 2008, more than eight billion futures contracts were traded worldwide with underlying assets<sup>a</sup> in equity indices  $(37\%)$ , individual equity  $(31\%)$ , interest rates (18%), agricultural goods (5%), energy (3%), currencies (3%), and metals (2%). The most popular are contracts on the S&P 500 and Dow Jones indices, followed by eurodollar and eurobund futures, and contracts on white sugar, soybeans, crude oil, aluminum, and gold. The notional amounts underlying futures on interest rates, equity indices, and currencies at the world's exchanges were estimated to be 27 trillion, 1.6 trillion, and 175 billion US dollars, respectively, in June  $2008^{\text{b}}$ .

# **Pricing Methods for Forwards in Discrete** Time

To analyze the futures and forward prices, we first look at discrete-time models, and then look at generalizations in continuous time.

Consider a discrete-time market model on a probability space  $(\Omega, \mathcal{F}, \mathbb{P})$  with a filtration  $(\mathcal{F}_n)_{n \in \mathcal{N}}$  where  $\mathcal{N} = \{0, 1, ..., N\}$  denotes our discrete-time set. We define assets  $S$  and  $B$  to model the underlying asset and a bank account, respectively, with associated stochastic price processes  $(S_n)_{n\in\mathcal{N}}$  and  $(B_n)_{n\in\mathcal{N}}$ . We assume that  $S$  is adapted and that  $B$  is predictable with respect to this filtration, and that both  $B$  and  $1/B$  are bounded. Associated with the asset S are cash flows  $(D_n)_{n\in\mathcal{N}}$  where  $D_n$  denotes the sum of all cash flows caused by holding one unit of  $S$  at

time  $n$ . These cash flows can be positive (such as dividends when  $S$  is a stock, or interest when  $S$  is a currency) or negative (such as storage costs when  $S$  is a commodity). We will always assume perfect market liquidity (see **Liquidity**), so all assets can be bought and sold in all possible quantities for their current market prices and no transaction costs (see Transaction Costs) are charged.

The cash flows associated with a forward contract that is initiated at time  $T_0 \in \mathcal{N}$  take place at the time of delivery  $T_d \in \mathcal{N}$  that is specified in the contract, with  $T_0 \leq T_d$ . At time  $T_d$ , the asset is delivered while the forward price agreed upon at the initial time  $T_0$  for delivery at time  $T_d$ , which we denote by  $F(T_0, T_d)$ , is paid in return. Since this forward price needs to be determined at time  $T_0$ , it should be  $\mathcal{F}_{T_0}$ -measurable. Moreover, the forward price is chosen in such a way that both parties agree to enter the contract without any cash changing hands at this initial time.

In complete and arbitrage-free markets (see Arbi**trage Pricing Theory**), it is often possible to find an explicit expression for the forward price  $F(T_0, T_d)$ , since the cash flows associated with the contract can then be replicated using other assets with known prices. Let us assume that there exists a unique martingale measure  $\mathbb{Q}$ , which is equivalent to  $\mathbb{P}$ , such that the discounted versions of tradable assets are martingales under this measure (see **Equivalent Martingale Measures**). This is almost equivalent to the assumption of a complete and arbitrage-free market; for the exact statement (see Fundamental **Theorem of Asset Pricing**). Contingent claims that pay a cash-flow stream of  $\mathcal{F}_n$ -measurable amounts  $X_n$  at the times  $n \in \mathcal{N}$  in such markets have a unique price p at time  $k \in \mathcal{N}$  equal to

$$p_k = \sum_{n \in \mathcal{N}, n \ge k} B_k \, \mathbb{E}^{\mathbb{Q}}[X_n / B_n \mid \mathcal{F}_k] \tag{1}$$

A specific example is the zero-coupon bond price at time  $k$  for the delivery of one unit cash at time  $T > k$ , which is equal to  $p(k, T) = B_k \mathbb{E}^{\mathbb{Q}}[1/B_T |$  $\mathcal{F}_k$ ].

Suppose that an investor enters into a forward contract at time  $T_0$ , which obliges him/her to deliver the underlying asset S at time  $T_d$ , and that he/she buys the underlying asset at time  $T_0$  to hold it until delivery. This will lead to a cashflow of  $-S_{T_0}$  at time  $T_0$ , to cash flows  $D_n$  at times  $\{n \in \mathcal{N}: T_0 \le n \le T_d\}$ , and a cash flow of  $F(T_0, T_d)$  at time  $T_d$  when he/she delivers the asset. Since a forward contract is entered into without any money changing hands and since the net position after delivery will be zero, the value of the cash-flow stream defined above must be zero if there is no arbitrage in the market. Using the previous equation, we thus find that

$$0 = -S_{T_0} + B_{T_0} \mathbb{E}^{\mathbb{Q}} [F(T_0, T_d) / B_{T_d} | \mathcal{F}_{T_0}]$$
  
+ 
$$\sum_{T_0 \le n \le T_d} B_{T_0} \mathbb{E}^{\mathbb{Q}} [D_n / B_n | \mathcal{F}_{T_0}]$$
(2)

Since *F (T*0*, Td )* is F*T*<sup>0</sup> -measurable, this leads to the following expression for a forward price in a complete and arbitrage-free market:

$$F(T_{0}, T_{d}) = \frac{S_{T_{0}}/B_{T_{0}} - \sum_{T_{0} \leq n \leq T_{d}} \mathbb{E}^{\mathbb{Q}}[D_{n}/B_{n} \mid \mathcal{F}_{T_{0}}]}{\mathbb{E}^{\mathbb{Q}}[1/B_{T_{d}} \mid \mathcal{F}_{T_{0}}]}$$
$$= \frac{S_{T_{0}} - B_{T_{0}} \sum_{T_{0} \leq n \leq T_{d}} \mathbb{E}^{\mathbb{Q}}[D_{n}/B_{n} \mid \mathcal{F}_{T_{0}}]}{p(T_{0}, T_{d})}$$
(3)

In particular, when there are no dividends or storage costs, the forward price is simply equal to the current price of the underlying asset divided by the appropriate discount rate until delivery. For commodities, where the cash flows *Dn* are often negative since they represent storage costs, this formula (3) is known as the *cost-of-carry formula*. Conversely, when the actual possession of an underlying asset is more beneficial than just holding the forward contract, this can be modeled by introducing positive cash flows *Dn*. Such benefits are often expressed as a rate, the so-called convenience yield, which may fluctuate as a result of changing expectations concerning the availability of the underlying asset on the delivery date.

The initial price of a forward contract is zero, but when the underlying asset's price changes, so does the value of an existing contract. If we denote by *G(T*0*, Td , k)* the value at time *k* of a forward contract entered at time *T*<sup>0</sup> ≤ *k* for delivery at time *Td* ≥ *k*, then a similar argument as before leads to

$$G(T_0, T_d, k) = B_k \mathbb{E}^{\mathbb{Q}} \left[ \frac{F(k, T_d) - F(T_0, T_d)}{B_{T_d}} \middle| \mathcal{F}_k \right]$$
  
=  $p(k, T_d) \left( F(k, T_d) - F(T_0, T_d) \right)$  (4)

# **Pricing Methods for Futures in Discrete Time**

All cash flows associated with a futures contract take place *via* the margin account. Let *(Mn)n*<sup>∈</sup><sup>N</sup> be the process describing the value of the margin account associated with a long position in one future on the underlying asset *S* defined above. If *f (k, Td )* is the futures price at time *k* for delivery of one unit of the asset at time *Td > k* (*k, Td* ∈ N), then the margin account values will satisfy

$$M_{k+1} = \frac{B_{k+1}}{B_k} M_k + f(k+1, T_d) - f(k, T_d) \quad (5)$$

where we assume that the interest rate used for the margin account is the same as the one used for *B*.

Futures prices are determined by supply and demand on the futures exchanges, but if we assume a complete and arbitrage-free market for *S* and *B*, we can derive a theoretical formula for the futures price. We consider an investment strategy where at a certain time *k* ∈ N, we open a new margin account, put an initial margin amount *Mk* into it, and take a long position in a futures contract for delivery at time *Td* . One time step later, we go short one future contract for the same delivery date, which effectively closes our futures position, and we then empty our margin account. Since our net position is then zero again and since we do not pay or receive money to go long or short a futures contract, the total value of this cash-flow stream at time *k* should be equal to zero, so

$$0 = -M_k + B_k \mathbb{E}^{\mathbb{Q}} \left[ \frac{M_{k+1}}{B_{k+1}} \middle| \mathcal{F}_k \right]$$
$$= B_k \mathbb{E}^{\mathbb{Q}} \left[ \frac{f(k+1, T_d) - f(k, T_d)}{B_{k+1}} \middle| \mathcal{F}_k \right] \quad (6)$$

Since *B* was assumed to be predictable, that is, *Bk*<sup>+</sup><sup>1</sup> is F*<sup>k</sup>* -measurable for all *k* ∈ N \ {*N*}, we may conclude from the above that the futures price process *f (*·*, Td )* is a *-*-martingale for any fixed delivery date *Td* ∈ N, and hence

$$f(k, T_d) = \mathbb{E}^{\mathbb{Q}}[S_{T_d} | \mathcal{F}_k]$$
(7)

since *f (Td , Td )* = *STd* . Note that this formula no longer holds if *B* fails to be predictable or when the interest rates paid on the bank account *B* and the margin account *M* are different.

# **Continuous-time Models**

The generalization to continuous-time models is rather straightforward for forward contracts, but more subtle for futures contracts.

Assume that the price process of the underlying asset is a stochastic process *S* on a probability space *(,* F*, )* with a filtration *(*F*t)t*<sup>∈</sup>[0*,T* ] that satisfies the usual conditions, that is, it is right continuous and F<sup>0</sup> contains all -null sets. We will assume that the process *S* is an adapted semimartingale and that the bank account process *B* is an adapted and predictable semimartingale, and *B* and 1*/B* are assumed to be bounded almost surely. We model the dividend and storage costs of the asset *S* using an adapted semimartingale *D*, with the interpretation that the total amount of dividends received minus the storage costs paid between two times *t*<sup>1</sup> and *t*<sup>2</sup> is equal to *Dt*<sup>2</sup> − *Dt*1<sup>−</sup> where 0 ≤ *t*<sup>1</sup> *< t*<sup>2</sup> ≤ *T* .

To determine the correct forward price *F (T*0*, Td )* for a forward contract initiated at time *T*<sup>0</sup> for delivery at time *Td* , we follow the same arguments as in the discrete-time case. If we borrow money to buy the underlying asset today and then hold on to it until we deliver it at the delivery date in return for a payment of the forward price, the total value of this cash-flow stream should be zero since we enter the forward contract without any cash payments. Therefore, *pt* should be zero in the formula above if we substitute *t* = *T*<sup>0</sup> and the cash-flow stream

$$X_{t} = 0, (t < T_{0}, t > T_{d}), \quad X_{T_{0}} = -S_{T_{0}},$$
  

$$X_{t} = D_{t} (t \in ]T_{0}, T_{d}[), \quad X_{T_{d}} = D_{T_{d}} + F(T_{0}, T_{d})$$
(9)

Using the fact that the forward price *F (T*0*, Td )* must be F*T*<sup>0</sup> -measurable then leads to

$$F(T_0, T_d) = \frac{1}{p(T_0, T_d)} \left( S_{T_0} - B_{T_0} \mathbb{E}^{\mathbb{Q}} \left[ \int_{T_0}^{T_d} \left( \frac{\mathrm{d}D_u}{B_{u-}} + \mathrm{d} \left[ D, \frac{1}{B} \right]_u \right) \, \big| \mathcal{F}_{T_0} \right] \right) \tag{10}$$

As in the discrete-time case, we assume that we have a complete and arbitrage-free market and that there exists a unique measure  that is equivalent to such that discounted versions of tradable assets become martingales under this measure (*see* **Equivalent Martingale Measures**). We model contingent claims by a cumulative cash-flow stream *(Xt)t*<sup>∈</sup>[0*,T* ], which is an adapted semimartingale. The total cash amount paid out by the contingent claim between two times *t*<sup>1</sup> and *t*<sup>2</sup> is given by *Xt*<sup>2</sup> − *Xt*1<sup>−</sup>, and *Xt* − *Xt*<sup>−</sup> corresponds to a payment at the single time *t* (with *t,t*1*, t*<sup>2</sup> ∈ [0*, T* ] and *t*<sup>2</sup> ≥ *t*1). Such contingent claims have a unique price *p* in a complete and arbitrage-free market, which at time *t* is equal to

$$p_{t} = B_{t} \mathbb{E}^{\mathbb{Q}} \left[ \int_{t}^{T} \left( \frac{\mathrm{d}X_{u}}{B_{u-}} + \mathrm{d} \left[ X, \frac{1}{B} \right]_{u} \right) \, \big| \, \mathcal{F}_{t} \right] \tag{8}$$

The last term involving the brackets compensates for the fact that the cash flows *X* and the bank account may have nonzero covariation, so it disappears when *B* has finite variation and is continuous, or when *B* is deterministic. Compare this to the discrete-time case, where we assumed that *(Bn)n*<sup>∈</sup><sup>N</sup> is predictable.

The formula for the value of a forward contract at a later time after *T*<sup>0</sup> is the same as in the discrete-time case.

We now turn to the definition of a futures price process *(f (t, Td ))t*<sup>∈</sup>[0*,Td* ] in continuous time for delivery at a fixed time *Td* ∈ [0*, T* ]. Let *(ψt)t*<sup>∈</sup>[0*,Td* ] be a futures investment strategy: a bounded and predictable stochastic process such that *ψt* represents the number of futures contracts (positive or negative) we own at time *t*. The associated margin account process *(Mt)t*<sup>∈</sup>[0*,T* ]is then defined on [0*, T* ] as

$$\mathrm{d}M_t = M_t \frac{\mathrm{d}B_t}{B_{t-}} + \psi_t \,\mathrm{d}f(t, T_d) \tag{11}$$

with *M*<sup>0</sup> ∈ , where we have again assumed that the margin account earns the same interest rate as the bank account *B*. As mentioned before, the futures price process should be equal to the underlying asset price at delivery, so *f (Td , Td )* = *STd* .

In a complete and arbitrage-free market, we consider an investment strategy where at any time *t* ∈ [0*, Td* ] we open a new margin account and put an initial margin amount *Mt* in, go long one future contract at time *t*, wait until a later date *s* ∈]*t,Td* ] and close our futures position by going short one contract, and close our margin account. If there is no arbitrage, the discounted value of the cash flows from this strategy should be zero at time  $t$  since we start and end without any position, so

$$M_t = B_t \mathbb{E}^{\mathbb{Q}} \left[ \frac{M_s}{B_s} \middle| \mathcal{F}_t \right] \tag{12}$$

This shows that  $M/B$  is a martingale under  $\mathbb{Q}$ , that is, the margin account should be a tradable asset. A bit of stochastic calculus shows that

$$\mathbf{d}\left(\frac{M_t}{B_t}\right) = \frac{\mathbf{d}f(t,T_d)}{B_{t-}} + \mathbf{d}\left[f(\cdot,T_d),\frac{1}{B}\right]_t \quad (13)$$

and we see that if  $B$  is continuous, of finite variation. bounded, and bounded away from zero, then the futures price process  $f(\cdot, T_d)$  is itself a martingale under  $\mathbb{Q}$  and hence

$$f(t, T_d) = \mathbb{E}^{\mathbb{Q}} \left[ f(T_d, T_d) \mid \mathcal{F}_t \right] = \mathbb{E}^{\mathbb{Q}} \left[ S_{T_d} \mid \mathcal{F}_t \right]$$
(14)

Note that in this case the difference between the forward and futures prices can be expressed as

$$F(t, T_d) - f(t, T_d)$$

$$= \frac{B_{T_0}}{p(T_0, T_d)} \left( \mathbb{E}^{\mathbb{Q}} \left[ \frac{S_{T_d}}{B_{T_d}} \middle| \mathcal{F}_{T_0} \right] - \mathbb{E}^{\mathbb{Q}} \left[ S_{T_d} \middle| \mathcal{F}_{T_0} \right] \mathbb{E}^{\mathbb{Q}} \left[ \frac{1}{B_{T_d}} \middle| \mathcal{F}_{T_0} \right] \right) \quad (15)$$

Since the expression in brackets is the  $\mathcal{F}_{T_0}$ conditional covariance between  $S_{T_d}$  and  $1/B_{T_d}$ , we immediately see that forward and futures prices coincide if and only if these two stochastic variables are uncorrelated when conditioned on  $\mathcal{F}_{T_0}$ , for example, when the bank account  $B$  is deterministic.

#### Extensions

For clarity of exposition, we have focused here on forward and future prices in complete and arbitragefree markets without transaction costs (see Transaction Costs). Early papers on the theoretical pricing methods are by Black [3] for deterministic interest rates and Cox et al. [5] and Jarrow and Oldfield [9] for the general case. Continuous resettlement is

treated by Duffie and Stanton [7] and Karatzas and Shreve [10], see also [12]. See [2] for a very clear summary of the principles involved. For excellent introductions to the practical organization of futures and forward markets and for empirical results on prices, the books by Duffie [6], Hull [8], and Kolb [11] are recommended.

For incomplete markets, there is a theory of equilibrium in futures market under mean-variance preferences; see, for example, [14] and the consumption-based capital asset pricing model of Breeden [4] (*see also* **Capital Asset Pricing Model**). Many futures allow a certain flexibility regarding the exact product that must be delivered and regarding the time of delivery. The value of this last "timing option" is analyzed in a paper by Biagini and Biörk [1].

When the bank account process  $B$  is not of finite variation and continuous, the futures price is no longer a martingale under  $\mathbb{Q}$ ; however under some technical conditions, it can be shown to be a martingale under another equivalent measure that can be found using a multiplicative Doob-Meyer decomposition (*see* **Doob–Meyer Decomposition**) as shown in [15]. The assumption that  $B$  and  $1/B$  are bounded is often too restrictive in practice; see [13] for weaker conditions.

#### **End Notes**

<sup>a.</sup>Sector estimates based on the US data, by the Futures Industry Association.

<sup>b.</sup> Ouarterly Review, December 2008, Bank for International Settlements.

#### References

- $[1]$ Biagini, F. & Björk, T. (2007). On the timing option in a futures contract, *Mathematical Finance* **17**(2), 267–283.
- [2] Björk, T. (2004). Arbitrage Theory in Continuous Time, 2nd Edition, Oxford University Press.
- Black, F. (1976). The pricing of commodity contracts, [3] *Journal of Financial Economics*  $3(1-2)$ , 167–179.
- Breeden, D.T. (1980). Consumption risk in futures [4] markets, Journal of Finance 35(2), 503-520.
- Cox, J.C., Ingersoll, J. Jr. & Ross, S.A. (1981). The [5] relation between forward prices and futures prices, Journal of Financial Economics 9(4), 321–346.
- [6] Darell, D. (1989). Futures Markets, Prentice-Hall.
- [7] Duffie, D. & Stanton, R. (1992). Pricing continuously resettled contingent claims, Journal of Economic *Dynamics and Control* **16**(3–4), 561–573.

# **6 Forwards and Futures**

- [8] Hull, J. (2003). *Options, Futures and Other Derivatives*, 5th Edition, Prentice-Hall.
- [9] Jarrow, R.A. & Oldfield, G.S. (1981). Forward contracts and futures contracts, *Journal of Financial Economics* **9**(4), 373–382.
- [10] Karatzas, I. & Shreve, S. (1998). *Methods of Mathematical Finance*, Springer-Verlag.
- [11] Kolb, R. (2003). *Futures, Options, and Swaps*, 4th Edition, Blackwell Publishing.
- [12] Norberg, R. & Steffensen, M. (2005). What is the time value of a stream of investments? *Journal of Applied Probability* **42**, 861–866.
- [13] Pozdnyakov, V. & Steele, J.M. (2004). On the martingale framework for futures prices, *Stochastic Processes and Their Applications* **109**, 69–77.
- [14] Richard, S.F. & Sundaresan, M.S. (1981). A continuous time equilibrium model of forward prices and futures

prices in a multigood economy, *Journal of Financial Economics* **9**(4), 347–371.

[15] Vellekoop, M. & Nieuwenhuis, H. (2007). *Cash Dividends and Futures Prices on Discontinuous Filtrations*. Technical Report 1838, University of Twente.

# **Related Articles**

**Commodity Forward Curve Modeling**; **Currency Forward Contracts**; **Electricity Forward Contracts**; **Eurodollar Futures and Options**; **LIBOR Rate**.

MICHEL VELLEKOOP
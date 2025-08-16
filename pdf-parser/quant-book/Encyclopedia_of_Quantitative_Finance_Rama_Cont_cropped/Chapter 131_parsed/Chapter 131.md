# **Equity Swaps**

A swap contract is a bilateral agreement between two parties, known as counterparties, to exchange cash flows at regularly scheduled dates in the future. In an equity swap, some of the cash flows are determined by the return on a stock or an equity index. Typically, one of the parties pays to the other the total return of a stock or an equity index. In exchange, he or she receives from the other a cash flow determined by a fixed or floating rate or the return of another stock or equity index. Equity swaps are also known as *equity-linked swaps* and *equity-indexed swaps*.

Equity swaps are not traded on an exchange but are privately negotiated. They are referred to as over-the-counter (OTC) contracts. One of the firstknown equity swap agreements was offered by the Bankers Trust in 1989. Since then, the market for equity swaps and other equity-linked derivatives has grown rapidly. There are no exact figures on the size of the market. However, the Bank for International Settlements (BIS) provides market size estimates. According to BIS, the estimate of the worldwide total notional amounts outstanding of equity swaps and equity forwards was over \$300 trillion as of December 2007.

Equity swaps provide means to get exposure to the underlying stock or index without making a direct investment. Because equity swaps are OTCcontracts, they can be tailor-made to specific needs. The contracts have been used to circumvent barriers for direct investments in particular markets, bypass various taxes, and minimize transaction costs.

# **Defining Equity Swaps**

Let {*T*0*, T*1*,...,TM* } be a sequence of dates. This is the *tenor structure* and we denote it by T. For a given day-count convention, we specify a sequence of year fractions<sup>a</sup> {*δ*1*, δ*2*,...,δM*} to <sup>T</sup>. We denote the counterparties by *A* and *B*.

### **Definition 1 A generic equity swap**

*An equity swap with tenor structure* T *is a contract that starts at time T*<sup>0</sup> *and has payment dates T*1*, T*2*, ... , TM . At each payment date Ti for i* = 1*,* 2*, ...M, the two counterparties A and B exchange payments. At least one of the payments will be based* *on the return of a stock or an equity index over the period* [*Ti*<sup>−</sup>1*, Ti*]*.*

In general, the cash flows are specified in such a way that the initial value, at time *T*0, of the swap equals zero. Usually the equity swap pays out the total return of the underlying stock or equity index including dividends. However, there are also variants where the dividend is excluded.

A swap contract has a notional principal.<sup>b</sup> It is a currency amount specified in the swap contract that determines the size of the payments expressed in currency units. While the notional principal of a bond, for instance, is paid out at maturity, the notional principal of a swap contract is, in general, never exchanged. Equity swaps can be classified into two categories depending on whether the notional principal is constant or varies over the lifetime of the swap. We focus on the former case, which is considered in the next section.

## *Contracts with Fixed Notional Principal*

Let *N* denote the fixed notional principal. Let {*Z(t)*} denote the price process of a stock or an equity index. Define the *period return R(Ti, Ti*<sup>+</sup>1*)* over the interval [*Ti, Ti*+1] for asset *Z* by

$$R(T_i, T_{i+1}) = \frac{Z(T_{i+1})}{Z(T_i)} - 1 \tag{1}$$

**Definition 2 A generic equity-for-fixed-rate swap**

*An equity-for-fixed-rate swap, with tenor structure* T*, which is written on the equity Z will have a predetermined swap rate K and will give rise to the following payments between the counterparties A and B at each payment date Ti:*

- *A pays to B the amount: NR(Ti*<sup>−</sup>1*, Ti).*
- *B pays to A the amount: NδiK.*

In general, the swap rate is chosen such that the initial value of the swap at time *T*<sup>0</sup> equals zero.

In its most simple form, this contract is referred to as a *plain vanilla equity swap*. The period return is then determined by a domestic asset or index and the nominal amount is expressed in units of the domestic currency. Examples can be found in [5] and [8].

Some equity swaps are structured so that instead of a fixed swap rate they pay a floating interest rate, usually a LIBOR rate. Let  $L(T_i, T_{i+1})$  denote the simple spot rate over the period  $[T_i, T_{i+1}]$ .

## **Definition 3 A generic equity-for-floating-rate** swap

An equity-for-floating-rate swap, with tenor structure  $T$ , which is written on the equity Z will give rise to the following payments between the counterparties A and B at each payment date  $T_i$ :

- A pays to B the amount:  $NR(T_{i-1}, T_i)$ . .
- B pays to A the amount:  $N\delta_i$   $(L(T_{i-1}, T_i) + s)$ .

where  $s$  is a constant rate such that the initial value of the swap at time  $T_0$  equals zero.

An equity-for-floating swap can be decomposed into an equity-for-fixed swap and a suitably chosen interest rate swap (see LIBOR Rate and [2]).

Let  $R_1$  and  $R_2$  denote the return of assets  $Z_1$  and  $Z_2$ , respectively.

#### **Definition 4 A generic equity-for-equity swap**

An equity-for-equity swap, with tenor structure T, which is written on the equities  $Z_1$  and  $Z_2$ , will give rise to the following payments between the counterparties A and B at each payment date  $T_i$ :

- A pays to B the amount:  $NR_1(T_{i-1}, T_i)$ .
- B pays to A the amount:  $N(R_2(T_{i-1}, T_i) + s\delta_i)$ .

where s is the constant rate such that the initial value of the swap at time  $T_0$  equals zero.

The equity-for-equity swap is also referred to as a two-way equity swap. The simplest contract of this type is a domestic equity-for-equity swap where both returns are based on domestic indices or assets.

So far, we have only considered domestic equity indices and assets. However, all of the three equity swaps mentioned above have versions where one or both cash flows are based on a foreign equity return or interest rate. They are so called *cross-currency swaps*.

To illustrate a cross-currency equity swap, suppose that the United States is the domestic market. Let the notional principal be expressed in US dollars. Let  $Z_1$ be a foreign equity index such as, for instance, the NIKKEI, while  $Z_2$  is a domestic equity index such as the S&P 500. The period return  $R_1$  is based on a foreign equity index, while the nominal amount is in domestic units. There is a currency mismatch in the cash flow that  $A$  pays (but none in the cash flow that  $B$  pays). This type of contract is referred to as a *quanto* swap (see also **Quanto Options**). Quanto swaps are more complicated to price than other swaps. Quanto contracts have been considered in  $[3, 4]$  and  $[7]$ .

From a pricing and hedging perspective, the simplest cross-currency swaps are the ones that are currency adjusted. Consider a cross-currency equityfor-equity swap with currency-adjusted returns. Let  $Z_1$  be a foreign equity, while  $Z_2$  is a domestic equity. Let  $X(t)$  denote the exchange rate expressed as the number of domestic currency units per foreign currency unit. Then the currency-adjusted period return over the interval  $[T_i, T_{i+1}]$  for the asset  $Z_1$  is

$$R_1(T_i, T_{i+1}) = \frac{X(T_{i+1})Z_1(T_{i+1})}{X(T_i)Z_1(T_i)} - 1 \qquad (2)$$

While the unit of  $Z_1(t)$  is foreign currency, the unit of  $Z_1(t)X(t)$  is domestic currency. Regarding the underlying index as the foreign asset times the exchange rate,  $R_1$  can be treated as the return on a domestic index. A cross-currency equity-for-equity swap that is currency adjusted is, from a valuation point of view, equal to a domestic equity-for-equity swap.

#### Contracts with Variable Notional Principal

Some equity swaps are constructed with a variable notional principal. A variable notional principal changes over time according to changes in the referenced equity index.

Consider an equity-for-fixed-rate swap. It can essentially be regarded as a leveraged position in the underlying equity. If the notional principal is constant, the realized returns from the equity index are withdrawn in each period, resulting in a position that is rebalanced periodically. If the notional principal is variable, the realized returns in each period are reinvested.

Let  $N_i$  denote the variable notional principal, which determines the size of the payments at time  $T_i$  for  $i = 1, 2, ..., M$ . Let  $N_1 = 1$  and  $N_i =$  $Z(T_{i-1})/Z(T_0)$  for  $i = 2, 3, ..., M$ . Thus, for instance, at the third payment date  $T_3$ 

- *A* pays to *B* the amount:  $\frac{Z(T_2)}{Z(T_0)}R(T_2, T_3)$ .<br>*B* pays to *A* the amount:  $\frac{Z(T_2)}{Z(T_0)}\delta_3 K$ .

Equity swaps with variable notional principals are treated in [2, 6] and [9].

## *More Equity Swaps & Strategies*

There can be many variations of the equity swaps listed so far. For instance, there can be more than one tenor structure, that is, the payments made by *A* and *B* can have different periodicity. It is also possible to make forward agreements to enter into a swap contract in the future. Such contracts are known as *forward swaps* or *deferred swaps*. There are also equity swaps with option features like *capped equity swaps* and *barrier equity swaps*. Further examples are *blended index swaps* and *outperformance swaps* (see [2, 6] and [8]).

We conclude by providing an example of how equity swaps were used in the United States during the 1990s to circumvent taxes. The executive equity swap strategies were developed for large single stock shareholders, for instance, a founder of a company. The swap was constructed so that the shareholder made payments based on the return of the stock to the swap contractor. In exchange, the shareholder received either a fixed interest rate or the return of a large equity index such as S&P 500. By entering into such a contract, the stockholder could keep the stocks and the voting rights, but still reduce the risk of the total portfolio and avoid capital gains taxes. As a result, the tax regulation was changed. The new regulation states that taxpayers should recognize that transactions that are essentially equivalent to a sale should be treated as such and thus be taxed. For a more detailed description on this topic, see [1] and [8].

# **End Notes**

a*.* For instance, if the convention "Actual/365" is used, *δ*<sup>1</sup> is equal to the number of days between the dates *T*<sup>0</sup> and *T*1, divided by 365.

b*.* Sometimes called *face value*.

# **References**

- [1] Bolster, P., Chance, D. & Rich, D. (1996). Executive equity swaps and corporate insider holdings, *Financial Managment* **25**(2), 14–24.
- [2] Chance, D. & Rich, D. (1998). The pricing of equity swaps and swaptions, *The Journal of Derivatives* **5**, 19–31.
- [3] Chung, S. & Yang, H. (2005). Pricing quanto equity swaps in a stochastic interest rate economy, *Applied Mathematical Finance* **12**(2), 121–146.
- [4] Hinnerich, M. (2007). *Derivatives Pricing and Term Structure Modeling*. PhD Thesis, Stockholm School of Economics, EFI, The Economic Research Institute, Stockholm.
- [5] Jarrow, R. & Turnbull, S. (1996). *Derivative Securities*, South-Western Publishing, Cincinnati.
- [6] Kijima, M. & Muromachi, Y. (2001). Pricing equity swaps in a stochastic interest rate economy, *The Journal of Derivatives* **8**, 19–35.
- [7] Liao, M. & Wang, M. (2003). Pricing models of equity swaps, *The Journal of Futures Markets* **23**(8), 121–146, 751–772.
- [8] Marshall, J. & Yuyuenyonwatana, R. (2000). Equity swaps: structures, uses, and pricing, In *Handbook of Equity Derivatives*, Jack C. Francis, William W. Toy, & J.G. Whittaker, eds, Wiley, New York.
- [9] Wu, T. & Chen, S. (2007). Equity swaps in a libor market model, *The Journal of Futures Markets* **27**(9), 893–920.

# **Further Reading**

Chance, D. (2004). Equity swaps and equity investing, *The Journal of Alternative Investing* **7**, 75–97.

# **Related Articles**

**Equity Default Swaps**; **Forwards and Futures**; **LIBOR Rate**; **Quanto Options**; **Total Return Swap**.

MIA HINNERICH
# **Currency Forward Contracts**

# **Executive Summary**

Structured forwards use combinations of options to replicate forwards like payout profiles. The main use of structured forwards is for corporate and institutional clients trying to hedge their foreign exchange exposures. While standard forwards lock in a fixed exchange rate, structured forwards give the user the advantage of the possibility of an improved exchange rate, while still guaranteeing a worstcase rate. As standard forwards, structured forwards usually have no upfront premium requirements (zerocost strategies). Having the chance of an improved exchange rate for no upfront premium suggests that structured forwards must have a guaranteed worstcase exchange rate that is worse than the prevailing forward rate. This is the risk involved when entering into structured forward transactions.

# **Forward Contract**

A foreign exchange forward transaction involves two parties, who enter into a contract, whereby one counterparty agrees to sell a specified amount of a currency A in exchange for a specified amount of another currency B on a specified date. The other counterparty agrees to buy the specified amount of that currency A in exchange of the other currency B.

#### *The Characteristics of Forward Contracts*

Both counterparties have the obligation to fulfill the contract (as opposed to an option transaction where only one of the parties has the obligation, the option seller, while the other counterparty, the option buyer, has the right, but no obligation). As both currency amounts are fixed on the day the contract is entered into, the exchange rate between the two currencies is fixed. Hence, the parties to the contract know from the beginning at what exchange rate they are obliged to buy or sell the specified currency.

For corporate and institutional clients, this can be a useful information, as they can use this exchange rate to calculate the cost of production of a given product or service. Another positive feature of forwards is that there is no upfront premium to be paid by either party. As both parties to the contract have an obligation to deliver and the contract is struck at the prevailing market forward rate, the transaction is by definition a zero-cost strategy. This is because the definition of the market forward rate is a future exchange rate of two currencies at a rate that demands no upfront payment from either party.

How can one calculate this market forward rate and what are the influencing factors?

#### *Calculating the Market Forward Rate*

The following example helps to determine the forward exchange rate of a given currency pair.

#### **Market Information.**

- Company X: London-based manufacturer exporting to the United States.
- The importing company: New York-based company importing from the United Kingdom.
- The bank: it is the other counterparty to the forward transaction.
- Company X sells its goods to the importing company. The sale is agreed in USD, and the payment of USD 100 000 is expected six months after the contract is signed. Therefore, the London-based company X has a foreign exchange exposure, as the change in the foreign exchange rate has an effect on its income in GBP.
- Current GBP/USD exchange rate: 2.0000. This means that 1 GBP is worth 2 USD.
- Current GBP interest rate: 6% per annum. This is the interest rate company X can borrow and lend in GBP.
- Current USD interest rate: 3% per annum. This is the interest rate company X can borrow and lend in USD.

What can company X do to eliminate its foreign exchange exposure? We know that company X will receive USD 100 000 in six months time. In fact they could already sell this USD 100 000 at the prevailing market rate (spot rate), but they don't have it yet. The solution is to go to the bank and borrow the USD 100 000. To be precise, they need to borrow less than USD 100 000, because they need to pay interest on the loan to the bank. So the exact amount to borrow is the net present value (NPV) of USD 100 000. To calculate this, we use the following formula:

$$NPV = \frac{N}{1 + r^* d/dc} \tag{1}$$

where

- *N* is the amount for which one wants to calculate the NPV. In this example, it is USD 100 000.
- *r* is the interest rate, expressed as percentage per annum, for the currency in which *N* is denominated.
- *d* is the duration of the deposit or loan in days. In this example, it is 180 days (i.e., six months).
- *dc* is the day-count fraction. This is usually 360, except for GBP deposits or loans where it is 365.

We are now able to calculate the amount company X has to borrow: USD 100 000/*(*1 + 0*.*03 × 180*/*360*)* = USD 98,522.17. If they borrow this money, they have to pay back exactly USD 100 000 in six months time including the interest charge. This is the amount company X is due to receive in six months time from the sales of its goods to the importing company.

If company X now sells the borrowed USD in the spot market and buys GBP, they receive GBP 49 261.08. This is calculated by dividing the borrowed USD amount by the current GBP/USD exchange rate (2.0000 in this example).

Company X now has the GBP and has eliminated the foreign exchange exposure. They can take GBP and deposit it with their bank at the current interest rate (6% in this example). The amount they get back after six months is equal to GBP 50 718.67—this is calculated as follows: GBP 49 261*.*08 × *(*1 + 0*.*06 × 180*/*365*)*.

After these series of transactions company X is left with no cash position at the beginning of the transaction. They receive GBP 50 718.67 after six months and have to pay USD 100 000 in exchange. The exchange rate that is implied from the abovementioned two amounts is 1.9717 (calculated as USD 100 000 divided by GBP 50 718.67).

What happens when a forward transaction is entered into? Exactly the same:

- At the beginning of the transaction:
  - company X has no cash position;
  - company X agrees to sell USD 100 000 for GBP at the market forward rate.

- At the end of the transaction:
  - company X pays USD 100 000 for the GBP amount exchanged at the agreed forward rate.

Because the two approaches described earlier have the same outcome, the GBP amount received for the USD 100 000 has to be the same; otherwise there would be an arbitrage opportunity. Therefore, the market forward rate in this example has to be 1.9717.

Generally, the forward rate can be calculated with a single and easy formula:

$$F_{\text{GBP/USD}} = S_{\text{GBP/USD}^*} \frac{1 + r_{\text{USD}^*} d/dc_{\text{USD}}}{1 + r_{\text{GBP}^*} d/dc_{\text{GBP}}}$$
(2)

where *F*GBP*/*USD, forward rate for GBP/USD; *S*GBP*/*USD, spot exchange rate for GBP/USD; *r*USD, USD interest rate expressed in percentage per annum; *r*GBP, GBP interest rate expressed in percentage per annum; *d*, duration of the deposit or loan in days; *dc*USD, day-count fraction for USD (360); and *dc*GBP, day-count fraction for GBP (365).

As the formula suggests, the market forward rate is a function of only the current (spot) exchange rate and the interest rates of the two currencies for the specified forward period. Hence, it is not market expectations, or any other factor that determines the arbitrage-free forward rate.

## **Structured Forwards**

The previous section helped us to understand how a foreign exchange exposure resulting from a crossborder transaction can be eliminated and hedged through a forward transaction. It showed that the forward exchange rate was fixed right at the beginning of the contract and hence the uncertainty about exchange rate movements was turned into a known rate with which companies can calculate their cost of production. The example also demonstrated that there is no cash flow at the beginning of a forward transaction and there is no premium or any other fee associated with it. A forward transaction is by definition a zero-cost strategy.

### *The Difference between Forwards and Structured Forwards*

The disadvantage of forwards is that favorable exchange rate moves are also eliminated when the exchange rate is fixed. In the previous example, the forward rate was calculated to be 1.9717. This is the rate at which company X has to buy GBP and sell the USD. If in six months time the GBP/USD exchange rate falls below 1.9717, company X would be better off without hedging the GBP purchase through a forward.

Structured forwards allow just this. They are more flexible, because favorable exchange rate moves, and, in fact, any market view can be incorporated into the transaction to enhance the rate at which a currency is exchanged for another.

As with forwards, structured forwards offer the worst-case exchange rate. This rate is fixed at the beginning of the contract and similar to a regular forward, it offers the benefit of certainty about the exchange rate that can be used for financial planning.

Similar to standard forward contracts, most structured forward contracts are zero-cost strategies, that is, no upfront premium is required.

We all know that there is no such a thing as a "free lunch". Therefore, to have the benefit of an improved exchange rate, a fixed worst-case rate, and a zerocost strategy, the company entering into a structured forward transaction needs to take on certain risks. This risk is usually structured so that the guaranteed worst-case exchange rate is set at a rate that is worse than the prevailing market forward rate. The hedging counterparty accepts this worse guaranteed rate for the chance of receiving a better rate, in case a predefined condition is met. As the examples in the following section demonstrate, these predefined conditions can take many forms and may incorporate the market view of the counterparty entering into the structured forward transaction.

#### *Examples of Structured Forwards*

As mentioned in the previous section, structured forwards offer the possibility to incorporate one's market view into a forward transaction. This view might be the appreciation or depreciation of a currency or even the view that a currency pair remains in a certain range over a given period of time. The following examples demonstrate how these different market views can be expressed with currency options that can be structured into the forward transaction. As a reminder: all examples follow the basic assumptions that the structured forward has a worst-case buying (or selling) rate and no upfront premium must enter into the transaction.

**Forward Plus.** The forward plus is the simplest of all structured forwards. It offers the possibility to take advantage of favorable market movements up to a certain point, while still having a certain worst-case hedged rate.

How does it work: by accepting a worst-case hedge rate that is less favorable than the prevailing market forward rate, we create excess cash. Remember, trading at the market forward rate is zero cost by definition. If one trades on a rate that is worse than the market rate, one can expect some compensation. The cash generated is used to buy an option that pays out, if the underlying currency pair moves favorably. To make this a zero-cost strategy, we need to introduce a barrier, or knockout. This has the effect that options cease to exist (are knocked out) if the barrier is reached. For our strategy, it means that we can participate in a favorable market move, but only up to a certain point, namely, the predefined barrier level. If the barrier is reached we are locked into a forward transaction with a rate equal to the worst-case rate.

Let us continue the previous example with company X: We calculated the market forward rate to purchase GBP against USD in six months time to be 1.9717. A forward plus could have a worst-case buying rate of 1.9850. This rate is 0.0133 worse than the market forward rate. As compensation for accepting this hedge rate, company X has the opportunity to buy GBP at the prevailing spot rate in six months time as long as the barrier of 1.8875 is not reached or breached during the life of the contract. As the barrier is observed continuously during the entire life of the transaction, we call this barrier an American style barrier (this is not to be confused with an American style option that is exercisable during the life of the option). So what does this right to buy the GBP at the prevailing market spot rate in six months time give to company X? Imagine that the barrier was never reached and the spot rate in six months time is at 1.9000. In this case, company X may buy the GBP at 1.9000 and it will outperform the forward transaction that would have forced it to buy the GBP at 1.9717. However, if the spot rate ever trades at or below the barrier of 1.8875, company X has to buy the GBP at the worst-case rate of 1.9850.

Table 1 and Figure 1 demonstrate possible scenarios with assumed spot rates after six months.

## **4 Currency Forward Contracts**

|                              | Forward plus buying rate |                 |                     |
|------------------------------|--------------------------|-----------------|---------------------|
| Spot rate in six months time | Barrier never reached    | Barrier reached | Market forward rate |
| 2.0200                       | 1.9850                   | 1.9850          | 1.9717              |
| 2.0100                       | 1.9850                   | 1.9850          | 1.9717              |
| 2.0000                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.9900                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.9850                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.9750                       | 1.9750                   | 1.9850          | 1.9717              |
| 1.9700                       | 1.9700                   | 1.9850          | 1.9717              |
| 1.9650                       | 1.9650                   | 1.9850          | 1.9717              |
| 1.9600                       | 1.9600                   | 1.9850          | 1.9717              |
| 1.9550                       | 1.9550                   | 1.9850          | 1.9717              |
| 1.9500                       | 1.9500                   | 1.9850          | 1.9717              |
| 1.9450                       | 1.9450                   | 1.9850          | 1.9717              |
| 1.9400                       | 1.9400                   | 1.9850          | 1.9717              |
| 1.9350                       | 1.9350                   | 1.9850          | 1.9717              |
| 1.9300                       | 1.9300                   | 1.9850          | 1.9717              |
| 1.9250                       | 1.9250                   | 1.9850          | 1.9717              |
| 1.9200                       | 1.9200                   | 1.9850          | 1.9717              |
| 1.9150                       | 1.9150                   | 1.9850          | 1.9717              |
| 1.9100                       | 1.9100                   | 1.9850          | 1.9717              |
| 1.9050                       | 1.9050                   | 1.9850          | 1.9717              |
| 1.9000                       | 1.9000                   | 1.9850          | 1.9717              |
| 1.8950                       | 1.8950                   | 1.9850          | 1.9717              |
| 1.8876                       | 1.8876                   | 1.9850          | 1.9717              |
| 1.8875                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.8800                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.8750                       | 1.9850                   | 1.9850          | 1.9717              |
| 1.8700                       | 1.9850                   | 1.9850          | 1.9717              |

| Table 1 |  |  | Forward plus scenario analysis |  |
|---------|--|--|--------------------------------|--|
|---------|--|--|--------------------------------|--|

![](_page_3_Figure_3.jpeg)

Forward plus (barrier not reached), forward plus (barrier reached), market forward rate

**Figure 1** Forward plus scenario analysis

As Figure 1 demonstrates, the forward plus outperforms the market forward rate, if the barrier is never reached and the GBP/USD spot rate at maturity is below 1.9717.

If we set the worst-case scenario even higher than 1.9850, we can set the barrier further down. Taking advantage of this flexibility, each company entering into a forward plus can create a product that suits its risk appetite.

**Range Forward.** The following example uses another market view to try to outperform the forward rate. In this case, we expect the underlying currency pair to trade within a predefined range during the life of the contract.

Like with the forward plus (and with nearly all other structured forwards), the worst-case hedge rate is less favorable than the prevailing market forward rate. The generated excess cash is spent on an option that pays out if the range holds. The payout of the option is then used to improve the worst-case rate.

Here is an example: we calculated the market forward rate to purchase GBP against USD in six months time to be 1.9717. A range forward could have a worst-case buying rate of 1.9850. This rate is 0.0133 worse than the market forward rate. In compensation for accepting this hedge rate, company X can buy GBP at 1.8850 (0.0867 better than the forward rate), if the GBP/USD exchange rate remains within the 2.0700–1.9400 range during the entire sixmonth period. If at any time during the life of the contract, the underlying currency pair trades outside the range, company X has to buy the GBP at the worst-case rate of 1.9850.

Table 2 and Figure 2 demonstrate possible scenarios with assumed spot rates after six months.

As Figure 2 demonstrates, the range forward outperforms the market forward rate, if the range holds, even if spot rate closes above the forward rate.

**Table 2** Range forward scenario analysis

| Spot rate in six months time | Range forward buying rate |                 |                     |
|------------------------------|---------------------------|-----------------|---------------------|
|                              | Barriers never reached    | Barrier reached | Market forward rate |
| 2.1000                       | 1.9850                    | 1.9850          | 1.9717              |
| 2.0700                       | 1.9850                    | 1.9850          | 1.9717              |
| 2.0699                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0500                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0300                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0250                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0200                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0150                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0100                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0050                       | 1.8850                    | 1.9850          | 1.9717              |
| 2.0000                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9950                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9900                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9850                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9800                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9750                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9700                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9650                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9600                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9550                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9500                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9450                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9401                       | 1.8850                    | 1.9850          | 1.9717              |
| 1.9400                       | 1.9850                    | 1.9850          | 1.9717              |
| 1.9300                       | 1.9850                    | 1.9850          | 1.9717              |
| 1.9250                       | 1.9850                    | 1.9850          | 1.9717              |
| 1.9200                       | 1.9850                    | 1.9850          | 1.9717              |

![](_page_5_Figure_1.jpeg)

Range forward (barrier not reached), range forward (barrier reached), market forward rate

**Figure 2** Range forward scenario analysis

If we set the worst-case scenario even higher than 1.9850, we can widen the range or improve the best-case buying rate. Taking advantage of this flexibility, each company entering into a range forward can create a product that suits its risk appetite.

## **References**

- [1] Wystup, U. (2006). *FX Options and Structured Products*, John Wiley & Sons.
- [2] Weithers, T. (2006). *A Practical Guide to the FX Markets*, John Wiley & Sons.
- [3] Villanueva, O.M. (2007). Spot-forward cointegration, structural breaks and FX market unbiasedness *Journal of International Financial Markets Institutions & Money* **17**, 58–78.

[4] Chisholm, A.M. (2004). *Derivatives Demystified: A Stepby-Step Guide to Forwards, Futures, Swaps and Options*, John Wiley & Sons.

## **Related Articles**

#### **Barrier Options**; **Forwards and Futures**; **Pricing Formulae for Foreign Exchange Options**.

TAMAS´ KORCHMAROS ´
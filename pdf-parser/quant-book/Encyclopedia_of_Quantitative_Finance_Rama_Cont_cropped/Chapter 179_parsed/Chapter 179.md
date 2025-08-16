# **Loan Valuation**

A loan is an agreement in which one party, called a *lender*, provides the use of property, the *principal*, to another party, the *borrower*. The borrower customarily promises to return the principal after a specified period along with payment for its use, called *interest* [3]. When the property loaned is cash, the documentation of the agreement between borrower and lender is called a *promissory note*.

Although cash loans can take many forms, traditionally, banks and other financial institutions are the primary lenders of cash and businesses, organizations, and individuals are the borrowers. Most loans to corporations share a common set of structural characteristics [2, 5].

- 1. Interest on loans is typically paid quarterly at a rate specified relative to some reference rate such as LIBOR (i.e., L + 250 bp).a Thus, loans have *floating-rate* coupons whose absolute values are not known with certainty except over the next quarter.
- 2. Often the firm's assets or receivables are pledged against the borrowed principal. Because of this, their recovery rates are generally higher than corporate bonds, which are most commonly unsecured.
- 3. Most loans are prepayable on any coupon date at par, although some agreements contain a prepayment penalty or have a noncall period. The loan prepayment feature ensures that loan prices rarely exceed several points above par.
- 4. Finally, unlike bonds which are public securities, loans are private credit agreements. Thus, access to firm fundamentals and loan terms may be limited and loan contracts are less standardized. It is not uncommon to find "nonstandard" covenants or other structural features catering to specific needs of borrowers or investors.

Loan valuation concerns the amount of interest that a lender requires for use of the property or an investor will charge for purchasing the loan agreement. That valuation depends on several factors, such as

- 1. the likelihood of failure to receive timely payments of principal, called *risk of default*;
- 2. the residual value of the loan in the event of default, called its *recovery value;*

- 3. the time by which the principal of the loan must be repaid, the *maturity*;
- 4. the current market rate of interest for the obligor's likelihood of default, called the *market credit spread*;
- 5. the likelihood of the event that a borrower will have repaid the principal at any particular date prior to maturity.

Although the bulk of the loans outstanding are rated investment-grade or better, these loans trade very infrequently because of their high credit quality and lack of price differentiation. In fact, most loans that trade after origination are those made by banks to borrowers having speculative-grade credit ratings. These loans, made to high-yield firms are typically referred to as *leveraged loans*, though the exact definition varies slightly among market participants.b

The types of loan facilities commonly traded in secondary markets include the following:

- 1. **Amortizing term loans**. Usually called "term loan A", the periodic payments from these loans include partial payment of principal, similar to what a mortgage loan does. These loans are usually held by banks and are becoming less popular.
- 2. **Institutional term loans**. These loans are structured to have bullet or close-to-bullet payment schedules and are targeted for institutional investors. They are referred to as "*term loan B*", "*term loan C*" and so on. Institutional term loans constitute the bulk of leveraged loan market.
- 3. **Revolving credit lines**. These are unfunded or partially funded commitments by lenders that can be drawn at the discretion of the borrowers. The facility is analogous to a corporate credit card. It can be drawn and repaid multiple times during the term of the commitment. These commitments are traded in secondary market. They are also known as *revolvers*.
- 4. **Second-lien term loans**. They have cash-flow schedule similar to that of institutional term loans, except that their claims on borrowers' assets are behind first-lien loan holders in the event of default.
- 5. **Covenant-lite loans**. These are borrowerfriendly versions of institutional term loans that have fewer than the typical stringent covenants

that restrict use of the principal or subsequent borrowing activities of the firm.

### **Loan Pricing**

Like bonds, loans contain risk of default; an obligor may fail to make timely payments of interest and/or principal. Thus, the notion of a credit spread to LIBOR has been used to characterize the riskiness of loans, where the credit spread,  $s$ , to LIBOR is calculated as

$$V = \sum_{t=1}^{4n} \frac{c_t/4}{\left(1 + \frac{r_t + s}{4}\right)^t} + \frac{F}{\left(1 + \frac{r_{4n} + s}{4}\right)^{4n}} \quad (1)$$

where  $V$  is the market value of the loan,  $c_t$  is the coupon (LIBOR + contractual spread),  $r_t$  is the spot rate for maturity  $t$  LIBOR rates, and  $F$  is the face value of the loan to be repaid at maturity. Loan coupons are generally paid quarterly and then reset relative to LIBOR and this is reflected in equation 1. Using equation 1, we can calculate a credit spread for any loan whose market price is known.

One problem with equation 1 for loan valuation is that it fails to account for the fact that loans, unlike bonds, are typically prepayable at par on any given coupon date. The loan prepayment option creates uncertainty in the expected pattern of cash flows and complicates comparisons of value among loans based on their credit spreads. Pricing the prepayment option has proved difficult because of its dependence on the evolution of an obligor's credit state and the changing market costs of borrowing. For example, if a firm's credit improves or the loan rate over LIBOR decreases, the likelihood of prepayment increases; the borrower can refinance at a lower rate. Conversely, if a borrower's credit deteriorates or lending rates increase, it will not be advantages for the borrower to refinance.

To account for the prepayment option, we price the loans using a credit-state-dependent backward induction method.<sup>c</sup> To illustrate, consider pricing a term loan with face value  $F$ , intermediate floatingrate coupon payments of  $c_t$ , and a maturity at time  $T$ , to a borrower of known credit quality,  $J$ . Specifically, Figure 1 displays pricing lattices for a five-year loan to a double-B rated (i.e.,  $J = BB$ ) obligor having a coupon of LIBOR  $+ 3\%,^d$  and face value of 100 at maturity.<sup>e</sup> Figure 1(a) shows how the obligor's credit state evolves over time. In the lattice, probabilities are assigned reflecting transitions from each node at time  $t$  to all nodes at  $t + 1$ . Thus, the probability of being at a given node will be conditional upon all the previous transitions. In practice, ratings transition probabilities are based on historical data from credit rating agencies,<sup>f</sup> and these are typically modified by the current market price of risk to produce risk-neutral ratings transition matrices.g,h

Having calculated transition probabilities between all future nodes, we then apply the backward induction method. At maturity  $T$ , the borrower pays the principal plus coupon,  $F + c_T$ , or the recovery

![](_page_1_Figure_10.jpeg)

Figure 1 Credit-dependent backward induction method. (a) Double-B rated obligor, whose credit transitions are derived from historical data and incorporate market risk premiums are used to specify the likelihood of being in any credit state at future times to maturity. (b) Calculation of node values using backward induction, whereby values at each non-defaulted node are the coupon value at that node plus the sum of the conditional cash flows from the later date, discounted one period at forward LIBOR. In the example in (b), we assume a refinancing penalty of  $0.5\%$  of the principal

value in default  $R \ast F$ . Those cash flows are discounted back to each node at the previous period using forward LIBOR at  $T-1$ . In other words, for each node at time  $i < T$  and credit state  $j$ , and  $j = (AAA, AA, \dots, CCC)$  we calculate an induced value,  $v_{i,j}$ , as

$$v_{(i,j)} = \min\left\{ \left( \frac{1}{\left( 1 + \frac{f_{i+1,i}}{4} \right)} \sum_{k=D}^{AAA} (P_{j,k,i} * v_{i+1,k}) \right) + c_i, K_i \right\}, \tag{2}$$

where  $P_{i,k,i}$  is the probability of migrating from state j to state k from time i to  $i + 1$ ,  $f_i$  is the forward LIBOR rate from time i to  $i + 1$ ,  $K_i$  is the terminal value of the loan at time *i*,<sup>i</sup> and  $v_{T,i} = F + c_T$ . Thus, at each node  $i, j$  we compute the induced value, compare it with the terminal value,  $K_i$ , and set the value at that node,  $v_{i,j}$  to the lesser of the two. In other words, if the induced value exceeds the terminal value, the loan is effectively repaid and terminates at  $i, i$ . Also, if the loan defaults at time  $i$ , the loan terminates with a value  $v_{i,D} = R * F$  for all i. Finally, the value of  $v_{i,j}$  at time 0 (in this example, at  $v_{0,BB}$ ) is the *model* price of the loan.

Although equation 2 is useful for calculating prices of illiquid loans and for estimating the coupon premiums to charge for new loans, it is less useful for evaluating relative value among existing loans, which are better assessed using credit spreads. In fact, we can calculate the credit spread for a loan by discounting its expected nondefault cash flows by a constant amount over the LIBOR curve such that the discounted value matches its current market price. For all nondefault cash flows at a given time, the borrower will either prepay the principal and terminate, or pay a coupon and continue. The prepayment region in the time-and-credit-state lattice can be determined using the values of  $v_{i,j}$  in equation 2. The probability of prepaying at period  $i$  is the sum of the probabilities of reaching nodes whose value of  $v_{i,j}$  equal those capped at the terminal values  $K_i$ . Given the probability transition matrix and the set  $\omega$  of all prepayment nodes, we can calculate the probability of prepayment at time  $i$  conditional on no prepayment before time  $i$ .

Let the conditional probability of prepayment at time be  $q_i$ ,<sup>j</sup> then the discounted cash flow is given by

$$V_{J} = \sum_{i=1}^{T} D_{i} * \prod_{j=1}^{i-1} (1 - q_{j}) * [(q_{i} * K_{i}) + ((1 - q_{i}) * CF_{i})]$$
(3)

where  $CF_i = c_i/4$  for  $i < T$ ;  $CF_i = (c_i/4 + F)$  for  $i = T$ , and the discount margin  $D_i$  is given by

$$D_{i} = \prod_{j=0}^{i} \frac{1}{\left(1 + \frac{f_{j,j-1} + \hat{s}}{4}\right)} \tag{4}$$

The credit spread,  $s$ , is determined by iteratively changing the parameter  $\hat{s}$  and recalculating the discounted value of the cash flows,  $V_J$ , until  $V_J$  converges to  $P$ , the market price.

Revolving lines of credit are priced by assuming that the fraction of the loan drawn at a particular time, called the *usage*, is directly related changes to the obligor's credit quality. In other words, if a borrower's credit rating improves, it can access credit more cheaply and is also less likely to draw on existing lines of credit. Conversely, a borrower with deteriorating credit will likely draw on the credit lines it obtained when more highly rated. In this framework, usage can be interpreted as credit-dependent face value. Thus, in the equations above the face value is modified by  $F \rightarrow U_i * F$ where j is the credit state and usage  $U_i$  ranges from  $0$  to  $1$ .

### **End Notes**

<sup>a.</sup>LIBOR stands for London interbank offered rate, which roughly corresponds to the interest rate charged between banks when lending large amounts of US dollars outside the United States. The coupon rate for a given quarter is set at the beginning of the period. For example, the  $L + 250$  bp coupon in the text indicates that the borrower will pay onequarter of 250 bp  $(0.625\%)$  plus the current three-month LIBOR rate on the next coupon date.

<sup>b.</sup> Although some people define leveraged loans on the basis of their balance sheet leverage ratio, it is more common to use credit ratings (i.e., below BBB-) or credit spread to LIBOR above some maximum.

<sup>c</sup>. Several versions of the backward induction method have been proposed over the years  $[1, 6, 7, 9]$ . The version presented in equations  $(1-3)$  embodies elements that are common to most of these methodologies.

d. Loan spreads are typically quoted in basis points such as LIBOR  $+ 300$  bp, where  $1\% = 100$  bp.

<sup>e</sup>. For convenience, we assume LIBOR is constant at 2%, thereby generating a constant 5% coupon, and that the loan pays annually, rather than the typical quarterly coupon

payment.  $\mathrm{^{f}.The\ most\ well\-known\ credit\ rating\ agencies\ are\ Fitch,}$ Moody's, and Standard & Poor's.

<sup>g</sup>. Ratings transition matrices are published regularly by the major agencies [4, 8].

Most models specify adjustment of physical credit transitions so that the default probabilities at each time,  $i$ , match the risk-neutral probabilities of default as implied by the bond and loan markets. For example, the riskneutral default probability for a single risky cash flow at time *t* is given as  $P_t^Q = \frac{1 - e^{-ts}}{(1 - R)}$  and  $P_t^Q = N(N^{-1}(P_t) +$ 

 $\beta\lambda\sqrt{t}$ ) where,  $P(t, Q)$  is the cumulative risk-neutral default

probability to time  $t$ ,  $s$  is the market credit spread, and  $R$  is the recovery rate in default. On the right, we calculate  $P_t^Q$  from  $P_t$  the physical default probability by adding a term related to the volatility of the credit relative to the market, the market price of risk, and the time to receipt of the cash flow. (For an elaboration and discussion of the derivation of this relation, see Bohn [1]. Zeng and Wen [9] describe its application to loan pricing.)

<sup>i</sup>.It is common to add a refinancing premium to the principal plus coupon when defining the terminal value for evaluating prepayment as there are costs and/or penalties associated with the refinancing process.

<sup>j</sup>. The probability of prepayment at time 1 from the initial state  $J$  is given by  $q_1 = \sum_{k \in \omega} P_{J,k,0}$ . For time  $i > 1$ , we must add the condition that the loan was not prepaid before time *i*; thus,  $q_i = \prod_{m=1}^{i-1} (1-q_m) * \sum_{k \in \omega, l \notin \omega} P_{l,k,i-1}$ .

## References

- Bohn, J. (2000). A Survey of Contingent-Claims Appro- $[1]$ aches to Risky Debt Valuation, Institutional Investor.
- Deitrick, W. (2006). Leveraged Loan Handbook, Citi [2] Markets and Banking.
- [3] Downs, J. & Goodman, J.E. (1991). Dictionary of Finance and Investment Terms, Barron's, Hauppauge, New York.
- Emery, K., Ou, S., Tennant, J., Kim, F. & Cantor, R. [4] (2008). Corporate Default and Recovery Rates, Moody's Global Corporate Finance. 1920-2007, Special Comment.
- Miller, S. & William, C. (2007). A Guide to the Loan [5] Market, Standard & Poor's.
- Rizk, H. (1993). GMPM Valuation Methodology: An [6] Overview, Citi Markets and Banking.
- [7] Rosen, D. Does Structure Matter? (2002) Advanced Methods for Pricing and Managing the Risk of Loan Portfolios, Algorithmics Inc.
- [8] Vazza, D., Aurora, D., Kraemer, N., Kesh, S., Torres, J. & Erturk, E. (2007). Annual 2006 Global Corporate Default Study and Rating Transition, Standard and Poor's Global fixed Income Research.
- Zeng, B. & Wen, K. (2006). CreditMark Valuation [9] Methodology, Moody's K.M.V.

# **Further Reading**

Aguais, S., Forest, L. & Rosen, D. (2000). Building a Credit Risk Valuation Framework for Loan Instruments, Algo Research Quarterly.

#### TERRY BENZSCHAWEL, JULIO DAGRACA & HENRY FOK
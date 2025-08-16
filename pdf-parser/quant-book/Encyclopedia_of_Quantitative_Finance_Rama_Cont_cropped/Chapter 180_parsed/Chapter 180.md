# **Credit Risk**

Credit risk is the risk of an economic loss from the failure of a counterparty<sup>a</sup> to fulfill its contractual obligations. For example, credit risk in the loan portfolio of a bank materializes when a borrower fails to make a payment, either the periodic interest charge or the periodic reimbursement of principal on the loan he contracted with the bank. Credit risk can be further decomposed into four main types: default risk, bankruptcy risk, deterioration in creditworthiness (or downgrading) risk, and settlement risk.

Default risk corresponds to the debtor's incapacity or refusal to meet his/her debt obligations, whether interest or principal payments on the loan contracted, by more than a reasonable relief period from the due date, which is usually 60 days in the banking industry.

Bankruptcy risk is the risk of actually taking over the collateralized, or escrowed, assets of a defaulted borrower or counterparty, and liquidating them.

Creditworthiness risk is the risk that the perceived creditworthiness of the borrower or counterparty might deteriorate. In general, deteriorated creditworthiness translates into a downgrade action by the rating agencies, such as Standard and Poor's (S&P) or Moody's, and an increase in the risk premium, or credit spread of the borrower. A major deterioration in the creditworthiness of a borrower might be the precursor of default.

Settlement risk is the risk due to the exchange of cash flows when a transaction is settled. Failure to perform on settlement can be caused by a counterparty defaulting, liquidity constraints, or operational issues. This risk is greatest when payments occur in different time zones, especially for foreign exchange transactions, such as currency swaps, where notional amounts are exchanged in different currencies.<sup>b</sup>

Credit risk is only an issue when the position is an asset, that is, when it exhibits a positive replacement value. In that situation, if the counterparty defaults, the firm loses either all of the market value of the position or, more commonly, the part of the value that it cannot recover following the credit event. The value it is likely to recover is called the *recovery value* or *recovery rate* when expressed as a percentage; the amount it is expected to lose is called the *loss given default* (*see* **Recovery Rate**).

Unlike the potential loss given default on coupon bonds or loans, the one on derivative positions is usually much lower than the nominal amount of the deal, and in many cases is only a fraction of this amount. This is because the economic value of a derivative instrument is related to its replacement, or market value, rather than its nominal or face value. However, the credit exposures induced by the replacement values of derivative instruments are dynamic: they can be negative at one point in time and yet become positive at a later point in time after market conditions have been changed. Therefore, firms must examine not only the current exposure, measured by the current replacement value, but also the profile of potential future exposures up to the termination of the deal.

## **Credit Risk at the Portfolio Level**

The first factor affecting the amount of credit risk in a portfolio is clearly the credit standing of specific obligors (*see* **Rating Transition Matrices**; **Credit Rating**). The critical issue, then, is to charge the appropriate interest rate, or spread, to each borrower so that the lender is compensated for the risk he/she undertakes and to set the right amount of risk capital aside (*see* **Economic Capital**).

The second factor is "concentration risk" or the extent to which the obligors are diversified in terms of number, geography, and industry.

This leads us to the third important factor that affects the risk of the portfolio: the state of the economy. During economic boom, the frequency of default falls sharply compared with the periods of recession. Conversely, the default rate rises again as the economy enters a downturn. Downturns in the credit cycle often uncover the hidden tendency of customers to default together, with banks being affected to the degree that they have allowed their portfolios to become concentrated in various ways (e.g., customer, region, and industry concentrations) [1].

Credit portfolio models are an attempt to discover the degree of correlation/concentration risk in a bank portfolio (*see* **Portfolio Credit Risk: Statistical Methods**).

The quality of the portfolio can also be affected by the maturities of the loans, as longer loans are generally considered more risky than short-term loans. Banks that build portfolios that are not concentrated in particular maturities—"time diversification"—can reduce this kind of portfolio maturity risk. This also helps reduce liquidity risk or the risk that the bank will run into difficulties when it tries to refinance large amounts of its assets at the same time.

## **Credit Derivatives and the ISDA Definition of a Credit Event**

With the spectacular growth of the market for credit default swaps (CDSs) (*see* **Credit Default Swaps**), it has become necessary to be specific about what is a credit event? A credit event, usually a default, triggers the payment on a CDS. This event, then, should be clearly defined to avoid any litigation when the contract is settled. CDSs normally contain a "materiality clause" requiring that the change in credit status be validated by third-party evidence.

The new CDS market has struggled to define the kind of credit event that should trigger a payout under a credit derivatives contract. Major credit events as stipulated in CDS documentations and as formalized by the International Swaps and Derivatives Association (ISDA) are the following.

- Bankruptcy, insolvency, or payment default.
- Obligation/cross default that means the occurrence of a default (other than failure to make a payment) on any other similar obligation.
- Obligation acceleration which refers to the situation where debt becomes due and repayable prior to maturity. This event is subject to a materiality threshold of \$10 million unless otherwise stated.
- Stipulated fall in the price of the underlying asset.
- Downgrade in the rating of the issuer of the underlying asset.
- Restructuring: this is probably the most controversial credit event.
- Repudiation/moratorium: this can occur in two situations. First, the reference entity (the obligor of the underlying bond or loan issue) refuses to honor its obligations. Second, a company could be prevented from making a payment because of a sovereign debt moratorium (City of Moscow in 1998).

One of the most controversial aspects of the debate is whether the restructuring of a loan—which can include changes such as an agreed reduction in interest and principal, postponement of payments, or change in the currencies of payment—should count as a credit event. The Conseco case famously highlighted the problems that restructuring can cause. In October 2000, a group of banks led by Bank of America and Chase granted to Conseco a threemonth extension of the maturity of approximately \$2.8 billion of short-term loans, while simultaneously increasing the coupon and enhancing the covenant protection. The extension of credit might have helped to prevent an immediate bankruptcy, but as a significant credit event it also triggered potential payouts on as much as \$2 billion of CDS.

The original sellers of the CDS were not happy and were annoyed further when the CDS buyers seemed to play the "cheapest to deliver" game by delivering long-dated bonds instead of the restructured loans; at the time, these bonds were trading significantly lower than the restructured bank loans. (The restructured loans traded at a higher price in the secondary market due to the new credit-mitigation features.)

In May 2001, following this episode, ISDA issued a restructuring supplement to its 1999 definitions concerning credit derivative contractual terminology. Among other things, this document requires that to qualify as a credit event, a restructuring event must occur to an obligation that has at least three holders, and that at least two-thirds of the holders must agree to the restructuring. The ISDA document also imposes a maturity limitation on deliverables—the protection buyer can only deliver securities with a maturity of less than 30 months following the restructuring date or the extended maturity of the restructured loan—and it requires that the delivered security be fully transferable. Some key players in the market have now dropped restructuring from their list of credit events.

## **End Notes**

a*.* In the following, we use indifferently the term *borrower* or *counterparty* for a debtor. In practice, we refer to issuer risk, or borrower risk, when credit risk involves a funded transaction such as a bond or a bank loan. In derivatives markets, counterparty risk is the credit risk of a counterparty for an unfunded derivatives transaction such as a swap or an option.

b*.* Settlement failures due to operational problems result only in payment delays and have only minor economic consequences. In some cases, however, the loss can be quite substantial and amount to the full amount of the payment due. A famous example of settlement risk is the 1974 failure of Herstatt Bank, a small regional German bank. The day it went bankrupt, Herstatt had received payments in Deutsche Mark from a number of counterparties but defaulted before payments were made in US dollars on the other legs of maturing spot and forward transactions.

Bilateral netting is one of the mechanisms that reduce settlement risk. In a netting agreement, only the net balance outstanding in each currency is paid instead of making payments on the gross amounts to each other. Currently, 55% of the foreign exchange (FX) transactions are settled through the CLS Bank that provides a payment-*versus*-payment (PVP) service that virtually eliminates the principal risk associated with settling FX trades [2].

## **References**

- [1] Basel Committee on Payment and Settlement Systems (2008). *Progress in Reducing Foreign Exchange Settlement Risk* , Bank for Internal Settlements, Basel, Switzerland, May 2008.
- [2] Caouette, J., Altman, E., Narayanan P. & Nimmo, R. (2008). *Managing Credit Risk: The Great Challenge for Global Financial Markets*, Wiley.

MICHEL CROUHY
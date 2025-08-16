# **ABS Indices**

Asset back securities (ABS) are financial debt securities based on a pool of underlying assets or collateral assets. When the assets are backed by mortgages, they are called *mortgage backed securities* (MBS). ABSs are backed by nonmortgage assets. This includes auto loans, credit card receivables, home equity loans, student loans, and so on. Owing to government guarantees, MBS typically entail no credit risk. However, ABSs generally lack such guarantees, so they entail credit risk. It might be for this reason that ABS backed by subprime mortgages are still called *ABS*, or more explicitly, *subprime residential mortgagebacked security* (*RMBS*) instead of MBS.

The basic building blocks of credit derivatives are credit default swaps (CDS). It was the standardization of the settlement terms and conditions of the corporate CDS contracts by International Swaps and Derivatives Association (ISDA) in early 1990s that allowed the corporate CDS market to grow and evolve quickly. The credit risk in subprime RMBS differs in fundamental ways from credit risk in corporate bonds. ISDA published its first pay-as-yougo (PAUG) CDS documentation for RMBS in June 2005, and followed up with amended versions in April 2006 and November 2006. This ISDA documentation standardization for PAUG CDS on subprime RMBS helped create a synthetic CDS market on the subprime RMBS bonds. In late 2005, 15 security firms, representing major brokers and dealers, along with an index company CDS Index Co. and a data provider, Mark-It Partner came up with the ABS CDS benchmark index, ABX.HE, for subprime RMBS, and the trading of ABX started on January 19, 2006. The index is supposed to roll every six months with newly issued subprime RMBS bonds as collateral assets. Owing to the subprime crisis and a lack of newly issued subprime RMBS bonds, we have only four series of ABX indices up to now; they are simply called *ABX* 2006-1, *ABX* 2006-2, *ABX* 2007-1, and *ABX* 2007-2 based on the vintage year of underlying subprime RMBS bonds.

Tranched ABX or TABX is the benchmark index tranche product based on ABX. Owing to the relatively small number of collateral ABS bonds of each vintage ABX index, we use the underlying ABS bonds of two conjacent ABX indices as collateral assets for the TABX. Shortly after the introduction of TABX, the subprime crisis emerged. In practice, TABX has never been liquidly traded. However, there are a large number of issuances of bespoke ABS collateralized debt obligations (CDOs) with non-ABX bonds as collateral assets.

We simply present the contract parts of the ABX and TABX and briefly discuss the modeling of TABX.

## **ABX**

ABX.HE indices are CDS benchmark index for a standard basket of subprime home equity ABS bonds. For each vintage ABX.HE, we have five indices based upon the rating of reference ABS bonds: AAA, AA, A, BBB and BBB− by both Moody's and S&P. The selection of the included bonds is rule-based according to the deal size (at least 500 millions) of the subprime home equity ABS shelf program with a limit from the same loan originator (four deals) and from the same master servicer (to six deals), and the weighted average life (4–6 years from the issuance for other ratings except AAA, and more than 5 years for AAA). Each vintage ABX.HE has 20 underlying collateral bonds, and a new series of index is supposed to be issued every six months.

As stated early, ABX is a CDS spread index whose premium leg or fixed leg is based on two parts: up-front payment in terms of percentage and a running payment in terms of a spread in basis point. This running spread is called a *fixed rate*, which is determined at the beginning so that the initial quote for the index is 100 or we do not need to pay any up-front premium if you buy protection or short the index. The following shows the market quote for ABX on November 28, 2009. Owing to the subprime crisis, most of the current "price" is very low. This implies that we need to pay a very high up-front payment to buy protection. For example, if we want to buy default protection on 2006-01 BBB−, we need to pay *(*100 − 5 16*/*32*)*% = 94*.*5% up-front premium based on the notional amount and 267 bps (basis points) running spread per annum, but paid monthly, on the basis of the outstanding notional amount. The outstanding notional amount declines over time on the basis of the reference obligations amortization.

The loss leg includes interest shortfall, writedown, principal shortfall adjusted by interest rate shortfall reimbursement, principal shortfall reimbursement, and write-down reimbursement. The protection buyer receives any interest shortfall, but the total amount is capped at a fixed rate. A credit event is defined as principal shortfall and write-down according to the 2005 ISDA PAUG template definition.

For example, if any one of the 20 referenced ABS bonds incurs a write-down of 1% in the amount of its current principal balance, and the referenced bond current factor is 70%, then the protection buyer of 100 millions receives the following payment:

Notional amount × current factor × weighting

$$\times$$
 loss rate = 100 millions  $\times$  0.7  $\times$  0.05  
 $\times$  0.1 = 35 000 (1)

After this credit event, the notional amount based on which that fixed rate is paid would be reduced by \$35 000 until the earlier of the next credit event or scheduled termination. ABX has been actively traded since its inception on a daily basis. Table 1 provides a market quote for ABX on Nov 28, 2008.

## **TABX**

TABX was introduced in February 2007 just before the subprime crisis emerged. TABX tranches reference a portfolio of 40 names from underlying bonds from 06-2 and 07-1 ABX.HE series and 07-1 and 07-2 ABX.HE series of a similar rating. Only two tranche baskets were traded initially: BBB and BBB−. The attachment and detachment points for the 06-2 and 07-1 portfolio and the fixed running spreads for all tranches are given in Table 2.

The tranche protection buyer receives protection against the write-downs and principal shortfalls on the reference ABS bonds. No interest shortfalls are

**Table 1** Market quote for ABX, November 28, 2008

covered by the tranche protection. On the fixed side, all tranches have a specified or fixed running spreads in bps as given in Table 1, and are traded on price up front. Fixed running spreads are capped on roll date at 500 bps. The subordination level is the initial subordination notional amount less write-downs, principal shortfalls, and amortization. Therefore, the detachment and attachment points of the tranche can change over each period depending on the loss evolution and amortization. We could think of TABX, or, broadly speaking, of ABS CDOs as CDOs with changing subordination levels.

## **Modeling of ABX and TABX**

The TABX market was a short-lived one. It was introduced in February 2007. Shortly after its introduction, we observed the first crash of the ABX indices. But there were billions of dollars of ABS CDOs structured and issued by Wall Street firms without ABX index bonds as collateral assets. There is no market consensus with respect to the ABS CDO valuation. Some practitioners tried to adapt the Gaussian copula model for ABS CDOs, which were hard to interpret since the results depended critically on the prepayment assumptions for the underlying subprime loans.

Figure 1 shows the whole securities involved in the TABX or ABS CDOs. The first layer of collateral assets for ABS bonds consists of individual mortgage loans underlying the ABS bonds. Each ABS bond takes about 5000–10 000 individual mortgage loans as collateral assets. Then ABX takes 20 ABS bonds as its underlying assets. The TABX takes 40 ABS bonds as collateral assets and goes through another tranche. The TABX is thus more like a CDO squared transaction. In the market, there is no consensus with

| Series | Fixing rate | Rating | Quote       | Series | Fixed rate | Rating | Quote       |
|--------|-------------|--------|-------------|--------|------------|--------|-------------|
| 07-2   | 76          | AAA    | 33-24/36-24 | 06-2   | 11         | AAA    | 46-00/49-00 |
| 07-2   | 192         | AA     | 6.00/8.00   | 06-2   | 17         | AA     | 11-00/14-00 |
| 07-2   | 369         | A      | 4.00/7.00   | 06-2   | 44         | A      | 5-00/8-00   |
| 07-2   | 500         | BBB    | 3.00/5.00   | 06-2   | 133        | BBB    | 2-16/4-16   |
| 07-2   | 500         | BBB−   | 3.00/5.00   | 06-2   | 242        | BBB−   | 2-16/4-16   |
| 07-1   | 9           | AAA    | 33-24/36-24 | 06-1   | 18         | AAA    | 75-00/78-00 |
| 07-1   | 15          | AA     | 4-16/6-16   | 06-1   | 32         | AA     | 30-00/33-00 |
| 07-1   | 64          | A      | 3.00/6-4-16 | 06-1   | 54         | A      | 11-00/14-00 |
| 07-1   | 224         | BBB    | 2-16/4-00   | 06-1   | 154        | BBB    | 4-24/6-24   |
| 07-1   | 389         | BBB−   | 2-16/4-00   | 06-1   | 267        | BBB−   | 4-16/6-16   |

| Index pool    | ABX rating | Attachment (%) | Detachment (%) | Fixed rate |
|---------------|------------|----------------|----------------|------------|
| 06-2 and 07-1 | BBB        | 0              | 3              | 500        |
| 06-2 and 07-1 | BBB        | 3              | 7              | 500        |
| 06-2 and 07-1 | BBB        | 7              | 12             | 500        |
| 06-2 and 07-1 | BBB        | 12             | 20             | 467        |
| 06-2 and 07-1 | BBB        | 20             | 35             | 200        |
| 06-2 and 07-1 | BBB        | 35             | 100            | 51         |
| 06-2 and 07-1 | BBB−       | 0              | 5              | 500        |
| 06-2 and 07-1 | BBB−       | 5              | 10             | 500        |
| 06-2 and 07-1 | BBB−       | 10             | 15             | 500        |
| 06-2 and 07-1 | BBB−       | 15             | 25             | 500        |
| 06-2 and 07-1 | BBB−       | 25             | 40             | 267        |
| 06-2 and 07-1 | BBB−       | 40             | 100            | 72         |

**Table 2** Attachment and detachment point for TABX tranches (06-2 and 07-1 portfolio) and running spreads

![](_page_2_Figure_3.jpeg)

**Figure 1** An overview of subprime RMBS products

respect to the CDO squared transaction even though attempts have been made to tackle this problem. One example is the approach in [1] in which the authors use a mixed Gaussian copula function along with the mapping of loss distributions. But this is only for corporate credits that have one risk or "decrement". For subprime loans, each loan is subject to two decrements: default and prepayment.

We believe the only approach to capture all features and complexities of the TABX or ABS CDOs is a bottom-up approach. In this approach, we model the fundamental driving factors for the mortgage loan pool: prepayment and default. We then generate the cash flows for the ABS bonds using the waterfall structure for each collateral ABS bond (like a cash-flow CDO tranche). This can be accomplished by running Intex. These cash flows include the write-downs, principal, interest rate, and coupon cap shortfalls. We can then aggregate the cash flows for the whole underlying pool of the TABX. The TABX tranche can then be assessed by the aggregate cash flows for the collateral pool. The dynamics and correlation have been introduced since there are common driving factors for prepayment and default, such as the home price appreciation (HPA) index. All other features are incorporated since we use the waterfall structure for each ABS bond. Calibration of the model to the observed ABX prices can be achieved if we use a few parameters for the prepayment and default curves.

## **Reference**

[1] Li, D.X. & Liang, M.H. (2005). *CDO Squared Pricing Using Gaussian Mixture Model with Transformation of Loss Distribution* at http://ssrn.com/abstract=890766.

## **Related Articles**

**CDO Square**; **Credit Default Swap (CDS) Indices**; **Securitization**.

DAVID X. LI
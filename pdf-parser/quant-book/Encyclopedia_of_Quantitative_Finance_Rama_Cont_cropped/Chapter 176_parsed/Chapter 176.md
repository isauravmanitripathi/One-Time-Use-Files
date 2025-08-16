# **Exposure to Default and Loss Given Default**

In the study of credit risk, the most relevant factor has traditionally been the borrower's probability of default (or intensity of default), expressing default risk and, indirectly, migration risk. However, there are other risk profiles that significantly affect the loss experienced by the lender upon the occurrence of a default: exposure at default and loss given default. The uncertainty surrounding these variables gives rise, respectively, to exposure risk and recovery risk. These risks (captured through parameters like EAD, LGD, and RR, as explained below) have become increasingly popular thanks to the preliminary drafts of the new accord on bank capital requirements ("Basel II") that were circulated by the Basel Committee after 1999 and led to a new regulatory text in 2004 [12].

## **Exposure at Default and Exposure Risk**

In the simplest forms of credit exposure, the amount due to the lender in the event of a default (that is, the exposure at default (EAD)) is known with certainty. This is the case, for example, of zero-coupon bonds or fixed-term loans, where the balance outstanding is predetermined in advance and cannot be modified without a formal credit restructuring.

However, the amount outstanding in the event of a default might also be uncertain, basically due to the following reasons:

- 1. changes in the value of the contract to which the defaulted party had committed itself (typically, an OTC derivative affected by a number of underlying variables);
- 2. the presence of a revolving credit line (e.g., a loan commitment) where the borrower could increase his/her credit usage before default.

While case 1, known as *counterparty risk*, can be considered as a sort of intersection between credit and market risk, case 2 represents a typical example of exposure risk. Here, the borrower's current exposure (that is, the drawn part of the credit line, DP) can increase to a larger EAD, with the increase *(E)* potentially as large as the current unused portion (UP) of the credit line. To account for exposure risk, banks compute credit conversion factors (CCF) as *CCF* ≡ *E/UP*. <sup>a</sup> Once a set of CCFs, associated with different types of borrowers and exposures, has been estimated, a bank can forecast EAD as

$$EAD = DP + CCF \cdot UP \tag{1}$$

CCFs are usually calibrated through a statistical analysis of past defaults (see, e.g., [9, 11, 25, 27]), where the CCF is explained through the characteristics of the borrower, the exposure, and the economic environment. When past events are analyzed, the UPs must be recorded some time before the default: this can be a fixed interval ("fixed time horizon," e.g., 12 months before the default) or a fixed moment in time for all defaults that occurred in the same period ("cohort approach," e.g., January 1 for all exposures defaulted in a given year); multiple UPs can also be recorded at several different instants in time ("variable time horizon," e.g., 6, 12, 24 months before default) to assess the impact of time-to-default on exposure risk.b

In fact, CCFs can be expected to increase with time-to-default: a study based on some 400 borrowers in the period 1995–2000 [9] has shown that one-year CCFs average 32%, while five-year CCFs average 72%; this may be due to a rating migration effect and a greater opportunity to draw down. CCFs also seem to be driven by the percent usage ratio of the credit line (*DP/(DP* + *UP)*): lower usage rates are usually associated with higher CCFs and with better ratings [9].

A well-known relationship also exists between ratings and CCFs: indeed, the latter have often been found to increase for borrowers with better ratings.c In other words, exposure risk is especially significant when default risk is comparatively low. This is an expected result, given that firms with investmentgrade ratings can get funds from the commercial paper market or by negotiating better terms with their suppliers, and hence tend to use a small portion of the available credit lines (which are comparatively more expensive); however, as their financial shape deteriorates and default gets closer, firms quickly resort to bank credit lines, as other sources of funds dry up.

Besides focusing on loan behavior at default, one can assess exposure risk by monitoring credit usage throughout the life of a facility, including both defaulted and performing exposures. These "usage ratios" have been found to behave very differently for firms that eventually default, even several years later, as opposed to nondefaulting obligors. For example, a sample of about 770 000 lines of committed credit lines recorded in the Spanish central credit register<sup>d</sup> shows that defaulting exposures have a median usage ratio of 50%, in contrast to 43% for nondefaulting facilities; this median usage ratio was found to increase (71%) in the last year before default. Usage ratios are instead lower, all other things being equal, for "seasoned" credit lines (i.e., credit lines that have been in place for a number of years); this suggests that relationship banking may play a role in preventing usage peaks in credit lines.

Other borrower characteristics may also help explain exposure risk: for example, usage ratios have been found to be higher for younger, smaller, and less profitable firms (as age, size, and profitability tend to be inversely related to PD, this is consistent with poorly rated companies being more dependent on bank credit lines).e Other important explanatory variables are the borrower's leverage, liquidity, and debt cushion; also, exposure risk tends to be higher for larger companies and for those having a larger share of bank debt in their liabilities mix [25]. However, generally, firm characteristics tend to have a comparatively limited impact on CCFs and usage statistics.

Exposure risk also seems to be affected by the macroeconomic cycle. For example, the gross domestic product (GDP) growth rate has been found [27] to be inversely related to credit line usage, and such a link is especially meaningful in the case of a slowdown or recession. This makes sense, as credit lines are often used to provide a liquidity buffer for borrowers in times of financial strain.

Other measures have been proposed as an alternative to CCFs: these are the *EAD factor*, *EADF* = *EAD/(DP* + *UP)*, and the *exposure multiplier*, *EM* = *EAD/DP*. The former can be considered as a special case of the usage ratio, recorded at the time of default; the latter cannot be computed when a credit line was totally undrawn before the borrower's default<sup>f</sup> .

CCFs can usually be expected to lie between 0 (if the UP is still unused at default) and 1 (if the whole UP gives rise to an extra exposure). However, the *E* and hence the CCF could also be negative; this is likely to be the case if the credit line is revocable or has some covenant entitling the bank to claim its money back before a proper default takes place. Curiously, however, Basel II states that CCFs cannot be set below zero, regardless of any empirical evidence that a bank may produce to its supervisors.

Apart from OTC derivatives and credit lines, exposure risk can also arise from the issuance of guarantees and other off-balance-sheet items (e.g., letters of credit, bid bonds, and performance bonds) that might be used by third parties to get relief after the default of the guaranteed entity (leading to monetary outflow for the guarantor, that is, to an EAD). In this case, the EAD can be anywhere between zero and the amount of the off-balance sheet item (OBS), and CCFs can be computed as *CCF* ≡ *EAD/OBS* . CCF estimates associated with different types of guarantees and OBS can then be used to forecast the EAD as *EAD* = *CCF* · *OBS*

## **Loss Given Default and Recovery Risk**

The loss rate given default—or simply loss given default (LGDg)—is the loss rate experienced by a lender on a credit exposure if the borrower defaults. It is given by 1 minus the recovery rate (*RR*) (see equation (3)) and can take any value between 0 and 100%. Formally,

$$LGD = 1 - RR \tag{2}$$

LGD is never known when a new loan is issued, although a reasonable estimate can be produced when the default occurs, at least if there is a secondary market where the defaulted exposure can be traded. In fact, RRs can be computed based on several approaches [8,33]:

1. The *market LGD* approach uses prices of defaulted exposures as an estimate of the RR. In practice, if a defaulted bond trades at 30 cents a euro, one can infer that the market is estimating a 30% RR (hence, a 70% LGD). This approach can be used only for exposures traded on a secondary market.

A variation of this approach (*emergence LGD* approach) estimates the RR on the basis of the market value of the new financial instruments (usually, shares or long-term bonds) that are offered to lenders in exchange for their defaulted claims. These are usually issued only when the restructuring process is over and the company A third version of market LGD involves the use of spreads on performing bonds as a source of information; in fact, spreads on corporate bonds depend on both the borrower's PD and the expected RR. Assuming the PD can be estimated otherwise, one can then work out the *LGD* implied by market spreads (*implicit market LGD*); alternatively, by assuming that some relationship exists between PD and LGD (see below), PD and LGD can be derived jointly [13]. Note that implicit market LGD makes it possible to use a considerably larger dataset, including performing exposures, and not only defaulted ones. However, note that LGDs derived from market prices often are risk-neutral quantities; therefore, some assumption on the relationship between them and real world LGDs is needed if implicit market LGDs are to be used.

2. When market data are not available (as for most traditional banking loans, where no secondary market exists) one must turn to the *workout approach*. This is based on the actual recoveries (and recovery costs) experienced by the lender in the months (years) after the default took place. It therefore requires to set up a database, where all recoveries on defaulted exposures are filed. According to this approach, the RR (also known as *ultimate recovery*) can be computed using the following equation:

$$RR = \frac{\sum_{i} R_i \cdot (1+r)^{-T_i}}{EAD} \tag{3}$$

where *Ri* is the *i*th recovery flow associated with the defaulted exposure (negative *R*is denote recovery costs), *r* is the appropriate discount rate,h and *Ti* is the time elapsed between the default and the *i*th recovery. Note that, based on equation (3), *RR* can be negative (hence *LGD* can exceed 100%) if recoveries do not offset recovery costs.

The determinants of RRs have been extensively investigated, mainly based on the market LGD approach, although some examples of workout LGDs exist (mainly for bank loans). Indeed, one of the first studies estimating RRs in the 1970s [6] was based on a survey carried out among the workout departments of a number of large banks in the period 1971–1975; the average recovery on unsecured loans (based on the face value of cash flows on defaulted exposures, recorded in the first three years after default and not discounted) was found to be about 30%.

In the following years, recoveries on bank loans have been found<sup>i</sup> to be affected by many factors, including the size of the loan and different collateral types. More generally, the four main drivers of RRs and LGDs can be summarized as follows:

#### **Exposure characteristics**

These include the presence of any collateral (be it represented by financial assets of other goods, such as plants, real estate, inventories) and its degree of effectiveness (that is, how easily it can be seized and liquidated); the priority level of the exposure, which can be senior or subordinated to other exposures; any guarantees provided by third parties (like banks, holding companies of public sector entities). An important driver of recoveries is also the exposure's "debt cushion", that is, the amount of the liabilities in the borrower's balance sheet that are junior to the one being evaluated; as the volume of such junior securities increases, so does the RR on the senior exposure, as its holders are more likely to find an adequate volume of assets to be liquidated and used as a source of cash [28,34].

#### **Borrower characteristics**

These include the industry where the company operates, which may affect the liquidation process, that is, the ease with which the firm's assets can be sold and turned into cash for the creditors,j the country of the obligor, which affects the speed and effectiveness of the bankruptcy procedures; some financial ratios, like the leverage (namely, the ratio between total assets and liabilities, which shows how many euros of assets are reported in the balance sheet for each euro of debt to be paid back) and the ratio of EBITDA (earnings before interest, taxes, depreciation, and amortization) to total turnover (which indicates whether the defaulted company is still capable of generating an adequate level of cash flow for its would-be borrowers). Another interesting variable affecting LGD is the borrower's *original* rating: indeed, "fallen angels" (i.e., investment-class obligors that were downgraded to junk) appear to behave differently from straight speculative-grade issuers, and have been found to recover significantly more than bonds of the same seniority that were rated as speculative-grade at issuance.<sup>k</sup>

#### **Lender (e.g., bank) characteristics**

These may include the efficiency levels of the department that takes care of the recovery process (workout department) or the frequency with which out-ofcourt settlements are reached with the borrowers, or nonperforming loans are spun-off and sold to third parties; in fact, sales of nonperforming loans and outof-court settlements, while reducing the face value of the recovery (compared to what could be obtained by the bank on the basis of a formal bankruptcy procedure), also significantly shorten the duration of the recovery process. The financial effect of this shorter recovery time usually more than offsets the lower recovered amount.

#### **Macroeconomic variables**

These mainly include the level of the interest rates (higher rates reduce the present value of recoveries) and the state of the economic cycle (if the economy is in recession, the value at which the companies assets can be liquidated is likely to be lower).

During the last years, an important stream of research has addressed the relationship between PD and LGD. From a theoretical point of view, the same macroeconomic background variables that affect the default probability of the borrowers (and cause default rates to rise) may drive down the liquidation value of assets and increase LGD (so that the distribution of LGDs is different in high-default and low-default periods).l This intuition has prompted a number of models<sup>m</sup> generalizing the "classic" singlefactor model in [17] and [22] to the case where recoveries and defaults are driven by a common component (usually systemic in nature).

From an empirical point of view, several pieces of evidence indicate that LGDs and default rates tend to increase together when the overall economic cycle deteriorates. For example, using data on US corporate bonds (Moody's Default Risk Service database) for 1982–1997, one finds that in a severe economic downturn (when defaults are more frequent), recoveries can be expected to drop by 20–25% compared with their unconditional average [20]. Similar results are found using Standard and Poor's Credit Pro database (bond and loan defaults) for 1982–1999 [15], as well as junk bond data for 1982–2000.n Evidence of a strong relationship between LGD and the state of the economy, including default frequencies, is also found by Moody's KMV in its LossCalc model [23], estimated on a dataset of over 3000 recoveries on loans, bonds, and preferred stock.

The correlation between economic cycle and recoveries appears stronger if estimated at the industry level [1]. In fact, if the sector where the borrower used to operate is undergoing a recession, the lender will find it more difficult to find a buyer for the defaulted company or its assets (as competitors are likely to suffer from excess production capacity) and recoveries will be lower than expected. As recessions may occur at the industry level when the economy as a whole is doing reasonably well, moving from economy-wide to industry-specific conditions can make the empirical link between default rates and recoveries much easier to detect.

The PD/LGD correlation has wide-ranging implications for credit risk models. First, the expected loss rate can no longer be considered as the product of the expected LGD times the borrower's unconditional PD, since a second, positive addendum must be factored in, accounting for covariance. Second, unexpected loss and Value at Risk prove to be considerably higher than they are if independence is assumed, as shown by [7]; in other words, if systematic risk plays an important role for RRs, estimates of economic capital turn out to be downward biased.o

While most RR studies focus on mean or median values, it is also important to understand the whole probability distribution of recoveries, if extreme scenarios are to be fully understood and managed. In the case of bank loans, the probability distribution of workout LGDs is usually strongly bimodal, with peaks at 0% and 100%. In the case of bonds, unimodal distributions may be sensible, but still it is strongly advisable to use flexible distributions, such as the beta (which can be either uni- or bimodal depending on the estimated parameters, and can easily be fit to the data by the generalized method of moments).p

Finally, it is worth emphasizing that, as with all other risks, recovery risk may also produce profits. Indeed, the price performance of defaulted bonds (estimated by comparing market LGDs to emergence LGDs) can prove extremely brilliant, although this is not always the case: while senior bonds (both secured and unsecured) have been found to perform very well in the postdefault period (with per annum returns of 20–30%), junior bonds often show negative returns [3].

## **Acknowledgments**

Part of this article, especially the LGD section, draws on previous work carried out with Andrea Sironi, to whom I wish to express my gratitude.

## **End Notes**

a*.* CCFs are sometimes also known as *loan equivalents* (*LEQ*s).

b*.* See [30] for further details on fixed time horizon, cohort approach, and variable time horizon.

c*.* See, for example, [11], where a sample of loan commitments in 1987–93 is analyzed, [25], based on 3281 defaulted exposures issued by 720 borrowers in 1985–2006, or [9].

d*.* These are all loan commitments above ¤6000 issued by Spanish banks after 1984. See [27] for further details.

e*.* See again [27], based on a subset of about 86 000 companies.

f*.* The EM is sometimes referred to as the *CCF* (in which case, what we called CCF is indicated as *LEQ*. Note that, given the important role played by bank capital regulation in shaping credit risk measurement techniques and jargon, we chose to use the word CCF in a way that is consistent with the terminology of the new Basel accord.

g*.* In principle, one should indicate the loss rate given default as LGDR (LGD rate) and use LGD for the absolute LGD (in euros or dollars). However, "LGD" is used by most practitioners (and by the new Basel accord on bank capital) to indicate the loss rate, while the absolute loss is usually indicated as *LGD* · *EAD*.

h*.* The choice of a suitable risk-adjusted *r* is far from trivial, and basically depends on the amount of systemic risk of the defaulted exposure. See [29].

i*.* See, for example, [10], based on 24 years of data compiled by Citibank, or [14], using a sample of 371 loans issued by Portugal's largest private bank during 1985–2000; both studies are based on the workout approach. A study on bank loans (large syndicated loans traded on the secondary market) based on the market LGD approach is, for example, [16].

j*.* See [1] based on market LGDs observed during the United States during 1982–1999. See also [5] and the literature survey in [33].

k*.* See [4], based on a sample of corporate bonds stratified by original rating and seniority: in the case of senior-secured exposures, for example, the median RR for fallen angels was 50.5% versus 33.5%.

l*.* A somewhat different approach has been proposed by Peura and Jovivuolle [31]. Using an option-pricing, *a la `* Merton framework, they present a model where collateral value is correlated with the value of the borrower's assets and hence to his/her PD. This leads to an *inverse* relationship between default rates and RRs.

m*.* See [19–21]. Jarrow [26] presents a model where, as in Frye's works, RRs and PDs are correlated and depend on the state of the economy; however, his methodology explicitly incorporates equity prices in the estimation procedure, allowing the separate identification of RRs and PDs and the use of a larger dataset. Furthermore, he explicitly incorporates a liquidity premium to account for the high variability in the spreads on US corporate debt. In [32] and [15] also models are proposed that account for the dependence of recoveries on systematic risk by extending Gordy's singlefactor model.

n*.* See [2]. Note, however, that this study finds that a single systematic risk factor—that is, the performance of the economy as a whole—is less predictive than theoretical models would suggest, while a key role is played by the supply of defaulted bonds.

o*.* See also the empirical results in [15].

p*.* For a more flexible approach, see [24] where a variation of the Gaussian kernel, known as *Beta kernel*, is used to fit the distribution of RRs of a sample of defaulted bonds from the period 1981–1999. See also [18], for an interesting utility-based approach to the estimation of the conditional probability distribution of RRs.

## **References**

- [1] Acharya, V., Bharath, S. & Srinivasan, A. (2007). Does industry-wide distress affect defaulted firms: evidence from creditor recoveries, *Journal of Financial Economics*, **85**, 787–821.
- [2] Altman, E.I., Brady, B., Resti, A. & Sironi, A. (2005). The link between default and recovery rates: theory, empirical evidence and implications, *Journal of Business* **78**(6), 2203–2228.
- [3] Altman, E.I. & Eberhart, A. (1994). Do seniority provisions protect bondholders' investments? *Journal of Portfolio Management* (Summer), 67–75.
- [4] Altman, E.I. & Fanjul, G. (2004). Defaults and returns in the high-yield bond market: the year 2003 in review and market outlook, in *Credit Risk—Models and Management*, D. Shimko, ed, RiskBooks, London.
- [5] Altman, E.I. & Kishore, V.M. (1996). Almost everything you wanted to know about recoveries on defaulted bonds, *Financial Analysts Journal* **52**(6), 57–64.
- [6] Altman, E.R.H. & Narayanan, P. (1977). ZETA analysis: a new model to identify bankruptcy risk of corporations, *Journal of Banking & Finance* **1**(1), 29–54.
- [7] Altman, E.I., Resti, A. & Sironi, A. (2005). *Recovery Risk—The Next Challenge in Credit Risk Management*, Risk Books, London.
- [8] Altman, E., Resti, A. & Sironi, A. (2005). The PD/LGD link: implications for credit risk modelling, in *Recovery*

*Risk—The Next Challenge in Credit Risk Management*, E. Altman, A. Resti & A. Sironi, eds, RiskBooks, London, pp. 253–266.

- [9] Araten, M. & Jacobs, M.J. (2001). Loan equivalents for revolving credit and advised lines, *The RMA Journal* **83**(8), 34–39.
- [10] Asarnow, E. & Edwards, D. (1995). Measuring loss on defaulted bank loans: a 24 year study, *Journal of Commercial Bank Lending* **77**(7), 11–23.
- [11] Asarnow, E. & Marker, J. (1995). Historical performance of the US corporate loan market: 1988–1993, *Journal of Commercial Bank Lending* (Spring), 13–32.
- [12] Basel Committee on Banking Supervision (2006). *International Convergence of Capital Measurement and Capital Standards—A Revised Framework—Comprehensive Version*, Bank for International Settlements, Basel.
- [13] Das, S.R. & Hanouna, P.E. (2007). *Implied Recovery*, Tratto da SSRN, http://ssrn.com/abstract=1028612.
- [14] Dermine, J. & Neto de Carvalho, C. (2005). How to measure recoveries and provisions on bank lending: methodology and empirical evidence, in *Recovery Risk— The Next Challenge in Credit Risk Management*, E. Altman, A. Resti & A. Sironi, eds, RiskBooks, London, pp. 101–120.
- [15] Duellmann, K. & Trapp, M. (2005). Systematic risk in recovery rates of US corporate credit exposures, in *Recovery Risk—The next Challenge in Credit Risk Management*, E. Altman, A. Resti & A. Sironi, eds, RiskBooks, London, pp. 235–252.
- [16] Emery, K. (2003). *Moody's Loan Default Database as of November 2003*, Moody's Investors Service, New York.
- [17] Finger, C. (2001). The one-factor creditmetrics model in the new Basel capital accord, *RiskMetrics Journal* **2**(1), 9–18.
- [18] Friedman, C. & Sandow, S. (2003). Ultimate recoveries, *Risk* August, 69–73.
- [19] Frye, J. (2000). Collateral damage, *Risk* (April), 91–94.
- [20] Frye, J. (2000). *Collateral Damage Detected*, Federal Reserve Bank of Chicago, Chicago.
- [21] Frye, J. (2000). Depressing recoveries, *Risk* (November), 108–111.
- [22] Gordy, M.B. (2003). A risk-factor model foundation for ratings-based bank capital rules, *Journal of Financial Intermediation* **12**, 199–232.
- [23] Gupton, G.M. & Stein, R.M. (2002). *LossCalc: Moody's Model for Predicting Loss Given Default (LGD)*, Moody's Investors Service, New York.
- [24] Hagmann, M., Renault, O. & Scaillet, O. (2005). Estimation of recovery rate densities: non-parametric and semi-parametric approaches versus industry practice, in *Recovery Risk: the Next Challenge in Credit Risk*

*Management*, E. Altman, A. Resti & A Sironi, eds, Risk Books, London.

- [25] Jacobs, M. (2007). *An Empirical Study of Exposure at Default*, mimeo Office of the Comptroller of the Currency, Washington, DC.
- [26] Jarrow, R. (2001). Default parameter estimation using market prices, *Financial Analysts Journal* **57**(5), 75–92.
- [27] Jimenez, G., Lopez, J.A. & Saurina, J. (2007). ´ *Empirical Analysis of Corporate Credit Lines*, San Francisco: working paper, 2007–14, Federal Reserve Bank of San Francisco, San Francisco.
- [28] Keisman, D. (2003). *Loss Stats*, Standard & Poor's, New York.
- [29] Maclachlan, I. (2005). Choosing the discount factor for estimating economic LGD, in *Recovery Risk—The Next Challenge in Credit Risk Management*, E. Altman, A. Resti & A. Sironi, eds, RiskBooks, London, pp. 285–306.
- [30] Moral, G. (2006). EAD estimates for facilities with explicit limits, in *The Basel II Risk Parameters: Estimation, Validation and Stress Testing*, E. Bernd & R. Robert, eds, Springer Verlag, Berlin.
- [31] Peura, S. & Jovivuolle, E. (2005). LGD in a structural model of default, in *Recovery Risk—The Next Challenge in Credit Risk Management*, E.I. Altman, A. Resti & A. Sironi, eds, RiskBooks, London, pp. 201–216.
- [32] Pykhtin, M. (2003). Unexpected recovery risk, *Risk* **16**(8), 74–78.
- [33] Schuermann, T. (2005). What do we know about Loss Given Default? in *Recovery Risk—The Next Challenge in Credit Risk Management*, A. Resti & E.I. Altman, eds, Risk Books, London.
- [34] Van de Castle, K. & Keisman, D. (1999). *Recovering Your Money: Insights Into Losses from Defaults*, Standard & Poor's, New York.

## **Further Reading**

Schleifer, A. & Vishny, R. (1992). Liquidation values and debt capacity: a market equilibrium approach, *Journal of Finance* **47**, 1343–1366.

## **Related Articles**

**Counterparty Credit Risk**; **Recovery Rate**; **Valueat-Risk**.

ANDREA RESTI
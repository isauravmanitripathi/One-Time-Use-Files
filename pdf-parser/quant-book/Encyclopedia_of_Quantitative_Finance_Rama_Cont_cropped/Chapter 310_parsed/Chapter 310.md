## **Risk-adjusted Return on Capital (RAROC)**

Maintaining credit worthiness is a cost of doing business for a bank. In a multibusiness bank, senior management faces the problem of allocating capital to the different businesses in order to maximize the market value of the bank to existing shareholders, subject to the constraint that it maintain its desired level of creditworthiness. The capital structure of the bank is set so that the bank's equity provides a buffer for the bank to maintain its desired level of creditworthiness. We refer to this buffer as the *economic capital* (*see* **Economic Capital**) of the bank. Traditional approaches to capital budgeting define the risk of a project in terms of a project's systematic risk with market factors. Such a measure does not address the concerns of senior management about how the project affects the overall risk of the bank. If a project increases the probability of default, to restore the bank's creditworthiness, the bank must increase its economic capital. The cost of the marginal increase in the economic capital should be allocated to the project and an adjusted net present value determined. The value additivity principle will not hold, as economic capital is not additive, as noted by Merton [8] (*see* **Convex Risk Measures**; **Expected Shortfall**).

In determining whether to add or eliminate a business from a bank's portfolio, a marginal approach is often advocated for determining the economic capital. The standard assumption is that the business is "small" in comparison with the existing portfolio. If this is not the case, the whole nature of the bank and its capital structure are affected, implying that the determination of the marginal effects is problematic. Merton and Perold [9] show that simply aggregating the marginal economic capital of individual businesses underestimates the total economic capital and the error can be substantial. Apart from these theoretical concerns, the actual determination of the marginal capital is fraught with many practical difficulties.

Each business within the bank contributes to the overall credit risk of the bank. The economic capital of the bank is less than the aggregate economic capital of the individual businesses on a stand-alone basis, owing to the fact that businesses are correlated.<sup>a</sup> We refer to the difference between the economic capital of the bank and the aggregate stand-alone value as the *portfolio effect*. This raises a number of challenging issues. The first is the measurement of economic capital. If economic capital is estimated on a standalone basis, does the bank own the portfolio effect or individual businesses? If businesses, how should economic capital be allocated? Given the allocation of capital to each business within the bank, how should it measure the performance of each business, recognizing that each business affects the overall creditworthiness of the bank and the cost of funding? What benchmark should be used to judge the performance of a business? How should the performance of a business be measured, if it does not fully utilize its allocated capital? These questions hint at some of the difficulties in measuring the performances of the businesses within the bank.

Practitioners have addressed the issue of an appropriate performance metric with the use of a riskadjusted rate of return on capital (RAROC).b A generic RAROC takes the form

$$RAROC = \frac{ER - EL - Costs}{EC} \tag{1}$$

where *ER* denotes the expected revenue, *EL* the expected losses, *Costs* the funding cost associated with the project, and *EC* the economic capital attributed to the project.c The economic capital is usually defined as the capital necessary to cushion against unexpected losses, operational, and market risks, and is often referred to as a *Value at Risk* (*see* **Value-at-Risk**; **Market Risk**). There are both practical and theoretical issues with the use of this type of metric. The first is the myopic nature of the measure. The second is the issue of how to measure economic capital for a business. The third is what benchmark to use to judge whether the risk-adjusted return is acceptable. The fourth is that economic capital is not a sufficient statistic for the measurement of risk. It is known from the work of Wilson [17], Froot and Stein [4], and Crouhy *et al.* [2] that economic capital does not incorporate the systematic risk of a business and serious errors can occur if projects are solely ranked on the basis of RAROC.d

Froot and Stein (FS) [4] assume that there are no agency issues—the management acts in the best interests of existing shareholders. In their three-period model, risk management arises endogenously from the need to avoid an adverse selection problem associated with costly external financing in the last period. They show that the expected excess rate of return for a new project depends on two terms. The first term depends on the covariance of the cash flow with the market portfolio and the second depends on the covariance of the project's cash flow with the nontradable cash flows of the bank multiplied by the price of nontradable risk. As FS observe, it is not clear how to estimate this term.

Banks are opaque to outsiders. Any outside assessment of the creditworthiness of a bank is out of date even when issued. Banks are translucent if not opaque to insiders, with information flows restricted across businesses inside the bank and even within businesses.e Perold [10] describes a singleperiod model that incorporates the deadweight costs generated by the opaqueness of banks. Stoughton and Zechner [14] examine the question of capital allocation among businesses of a bank, assuming information asymmetry between the different business managers and senior management in a singleperiod model. The investment in risky technologies is financed with debt. Equity is used to satisfy a Valueat-Risk constraint. They derive a type of RAROC performance metric for each business, the hurdle rate being driven by the cost of debt, the distribution associated with the information asymmetry, and the outside employment opportunities for managers. Implication and measurement issues are not addressed.

None of these papers attempt to address the myriad of practical issues facing banks. A start is made in [15]. Each business within the bank is assumed to have its own balance sheet. This necessitates making some assumptions about the capital structure of the business. The risky assets of the business are financed with debt. The bank lends the business an amount of debt and charges the business an interest rate reflecting the expected maturity of the project and the credit risk of the bank. The required economic capital depends on the nature of the risks associated with project over its expected duration, giving rise to a *term structure of required economic capital*. f This is taken as exogenous. The economic capital is assumed to be financed *via* equity. The business invests the economic capital in a short-term defaultfree asset. The costs associated with economic capital arise from taxation. The resulting hurdle rate depends on the systematic risk associated with the risky investment and a second factor due to the requirement to hold costly economic capital. The weights of the two factors can be estimated, implying that it is possible to establish a required benchmark for performance measurement. If the term structure of economic capital allocated to the business is done on a marginal basis, the required rate of return on the business depends on the variance of the return on the business, the variance of the return on the remaining part of the bank, and the covariance between the two returns. If done on a stand-alone basis, it depends on the variance of the return on the business.

## **End Notes**

a*.* Many different methods, from bottom–up to top–down, have been advocated for the allocation of capital. See [6, 16, Chapter 6] for brief descriptions.

b*.* Matten [5, Chapter 7], describes many different types of performance metrics used by practitioners, as well as references to the history of RAROC. In a recent survey of chief risk officers of financial firms—see [11]—nearly 90% stated that they used risk-adjusted performance measures, with RAROC being the dominant measure.

c*.* See [1, Chapter 14; 12, Chapter 7] for a detailed description of how to apply RAROC.

d*.* See [3] for a discussion on the pitfalls of RAROC.

e*.* The issue of opaqueness in financial institutions is discussed in [13, 7].

f*.* A simple example would be a foreign currency swap. Principal is exchanged in this type of swap and this increases the credit risk. Initially, this is low risk, though as the swap approaches maturity, more economic capital is required.

## **References**

- [1] Crouhy, M., Galai, D. & Mark, R. (2001). *Risk Management*, McGraw-Hill, New York.
- [2] Crouhy, M., Turnbull, S.M. & Wakeman, L. (1999). Measuring risk adjusted performance, *Journal of Risk* **2**(1), 5–35.
- [3] Demine, J. (1998). Pitfalls in the application of RAROC in loan management, *Arbitrageur* **1**(1), 21–27.
- [4] Froot, K.A. & Stein, J.C. (1998). Risk management, capital budgeting and capital structure policy for financial institutions: an integrated approach, *Journal of Finance* **48**, 1629–1658.
- [5] Matten, C. (2000). *Managing Bank Capital*. John Wiley & Sons, New York.
- [6] McNeil, A. Frey, R. & Embrechts, P. (2005). *Quantitative Risk Management*, Princeton University Press, NJ.

- [7] Merton, R.C. (1993). Operation and regulation in financial intermediation: a functional perspective, in *Operational and Regulation of Financial Markets*, P. Englund, ed, The Economic Council, Stockholm.
- [8] Merton, R.C. (1997). A model of financial guarantees for credit sensitive, opaque financial intermediaries, *European Finance Review* **1**, 1–13.
- [9] Merton, R.C. & Perold, A.F. (1993). Management of risk capital in financial firms, in *Financial Services*, S.L. Hayes, ed, Harvard Business School Press, Boston.
- [10] Perold, A.F. (2001). *Capital Allocation in Financial Firms*, Working paper, Harvard Business School.
- [11] Prmia (2007). *Risk Adjusted Performance Measurement*, surveys@prmia.org.
- [12] Ranson, B.J. (2003). *Credit Risk Management*, Thomson, Sheshunoff, TX.
- [13] Ross, S.A. (1989). Institution markets, financial marketing, and financial innovation, *Journal of Finance* **44**, 541–556.

- [14] Stoughton, N.M. & Zechner, J. (2006). *Optimal Capital Allocation Using RAROC and EVA*, Working paper, University of Calgary.
- [15] Turnbull, S.M. (2000). Capital allocation and risk performance measurement in a financial institution, *Financial Markets, Institutions & Instruments, NYU* **9**(5), 325–357.
- [16] Turnbull, S.M. (2002). Bank and business performance measurement, *Journal of Economic Notes* **31**(2), 215–236.
- [17] Wilson, T. (1992). RAROC remodelling, *Risk* **5**(8), 112–119.

## **Related Articles**

**Economic Capital Allocation**; **Economic Capital**; **Market Risk**; **Value-at-Risk**.

STUART M. TURNBULL
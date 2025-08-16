# **Special-purpose Vehicle (SPV)**

A special-purpose vehicle (SPV) is a legal entity created by a firm for a specific business objective, usually in the context of **securitization**. SPVs are often used to finance a project or issue securities without putting at risk the original holder of the securitized portfolio.

We focus here on quasi-operating companies, which are SPVs operating in primarily one type of business: interest rate and foreign exchange derivatives, credit derivatives, and buy and hold assets or others. Derivative product companies (DPCs), structured investment vehicles (SIVs), and credit derivative product companies (CDPCs) are the most well-known operating companies.

## **Derivative Product Companies (DPCs)**

(DPCs) are intermediaries between financial institutions (known as their *parents* or *sponsors*) and their third-party counterparties [2, 5]. DPCs intermediate swaps between the sponsor and third parties under the approved International Swaps and Derivatives Association (ISDA) Master Agreement. Enhanced subsidiaries differ from other derivativeproduct subsidiaries, as their credit ratings do not depend on their parent's guarantee. A DPC may engage in over-the-counter interest rate, currency, and equity swaps and options as well as certain exchangetraded futures and options depending on its individual structure. A DPC is capitalized at a level appropriate for the scope of its business activities and desired rating. In most cases, DPCs have been set up to overcome credit sensitivity in the derivative-product markets. There are two types of DPCs: continuation and termination structures. The continuation structures are designed to honor their contracts to full maturity even when a wind-down event occurs, while termination structures are designed to honor their contracts to full maturity, or should certain events occur, to terminate and cash settle all their contracts prior to their final maturity. DPCs are typically AAA rated and are often referred to be the *AAA face of the sponsor*. They are market risk neutral by mirroring their trades with the third parties with the parent or the sponsor. They are exposed to the credit risk of third parties. The structure is equipped with exit strategies and resources so that upon certain winddown scenarios, the vehicle is expected to meet its derivative obligations with AAA certainty.

The market for DPCs developed in early 1990. Every bank seeking to be eligible as an AAA counterparty in derivative contracts sponsored its own DPC.

Credit risk of third-party counterparties is quantified by sophisticated models. Potential future market environment is simulated and valuation modules are used to project the mark-to-market of each swap contract. By combining market paths with credit paths (in which the creditworthiness of the counterparty is simulated), one can assess where capital is being deployed to cover for losses. The potential losses corresponding to each market path can be analyzed by combining the results of default simulations and the counterparty exposures. A consideration of losses across all market paths permits the construction of a distribution of potential credit losses. The credit enhancement to protect against losses at a given level of confidence may be analyzed. This risk model can also quantify the potential change in the portfolio's value over a period of time.

A DPC with a continuation structure generally receives collateral from the parent to cover its exposure to the parent resulting from the back-toback trades. This collateral amount, after appropriate discount factors are applied, is equivalent to the net mark-to-market value of the DPC's portfolio of contracts with its parent. Upon the occurrence of certain events, however, the management of the DPC's portfolio will typically be passed on to a contingent manager.

In the short period prior to the transfer of portfolio management to the contingent manager, the value of the DPC's contracts with its parent could rise. Using the capabilities of the risk model, the potential increase in the DPC's credit exposure to the parent may be quantified.

In a termination structure, the value of the DPC's portfolio can change over the period beginning with the last regular valuation date and ending at the early termination valuation date upon occurrence of a termination trigger event. Again, the potential change in the portfolio's value may be determined at the desired level of confidence by using the same risk model.

DPCs are equipped with a liquidity model that covers short-term liquidity squeezes and with operational capital that covers operational risks.

## **Structured Investment Vehicles (SIVs)**

SIVs are limited-purpose operating companies that take arbitrage opportunities by purchasing mostly highly rated medium- and long-term assets and funding themselves with cheaper short-term commercial paper (CP) and medium-term notes (MTNs) [3, 6, 7].

SIV-Lites combine features of both collateralized debt obligations (CDOs) and SIV technologies. They typically purchase high-grade asset-backed securities (ABSs), primarily residential mortgage-backed securities (RMBS), but may also include a small portion of commercial mortgage-backed securities (CMBS) or other ABSs and fund themselves by issuing shortterm CP or repurchase agreements (REPOs) and MTNs. SIVs and SIV-Lites roll their senior shortterm liabilities (REPOs and CPs) unless a market disruption event occurs or any other liquidation trigger is reached.

When analyzing SIVs or SIV-Lites, stochastic cash-flow models could be used to quantify the risks they are exposed to. The main risk factors of the asset portfolio, which include credit migration and market risk, are captured and projected by Monte Carlo simulation. Credit migration measures the new credit profile of the portfolio. Defaults net of recovery result in loss in the portfolio. Upgrades and downgrades directly affect the credit profile and the market value of the portfolio. Asset spreads and asset market values are projected in the capital model as well as credit migration. Historical spread data are used to calibrate the asset spread model. Rating migration, default correlation, and recovery assumptions are based on historical default studies and applied to the capital model. Market risk involves interest rates and foreign exchange rates (if there exists foreign currency valuation) modeling. SIVs or SIV-Lites are designed to be market risk neutral. Additional interest rate and foreign exchange rate sensitivity tests are usually used to this end. These tests mainly measure the change in the net asset portfolio value caused by a sudden change in the interest rates or foreign exchange rates. Liquidation risk is the most complicated risk factor to be modeled. Liquidation assumptions on the assets are required when senior debts cannot be rolled over. Haircuts on the assets for the liquidation purpose are based on stressed historical asset price movements and applied appropriately when needed.

Since the stability of capital requirement is one of the key components in the risk management of SIVs or SIV-Lites, a certain large number of Monte Carlo paths are generated to test whether the model converges in a good manner.

A liquidity model might be used to monitor the vehicle's internal liquidity relative to the liabilities. Net cumulative outflow (NCO) tests are normally calculated for each rolling 1, 5, 10, and 15 business day period commencing on the next day of calculation through and including the day that is one year from the day of such calculation, for example, the vehicle needs to determine on a daily basis its 1, 5, 10, and 15 day peak NCO requirements over a period of one year.

SIVs and SIV-Lites also face management and operational risk that is covered by additional capital.

In mid-2007, SIVs and SIV-Lites experienced a number of difficulties owing to, among other things, the liquidity crunch and spread widening. Various SIVs and SIV-lites were downgraded by rating agencies. Some of them went into default. SIV exposures in rated funds have dropped dramatically since the last quarter of 2007.

## **Credit Derivative Product Companies (CDPCs)**

CDPCs are special-purpose entities that sell credit protection under credit default swaps (CDS) or certain approved forms of insurance policies [1, 4]. Unlike traditional DPCs, which are engaged in interest rate, currency, and equity swaps and options, CDPCs sell protection on single-name obligors, such as corporate, sovereign, and asset-backed securities, or on tranched, structured finance obligations. CDPCs can also buy protections or enter interest rate and currency swaps. However, that is mainly for hedging purposes.

When analyzing CDPCs, sophisticated models are built to quantify the risk of CDPCs and analyze the amount of capital needed to meet the obligations for their counterparty ratings and various debt-note ratings, respectively. These obligations include payments on credit events, payments on senior fees expenses, and potential termination payments upon counterparty defaults.

The key risk factors that CDPCs might be exposed to are credit risk for the reference entities, counterparty risk, and market risk. Credit risk is the primary concern for a CDPC. If the reference entity on which a CDPC sells protection defaults, the CDPC will suffer a loss. Historical default studies and rating analysis are applied to simulate the time to default of the reference portfolio. Correlation and recovery assumptions are used to size the loss. Single-period time-to-default models are efficient tools to model credit risk. However, multiperiod rating transition models become necessary when the credit qualities of the underlying assets are required to be featured in the capital model. When modeling the credit risk of CDO tranches, drilling down to the underlying obligors is more effective to model the correlation risk.

When a CDS counterparty experiences a default, the swap contracts that are associated with that counterparty are unwound and a termination payment (fair market value) may need to be calculated. Credit spread widening can lead to large termination payments upon counterparty default. Spread models quantify the potential deterioration in the creditworthiness of the assets as well as market volatility. Spread data are usually grouped in rating and industry categories.

Market standard valuation modules for singlename CDS contracts and tranched CDO transactions are generally used to calculate the fair market value upon the counterparty defaults. Besides credit spreads, interest rate projection is necessary for the discounting of future cash flows in order to calculate present values, the amount of coupon paid on the notes, and the amortization schedule for CDPCs that invest in prepayment-sensitive assets such as ABSs. A CDPC is exposed to foreign exchange risk when it makes or receives payments in more than one currency, and no hedge has been set up to neutralize the mismatch. In this case, the foreign exchange rate is modeled in the capital model. The cash-flow waterfall is added to the default model according to the structure of the CDPCs. CDPCs also face liquidity risk. A liquidity model might be developed to size capital for short-term needs.

Like modeling SIVs or SIV-Lites, the model calibration is a complex exercise. A certain large number of Monte Carlo paths are generated to test appropriate model convergence.

CDPCs also face operational risks and CDPC management risk. Additional capital is typically assigned for these risks.

Since CDPCs have no market value triggers that would force them to sell assets or reduce leverage, they have not been affected as significantly by the subprime mortgage crunch as SIVs or SIV-Lites in 2007. However, CDPCs have been experiencing a hard time to find counterparties because of the volatility of the spreads.

## **References**

- [1] *Criteria for Rating Global Credit Derivative Product Companies*, Standard & Poor's, www.ratingsdirect.com
- [2] Gupton G.M., Finger C.C. & Bhatia M., Morgan Guaranty Trust Company, (1997). *CreditMetrics*, Technical Document, April 1997.
- [3] Merrill Lynch (2005). *Fixed Income Strategy, "SIVs are Running Strong"*, January 28, 2005.
- [4] Polizu, C., Jiang, J. & Venus, S. (2007). *Structured Finance ViewPoint on Quantitative Analytics: Creating Transparency To Better Manage Risk*, Standard & Poor's.
- [5] *Rating Derivative Product Companies S&P Structured Finance Criteria*, Feb 2000, www.ratingsdirect.com
- [6] de Servigny, A. & Jobst, N. (2007). *Quantitative Handbook of Structured Finance*, 1st Edition, McGraw-Hill.
- [7] *Structured Investment Vehicle Criteria* (published on March 13, 2002), www.ratingsdirect.com

## **Related Articles**

#### **Collateralized Debt Obligations (CDO)**; **Credit Default Swaps**; **Securitization**.

CRISTINA POLIZU & JENNIFER JIANG
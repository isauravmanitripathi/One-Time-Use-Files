# **Collateralized Debt Obligations (CDO)**

Collateralized debt obligations (CDOs) can be generically defined as structured products using tranchinga and securitization technology to repackage and redistribute credit risks. Figure 1 symbolically depicts the mechanics of a CDO.

The first forms of CDOs appeared during the 1980s with the repackaging of high-yield bonds such as collateralized bond obligations (CBOs), following hot on the heels of the first collateralized mortgage obligations (CMOs) pioneered by First Boston in the United States in 1983. This technique was later extended to other asset classes such as bank loans (especially leveraged loans). With the advent of the credit derivatives market and the surge in credit default swap (CDS) trading at the beginning of the decade, CDOs became one of the fastest growing segments of the credit market (the so-called structured credit market) and a crucible of financial innovation. In the limited time frame of a few years (2001–2007), CDOs and structured credit arguably became the hottest areas in capital markets and among the greatest fee and trading income generators for investment banks, asset managers, and hedge funds, until the 2007 subprime crisis marked the (temporary?) end of the party.

This article first provides definitions and a typology of CDOs, based on their main characteristics. The second section deals with the main modeling techniques for CDOs. We then dwell upon the impact of the 2007 subprime crisis on the CDO business and look at the evolution of the market and structures in the aftermath of this watershed. Our concluding remarks deal with the future for CDOs in a post–credit crisis world.

## **Definitions and Typology of CDOs**

CDOs cover a large variety of products and structures. The following parameters can be used to define the different types of CDOs.

#### *The Nature of Collateral Assets*

The common denominator of CDO transactions was, until 2002–2003, the application of securitization techniques to (credit) assets sourced in the financial markets, such as bonds (CBOs), or from financial institution balance sheets, such as bank loans (collateralized loan obligations (CLOs)). Theoretically, any asset generating recurrent cash flows can be securitized and therefore be used as a collateral to a CDO transaction. What distinguishes CDOs from securitization transactions (asset-backed securities (ABSs)),b which deal with extended pools of small credit exposures, is that CDO underlying assets can be construed as unitary credit risks and analyzed as such (each CDO underlying asset usually carries an individual credit rating).

In this decade, the range of instruments used as CDO collateral has considerably increased, including securitization issues (CDOs of ABS), other CDOs (CDOs of CDOs), trust-preferred securities (TRUPs), and going as far as hedge funds<sup>c</sup> or private equity participations.

In parallel, the rise of credit derivatives (CDSs) has led to the emergence of a new type of products, the synthetic CDOs.d Instead of "cash" securities, these instruments reference a pool of CDSs, which replicate the risk and cash-flow profile of a bond portfolio. The credit risk is transferred to the specialpurpose vehicle (SPV) using CDS technology, which then issues securities backed by this "synthetic" portfolio. What makes synthetic CDOs attractive to structurers and managers is that they avoid the logistics and financial risk of buying in and warehousing securities while a CDO is being constructed and sold to investors. The use of CDSs as reference "assets" for CDOs opened the door to innovative structures and management techniques, which led part of the structured credit business away from traditional securitization and closer to exotic derivative trading as discussed later.

#### *Risk Transfer Mechanism*

One must first distinguish credit risk transfer from the collateral portfolio to SPV and, second, from the SPV to capital market investors.

Credit risk transfer from the collateral portfolio to the SPV may happen *via* the following:

![](_page_1_Figure_1.jpeg)

**Figure 1** Mechanics of a CDO (Bruvere *et al.* 2005)

- "real" asset acquisition (true sale): "cash CDO" or
- credit derivative technology (or other, e.g., insurance): "synthetic CDO" or collateralized synthetic obligation (CSO).

Risk transfer from the SPV to capital market investors can take the following forms:

- SPV credit-linked note issuance: "funded CDO";
- credit derivatives (CDSs) sold by the investor to the SPV: "unfunded CDO"; and
- a combination of the above-mentioned: "partially funded CDO". Most whole capital structure CDOs fall into that category.

#### Objective of the Transaction

Most CDOs are structured for arbitrage purposes. Arbitrage CDOs are tailor-made investment products, using cash or synthetic technology, created for the benefit of capital market investors. In these transactions, collateral assets are usually sourced in the fixed-income cash or credit derivative markets.

However, a significant part of the CDO market was also driven with the purpose of bank balance sheet management. In such a transaction, the

objective for the sponsor bank is to obtain regulatory or economic capital relief using CDO technology to transfer credit risk to investors. In these transactions, assets or credit risk exposures are typically sourced from the sponsor bank's own balance sheet.

#### Static or Managed CDOs

"Static CDOs" are characterized by the fact that the composition of the reference portfolio does not change over the life of the transaction (but for substitutions in a limited number of cases).

At the opposite end of the spectrum, "managed CDOs" (see **Managed CDO**) allow for the dynamic management of the portfolio of collateral assets within a predetermined set of constraints. CDOs are usually managed by a third-party asset manager with credit management expertise. In a managed arbitrage CDO, the asset manager's objective may be the following:

- to avoid default and ensure timely payment of interest and repayment of principal ("cash-flow CDO") or
- to optimize the market value of the underly- $\bullet$ ing collateral pool through active management ("market-value CDO").

"Self-managed CDOs" enable investors themselves to manage the reference portfolio of the CDO they have underwritten.

The following section provides an analysis of the main CDO modeling techniques.

## **Analysis of CDO Modelling Techniques**

### *Cash-flow CDOs*

On the basis of securitization techniques, cash-flow CDOs usually aim at exploiting an arbitrage opportunity between the yield generated by a portfolio of credit assets and that required by investors on the securitized debt, the great majority of which (80–90%) is rated investment grade due to the various credit enhancement mechanisms:

• *Tranching and waterfall*

The creation of several layers of risk ("tranches") and the sequential allocation of income generated by the collateral portfolio in order of tranche seniority.

• *Subordination*

Losses are absorbed by all junior tranches to a given tranche, thus providing a protection "cushion" (when the CDO is liquidated, the senior creditors have priority over the mezzanine investors, who have priority over the equity holders).

• Overcollateralization (O/C) and interest cover (I/C) tests

These act as CDO covenants, leading to the diversification of cash flows toward the early repayment of the most senior tranche if they are breached, thus strengthening the level of subordination.

• *Diversification*

Reference portfolios are diversified in terms of obligor geography and sector, thus limiting the risk of correlated defaults.

Risks and sources of performance in cash-flow CDOs include the following:

• *Default risk*

Underperformance of the underlying portfolio (defaults) leads to a decrease in the amount of assets (and therefore the amount of capital, the equivalent of a write-off in accounting terms) and in future income streams (since the coupon is no longer being paid on the asset in default) and therefore in the dividend amounts ultimately paid to the equity tranche investors.

• *Portfolio management*

Active trading by the CDO manager may generate losses (which have the same impact as a default) or gains (which are then paid out in dividends or incorporated into the CDO capital, thereby, increasing the subordination level). Generally, the CDO manager is only able to modify the portfolio for a given period (5–7 years, the so-called reinvestment period). He/she must comply with a set of criteria (quality of the portfolio, sector diversification, maturity profile, maximum annual trading allowance, etc.) defined in accordance with the rating agencies.

• *Ramp-up risk*

When a cash CDO is launched, the underlying portfolio cannot be immediately constituted by the manager (essentially to avoid disturbing market liquidity). The portfolio is, therefore, built up over 3–6 months (the ramp-up period). During that time, asset prices may go up and the initial average coupon target for the portfolio might not be attained. In addition, the bank arranging the transaction carries the credit risk of the collateral during the ramp-up period (the so-called "warehousing" risk). To avoid taking too much risk on their balance sheets and allocate capital, banks have been using off-balance sheet vehicles (such as conduits and structured investment vehicles (SIVs)) to park the assets during the ramp-up period. However, as witnessed during the 2007 credit crisis, these defense structures backfired as liquidity dried up and banks were forced to reconsolidate the vehicles and the security warehouses on their balance sheets.

• *Reinvestment risk*

During the life of the transaction, the manager is regularly led to replace assets and therefore to reinvest part of the portfolio. Market conditions may change and the average coupon level might not be attained. To manage this risk, the manager and the other equity investors usually have an early termination option on the CDO.

#### *Synthetic CDOs: Correlation Products*

In the synthetic space, tranching and securitization techniques can also be applied to a portfolio of CDSs (the so-called whole capital structure (WCS) synthetic CDOs).

However, a watershed appeared with the creation of single-tranche technology, fed by the rise in CDS trading liquidity and advances in credit-modeling expertise. For an investor, any CDO tranche can be considered as a "put spread"e on the losses of the reference portfolio (the attachment and the detachment points of the CDO tranche being equivalent to the two strike prices of this option combination). Thus, the pricing of a CDO tranche (*x*% to *y*%) can be deduced from the value of the portfolio (i.e., the losses from 0 to 100%) from which the value of the equity tranche (0% to *x*%) and that of the senior tranche (*y*% to 100%) are subtracted. These techniques led to the development of the exotic credit market, which trades on the basis of "correlation", not unlike the equity derivative market, and volatility.

In a bespoke single-tranche CDO, the arranger usually retains the unsold tranches on its books and dynamically manages their credit risk by selling a fragment (delta) of the notional amount determined for each reference credit entity in the portfolio. This delta must then be readjusted dynamically depending on the changes in the credit spreads. The objective of delta hedging is to neutralize the price variations in the tranche that are linked to changes in the spread of the entities in the underlying portfolio. The delta of a tranche depends upon its seniority and residual maturity. Since deltas are being determined using marginal spread variations, a significant change in spreads will lead to a profit or loss depending upon the convexity of the tranche price ("gamma" in option language). Synthetic CDO arrangers, therefore, not only manage first-order risk levels but also need to monitor their convexity positions.

These hedging mechanisms, however, are not perfect, since they do not deal with second-order risks:

- *Recovery rate in the event of default* This parameter cannot be inferred from market data. Thus, it is necessary for the dealers to set aside appropriate levels of reservesf to cover this risk.
- *P&L in the event of default*

Tranche convexity properties are magnified in the event of default and bank positions must be managed accordingly.

• *Correlation ("rho")*

The pricing and risk management of CDOs are based on correlation rate assumptions. Correlation is determined on the basis of a smile (or skew), which depends mainly on the subordination of the tranche considered. Different correlation rates can thus be given to the attachment and detachment points *x* and *y*. This approach by "correlation pairs" is commonly referred to as *base correlation.*

• With the rise of the credit index market,g CDO arrangers have benefited from new methods for managing their correlation books. Standard tranches are now traded on the main indices in the interbank market, thus providing a benchmark level for the correlation parameters. Until the 2007 credit crisis, liquidity had significantly increased in the CDO tranche market, enabling arrangers to rebalance their books with credit hedge funds and other sophisticated investors.

## **The Impact of the Subprime Crisis on the Evolution of the CDO Market**

With the 2007 subprime and credit crisis, CDOs have come to epitomize the evil of financial innovation. The credit-risk-dispatching mechanism implicit in CDO structures has been broadly accused of fostering the wide spread of poorly understood risks among mainstream capital market investors lured by attractive yields in a low interest-rate environment. To what extent does that charge stand?

## *ABS CDOs and Subprime Crisis: How Did It Happen?*

A key driver for the subprime residential mortgagebacked securities (RMBS) market was the strong demand for subordinated bonds (aka mezzanine tranches, in particular, BBB and BB) from ABS CDO managers.

The reason these bonds were so attractive is that the rating agencies assumed that a portfolio of subordinate mezzanine bonds from various ABS issues would not be highly correlated (much as they assume that corporate bonds from various industries are not highly correlated). Because of this low-correlation assumption, pooling subprime mezzanine bonds into a CDO structure enabled the CDO manager to create, in essence, new AAA-rated CDO bonds, using only BBB subprime RMBS.

The assumed diversification benefit drove the capital structure of the CDO and explains a large of part of the enormous "misrating" of subprime CDO risk by rating agencies (let alone the rating of the underlying subprime RMBS risk itself).

**ABS CDO—A Key Driver of the "Subprime" Demand.** The demand from ABS CDOs allowed RMBS originators to lay off a significant portion of the risk. We estimate that \$70 billion of mezzanine subprime RMBS were issued in 2005–2007 *versus* \$200 billion of mezzanine ABS CDOs over the same period. Such notional amount of mezzanine ABS CDOs roughly represents an implied capacity of \$90 billion for mezzanine subprime RMBS investments (over the vintages 2005–2007).h

This excess demand was filled by synthetic risk (CDS) buckets. The creation of the ABS CDS market multiplied credit risk in the system, allowing for the creation of far more CDOs than the available cash "CDOable" assets. For example, one tranche of a subprime RMBS securitization (nominal \$15.2 million) was referenced in at least 31 mezzanine ABS CDOs (total notional of \$240.5 million).

High-grade ABS CDOs also need to be taken into account. Although the "subprime" demand from these CDOs (roughly \$85 billion) was lower than the nominal of high-grade subprime actually issued (\$230 billion), they fueled the issuance of mezzanine ABS CDOs through the feature of the "inner CDO bucket". Such a bucket typically had an average size of 20%, allowing CDO arrangers to channel a significant portion of ABS CDO risk. Such "resecuritization" was also facilitated by the existence of CDS on CDOs, further multiplying the credit risk in the system: one tranche of a mezzanine ABS CDO (\$7.5 million nominal) was referenced in at least 17 high-grade ABS CDOs (\$154 million total notional).

At first sight, it would, therefore, be fair to conclude that, since 2005, ABS CDOs have globally absorbed almost every cash-subordinated bond created in the subprime world (and have sold significant protection in synthetic form as well), while traditional cash buyers were largely absent. However, does this mean that the credit risk was effectively transferred to "mainstream" capital market investors?

**Anatomy of the ABS CDO Market: Where Did It All Go?.** About \$430 billion of ABS CDOs were issued between 2005 and 2007. However, the amount of risk transferred outside the banking system was actually limited because of the following factors:

- investment banks retaining a significant part of super-senior risk, either directly (\$85 billion for the most affected: Citigroup, UBS, Merrill Lynch, Morgan Stanley) or indirectly (by taking on counterparty risk on monoline insurers; \$120 billion notional amounts);
- resecuritization effect though CDO bucket (\$40 billion notional);
- off-balance sheet vehicles, for which banks retained all potential losses (conduits) or part of the losses (SIV, ∼\$15 billion of ABS CDO investments); and
- "quasi-"off-balance sheet vehicles, such as money market funds that were subsequently supported by bank capital.

Outside the main banking sector, the most notable "CDO" casualties were either sophisticated insurers (such as AIG) or medium-sized banks (IKB, SachsenLB, and other German Landesbanken).

As a result, it appears that CDOs were primarily a repackaging tool. The main roots of the "subprime" demand stem from abusive off-balance sheet structures (SIVs, conduits) and regulatory capital arbitrages (negative basis trades, long/short badly captured by Value-at-Risk (VaR) models, etc.), both of which resulted in maintaining most of the risk within the banking system while "masking" its true price/value.

One could argue that there was no "real" CDO market for RMBS where rational investors could have sent earlier warning signals (by reducing demand, refusing incestuous features such as CDO buckets within ABS CDOs) and acted as stabilization agents (long-term demand, different investor base than in the underlying RMBS market).

In addition, the derivative market did not perform up to its objectives, as it was created too late (the ABX index, which effectively introduced a greater price transparency) and actually magnified the effects of the mispricing/misrating of RMBS risk.

In conclusion, if the ABS CDO market effectively drove the demand for mezzanine subprime RMBS, its impact on mainstream investors has been limited. In that respect, it is worth noting that the vast majority of RMBS risk (approximately 82 cents on the dollar) ended up being rated AAA and acquired not by CDOs but by institutions taking advantage of very cheap funding.

#### *How did Other CDO Markets Fare?*

**Leveraged Loan CLOs.** CLOs have suffered from pressure on both the asset and the liabilities sides. Prices of leveraged loans fell in line with the overall credit market, due to technical factors (significant loan overhang resulting from warehouses at the major investment banks) and fundamental fears (increase in default rates, weakly structured leveraged buyout (LBO) deals). On the liability side, we estimate that negative basis buyers represented 50% of the AAA CLO buyer base, while banks and SIVs/CDOs accounted for 25% and 15%, respectively. The CLO market suffered from the disappearance of such "cheap funding".

Even though we witnessed an LBO "bubble" (private equity houses taking advantage of the strong CLO bid), the impact of the burst has not been as significant as for the ABS CDO market:

- CLOs were not the sole buyer of leveraged loans.
- They did not suffer from misrating.
- New AAA CLO buyers stepped in (Asian institutions, unaffected banks, insurance companies).

Most of the CLO deals issued in 2008 have been balance sheet driven (cleaning up of warehouses), with simple two-tier structures (AAA and equity), where the AAA tranche (or the equity) is retained by the originating bank.

As the full capital structure execution is challenging and as the sourcing of cash asset is difficult (illiquidity, no warehouse providers for ramp up), the development of single-tranche synthetic CLOs, supported by the growth of the Loan CDS market (ISDA documentation, launch of LCDX and LevX indices), is a key feature of the forthcoming years.

**Corporate Synthetic CDOs.** With the huge growth in synthetic CDOs, what is commonly referred to as the *structured bid* became a dominant driver of credit spreads. While a combination of mark-tomarket losses, rating downgrade risk, and headline risk could have caused investors to unwind positions in synthetic CDOs, this market segment actually held up well in line with the underlying asset quality (corporate earnings) further supported by the liquidity provided by banks (correlation desks).

Even though the market avoided the "great unwind", the buying base for these products has essentially gone away, and while some prop desks and hedge funds are still active, the institutional money that provided the liquidity backbone has vanished.

## **Conclusion: Where Next for CDOs?**

The postcrisis CDO market will probably be characterized by a convergence trend toward the mechanics of the corporate synthetic market, which has proved more efficient and resilient for the distribution of credit risk:

- the development of index and index tranches (transparent and traded correlation) fueling liquidity;
- less reliance on rating agencies and more in-house due diligence on assets; and
- a return to balance-sheet-driven transactions.

The main challenges for the CDO market include the following:

- restoring investor confidence in the benefit of structured products by providing better transparency and liquidity;
- addressing the AAA funding issue (now that SIVs and conduits have been dissolved); and
- overcoming the discrepancies in accounting treatment.i

Once the dust has settled, we expect securitization and CDO transactions to come back on the basis of more transparent and rational fundamentals.

## **End Notes**

a*.* Tranching is the operation by which the cash flows from a portfolio of assets are allocated by order of priority to create various layers ("tranches"), from the less risky ("senior" tranche) to the most risky ("first loss" or "equity" tranche). Tranching technology is usually performed using rating agency guidelines in order to ensure that the senior tranche attracts the most favorable rating (triple-A).

b*.* Asset-backed securities are securities representing a securitization issue. The ABS market covers mortgage-backed securities (residential and commercial), consumer (credit card, student loans, auto loans), and commercial loans (trade receivables, leases, small business loans, etc.).

c*.* Collateralized fund obligations.

d*.* "Synthetic" in as far as the mechanism for transferring risk is synthetic, using a derivative.

e*.* Combination of two put options on the same underlying asset, at two different strike prices.

f*.* Usually in the form of bid–ask spreads.

g*.* iTraxx for the European market and CDX.NA for the US market.

h*.* On the basis of the following assumptions: 50% of the portfolio allocated to subprime, of which 60% to the precedent vintage.

i*.* While a cash CDO (or any cash bond) can be accounted for as "available for sale" by banks and insurers (meaning that its price volatility will directly impact the equity base of the investor), the valuation of an equivalent synthetic products impacts the income (P&L) of the investor.

## **Reference**

[1] Bruyere, R., Cont, R., Copinot, R., Jaeck, Ch., Fery, L. & Spitz, T. (2005). *Credit Derivatives and Structured Credit: A Guide for Investors*, Wiley.

## **Related Articles**

**Base Correlation**; **Basket Default Swaps**; **CDO Square**; **CDO Tranches: Impact on Economic Capital**; **Collateralized Debt Obligation (CDO) Options**; **Credit Default Swaps**; **Default Barrier Models**; **Forward-starting CDO Tranche**; **Managed CDO**; **Multiname Reduced Form Models**; **Nested Simulation**; **Random Factor Loading Model (for Portfolio Credit)**; **Reduced Form Credit Risk Models**; **Special-purpose Vehicle (SPV)**; **Total Return Swap**.

RICHARD BRUYERE & CHRISTOPHE JAECK
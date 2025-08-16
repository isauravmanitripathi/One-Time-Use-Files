# **Leveraged Super-senior Tranche**

A leveraged super-senior (LSS) note is a structure that allows investors to take a leveraged exposure to the super-senior (SS) part of a collateralized debt obligation (CDO). This provides an enhanced level of return while typically maintaining a AAA rating. Leverage is achieved by posting an initial collateral amount that is less than the notional of the underlying SS tranche. All credit losses to the investor are capped at the collateral amount, but the coupon is paid on the full notional. Early unwind clauses are typically included in the trade to mitigate the risk to the issuer that losses exceed the collateral amount. Compared to a standard SS tranche the investor is exposed to markto-market (MTM) risk as well as credit risk, that is, for certain market moves his/her principal could be reduced even if no credit losses have occurred owing to a forced unwind. The issuer faces a so-called gap risk, the risk that the MTM of the tranche will fall below the initially posted collateral amount before a trade unwind can take place.

### **Super-senior Swap**

In an (unleveraged) SS swap transaction an investor (protection seller) will take exposure to credit losses on the SS tranche of a CDO (*see* **Collateralized Debt Obligations (CDO)**). This means that in return for a regular fee (or coupon), the investor will make good all losses on the underlying reference portfolio that exceed the attachment amount, but are below the detachment amount. For an SS tranche the attachment point will be higher than what is required for achieving a AAA rating (*see* **Credit Rating**). The spread of the tranche is the fee that values the swap at 0.

### **Leveraged Super-senior (LSS) Swap**

Since the risk of experiencing any losses on an SS tranche is remote, the spread for a standard SS tranche is low. In particular, it is lower than for other AAArated securities, which limits the attractiveness of the transaction to investors. LSS structures became popular in 2005, when spreads on the 22–100%, 5-year, iTraxx index (*see* **Credit Default Swap (CDS) Indices**) tranche were around 5 bps.

Issuers of LSS notes are typically investment banks. When arranging a CDO transaction the issuer needs to be able to sell the entire capital structure, as otherwise he/she will be left with the remaining risk. For the reasons mentioned above, it can be harder to sell SS risk than risk on mezzanine and senior tranches. The LSS transaction allows the issuer to repackage the SS risk in a way that is attractive to the investor.

In an LSS transaction, the investor will invest in an SS tranche with notional *N* (referred to as the *reference tranche*). However, he/she will only post an initial collateral amount *X* (also referred to as the *participation amount*) that is less than the notional amount of the tranche. Any credit losses to the investor will reduce the collateral and losses are thus capped at the collateral amount, *X*. However, the investor still receives a coupon on the full notional, *N*, of the reference SS tranche. The ratio, *N/X*, is referred to as the *leverage*. If losses reach the collateral amount, the trade will terminate without any further cash flows. The typical structure of the LSS trade can be seen in Figure 1. We compare credit losses on the LSS and a standard SS in Figure 2.

The LSS structure provides an increased coupon to the investor compared to investing the collateral amount *X* in a standard SS tranche. The reason for this is that the investor takes on MTM risk over and above his/her credit risk as is described below.

The issuer of an LSS note (protection buyer) is only covered for losses up to the collateral amount *X*. However, he/she will typically hedge his/her position by selling protection on the corresponding standard SS tranche (cf. the section Hedging and Risks) where he/she is liable for all the losses on the tranche up to the full notional amount *N*. Thus, the issuer needs to mitigate the risk that losses exceed the collateral level. This is done *via* the inclusion of a trigger mechanism: As soon as a predefined trigger level is reached the trade will unwind at the MTM of the reference tranche capped at *X*. The trigger should thus be set such that the MTM on unwind will be less than *X*.

We note that in some transactions the investor has the option of posting more collateral upon trigger to avoid an unwind. In this case, the investor will continue to be paid the coupon of the original

![](_page_1_Figure_1.jpeg)

**Figure 1** This figure shows the standard structure of cash flows in an LSS transaction

![](_page_1_Figure_3.jpeg)

**Figure 2** This figure shows the credit losses to the investor and the risky fee notional, *N (t)*, as a function of the portfolio losses. The coupon amount paid to the investor at a coupon date *ti* is *s* · *N (ti)*, where *s* is the spread. For comparison we include both the behavior of the LSS and the reference unleveraged super-senior (SS)

transaction. This means that it is never optimal for the investor to deliver since after posting more collateral he/she will be liable for more losses without receiving a higher coupon in compensation. It is more favorable to reinvest in a new LSS transaction.

We describe the three main types of trigger mechanisms below. There is a trade-off between how well the trigger can approximate the MTM of the trade and how easy it is to objectively assess whether the trigger has been breached.

## **• Loss Trigger**

A loss trigger is breached when the amount of portfolio notional lost owing to defaults exceeds the trigger level. This is the easiest trigger to monitor as the loss amounts can be objectively determined. However, the loss provides an imperfect approximation for the MTM of the tranche. In particular, if spreads widen, the value of the LSS can drop severely from the point of view of the investor even in the absence of any defaults. This poses a risk to the issuer since at the time of trigger the MTM of the tranche could have dropped below the collateral amount.

## **• Spread Trigger**

Spread triggers are based on the average spread of the underlying portfolio. Trigger levels can be defined as a function of the time to maturity and the level of losses in the portfolio. This provides a much better proxy to the MTM of the tranche than the loss trigger. For some standard portfolios, for example, iTraxx or CDX (*see* **Credit Default Swap (CDS) Indices**), the value of the average spread can also be assessed using publicly available information and is hence unambiguous. Often, however, the LSS is based on bespoke portfolios. In this case, the valuation of the SS spreads will have to rely on models, for which there is no universally agreed methodology.

## **• Mark-to-market Trigger**

The MTM trigger is based on the MTM of the reference (unleveraged) SS tranche. Clearly, if the MTM trigger is set below the collateral level the issuer ensures that the collateral will cover the unwind payment (up to gap risk, cf. the section Hedging and Risks). The disadvantage is that the MTM trigger is the hardest to asses objectively. Typically, the MTM for a tranche is not quoted, and hence one has to rely entirely on (complex) models for valuation.

### **Hedging and Risks**

If the trigger mechanism guaranteed that upon unwind the issuer will receive the full MTM of the reference swap then this swap would provide a perfect hedge for the LSS. The coupon amount the investor would receive would be the same, as if he/she had invested the full notional amount *N* in an SS swap transaction.

However, there are two reasons why the trade can unwind without recovering the full MTM of the hedge:

- Typically, there will be a delay between a trigger breach and the actual unwind of the hedge. In this period, there is the risk that the MTM will drop below the collateral amount. The issuer then has to make good the difference *(MT M* − *X)*. This is the so-called *gap risk*: The issuer is exposed to large and sudden increases in the value of SS protection or equivalently increases in the spread.
- Even in the absence of a trigger breach, the LSS will unwind if the SS tranche losses have wiped out the collateral. Since the collateral is 0 in this case, the issuer will have to pay the full MTM of the hedge to unwind his/her position. However, this scenario is unlikely, since the trigger should be set so that a trigger event occurs before the collateral has been reduced to 0.

The investor in an LSS transaction faces MTM risks as well as credit risks associated with SS tranche losses. In the case of a trigger event, the investor will be forced to unwind his/her position and will lose part or all of his/her principal as he/she realizes his/her MTM losses (unless he/she posts more collateral). Unless dealing with a loss trigger, a trigger breach can happen even if the investor has not incurred any actual credit losses, for example, if there is a dramatic rise in spreads.

### **Valuation**

The valuation of LSS transactions poses additional challenges to that of pricing a standard SS tranche. This is because the unwind feature means that we need to be able to value the risk of possible MTM losses to the investor and the issuer. Hence, we need to model the joint behavior of MTM and the portfolio losses. This is a dynamic problem that requires more than knowledge of the marginal loss distributions needed for standard tranche pricing.

There are two main candidates for dynamic credit models that can, in principle, be used to value an LSS transaction:

- low-dimensional models of the portfolio loss process;
- dynamic models of all single name spreads in the portfolio (*see* **Duffie–Singleton Model**; **Multiname Reduced Form Models**).

Modeling and valuation of the LSS product is not only important for the issuer and the investor but also for assessing the rating of the note. This depends not only on the probability of experiencing credit losses but also on the probability of having a trigger event. Rating agencies (*see* **Credit Rating**) use in-house models for this as described in, for example, [1, 2].

### **Model-independent Bounds**

Some model-independent bounds for the value of the LSS can be derived. We discuss this from the perspective of the issuer who is long protection. Let us denote the spread of a standard tranche with attachment point *a* and detachment point *b* by *Sa,b*.

The spread of the corresponding leveraged tranche with collateral amount *x* will be denoted by *Sa,b,x*. Note that the leverage amount *α* is given by *α* = *(b* − *a)/x*. The most basic bound we can then write down is

$$S_{a,b} \le S_{a,b,x} \le \alpha \cdot S_{a,b} \tag{1}$$

This means the following:

• The spread of the leveraged tranche is less than the leverage amount times the spread of the unleveraged tranche. This is because the issuer has additional unwind and gap risk. The difference *<sup>α</sup>* · *Sa,b* <sup>−</sup> *Sa,b,x (*2*)*

$$\alpha \cdot S_{a,b} - S_{a,b,x} \tag{2}$$

is the *gap charge*.

• The spread of the leveraged tranche is greater than that of the unleveraged tranche. This is because of the trigger mechanism, which allows the issuer to recover the MTM of the unleveraged tranche up to the collateral amount.

We can also give a more stringent floor for the LSS value. To this, we introduce the fee leg value *Fa,b* and contingent (or loss) leg value *Ca,b* of a tranche (*see* **Collateralized Debt Obligations (CDO)**). The (positive) value of the fee leg is the expected value of all coupon payments paid on the risky notional. The contingent leg is the (positive) expected value of any loss payments. We now have the following bounds:

$$C_{a,a+x} \le C_{a,b,x} \tag{3}$$

This is because on the contingent leg, the issuer will at least recover losses up to *a* + *x*. He can effectively recover more on unwind since he/she receives the MTM of the unleveraged tranche.

We also have

$$F_{a,b} \ge F_{a,b,x} \tag{4}$$

This corresponds to the fact that on the fee leg the issuer will at most pay the fees of the unleveraged reference tranche. He/she might effectively pay less if there is an unwind not due to the trigger such that no MTM exchange takes place.

For a more rigorous discussion we refer to [3].

### **References**

- [1] Chandler, C., Guadagnuolo, L. & Jobst, N. (2005). CDO spotlight: Approach to rating super senior CDO notes, in *Standard & Poors Structured Finance*, Standard & Poor's a Division of the McGraw-Hill Companies, Inc., New York.
- [2] Osako, C., Perkins, W. & Kissina, I. (2005). Leveraged super-senior credit default swaps, Fitch Ratings Structured Finance July.
- [3] Gregory, J. (2008). A trick of the credit tail, *Risk* **21**(3), 88–92.

### **Related Articles**

**Forward-starting CDO Tranche**.

MATTHIAS ARNSDORF
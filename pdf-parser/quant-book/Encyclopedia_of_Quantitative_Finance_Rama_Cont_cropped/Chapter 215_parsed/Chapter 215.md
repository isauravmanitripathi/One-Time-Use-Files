# **Bond**

A *bond*, or a *debt security*, is a financial claim by which the *issuer*, or the borrower, is committed to paying back to the *bond holder* or the lender, the cash amount borrowed, called *principal*, plus periodic coupon interests calculated on this amount during a given period. It can have either a standard or a nonstandard structure. A *standard bond* is a fixed coupon bond without any embedded option, delivering its coupons on periodic dates and principal on the maturity date. Nonstandard bonds include, among others, zero-coupon bonds, floating rate notes, inflation-linked bonds, callable and putable bonds, and convertible bonds.

An example of a standard bond would be a US treasury bond with coupon interest 4%, maturity date November 15, 2017, and a nominal issued amount of \$20 billion, paying a semiannual interest of \$400 million (\$20 billion × 4%*/*2) every six months until November 15, 2017 included, as well as \$20 billion on the maturity date.

A bond issuer has a direct access to the market, and so avoids borrowing from investment banks at higher interest rates. A bond holder has the status of a creditor, unlike an equity holder, who has the status of an owner of the issuing corporation. This is the reason why a bond is less risky than an equity.

A bond issue is mainly characterized by the following components [4]:

- *The issuer name*: For example, France for a treasury bond issued in France.
- *The issuer type*: This is mainly the economic sector the issuer belongs to.
- *The issuer domicile*.
- *The issuance market*: The issuance market may differ from the issuer domicile. For example, the Eurodollar market corresponds to bonds denominated in USD and issued in any country other than the United States.
- *The bond currency denomination*.
- *The maturity date*: This is the date on which the principal amount is due.
- *The coupon rate*: It is expressed in percentage of the principal amount.
- *The coupon type*: It can be fixed, floating, or a mix of the two.

- *The coupon frequency*: Most commonly, it is semiannual in the United States, the United Kingdom, and Japan, and annual in the Euro zone, except for Italy, where it is semiannual.
- *The day-count type*: The most common types are actual/actual, actual/365, actual/360, and 30/360. Actual/actual (actual/365, actual/360) means that the accrued interest between two given dates is computed using the exact number of calendar days between the two dates divided by the exact number of calendar days of the ongoing year (365, 360). The term 30/360 means that the number of calendar days between the two dates is computed, assuming each month count as 30 days.
- *The interest accrual date*: This is the date when interest begins to accrue.
- *The settlement date*: This is the date on which payment is due in exchange for the bond. It is equal to the trade date plus a number of working days (generally, one to three, depending on the country).
- *The issuance price*: This is the percentage price paid at issuance.
- *The spread at issuance*: The spread in basis points to the benchmark treasury curve or the swap curve.
- *The rating*: A ranking of a bond's quality and its record in paying interest and principal. The three major rating agencies are Moody's, Standard and Poor's, and Fitch.
- *The outstanding amount*: This is the amount of the issue still outstanding.
- *The par* or *nominal* or *principal* amount: The face value of the bond.
- *The redemption value*: Expressed in percentage of the nominal amount, it is the price at which the bond is redeemed on the maturity date.
- *The identifying code*: The most popular ones are the *ISIN* (International Securities Identification Number) and the *CUSIP* (Committee on Uniform Securities Identification Procedures) numbers.

# **Bond Price and Yield to Maturity**

Bonds are usually quoted in price, yield, or spread against an underlying benchmark bond or reference swap rate. The price of a bond is always expressed in percentage of its nominal amount. The *quoted price* (or *market price*) of a bond is usually its *clean* price, that is, its *gross* price minus the *accrued interest*. When an investor purchases a bond, he is actually entitled to receive all the future cash flows of this bond, until he no longer owns it. If he buys the bond between two coupon payment dates, he logically must pay it at a price reflecting the fraction of the next coupon that the seller of the bond is entitled to receive for having held it until the sale. This price is called the *gross price* (or *dirty price* or *full price*). It is computed as the sum of the clean price and the portion of the coupon that is due to the seller of the bond. This portion is called the *accrued interest*. It is computed from the settlement date on.

The quoted *yield to maturity* of a bond is the discount yield that equalizes its gross price times its nominal amount to the sum of its discounted cash flows. As an illustration, let us consider a French bond paying an annual coupon of 7%, residual maturity 8.5 years and market price 106.459%. The accrued interest is equal to 7% × 0*.*5 = 3*.*5% (there have been six months since the last coupon payment). The bond annual yield to maturity is such that

$$106.459\% + 3.5\% = \sum_{i=0}^{8} \frac{7\%}{(1+R)^{i+0.5}} + \frac{100\%}{(1+R)^{8.5}}$$
(1)

which can be solved to yield *R* = 6%.

The price–yield to maturity relationship is inverse and convex. The inversion property means that the higher (lower) the price, the lower (higher) the yield to maturity. The convexity property means that the previous property is not symmetrical. Actually, for the same absolute change in the yield to maturity, the bond price will increase more than decrease. Convexity is an attractive property that tends to increase with bond maturity.a A bond price is also dependent on time to maturity. All else being equal, as the bond residual maturity decreases, its price converges to the redemption value. This so-called *pull-to-par phenomenon* is particularly noticeable for bonds with coupons far from their yield to maturity. The price–yield to maturity relationship is given by the following formula [1], where we assume that the bond has just paid a coupon:

$$P = \sum_{i=1}^{\delta T} \frac{CF_i}{\left(1 + \frac{R}{\delta}\right)^i} \tag{2}$$

Here, *P* denotes the bond dirty price, *T* its maturity expressed in years, *CF<sup>i</sup>* its cash flows, *R* its yield to maturity, *δ* is 1 for an annual bond, 2 for a semiannual bond, 4 for a quarterly bond, and so forth.

In other words, the yield to maturity is the internal rate of return of the cash flows produced by the bond, using a constant discount rate across all cash flows. The yield to maturity may therefore be interpreted as an "average" discount rate throughout the life of the bond or, equivalently, as the discount rate that would prevail if the yield curve happened to be flat at date *t* (which of course is not generally the case). It may be easily computed by trial and error or using built-in functions on Excel.

Under certain technical conditions, there exists a one-to-one correspondence between the price and the yield to maturity of a bond. Therefore, giving a yield to maturity for a bond is equivalent to giving a price for the bond. It should be noted that this is precisely what is actually done in the bond market, where bonds are most often quoted in yield to maturity. While bond yield to maturity is a useful concept, it should be approached with some care, given that it represents a weighted average of discount yields across maturities. Indeed, unless the term structure of interest rates is flat, there is no reason why one would consider the yield to maturity on, say, a 10 year bond as the relevant discount rate for a 10-year cash flow horizon. In fact, the relevant discount rate is the 10-year pure discount (or zero coupon) rate.

The yield to maturity, as the name suggests, can be viewed as the expected rate of return on a bond and allows comparison two bonds of the same issuer with close maturities with each other. Let us consider a 10-year bond and a 10.25-year bond issued by the French treasury, both quoted at par value (i.e., 100%). The former (the latter) yields 4.50% (4.55%). An investor will most likely prefer the second one, as it yields 5 more basis points (0.05%) than the other (a nonnegligible premium) for a maturity that is slightly longer (three months). However, the yield to maturity on an investment will be achieved only under the following constraints:

- Once bought, bond securities have to be held until maturity.
- Bond coupons (equal in our example to the yield to maturity) have to be reinvested at the bond yield to maturity.

The first assumption is restrictive in the sense that it excludes early bond sales. If interest rates go down, an investor will be willing to sell the bond before maturity so as to take advantage of capital gains. This condition is only acceptable for long-term investors (pension funds, insurance companies), who are traditionally buy-and-hold investors. The second assumption is not realistic for two reasons:

- During the life of a bond, interest rates increase and decrease, but never remain unchanged. Consequently, postulating a unique reinvestment rate is not particularly relevant.
- Taking their respective yield to maturity for two bonds as reinvestment rate, that is, assuming that two different cash flows falling on the same date can be reinvested at different interest rates, boils down to questioning the uniqueness of the reinvestment rate at a given time for the same investment horizon [2].

In general, the expected return on a bond nearly always differs from its yield to maturity, except for zero-coupon bonds, which embed no reinvestment risk, as they deliver no intermediary cash flows before maturity. In practice, instead of using the yield to maturity, investors compute the *total rate of return* on a bond, which is equal to the sum of the difference between the sale price and the purchase price and the coupons reinvested at the interest rate corresponding to each reinvestment period, divided by the purchase price. So as to determine the future reinvestment rates as well as the yield at which the bond will be sold, investors often apply various scenarios of evolution of interest rates (worst case, best case, and neutral scenarios)—this is known as *scenario analysis*. To each scenario corresponds a specific total rate of return.

#### **Duration and Convexity**

While the concept of yield to maturity has its flaws, it is quite useful in the construction of hedges against interest rate risk. Indeed, as we have seen, the bond price can generally be written as a unique function of the yield to maturity, so it is sensible to treat the yield to maturity as the main stochastic risk factor driving the price of the bond. If the yield happens to increase, the bond value will decrease, generating (in case of early unwinding) potentially significant losses against which one can choose to be immunized. For this purpose, market participants rely on an interest rate risk measure, whose popularity is inseparable from that of the yield to maturity: duration. This concept, which was developed in 1938 by the American economist Frederick Robertson Macaulay ( $1882-1970$ ), only became famous in the bond markets from the 1970s onward, a period precisely characterized by a large increase in interest rates and hence a sharp rise in interest rate risk. Macaulay had realized that a bond maturity was an insufficient measure of its effective life because it effectively took only the final cash flow into account. As an alternative to the outright maturity, he suggested that bond interest rate risk be characterized by the average "length" of the bond cash flows—the so-called *Macaulay duration* [3]. These days, a more common measure for interest rate risk is the socalled *modified duration*, which is simply defined as the absolute value of the first derivative of the bond price with respect to its yield, divided by the bond price itself. The Macaulay duration can be computed as the modified duration multiplied by the factor  $1 + \frac{R}{\delta}$ . A third measure of duration—the *dollar duration*—equals the modified duration times the bond price. Notice that dollar duration measures directly the change in value for a small change in the yield to maturity, whereas modified duration measures percentage change in value.

All duration measures are related to the slope of the bond-yield function at the current yield  $R$ , and as such can be interpreted as related to first-order terms of a Taylor expansion of the bond price in its yield. Duration is an appropriate measure of risk for small parallel moves in yield. However, when one wants to quantify the impact of large parallel yield curve moves, it should be accompanied by a secondorder measure, called *convexity*, which is the second derivative of the bond price with respect to yield to maturity, divided by the bond price. Formally, we can accomplish this by simply adding another term to the Taylor expansion.

For this, let us denote the bond modified duration by  $S$ , its convexity by  $C$ , the change in the yield to maturity by  $\Delta R$ , and the change in the bond price by  $\Delta P$ , such that

$$\frac{\Delta P}{P} \sim -S \times \Delta R + 0.5 \ C \times (\Delta R)^2$$

Duration and convexity, which are based on the flat shape of the term structure of interest rates and on exclusively parallel shifts in interest rates, are faced with two significant hurdles: yield curves are practically never perfectly flat and they are not solely affected by parallel movements.

Interestingly, the Macaulay duration of a bond or bond portfolio is the investment horizon such that investors will not care if interest rates drop or rise as long as changes are small. In other words, capital gain risk is offset by reinvestment risk, as shall be shown now in the following example.

Consider a three-year standard bond with a 5% yield to maturity and a \$100 face value, which delivers a 5% coupon rate. Coupon frequency and compounding frequency are assumed to be annual. The bond price is \$100 and its Macaulay duration is equal to 2.86 years. We assume that the yield to maturity changes instantaneously and stays at this level during the life of the bond. Whatever the change in the yield to maturity, we show in Table 1 that the sum of the bond price and the reinvested coupons after 2.86 years is always the same and equal to 114.972.

The main properties of the three duration measures are as follows:

- The Macaulay duration of a zero-coupon bond . equals its time to maturity.
- Holding the maturity and the yield to maturity of a bond constant, the lower a bond coupon rate. the higher its Macaulay or modified or dollar duration.
- Holding the coupon rate and the yield to maturity of a bond constant, its Macaulay or modified

| anlo |  |
|------|--|
|------|--|

| Yield<br>to maturity $(\%)$ | Bond<br>price | Reinvested<br>coupons | Total   |
|-----------------------------|---------------|-----------------------|---------|
| 4                           | 104.422       | 10.550                | 114.972 |
| 4.5                         | 104.352       | 10.620                | 114.972 |
| 5                           | 104.282       | 10.690                | 114.972 |
| 5.5                         | 104.212       | 10.760                | 114.972 |
| 6                           | 104.142       | 10.830                | 114.972 |

duration increases with time to maturity, as dollar duration decreases.

- Holding other factors constant, the lower a bond yield to maturity, the higher its Macaulay or modified duration and the lower its dollar duration
- Duration is a linear operator. In other words, the duration of a portfolio  $P(D_P)$  invested in n bonds  $i$  denominated in the same currency with weights  $w_i$  is the weighted average of all bond durations  $(D_i)$ :

$$D_P = \sum_{i=1}^n w_i D_i \tag{3}$$

This relationship holds for all definitions of duration (Macaulay, modified, dollar).

There are two commonly used measures of second-order interest rate risk. We have already encountered the convexity  $(C)$  but market practitioners also use the *dollar convexity*, defined as the bond convexity times the bond price. Dollar convexity is used to quantify the absolute change in a bond price due to convexity for a given change in the yield to maturity.

The main properties of the convexity and dollar convexity measures are as follows:

- For a given bond, the change in value due to the convexity term is always positive.
- Holding the maturity and the yield to maturity of a bond constant, the lower the coupon rate, the higher its convexity and the lower its dollar convexity.
- Holding the coupon rate and the yield to matu-. rity of a bond constant, its convexity and dollar convexity increase with its time to maturity.
- Holding other factors constant, the lower a bond yield to maturity, the higher its convexity and dollar convexity.
- Convexity is a linear operator. In other words, the convexity of a portfolio  $P$  invested in  $n$ bonds denominated in the same currency with given weights is the weighted average of all bond convexities.

# **End Notes**

<sup>a.</sup>Note that the convexity of a zero-coupon bond is approximately equal to the square of its maturity.

### **References**

- [1] Fabozzi, F.J. (1996). *Fixed-Income Mathematics*, 3rd Edition, McGraw-Hill, New York.
- [2] La Bruslerie, H. de (2002). *Gestion obligataire*, 2nd Edition, Economica, Paris.
- [3] Macaulay, F.R. (1938). *The Movements of Interest Rates, Bond Yields and Stock Prices in the United States since 1856*, National Bureau of Economic Research, New York.
- [4] Martellini, L., Priaulet, P. & Priaulet, S. (2003). *Fixed-Income Securities: Valuation, Risk Management and Portfolio Strategies*, Wiley Finance, Chichester.

### **Related Articles**

**Caps and Floors**.

STEPHANE ´ PRIAULET
# **Convertible Bonds**

A convertible bond (CB) is a *corporate bond* that may be converted into a certain number of shares of the issuing company, also known as the *underlying* equity. By offering the investor an option to participate in its future growth, the company is able to finance itself at a lower cost. Alternatively, the CB provides a means to issue equity in a deferred fashion when the market context or timing may not be right for the company.

Like any corporate bond, the CB is issued with a nominal, *principal*, or face value, to be redeemed at maturity, sometimes at a premium, and pays interest, typically periodic coupons, fixed or floating. In some cases (in particular, when no coupons are paid), the principal accretes continuously at a rate guaranteeing a given *yield to maturity* (YTM), and the final redemption value is the result of the accretion. The CB can be redeemed earlier than maturity at the option of the issuer (issuer's call), often with penalties in *call protection* periods (make-whole premium, guaranteed yield). Alternatively, the holder can opt out of the convertible and get his/her money back at certain prespecified discrete dates, or put dates. Coupons can be fixed or floating. The number of shares against which the CB can be converted is the conversion ratio. The value the holder obtains following conversion is the *conversion value*: ratio  $\times$  share value. The *conversion price* is the ratio of nominal over conversion ratio. It is the value of the underlying above which conversion value becomes greater than the nominal, thus making the conversion potentially attractive.

The interplay of options that are embedded in the CB (part held by the investor, part by the issuer) translates into a hierarchy of conditions bounding and constraining its value. Given the many ways in which the principal may be redeemed (coupons, redemption at a premium, accretion, mixture of the two) and the fact that the process of redemption may be interrupted prematurely, either by the holder's option to convert (or to put) or by the issuer's call, we first need to define the intermediate notion of the holder's *claim*. This is the amount the investor is entitled to claim at any intervening time between issue date and maturity, should the bond terminate at that time, in order to secure the same yield on investment as the YTM.

$$\text{claim}(t) = \sum_{T \ge t_i \ge t} \frac{C_i}{\left(1 + \text{YTM}\right)^{(t_i - t)}} + \frac{\text{redepth}}{\left(1 + \text{YTM}\right)^{(T - t)}}\tag{1}$$

where  $C_i$  is the coupon payment at time  $t_i$ ;  $t_i$  is a coupon date (in number of years since a reference date); YTM is the annualized yield to maturity guaranteed by the claim; and redemption is the amount redeemed at the maturity date.

$$\begin{array}{r} \text{redepth} = \text{principal (possibly accreted)} \\ + \text{redepth} \text{ of } \text{remium} \end{array} \tag{2}$$

At time  $t = 0$ , the claim is, by definition, the issue price, which is also the initial amount of money that gets invested, and this defines the annualized yield to maturity, YTM. At maturity, the claim is the redemption amount.

The claim serves as the basis of all three options characterizing the CB. Conditions on the CB value are enforced in the following sequence order.

Whenever the issuer has the right to exercise his/her early call option, he/she will do so optimally as soon as the CB value exceeds the amount he/she would otherwise be contractually bound to redeem, should he/she opt for early redemption (early redemption price). This entails the following constraint:

$$V(S, t) \le \text{early redemption price} \tag{3}$$

The early redemption price is usually defined as a percentage of the claim at the time or early call. Alternatively, it can be set in such a way as to guarantee a certain yield up to the date of call, which may be different from the yield to maturity.

The holder's conversion option overrides the issuer's call. It is expressed by the following condition

$$V(S, t) \ge \text{conversion ratio} \times S \tag{4}$$

and applied hierarchically after the issuer's call.

At maturity  $T$ , note that the combination of the early redemption option (which is no longer "early" and no longer an option) and the conversion option yields the following final payoff condition:

$$V(S, T) = \max(\text{conversion ratio} \times S, \text{redemption})$$
(5)

Finally, the put condition is the last one to be applied. If the investor finds, at put dates, that the CB value is still lower than the put strike (even after allowing for the option to convert), he/she will exercise his/her put. Thus

$$V(S, t_p) \ge \text{put price} \tag{6}$$

where *tp* is a put date.

Similar to the early redemption price, put price is defined as a percentage of the claim or through a guaranteed yield to put.

# **Options versus Convertible Securities**

The convertible bond is a hybrid security belonging to the category of *corporate debt* (as such, subject to credit risk) and to the category of *convertible security*. Convertible securities are claims, issued by a company that can be *converted* into the underlying equity of the company during their lifetime. Warrants belong to this general category. They feature a strike price and are very similar to American call options.

The terminology of warrants differs from that of options for reasons that run deeper than casual jargon. We do not *exercise* a warrant; we *convert* it. The warrant is not the right to *buy* the underlying share; we say it is *convertible* into that share. Indeed, the warrant is issued by the company, whereas the call option is written by an independent counterparty; *option buyers* and *option sellers* exchange their contracts independently, in the over-the-counter (OTC) market or on a listed exchange. To put it bluntly, the difference between convertible securities and options is the whole difference between being an investor in the company and taking an external view (bet) on the evolution of the price of its underlying equity. It is the difference between *corporate events* and *incorporeal events* (which is discussed later).

The number of convertible bonds that a corporation can issue cannot exceed the total number of shares that it would eventually have to issue upon conversion. Issuing convertibles alters its capital structure and dilutes the earnings of the existing shareholders. Options, by contrast, can be written in unlimited amounts, all the more so because the procedure of cash settlement no longer compels the option seller to actually deliver the underlying share.

# **Dynamics of Abstraction**

It is important to emphasize the difference between convertible securities and options, if only for the reason that the first are of earthly nature (they tend to remain and "deposit"), whereas the latter are volatile (they tend to "evaporate"). This material difference has ramifications bordering on ethics. Indeed, options lend themselves easily to the logic, therefore to the charge, of betting and gambling. Not everybody is aware that the fathers of volatility arbitrage, Sheen Kassouf and Ed Thorp, first exercised their skills and "system" in the convertibles area, and not in options [7]. Options had been banned in the aftermath of the 1929 market crash, and it was not until the early 1970s that they regained some liquidity and Black and Scholes were able to study them in order to derive their formula. The Chicago Board Options Exchange played no little role, subsequently, in bringing options back in favor, truly resurrecting their markets. (The belief had caught on that the Black–Scholes–Merton (BSM) formula, and the option trading it involved, were not about speculation and gambling after all, but about *efficient pricing* [6].)

As a matter of fact, the BSM paradigm put all derivatives on an equal footing. It led to the mathematization of their valuation, thus leveling out all their genealogical or ethical differences. From the valuation perspective, everybody now viewed derivatives as *pure payoff structures*, that is to say, as cash flow events that were simply triggered by the price trajectory of the underlying. From then on, the only dynamics that mattered was the price dynamics of the underlying. Find the right stochastic process to model the underlying behavior, and all the derivative pricing problems will be solved. This was the beginning of the *quant* era: the heedless, unstoppable sophistication of valuation models and payoff structures.

This pricing paradigm treated convertible securities, and more specifically convertible bonds, no differently than equity options. The convertible bond was identified with a corporate bond, whose valuation posed no greater difficulty than the rest of fixed income, bundled with an equity option, whose valuation posed no greater difficulty than BSM, or so everybody thought. Owing to the American-styled conversion feature, the suggestion was to price the CB by dynamic programming techniques, for example, Cox's binomial tree (see Binomial Tree; American Options). The procedure is initialized with the terminal payoff condition: either convert into equity or have the principal redeemed. Rolling backward, the cash payments accruing from the fixed-income part are simply added in the nodes at coupon dates and they become an integral part of the value of the CB. The procedure keeps comparing this value to conversion value, as it progresses to the present date, in order to check for early conversion [5, 9].

Credit risk started posing a problem though, when it was observed that the convertible bond had effectively a shorter maturity than the advertised one due to the probability of early conversion. How could the fixed-income component of the CB be valued using the same credit spread as the corporate bond of same official maturity? Is not the CB in effect less subject to credit risk than the pure bond because it is likely to wind up as equity, and this, "of course," bears no credit risk?

In terms of the pricing procedure, this is the question of the rate with which to discount the value of the CB in the tree. Should it be the riskfree rate (as in BSM), the risky rate (risk-free + credit spread), or a mixture of the two? Some have suggested using a weighted average of the two rates, depending on the probability of early conversion [4]. The delta of the CB would be the estimate of this probability. Others have proposed to split the CB into a credit-risky component and a riskless component (as the hybrid nature of the instrument naturally suggests) and the dynamic programming technique would now determine the splitting, because this obviously depends on the optimal conversion policy [8].

Ultimately, the right approach was to abandon the whole idea of patching together two pricing paradigms that had nothing in common: BSM (with dynamic hedging and dynamic programming) and fixed income (with static discounting using credit spreads). Rather, credit risk should be brought to bear right at the heart of the dynamics, and the process of the underlying equity itself revised. The vague notion of credit risk was thus reduced to the definite, probabilistic occurrence of a *default event*.

Default risk was modeled through a Poisson process superimposed on the traditional BSM diffusion. Its intensity, or hazard rate, measured the instantaneous probability of default, conditionally on default not having occurred earlier. The Poisson process triggers a massive jump both in the underlying equity price and in the derivative price. Typically, the convertible bond would jump to its recovery value, modeled as a fraction of the claim at the time of default. All equity and credit derivatives could now be valued in this reduced-form, unified framework. To that end, the dynamic hedging argument of BSM had to be generalized to cover the jump to default. A second, credit-sensitive, hedging instrument would thus be needed on top of the underlying. There was no need to split the CB any longer, as the insertion of the hazard rate in the pricing equation, combined with the explicit expression of the fate of the CB after default (recovery), mechanically determined the "rate" with which to discount values in the tree or in the PDE (see Partial Differential Equations) [2, 3].

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r + \lambda) S \frac{\partial V}{\partial S}$$
  
=  $r V + \lambda (V - R \operatorname{claim}(t))$  (7)

where  $\sigma$  is the diffusion coefficient,  $\lambda$  is the hazard rate,  $r$  is the risk-free interest rate, and  $R$  is the recovery ratio.

# The Equity–Credit Problem

This revision of the underlying dynamics set up the stage for the *equity-to-credit problem*. As the hazard rate was now recognized as the second factor alongside the diffusion coefficient, it could potentially be made stochastic and correlated with the process of the underlying  $[1]$ .

Equity-to-credit, or rather, credit-to-equity dynamics is the real dynamics ruling the CB. Conversion is *but a movement from credit to equity.* Debt, passively binding creditor and debtor, is converted into activity, project, enterprise, participation in the upside (see **Equity-Credit Problem**). Recall that conversion is an altogether more consequential transmutation than just exercising a right. The entire convertible can be reread in the light of this difference. The owner of a convertible security is more involved in the company than the buyer of an option. As such, he/she has to be protected. Dividend protection, takeover protection, call protection, and so on, are among the many clauses that make for the increasingly thicker CB prospectuses nowadays. Dividend protection dates

back to the warrants that Thorp and Kassouf used to trade. It protects the holder of the convertible security against the fall of the underlying share following dividend announcements, by readjustment of the conversion ratio or by a "pass-through" procedure. Takeover protection entitles the holder to sell back the convertible (takeover put) or to convert it against a greater number of shares than initially promised (ratchet clause), when a change of control or takeover is announced. Alternatively, the conversion ratio can be adjusted in proportion with the ratio of the price of the share of the company taking over and of the company being taken over.

As for the events that may trigger a change in the CB structure (early conversion by the holder, early redemption by the issuer, reset of the conversion price in case of resettable CBs, etc.), there is not one of them that is not "slowed down" and "mashed down" by a host of averaging clauses (as if the convertible had truly to *digest* the event). Only if the underlying trades 20 days out of 30 above a certain trigger level is the issuer entitled to call back the bond (soft call), or is the holder entitled to convert it (contingent conversion); the conversion price is reset at the average of closing prices of the underlying over a certain number of days before the reset date, etc.

From the point of view of holders of options (as opposed to convertible securities), all that matters is the price process of the underlying equity, which screens off all the deeper corporate changes. Dividend announcements, takeover announcements, and so on, are among many factors that may otherwise affect the price of the underlying, so why would option holders regard them any differently than the rest of price shocks and jumps that they prepare to face anyway? In their view, events are incorporeal and are only expressed in terms of underlying price changes: barriers and triggers may very well be breached punctually and without averaging clauses, so long as everybody agrees.

Holders of convertible securities, by contrast, are the *patient* readers of grave and significant corporate events, and the convertible is the book that binds and encodes those events.

# **References**

- [1] Ayache, E. (2004). The equity-to-credit problem, in *The Best of Wilmott 1, Incorporating the Quantitative Finance Review, 2004*, P. Wilmott, ed., John Wiley & Sons, Ltd, Chichester, West Sussex, pp. 79–107.
- [2] Ayache, E., Forsyth, P.A. & Vetzal, K.R. (2002). Next generation models for convertible bonds with credit risk, *Wilmott Magazine* December, 68–77.
- [3] Ayache, E., Forsyth, P.A. & Vetzal, K.R. (2003). The valuation of convertible bonds with credit risk, *Journal of Derivatives* **11**, 9–29.
- [4] Goldman Sachs (1994). Valuing convertible bonds as derivatives, in *Quantitative Strategies Research Notes*, Goldman Sachs.
- [5] Hull, J. (2008). *Options, Futures, and other Derivatives*, 7th edition, Prentice-Hall, Englewood Cliffs, New Jersey.
- [6] MacKenzie, D. (2003). An equation and its worlds: bricolage, exemplars, disunity and performativity in financial economics, *Social Studies of Science* **33**, 831–868.
- [7] Thorp, E.O. & Kassouf, S.T. (1967). *Beat the Market*, Random House, New York.
- [8] Tsiveriotis, K. & Fernandes, C. (1998). Valuing convertible bonds with credit risk, *Journal of Fixed Income* **8**, 95–102.
- [9] Wilmott, P. (2006). *Paul Wilmott on Quantitative Finance*, 2nd edition, John Wiley & Sons, London.

# E´ LIE AYACHE
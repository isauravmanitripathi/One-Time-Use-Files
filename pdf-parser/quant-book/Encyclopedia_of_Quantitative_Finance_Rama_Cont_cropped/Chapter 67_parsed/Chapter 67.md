# **Arbitrage Strategy**

It is difficult to imagine a normative condition that is more widely accepted and unquestionable in the minds of anyone involved in the field of quantitative finance other than the *absence of arbitrage opportunities* in a financial market. Put plainly, an *arbitrage strategy* allows a financial agent to make certain profit out of nothing, that is, out of zero initial investment. This has to be disallowed on economic basis if the market is in equilibrium state, as opportunities for riskless profit would result in an instantaneous movement of prices of certain financial instruments.

Let us give an illustrative example of an arbitrage strategy in the foreign exchange market, commonly called the *triangular arbitrage*. Suppose that Mary, in Paris, is buying<sup>a</sup> the US dollar for ¤0*.*685. Tom, in San Francisco, is buying Japanese yen for \$0*.*009419. Finally, Toru, in Tokyo, is buying one euro for ¥155*.*02. All these transactions are supposed to be able to occur at the *same time*. There is something worth noting in the situation just described—something that could allow you to make riskless profit. Let us see how. You borrow \$10 000 from your rich aunt Clara and tell her you will return the money in a matter of minutes. First, you approach Mary and change all your dollars to euros. This means that you will get ¤6850. With the euros in hand, you contact Toru and change them into yen—you will get ¥*(*6850 × 155*.*02*)* = ¥1 061 887. Finally, you call Tom, wire him all your yen and change them back to dollars, which gets you \$*(*1 061 887 × 0*.*009419*)* ≡ \$10 001*.*91. You give the \$10 000 back to your aunt Clara as promised, and you have managed to create \$1*.*91 out of thin air.

Although the above-mentioned example is oversimplistic, it gives a clear idea of what arbitrage is: a position on a combination of assets that requires zero initial capital and results in a profit with *no* risk involved. Let us now take a step further and see what will happen under the situation of the preceding example. As more and more investors become aware of the discrepancy between prices, they will all try to use the same smart strategy that you used for their benefit. Everyone will be trying to exchange US dollars for euros in the first step of the arbitrage, which will drive Mary to start buying the US dollar for less than ¤0*.*685 because of the high demand for the euros she is selling. Similarly, Tom will start buying Japanese yen for less than \$0*.*009419 and Toru will be buying euro for less than ¥155*.*02. Very soon, the situation will be such that nobody is able to make a riskless profit anymore.

The economic rationale behind asking for nonexistence of arbitrage opportunities is based exactly on the discussion in the previous paragraph. If arbitrage opportunities were present in the market, a multitude of investors would try to take advantage of them simultaneously. Therefore, there would be an almost instantaneous move of the prices of certain financial instruments as a response to a supply–demand imbalance. This price movement will continue until any opportunity for riskless profit is no longer available.

It is important to note that the preceding, somewhat theoretical, discussion does *not* imply that arbitrage opportunities *never* exist in practice. On the contrary, it has been observed that opportunities for some, albeit usually minuscule, riskless profit appear frequently as a consequence of the huge amount of distant geographic trading locations, as well as a result of the numerous financial products that have sprung up and are sometimes interrelated in complicated ways. Realizing that such opportunities exist is a matter of rapid access to information that a certain group of investors, so-called *arbitrageurs*, has. It is rather the *existence* of arbitrageurs acting in financial markets that ensures that when arbitrage opportunities exist, they will be fleeting.

The principle of not allowing for arbitrage opportunities in financial markets has far-reaching consequences and has immensely boosted research in quantitative finance. The ground-breaking papers of Black (*see* **Black, Fischer**) and Scholes [1] and Merton (*see* **Merton, Robert C.**) [3], published in 1973, were the first instances explaining how absence of arbitrage opportunities leads to rational pricing and hedging formulas for European-style options in a geometric Brownian motion financial model.b This idea was consequently taken up and generalized by many authors and has lead to a profound understanding of the interplay between the economics of financial markets and the mathematics of stochastic processes, with deep-reaching results *see* **Fundamental Theorem of Asset Pricing**; **Riskneutral Pricing**; **Equivalent Martingale Measures**; and **Free Lunch** for some amazing developments on this path.

We close the discussion of arbitrages on an amusing note. Such is the firm belief on the principle of not allowing for arbitrage opportunities in financial modeling that even jokes have been created in order to substantiate it further. We quote directly from Chapter 1 of [2], which can be used as an excellent introduction to arbitrage theory: *A professor working in Mathematical Finance and a normal*<sup>c</sup> *person go on a walk and the normal person sees a* ¤*100 bill lying on the street. When the normal person wants to pick it up, the professor says: "Don't try to do that. It is absolutely impossible that there is a* ¤*100 bill lying on the street. Indeed, if it were lying on the street, somebody else would have picked it up before you."*

## **End Notes**

a*.* All the prices referred to in this example are *bid* prices of the currencies involved.

b*.* For historical perspectives regarding option pricing and hedging, *see* **Black, Fischer**; **Merton, Robert C.**; **Arbitrage: Historical Perspectives**; and **Option Pricing Theory: Historical Perspectives**. For a more thorough quantitative treatment, *see* **Risk-neutral Pricing**.

c*.* Is this bold distancing from normality of mathematical finance professors, clearly implied from the authors of [2], a decisive step toward illuminating the perception they have of their own personalities? Or is it just a gimmick used to add another humorous ingredient to the joke? The answer is left for the reader to determine.

## **References**

- [1] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *The Journal of Political Economy* **81**, 637–654.
- [2] Delbaen, F. & Schachermayer, W. (2006). *The Mathematics of Arbitrage*, *Springer Finance*, Springer-Verlag, Berlin.
- [3] Merton, R.C. (1973). Theory of rational option pricing, *Bell Journal of Economics and Management Science* **4**, 141–183.

## **Further Reading**

- Dalang, R.C., Morton, A. & Willinger, W. (1990). Equivalent martingale measures and no-arbitrage in stochastic securities market models, *Stochastics and Stochastics Reports* **29**, 185–201.
- Delbaen, F. (1992). Representing martingale measures when asset prices are continuous and bounded, *Mathematical Finance* **2**, 107–130.
- Delbaen, F. & Schachermayer, W. (1994). A general version of the fundamental theorem of asset pricing, *Mathematische Annalen* **300**, 463–520.
- Delbaen, F. & Schachermayer, W. (1998). The fundamental theorem of asset pricing for unbounded stochastic processes, *Mathematische Annalen* **312**, 215–250.
- Elworthy, K.D., Li, X.-M. & Yor, M. (1999). The importance of strictly local martingales; applications to radial Ornstein-Uhlenbeck processes, *Probability Theory and Related Fields* **115**, 325–355.
- Follmer, H. & Schied, A. (2004). ¨ *Stochastic Finance*, *de Gruyter Studies in Mathematics*, extended Edition, Walter de Gruyter & Co., Berlin, Vol. 27.
- Hull, J.C. (2008). *Options, Futures, and Other Derivatives*, 7th Edition, Prentice Hall.
- Michael Harrison, J. & Kreps, D.M. (1979). Martingales and arbitrage in multiperiod securities markets, *Journal of Economic Theory* **20**, 381–408.
- Michael Harrison, J. & Pliska, S.R. (1981). Martingales and stochastic integrals in the theory of continuous trading, *Stochastic Processes and Their Applications* **11**, 215–260.
- Shreve, S.E. (2004). *Stochastic Calculus for Finance. I: The Binomial Asset Pricing Model*, *Springer Finance*, Springer-Verlag, New York.

## **Related Articles**

**Black, Fischer**; **Equivalent Martingale Measures**; **Fundamental Theorem of Asset Pricing**; **Free Lunch**; **Good-deal Bounds**; **Merton, Robert C.**; **Ross, Stephen**; **Risk-neutral Pricing**.

CONSTANTINOS KARDARAS
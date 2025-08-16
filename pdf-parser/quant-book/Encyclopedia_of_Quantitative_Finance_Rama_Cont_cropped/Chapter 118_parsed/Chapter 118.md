## **Stock Pinning**

Stock pinning, or simply *pinning*, is formally the occurrence of a closing stock print, on option expiration day, which exactly matches the denominated value of a strike price. As an example, let stock XYZ have strikes 30, 32.5, 35, and 40. If on Friday, May 16, 2008 at 4:00 pm EDT (USA), the third Friday of the month and thus an expiration day for listed options, the closing print of XYZ is \$35, then stock XYZ is said *to pin*. Prices of \$34.27, \$31.60, or even \$32.48, are said not to have pinned. Figure 1 is a tick price graph of KO (Coca Cola Corporation) showing the last several days prior to a pinning expiration.

As a practical matter, it may be useful experimentally to consider pinning to have occurred if the stock expires within a certain interval of a strike price. There are several reasons for this looser definition. Empirically there may be several "closing prints"

![](_page_0_Figure_4.jpeg)

**Figure 1** KO (Coca Cola) tick data for a pinning expiration, October 17, 2003

![](_page_0_Figure_6.jpeg)

**Figure 2** All optionable stocks in 2002 divided into quartiles by pinning strength, *β*. As predicted, the probability of pinning increases with beta. (Pinning criteria \$0.15, courtesy Bart Rothwell)

![](_page_1_Figure_1.jpeg)

**Figure 3** Cumulative distribution function of pinning of stocks, which are within \$1 of a strike with 1 week to go to expiration as a function of the parameter, *β*. (Courtesy Tom MacFarland)

![](_page_1_Figure_3.jpeg)

**Figure 4** The percentage of days KO closed within \$0.15 of a strike in a 10-year period January 1, 1996 to January 1, 2005. 0 is expiration day, negative integers are days prior to expiration, positive integers are days following expiration. (Courtesy Bart Rothwell)

making a choice of the closing price arbitrary. Tick data shows that a stock may be effectively *pinned* over the last several minutes before expiration but then have a closing print just off the strike. In the first example, this might happen if the last quote were \$34.98 bid, at \$35.01, and the closing price stayed in the interval but was not precisely \$35.

Two additional reasons for a looser definition are the automatic exercise conditions mandated by the OCC (Options Clearing Corporation) and the consequent *pin risk*, which attends expiring short positions on the (nearly) pinned strike. The OCC has traditionally fixed an interval about a strike outside of which in-the-money puts and calls would be automatically exercised by the clearing process; options within the interval would require *exercise notice* by the holder. Over time, the OCC has reduced the interval to the current \$0.01 (from \$0.05 before June 2008 expiration); traders will declare a stock to have pinned if it falls within the OCC interval. Pin risk attends to any short position inside this interval because an uncertain number of options may be assigned and thus an uncertain postexpiration stock position exists in the positions of those short the expiring at-the-money options.a

![](_page_2_Figure_1.jpeg)

**Figure 5** All stocks, January 1996 to September 2002 [Reproduced with permission from Stock price clustering on option expiration dates, Ni *et al.*, Journal of Financial Econometrics, Elsevier 2005.]

![](_page_2_Figure_3.jpeg)

**Figure 6** Nonoptionable stocks do not pin, January 1996 to September 2002 [Reproduced with permission from Stock price clustering on option expiration dates, Ni *et al.*, Journal of Financial Econometrics, Elsevier 2005.]

So far we have defined a single instance of pinning. Complementing the notion of an individual instance of stock pinning is an ensemble assertion of stock pinning. In this perspective, a stock, or stocks, is said to pin if, no matter how small an interval one chooses about a strike price, there

![](_page_3_Figure_1.jpeg)

**Figure 7** All optionable stocks, January 1996 to September 2002. (Pinning criterion \$0.125): pinning when professional traders are (a) long and (b) short the expiring at-the-money strike

is a finite probability of finding closing prints within the interval. To compute this limit, expressed mathematically as

$$\lim_{\varepsilon \to 0} P(|S-K| \le \varepsilon) > 0 \tag{1}$$

where *ε* is an interval about (any) strike *K*, *S* is the stock price at expiry, and *P* is the probability among all expiration closes, one can do empirical experiments or theoretical calculations. It is important to note that standard models of option pricing such as Black–Scholes, Heston, SABR, and stochastic volatility models, in general, cannot exhibit pinning mathematically.

Although traders had long believed pinning to be a real phenomenon, little theoretical or experimental effort was made to examine the subject through the 1990s. Krishnan and Nelkin [3] looked at the data set of MSFT (Microsoft Corporation) expirations and found evidence of pinning. They proposed a model that combined a Gaussian random walk with a Brownian bridge process in order to force pinning to a strike. The model *perforce* guaranteed pinning, but suffered from many obvious weaknesses: stocks do not always pin; they can pin at many possible strikes; and the choice of the amount of Brownian bridge component was exogenously (and arbitrarily) imposed.

Then Avellaneda and Lipkin [1], and nearly simultaneously, Ni *et al.* [4], produced theoretical and experimental arguments for pinning. In the former work, Avellaneda and Lipkin proposed an asymmetric hedging strategy for professional traders—aggressive hedging of long gamma positions and weak hedging of short gamma positions. This hedging strategy coupled with a stock impact function (simplistically assumed to be linearb) led directly to pinning (with nonzero probability), which depended naturally and endogenously on the option open interest, the intrinsic stock volatility, the (logarithmic) distance to the strike and the time to expiration. In dimensionless form, the *strength parameter*, *β*, is proportional to the open interest and inversely proportional to the volatility. Figures 2 and 3 show, experimentally, the monotonic growth of pinning probability with *β*.

Ni *et al.* used the IVY and CBOE databases to check pinning frequencies. Figures 4 and 5, typical Ni *et al.* graphs, indicate the excess clustering of stock prices near a strike on expiration days for KO and for the entire market over extended periods. Figure 6 demonstrates the absence of pinning in nonoptionable stocks. Finally, Ni *et al.* lent support for the hedging assumptions of Avellaneda and Lipkin. Figure 7(a,b) shows the difference between pinning when professional traders are long (a) and short (b) the expiring at-the-money strike.

Since 2004, other research groups, for example, Jeannin, *et al.* [2], have continued to explore the details of pinning.

## **End Notes**

a*.* Practitioners define *pin risk* as the uncertain deltas which an otherwise balanced position might have postexpiration due to the assignment of calls or puts on a near pinning strike. For example, a position long 50 calls and short 50 puts on the \$25 strike, for a stock which expires near \$25, may be assigned from 0 to 5000 shares of stock due to the uncertain number of puts which may have been exercised. This amount of stock thus assigned is independent of the number of calls the trader chooses to exercise himself.

b*.* Following the initial 2003 work, Gennady Kasyan (with Avellaneda and Lipkin, unpublished) showed that any impact function stronger than square-root would result in pinning. This suggests that weaker impact functions may be contradicted by the extensive market evidence of stock pinning.

## **References**

- [1] Avellaneda, M. & Lipkin, M.D. (2003). A market-induced mechanism for stock pinning, *Quantitative Finance* **3**, 417–425.
- [2] Jeannin, M., Iori, G. & Samuel, D. (2008). The pinning effect: theory and a simulated microstructure model, *Quantitative Finance* **8**, 823–831.
- [3] Krishnan, H. & Nelken, I. (2001). The effect of stock pinning upon option prices, *Risk* December.
- [4] Ni S, Pearson N., Poteshman A. (2004). Stock price clustering on option expiration dates, *SSRN* August 27.

## **Related Articles**

**Price Impact**.

MIKE LIPKIN
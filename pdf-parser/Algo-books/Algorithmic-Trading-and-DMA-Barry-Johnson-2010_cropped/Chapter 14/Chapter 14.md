![](_page_0_Picture_1.jpeg)

Multi-asset trading is nothing new; however, trading between different asset classes poses a whole new set of issues for trading algorithms.

### 13.1 Introduction

Multi-asset trading is starting to attract nearly as much hype as algorithmic trading. In its simplest form, it means single systems that allow investors and traders to manage trading across multiple asset classes. Though, in terms of algorithmic trading the most interesting prospect is cross-asset trading. This offers the potential of simultaneously trading a wide variety of different asset types using a single trading strategy.

Historically, the world markets have been highly segmented, both regionally and across asset classes. Electronic trading has helped open up markets, allowing a much broader range of access. Trading any asset globally is rapidly becoming a straightforward technical issue. Increasing numbers of order (OMS) and execution management systems (EMS) now provide unified platforms that enable trading across a range of asset classes. Similarly, communications protocols such as FIX have expanded to cater for equities, bonds, FX and an array of derivatives.

Hedge funds are arguably the principal driver behind the current trend towards multi-asset trading. Their strategies are becoming increasingly complex as they constantly seek new sources of profit, or alpha. Risk management has also become progressively more sophisticated in its use of derivatives for hedging. Consequently, the overall buy-side use of derivatives has spiralled over the last few years, leading to increased demand for multi-asset support.

The sell-side has had to evolve to cope with a new era of lower margins and higher volumes. Many firms have started reorganizing themselves; the old asset class silos are disappearing. Equities and derivatives businesses are merging, in some cases even fixed income and equities desks are integrating. Sales desks are becoming more customerfocussed, able to cater for trading a wide range of assets. The aim is to try to achieve greater efficiencies of scale and so reduce the overall costs. Cross-asset trading strategies also offer them a significant means of differentiation, as well as the benefits associated with being firstto-market.

Competition amongst execution venues is also helping. As we saw in Chapter 3, the competition is now truly global and has even started to span across asset classes. Exchanges are increasingly catering for equities, derivatives and even fixed income trading. For example, both NYSE and NASDAQ have expanded to offer trading in ETFs, futures and options. The NYSE has even relaunched its bond-trading platform. Many of the European and stock exchanges also handle bonds, whilst some of the Nordic exchanges also cater for derivatives. In Asia, Australia, Korea and Singapore have all seen mergers between their stock and derivatives exchanges. Likewise, the major derivatives exchanges have started branching out into other asset classes as well. For instance, Eurex also caters for bond trading whilst the ISE has created its own stock market. Competition is also increasing between the "dark pool" ATSs. Indeed, if some of the newer ATS entrants in FX and options prove successful, we may see mergers and takeovers in this arena as well.

Regulations will also play an important part in the expansion of multi-asset trading. In Europe, MiFID means that regulations now span across a broad section of asset classes, which should help clear the way for cross-asset trading. Though, in the U.S. the disparate regulatory bodies mean that it may be more complicated, as evidenced with difficulties over newer assets such as ETFs and single stock futures.

Another factor that will be crucial to the growth of multi-asset trading is the provision of unified mechanisms for clearing and settlement. Prime brokerage services will need to expand across the various asset classes. Netting agreements for collateralization and margin requirements will also have to encompass a much wider range of assets.

Although the divisions between the world's markets are becoming increasingly blurred, the exact outcome of all this change is still uncertain. At present, very few execution venues actually provide cross-asset trading. Some of the reasons for this are highlighted in an article by Ivy Schmerken (2006): Many exchanges still run separate platforms and matching engines for each asset class, some may have half a dozen different systems. Whilst there may he interest, the demand has still not been sufficient to justify the expense of merging these systems. That said, as exchanges migrate to new platforms support for multiple asset classes is becoming a key consideration. Another important factor is that whilst linked orders may he convenient, such "one-stop shopping" runs counter to broker's best-execution obligations. In the short-term, many of the cross-asset trading solutions are likely to be from brokers and other third-parties. Complex orders can easily be split into multiple legs and routed to different venues. Reduced latencies have also helped to reduce the legging risk for such strategies. Hence, it is likely that for the foreseeable future much of the innovation in crossasset trading will be provided by specialised algorithms/platforms as brokers seek to continue to differentiate themselves with new value-added services.

### 13.2 Multi-asset trading strategies

Despite all the hype, cross-asset trading is nothing new. Cash positions in stock, bonds and commodities have been hedged with futures and options ever since the creation of derivative contracts. The ability to protect against a broad spectrum of risks has made derivatives a virtually indispensable tool. Cross-asset arbitrage is nothing new, either. In particular, index arbitrage and basis trading have been around for decades. Though, the high cost of entry has meant that historically such arbitrage has been monopolised by market makers, dealers and proprietary traders. More recently, electronic trading has helped lower the cost of entry. Easier access and decreasing transaction costs have made cross-asset trading viable for a much wider range of investors and traders. On the downside, it has also substantially reduced the timescales; many opportunities might now only last minutes, seconds or even less.

Ten years ago, the precursors of modern trading algorithms were efficiency tools, helping traders cope with the ever-increasing order flow. Finally, they were packaged up into discrete strategies and made available to clients as trading algorithms. Dealers' hedging and arbitrage systems arguably contain a lot more proprietary techniques. However, there is no real reason why the more established ones could not undergo a similar transformation. In fact, several broker dealers have already started releasing algorithms that provide hedging and other types of cross-asset trading. Similarly, hedge funds and other investment institutions have begun creating their own dedicated algorithms, to protect their own proprietary techniques. Vendors have already started to provide platforms geared up for this, for example, Flextrade, Progress Apama and AlgoTrader's OptimEx.

Unlike for existing trading algorithms, it is slightly more difficult to predict exactly what future multi-asset algorithms might look like. Broadly speaking, we can use some of the existing types of trading as a basis, as outlined in Table 13-1:

| Strategy type | Examples                      | Assets involved |                     |
|---------------|-------------------------------|-----------------|---------------------|
| Utility       | FX eash trades                | Stock           | FX                  |
|               | Covering short sales          | Stock           | Stock Lend/Rev repo |
| Structured    | Principal protected notes     | Bond            | Option              |
|               | Hedging market risk           | Stock/s         | Future/s            |
| Hedging       | Hedging interest rates        | Bond/s          | Future/s            |
|               | Hedging the "Greeks"          | Option/s        | Stoek/s             |
|               | ADR arbitrage                 | $\text{DR}$     | Stock               |
|               | Basis trading                 | Future/s        | Bond/s              |
|               | Index arbitrage               | Future/s        | Stocks              |
| Arbitrage     | Option arbitrage              | Options         | Stocks/Bonds        |
|               | Futures and options arbitrage | Options         | Future/s            |
|               | Dividend arbitrage            | Stock           | Option/s            |

### Table 13-1 Some examples of cross-asset trading types

The utility strategies are relatively straightforward additions, such as incorporating FX cash trades with stock trading in order to facilitate cross currency trading or covering short sales using stock lending or reverse repos.

Structured products are combinations of cash and derivative assets designed to meet specific investment objectives, such as enhancing returns or reducing risk. The more straightforward products, such as principal protected notes, may well form the basis for some multi-asset trading strategies.

Likewise, hedging provides a mechanism for offsetting risk, generally via derivatives. Although this is often simply applied to existing positions, hedging may also be used in tandem with normal trading, such as for portfolio transitions. Hedging also forms the backbone of many of the arbitrage techniques that seek to extract risk-free profits when price imbalances occur.

Note that a reasonable grasp of derivatives is important for many of these trading strategies. So if you are new to these instruments, it may be worth rereading the corresponding parts of Chapter 3 and Appendix E. Alternatively, for a more detailed review 'Understanding Futures Markets' by Robert Kolb and James Overdahl (2006) or 'Options, Futures, and Other Derivatives' by John Hull (2003) are both good starting points.

In the following sections, we shall look at each of these various strategy types before reviewing some of the key considerations for multi-asset trading algorithms.

# 13.3 Utility strategies

These are simple extensions of procedures, which are routinely carried out manually. For example, when trading assets denominated in foreign currencies we could automate the FX cash trades. Automatic handling could also cover short sales, by finding lending or reverse repos to borrow the required asset. As volumes continue to increase and traders get busier the market for such conveniences may well expand.

### FX cash trades

When trading pairs or portfolios of assets with multiple currencies the exchange rates are an important consideration. Admittedly, settlement currencies may often be specified; however, any changes in the exchange rate could mean settling at a disadvantageous rate. Therefore, when trading assets denominated in a different currency it may be appropriate to also perform an FX cash trade, to ensure there is a sufficient amount of local currency for settlement.

Trading systems may be extended to issue FX cash trades to match the value traded. Depending on the value and the volatility of the currency, this could be carried out automatically upon completion of the order. Alternatively, the currency could be traded in parallel with the order. Existing trading algorithms could be extended to incorporate currency handling, or it could be done manually using DMA. The client may also want to perform this across multiple assets, so a net currency position could be traded. This might be handled by the broker or, if execution information is sent back to the client in real-time, they could take charge of this for themselves.

For example, let's consider a pairs trade between the pharmaceutical firms Genentech (U.S.) and GlaxoSmithKline (U.K.) for \$10 million. The ratio algorithm will steadily build positions in the two companies. To ensure our U.K. sterling cash account is sufficient for settlement the algorithm could also incrementally issue FX cash orders for sterling based on the current size of our GlaxoSmithKline position. This might simply mean issuing limit orders; alternatively, a separate algorithm could be used to handle the FX trading.

### Covering short sales

To sell short most cash assets we will usually need to cover the position by borrowing the asset, either via stock lending or reverse repos. As the markets for stock lending and repos become increasingly electronic this also opens up the possibility of automating short covering. Hence, an algorithm could scan the lending and/or repo markets to source the required asset. Since it may be more difficult to borrow the asset, the short sale could even be made dependent on the success of this transaction. It could even take account of the cost of borrowing when placing the short sell orders to ensure the fees are covered.

## **13.4 Structured strategies**

Structured products are synthetic assets created to meet specific investment requirements, such as enhancing the yield, increasing tax efficiency or reducing risk for a given asset. Financial engineering is used to determine the required combinations of cash and derivative assets to meet these objectives.

Structured products have primarily been targeted at retail investors, although usage by institutional investors is also growing. Over \$100 billion of new issues were made in 2007 according to estimates from the Structured Products Association (SPA) (2008). <sup>1</sup> Indeed, their increasing popularity means they are starting to emerge as a separate asset class. Note that they are principally designed to be kept to maturity, so this is an OTC only marketplace with little or no secondary trading.

Although structured products may be highly complex and tailored to the needs of a specific investor, there are also some increasingly common variants such as structured notes, as Chris Biscoc (2005) points out. Trading algorithms may well evolve which approximate to some of the more common or straightforward products.

#### Principal protected notes

Principal protected notes offer a guarantee to return a set percentage (usually 100%) of the amount invested at maturity. As well as this, they also offer the potential of additional returns, derived from the performance of other asset/s. Note that a participation rate may be set on the enhanced returns, so the investor might receive 70 or 80% of them.

Equity linked notes are effectively debt instruments combined with an option on a specific stock or index. They do not usually have any coupon payments; instead the returns at maturity are based on the gains of the underlying equity. The investment amount is protected to maturity, although it is still exposed to issuer default risk.

Interest rate linked notes are based on the moves for market benchmark rates, such as Fed Funds or LIBOR. Range accrual notes only accrue interest on days when the reference rate is within a set range.

Currency (or FX) linked notes augment their returns from the performance of a currency, or basket of currencies. There are also range accrual notes where interest is accrued only on days when the currency is within set bounds.

Hybrid linked notes even allow the performance to depend on multiple asset classes.

Many of these structured notes have a maturity of between 1-3 years. The basic principle behind them is to invest in risk-free bonds which provide the protection. For instance, zero coupon bonds may be bought at a discount to achieve this. The remaining funds may be used to purchase derivatives to enhance the returns. This might be purchasing long-term call options for the required stock, currency or commodity. Alternatively, some structures may incorporate more exotic derivatives, such as barrier options.

As an example we might construct a \$1 million two year principal protected note by purchasing two year zero coupon Treasury notes with a notional of \$1 million. These are priced at 90, leaving \$100,000 to purchase two-year call options to provide the enhanced returns. A customised trading algorithm could be used to link these two orders together.

# 13.5 Hedging strategies

Hedging is simply a mechanism for offsetting risk. Since positions may be constantly exposed to market risk, hedging is effectively a continual cycle comprising of the following three stages:

- analysing the various risks for existing positions
- $\bullet$ determining what is required to counteract them
- issuing orders to achieve the target hedge positions

For cash assets, such as stocks or bonds, hedging often uses derivatives. Whilst for

<sup>&</sup>lt;sup>1</sup> Based on data from MTN-I, Prospect News and StructuredRetailProducts.com.

derivative positions the hedging may be based on the underlying assets, other derivatives or a combination of the two.

Transaction costs mean that it is not necessarily cost effective to constantly adjust the hedging positions. As always, it is a careful balancing act between risk and cost. That said, electronic trading has made it much more viable to perform hedging in real-time.

For existing positions, investment firms already maintain their own hedging, which may then he traded manually or via trading algorithms or DMA. For portfolio trades the brokers could also incorporate any required hedging, as we saw for FX cash trades. In Chapter 12, we saw that dedicated portfolio trading algorithms that incorporate portfolio risk are already available. Extending these to also handle hedging with derivatives is not that great a leap.

For example, consider an investment fund worth \$1 billion hedged with S&P 500 futures. A portfolio trade to increase the fund by 10% would need a corresponding increase in the futures cover. So in addition to the portfolio of stocks the broker could also trade the additional futures for the hedging. Alternatively, if the broker is supplying frequent status updates, the buy-side traders could manage the futures hedging themselves, although they may be disadvantaged by any delays.

In the following sub-sections, we shall outline some of the commoner types of hedging which might he incorporated into custom algorithms.

# **Hedging market risk**

Futures can provide a cost-efficient means of hedging market risk, particularly for portfolios. For stock portfolios, an index future allows us to offset market risk. The number of futures contracts required can be determined based on the overall beta of the portfolio  $(\beta_P)$ , using the following equation:

Number of Contracts = 
$$-\beta_P \frac{V_P}{V_F} = -\beta_P \frac{V_P}{P_F \cdot m}$$
 (13-1)

where  $V_P$  and  $V_F$  are the corresponding market values of the portfolio and of a futures contract. The futures value may also be expressed in terms of its price  $P_F$  and its contract multiplier  $m$ .

Remember that the actual beta of a portfolio for a specific index may be determined by comparing its returns with those of the index, as we saw in Chapter 12. The portfolio beta  $(\beta_P)$  may in turn be derived from its covariance:

$$\beta_p = \frac{Cov(r_p, r_m)}{Var(r_m)}$$

where  $r_p$  and  $r_m$  are the respective returns for the portfolio and the index.

**Example 13-1:** Let's assume we need to add \$5 million of S&P 500 stocks to our portfolio. To protect against a falling market we can sell an equivalent number of September futures contracts. For convenience, we will base this on their closing value  $(1,559.7)$  with a multiplier of \$250/point. Since this is a basket of S&P stocks, we shall assume the beta is  $1.0.$ 

Using equation  $13-1$ , we get:

Number of contracts =  $-$5,000,000 / ($250 * 1,559.7) = -12.82 \approx -13$ 

Therefore, selling 13 futures contracts should provide sufficient hedging for our portfolio. A month later, the S&P 500 fell from 1549.37 to 1445.94, whilst the futures price fell to 1449.9. Hence, the stock position sees a loss of nearly 7%, or \$333,780. Conversely, the value of the short futures hedge actually increased, due to the 109.8 drop in price. This equates to \$250 x 13 x  $(1559.7-1449.9) = $356,850.$ 

Table 13-2 summarises the market values at each date. Overall, the hedge worked: If we nceded to liquidate the portfolio in August, the losses realised from the stock sales would be more than compensated for by the gain from our futures.

| Date   | Position               | Market<br>Value/\$ | Net<br>Value/\$ |
|--------|------------------------|--------------------|-----------------|
| 16 Jul | Stock portfolio        | 5,000,000          |                 |
|        | $S&P 500 SEP$ futures  | -5,069,025         | -69,025         |
|        | Stock portfolio        | 4,666,219          |                 |
| 17 Aug | $S\&P$ 500 SEP futures | -4,712,175         | -45,956         |

Table 13-2 An example of short futures hedging

**Example 13-2:** Let's now consider shorting a \$5 million basket of stocks. Compared to the S&P 500 the basket has a beta of 1.5. To protect against a rising market we will need to buy more futures than before:

Number of contracts =  $-1.5 * 5,000,000 / ($250 * 1,559.7) = 19.23 \approx 19$ 

So in this case we need to huy 19 futures to hedge our short basket. The beta also means that the falling market will probably have even more effect on this portfolio. Indeed, by the 17<sup>th</sup> August it is only worth \$4,475,000. So if we were to buy back the stocks we could realise a profit of \$525,000. However, these potential profits will be reduced by losses from the futures hedge. The market values and the  $\beta$ -adjusted equivalents are shown in Table 13-3:

| Date   | Position                                  | Market<br>Value/\$      | <b>B</b> -adjusted<br>Market Value/\$ | Net<br>Value/\$ |
|--------|-------------------------------------------|-------------------------|---------------------------------------|-----------------|
| 16 Jul | Stock portfolio<br>$S&P 500 SEP$ futures  | -5,000,000<br>7,408,575 | -7,500,000<br>7,408,575               | 2,408,575       |
| 17 Aug | Stock portfolio<br>$S\&P$ 500 SEP futures | -4,475,000<br>6,887,025 | -6,712,500<br>6,887,025               | 2,412,025       |

### Table 13-3 An example of long futures hedging

The long futures position decreases in value by 250 x 19 x  $(1559.7-1449.9) = $521,550.$ Thus, the hedging prevented us from realising any significant directional profits. More importantly, though, it protected us from any losses due to a rising market.

For instance, let's consider if the S&P had actually risen to 1600, and the SEP future to 1605. Our short stock position would instead be worth \$5,250,000, effectively a loss of  $$250,000$ . This is offset by a gain of  $$215,175$  in the value of the futures position, as shown in Table 13-4. Although not perfect, this hedge has still provided an important insurance mechanism against market moves.

| Date   | Position                               | Market<br>Value/\$      | $\beta$ -adjusted<br>Market Value/\$ | Net<br>Value/\$ |
|--------|----------------------------------------|-------------------------|--------------------------------------|-----------------|
| 16 Jul | Stock portfolio<br>S&P 500 SEP futures | -5,000,000<br>7,408,575 | -7,500,000<br>7,408,575              | 2,408,575       |
| 17 Aug | Stock portfolio<br>S&P 500 SEP futures | -5,250,000<br>7,623,750 | -7,875,000<br>7,623,750              | 2,373,750       |

Table 13-4 An alternative scenario for long futures hedging

### Hedging interest rate risk

Fixed income assets are obviously affected by changes in interest rates. When market interest rates increase bond prices decrease, and vice versa. This is because the cash flows are fixed, so a higher interest rate reduces their present value.

For a standard bond we may represent its current value  $(V)$  as the sum of all its future cash flows  $(C_i)$  each discounted to their present value  $(P(i))$  based on the rate  $(r)$ :

$$V = \sum_{i} P(i) = \sum_{i} C_i e^{-r\Delta i}$$

where  $T_i$  is the time left to maturity for each payment (in years). Note the rate  $(r)$  is effectively the yield to maturity (YTM) of the bond. It represents the overall interest rate that would be earned by buying it at the current market price and holding to maturity.

**Example 13-3:** Let's consider a 2-year bond with an annual coupon of 5% for a notional value of \$100,000. It is priced such that its yield to maturity (YTM) is also 5%.

So at the end of the first year we receive a coupon of \$5,000, which has a current value of  $(5,000 \text{ *e}^{-0.05*1}) = $4,756.$ 

At the end of the second year, we receive both the final coupon payment and the full notional amount. This gives a total current value of \$99,764, shown in Table 13-5.

|         |        | $YTM=5.00\%$ |        |          | YTM=5.01% | YTM=4.99% |
|---------|--------|--------------|--------|----------|-----------|-----------|
| Time    | Cash   | Present      |        | Weighted | Present   | Present   |
| (vears) | flow   | value        | Weight | time     | value     | value     |
|         | 5,000  | 4.756        | 0.05   | 0.05     | 4,756     | 4,757     |
|         | 05,000 | 95,008       | 0.95   | 1.90     | 94.989    | 95,027    |
| Total   |        | 99,764       |        | 1.95     | 99,745    | 99,784    |

#### Table 13-5 Calculating value of a bond

Now let's consider the situation if interest rates increase by one basis point (bps). The bond's yield to market will also increase to 5.01%. The present value of the second year payment is now  $(105,000 * e^{-0.0501*2}) = $94,989$ , so the overall value of the bond decreases by \$19. Conversely, if rates decrease by one basis point the value increases to \$99,784, or \$20.

Thus, the average change in value for a 1 bps change in interest rates =  $(19+20/20)$  = \$19.5. This risk measure is sometimes referred to as the PVBP (price value of a basis point), whilst if measured in dollars it is called the  $DV01$  (dollar value of a basis point change).

Alternatively, we can use duration to represent the sensitivity of a bond to interest rate

movements. This is inversely related to the coupon rate, so higher rate bonds have shorter durations, whilst for zero coupon bonds the duration is equal to their maturity. The duration  $(D)$  may be expressed as the sum of the weighted maturities for the associated cash flows:

$$D = \sum_{i=1}^{n} \frac{P(i) \ T_i}{V}$$

For Example 13-3, the weight column in Table 13-5 is simply each present value divided by the total. Hence, the duration for the bond is  $1.95$  years when the yield to market is 5%.

These risk metrics may also be applied to portfolios of bonds, as a weighted sum based on the size of each bond's position. Hull (2003) shows that the number of interest rate futures  $(N)$  required to hedge this risk may be determined using the following equation:

$$N = -\frac{D_S \cdot S}{D_F \cdot F}$$

where  $D_S$  is the duration of the portfolio (or bond) and  $D_F$  is the duration of the underlying (cheapest to deliver) bond for the future. The value of the portfolio is  $S$  and the value of a future is F. Alternatively we can express this based on  $DV01$ :

$$N = -\frac{DV01_{bond}}{DV01_{future}} \times \frac{S}{F}$$
(13-2)

There are several ways to determine the  $DV01$  for a future, the easiest is to make an approximation based on the  $DV01$  of the most economical underlying asset, the "cheapest to deliver" (CTD). So the  $DV01_{future}$  is in turn based on the  $DV01$  of this CTD bond and a conversion factor  $(CF)$ .

$$DV01_{future} = -\frac{DV01_{CTD}}{CF}$$

**Example 13-4:** A bond portfolio worth \$10 million has a  $DV01$  of \$195. The current futures contract for a ten-year bond is priced at 94.20, with a notional of  $100,000$ .

Each futures contract is worth  $(94.2/100) \times $100,000 = $94,200$ .

At the future's maturity, the cheapest to deliver bond has a  $DV01$  of \$250.

For simplicity, let's assume the conversion factor is 1, so the  $DV01$  of our future is \$250.

Using equation 13-2:

$$\# contracts = -\frac{195}{250} \times \frac{\$10,000,000}{\$94,200} = -82.8$$

Therefore, by selling 83 futures contracts we should have hedged our bond portfolio. If interest rates increase, both the bond portfolio and the futures contracts will be worth less. The loss in value from the bond portfolio should be offset by profit from the short futures position. Conversely, a drop in interest rates will make the bond portfolio worth more, whilst the futures position will realise a loss.

There are some other important assumptions with this approach: Firstly, it relies on the cheapest to deliver bond not changing. Neither does it account for basis risk, the possibility that the spot price of the asset and the futures price do not converge, towards the expiration date. Basis trading is covered in more detail in section 13.6.

It is also important to remember that  $DV01$  applies to small changes in interest rates. Still, this is not a linear relationship. With large changes in rates more significant price changes may occur. This is due to a property called convexity: Bonds or portfolios with higher convexity will see higher increases in value as rates decline than those with lower convexity. To compensate for this it is possible to adjust the hedge calculation to also incorporate convexity.

Finally, there is no guarantee that interest rate changes will apply uniformly across the yield curve. If this does not happen, the portfolio will be exposed to different risks depending on the maturity. This may be handled by identifying these "gaps" and adding extra hedging for them. More details about all these considerations may be found in Hull (2003).

#### Hedging derivative risk factors (the "Greeks")

Hedging derivatives requires us to fully understand their sensitivities to the price of the underlying asset as well as factors such as interest rates. There are many different pricing models for derivatives; however, the Black Scholes (1973) is easily the best known:

A call option's price  $(C)$  may be defined as a function of the price of its underlying asset  $(S)$  and the time left to expiry  $(T)$ :

$$C(S,T) = S\Phi(d_1) - Ke^{-rT}\Phi(d_2) \tag{13-3}$$

where K is the option's strike price, r is the interest rate and  $\Phi$  is the standard normal cumulative distribution function. The first component  $(S \Phi(d_i))$  corresponds to a probability weighted estimate of the asset price at expiration, whilst the second  $(Ke^{rT}\Phi(d_2))$  represents a discounted exercise price. In turn, the factors  $d_1$  and  $d_2$  are defined by:

$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \qquad d_2 = d_1 - \sigma\sqrt{T} \tag{13-4}$$

where  $\sigma$  is the asset's price volatility. The option price is sensitive to all of these key parameters, each of which has been assigned its name based on the name for their mathematical symbol. Since most of these are Greek, they became known as the "Greeks".

Delta represents the rate of change in value with respect to the underlying price. Rho measures the sensitivity to changes in the interest rate. Vega reflects the impact of changes in volatility and theta corresponds to the effect of time on the derivative's value. Gamma is a secondary risk factor, rather than directly mapping to one of the parameters in equations 13-3 or 13-4 it measures the rate of change in delta based on changes in the underlying price.

Since the focus of this chapter is cross-asset trading, we will concentrate on the hedges targeting risk from changes the underlying price, namely delta and gamma.

#### Delta Hedging

Delta hedging balances some of the risk from an option position by buying or selling a set amount of the underlying asset. This protects against price moves in the underlying.

The value of delta ranges between  $-1.0$  and  $1.0$ . A delta of  $1.0$  means that for every rise (fall) of \$1 in the underlying asset the derivative's price will also rise (fall) by \$1. Conversely, a negative delta means that the derivative's price moves in the opposite direction. So a delta equal to  $-0.5$  means that a price increase of \$1 for the underlying asset will result in a price drop of  $0.5$  for the derivative.

Using the Black Scholes model, equation 13-3, the delta for a call option is actually equal to the weighting  $\Phi(d_I)$ , so these have deltas ranging from 0 to 1.0. Conversely, for put options the delta is  $(\Phi(d_1) - 1)$ , so these vary from 0 to -1.0.

The size of the delta reflects how likely the option is to be exercised. An option is said to be at-the-money when its strike price is equal to the market price of its underlying. A call (put) option is in-the-money when the underlying market price is higher (lower) than its strike price, whilst if the opposite holds true it is said to be out-of-the-money. At-thc-money options tend to have deltas around  $\pm 0.5$ , as they become deeper in-the-money this becomes closer to  $\pm 1.0$ , whilst deeply out-of-the-money options have deltas approaching 0.0. Nearer to expiration, deltas tend to become closer to  $\pm 1.0$ . Deltas also vary based on changes in the underlying asset price, volatility and interest rate, as we can see from equation 13-4.

When calculating the delta risk for positions we must also incorporate whether they are long or short. This is done by negating the deltas of short positions. Thus a long call position and a short put position are both actually delta positive, due to the double negatives for the short put. Similarly, short call and long put positions are both delta negative.

For instance, a long position of 50 call options with a delta of 0.5 has a delta-adjusted position of  $50 \times 0.5 = 25$ . To delta hedge this position we can sell 25 shares of the underlying asset. Alternatively, we might buy  $100$  out-of-the-money puts each with a delta of  $-0.25$ (although hedging with another option can introduce additional risk factors). Either way we achieve our goal of achieving a delta neutral position.

**Example 13-5(a):** We have sold 100 OCT 50 call options for EFG at  $4.$  EFG is currently trading at \$45 and its volatility is 20%.

Since we have sold a call option we are delta negative, therefore we can hedge this by buying shares of EFG. Given that the call option delta is initially 0.15, this means buying 15 shares. The hedge will be updated on a daily basis for the lifetime of the option. Table 13-6 shows how this progresses over time.

| Date      | Asset<br>price | Option<br>delta | Delta<br>shares | Hedging<br>$P/L$ \$ |
|-----------|----------------|-----------------|-----------------|---------------------|
| 13 Aug 07 | 45.30          | 0.15            | 15              |                     |
| 14 Aug 07 | 46.90          | 0.19            | 19              | 30.4                |
| 15 Aug 07 | 47.80          | 0.33            | 33              | 29.7                |
| 16 Aug 07 | 48.60          | 0.44            | 44              | 35.7                |
|           |                |                 |                 |                     |
| 17 Sep 07 | 53.80          | 0.75            | 75              |                     |
| 18 Sep 07 | 55.60          | 0.89            | 89              | 160.2               |
| 19 Sep 07 | 56.25          | 0.92            | 92              | 59.8                |
| 20 Sep 07 | 57.50          | 0.95            | 95              | 118.8               |

Table 13-6 An example of delta hedging

As the call options become deeper in-the-money, their delta approaches 1.00, so by the end of September we effectively have a fully covered call position. It is likely that the option will be assigned, causing us to realise a loss. Though, the delta hedging means that much of this loss will be covered by gains from our long hedge.

With any hedging strategy, it is vital to strike the right balance between cost effectiveness and risk. This is particularly true for delta hedging since the delta is affected by so many factors. Changes in the underlying asset price, its volatility, the interest rate and the time left to expiry may trigger a change in the delta. In theory, we should constantly adjust the hedge position to ensure we remain delta neutral. Unfortunately, due to transaction costs this is impractical.

Re-hedging may be carried out in an ad-hoc fashion based on  $(1)$  time,  $(2)$  delta or  $(3)$  the underlying price, as Euan Sinclair (2008) points out in his book 'Volatility Trading'. Thus position adjustments may be made at discrete time intervals, when the delta reaches a specific level or when the underlying asset reaches a set price level, such as for every \$1 or 1% move. Alternatively, Sinclair (2008) outlines some more systematic approaches based on utility theory, which take into account the risk aversion of the trader. These use delta banding, with hedging only undertaken when the delta moves outside its allowed range. Short positions are hedged more defensively whilst long positions are handled more loosely (the deltas are allowed "to run"). The width of the delta band corresponds to the trader's risk aversion.

The type of volatility being used for these calculations can also play an important role. As we saw in Chapter 10, implied volatility is based on the market prices of options contracts, whilst realised volatility is determined from the underlying asset price changes. Both of these may be used to try to forecast what future volatility may be. For delta hedging, Sinclair  $(2008)$  notes that using implied volatility lowers the variance of the profit and loss  $(P&L)$ over time, although the final P&L is less certain when compared to using realised volatility.

Delta hedging is an important tool; hence, venues have already started offering linked orders between a stock and its options. For example, the International Securities Exchange (ISE) introduced "buy-write" orders in 2004. The stock leg is sent to NYFIX for execution, upon completion the option leg then becomes active on the ISE's order book. Initially, only a 1:1 ratio was supported, although this has since been extended to support any ratio.

#### Gamma Hedging

Gamma hedging is an extension of delta hedging which also aims to keep the gamma close to zero. Delta hedging works well for small moves in the price of the underlying. However, the delta can change rapidly when the option is almost at-the-money. By controlling the gamma, we can slow this rate of change and so improve the effectiveness of delta hedging.

As we have already seen, gamma is a second derivative risk measure which represents how much the delta will change when the underlying asset's price moves by one unit, such as \$1. For instance, let's consider a call option priced at \$6 with a delta 0.5 and a gamma of  $0.25$ . When the underlying asset price increases by \$1, the delta means the call option will increase to  $6.5$ , whilst its delta will increase to 0.75 because of the gamma.

Based on the Black Scholes model, equation 13-3, we can actually define gamma as:

$$\frac{\varphi(d_1)}{S\sigma\sqrt{T}}$$

where  $\varphi$  is the standard normal probability density function, S is the underlying asset's price,  $\sigma$  is its volatility, T is the time to expiry and  $d_1$  is as defined in equation 13-4.

Unfortunately, the gamma of the underlying asset or any futures/forwards is zero. Thus, gamma hedging relies primarily on options, or any other derivatives that have a non-linear relationship with the underlying asset's price.

**Example 13-5(b):** Let's add a gamma hedge to our position from Example  $13-5(a)$ .

Initially, the call option delta is  $0.15$  and the gamma is  $0.1$ .

Our net delta is  $-100 \times 0.15 = -15$ . This is offset to 0.0 by buying 15 EFG. Our net gamma is currently  $-100 \times 0.1 = -10$ .

We can offset this gamma with a long option position in a cheap out-of-the-money call. For this example, let's assume the call's delta is 0.088 and its gamma is 0.08. Buying 125 of these options offsets the gamma by  $125 \times 0.08 = 10$ , making us gamma neutral. Though, it also alters our net delta:

Net delta =  $(-100 \times 0.15) + 15 + (125 \times 0.088) = 11$ .

So to remain delta neutral we need to reduce our long position in EFG from 15 to 4.

Note that care must be taken when gamma hedging, since the new option positions can also introduce other risks. For instance, being delta and gamma neutral may well lead to volatility (vega) risk. Hedging against vega also relies on options. So to become vega neutral we may well need to take on a new option position and rebalance the portfolio in order to achieve the desired risk characteristics. Time (theta) and interest rate (rho) based risks may also be introduced. These are beyond the scope of this book, but Hull (2003) is a good starting point.

### **13.6 Arbitrage strategies**

Simple arbitrage, such as assets listing with different prices on multiple venues, is easy to understand and take advantage of. Essentially, "we buy low and sell high". Though, all trading has associated risks: For example, having bought the asset at the first venue, what if the market price at the second venue has adjusted? Suddenly, our profit margin may have disappeared, plus we must also take account of transaction costs. Hence, to try to guarantee profits any successful arbitrage must minimise risk by incorporating hedging techniques.

As well as simple price arbitrage, each asset class can also have its own particular arbitrage opportunities. For instance, yield curve arbitrage takes advantage of discrepancies in the pricing between short, medium or long-term bonds. Similarly, cash-flow arbitrage decomposes bonds into their effective constituents. If there are cheaper alternatives to create the same cash-flow, arbitrageurs may take advantage of the discrepancy. An example of this is stripping the coupons from bonds, such as U.S. Treasuries, and trading the zero-coupon bonds and their coupon strips separately.

However, the focus of this chapter is multi-asset trading: Arbitrage opportunities trading across different countries may involve multiple currencies, hence an FX cash trade may also be necessary to minimise the currency risk. For example, there can still be price discrepancies between dual listed companies, or stocks and their depositary receipts.

Derivatives are the main source of multi-asset arbitrage. In fact, one of the oldest types of arbitrage is basis trading. This is typically used to take advantage of mispricing between futures and their underlying commodities or bonds, although the principle may just as well be applied for options. Since both futures and options can be based on the same underlying cash assets, there is actually the potential for a three-way set of arbitrages between them. This is demonstrated for stock indices by pathways (a), (b) and (c) in Figure 13-1, which is

![](_page_13_Figure_1.jpeg)

based on a diagram from Sheri Markose and Hakan Er (2000).

Figure 13-1 Cross-asset index arbitrage opportunities

Index arbitrage focuses on mispricing between index futures and the underlying cash index, as shown by pathway (a) in Figure 13-1. Like basis trading, it is based on the concept of the future's fair value. For options, arbitrage is often based on the principle of Put-Call parity, shown by pathway (b). Pathway (c) shows the potential arbitrage between futures and options; this is driven by the Put-Call-Futures parity relationship.

The introduction of ETFs has provided additional opportunities for arbitrage. Thus, Figure  $13-1$  also shows pathways (d), (e) and (f) for cash indices. The daily creation and redemption mechanism (d) for ETFs provides a natural arbitrage with the underlying assets, whilst ETFs may act as substitutes for the cash assets in index arbitrage (e) and potentially even Put-Call option arbitrage (f). The creation of single stock futures based on ETFs should add even more permutations.

Note that many of the pathways shown in Figure 13-1 may also be applied for other types of underlier. There are also other derivative-based arbitrages, such as dividend arbitrage.

Clearly, speed plays a key role in successful arbitrage. Hence, electronic trading has had a huge effect. The simplest arbitrages have almost disappeared, since even for fragmented markets it is now relatively easy to spot and take advantage of any such opportunities within milliseconds. Even the more complex multi-market or multi-asset opportunities are likely to be monitored closely. Often, the timescales involved, and the associated margins, for such opportunities have been drastically reduced. So it is vital to get the hedging right.

It is also important to note that just because an arbitrage opportunity exists, that does not necessarily mean it is profitable. The cost of hedging must be considered, plus the associated transaction costs. So cost minimisation is another key focus. Taking advantage of any facilities such as netting trades via a CCP or cross-margining (to reduce margin payments for any futures positions) can also make a significant difference.

Given the progression of electronic and algorithmic trading, it is likely that in the future arbitrage opportunities will become even more complex, possibly involving exotic derivatives. As the saying goes, "There is no such thing as a free lunch"; arbitrage opportunities may well be out there, but making a profit from them is often non-trivial.

#### Multiple listing/depositary receipt arbitrage

Some companies are dual-listed or listed on multiple exchanges. However, the most widespread arbitrage opportunity comes from trading between depositary receipts and their underlying local stocks.

Figure 13-2 shows some examples of the price differences between ADRs and other crosslisted shares in the U.S., taken from an extensive study by Louis Gagnon and G. Andrew Karolyi (2003). Each chart plots both the U.S. dollar price of the ADR and the local price of the stock converted into dollars. Mispricing opportunities arise from both the difference in currency and local information. Different time zones and languages can mean that information flows to the markets at differing rates. For large cap stocks from developed countries, such as British Petroleum (BP) and Toyota Motor Corp., this should pose less of a problem. Indeed, we can see very few price discrepancies for these. Though, for smaller cap stocks or those from developing countries there can be quite substantial inconsistencies. For example, Figure 13-2 shows clear differences for Taiwan Semiconductor Manufacturing and Infosys Technologies. They also found that cross-listed stocks tended to follow U.S. market indices more closely than other domestic stocks.

![](_page_14_Figure_2.jpeg)

![](_page_14_Figure_3.jpeg)

![](_page_14_Figure_4.jpeg)

Figure 13-2 ADR prices versus their local shares

Another factor to consider for depositary receipts is the administration fee that is charged for their conversion. When this is taken into account, it can significantly reduce the number of arbitrage opportunities.

In order to implement this arbitrage we need a model that compares both prices, accounting for any currency differences and any additional fees. The orders for the ADR and the stock must also be dependent, much like for pair trading. As with any cross currency arbitrage, in order to take full advantage of price imbalances it is important to minimise the currency risk. So, as we saw for cross currency trades, a separate FX cash trade may be used. In fact, brokers are already starting to provide automated conversion services, notably ADR Direct from BNY ConvergEx. This allows clients to convert to and from ADRs as well as providing an automatic currency conversion.

#### Basis trading

In general, basis trading refers to an arbitrage between a futures contract and its underlying cash product. Though, in theory it could also be applied to the arbitrage between other derivatives and their corresponding underlying assets. The name is derived from the concept of the future's basis  $(B)$ , which is the difference between the current cash market price  $(S)$ and the futures contract's price  $(F)$ :

$$B = S - F \quad \equiv \quad F = S - B \tag{13-5}$$

This is also sometimes referred to as the total basis or the gross basis. Note that when the gross basis is positive the futures price is below the cash price, which is referred to as normal backwardation. Alternatively, a negative basis means the futures price is higher than the cash price, sometimes described as contango.

The basis changes over time, although generally it is less volatile than either the cash or the futures prices. However, towards expiration of the future the two prices will start to converge, since at expiry there is no real difference between a futures contract and the cash asset, barring transaction costs. This convergence means that the basis must also decrease, and should reach zero when the futures contract expires, as shown in Figure 13-3.

![](_page_15_Figure_6.jpeg)

Figure 13-3 Convergence of basis towards zero

Another way of expressing the relationship between the cash and futures prices is the cost of carry model:

$$F = S + C \tag{13-6}$$

where the cost of carry  $(C)$  represents the net costs associated with the cash position:

$$Cost \ of \ carry = \ Full \ cost + \ Storage \ cost - \ Income \ earned$$

In turn, this cost may be represented as:

$$C = (S \cdot r^{T/365}) + A - I \tag{13-7}$$

where r is funding interest rate, T is number of days until the futures contract expires,  $A$ represents the storage costs and  $I$  corresponds to the income earned.

The funding cost is the interest that would have to be paid to fund a cash position for the period of the futures contract, often this is based on the repo rate. The storage costs and income earned will differ depending on what the underlying asset is. For instance, with investment assets, such as bonds or stocks, the storage costs will be negligible whilst the income earned may be considerable (Bonds may earn accrued interest whilst equities may receive dividends.). Alternatively, for commodities the storage costs may be sizeable whilst no income will be generated.

When the net cost of carry is positive the futures position is more attractive since we will not need to make any payments until the future reaches expiry, apart from margin calls. Whereas if the cost of carry is negative it actually pays to take on the cash position instead.

The net basis, also termed the value basis, adjusts the gross basis for the cost of carry:

#### $Net \text{ basis} = Gross \text{ basis} + Cost \text{ of } carry$

Hence, the net basis represents the difference between the fair value of the future and its actual market price. A positive value shows it is underpriced, whilst a negative one means it is overpriced.

Buying the basis means issuing a buy order for the cash asset whilst simultaneously selling the corresponding futures contract. This is also called cash-and-carry trading. When we are long the basis, we benefit from any increases in the basis; in other words, from price rises for the cash asset or price drops for the future. Effectively, being long the basis allows us to earn the cost of carry.

Selling the basis is the opposite process, so the cash asset is sold and the future is bought. This is also known as reverse cash-and-carry trading. A short basis position will benefit from a decreasing basis; effectively it pays the cost of carry.

These strategies may effectively be implemented by using an appropriate pricing model and linking the orders for the future and the underlying asset/s.

#### Index arbitrage

Index arbitrage focuses on the profit opportunities that arise between index futures and their underlying constituents. Typically, most index arbitrage is carried out for stock indices, although it could also be applied to bond indices or even CDS indices. Effectively, it is another example of basis trading, except that the cash position corresponds to a basket of asscts.

Based on equation 13-6, we can use the cash price and the net cost of carry to determine the fair value of the futures contract. Opportunities for arbitrage arise when the market price for the index future deviates significantly from this fair value. If the futures price exceeds the fair value then a cash-and-carry trade can profit by buying the constituents of the index whilst selling the overpriced futures contract. Conversely, when the futures price is less than its fair value we can use a reverse cash-and-carry trade to buy the futures and sell the index. Generally, these positions will be closed out once the price discrepancy has disappeared, rather than when the futures contract expires.

As we noted for the cost of carry, the income earned is dependent on the underlying asset. Thus, accurately estimating the dividend cash flows is key to successful stock index arbitrage. The issuance of dividends is reasonably seasonal; however, even for short periods they may be delayed or even brought forward. Similarly, whilst analysts can offer reasonable estimates for the normal dividend amounts, special dividends can be much harder to predict. Unfortunately, special dividends often make a substantial proportion of the overall dividend cash flow, as James Cummings and Alex Frino (2007) note. Clearly, the risk of inaccuracy is greater for larger indices, such as the Russell 2000, and for longer periods.

**Example 13-6:** Let's determine the cost of carry and fair value for the S&P 500 SEP 2007 future using the following data for the 26<sup>th</sup> of June 2007, from www.lndexArb.com (2007).

- The SEP 07 contract has 87 days to expiry
- The short-term interest rate is around 5.52%.
- The cash index value is  $1492.89$

Before we can substitute these values into equation 13-7, we need to estimate a figure for the income earned from dividends (I). The estimate from www.indexArb.com (2007) for this is \$57,411, which we may convert into index points by using an appropriate divisor. In this case, the divisor is 8,883.46 giving an adjusted dividend of 6.46 index points. Note we shall assume the storage cost is zero. Thus, the cost of carry may be determined as:

$$C = (1492.89 * 1.0552^{87/365}) - 6.46 = 12.78$$

Using equation 13-6 the fair value of the future is  $(1492.89 + 12.78) = 1505.67$ .

**Example 13-6(a):** Let's now assume the current S&P 500 SEP 07 futures price is 1510.00.

Compared to our fair value of 1505.67 the futures contract seems overpriced, with a basis of -17.11. Therefore, it may be worth considering a cash and carry trade, selling the September future and buying the equivalent basket of stocks. Table 13-7 shows the resultant cash flows for such a strategy.

| Date    | Action                                    | Underlying<br>cash flow/\$ | Futures<br>cash flow/\$ |
|---------|-------------------------------------------|----------------------------|-------------------------|
|         | Buy stocks for \$250 x 1492.89            | $-373222.50$               |                         |
| 26 June | Borrow cash at $5.52\%$                   |                            |                         |
|         | Sell SEP future at $1510.00$              |                            |                         |
|         | Sell stocks for \$250 x 1533.38           | 383,345.00                 |                         |
|         | Receive dividends, $$250 \times 6.46$     | 1,615.00                   |                         |
| 21 Sept | Interest payments for 87 days loan        | $-4,810.58$                |                         |
|         | Future expires, \$250 x (1510.00-1533.38) |                            | -5845.00                |
|         | Gross amounts                             | 6,926.92                   | -5845.00                |
|         |                                           | Total                      | 1.081.92                |

### Table 13-7 Example cash flows for cash and carry index arbitrage

Note that the  $S\&P$  500 is a market capitalization based index, so each constituent has a weighting based on their company's size. To make things slightly easier we will assume we can create a basket of stocks equivalent to the value of the futures contract. The value of this basket is equal to the futures multiplier ( $$250$ ) times the index closing price. <sup>2</sup> The S&P 500 futures contract expires on the third Friday of the delivery month, in this case September 21<sup>st</sup>; at which point we must sell back our stocks (with market on open orders) whilst the future is settled for cash.

<sup>&</sup>lt;sup>2</sup> Alternatively, we could use the E-Mini contract that has a multiplier of  $$50$ .

Also, note that throughout the lifetime of this trade there will be various other eash flows, such as the daily futures margin payments and loan interest payments. Stock dividends will also be paid out intermittently over the period, and may be reinvested until expiry to further reduce costs. For simplicity, all these cash flows are merely presented in Table 13-7 as accumulated sums to be paid at expiry.

Overall, we can see that in this example the profit is derived solely from the cash leg, which had a gross profit of nearly \$7,000. Much of this was due to the overall increase of the stock index, although the dividend payments actually ensured that the strategy did more than break even. Offsetting this were the interest payments and the loss of nearly \$6,000 on the futures position. The futures leg did provide a successful hedge, since if the index had fallen we would have been in the opposite position. If this had happened, the profit from the futures contract would have compensated for the loss on the stocks.

**Example 13-6(b):** In actual fact the S&P 500 SEP 2007 futures price closed at 1497.80 on the 26<sup>th</sup> of June.

Compared to our fair value of 1505.67 the futures contract now seems underpriced, with a basis of -4.91. Therefore a reverse cash and carry trade is actually more appropriate. So we should consider buying the September future and selling the equivalent basket of stocks. The resultant cash flows for this approach are shown in Table 13-8.

| Date    | Action                                    | Underlying<br>cash flow/\$ | Futures<br>cash flow/\$ |
|---------|-------------------------------------------|----------------------------|-------------------------|
|         | Sell stocks for \$250 x 1492.89           | 373222.50                  |                         |
| 26 June | Lend cash at 5.52%                        |                            |                         |
|         | Buy SEP future at 1497.80                 |                            |                         |
|         | Buy stocks for \$250 x 1533.38            | -383,345.00                |                         |
| 21 Sept | Interest from 87 days loan                | 4,810.58                   |                         |
|         | Future expires, \$250 x (1533.38-1497.80) |                            | 8,895.00                |
|         | Gross amounts                             | -5,311.92                  | 8,895.00                |
|         |                                           | Total                      | 3,583.08                |

#### Table 13-8 Example cash flows for reverse cash and carry index arbitrage

This time, our long futures position actually benefits from the increase in the index level, leading to a gross profit of \$8,895. In comparison, our short cash position realised losses of \$10,122, which were offset by the \$4810 income from interest. Though, since we were short stock, there was no additional income from dividends.

Note that for both of these examples the final value of the stock basket is actually based on the futures settlement price (1533.38), rather than the opening price of the S&P 500 on the  $21^{st}$  (1520.11). This is because the index's opening price is based on when the NYSE opened rather than when all the morning's opening auctions had completed, which could actually be some time after the official open. Therefore, the official index open is actually based on some stocks' close prices from the 20<sup>th</sup>. So at expiry the CME instead provides a special opening quotation (SOQ), which is not finalised until all of the index constituent's official opening prices are set. This ensures that arbitrageurs can liquidate their trades at coordinated levels. Though, it does mean that there can sometimes be a sizable difference between these two prices. The SOQ was introduced in June 1987 to try to minimise the volatility, prior to this settlement was based on the closing price. For more information, please see the CME  $(2005)$  documentation.

There are some further complications, which were omitted from Example 13-6 (a) and (b) for clarity. Real-world arbitrage strategies must cope with the risk that the cost of carry is uncertain. Over the length of the trade short-term interest rates could shift, similarly the dividend cash flow may differ from its estimate. Arbitrageurs must also account for factors such as transaction costs, interest rates and market regulations.

Transaction costs obviously have a direct impact on arbitrage opportunities; high costs can make even significant mispricings unprofitable. Consequently, arbitrage models should also factor in the bid offer spread for the stocks and futures, as well as any fees or commissions. For larger waves, market impact could be an important factor as well. Also, when shorting stocks the cost of borrowing them must also be considered. This means that index futures are more often underpriced than overpriced, as Catherine Shalen (2002) points out.

Funding rates can also have an effect. The same funding rate was used throughout Example 13-6 (a) and (b). Though, the interest rates to borrow will be slightly higher than this market rate, whilst those for lending will be lower.

Market regulations can also have a noticeable impact on arbitrage. Short selling restrictions, such as the up-tick rule, make it more difficult to keep the cash and futures legs synchronized. Market collars also pose a considerable problem. For example, the NYSE Rule 80A enforces a collar based on the DJIA index; when triggered it requires indexarbitrage orders for the S&P 500 stocks to be stabilizing. So if the index falls 190 points (from the prior close) arbitrage orders can only be sold on an up-tick; conversely, if it rises by this amount buy orders must be on a down-tick.

To counter some of these issues, arbitrageurs often close out of their positions before the futures contract expires. Indeed a study of the NYSE by George Sofianos (1990) found this to be true for over 70% of positions, with liquidation occurring upon reversal of the original mispricing or within a few days. Arbitrageurs may also sometimes trade only a portion of the actual index, instead creating a subset that acts as a proxy. Although this offers reduced transaction costs, it does create the potential risk of tracking error between the proxy and the actual index.

Clearly, successful index arbitrage is non-trivial. Whilst there is still plenty of money to be made from this, it is not without some risk or difficulty. To automate this process we require detailed price models that need to take account of all of these factors. Similarly, to perform the trading we shall need to use approaches for handling baskets of orders, as we saw in Chapter 12. This will also need to be linked to the futures trading.

#### ETF Index Arbitrage

The daily creation and redemption mechanism for ETFs ensures that there is a natural arbitrage between these funds and their underlying assets. Therefore, when the ETF trades at a premium (discount) to its net asset value (NAV) dealers can simply sell (buy) the ETF and buy (sell) the underlying assets. This ensures that any mispricing for the ETF is kept to a minimum.

The rapid growth of the ETF marketplace has given rise to new arbitrage opportunities. In particular, for index arbitrage they can replace the cash leg. ETFs are attractive to arbitrageurs because they arc:

- based on the actual index  $\bullet$
- easy to short

- not subject to any up-tick rules
- potentially much cheaper to trade than a basket of stocks

Since ETFs represent a pro-rata share in a fund modelled on the index they should have a negligible tracking error. Their inherent daily creation mechanism means that short sales pose no issues. As Gary Gastineau (2003) notes, this also means short squeezes are not possible. The lack of an up-tick rule also makes them much more flexible when selling. Thus ETFs circumvent many of the issues we saw in the previous section. They offer a low risk and cost efficient alternative for index arbitrageurs, provided they have sufficient liquidity.

There is one key difference between using a basket of stocks or an ETF for the cash leg of an index arbitrage, as Andrew Economopoulos (2005) highlights: For ETFs, dividends are accumulated in the fund and distributed 45 days after the ex-dividend date. The value of these accumulated dividends will actually be discounted, so the market price of an ETF will be slightly lower than its net asset value (NAV). This also means the ETF may actually trade at a slight premium to the index, which will also be reflected in any futures fair value based on the ETF price.

Arguably, the main appeal of ETFs is their potential to substantially reduce transaction costs. For instance, Economopoulos (2005) gives an example of the S&P 500, where ten SPDR shares are equivalent to the index. For a portfolio worth \$25 million he estimated a total cost of \$170,362 for trading the cash index. In comparison using the SPDR ETF cost \$45,357 whilst the futures only cost \$2,777. Table 13-9 helps to explain these differences.

|            | Shares purchased | Average spread $(\$)$ | $Cost \ (bps)$ |
|------------|------------------|-----------------------|----------------|
| Cash index | 714,185          | 0.219                 | 68             |
| ETF        | 266.810          |                       |                |

Source: Economopoulos (2005)

#### Table 13-9 Round trip cost comparison between cash and ETFs

The main cause is the sheer number of stocks which have to be traded. Combined with a higher spread this leads to a total cash index cost of 68 bps, whereas the ETF costs some 50 bps less. Even accounting for the fund management costs of 4.6 bps the ETF offers a considerable saving over trading cash equities.

Note that realizing these savings requires the ETF to have enough liquidity. So the liquidity premium must be sufficiently low; otherwise it will cancel out any savings. For instance, Economopoulos (2005) points out that prior to 1996, even though the SPDR ETF offered a cost advantage, its liquidity was insufficient to attract traders as a cash substitute. He also notes that the mispricing relationship declined after November, 1997, suggesting increased arbitrage. This seems to be linked to the CME halving the denomination of the S&P 500 futures contract, and their earlier introduction of the E-mini contract. Likewise, an earlier study by Lorne Switzer, Paula Varson and Samia Zghidi (2000) found that the introduction of the SPDR ETF had improved the pricing efficiency in the futures market, observing that mispricing was negatively related to SPDR volume.

Another benefit of arbitrage using ETFs is that we no longer need to trade baskets of assets. Thus a more straightforward pair trading approach may be used, although we will still clearly need a sophisticated pricing model.

#### Option arbitrage

Put-call parity is a key principle in option pricing, most notably demonstrated by Hans Stoll (1969). He highlighted the relationship between the fair values for a pair of identical European eall and put options and their underlying asset, as shown in equation 13-8:

$$C_t + Xe^{-rt} = P_t + I_t \tag{13-8}$$

where C is the price of the call option,  $P$  is the price of the put,  $I$  is the price of the underlying, X is their strike price, r is the interest rate and t is the time left to expiry. Note that this depends on the put and the call having the same strike price and expiration.

Stoll showed that by using this principle the payoff of any one of the trio may be recreated by an appropriate combination of the other two. Hence, the whole concept of synthetic option positions was spawned. For example, a synthetic long call is just a long position in the underlying combined with purchasing an at-the-money (ATM) put. Alternatively, a synthetic long put corresponds to a short position in the underlying together with the purchase of an ATM call option.

Using put-call parity we should always be able to infer the fair price for a call or a put option based on the prices of the other two assets. So, any mispricing may be easily spotted and taken advantage of by arbitrageurs. If the call option is relatively overpriced then a conversion strategy may be used. This means selling the call and hedging by creating a synthetic long call position. Alternatively, if the put option is overpriced we may adopt a reversal, or reverse conversion strategy, which consists of selling the overpriced put and hedging with a synthetic long put.

A conversion strategy comprises of selling ATM call options, and buying the underlying and ATM puts. Alternatively, we can view this as going long the underlying and creating a synthetic short position. Figure 13-4 shows the payouts for this strategy.

![](_page_21_Figure_8.jpeg)

Figure 13-4 Payouts for the conversion strategy

Any gains in the underlying will be offset by losses from the calls; similarly, any losses will be compensated for by gains in the puts. Hence, the position is completely hedged.

**Example 13-7(a)**: Asset HJK is currently trading at \$50. The OCT 50 call is priced at \$3 whilst the OCT 50 put is  $2$ . The interest rate is  $5.52\%$ .

Based on equation 13-8, we should first determine the discount factor, assuming that both options will expire in a month, so  $e^{-rt} = e^{-1/12 \times 0.0552} = 0.995$ .

We can now substitute these values into the put-call parity equation  $(13-8)$ :

 $3 + (50 \times 0.995) = 2 + 50 \implies 52.75 \neq 52$ 

Clearly, either the call option is overpriced or the put is underpriced. Assuming that the call option price is fair then the put option should actually be  $$2.75$ .

Either way, we can take advantage of this with a conversion strategy:

|           |                      | Income               |        | Outgoings               |
|-----------|----------------------|----------------------|--------|-------------------------|
| $\bullet$ | Buy underlying       |                      |        | $50 \times 100 = 5,000$ |
|           | Sell ATM calls       | $3 \times 100 = 300$ |        |                         |
|           | Buy ATM puts         |                      |        | $2 \times 100 = 200$    |
|           | $Total = $ -4,900 =$ | \$300                | $\sim$ | \$5,200                 |

Setting up the conversion trade has cost \$4,900, so it is \$100 cheaper than simply buying the underlying. This saving is due to the difference in pricing between the ATM calls and puts. This profit is immediately locked in, as Figure 13-4 shows.

In October, if the asset price rises to \$60 the call options will be in-the-money and so will be exercised. The long underlying position may be used for delivery. The put options will become worthless. Overall, we shall receive \$5,000, giving a gross profit of \$100.

Conversely, if the price fell to \$40 the puts will be in-the-money whilst the call options will be worthless. So we can exercise the put options to sell our underlying position for \$5,000, again leaving a gross profit of \$100.

Alternatively, if the price does not change we can sell the underlying for \$5,000, with a gross profit of \$100.

Regardless of the outcome, a gross profit of \$100 should be achieved. All that remains is to subtract any interest payments and transaction costs.

For a reversal strategy, we sell ATM put options, and sell the underlying and buy ATM calls. We can also view this as shorting the underlying and creating a synthetic long position. Figure 13-5 plots the potential payouts for this approach.

**Example 13-7(b):** Asset HJK is still trading at  $$50$ , but now the OCT 50 call has fallen to  $$2$ whilst the OCT 50 put has risen to \$3.

Let's assume the call price is fair, in which case, based on the discount we calculated in Example 13-7(a), the put should be priced at  $$1.77$ . This time the put is overpriced relative to the call, in which case we can adopt a reversal:

|                   | Income                    | Outgoings            |
|-------------------|---------------------------|----------------------|
| Sell underlying   | $$50 \times 100 = $5,000$ |                      |
| Buy ATM calls     |                           | $2 \times 100 = 200$ |
| Sell ATM puts     | $3 \times 100 = 300$      |                      |
| $Total = 5,100 =$ | \$5,300<br>-              | \$200                |

![](_page_23_Figure_1.jpeg)

Figure 13-5 Payouts for the reversal strategy

Again, setting up the reversal trade has proven more profitable than simply shorting the underlying. Once more, the profit is derived from the difference in pricing between the ATM calls and puts, and is instantly locked in. As we can see from Figure 13-5, any losses on the underlying are offset by gains from the calls, whilst any gains are neutralised by the puts.

In October, if the asset price rises to \$60 the call options will be in-the-money and so will be exercised, allowing us to flatten our underlying short for \$5,000. The puts will expire worthless. Hence, the overall gross profit remains \$100.

If the price falls to \$40 then our call options will expire worthless. Though, the put options we sold will expire in-the-money, so the purchaser will want to sell us 100 HJK for \$5,000. This flattens our short position, leaving us with \$100 profit again.

If the price does not change, we can llatten our short position, at a cost of  $$5,000$ .

The net profit for this strategy will also incorporate any interest earned for the \$5,000 over the month, which will help offset any borrowing costs associated with shorting the underlying.

### Futures and options arbitrage

The put-call parity relationship we saw in equation 13-8 relates the prices of options with the price of the underlying asset. Similarly, we can relate these to futures positions, as Alan Tucker (1991) showed with the Put-Call-Futures (P-C-F) parity relationship.

The price of a stock index future may be related to the underlying index price  $(S)$  by its forward value:

$$F_i = S_i \, e^{(r-q)\tau}$$

where q is a constant rate representing income from dividends, r is the risk-free rate and  $\tau$ is the time to expiry. Sheri Markose and Hakan Er (2000) rearrange this to show that discounting the futures price gives the underlying stock index price adjusted for dividends:

$$F_t e^{-r\tau} = S_t e^{-q\tau}$$

We can substitute this into the right hand side of the put-call parity equation  $(13-8)$  to express it in terms of the futures price, and so define the P-C-F parity:

$$C_t + X e^{-r\tau} = P_t + F_t e^{-r\tau}$$

If the futures contract is underpriced relative to the options we can take advantage using a conversion strategy. Essentially, this is the same as we saw in Example 13-7(a), except we go long the futures contract rather than the underlying. To counter this position, a synthetic short future is created by selling ATM calls and buying the equivalent puts. The synthetic future is completed by lending an additional cash amount, based on the discounted difference between the strike price and the futures price i.e.  $(X - F_i) e^{-r\tau}$ .

Whereas if the futures contract is overpriced compared to the options then we can adopt a reversal strategy, as we saw in Example  $13-7(b)$ . Again, rather than shorting the underlying we sell the futures contract. This is then hedged with a synthetic long futures position, from buying ATM calls and selling the puts and borrowing  $(X - F_t) e^{-r\tau}$ .

Trading a futures contract is a much cheaper alternative to trading a basket of stocks. So trading based solely on index futures and options can prove a cost-effective and efficient means of index arbitrage.

In their study of FTSE-100 P-C-F arbitrage, Markose and Er (2000) note that when the index future is at its fair value the put-call and put-call-futures parity conditions are identical. They concluded that some of the most profitable P-C-F arbitrage opportunities were for futures contracts further from maturity, such as 20-50 and 50-80 days. They also noted that the so-called Black effect could have a substantial impact on the opportunities for arbitrage. This is due to market makers for index options often using the Fisher Black (1976) pricing method, a modification of the Black Scholes formula that is based on the futures price rather than the index. The effect can mean that overpriced index futures lead to overpriced calls and underpriced puts, and vice-versa. Markose and Er (2000) found that the Black effect limited the efficiency of P-C-F arbitrage and in some circumstances noted that arbitrage could even exacerbate the futures underlying mispricing.

#### Dividend arbitrage

Company dividend payments can be an important source of earnings. Dividend arbitrage combines a position in the stock with deep in-the-money options in order to lock in profits.

When a dividend is formally announced, the company will specify when the payment will actually be made, termed the due date. They also stipulate the record date that determines the actual entitlement, since only the shareholders of record at this time will receive payments. However, since it takes time for trades to be cleared and settled, the exchange will usually set a separate deadline. This is the ex-dividend (or ex-div) date, which is often two days before the record date. Anyone purchasing the stock before the ex-dividend date will receive the dividend, even if they subsequently sell the stock. Thus, the market price usually reflects this fact with a price drop equal to the dividend, as shown in Figure 13-6.

If we buy the stock just before the ex-div date we are effectively paying a premium based on the dividend value. The price drop at the ex-div date will realise an immediate loss for long positions. Only at the subsequent due date will the dividend actually be paid. So a quick sale will often return a loss, or at best a negligible profit. To lock in any profits from the dividend there are two main types of arbitrage based on either buying put options or selling call options.

![](_page_25_Figure_1.jpeg)

Figure 13-6 The price effect of stock dividend payments

By purchasing an in-the-money put option at the same time as buying the stocks, we have locked in an exit price. Although, there will be a significant premium to be paid for such options. In order for this strategy to be profitable, this premium must be less than the exercise profit and the dividend payment.

**Example 13-8:** Stock EFG is trading at \$50; it goes ex-div on the 20th September paying \$2/share. A SEP 55 put costs \$6.

To lock in dividend profits we can buy 100 EFG and 100 SEP 55 puts. The resultant cash flows are shown in Table 13-10:

| Date    | Action                            | Cash flow/\$ |
|---------|-----------------------------------|--------------|
| 18 Sept | Buy stocks for $$50 \times 100$   | $-5.000$     |
|         | Buy SEP 55 put for \$6 x 100      | -600         |
| 20 Sept | Exercise put for $$55 \times 100$ | 5,500        |
|         | Dividend payment $2 \times 100$   | 200          |
|         | Total                             |              |

**Table 13-10 Dividend arbitrage using puts** 

The exercise cost is \$100 whilst \$200 is made from the dividend; therefore, the SEP 55 puts are sufficiently cheap to result in a net profit of \$100. This trade is risk free since we have flattened our long position by exercising the puts, so we are unaffected by price changes on the ex-div date.

The alternative approach is to sell an in-the-money call option. Though, this relies on the fact that assignment does not occur before the ex-div date (that is the purchaser does not exercise them). At which point, the price drop will affect both the stock and its options. We should be able to buy back the call option more cheaply, which will offset the losses from our stock position, leaving the dividend payment as profit.

Example 13-9: Stock HJK is trading at \$60; it goes ex-div on the 16th October paying \$2/share. An OCT 50 call costs \$10.

We can lock in the dividend profits by going long 100 HJK and selling 100 calls. Assuming that the call options were not assigned, the cash flows for the stocks and options balance out leaving \$200 profit from the dividend, as shown in Table 13-11.

| Date   | Action                           | Cash flow/\$ |
|--------|----------------------------------|--------------|
| 15 Oct | Buy stocks for $60 \times 100$   | $-6.000$     |
|        | Sell OCT 50 call for \$10 x 100  | 1,000        |
|        | Sell stocks for $$58 \times 100$ | 5,800        |
| 16 Oct | Buy call for $8 \times 100$      | -800         |
|        | Dividend payment, $2 \times 100$ | 200          |
|        | Total                            |              |

### Table 13-11 Dividend arbitrage using covered calls

Thus, the main risk with this strategy is the likelihood of the call option being assigned before the ex-div date, which would lead to a loss of the dividend profits. Further examples may be found at TheOptionsGuide.com (2007).

# 13.7 Adapting algorithms for multi-asset trading

In many ways, multi-asset trading algorithms are similar to the two-sided portfolio trading algorithms we saw in Chapter 12. Though, since they involve a more diverse range of markets they are more likely to suffer from marked differences in liquidity. This could pose real problems for achieving best execution. Therefore, risk models need to start expanding to cope with this.

### Factors to consider for multi-asset trading algorithms

Obviously, the main starting point for any multi-asset trading is to already have successful algorithms in place for trading each of the target asset classes. This ensures that any asset class specific issues have already been identified and appropriate adjustments have been made.

Multi-asset trading adds an extra level of complexity since it will invariably mean trading across different trading platforms, currencies and time-zones. Hence, it is vital that any trading algorithms can cope with differences in:

- Liquidity  $\bullet$
- Latency  $\bullet$
- Transparency ●
- Consistency ٠
- Dependency

Otherwise, there may be a considerable additional risk exposure.

## Liquidity

As we saw in Chapter 3, liquidity varies considerably between the various markets and asset classes, just as it does between specific assets. Multi-asset trading algorithms need to balance their trading based on the liquidity of the target assets. Simplistically, this means focussing on the lowest common denominator, so the most illiquid asset drives the rate of trading.

For instance, when trading a corporate bond against its stock, orders might only be placed for the stock leg once an execution has been confirmed for the less liquid bond. Alternatively, we could use legging to provide some more flexibility over execution, just as we saw for pairs trades. Though, for very illiquid assets this could expose us to significant risk. Whilst such approaches will work, they could miss opportunities for the more liquid assets.

#### Latency

Latency can be just as important as liquidity. It makes it harder to rely on the prices we can see, since by the time our order is handled the price may have shifted.

Each asset class may well be traded over different platforms, across different execution venues and possibly even spanning time-zones. Exchanges are now focussed on reaching turnaround times less than I0 ms. However, there are still plenty of venues where this figure is more like 100 ms or more. So there are bound to be differences in latency between the venues.

The actual trading mechanism is another key factor for latency, since it is quite possible that trading might need to span both order books and request-for-quote (RFQ) or request-forstream (RFS) based platforms. In such eases, the difference in latencies might range from milliseconds to seconds.

For example, let's consider executing a simple pairs trade, both assets have the same liquidity except one trades at a venue with a latency of 50ms whilst for the other it is 500ms. If we place a matching buy and sell order for each asset there is at least 450ms of uncertainty. A busy trader might not notice this lag; after all, it is equivalent to a few blinks. However, it can still have an appreciable effect. In order to compensate for this, the trading algorithm will have to bias trading towards the venue with higher latency.

#### Transparency

Transparency can also vary considerably between markets. Within a single market, differing levels of transparency have proved fairly successful. Highly transparent primary venues allow for easy price discovery, whilst more opaque venues enable volume discovery. Indeed, the "dark pool" ATSs have proven so successful for equities because although being opaque their price discovery tends to be based on the primary exchanges.

Across asset classes, differences in transparency can pose more of a problem, since there are no equivalent links. For instance, the entire order book might be visible when trading stocks, but for other assets we might only be able to see the best bid and offer. Although we might have confidence of best execution for our stock trading, it is much harder to have this for the other assets.

#### Consistency

Consistency is another major factor for ensuring successful multi-asset trading, particularly for transaction costs. As we saw in section 13.6, there is a wide range of arbitrage opportunities between asset classes. For these to be profitable it is vital that any additional eosts are considered when looking at relative prices. This might be as obvious as incorporating the different bid offer spreads, commissions or routing/handling fees. However, it must also include asset specific factors such as storage/delivery fees, accrued interest or dividend payments.

#### Dependency

Over the years, microstructure studies have analysed the price relationships across many of the different asset elasses. For example, studies have focussed on whether the futures markets lead or lag the markets for their underlying assets. Such inter-market relationships are an important source of information for short-term predictions of prices and other market

conditions, as we will see in Chapter 15. Taking advantage of these could be the difference between a profitable trading strategy and a loss-making one.

#### Minimising risk

Lower transaction costs may be achieved for portfolios by maximising the natural hedging, or diversification, for as long as possible. Therefore, it is quite likely that risk-based models, similar to those we saw for portfolio trading, will be at the heart of next generation multiasset algorithms. Clearly, constructing multi-asset risk models is more complex than the existing single asset ones. However, these should hopefully provide the flexibility required to achieve best execution for all the assets in a mixed portfolio.

| Asset                   | Size/\$mm | Side | Liquidity | Risk   |
|-------------------------|-----------|------|-----------|--------|
| Euro mid-cap stock      | 10        | Buv  | Medium    | High   |
| Euro equity put options |           | Buy  | Low       | Medium |
| $\text{Euro FX}$        | 10        | Buy  | High      | Medium |
| U.S. equity put options |           | Buv  | Medium    | Low    |
| U.S. large-cap stock    | 10        | Buv  | High      | Low    |

For example, let's consider the dummy trade list shown in Table 13-12.

Table 13-12 Potential prioritisation for a sample portfolio

In this particular case, the European mid-cap stock and its put options have the lowest liquidity. Note that the put options are intended for hedging and so may be made dependent on the underlying stock position. The out-of-the-money puts for the U.S. large-cap stock are assigned a lower overall risk than the FX trade, since the required size is less. Hence, for this basket the mid-cap stock position poses the most risk, so we can target this more aggressively. This is clearly a simplistic example, but it highlights the fact that liquidity should not be the sole determinant when evaluating trading strategies.

A more quantitative approach would be to determine the marginal contribution to risk (MCR) for each order in the trade list and then adjust their execution accordingly, as we saw in Chapter 12. We should also try to incorporate factors such as latency into the estimates for timing risk.

#### Trading algorithm choice

The simplest multi-asset orders could be handled by slight extensions to existing algorithms. For example, we could extend the pairs/spread trading mechanism that we saw in Chapter 5. An additional leg could incorporate handling FX cash trades with relative ease.

Alternatively, for strategies where there is a clear dependency between the orders, a conditional algorithm could be created; essentially, this would just use conditional orders. This could be used to try to cover short sales with orders for lending/repos. It might also provide the mechanism for simple structured notes, or even some hedging.

For more complex strategies, the "algorithm of algorithms" approach that we saw in Chapter 12 seems a reasonable starting point. Again, the portfolio algorithm would need to contain the required control logic, whilst the individual orders could continue to use standard single asset algorithms. So stock, bond, currency, future and option positions could each be handled by their own algorithms, which the portfolio algorithm continually checks and adjusts. If the links between the investor and the broker are sufficiently fast and reliable, there is no real reason why the portfolio algorithm could not reside on the buy-side, with updates sent to the individual algorithms being worked on the sell-side.

Similarly, since hedging and arbitrage rely on position information and potentially proprietary analytics these are good candidates for in-house development by the buy-side.

# 13.8 Summary

- m Multi-asset trading strategies are now more widely accessible due to electronic trading:
  - Utility strategies incorporate FX cash trades or cover short sales.
  - Some structured products may be recreated using algorithms.
  - Hedging strategies offset risk, whether this is for duration, beta, delta or gamma.  $-$
  - Arbitrage strategies take advantage of mispricing between assets, even between asset classes. Hedging is also vital to lock these profits in by staying risk-free.
- To cope with trading across different asset classes it is vital that strategies take account of differences in:
  - Liquidity
  - Latency
  - Transparency
- For best execution, strategies must also ensure that prices are compared consistently, by . including any relevant asset specific costs or factors.
- Strategies may also use established inter-market price relationships to gain an edge from short-term price forecasts.
- m Multi-asset trading may require extensions to existing trading algorithms to deal with:
  - Adding conditional orders
  - Adopting a pairs/spread trading approach
  - Handling the different legs as a portfolio, possibly adopting an "algorithm of algorithms" to minimise risk
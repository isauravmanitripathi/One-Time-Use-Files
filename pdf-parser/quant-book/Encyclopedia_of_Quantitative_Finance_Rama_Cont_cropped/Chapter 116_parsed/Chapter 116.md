# **Delta Hedging**

The delta of an asset or a portfolio broadly means net market exposure to an asset class. This may be for a single asset, like an option, or for a portfolio, like an S&P 500 benchmarked mutual fund. Delta hedging is the process of reducing the size of this exposure to a target level to reduce the amount of risk exposure due to the delta present in the portfolio.

Delta hedging is a term used in two broad categories: delta hedging of investment portfolios and delta hedging of financial derivartives.

## **Delta Hedging of Investment Portfolios**

The delta of a portfolio is determined based on the assets in the portfolio. For equity portfolios, it may mean net equity exposure, for fixed income portfolios it may mean portfolio duration, while for commodity portfolios it could be exposure to the underlying commodity such as bushels of corn or barrels of oil. To delta hedge a portfolio, the portfolio manager determines what target net delta level is desired for the portfolio and uses a broad market instrument like a futures or swaps to achieve that desired level of delta. In addition, some portfolio managers might be more precise by hedging sensitivity to one factor (beta hedging) or multiple factors.

# **Delta Hedging of Financial Derivatives**

Financial derivatives provide linear or nonlinear exposure to an underlying asset price level. While it is possible that both the buyer and the seller of a specific derivative are interested in identically opposite exposures, it is more common that one of the parties to the transaction is a financial intermediary or market maker that plans to hedge or reduce some of the risks of the transaction.

Delta hedging is the simplest form of hedging financial derivatives. This hedging aims to neutralize the direct exposure to the underlying asset, or delta, while maintaining second-order exposures to convexity, volatility, and time. In this discussion, we assume that a market maker enters into a financial derivative transaction and decides to hedge the delta arising from the transaction. If the net delta exposure between the financial derivative and the hedge is zero, the position is said to be *delta neutral*.

## **The Process of Delta Hedging**

The process of delta hedging incorporates some or all of the following steps.

#### *Calculation of Delta*

Typically, this is based on risk neutral valuation of the product. As a result the delta may vary depending on the underlying model used in the valuation. This variation may be small for simple products but may result in material differences for complex products. For example, a vanilla equity call option at-themoney (ATM) might have a similar delta based on Black–Scholes [1] inputs or a local volatility model, while a knock-out put, might have materially different deltas if measured by the two models above.

#### *Determining the Appropriate Hedging Instrument*

Entering into a hedge has various costs, the key aspects of which are mentioned below:

#### 1. **Liquidity of the hedging instrument**

It is ideal that the hedging instrument is easily tradable with a low bid/ask spread. For derivatives, where the underlying is less liquid or there might be some market impact in executing the hedge, the price of the financial derivative is based on the average realized execution price level of the hedge.

#### 2. **Basis risk in the hedging instrument**

In practice, some of the hedging instruments may have a small basis risk *versus* the actual underlying, which needs to be hedged. This usually happens when the actual underlying has significant transaction or liquidity costs and the basis tracking risk is low.

#### 3. **Financing costs**

There might be costs associated with going long or short an asset as a hedge or entering into a financial swap transaction (e.g., the cost of posted collateral).

#### 4. **Stability of the hedge**

If the hedge involves going long an asset or entering into a long-term linear over the counter (OTC) derivative, the hedge is considered stable. However, if the market maker requires to borrow the hedge to go short (e.g., short stocks or bonds), then the hedge may be subject to a lack of availability to borrow in the marketplace.

### *Incorporating the Cost of Hedging into the Price of the Financial Derivative*

- 1. Market makers who seek to hedge a position may incorporate the cost of hedging using adjustments to the financing rates, expected loss owing to basis risk, or future rollover costs of short-term hedges (like futures) into the pricing of the derivative.
- 2. In addition, the market maker may seek contractual obligations to the ensure that if he is unable to hedge the contract, he has a right to unwind the derivative at fair market price.

# **Examples of Delta Hedging**

Below are some examples of delta hedging.

**Example 1. Listed put option on S&P 500 index.** Market Maker Derivatives Inc. (MMDI) sells an exchange listed put on the S&P 500 (SPX) Index on a \$100mm notional with a strike price of \$1350 and one year expiration to a client when the SPX is trading at \$1400. The Black–Scholes model calculates the delta of the position at 38.5%. To delta hedge and neutralize the position to P&L swings from changes in the level of the SPX, MMDI needs to sell \$38.5mm of SPX Index. MMDI can do one of the following to achieve this:

- 1. Sell \$38.5mm in SPX index futures (1100 futures at \$1400 with a 250 multiplier). Since these futures expire every three months, the market maker needs to roll this exposure into a new contract every three months.
- 2. Sell \$38.5mm of a one-year swap on the SPX Index with another counterparty for one year or enter into an OTC put/call combo transaction (buying a put and selling a call with the same strike price to replicate a forward using put–call parity) for \$38.5 mm notional. This is done in the OTC market place and appropriate International Swaps and Derivatives Association, Inc. (ISDA) (http://www.isda.org/) documents and collateral agreements need to be in place before this is done.

3. Sell \$38.5mm a basket of stock that comprises S&P 500 index, paying a borrowing fee and executing stock orders on the exchange.

## **Example 2. Long total return swap on XYZ commodity index.**

MMDI sold a five-year total return swap on the XYZ commodity index to a client for \$10mm notional, which has a delta of \$10mm. To hedge the position, MMDI can do one of the following:

- 1. Buy an equal and offsetting swap with another client or market counterparty or a basket of commodities swaps for each of the components of the XYZ index from another counterparty which is the perfect hedge (assuming no counterparty risk).
- 2. Hedge the XYZ index with a much more actively traded index like the CRB index taking into account the tracking risk and weighting differences of the components between the two indices.
- 3. Maintain a portfolio of long futures on commodities, which compromises the XYZ index and rolling futures on the position for the next five years. The market maker assumes the risk of rolling the futures positions to changes in the shape of the commodity forward curve.

# **Rehedging Delta with Time, Spot Moves**

The delta of a financial product may change with time or the levels of the different market parameters such as volatility, underlying price, interest rates, or skew. It is then necessary to periodically adjust the size of the hedge to maintain the delta at a preset level. The rate of change of the delta is proportional to the gamma (*see* **Gamma Hedging**).

# **Reference**

[1] Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities, *Journal of Political Economy* **81**(May-June), 637–659.

# **Related Articles**

**Hedging**; **Hedging of Interest Rate Derivatives**; **Option Pricing: General Principles**.

VIJU JOSEPH

# **Dispersion Trading**

Dispersion trading refers to the practice of selling index variance while buying variance of its constituents at the same time. The reverse strategy (buying index variance while selling constituents variance) can also be employed, but it is not as popular.

To understand dispersion trading, consider the index as a basket of stocks:

$$S_I = \sum_{i=1}^n w_i S_i \tag{1}$$

where  $w_i$  is the weight of  $S_i$  in the basket.

The variance of the index is related to that of the individual stocks by

$$\sigma_I^2 = \sum_{i=1}^n w_i^2 \sigma_i^2 + 2 \sum_{i=1}^n \sum_{j>i}^n \rho_{ij} w_i w_j \sigma_i \sigma_j \qquad (2)$$

The variance is defined as

$$\sigma_i^2 = \frac{1}{T} \sum_{t=1}^T (S_i^t - \bar{S}_i)^2 \tag{3}$$

with  $\bar{S}_i = \frac{1}{T} \sum S_i^t$ , and the correlation  $\rho_{ij}$  is defined

$$\rho_{ij} = \frac{1}{T} \sum_{t=1}^{T} (S_i^t - \bar{S}_i)(S_j^t - \bar{S}_j) / (\sigma_i \sigma_j) \qquad (4)$$

If we hold the realized variances of every component stock constant, the maximum for the index variance is reached when the correlation between all the components is  $100\%$ . If the correlation between stocks is not perfectly 100%, the index variance is lower. The more "dispersed" the stocks are, the lower is the index variance.

A measure of dispersion—the dispersion spread—can be defined as

$$D = \sqrt{\left(\sum_{i=1}^{n} w_i \sigma_i\right)^2 - \sigma_I^2} \tag{5}$$

or, alternatively, it has also been defined as

$$D = \sum_{i=1}^{n} w_i \sigma_i - \sigma_I \tag{6}$$

 $D = 0$  corresponds to the case when there is no dispersion—all correlations are  $100\%$ .

So, to long dispersion is equivalent to be short correlation and vice versa.

To characterize the correlation between the constituents, one can define the average correlation as if the correlation is the same between every pair of stocks in the basket

$$\bar{\rho} = \frac{\sigma_I^2 - \sum_{i=1}^n w_i^2 \sigma_i^2}{2\sum_{i=1}^n \sum_{j>i}^n w_i w_j \sigma_i \sigma_j} \tag{7}$$

However, sometimes, it is easier to calculate the less accurate "correlation proxy," which is defined as

$$\tilde{\rho} = \frac{\sigma_I^2}{\left(\sum_{i=1}^n w_i \sigma_i\right)^2} \tag{8}$$

This correlation proxy can be interpreted as the "average" of all correlations between all pairs of stocks in the index including a stock with itself (which we know should be 100%). When the number of stocks in the index  $n$  is high, it can be seen that  $\sum_{i}^{n} w_{i}^{2} \sigma_{i}^{2}$  is much less compared to the retained terms.

$$\sum_{i=1}^{n} w_i^2 \sigma_i^2 \ll \sigma_I^2 \tag{9}$$

$$\sigma_I^2 \simeq \sigma_I^2 - \sum_{i=1}^n w_i^2 \sigma_i^2 \tag{10}$$

$$2\sum_{i=1}^{n}\sum_{j>i}^{n}w_{i}w_{j}\sigma_{i}\sigma_{j} \simeq 2\sum_{i=1}^{n}\sum_{j>i}^{n}w_{i}w_{j}\sigma_{i}\sigma_{j}$$
$$+\sum_{i=1}^{n}w_{i}^{2}\sigma_{i}^{2} \qquad (11)$$

The correlation proxy and correlation are very close to each other. The implied correlation can be simply inferred from the ratio of average volatilities. Sometimes it is also convenient to calculate the mean variance ratio that is more directly related to the trade profit/loss (P/L).

By definition, realized correlation is the correlation calculated using realized volatilities, and implied correlation is the correlation calculated using implied volatilities. Implied volatilities decide the price of the traded instruments like vanilla options and variance swaps.

The success of dispersion trades relies on the fact that statistically the realized correlation tends to be below the implied correlation. Historically, if one were long dispersion, on average, one made more money than the amount one lost. There are many different reasons for this phenomenon, for example, one may argue that there is more market demand for index volatility than that of the individual stock, which means usually there is more premium for equity stock volatility. More importantly, correlation jumps to a very high level when extreme market conditions exist, namely, global recession and market crash, while it stays low in a normal and uneventful market.

To long the volatility of each component stock, and short the index volatility, one can either trade vanilla options or variance swaps. The variance swaps provide direct exposure to variance without the unnecessary cost and hassle of hedging against daily stock movements.

One issue in dispersion trade is to decide the relative weight for index and constituents variances. There is no single "correct" relative weight to use. For example, vega neutral weights aim to make the sum of constituents vega and index vega zero, so that the trade is hedged against fluctuations in level of volatility. "Premium neutral" weights make the initial premium of buying constituents and selling index cancel each other.

In reality, it is impractical to trade all constituents. Often, a selection of names in the index (or even those not in the index) is used. This is called a *proxy basket*. One can build the proxy basket by selecting, for example, the names that have the largest weights in the index, or the names that are judged relatively "cheap", or the names that are mostly likely to "disperse" against each other, or simply by the stock fundamentals.

## **Related Articles**

**Basket Options**; **Correlation Swap**.

YONG REN
# **Call Auction Markets**

Countless market structures exist for equity trading. Each is a variant of and/or a hybrid combination of four generics: (i) the continuous order-driven, agency market, (ii) the periodic order-driven call auction, (iii) the continuous quote-driven, dealer market, and (iv) the negotiated market (e.g., floor trading, upstairs block negotiation, and electronic negotiation). One of the common market mechanisms is the *call auction market*.

The distinguishing characteristic of a call auction is the batching of orders for simultaneous execution in a multilateral trade at a single clearing price, at a single point in time. This contrasts with continuous trading (either order or quote driven) where a trade can occur whenever a buy and a sell order match or cross in price.

At the specific point in time when a market is "called", buy orders are sorted and the shares aggregated from the highest priced buy to the lowest, and sell orders are sorted and the shares aggregated from the lowest priced sell to the highest. The two arrays of aggregated shares are matched, and the clearing price is set at the value at which the largest number of shares will execute—where the aggregated number of shares to buy (which decreases with price) equals the aggregated number of shares to sell (which increases with price). Buy orders at the clearing price and higher execute, as do sell orders at this price and lower (further rules of order execution are used when the number of shares to buy does not match the number of shares to sell exactly). Because all orders execute at the common clearing price (not the price at which they have been placed), executable orders are generally price improved.

If the clearing price at the auction is determined as just described, the system is a *price discovery call*. If the clearing price is set elsewhere (exogenously), the system is a *crossing network.* The clearing price for an intraday crossing network is typically the midpoint of the bid and ask quotes posted by a major market center. The after-hours crosses typically use market closing prices. This article focuses on *price discovery* call auctions. For further discussion of the properties of call auction trading, see [4, 5] and [14], Chapter 4.

#### **The Advent of Electronic Calls**

Each of the four above-noted generic forms of trading can involve human-to-human interaction (either faceto-face on an exchange floor or via the telephone) and/or electronic technology. Call auction trading, however, predates electronic technology. One hundred and thirty eight years ago, the New York Stock Exchange was a call market. The Tel-Aviv Stock Exchange through the 1970s and the Paris Bourse, before it introduced its electronic, order-driven market in 1986, were also nonelectronic call auctions. Pressure from an increasing order flow and from competing continuous markets crowded out the nonelectronic calls.

In the past two decades, call auction trading has made its re-entrance as an electronic marketplace. The electronic calls are being used, most notably, by Deutsche Borse; NYSE Euronext's Paris, Ams- ¨ terdam, and Brussels exchanges; the London Stock Exchange; SWX Swiss Exchange; and the Nasdaq Stock Market. The New York Stock Exchange opens and closes its markets with calls but, as of this writing, its calls are not fully electronic.

The electronic calls are not standalone systems but have been combined with continuous trading to create hybrid markets. With a hybrid structure, an investor can select among alternative trading venues depending on the size of his or her order, the liquidity of the stock being traded, and the investor's own motive for trading.

## **Tempering Volatility at Market Openings and Closings**

Because they consolidate orders and amass liquidity, call auctions have been used to sharpen price discovery. As such, they are generally run to open and to close a market, and to reopen a market that has been halted because of stressful market conditions. The opening is itself a time of stress because of the difficulty of translating overnight news into new share values. The closing is a time of stress because of trader impatience to "get the job done" before the trading session ends. The stress that characterizes openings and closings is apparent in the sharp accentuation of intraday volatility in the first and last minutes of a trading day [11].

Paris introduced electronic closing calls in 1996 and 1998 in response to derivative traders' demand for better closing prices. In 2004, Nasdaq introduced its electronic calls (which it refers to as its *Crosses*) for a similar reason. As reported in [11], "Nasdaq decided to introduce Closing Cross in Fall 2003 after a competing market, the American Stock Exchange, responding to a strongly expressed request from Standard & Poor's for better closing prices, started planning a closing call of its own that would be used for Nasdaq stocks."

The accentuation of volatility at market openings and closings has been well documented in the academic literature (relevant volatility studies include [1, 7–11, 16]). The ability of call auctions to contain this volatility and improve market quality has also been established [2, 11–13, 15]. Nevertheless, Ellul *et al.* [6] suggest that the call "suffers from a high failure rate to open and close trading especially when trading conditions are difficult." The theoretical analysis of order submission to a call auction by Chakraborty *et al.* [3] also shows the difficulty of getting early order submission (a "bookbuilding" problem); these authors suggest that the effectiveness of a call depends on structural issues such as its transparency and whether or not it includes a market maker to "animate" bookbuilding.

# **Smaller Cap Stocks and Large Institutional Orders**

The ecology of an order-driven market breaks down when it receives inadequate order flow. Call auction trading, because it amasses liquidity at fixed points in time, can help overcome this problem. Accordingly, call auctions are important for trading mid- and smallcap stocks (the Paris Bourse uses them for these issues).

Placing large, institutional-sized orders on a continuous, open book market is also problematic (disclosure of a large order before it executes fully can cause adverse price moves that raise execution costs). Order batching, by amassing liquidity and delivering price improvement, also mitigates this adverse effect.

# **Order Handling in Call versus Continuous Markets**

Orders are handled differently in call auctions than in continuous trading:

- In continuous order-driven markets, limit orders set the prices at which market orders execute, and limit orders sitting on the book provide immediacy to market orders. In contrast, market orders in a call auction are nothing more than extremely aggressively priced limit orders. Specifically, a market order to buy has an effective price limit of infinity, and a market order to sell has an effective price limit of zero.
- Limit orders in continuous trading generally execute at the prices at which they have been placed. Because in call auction trading all orders execute at the common clearing price, the more aggressively priced limit orders are price improved. This encourages participants to price their orders more aggressively, which enhances market liquidity.
- All participants in a call auction wait until the next call for their orders to execute. Thus, market orders do not receive immediacy as they do in continuous trading.
- In continuous trading, limit orders supply liquidity and market orders dry up liquidity. This distinction does not apply in call auction trading. In a call auction, all participants supply liquidity to each other. However, if limit orders on the book are publicly displayed, those participants who place their orders early in the precall, order entry period are key contributors to liquidity creation (i.e., they animate bookbuilding).

### **Overview**

Comprehensively viewed, imbedding call auctions in a continuous trading environment can have major positive benefits: most notably, lower volatility, lower execution costs, and sharper price discovery. The success of a call auction is not foreordained, however. To operate effectively, critical mass order flow must be received. Whether the requisite order flow is achieved depends critically on a call auction's specific architectural design.

#### **Acknowledgments**

Parts of this article have been adapted, with kind permission of Springer Science and Business Media, from *The Encyclopedia of Finance*, 2006, Alice C. Lee and C.F. Lee, Editors, Springer Science + Business Media, LLC, Chapter 35, pages 623–629, "Call Auction Trading," Robert A. Schwartz and Reto Francioni.

#### **References**

- [1] Amihud, Y. & Mendelson, H. (1987). Trading mechanisms and stock returns: an empirical investigation, *Journal of Finance* **42**, 533–553.
- [2] Barclay, M.J., Hendershott, T. & Jones, C.M. (2005). *Order Consolidation, Price Efficiency, and Extreme Liquidity Shocks*, working paper, University of Rochester.
- [3] Chakraborty, A., Pagano, M.S. & Schwartz, R.A. (2009). *Order Revelation at Market Openings*, working paper, Baruch College.
- [4] Cohen, K.J. & Schwartz, R.A. (1989). An electronic call market: its design and desirability, in *The Challenge of Information Technology for the Securities Markets: Liquidity, Volatility, and Global Trading*, H.C. Luca & R.A. Schwartz, eds, Dow Jones-Irwin, Homewood, IL, pp. 15–58.
- [5] Economides, N. & Schwartz, R.A. (1995). Electronic call market trading, *Journal of Portfolio Management* **21**, 10–18.
- [6] Ellul, A., Shin, H.S. & Tonks, I. (2005). Opening and closing the market: evidence from the London stock exchange, *Journal of Financial and Quantitative Analysis* **40**, 779–801.
- [7] Fleming, M.J. & Remolina, E.M. (1999). Price formation and liquidity in the US treasury market: the response to public information, *Journal of Finance* **5**, 1901–1915.

- [8] Hasbrouck, J. (1993). Assessing the quality of a security market: a new approach to transaction-cost measurement, *The Review of Financial Studies* **6**, 191–212.
- [9] Hasbrouck, J. & Schwartz, R.A. (1988). Liquidity and execution costs in equity markets, *Journal of Portfolio Management* **14**, 10–16.
- [10] Ozenbas, D., Schwartz, R.A. & Wood, R.A. (2002). Volatility in US and European equity markets: an assessment of market quality, *International Finance* **5**, 437–461.
- [11] Pagano, M., Peng, L. & Schwartz, R.A. (2009). *Market Structure and Intra-day Price Volatility: An Event Study on Nasdaq's Crosses*, working paper, Villanova University.
- [12] Pagano, M.S. & Schwartz, R.A. (2003). A closing call's impact on market quality at Euronext Paris, *Journal of Financial Economics* **68**, 439–484.
- [13] Pagano, M.S. & Schwartz, R.A. (2005). Nasdaq's closing cross: has its new call auction given Nasdaq better closing prices? Early findings, *Journal of Portfolio Management* **31**, 100–111.
- [14] Schwartz, R.A., Francioni, R. & Weber, B.W. (2006). *The Equity Trader Course*, John Wiley & Sons.
- [15] Smith, J. (2006). Nasdaq's electronic closing cross: an empirical analysis, Nasdaq economic research, *Journal of Trading* **1**(3), 47–64.
- [16] Werner, I. & Kleidon, A. (1996). UK and US trading of British cross-listed stocks: an intra-day analysis of market integration, *Review of Financial Studies* **9**, 619–664.

ROBERT A. SCHWARTZ & PAUL L. DAVIS
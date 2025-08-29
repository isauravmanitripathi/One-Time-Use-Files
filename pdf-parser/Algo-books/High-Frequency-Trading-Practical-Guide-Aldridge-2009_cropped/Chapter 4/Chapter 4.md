![](_page_0_Picture_0.jpeg)

wide range of securities and numerous market conditions fit the profile for trading at high frequencies. Some securities markets, however, are more appropriate than others. This chapter examines the topic of market suitability for high-frequency trading.

To be appropriate for this type of trading, two requirements must be met: the ability to quickly move in and out of positions and sufficient market volatility to ensure that changes in prices exceed transaction costs. The volatilities of different markets have been shown to be highly interrelated and dependent on the volume of macroeconomic news reaching the markets. The ability to quickly enter into positions as well as to close them is in turn determined by two factors: market liquidity and availability of electronic execution.

Liquid assets are characterized by readily available supply and demand. Liquid securities such as major foreign exchange pairs are traded  $24 \text{ hours a day}, 5 \text{ days a week. Less liquid securities, such as penny stocks,}$ may trade only once every few days. Between trades, the prices on illiquid assets may change substantially, making less liquid securities more risky as compared with more liquid assets.

High-frequency strategies focus on the most liquid securities; a security requiring a holding period of 10 minutes may not be able to find a timely counterparty in illiquid markets. While longer-horizon investors can work with either liquid or illiquid securities, Amihud and Mendelson (1986) show that longer-horizon investors optimally hold less liquid assets. According to these authors, the key issue is the risk/return consideration; longer-term investors (already impervious to the adverse short-term market moves) will obtain higher average gains by taking on more risk in less liquid investments.

According to Bervas  $(2006)$ , a perfectly liquid market is the one where the quoted bid or ask price can be achieved irrespective of the quantities traded. Market liquidity depends on the presence of trading counterparties in the market, as well as the counterparties' willingness to trade. The market participants' willingness to trade in turn depends on their risk aversions and expectations of impending price movements, along with other market information.

One way to compare the liquidity of different securities is to use the average daily volume of each security as the measure of liquidity. In terms of daily average trading volume, foreign exchange is the most liquid market, followed by recently issued U.S. Treasury securities; then come equities, options, commodities, and futures. Of the most liquid securities, only spot foreign exchange, equities, options, and futures markets have enabled fully automated execution; the remaining markets still tend to negotiate on a contract-by-contract basis over the counter (OTC), slowing down the trading process. Table 4.1 enumerates current market volumes and execution methods for different securities. As the demand for high-frequency trading increases, the development of electronic trading in the OTC markets may prove highly profitable. Figure 4.1 graphically illustrates optimal trading frequencies for various securities where the optimal trading frequency is a function of available market liquidity. The following sections discuss the pros and cons of high-frequency trading in each security market in detail

## FINANCIAL MARKETS AND THEIR SUITABILITY FOR HIGH-FREQUENCY TRADING

This section discusses the availability of various financial markets for highfrequency trading. As discussed in the first section of this chapter, for a market to be suitable, it must be both liquid and electronic to facilitate the quick turnover of capital. In the following subsections, we consider three key elements of each market:

- Available liquidity
- Electronic trading capability
- Regulatory considerations

| Market                              | Average Daily<br>Volume (Billions) | Dominant<br>Execution Method |
|-------------------------------------|------------------------------------|------------------------------|
| Foreign exchange swaps*             | 1,714.4                            | OTC                          |
| Foreign exchange spot*              | 1,004.9                            | Electronic                   |
| Foreign exchange outright forwards* | 361.7                              | OTC                          |
| U.S. Treasury**                     | 570.2                              | OTC                          |
| Agency MBS**                        | 320.1                              | OTC                          |
| Federal agency securities**         | 83.0                               | OTC                          |
| Municipal**                         | 25.0                               | OTC                          |
| Corporate debt**                    | 24.3                               | OTC                          |
| NYSE***                             | 2.6                                | Electronic                   |
| Options****                         | 1.6                                | Electronic and OTC           |

| TABLE 4.1 | Average Daily Volume and Dominant Execution Method for Major |
|-----------|--------------------------------------------------------------|
|           | Security Classes                                             |

\*Information on the global volume of foreign exchange is for April 2007 as reported in the Triennial Central Bank Survey.

\*\*Information on the U.S. debt daily volume is quoted from 2007 data reported by the Securities Industry and Financial Markets Association (SIFMA). By January 2009, in the aftermath of the credit crisis, the average daily volume in U.S. Treasuries decreased to USD 358 billion, Agency MBS volume increased to 358 billion, federal agency securities volume decreased to 75 billion, municipal bonds to 12 billion, and corporate debt to 12 billion.

\*\*\*The average daily volume is computed for the month of April 2009 from the daily volume reported by the NYSE.

\*\*\*\*The trading volume for options is quoted from the average daily volume reported by the Options Clearing Corporation for May 2009.

![](_page_2_Figure_7.jpeg)

**FIGURE 4.1** Optimal trading frequency for various trading instruments, depending on the instrument's liquidity.

#### Fixed-Income Markets

The fixed-income markets include the interest rate market and the bond market. The interest rate market trades short- and long-term deposits, and the bond market trades publicly issued debt obligations. Interest rate products and bonds are similar in that they both pay fixed or prespecified income to their holders. Aside from their fixed-income quality, bonds and interest rate products exhibit little similarity.

Both interest rate and bond markets use spot, futures, and swap contracts. Spot trading in both interest rate products and bonds implies instantaneous or "on-the-spot" delivery and transfer of possession of the traded security. Futures trading denotes delivery and transfer of possession at a prespecified date. Swap trading is a contractual transfer of cash flows between two parties. Interest rate swaps may specify swapping of a fixed rate for a floating rate; bond swaps refer mostly to a trading strategy whereby the investor sells one bond and buys another at a comparable price, but with different characteristics.

In fixed-income markets, many investors are focused on the product payouts rather than on the prices of the investments themselves. Highfrequency traders taking advantage of short-term price deviations win, as do longer-term investors.

**Interest Rate Markets** The spot interest rate market comprises quotes offered by banks to other banks, and can be known as "spot interest rates," "cash interest rates," or "interbank interest rates." As other financial products, interbank interest rates are quoted as a bid and an ask. A bid interest rate is quoted to banks wanting to make a deposit, whereas the ask quote is offered to banks to take a credit.

The quoted interest rates are not necessarily the rates at which banks lend each other money. The actual lending rate is the quoted interest rate plus a credit spread, where the credit spread is the amount that compensates the lending bank for the risk it takes while lending. The risk of the lending bank in turn depends on the creditworthiness of the borrowing bank. The lower the creditworthiness of the borrowing bank, the higher the risk that the lending bank takes by lending out the money, and the higher the credit spread intended to compensate the lending bank for the risk of lending.

Spot interest rates have fixed maturity periods denominated in days or months. Current maturity periods constitute the following set:

- Overnight: O/N
- The next business day after tomorrow, known as "tomorrow next": T/N
- One week S/W

- One month: 1M
- Two months: 2M
- Three months: 3M
- Six months: 6M
- Nine months: 9M
- One year: 1Y

Interest rate futures are contracts to buy and sell underlying interest rates in the future. Short-term interest rate futures are more liquid than spot interest rate futures. The liquidity of the interest rate futures market is reflected in the bid-ask spread of the interest rate futures; a bid-ask spread on interest rate futures is on average one-tenth of the bid-ask spread on the underlying spot interest rate.

Interest rate futures are commonly based on the 3-month deposit rate. The actual quotation for a futures bid or ask prices,  $f_{\text{bid}}$  and  $f_{\text{ask}}$ , respectively, depends on the annualized bid or ask OTC forward rates,  $r_{\rm bid}$  and  $r_{\text{ask}}$ , as follows:

$$f_{\text{bid}} = 100 \left(1 - \frac{r_{\text{bid}}}{100\%}\right)$$
$$f_{\text{ask}} = 100 \left(1 - \frac{r_{\text{ask}}}{100\%}\right)$$

A 3-percent forward rate, for example, results in a futures price of 97.00. The forward rates underlying the futures contracts typically mature in three months. The futures contracts usually have four standardized settlements per year—in March, June, September, and December.

Unlike spot interest rates, interest rate futures do not vary according to the creditworthiness of the borrower. Instead of pricing default risk into the rate explicitly, exchanges trading interest rate futures require borrowers to post collateral accounts that reflect the creditworthiness of the borrower.

Swap products are the most populous interest rate category, yet most still trade OTC. Selected swap products have made inroads into electronic trading. CME Group, for example, has created electronic programs for 30day Fed Funds futures and CBOT 5-year, 10-year, and 30-year interest rate swap futures; 30-day Fed Funds options; 2-year, 5-year and 10-year Treasury note options; and Treasury bond options. As Table 4.2 shows, however, electronic trading volumes of interest rate products remain limited.

**Bond Markets** Bonds are publicly issued debt obligations. Bonds can be issued by a virtual continuum of organizations ranging from federal governments through local governments to publicly held corporations. Bonds

| Daily Dollar Volume in Most Active Interest Rate<br>Products on CME Electronic Trading (Globex) on<br>TABLE 4.2<br>6/12/2009 Computed as Average Price Times<br>Total Contract Volume Reported by CME |  |                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------|
| Instrument                                                                                                                                                                                            |  | Futures Daily Volume<br>(in USD thousands) |
| Eurodollar deposits                                                                                                                                                                                   |  | 196,689.9                                  |
| LIBOR                                                                                                                                                                                                 |  | 163.5                                      |
| 30-Year Swap                                                                                                                                                                                          |  | 934.5                                      |
| 5-Year Swap                                                                                                                                                                                           |  | 1,295.2                                    |
| 10-Year Swap                                                                                                                                                                                          |  | 978.6                                      |
| 30-Day Fed Funds                                                                                                                                                                                      |  | 2,917.7                                    |
|                                                                                                                                                                                                       |  |                                            |

typically pay interest throughout their lifetimes and pay back the principal at the end of the bond contract, known as the maturity of the bond. Bonds can also embed various options, to suit both the needs of the issuer and the needs of the target buyer. For example, a company in the midst of a turmoil may decide to issue bonds that embed an option to convert the bond into the company's stock at some later date. Such a bond type is known as a convertible bond and is designed to give prospective investors the security of preferred redemptions should the company be liquidated; should the company fully recover, the bond gives investors the ability to convert it into equity and thus obtain a higher return in the long run. In addition to risk-averse investors, convertible bonds may attract investors desiring a conservative investment profile at present and a riskier equity profile in the long run.

Despite the advantageous breadth of the bond market, spot bonds are transacted mostly OTC and do not generate a readily observable stream of high-frequency data.

Unlike bonds that can be custom tailored to the buyer's specifications, bond futures contracts are standardized by the exchange and are often electronic. (See Table 4.3.) Bond futures have characteristics similar to those of the interest rate futures. Like interest rate futures, bond futures settle four times a year—in March, June, September, and December. The exact settlement and delivery rules vary from exchange to exchange. Bond futures with the nearer expiry dates are more liquid than their counterparts with longer maturities.

While interest rate futures are based on notional 3-month deposits, bond futures are typically based on government bonds with multiyear maturities. As such, bond futures register less influence from the central banks that issue them. Bonds issued with maturity of less than two years are referred to as "bills," whereas bonds issued with maturity of two to ten years are often called "notes."

| TABLE 4.3<br>Electronic Trading (Globex) on 6/12/2009 Computed as Average<br>Price Times Total Contract Volume Reported by CME |                                            |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Instrument                                                                                                                     | Futures Daily Volume<br>(in USD thousands) |
| 30-Year U.S. Treasury Bond, Futures                                                                                            | 19,486.6                                   |
| 10-Year U.S. Treasury Note, Futures                                                                                            | 82,876.5                                   |
| 5-Year U.S. Treasury Note, Futures                                                                                             | 31,103.0                                   |
| 2-Year U.S. Treasury Note, Futures                                                                                             | 14,187.1                                   |

#### **TABLE 4.3** Daily Dollar Volume in Most Active Bond Futures Products on CME Electronic Trading (Globex) on 6/12/2009 Computed as Average

#### **Foreign Exchange Markets**

In a nutshell, a foreign exchange rate is a swap of interest rates denominated in different currencies. Foreign exchange trading originated in 1971 when the gold standard collapsed under the heft of U.S. debt. From 1971 until the late 1980s, foreign exchange traded entirely among commercial banks that made deposit arrangements in different currencies. Commercial banks had exclusive access to inter-dealer networks, consisting of loose groups of third-party agents facilitating quick distribution of orders among different commercial banking clients. Investment banks, such as Goldman Sachs, had no direct access to the inter-dealer networks and transacted their foreign exchange trades through commercial banks instead.

In the early 1990s, investment banks were able to gain access to brokerdealer networks. In the late 1990s non-bank companies and non–U.S. investment banks connected directly to the inter-dealer pools. Since 2003, hedge funds and proprietary trading funds have also been granted access to the inter-dealer liquidity. Currently, spot, forward, and swap foreign exchange products trade through this decentralized and unregulated mechanism. Only foreign exchange futures and selected options contracts can be found on exchanges.

The decentralization of foreign exchange trading has had two key consequences: the absence of "one price" and the absence of volume measures.

The absence of a single coherent price at any given time is a direct consequence of decentralization. Different dealers receive different information and price their securities accordingly. The lack of one price can present substantial arbitrage opportunities at high trading frequencies. Another consequence of decentralization is that the market-wide measure of volume at any given time in foreign exchange is not available. To monitor developments in foreign exchange markets, central banks conduct financial institution surveys every three years. These surveys are then aggregated and published by the Bank for International Settlements (BIS).

BIS estimates that the total foreign exchange (FX) market in 2007 had a daily trading volume of \$3 trillion. This includes the spot market and forwards, futures, options, and swaps. The spot market accounts for about 33 percent of the total daily turnover or about \$1 trillion. According to BIS Triennial Surveys, the proportion of spot transactions among all FX trades has been decreasing; in 1989, spot represented 59 percent of all FX trades. In 1998, spot accounted for only 40 percent of all FX trades. Of the \$2 trillion of daily FX volume that is not spot, \$1.7 trillion is contributed by FX swaps.

Some FX futures and options are traded on exchanges. Table 4.4 shows daily electronic trading volumes in most common foreign exchange futures on CME.

Foreign exchange markets profitably accommodate three types of players with distinct goals: high-frequency traders, longer-term investors, and corporations. The main objective of high-frequency traders is to capture small intra-day price changes. The main objective of longer-term investors is to gain from global macro changes. Finally, the main objective of corporate currency managers is usually hedging of cross-border flows against adverse currency movements—for example, a Canadian firm selling in the United States may choose to hedge its revenue stream by purchasing puts on USD/CAD futures. The flows of the three parties can be quite distinct, as Table 4.5 illustrates.

Table 4.5 reports summary statistics for EUR/USD order flows observed by Citibank and sampled at the weekly frequency between January 1993 and July 1999: A) statistics for weekly EUR/USD order flow aggregated across Citibank's corporate, trading, and investing customers; and B) order flows from end-user segments cumulated over a week. The last four columns on the right report autocorrelations *i* at lag *i* and *p*-values for the null that (*i* = 0). The summary statistics on the order flow data are from Evans and Lyons (2007), who define order flow as the total value of EUR/USD purchases (in USD millions) initiated against Citibank's quotes.

| TABLE 4.4<br>CME Electronic Trading (Globex) on 6/12/2009 Computed as<br>Average Price Times Total Contract Volume Reported by CME |  |                                            |                                                 |
|------------------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------|-------------------------------------------------|
| Currency                                                                                                                           |  | Futures Daily Volume<br>(in USD thousands) | Mini-Futures Daily Volume<br>(in USD thousands) |
| Australian Dollar                                                                                                                  |  | 5,389.8                                    | N/A                                             |
| British Pound                                                                                                                      |  | 17,575.6                                   | N/A                                             |
| Canadian Dollar                                                                                                                    |  | 6,988.1                                    | N/A                                             |
| Euro                                                                                                                               |  | 32,037.9                                   | 525.3                                           |
| Japanese Yen                                                                                                                       |  | 8,371.5                                    | 396.2                                           |
| New Zealand Dollar                                                                                                                 |  | 426.5                                      | N/A                                             |
| Swiss Franc                                                                                                                        |  | 4,180.6                                    | N/A                                             |

Daily Dollar Volume in Most Active Foreign Exchange Products on

| m<br>Su<br>TABLE 4.5       | mary Statistics of Weekly EUR/USD Order Flo |                                    | w                                             | observed by Citibank between January 1 |                      | 993 and July 1     | 999         |
|----------------------------|---------------------------------------------|------------------------------------|-----------------------------------------------|----------------------------------------|----------------------|--------------------|-------------|
|                            |                                             | m<br>Su                            | mary Statistics (Citibank weekly EUR/USD      |                                        | w 1<br>order flo     | 999)<br>993–1      |             |
|                            |                                             |                                    |                                               |                                        | Autocorrelations Lag |                    |             |
| w<br>Order Flo             | Standard<br>Mean                            | m<br>m<br>mu<br>mu<br>Maxi<br>Mini | wness or<br>Kurtosis*<br>Ske                  | 1                                      | 2                    | 4                  | 8           |
|                            | −0.043                                      | 3.722                              | 05<br>0.1                                     | −0.061                                 | 0.027                | 0.025              | −0.015      |
| A: Total for EUR/USD       | 1.234                                       | −3.715                             | 3.204                                         | (0.287)                                | (0.603)              | (0.643)            | (0.789)     |
| B: EUR/USD Order Flo       | ws                                          |                                    |                                               |                                        |                      |                    |             |
| mer Type<br>per Custo      |                                             |                                    |                                               |                                        |                      |                    |             |
|                            | 6.774<br>−1                                 | 549.302                            | −0.696                                        | −0.037                                 | −0.04                | 0.028              | −0.028      |
| (i) Corporate U.S.         | 08.685<br>1                                 | −529.055                           | 9.246                                         | (0.434)                                | (0.608)              | (0.569)            | (0.562)     |
| (ii) Corporate Non–U.S.    | −59.784                                     | 8<br>634.91                        | −0.005                                        | 0.072                                  | 0.089                | −0.038             | 03<br>0.1   |
|                            | 96.089<br>1                                 | 9<br>−692.41                       | 3.908                                         | (0.223)                                | (0.124)              | (0.513)            | (0.091)     |
|                            | 9<br>−4.11                                  | 63<br>0.1<br>71<br>1               | 0.026                                         | −0.021                                 | 0.024                | 0.126              | −0.009      |
| (iii) Traders U.S.         | 346.296                                     | −2024.28                           | 8.337                                         | (0.735)                                | (0.602)              | 01)<br>(0.1        | (0.897)     |
|                            | 87<br>11.1                                  | 06<br>972.1                        | 0.392                                         | −0.098                                 | 0.024                | 0.015              | 0.083       |
| (iv) Traders Non–U.S.      | 83.36<br>1                                  | −629.139                           | 5.86                                          | (0.072)                                | (0.660)              | (0.747)            | 40)<br>(0.1 |
| (v) Investors U.S.         | 9.442<br>1                                  | 535.32                             | −1.079                                        | 0.096                                  | −0.024               | −0.03              | 6<br>−0.01  |
|                            | 46.627<br>1                                 | −874.15                            | 11.226                                        | (0.085)                                | (0.568)              | (0.536)            | (0.690)     |
|                            | 15.85                                       | 881.284<br>1                       | 0.931                                         | 0.061                                  | 07<br>0.1            | −0.03              | 4<br>−0.01  |
| (vi) Investors Non–U.S.    | 273.406                                     | 8.895<br>−71                       | 9.253                                         | 82)<br>(0.1                            | (0.041)              | (0.550)            | (0.825)     |
| wness of order flo<br>*Ske | ws measures whether the                     | w to<br>ws ske<br>flo              | ward either the positive or the negative side |                                        |                      | of their mean, and |             |

kurtosis indicates the likelihood of extremely large or small order flows. Statistical properties of skewness and kurtosis are discussed in detail in Chapter 8.

| Instrument | Futures Daily Volume<br>(in USD thousands) | Mini-Futures Daily Volume<br>(in USD thousands) |
|------------|--------------------------------------------|-------------------------------------------------|
| S&P 500    | 2,331.6                                    | N/A                                             |
| Nasdaq100  | 172.4                                      | N/A                                             |
| E-mini     | 2,300,537.2                                | N/A                                             |
| E-Mid-cap  | 40,820.9                                   | N/A                                             |
| E-Nasdaq   | 515,511.8                                  | N/A                                             |
| Nikkei     | 56,570.3                                   | N/A                                             |
| GSCI       | 211.0                                      | N/A                                             |
| MSCI EAFE  | 24,727.7                                   | 2,126.9                                         |

|           | Daily Dollar Volume in Most Active Equity Futures on CME Electronic |
|-----------|---------------------------------------------------------------------|
| TABLE 4.6 | Trading (Globex) on 6/12/2009 Computed as Average Price Times       |
|           | Total Contract Volume Reported by CME                               |

### **Equity Markets**

Equity markets are popular among high-frequency players due to the market inefficiencies presented by the markets' sheer breadth; in 2006, 2,764 stocks were listed on NYSE alone. In addition to stocks, equity markets trade exchange-traded funds (ETFs), warrants, certificates, and even structured products. There are stock futures and options, as well as index futures and options. Most stock exchanges provide full electronic trading functionality for all of their offerings. Table 4.6 documents sample daily electronic trading volumes in most active equity futures trading on Globex.

Equity markets display diversity in investment objectives. Many equity market participants invest in long-term buy-and-hold patterns. Short-term opportunities for high-frequency traders abound.

#### **Commodity Markets**

Commodities products also include spot, futures, and options. Spot commodity contracts provide physical delivery of goods (e.g., a bushel of corn) and are therefore ill suited for high-frequency trading. Electronically traded and liquid commodity futures and options, on the other hand, can provide viable and profitable trading strategies.

Like other types of futures, commodity futures are contracts to buy or sell the underlying security—in this case a commodity, at a prespecified point in time in the future. Futures of agricultural commodities may have irregular expiry dates due to the seasonality of harvests. Commodity futures contracts tend to be smaller than FX futures or interest rate futures contracts.

| Commodity    | Futures Daily Volume<br>(in USD thousands) | Mini-Futures Daily Volume<br>(in USD thousands) |
|--------------|--------------------------------------------|-------------------------------------------------|
| Corn         | 121,920.9                                  | 178.0                                           |
| Wheat        | 33,399.5                                   | N/A                                             |
| Soybeans     | 147,168.6                                  | 423.1                                           |
| Soybean Meal | 13,089.6                                   | N/A                                             |
| Soybean Oil  | 4,334.1                                    | N/A                                             |
| Oats         | 212.9                                      | N/A                                             |
| Rough Rice   | 447.0                                      | N/A                                             |
| Milk         | 12.9                                       | N/A                                             |
| Dry Milk     | 0.1                                        | N/A                                             |
| Cash Butter  | 14.3                                       | N/A                                             |
| Pork Belly   | 1.6                                        | N/A                                             |
| Lean Hog     | 1,385.0                                    | N/A                                             |
| Live Cattle  | 728.0                                      | N/A                                             |
| Feeder       | 179.8                                      | N/A                                             |
| Lumber       | 167.3                                      | N/A                                             |
| Ethanol      | 40.8                                       | N/A                                             |

|           | Daily Dollar Volume of Commodity Products in CME Electronic   |
|-----------|---------------------------------------------------------------|
| TABLE 4.7 | Trading (Globex) on 6/12/2009 Computed as Average Price Times |
|           | Total Contract Volume Reported by CME                         |

In 2009, CME offered electronic futures and options trading in commodities shown in Table 4.7. Table 4.7 also shows daily volumes on selected electronically traded futures recorded on CME on June 12, 2009.

# **CONCLUSION**

As previous sections have shown, electronic trading is rapidly advancing to bring instantaneous execution to most securities. The advantages of highfrequency trading in the developing electronic markets are two-fold:

- First-to-market high-frequency traders in the newly electronic markets are likely to capture significant premiums on their speculative activity simply because of the lack of competition.
- In the long term, none of the markets is a zero-sum game. The diverse nature of market participants ensures that all players are able to extract value according to their own metrics.
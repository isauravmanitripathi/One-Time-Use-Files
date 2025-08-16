## **Eurodollar Futures and** Options

A Eurodollar rate is an interest rate on US dollar deposits that are held in banks outside the United States. The Eurodollar futures contract is a contract whose underlying is the three-month Eurodollar interest rate. When launched in 1981 at the Chicago Mercantile Exchange (CME), the Eurodollar futures were the world's first cash-settled futures contract. Since then, they have become the most actively traded short-term interest rate contract. At the time of writing, an average of more than 1.5 million contracts are traded each day and open interest exceeds 20 million positions (see  $[2]$ ).

Each futures contract has a notional or "face value" of \$1 000 000. On the expiry date of the contract, the futures price is determined by the London Interbank Offered Rate (LIBOR; see LIBOR Rate), which is applied to Eurodollar deposits for a threemonth period starting from the third Wednesday of the delivery month. If  $R$  is the fixing of the threemonth LIBOR at expiration, expressed with quarterly compounding, the futures final settlement price is defined as  $100 - R$ , and the payoff of one futures contract is  $1000000 \times (1-0.25 \times R\%)$ . This results in futures price dropping when yield rises.

Eurodollar futures are closely related to the forward rate agreements (FRAs; see LIBOR Rate). However, the futures are marked-to-market daily, and for a long Eurodollar futures position, the margin payments are financed at a higher cost when rates rise and invested at a lower rate when rates decline. To compensate for the disadvantage of being long Eurodollar futures against FRA, the futures price must be lower and the futures rate ( $= 100 -$  futures price) must be higher than the corresponding forward rates. Empirical study by Burghardt [1] shows that this difference, known as "convexity bias", may exceed 15 basis points for futures contracts with five years to expire. The exact magnitude of the bias is model dependent, for example, Hull [4] used the approximation  $\frac{1}{2}\sigma^2 t_1 t_2$ , where  $\sigma$  is the annualized standard deviation of the short-term interest rate,  $t_1$  is the time of maturity of the futures contract, and  $t_2$  is the time of maturity of the deposit. Readers should refer to [5, 6] for the theoretical framework (also see [8] and the reference therein for more results).

Eurodollar futures contracts are listed in a March quarterly expiration cycle. At any given time, there are forty quarterly expiries listed, spanning out 10 years, plus the four nearest serial months (non quarterly months). In addition to the outright individual contracts, the CME also lists a variety of products that enable one to initiate positions more efficiently on a particular segment of the yield curve. Some examples are orders known as *Packs and Bun*dles. Packs are the simultaneous purchase or sale of an equally weighted, consecutive series of four Eurodollar futures. Bundles are consecutive series of futures beginning with the front contract. Both packs and bundles are quoted by the average of net price changes from the previous day's close of the constituent contracts.

CME lists American-style call and put options on Eurodollar futures. There are several types of such options. Ouarterly Eurodollar options expire in the same month as the underlying futures. Serial options are listed for the two nearest serial months with the next quarterly futures as the underlying contracts. Midcurve options are options with short expiration on longer-dated futures. They expire one, two, or four years before the underlying quarterly futures expire. Option premiums are paid in full at the time of purchase, the so-called "*stock-type*" settlement.

Eurodollar options can be priced under the Black-Scholes model with dividend yield equal to the risk-free rate (see Black-Scholes Formula), and numerical methods are needed to evaluate the early exercise premium (see American Options). More complexity arises when considering the underlying futures that are highly correlated with the risk-free rate. We refer interested readers to [3] for a more detailed treatment of this subject.

Eurodollar futures and options are also traded at the Singapore Futures Exchange (SGX) and Euronext. The contracts traded at the CME and SGX are identical. Euronext adopts the "futures-type" settlement for options, where unlike the "stock-type", premium is not paid up front but marked to market. Oviedo [7] showed that early exercise is not optimal under "futures-type" settlement; therefore, Euronext options can be priced "as if" European-style.

## References

[1] Burghardt, G. (2003). The Eurodollar Futures and Options Handbook, McGraw-Hill.

- [2] Chicago Mercantile Exchange. *CME Eurodollar Future Brochure*, CME website, available at: http://www.cme. com/files/eurodollar futures.pdf
- [3] Henrard, M. (2005). *Eurodollar Futures and Options: Convexity Adjustment in HJM One-Factor Model*, available at SSRN: http://ssrn.com/abstract=682343
- [4] Hull, J.C. (2006). *Options, Futures, and Other Derivatives*, Pearson Prentice Hall.
- [5] Hunt, P. & Kennedy, J. (2000). *Financial Derivatives in Theory and Practice*, John Wiley and Sons.
- [6] Musiela, M. & Rutkowski, M. (2000). *Martingale Methods in Financial Modeling*, Springer.
- [7] Oviedo, R. (2006). *The Suboptimality of Early Exercise of Futures-Style Options: A Model-Free Result, Robust to Market Imperfections and Performance Bond Requirements*, available at SSRN: http://ssrn.com/abstract= 825104

[8] Piterbarg, V.V. & Renedo, M.A. (2006). Eurodollar futures convexity adjustments in stochastic volatility models, *Journal of Computational Finance* **9**(3), 71–94.

## **Related Articles**

## **American Options**; **Black–Scholes Formula**; **LIBOR Rate**.

YUHUA YU
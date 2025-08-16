## **Basket Options**

Equity basket options are derivative contracts that have as underlying asset a basket of stocks. This category may include (broadly speaking) options on indices as well as options on exchange-traded funds (ETFs), as well as options on bespoke baskets. The latter are generally traded over the counter, often as part of, or embedded in, structured equity derivatives.

Options on broad market ETFs, such as the Nasdaq 100 Index Trust (QQQQ) and the S&P 500 Index Trust (SPY), are the most widely traded contracts in the US markets. As of this writing, their daily volumes far exceed those of options on most individual stocks. Owing to this wide acceptance, QQQQ and ETF options have recently been given quarterly expirations in addition to the standard expirations for equity options. Options on sector ETFs, such as the S&P Financials Index (XLF) or the Merrill Lynch HOLDR (SMH), are also highly liquid.

If we denote by  $B$  the value of the basket of stocks at the expiration date of the option, a basket call has payoff given by  $\max(B - K, 0)$  and a basket put has payoff  $\max(K - B, 0)$ , where K is the strike price. Most exchange-traded ETF options are physically settled. Index options tend to be cash settled. Over-the-counter basket options, especially those embedded in structured notes, are cash settled.

The fair value price of a (bespoke) basket option is determined by the joint risk-neutral distribution of the underlying stocks. If we write the value of the basket as

$$B = \sum_{i=1}^{n} w_i S_i \tag{1}$$

where  $w_i$ ,  $S_i$  denote respectively the number of shares of the  $i$ th stock and its price, the returns satisfy

$$\frac{dB}{B} = \sum_{i=1}^{n} \frac{w_i S_i}{B} \frac{dS_i}{S_i} = \sum_{i=1}^{n} p_i \frac{dS_i}{S_i}, \quad \text{with}$$
$$p_i \equiv \frac{w_i S_i}{B} \tag{2}$$

Here,  $p_i$  represents the instantaneous capitalization weight of the  $i$ th stock in the basket, that is, the percentage of the total dollar amount of the basket associated with each stock. If we assume that these weights are approximately constant which is reasonable, it follows that the volatility of the basket and the volatilities of the stocks satisfy the relation

$$\sigma_B^2 = \sum_{ij=1}^n p_i p_j \sigma_i \sigma_j \rho_{ij} \tag{3}$$

where  $\sigma_B$  is the volatility of the basket,  $\sigma_i$  are the volatilities of the stocks, and  $\rho_{ij}$  is the correlation matrix of stock returns. If we assume lognormal returns for the individual stocks, then the probability distribution for the price of the basket is not lognormal. Nevertheless, the distribution is well approximated by a lognormal and equation  $(3)$  represents the natural approximation for the implied volatility of the basket in this case.

The notion of *implied correlation* is sometimes used to quote basket option prices. The market convention is to assume (for quoting purposes) that  $\rho_{ij} \equiv \rho$ , a constant. It then follows from equation (1) that the implied correlation of a basket option is

$$\rho \equiv \frac{\sigma_B^2 - \sum_{i=1}^n p_i^2 \sigma_i^2}{\sum_{i \neq j} p_i p_j \sigma_i \sigma_j} = \frac{\sigma_B^2 - \sum_{i=1}^n p_i^2 \sigma_i^2}{\left(\sum_{i=1}^n p_i \sigma_i\right)^2 - \sum_{i=1}^n p_i^2 \sigma_i^2}$$
$$\approx \frac{\sigma_B^2}{\left(\sum_{i=1}^n p_i \sigma_i\right)^2} \tag{4}$$

Implied correlation is the market convention for quoting the implied volatility of a basket option as a fraction of the weighted average of implied volatilities of the components.

For example, if the average implied volatility for the components of the QQQQ for the December atthe-money options is 25% and the corresponding QQQQ option is trading at an implied volatility of 19%, the implied correlation is  $\rho \approx (19/25)^2 = 58\%$ .

This convention is sometimes applied to options that are not at the money as well. In this case, in the calculation of implied correlation for the basket option, the implied volatilities for the component stocks are usually taken to have the same moneyness as the index in percentage terms. Other conventions for choosing the volatilities of the components, such as equal-delta or "beta-adjusted" moneyness, are sometimes used as well. Since the corresponding implied correlations can vary with strike price, market participants sometimes talk about the *implied correlation skew* of a series of basket options.

## **Further Reading**

Avellaneda, M., Boyer-Olson, D., Busca, J. & Friz, P. (2002). Reconstructing volatility, *Risk* **15**(10).

Haug, E.G. (1998). *The Complete Guide to Option Pricing Formulas*, McGraw-Hill.

Hull, J. (1993). *Options Futures and Other Derivative Securities*, Prentice Hall Inc., Toronto.

## **Related Articles**

**Correlation Swap**; **Exchange-traded Funds (ETFs)**.

MARCO AVELLANEDA
# **Cliquet Options**

Cliquet options can be broadly characterized as contracts whose economic value depends on a series of periodic settlement values. Each settlement period has an associated strike whose value is set at the beginning of the period. This periodic resetting of the strike allows the cliquet option to remain economically sensitive across wide changes in market levels.

## The Market for Cliquet Options

The early market in cliquet options featured vanilla contracts that were simply a series of forward starting at-the-money options. Rubinstein [4] provided pricing formulae for forward-start options in a Black-Scholes framework resulting in Black-Scho les pricing for vanilla cliquets. Cliquet products now trade on exchanges and the fore-runner to these listings were reset warrants, whose first public listings in the United States appeared in 1993 [5] and 1996 [1, 2]. Cliquet options are equally effective in capturing bullish (call) and bearish (put) market sentiments.

The current market for cliquet options accommodates a rich variety of features, which are sometimes best illuminated in discussions of pricing methods [6, 7]. The most actively traded cliquets are return-based products that accumulate periodic settlement values and pay a cash flow at maturity. The return characteristics and the price appeal of a cliquet can be tailored by adding caps and floors to the period returns and by introducing a strike moniness factor different from one. Defining the *i*th settlement value,  $R_i$ , in a call style cliquet by

$$R_{i} = \text{Max}\left(\text{floor}_{i}, \text{Min}\left(\frac{S_{i}}{S_{i}^{0}} - k_{i}, \text{cap}_{i}\right)\right) \qquad (1)$$

where  $floor_i$  is the one-period(local) return floor for period  $i$ ;  $cap_i$  is the one-period(local) return cap for period  $i$ ;  $S_i$  is the market level on the settlement date for period *i*;  $S_i^0$  is the market level on the strike setting date for period  $i$ ; and  $k_i$  is a strike moniness factor for period  $i$ .

The payoff at maturity is given by

$$payoff = Notional \cdot \text{Max}$$

$$\times \left( GF, \text{Min}\left(\sum_{i}^{n} R_{i}, GC\right)\right) \qquad (2)$$

where  $GF$  is a global floor;  $GC$  is a global cap; and notional is the principal amount of the investment.

The investor forgoes returns above the local cap and is protected against returns below the local floor. For the same investment cost, investors can participate in more of the upside return by raising the local cap at the expense of a lowered local floor and the increased exposure to downside returns.

# **Applications of Cliquet Options**

The periodic strike setting feature of a cliquet enables an investor to implement a strategy consistent with rolling options positions but without exposure to volatility movements. For example, an investor could buy a cliquet to implement a rolling three-month put strategy and be immunized against the future increase in options premiums that would accompany increases in volatility throughout the life of the strategy. Hence a cliquet provides cost certainty, whereas the rolling put strategy does not.

Cliquet products are often embedded in principalprotected notes, which combine certain aspects of fixed-income investing with equity investing. These notes guarantee the return of principal at maturity with the investment upside provided by the cliquet return. Retail notes would generally base investment gains on a broad market index such as the S&P 500 index. Principal-protected notes may further guarantee a minimum investment yield, which compounds to the value of the global floor at maturity. The guaranteed yield may be considered as part of the equity return, as it is in equation  $(2)$ , or it can be considered as part of the fixed-income return. In the latter case, the equity payoff in equation  $(2)$  would be modified as in equation  $(3)$ :

$$ayoff = Notional \cdot Max$$

$$\times \left(0, \text{Min}\left(\sum_{i}^{n} R_{i}, GC\right) - GF\right) \tag{3}$$

where the global floor now sets a strike on the sum of periodic returns.

#### Summary

p

We have discussed the general characteristics of cliquet options and illustrated the payoff for one commonly traded type of the cliquet. Numerous variations exist and can be tailored to give very different riskreward profiles. Some are distinguished in the market by specific names, for example reverse cliquets [3]. The customizability of cliquet options likely means we will continue to see product innovation in this area in the future.

## **References**

[1] Conran, A. (1996). *IFC Issues S&P 500 Index Bear Market Warrants*, November 26, 1996 Press Release, http: //www.ifc.org/ifcext/media.nsf/Content/PressReleases.

- [2] Gray, S.F. & Whaley, R.E. (1997). Valuing S&P 500 bear market warrants with a periodic reset, *Journal of Derivatives* **5**(1), 99–106.
- [3] Jeffrey, C. (2004). Reverse cliquets: end of the road? *RISK* **17**(2), 20–22.
- [4] Rubinstein, M. (1991). Pay now, choose later, *RISK* **4**, 13.
- [5] Walmsley, J. (1998). *New Financial Instruments*, 2nd edition, John Wiley & Sons, New York.
- [6] Wilmott, P. (2002). Cliquet options and volatility models, *Wilmott Magazine*, 6.
- [7] Windcliff, H., Forsyth, P.A. & Vetzal, K.R. (2006). Numerical methods and volatility models for valuing cliquet options, *Applied Mathematical Finance* **13**, 353.

RICK L. SHYPIT
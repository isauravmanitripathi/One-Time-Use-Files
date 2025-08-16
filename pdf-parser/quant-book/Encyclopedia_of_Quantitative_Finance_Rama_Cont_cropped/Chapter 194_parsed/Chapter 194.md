# **Credit Default Swap Index Options**

Portfolio credit default swaps (CDSs) referencing indices such as CDX and iTraxx are the most liquid instruments in today's credit market and options on these have become mainstream. A CDS index option (also called a *portfolio swaption*) is an option to enter into a portfolio swap as a protection buyer or a protection seller. A portfolio swap (also called a *CDS index swap*) is similar to a portfolio of singlename CDS all with the same coupon (for details, *see* **Credit Default Swap (CDS) Indices**).

Both portfolio swaps and swaptions are traded over the counter but are standardized. The conventions for how portfolio swaps are quoted and traded are important for properly valuing portfolio swaptions.

In this article, we outline the basic conventions and terminology for portfolio swaptions, explain the standard model used by most market participants, and briefly discuss other models and approaches.

### **Conventions and Terminology**

A portfolio swaption is an option to enter into a portfolio swap as a protection buyer (payer swaption) or a protection seller (receiver swaption). The swaption is defined by the underlying portfolio swap, for example, 5-year CDX.IG.11, the expiration date, and the strike spread or strike price. For investment grade portfolios, it is a convention to specify a strike spread, whereas for high yield portfolios a strike price is usually specified. Trading is primarily in options on 5-year portfolio swaps. Option maturities are less than 1 year, with most liquidity in 1–3 months maturities. The standard option expiration dates are the 20th of each month.

The strike, whether it is specified as a spread or as a price, must be converted by a simple calculation to determine the cash amount to be exchanged between the swaption counterparties upon exercise. The calculation is easiest when a strike price is specified:

Cash amount = Notional 
$$\cdot$$
 (Strike price  $-100\%$ )

− Accrued coupon *(*1*)*

The cash amount is paid by the protection buyer. The accrued coupon enters the calculation because portfolio swaps, by convention trade with accrued coupon, similar to the way bonds trade with accrued interest. To simplify the exposition, we ignore accrued coupon in the remainder of the article.

When a strike spread is specified, the cash amount is calculated using the standard CDS valuation model, for example, as implemented in the Bloomberg CDSW screen:

Cash amount = Notional · PV01·

*(*Strike spread − Coupon*) (*2*)*

The coupon is the fixed premium rate for the underlying portfolio swap. When valuing a portfolio swaption, it is important to respect the exact market convention for calculating the PV01 such as the flat spread curve convention (*see* **Credit Default Swap (CDS) Indices**).

Another important market convention is that if the swaption is exercised, the option holder will buy or sell protection on all names in the portfolio including those that may have defaulted before option expiration.

## **The Standard Model**

Now, suppose that *V* is the value at option expiration of owning protection on all names in the portfolio including those that have already defaulted. Option payoff at exercise is then

Payer swaption payoff at exercise

= max{*V* − Cash amount*,* 0}

Receiver swaption payoff at exercise

$$= \max\{\text{Cash amount} - V, 0\} \tag{3}$$

where the cash amount is calculated from the strike price as in equation (1) or from the strike spread using a CDS valuation model as in equation (2). The cash amount is not affected by defaults. In fact, if a strike price is specified, the cash amount is known with certainty before option expiration. If a strike spread is specified, the only uncertainty about the cash amount derives from uncertainty about the interest rate curve. However, when pricing portfolio swaptions, it is standard to assume that forward rates are realized.

To price a swaption, we must specify a stochastic model for *V* . In addition to assuming that risk-neutral valuation is proper [1, 3], the standard model is based on two minimal assumptions that are clarified further:

- 1. the spread of the underlying portfolio swap is lognormally distributed and
- 2. the model correctly prices a synthetic forward contract constructed by combining a long payer and a short receiver with the same strikes.

The standard model assumes that *V* is a function, *V (X)*, of a hypothetical spread:

$$X = E(X) \exp\left(-0.5\sigma^2 T + \sigma \text{ Normal}(0, T)\right) \quad (4)$$

where Normal(0*, T* ) is random normal variable with mean 0 and variance *T* (the time, in years, to option expiration), and *σ* is the free parameter that we interpret as the spread volatility. *E(X)* is the expected value of *X*. The function *V (X)* is the one found in equation (2) when the cash amount is seen as a function of the strike spread.

The swaptions are priced by discounting their expected terminal payoff (risk-neutral valuation). To understand where *E(X)* comes from, consider a payer and a receiver swaption both with a strike price of 100% or equivalently strike spreads equal to the coupon in the underlying portfolio swap. In this case, the cash amount in equation (1) or (2) is zero and the terminal payoff from a position that is long the payer and short the receiver is *V* . The value of this position is therefore

$$V_0 = D(T)E(V(X)) \tag{5}$$

where *D(T )* is the discount factor to time *T* (option expiration).

The value of a position that pays *V* , that is, *V*0, can also be determined from the credit curve of the underlying portfolio (potentially using the credit curves of all the names in the portfolio) since it is simply the value of owning protection on all names in the portfolio but only having to pay premium from option expiration onward. Once we have a value for *V*0, *E(V (X))* can be found as *V*0*/D(T )* and *E(X)* can be implied from this value. We can then price the swaptions using *σ* as the only additional parameter.

It is recommended to solve the model numerically to get the most accurate pricing. However, by making a few simple approximations (such as simplifying the expression for the PV01 in equation (2)) it is possible to derive approximate closed-form solutions that look like Black formulas.

See [2] for details on the model outlined above.

#### **Other Models and Approaches**

The standard model is a simple approach to what could be a very complicated problem. Instead of trying to model the credit curves and default of each of the names in the portfolio, the approach in the standard model is to model the hypothetical spread on the aggregate portfolio that also includes defaulted names. Thereby the model has only one free parameter, the aggregate spread volatility, and the approach becomes similar to using Black–Scholes for S&P 500 options. This analogy to the equity world suggests paths to the next generation of models such as introducing stochastic volatility and jumps or creating a model that starts from the individual credits by modeling their default, spread volatility, and spread correlation.

#### **References**

- [1] Morini, M. & Brigo, D. (2007). *Arbitrage-free Pricing of Credit Index Options*, Working Paper, Bocconi University.
- [2] Pedersen, C. (2003). *Valuation of Portfolio Credit Default Swaptions*, *Lehman Brothers Quantitative Credit Research Quarterly*, 2003-Q4, pp. 71–81.
- [3] Rutkowski, M. & Armstrong, A. (2008). *Valuation of Credit Default Swaptions and Credit Default Index Swaptions*, Working Paper, University of New South Wales.

#### **Related Articles**

**Credit Default Swaps**; **Credit Default Swap (CDS) Indices**; **Credit Default Swaption**; **Hazard Rate**.

CLAUS M. PEDERSEN
# **Emissions Trading**

There are numerous forms of environmental impact associated with human activity. The best known in the energy sector are emissions to air, particularly carbon dioxide, sulfur dioxide (SOx), nitrogen oxides (NOx), and other emissions such as mercury. Regulatory intervention can limit these emissions in a number of ways.

Our aim here is to show how management under the "cap-and-trade" regulatory mechanism for emission limitation can be partially modeled in terms of standard instruments for financial derivatives. We discuss briefly how similar modeling techniques can be applied to more complex environmental factors such as emission of particulates, impact on water, and impact on local amenity. The modeled entity is principally the price of the cap-and-trade allowance, and we also briefly consider the shadow price of other forms of environmental limits, and other features, such as the emissions cap and its allocation.

The politics, economics, and science of emissions impact and emission abatement, and the various regulatory schemes, are well covered in other texts and are not covered here. We offer a caveat here; while we characterize the microeconomics of emission abatement using supply and demand curves, we should be aware that the long-term nature of emission impacts are, in some aspects, more amenable to a classical economic analysis than the neoclassical analysis that standard quantitative approaches to derivative instruments necessarily entail.a Beyond the politics and economics, the essential challenge in the modeling of allowance prices in particular, is the capture of the essential features of the allowance, so that the pricing problem can be framed in terms of standard quantitative analysis of derivatives.

## **Regulatory Interventions**

The key methods for regulatory intervention can be divided into (i) technology prescription; (ii) instantaneous limits which are usually measured by instrumentation; (iii) annual limits which are commonly measured by estimation using the average composition of the fuel; and (iv) taxes and subsidies. Commonly, more than one intervention will apply.

An efficient form of regulatory intervention to optimize emission abatement is a tax at the marginal damage rate, if known accurately. See [6] this may be regional, periodic or otherwise varying across time, and stochastic according to the evolution of information. This is currently impractical for a variety of reasons including agreement on current benchmarks, definitions, and included sectors, changing purchasing power of international currency in different countries, and the difficulty in securing agreements.

In the pure cap system, each registered source (or collection of sources under one company) of emission has an annual limit that may not be exceeded and which is allocated, with or without cost, to emitters. Relative to the pure tax system, this system has the practical benefit of easier implementation, limited step change, and relatively straightforward definition of source, which can change over time. So, for example, international air travel can be included in the scheme after its inception. The total cap should, in theory, be increased as the emission comes within the scope of the scheme.

In the cap-and-trade system, each source is assigned an emission allowance for the compliance period.b The source can emit more if it purchases allowances from other sources, and can sell allowances if it can reduce its emissions below the cap. Initial allowances are commonly related to past emissions, and allocations are reduced over time. Ultimately, the free allocation of allowances can be reduced to zero, with the central administrator selling a fixed (i.e., maintaining a set amount of emissions) or variable (maintaining a set tax rate) amount of allowances.

Here, we pay attention to the quantitative analysis of allowance prices in the cap-and-trade system.

# **Framework**

From an analytic perspective, the most important features of the regulatory framework are as follows:

- The compliance periods—length and phase.
- Banking and borrowing—regulatory exchange rate between allowances in different compliance periods.c
- The use of "grandfathering" for allocation—the extent to which caps are dependent on historic emission.

- Allocation to new facilities and withdrawal for closing facilities.
- Buyout mechanisms—a penalty mechanism within the overall scheme, or government withholding of their allowance allocations, allowing a penalty mechanism within the country without affecting the global cap.
- Fines—for emitting without allowance.
- Relationship between schemes—allowed exchange between schemes, double count of emissions, and emissions missing from schemes.
- Recycling of fines, buyout, and other revenues to allowance "producers".
- Sequestration allowances for sinks.
- Coverage—countries, sectors, producers, and consumers.
- Restrictions and other scheme details—for example, in the United Kingdom, Climate Change Levy Exempt Certificates can be borrowed for only five periods in a row.

# **Using Supply Stacks**

Let us first assume that the only way to reduce the emission is to "switch on" a series of installed abatement technologies at the expense of a (upward sloping and curving) marginal cost. Assuming steady demand and a constant generation mix, the abatement "stack" can be simply represented. The effect of a rate limit in tonnes per day on the "production stack" of allowances is linearly related to the residual time in the compliance period (see Figure 1).

In the absence of banking and borrowing of allowances (which we treat as a 0% and ∞% intercompliance period exchange rate, respectively), then it is easy to see not only why allowance prices become extremely volatile as the end of the compliance period arrives but also how this volatility is itself volatile according to the prevailing use of technology (i.e., whether we are operating at the higher or lower cost part of the allowance production curve).

When considering the installation of new technology to produce allowances, we can treat each technology as having a capital and fixed cost (the option premium) and a marginal cost (the strike price for the technology owner). We expect our technology to endure across compliance periods and hence this creates a shadow exchange rate and option interdependence between periods. If we apply a simple rule that ensures an exact recovery of total fixed and variable costs in each compliance period, then the marginal price offered is stochastic according to the past and planned fixed cost recovery within the compliance period. So, for example, the offer cost from a technology may be lower if it has run at a high load factor during the compliance period and thereby recouped most of its fixed costs, or as a result of high forward prices within the compliance period the planned load factor is high and therefore the offer cost can be relatively low.

Allowances can be "produced" in a number of other ways including demand reduction, sequestration and offset, and banking and borrowing.

## **Sources of Uncertainties**

There are three principal sources of uncertainty:

- production cost stack
- demand for energy—high energy demand creates high allowance demand
- regulatory change.

![](_page_1_Figure_20.jpeg)

Tonnes "produced" over compliance period

**Figure 1** The cost curve for allowances in relation to the horizon to the end of the compliance period

Regulatory change uncertainties are (i) change in framework; (ii) change in coverage; and (iii) changes in the figures under the framework (cap, buyout price, banking and borrowing rates, etc.). These changes are themselves influenced by changing knowledge about damage rates, sector outputs, and political effects.

# **Price Characterization**

If there is no banking or borrowing across a compliance period, then the steepening of the abatement stack that can be applied to the residual period causes an increase in volatility. Since the compliance period is set in calendar time, rather than having a rolling horizon, the volatility term structure is therefore not stationary. Similarly for any nearby compliance period, there is no equilibrium price to revert to, although there are a number of reference prices, such as the short-run marginal cost of abatement, the fully loaded cost of abatement (loading the fixed costs onto the short-run marginal costs to ensure precise cost recovery over the compliance period), value of lost load, buyout prices, and gaming prices. An example of a gaming price is the price outcome from Cournot competition between allowance producers.

In the same way that monthly futures can be regarded as derivatives of forward price curves with daily resolution, compliance period allowances can be regarded as derivatives of the daily allowance price curve, which itself is constructed from the abatement stack. In common with futures, allowances can be regarded as "cheapest to deliver". There is never merit in submitting the allowance prior to the end of the compliance period, but due to the limit on the "production rate" of allowances, the rate of physical production of allowances can have complex structures within the compliance period. This is a standard optimization problem used, for example, in hydro reservoir optimization. The cost of capital should be taken into account when optimizing. The forward price curve for allowances in each compliance period is a discrete vector, with as many forward allowance prices as there are actual and expected compliance periods. To a degree, this allows us to treat the long-term problem as a "Bermudan" rather than "American" one, although the latent price structure within the compliance period is important.

- Long-term prices—since the economic theory is that the regulatory cap should be adjusted such that the cost of marginal abatement enacted is equal to the marginal damage rate, there is, in theory, a long-term equilibrium price. Indeed, since climate change has such universal impact, we may regard the optimal long-term allowance price as a, and possibly *the*, international numeraire asset.d However, the uncertainties surrounding the marginal damage rate, the difficulty of denominating the allowance in currency, and the difference between practically achievable allowance prices and the "ideal" price are such that the long-term price has a very high degree of uncertainty associated with it, and the long-term price can change on an instantaneous basis.e Hence we should regard the long-term price as highly volatile.
- Negative prices—market prices for allowances cannot have negative values, and hence allowances can be regarded as assets in this sense. However, under a pure cap regime, the shadow prices for allowances can be negative since ongoing allocations are related to past emissions, and production below the allocation risks an allowance reduction in future.
- Embedded options—schemes such as the Renewables Obligation scheme in the United Kingdom can have buyout prices, which allows the retail supplier to pay the buyout price instead of procuring allowances. So the cost is capped for retail suppliers, while the Renewable Obligation Certificate (ROC) price, created by the recycling of buyout revenues, is higher and volatile. However, if the cost of ROC production falls below the buyout price, suppliers will buy ROCs instead of paying the buyout. Therefore retail suppliers have embedded put options in their compliance costs. The compliance cost therefore has a stochastic element even if the buyout price is known.
- Government influence—there are a number of mechanisms that can be used by the government to adjust prices. For example, the government can allocate to sectors less than the national limit, leaving it with "hot air". This increases the cost of compliance. The government can then release the hot air at low or high prices to sectors of its choice. The impact on price depends on the effect that discretionary allocation has on physical production of allowances. Given that the market

solution in theory delivers the neoclassical optimum, then from a modeling perspective, government influence in allocation should be regarded as increasing allowance prices.

- Path dependence—the two key drivers to path dependence are the cost structures of emission abatement, and the effect of the fixed cap on emissions under conditions of stochastic energy consumption. We have already seen that if "allowance producers" recover their full costs in each compliance period, that their offer price above marginal costs depends on the fixed cost recovery to date. So, for them, high historic compliance prices have a depressing effect on forward allowance prices within the compliance period. The fixed volume of the cap has the opposite effect. If energy demand has been high in the early part of the compliance period, then emissions will have been high, and the residual cap volume will have been depleted, which has an elevating effect on allowance prices. The modeling of this is very similar to that for an energy complex, which has an element of fixed energy amount. An example might be a complex with hydro reservoirs and combined cycle gas turbines. We return to the swing modeling in an electricity context below.
- Cost of risk—the cost of riskf for traded commodities is the cost of risk of the marginal player. As the compliance period draws to a close, each player ensures that they are not short and places decreasing reliance on the market to close short positions. This may manifest itself as a substantial negative cost of risk (i.e., forward price above expectation price for the last submission date of the compliance period) in the medium short term, with a possibly positive cost of risk in the very short term as emission uncertainty decreases and installations hold (and can sell) long allowance positions. There are pressures for long-term risk to be in either direction. Allowance producers (who have positive cost of long-term allowance price risk) are commonly the same entities as the emitters (who have positive costs of long-term energy price risk).
- Hidden variables—the cost of abatement is highly dependent on the power generation technology mix operating. So, for example, low gas prices will cause combined cycle gas turbines to displace coal-fired power stations,

and the abatement stack will be dominated by technologies at coal plant. The allowance price depends on the price paths of the major fossil fuels (coal, oil, gas). A critical hidden variable is the amount of cap remaining in the compliance period.

# **Instrument Pricing**

Here we consider that the underlying commodity is the emissions allowance for some examples of exchanges, see Nordpool, European Climate Exchange and EEX, or its index price.

- Modeling—we have the usual mixture of static optimization, stochastic dynamic programming using multidimensional trees/forests, and semianalytic techniques available. Owing to the high degree of importance of hidden nonstationary variables<sup>g</sup> in influencing the forward allowance price, the application of one-factor Monte Carlo techniques should be undertaken with some caution.
- Options—emissions options are traded, with the main instrument being the European option. They are important because of the effect that allowance prices have on the operation of energy installations. This is best illustrated by using the capno-trade system with a single power plant as an example. Consider a simplified power station that is operationally flexible, never fails, has no variability in its emission abatement, and has a pure cap-no-trade regime. It can be regarded equivalently as a family of European fuel-plusallowance-to-power options with the internal market allowance price (i.e., the shadow price) adjusting such that the compliance period limit is exactly reached, or a family of European fuelto-power options with the number of exercises limited by the cap (variously called *swing, flexicap*, or *take or pay*). We note in each case that the option value is path dependent. If the key factor prices for electricity (coal, oil, gas, etc.) and the price of electricity are all regarded as exogenous to allowance prices, then the allowance price can be modeled using standard techniques for hydro reservoirs (the cap being treated as a reservoir, with limitations on physical production rate). In reality, these factors have interdependency that is high, periodic, complex, and variable. Across the

entire global energy complex, the emission limit, net of sequestration, is reached, but the modeling of this is excessively complex.

At any instant, optimization methods provide the efficient marginal and total cost of abatement to meet the cap. Dynamic marginal prices arise from exogenous shocks to the system, such as shock or to the cap limit. This visualization is particularly useful in assessing the codependence between the key factors and, in fact, the only truly exogenous factor in the early stages of the scheme is the cap itself. In the later stage, if the scheme is efficient, the exogenous factor is actually the allowance price.

- Intercompliance period swaps—the swap rate is determined by the caps, the abatement demand (caused by energy consumption), the abatement cost stacks in the two compliance periods, and the rules such as those on banking and borrowing and on interscheme fungibility such as the clean development mechanism for greenhouse gases.
- Compliance period swaptions—in the absence of banking and borrowing within the scheme, the swaption volatility is a result of (i) shared economics between the periods and (ii) activities that can "produce" allowances in one period at the expense of the other. In economics terminology, these are complements and substitutes, respectively. An example of the former is as follows: if a high allowance price in the nearcompliance period makes an abatement scheme attractive, then while the factors that made the near-period allowance price high might have a similar effect on the later period, the enactment of the abatement scheme might have a depressing effect on the allowance prices in the later period. An example of the latter is the use of physical and commercial storage in the energy complex. For example, if a full hydro reservoir is emptied in the first compliance period, then the carbon intensity of production will be low in this period and high in the next. The ability to adjust the release of water therefore has the economic result of storage of allowances, equivalent to banking and borrowing.

# **Intercommodity Price and Price Movement Relationships**

First consider a simple system in which we have one coal- and one gas-fired power stations in country, an in-country, cap-no-trade SOx regime for the coalfired stations, exogenously determined nonseasonal coal and gas prices, exogenously determined inelastic domestic demand for power, and an international capand-trade CO2 scheme. Let us simplify the problem by ignoring fixed costs and assuming that the power stations offer power at the variable cost of fuel and allowances. Finally let us begin by assuming that coal is cheaper than gas on an efficiency adjusted basis.

The number of hours that the power price is set by the coal price is set by the minimum of (i) the number of hours for which the coal-fired capacity is sufficient to satisfy demand; (ii) the number of hours that the coal-fired generation can run under the SOx cap; and (iii) the number of hours for which the coal price is less than the gas price.

Figure 2(a) shows this. First for a nonseasonal gas price, we can see that for the hours on the right, the CO2 price affects the power price by the effect on coal-fired costs (roughly speaking 0.9 t CO2/MWh), and for the hours on the left the CO2 price affects the power price by the effect on gas-fired costs (roughly speaking 0.4 t CO2/MWh). In the middle, the power price is raised as a result of the result on coal-fired hours, but this is mitigated by the lower carbon costs for gas-fired generation.

Figure 2(b) shows the impact of seasonality in gas prices. This can either increase or decrease the amount of gas-fired generation.

Here, we have taken the CO2 price as exogenously determined and examined the effect of power prices. If we instead wish to view the effect of demand variation, demand elasticity, gas prices, coal prices, SOx prices (or shadow prices), then we allow these to change and examine the effect on the volume of CO2 allowances consumed, and thence construct the stack of amount of CO2 allowances consumed in relation to CO2 prices to find the price elasticity of CO2 allowance demand.

## **Correlation and Cointegration**

Correlation term structures—we have noted a number of features that reduce the tractability of correlation analysis. These are as follows:

![](_page_5_Figure_1.jpeg)

Figure 2 (a) Impact of restriction on coal-fired hours on price setting plant. (b) Effect of gas price seasonality on the number of hours for which gas price is cheaper than coal

- 1. Path dependence.
- 2. The "fundamental" long-term "value" of  $CO_2$ allowances, associated with the uncertainty of this value and the difficulty of driving allowance prices to this value through adjustment of caps.
- 3. Complex co-integration relationships in the energy complex.
- 4. Nonstationarity of allowance price term structures.
- 5. Complex periodicity (daily, weekly, annual) in relation to the compliance periods.

While there are price or price return correlation measures that can be constructed, such as between commodities in the current or next compliance period, or between compliance periods, the nonstationarity and periodicity issues are such that it is very difficult

at this stage to apply this in a useful way for derivative pricing.

# **Other Kinds of Limits**

When running a power station fleet or other physical complex, with multiple commodity inputs and environmental and amenity impact outputs, it is helpful to construct shadow prices to optimize the profitability of the operation. The theoretical approach is to use Lagrange multipliers, and the equivalent effect can be modeled by optimizing the operation subject to constraints, which may vary. For example, the combustion of a coal that is low in sulfur, and therefore SOx, may entail high NOx, particulates, carbon in ash, and ash. Figure 3 shows this in generic form. where the limit for factor  $X$  could be of various forms.

![](_page_5_Figure_12.jpeg)

Figure 3 The shadow cost of complex environmental limits

such as height or temperature of water body, road traffic for bulk transport, or local air quality.

## **Conclusions**

- 1. For small complexes we can limit the number of exogenous variables. For example in a country with a SOx cap-and-trade, we initially model all technologies and costs as fixed. We then model the SOx price change from a shock to the cap, or fuel prices, or both.
- 2. For a large complex such as the European Emission Trading Scheme under the Kyoto protocol, the same methods apply in principle, but the exogenous variables are more complex. In the early stages of the scheme, the cap is the exogenous variable. In the later stage it is the monetized marginal damage rate.

## **End Notes**

a*.* There are two particularly important considerations here. First that the ambient trading price of allowances that results from the cap is not exogenously determined but is closely related to the societal damage cost of emissions, and secondly that the interest rate used for the damage cost is driven not by the rolled-up money market account in the Arrow–Debreu market economy but the intergenerational interest rate in the overlapping generations economy.

b*.* For an early description of the sulfur dioxide scheme in the USA, see [3].

c*.* This is socially efficient and refer to [5].

d*.* As mentioned in the beginning, we should be aware that the concept of a numeraire asset is less easily applied in classical economic analysis.

e*.* For fitting of jump modeling to EEX data, see [2]. f*.* This can be expressed in terms of convenience yield– see [1].

g*.* For empirical fits using GARCH modelling, see [4].

## **References**

- [1] Borak, S., Hardle, W., Tr ¨ uck, S. & Weron, R. (2006). ¨ *Convenience Yields for CO2 Emission Allowance Futures Contracts*, SFN Discussion Paper 2006-076. University of Berlin.
- [2] Daskalakis, G., Pychoyios, D. & Markellos, R. (2006). *Modeling CO2 Emission Allowance Prices and Derivatives: Evidence from the European Trading Scheme*, Athens University and Manchester Business School.
- [3] Joskow, P., Schmalensee, R. & Bailey, E. (1998). The market for sulfur dioxide emissions, *American Economic Review* **88**, 669–685.
- [4] Paolella, M.S. & Taschini, L. (2006). *An Econometric Analysis of Emission Trading Allowances*. Finrisk Working Paper 341.
- [5] Rubin, J. (1996). A model of intertemporal emissions trading, banking and borrowing, *Journal of Environmental Economics and Management* **31**, 269–286.
- [6] Weitzman, M. L. (1974). Prices vs. quantities, *The Review of Economic Studies* **41**(4), 477–491.

# **Further Reading**

European Climate Exchange www.europeanclimateexchange. com, 2008.

European Energy Exchange www.eex.com, 2008.

International Emissions Trading Association www.ieta.org, 2008.

Nordpool www.nordpool.com.

Powernext www.powernext.fr, 2008.

CHRIS HARRIS
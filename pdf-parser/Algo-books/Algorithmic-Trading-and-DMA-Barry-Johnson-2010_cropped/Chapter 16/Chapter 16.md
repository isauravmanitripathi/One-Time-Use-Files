# Chapter 15-Data mining and artificial intelligence

Trading is a complex process; markets keep getting faster and the volumes of data keep escalating. Data mining and artificial intelligence offer the potential to give traders an edge by spotting or predicting trends.

# 15.1 Introduction

Trading algorithms and execution tactics are inherently reactive, responding to market conditions based on predefined rules. In Chapter 10, we saw how they may be enhanced by using short-term prediction models for key market conditions, such as volume and price. These allow a more proactive approach, placing more passively priced orders.

However, in volatile markets, such as those during the 2007-09 financial crisis, sudden unexpected shifts can occur. These are hard to predict and can wrong-foot forecasts based on statistical analysis of historical data. Techniques such as data mining and artificial intelligence offer the potential to improve short-term predictions for key market variables, even during volatile markets. This is because they can incorporate a much wider range of factors in their forecast models. They may also be able to cope better with today's more complex marketplaces, where trading is fragmented between multiple venues.

Data mining is all about finding and confirming trends and/or relationships, some of which may be obvious whilst others may be much more subtle. Many of these techniques are purely statistical in nature. Certainly, much of the market microstructure analysis we have already seen in Chapters 8 and 10 may be viewed as a form of data mining. Likewise, textual analysis can be incorporated. So associations may also be inferred from information in news stories or company reports, as we saw in Chapter 14.

Artificial Intelligence (AI) systems are designed to adapt and learn, and so they can effectively think for themselves. There are two main types, namely conventional AI and computational intelligence. Conventional AI is a top-down approach, which applies logic and rules to make decisions. Essentially, trading algorithms are an example of conventional AI. Computational intelligence takes a bottom-up approach, and is inspired by biological mechanisms. For instance, neural networks try to reproduce the action of our brain's neurons, whilst genetic computation simulates evolution.

In terms of trading and finance, there are three main applications for these techniques: <sup>1</sup>

- Prediction
- Finding associations/relationships

 $^{1}$  As suggested in a review by Stephen Smith (1998).

Generating trading strategies

All of these are quite closely related. Prediction and association mining often use similar methods to find relationships in the data. These may form the basis of new trading rules or strategies. Artificial intelligence systems are able to test a huge number of variations in parallel, seeking the optimal solution. Hence, they can also help in the creation, testing and fine-tuning of rules for trading strategies/algorithms and their associated parameters.

In the following sections, we will review these techniques and survey some of the reports on their effectiveness, particularly for short-term forecasts. We will also consider how they might be incorporated to enhance execution.

# 15.2 Data mining

As its name suggests, data mining is all about data. By applying analytical techniques, trends and/or relationships may be found within data, or between different datasets.

## Data mining techniques

Dongsong Zhang and Lina Zhou (2004) provide a nice overview of data mining for the financial markets. There are several main types, namely:

- Classification and clustering analysis
- $\bullet$ Time-series mining
- Association rule mining  $\bullet$

These employ a range of different statistical analysis/inference methods. They may also incorporate AI-based mechanisms such as neural networks and genetic algorithms.

#### Classification and clustering analysis

Classification and clustering analysis both seek to identify common features in the data. Any commonalities may then be used for predictions, since if the results are known for one entity (or may be accurately estimated) they are likely to be comparable for those with similar properties. Note that often such predictions will focus on the direction rather than the potential value. For example, specific conditions might be used to determine whether a stock index or exchange rate will increase or decrease in a certain time span. These analyses may also be used for risk management or for spotting potential investments.

Classification may be strictly hierarchical, in which case properties such as country, currency, industry and sector are useful. Other factors such as the financial ratios (e.g. price to book) may also be used. Cluster analysis may also be applied to create intermediate hierarchies, based on results such as price returns or volatility.

Alternatively, a more geometric approach may be taken. This is often achieved using AIbased techniques, which we shall cover in section 15.3. For instance, the k-nearest neighbour algorithm classifies based on a majority vote from its neighbours. Likewise, probabilistic neural networks employ a weighted vote for each category based on the distance from test cases. Support vector machines may also be used to seek the plane/s which optimally separate/s any categories or clusters.

## **Time-series mining**

In finance, time series analysis is often used for forecasting. As we saw in Chapter 10, regression-based models, such as ARMA, are used to make short-term predictions for prices or volatility. Historical volume profiles are another example, using average-based models to estimate future trading volumes.

Time series analysis can also use factor models to try to identify any regular features, such cyclical or seasonal effects. Thus, data is often de-trended and normalised. Curve fitting techniques may be applied as well, using lagged data, simple moving averages or even Fourier transforms or wavelets to try to model the data. Transformations may also be used: shifting, scaling or warping the data to try to highlight any patterns. Due to the non-linear nature of many of these patterns, Al techniques, such as neural networks and support vector machines, have proved to be effective forecasting tools. We will cover this more fully in section 15.3.

In addition to purely quantitative forecasting, these techniques may also be used more qualitatively. For example, a common application is identifying turning points in the time series, to determine when a sudden change in direction is likely.

#### Association rule mining

Association rules are probably best known for their shopping basket examples. Supermarkets can use their huge databases to determine relationships, such as what type of milk customers will buy based on their choice of breakfast cereal.

In statistics, an association represents any relationship between two variables that makes them dependent. In terms of probability, this means the occurrence of one event makes it more likely that the other will occur. Correlation is often used to measure statistical associations. As we saw in Chapter 12, the correlation coefficient can be found by dividing the covariance of the two variables by the product of their standard deviations.

![](_page_2_Figure_7.jpeg)

![](_page_2_Figure_8.jpeg)

Figure 15-1 Association and causality

Note, it is important to differentiate between association and causality. A statistical association between two types of data is simply that; it does not imply anything more. Stephen Johnson (2008) illustrates this with two clearly unrelated datasets, namely the U.S. imports of fresh lemons from Mexico and the U.S. Highway fatality rate. Figure 15-1 shows a similar plot of lemon imports versus pedestrian fatalities for the period 1994-2000. For this sample, the correlation coefficient ( $\rho$ ) is -0.965. As we can see from the negative slope in Figure 15-1, there seems to be a significant negative association between the two, with fatalities decreasing as lemon imports increase.

When looking at associations, it is also important to consider the measure of confidence we can have in them.  $R^2$  is a statistical measure of the "goodness of fit" between different data sets. In the case of statistical models, it shows how likely future outcomes are to be predicted by the model. An  $R^2$  of 1.0 (or 100%) represents a perfect match, so the  $R^2$  of 0.93 means we can be confident that this association holds for this sample data.

However, can we really infer any link between lemon imports and traffic accidents? Even when we find a statistically significant association, it is difficult to prove a causal link. Probability models may quantify the likelihood of each occurrence, whilst Bayes' theorem helps to relate the conditional probabilities between two such events. Prediction models can also be used, to see if an event may be linked to subsequent events or specific reactions. Though, it is important to remember that we are still dealing in probability, not certainty.

## Finding patterns/associations

In Chapter 10, we saw how statistical analysis of historical data could be used to provide forecasting models for key market variables, such as price, volatility and liquidity. Much of this focussed on data for a specific asset. However, useful information may also be inferred from relationships between assets, both in the same market and across different markets or even asset classes. Data mining can help to find these associations, allowing us to create forecasting models that are based on a wider range of data.

Some of these associations are already well known, such as the beta of a stock versus its index. Others require some more work to find. For instance, lead/lag relationships may be found between some key sectors and the market as a whole, or in the supply chain. They can also exist between countries and between the cash and derivative markets. Therefore, automated data mining techniques provide a way of searching for useful or promising relationships. The results may then be examined more closely to see how viable they are as predictive indicators. They may also be related to other sources of information, such as news and macroeconomic indicators, as we saw in Chapter 14.

Relationships between assets and markets are also heavily dependent on market conditions. At the most basic level, many of the world's markets are driven by a mixture of fear and greed, which is why volatile conditions can so easily spread between markets. For example, the Mexican Peso crisis, the Asian currency crisis, Russia's devaluation, the collapse of LTCM, and the 2007/8 sub-prime debacle all led to substantial downturns, which spread across the world's markets. In such volatile times, tracking other key markets, such as the U.S., can be another useful predictive indicator. The "flight to quality" is a wellestablished phenomenon, with investors shifting to safer, or more liquid, assets during troubled times. Therefore, it can also be useful to look across asset classes, for instance during volatile markets investors may well shift to hold more bonds than equities.

#### Intra-market relationships

Many of the studies examining intra-market relationships have focussed on corporations, due to their ease of classification via industries and sectors.

A detailed study of the co-movements for U.S. industry sectors was carried out by Jarl Kallberg and Paolo Pasquariello (2008). They created a model for returns based on four fundamental factors. Three of these were the systematic risks identified by Eugene Fama and Kenneth French (1993): market, book-to-market and small-firm risk. The fourth factor was sector risk. They found a significant amount of excess co-movement, based on the covariation between asset prices. For some sectors, such as utilities and non-cyclical services, the excess was much higher than average. Whilst for others, such as general industrials, noncyclical consumer goods, financials and cyclical services, the excess was slightly below average. This is summarised in Table 15-1, which is ordered based on their findings.

|        | Sector                      | Examples                                                                                   |
|--------|-----------------------------|--------------------------------------------------------------------------------------------|
| Higher | Utilities                   | Electricity, gas distribution, water providers                                             |
|        | Non-Cyclical Services       | Food/drug retailers, telecom providers                                                     |
|        | Resources                   | Mining, oil and gas                                                                        |
|        | Information Technology      | Hardware, software and computer services                                                   |
|        | Cyclical Consumer Goods     | Automobiles, household goods and textiles                                                  |
|        | Basic Industries            | Chemicals, construction /building materials,<br>forestry and paper, steel and other metals |
|        | General Industrials         | Aerospace and defence, diversified industrials,<br>engineering and machinery               |
|        | Non-Cyclical Consumer Goods | Beverages, food producers, health,<br>pharmaceuticals, tobacco                             |
|        | Financials                  | Banks, insurance, investment companies                                                     |
| Lower  | Cyclical Services           | General retailers, leisure, media, transport                                               |

#### Table 15-1 Excess co-movement for specific sectors

Their fundamental model was only able to explain 27% of the excess co-movement for the market as a whole. Whilst for some sectors, such as resources and utilities, it was much more effective. Thus, a sizeable proportion of the co-movement was attributable to nonfundamental factors. However, there was also a considerable amount, which was not. Kallberg and Pasquariello went on to investigate some additional factors that might explain the remainder of the excess co-movement. They found that it was negatively related to market volatility and the level of short-term interest rates.

Co-movement also appeared to be negatively related to U.S. monetary and real output developments. Conversely, it was positively related to the dispersion and the number of analysts' carnings forecasts, which acts as a proxy for information flow. Momentum, contemporaneous and lagged returns were found to have negligible explanatory effects. Overall, these other factors were able to explain another 23% of the excess co-movement.

An additional factor that might help explain excess co-movement is firm size. Kewei Hou (2002) observed a significant lead/lag effect for stocks in the U.S., with the returns of large firms leading those of smaller companies. Lior Menzly and Oguzhan Ozbas (2004) found that for small and medium-sized firms cross-industry momentum could be significant, whilst it was negligible for larger firms (above the NYSE median market capitalisation cut-off).

The supply chain is another potential factor for relating the price moves between different sectors. A lead/lag relationship seems reasonable since problems with upstream suppliers could well affect the future returns of firms that are dependent on their goods. For instance, Y.L. Hsich, Don-Lin Yang and Jungpin Wu (2006) used genetic algorithms to analyse the price relationships between firms in Taiwan's technology industry. Rules were created based on the daily returns. Using these, they found they could predict future price changes with 60-70% accuracy. In the U.S., Menzly and Ozbas (2004) used the input-output survey from the Bureau of Economic Analysis to quantify the supply chain. They found a significant momentum from upstream and downstream industries. The effect from upstream industries was about double the size of the cross-industry momentum, whilst for downstream industries it was less, but still around 50% larger.

Certain industries can also act as an important indicator for the market as a whole. Harrison Hong, Walter Torous and Rossen Valkanov (2007) analysed the relationship between industry and market returns in a range of countries. For the U.S., they found that the returns from stocks in over a dozen industries showed a significant lead, of around a month, versus the market as a whole. In terms of economic significance, the banking sector led, followed by real estate, print, apparel and services. They also found a negative relationship for some of the resource-based industries, such as petroleum and metals. Overall, they concluded that the industries that lcd the market also acted as indicators of economic activity. A similar effect was found for other countries, including the U.K., Canada, Germany, and Japan, although there was more variation in the number of key industries.

#### Inter-market relationships

The intraday dynamics between international equity markets have been analysed by Kari Harju and Syed Hussain (2006a). Once the returns were deseasonalized, they found a correlation of 0.54 between the returns for the U.K. FTSE and the German DAX. Interestingly, this increased to 0.7 at around 15:30 Central European Time (CET), which coincides with the U.S. open. The significance of the U.S. open is also highlighted in a similar study by Harju and Hussain (2006), where they compared the average intraday returns for major European indices between days when the U.S. markets were open or closed. They found a clear shift in the returns at around 15:30 CET on the days when the U.S. markets were open.

Harju and Hussain (2006a) also used a vector autoregressive exponential GARCH model to analyse the volatility. They found that significant price spillovers from Germany and the U.S. rapidly spread to the U.K. The German market also affected U.S. returns, but they could find no evidence of the U.K. significantly affecting either the U.S. or Germany.

A similar analysis was carried out by Kate Phylaktis and Lichuan Xia (2008). They analysed the returns of stocks across Europe, Asia and Latin America. Overall, they found the Asian stocks to be more responsive to the US market than to the regional markets, whilst European and Latin American stocks showed more reaction to regional markets than the U.S. That said, a notable exception is information technology, which was found to be globally responsive for firms from every region.

Robin Brooks and Marco Del Negro (2003) broke down returns into global, country and industry specific components for stocks from 20 countries. They confirmed that the level of risk for a stock was dependent on its international exposure. A 10% increase in international sales was found to increase the stock's exposure to global shocks by  $2\%$ , whilst reducing its country specific risk by  $1.5\%$ .

## Cross asset class relationships

A lot of research has focussed on the lead/lag relationships that can exist between asset classes, particularly between cash and derivatives. The potential for arbitrage means that the price differences between markets should generally not be any larger that the costs of executing the arbitrage.

Jeff Fleming, Barbara Ostdiek and Robert Whaley (1996) analysed the relationships between stock indices and their futures or options markets. They found that the lead/lag return relations amongst these markets were consistent with their relative trading costs. The cost-efficient index derivatives appeared to lead prices in the stock market, in turn the prices of index futures tended to lead those of index options. Similar results were found in an analysis of the Korean KOSPI 200 index by Jangkoo Kang, Soonhee Lee and Changjoo Lee

(2004). They noted that both the futures and the options markets led the cash index prices by up to ten minutes, even when accounting for transaction costs. They also analysed the relationship for volatility and found the cash market again lagged the others, this time by around five minutes.

The lead/lag relationship for S&P 500 index options was analysed by Phelim Boyle, Soku Byoun and Hun Park (2002). They also found that the contracts led the cash index. In another study, Fleming, Ostdiek and Whaley (1996) noted that, in terms of the lead/lag relationship, the prices of index calls and index puts moved together. Though, analysis of short-term at-the-money (ATM) CAC 40 index options by Alexis Cellier (2003) noted a marked difference between calls and puts. The call options led the cash index by up to five minutes, although a significant effect was found to last for up to fifteen minutes. The puts were found to be more contemporaneous with the index.

For single stock options, Richard Holowczak, Yusif Simaan and Liuren Wu (2006), and Sugato Chakravarty, Huseyin Gulen and Stewart Mayhew (2004) analysed the price discovery with U.S. stocks. Both groups found stocks tended to lead options prices. Though, they also noted that during periods of substantial options trading the options market became more informative. In their study, Chakravarty, Gulen and Mayhew (2004) estimated that the option market's contribution to price discovery was around a fifth, so there was a meaningful two-way flow between the two markets. In earlier work, Matthew O'Connor (1999) also found that the stock market lcd the options market. He observed that the lead was related to the options' trading costs. Whilst Holowczak, Simaan and Wu (2006) noted that the increasing use of automated quoting algorithms by options market makers was helping increase the reliance on the stock market for prices.

The relationships between the corporate bond, credit default swaps (CDS) and stock markets were analysed by Lars Norden and Martin Weber (2005), for a sample of 90 firms from Europe, the U.S. and Asia. Stock returns were seen to lead changes in the spreads for both bonds and CDSs. They also found that CDS spread changes were likely to have more influence on bond spreads than vice versa. The stock market lead may be ascribed to its higher liquidity and trading volumes, as well as the relative case of shorting stocks. Similar results were found in an carlier U.S. based study by Francis Longstaff, Sanjay Mithal and Eric Neis (2003). They noted that both the stock and CDS markets led the corporate bond market. In their study, Norden and Weber (2005) found that CDSs were more sensitive to moves in the stock market than bonds, and this effect increased for firms with lower credit ratings. This additional sensitivity was explained by the fact that CDSs represent pure issuer credit risk, whilst bonds are a bundle of both credit risk and market risk.

For currencies, Tiffany Hutcheson (2003) analysed the differences between the intraday returns based on CME FX futures contracts and Reuters spot prices for the euro and the U.S. dollar. She found that the spot market led the futures market, within a 5-minute period.

The relationships for commodity prices were studied by Frank Asche and Atle Guttormsen (2001). They analysed the relationship between spot and futures prices for gas (or heating) oil on the International Petroleum Exchange (IPE). They saw that the futures price did indeed lead the spot prices. They also reported that the prices of futures contracts with a longer time to expiration led those that were closer to expiry.

#### **Crises and contagion**

The relationships that exist within and between markets can change considerably during extreme periods. In terms of intra-market relationships, research has shown that correlation tends to increase for downward moves, so this can be an important issue for forecasts.

Param Silvapulle and Clive Granger (2001) analysed the daily returns for the Dow Jones Industrial stocks between 1991-9. They confirmed that the correlation between them increased for large negative market movements, whilst there was no notable difference for large positive movements. They concluded that this reaction reduced the benefits of diversification, so in downturns portfolios can be exposed to more risk than expected. A similar increase in correlation during market falls was reported by Andrew Ang and Joseph Chen (2002). In their analysis of the correlations between U.S. stocks and the market as a whole, they noted the effect was strongest for the most extreme drops. They also found that the largest changes in correlation were for firms that were smaller, had seen low returns recently or could be categorised as "growth" stocks. A significant change was also observed for the traditionally defensive sectors, such as petroleum and utilities. Interestingly, stocks with lower betas were affected most; higher risk stocks were less affected.

Across markets, Donald Lien, Y.K. Tse and X.B. Zhang (2002) analysed the relationship between stock and futures markets for the Nikkei 225 index between 1995 and 1999. They found three clusters of structural changes. The first of these originated in the futures market, as we might expect; however, the other two were led by the stock market. They also found another structural shift in the stock market, although this did not seem to be large enough to affect the futures. Hence, the traditional lead/lag relationships that we saw in the previous sub-section do not always hold during crises.

A global increase in correlation has also been observed during crises. François Longin and Bruno Solnik (2001) used "extreme value theory" to derive the distribution of extreme correlations between the U.S., European and Asian stock markets. They established that the change in correlation was related to the market trend rather than the market volatility. Thus, correlation was seen to increase in bear markets but was less affected in hull markets. There was a notable shift in correlation for a drop of 10% whereas a rise of 10% behaved as expected. They concluded that the probability of having large losses simultaneously on two markets is larger than might be expected. Simón Sosvilla-Rivero and Pedro Rodríguez (2004) also studied the relationship between the S&P 500, FTSE 100 and the Nikkei 225 stock indices. They found that the S&P 500 seemed to lead the other two markets in terms of extreme positive or negative returns.

Research has also focused on how these crises spread across markets. For instance, a nice summary of the Asian currency crisis is provided by Jarl Kallberg, Crocker Liu and Paolo Pasquariello (2005). They examined both returns and volatility for currencies and stocks and tracked how the information shocks moved from country to country in the 1992-1998 time period. For volatility, they found that the first breaks actually clustered around the 1994-5 Mexican Peso crisis for Malaysia, Taiwan and Thailand. Volatility breaks were found for the other Asian countries towards the end of 1997. The equity markets were then affected by the currency volatility. Return shocks were found to affect Malaysia and South Korea in early 1998, these then spread across the rest of Asia. Phylaktis and Xia (2008) also examined both the Mexican and Asian crises in their sectoral analysis. They found that nearly half the sectors in Europe, Asia and Latin America were affected by the Mexican crisis. Yet, in the Asian currency crisis, they found no additional contagion in Europe or Latin America.

The effects of contagion have also been studied for the debt markets. Amar Gande and David Parsley (2005) analysed the publicly traded U.S. dollar denominated sovereign debt for 34 countries across Europe, Asia and the Americas. They found that, on average, a onenotch downgrade, such as from AA+ to AA, for a country's credit rating led to an increase in the spreads of sovereign bonds for the other countries. Assuming a 6% yield, they estimated this could lead to a change of 12 bps in the spread. They also found evidence for competitive

spillovers occurring, so a downgrade for a country with highly negatively correlated trade or capital flows to the U.S. actually led to a decrease in the spreads for similar countries.

During crises, there is often a "flight to quality". George Theocharides (2006) found evidence of this for U.S. bonds; resulting in wider spreads for corporate bonds and a drop in the yields for U.S. Treasuries. He also noted a tendency for older bonds to be traded during these periods. But for U.S. corporate bonds, he found that company specific shocks had negligible effects on the bonds from firms in the same industry.

Research is still divided about exactly how and why contagion occurs. Data mining has been applied to try to identify the causes of contagion. For example, it has been linked to the dynamics of economic fundamentals, such as interest rates. In fact, Robert Shiller (1989) found that a marked proportion of the excess covariance between U.S. and U.K. stocks could be explained by positively correlated interest rates. A nice summary of research into contagion is provided by Kallberg and Pasquariello (2008): Studies by Kathy Yuan (2005), Albert Kyle and Wei Xiong (2001) and Guillermo Calvo (2002) have focussed on liquidity shocks due to the trading activity of financially constrained investors. Other researchers such as Paolo Pasquariello (2007) and Jeff Fleming, Chris Kirby and Barbara Ostdiek (1998) have concentrated on investors' portfolio rebalancing activity. Both are probably contributory factors, although further research will be needed to fully quantify their relative importance.

#### Important precautions for data mining

Statistical analysis is an important tool, but it can also be a dangerous one. Indeed, there are lies, damned lies, and statistics, as popularised by Mark Twain (1907). As with any analysis, due care must be taken to check any potential relationships which may be discovered. It is essential to apply economic sanity checks and a wide range of testing before too much is read into any relationship.

Stefan Zemke (2002) provides a nice review of some of the potential pitfalls that should be considered when handling financial data. In particular, he emphasises the importance of the data pre-processing. To start with, we must be sure that the data quality is good enough. The old maxim "garbage in, garbage out" holds just as true for statistical analysis as for computer programs. Therefore, it is important to have checks in place to inspect and, if necessary, clean the data. Apparent outliers may in fact be genuine; they may be due to events such as stock splits or dividends. Similarly, missing data may need to be back-filled, or simply excluded.

Inferring relationships from data must also be done with some caution. Again, it is important to remember that any associations often simply reflect a probability, rather than a truly causal relationship: Just because one event has happened, it does not necessarily guarantee anything – although it may make related events more likely to occur. A commonly cited example is the "Texas sharpshooter" fallacy: If we just look at a target with several shots in the dead centre, we might assume that the shooter had a good aim. However, without having seen the shots we do not know how far they were taken from, or even whether the target was painted on afterwards! In other words, it is always important to check whether the discovered relationships make economic sense. This may also mean taking into account factors such as transaction costs.

For relationships to be meaningful, they must be based on a reasonably sized dataset. Two points can always be joined by a straight line (with an  $R^2$  of 1.0 or 100%). For instance, back in Figure 15-1 we saw that the data for U.S. lemon imports and pedestrian fatalities were very closely related, with an  $R^2$  of 0.93. However, this is only for annual results from 1994-2000; in fact, this range was chosen solely because it happened to give a high correlation and

 $R^2$ . If we expand the period up to 2008 the correlation drops to -0.554, with an  $R^2$  of only 0.31.

Another risk when data mining is the potential for over-fitting data. Essentially, this means that the discovered relationship works perfectly for the test data; but as soon as it is exposed to real data it gives completely useless results. For example, let's consider if there might be any link between the Dow Jones Industrial Average (DJIA) and U.S. traffic accidents from 1995-2007, as shown in Figure 15-2.

![](_page_9_Figure_3.jpeg)

Source: US DOT (2009)

Figure 15-2 The dangers of over-fitting data

Again, the correlation of  $-0.87$  and an  $R^2$  of 0.75 shows a reasonably close fit between these datasets. Maybe if we added some other datasets, a meaningful relationship might be found. David Leinweber (2000) carries out a brilliant example of this: he starts with the returns for the S&P 500, finding a reasonable fit with the level of butter production in Bangladesh, achieving an  $R^2$  of 0.75. Determined to improve the model he then found that incorporating U.S. cheese production and the sheep population of both countries raised the  $R<sup>2</sup>$  to 0.99 for the test period. Equally high  $R<sup>2</sup>$  were achieved for models using fitted polynomials based on the year's digits. So associations can be found hetween almost anything if you look hard enough.

Obviously, these are purposefully outlandish examples. Unsurprisingly, the relationships are non-existent outside the test period. However, Leinweber makes the key point that just because regression charts for interest rates or GDP seem plausible, the statistics can sometimes be just as meaningless. So when examining data, it is important to hold back a portion to allow for "out-of-sample" testing. Leinweber also suggests that this should be done on both a temporal and a cross-sectional basis.

# 15.3 Artificial Intelligence

The term Artificial Intelligence (AI) was first coined by John McCarthy in 1956 during a workshop on computers and intelligence at Dartmouth. AI systems are designed to adapt and learn, and so effectively think for themselves.

The progress of Al has certainly had its fair share of "ups and downs". Buoyed by early success in the 1960s AI seemed unstoppable. A brief slowdown in the 1970s was followed

by a surge in the 1980s as the sudden availability of personal computers helped it become more commercial. In fact, by 1985 the market for AI systems had reached a billion dollars, according to Daniel Crevier (1993). In the mid 1980s, AI systems spread to finance and more specifically trading, heralding the dawn of AI-driven automated trading. Although the harsh realities of dealing on the world's markets meant that many such systems became write-offs within a few years. Overall, a lack of results meant the honeymoon ended and much of the corporate and government funding for AI research disappeared.

The 1990s saw a resurgence of AI techniques, particularly in the technology industry. It again became headline news in 1997, when IBM's Deep Blue computer managed to heat the Grand Master Gary Kasparov at chess, nearly fifty years after the first AI researchers had begun. Unsurprisingly, financial applications for AI are once again being found.

## Types of artificial intelligence

AI can actually be split into two main approaches:

- Conventional AI
- Computational intelligence

Conventional AI is a top-down approach that uses logic and rules to make decisions. This generally relies on data that has been translated into known symbols, employing custommade knowledge bases or statistical analysis. Examples of conventional AI include expert and case-based reasoning systems, as well as Bayesian networks.

On the other hand, computational intelligence is a bottom-up approach that takes its inspiration from biological mechanisms. For instance, neural networks try to reproduce the action of our brain's neurons, whilst evolutionary computation simulates populations. Other examples are hybrid intelligent systems, which are a combination of neural and evolutionary mechanisms, whilst fuzzy logic offers probability based solutions.

#### **Conventional AI**

Conventional AI is generally based on logic. Experts define rules for how to identify specific situations and what actions to take in response to them. These may be broken down into simple logical statements: IF <this happens> THEN <do this> ELSE <do this instead>. Rules also need to be placed in context; hence, structures like decision trees may be used to ensure they are followed in a sensible order. Once enough of these are defined, a system has all the basics of how to cope. Obviously, though, there are some subtle nuances - there will always be situations that simply do not follow the rules.

All of this sounds rather familiar, since a trading algorithm is essentially a complex collection of rules each designed to respond to various events. The rules themselves have generally been determined by experienced traders or quants. So, in essence, a trading algorithm is just an instance of an AI expert system.

Conventional AI may be also used to make forecasts; however, the reliance on explicit rules means it is less adaptable than techniques involving computational intelligence.

#### Computational intelligence

Computational intelligence, or soft computing, applies an array of different techniques, using elements of learning, optimisation and adaptation/evolution.

Machine learning is used by computer systems to recognize complex patterns in data, and make intelligent decisions based on this. There are three main categories:

Supervised learning  $\bullet$ 

- Unsupervised learning
- Reinforcement learning

Supervised learning is adopted by many soft computing techniques, from the k-nearest neighbour algorithm to neural networks and support vector machines. During training, the ideal outputs are provided for test inputs. Hence, the learning mechanism will try to validate its own outputs against these target values. Repeated cycles should mean it optimises itself to produce output much closer to the ideal. With unsupervised learning, no test outputs are provided, so the mechanism must find another way to validate itself. Reinforcement learning takes a different approach: instead of using a dedicated training period, it relies on constant feedback from its environment. Some neural networks use unsupervised or reinforcement learning.

Optimisation is also important. For many problems, there is an optimal solution, which may be found by searching through the possible solutions. Computational intelligence may be employed to search the solution space more efficiently.

Likewise, adaptation is another key consideration. One of the downfalls of conventional AI is the fact that situations can arise for which none of the pre-determined rules fit. By being able to adapt, or evolve, computational intelligence has a better chance of dealing with such situations.

In the following sub-sections, we shall examine some of these methods in more detail, starting with the simplest k-nearest neighbour algorithm then progressing on to neural networks and support vector machines and finally genetic algorithms and programming.

k-nearest neighbour algorithm

The k-nearest neighbour (k-NN) algorithm classifies objects based on a majority vote from its closest  $k$  neighbours, where  $k$  is a small number. To start with, we need to seed the mechanism with some sample assignments. For instance, Figure 15-3 shows an example where objects have already been classified as type 1 or type 2.

![](_page_11_Figure_9.jpeg)

Figure 15-3 An example of k-NN classification

When classifying sample objects, if  $k = 2$  then A will be classed as type 1 since its closest two neighbours are both type 1, whilst B will be classed as type 2, as shown by the shaded circles. If we now use  $k = 5$ , for sample A three of the five closest neighbours are now type 2, so A would be reclassified as type 2. Although this is a simple 2D example, the concept may also be extended for multiple dimensions.

The k-NN mechanism may be used for regression as well, so the ideal value for our

sample object is based on the average values for its  $k$  nearest neighbours, each weighted by their distance from the sample. Note, there is very little training for the k-NN algorithm; it simply consists of storing the details for the seeded training samples. The rest is done in the elassification phase.

#### **Neural networks**

Artificial neural networks (ANNs), also known as neural nets, take their biological inspiration from the mechanism of neurons. The brain is a complicated network of interconnected neurons where information is passed by electrical stimulation. Signals are received by a neuron's dendrites, or branches, which in turn connect to many other neurons. If sufficient electrical signals are received, the neuron may become activated; in which case it will transmit a signal to other neurons via its axon. The human brain has around a hundred billion ( $10^{11}$ ) neurons whilst there may be 100-500 trillion ( $10^{12}$ ) connections (or synapses), based on estimates from David Drachman (2005).

Each node in a neural network mimics the biological structure fairly closely, as Figure 15-4 tries to show. A node takes inputs  $I_{1,2,3}$  which are then processed and the resultant output  $O_n$  is transmitted. The actual processing may be split into two, firstly summing the input data then determining what kind of output signal is appropriate (if at all).

![](_page_12_Figure_5.jpeg)

Figure 15-4 A neural network node

Note that the summation function applies distinct weights  $w_{l,2,3}$  to the corresponding inputs, so the signals from some connections may be given more importance than others. The activation function determines the appropriate output for the node, based on this input information. Often the activation function is a reasonably simple method that normalises the summed inputs to become a value in the ranges  $[-1, 1]$  or  $[0, 1]$ . This might be achieved with a threshold function (which will only output a set value if the inputs are more than a specific limit) or with continuous Gaussian, trigonometric or sigmoid functions.

The node shown in Figure 15-4 is effectively an example of a perceptron, which was invented by Frank Rosenblatt in 1957. By itself, this is of limited use; however, when multiple nodes are connected together the resultant networks can be much more powerful and versatile. Figure 15-5 shows some example networks where each circle represents an individual node. In turn, each of these nodes may be classed as being input, output or hidden. Generally, there is one input node for each variable being investigated. The number of output nodes will depend on the information that the network must generate. In between these, there may be any number of hidden nodes, acting as the intermediate steps in the transition from input to output data. They are often arranged in layers, although grids may be used as well.

![](_page_13_Figure_1.jpeg)

Figure 15-5 Example (a) feed-forward and (b) recurrent neural networks

The overall size of a network is an important consideration. Too few nodes and it may fail to fit the data well enough, too many and it becomes a significant computational burden. There is also the risk of over-fitting data, which can lead the network to start modelling random noise. Unfortunately, there is no real consensus on exactly how best to size a network. As a rough rule of thumb, Lou Mendelsohn (1993) suggests using between half and double the number of input variables as hidden nodes.

That said, the architecture of a neural network is much more than just how many nodes it employs. It also specifies how the nodes are interconnected and how signals flow through the network. In terms of how signals flow through networks Figure 15-5 shows the two main types, namely feed-forward and recurrent. Feed-forward networks process signals in a linear fashion. So they are organised much like the internals of each node. Recurrent networks allow signals to flow in both directions. Nodes may connect to themselves or even nodes in earlier layers, as we can see in Figure 15-5(b). These feedback loops mean that recurrent networks can retain additional state information, allowing them to better adapt to input signals that change over time.

There is also a range of other architectures catering for specific applications, such as probabilistic and general regression neural networks. For more details of these approaches, a nice overview is provided on the DTReg (2008) website and by Joarder Kamruzzaman, Rezaul Begg and Ruhul Sarker (2006).

The training of the network is also an important consideration. Back propagation is a commonly adopted method for supervised learning. The error value is the difference between the output value and the desired figure. In back propagation, this error value is passed backwards through the network, so that each hidden node can then compare this with its own inputs to see how strongly these relate to the required output. The hidden nodes then modify the weights for these to reduce the overall error. After a series of cycles, the weightings should be optimised.

One of the disadvantages of neural networks is their "black box" nature. After training, a model may provide useful results, but to determine how this has been achieved means decoding the various weightings to discover the relationships. That said, interpreters can be created to handle this; indeed, researchers have been using other AI techniques, such as genetic algorithms or programming, to do this automatically.

#### Support vector machines

A support vector machine (SVM) classifies objects by seeking the plane that optimally separates them. For example, Figure 15-6(a) shows the classification problem we considered back in Figure 15-3. The solid line marks a plane between the two types.

![](_page_14_Figure_4.jpeg)

Figure 15-6 Examples of SVM (a) classification and (b) regression

SVMs may also be applied to regression, as shown in Figure 15-6(b), by using Vladimir Vapnik's (1995) error-insensitive loss function. The bold line represents the best plane for the data values, from which we can actually interpolate the ideal values. The dotted lines show additional boundaries that incorporate a maximum permitted error. Any data outside this boundary is effectively ignored.

The examples shown in Figure 15-6 have straightforward linear solutions; however, SVMs are also able to deal with problems spanning multiple dimensions. For a more detailed review of SVMs Kristin Bennett and Colin Campbell's (2000) report is a good starting point.

In many ways, SVM models are actually quite similar to neural networks, although their training is very different: Essentially, it is like solving a quadratic programming problem with linear constraints. So for optimisation problems this means that a unique and globally optimal solution will be found. There is no risk of solutions reaching local minima, which can happen with techniques like back propagation.

## **Evolutionary computation**

Evolutionary algorithms are based on the theory of natural selection, first proposed by Charles Darwin (1859). Traits or properties that are successful become increasingly common over successive generations of a population. This is due to the increased likelihood of survival of individuals with those traits. Evolution relies on the transmission of these traits by genetic inheritance, as well as the innovation provided by mutation.

Computer simulations of evolution started in the 1950s, but one of the most well known models is still John Conway's (1970) Game of Life, a deceptively simple grid-based cellular automaton.

#### **Genetic algorithms**

Genetic algorithms (GAs) became popular in the 1970s, most notably based on work by John Holland (1975). For GAs, the population of individuals represent potential solutions to a given problem. A fitness function is used to gauge the quality of each individual. Evolutionary cycles are then repeated, with selection biased to ensure that the next generation is based on those with the highest scores. A nice summary of this cycle is provided by Jin Li and Edward Tsang (1999):

- Create an initial population. 1.
- 2. Assess the fitness of each individual. (a)
  - Select the set of parents for the next generation. (b)
  - (c) Create a new generation of individuals.
- 3. Repeat step 2 until the required cycles are completed or the time is up.

The aim is that once these iterations are finished the population should be dominated by the highest scoring individuals, and so hopefully the hest potential solutions for the problem. Though, this does not guarantee that the global optimum will be reached.

Each individual in the population may be defined as a sequence of genes, which in turn correspond to a set of specific settings or parameters for the required solution. Often these are encoded in a binary fashion, as shown in Figure 15-7:

# 0 1 0 0 1 1 1 0 0 0 1

#### Figure 15-7 Binary representation for an individual GA solution

This is because the bitwise format is very easy to manipulate when simulating reproduction and mutation. The reproduction is based on a genetic crossover, as shown in Figure 15-8(a): The genes of each parent are cut in two at some random point (marked by the dotted line) and then spliced with the corresponding remainder from their partner. This generates siblings that share parts of each parent's characteristics.

![](_page_15_Figure_12.jpeg)

Figure 15-8 Examples of GA (a) reproduction and (b) mutation

The fitness function is obviously central to finding good solutions. Often determining the fitness of a potential solution will entail running a separate simulation. For instance, the individual's settings might correspond to settings for a set of trading rules. These will then need to be back tested to determine their effectiveness. Only then may the overall fitness be rated.

Since there is the danger that the population might simply revolve around a single good solution, it is also important to incorporate mutation, which adds the potential for completely new variants. As we can see in Figure 15-8(b), with a bitwise implementation this is extremely simple, since all we need to do is toggle the value at random points. Mutation helps increase the potential for the population to span a wider range of possible solutions. and so scan more of the search space for the optimal solution. An alternative to mutation is to use immigration, in which case completely new individuals are randomly generated and introduced into each cycle, as suggested by Jurgen Branke (1999).

#### Genetic programming

Genetic programming (GP) is a natural progression of the work done by genetic algorithms. Instead of relying on simple bit-strings, the individuals are based on more complex data structures, such as trees. This allows even more sophisticated modelling. The early work in this field was led by John Koza (1992). Initially, much of the focus was on evolving actual computer programs; however, this has since expanded to encompass fields as diverse as quantum computing and electronic design.

Tree-based structures are ideally suited for mathematical expressions, for example, Figure 15-9(a) shows a tree for the equation  $(8 * ((3 + 2) / 4))$ . Similarly, they may be also be used to encode trading rules. For example, Figure 15-9(b) shows a trading rule that requires the Bid price to be less than 10 and the corresponding size to be more than 500.

![](_page_16_Figure_4.jpeg)

Figure 15-9 Example trees for (a) mathematical and (b) trading rules

Processing for genetic programming is just as with genetic algorithms. Crossover and mutation are essentially the same, except that it is based around nodes of the tree rather than bits in the bit-string. Potential issues with this approach are that over a reasonable number of cycles the trees can become quite complex. In addition, some crossovers or mutations may lead to defunct expressions such as  $1 = 1$ . Note that it is important to leave the trees alone during testing. This is because further crossovers and mutations can easily change defunct expressions to become useful ones, as Jean-Yves Potvin, Patrick Soriano and Maxime Vallée (2004) point out.

## Predicting data and trends

In terms of applications, AI has often been used as a forecasting tool. This expands on the forecasting techniques we saw in Chapter 10. Again, the goal is to enhance execution rather than find investment opportunities, since when an order is received the decision to buy or sell the asset has already been made. Hence, we will focus on short-term predictions of market conditions. The results of these predictions may be used within cost or risk models as a factor in determining order choice and placement. These should help the algorithms/tactics decide on an appropriate level of aggressiveness. Note that for such decisions directional trends can be just as useful as actual numbers.

#### Predicting asset prices

Understandably, much of the research has focussed on forecasting asset prices. In terms of AI-based models, neural networks are the commonest approach, although support vector machines are increasingly being adopted.

#### Price prediction with neural networks

Neural networks were first applied to stock price prediction in a study by Halbert White (1988). He employed a feed-forward network to analyse the daily stock returns of IBM in order to test the Efficient Markets Hypothesis (EMH), which asserts that asset prices follow a random walk. Although no predictive rules were found, his research highlighted the potential for such analysis. Indeed, a later study of six other U.S. stocks by George Tsibouris and Matthew Zeidenberg (1995) found some predictive ability from historical prices. Further prediction studies of stock returns, such as those by Apostolos-Paul Refenes, Achileas Zapranis and Gavin Francis (1995) and Manfred Steiner and Hans-Georg Wittkemper (1995), found that neural networks outperformed comparable statistical techniques, such as regression models. Some studies have even incorporated aspects of technical analysis, for instance, K. Kamijo and T. Tanigawa (1990) used an Elman recurrent network to predict stock prices for Japanese stocks. Their method sought to find triangle patterns to determine whether price rises might be permanent, based on historical highs, lows and closes.

Predicting stock indices has been a particularly popular area of research. Amol Kulkarni (1996) performed a study of the S&P 500, with weekly data covering both the crash of October 1986 and the bull run of 1994. His network was a straightforward feed-forward net, with 19 input neurons and a single hidden layer of 7 neurons. The model incorporated both short- and long-term interest rates together with historical prices. It was trained with 275 weeks of data. He found that for out-of-sample testing the network gave reasonable predictions one week ahead of the actual index, as shown in Figure 15-10.

![](_page_17_Figure_3.jpeg)

Figure 15-10 Predicted values for the S&P 500 (a) during the 1986 crash and (b) the 1994 bull run

It also correctly predicted the overall price trend 65 out of 75 times for the period of the 1986 crash, and 43 out of 50 times for the 1994 bull-run. In particular, he ascribed its success over the period of the 1986 crash to having incorporated the effect of rising long-term interest rates, since there was no hint of this from the index price trends.

In their study of the S&P 500 index, Tim Chenoweth, Zoran Obradović and Sauchi Lee (1995) also used interest rate data, namely the US Treasury rate, lagged by two and three months. They employed two separate neural networks, which were trained with either upward or downward trending index data. The quality of the prediction was found to be sufficient to yield an annual rate of return close to 15%.

Another study which looked at both "bull" and "bear" markets was carried out for the Madrid stock market's General Index by Fernández-Rodríguez, González-Martel and Simón Sosvilla-Rivero (2000). They used a feed-forward network with nine inputs for the previous

close prices and a single hidden layer with four neurons. Their results proved superior to a simple buy-and-hold strategy; although incorporating transaction costs showed the ANN underperformed buy and hold during bull markets.

Other factors have also been incorporated into models, such as FX and the prices of other major indices. Thomas Ankenbrand and Marco Tomassini (1995) carried out a study of the Swiss Performance Index. Their model incorporated interest rates, relative performance to the S&P 500 and the DEM/USD exchange rate, due to the importance of exports for Swiss companies. Overall, the prediction accuracy was around 70% out-of-sample.

Technical indicators such as moving averages and RSI were also used as input together with the historical prices for the main indices on the Kuala Lumpur stock exchange by Jingtao Yao, Chew Lim Tan and Hean-Lee Poh (1999) and Yao and Poh (1995). They tested feed-forward networks with back propagation for a range of different network configurations. Networks with two hidden layers seemed to give the best results, both in terms of accuracy and from paper-trading profits. Overall, they estimated that annual returns of up to 26% could be achieved from these predictions for the 1990 data, taking into account 1% transaction costs.

Using neural networks for predicting prices is not solely limited to equities; they have been applied to most of the major asset classes, such as bonds, FX, futures and options.

Forecasts of U.S, U.K and German 10-year government bond yields were made by Christian Dunis and Vincent Morrison (2004). The inputs for their ANN-based models incorporated a range of daily close prices for 2001-3, including currencies, leading stock indices and commodities like oil. They actually found the ARMA model to give consistently more accurate predictions; however, the ANN-based models proved to be the best at predicting the directional trends. Hence, their trading simulation actually saw the most profit from the ANN-based models.

A study of the U.S. dollar/euro exchange rate, using daily data from 1994-2001, by Christian Dunis and Mark Williams (2003), noted that ANN-based models outperformed statistical techniques such as ARMA. The exchange rates for six different currencies versus the U.S. dollar were modelled by Yao and Tan (2000), using weekly moving averages from 1984-95 as inputs. They found that for most of the currencies the neural network outperformed ARIMA based models, reaching accuracies of over 70% with relatively low deviations. Similar results were found by Joarder Kamruzzaman and Ruhul Sarker (2003), in their study based on a range of currencies versus the Australian dollar. Weekly data was used with training over 500 weeks. Two of the out-of-sample forecasts (spanning 65-weeks) are shown in Figure 15-11. Another feature of their research was the comparison of a range of learning mechanisms. They reported that scaled conjugate gradient-based learning gave significantly better results than back propagation.

The short-term dynamics of daily prices for S&P 500, Libor and Deutsche Mark futures were analysed using Elman recurrent networks by Ludmila Dmitrieva, Yuri Kuperin and Irina Soroka (2002). The best predictions were achieved for the S&P 500. Similarly, ANNs were used to predict NYMEX crude oil future prices by Saeed Moshiri and Faezeh Foroutan (2004). Their ANN-based predictions outperformed both ARMA and GARCH models.

Neural networks have also been applied for predicting the prices of options. Gunter Meissner and Noriko Kawano (2001) forecasted the daily prices of options on ten U.S. hightech stocks from 1999-2000. They compared standard feed-forward networks with those based on radial basis functions (RBF) and probabilistic and generalised regression networks. The inputs were based on those for the Black Scholes model, so they used the ratio of the spot to the strike price, the maturity, the risk-free rate and a GARCH estimate of the volatil-

![](_page_19_Figure_1.jpeg)

Figure 15-11 ANN based 65 week currency forecasts

ity. The standard feed-forward networks performed best, outperforming all the other types including the standard Black Scholes model. Subrata Mitra (2006) also saw improved performance when using an ANN to modify the Black-Scholes based pricing model for call options on India's Nifty stock index. Whilst Alex Faseruk and Lev Blynski (2006) used a simple back-propagation ANN to forecast the price of the OEX S&P 100 index option from the CBOE, using data from 1986-93. They also noted that the ANN model outperformed the conventional Black-Scholes pricing model when both were based on historical volatility. Switching both models to use implied volatility gave improved results; although the ANN's relative outperformance was less.

Most of the examples, so far, have been based on feed-forward or recurrent networks, but other types have also been successful. For example, a probabilistic neural network was used to predict the Singapore Stock Price Index by Steven Kim and Se Hak Chun (1998). Whilst Sung-Suk Kim (1998) used a time delay recurrent network to forecast the Korean Stock Market Index.

#### Price prediction with SVMs

Support vector machines (SVMs) have also been applied to forecast prices. A study of the Nikkei 225 stock index, using weekly data from 1990-2002, was performed by Wei Huang, Yoshiteru Nakamori and Shou-Yang Wang (2004). They compared the SVM's predictions with an Elman recurrent neural network and found that the highest accuracy was achieved by the SVM  $(73\%)$ , followed closely by the neural net  $(69\%)$ . A similar analysis was performed for six major Asian stock market indices by Wun-Hua Chen, Jen-Ying Shih and Soushan Wu (2006). They used SVMs to predict the returns for the Nikkei 225, Australia's All Ordinaries, Hong Kong's Hang Seng, the Singapore Straits Times, Taiwan's weighted index and Korea's KOSPI indices. Daily close prices were used with test data from 1984-2001. For comparison, they also tested auto regressive (AR1) models and back propagation (BP) neural nets. Overall, they found mixed results for the performance of both SVMs and neural nets. In terms of accuracy, the SVM models performed better for the indices in Hong Kong, Taiwan and Korea, whilst for Japan and Singapore the neural nets were better. In out-of-sample testing there was no appreciable difference between the two models for Australia, as shown in Figure 15-12. Both SVMs and neural nets performed better than autoregressive models, except for predicting the direction of returns.

Tony Van Gestel *et al.* (2001) used least squares SVM regressions to predict the time series and related volatility for U.S. short-term interest rates, as well as the German DAX

![](_page_20_Figure_1.jpeg)

Source: Chen, Shih and Wu (2006) Copyright 2006 Inderscience Enterprises Ltd. Reproduced with permission

## Figure 15-12 A comparison of the relative differences in percentage of price (RDP) for the All Ordinaries index

stock index. The accuracy of prediction for the sign of future returns was over 5% higher for the SVM models compared to both autoregressive (AR) and GARCH methods.

SVMs have also been used to predict the prices of futures, Francis Tay and Lijuan Cao (2001) studied five contracts, covering both stock indices (S&P 500 and CAC 40) and major government bonds (U.S. 10 and 30 year, and German 10 year bunds). Daily close prices were used with a training period of over 900 days. A neural network was used for additional comparison. Overall, the forecasts from the SVMs were better than from the neural net. The deviations from the actual were smaller and the predictions of the directional trend were more accurate.

For option prices, Michael Pires, Tshilidzi Marwala (2007) found that SVM's offered the most effective price forecasts for American options, with significantly less deviations when compared to ANN-based models.

#### **Predicting volatility**

R. G. Donaldson and Mark Kamstra (1997) created a non-linear GARCH model, based on a neural net, to study the return volatility of stocks from the U.S., Canada, U.K. and Japan. They found that the neural network captured volatility effects overlooked by traditional GARCH and EGARCH methods.

For stock indices, Fernando Gonzalez Miranda and Neil Burgess (1997) used neural networks to predict the intraday volatilities from Spain's IBEX 35 index options. Again, the networks were found to outperform more traditional linear methods. Apostolos-Paul Refenes and Will Holt (2001) also found that neural networks generally outperformed other statistical methods for volatility prediction. Likewise, a study by Peter Tiňo, Christian Schittenkopf and Georg Dorffner (2000) found neural networks effective in predicting the volatility of the U.K. FTSE and Germany's DAX stock index options. Though, they noted that on average simple binary Markov models outperformed both GARCH and neural network based techniques in simulated trading tests.

Valeriy Gavrishchaka and Supriya Banerjee (2006) used a support vector machine to forecast the volatility of the S&P 500 index. They found that it was comparable to be best GARCH model across different volatility regimes, and even outperformed GARCH in some.

Currency volatility was modelled by Christian Dunis and Xuehuan Huang (2002). They used both feed-forward and recurrent neural networks to predict the volatility of the British pound and the Japanese yen versus the U.S. dollar, using daily data from 1993-99. Again, both the ANNs performed well compared to GARCH models, giving the best simulated trading results. The recurrent networks marginally outperformed the feed-forward ones in terms of directional accuracy. Overall, though, the highest accuracy was achieved by a combination model that incorporated both the neural and GARCH estimates.

Even the volatility for options on index futures has been analysed. Shaikh Hamid and Zahid Iqbal (2004) used ANNs to study the S&P 500, using daily prices from 1984-94. They found that the volatilities from the neural network outperformed implied volatility forecasts, and were not significantly different from realized volatility.

More exotic neural models have also been used to predict volatility. For instance, Dirk Ormoneit and Ralph Neuneier (1996) used a conditional density estimating neural network to predict volatility of the DAX. They found that this outperformed a standard feed-forward network. Similarly, a mixture-density network was applied to the DAX index by Christian Schittenkopf, Georg Dorffner and Engelbert Dockner (2000). This is essentially a set of neural networks used to estimate the parameters for a mixture density model. They found that their predictions had a higher correlation with the implied volatilities than those of the GARCH model. In an earlier work Schittenkopf, Dorffner and Doekner (1998) also studied the volatility of the Austrian stock market.

Genetic programming (GP) has been used to forecast volatility as well. In a study of the S&P100 index, using intraday data from 1987-2003, Irwin Ma, Tony Wong and Thiagas Sankar (2007) found they could achieve 75-80% accuracy within a hundred generations. Wo-Chiang Lee (2006) used both ANN and GP models to forecast the volatility of Taiwan's TAIEX index. He found that empirically both types performed reasonably well in forecasting out-of-sample volatility compared to other methods, such as GARCH.

#### **Predicting volume**

A study forecasting the total daily trading volume on the NYSE was carried out by Blake LeBaron and Andreas Weigend (1994). They applied a bootstrapping, or resampling, technique, to simple feed-forward networks. The inputs were the aggregate turnover and the level of the DJIA. The turnover was detrended by dividing by its 100-day moving average. (Note logarithms were used to ensure the distributions of the input series were less skewed.) Contrary to their expectations, they found that the neural network did not give a marked improvement over standard linear models, although they reasoned that better results might be achieved by using additional forecast variables.

More promising results were found in a subsequent study of trading volume for six futures contracts on the on the Winnipeg Commodity Exchange by Iebeling Kaastra and Milton Boyd (1995). They again used feed-forward networks, but with an expanded set of input parameters. These were individually selected as predictors for futures trading volume. So the models were based on lagged trading volume, the futures price volatility, open interest and the average cash price as well as a proxy for the overall hedging demand. The neural network outperformed both naïve and ARIMA models, providing forecasts for up to nine months into the future.

# 15.4 Incorporating in trading strategies

Trading algorithms and execution tactics can adapt to market conditions. Limit order models may be used to determine the execution probability of orders, whilst cost-models help estimate the potential market impact and risk associated with a trading strategy. Hence, it is not a great leap to consider adding short-term forecast models. These may also be used to augment models for execution probability and/or cost estimates.

Algorithms may be broken down into specific trading rules. Generally, these are defined by experienced traders, or quants, based on experience of what works best for a specific market. Often this requires a substantial amount of testing and fine-tuning. Artificial intelligence systems offer a way of enhancing this process, since they can dynamically test a huge number of variations in parallel. Evolutionary algorithms may be used to fine tune trading rules and/or their parameters. Alternatively, whole rule-sets or algorithms could be evolved. Closely linked with this, is the ability to back-test the rules or strategies to determine their performance. By successfully automating both of these processes, we should be able to harness the power modern computers provide to literally test thousands of combinations.

## Applying short-term forecast models

In Chapter 5, we used charts to compare the typical order placement patterns for a range of trading algorithms. However, during the execution it is important to remember that we do not know exactly what the future holds. So from time T in Figure 15-13 all we really have is uncertainty.

![](_page_22_Figure_6.jpeg)

Figure 15-13 Using short-term estimates for future market conditions

Modern trading algorithms are used to making dynamic adjustments to cope with changing market conditions. Though, if a sudden shift occurs such a reactive approach can be caught out and forced to play eatch up at less favourable prices, leading to sub-optimal

performance.

Data mining and artificial intelligence offer the potential to improve our short-term predictions for key market variables, such as price, volume and liquidity. This may be direct, using specific forecasting techniques, or indirect, based on changes in other assets or markets where data mining has shown a clear association.

Volume prediction is important for many trading algorithms. If future trade flow differs markedly from the historical volume profile then VWAP algorithms will probably struggle to meet their benchmarks. Even implementation shortfall algorithms need an accurate idea of the daily trading volume in order to determine the optimal trading horizon. A sudden spike or lull in volume will affect its performance. Likewise, a sudden shift could lead a dynamic percent of volume (POV) algorithm to chase the market, incurring considerable market impact. Using a short-term forecast would enable POV algorithms to place more passively priced orders in anticipation of future trading volume.

As we saw in Chapter 10, historical volume profiles go some of the way towards this, particularly when seasonal or even asset specific factors are incorporated. AI-based models can also offer useful short-term volume predictions, which may perform better in volatile markets. They might also be able to cope better with today's complex marketplaces, where volume is fragmented between multiple venues. However, so far there seems to have been little AI-based research into this.

Similarly, the market price may exhibit a consistent price trend, or there may be a reversion as in Figure 15-13. In Chapter 5, we saw how price adaptive algorithms can easily adapt to this. A passive in-the-money (PIM) strategy assumes any trends will persist and so prices orders more passively when market conditions are favourable, seeking to maximise the potential price improvement. Conversely, an aggressive in-the-money (AIM) tactic takes the opposite approach, assuming that trends will soon mean revert and so aggressively takes advantage of favourable prices. For instance, let's assume we are selling asset ABC, three potential short-term price forecasts are shown in Figure 15-14.

![](_page_23_Figure_6.jpeg)

Figure 15-14 Linking expected trading rate to future conditions

So at time T, a PIM strategy might expect the favourable trend to persist (pathway c) and so will continue to passively price its orders. If the trend slows down (pathway h) or even reverts (pathway a) it will need to trade more aggressively, trying to stem the now less favourable price trend. In comparison, an AIM strategy would expect reversion, so if the trend actually persists it will under perform.

Reacting to the changes as they happen will mean seeking immediate fills and so paying half the spread as well as any market impact costs. Whereas if at time T we could accurately forecast such a reversion, our trading algorithm could alter its approach. Less passively priced orders could be placed, reducing our potential spread and impact costs.

In terms of their choice of execution tactics, the controlling algorithms may decide to switch between more or less aggressive approaches, based on their perception of the current market conditions. For instance, if the current price trend is expected to stay favourable the algorithm may adopt a more passive tactic, such as layering orders, to try to maximise the price improvement.

Price volatility is another important factor for many trading strategies. Historical volatility is certainly useful, but in highly volatile markets, it can still underestimate the actual volatility. AI-based methods have proven to give more accurate forecasts than estimations based on implied volatility and statistical analysis.

This approach may also be adopted for other market conditions, such as liquidity or spreads. Provided the short-term forecasts are accurate, we should be able to benefit from more proactive order placement. If they are not then the orders may be cancelled, and more aggressively priced orders may be used to catch up.

#### Incorporating forecast models

In Chapter 11, we looked at how a simplified algorithmic trading environment might be set up. Figure 15-15 illustrates how this could be extended in order to incorporate short-term estimation models.

![](_page_24_Figure_8.jpeg)

#### Figure 15-15 Extending an algorithmic trading environment

Keeping the models separate from the actual algorithm allows them to be reused more easily. Each trading algorithm, or even execution tactic, may then use these short-term market estimates as part of their decision making process, choosing how much weight to give this information.

In fact, several models may be used, weighting the results from each and adjusting for optimal performance, as we saw for the neural network node back in Figure 15-4. This is similar to a technique called ensemble learning, which may be used to improve the accuracy of forecasting. Multiple models are employed for the forecast; each one is given a weighted vote (labelled A-E in Figure 15-4), based on its accuracy from prior testing. Even if models are not that accurate to start with, by combining them in this way the probability of a correct forecast increases. Hence, a variant of this technique is called boosting.

The models themselves may be purely statistical, as we saw in Chapter 10, or use AI or relationships learned from data mining. For example, short-term price estimation might be achieved hy looking to the futures or options markets, or other major market indices, based on historical lead/lag relations. Another model might track prices across stock industries or sectors based on historical correlations. For example, in Chapter 14 we saw how news in one company led to a spillover effect across the whole sector (in this case biotechnology). A further model might simply give an indication of whether the price is likely to increase or decrease, based on analysis (statistical or AI-based) of previous prices.

Clearly, each model will need access to a range of data, from:

- Market data for the specific asset
- . Market data for other related assets and/or indices/indicators
- ٠ News/sentiment data
- $\bullet$ Business cycle/Macroeconomic data
- $\bullet$ Historical data for any/all of the above

There should also be monitoring to ensure that the forecast models are improving the overall performance of the trading algorithms. A control might even use market data to check the accuracy of the model/s, and make adjustments based on whether the market reaction is more or less than expected. Factors such as performance and reliability play a part as well, as we saw in Chapter 11. Any analytics must also be calculated fast enough to be useful for execution and/or order placement decisions.

## Generating trading strategies/rules/parameters

Trading algorithms and execution tactics are sets of trading rules that are chosen to meet specific objectives. These rules are generally defined by traders, but there will also have been a significant amount of testing and fine-tuning to ensure they perform sufficiently.

Tree-based expressions, supported by genetic programming techniques, provide a very flexible means of generating or evolving trading rules, as we saw hack in Figure 15-9. Evolutionary algorithms are potentially well suited to such fine-tuning; since they have the ability to test a huge number of variations in parallel. The changes being tested might be as simple as different parameters, alternatively whole sets of rules may be evolved.

Much of the research into trading rule generation has concentrated on investment decisions. Technical trading rules for the S&P 500 index were created by Franklin Allen and Risto Karjalainen (1999), using daily price data. The rules were specified in expression trees that incorporated variables, such as market prices, and functions, such as moving averages. A similar approach was adopted by James Butler (1997) and Edward Tsang et al. (2000) to create the EDDIE (Evolutionary Dynamic Data Investment Evaluator) system. They also incorporated fundamental data, such as the price-earnings ratio, together with market prices in the rules. EDDIE was used by Butler (1997) and Li and Tsang (1999, 1999a) to predict whether a specific rate of return (or more) could be achieved within a given timeframe (1-3 months) for the S&P 500 and DJIA stock indices. In each case, they found that it was indeed possible to generate rules that could outperform random tests and common technical rules. A variant was even created by Tsang, Markosc and Er (2005) to investigate the futures call-put parity arbitrage for the FTSE-100 index, which outperformed naïve arbitrage rules.

However, generated trading rules may be just as easily be used for execution tactics, such as order placement decisions. Figure 15-16 shows what the rule-tree might look like for a sample execution tactic. This models the decision for choosing between market order and a limit order placement.

![](_page_26_Figure_2.jpeg)

Figure 15-16 An example order placement rule

The rules are based on order book conditions and asset specific variables, as we saw in Chapter 8. Thus, less aggressively priced limit orders are placed when:

- the spread is less than its historical intraday average, or
- the book depth (on the same side) is less than double our order size, or ٠
- the short-term volatility is 10% greater than normal.

This approach could also be applied to choose between execution venues in fragmented markets, or to try to minimise legging risk for contingent/pairs and portfolio trades.

## **Back-testing**

Back-testing is an important means of verifying the potential performance and profitability of any trading strategy. It allows us to see how the strategy might have performed under market conditions. Testing can also show how the strategy copes with specific situations, such as news events or market crashes.

A nice overview of the key considerations for back-testing is provided by Steve Oppenheimer and Thomas Parry (2007) in eForex magazine. As they point out, it is important to be able to simulate how the market might have reacted to our orders. To do this accurately we need to consider the available liquidity, as well as taking into account factors such as latency. Another important consideration is how deterministic the simulation is. For example, when testing trading rules or parameters we want to be able to see the impact of just these changes. If the simulation is deterministic then each time the results will be the same, making it easier to isolate the effect of any rules changes. In comparison, random (or stochastic) simulations will give completely different results each time. Ideally, it would be useful for the simulation to be able to toggle between these two types, giving us the most flexibility.

So far in this book, we have concentrated on empirical studies; however, there has also been a lot of research based on artificial markets. These offer one potential solution for backtesting. In particular, artificial markets allow us to test a wide variety of conditions such as trending or volatile markets or even sudden liquidity crises. An alternative approach is to base the simulation on real market data. In which case the simulator somehow needs to merge the test orders with this data and try to emulate the appropriate reactions.

#### Testing with artificial markets

Artificial intelligence is being used to create simulated marketplaces that are populated with electronic agents, although some also allow human participants. Unlike real markets, these simulations may be controlled and configured, allowing active experimentation. Research is primarily focussed on market microstructure analysis and testing the performance of specific trading strategies. The data from these simulations may then be compared with theoretical predictions and empirical evidence from real markets.

#### **Artificial agents**

The artificial agents used to simulate trading can range from simple random order generators to rule-based agents or even ones based on sophisticated AI techniques. A nice summary of the various types is given by Blake LeBaron (2000).

Purely random agents are easily implemented, but they can often lead to high volatility. In comparison, experiments involving human traders generally achieve quite a rapid price convergence. LeBaron (2000) notes that market efficiency tests assign random agents at between 50-100%, whilst human traders are much closer to 100%.

One step up from purely random order generators is the zero-intelligence agent, as outlined by Dhananjay Gode and Shyam Sunder (1993). These still place random orders to buy or sell, but they also adhere to strict budget constraints. LeBaron (2000) notes that such budget constrained agents allocate assets at over 97% efficiency, which is close to the performance of humans in similar tests.

Dave Cliff's (1997) zero-intelligence plus (ZIP) traders further extend this model to include a variable profit (or utility) margin. Each ZIP agent has an inbuilt price limit. In addition to this, there are three main parameters, namely its profit margin, learning rate and a momentum term. Using these, each agent can determine a target price, based on its price limit and the desired profit margin together with a random factor. The learning rate parameter controls the rate of convergence between the agent's order prices and their target price. The momentum term dictates how much history the agent takes into account when reevaluating its margin. Essentially, this adjustment is based on how successful the agent has been at getting its orders filled, as well as the dynamics of the market price. A genetic algorithm may be used to optimise these parameter settings.

Similarly, Steven Gjerstad and John Dickhaut (1998) created agents that maintain an order and trade history. From this, they form a subjective "belief" function that represents their estimated probability of the fair price.

Other studies have used agents that are even more sophisticated. For instance, Marco Raberto et al. (2003) created them based on particular investment styles. Momentum and contrarian agents used simple technical trading rules to make decisions, whilst fundamental agents traded based on a firm view of the asset's value. Gilles Daniel (2006) created selfreferential agents, which acted as informed and rational arbitrageurs. Agents have also been designed to adopt the role of market makers. For example, Sanmay Das (2005a), Yi Feng, Ronggang Yu, and Peter Stone (2003) and Alexander Sherstov and Peter Stone (2004) all report on market making agents.

The performance of both human and electronic agents in a continuous double auction was analysed by Rajarshi Das *et al.* (2001). Several different agents were used, including ZIP traders. To their surprise, they found that the electronic traders consistently outperformed their human counterparts by around 20%.

#### **Artificial markets**

Research into trading strategies and market microstructure has yielded a range of different market simulators. A nice overview of these is provided by Julien Derveeuw *et al.* (2007), Gilles Daniel (2006) and LeBaron (2001).

The Santa Fe artificial stock market was one of the earliest simulated markets to be created. Trading evolves around two assets, a risk-free bond and a risky stock. In the first version, outlined by Richard Palmer *et al.* (1994), the market was driven solely by the decision of the agent traders to buy or sell. In later versions, described by Blake LeBaron (2001a), agents could predict the value of the stock based on estimates for its future dividend.

The Genoa artificial stock market, outlined by Marco Raberto *et al.* (2001), supports the same two assets as the Santa Fe simulator, but agents may issue limit orders. Using this model, they were able to see some of the key features of price dynamics, namely volatility clustering and fat-tailed distributions.

The NatLab market simulator provides a fully asynchronous event driven platform. The design is based around a central order book and supports both market and limit orders. By using a mixture of different agent trader types the simulator has been able to reflect phenomena such as financial bubbles, crashes and recoveries, as detailed by Lev Muchnik, Yoram Louzoun and Sorin Solomon (2006).

Another notable platform is the U-Mart simulator, reported by Yoshihiro Nakajima *et al.* (2004), which provides an artificial futures market for both human and machine agents.

#### Simulating real markets

Artificial agents and markets can be useful for testing. However, basing the simulation on real market data gives an immediate head start in terms of realism. The simulator needs to be able to recreate the order book and apply the same trade matching rules as the venue it is simulating. Though, simply giving an immediate fill for every test order with a matching price does not provide sufficient realism. The simulator also needs to take into account competition from other participants. Otherwise, the strategy/algorithm being tested may perform poorly when transferred to the real world. Therefore, it is also vital that the simulator provides a realistic reaction to the test orders. Figure 15-17 shows an example of what this might look like.

As we saw with market impact, it is difficult to predict the long-term effect of placing additional orders. Though, based on the short-term responses we saw from the empirical studies in Chapter 8, simulators can make slight adjustments to the historical data in response to the test orders. For instance, subsequent orders might be priced more passively if the test orders increase the available depth on the order book. The simulator might also take into account other market conditions, such as volatility or price trends.

Some research groups have already created their own simulations based on real data. Most notably the Penn-Lehman Automated Trading Project (PLAT), as described by Michael Kearns and Luis Ortiz (2003). This order book based platform integrates data from the former Island ECN. The Penn Exchange Simulator augments the order book data from the ECN with its own simulated orders. Additional realism is provided by competition from multiple agents. Thus, agents' orders may end up executing with simulated ones from the ECN or with orders from a competitor. Based on this approach Sheri Markose, Azeem Malik, Wing-Lon Ng (2007) also report on a simulator for London's SETS limit order book.

![](_page_29_Figure_1.jpeg)

Figure 15-17 An example test environment

Commercial simulators are available as well. These are focussed on catering for the testing needs of algorithmic trading systems. For instance, Allied Testing's Exchange Simulator (SIM)  $^{2}$  provides both live and playback modes, much like PLAT. The order book is recreated using exchange data feeds. It can also be reconstructed using the order book depth and by inferring the order flow based on trade details from level two market data. Instead of using competing agents, the simulator responds to user orders based on the available liquidity. It adjusts the historical data in response to the user's trading activity and even simulates new orders to mimic the typical market reactions. These reactions also take account of stock-specific behaviour, so orders tend to queue for assets with large spreads whilst for more liquid assets simulated orders compete by using more aggressive pricing and filling any gaps in the order book. Hence, the simulator is able to provide behaviour tailored to the typical dynamics and microstructure properties of each asset.

Both PLAT and SIM support real-time and replay modes, so simulations may be performed live or back-tested by replaying historical data. This provides a very flexible framework for testing and training. Note that single agent testing is likely to be more deterministic, and so more suited to reproducibly testing changes for trading rules and parameters. Further testing may then be performed in a multi agent environment.

## 15.5 The future

Artificial intelligence often evokes images of the "black box" supercomputers used to play chess. However, chess is a game with defined board and a very strict set of rules, so despite the billions of permutations a computer can potentially learn every move, as James Finnegan points out in CFA Magazine (2006).

Financial markets are a lot more complex than chess; for starters, there are a lot more participants, and the rules are less well defined and constantly evolving. Relying on a computer's processing power and brute force is not going to solve the problem of best execution. Artificial intelligence may well offer a solution, although it still appears to be

<sup>&</sup>lt;sup>2</sup> A free online trial version of Allied Testing's simulator is available at http://exchangesimulator.alliedtesting.com

some way in the future.

Autonomous vehicles may offer a closer approximation to the required complexity than chess. These also highlight the rapid progress that is being made in AI. In 2004, the objective of the DARPA (Defense Advanced Research Projects Agency) Grand Challenge was for autonomous vehicles to navigate a 142-mile long course through the Mojave Desert. The vehicles relied on a combination of satellite navigation, radar, laser range finding, and video cameras. The AI systems somehow needed to take all these disparate inputs and use them to keep control of the vehicle and navigate safely to the destination. On this first run within a few hours all of the fifteen competitors had failed, been disqualified or withdrawn. However, the 2005 rerun was much more successful with five teams finishing. Stanford University's robot-car "Stanley" completed the course in less than seven hours. In fact, all but one of the 2005 entrants surpassed the 7.36 mile limit, which had been achieved in 2004.

On the back of this rapid progress, DARPA significantly raised the goals for their 2007 Urban Challenge. This time, the vehicles had to negotiate 60 miles through a mock city avoiding obstacles. The AI systems also had to contend with other vehicles, and more complex driving patterns such as overtaking and parking. The entry from Carnegic Mellon won, but all the cars showed considerable improvements over the previous models. This is a closer approximation to the financial markets, since they had to contend with other drivers and other AI-based systems.

The techniques we have covered in this chapter may seem somewhat esoteric. Still, if AI systems can be used to drive a car 60 miles through town and park it without crashing, then there is certainly some scope for them to be applied to the financial markets. It is important to remember that we are not talking about recreating human intelligence. Best execution seems like a fuzzy goal, but it is still less complicated than life. AI systems for trading are not conscious and they cannot communicate. In terms of raw intelligence, the goal is probably more like that of an insect, which (in theory) should be a lot more achievable.

That said, the financial markets have thousands of traders, each with their own opinions and strategies. Collectively their behaviour shapes the markets, and so affects the prices of assets. Advances are certainly being made in collective intelligence, using massive multiagent simulations. But this an incredibly complex phenomenon, so the science of forecasting market reactions is still evolving.

Admittedly, some of the studies we have seen in this chapter have failed to show AI techniques performing substantially better than statistical models. Nevertheless, computers continue to get more and more powerful. Over the next few years, they will be able to support increasingly complex data mining and artificial intelligence techniques. Therefore, their accuracy and speed are likely to increase. Hardware innovations, such as memristors, may even make building dedicated artificial intelligence hardware viable. As for whether this latest progress in AI will be successfully applied to trading - only time will tell.

## 15.6 Summary

- Artificial intelligence (AI) and data mining offer the potential to give traders an edge by spotting or predicting trends; they may even be used to generate trading strategies.
- Data mining is a mix of statistical analysis and inference techniques:

- Classification and clustering analysis seek to identify common features in the data.
- Time-series mining is generally used for forecasting or spotting trends.
- Association rule mining searches for correlation patterns.
- Relationship based data mining has analysed:
  - Intra-market relationships, such as co-movements between industries and sectors.
  - Inter-market relationships, highlighting the correlation between major markets. -
  - \_ Crises and contagion, highlighting that relationships can change significantly during extreme periods. For instance, correlation tends to increase with downward moves.
- AI can actually be split into two main approaches  $\blacksquare$ 
  - Conventional AI is a top-down approach using logic and rules to make decisions. This often relies on data from statistical analysis or custom-made knowledge bases.
  - Computational intelligence is a flexible bottom-up approach, inspired by biological mechanisms. Neural networks try to reproduce the action of our brain's neurons, whilst evolutionary computation simulates populations.
- Trading algorithms are already an example of conventional AI since they encapsulate ı trading logic within a rules-based framework.
- Short-term predictions of conditions, such as prices and volatility have been shown as  $\mathbf{L}$ effective, using neural networks, support vector machines and statistical analysis.
- $\blacksquare$ Evolutionary algorithms and genetic programming can test a huge number of variations in parallel, making them suitable for checking trading strategies and their parameters.
- $\mathbf{u}$ Back-testing is an important means of verifying the potential performance and profitability of any trading strategy. AI can help create simulated marketplaces for this.
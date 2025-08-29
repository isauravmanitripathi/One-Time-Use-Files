![](_page_0_Figure_1.jpeg)

Information is everything. Automated news handling and interpretation can be complex, but these techniques offer the potential to further enhance trading strategy performance.

# 14.1 Introduction

The world's markets are driven by information, much of which is reported in news headlines and stories. Adapting to breaking news events can give traders a significant edge over the rest of the market. Over the last few years, the incorporation of news into algorithmic trading systems has attracted more and more attention.

Clearly, the relentless increase in both the speed and capacity of computers offers a massive potential for news-based analysis. Nevertheless, people are still much more adept at interpreting news and events than machines. Computer-based news analysis is a non-trivial task. Part of the difficulty is simply the fact that news is often based on unstructured text so it is difficult for rule-based systems to process it, and even harder for them to reliably interpret it. The increasing digitisation of news to computer-readable formats is helping to bridge this gap. Complex artificial intelligence and natural language processing techniques are also being employed. As we shall see in the following sections, progress is being made on computer-based analysis, but there is still quite a long way to go.

## 14.2 Types of news

News items can represent a wide variety of information. Broadly speaking, we can categorise most news items into three main classes: global/regional, macroeconomic and corporate.

| Event           | Examples                                         |
|-----------------|--------------------------------------------------|
| Global/regional | Political events, wars and terrorism, natural    |
|                 | disasters                                        |
| Macroeconomic   | Interest rate, US non-farm payroll, Gross        |
|                 | Domestic Product (GDP) announcements             |
| Corporate       | Mergers and acquisitions, bankruptcies,          |
|                 | board/executive changes, product releases,       |
|                 | quarterly/annual reports, dividend announcements |

Table 14-1 Key news types

Table 14-1 shows some examples. Note that all three types of news can have distinct effects on the volume and volatility of both markets and specific assets. Though, the full effects of global/regional news can be quite difficult to interpret. Hence, this chapter focuses on the impact of both macroeconomic and corporate news.

## Macroeconomic news

Most macroeconomic news comes in the form of regular announcements that provide information on key economic indicators. There is a wide range of different indicators; some of the main ones for the U.S. economy are shown in Table 14-2.

| Class                  | Announcement Type                          | Frea | Time  |
|------------------------|--------------------------------------------|------|-------|
| GDP                    | Gross Domestic Product (GDP)               | Q    | 8:30  |
| Consumption            | Personal Consumption Expenditures          | M    | 8:30  |
|                        | <b>Business Inventories</b>                | M    | 8:30  |
|                        | Durable Goods Orders                       | M    | 8:30  |
| Investment             | Factory Orders                             | Μ    | 10:00 |
|                        | Construction Spending                      | M    | 10:00 |
|                        | New Home Sales                             | M    | 10:00 |
| Net Exports            | Trade Balance                              | M    | 8:30  |
| Government Expenditure | Government Budget                          | Μ    | 14:00 |
| FOMC                   | Target Federal Funds Rate                  | 6W   | 14:15 |
| Money supply           | M2                                         | W    | 16:30 |
|                        | Non-Farm Payrolls/Employment               | M    | 8:30  |
|                        | Initial Unemployment Claims                | W    | 8:30  |
| Real Activity          | Industrial Production Capacity Utilization | M    | 9:15  |
|                        | Retail Sales                               | M    | 8:30  |
|                        | Personal Income                            | M    | 8:30  |
|                        | Consumer Credit                            | M    | 15:00 |
| Prices                 | Producer Price Index (PPI)                 | Μ    | 8:30  |
|                        | Consumer Price Index (CPI)                 | M    | 8:30  |
|                        | Index of Leading Indicators                | M    | 8:30  |
| Forward-Looking        | ISM/NAPM Index                             | M    | 10:00 |
|                        | Consumer Confidence Index                  | M    | 10:00 |
|                        | <b>Housing Starts</b>                      | M    | 8:30  |

## Table 14-2 Some of the key U.S. macroeconomic announcements

The classification scheme is based on those commonly adopted in economic literature. In the U.S., most of the announcements are made monthly (M), although some are issued quarterly (Q) or weekly (W). Indicators may also be referred to as procyclical or countercyclical; this just shows whether they move in the same direction as the economy or not. For instance, GDP and Non-Farm payrolls are procyclical indicators, whilst unemployment claims is a countercyclical one.

The Gross Domestic Product (GDP) is probably the best-known indicator of an economy. It represents the total value of goods and services produced by a country, usually over a year. Another way of expressing GDP is:

## $GDP = \text{Consumption} + \text{Investment} + \text{Net Exports} - \text{Government Expenditure}$

GDP announcements are generally made quarterly and often in several stages, beginning

with an advance figure, followed by preliminary and then final figures. The Real GDP is a GDP based indicator that includes adjustments for price changes and inflation.

*Consumption* represents private consumption; in other words, household expenditures on food, clothing and bills for utilities, health, education and insurance.

*Investment* corresponds to the investment in capital, which in turn is broken down into several sub-categories: *Business Inventories* reflects the three stages of production, namely manufacturing, wholesaling and retail. Effectively, it acts as a leading indicator for consumer demand, *Durable Goods Orders* measures the number of orders placed with manufacturers, similarly *Factory Orders* monitors the total order placements. These give an indication of the health of the factory/manufacturing sectors. The remaining investment indicators highlight the state of the building/housing markets. *Construction Spending* provides an estimate of the total domestic expenditure on all types of construction, whilst *New Home Sales* focuses on family dwellings. These may be used to estimate the future demand for mortgages. Housing market indicators also often act as a leading indicator for the general health of the economy.

Net Exports are reflected by the balance of trade. Essentially, this is the difference between the value of an economy's imports and exports.

*Government Expenditure* is represented by the overall budget, which incorporates the cost of government services and projects as well as the wage bill for government sector employees.

Another important economic indicator is the Target Federal Funds rate, which reflects U.S. monetary policy. For the money markets, the  $M2$  indicator measures the total U.S currency held in reserves, checking, savings or current accounts.

The Real Activity indicators provide a view on key economic activities such as employment, retail sales, credit and personal income. Non-Farm Payrolls, or the *Employment* report, provides a count of the number of paid full and part-time employees. Whilst the Initial Unemployment Claims shows the number of people newly out of work. Industrial Production gives a measure of the output of domestic industries. Retail Sales values the total sales from retail stores, and so reflects consumer spending. *Personal Income* measures the total income before and after taxes, whilst *Consumer Credit* measures the level of personal debt.

The *Price Indices* provide measures of the average costs for manufacturers (PPI) or for consumers (CPI). Therefore, they act as indicators for inflation, whether it is for commodity prices or domestic.

Most of the indicators so far mentioned provide a lagged measure of economic performance. The *Index of Leading Indicators* tries to provide a forecast for the economy in the next six to nine months. The *Institute for Supply Management* (ISM) Survey, formerly the National Association of Purchasing Management (NAPM), gives an indication of whether the manufacturing sector is expanding or contracting. Similarly, the Consumer Confidence survey measures the level of optimism held by consumers.

Macroeconomic indicators may differ slightly for other countries, but essentially they all offer the same kind of information.

#### Corporate news

For corporations, news arrives in two main forms: Company reports provide regular indications on the economic strength of a firm. Other corporate news is just a catch-all for any important event that might happen for a firm.

Company reports provide results, showing their historical performance, and estimates for

future earnings and growth. Often these are made yearly, although for some countries, such as the U.S., they are filed quarterly. Unlike macroeconomic indicators, these are not tied to specific dates, firms may freely choose to bring forward or delay their reports. The same applies for any dividend announcements.

In terms of other corporate news, a wide range of specific events may occur. This can include anything from:

- New issues or repurchases, of shares or debt
- $\bullet$ New or lost orders/sales
- . New product releases
- ٠ Joint ventures/mergers/takeovers
- $\bullet$ Management changes
- Lawsuits
- . Bankruptcy
- . Analyst upgrades/downgrades

Obviously, such news tends to be less predictable, both in terms of when it is released and how the market reacts to it.

## 14.3 The changing face of news

News has been steadily changing over the last few years, from how it is delivered to where it is being sourced.

Increasingly, news items are being fully digitised into machine-readable formats. This is making it much easier for computer programs to filter and even analyse the information from news stories.

The internet has also had a significant impact, making alternative sources of information, such as message boards and blogs, easily accessible. In fact, these are even starting to compete with the mainstream news services to deliver scoops, although credibility and reliability are still issues.

## Digitisation of news

News has been available digitally, in one form or other, for decades. Though, only over the last few years have we seen more efforts to make it easier for computers to actually process and interpret it.

When news screens first became accessible digitally, they were simply copies of the original terminal screens. An example is simulated in Figure 14-1.

09:06 NEWS Futures slip as fears persist on subprime 09:05 NEWS DEF Corp Q2 results \$0.25 EPS 09:04 NEWS AN Other Corp raise offer for Target One to \$5.50/sh 09:03 VEND Target One shareholders getting impatient over bidding 09:01 NEWS BANK-2 writes down \$7 bn on subprime, sector falls 09:00 NEWS AN Other says merger makes sense 08:55 HOT1 More doom and gloom, poll expects turmoil to continue 08:51 ALER Commodities rally as oil reaches new high 08:49 NEWS AFG Inc expands into Asia with \$500 mn new plant

#### Figure 14-1 An example news terminal screen

The only real way to handle news in this format is to extract the raw text, also known as "screen scraping". Just like web page scraping, this has been used as a means of merging headlines from a range of sources or adding rudimentary filtering. Although such an approach is useful for delivering headlines for traders to read, it is less suitable for computerised news analysis and interpretation.

In the early '90s, vendors introduced news feeds that could deliver separate headlines and stories. For example, Reuters journalists tagged each headline and story with specific categories. The categories covered markets, countries, languages, industries and companies. This was a more versatile delivery mechanism, making storage and retrieval of news much easier. The category codes could be easily used to filter news items. However, the news was still in a single body of text, which had to be parsed for interpretation and analysis.

```
Headline: 09:05 NEWS DEF Corp Q2 results $0.25 EPS
                                     |Symbol|DEF.Q|Type|Research
Story:
|Time|09:05
                      |Source|VEN1
|Symbol|DEF.Q
                      | Type | Research
                                             |Country|US
|Title|DEF Corp Q2 results $0.25 EPS
[Story] * Second quarter earnings per share $0.25
        * Second quarter revenue rose 15 percent to $100 million
        * Estimates second quarter earnings per share $0.20
          revenue view $85 million
```

![](_page_4_Figure_4.jpeg)

A simulated example is shown in Figure 14-2 based on the headline we saw in Figure 14-1 for DEF Corp. The data is delivered in a fully digital format, so for readability it is shown as plain text with the different fields separated (using I characters). The natural progression from this has been for vendors to start digitising the actual news content.

```
<News>
   <pre><Headline>DEF Corp Q2 results $0.25 EPS</Headline></pre>
   <Category>CorpEarnings</Category> <Source>RTRS</Source>
   <Sector>Tech</Sector>
                           <Identifiier>DEF.Q</Identifier>
   <Results>
       <Type>EPS</Type>
       <Value>25</Value>
       <Units>CPS</Units>
    </Results>
    <Estimate>
       <Type>EPS</Type>
       <Value>20</Value>
       <Units>CPS</Units>
   </Estimate>
  <Story>
     * Second quarter earnings per share $0.25
      . .
 </story>
</News>
```

![](_page_4_Figure_7.jpeg)

Indeed, they have started converting their news feeds for delivery in various formats, often

based on the Extensible Markup Language (XML). So our example story might now look something like Figure 14-3 (again reformatted for readability). Clearly, this allows more fields to be added to the data and makes the information easier to access. For this example, both the actual earnings per share (EPS) and the estimate figures are now readily accessible for computerised systems, without the need for any text parsing. This allows programs to read in these values in much the same way as they might use bid and offer prices from market data feeds. Hence, they are much more easily incorporated into rules for trading strategies and algorithms. This technology is already available; for example, the Dow Jones Elementized News Feed publishes key corporate and economic data elements such as earnings numbers while simultaneously publishing the news stories about the earnings.

## Digitisation of corporate reports/research

Digitisation is also starting to be established for corporate reporting and research. The eXtensible Business Reporting Language (XBRL) provides a framework for corporations to create machine-readable reports. Instead of just being treated as blocks of text and tabular data, XBRL reports ensure that each item has its own unique tag. Thus, every item on the balance sheet or expenses is tagged, and may even be assigned to groups or linked to other items. A taxonomy acts as the classification scheme that enables the data and tags to be correctly interpreted. This allows the same set of information to be viewed and processed in a variety of different ways whilst maintaining consistency. Being machine-readable, this should allow automated systems to perform most of the routine data processing and validation steps. The hope is that this will free up analysts, allowing them to focus on more value-added aspects, whether they are sell-side researchers, buy-side investors, auditing accountants or regulators.

For the companies themselves, XBRL will clearly require a lot of work. Hopefully, it will help streamline the process of corporate data collection and reporting, allowing finance divisions to more quickly and reliably generate management reports and financial statements. Still, the uptake of XBRL is most likely to be determined by regulation, rather than longterm efficiency gains.

Clearly, the migration to something like XBRL is a much bigger task than elementized news feeds. Instead of a handful of major news vendors there are hundreds of thousands of companies across dozens of countries with a wide range of accounting and reporting practices.

The main driving force behind the adoption of XBRL will be the U.S. The SEC has already paved the way for filing in XBRL by U.S. companies and is looking to transform its company information database (EDGAR). To date, this has been a voluntary filing programme, although it should be mandatory for the largest companies from 2009 and for all public companies by 2011. Other countries have also started adopting XBRL. For instance, in Europe the Spanish Stock Exchange now uses it to receive and distribute reports from over 3,000 listed companies. The National Bank of Belgium has plans to migrate the filing of accounts for commercial and industrial companies to XBRL. Similarly, the UK government plans to make XBRL mandatory for the filing of company accounts. The shift to IFRS (International Financial Reporting Standards), a unified set of accounting standards, should also help ease Europe's transition to XBRL. In Asia, the task is more complex, since every country has its own set of accounting standards, each of which will need to be handled by their own XBRL taxonomies. That said, in 2005 more than 800 Chinese companies filed their half-year reports with the Shanghai Stock Exchange using XBRL. The Tokyo Stock Exchange has also launched a pilot scheme.

Closely linked with XBRL is the Research Information eXchange Mark-up Language (RIXML). This framework is intended for the distribution of investment and financial research. Taken together, these projects mean that most corporate-related reports will be available in completely machine-readable formats. Whilst this is most applicable for quantitative investment systems, trading algorithms may also benefit from the ability to quickly interpret the key information, such as earnings figures/estimates, in real-time updates. More information on XBRL may be found at www.xbrl.org, whilst the homepage for RIXML is www.rixml.org.

## Changing sources of news

The internet is steadily transforming the news, in terms of how information is supplied and how quickly, as well as from where it may be sourced. The major news wires and press services have been electronic for a long time. However, conventional media is starting to face fresh competition from social media, which covers the raft of technologies now used to share information and opinions, such as blogs, message boards, wikis and podcasts. Social media sites can offer glimpses of information well before it reaches the mainstream media as official press releases and news wires. Figure 14-4 gives a nice illustration of this shift:

![](_page_6_Picture_5.jpeg)

Source: ©Monitor110 (2007) Reproduced with permission from Monitor110, Inc.

Figure 14-4 The new information dissemination cycle

Companies, such as Collective Intellect, trawl through thousands of web sites and message boards to glean useful information. Official press releases and other information may be extracted from a range of government, regulatory and corporate web sites, whilst opinions and rumours may be sourced from blogs and discussion boards.

Services that aggregate both conventional and alternative media sources are also being established. These provide a uniform means of accessing data from a huge range of feeds. For instance, Relegence's First Track product scans over 18,000 different business-centric

sources, ranging from the news wires and business media, to domestic and foreign newspapers, as well as government and corporate web sites and blogs. Their Mail Track product can even incorporate email and its attachments. This is particularly useful given how much information is communicated over email, from internal memos to newsletters and research notes. The major news agencies are also starting to offer similar facilities, for example, news and information from Dow Jones is available through their own current awareness solution (Dow Jones Factiva).

Thus, a new breed of alternative and complementary news services has been created. Will these be the equivalent of ECNs for news?

#### **Potential benefits**

Sourcing information from alternative sources can give a significant head start over more conventional news feeds. For instance, over a fortnight before Google's Q4 2005 earnings announcement a blog created by a Yahoo technologist predicted that they would miss their Q4 estimates. Admittedly, this could be seen as misinformation from the competition, in fact CNN Money picked up the story on January 31<sup>st</sup> with a report titled "Rival trashes Google's growth prospects". However, the prediction proved to be accurate with the stock falling by up to  $10\%$  shortly after the earnings announcement, as shown in Figure 14-5(a). Clearly, it is much easier to judge such information with hindsight. Although an alternative point of view from a domain expert is still useful, even if it had proven to be incorrect.

![](_page_7_Figure_5.jpeg)

Source: ©Monitor110 (2007)

Reproduced with permission from Monitor 110, Inc

Figure 14-5 Two examples of information available before the news wires

Blogs and forums are not the only source of news leads; regulatory bodies can also give an insight into upcoming announcements. This is particularly appropriate in the field of medicine. For example, Figure 14-5(b) highlights an example for Genentech: Avastin is their

trade name for Bevacizumab, an anti-angiogenic drug that has been approved for use against colorectal cancer since 2004. On March 14<sup>th</sup> 2005, the National Cancer Institute (NCI) posted the results of Phase III trials using Bevacizumab combined with chemotherapy for patients with advanced lung cancer. Around four hours later, Genentech released this news to the press, resulting in a 25% hike in its stock price. Anyone who made the connection between Bevacizumab and Genentech could have had a significant market lead.

## A note of caution

Credibility is vital for news. The news wires and press services have carefully built their reputations over the last century. Still, human or technical errors may mean incorrect news or old stories can sometimes be picked up: Chief executives have been given premature obituaries and company reports from years before have appeared as if just issued.

Clearly, when using information taken from alternative sources, such as internet blogs or news forums, more caution must be taken. Fake news announcements are not uncommon for micro-cap or penny stocks, with fraudsters adopting "pump and dump" tactics. Though, as David Leinweber and Ananth Madhavan (2001) point out, large-cap stocks are not immune to such fraud either: They use the example of Lucent Technologies, which in March 2000 saw its market cap drop \$7 billion in a day, triggered by a series of fake postings. The scam was successful because at the start of the year internet bulletin boards and chat rooms were full of negative rumours about the company, which were confirmed when Lucent issued an earnings warning on January 6<sup>th</sup>. So on March 22<sup>nd</sup>, when a series of postings suggested that Lucent would not meet their Q1 earnings projections these carried more weight than might have been expected. Indeed, Lucent's stock price started to fall rapidly. Then in the same evening, a new posting was made titled "LUCENT RELEASES EARNINGS WARNING! DAMN!" together with comments from a disappointed investor and what appeared to be a press release from Lucent, similar to the one from January. This was forwarded to over 20 different message boards. The next day, Lucent's price continued to fall before the company was finally able to convince the market that the news was fraudulent. A subsequent SEC investigation found that a single fraudster had used a trio of aliases to post the fake news item together with a barrage of replies and comments to lend credibility to it. The names used were specifically chosen to be similar to those of established posters, although with user names like "hot\_like\_wasabe" it is clearly hard to tell friend from foe. How did they find the fraudster? Well, unsurprisingly, he made a huge profit from buying Lucent on the 22<sup>nd</sup> and 23<sup>rd</sup> of March.

Hence, vendors sourcing data from social media sites are incorporating filters and ranking mechanisms to ensure that only the most reliable sources are used. Analysts are sometimes involved to ensure additional data quality. Some vendors even use voting systems to incorporate end-user feedback on the quality/relevancy of particular articles and sources. Gaining a solid reputation takes both time and results, so for the moment experience gives the established media the edge.

# 14.4 Computerised news handling techniques

Computerised news handling was originally based on simple categorisation and filtering techniques. In an effort to analyse and interpret this information these have evolved into even more complex mechanisms.

## **News filtering**

Given the amount of information available, news filtering is vital to ensure traders and investors notice the stories that are important to them, rather than being distracted by the general flow of news.

Back in the days of terminals, the news services directly controlled the filtering, providing specific pages for key news topics. Whilst "screen scraping" techniques could be used, it was difficult to achieve 100% accuracy, particularly for companies since a wide range of names and abbreviations may be used. Filtering became much easier when vendors started tagging news with additional data, such as the Reuters News 2000 category codes. Adding this metadata allowed users to configure custom filters for themselves, based on any combination of category codes. Similarly, elementized news feeds offer the prospect of even finer grained filtering. Instead of having to rely on the categorisations assigned by news editors and/or journalists, we can now create filters which match on the actual contents of the news.

Outside of the mainstream news services, information on web sites, blogs and forums is much more unstructured. Again, these were initially handled with simple "screen scraping" programs. This has since progressed to more advanced techniques based on textual and statistical analysis, or even natural language processing. Commercial software to do this data processing is becoming available, similarly alternative news feed services have started attaching additional meta-data to the raw information, which may then be used for more standardised filtering.

Clustering is closely aligned with filtering, ensuring that we do not see a handful of headlines, from various sources, all for the same event. This can be as simple as removing duplicate headlines. Alternatively, more sophisticated approaches cluster based on their interpretation of the actual information, coping with the fact that each source may use slightly different headlines for the same story. This is offered by systems like Relegance's First Track and Infonic's Burst>.

#### News association

News stories all differ in their effects. However, implicit relationships mean that beyond the immediate impact, secondary and tertiary effects can also propagate throughout the markets. For instance, macroeconomic factors will often have more immediate impact on the fixed income and foreign exchange markets; ultimately, though, they can also affect stock prices. Likewise, bad news for a company may cause its price to drop, but it may also affect the price of its main competition or even the whole sector.

Ideally, we would like to see any associated news that might affect us. For example, we could simply reduce the level of filtering, e.g. by shifting the focus from company-level to sector-level. Still, we do not want to be so inundated with news that we miss key items. The goal is to strike the best balance between these two extremes. One way of tackling this is to incorporate a dependency model that reflects all the key relationships. For instance, consider a supply chain. It is highly likely that a problem with a component supplier may also affect other companies, both upstream and downstream. In the U.S., firms must disclose financial information for any customer representing more than 10% of the total sales, or any industry segment that comprised more than 10% of consolidated yearly sales, assets or profits. This data may be used to infer the main dependencies.

There are several ways to construct dependency models. For example, services like TextMap create them based on analysis of distinct entities from historical news archives. Figure 14-6 shows an association map for news stories about Google.

![](_page_10_Figure_1.jpeg)

Figure 14-6 An association map for Google

We could also weight the importance of each relationship based the number of news matches. Though, we should probably also try to incorporate how these correlate with actual asset prices. Therefore, for the time being the most accurate dependency models are still created manually, and generally based on fundamental analysis. Hence, Relegence's Connect service incorporates proprietary mappings of corporate relationships and supply chains from the broker Credit Suisse.

A nice example of just how useful such relationships can be is given by Lauren Cohen and Andrea Frazzini (2008). In 2001, the Callaway Golf Corp. was the major customer for Coastcast Corp.'s golf club heads, accounting for 50% of their production. On the 7<sup>th</sup> of June 2001, Callaway was downgraded by one of the analysts covering it; the following day it lowered its Q2 revenue projections by \$50 million. Effectively, this meant nearly a 50% reduction in its expected earnings per share (EPS), falling from 70 down to 35-38 cents per share. This resulted in a 30% drop in its market price to close at \$15.03 on the  $8^{\text{th}}$  of June. However, such negative news about its largest customer did not seem to affect Coastcast's share price at all. Cohen and Frazzini searched the archives for the newswires and financial publications but could find no mention of Coastcast in the two months after Callaway's slump. It was not until July 5<sup>th</sup> that the price of Coastcast began to steadily decline, announcing an EPS of -4 cents on July  $19^{\text{th}}$ .

Figure 14-7 shows the price changes over this period (normalised relative to 1<sup>st</sup> May 2001 levels). Anyone closely tracking both companies would have had nearly a month before the price of Coastcast Corp. dropped in a similar fashion to Callaway Golf Corp. To prove their point Cohen and Frazzini tested a strategy of buying firms whose customers had the most positive returns in the previous month and shorting those with the worst. They found

![](_page_11_Figure_1.jpeg)

Source: Cohen and Frazzini (2007), Journal of Finance, Wiley-Blackwell Reproduced with permission from publisher

## Figure 14-7 Delayed reaction of Coastcast Corp.'s price to the slump in its leading customer Callaway Golf Corp.

potential annualized returns of 18.6%. Unsurprisingly, association based analysis is proving to be increasingly popular.

## **News analysis**

At present, the most common form of news analysis is interpreting its sentiment. Once we can reliably determine whether a specific news item is good or bad we can then start to estimate its impact on the market.

The simplest way of trying to determine sentiment is to look for, and count, specific words, such as "exceeds" or "profits". Clearly, this has its limits, since the text may contain words that by themselves may be construed as positive, e.g. "rising", but in context are actually negative, e.g. "debt is rising". The next logical progression is to extend the counting to phrases. A study by Young-Woo Seo, Joseph Giampapa and Katia Sycara (2002) used bigrams (two linked keywords) to infer sentiment. Their technique extracts the key phrases by first removing any unnecessary words or identities, so "Shares of ABC Company rose" becomes the bigram "Shares rose" for ABC. These bigrams are then translated into a sentiment based on a range of five different classifications, as shown in Table 14-3.

News stories also differ in terms of whether they are reporting facts after the event or reflecting predictions for the future. So news that is certain uses phrases like "revenue rose" or "shares fell", whereas uncertain news includes words like expect, forecast, anticipate or warning. Overall, this technique can achieve reasonable results, in particular for simpler text such as news headlines. However, everything that does not contain a good or bad bigram is classified as neutral, so useful information may be ignored. Therefore, they concluded that its

| Class              | Examples                                                                                                                                                                               |  |  |  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| GOOD               | Shares of ABC Company rose ½ or 2 percent<br>on the Nasdag to \$24-15/16.<br><i>Bigrams</i> : "revenue rose", "exceeds expectations", "share rose", "rose<br>profit"                   |  |  |  |
| GOOD.<br>UNCERTAIN | ABC Company predicts fourth-quarter<br>earnings will be high.<br>Bigrams: "expect earnings", "forecasts earnings", "anticipate earnings"                                               |  |  |  |
| NEUTRAL            | ABC and XYZ Inc. announced plans to develop<br>an industry initiative.<br><i>Bigrams:</i> "alliance company", "alliance corp", "announces product"                                     |  |  |  |
| BAD,<br>UNCERTAIN  | ABC (Nasdag: ABC) warned on Tuesday that<br>Fourth-quarter results could fall short of<br>expectations.<br><i>Bigrams</i> : "warning profits", "short expectation", "warning earnings" |  |  |  |
| BAD                | Shares of ABC (ABC: down \$0.54 to \$49.37)<br>fell in early New York trading.<br>Bigrams: "share off", "share down", "profit decrease", "fall percent",<br>"sales decrease"           |  |  |  |

Source: Seo, Giampapa and Sycara (2002)

## Table 14-3 Example sentiment classifications

inability to cope with complex grammar prevented it from exceeding 75% accuracy.

A further complication is the fact that news articles frequently contain information on a range of items or companies. Therefore, to ensure an accurate sentiment analysis we really need to be able to extract the exact context of any key words or phrases. This lead Seo, Giampapa and Sycara (2002) to consider future approaches based on more sophisticated natural language processing (NLP) techniques and semantic analysis. These techniques are more appropriate, since they can cope with more complex grammar. For example, they break down sentences into grammatical units, so phrases such as "profits falling" can be attributed to a specific entity.

Commercial systems capable of large-scale sentiment analysis are now becoming available. For instance, Infonic's Sentiment> offers a potential capacity of 10 articles/second at high levels of accuracy. It adopts a hybrid approach: the first phase performs linguistic analysis to extract the key features from each document. The second phase of processing performs the actual classification, based on machine learning. Numeric sentiments are then assigned for each story, together with a confidence level. It can also assign separate scores if the story concerns multiple companies. The major news services are starting to offer sentiment analysis as well. Indeed, Reuters has used the Infonic software to make available sentiment analysis for their own news feeds via their NewsScope Sentiment Engine.

## **News interpretation**

The logical progression from sentiment analysis is for systems to be able to perform a full interpretation of the news. Rather than simply deciding whether a given story is good or bad, they start to estimate how much the information should change the asset's price. So interpretation systems will need to identify and extract all the key information from the news story. Again, this may use NLP based approaches. Alternatively, with the increasing

availability of machine-readable news and corporate reports this may just be a matter of extracting data using the required tags.

However the information is sourced, it must then be used to determine its effect on the asset's price. Asset pricing is non-trivial, so in order to interpret the potential impact on prices the new information will need to be incorporated into dedicated asset pricing models. Obviously, this is easier to do for some stories than others. For example, an announcement of a new contract can mean adjustments to figures for expected sales and costs, whilst the resignation of a senior executive is more difficult to quantify. More advanced news interpretation techniques may even try to "read between the lines". For example, a study by Antonina Kloptchenko *et al.* (2004) found that the tone used in company reports often better reflects future performance than the reported results.

The new target prices generated by this analysis may then be used to make investment decisions. Still, in terms of execution its use is debatable. The changes may not be reflected soon enough in the markets for execution systems to benefit from this information in realtime.

## **News mining**

News mining combines the analysis of historical data with information from news archives. At present, much of the research focuses on interpreting the text from news headlines/stories and using this to explain price changes. Pattern recognition techniques are used to infer the market impact of news. Artificial intelligence (AI) techniques, such as neural networks or support vector machines, are then trained on this historical data in order to learn how to predict future changes.

As we saw in the previous sub-sections, accurately interpreting the meaning of news is a complex task. Many studies struggle to achieve better than 50% accuracy. Though, given time, it is likely that semantic analysis will improve sufficiently to make such techniques a worthwhile addition (in the not too distant future). In the meantime, data is also becoming available in machine-readable formats such as XML.

Analysing the short-term impact of news is an easier goal than estimating its mid and long-term effects. By comparing the news data, such as EPS figures, with market expectations we can determine how much of a surprise the news actually is. If the news meets expectations then the market will most likely already have incorporated this information into the asset's price, so a significant price change is unlikely. Whereas if the news is a huge surprise then a period of volatility will be likely, whilst the market adjusts to this new information. Section 14.5 provides a review of empirical market studies detailing these short-term effects.

Note that when trying to assess the impact of a particular news story or headline, rather than treating it as a discrete event we can look back over previous news items to confirm how much new information it actually contains. By chaining together news stories, we can determine the relative amount of new information each one contains. Thus, we can start to analyse whether news has a substantial momentum effect. This could also enable us to study how effectively new information is assimilated by the market, and whether it under or overreacts to news.

An interesting example is given in a study by Gur Huberman and Tomer Regey (2001). EntreMed Inc. (ENMD) is a pharmaceutical company focussed on releasing drugs for the treatment of cancer and inflammatory diseases. On May 3<sup>rd</sup> 1998, the Sunday edition of the New York Times (1998) had an article on its front page titled "HOPE IN THE LAB: A special report; A Cautious Awe Greets Drugs That Eradicate Tumors in Mice". This outlined the potential of endostatin, an anti-angiogenic protein. Endostatin was found to inhibit the growth of cancer tumours, and in studies on mice had demonstrated no onset of drug resistance. In fact, after repeated cycles it was even found to remove the tumours in mice altogether, effectively curing the cancer. The article also mentioned EntreMed, since they had the licence for producing the drugs based on this research. On the following Monday, EntreMed's price opened at 85 falling to close at around 52, up from 12.063 on the previous Friday, a 330% increase. This is shown in Figure 14-8.

![](_page_14_Figure_2.jpeg)

Source: Huberman and Regev (2001) , Journal of Finance, Wiley-Blackwell Reproduced with permission from publisher

Figure 14-8 EntreMed trading price and volume around news of its new drug

Still, as Huberman and Regev note the news story did not actually bring any significant new information to the market. In fact, it was just a fuller version of an earlier article printed in the New York Times (1997) the previous November 27<sup>th</sup>, titled "Tests on Mice Block a Defense by Cancer". This covered the publishing of the same research results in the journal Nature. There was also coverage on CNN's MoneyLine and CNBC's Street Signs on November 27<sup>th</sup>. Although this earlier news was released around Thanksgiving, it still saw a sizeable market reaction with a 28.4% price increase. They concluded that the key difference would seem to be due to being placed on the front page of the New York Times versus page 28, generating corresponding increases of 330% versus 28%. Certainly, there was an overreaction to the news in May. The persistent price increase in EntreMed may reflect an underreaction by professional investors in November; alternatively, it may also reflect the massive additional publicity that the company received. So when tracking the impact of news we should also consider how much attention the information might receive.

News mining may also be used to infer relationships that are more complex. For instance, the spillover effects and correlations that can occur between assets, typically across stock industries and sectors. In the case of EntreMed, Huberman and Regev (2001) note that on May 4<sup>th</sup> the seven firms of the NASDAQ Biotechnology Combined Index (excluding ENMD) saw a daily average return of 4.89% whilst the spotlight was on this sector.

It is also important to consider other sources of information when carrying out news mining. Asset pricing is complex, so key factors, such as market conditions or fundamental data, are necessary to explain the asset's price changes. For example, consider the substantial price lag, which we saw for the supplier-customer relationship between Coastcast Corp. and Callaway Golf Corp. Data mining could be used to check whether any other market variables might explain such a lag, other than investor under-reaction.

As with any forecasting method, caution must be taken to ensure that data is not overfitted, as we will see in Chapter 15. A common method is to exclude a set period of the historical data and news archives, often the most recent. Any relationships based on the main dataset may then be retested on the excluded period to check their suitability. Any rules that survive this test may then be exposed to further testing with real-time news and prices.

# 14.5 Market reactions to news

News announcements represent a flow of information to the markets. Since most asset prices are based on such information it is hardly surprising that news can have a marked effect.

A large number of empirical studies have analysed the impact of news for most of the major markets. In this section, we will review these to see the effects of both macroeconomic and corporate news on prices, trading volumes, liquidity and volatility. We shall also consider how other factors, such as the business cycle, affect the market response to news.

## Reactions to macroeconomic news

Macroeconomic news gives a regular indication of the performance of an economy. The announcements may be used to predict future economic growth, so they can have a marked effect on the trading of most asset classes. For instance, if key indicators show signs of a recession then governments may be prompted to change interest rates or alter their fiscal policy. Companies may well have to adjust their expected earnings in the light of these new conditions. Likewise, investors may choose to alter their portfolios, shifting to safer larger cap stocks or increasing the proportion of bonds.

The impact of news on asset prices varies somewhat for different asset classes. For example, news of an interest rate drop will help increase the price of existing bonds, whilst it weakens the currency. For corporations, the picture is slightly more complex, since they may benefit from lower interest rate but may also suffer from the weaker currency. Though, in terms of trading volume, liquidity and volatility, the reaction is generally a significant shortterm increase for all asset classes.

### Price

In their study of U.S. Treasuries, Pierluigi Balduzzi, Edwin Elton and T. Clifton Green (1997) found that the Non-Farm Payroll announcement had the most impact on prices. The impact was persistent and almost immediate; it also behaved roughly symmetrically between positive and negative surprises. In addition to Non-Farm Payrolls, they found that announcements for PPI, CPI, Consumer Confidence, ISM/NAPM survey, New Home Sales, Durable Goods Orders, Housing Starts and Initial Jobless Claims all had a noticeable impact on the market price. For example, Figure 14-9 shows the reaction to the Consumer Price Index for the 10-year note.

A comparable effect was observed for the 5-year Treasury note in analysis by Michael Fleming and Eli Remolona (1997). The key announcements were broadly similar, with Non-Farm Payrolls dominating, whilst PPI, CPI, Consumer Confidence, ISM/NAPM survey and

![](_page_16_Figure_1.jpeg)

Minutes Relative to the Announcement Time

Source: Balduzzi, Elton and Green (1997) Reproduced with permission from publisher Copyright © 2001, School of Business Administration, University Of Washington

#### Figure 14-9 Price responses of the active 10-year Treasury note to surprises in CPI

New Home Sales were also found to be significant. Though, they found Durable Goods Orders and Housing Starts had much less effect. Instead, they observed that Retail Sales and the Federal Funds Target rate were more important, as we can see from their relative rankings in Table 14-4.

Unfortunately, the complexity of the relationship between macroeconomic indicators and bond prices means that each study seems to find slightly different relationships. Some of this may be related to the investment timescales associated with different assets. Balduzzi, Elton and Green (1997) analysed the effect on 3-month bills, 2-year notes and 30-year bonds. They observed that the size of the reaction tended to increase with the maturity of the Treasury, highlighting the increased volatility of longer-term bond prices. A later study by Fleming and Remolona (1999) also focussed on this trend. They found this effect to occur for most announcements with the exception of the price indices (CPI and PPI) where the reaction seemed to remain constant for maturities over four years.

The number of announcements that affect different securities also seems to vary based on the maturity date. Balduzzi, Elton and Green (2001) reported that nine announcements significantly affected the price of the 3-month bill, whilst there were 13 for the 2-year note, 16 for the 10-year note, then falling back to 10 for the 30-year bond. This could be due to differences in the applicability of each announcement to both short and long-term expectations.

For exchange rates, Alain Chaboud *et al.* (2004) analysed the impact of announcements using data from EBS. They found sudden increases in price occurred almost instantly, but only lasted for about 5-10 minutes and generally stabilised in less than an hour. Surprises for GDP and Non-Farm Payrolls generally had the most effect. Overall, they found that news that indicated stronger than expected activity for the U.S. was systematically followed by dollar appreciation. A similar trend was reported in an earlier study by Torben Andersen et al. (2003). They observed the largest price changes for Non-Farm Payrolls and Trade Balance surprises, followed by Durable Goods Orders, Retail Sales and the Federal Funds

| Announcement <sup>1</sup>      | Effect on: 2 |         | Ranking by: |        |
|--------------------------------|--------------|---------|-------------|--------|
|                                | Price        | Volume  | Price       | Volume |
| Employment (Non-Farm Payrolls) | $-23.1$      | 60.52   |             | 2      |
| Producer Price Index           | $-8.59$      | 27.87   | 2           | 8      |
| Retail Sales                   | $-6.51$      | 39.03   | 5           | 4      |
| Consumer Price Index           | $-6.48$      | 24.56   | 6           | 12     |
| New Single-Family Home Sales   | $-5.08$      | 23.97   | 7           | 13     |
| Federal Funds Target Rate      | $-4.61$      | 60.8    | 8           |        |
| Consumer Confidence            | $-4.42$      | 9.62    | 9           | 16     |
| NAPM Survey                    | $-4.17$      | 35.83   | 11          | 5      |
| Industrial Production          | $-3.87$      | 17.81   | 12          | 14     |
| <b>Housing Starts</b>          | $-3.42$      | 12.05   | 13          | 15     |
| <b>Gross Domestic Product</b>  | -3.2         | 29.04   | 14          | 7      |
| Trade Balance                  | $-2.5$       | 4.94    | 15          | 21     |
| Construction Spending          | $-1.79$      | $-5.35$ | 16          | 19     |
| Consumer Credit                | $-1.7$       | 2,24    | 17          | 23     |
| Factory Inventories            | 1.61         | 27.55   | 18          | 0      |
| Durable Goods Orders           | $-1.41$      | $-5.1$  | 19          | 20     |
| Leading Indicators             | $-0.46$      | 2.28    | 22          | 22     |
| Federal Budget                 | $-0.29$      | $-1.86$ | 23          | 24     |
| Personal Income                | 0.19         | $-1.66$ | 24          | 25     |
| Business Inventories           | 0.05         | 24.88   | 25          | 11     |

Source: Fleming and Remolona (1997)

## Table 14-4 Impact of macroeconomic announcement surprises on the 5-year U.S. **Treasury note**

Target Rate. Though, there were slight differences for the various exchange rates, for instance, the Trade Balance had the most impact for the yen/dollar, whilst GDP advance notices were important for both the euro and the Swiss franc versus the dollar.

For equities, a study by Rui Albuquerque and Clara Vega (2007) analysed the response of the stocks in the Dow Jones Industrial Average (DJIA) and Portugal's PSI-20 indices to macroeconomic news. They grouped the announcements into classes, such as consumption and investment, but also analysed the impact of individual announcements. In general, for the DJIA, U.S. macroeconomic announcements led to an immediate response that stabilised within the first hour. Though, for the price indices (CPI and PPI) and Initial Unemployment Claims they found the impact was only appreciable for around the first ten minutes. Overall, the most positive responses were for good news in Personal Consumption Expenditures, Capacity Utilization, Personal Income, the Index of Leading Indicators and the Trade Balance. The most negative responses were for news on the GDP Advance, ISM/NAPM survey, Housing Starts, New Home Sales and the Federal Funds Target Rate. For instance, they found that a one standard deviation unexpected surprise in the Federal Funds Target

<sup>&</sup>lt;sup>1</sup> Note that Fleming and Remolona (1997) also included the results of Treasury auctions in their study. These have been excluded for ease of comparison with other studies. For reference the auction results for the 10-year note had the  $3^{\text{rd}}$  most significant effect on prices and the  $6^{\text{th}}$  most effect on volumes. The 30-year hond auction was  $4^{\text{th}}$  in terms of prices and  $3<sup>rd</sup>$  for volumes.

<sup>&</sup>lt;sup>2</sup> The effect column shows the actual coefficients from regressing the price and volume with the surprise factor which is based on the difference between the actual announcement and the expected forecast figures.

Rate could lead to a 0.5% decrease in the DJIA. Similar studies that focussed on the impact of FOMC announcements found around a 1% response for Federal Funds surprises. Michael Ehrmann and Marcel Fratzscher (2004) analysed the impact on the S&P 500 and Ben Bernanke and Kenneth Kuttner (2005) studied the CRSP value weighted index. Albuquerque and Vega (2007) reason that the difference in results is due to their sample being based on the DJIA which is a small sample of large firms, which are often less affected by monetary policy surprises.

A useful comparison of the effects for a range of futures contracts is provided in a study by Andrew Clare and Roger Courtenay (2001), shown in Figure 14-10. Using data for 1994-99, they investigated the impact of U.K. macroeconomic and interest rate announcements, which are generally released at 9:30am and 12:00pm. The aim of their study was to determine the effect of operational independence being granted to the Bank of England in 1997 allowing the Monetary Policy Committee to set interest rates.

![](_page_18_Figure_3.jpeg)

Source: Clare and Courtenay (2001) Reproduced with permission from Deutsche Bundesbank

### Figure 14-10 Impact of macroeconomic news on the prices of futures and currencies

They tracked the price reaction of curreneies and LIFFE futures contracts for short-term (Short Sterling) and long-term (Long Gilts) debt and the FTSE-100 stock index. The average hourly responses are shown in Figure 14-10. From these charts, it is clear that the interest rate changes have much more considerable effect on both the futures and the currency than other macroeconomic data. Interestingly, the largest overall impact for interest rates was for the FTSE-100 futures, although these had much less response to more general U.K. macroeconomic announcements. In comparison, the currency and Long Gilts appeared to be the most affected by general macroeconomic news. The Long Gilts also seemed to be more volatile than the Short Sterling, which is similar to what we have seen for U.S. Treasuries.

#### Volume

The fixed scheduling of many U.S. macroeconomic announcements makes their effect on trading activity and volumes easy to spot. For instance, the sudden peak in inter-dealer trading activity for Treasury notes at 8:30am is clear to see in Figure 14-11, taken from a study by Fleming and Remolona (1997). There is also a noticeable peak for the 10:00am news. Fleming and Remolona (1998) observed an almost identical trend for traded volume.

![](_page_19_Figure_4.jpeg)

Source: Fleming and Remolona (1997) Reproduced with permission from Federal Reserve Bank of New York

# Figure 14-11 Intraday activity on announcement days for five year U.S Treasury notes

Therefore, key macroeconomic announcements can lead to large, but short-term, increases in trading volume. This has been reported by a wide range of studies. For example, Fleming and Remolona (1998) observed elevated volumes in the 5-year note for over 90 minutes after Employment and CPI/PPI price index announcements. Similarly, a study of the effect of FOMC announcements by Michael Fleming and Monika Piazzesi (2005) analysed the impact for 3 and 6-month bills and 2, 5 and 10-year notes. They found a significant volume increase that lasted for around 45 minutes after the announcements, whilst volumes remained higher than normal for  $1\frac{1}{2}$  to  $2\frac{1}{2}$  hours.

In the previous section, we saw how each type of announcement had a markedly different effect on the market price. Fleming and Remolona (1997) also analysed the impact of each announcement on the trading volume. The results are displayed back in Table 14-4. The largest influence was held by the Federal Funds Target Rate and the Non-Farm Payrolls, which had virtually identical coefficients from the regression analysis. In terms of importance, these were then followed by Retail Sales, the ISM/NAPM survey, GDP, and PPI

announcements. In total, around a dozen of the announcements had a notable impact on trading volume. Balduzzi, Elton and Green (2001) found a similar number of key announcements.

The volume effects tend to be comparable across the range of Treasury securities, although the relative sizes differ. Fleming and Piazzesi (2005) found the largest percentage increases for the 3 and 6-month bills, with peaks of around 400%. In comparison, the increases for five and ten year notes reached about 150%. Likewise, a study by Balduzzi, Elton and Green (2001) found volume for the 10-year note peaked at around 170-200% of normal levels within the first fifteen minutes after the announcement. Though, for the 3month bill they found the volume effects to be much weaker.

Another trend Fleming and Piazzesi (2005) reported was a slight decrease in volumes around an hour before the announcements. They attribute this as being "the calm before the storm" when traders wait to see what news the announcement brings. Fleming and Remolona (1998) noted a slight lag of up to two minutes after the announcement when volumes remain at normal levels. This might be attributed to a delay whilst the market reacts to the news.

For exchange rates, Chaboud et al. (2004) focussed on a subset of indicators in their study of the impact of macroeconomic announcements. The reactions shown in Figure 14-12 are for Employment (Non-Farm Payrolls), since this had the largest impact. Note this is essentially a percentage change, since 100 represents the average one-minute volume. For comparison, the average volumes for non-announcement days are shown as dotted lines.

![](_page_20_Figure_5.jpeg)

Figure 14-12 Average one-minute volume on announcement days for (a) Euro/Dollar, (b) Dollar/Yen

GDP has nearly as much effect, followed by Retail Sales, Trade Balance and the Producer Price Index. The FOMC results had less immediate impact; however, their overall effect seemed to last longer. In addition, as we can see from the relative scales in Figure 14-12, the Dollar/Yen was much less affected than the Euro/Dollar; this trend was consistent across the other macro indicators.

## Liquidity

An appreciable increase in the bid offer spread often accompanies macroeconomic announcements. For instance, Fleming and Remolona (1998) observed sharp increases in the spread for five year U.S. Treasury notes around 8:30 and 10:00am on announcement days. Empirical studies also find a consistent trend for the effect on the bid offer spreads: Just before the announcement, they start to widen, peaking around the time of the news. The spreads remain at higher than normal levels for between half an hour to two hours afterwards. Fleming and Piazzesi (2005) found the 10-year note recovered fastest, in around 30 minutes. The 3 and 6-month bills and the 2-year note took much longer to recover. A similar effect was noted by Fleming and Remolona (1997a) and Balduzzi, Elton and Green (2001). The latter study also notes that the Employment report caused the most effect, both in terms of the size of the spread increase and its duration.

#### Volatility

The effect of news on short-term volatility can be extremely important, often more so than its effect on trading volumes. Some of the volatility is due to the market adjusting to the new information delivered in the news announcement, whilst some of it is also due to the sudden changes in trading volume and liquidity.

For U.S. Treasuries, the distinctive spikes in response to macroeconomic news at 8:30am and 10:00am are again evident in Figure 14-13 (as a standard deviation of log price changes), taken from Fleming and Remolona (1997).

![](_page_21_Figure_5.jpeg)

Source: Fleming and Remolona (1997) Reproduced with permission from Federal Reserve Bank of New York

#### Figure 14-13 Intraday volatility on announcement days for 5 year U.S Treasury notes

Studies by Fleming and Piazzesi (2005), Fleming and Remolona (1997a) and Balduzzi, Elton and Green (1997) all found that volatility increased immediately after the announcement, remaining at higher than normal levels for over an hour. For instance, Balduzzi, Elton and Green (1997) found that the volatility for the ten-year note stayed at more than twice its normal levels for 30-45 minutes afterwards. Fleming and Piazzesi (2005) found that the largest changes in volatility were for the 3-6 month bills and the 2-year notes.

In terms of the actual announcement types, Balduzzi, Elton and Green (2001) found that the largest increases in volatility were for the employment and PPI announcements, both for 3-month bills and 10-year notes.

For exchange rates, there is a similar spike in volatility around the announcement, as shown by the average absolute one-minute returns in Figure 14-14, taken from a study by Chaboud *et al.* (2004).

![](_page_22_Figure_1.jpeg)

Figure 14-14 Intraday volatility (in bps) on announcement days for (a) Euro/Dollar, (b) Dollar/Yen

They found that volatility also follows the same trends that we saw for FX trading volumes. Hence, announcements for employment, GDP and target federal funds rate had the most impact, followed by retail sales, trade balance and the PPI.

#### Reactions to corporate news/announcements

Corporate news is obviously much more closely linked to specific assets than macroeconomic news. That said, the information may also have a considerable effect on other firms in the same industry/sector, or the supply chain.

Earnings announcements are the corporate equivalent of macroeconomic indicators, so there is a lot of activity around these. Indeed, analysis of S&P 500 companies by Paul Tetlock, Maytal Saar-Tscchansky and Sofus Macskassy (2008) found that company news tended to cluster around earnings announcements.

#### Price

In a study of French stocks, Angelo Ranaldo (2008) confirmed that news events, and particularly earnings announcements, triggered significant short-term price changes. The effect on prices was much larger and lasted for up to an hour for earnings announcements, reflecting the additional information that they convey. He also noted that for intraday announcements the shift in prices actually started around ten minutes before a corresponding news item in his data. Potentially, these premature market movements are due to the fact that there are many sources of information available to traders, whilst his study focussed on Reuters headlines.

An interesting analysis of the effect of overnight earnings announcements was carried out by Louhichi Wael (2008), again for French stocks. Overall, he found that prices could increase by 1.7% for stocks where the announcement was good news, whilst bad news led to a fall of around 1%. These abnormal returns persisted for well over an hour for both types of news. Since his study focussed on overnight announcements most of these changes were achieved in the opening auction, yielding an increase of  $0.96\%$  for good news and  $-1.28\%$  for bad news. He also observed a slight reversal around half an hour after announcements of bad news, suggesting a possible initial overreaction.

For stocks, the effects of news can last days, weeks or even longer. Wael's (2008) study also analysed the performance for six days before and after each announcement. He found the abnormal results were mainly centred on the announcement day, although there were some minor reversals over the following days, particularly for bad news. The mid-term effect of news items on U.S. stock returns was also analysed by Paul Tetlock, Maytal Saar-Tsechansky and Sofus Macskassy (2008). They tracked around 350,000 news articles for S&P 500 companies. The news was taken from both the Dow Jones News Service (DJNS) and the Wall Street Journal (WSJ) from 1980 through to 2004. Stories were classified as positive or negative using lexicon-based sentiment analysis. Overall, they found effects persisted for over ten days after the announcement. Figure 14-15 shows a plot of the abnormal event returns covering ten days before and after a news story.

![](_page_23_Figure_2.jpeg)

Trading Day Relative to Story Release

Source: Tetloek, Saar-Tsechansky and Maeskassy (2007), Journal of Finance, Wiley-Blackwell Reproduced with permission from publisher

## Figure 14-15 Firms' valuations around news stories

As we can see in Figure 14-15, positive news led to similar improvements in returns, although the reaction to news from the Dow Jones news wire seemed to lag behind that for the Wall Street Journal. Whereas for negative news, there was a marked difference in the losses, with more effect seen from news published in the Wall Street Journal. They also noted that the market anticipated the news over the preceding days. In fact, the returns the day before the announcement could be nearly as important as those on the actual day the story broke. There was also a noticeable delay in seeing the full effect of the news, suggesting that it takes the market a while to fully react to it. This drift can actually last several days. The slight reversal that is visible for the reaction to bad news from Dow Jones also suggests that there may be a slight overreaction for bad news.

An earlier study of U.S. stocks by Wesley Chan (2002) found broadly similar results. He noted that stocks experiencing negative returns associated with news stories continued to under-perform their peers. In comparison, stocks with similar negative returns but no public news tended to see a price reversal in the following month. Much less price drift was evident with positive returns. He also found the drift to be more pronounced for smaller and less liquid companies.

One of the factors that make corporate announcements different from macroeconomic news is that the exact dates of these notices can vary considerably. Estimates for these used to be from calendar-based calculations, although it is becoming more common for firms to provide the expected dates for their next announcement. Products such as Thomson Financial's First Call Corporation now provide centralised sources for these dates. Other than providing a warning for upcoming announcements, the estimated dates may actually be used to help predict whether the news will be good or bad. This is because firms tend to be keen to announce good news and defer issuing bad news. A more quantitative analysis of this effect was performed by Mark Bagnoli, William Kross and Susan Watts (2004). They analysed the returns for U.S. stocks based on the lag between the estimated dates and the actual corporate announcements, for around 26,000 examples between 1995-8. They found that, on average, late announcements contained bad news  $44.5\%$  of the time, whilst this was only  $36.1\%$  for early or on-time announcements. The proportion increased so that after seven days late more than 50% of notices had bad news. For reporting losses they found that this was more than 90% more likely with late announcements than on-time ones. They found no such obvious trends for firms that made early reports.

Overall, Bagnoli, Kross and Watts (2004) discovered an average fall of one penny/share below the consensus forecasts for each day of delay from the expected date of the announcement. In terms of market prices, they observed similar declines for stocks that were late in making announcements. For instance, a delay of four days led to a cumulative loss of around 1% of returns. In addition to these losses, they also noted that the market reaction on the actual day of the announcement depended on how late it had been. Firms that reported late saw even more adverse reactions to bad results than those with similar results who reported on time. In comparison, they found the market reaction to be more aggressive for early announcements.

#### Volume

Unsurprisingly, corporate news also leads to noticeable short-term volume increases. Ranaldo (2008) observed this in terms of hoth volume and number of trades in his study of French stocks. Wael (2008) also found that for both good and bad news trading volumes increased slightly up to thirty minutes before the news breaks. Though, the most significant shift was still centred in the ten minutes around the actual announcement. He also noted that the heightened trading volumes persisted for around two days when the news was bad, and for five days after good news. Similar volume effects were found for the Spanish stock exchange by David Abad, Sonia Sanabria and José Yagüe (2005). They noted that both trading volume and frequency were unusually high up to three hours before the announcement, together with a sizeable increase when the news was released. These effects then persisted at abnormal levels for the rest of the trading day.

As we have already seen with prices, the effect of news on trading volumes can often be more prolonged for stocks; indeed, the volume increase can drift over days and weeks. For example, a study of U.S. stocks by Joon Chae (2005) found announcements had a considerable effect on volumes for more than 15 days afterwards. He also noted that the volume preceding scheduled earnings announcements actually decreased slightly in anticipation of the results. Although for unscheduled announcements, such as changes in Moody's ratings, takeovers or acquisitions, he found that the volume increased noticeably in the days beforehand.

#### Liquidity

The effect of corporate news on liquidity is less clear-cut, since the results of empirical research are mixed. Some studies find marked decreases in liquidity around announcements whilst some report increases and others find the changes to be negligible.

A decrease in liquidity around corporate announcements has been noted for studies of the NYSE by Kenneth Kavajecz (1999), Itzhak Krinsky and Jason Lee (1996) and Charles Lee, Belinda Mucklow and Mark Ready (1993). These showed how the quoted spreads increased whilst the available depth, from both specialists and the order book, decreased. Similarly, Jean-François Gajewski (1999) found that spreads widened after corporate announcements for French stocks.

A noticeable increase in liquidity was found to occur after the announcement in a study of the Spanish stock exchange by Abad, Sanabria and Yague (2005). They used a wide range of measures to analyse the available liquidity. In the time before the announcement, they found no notable changes in the bid offer spread or order book depth. Though, for around 90 minutes after the announcement, they observed a marked narrowing of the spread and an increase in the available depth. After this period, these returned to more normal levels. Wael (2008) found a similar decrease in spreads for French stocks, but also noted that spread levels were noticeably higher in the days preceding the news. Alternatively, Kazuhisa Otagawa (2003) found a consistent decrease in spreads both before and after quarterly earnings announcements for Japanese stocks. On the announcement day, market depth was found to improve slightly as well.

Not all research has found a noteworthy change in liquidity around corporate news events. For example, in a study of German stocks Peter Gomber, Uwe Schweickert and Erik Theissen (2004) tracked changes using the Xetra Liquidity Measure (XLM). Overall, they found no significant changes in the available liquidity at the time of the actual news item. Though, they did observe a slight decrease in liquidity in the fifteen minutes before the news release, which they attribute to traders having access to multiple information sources. The effect was most noticeable for the less liquid non-DAX stocks. Fifteen minutes after a news item, their XLM cost had increased by around 3% hence giving a slight reduction in their overall liquidity. In comparison, DAX stocks actually saw around a 3% reduction in their XLM cost after a news item, suggesting a slight improvement.

Some of these differences may be attributable to the markets being studied. For instance, markets where liquidity is provided by market makers or specialists may well exhibit increased spreads around announcements, as dealers try to minimise the cost of trading with more informed traders. Though, as Ranaldo (2008) points out, this effect may be reduced by competition between liquidity providers. In some markets, the liquidity may shift to hidden orders or on to "dark pool" ATSs. For instance, a study of the INET ECN (now part of NASDAQ) by Bidisha Chakrabarty and Ken Shaw (2006) showed that both the number and average size of hidden orders increased around earnings announcements, lasting up to seven days afterwards.

The information content of the news is another potential factor. An increase in liquidity after an announcement may suggest a decline in information asymmetry between traders. A study of French stocks by Faten Lakhal (2008) found that the uncertainty around earnings forecasts triggered an increase in spreads, leading to a decrease in the available liquidity. In comparison, the certainty of quarterly announcements was found to lead to an increase in liquidity. Wael (2008) also noted that the immediate impact on liquidity after an announcement was very much dependent on what information was imparted. Announcements that met expectations (no news) saw an immediate decrease in their spreads, which then gradually reverted to normal levels over the next 90 minutes. Unexpected news took longer to react: For good news, spreads returned to normal about half an hour after the announcement, whilst for bad news they took nearly an hour. Similarly, unexpected news seemed to lead to much higher spreads in the half hour before each announcement, again this effect was most pronounced for bad news.

The level of information may also be reflected in differences between quarterly and annual reports. A study of earnings announcements by Theresa Libby, Robert Mathieu and Sean Robb (2002) found that the changes in liquidity were greater for quarterly announcements than annual ones.

Dispersion in market expectations may be another factor accounting for these differences. For instance, a study of NASDAQ by John Affleck-Graves, Carolyn Callahan and Niranjan Chipalkatti (2002) found that firms with less predictable carnings had consistently higher spreads, particularly in the days around announcements.

One last potential factor is the timing of the announcements. A study of the Spanish stock exchange by Abad, Sanabria and Yagüe (2005) found that overnight announcements led to an immediate improvement of liquidity at the following open. They reasoned this was because investors and traders had the time to properly evaluate the information. For intraday announcements, they found that it took around 90 minutes after the news before a notable improvement in liquidity was observed. They also noted a tendency for Spanish firms to prefer intraday releases when earnings were lower than expected.

#### Volatility

Volatility is usually higher immediately after a corporate announcement. Ranaldo (2008) found higher levels to persist for 10 minutes after firm-specific news and for over 40 minutes after earnings announcements. Likewise, Abad, Sanabria and Yagüe (2005) noted significantly raised levels of volatility for around 45 minutes after earnings announcements.

The volatility may also be affected by whether the news is good or bad. Unsurprisingly, after bad news Tetlock, Saar-Tsechansky and Macskassy (2008) found there to be higher levels of volatility. Wael (2008) also noted that it takes longer for the market to adjust to bad news than good. Thus, higher volatility persisted for nearly an hour after bad news, compared to around half an hour for good news.

#### Other factors which affect the impact of news

The effect that news has obviously depends on the information that it brings to the market. News provides information that either confirms or confounds the market consensus. So the degree of surprise indicates how the market will react. The timeliness of news also dictates whether it is new information or simply a confirmation of existing data.

Market conditions and the business cycle are another important consideration, since these reflect investor sentiment. In a declining market, even good news can fail to buck the trend. Therefore, the reaction to news is also dependent on the prevalent conditions.

#### Reactions to surprises

In order to gauge the degree of surprise, we need a common source of expectations. For macroeconomic indicators this means data from consensus forecasts. These are provided in publications such as the Wall Street Journal and Barron's. Another source, widely used in research studies, is the consensus forecasts from Money Market Services International (MMS). These surveys of money market managers provide estimates for what they expect

the upcoming economic announcements to be. Based on these expected values, we can then determine how much of a surprise the actual announcements really are.

In their analysis of U.S. Treasuries, Balduzzi, Elton and Green (1997) confirmed that the size of the surprise affected the price change. They highlighted the potential impacts by expressing the price changes caused by a one standard deviation surprise, as a percentage of the daily volatility, shown in Table 14-5.

| Macroeconomic announcement                                                             | Price change as %<br>of daily volatility |  |  |
|----------------------------------------------------------------------------------------|------------------------------------------|--|--|
| Non-Farm Payrolls                                                                      | 89                                       |  |  |
| $\text{PPI}$                                                                           | 39                                       |  |  |
| CPI, Durable Goods Orders, Retail Sales,<br>NAPM Index, Consumer Confidence            | $25 - 30$                                |  |  |
| Initial Jobless Claims, Capacity Utilization,<br>Industrial Production, New Home Sales | $12 - 19$                                |  |  |
| Factory Orders, M2 Medians                                                             |                                          |  |  |

Source: Balduzzi, Elton and Green (1997)

#### Table 14-5 Effect of macroeconomic surprises on U.S. 10-year Treasury notes

For example, a one standard deviation surprise in Non-Farm Payrolls was around 110,000. An unexpected announcement with a corresponding increase could lead to a price change equivalent to nearly 90% of the daily volatility. Given a daily volatility of 0.47% for the 10year note, this equates to a price change of 0.418% due to the surprise. They also confirmed that procyclical indicators, such as Non-Farm Payrolls, had a negative effect on bond prices, whilst counter-cyclical ones, such as Initial jobless claims, had a positive effect.

In terms of trading volume, Balduzzi, Elton and Green (1997) found little evidence for it being affected by the size of surprises. They reasoned that the trading volume is more closely related to the dispersion of views across the market.

#### Timeliness

The timeliness of an announcement particularly applies to the regular macroeconomic announcements. It helps quantify their information content by relating them to the data they are based on. Fleming and Remolona (1997) used the timeliness of an announcement to help explain its impact on U.S. Treasury prices. Likewise, David Vcredas (2006) used it to explain the behaviour of Treasury futures.

For example, Figure 14-16 shows some of the major U.S. macroeconomic announcements ordered in terms of the data they are based on, taken from an article by Fleming and Remolona (1997). Consequently, the forward-looking Consumer Confidence measure is on the far left hand side. The majority of announcements are in the middle since they report on results for the previous month. On the right hand side, the Trade Balance reports two month old data, so as an announcement it imparts less new information to the market when compared to other indicators. Less timely reports are likely to have less impact on prices and volumes, which is indeed what Fleming and Remolona (1997) observed for the U.S. Treasury markets. Hence, the timeliest reports, such as Employment, PPI, CPI and Retail Sales tend to have the strongest effects.

In comparison, the forward-looking indicators, namely Consumer Confidence and the ISM/NAPM survey have slightly less impact. This is probably because they are forecasts

![](_page_28_Figure_1.jpeg)

Source: Fleming and Remotona (1997) Reproduced with permission from Federal Reserve Bank of New York

#### Figure 14-16 U.S. macroeconomic announcement release dates

rather than actual reports, so the bond markets attribute more weight to the real data.

Veredas (2006) took a similar approach in his study of the 10-year U.S. Treasury note future. He used timeliness to rate the impact of different announcements, as shown in Figure 14-17. The forward looking consumer confidence (CC) and ISM/NAPM surveys were given more weight by the futures market, whilst employment remained the most significant report. As with the underlying bonds, important announcements such as GDP and the trade balance actually had only a limited effect, since they relay very little new information.

![](_page_28_Figure_6.jpeg)

Source: Veredas (2006), Journal Empirical Economics, Physica-Verlag Heidelberg, Reproduced with permission from publisher

#### Figure 14-17 The impact of timeliness for the U.S. 10-year Treasury note future

Another point to consider is that market reactions are not always for the latest figures. Revisions to key macroeconomic indicators can have a considerable effect as well. Indeed, Veredas (2006) notes that the repeated revisions for GDP help to reduce market interest in it as an indicator.

## Market conditions

In their study of the response of U.S. Treasuries to news, Fleming and Remolona (1997) also considered the potential effects caused by market conditions. They demonstrated that the price reaction for a given surprise was often greater during conditions of increased uncertainty. As indicators for market uncertainty, they used the implied volatility of Treasury futures options together with the expected change in the Federal Funds Target Rate. For the price impact on the 5-year note, they found that the uncertainty from implied volatility helped explain the market reaction to announcements for Durable Goods Orders, Housing Starts and GDP surprises. The expected change in the Federal Funds Target Rate helped explain the reaction of Employment and Durable Goods Orders surprises.

In terms of trading volume, they noted that both indicators still had an effect, although the links were somewhat weaker than for prices. Both indicators of uncertainty helped explain the increases for CPI, PPI and Trade Balance surprises. As with prices, the expected Federal Funds Target Rate also helped to account for the increases for Employment and Durable Goods Orders surprises.

#### **Business cycle**

The business cycle is closely related to market conditions. We can break down the cycle into four main stages which reflect when the market is at its top or bottom, and when it is either expanding or contracting. News surprises may well have considerably different impacts depending on what stage of the business cycle the market is at. Intuitively, we might expect the most impact to be in the expansion and contraction parts of the cycle, since these phases are more likely to have higher uncertainty/volatility.

One measure of the business cycle is an index from the Institute for Supply Management (ISM). Unlike factors like the GDP, it is a forward-looking measure, based on a survey of market expectations from the manufacturing industry. More details about the ISM may be found in Niemira and Zukowski (1998).

David Veredas (2006) used the ISM to confirm whether business cycles do indeed alter the impact of macroeconomic news on the price of U.S. 10-year Treasury note futures. He found a strong inverse correlation  $(-0.71)$  between the futures price and the ISM, which is shown in Figure 14-18. For each peak in the ISM, the price of the Treasury future was generally at a low, and vice versa: Based on historical data, Veredas (2006) concluded that when the ISM was above 55 the business cycle was at a top, whilst below 50 it was at a bottom. In between this range, a rising value was treated as the expansion part of the cycle, whilst a falling one indicated a contraction.

Veredas also analysed the impact of surprises on the price of the futures contract during specific cycles. Overall, he found that news tended to have more effect in down cycles than in up cycles. He noted that bad news had more impact in good times than bad, whilst good news had less effect when the cycle was already depressed. As an illustration of this Figure 14-19 shows corresponding plots of the impact of surprises in the figures for Consumer Confidence. Note that the solid lines show the average response whilst the dotted lines are only negative surprises and the dashed lines only positive ones. The time axis represents tenminute intervals.

When the business cycle is down or contracting (shown on the right hand side of Figure 14-19) we can see that any type of news has a negative impact on prices. Interestingly, in these depressed phases positive surprises seem to cause the most impact.

![](_page_30_Figure_1.jpeg)

Source: Veredas (2006), Journal Empirical Economics, Physica-Verlag Heidelberg, Reproduced with permission from publisher

![](_page_30_Figure_3.jpeg)

![](_page_30_Figure_4.jpeg)

Source: Veredas (2006), Journal Empirical Economics, Physica-Verlag Heidelberg, Reproduced with permission from publisher

## Figure 14-19 Impulse responses of U.S. 10-year Treasury note price to shocks in Consumer Confidence when economy is in the (a) top, (b) bottom, (c) expansion, (d) contraction part of the cycle

When the cycle is at a top or in expansion (shown on the left hand side of Figure 14-19), we can see that negative surprises led to the largest price drops. Overall, for Consumer Confidence the most significant price drop seems to be caused by negative surprises in an expansion cycle. Veredas notes that whenever the indicator was against the trend it seemed

431

to have more impact, probably due to more publicity. It is also worth noting that in most of these cases the initial impact dissipated reasonably quickly, with the prices returning to normal within one or two hours of the news.

## 14.6 Incorporating news into trading strategies

Precognition, or "second sight", would clearly be a very useful add-on for most investment and trading strategies. However, the focus of this book is on execution, not investment. Though we may not be able to reliably predict exactly what information news will bring, we can still estimate how the market might react, as we saw in the previous section. These shortterm predictions of market conditions may enable our trading strategies to take advantage of the market response, rather than simply reacting to the rapidly changing conditions.

Even though we are using news to augment trading strategies, rather than to generate investment ideas, certain precautions are still necessary. Correct interpretation is vital otherwise, the estimates for the market response will be wrong. The accuracy and validity of information is also important.

An easy way of incorporating news into trading strategies is to use indicators. They provide a simple means for algorithms to interpret whether news is good or bad, and so respond accordingly. These may then be added to adaptive trading algorithms alongside the price trend and short-term liquidity indicators that many already use. In the future, we might also start to see more opportunistic news-driven algorithms.

## Precautions for automated news handling

We have become used to trading algorithms and execution tactics routinely making automatic decisions about the location, price and size of orders. These decisions are often based on a mix of historical and real-time market data, and the responses are driven by rules specified by expert traders and subjected to rigorous testing. Increasingly, though, algorithms are becoming even more adaptive, responding dynamically to changing market conditions, such as liquidity. Therefore, reacting to news may just be viewed as another real-time adaptation. Just as with anything else, the standard computer maxim of "Garbage in, garbage out" applies. Bad data or poor interpretations could lead to expensive mistakes.

Market conditions, such as prices, spreads or depths, correspond to actual quantifiable factors. News is always an interpretation, even if this is done by a vendor rather than inhouse systems. Thus, accuracy and authenticity are obviously key concerns when leaving a system to automatically react to news headlines/stories. Though, in the short-term, whether it is inaccurate or even false is less significant, since the whole market reacts to the same news.

Given that bad news data of one sort or another is almost certain to creep through at some point, it is important to apply some additional controls/sanity checks. If the market reacts as expected then we may assume the news is being treated as valid by other market participants. If not, then it may be safer to trigger an alert allowing a trader to monitor the situation and either intervene or resume the trading algorithm. These checks may need to be performed repeatedly after any news announcements. So an immediate aggressive response to a news item may not be the best approach, although neither is waiting until the market reaction has subsided. We need to strike some sort of balance, trying to safely capitalise on advantageous conditions without taking excessive risks, much like the behaviour of an adaptive shortfall or a liquidity-based algorithm.

On the other hand, we may not even be alerted about a news story. The news filtering may not identify the story as being relevant for our order. News handling systems may fail to correctly identify the key entities affected by the story. Alternatively, the news vendor might accidentally miss an important tag, or fail to consistently tag all stories in the same way. Whatever happens, though, the news will still spread and the market will still react. Hence, in such cases we are reliant on the trading algorithm simply adapting to the changing market conditions, just as it would if there were no news component.

## Potential news-based indicators

Converting textual information from news into a numeric indicator makes it much easier for computer-based systems to react to it. Obviously, this is easier to do for some news, such as macroeconomic or earnings announcements, than others. As we saw in section 14.3, the increasing digitization of news and corporate reports means that soon much of this key information will be readily available digitally.

News indicators can range from a simple count of the number of stories to more complex sentiment-based analysis. They can also be used to quantify the difference between consensus estimates and actual announcements.

#### News flow

Following the old adage "There is no smoke without fire", news flow is itself an important trading signal. The sheer volume of news items can be just as much an indicator as the actual information they convey. Clearly, we cannot reliably use the number of headlines to predict future prices; for that we need to know whether the news was good or bad. Though, a sudden rush of headlines does suggest that volatility may increase, since uncertainty breeds volatility. Therefore, by tracking the amount of news generally associated with a given topic or asset we can determine historical averages.

![](_page_32_Figure_7.jpeg)

Source: © Ranaldo (2008)

Reproduced with permission from author

Figure 14-20 Intraday news patterns

Time of day effects may need to be taken into account as well, since news events can cluster around the open and close, as we can see in Figure 14-20. This shows the results from a study of news patterns for French stocks by Ranaldo (2008). In particular, he found the peaks for news were most pronounced for the CAC 40 index compared to firm specific news.

Thus, when news levels rise significantly above the historical average we have an immediate indicator that something unusual is happening. This gives us a very quick and easy way of tracking potential issues, since we do not even need to read or interpret the actual news stories. For example, Relegence calculates a news heat index, based on the number of stories for a specific company, converting this to a scale ranging from  $-4$  to  $+4$ .

For traders, a news flow indicator acts as a simple alert, allowing them to study the situation more carefully. Whilst for trading algorithms, it can be used as an indicator that short-term volatility is likely to increase. So, risk and cost-based algorithms can then adjust their trading strategies accordingly.

## **News sentiment**

In section 14.4, we saw how news items could be analysed to extract whether they represented good, bad or neutral information. By assigning these sentiments numeric scores we can calculate averages, so we can determine the prevalent market sentiment hour by hour or day by day. We can also track sentiment over time just as if it were price or return data. For instance, Figure 14-21 shows charts of the stock prices and sentiment for two companies, from a study by Sanjiv Das (2005). The sentiments were determined from statistical analysis of bulletin board messages; each point on the charts represents the arrival of a new message.

![](_page_33_Figure_6.jpeg)

Source: © Das (2005)

Reproduced with permission from author

## Figure 14-21 The stock prices (upper) and sentiment (lower) charted throughout the trading day

Obviously, substantial changes in price can have a marked impact on the associated sentiment, as we can see in Figure 14-21. Though, inferring future changes in price based on the sentiment is more complex. For example, the continued shift in sentiment for Dell Computer seen in Figure 14-21 is not immediately reflected in the market price. So, at the level of individual companies, the complex relationship between sentiment and price can make it difficult to reliably take advantage of this information.

Sentiment scores may also be aggregated across sectors or indices to create broader indicators, as shown in Figure 14-22. Sanjiv Das and Mike Chen (2007) found a significantly stronger correlation between sentiment and returns for indices than for individual stocks. In their study, they aggregated the sentiment for the 25 stocks in the Morgan Stanley High Tech Index (MSH), based on nearly 150,000 bulletin board messages. The correlation between the two series shown in Figure 14-22 was relatively low, only 0.48. Though, using regression analysis Das and Chen found that the MSH 35 index was strongly related to its value from the previous day and was also significantly related to the sentiment index value from the prior day. In comparison, the sentiment index was found to have no such dependency on the stock index, so they concluded that the causality flowed from the sentiment to the stock index. Thus, sentiment offered some explanatory power for the level of the MSH 35.

![](_page_34_Figure_3.jpeg)

Copyright 2007, the Institute for Reprinted by permission Source: Das and Chen (2007) Operations Research and the Management Sciences, 7240 Parkway Drive, Suite 300, Hanover, Maryland 21076

Figure 14-22 Comparing the MSH Index with aggregated sentiments

They also found that higher trading volume was significantly correlated with positive sentiment, but could find no relationship between volume and the previous day's sentiment.

#### **News surprises**

As we have already seen, the size of the surprise information contained in a news story can often have a substantial effect on market conditions, particularly prices. Some news obviously lends itself to this approach more than others. Macroeconomic or corporate announcements deliver new numbers to the market, whether they represent Non-Farm Payrolls figures or a firm's quarterly earnings. These may quickly be compared with expected figures to determine how much of a surprise they represent. A nice example of this is given in a study by Linda Goldberg and Deborah Leonard (2003). Figure 14-23, reproduced from this study, shows the monthly changes in Non-Farm Payroll data together with the market expectations from MMS surveys between January 2000 and June 2002.

![](_page_35_Figure_1.jpeg)

Source: Goldberg and Leonard (2003) Reproduced with permission from Federal Reserve Bank of New York

## Figure 14-23 U.S. Non-Farm payrolls: Announcements, expectations and news

To quantify the size of any surprises they normalised the difference between actual and expected figures by dividing by the standard deviation of Non-Farm Payrolls relative to expectations for the period. For real-time analysis, we could adopt a similar approach using a standard deviation hased on historical data. The normalisation confirms that events such as the ones at 7/00 and 2/01 are statistically significant. Based on the empirical results we have already seen, we might expect the surprise factor of such events to have a noticeable effect on the market. Since this news is easy to interpret, it is also likely that the impact will be relatively short-lived, as the market can rapidly incorporate the information into its prices.

Other types of news may require much more analysis in order to interpret their information. Quantitative models or fundamental analysis may be required to recalculate new fair values for assets. Some news may be extremely difficult to quantify, such as the resignation of a senior executive or losing a key contract. Hence, such news tends to take longer for the market to react to. There may also be a wider range of interpretations, so this dispersal of views could lead to an increase in volatility. There might even be a decline in liquidity while the market analyses the potential effects. So even for more complex news items without fully interpreting them we may be able to make some simple estimates of their short-term effect on the market's liquidity and volatility.

#### News-based algorithms

News-based algorithms have already attracted the moniker "news flow" algorithms. Note that our focus remains on execution, rather than automated trading. Consequently, news is simply treated as information that affects our execution decisions. Unlike price, volume, liquidity or volatility, news is not a core market variable - it arrives sporadically. The arrival of news is a factor that has a clear short-term impact on these market variables, as we saw in section 14.5. Focussing solely on news cannot guarantee to meet specific investment objectives such as minimising market impact or transaction costs. For this reason, newsbased algorithms are clearly more opportunistic in nature.

## Incorporating news handling into existing algorithms

Just as price and liquidity-adaptive behaviour is being incorporated into existing algorithms, the same can be done for news. Adding a news handling capability may well improve their performance when news events do occur. For example, VWAP algorithms could modify their target volume profiles to account for the news release, whilst shortfall-based algorithms could alter their short-term volatility estimates. Similarly, temporary adjustments could be made to limit order models used by cost-based algorithms or execution tactics to determine the optimal approach for order placement. Thus, news just becomes another factor, like price and liquidity, upon which algorithms and execution tactics base their order placement decisions.

## **News-adaptive algorithms**

These are the news-based equivalents of price-adaptive algorithms. In which case a newsadaptive algorithm might trade a sell order less aggressively when good news arrives, whilst for a buy order it might be more aggressive. Clearly, this approach is closely related to priceadaptive algorithms. However, since news is the trigger the decisions are effectively making short-term estimates of how they think the price will react to the news. So long as the market reaction behaves as expected, the news adaptation should give slightly better results than the more reactive price-based approach. Again, this highlights the importance of inhuilt monitoring to ensure that the market does react as our interpretation of the news suggests.

## **News-driven algorithms**

Market prices and trades vary continuously throughout the day, hence algorithms such as percent of volume or price inline can constantly track this data and adjust their trading patterns accordingly. In comparison, the arrival of news is a much more discrete event. Each day there might only be a handful of news stories that might affect an order, and often there may be none. Even for a worst case scenario there is likely to only be a few pieces of significant news arriving in a day. There may well be 30 or 40 different stories, but many of these will simply be the same information from different sources, possible revisions, or daily summaries outlining the effect the news has had on the market. Thus, if an order is to be driven solely by news it will tend to behave more like a conditional order, only being activated if good (or bad) news appears. For some investment firms news-conditional orders may act as a useful placeholder to reduce (or increase) their position if a certain event occurs. Essentially, though, it is much like a stop order, but based on information rather than price. In fact, a stop order (or trailing stop) might be used just as well, given a reasonably accurate estimate for the potential impact of the news.

In the future news-driven algorithms may well become more complex, but at the moment it is hard to tell what form these might take.

# 14.7 Summary

- Adapting to breaking news events can give traders a significant edge, although people are still more adept at interpreting news and events than machines.
- Major news wires and press services have been electronic for a long time. Conventional  $\blacksquare$

media is now facing competition from social media, such as message boards and blogs.

- Computer-based news analysis is a non-trivial task Complex artificial intelligence and natural language processing techniques are being employed to analyse unstructured text:
  - News filtering searches for keys to narrow the amount of information.
  - News association uses relationships to spot secondary/tertiary effects.
  - News analysis is primarily sentiment analysis at the moment.
  - News interpretation combines information with asset pricing models for forecasts.
  - News mining combines the analysis of historical data with information from news archives, helping to find causal relationships between the news and market prices.
- Market reactions to news depend on the information relayed and market conditions.
  - With macroeconomic news, the reaction varies for different assets. For instance, news of an interest rate drop will help increase the price of existing bonds, but weakens the currency. Corporations may benefit from lower interest rate, but may also suffer from the weaker currency.
  - For corporate news, the reaction is more closely linked to specific assets, although it may also have an effect on other firms in the same industry/sector.
- News-based indicators may easily be added to existing trading algorithms:
  - News flow can help to forecast future volatility.
  - Sentiment can be tracked over time just as if it were price or return data.
  - Surprise relates to the difference between consensus estimates and actual figures.
- News is not a core market variable like price. Each day there might only be a handful of news stories that affect an asset. So:
  - News-adaptive algorithms use appropriate indicators for short-term estimations of how the market may react to the news.
  - News-driven algorithms are likely to be more like conditional orders, triggered by a set outcome or information.
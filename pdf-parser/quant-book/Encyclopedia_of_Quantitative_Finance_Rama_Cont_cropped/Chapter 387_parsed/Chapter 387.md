# Reinsurance

In a reinsurance contract, one party (the reinsurer) agrees to indemnify for a certain premium another party (called the *reinsured*, the *first-line insurer* or also the *ceding company*) for specified parts of its underwritten insurance risk. Hence, reinsurance is a form of risk sharing between insurance companies (cf. [3]). One among the main motivations for an insurance company to buy reinsurance is to reduce the probability of suffering losses that it cannot easily cope with, in particular, the appearance of excessively large or unusually many claims from the underwritten policies. Also, reinsurance is a way to increase the underwriting capacity (which is particularly but not exclusively relevant for smaller insurance companies) and can be interpreted as a (virtual) increase in the solvency (see Solvency) capital of the ceding company. Replacing a part of the random costs (claims) by fixed costs (premiums) is the core insurance activity and helps the policy holders to stabilize their business. But this also applies to the first-line insurer as a reinsurance customer and reinsurance can increase the effectiveness of the marketplace. For the same reason, a reinsurance company may itself, again for some suitable premium, pass on parts of the reinsured risks to another reinsurer (both domestic and international), which is then called *retrocession*. For the general concept of the *need for reinsurance* see, for example, Gerber [16] and Schnieper [25].

The type and amount of reinsurance coverage may be negotiated for individual risks in the portfolio (*fac*ultative reinsurance). But predominantly reinsurance *treaties* are signed, which are obligatory agreements that specify the type and amount of reinsurance coverage for an entire portfolio of risks within an insurance branch (usually for a time horizon of one year).

Among the crucial questions in the context of reinsurance are:

- Which type of reinsurance form is appropriate in a given situation?
- How much reinsurance should be purchased?
- What should be the premium?

# **Forms of Reinsurance**

Let  $X(t) := \sum_{i=1}^{N(t)} X_i$  denote the aggregate claim amount in an insurance portfolio up to time  $t$ , where

the counting process  $N_t$  specifies the number of claims up to time t and the random variables  $X_i$ denote the individual claim sizes. In every reinsurance treaty, this amount is split into  $X(t) = D(t) +$  $R(t)$ , where  $D(t)$  is the amount that the insurance company retains for itself (the *deductible*) and  $R(t)$ is the *reinsured* amount to be covered by the reinsurance company.

There are two types of proportional reinsurance forms.

#### Quota-Share Reinsurance

A very common and simple reinsurance form is the  $\text{quota-share (QS)}$  treaty, where one has

$$R(t) := a X(t), \qquad D(t) := (1 - a) X(t) \qquad (1)$$

for some proportionality factor  $0 < a < 1$ . In this case, it is straightforward to calculate the distribution of  $R(t)$  and  $D(t)$ , once the distribution of  $X(t)$  is known.

## Surplus Reinsurance

While in a QS treaty also small claims are reinsured (which the first-line insurer often wants to keep for himself), a surplus treaty only reinsures claims  $X_i$  whose corresponding insured sum  $Q_i$ exceeds some retention  $M$ . In the latter case, the first-line insurer deducts a proportion  $M/Q_i$  and shifts the remaining part to the reinsurer. Consequently,

$$R(t) = \sum_{i=1}^{N(t)} \left(1 - \frac{M}{Q_i}\right) X_i \, 1_{\{Q_i \ge M\}},$$
$$D(t) = \sum_{i=1}^{N(t)} \left(X_i I(Q_i \le M) + M \frac{X_i}{Q_i} \, 1_{\{Q_i > M\}}\right) \quad (2)$$

Surplus treaties are quite popular in practice, in particular in fire, marine, and storm insurance.

Other types of reinsurance forms are of nonproportional nature.

## Excess-of-Loss Reinsurance

In an excess-of-loss (XL) treaty, for each individual claim the excess over some retention  $M$  is paid by the reinsurer:

$$R(t) := \sum_{i=1}^{N(t)} (X_i - M)^+, \quad D(t) := \sum_{i=1}^{N(t)} \min(X_i, M)$$
(3)

XL covers are, for instance, popular in casualty and windstorm insurance. In most situations, there is an upper limit  $L$  of the XL cover of each risk as well, resulting in the treaty

$$R(t) := \sum_{i=1}^{N(t)} \min\{(X_i - M)^+, L\} \tag{4}$$

where  $L$  is then the size of the so-called *XL* reinsurance layer (the usual notation is then  $L \text{ } xs \text{ } M$ ). It is also common to have an upper limit  $k \cdot L$  on the total reinsured amount  $R(t)$  for some integer k. In the latter case, one is said to have  $k$  reinstatements and, depending on the contract, the premium for a higher reinstatement often only has to be paid once the lower reinstatement is used up.

A variant of XL reinsurance is the per-event XL cover (or sometimes called *catastrophe XL cover*), where all claims due to some external event such as a storm or an earthquake are first added and then treated as a single claim in an XL contract (avoiding the issue that for many small claims the XL treaty may not provide sufficient protection).

## Stop-Loss Reinsurance

The stop-loss  $(SL)$  treaty acts on the aggregate claim amount  $X(t)$  of the portfolio:

$$R(t) := \left\{ \sum_{i=1}^{N(t)} X_i - C \right\}^+, \quad D(t) := \min(X(t), C) \tag{5}$$

where  $C$  is some retention. In general, there is again an additional upper limit on  $R(t)$ .

In practice, often combinations of the above reinsurance forms are employed (together with upper limits on the total reinsurance cover).

#### Large-Claim Reinsurance

Let  $\{X_1^*, X_2^*, \ldots, X_{N(t)}^*\}$  denote the order statistics of the claims ordered according to their size. Then the largest claims reinsurance is defined through

$$R(t) := \sum_{i=1}^{r} X_{N(t)-i+1}^{*}, \quad D(t) := \sum_{i=1}^{N(t)-r} X_{i}^{*} \quad (6)$$

that is, the reinsurer covers the  $r$  largest claims of the portfolio that have occurred up to time  $t$  (which again usually is 1 year). Another variant called excedent *du cout moyen relatif* (ECOMOR) was introduced by Thépaut [27] with a reinsured amount of the form

$$R(t) := \sum_{i=1}^{N(t)} \left\{ X_i - X_{N(t)-r}^* \right\}^+ \tag{7}$$

so that in this case the reinsurer covers only that part of the  $r$  largest claims that overshoots the random retention  $X_{N(t)-r}^*$ . Such a contract gives the reinsurer protection against claim inflation, since if the claim amounts increase, the retention will also increase.

Although theoretically appealing, large-claim reinsurance treaties are rarely applied in practice.

## **Reinsurance Premiums**

In the first place, reinsurance is a specific form of insurance. Consequently, the principles of premium calculation (see Actuarial Premium Principles) can, to some extent, also be applied in the reinsurance setting, once the moments or even the distribution of the number and the size of the reinsured claims are available (although costs and loading factors will in general be different). Extreme value statistics is of vital importance in this context, since typically the reinsured claims are heavy tailed and their distribution has to be estimated, often on the basis of only a few data points (see Heavy Tails in Insurance and  $[14]$ ).

Whereas for proportional reinsurance the actuarial reinsurance premium will simply be the corresponding proportion of the premium that the firstline insurer has received for the underlying risks (minus some acquisition and administration costs), the situation for nonproportional reinsurance is more involved.

The claim number process for the reinsured claims in an XL treaty can be interpreted as an independent thinning of the point process (see **Point Processes**) that generates the claims for the first-line insurer. For many practically relevant examples, the resulting

3

claim number process for the reinsurer is then of the same form with just some parameters modified (see, e.g., [4]). For the premium calculation of an XL treaty with retention  $M$ , under the assumption of independence between the number and the sizes of the claims as well as identically distributed claim sizes, often the reduction effect

$$r(M) := \frac{E(D(t))}{E(X(t))} = \frac{1}{E(X)} \int_0^M (1 - F(w)) \, \mathrm{d}w \tag{8}$$

is used, which turns out to be the equilibrium *distribution function* of the distribution function  $F$  of an individual claim  $X$ . In practice, one distinguishes between *exposure rating*, where the reinsurer uses the portfolio and premium information of the first-line insurer, and *experience rating*, which is mainly based on the previous claim experience of the XL layer itself. Especially, the latter method often faces the challenge of having only a few data points available, in which case credibility estimates (see Credibility **Theory**) may be used. Another important aspect in XL treaties is potential claims inflation, which may be substantial (as the time until settlement of a claim may be large) and would often just affect the reinsurer. Hence, typically some *index clause* is arranged, which splits the amount of claims inflation between the first-line insurer and the reinsurer.

For SL treaties, the aggregate claim distribution (see Accumulated Claims) of the first-line insurance portfolio will be the crucial quantity to determine suitable reinsurance premiums, using, for instance, generalized stop-loss transforms to determine moments of the reinsured claim amount (for numerical and algorithmic issues, see [20]).

Premium calculations for large-claim reinsurance contracts are more involved, but several asymptotic results using extreme value theory are available (see [4] for a survey). Note that for all these treaties it is also important to adequately assess the possible dependence among the risks, as this may drastically influence the appropriate premium (see, for instance, [12]).

In addition to the resulting actuarial premium, the actual reinsurance premium will also be influenced by other factors like competition, volume of the portfolio, and perhaps a loading that accounts for potential moral hazard and adverse selection. Here moral hazard refers to the tendency of the reinsured not to be as strict in the claim settlement process as without reinsurance (see, e.g., [13]), whereas adverse selection accounts for the asymmetry of information of the cedant and the reinsurer on the underlying risk in general (see [19]). Also, for contracts like the XL treaty, the reinsurer typically has no insight into the number and sizes of the claims below the retention and needs to get information from other sources, which also increases the costs (see, e.g., [17, 18]). General considerations on planning in reinsurance can be found in  $[26]$ .

Robustness questions of reinsurance premiums are discussed in Brazauskas [8]. In addition, the economic environment influences the pricing of reinsurance risks (see  $[1, 2]$ ).

# **Choice of Reinsurance**

Each reinsurance form has its particular advantages and disadvantages in terms of the type of protection it provides (frequency risk, large-claim risk), premium calculation, practical handling, administration and processing of loss estimation (including issues like moral hazard and adverse selection). An insurer may have a concrete objective such as to maximize expected profit after reinsurance (subject to a certain security level condition) or to minimize the probability of ruin after reinsurance (see **Ruin Theory**). There are a number of theoretical results available which under specific assumptions on the underlying premium principle identify the optimal reinsurance form with respect to given maximization criteria and constraints (see [4] for an overview). A natural and close connection between such optimality questions and utility theory (see **Utility Function**) is, for example, discussed by Borch [7] and Bühlmann and Jewell [9]. For instance, under an expected value premium principle of the reinsurer and a given reinsurance premium, an SL contract maximizes the expected utility of terminal wealth for any risk-averse utility function (a result attributed to K. Arrow, see Arrow, **Kenneth**). As a consequence, in this setting an SL contract also minimizes the retained variance  $Var(D)$ of the first-line insurer. On the other hand, under a variance or standard deviation premium principle and a fixed value of  $Var(R)$ , a QS contract minimizes  $Var(D)$  [5, 23]. Already these two examples illustrate that the selected reinsurance premium principle plays a decisive rule for the optimal decision. Also, the optimality results usually heavily depend on the type and amount of transaction costs involved. In recent years many refinements of such optimality results have been developed (see [4, 21] for a general survey on this topic). For a dual approach in the framework of solvency in finance and insurance, see [29]. In the collective model, it is also quite common to look for reinsurance strategies that minimize the Lundberg adjustment coefficient (*see* **Cramer–Lundberg ´ Estimates**; [15] and [10]). An overview on optimal dynamic reinsurance strategies to minimize the probability of ruin can be found in [24] (*see* **Ruin Theory** and **Stochastic Control in Insurance**). For other optimization criteria, see [30].

In practice, the concrete form and amount of reinsurance choice for a certain portfolio often also will be influenced by experience, availability of reinsurance offers, and current market prices.

# **Reinsurance and Finance**

The financial component in any insurance and reinsurance activity has become more important over the last years, not the least due to higher interest rates, longer time horizons for claim settlement, and the general need to combine the analysis and management of assets and liabilities (see, e.g., [28]). Financial pricing of reinsurance contracts in various contexts is discussed in [11] (*see* **Insurance Derivatives**), and note that a (re)insurance market is incomplete, (*see* **Complete Markets**). Since reinsurance is a global business, foreign exchange risk (*see* **Foreign Exchange Markets**) also has to be considered (cf. [6]).

Nowadays, classical reinsurance is often complemented by other mechanisms to cope with risk (summarized under the name *alternative risk transfer*) that have a certain financial flavor such as *captives, finite risk reinsurance, multi-trigger products*, and *contingent capital* (cf. [22]). Further bridging the gap between insurance and finance, insurance companies also started to transfer some of their risk directly to the capital market (*see* **Securitization**). This includes *reinsurance sidecars*, where investors act like a QS reinsurer, as well as the issuance of catastrophe bonds (*see* **Catastrophe Bonds**). Recently, some structured insurance-linked products such as *catastrophe* collateralized debt obligations (CDOs) (*see* **Collateralized Debt Obligations (CDO)**) have also been issued in the financial market, which sometimes receive quite competitive credit ratings for their tranches . At the same time, some of the traded catastrophe CDOs offer loss coverage that can be significantly cheaper than in classical reinsurance contracts.

# **References**

- [1] Aase, K.K. (1993). Equilibrium in a reinsurance syndicate: existence, uniqueness and characterization, *ASTIN Bulletin* **23**, 185–211.
- [2] Aase, K.K. (1993). Premiums in a dynamic model of a reinsurance market, *Scandinavian Actuarial Journal* (2), 134–160.
- [3] Aase, K.K. (2002). Perspectives of risk sharing, *Scandinavian Actuarial Journal* (2), 73–128.
- [4] Albrecher, H. & Teugels, J. (2009). *Reinsurance: Actuarial and Financial Aspects*, John Wiley & Sons, Chichester. To appear.
- [5] Beard, R., Pentikainen, T. & Pesonen, E. (1984). ¨ *Risk Theory*, Chapman & Hall, London.
- [6] Blum, P., Dacorogna, M., Embrechts, P., Neghaiwi, P. & Niggli, H. (2001). Using DFA for modelling the impact of foreign exchange risk on reinsurance decisions, *CAS Forum* Summer, 49–94.
- [7] Borch, K. (1961). The utility concept applied to the theory of insurance, *Astin Bulletin* **1**, 245–255.
- [8] Brazauskas, V. (2003). Influence functions of empirical nonparametric estimators of net reinsurance premiums, *Insurance, Mathematics and Economics* **32**(1), 115–133.
- [9] Buhlmann, H. & Jewell, W. (1979). Optimal risk ¨ exchanges, *Astin Bulletin* **10**, 243–262.
- [10] Centeno, M. (2002). Measuring the effects of reinsurance by the adjustment coefficient in the Sparre Anderson model, *Insurance, Mathematics and Economics* **30**(1), 37–49.
- [11] De Waegenaere, A. (1994). Equilibria in a mixed financial-reinsurance market with constrained trading possibilities, *Insurance, Mathematics and Economics* **14**(3), 205–218.
- [12] Denuit, M., Dhaene, J., Goovaerts, M. & Kaas, R. (2005). *Actuarial Theory for Dependent Risks*, Wiley, Chichester.
- [13] Doherty, N. & Smetters, K. (2006). Moral hazard in reinsurance markets, *Journal of Risk and Insurance* **72**(3), 375–391.
- [14] Embrechts, P., Kluppelberg, C. & Mikosch, T. (1997). ¨ *Modelling Extremal Events*, Springer, New York, Berlin, Heidelberg, Tokyo.
- [15] Gerber, H. (1979). *An Introduction to Mathematical Risk Theory*. Huebner Foundation Monograph 8, Huebner Foundation, Homewood, Ill.
- [16] Gerber, H. (1980). Principles of premium calculation and reinsurance, *Transactions of the 21th International Congress of Actuaries* **I**, 137–142.

- [17] Hurlimann, W. (1994). A note on experience rating, ¨ reinsurance and premium principles, *Insurance, Mathematics and Economics* **14**(3), 197–204.
- [18] Hurlimann, W. (1995). Links between premium princi- ¨ ples and reinsurance, *Transactions of the 25th International Congress of Actuaries*, Brussels, pp. 141–168.
- [19] Jean-Baptiste, E. & Santomero, A. (2000). The design of private reinsurance contracts, *Journal of Financial Intermediation* **9**, 274–297.
- [20] Kaas, R. (1993). How to (and how not to) compute stoploss premiums in practice, *Insurance, Mathematics and Economics* **13**(3), 241–254.
- [21] Mack, T. (1996). *Schadensversicherungsmathematik*. Verlag Versicherungswirtschaft E.V., Karlsruhe.
- [22] Neuhaus, W. (2004). Alternative risk transfer, in *Encyclopedia of Actuarial Science*, J. Teugels & B. Sundt, eds John Wiley & Sons, Ltd., Chichester, Chapter.
- [23] Pesonen, M.I. (1984). Optimal reinsurances, *Scandinavian Actuarial Journal* (2), 65–90.
- [24] Schmidli, H. (2008). *Stochastic Control in Insurance*, Springer-Verlag London Ltd., London.

- [25] Schnieper, R. (1990). Insurance premiums, the insurance market and the need for reinsurance, *Schweizerische Vereinigung der Versicherungsmathematiker Mitteilungen* **1990**(1), 129–147.
- [26] Straub, E. (1984). Actuarial remarks on planning and controlling in reinsurance, *Astin Bulletin* **14**, 183–191.
- [27] Thepaut, A. (1950). Une nouvelle forme de r ´ eassurance. ´ le traite d'exc ´ edent du co ´ ut moyen relatif (ECOMOR), ˆ *Bulletin Trimestriel de l'Institut des Actuaires Francais* **49**, 273.
- [28] Wuthrich, M.V., B ¨ uhlmann, H., and Furrer, H. (2008). ¨ *Market-consistent Actuarial Valuation*, EAA Lecture Notes, Springer, Berlin.
- [29] Yaari, M. (1987). The dual theory of choice under risk, *Econometrica* **55**, 95–115.
- [30] Young, V.R. (1999). Optimal insurance under Wang's premium principle, *Insurance, Mathematics and Economics* **25**(2), 109–122.

HANSJORG ¨ ALBRECHER
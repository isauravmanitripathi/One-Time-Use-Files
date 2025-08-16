# **Collateralized Debt Obligation (CDO) Options**

The synthetic collateralized debt obligation (CDO) tranche activity is still a relatively new business, which started in late 2000. Initially seen as an eccentricity in the securitization market, it finally got a life on its own. Contrary to the rest of the securitization market, it grew as an arbitrage business, where the bank will not gain from structuring fees (like for cash CDOs) but from an arbitrage between two different markets: single-name credit default swaps versus synthetic single-tranche CDO. Its evolution was then marked by multiple borrowings from equity derivatives market, using its terminology (single tranche viewed as call spread on credit losses) and its technology (correlation smiles and the type of derivatives on it). This helps explain why the article focuses exclusively on synthetic CDO tranches, because to our knowledge there do not exist derivatives based on cash CDO notes.<sup>a</sup>

For a more comprehensive CDO framework, see Collateralized Debt Obligations (CDO), and for an introduction to CDO tranche pricing, see Intensitybased Credit Risk Models. However, we introduce those two important notions that are used in this article:

- A credit default swap (CDS) is a bilateral contract where the protection buyer will pay a quarterly premium (expressed as a proportion of the CDS notional) and receive from the protection seller, if specific events took place (related to the default or bankruptcy of a specific corporate entity), a payment corresponding to one minus the price of a bond of the defaulted entity, that payment being called the severity of default or the credit loss.
- A synthetic CDO tranche is a bilateral contract where the protection buyer will pay a quarterly premium (the premium leg of the swap) and receive from the protection seller the increment in loss on the tranche (the loss leg of the swap), where the loss on the tranche is contractually defined as a function of the sum of credit losses on a portfolio of single-names CDS, or more accurately as min  $(d - a, \max(L_t - a))$  with the following:

- $L_t$  represents cumulative credit losses on that portfolio up to date  $t$ , that is, the sum of different severities of defaulted entities that are in that portfolio:
- $a$  is defined as the attachment point of the CDO tranche in proportion of the initial pool size: and
- d is defined as its detachment point.

# Definitions

Here, we list the different derivatives that we have seen in the synthetic CDO markets created between 2001 and 2007. Those derivatives can be categorized in two groups: derivatives on CDO tranches where the behavior of the derivative is conditioned by losses realization, or default-path-dependent derivatives, and derivatives conditioned by a spread/market value evolution. Some derivatives like leveraged supersenior (LSS) (see Leveraged Super-senior **Tranche**) can be in the two categories depending on their variations.

The first category of default-path-dependent structure is also known as *reset tranches* (as defined in [4]): those are CDO tranches where the attachment point and/or the width of the tranche are modified at a future reset date as a predetermined function of the portfolio losses up to that date.

- Forward-starting CDO (see Forward-starting . CDO Tranche and [2]): this is a CDO tranche where the contract becomes effective at a future date, where any entities defaulting between the entry into the forward and its effective date will be considered to have a recovery rate at 100%, or in other words at the effective date, the CDO tranche will have an attachment point equal to the sum of the cumulative losses up to that date  $t_1$  and the pre-fixed initial attachment point (i.e.,  $a + L_{t_1}$ ), its width being unchanged in dollar amount (i.e.,  $d-a$ ). There is also a variation on that contract [7] where the forward CDO is the obligation to enter into a CDO tranche at a future date, taking into consideration the erosion of subordination due to losses up to the effective date, and the decrease in the width, but not the losses on the tranche, thus a subordination of max  $(0; a - L_{t_1})$ and width of min  $(d; \max(a; L_{t_1}))$ .
- Subordination step-up: This is a standard CDO . tranche except that at the reset date, if losses have

not started to touch the tranche the subordination will be increased by a fixed amount. Multiple variations of those contracts exist with several reset dates or increase in subordination linked to losses being in a specific band.

• *Leveraged supersenior* (*see* **Leveraged Supersenior Tranche**): This is a synthetic CDO tranche, with a large attachment point, thus its supersenior nature, which is initially partially collateralized by the protection seller. Owing to that partial collateralization, when a loss trigger or mark-to-market (MtM) trigger is breached, the protection seller has the obligation of either providing additional collateralization or unwinding its contract at market value. When the trigger is based on loss level, this can be viewed as a reset tranche.

The second category encompasses all derivatives in the classical sense, that is, derivatives based on the market value of the underlying asset.

- *Call on CDO tranches*: This is an option giving the option holder the possibility to buy protection on a synthetic CDO tranche at a predetermined spread on one of several future dates, being either European for one single date or Bermudan for a set of future dates. The strike is defined as a spread level (and not as a value of the tranche). The synthetic CDO tranche, that is, portfolio composition, attachment/detachment points, and maturity, is defined initially, and akin to the differentiation done on forward-starting CDO, losses up to the exercise date of the option may or may not affect the attachment point.
- *Put on CDO tranches*: Contrary to the call option, this gives the option holder the possibility to sell protection on a CDO tranche at a predetermined spread.
- *Callable structure*: This is an option that gives the protection seller (or the protection buyer) the right to terminate the transaction at no additional costs during its life. If the option is for the protection seller, this is, in fact, a Bermudan call on the CDO tranche itself with a strike equal to its initial spread level. Here the attachment point of the underlying synthetic CDO tranche will be eroded by losses up to the exercise date of the option.
- *Rating guarantee*: We know of one investment bank that worked on the possibility to issue a guarantee on the CDO tranche rating, giving the

option to investors to put their CDO tranche at par to the issuer of such guarantee if the rating was downgraded below a prespecified threshold. This is in effect a callable structure conditional on the tranche being downgraded by a rating agency.

# **Purpose and Market**

The purpose of those innovations is, in most cases, related to issues encountered by the bank's desk working on synthetic CDO tranches. The innovations in that market were always caused not by a need of the investors but by potential arbitrages to exploit. Synthetic CDO tranche from 2001 to 2007 was a booming market with several success stories. However, this was a very competitive market, where the competitive advantage was due to the endless creation of new structural features. Indeed, as soon as an innovation was introduced to the market by one player, several others tried to imitate it, soon depleting the potential gains evidenced by such innovation (Figure 1).

Each innovation was triggered by either an arbitrage to exploit or a specific problem encountered by the desk:

- *Forward-starting CDO*: Those products were created to exploit discrepancies between the terms structure of spread as the five-year maturity spread was depleted because of the wave of five-year synthetic CDO tranches. Synthetic CDO tranches were starting to be structured at 10 years or even as forward starting 5–10 years to benefit from the tightening at 5 years. Indeed, a 5–10 years forward starting CDO can be seen as a combination of a 10 years synthetic tranche and a 5 years synthetic tranche, selling protection for 10 years but buying protection for the first 5 years.
- *Leveraged supersenior*: When the correlation desk sold synthetic CDO tranches, they sold mainly equity and mezzanine tranches, and thus either delta-hedged them or kept the most senior tranches on their book. The supersenior exposures were very hard to sell due to their low spreads compared to their notional amounts, that is, the amount of cash needed to invest in those tranches. The creation of LSS allowed those desks to buy protection on supersenior synthetic CDO tranches by broadening the investor base outside of its

![](_page_2_Figure_1.jpeg)

**Figure 1** Evolution of the notional of the credit derivatives market with several innovations

initial clients (monolines or (re)insurance companies), the LSS having a higher spread for an "assumed" low credit risk.

#### Valuation

The valuation of a CDO tranche, whether initially or during its life, relies on the knowledge of the loss distribution of the underlying portfolio through time or, in other words on the law governing the random path  $L_t$  representing the cumulative losses up to  $t$ . The knowledge of the loss distribution at different future date (thus a loss distribution surface) is required<sup> $b$ </sup> to price a CDO tranche, that is, to value the two legs of that tranche swap:  $P[L_T \leq l | \mathcal{F}_t]$ the probability that losses up to time  $T$  will exceed threshold  $l$  knowing the losses at time  $t$ .<sup>c</sup> If the existing information in the market consists of the credit index tranches prices, in the arbitrage pricing theory framework, from those prices we will extract constraints on the "spot" loss distribution surface being  $P \mid L_T \leq l \mid \mathcal{F}_{t_0}$ .

Some CDO derivatives can be valued with that "spot" loss distribution surface: the forward-starting CDO as described in [7] (the second variation as described above) can be understood as a long-short position on maturities: long, the CDO tranche at the longest maturity and short, the same CDO tranche at the effective date. Indeed, on comparing the two positions—a  $t_1/t_2$  forward-starting CDO tranche *versus* a long CDO tranche at  $t_2$  and a short CDO tranche at  $t_1$  with the same attachment/detachment points:

- . if losses are always below the attachment point, no CDO tranches will be touched;
- if  $L_{t_1} < a$  and  $L_{t_2} > a$ , the forward-starting CDO  $\bullet$ will lose min  $(d - a, L_{t_2} - a)$  and the long CDO tranche will lose the same amount; and
- if  $L_{t_1} > a$  and  $L_{t_2} > a$ , the forward-starting  $\bullet$ CDO will lose min $(d - L_{t_1}, L_{t_2} - L_{t_1})$  and the long-short CDO tranches will lose/gain  $\min(d-a, L_{t_2}-a)/\min(d-a, L_{t_1}-a)$ , which gives the same aggregate amount.<sup>d</sup>

However, to value the other reset tranches, we need an additional information: the intertemporal dependence of losses, that is, the dependence between losses at different dates. For a forward-starting CDO—first variation—we need the law of  $(L_{t_1}, L_{t_2})$ to be able to price it.

In addition, for options on tranche, dependent on future spreads, the knowledge of the "spot" loss distribution surface is not sufficient to value those options. An additional assumption related to spread volatility is needed: this can be an *ad hoc* assumption directly on the volatility [7] or can be embedded into a stochastic deformation of the loss distribution surface  $P[L_T \leq l | \mathcal{F}_t]$  through time. This leads researchers to introduce the class of models known as a dynamic losses model. The dynamic losses model defined so far relies on the standard CDO models. which are classified according to two broad categories [8]:

- Top-down models: The top-down approach will only look at the evolution of the losses on the portfolio and model its dynamics. The seminal paper describing a general framework for such dynamic of the "forward" loss distribution surface is [11], where the distribution of losses in the portfolio is represented as a Markov chain with stochastic transition rates. Andersen et al. [3] explore the same road in a less general manner. Those approaches are tractable, flexible but they do not capture information from the single-names CDS market.
- Bottom-up models: The approach starts with a representation of the credit risk of the underlying single names in order to build a loss distribution surface. Starting from the modeling of individual defaults, they use classical credit modeling:
  - Structural models (see Default Barrier **Models**): A structural model computes the default as the breaching by a random process of a barrier (in the initial Merton seminal article the first represents the assets of a company and the second its indebtness). That class of model incorporates a dynamic for the probabilities of losses naturally, introducing default dependencies through the random process, with linear combination of random process (Brownian motion or Gamma process, see [9]). A related class of models looks at a discrete evolution of creditworthiness, generally with a Markov chain, where the use of stochastic transition rates can also be applied (a related example is in  $[1]$ ).
  - Reduced-form models (see Intensity-based Credit Risk Models): A reduced-form model uses hazard rates to represent the risk of

default of individual companies; a portfolio can be analyzed with correlated hazard rates. A natural extension of those models to address dynamic losses is to use stochastic hazard rate for each company, which may be linked through common jumps (as first introduced by Duffie and Gârleanu [5]), correlated Brownian motion, or even introduction of stochastic time process mapping calendar time to business time  $[10]$ .

Following the financial crisis of 2008, the landscape for synthetic CDO tranches has seen a change in paradigm. The default of Lehman Brothers in September 2008 and the demise of the investment bank business model have exposed the shaky foundations of the CDO market: liquidity drying in stress period and lack of acknowledgment of the counterparty risk in the CDS market. However, the initiatives that are currently discussed (standardization of that market, central clearing house) will, on the long term, expand the scope of that market and ultimately be beneficial for the development of those instruments.

### **End Notes**

<sup>a.</sup> Apart from rare guarantees offered by structuring desks or call optionality for the equity tranche of cash CDOs. <sup>b</sup>.In reality as pointed out in [6], the knowledge of the expected loss on the CDO tranche is sufficient to price it. <sup>c.</sup>The filtration  $\mathcal{F}_t$  may embed more information than the cumulative losses up to that time.

<sup>d.</sup>Taking into account even the timing of payment of losses, the two positions are the same.

#### References

- [1] Albanese, C., Chen, O., Dalessandro, A. & Vidler, A. (2005). *Dynamic Credit Correlation Modeling*, Working Paper, Imperial College.
- [2] Andersen, L. (2006). Portfolio Losses in Factor Models: Term Structures and Intertemporal Loss Dependence.
- Andersen, L., Piterbarg, V. & Sidenius, J. (2005). [3] A New Framework for Dynamic Credit Portfolio Loss Modelling. Working Paper, November.
- Baheti, P., Mashal, R. & Naldi, M. (2006). Step it Up [4] or Start it Forward: Fast Pricing of Reset Tranches, Lehman Brothers Quantitative Credit Research, Vol. 2006-Q1.
- [5] Duffie, D. & Gârleanu, N. (2001). Risk and the valuation of collateralized debt obligations, Financial Analysts Journal 57, 41-59.

- [6] Hull, J. & White, A. (2006). Valuing credit derivatives using an implied copula approach, *Journal of Derivatives* **14**, 8–28.
- [7] Hull, J. & White, A. (2007). Forward and European options on CDO tranches, *Journal of Credit Risk* **3**, 63–73.
- [8] Hull, J. & White, A. (2008). Dynamic models of portfolio credit risk: a simplified approach, *Journal of Derivatives* **15**, 9–28.
- [9] Jackel, P. (2008). ¨ *The Discrete Gamma Pool Model*. Working Paper, August.
- [10] Joshi, M. & Stacey, A. (2006). Intensity Gamma, *Risk* **19**, 78–83.
- [11] Schonbucher, P.J. (2006). *Portfolio Losses and the Term Structure of Loss Transition Rates: A New Methodology*

*for the Pricing of Portfolio Credit Derivatives*. Working Paper, ETZH.

# **Related Articles**

**Collateralized Debt Obligations (CDO)**; **Default Barrier Models**; **Forward-starting CDO Tranche**; **Intensity-based Credit Risk Models**; **Leveraged Super-senior Tranche**.

OLIVIER TOUTAIN
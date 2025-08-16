# **CDO Square**

A CDO-of-CDO, or CDO square (CDO2), is a type of collateralized debt obligation (CDO) that has CDO tranches as reference assets. The CDO2 market is a natural extension of the CDO market. The concept of CDO<sup>2</sup> was pioneered by the ZAIS group, when they launched ZING I in 1999, focusing on Euro CDO assets [2]. Recognizable growth of the CDO<sup>2</sup> market, particularly in the United States, was fueled by the excessive volume growth of the CDO market in the new millennium. In 2004, the situation of tightening credit spreads and a stable credit outlook shifted investor and dealer interest toward more structured credit basket products in the search for yield and tailored risk-return profiles. The repackaging of CDO tranches *via* the CDO<sup>2</sup> technology allows the dealer to manage the risk and capital cost of (residual) trading book positions. As in the case of CDOs, the dealer can exploit the rating alchemy, that is, the difference between traded and historical default probabilities as well as default correlations, to generate positive carry strategies. The investor will benefit from a more diversified reference portfolio, generally higher yield than similarly rated corporate debt, and the double-layer subordination effect.

We distinguish three main CDO2 transaction types: cash CDO2, synthetic CDO2, and hybrid CDO2. All transaction types can either refer to a static portfolio of CDOs or can be combined with an active management of the reference CDO portfolio. In a cash or cash-flow CDO2, the reference assets are existing cash CDOs, which typically provide the funds to pay CDO<sup>2</sup> investors. In a synthetic CDO2, the credit risk is generated synthetically, for example, *via* unfunded CDO tranche swaps. Hybrid CDO2s appeared with the rise of the structured finance CDO market and comprise both elements. Typically, in such transactions, the major portion (ca. 80–90%) of the reference portfolio is cash asset-backed security (ABS) exposure and the remainder is synthetic CDOs. It is quite common to use a special purpose vehicle (SPV) overlay for cash CDO<sup>2</sup> and hybrid CDO2.

## **Mechanics of a Synthetic CDO2**

A synthetic CDO<sup>2</sup> tranche follows the same mechanics as an ordinary CDO tranche (*see* **Collateralized Debt Obligations (CDO)**), with the only difference that its reference portfolio is made up of CDO tranches. This portfolio is called the *outer or master portfolio*. CDO tranches are determined by their corresponding reference portfolio plus an attachment (or subordination) level and detachment (or exhaustion) level with regard to aggregated credit losses. Hence, we refer to the loss attachment and detachment of the outer portfolio as *outer attachment* and *outer detachment*. Similarly, each CDO tranche of the outer portfolio is described by a corresponding inner reference portfolio and an inner attachment and detachment level (compare with Figure 1 for a schematic description). The inner reference portfolios often overlap and include some of the same reference assets.

Inner attachment and detachment levels as well as the reference notional of assets in inner portfolios are quite often of comparable size. Typically, we find ca. 50–150 assets per inner portfolio and ca. 5–10 inner CDO tranches, which generally translate into a total of ca. 250–500 different reference assets.

CDO<sup>2</sup> investors benefit from two layers of subordination. First, we must have a considerable number of default events with associated loss rates to exceed the subordination of at least one inner CDO tranche. This will trigger losses on the outer portfolio. However, only if the subordination of the outer CDO tranche is exhausted, we will recognize CDO<sup>2</sup> losses. The mathematical description of the aggregated CDO<sup>2</sup> loss *L*out*(t)* for any future date *t* during the contract term reflects the double-layer effect.

First, the inner portfolio losses *Lj (t)* have to be determined *via*

$$L_j(t) = \sum_{i=1}^{N} N_{ij} \cdot (1 - R_i) \cdot 1_{\{\tau_i \le t\}} \tag{1}$$

where *Nij* is the notional of assets *i* = 1*,...,N* in the inner reference portfolios *j* = 1*,...,M*, *Ri* denotes the asset-specific recovery rate and 1{*τi*≤*t*} is the (stochastic) default indicator function for the default time *τi* of reference asset *i*. Second, the inner portfolio losses *Lj (t)* have to be transformed into

![](_page_1_Figure_1.jpeg)

**Figure 1** Schematic  $\text{CDO}^2$  description

inner CDO tranche losses  $L_{\text{inn},j}(t)$  (see Collateralized Debt Obligations (CDO))

$$L_{\text{inn},j}(t) = \min[D_j - A_j, \max[L_j(t) - A_j, 0]]$$
(2)

where  $A_i$  and  $D_i$  denote the inner attachment and exhaustion level of the corresponding inner reference portfolio *j*. Third, the outer tranche or  $\text{CDO}^2$  tranche loss can be computed as

$$L_{\text{out}}(t) = \min \left[ D_{\text{out}} - A_{\text{out}}, \max \left[ L_{\text{tot}}(t) - A_{\text{out}}, 0 \right] \right]$$
(3)

where  $A_{\text{out}}$  and  $D_{\text{out}}$  denote the attachment and exhaustion points of the outer tranche and  $L_{\text{tot}}(t)$  =  $\sum_{i=1}^{M} L_{\text{inn},j}(t)$  the sum of inner tranche losses.

#### **Risk Analysis and Pricing**

The limited universe of liquid and actively traded reference assets naturally yields overlaps in inner reference portfolios; in other words, reference assets tend to occur in more than one real-life inner reference portfolio. This causes the  $\text{CDO}^2$  loss distribution to display fatter tails on both ends, since the

(non)occurrence of an isolated default event might simultaneously affect several inner reference portfolios, thereby displaying a leveraged effect [1]. This impact is even more pronounced in case of thin tranches and understood as cliff risk of CDO<sup>2</sup>s. Moreover, the double-layer tranche technology generally amplifies correlation sensitivities: an increase in the asset correlation yields a higher increase of correlation between affected inner CDO tranches. In summary, overlap and correlation are the main risk drivers of a  $\text{CDO}^2$  tranche. In addition, the described effects considerably increase the impact of other risk drivers such as changing credit spreads (respectively, changing default probabilities) and changing recovery rates.

The key ingredient to pricing is the stochastic evaluation of the accumulated CDO<sup>2</sup> tranche loss  $L_{\text{out}}(t)$  as determined in the previous paragraph. This requires the consistent use of a multivariate credit (default) model. Since no market standard has been developed yet owing to the lack of truly observable correlation information, the necessity and benefit of appropriate scenario models are highlighted in this article. The rating agencies Moody's, Standard & Poor's, and Fitch have consistently adapted their CDO rating technology to the CDO<sup>2</sup> case. In particular, the rating technology comes with a look-through capability to underlying assets of inner reference portfolios. However, the look-through capacity stops with ABS-type assets that are modeled as a single asset.

### **References**

- [1] Kakodkar, A., Galiani, S., Jonsson, J.G. & Gallo, A. (2006). *Credit Derivatives Handbook 2006—Vol. 2 A Guide to the Exotics Credit Derivatives Market, Credit Derivatives Strategy*, Merrill Lynch, New York.
- [2] Smith, D. (2003). CDOs of CDOs: art eating itself? in *Credit Derivatives: The Definite Guide*, J. Gregory, ed, Risk Books, London, pp. 257–279.

### **Related Articles**

#### **Collateralized Debt Obligations (CDO)**; **Managed CDO**; **Structured Finance Rating Methodologies**.

HANS-JURGEN ¨ BRASCH
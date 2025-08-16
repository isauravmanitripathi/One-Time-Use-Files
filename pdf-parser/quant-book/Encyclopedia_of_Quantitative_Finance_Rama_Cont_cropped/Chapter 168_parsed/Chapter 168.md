# **CreditRisk+**

CreditRisk+ is a portfolio credit risk model developed by the bank Credit Suisse, who published the methodology in 1997 [2].

A portfolio credit risk model is a means of estimating the statistical distribution of the aggregate loss from defaults in a portfolio of loans or other credit-risky instruments over a period of time. More generally, changes in credit quality other than default can be considered, but CreditRisk+ in its original form is focused only on default. The most widely used portfolio credit risk models are undoubtedly the so-called structural models, including models based on the Gaussian copula framework (*see* **Structural Default Risk Models**). CreditRisk+ performs its calculation in a different way to these models, but it is recognized that CreditRisk+ and Gaussian copula models have a similar conceptual basis. A detailed discussion can be found in [4, 7].

Financial institutions use portfolio credit risk models to estimate aggregate credit losses at high percentiles, corresponding to very bad outcomes (often known as the *tail* of the loss distribution). These estimates are then used in setting and allocating economic capital (*see* **Economic Capital**) and determining portfolio performance measures such as riskadjusted return on capital (*see* **Risk-adjusted Return on Capital (RAROC)**).

Portfolio credit risk models have two elements. The first is a set of statistical assumptions about the effect of economic influences on the likelihood of individual borrowers defaulting, and about how much the individual losses might be when they default. The second element is an algorithm for calculating the resulting loss distribution under these assumptions for a specific portfolio. Unlike most portfolio credit risk models, CreditRisk+ calculates the loss distribution using a numerical technique that avoids Monte Carlo simulation. The other distinction of CreditRisk+ is that it was presented as a methodology rather than as a software implementation. Practitioners and institutions have developed their own implementations, leading to a number of significant variants and improvements of the original model. The model has also been used by regulators and central banks: CreditRisk+ played a role in the early formulation of the Basel accord (see [5]) and has been used by central banks to analyze countrywide panel data on defaults (an example is reported in [1]).

For these reasons, since its introduction in 1997, CreditRisk+ has consistently attracted the interest of practitioners, financial regulators, and academics, who have generated a significant body of literature on the model. An account of CreditRisk+ and its subsequent developments can be found in [6].

## **The CreditRisk+ Algorithm**

The function of CreditRisk+ is to transform data about the creditworthiness of individual borrowers into a portfolio-level assessment of risk. In most portfolio credit risk models, this step requires Monte Carlo simulation (*see* **Credit Portfolio Simulation**). However, CreditRisk+ avoids simulation by using an efficient numerical algorithm, as outlined below.

The approach confers advantages in terms of speed of computation and enhanced understanding of the drivers of the resulting distribution: many useful statistics, such as the moments of the loss distribution, are given by simple formulae in CreditRisk+, whose relationship to the risk management features of the situation is transparent. On the other hand, owing to its analytic nature, CreditRisk+ is a relatively inflexible portfolio model, and as such has tended to find application where transparency and ease of calculation are more important than flexible parameterization.

To understand the CreditRisk+ calculation, we consider a portfolio containing *N* loans, where we wish to assess the loss distribution over a one-year time horizon. (The model can be applied to bonds or derivatives counterparties, but the main features of the calculation are the same.) To run CreditRisk+, a number *R* of economic factors must be chosen. This can be the number of distinct economic influences on the portfolio that are considered to exist (say, the number of geographical regions or industries significantly represented in the portfolio), but it is often assumed in practice that *R* = 1*,* in which case the model is said to be in "one-factor" mode. CreditRisk+ with one factor gives an assessment of risk that ignores subtle industry or geographic diversification, but can capture the correct overall amount of economic and concentration risk present in the portfolio, and is sufficient for many purposes. In any event, typically  $R$  is much less than  $N$ , the number of loans, reflecting the fact that all the significant influences on the portfolio affect many borrowers at once.

For each loan *i*, where  $1 \le i \le N$ , the model needs the following input data:

- 1. Long-term average probability of default  $p_i$ : This is the probability that the obligor will default over the year, typically estimated from the credit rating (see **Credit Rating**).
- 2. Loss on default  $E_i$ : This is typically estimated as the loan notional less an estimated recovery amount (see **Recovery Rate**).
- 3. Economic factor loadings: These are given by  $\theta_{i,j}$ , for  $1 \leq j \leq R$ , where R is the number of factors introduced above.  $\theta_{i,j}$  must be nonnegative numbers satisfying  $\sum_{j=1}^{R} \theta_{i,j} = 1$  for each *i*.

The factor loadings  $\theta_{i,j}$  require some further explanation: they represent the sensitivity of the obligor  $i$  to each of the  $R$  economic factors assumed to influence the portfolio. In general, determining suitable values for  $\theta_{i,j}$  is one of the main difficulties of using CreditRisk+, and analogous difficulties exist for all portfolio models. Note, however, that if  $R$ is chosen to be 1 ("one-factor mode" as described above), then we must have  $\theta_{i,1} = 1$  for all i, and there is no information requirement. This reflects the fact that one-factor mode ignores the subtle industry or geographic diversification effects in the portfolio, but is, nevertheless, a popular mode of use of the model due to the simpler parameter requirements.

To understand how CreditRisk+ processes this data, let  $X_1, \ldots, X_R$  be random variables, each with mean  $E(X_i) = 1$ . The variable  $X_i$  represents the economic influence of sector  $j$  over the year. In common with most portfolio credit risk models, CreditRisk+ does not incorporate economic prediction. Instead, uncertainty about the economy is reflected by representing economic factors as random variables in this way.  $CreditRisk +$  then assumes that the realized probability of default  $P_i$  for loan *i* is given by the following critical relationship:

$$P_i = p_i(\theta_{i,1}X_1 + \ldots + \theta_{i,R}X_R) \tag{1}$$

The realized default probability  $P_i$  depends not only on the long-term average probability of default

 $p_i$  but also on the random variables  $X_1, \ldots, X_R$ . Note that because  $E(X_j) = 1$  and  $\sum_{i=1}^R \theta_{i,j} = 1$ , we have

$$E(P_i) = p_i(\theta_{i,1} + \ldots + \theta_{i,R}) = p_i$$
 (2)

so that the long-term average default probability (or equivalently, the average of the default probabilities across all states of the economy) is  $p_i$  as required. In a particular year, however,  $P_i$  will differ from its longterm average. If the borrower  $i$  is sensitive to a factor j, (i.e.,  $\theta_{i,j} > 0$ ), and if a large value is drawn for  $X_j$ , then this represents a poor economy with a negative impact on the obligor  $i$ , and we will tend to have  $P_i > p_i$ , meaning that the obligor i is more likely to default in this particular year than on average. Because the same will be true of other obligors  $i'$ with  $\theta_{i',i} > 0$ , the economic influence represented by factor  $j$  can affect a large number of obligors at once. This mechanism incorporates systematic risk, which affects many obligors at once and so cannot be diversified away. The same mechanism in various forms is present in all commonly used portfolio credit risk models.

Two technical assumptions are now made in CreditRisk+:

- 1. The random variables  $X_i$ ,  $1 \le j \le R$ , are independent, and each has a Gamma distribution with mean 1 and variance  $\beta_i$ .
- 2. For each loan  $i$ ,  $1 \le i \le N$ , the loss given default  $E_i$  is a positive integer.

The first assumption is made to facilitate the  $CreditRisk + numerical algorithm. In other credit risk$ models, notably the Gaussian copula models, the variables that play the role of the  $X_i$  are assumed to be normally distributed. Although these assumptions seem very different, in fact for many applications they have little effect on the final risk estimate. Assumption (1) can, however, lead to difficulties in parameterizing CreditRisk+.

The second assumption, known as *bucketing* of exposures, also requires some further explanation. Without this assumption,  $E_i$  could be any positive amounts, all expressed in units of a common reference currency. An insight of CreditRisk+ is that the precise values of  $E_i$  are not critical:  $E_i$  can be rounded to whole numbers without significantly affecting the aggregate risk assessment (a simple way of estimating the resulting error is given in Section A4.2 of  $[2]$ ). The amount of rounding depends on

how *Ei* are expressed before rounding; for example, it is common to express *Ei* in millions, so that a loss on default of say 24*.*35*,* meaning 24*.*35 million units of the reference currency, would be rounded to 25*.*

After bucketing of exposures, the aggregate loss from the portfolio must itself be a whole number (in the example above, this would mean a whole number of millions of the reference currency). The loss distribution can therefore be summarized in terms of its *probability generating function*

$$G(z) = \sum_{n=0}^{\infty} A_n z^n \tag{3}$$

where *An* denotes the probability that the aggregate loss is exactly *n.* To obtain the loss distribution, we need the numerical value of *An,* for *n* = 0 (corresponding to no loss), 1*,* 2*,...* up to a desired point. For CreditRisk+, with the inputs described above, it can be shown that the probability generating function (3) is given explicitly as

$$G(z) = \prod_{j=1}^{R} \left( 1 - \beta_j \left( \sum_{i=1}^{N} \theta_{i,j} p_i (z^{E_i} - 1) \right) \right)^{-1/\beta_j} \tag{4}$$

For the derivation of this equation, see, for example [2], Section A9 or [6], Chapter 2. The derivation involves a further approximation, known as the *Poisson approximation*, which can roughly be described as assuming that the default probabilities *pi* are small enough that their squares can be neglected. CreditRisk+ then uses an approach related to the socalled Panjer algorithm, which was developed originally for use in actuarial aggregate claim estimation. This relies on the fact that there exist polynomials *P (z)* and *Q(z),* whose coefficients can be computed explicitly from the input data *via* equation (4), and which satisfy

$$P(z)\frac{\mathrm{d}G(z)}{\mathrm{d}z} = Q(z)G(z) \tag{5}$$

Equating the coefficients of *z<sup>n</sup>* on each side of this identity, for each *n* ≥ 0*,* leads finally to a simple *recurrence relationship* between *An* in equation (3). The recurrence relationship expresses the value of *An* for each *n,* in terms of the earlier coefficients *A*0*,...,An*<sup>−</sup>1*.* The calculation is started by calculating *A*0*,* which is the probability of no loss, by setting *z* = 0 in equation (4) to give the explicit formula

$$A_0 = G(0) = \prod_{j=1}^R \left( 1 + \beta_j \left( \sum_{i=1}^N \theta_{i,j} p_i \right) \right)^{-1/\beta_j} \quad (6)$$

and the recurrence relation then allows efficient calculation of *An* up to any desired level. For a complete treatment of this algorithm, see, for example, [6], Chapter 2.

## **Later Developments of CreditRisk+**

Many enhancements to CreditRisk+ have been proposed by various authors (see the introduction to [6] for a discussion of some of the drawbacks of the original model). Developments have fallen into the following broad themes:

- 1. alternative calculation algorithms, such as saddlepoint approximation, Fourier inversion, and the method of Giese [3];
- 2. improved capital allocation methods, notably the method of Haaf and Tasche;
- 3. inclusion of additional risks, such as migration risk and uncertain recovery rates;
- 4. improved methods for determining inputs, particularly the economic factor loadings *θi,j* ;
- 5. application to novel situations such as default probability estimation [8]; and
- 6. asymptotic formulae, notably the application of the "granularity adjustment" [5].

The reader is also referred to [6] for details on many of these developments.

#### **References**

- [1] Balzarotti, V., Castro, C. & Powell, A. (2004). *Reforming Capital Requirements in Emerging Countries: Calibrating Basel II using Historical Argentine Credit Bureau Data and CreditRisk*+. Working Paper, Universidad Torcuato Di Tella, Centro de Investigacion en Finanzas. ´
- [2] Credit Suisse Financial Products (1997). *CreditRisk*<sup>+</sup>*, a Credit Risk Management Framework*, Credit Suisse Financial Products, London.
- [3] Giese, G. (2003). Enhancing CreditRisk+, *Risk* **16**(4), 73–77.
- [4] Gordy, M. (2000). A comparative anatomy of Credit Risk Models, *Journal of Banking and Finance* **24**, 119–149.

### **4 CreditRisk+**

- [5] Gordy, M. (2004). Granularity adjustment in portfolio Credit Risk Measurement, in *Risk Measures for the 21st Century*, G. Szego, ed., John Wiley & Sons, Heidelberg.
- [6] Grundlach M. & Lehrbass, F. (eds) (2004). *CreditRisk*+ *in the Banking Industry*, Springer Finance.
- [7] Koyluoglu, H.U. & Hickman, A. (1998). Reconcilable differences, *Risk* **11**(10), 56–62.
- [8] Wilde, T. & Jackson, L. (2006). Low default portfolios without simulation, *Risk* **19**(8), 60–63.

#### **Related Articles**

**Credit Risk**; **Gaussian Copula Model**; **Structural Default Risk Models**.

TOM WILDE
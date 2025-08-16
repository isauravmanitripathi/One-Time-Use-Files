# **Rating Transition** Matrices

Rating transition matrices play an important role in credit risk management both as a method for summarizing the empirical behavior of a rating system and as a tool for computing probabilities of rating migrations in, for example, a portfolio of risky loans. Analysis of statistical properties of rating transition matrices is intimately linked with Markov chains. Even if rating processes in general are not Markovian, statistical analysis of rating systems often focuses on assessing a particular deviation from Markovian behavior. Furthermore, the tractability of the Markovian setting can be preserved in some simple extensions.

## **Discrete-time Markov Chains**

Let the rating process  $\eta = (\eta_0, \eta_1, \ldots)$  be a discretetime stochastic process taking values in a finite state space  $\{1, \ldots, K\}$ . If the rating process is a Markov chain, the probability of making a particular transition between time t and time  $t + 1$  does not depend on the history before time  $t$ , and one-step transition probabilities of the form

$$p_{ij}(t; t+1) = Pr(\eta_{t+1} = j \mid \eta_t = i) \tag{1}$$

describes the evolution of the chain. If the one-step transition probabilities are independent of time, we call the chain time homogeneous and write

$$p_{ij} = Pr(\eta_{t+1} = j \mid \eta_t = i) \tag{2}$$

The one-period transition matrix of the chain is then given as

$$P = \begin{pmatrix} p_{11} & \cdots & p_{1K} \\ \vdots & & \vdots \\ p_{K1} & \cdots & p_{KK} \end{pmatrix} \tag{3}$$

where  $\sum_{j=1}^{K} p_{ij} = 1$  for all *i*.<br>Consider a sample of *N* firms whose transitions between different states are observed at discrete dates  $t = 0, \ldots, T$ . Now introduce the following notation:

 $n_i(t)$  = number of firms in state *i* at date *t*.

- $n_{ii}(t)$  = number of firms that went from *i* at . date  $t-1$  to j at date t.
- $N_i(t) = \sum_{t=0}^{T-1} n_i(t)$  = number of firm exposures recorded at the beginning of transition periods.
- $N_{ij}(T) = \sum_{t=1}^{T} n_{ij}(t)$  = total number of transi-٠ tions observed from  $i$  to  $j$  over the entire period.

If we do not assume time homogeneity, we can estimate each element of the one-step transition probability matrix using the maximum-likelihood estimator

$$\widehat{p_{ij}}(t-1;t) = \frac{n_{ij}(t)}{n_i(t-1)}$$
(4)

which simply is the fraction of firms that made the transition divided by the number of firms which could have made the transition.

Assuming time homogeneity, the maximumlikelihood estimator of the transition probabilities matrix is  $\sim 10^{-1}$ 

$$\widehat{p}_{ij} = \frac{N_{ij}(T)}{N_i(T)}\tag{5}$$

for all  $i, j \in K$ . This estimator is different from the estimator obtained by estimating a sequence of  $1$ -year transition matrices and then computing the average of each element at a time. The latter method will weigh years with few observations as heavily as years with many observations. If the viewpoint is that there is variation in 1-year transition probabilities over time due to, for example, business cycle fluctuations, the averaging can be justified as a way of obtaining an unconditional 1-year default probability over the cycle.

Rating agencies often form a cohort of firms at a particular date, say January 1, 1980, and record transition frequencies over a fixed time horizon, say 5 years. This can be done in a straightforward way using only information on the initial rating and final rating after 5 years, assuming that all companies that are in the cohort, to begin with, stay in the sample. In practice, rating withdrawals occur, that is, firms or debt issues cease to have a rating. According to [4], the vast majority of withdrawals are due to debt maturing, being redeemed or called. It is traditional in the rating literature to view these events as "noninformative" censoring. One way to deal with withdrawals is to eliminate the firms from the sample and in essence use only those firms that do not have their rating withdrawn in the 5-year period. Another way is to estimate a sequence of 1-year transition probability matrices using the 1-year estimator and then estimate the 5-year matrix as the product of 1-year matrices. In this case, information of a firm whose rating is withdrawn is used for the years where it is still present in the sample. Both methods rely on the assumption of withdrawals being noninformative.

## **Continuous-time Markov Chains**

When one has access to full rating histories and therefore knows the exact dates of transitions, the continuous-time formulation offers significant advantages in terms of tractability. Recall that the family of transition matrices for a time-homogeneous Markov chain in continuous time on a finite state space can be described by an associated generator matrix, that is, a  $K \times K$  matrix  $\Lambda$ , whose elements satisfy

$$\lambda_{ij} \ge 0 \text{ for } i \ne j$$
  
$$\lambda_{ii} = -\Sigma_{j \ne i} \lambda_{ij}$$
(6)

Let  $P(t)$  denote the  $K \times K$  matrix of transition probabilities, that is,  $p_{ij}(t) = P(\eta_t = j | \eta_0 = i)$ . Then

$$P(t) = \exp(\Lambda t) \tag{7}$$

where the right hand side is the matrix exponential of the matrix  $\Lambda t$  obtained by multiplying all entries of  $\Lambda$  by t.

In case a row consists of all zeros, the chain is absorbed in that state when it hits it. It is convenient to work with the default states as absorbing states even if firms in practice may recover and leave the default state. If we ask what the probability is that a firm will default before time  $T$  then this can be read from the transition matrix  $P(T)$  when we have defined default to be an absorbing state. If the state is not absorbing, but  $P$  allows the chain to jump back into the nondefault rating categories, then the transition probability matrix for time  $T$  will only give the probability of being in default  $at$  time  $T$  and this (smaller) probability is typically not the one we are interested in for risk management purposes.

Assume that we have observed a collection of firms between time  $0$  and time  $T$ . The maximumlikelihood estimator for the off-diagonal elements of the generator matrix is given by

$$\hat{\lambda}_{ij} = \frac{N_{ij}(T)}{\int_0^T Y_i(s) \, \mathrm{d}s} \tag{8}$$

where  $Y_i(s)$  is the number of firms in rating class i at time s and  $N_{ii}(T)$  is the total number of direct transitions over the period from i to j, where  $i \neq j$  $i$ . The denominator counts the number of "firmyears" spent in state  $i$ .

Any period a firm spends in a state will be picked up through the denominator. In this sense all information is being used. Note also how (noninformative) censoring is handled automatically: When a firm leaves the sample, it simply stops contributing to the denominator. Also, this method will produce estimates of transition probabilities for "rare transitions", even if the rare transitions have not been observed in the sample. For more on this, see [9].

#### Nonhomogeneous Chains

For statistical specifications and applications to pricing, the concept of a nonhomogeneous chain is useful. In complete analogy with the discrete-time case, the definition of the Markov property does not change when we drop the assumption of time homogeneity, but the description of the family of transition matrices requires that we keep track of calendar dates instead of just time lengths.

For each pair of states i, j with  $i \neq j$ , let  $A_{ij}$  be a nondecreasing right-continuous (and with left limits) function, which is zero at time zero. Let

$$A_{ii}(t) = -\sum_{j \neq i} A_{ij}(t) \tag{9}$$

and assume that

$$\Delta A_{ii}(t) \ge -1 \tag{10}$$

Then there exists a Markov process with state space  $1, \ldots, K$  whose transition matrix is given by

$$P(s,t) = \Pi_{[s,t]}(I + dA)$$
  

$$\equiv \lim_{\max|t_i - t_{i-1}| \to 0} \Pi_i(I + A(t_i) - A(t_{i-1}))$$
(11)

where  $s \le t_1 \le t_n \le t$ . One can think of the probabilistic behavior as follows: Given that the chain is in state  $i$  at time  $s$  the probability that it remains in that state at least until t (assuming that  $\Delta A_{ii}(u)$  >  $-1$  for  $u \le t$ ) is given by

$$P(\Delta \eta_u = 0 \text{ for } s < u \le t | \eta_s = i)$$
  
=  $\exp(-(A_{ii}(t) - A_{ii}(s)))$  (12)

We are interested in testing assumptions on the intensity measure when it can be represented through integrated intensities, that is, we assume that there exists integrable functions (or transition intensities)  $\lambda_{ii}(\cdot)$  such that

$$A_{ij}(t) = \int_0^t \lambda_{ij}(s) \, \mathrm{d}s \tag{13}$$

for every pair of states i, j with  $i \neq j$ .

In this case, given that the chain jumps away from *i* at date  $t$ , the probability that it jumps to state *j* is given by  $\frac{\lambda_{ij}(t)}{\sum_{k\neq i}\lambda_{iK}(t)}$ .

A homogeneous Markov chain with intensity matrix  $\Lambda$  has  $A_{ij}(t) = \lambda_{ij}t$  and in this special case we can write  $P(s, t) = \exp(\Lambda(t - s)).$ 

For a method for estimating the continuous-time transition probabilities nonparametrically using the so-called Aalen-Johansen estimator, see, for example, [2]. The specification of individual transition intensities allows us to use hazard regressions on specific rating transitions. For an example of nonparametric techniques, see [5]. A Cox regression approach can be found in [9].

#### **Empirical Observations**

There is a large literature on the statistical properties of the observed rating transitions, mainly for firms rated by Moody's and Standard and Poors. It has been acknowledged for a long time that the observed processes are not time homogeneous and not Markov. This is consistent with stated objectives of rating agencies of trying to avoid rating reversals and seeking to change ratings only when the change in credit quality is seen as enduring—a property sometimes referred to as "rating through the cycle". This is in contrast to "point-in-time" rating. The distinction between the two approaches is not rigorous, but a rough indication of the difference is that

a primary concern of through-the-cycle rating is the correct ranking of the firm's default probabilities (or expected loss) over a longer time horizon, whereas a point-in-time is more concerned with following actual, shorter-term default probabilities seeking to maintain a constant meaning of riskiness associated with each rating category.

The degree to which transition probabilities depend on the previous rating history, business cycle variables, and the sector or country to which the rated companies belong has been investigated, for example, in papers  $[1, 9, 10]$ . A good entry into the literature is in the special journal issue introduced by Cantor [3].

Rating agencies have a system of modifiers that effectively enlarge the state space. For example, Moody's operates with a watchlist and long-term outlooks. Being on a watchlist signals a high likelihood of rating action in a particular direction in the near future, and outlooks signal longer term likely rating directions. Hamilton and Cantor [7] investigate the performance of ratings when the state space is enlarged with these modifiers and conclude that they go a long way in reducing dependence on rating history.

## **Correlated Transitions**

In risk management, the risk of loan portfolios and exposures to different counterparties in derivatives contracts depends critically on the extent to which the credit ratings of different loans and counterparties are correlated.

We finish by briefly outlining two ways of incorporating dependence into rating migrations. For the first approach, see, for example, [6]; we map rating probabilities into thresholds. The idea is easily illustrated through an example. If firm 1 is currently rated  $i$  and we know the (say) 1-year transition probabilities  $p_{i1}, \ldots, p_{iK}$ , then we can model the transition to the various categories using a standard Gaussian random variable  $\epsilon_1$  and defining thresholds  $a_1 > a_2 > \ldots > a_{K-1}$  such that

$$p_{iK} = P(\epsilon_1 \le a_{K-1}) = \Phi(a_{K-1}) \qquad (14)$$

$$p_{i,K-1} = P(a_{K-1} \le \epsilon_1 \le a_{K-2})$$
  
=  $\Phi(a_{K-2}) - \Phi(a_{K-1})$  (15)

$$p_{i1} = P(a_1 < \epsilon_1) = 1 - \Phi(a_1) \tag{16}$$

Similarly, for firm 2, we can define thresholds *b*1*,...,bK*<sup>−</sup><sup>1</sup> and a standard random normal variable <sup>2</sup> so that the transition probabilities are matched as earlier. Letting <sup>1</sup> and <sup>2</sup> be correlated with correlation coefficient *ρ* induces correlation into the migration patterns of the two firms. This can be extended to a large collection of firms using a full correlation matrix obtained, for example, by looking at equity return correlations.

A second approach, which makes it possible to link up rating dynamics with continuous-time pricing models, is proposed in [8]. The idea here is to model the "conditional generator" of a Markov process as the product of a constant generator  and a strictly positive affine process *µ,* that is, conditionally on a realization of the process *µ,* the Markov chain is time non-homogeneous with the transition intensity *λij (s)* = *µ(s)λij .* This framework allows for closed form computation of transition probabilities in a setting where rating migrations are correlated through dependence on state variables.

# **References**

[1] Altman, E. & Kao, D.L. (1992). The implications of corporate bond rating drift, *Financial Analysts Journal* **48**(3), 64–75.

- [2] Andersen, P.K., Borgan, O., Gill, R. & Keiding, N. (1993). *Statistical Models Based on Counting Processes*, Springer, New York.
- [3] Cantor, R. (2004). An introduction to recent research on credit ratings, *Journal of Banking and Finance* **28**, 2565–2573.
- [4] Cantor, R. (2008). *Moody's Guidelines for the Withdrawal of Ratings*, Rating Methodology, Moody's Investors Service, New York.
- [5] Fledelius, P., Lando, D. & Nielsen, J. (2004). Nonparametric analysis of rating transition and default data, *Journal of Investment Management* **2**(2), 71–85.
- [6] Gupton, G., Finger, C. & Bhatia, M. (1997). *Credit-Metrics—Technical Document*, Morgan Guaranty Trust Company.
- [7] Hamilton, D. & Cantor, R. (2004). *Rating Transitions and Defaults Conditional on Watchlists, Outlook and Rating History*, Special comment, Moody's Investors Service, New York.
- [8] Lando, D. (1998). On Cox processes and credit risky securities, *Review of Derivatives Research* **2**, 99–120.
- [9] Lando, D. & Skødeberg, T. (2002). Analyzing rating transitions and rating drift with continuous observations, *The Journal of Banking and Finance* **26**, 423–444.
- [10] Nickell, P., Perraudin, W. & Varotto, S. (2000). Stability of ratings transitions, *Journal of Banking and Finance* **24**, 203–227.

DAVID LANDO
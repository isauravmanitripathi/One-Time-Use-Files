# **Complete Markets**

According to the arbitrage pricing of derivative securities, the arbitrage price of a financial derivative is defined as the wealth of a self-financing trading strategy based on traded primary assets, which replicates the terminal payoff at maturity (or, more generally, all cash flows) from the financial derivative. Hence, an important issue arises whether any financial derivative admits a replicating strategy in a given model; if this property holds, then the market model is said to be *complete*. Completeness of a market model ensures that any derivative security can be priced by arbitrage and hedged by a dynamic trading in primary traded assets. For example, in the framework of the Cox, Ross, and Rubinstein [9] model, not only the call and put options but also any pathindependent or path-dependent contingent claim can be replicated by a dynamic trading in stock and bond. Similarly, the classic Black and Scholes [3] model enjoys the property of completeness, although a suitable technical assumption needs to be imposed on the class of considered contingent claims.

Even for an incomplete model, the class of hedgeable derivatives, formally represented by attainable contingent claims, can be sufficiently large for practical purposes. Therefore, completeness should not be seen as a necessary requirement, as opposed to the no-arbitrage property, which is an indispensable feature of any financial model used for arbitrage pricing of derivative securities.

### **Finite Market Models**

The issue of completeness of a *finite* market model was analyzed, among others, by Taqqu and Willinger [24]. The finiteness of a market means that the underlying probability space is finite,  $\Omega = {\omega_1, \omega_2, \ldots, \omega_d}$ , and trading activities may only occur at the finite set of dates, denoted as  $\{0, 1, \ldots, T\}$ . As a standard example of a finite market model, one may quote, for instance, the Cox, Ingersoll, and Ross [9] binomial tree model (see **Binomial Tree**) or any its multinomial extensions.

Let  $S^1, S^2, \ldots, S^k$  be the stochastic processes describing the spot (or cash) prices of some nondividend paying financial assets. As customary, we postulate that the price process of at least one asset

is given as a strictly positive process, so that it can be selected as a *numéraire asset*. Let us then assume that  $S_t^k > 0$  for every  $t \leq T$ . To emphasize the special role of the process  $\overline{S^k}$ , we will sometimes write B instead of  $S^k$ . We assume that all assets are perfectly divisible and the market is frictionless, that is, there are no restrictions on the short-selling of assets, transaction costs, taxes, and so on.

We consider a probability space  $(\Omega, \mathcal{F}_T, \mathbb{P}),$ which is equipped with a filtration  $\mathbb{F} = (\mathcal{F}_t)_{t < T}$ . A probability measure  $\mathbb{P}$ , to be interpreted as the real-life probability, is an arbitrary probability measure on  $(\Omega, \mathcal{F}_T)$  such that  $\mathbb{P}(\omega_i) > 0$  for every  $i =$  $1, 2, \ldots, d$ . For convenience, we assume throughout that the  $\sigma$ -field  $\mathcal{F}_0$  is trivial, that is,  $\mathcal{F}_0 = \{\emptyset, \Omega\}$ . All processes considered in what follows are assumed to be  $\mathbb{F}$ -adapted.

## **Trading Strategies**

The component  $\phi^i_t$  of a trading strategy  $\phi =$  $(\phi^1,\phi^2,\ldots,\phi^k)$  represents the number of units of the  $i$ th security held by an investor at time  $t$ . In other words,  $\phi_t^i S_t^i$  is the amount of funds invested in the *i*th security at time *t*. Hence, the *wealth process*  $V(\phi)$ of a trading strategy  $\phi$  is given by the equality, for  $t = 0, 1, \ldots, T$ 

$$V_t(\phi) = \sum_{i=1}^k \phi_t^i S_t^i \tag{1}$$

The initial wealth  $V_0(\phi) = \phi_0 S_0$  is also referred to as the *initial cost* of  $\phi$ .

A trading strategy  $\phi$  is said to be *self-financing* whenever it satisfies the following condition, for every  $t = 0, 1, \ldots, T - 1,$ 

$$\sum_{i=1}^{k} \phi_{t}^{i} S_{t+1}^{i} = \sum_{i=1}^{k} \phi_{t+1}^{i} S_{t+1}^{i} \tag{2}$$

In the financial interpretation, this condition means that the portfolio  $\phi$  is revised at any date t in such a way that there are no infusions of external funds and no funds are withdrawn from the portfolio. We denote by  $\Phi$  the vector space of all self-financing trading strategies. The *gains process*  $G(\phi)$  of any trading strategy  $\phi$  equals, for  $t = 0, 1, \ldots, T$ ,

$$G_t(\phi) = \sum_{u=0}^{t-1} \sum_{i=1}^k \phi_u^i (S_{u+1}^i - S_u^i)$$
(3)

with  $G_0(\phi) = 0$ . It can be checked that a trading strategy  $\phi$  is self-financing if and only if the equality  $V_t(\phi) = V_0(\phi) + G_t(\phi)$  holds for every  $t =$  $0, 1, \ldots, T.$ 

#### **Replication and Arbitrage**

A European contingent claim  $X$  with maturity  $T$  is an arbitrary  $\mathcal{F}_T$ -measurable random variable. Since the space  $\Omega$  is assumed to be a finite set with d elements, any claim X has the representation  $X =$  $(X(\omega_1), X(\omega_2), \ldots, X(\omega_d)) \in \mathbb{R}^d$ . Hence, the class  $\mathcal{X}$  of all contingent claims that settle at  $T$  may be identified with the vector space  $\mathbb{R}^d$ .

A *replicating strategy* for the contingent claim  $X$ , which settles at time  $T$ , is a self-financing trading strategy  $\phi$  such that  $V_T(\phi) = X$ . For any claim X, we denote by  $\Phi_X$  the class of all replicating strategies for  $X$ .

The wealth process  $V(\phi)$  of an arbitrary strategy  $\phi$  from  $\Phi_X$  is called a *replicating process* of X in  $\mathcal{M}$ . Finally, we say that a claim X is *attainable* in  $\mathcal{M}$  if it admits at least one replicating strategy. We denote the class of all attainable claims by  $\mathcal{A}$ .

**Definition 1** A market model  $\mathcal{M}$  is said to be complete if every claim  $X \in \mathcal{X}$  is attainable in  $\mathcal{M}$ or, equivalently, if for every  $\mathcal{F}_T$ -measurable random variable  $X$  there exists at least one trading strategy  $\phi \in \Phi$  such that  $V_T(\phi) = X$ . In other words, a market model  $\mathcal{M}$  is complete whenever  $\mathcal{X} = \mathcal{A}$ .

Let  $X$  be an arbitrary attainable claim that settles at time T. We say that X is *uniquely replicated* in  $\mathcal{M}$ if it admits a unique replicating process in  $\mathcal{M}$ , that is, if the equality  $V_t(\phi) = V_t(\psi), t \in [0, T]$ , holds for arbitrary trading strategies  $\phi$ ,  $\psi$  from  $\Phi_X$ . Then the process  $V(\phi)$  is termed the *wealth process* of X in  $\mathcal{M}$ .

## Arbitrage Price

A trading strategy  $\phi \in \Phi$  is called an *arbitrage opportunity* if  $V_0(\phi) = 0$  and the terminal wealth of  $\phi$  satisfies

 $\mathbb{P}(V_T(\phi) \ge 0) = 1$  and  $\mathbb{P}(V_T(\phi) > 0) > 0 \tag{4}$ 

where  $\mathbb{P}$  is the real-world probability measure. We say that a market  $\mathcal{M} = (S, \Phi)$  is arbitrage free if there are no-arbitrage opportunities in the class  $\Phi$  of all self-financing trading strategies.

It can be shown that if the market model  $\mathcal{M}$  is arbitrage free, then any attainable contingent claim  $X$ is uniquely replicated in  $\mathcal{M}$ . The converse implication is not true, however, that is, the uniqueness of the wealth process of any attainable contingent claim does not imply the arbitrage-free property of a market, in general. Therefore, the existence and uniqueness of the wealth process associated with any attainable claim is insufficient to justify the term *arbitrage price.* Indeed, it is easy to give an example of a finite market in which all claims can be uniquely replicated, but there exists a strictly positive claim which can be replicated by a self-financing strategy with a negative initial cost.

**Definition 2** Let the market model  $\mathcal{M}$  be arbitrage free. Then the wealth process of an attainable claim  $X$  is called the arbitrage price of  $X$  in  $\mathcal{M}$  and it is denoted by  $\pi_t(X)$  for every  $t = 0, 1, \ldots, T$ .

## **Risk-neutral Valuation Formula**

Recall that we write  $S^k = B$ . Let us denote by  $S^*$  the process of *relative prices*, which equals, for every  $t = 0, 1, \ldots, T,$ 

$$S_t^* = (S_t^1 B_t^{-1}, S_t^2 B_t^{-1}, \dots, S_t^k B_t^{-1})$$
  
=  $(S_t^{*1}, S_t^{*2}, \dots, S_t^{*(k-1)}, 1)$  (5)

where we denote  $S^{*i} = S^i B^{-1}$ . Recall that the probability measures  $\mathbb{P}$  and  $\mathbb{Q}$  on  $(\Omega, \mathcal{F})$  are said to be *equivalent* if, for any event  $A \in \mathcal{F}$ , the equality  $\mathbb{P}(A) = 0$  holds if and only if  $\mathbb{Q}(A) = 0$ . Similarly,  $\mathbb{Q}$  is said to be *absolutely continuous* with respect to  $\mathbb{P}$  if, for any event  $A \in \mathcal{F}$ , the equality  $\mathbb{P}(A) = 0$ implies that  $\mathbb{Q}(A) = 0$ . Clearly, if the probability measures  $\mathbb{P}$  and  $\mathbb{Q}$  are equivalent, then they are also equivalent to each other. The following concept is crucial in the so-called risk-neutral valuation approach.

**Definition 3** A probability measure  $\mathbb{P}^*$  on  $(\Omega, \mathcal{F}_T)$ equivalent to  $\mathbb{P}$  (absolutely continuous with respect to  $\mathbb{P}$ , respectively) is called a equivalent martingale measure for  $S^*$  (*a* generalized martingale measure for  $S^*$ , respectively) if the relative price  $S^*$  is a  $\mathbb{P}^*$ martingale with respect to the filtration  $\mathbb{F}$ .

An  $\mathbb{F}$ -adapted, k-dimensional process  $S^* =$  $(S^{*1}, S^{*2}, \ldots, S^{*k})$  is a  $\mathbb{P}^*$ -martingale with respect to a filtration  $\mathbb{F}$  if the equality

$$\mathbb{E}_{\mathbb{P}^*}(S_{t+1}^{*i} \mid \mathcal{F}_t) = S_t^{*i} \tag{6}$$

holds for every i and  $t = 0, 1, \ldots, T - 1$ .

We denote by  $\mathcal{P}(S^*)$  and  $\mathcal{Q}(S^*)$  the class of all equivalent martingale measures for  $S^*$  and the class of all generalized martingale measures for  $S^*$ , respectively, so that the inclusion  $\mathcal{P}(S^*) \subset \mathcal{Q}(S^*)$ holds. It is not difficult to provide an example in which the class  $\mathcal{P}(S^*)$  is empty, whereas the class  $\mathcal{Q}(S^*)$  is not.

**Definition 4** A probability measure  $\mathbb{P}^*$  on  $(\Omega, \mathcal{F}_T)$ equivalent to  $\mathbb{P}$  (absolutely continuous with respect to  $\mathbb{P}$ , respectively) is called an equivalent martingale measure for  $\mathcal{M} = (S, \Phi)$  (*a* generalized martingale measure for  $\mathcal{M} = (S, \Phi)$ , respectively) if for every trading strategy  $\phi \in \Phi$  the relative wealth process  $V^*(\phi) = V(\phi)B^{-1}$  is a  $\mathbb{P}^*$ -martingale with respect to the filtration  $\mathbb{F}$ .

We write  $\mathcal{P}(\mathcal{M})$  ( $\mathcal{Q}(\mathcal{M})$ , respectively) to denote the class of all equivalent martingale measures (of all generalized martingale measures, respectively) for  $\mathcal{M}$ . For conciseness, an equivalent martingale measure (a generalized martingale measure, respectively) is abbreviated as EMM (GMM, respectively). Note that an equivalent martingale measure is sometimes referred to as a *risk-neutral probability*.

It can be shown that a trading strategy  $\phi$  is self-financing if and only if the relative wealth process  $V^*(\phi) = V(\phi)B^{-1}$  satisfies, for every  $t =$  $0, 1, \ldots, T$ 

$$V_t^*(\phi) = V_0^*(\phi) + \sum_{u=0}^{t-1} \sum_{i=1}^k \phi_u^i (S_{u+1}^{i*} - S_u^{i*}) \tag{7}$$

Therefore, for any  $\phi \in \Phi$  and any GMM  $\mathbb{P}^*$  the relative wealth  $V^*(\phi)$  is a  $\mathbb{P}^*$ -martingale with respect to the filtration  $\mathbb{F}$ . This leads to the following result.

**Lemma 1** A probability measure  $\mathbb{P}^*$  on  $(\Omega, \mathcal{F}_T)$  is a GMM for the market model  $\mathcal{M}$  if and only if it is a GMM for the relative price process  $S^*$ , that is,  $\mathcal{P}(S^*) = \mathcal{P}(\mathcal{M})$  and  $\mathcal{Q}(S^*) = \mathcal{Q}(\mathcal{M}).$ 

The next result shows that the existence of an EMM for  $\mathcal{M}$  is a sufficient condition for the no-arbitrage property of  $\mathcal{M}$ . Recall that trivially  $\mathcal{P}(\mathcal{M}) \subseteq \mathcal{Q}(\mathcal{M})$  so that the class  $\mathcal{Q}(\mathcal{M})$  is manifestly nonempty if  $\mathcal{P}(\mathcal{M})$  is so.

**Proposition 1** Assume that the class  $\mathcal{P}(\mathcal{M})$  is nonempty. Then the market  $\mathcal{M}$  is arbitrage free. Moreover, the arbitrage price process of any attainable contingent claim  $X$ , which settles at time  $T$ , is given by the risk-neutral valuation formula, for every  $t = 0, 1, \ldots, T$ 

$$\pi_t(X) = B_t \mathbb{E}_{\mathbb{P}^*}(X B_T^{-1} \mid \mathcal{F}_t) \tag{8}$$

where  $\mathbb{P}^*$  is any EMM (or GMM) for the market model  $\mathcal{M}.$ 

It can be checked that the binomial tree model (see **Binomial Tree**) with deterministic interest rates is complete, whereas its extension in which the stock price is modeled by a trinomial tree is incomplete. Completeness relies, in particular, on the choice of traded primary assets. Hence, it is natural to ensure completeness of an incomplete model by adding new traded instruments (typically, plain-vanilla options).

## **Completeness of a Finite Market**

We already know that if the set of equivalent martingale measures is nonempty, then the market model  $\mathcal{M}$  is arbitrage free. It appears that this condition is also necessary for the no-arbitrage property of the market model  $\mathcal{M}$ .

**Proposition 2** Suppose that the market model  $M$ is arbitrage free. Then the class  $\mathcal{P}(\mathcal{M})$  of equivalent martingale measures for  $\mathcal{M}$  is nonempty.

This leads to the following version of the *first fun*damental theorem of asset pricing (the First FTAP).

**Theorem 1** A finite market model  $M$  is arbitrage free if and only if the class  $\mathcal{P}(\mathcal{M})$  is nonempty, that is, there exists at least one equivalent martingale measure for  $\mathcal{M}$ .

In the case of a finite market model, this result was established by Harrison and Pliska [13]. For a probabilistic approach to the First FTAP we refer to Taqqu and Willinger [20], who examine the case of a finite market model, and to papers by Dalang et al. [10] and Schachermayer [23], who study the case of a discrete-time model with infinite state space.

The following fundamental result provides a relationship between the completeness property of a finite market model and the uniqueness (or nonuniqueness) of an EMM. Any result of this kind is commonly referred to as the second fundamental theorem of asset pricing.

**Theorem 2** Assume that a market model  $M$  is arbitrage free so that the class  $\mathcal{P}(\mathcal{M})$  is nonempty. Then  $\mathcal{M}$  is complete if and only if the uniqueness of an equivalent martingale measure for  $\mathcal{M}$  holds.

If an arbitrage-free market model is incomplete, not all claims are attainable and the class  $\mathcal{P}(\mathcal{M})$  of equivalent martingale measures comprises more than one element. In that case, one can use the following result to determine whether a given contingent claim is attainable.

**Corollary 1** A contingent claim  $X \in \mathcal{X}$  is attainable in an arbitrage-free market model  $\mathcal{M}$  if and only if the map  $\mathbb{P}^* \mapsto \mathbb{E}_{\mathbb{P}^*}(XB_T^{-1})$  from  $\mathcal{P}(\mathcal{M})$  to  $\mathbb{R}$  is constant.

It follows from this result that if a claim is attainable, so that its arbitrage price is well defined, the price can be computed using the risk-neutral valuation formula under any of (possibly several) martingale measures. In addition, if the risk-neutral valuation formula yields the same result for any choice of an EMM for the market model at hand, then a given claim is necessarily attainable.

# **Multidimensional Black and Scholes** Model

A multidimensional Black and Scholes model is a natural extension to a multiasset setup of the classic Black and Scholes [3] options pricing model. Let  $k$ denote the number of primary risky assets. For any  $i = 1, \ldots, k$ , the price process  $S^i$  of the *i*th risky asset, referred to as the  $i$ th stock, is modeled as an Itô process (the dot  $\cdot$  stands for the inner product in  $\mathbb{R}^d$ 

$$dS_t^i = S_t^i(\mu_t^i dt + \sigma_t^i \cdot dW_t) \tag{9}$$

with  $S_0^i > 0$  or, more explicitly,

$$\mathrm{d}S_t^i = S_t^i \left(\mu_t^i \,\mathrm{d}t + \sum_{j=1}^d \sigma_t^{ij} \,\mathrm{d}W_t^j\right) \qquad (10)$$

where  $W = (W^1, \ldots, W^d)$  is a standard *d*-dimensional Brownian motion, defined on a filtered probability space  $(\Omega, \mathbb{F}, \mathbb{P})$ . We make the natural assumption that the underlying filtration  $\mathbb{F}$  coincides with the filtration  $\mathbb{F}^W$  generated by the Brownian motion W. The coefficients  $\mu^i$  and  $\sigma^i$  follow bounded progressively measurable processes on the space  $(\Omega, \mathbb{F}, \mathbb{P}),$  with values in  $\mathbb{R}$  and  $\mathbb{R}^d$ , respectively. An important special case is obtained by postulating that for every *i* the volatility coefficient  $\sigma^i$  is represented by a fixed vector in  $\mathbb{R}^d$  and the appreciation rate  $\mu^i$ is a real number.

For brevity, we write  $\sigma = \sigma_t$  to denote the volatility matrix—that is, the time-dependent random matrix  $[\sigma_t^{ij}]$ , whose *i*th row specifies the volatility of the  $i$ th traded stock. The last primary security is the risk-free savings account  $B$  with the price process  $S^{k+1} = B$  satisfying

$$\mathrm{d}B_t = r_t B_t \,\mathrm{d}t, \quad B_0 = 1 \tag{11}$$

for a bounded, nonnegative, progressively measurable interest rate process  $r$ . This means that, for every  $t \in [0, T],$ 

$$B_t = \exp\left(\int_0^t r_u \, d_u\right) \tag{12}$$

To ensure the absence of arbitrage opportunities, we postulate the existence of a  $d$ -dimensional, progressively measurable process  $\gamma$  such that the equality

$$r_t - \mu_t^i = \sum_{j=1}^d \sigma_t^{ij} \gamma_t^j = \sigma_t^i \cdot \gamma_t \tag{13}$$

is satisfied simultaneously for every  $i = 1, \ldots, k$  (for Lebesgue a.e.  $t \in [0, T]$ , with probability one). Note that the *market price for risk*  $\gamma$  is not uniquely determined, in general. Indeed, the uniqueness of a solution  $\gamma$  to this equation holds only if  $d \leq k$  and the volatility matrix  $\sigma$  has the full rank for every  $t \in [0, T]$ .

For example, if  $d = k$  and the volatility matrix  $\sigma$  is nonsingular (for Lebesgue a.e.  $t \in [0, T]$ , with probability one), then, for every  $t \in [0, T]$ ,

$$\gamma_t = \sigma_t^{-1}(r_t \mathbf{1} - \mu_t) \tag{14}$$

where  $1$  denotes the *d*-dimensional vector with every component equal to one, and  $\mu_t$  is the vector with components  $\mu_t^i$ . For any process  $\gamma$  satisfying the above equation, we introduce a probability measure  $\mathbb{P}^*$  on  $(\Omega, \mathcal{F}_T)$  by setting

$$\frac{d\mathbb{P}^*}{d\mathbb{P}} = \exp\left(\int_0^T \gamma_u \cdot dW_u - \frac{1}{2} \int_0^T \|\gamma_u\|^2 \, du\right),\tag{15}$$
  
$$\mathbb{P}\text{-a.s.}$$

provided that the right-hand side in the last formula is well defined. The Doléans (stochastic) exponential

$$\eta_t = \exp\left(\int_0^t \gamma_u \cdot dW_u - \frac{1}{2} \int_0^t \|\gamma_u\|^2 \, \mathrm{d}u\right) \quad (16)$$

is known to be a strictly positive supermartingale (but not necessarily a martingale) under  $\mathbb{P}$ , since it may happen that  $\mathbb{E}_{\mathbb{P}^*}(\eta_T) < 1$ . A probability measure  $\mathbb{P}^*$  equivalent to  $\mathbb{P}$  is well defined if and only if the process  $\eta$  follows a  $\mathbb{P}$ -martingale, that is, when  $\mathbb{E}_{\mathbb{P}^*}(n_T) = 1.$  For the last property to hold, it is enough (but not necessary) that  $\gamma$  is a bounded process.

Assume that the class of martingale measures is nonempty. By virtue of the Girsanov theorem, the process  $W^*$ , which equals, for every  $t \in [0, T]$ ,

$$W_t^* = W_t - \int_0^t \gamma_u \, \mathrm{d}u \tag{17}$$

is a  $d$ -dimensional standard Brownian motion on  $(\Omega, \mathbb{F}, \mathbb{P}^*)$ . It follows from the Itô formula that the discounted stock price  $S_t^{*i} = S_t^i B_t^{-1}$  satisfies under  $\mathbb{P}^*$ 

$$dS_t^{*i} = S^{*i} \sigma_t^i \cdot dW_t^* \tag{18}$$

for any  $i = 1, \ldots, k$ . This means that the discounted prices of all stocks follow local martingales under  $\mathbb{P}^*$ , so that any probability measure described above is a martingale measure for our model and it corresponds to the choice of the savings account as the *numéraire* asset. The class of *tame strategies* relative to  $B$  is defined by postulating that the discounted wealth of a strategy follows a stochastic process bounded from below. The market model obtained in this way is referred to as the *multidimensional Black and Scholes* model.

In the classic version of the multidimensional Black and Scholes model, one postulates that  $d =$ k, the constant volatility matrix  $\sigma$  is nonsingular, and the appreciation rates  $\mu_i$  and the continuously compounded interest rate  $r$  are constant. It is easily

seen that under these assumptions, the martingale measure  $\mathbb{P}^*$  exists and is unique.

## **Completeness of the Multidimensional Black and Scholes Model**

The completeness of the multidimensional Black and Scholes model is defined in much the same way as for a finite market model, except that certain technical restrictions need to be imposed on the class of contingent claims we wish to hedge and price. This is linked to the fact that not all self-financing trading strategies are deemed to be *admissible*. Some of them should be excluded in order to ensure the no-arbitrage property of the model (in addition to the existence of a martingale measure). Typically, one considers the class of tame strategies to play the role of admissible trading strategies.

The multidimensional Black and Scholes model is said to be *complete* if any  $\mathbb{P}^*$ -integrable, bounded from below contingent claim  $X$  is attainable, that is, if for any such claim  $X$  there exists an admissible trading strategy  $\phi$  such that  $X = V_T(\phi)$ . Otherwise, the market model is said to be *incomplete*.

Since, by assumption, the interest rate process  $r$ is nonnegative and bounded, the integrability and boundedness of  $X$  is therefore equivalent to the integrability and boundedness of the discounted claim  $X/B_T$ . It is not postulated that the uniqueness of an EMM holds, and thus the  $\mathbb{P}^*$ -integrability of X refers to any EMM for the model. The next result establishes necessary and sufficient conditions for the completeness of the Black and Scholes market.

**Proposition 3** The following are equivalent:

- 1. the multidimensional Black and Scholes model is complete;
- 2. inequality  $d \leq k$  holds and the volatility matrix  $\sigma$  has full rank for Lebesgue a.e.  $t \in$  $[0, T]$ , with probability 1;
- 3. there exists a unique equivalent martingale measure  $\mathbb{P}^*$  for discounted stock price  $S^{*i}$  for  $\textit{every } i = 1, \ldots, k.$

The classic one-dimensional Black and Scholes market model introduced in  $[3]$  is clearly a special case of the multidimensional Black and Scholes model. Hence, the above results apply also to the classic Black and Scholes market model, in which the martingale measure  $\mathbb{P}^*$  is well known to be unique. We conclude that the one-dimensional Black and Scholes market model is complete, that is, any  $\mathbb{P}^*$ integrable contingent claim is  $\mathbb{P}^*$ -attainable and thus it can be priced by arbitrage.

In the general semimartingale framework, the equivalence of the uniqueness of an EMM and the completeness of a market model were conjectured by Harrison and Pliska [13, 14] (see also [18]). The case of the Brownian filtration is examined in [16]. Chatelain and Stricker [7, 8] provide definitive results for the case of continuous local martingales (see also [1, 20] for related results). They focus on the important distinction between the vector and componentwise stochastic integrals.

#### **Local and Stochastic Volatility Models**

Note that we have examined the completeness of the market model in which trading was restricted to a predetermined family of primary securities. In practice, several derivative securities are also traded either on organized exchanges or over-the-counter and thus they can be used to formally complete a given market model. Let us comment briefly on two classes of models in which, for simplicity, we assume that the bond price is deterministic.

Following Dupire [12], we define the stock price as a solution to the following stochastic differential equation:

$$dS_t = S_t(\mu(S_t, t) dt + \sigma(S_t, t) dW_t^*)$$
(19)

where  $S_0 > 0$  and the function  $\sigma : \mathbb{R}_+ \times \mathbb{R}_+ \to \mathbb{R}$ represents the so-called local volatility. In practice, the function  $\sigma$  is obtained by fitting the model to market quotes of traded options. Model of this form is complete and thus any derivative security with the stock price as an underlying asset can be hedged and priced by arbitrage (provided, of course, that the model is arbitrage free). Another example of a complete model in which the volatility follows a stochastic process is discussed by Hobson and Rogers [15].

In a typical stochastic volatility model, the stock price  $S$  is governed by the equation

$$dS_t = \mu(S_t, t) dt + \sigma_t S_t dW_t \tag{20}$$

where the *stochastic volatility* process  $\sigma$  satisfies

$$d\sigma_t = a(\sigma_t, t) dt + b(\sigma_t, t) d\hat{W}_t \qquad (21)$$

where W and  $\widehat{W}$  are (possibly correlated) onedimensional Brownian motions defined on some filtered probability space  $(\Omega, \mathbb{F}, \mathbb{P})$ . Owing to the presence of the Brownian motion  $\widehat{W}$ , stochastic volatility models are incomplete if stock and bond are the only trade primary assets. By postulating that some plain-vanilla options are traded, it is possible to complete a stochastic volatility model, however. Completeness of a model of financial market with traded call and put options and related topics, such as *static hedging* of exotic options, was examined by several authors: Bajeux-Besnainou and Rochet [2], Breeden and Litzenberger [4], Brown et al. [5], Carr et al. [6], Derman et al. [11], Madan and Milne [17], Nachman [19], Romano and Touzi [21], and Ross [22], to mention a few.

## References

- $[1]$ Artzner, P. & Heath, D. (1995). Approximate completeness with multiple martingale measures, Mathematical Finance 5, 1-11.
- [2] Bajeux-Besnainou, I. & Rochet, J.-C. (1996). Dynamic spanning: are options an appropriate instrument, Mathematical Finance  $6$ , 1–16.
- Black, F. & Scholes, M. (1973). The pricing of options [3] and corporate liabilities, Journal of Political Economics 81. 637-654.
- Breeden, D. & Litzenberger, R. (1978). Prices of state-[4] contingent claims implicit in option prices, Journal of Business 51, 621-651.
- Brown, H., Hobson, D. & Rogers, L. (2001). Robust [5] hedging of options, Applied Mathematical Finance 5,  $17 - 43$
- Carr. P., Ellis, K. & Gupta, V. (1998). Static hedging of [6] exotic options, *Journal of Finance* **53**, 1165–1190.
- Chatelain, M. & Stricker, C. (1994). On componentwise [7] and vector stochastic integration, Mathematical Finance 4.  $57-65$
- Chatelain, M. & Stricker, C. (1995). Componentwise [8] and vector stochastic integration with respect to certain multi-dimensional continuous local martingales, in Seminar on Stochastic Analysis, Random Fields and Applications, E. Bolthausen, M. Dozzi, F. Russo, eds, Birkhäuser, Boston, Basel, Berlin, pp. 319-325.
- [9] Cox, J.C., Ross, S.A. & Rubinstein, M. (1979). Option pricing: a simplified approach, Journal of Financial Economics 7, 229–263.
- [10] Dalang, R.C., Morton, A. & Willinger, W. (1990). Equivalent martingale measures and no-arbitrage in
# **Stochastic Discount** Factors

Economic agents make investment decisions within active and liquid financial markets. Capital is allocated today in exchange for some future income stream. If there is no uncertainty regarding the future payoff of an investment opportunity, the yield that will be asked on the investment will equal the riskfree interest rate prevailing for the time period covering the time of investment until the time of the payoff. However, in the presence of any payoff uncertainty at the time of undertaking an investment venture, economic agents will typically ask for risk compensation, and thus for some *investment-specific* yield, which will discount the expected future payoff stream. The yields that particular agents ask for depend both on their statistical views on possible future outcomes, as well as their attitudes toward risk.

Yields vary across different investment opportunities and their interrelations are difficult to explain. For the same agent, a different discounting factor has to be used for every separate valuation occasion. If, however, one is ready to accept discounting that varies randomly with the possible outcomes, and therefore accepts the concept of a *stochastic* discount factor, then a very economically consistent theory can be developed. Asset valuation becomes a matter of randomly discounting payoffs under different states of nature and weighing them according to the agent's probability structure. The advantages of this approach are obvious, since a *single* discounting mechanism suffices to describe how any asset is priced by the agent.

We discuss the theory of stochastic discount factors first in a discrete-time, finite state space and then in the more practical case of Itô-process models.

# **Stochastic Discount Factors in Discrete Probability Spaces**

We start by introducing all relevant ideas in a very simple one-time-period framework and finite states of the world. There are plenty of textbooks with vast exposition on these and other related themes (e.g., [1] or the first chapters of  $[9]$ —see also  $[5]$  for the general state-space case).

## The Setup

Consider a very simplistic example of an economy. where there are only two dates of interest, represented by times  $t = 0$  (today) and  $t = T$  (the financialplanning horizon). There are several states of nature possible at time  $T$  and, for the time being, these are represented as a *finite* set  $\Omega$ . Only one  $\omega \in \Omega$  will be revealed at time  $T$ , but this is not known in advance today.

In the market, there is a *baseline* asset with a price process  $S^0 = (S^0)_{t=0,T}$ . Here,  $S_0^0$  is a strictly positive constant and  $S_T^0(\omega) > 0$  for all  $\omega \in \Omega$ . The process  $\beta := S_{0}^{0}/S^{0}$  is called the *deflator*. It is customary to regard this baseline asset as riskless, providing a simple annualized interest rate  $r \in \mathbb{R}_+$  for investment from today to time T; in this case,  $S_0^0 = 1$  and  $S_T^0 = 1 + rT$ . This viewpoint is *not* adapted here, since it is unnecessary.

Together with the baseline asset, there exist  $d$  other liquid *traded* assets whose prices  $S_0^i$ ,  $i = 1, \ldots, d$ today are known constants, but the prices  $S_T^i$ ,  $i =$  $1, \ldots, d$ , at day T depend on the outcome  $\omega \in \Omega$ , that is, they are random variables.

# Agent Portfolio Selection via Expected Utility Maximization

Consider an economic agent in the market as described above. Faced with inherent uncertainty, the agent postulates some likelihood on the possible outcomes, modeled via a probability measure  $P: \Omega \mapsto [0, 1]$  with  $\sum_{\omega \in \Omega} P[\omega] = 1$ . This gives rise to a probability  $\mathbb{P}$  on the subsets of  $\Omega$  defined *via*  $\mathbb{P}[A] = \sum_{\omega \in A} \mathsf{P}(\omega)$  for all  $A \subseteq \Omega$ . This probability can either be *subjective*, that is, coming from views that are agent specific, or *historical*, that is, arising from statistical considerations via some estimation procedure.

Economic agents act in the market and optimally invest to maximize their satisfaction. Each agent has some *preference structure* on the possible future random payoffs that is represented here *via* the *expected* utility paradigm.<sup>a</sup> There exists a continuously dif*ferentiable, increasing, and strictly concave function*  $U:\mathbb{R}\mapsto\mathbb{R}$ , such that the agent will prefer a random payoff  $\xi : \Omega \mapsto \mathbb{R}$  from another random payoff  $\zeta: \Omega \mapsto \mathbb{R}$  at time *T* if and only if  $\mathbb{E}^{\mathbb{P}}[U(\zeta)] \leq$  $\mathbb{E}^{\mathbb{P}}[U(\xi)],$  where  $\mathbb{E}^{\mathbb{P}}$  denotes expectation with respect to the probability  $\mathbb{P}$ .

Starting with capital  $x \in \mathbb{R}$ , an economic agent chooses at day zero a strategy  $\theta \equiv (\theta^1, \dots, \theta^d) \in$  $\mathbb{R}^d$ , where  $\theta^j$  denotes the units from the *j*th asset held in the portfolio. What remains,  $x - \sum_{i=1}^{d} \theta^{i} S_{0}^{i}$ , is invested in the baseline asset. If  $X^{(\overline{x},\theta)}$  is the wealth generated starting from capital  $x$  and investing according to  $\theta$ , then  $X_0^{(x,\theta)} = x$  and

$$X_T^{(x;\theta)} = \left(x - \sum_{i=1}^d \theta^i S_0^i\right) \frac{S_T^0}{S_0^0} + \sum_{i=1}^d \theta^i S_T^i$$
$$= x \frac{S_T^0}{S_0^0} + \sum_{i=1}^d \theta^i \left(S_T^i - \frac{S_T^0}{S_0^0} S_0^i\right) \tag{1}$$

or, in deflated terms,  $\beta_T X_T^{(x;\theta)} = x + \sum_{i=1}^d \theta^i$  $(\beta_T S_T^i - S_0^i)$ . The agent's objective is to choose a strategy in such a way as to *maximize expected utility*, that is, find  $\theta_*$  such that

$$\mathbb{E}^{\mathbb{P}}\left[U\left(X_{T}^{(x;\theta_{*})}\right)\right] = \sup_{\theta \in \mathbb{R}^{d}} \mathbb{E}^{\mathbb{P}}\left[U\left(X_{T}^{(x;\theta)}\right)\right] \tag{2}$$

The above problem will indeed have a solution if and only if no arbitrages exist in the market. By definition, an *arbitrage* is a wealth generated by some  $\theta \in \mathbb{R}^d$  such that  $\mathbb{P}[X_T^{(x;\theta)} \ge 0] = 1$  and  $\mathbb{P}[X_T^{(x;\theta)} > 0] > 0$ . It is easy to see that arbitrages exist in the market if and only if  $\sup_{\theta \in \mathbb{R}^d} \mathbb{E}^{\mathbb{P}}[U(X_T^{(x;\theta)})]$  is not attained by some  $\theta_* \in \mathbb{R}^d$ . Assuming, then, the noarbitrage (NA) condition, concavity of the function  $\mathbb{R}^d \ni \theta \mapsto \mathbb{E}^{\mathbb{P}}[U(X_T^{(x;\theta)})]$  will imply that the firstorder conditions

$$\frac{\partial}{\partial \theta^{i}}\Big|_{\theta=\theta_{*}} \mathbb{E}^{\mathbb{P}}\Big[U\left(X_{T}^{(x;\theta)}\right)\Big] = 0, \quad \text{for all } i = 1, \dots, d$$
(3)

will provide the solution  $\theta_*$  to the problem. Since the expectation is just a finite sum, the differential operator can pass inside, and then the first-order conditions for optimality are

$$0 = \mathbb{E}^{\mathbb{P}} \left[ \left. \frac{\partial}{\partial \theta^{i}} \right|_{\theta = \theta_{*}} U \left( X_{T}^{(x;\theta)} \right) \right]$$
  
$$= \mathbb{E}^{\mathbb{P}} \left[ U' \left( X_{T}^{(x;\theta_{*})} \right) \left( S_{T}^{i} - \frac{S_{T}^{0}}{S_{0}^{0}} S_{0}^{i} \right) \right],$$
  
$$i = 1, \dots, d \tag{4}$$

The above is a nonlinear system of  $d$  equations to be solved for d unknowns  $(\theta^1_*, \ldots, \theta^d_*)$ . Under NA, the system 4 has a solution  $\theta_*$ . Actually, under a trivial nondegeneracy condition in the market, the solution is unique; even if the optimal strategy  $\theta_*$  is not unique, strict concavity of  $U$  implies that the optimal wealth  $X_T^{(x;\theta_*)}$  generated is unique.

A little bit of algebra on equation (4) gives, for all  $i = 1, \ldots, d,$ 

$$S_0^i = \mathbb{E}^{\mathbb{P}} \left[ Y_T S_T^i \right], \text{ where}$$
  
$$Y_T := \frac{U' \left( X_T^{(x;\theta_*)} \right)}{\mathbb{E}^{\mathbb{P}} \left[ (S_T^0 / S_0^0) U' \left( X_T^{(x;\theta_*)} \right) \right]}$$
(5)

Observe that since  $U$  is continuously differentiable and strictly increasing,  $U'$  is a strictly positive function, and therefore  $\mathbb{P}[Y_T > 0] = 1$ . Also, equation (5) also holds trivially for  $i = 0$ . Note that the random variable  $Y_T$  that was obtained above depends on the utility function U, the probability  $\mathbb{P}$ , as well as on the initial capital  $x \in \mathbb{R}$ .

**Definition 1** In the model described above, a process  $Y = (Y_t)_{t=0,T}$  will be called a stochastic discount factor if  $\mathbb{P}[Y_0=1,Y_T>0]=1$  and  $S_0^i=\mathbb{E}^{\mathbb{P}}\left[Y_TS_T^i\right]$ for all  $i = 0, \ldots, d$ .

If  $Y$  is a stochastic discount factor, using equation  $(1)$ , one can actually show that

$$\mathbb{E}^{\mathbb{P}}\left[Y_{T}X_{T}^{(x;\theta)}\right] = x, \quad \text{for all } x \in \mathbb{R} \text{ and } \theta \in \mathbb{R}^{d}$$
(6)

In other words, the process  $YX^{(x;\theta)}$  is a  $\mathbb{P}$ -martingale for all  $x \in \mathbb{R}$  and  $\theta \in \mathbb{R}^d$ .

#### Connection with Risk-neutral Valuation

Since  $\mathbb{E}^{\mathbb{P}}[S_T^0 Y_T] = S_0^0 > 0$ , we can define a probability mass  $\mathcal{Q}$  by requiring that  $\mathcal{Q}(\omega) = (S_T^0(\omega)/S_0^0)$  $Y_T(\omega) \mathsf{P}(\omega)$ , which defines a probability  $\mathbb{Q}$  on subsets of  $\Omega$  in the obvious way. Observe that, for any  $A \subseteq \Omega$ ,  $\mathbb{Q}[A] > 0$  if and only if  $\mathbb{P}[A] > 0$ ; we say that the probabilities  $\mathbb{P}$  and  $\mathbb{Q}$  are *equivalent* and we denote this by  $\mathbb{Q} \sim \mathbb{P}$ . Now, rewrite equation (5) as

$$S_0^i = \mathbb{E}^{\mathbb{Q}} \left[ \beta_T S_T^i \right], \quad \text{for all } i = 0, \dots, d \quad (7)$$

A probability  $\mathbb{Q}$ , equivalent to  $\mathbb{P}$ , with the property prescribed in equation (7) is called *risk-neutral* or an equivalent martingale measure. In this simple framework, stochastic discount factors and risk-neutral probabilities are in one-to-one correspondence. In fact, more can be said.

**Theorem 1** [Fundamental Theorem of Asset Pricing] In the discrete model as described previously, the following three conditions are equivalent:

- 1. There are no arbitrage opportunities.
- 2. A stochastic discount factor exists.
- 3. A risk-neutral probability measure exists.

The fundamental theorem of asset pricing was first formulated by Ross [11] and it took 20 years to reach a very general version of it in general semimartingale models that are beyond the scope of our treatment here. The interested reader can check the monograph [3], where the history of the theorem and all its proofs are presented.

#### The Important Case of the Logarithm

The most well-studied case of utility on the real line is  $U(x) = \log(x)$ , both because of its computational simplicity and for the theoretical value that it has. Since the logarithmic function is only defined on the strictly positive real line, it does not completely fall in the aforementioned framework, but it is easy to see that the described theory is still valid.

Consider an economic agent with logarithmic utility that starts with initial capital  $x = 1$ . Call  $X^* =$  $X^{(1;\theta_*)}$  the optimal wealth corresponding to log-utility maximization. The fact that  $U'(x) = 1/x$  allows to define a stochastic discount factor  $Y^*$  via  $Y_0^* = 1$  and

$$Y_T^* = \frac{1}{X_T^* \mathbb{E}^{\mathbb{P}} \left[ 1/(\beta_T X_T^*) \right]} \tag{8}$$

From  $\mathbb{E}^{\mathbb{P}}[Y_T^*X_T^*] = 1$ , it follows that  $\mathbb{E}^{\mathbb{P}}[1/$  $(\beta_T X_T^*)$  = 1 and therefore  $Y^* = 1/X^*$ . This simple relationship between the log-optimal wealth and the stochastic discount factor that is induced by it is one of the keys to characterize the existence of stochastic discount factors in more complicated models and their relationship with absence of free lunches. It finds good use in the section Stochastic Discount Factors for Itô Processes for the case of models using Itô processes.

## Arbitrage-free Prices

For a claim with random payoff  $H_T$  at time T, an *arbitrage-free* (AF) price  $H_0$  is a price at time zero such that the extended market that consists of the original traded assets with asset prices  $S^i$ ,  $i = 0, \ldots, d$ , augmented by the new claim, remains AF. If the claim is *perfectly replicable*, that is, if there exists  $x \in \mathbb{R}$  and  $\theta \in \mathbb{R}^d$  such that  $X_T^{(x;\theta)} = H_T$ , it is easily seen that the unique AF price for the claim is  $x$ . However, it is frequently the case that a newly introduced claim is not perfectly replicable using the existing liquid assets. In that case, there exists more than one AF price for the claim; actually, the set of all the possible AF prices is  $\{\mathbb{E}^{\mathbb{P}}[Y_T H_T] \mid Y \text{ is a stochastic discount factor}\}.$  To see this, first pick a stochastic discount factor  $Y_T$  and set  $H_0 = \mathbb{E}[Y_T H_T]$ ; then, Y remains a stochastic discount factor for the extended market, which therefore does not allow for any arbitrage opportunities. Conversely, if  $H_0$  is an AF price for the new claim, we know from Theorem 1 that there exists a stochastic discount factor  $Y$  for the extended market, which satisfies  $H_0 = \mathbb{E}[Y_T H_T]$  and is trivially a stochastic discount factor for the original market. The result we just mentioned justifies the appellation "Fundamental theorem of asset pricing" for Theorem 1.

## Utility Indifference Pricing

Suppose that a new claim promising some random payoff at time  $T$  is issued. Depending on the claim's present traded price, an economic agent might be inclined to take a long or short position—this will depend on whether the agent considers the market price low or high, respectively. There does exist a market price level of the claim that will make the agent indifferent to going long or short on an infinitesimal<sup>b</sup> amount of asset. This price level is called *indifference price*. In the context of claim valuation, utility indifference prices have been introduced in  $[2]$ ;<sup>c</sup> however, they had been widely used previously in the science of economics. Indifference prices depend on the particular agent's views, preferences, as well as portfolio structure, and should not be confused with market prices, which are established using the forces of supply and demand.

Since the discussed preference structures are based on *expected utility*, it makes sense to try and understand quantitatively how *utility indifference prices* are formed. Under the present setup, consider a claim with random payoff  $H_T$  at time T. The question we wish to answer is this: what is the indifference price  $H_0$  of this claim today for an economic agent?

For the time being, let  $H_0$  be any price set by the market for the claim. The agent will invest in the risky assets and will hold  $\theta$  units of them, as well as the new claim, taking a position of  $\epsilon$  units. Then, the agent's terminal payoff is

$$X_T^{(x;\theta,\epsilon)} := X_T^{(x;\theta)} + \epsilon \left( H_T - \frac{S_T^0}{S_0^0} H_0 \right) \tag{9}$$

The agent will again maximize expected utility, that is, will invest  $(\theta_*, \epsilon_*) \in \mathbb{R}^d \times \mathbb{R}$  such that

$$\mathbb{E}^{\mathbb{P}}\Big[U\left(X_{T}^{(x;\theta_{*},\epsilon_{*})}\right)\Big] = \sup_{(\theta,\epsilon)\in\mathbb{R}^{d}\times\mathbb{R}}\mathbb{E}^{\mathbb{P}}\Big[U\left(X_{T}^{(x;\theta,\epsilon)}\right)\Big]$$
(10)

If  $H_0$  is the agent's indifference price, it must follow that  $\epsilon_* = 0$  in the above maximization problem; then, the agent's optimal decision regarding the claim would be not to buy or sell any units of the asset. In particular, the concave function  $\mathbb{R} \ni$  $\epsilon \mapsto \mathbb{E}^{\mathbb{P}} \left[ U \left( \hat{X}^{(x;\theta_*,\epsilon)}_T \right) \right]$  should achieve its maximum at  $\epsilon = 0$ . First-order conditions give that  $H_0$  is the agent's indifference price if

$$0 = \frac{\partial}{\partial \epsilon} \Big|_{\epsilon=0} \mathbb{E}^{\mathbb{P}} \Big[ U \left( X_T^{(x;\theta_*,\epsilon)} \right) \Big]$$
  
$$= \mathbb{E}^{\mathbb{P}} \Big[ U' \left( X_T^{(x;\theta_*,0)} \right) \left( X_T - \frac{S_T^0}{S_0^0} X_0 \right) \Big] \quad (11)$$

A remark is in order before writing down the indifference-pricing formula. The strategy  $\theta_*$  that has been appearing above represents the optimal holding in the liquid traded assets when all assets and the claim are available—it is *not*, in general, the agent's optimal asset holdings if the claim were *not* around. Nevertheless, *if* the solution of problem  $(10)$  is such that the optimal holdings in the claim are  $\epsilon_* = 0$ , *then*  $\theta_*$  are also the agent's optimal asset holdings if there had been no claim to begin with. In other words, if  $\epsilon_* = 0$ ,  $X_T^{(x;\theta_*,0)}$  is exactly the same quantity  $X_T^{(x;\theta_*)}$  that appears in equation (4). Remembering the definition of the stochastic discount factor  $Y_T$  of

equation  $(5)$ , we can write

$$H_0 = \mathbb{E}^{\mathbb{I}^p} \left[ Y_T H_T \right] \tag{12}$$

It is important to observe that  $Y_T$  depends on a number of factors, namely, the probability  $\mathbb{P}$ , the utility U, and the initial capital x, but not on the particular claim to be valued. Thus, we need only one evaluation of the stochastic discount factor and we can use it to find indifference prices with respect to all kinds of different claims.

#### State Price Densities

For a fixed  $\omega \in \Omega$ , consider an Arrow-Debreau security that pays off a unit of account at time  $T$ if the state of nature is  $\omega$ , and pays off nothing, otherwise. The indifference price of this security for the economic agent is  $p(\omega) := Y(\omega)P(\omega)$ . Since  $Y$  appears as the density of the "state price"  $p$ with respect to the probability  $\mathbb{P}$ , stochastic discount factors are also termed state price densities in the literature. For two states of nature  $\omega$  and  $\omega'$  of  $\Omega$  such that  $Y(\omega) < Y(\omega')$ , an agent who uses the stochastic discount factor  $Y$  would consider  $\omega'$  a more unfavorable state than  $\omega$  and would be inclined to pay more for insurance against adverse market movements.

#### Comparison with Real-world Valuation

Only for the purpose of what is presented here, assume that  $S_0^0 = 1$  and  $S_T^0 = 1 + rT$  for some  $r \in \mathbb{R}_+$ . Let Y be a stochastic discount factor; then, we have  $1 = S_0^0 = \mathbb{E}^{\mathbb{P}}[Y_T S_T^0] = (1 + rT)\mathbb{E}^{\mathbb{P}}[Y_T].$ Pick any claim with random payoff  $H_T$  at time T and use  $H_0 = \mathbb{E}^{\mathbb{P}}[Y_T H_T]$  to write

$$H_0 = \frac{1}{1 + rT} \mathbb{E}^{\mathbb{P}}[H_T] + \text{cov}^{\mathbb{P}}(Y_T, H_T) \qquad (13)$$

where  $\text{cov}^{\mathbb{P}}(\cdot, \cdot)$  is used to denote *covariance* of two random variables with respect to  $\mathbb{P}$ . The first term  $(1+rT)^{-1}\mathbb{E}^{\mathbb{P}}[H_T]$  of the above formula describes "real-world" valuation for an agent who would be neutral under his views  $\mathbb{P}$  in facing the risk coming from the random payoff  $H_T$ . This risk-neutral attitude is usually absent: agents require compensation for the risk they undertake, or might even feel inclined to pay more for a security that will insure them in cases of unfavorable outcomes. This is exactly mirrored by the

correction factor  $\text{cov}^{\mathbb{P}}(Y_T, H_T)$  appearing in equation (13). If the covariance of  $Y_T$  and  $H_T$  is negative, the claim tends to pay more when  $Y_T$  is low. By the discussion in the section State Price Densities, this means that the payoff will be high in states that are not greatly feared by the agent, who will therefore be inclined to pay *less* than what the real-world valuation gives. On the contrary, if the covariance of  $Y_T$  and  $H_T$  is positive,  $H_T$  will pay off higher in dangerous states of nature for the agent (where  $Y_T$  is also high), and the agent's indifference price will be higher than the real-world valuation.

# Stochastic Discount Factors for Itô Processes

#### The Model

Uncertainty is modeled via a probability space  $(\Omega, \mathcal{F}, \mathbf{F}, \mathbb{P}), \text{ where } \mathbf{F} = (\mathcal{F}_t)_{t \in [0,T]} \text{ is a filtration}$ representing the flow of information. The market consists of a *locally* riskless savings account whose price process  $S^0$  satisfies  $S_0^0 > 0$  and

$$\frac{\mathrm{d}S_t^0}{S_t^0} = r_t \mathrm{d}t, \quad t \in [0, T]$$
 (14)

for some **F**-adapted, positive *short-rate* process  $r =$  $(r_t)_{t\in\mathbb{R}}$ . It is obvious that  $S_t^0 = S_0^0 \exp(\int_0^t r_u du)$  for  $t \in [0, T]$ . We define the deflator  $\beta$  via

$$\beta_t = \frac{S_0^0}{S_t^0} = \exp\left(-\int_0^t r_u du\right), \quad t \in [0, T] \quad (15)$$

The movement of  $d$  risky assets will be modeled *via* Itô processes:

$$\frac{\mathrm{d}S_t^i}{S_t^i} = b_t^i \mathrm{d}t + \langle \sigma_t^{i}, \mathrm{d}W_t \rangle, \quad t \in \mathbb{R}_+, \quad i = 1, \dots, d$$
(16)

Here,  $b = (b^1, \ldots, b^d)$  is the **F**-adapted *d*-dimensional process of *appreciation rates*,  $W =$  $(W^1,\ldots,W^m)$  is an *m*-dimensional  $\mathbb{P}$ -Brownian motion representing the sources of uncertainty in the market, and  $\langle \cdot, \cdot \rangle$  denotes the usual inner product notation:  $\langle \sigma_t^{,i}, dW_t \rangle = \sum_{j=1}^m \sigma_t^{ji} dW_t^j$  where  $(\sigma^{ji})_{1 \le j \le m, \ 1 \le i \le d}$  is the **F**-adapted  $(m \times d)$ -matrixvalued process whose entry  $\sigma_t^{ji}$  represents the impact

of the  $j$ th source of uncertainty on the  $i$ th asset at time  $t \in [0, T]$ . With " $\top$ " denoting transposition,  $c := \sigma^{\top} \sigma$  is the  $d \times d$  local covariation matrix. To avoid degeneracies in the market, it is required that  $c_t$  has full rank for all  $t \in [0, T]$ ,  $\mathbb{P}$  almost surely (a.s.). This implies, in particular, that  $d < m$ —there are more sources of uncertainty in the market than are liquid assets to hedge away the uncertainty risk. Models of this sort are classical in the quantitative finance literature—see, for example, [8].

**Definition 2** A risk premium is any m-dimensional, **F**-adapted process  $\lambda$  satisfying  $\sigma^{\top} \lambda = b - r \mathbf{1}$ , where  $\mathbf{1}$  is the d-dimensional vector with all unit entries.

The terminology "risk premium" is better explained for the case  $d = m = 1$ ; then  $\lambda = (b$  $r/\sigma$  is the premium over the risk-free rate that investors require per unit of risk associated with the (only) source of uncertainty. In the general case,  $\lambda^{j}$  can be interpreted as the premium required for the risk associated with the  $j$ th source of uncertainty, represented by the Brownian motion  $W^j$ . In *incomplete* markets, when  $d < m$ , Proposition 1 shows all the different choices for  $\lambda$ . Each choice will parameterize the different risk attitudes of different investors. In other words, risk premia characterize the possible stochastic discount factors, as is revealed in Theorem 3.

If  $m = d$ , the equation  $\sigma^{\top} \lambda = b - r \mathbf{1}$  has only one solution:  $\lambda^* = \sigma c^{-1}(b - r\mathbf{1})$ . If  $d < m$  there are many solutions, but they can be characterized using easy linear algebra.

**Proposition 1** The risk premia are exactly all processes of the form  $\lambda = \lambda^* + \kappa$ , where  $\lambda^* := \sigma c^{-1}(b - \lambda^*)$ r1) and  $\kappa$  is any adapted process with  $\sigma^{\top}\kappa = 0$ .

If  $\lambda = \lambda^* + \kappa$  in the notation of Proposition 1, then  $\langle \lambda^*, \kappa \rangle = (b - r\mathbf{1})^\top c^{-1} \sigma^\top \kappa = 0$ . Then,  $|\lambda|^2 =$  $|\lambda^*|^2 + |\kappa|^2$ , where  $|\lambda^*|^2 = \langle b - r\mathbf{1}, c^{-1}(b - r\mathbf{1}) \rangle$ .

#### Stochastic Discount Factors

The usual method of obtaining stochastic discount factors in continuous time is through risk-neutral measures. The fundamental theorem of asset pricing in the present Itô-process setting states that absence of free lunches with vanishing risk<sup>d</sup> is equivalent to the existence of a probability  $\mathbb{Q} \sim \mathbb{P}$  such that  $\beta S^i$  is (only) a *local*  $\mathbb{Q}$ -martingale for all  $i = 0, \ldots, d$ . (For the definition of local martingales, check, e.g., [7].) In that case, by defining Y via  $Y_t = \beta_t (d\mathbb{Q}/d\mathbb{P})|_{\mathcal{F}_t}$ ,  $YS^i$ is a local  $\mathbb{P}$ -martingale for all  $i = 0, \ldots, d$ . The last property is taken here as the *definition* of a stochastic discount factor.

**Definition 3** Consider the above Itô-process setup,  $a$  stochastic process  $Y$  is called a stochastic discount factor if

- $Y_0 = 1$  and  $Y_T > 0$ ,  $\mathbb{P}$  a.s.<br>•  $YS^i$  is a local  $\mathbb{P}$ -martingale for  $all$  $i = 0, 1, \ldots, d.$

In the case where  $YS^0$  is an actual martingale, that is,  $\mathbb{E}^{\mathbb{P}}[Y_T S_T^0] = S_0^0$ , a risk-neutral measure  $\mathbb{Q}$  is readily defined *via* the recipe  $d\mathbb{Q} = (Y_T S_T^0 / S_0^0) d\mathbb{P}$ . However, this is not always the case, as Example 1 below will show. Therefore, existence of a stochastic discount factor is a weaker notion than existence of a risk-neutral measure. For some practical applications though, these differences are unimportant. There is further discussion of this point later in the section Stochastic Discount Factors and Equivalent Martingale Measures.

**Example 1** Let  $S^0 \equiv 1$  and  $S^1$  be a threedimensional Bessel process with  $S_0^1 = 1$ . If **F** is the natural filtration of  $S^1$ , it can be shown that the *only* stochastic discount factor is  $Y = 1/S^1$ , which is a *strict local martingale* in the terminology of [4].

#### Credit Constraints on Investment

In view of the theoretical possibility of continuous trading, to avoid so-called *doubling strategies* (and for the fundamental theorem of asset pricing to hold), *credit constraints* have to be introduced. The wealth of agents has to be bounded from below by some constant, representing the credit limit. Shifting the wealth appropriately, one can assume that the credit limit is set to zero; therefore, only positive wealth processes are allowed in the market.

Since only strictly positive processes are considered, it is more convenient to work with *proportions* of investment, rather than absolute quantities as was the case in the section Stochastic Discount Factors in Discrete Probability Spaces . Pick some F-adapted process  $\pi = (\pi^1, \ldots, \pi^{\hat{d}})$ . For  $i = 1, \ldots, d$  and  $t \in$ [0, T], the number  $\pi_t^i$  represents the *percentage* of capital in hand invested in asset  $i$  at time  $t$ . In that case,  $\pi^0 = 1 - \sum_{i=1}^d \pi^i$  will be invested in the savings account. Denote by  $X^{\pi}$  the wealth generated by starting from unit initial capital  $(X_0^{\pi} = 1)$  and invest according to  $\pi$ . Then,

$$\frac{\mathrm{d}X_t^{\pi}}{X_t^{\pi}} = \sum_{i=0}^d \pi_t^i \frac{\mathrm{d}S_t^i}{S_t^i} = (r_t + \langle \pi_t, b_t - r_t \mathbf{1} \rangle) \,\mathrm{d}t + \langle \sigma_t \pi_t, \mathrm{d}W_t \rangle \tag{17}$$

To ensure that the above wealth process is well defined, we must assume that

$$\int_{0}^{T} |\langle \pi_{t}, b_{t} - r_{t} \mathbf{1} \rangle| \, \mathrm{d}t < +\infty \text{ and}$$
$$\int_{0}^{T} \langle \pi_{t}, c_{t} \pi_{t} \rangle \mathrm{d}t < +\infty, \; \mathbb{P} \text{ a.s} \tag{18}$$

The set of all  $d$ -dimensional, **F**-adapted processes  $π$  that satisfy equation (18) is denoted by Π. A simple use of the integration-by-parts formula gives the following result:

**Proposition 2** If  $Y$  is a stochastic discount factor, then  $Y X^{\pi}$  is a local martingale for all  $\pi \in \Pi$ .

#### Connection with "No Free Lunch" Notions

The next line of business is to obtain an existential result about stochastic discount factors in the present setting, also connecting their existence to an NA-type notion. Remember, from the section The Important Case of the Logarithm, the special stochastic discount factor that is the reciprocal of the log-optimal wealth process. We proceed somewhat heuristically to compute the analogous processes for the Itô-process model. The linear stochastic differential equation  $(17)$ has the following solution, expressed in logarithmic terms:

$$\log X^{\pi} = \int_{0}^{\cdot} \left( r_{t} + \langle \pi_{t}, b_{t} - r_{t} \mathbf{1} \rangle - \frac{1}{2} \langle \pi_{t}, c_{t} \pi_{t} \rangle \right) dt$$
$$+ \int_{0}^{\cdot} \langle \sigma_{t} \pi_{t}, dW_{t} \rangle \tag{19}$$

Assuming that the local martingale term  $\int_0^{\infty} \langle \sigma_t \pi_t \rangle$  $dW_t$  in equation (19) is an actual martingale, the aim is to maximize the expectation of the drift term. Notice that we can actually maximize the drift *pathwise* if we choose the portfolio  $\pi_* = c^{-1}(b$ r1). We need to ensure that  $\pi_*$  is in  $\Pi$ . It is easy to see that the equations in  $(18)$  are both satisfied if and only if  $\int_0^T |\lambda_t^*|^2 dt < \infty \mathbb{P}$  a.s., where  $\lambda^* := \sigma c^{-1} (b - r \mathbf{1})$ is the special risk premium of Proposition 1. Under this assumption,  $\pi_* \in \Pi$ . Call  $X^* = X^{\pi_*}$  and define

$$Y^* := \frac{1}{X^*}$$
  
=  $\beta \exp\left(-\int_0^{\cdot} \langle \lambda_t^*, \mathrm{d}W_t \rangle - \frac{1}{2} \int_0^{\cdot} |\lambda_t^*|^2 \mathrm{d}t\right)$  (20)

Using the integration-by-parts formula, it is rather straightforward to check that  $Y^*$  is a stochastic discount factor. In fact, the ability to define  $Y^*$  is the way to establish that a stochastic discount factor exists, as the next result shows.

**Theorem 2** For the Itô process-model considered above, the following are equivalent.

- 1. The set of stochastic discount factors is nonemptv.
- $\int_0^T |\lambda_t^*|^2 \mathrm{d}t$ ,  $< \infty \mathbb{P}$ -a.s.; in that case,  $Y^*$  defined 2. in equation (20) is a stochastic discount factor.
- 3. For any  $\epsilon > 0$ , there exists  $\ell = \ell(\epsilon) \in \mathbb{R}_+$  such that  $\mathbb{P}[X_T^{\pi} > \ell] < \epsilon$  uniformly over all portfolios  $\pi \in \Pi$ .

The interest reader is referred to [6], where the property of the market described in statement 3 of the above theorem is termed No Unbounded Profit with Bounded Risk.

The next structural result about the stochastic discount factors in the Itô-process setting reveals the importance of  $Y^*$  as a building block.

**Theorem 3** Assume that  $\mathbf{F}$  is the filtration generated by the Brownian motion W. Then, any stochastic discount factor  $Y$  in the previous Itô-process model can be decomposed as  $Y = Y^* N^{\kappa}$ , where  $Y^*$  was defined in equation (20) and

$$N_t^{\kappa} = \exp\left(-\int_0^t \langle \kappa_u, \mathrm{d} W_u \rangle - \int_0^t |\kappa_u|^2 \mathrm{d} u\right),$$
  
 
$$\forall t \in [0, T]$$
(21)

where  $\kappa$  is an m-dimensional **F**-adapted process with  $\sigma^{\top}\kappa = 0.$ 

If the assumption that  $\mathbf{F}$  is generated by  $W$  is removed, one still obtains a similar result with  $N^{\kappa}$ being replaced by *any* positive  $\mathbf{F}$ -martingale  $N$  with  $N_0 = 1$  that is *strongly* orthogonal to W. The specific representation obtained in Theorem 3 comes from the *martingale representation theorem* of Brownian filtrations; see, for example, [7].

## Stochastic Discount Factors and Equivalent *Martingale Measures*

Consider an agent who uses a stochastic discount factor  $Y$  for valuation purposes. There is a possibility that  $YS^{i}$  could be a *strict local*  $\mathbb{P}$ -martingale for some  $i = 0, \ldots, d$ , which would mean that<sup>e</sup>  $S_0^i >$  $\mathbb{E}^{\mathbb{P}}[Y_T S_T^i]$ . The last inequality is puzzling in the sense that the agent's indifference price for the  $i$ th asset, which is  $\mathbb{E}^{\mathbb{P}}[Y_T S_T^i]$ , is *strictly* lower than the market price  $S_0^i$ . In such a case, the agent would be expected to wish to short some units of the  $i$ th asset. This is indeed what is happening; however, because of credit constraints, this strategy is infeasible. The following is a convincing example that establishes this fact. Before presenting the example, an important issue should be clarified. One would rush to state that such "inconsistencies" are tied to the notion of a stochastic discount factor as it appears in Definition 3, and that is *strictly* weaker than existence of a probability  $\mathbb{Q} \sim \mathbb{P}$  that makes all discounted processes  $\beta S^i$ *local*  $\mathbb{Q}$ -martingales for  $i = 0, \ldots, d$ . Even if such a probability *did* exist,  $\beta S^i$  could be a *strict local*  $\mathbb{Q}$ martingale for some  $i = 1, \ldots, d$ ; in that case,  $S_0^i >$  $\mathbb{E}^{\mathbb{Q}}[\beta_T S^i_T]$  and the same mispricing problem pertains.

**Example 2** Let  $S^0 \equiv 1$ ,  $S^1$  be the *reciprocal* of a three-dimensional Bessel process starting at  $S_0^1 = 1$ under  $\mathbb{P}$  and **F** be the filtration generated by  $S^1$ . Here,  $\mathbb{P}$  is the *only* equivalent local martingale measure and  $1 = S_0^1 > \mathbb{E}^{\mathbb{P}}[S_T^1]$  for all  $T > 0$ . This is a *complete* market—an agent can start with capital  $\mathbb{E}^{\mathbb{P}}[S^1_T]$  and invest in a way so that at time  $T$  the wealth generated is exactly  $S_T$ . Naturally, the agent would like to long as much as possible from this replicating portfolio and go as short as possible from the actual asset. However, in doing so, the possible downside risk is infinite throughout the life of the investment and the enforced credit constraints will disallow for such strategies.

In the context of Example 2, the law of one price fails, since the asset that provides payoff  $S_T^1$ at time T has a market price  $S_0^1$  and a replication price  $\mathbb{E}^{\mathbb{P}}[S_T^1] < S_0^1$ . Therefore, if the law of one price is to be valid in the market, one has to insist on existence of an equivalent (true) martingale measure  $\mathbb{Q}$ , where each discounted process  $\beta S^i$  is a *true* (and not only local)  $\mathbb{Q}$ -martingale for all  $i = 0, \ldots, d$ . For pricing purposes then, it makes sense to ask that the stochastic discount factor  $Y^{\kappa}$  that is chosen according to Theorem 3 is such that  $Y^{\kappa} S^{i}$  is a true  $\mathbb{P}$ -martingale for all  $i = 0, \ldots, d$ . Such stochastic discount factors give rise to probabilities  $\mathbb{Q}^{\kappa}$  that make all deflated asset-price-process  $\mathbb{O}^{\kappa}$ -martingales and can be used as pricing measures.

Let us now specialize to the important "diffusion" case where  $r_t = r \in \mathbb{R}$  for all  $t \in [0, T]$  and  $\sigma_t =$  $\eta(t, S_t)$  for all  $t \in [0, T]$ , where  $\eta$  is a nice function with values in the space of  $(m \times d)$ -matrices. As long as a claim written only on the traded assets is concerned, the choice of  $\mathbb{Q}^{\kappa}$  for pricing is irrelevant, since the asset prices under  $\mathbb{Q}^{\kappa}$  have dynamics

$$\frac{\mathrm{d}S_t^i}{S_t^i} = r_t \mathrm{d}t + \langle \sigma_t^{\cdot i}, \mathrm{d}W_t^\kappa \rangle,$$
  
$$\forall t \in [0, T], \quad i = 1, \dots, d \qquad (22)$$

where  $W^{\kappa}$  is a  $\mathbb{Q}^{\kappa}$ -Brownian motion. However, if one is interested in pricing a claim written on a nontraded asset whose price process Z has  $\mathbb{P}$ -dynamics

$$dZ_t = a_t dt + \langle f_t, dW_t \rangle, \quad t \in [0, T]$$
 (23)

for **F**-adapted *a* and  $f = (f^1, \ldots, f^m)$ , then the  $\mathbb{Q}^{\kappa}$ dynamics of  $Z$  are

$$dZ_{t} = (a_{t} - \langle f_{t}, \lambda_{t}^{*} \rangle - \langle f_{t}, \kappa_{t} \rangle) dt + \langle f_{t}, dW_{t}^{\kappa} \rangle,$$
  
$$\forall t \in [0, T]$$
(24)

The dynamics of  $Z$  will be independent of the choice of  $\kappa$  only if the volatility structure of the process Z, given by f, is in the range of  $\sigma^{\top}$ . This will mean that  $\langle f, \kappa \rangle = 0$  for all  $\kappa$  such that  $\sigma^{\top} \kappa = 0$  and that  $Z$  is perfectly replicable using the traded assets. As long as there is any randomness in the movement in  $Z$  that cannot be captured by investing in the traded assets, that is, if there exists some  $\kappa$  with  $\sigma^{\top}\kappa = 0$ and  $\langle f, \kappa \rangle$  not being identically zero, perfect replicability fails and pricing becomes a more complicated issue, depending on the preferences of the particular agent as given by the choice of  $\kappa$  to form the stochastic discount factor.

## **End Notes**

<sup>a.</sup>One can impose natural conditions on preference relations defined on the set of all possible outcomes that will lead to numerical representation of the preference relationship via expected utility maximization. This was axiomatized in [10]—see also Chapter 2 of [5] for a nice exposition.

<sup>b.</sup>We stress "infinitesimal" because when the portfolio holdings of the agent change, the indifference prices also change; thus, for large sales or buys that will considerably change the portfolio structure, there might appear an incentive, that was not there before, to sell or buy the asset. <sup>c.</sup>For this reason, utility indifference prices are sometimes referred to as *Davis prices*.

<sup>d</sup> Free lunches with vanishing risk is the suitable generalization of the notion of arbitrages to get a version of the fundamental theorem of asset pricing in continuous time. The reader is referred to  $[3]$ .

<sup>e.</sup>The inequality follows because positive local martingales are supermartingales—see, for example, [7].

#### References

- Cochrane, J.H. (2001). Asset Pricing, Princeton Univer- $[1]$ sity Press.
- Davis, M.H.A. (1997). Option pricing in incomplete [2] markets, in Mathematics of Derivative Securities (Cambridge, 1995), Publications of the Newton Institute, Cambridge University Press, Cambridge, Vol. 15, pp. 216-226.
- [3] Delbaen, F. & Schachermayer, W. (2006). The Mathematics of Arbitrage, Springer Finance, Springer-Verlag, Berlin.
- [4] Elworthy, K.D. & Li, X.-M. & Yor, M. (1999). The importance of strictly local martingales; applications to radial Ornstein-Uhlenbeck processes, Probability Theory and Related Fields 115, 325-355.
- [5] Föllmer, H. & Schied, A. (2004). Stochastic Finance, extended Edition, de Gruyter Studies in Mathematics, Walter de Gruyter & Co., Berlin, Vol. 27.
- [6] Karatzas, I. & Kardaras, C. (2007). The numéraire portfolio in semimartingale financial models, Finance and Stochastics 11, 447-493.
- Karatzas, I. & Shreve, S.E. (1991). Brownian Motion [7] and Stochastic Calculus, 2nd Edition, Graduate Texts in Mathematics, Springer-Verlag, New York, Vol. 113.
- [8] Karatzas, I. & Shreve, S.E. (1998). Methods of Mathematical Finance, Applications of Mathematics (New York), Springer-Verlag, New York, Vol. 39.
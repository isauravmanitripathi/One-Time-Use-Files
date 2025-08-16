# **Lattice Methods for Path-dependent Options**

Path-dependent options are options whose payoffs depend on some specific function  $F$  of the entire trajectory of the asset price  $F_t = F(t, (S_u)_{u \le t})$ . The most well-known examples are the lookback options and Asian options. In a lookback option, the payoff function is dependent on the realized maximum or minimum price of the asset over a certain period within the life of the option. The Asian options are also called *average options* since the payoff depends on a prespecified form of averaging of the asset price over a certain period. Consider an arithmetic average Asian option that is issued at time  $0$  and expiring at  $T > 0$ , its terminal payoff is dependent on the arithmetic average  $A_T$  of the asset price process  $S_t$ over period [0, T]. The running average value  $A_t$  is defined as

$$A_t = \frac{1}{t} \int_0^t S_u \, \mathrm{d}u \tag{1}$$

with  $A_0 = S_0$ . We are interested in the correlated evolution of the path function with the asset price process. In the above example of arithmetic averaging, the law of evolution of  $A_t$  is given as

$$dA_t = \frac{1}{t}(S_t - A_t) dt$$
 (2)

A variant of the lattice tree methods (binomial/trinomial methods), called the *forward shooting* grid (FSG) approach, has been successfully applied to price a wide range of strong path-dependent options, such as the lookback options, Asian options, convertible bonds with reset feature and Parisian feature. reset strike feature in shout options, and so on. The FSG approach is characterized by augmenting an auxiliary state vector at each node in the usual lattice tree, which serves to capture the path-dependent feature of the option. Under the discrete setting of lattice tree calculations, let  $G$  denote the function that describes the correlated evolution of  $F$  with  $S$  over the time step  $\Delta t$ , which can be expressed as

$$F_{t+\Delta t} = G(t, F_t, S_{t+\Delta t}) \tag{3}$$

For example, let  $A^n$  denote the discretely observed arithmetic average defined as

$$A^n = \frac{\sum_{i=0}^n S^i}{n+1} \tag{4}$$

where  $S^i$  is the observed asset price at time  $t_i$ ,  $i =$  $0, 1, \ldots, n$ . The correlated evolution of  $A^{n+1}$  with  $S^{n+1}$  is seen to be

$$A^{n+1} = A^n + \frac{S^{n+1} - A^n}{n+2} \tag{5}$$

Another example is provided by the correlated evolution of the realized maximum price  $M_t$  and its underlying asset price process  $S_t$ . Recall  $M_t =$  $\max S_u$  so that  $0 \leq u \leq t$ 

$$M_{t+\Delta t} = \max(M_t, S_{t+\Delta t}) \tag{6}$$

In the construction of the auxiliary state vector, it is necessary to know the number of possible values that can be taken by the path-dependent state variable. For the lookback feature, the realized maximum asset price is necessarily one of the values taken by the asset price in the lattice tree. However, the number of possible values for the arithmetic average grows exponentially with the number of time steps. To circumvent the problem of dealing with exceedingly large number of nodal values, the state vector is constructed such that it contains a set of predetermined nodal values that cover the range of possible values of arithmetic averaging. Since the realized arithmetic average does not fall on these nodal values in general, we apply interpolation between the nodal values as an approximation.

The FSG approach is pioneered by Hull and White [4] and Ritchken et al. [10] for pricing American and European style Asian and lookback options. Theoretical studies on the construction and convergence analysis of the FSG schemes are presented by Barraquand and Pudet [1], Forsyth et al. [3], and Jiang and Dai [5]. A list of various applications of the FSG approach in lattice tree algorithms for pricing strongly path-dependent options/derivative products is given as follows:

- options whose underlying asset price follows various kinds of GARCH processes [11];
- path-dependent interest rate claims [9];  $\bullet$
- Parisian options, alpha-quantile options, and strike . reset options  $[6]$ ;

#### 2 **Lattice Methods for Path-dependent Options**

- soft call requirement in convertible bonds [7]; ٠
- target redemption notes [2]; and
- employee stock options with repricing features [8]

In this article, we illustrate the application of the FSG lattice tree algorithms for pricing options with path-dependent lookback and Asian features, convertible bonds with the soft call requirement (Parisian feature), and call options with the strike reset feature.

### **Lookback Options**

Let the risk neutral probabilities of upward, zero, and downward jump in a trinomial tree be represented by  $p_u$ ,  $p_0$ , and  $p_d$ , respectively. In the FSG approach for capturing the path dependence of the discrete asset price process, we append an augmented state vector at each node in the trinomial tree and determine the appropriate grid function that models the discrete correlated evolution of the path dependence. Let  $V_{i,k}^n$  denote the numerical option value of the path-dependent option at the  $n$ th-time level and  $i$  upward jumps from the initial asset value  $S_0$ . Here, k denotes the numbering index for the values assumed by the augmented state vector at the  $(n, j)$ th node in the trinomial tree. Let u and  $d$  denote the proportional upward and downward jump of the asset price over one time step  $\Delta t$ , with  $ud = 1$ . Let  $g(k, j)$  denote the grid function that characterizes the discrete correlated evolution of the path-dependent state variable  $F_t$  and asset price process  $S_t$ . When applied to the trinomial tree calculations, the FSG scheme takes the following form:

$$V_{j,k}^{n} = e^{-r\Delta t} \left[ p_u V_{j+1,g(k,j+1)}^{n+1} + p_0 V_{j,g(k,j)}^{n+1} + p_d V_{j-1,g(k,j-1)}^{n+1} \right]$$
(7)

where  $e^{-r\Delta t}$  denotes the discount factor over one time step (Figure 1).

We consider the floating strike lookback option whose terminal payoff depends on the realized maximum of the asset price, namely,  $V(S_T, M_T, T) =$  $M_T - S_T$ . The corresponding discrete analogy of the correlated evolution of  $M_t$  and  $S_t$  is given by the following grid function (equation 6):

$$g(k, j) = \max(k, j) \tag{8}$$

![](_page_1_Figure_11.jpeg)

Figure 1 The discrete correlated evolution of the pathdependent state variable  $F_t$  and asset price process  $S_t$  is characterized by the grid function  $g(k, j)$ 

As in usual trinomial calculations, we apply the backward induction procedure, starting with the lattice nodes at maturity. Suppose that there are a total of  $N$  time steps in the trinomial tree so that the maximum value of the discrete asset price process is  $S_0 u^N$ , corresponding to N successive jumps from the initial value  $S_0$ . The possible range for realized maximum asset price would be  $\{S_0, S_0u, \ldots, S_0u^N\}$ . When these possible values of the path-dependent state variable are indexed by  $k$ , then  $k$  assumes values from  $0, 1, \ldots$ , to N. The terminal option value at the  $(N, j)$ th node and kth value in the state vector is given as

$$V_{j,k}^{N} = S_{0}u^{k} - S_{0}u^{j},$$
  

$$j = -N, -N + 1, ..., N \text{ and}$$
  

$$k = \max(j, 0), \max(j, 0) + 1, ..., N \quad (9)$$

Applying backward induction over one time step from expiry, the option values at the  $(N-1)$ th time level are given as

$$V_{j,k}^{N-1} = e^{-r\Delta t} \left[ p_u V_{j+1,\max(k,j+1)}^N + p_0 V_{j,\max(k,j)}^N + p_d V_{j-1,\max(k,j-1)}^N \right]$$
  

$$j = -N + 1, -N + 2, \dots, N - 1,$$
  

$$k = \max(j, 0) + 1, \dots, N - 1 \tag{10}$$

where the terminal option values are defined in equation (9). The backward induction procedure is then repeated to obtain numerical option values at the lattice nodes at earlier time levels. Note that the range of the possible values assumed by the path-dependent state variable narrows as we proceed backward in a stepwise manner until we reach the tip of the trinomial tree.

#### **Asian Options**

Recall that the asset price  $S_i^n$  at the  $(n, j)$ th node in the trinomial tree is given as

$$S_j^n = S_0 u^j = S_0 e^{j\Delta W}, \quad j = -n, -n+1, \dots, n$$
(11)

where  $u = e^{\Delta W}$  with  $\Delta W = \sigma \sqrt{\Delta t}$ . Here,  $\sigma$  is the volatility of the asset price. The average asset price at the *n*th time level must lie between  $\{S_0u^{-n}, S_0u^n\}$ . We take  $\rho < 1$  and let  $\Delta Y = \rho \Delta W$ . Let floor(x) denote the largest integer less than or equal to  $x$ and  $\text{ceil}(x) = \text{floor}(x) + 1$ . We set the possible values taken by the average asset price to be

$$A_k^n = S_0 e^{k\Delta Y}, \quad k = \text{floor}\left(-\frac{n}{\rho}\right), \dots, \text{ceil}\left(\frac{n}{p}\right) \tag{12}$$

The earlier FSG schemes choose  $\rho$  to be a sufficiently small number that is independent of  $\Delta t$ . The larger the value chosen for  $1/\rho$ , the finer the quantification of the average asset price. In view of numerical convergence of the FSG schemes, Forsyth *et al.* [3] propose to choose  $\rho$  to depend on  $\sqrt{\Delta t}$ (say,  $\rho = \lambda \sqrt{\Delta t}$ , where  $\lambda$  is independent of  $\Delta t$ ), though this would result in an excessive amount of computation in actual implementation. Further details on numerical convergence of various versions of the FSG schemes are presented later.

Suppose that the average is  $A_k^n$  and the asset price moves upward from  $S_j^n$  to  $S_{j+1}^{n+1}$ , then the new average is given as (equation  $5$ )

$$A_{k^{+}(j)}^{n+1} = A_k^n + \frac{S_{j+1}^{n+1} - A_k^n}{n+2}$$
(13)

Next, we set  $A_{k^+(j)}^{n+1}$  to be  $S_0e^{k^+(j)\Delta Y}$  for some value  $k^+(i)$ , that is,

$$k^{+}(j) = \frac{\ln A_{k^{+}(j)}^{n+1}/S_0}{\Delta Y} \tag{14}$$

Note that  $k^+(j)$  is not an integer in general, so  $A_{k^+(i)}^{n+1}$  does not fall onto one of the preset values for the average. Recall that floor( $k^+(j)$ ) is the largest integer less than or equal to  $k^+(i)$ and  $\text{ceil}(k^+(j)) = \text{floor}(k^+(j)) + 1$ . By the above construction,  $A_{\text{floor}(k^+(j))}^{n+1}$  and  $A_{\text{ceil}(k^+(j))}^{n+1}$  now fall onto the set of preset values. Similarly, we define

$$A_{k^{-}(j)}^{n+1} = A_k^n + \frac{S_{j-1}^{n+1} - A_k^n}{n+2}$$
  
$$A_{k^{0}(j)}^{n+1} = A_k^n + \frac{S_j^{n+1} - A_k^n}{n+2}$$
 (15)

corresponding to the new average at the  $(n +$ 1)th time level when the asset price experiences a downward jump and zero jump, respectively. In addition, floor $(k^-(j))$ , ceil $(k^-(j))$ , floor $(k^0(j))$ , and  $\text{ceil}(k^0(j))$  are obtained in a similar manner.

Let  $V_{i,k^+(i)}^n$  denote the Asian option value at node  $(n, j)$  with the averaging state variable  $A_t$ assuming the value  $A_{k^+(j)}^n$ , and assuming similar notation for  $V_{j,\text{floor}(k^+(j))}^n$ , and so on. In the lattice tree calculations, numerical option values for  $V_{i k}^{n}$  are obtained only for the case when  $k$  is an integer. Since  $k^+(j)$  assumes a noninteger value in general,  $V_{i,k^+(j)}^n$ is approximated through interpolation using option values at the neighboring nodes. Suppose that linear interpolation is adopted; we approximate  $V_{i,k^+(i)}^n$  by the following interpolation formula:

$$V_{j,k^{+}(j)}^{n} = \epsilon_{j,k}^{+} V_{j,\text{ceil}(k^{+}(j))}^{n} + (1 - \epsilon_{j,k}^{+}) V_{j,\text{floor}(k^{+}(j))}^{n}$$
(16)

where

$$\epsilon_{j,k}^{+} = \frac{\ln A_{k^{+}(j)}^{n} - \ln A_{\text{floor}(k^{+}(j))}^{n}}{\Delta Y} \tag{17}$$

The FSG algorithm with linear interpolation for pricing an Asian option can be formulated as follows (Figure  $2$ ):

$$V_{j,k}^{n} = e^{-r\Delta t} \left( p_{u} V_{j,k^{+}(j)}^{n+1} + p_{0} V_{j,k^{0}(j)}^{n+1} + p_{d} V_{j,k^{-}(j)}^{n+1} \right)$$
  

$$= e^{-r\Delta t} \left\{ p_{u} \left[ \epsilon_{j,k}^{+} V_{j,\text{ceil}(k^{+}(j))}^{n+1} + (1 - \epsilon_{j,k}^{+}) V_{j,\text{floor}(k^{+}(j))}^{n+1} \right] + p_{0} \left[ \epsilon_{j,k}^{0} V_{j,\text{ceil}(k^{0}(j))}^{n+1} + (1 - \epsilon_{j,k}^{0}) V_{j,\text{floor}(k^{0}(j))}^{n+1} \right] + p_{d} \left[ \epsilon_{j,k}^{-} V_{j,\text{ceil}(k^{-}(j))}^{n+1} + (1 - \epsilon_{j,k}^{-}) V_{j,\text{floor}(k^{-}(j))}^{n+1} \right] \right\}$$
(18)

![](_page_3_Figure_1.jpeg)

**Figure 2** The average value  $A_k^n$  at the *n*th time step changes to  $A_{k^+(i)}^{n+1}$  at the  $(n+1)$ th time step upon an upward move of the asset price from  $S_j^n$  to  $S_{j+1}^{n+1}$ . The option value at node  $(n + 1, j + 1)$  with asset price average  $A_{k+(j)}^n$  is approximated by linear interpolation between the option values with asset price average  $A_{\text{floor}(k^+(j))}^{n+1}$  and  $A_{\text{ceil}(k^+(j))}^{n+1}$ 

#### Numerical Convergence of FSG Schemes

Besides linear interpolation between two neighboring nodal values, other forms of interpolation can be adopted (say, quadratic interpolation between 3 neighboring nodal values or nearest node point interpolation). Forsyth et al. [3] remark that the FSG algorithm using  $\rho$  that is independent of  $\Delta t$  and the nearest node point interpolation may exhibit large errors as the number of time steps increases. They also prove that this choice of  $\rho$  in the FSG algorithm together with linear interpolation converges to the correct solution plus a constant error term. Unfortunately, the error term cannot be reduced by decreasing the size of the time step. To ensure convergence of the FSG calculations to the true Asian option price, they propose to use  $\rho$  that depends on  $\sqrt{\Delta t}$ , though this would lead to a large number of nodes in the averaging direction. More precisely, if  $\rho$  is independent of  $\sqrt{\Delta t}$ , then the complexity of the FSG method is  $O(n^3)$ , but convergence cannot be guaranteed. If we set  $\rho = \lambda \sqrt{\Delta t}$ , which guarantees convergence, then the complexity becomes  $O(n^{7/2})$ .

## Soft Call Requirement in Callable **Convertible Bonds**

Most convertible bonds contain the call provision that allows the issuer to have the flexibility to manage the debt-equity ratio in the company's capital structure. To protect the conversion premium paid upfront by the bondholders to be called away too soon, the bond indenture commonly contains the hard call protection clause that prevents the issuer from initiating a call during the early life of the convertible bond. In addition, the soft call clause further requires the stock price to stay above the trigger price (typically 30% higher than the conversion price) for a consecutive or cumulative period before initiation of issuer's call. The purpose of the soft call clause is to minimize the potential of market manipulation by the issuer.

The path-dependent feature that models the phenomenon of the asset price staying above some threshold level for a certain period of time is commonly called the *Parisian feature*. Let  $B$  denote the trigger price and the "Parisian" clock starts counting (cumulatively or consecutively) when the asset price stays above  $B$ . In the discrete trinomial evolution of the asset price, we construct the grid function  $g_{\text{cum}}(k, j)$  that models the correlated evolution of the discrete asset price process and the cumulative counting of the number of time steps that  $S_i \geq B$ . Given that  $k$  is the cumulative counting of the number of time steps that the asset price has been staying above B, the index k increases its value by 1 when  $S_i \geq B$ . Then we have

$$g_{\text{cum}}(k, j) = k + \mathbf{1}_{\{S_j \ge B\}} \tag{19}$$

where  $\mathbf{1}_{\{S_i \geq B\}}$  denotes the indicator function associated with the event  $\{S_i \geq B\}$ . In a similar manner, the grid function  $g_{\text{con}}(k, j)$  that models the consecutive counting of the number of time steps that  $S_i \geq B$  is defined as

$$g_{\text{con}}(k,j) = (k+1)\mathbf{1}_{\{S_j \ge B\}} \tag{20}$$

Using the FSG approach, the path dependence of the soft call requirement can be easily incorporated into the pricing algorithm for a convertible bond with call provision [7]. Suppose that the number of cumulative time steps required for activation of the call provision is  $K$ ; then the dynamic programming procedure that enforces the interaction of the game option of holder's optimal conversion and issuer's optimal call is applied at a given lattice grid only when the condition  $g_{\text{cum}}(k, j) \geq K$  is satisfied.

# **Call Options with Strike Reset Feature**

Consider a call option with strike reset feature where the option's strike price is reset to the prevailing asset price on a preset reset date if the option is out of the money on that date. Let  $t_i$ ,  $i = 1, 2, \ldots, M$ , denote

the reset dates and  $X_i$  denote the strike price specified on  $t_i$  based on the above reset rule. Write  $X_0$  as the strike price set at initiation; then,  $X_i$  is given as

$$X_i = \min(X_0, X_{i-1}, S_{t_i}) \tag{21}$$

where  $S_{t_i}$  is the prevailing asset price at reset date  $t_i$ . Note that the strike price at expiry of this call option is not fixed since its value depends on the realization of the asset price at the reset dates. When we apply the backward induction procedure in the trinomial calculations, we encounter the difficulty in defining the terminal payoff since the strike price is not yet known. These difficulties can be resolved easily using the FSG approach by tracking the evolution of the asset price and the reset strike price through an appropriate choice of the grid function [6].

Recall that  $S_0$  is the asset price at the tip of the trinomial tree and the asset price after  $j$  net upward jumps is  $S_0 u^j$ . In our notation, the index k is used as the one-to-one correspondence to the asset price level  $S_0u^k$ . Say, suppose that the original strike price  $X_0$ corresponds to the index  $k_0$ , this would mean  $X_0 =$  $S_0 u^{k_0}$ . For convenience, we may choose the proportional jump parameter  $u$  such that  $k_0$  is an integer. In terms of these indexes, the grid function that models the correlated evolution between the reset strike price and asset price is given as (see equation  $21$ )

$$g_{\text{reset}}(k, j) = \min(k, j, k_0) \tag{22}$$

where  $k$  denotes the index that corresponds to the strike price reset in the last reset date and  $j$  is the index that corresponds to the prevailing asset price at the reset date.

Since the strike price is reset only on a reset date, we perform the usual trinomial calculations for those time levels that do not correspond to a reset date while the augmented state vector of strike prices are adjusted according to the grid function  $g_{reset}(k, j)$  for those time levels that correspond to a reset date. The FGS algorithm for pricing the reset call option is given as

$$V_{j,k}^{n} = \begin{cases} p_u V_{j+1,k}^{n+1} + p_0 V_{j,k}^{n+1} + p_d V_{j-1,k}^{n+1} \\ \text{if } (n+1)\Delta t \neq t_i \text{ for some } i \end{cases}$$
$$p_u V_{j+1,g_{\text{reset}}(k,j+1)}^{n+1} + p_0 V_{j,g_{\text{reset}}(k,j)}^{n+1} \\ + p_d V_{j-1,g_{\text{reset}}(k,j-1)}^{n+1} \\ \text{if } (n+1)\Delta t = t_i \text{ for some } i \end{cases}$$
(23)

Lastly, the payoff values along the terminal nodes at the  $N$ th time level in the trinomial tree are given as

$$V_{j,k}^{N} = \max(S_0 u^j - S_0 u^k, 0),$$
  

$$j = -N, -N + 1, \dots, N$$
(24)

and k assumes values that are taken by j and  $k_0$ .

#### References

- Barraquand, J. & Pudet, T. (1996). Pricing of Amer-[1] ican path-dependent contingent claims, Mathematical Finance 6, 17-51.
- [2] Chu, C.C. & Kwok, Y.K. (2007). Target redemption note, Journal of Futures Markets 27, 535-554.
- [3] Forsyth, P., Vetzal, K.R. & Zvan, R. (2002). Convergence of numerical methods for valuing pathdependent options using interpolation, Review of Derivatives Research 5, 273-314.
- Hull, J. & White, A. (1993). Efficient procedures for [4] valuing European and American path dependent options, *Journal of Derivatives*  $1$ (Fall), 21–31.
- Jiang, L. & Dai, M. (2004). Convergence of bino-[5] mial tree method for European/American path-dependent options, SIAM Journal of Numerical Analysis 42(3), 1094-1109.
- Kwok, Y.K. & Lau, K.W. (2001). Pricing algorithms [6] for options with exotic path dependence, Journal of Derivatives 9, 28-38.
- Lau, K.W. & Kwok, Y.K. (2004). Anatomy of option [7] features in convertible bonds, Journal of Futures Markets 24(6), 513-532.
- Leung, K.S. & Kwok, Y.K. (2008). Employee stock [8] option valuation with repricing features, Quantitative *Finance*, to appear.
- [9] Ritchken, P. & Chuang, I. (2000). Interest rate option pricing with volatility humps, Review of Derivatives Research 3, 237-262.
- [10] Ritchken, P.L., Sankarasubramanian, L. & Vijh, A.M.  $(1993)$ . The valuation of path dependent contract on the average, Management Science 39, 1202-1213.
- $[11]$ Ritchken, P. & Trevor, R. (1999). Pricing option under generalized GARCH and stochastic volatility processes, Journal of Finance 54(1), 377-402.

#### **Related Articles**

Asian Options; Binomial Tree; Convertible Bonds; Lookback Options; Quantization Methods; Tree Methods.

YUE-KUEN KWOK
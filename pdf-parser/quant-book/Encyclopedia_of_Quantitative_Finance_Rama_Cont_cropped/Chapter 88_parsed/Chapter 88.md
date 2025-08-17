# **Binomial Tree**

This model, introduced by Cox *et al.* [1] in 1979, has played a decisive role in the development of the derivatives industry. Its simple structure and easy implementation gave analysts the ability to price a huge range of financial derivatives in an almost routine way. Nowadays its value is largely pedagogical, in that the whole theory of arbitrage pricing in complete markets can be explained in a couple of pages in the context of the binomial model. The model is covered in every mathematical finance textbook, but we mention in particular [4], which is entirely devoted to the binomial model, and [2] for a careful treatment of American options.

## **The One-period Model**

Suppose we have an asset whose price is *S* today and whose price tomorrow can only be one of two known values *S*0, *S*<sup>1</sup> (we take *S*<sup>0</sup> *> S*1); see Figure 1. This apparently highly artificial situation is the kernel of the binomial model. We also suppose there is a bank account paying a daily rate of interest *r*1, so that \$1 today is worth \$*R* = \$*(*1 + *r*1*)* tomorrow. We assume that borrowing is possible from the bank at the same rate of interest *r*1, and that the risky asset can also be borrowed (sold short, in the usual financial terminology). The only other assumption is that

$$S_1 < RS < S_0 \tag{1}$$

If *RS* ≤ *S*1, we could borrow \$*B* from the bank and buy *B/S* shares of the risky asset. Tomorrow these will be worth at least *S*1*B/S*, while only *RB* has to be repaid to the bank, leaving a profit of either *B(S*<sup>1</sup> − *RS)/S* or *B(S*<sup>0</sup> − *RS)/S*.Both of these are nonnegative and at least one is strictly positive. This is an *arbitrage opportunity*: no initial investment, no loss and the chance of a positive profit at the end

![](_page_0_Figure_6.jpeg)

**Figure 1** One-period binomial tree

(*see* **Arbitrage Strategy**). There is also an arbitrage opportunity if *RS > S*0, realized by short-selling the risky asset.

A *derivative security*, *contingent claim*, or *option* is a contract that pays tomorrow an amount that depends only on tomorrow's asset price. Thus any such claim can only have values, say *O*<sup>0</sup> and *O*<sup>1</sup> corresponding to "underlying" prices *S*0, *S*1, as shown in Figure 1.

Suppose we form a portfolio today consisting of *N* shares of the risky asset and \$*B* in the bank (either of both of *N*, *B* could be negative). The value today of this portfolio is *p* = *B* + *NS* and its value tomorrow will be *RB* + *NS*<sup>0</sup> or *RB* + *NS*1. Now choose *B*, *N* such that

$$RB + NS_0 = O_0$$
  
$$RB + NS_1 = O_1$$
 (2)

There is a unique solution as long as *S*<sup>1</sup> -= *S*0, given by

$$N^* = \frac{O_0 - O_1}{S_0 - S_1}, \quad B^* = \frac{1}{R}(O_0 - NS_0) \quad (3)$$

With these choices, the portfolio value tomorrow exactly coincides with the derivative security payoff, whichever way the price moves. If the derivative security is offered today for any price other than *p* = *RB*<sup>∗</sup> + *N*<sup>∗</sup> there is an arbitrage opportunity (realized by "borrowing the portfolio" and buying the option or conversely). Thus "arbitrage pricing" reduces to the solution of a pair of simultaneous linear equations.

It is easily checked that *p* = *(q*0*O*<sup>0</sup> + *q*1*O*1*)/R* where

$$q_0 = \frac{RS - S_1}{S_0 - S_1}, \quad q_1 = \frac{S_0 - RS}{S_0 - S_1} \tag{4}$$

We see that *q*0*, q*<sup>1</sup> depend only on the underlying market parameters, not on *O*<sup>0</sup> or *O*1, that *q*<sup>0</sup> + *q*<sup>1</sup> = 1 and that *q*0*, q*<sup>1</sup> *>* 0 if and only if the no-arbitrage condition (1) holds. Thus under this condition *q*0*, q*<sup>1</sup> define a probability measure *Q* and we can write the price of the derivative as

$$p = E_{\mathcal{Q}}\left(\frac{1}{R}O\right) \tag{5}$$

Note that  $Q$ , the so-called *risk-neutral* measure, emerges from the "no-arbitrage" argument. We said nothing in formulating the model about the probability of an upward or downward move and the above argument does not imply that this probability has to be given by  $O$ . A further feature of  $O$  is that if we compute the expected price tomorrow under  $Q$  we find that

$$S = \frac{1}{R}(q_0 S_0 + q_1 S_1) \tag{6}$$

showing that the discounted price process is a  $O$ martingale. This is summarized as follows:

- Under condition  $(1)$  there is a unique arbitragefree price for the contingent claim.
- Condition  $(1)$  is equivalent to the existence of a unique probability measure  $O$  under which the discounted asset price is a martingale.
- The contingent claim value is obtained by computing the discounted expectation of its exercise value with respect to a certain probability measure  $Q$ .

Much of the classic theory of mathematical finance (see Fundamental Theorem of Asset Pricing; Risk**neutral Pricing**) is concerned with identifying conditions under which these three statements hold for the more general price models. They hold in particular for the multiperiod models discussed below.

## The Multiperiod Model

More realistic models can be obtained by generalizing the binomial model to  $n$  periods. We consider a discrete-time price process  $S(i)$ ,  $i = 0, \ldots, n$  such that, at each time i,  $S(i)$  takes one of  $i + 1$  values  $S_{i0} > S_{i1} > \ldots > S_{ii}$ . While we could consider general values for these constants, the most useful case is that in which the price moves "up" by a factor  $u$  or "down" by a factor  $d = 1/u$ , giving a recombining<br>tree with  $S_{ij} = Su^{i-2j}$  where  $S = S(0)$ ; see Figure 2 for the two-period case. We can define a probability measure Q by specifying that  $P[S(i + 1)] =$  $uS(i)|S(i)| = q_0$  and  $P[S(i + 1) = dS(i)|S(i)] = q_1$ where  $q_0$  and  $q_1$  are given by equation (4) above; in this case,  $q_0 = (Ru - 1)/(u^2 - 1), q_1 = 1 - q_0.$ Thus  $S(i)$  is a discrete-time Markov process under  $Q$  with homogeneous transition probabilities. Specifically, it is a *multiplicative random walk* in that each

![](_page_1_Figure_10.jpeg)

Figure 2 Two-period binomial tree

successive value is obtained from the previous one by multiplication by an independent positive random factor.

Consider the two-period case of Figure 2 and a contingent claim with exercise value  $O$  at time 2 where  $O = O_0$ ,  $O_1$ ,  $O_2$  in the three states as shown. By the one-period argument, the no-arbitrage price for the claim at time 1 is  $v_{1,0} = (q_0 O_0 + q_1 O_1)/R$  if the price is  $uS$  and  $v_{1,1} = (q_0O_1 + q_1O_2)/R$  if the price is dS. However, now our contingent claim is equivalent to a one-period claim with payoff  $v_{1,0}$ ,  $v_{1,1}$ , so its value at time 0 is just  $(q_0v_{1,0} + q_1v_{1,1})/R$ , which is equal to

$$v_{0,0} = E_{\mathcal{Q}} \left[ \frac{1}{R^2} O \right] \tag{7}$$

Generalizing to  $n$  periods and a claim that pays amounts  $O_0, \ldots, O_n$  at time n, the value at time 0 is

$$v_{0,0} = E_Q \left[ \frac{1}{R^n} O \right] = \frac{1}{R_n} \sum_{j=0}^n C_j^n q_0^{n-j} q_1^j O_j \qquad (8)$$

where  $C_i^n$  is the binomial coefficient  $C_i^n = n!/j!$  $(n - j)!$ . From equation (3) the initial hedge ratio (the number  $N$  of shares is the hedging portfolio at  $time 0) is$ 

$$N = \frac{v_{1,0} - v_{1,1}}{uS - dS}$$
  
=  $\frac{1}{SR^{n-1}(u - d)} \sum_{j=0}^{n-1} C_j^{n-1} q_0^{j} (O_j - O_{j+1})$  (9)

For example, suppose  $S = 100$ ,  $R = 1.001$ ,  $u =$ 1.04,  $n = 25$ , and O is a call option with strike  $K =$ 100, so that  $O_j = [Su^{n-2j} - K]^+$ . The option value is  $v_{0.0} = 9.086$  and  $N = 0.588$ . The initial holding in the bank is therefore  $v_{0.0} - NS = -49.72$ . This is the typical situation: hedging involves leverage (borrowing from the bank to invest in shares).

#### Scaling the Binomial Model

Now let us consider scaling the binomial model to a continuous limit. Take a fixed time horizon T and think of the price  $S(i)$  above, now written  $S_n(i)$ , as the price at time  $iT/n = i\Delta t$ . Suppose the continuously compounding rate of interest is  $r$ , so that  $R = e^{r\Delta t}$ . Finally, define  $h = \log u$  and  $X(i) =$  $\log(S(i)/S(0))$ ; then  $X(i)$  is a random walk on the lattice  $\{\ldots -2h, -h, 0, h, \ldots\}$  with right and left probabilities  $q_0$ ,  $q_1$  as defined earlier and  $X(0) = 0$ . If we now take  $h = \sigma \sqrt{\Delta t}$  for some constant  $\sigma$ , we find that

$$q_0, q_1 = \frac{1}{2} \pm \frac{h}{2\sigma^2} \left( r - \frac{1}{2}\sigma^2 \right) + O(h^2) \qquad (10)$$

Thus  $Z(i) := X(i) - X(i-1)$  are independent random variables with

$$EZ(i) = \frac{h^2}{\sigma^2} \left( r - \frac{1}{2}\sigma^2 \right) + O(h^3)$$
$$= \left( r - \frac{1}{2}\sigma^2 \right) \Delta t + O(n^{-3/2}) \quad (11)$$

and

$$\operatorname{var}(Z(i)) = \sigma^2 \Delta t + O(n^{-2}) \tag{12}$$

Hence  $X_n(T) := X(n) = \sum_{i=1}^n Z(i)$  has mean  $\mu_n$ and variance  $V_n$  such that  $\overline{\mu_n} \rightarrow (r - \sigma^2/2)T$  and  $V_n \to \sigma^2 T$  as  $n \to \infty$ . By the central limit theorem, the distribution of  $X_n(T)$  converges weakly to the normal distribution with the limiting mean and variance. If the contingent claim payoff is a continuous bounded function  $O = h(S_n(n))$ , then the option value converges to a normal expectation that can be written as

$$V_0(S) = \frac{e^{-rT}}{\sqrt{2\pi}} \int_{-1}^1 h\left(S \exp\left(r - \frac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}x\right) e^{-\frac{1}{2}x^2} \mathrm{d}x \tag{13}$$

This is the Black-Scholes formula. It can be given in more explicit terms when, for example,  $h(S) = [S - K]^+$ , the standard call option (see Black-Scholes Formula).

#### **American Options**

In the multiperiod binomial model, the basic computational step is the backward recursion

$$v_{i-1,j} = \frac{1}{R}(q_0 v_{i,j} + q_1 v_{i,j+1}) \tag{14}$$

defining the values at time step  $i - 1$  from those at time  $i$  by discounted conditional expectation, starting with the exercise values  $v_{n,j} = O_j$  at the final time  $n$ . In an American option, we have the right to exercise at any time, the exercise value at time  $i$  being some given function  $h(i, S_i)$ , for example,  $h(i, S_i) =$  $[K-S_i]^+$  for an American put. The exercise value at node  $(i, j)$  in the binomial tree is therefore  $\tilde{h}(i, j) =$  $h(i, Su^{i-2j})$ . In this case, it is natural to replace equation  $(14)$  by

$$v_{i-1,j} = \max\{v_{k-1,j}^c, h(i-1,j)\}\tag{15}$$

where  $v_{i-1,i}^c$  is given by the right-hand side of equation (14). At each node  $(i - 1, j)$ , we compare the "continuation value"  $v_{i-1,j}^c$  with the "immediate exercise" value  $\tilde{h}(i-1, j)$  and take the larger value. This intuition is correct, and the value  $v_{0,0}$  obtained by applying equation (15) for  $i = n, n - 1, \ldots, 1$ with starting condition  $v_{n,j} = \hat{h}(n, j)$  is the unique arbitrage-free value of the American option at time 0.

The reader should refer to American Options for a complete treatment, but, in outline, the argument establishing the above claim is as follows. The algorithm divides the set of nodes into two, the stop*ping set*  $S = \{(i, j) : v_{i, j} = \tilde{h}(i, j)\}$  and the complementary *continuation set*  $C$ . By definition,  $(n, j) \in S$ for  $j = 0, \ldots, n$ . Let  $\tau^*$  be the stopping time  $\tau^* =$  $\min\{i: S_i \in \mathcal{S}\}\.$  Then  $\tau^*$  is the optimal time at which the holder of the option should exercise. The process  $V_i = v_{i, S_i}/R^i$  is a supermartingale, while the stopped process  $V_{i \wedge \tau^*}$  is a martingale with the property that  $V_{i \wedge \tau^*} \ge h(i \wedge \tau^*, S_{i \wedge \tau^*})/R^i$ . These facts follow from the general theory of optimal stopping, but are not hard to establish directly in the present case. The value  $V_{i \wedge \tau^*}$  can be replicated by trading in the underlying asset (using the basic hedging strategy (3) derived for the one-period model). It follows that this strategy (call it  $SR$ ) is the *cheapest superreplicating strategy*, that is,  $x = v_{0,0}$  is the minimum capital required to construct a trading strategy with value  $X_i$ at time *i* with the property that  $X_i \ge h(i, S_i)$  for all *i* almost surely. If the seller of the option is paid more than  $v_{0,0}$ , then he or she can put the excess in the bank and employ the trading strategy  $SR$ , which is guaranteed to cover his or her obligation to the buyer whenever he or she chooses to exercise. Conversely, if the seller will accept  $p < v_{0,0}$  for the option then the buyer should short  $SR$ , obtaining an initial value  $v_{0,0}$  of which p is paid to the seller and  $v_{0,0} - p$ placed in (for clarity) a second bank account. The short strategy has value  $-X_i$  and the buyer exercises at  $\tau$ \*, receiving from the seller the exercise value  $h(\tau^*, S_{\tau^*}) = X_{\tau^*},$  which is equal and opposite to the value of the short hedge at  $\tau^*$ . Thus, there is an arbitrage opportunity for one party or the other unless the price is  $v_{0,0}$ .

The impact of the binomial model as introduced by  $\text{Cox } et al.$  [1] is largely due to the fact that the European option pricer can be turned into an American option pricer by a trivial one-line modification of the code. Pricing American options in (essentially) the Black-Scholes model was recognized as a free-boundary problem in partial differential equations (PDE) by McKean [3] in 1965, but the only computational techniques were PDE methods (see Finite Difference Methods for Early Exercise Op**tions**) generally designed for much more complicated problems.

#### **Computations in the Binomial Model**

Nowadays the binomial model is rarely, if ever, used for practical problems, largely because it is comprehensively outperformed by the trinomial tree (see Tree Methods).

First, the form of the tree given above is probably not the best if we want to regard the tree as an approximation to the Black-Scholes model. We see from equation  $(10)$  that the risk-neutral probabilities  $q_0, q_1$  depend on r, so if we want to calibrate the model to the market yield curve we will need timevarying  $q_0, q_1$ . This can be avoided if we write the Black-Scholes model as

$$S_t = F_{0,t} M_t \tag{16}$$

where  $F_{0,t}$  is the forward price quoted at time 0 for exchange at time  $t$  and

$$M_t = \exp\left(\sigma W_t - \frac{1}{2}\sigma^2 t\right) \tag{17}$$

is the exponential martingale with Brownian motion  $W_t$ . See **Black–Scholes Formula** for this representation.  $F_{0,t}$  only depends on the spot price  $S_0$  and the yield curve (and the dividend yield, if any), so the only stochastic modeling required relates to the Brownian motion  $\sigma W_t$ . Here we can use a standard "symmetric random walk" approximation: divide the time interval [0, T] into n intervals of length  $\delta = T/n$ and take a space step of length  $h = \sigma \sqrt{\delta}$ . At each discrete time point, the random walk (denoted  $X_i$ ) takes a step of  $\pm h$  with probability 1/2 each—this is just a binomial tree with equal up and down probabilities. For a single step  $Z = X_i - X_{i-1} = \pm h$  we have  $E[e^Z] = \cosh h$ , so if we define  $\alpha = \log(\cosh h)$  then  $M_i^{(n)} = \exp(X_i - \alpha i)$  is a positive discrete-time martingale with  $E[M_i^{(n)}] = 1$ . It is a standard result that the sequence  $M^{(n)}$  (suitably interpreted) converges weakly to *M* given by equation (17) as  $n \to \infty$ . This gives us a discrete-time model

$$S_i^{(n)} = F_{0,i\delta} M_i^{(n)} \tag{18}$$

such that  $E[S_i^{(n)}] = F_{0,i\delta}$  holds *exactly* at each *i*. At node  $(i, j)$  in the tree the corresponding price is  $F_{0,i\delta} \exp((n-j)h - i\alpha)$ . Essentially, we have replaced the original multiplicative random walk representing the price  $S(t)$  by an additive random walk representing the return process  $\log S(t)$ . The advantages of this are (i) all the yield curve aspects are bundled up in the model-free function  $F$ , and (ii) the stochastic model is "universal" (and very simple).

The decisive drawback of any binomial model is the absolute inflexibility with respect to volatility: it is impossible to maintain a recombining tree while allowing time-varying volatility. This means that the model cannot be calibrated to more than a single option price, making it useless for real pricing applications. The trinomial tree gets around this: we can adjust the local volatility by changing the transition probabilities while maintaining the tree geometry (i.e., the constant spatial step  $h$ ).

## **References**

- [4] Shreve, S.E. (2005). *Stochastic Calculus for Finance, Vol 1: The Binomial Asset Pricing Model*, Springer.
- [1] Cox, J., Ross, S. & Rubinstein, M. (1979). Option pricing, a simplified approach, *Journal of Financial Economics* **7**, 229–263.
- [2] Elliott, R.J. & Kopp, P.E. (2005). *Mathematics of Financial Markets*, 2nd Edition, Springer.
- [3] McKean, H.P. (1965). Appendix to P.A. Samuelson, rational theory of warrant pricing, *Industrial Management Review* **6**, 13–31.
- **Related Articles**

**Black–Scholes Formula**; **Quantization Methods**; **Tree Methods**.

MARK H.A. DAVIS
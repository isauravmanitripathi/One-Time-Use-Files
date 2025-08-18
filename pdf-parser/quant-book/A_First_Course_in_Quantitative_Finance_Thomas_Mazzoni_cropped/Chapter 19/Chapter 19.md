19.1

# Plain Vanilla Fixed-Income Derivatives

The major lesson we have learned so far is that knowledge of the forward curve, as it stands today, is enough to price any of the fixed-income instruments introduced until now. An option on such an instrument, expiring sometime in the future, requires knowledge of the forward curve as it will be at the time of expiry. This adds another level of sophistication to option pricing problems, and as we shall see, increases the complexity considerably.

## The T-Forward Measure

Pricing derivatives on bonds or rates is largely a question of selecting a well suited numéraire and evaluating the conditional expectation of the claim in the associated equivalent martingale measure. We have done that many times before. To be more precise, we chose the bank account  $B(t)$  as a numéraire, and the associated equivalent martingale measure was the risk-neutral measure  $Q$ . We thus obtained the martingale pricing relation

$$\frac{V_t}{B(t)} = E^Q \left[ \frac{V_T}{B(T)} \middle| \mathcal{F}_t \right],\tag{19.1}$$

for an arbitrary T-claim  $V$ . It does not matter if  $V$  is a derivative or a genuine security. We have merely stated this relation in a slightly different form as

$$V_t = E^{\mathcal{Q}} \left[ \frac{B(t)}{B(T)} V_T \middle| \mathcal{F}_t \right] = E^{\mathcal{Q}} \left[ e^{-\int_t^T r(s) ds} V_T \middle| \mathcal{F}_t \right] \tag{19.2}$$

most of the time. If the interest rate  $r(t)$  is deterministic, we can pull the discount factor out of the expectation and we are back in our familiar setting for security markets. Unfortunately, we are now in a stochastic interest rate world and furthermore, we have to assume that  $V$  also depends on  $r$ . This means, we cannot factor the last expectation value in (19.2), because there are covariance contributions between the discount factor and the payoff of the T-claim. There is a surprising twist to this problem. We can eliminate the covariance by choosing another numéraire. Recall that every traded asset with nonnegative price for all times  $t$  can be selected as a numéraire. So let's take the discount bond  $P(t, T)$  and call the associated martingale measure the T-forward measure  $Q_T$ . One then obtains in complete analogy to (19.1)

$$\frac{V_t}{P(t,T)} = E^{Q_T} \left[ \frac{V_T}{P(T,T)} \middle| \mathcal{F}_t \right]. \tag{19.3}$$

#### Plain Vanilla Fixed-Income Derivatives

Recalling that  $P(T, T) = 1$ , we obtain

$$V_t = P(t, T)E^{Q_T}[V_T|\mathcal{F}_t].\tag{19.4}$$

Now the discount factor has moved out of the expectation. Of course there is a price to pay. We have to figure out the dynamics of  $V_t$  under the T-forward measure  $O_T$ .

Let's start with a very simple quantity, the forward price. In a stochastic interest rate framework, the forward price  $F$  at time t of any T-claim V has to be

$$F_t = \frac{V_t}{P(t,T)}.\t(19.5)$$

This can be easily verified by an arbitrage argument, taking into account that  $P(T, T) = 1$ , and therefore  $F_T = V_T$ . But this means that due to (19.4),  $F_t$  is a martingale under  $Q_T$ 

$$F_t = E^{Q_T}[F_T|\mathcal{F}_t].\tag{19.6}$$

Since a martingale is driftless, we can immediately conclude that in a geometric *Brownian* motion setup, the dynamics of  $F_t$  look like

$$dF_t = \sigma F_t dW_t \tag{19.7}$$

under  $Q_T$ . But what about the future price? We learned that future and forward prices coincide, as long as interest rates are deterministic. Now that we have entered the realm of stochastic interest rates, we should take a closer look at this. The future price  $\hat{F}_t$  is a price quoted in the market, which makes entering a future contract on  $V$  at time t costless. It is immediately clear that  $\hat{F}_T = V_T$  has to hold. The future contract is (nearly) continuously resettled, and therefore entering the contract with no upfront payment implies that

$$E^{\mathcal{Q}}\left[\int_{t}^{T} e^{-\int_{t}^{u} r(s)ds} d\hat{F}_{u} \middle| \mathcal{F}_{t}\right] = 0 \tag{19.8}$$

has to hold. Resettlement is done with the help of a margin account. Like the bank account, the margin account is a random process, but it has a very interesting property. Let  $M(t)$  be the discounted value of the margin account. Then the following relation holds

$$M(t) = \int_0^t e^{-\int_0^u r(s)ds} d\hat{F}_u = E^{\mathcal{Q}} \left[ \int_0^T e^{-\int_0^u r(s)ds} d\hat{F}_u \middle| \mathcal{F}_t \right] = E^{\mathcal{Q}} [M(T) | \mathcal{F}_t]. \tag{19.9}$$

**Quick calculation 19.1** Use  $(19.8)$  to prove the second equality.

The margin account only changes if the future price changes and hence, if  $M(t)$  is a *Q*-martingale, so is  $\hat{F}_t$ . We thus conclude that

$$\hat{F}_t = E^{\mathcal{Q}}[\hat{F}_T | \mathcal{F}_t] \tag{19.10}$$

has to hold. But because  $\hat{F}_T = F_T = V_T$ , future and forward prices cannot coincide. They are conditional expectations of the same quantity under different probability measures.

Let's analyze an S bond under the T-forward measure for  $t \le T < S$ . To keep things simple, we choose the discount bond. Then we have

$$\frac{P(t,S)}{P(t,T)} = E^{\mathcal{Q}_T}[P(T,S)|\mathcal{F}_t].\tag{19.11}$$

Let us rewrite this expression in terms of the respective forward rates to obtain

$$e^{-\int_T^S f(t,s)ds} = E^{\mathcal{Q}_T} \left[ e^{-\int_T^S f(T,s)ds} \Big| \mathcal{F}_t \right]. \tag{19.12}$$

We might thus suspect that the forward rate itself, or at least one of them, is a  $Q_T$ martingale. To elaborate this hypothesis, we need to learn something about the relation of the measures O and  $O_T$ . Remember that the *Girsanov*-theorem expressed the relation between the physical measure  $P$  and the risk-neutral measure  $Q$  with the help of the *Radon–Nikodym*-derivative  $\frac{dQ}{dP}$ . Thus, to switch between Q and  $Q_T$ , all we need is the appropriate *Radon–Nikodym*-derivative, which is easily recovered by replacing the numéraires

$$\left. \frac{dQ}{dQ_T} \right|_{\mathcal{F}_t} = \frac{P(t,T)/P(T,T)}{B(t)/B(T)} = \frac{P(t,T)}{e^{-\int_t^T r(s)ds}}.$$
(19.13)

We have thus for an arbitrary  $T$ -claim  $V$ 

$$E^{\mathcal{Q}}\left[e^{-\int_t^T r(s)ds}V_T\middle|\mathcal{F}_t\right] = E^{\mathcal{Q}_T}\left[e^{-\int_t^T r(s)ds}V_T\frac{d\mathcal{Q}}{d\mathcal{Q}_T}\middle|\mathcal{F}_t\right] = P(t,T)E^{\mathcal{Q}_T}[V_T|\mathcal{F}_t].\tag{19.14}$$

Let's now look at a very special *T*-claim,

$$-\frac{\partial P(t,T)}{\partial T} = E^{\mathcal{Q}} \left[ -\frac{\partial}{\partial T} e^{-\int_t^T r(s)ds} \Big| \mathcal{F}_t \right] = E^{\mathcal{Q}} \left[ e^{-\int_t^T r(s)ds} r(T) \Big| \mathcal{F}_t \right]. \tag{19.15}$$

Dividing both sides by  $P(t, T)$ , and using (19.13) to express the right hand side in the T-forward measure yields

$$-\frac{\partial \log P(t,T)}{\partial T} = E^{Q_T}[r(T)|\mathcal{F}_t].$$
(19.16)

**Quick calculation 19.2** Confirm this equation.

Now remember that the left hand side of (19.16) is the forward rate  $f(t, T)$ , and that  $r(T) = f(T, T)$ . It follows immediately that the forward rate

$$f(t,T) = E^{Q_T}[f(T,T)|\mathcal{F}_t]$$
(19.17)

is a  $Q_T$ -martingale.

## **19.2 The Black-76-Model**

The pricing methodology in fixed-income derivative markets is largely built around Black's formula, also called the *Black*-76-model. Originally, it was designed to price options on futures in a deterministic interest rate world. So let's turn back the clock for a moment and assume a fixed interest rate *r*. The risk-neutral price process for an arbitrary non-dividend paying underlying is the geometric *Brown*ian motion

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$dS_t = rS_t dt + \sigma S_t dW_t. \tag{19.18}$$

What is the dynamics of the forward price *F<sup>t</sup>* = *e <sup>r</sup>*(*T*−*t*)*St*? An application of Itô's lemma yields

$$dF_t = \sigma F_t dW_t. \tag{19.19}$$

**Quick calculation 19.3** Apply Itô's lemma to confirm this result.

That is, the forward price process is a *Q*-martingale. But that means the risk-neutral measure *Q* and the *T*-forward measure *Q<sup>T</sup>* have to coincide. We can use the generalized version of the *Black–Scholes*-formula on page 269, set *b* = 0, and compute let's say the price of a European call option

$$C_t(K,T) = e^{-r(T-t)} (F_t \Phi(d_+) - K\Phi(d_-)), \qquad (19.20)$$

with Φ(*x*) again denoting the cumulative distribution function of a standard normal random variable *X*, and

$$d_{+/-} = \frac{\log(F_t/K) \pm \frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}}.\t(19.21)$$

In case of a fixed interest rate *r*, the price of a discount bond is *P*(*t*,*T*) = *e* −*r*(*T*−*t*) , and therefore we can conclude that

$$E^{Q_T}[(F_T - K)^+ | \mathcal{F}_t] = F_t \Phi(d_+) - K\Phi(d_-), \qquad (19.22)$$

for the *QT*-martingale *F<sup>t</sup>* . But the forward price is a *QT*-martingale whether or not interest rates are deterministic. Thus, in general the price of a plain vanilla European call option is

$$C_t(K,T) = P(t,T)(F_t\Phi(d_+) - K\Phi(d_-)). \tag{19.23}$$

By completely analogous arguments, one obtains the price of the corresponding plain vanilla put option

$$P_t(K,T) = P(t,T)(K\Phi(-d_-) - F_t\Phi(-d_+)). \tag{19.24}$$

Often interest rate sensitive products like bonds for example, need at least a deterministic term structure of volatility  $\sigma(t)$ . Take the simplest possible example, the discount bond. We know that its value approaches one for  $t \to T$ . This is also known as the pull to par phenomenon. But this means that the volatility of its dynamics has to vanish in that limit. To accommodate such requirements, we can express (19.21) in a slightly more general way

$$d_{+/-} = \frac{\log(F_t/K) \pm \frac{1}{2} \int_t^T \sigma^2(s) ds}{\sqrt{\int_t^T \sigma^2(s) ds}}.$$
 (19.25)

Note that those formulas have to hold for every *T*-forward price, independently of the actual underlying.

#### Example 19.1

What is the fair price of a plain vanilla European call option, expiring at  $T$ , on a discount bond with maturity date S, with  $t < T < S$ ?

#### Solution

The forward price of the S-bond is  $F_t = \frac{P(t,S)}{P(t,T)}$ . Of course this price is a  $Q_T$ -martingale and Black's formula immediately yields

$$C_t(K, T) = P(t, S)\Phi(d_+) - P(t, T)K\Phi(d_-),$$

with

$$d_{+/-} = \frac{\log\left(\frac{P(t,S)}{P(t,T)K}\right) \pm \frac{1}{2} \int_t^T \sigma_P^2(s) ds}{\sqrt{\int_t^T \sigma_P^2(s) ds}}$$

**Quick calculation 19.4** Compute  $d_{+/-}$  for the bond volatility  $\sigma_P(t) = \sigma \cdot (T - t)$ .

Note that in the *Black*-76-model, call and put prices are uniquely determined, if the strike price  $K$ , the expiry date  $T$ , and the implied volatility

$$\sigma_{\text{imp.}} = \sqrt{\frac{1}{T - t} \int_{t}^{T} \sigma^{2}(s) ds}$$
(19.26)

are known, because the forward price can be observed in the market. It is thus customary to quote K, T, and  $\sigma_{\text{imp}}$  instead of the call or put price.

## **19.3 Caps and Floors**

Caps/floors can be understood as payer/receiver interest rate swaps, where payments are only exchanged, if there is a net profit. As we shall see, there is a natural parity relation between caps, floors, and swaps. A cap can be decomposed into individual caplets. Assume we have *t* < *S* < *T*, where *S* is the reset date, and ∆*t* = *T* − *S*. Then, the payoff of the *T*-caplet with unit principal is

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\mathrm{Cpl}_{T}(\kappa, T) = \Delta t (L(S, T) - \kappa)^{+}.$$
 (19.27)

To determine the value of this caplet at time *t*, we have to analyze the dynamics of the LIBOR *L*(*S*,*T*). To this end, define the forward LIBOR *L*(*t*, *S*,*T*), using the relation (18.13) on page 421 between simple and continuous compounding

$$\frac{1}{1 + \Delta t L(t, S, T)} = e^{-\int_{S}^{T} f(t, s) ds} = \frac{P(t, T)}{P(t, S)}.$$
(19.28)

If we turn both sides of (19.28) upside down, we obtain

$$1 + \Delta t L(t, S, T) = \frac{P(t, S)}{P(t, T)}.$$
(19.29)

The right hand side of (19.29) is a *QT*-martingale, and so has to be the left hand side. The constant 1 is a trivial martingale under every measure and thus, ∆*tL*(*t*, *S*,*T*) must also be a *QT*-martingale

$$\Delta t L(t, S, T) = \Delta t E^{\mathcal{Q}_T} [L(S, S, T) | \mathcal{F}_t]. \tag{19.30}$$

It is immediately obvious that the coefficient ∆*t* cancels out of the equation, and from (19.28) it is easy to see that *L*(*S*, *S*,*T*) = *L*(*S*,*T*) has to hold.

**Quick calculation 19.5** Confirm this statement.

Summarizing our results, the forward LIBOR *L*(*t*, *S*,*T*) is a martingale under the *T*-forward measure, and from (19.29) it is given by

$$L(t, S, T) = \frac{1}{\Delta t} \left( \frac{P(t, S)}{P(t, T)} - 1 \right). \tag{19.31}$$

It is now a trivial exercise to compute the value of the *T*-caplet at time *t*, which is given by

$$\text{Cpl}_{t}(\kappa, T) = P(t, T)\Delta t (L(t, S, T)\Phi(d_{+}) - \kappa\Phi(d_{-})), \qquad (19.32)$$

with

$$d_{+/-} = \frac{\log\left(\frac{L(t,S,T)}{\kappa}\right) \pm \frac{1}{2} \int_t^S \sigma^2(s) ds}{\sqrt{\int_t^S \sigma^2(s) ds}}.$$
(19.33)

Usually, the caplet implied volatilities are quoted in the market, or to be a little more precise, they can be stripped from quoted cap volatilities. We will learn later how this works. The important point is that everything we need in order to compute the caplet price can be observed in the market. You may wonder, why the squared volatility in  $(19.33)$  is integrated only up to time S and not time T. This is because S is the reset date, which means the floating rate to be used for compounding between S and T is fixed at time S. Thus, a caplet is strictly speaking an option that expires at S, but pays off at the later time  $T$ .

A cap is a collection of caplets, based on a tenor structure like the one for swaps. Assume that interest payments are to be exchanged on a previously fixed schedule  $T_0,\ldots,T_N$ , where  $T_0$  is only the first reset date for the floating reference rate, and  $\Delta t = T_n - T_{n-1}$ . Then it is immediately clear that the price of the cap at  $t \leq T_0$  is

$$\mathrm{Cp}(t,\kappa) = \sum_{n=1}^{N} \mathrm{Cpl}_{t}(\kappa, T_{n}). \tag{19.34}$$

This formula looks not at all spectacular, but it relies heavily on the family of  $T_n$ forward measures for  $n = 1, \ldots, N$ . To see this, let's rewrite (19.34) in a slightly different form

$$\text{Cp}(t,\kappa) = \Delta t \sum_{n=1}^{N} P(t,T_n) E^{\mathcal{Q}_n} \left[ \left( L(T_{n-1},T_n) - \kappa \right)^{+} \middle| \mathcal{F}_t \right], \tag{19.35}$$

where  $E^{Q_n}[\ldots]$  is the conditional expectation under the  $T_n$ -forward measure. It is a great advantage of the martingale pricing framework over the partial differential equation approach that we can freely manipulate the probability measure by changing the numéraire. In the field of fixed-income derivative pricing, this feature becomes very powerful.

For  $t < S < T$  and  $\Delta t = T - S$ , the payoff of a T-floorlet is given by

$$\mathrm{Fll}_{T}(\kappa, T) = \Delta t(\kappa - L(S, T))^{+}.$$
(19.36)

This is immediately identified as the payoff of a put option on the LIBOR  $L(S, T)$ , with strike rate  $\kappa$ . We can now apply exactly the same chain of arguments to conclude that the price of the T-floorlet in Black's model has to be

$$\text{Fll}_{t}(\kappa, T) = P(t, T)\Delta t(\kappa\Phi(-d_{-}) - L(t, S, T)\Phi(-d_{+})),\tag{19.37}$$

#### **449 Plain Vanilla Fixed-Income Derivatives**

with *d*+/<sup>−</sup> precisely as in (19.33). As in case of the cap, the floor is a collection of floorlets, based on a tenor structure *T*0, . . . , *TN*. Thus, its fair price is

$$\mathrm{Fl}(t,\kappa) = \sum_{n=1}^{N} \mathrm{Fl}_{t}(\kappa, T_{n}). \tag{19.38}$$

Why should one wish to hold a cap or a floor? Imagine you have credit liabilities and interests are to be paid with reference to a floating rate, for example the respective LIBOR. Then you can "cap" the interest rate by buying a cap with the appropriate tenor structure and an exercise rate κmax. If the LIBOR exceeds κmax during the lifetime, the contract pays off the difference and you have effectively limited the maximum interest rate. Of course such an insurance does not come for free. But you can reduce the costs, if you are willing to pay interests at a rate of at least κmin. Shorting a floor on the same tenor structure and strike rate κmin generates proceeds from selling the contract. But now, the interest rate is effectively trapped between κmin and κmax. Such a position is called a collar. Let's raise an abstract question, independent of any background motivations. What would we get, if we held a collar with κmin = κmax = κ? If the appropriate LIBOR is greater than the strike rate κ, we would earn the difference from the cap. Otherwise we would have to pay the difference from the short position in the floor. But this payoff profile is exactly identical with the one of a payer interest rate swap. We have thus discovered the payer swap parity relation

$$Cp(t,\kappa) - Fl(t,\kappa) = IRS_{P}(t,\kappa). \tag{19.39}$$

**Quick calculation 19.6** State the receiver swap parity relation.

Caps and floors are easy to valuate, because they can be decomposed into caplets and floorlets, which can be priced with Black's formula. Such a decomposition property is not mandatory for interest rate derivatives and we will encounter an example where it is absent in the next section.

## **19.4 Swaptions and the Annuity Measure**

A swaption is a contract that grants its holder the right, but not the obligation, to enter a swap contract at a fixed rate κ sometime in the future. Usually the expiry date of the option is the first reset date *T*<sup>0</sup> of the associated swap. A payer swaption has the payoff

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\text{SWpt}_{P}(T_{0},\kappa) = \left(\Delta t \sum_{n=1}^{N} P(T_{0},T_{n})(L(T_{0},T_{n-1},T_{n})-\kappa)\right)^{+},\tag{19.40}$$

with our usual notation for the tenor structure. Now we run into a problem. This payoff cannot be decomposed into a sum of individual payoffs, depending only on one forward LIBOR. Hence, we cannot apply our  $T_n$ -forward measure trick.

Let's try to rewrite the payoff function. Recall the definition of the par rate of a swap at  $t = T_0$ , (18.54) on page 439. For  $t < T_0$  define the forward swap rate

$$r_S(t) = \frac{P(t, T_0) - P(t, T_N)}{\Delta t \sum_{n=1}^{N} P(t, T_n)}.$$
(19.41)

**Ouick calculation 19.7** Convince yourself that  $r_s(T_0)$  is the original par rate.

The numerator of  $(19.41)$  is the present value of the floating leg of the swap and the denominator is called the annuity factor

$$A(t) = \Delta t \sum_{n=1}^{N} P(t, T_n).$$
 (19.42)

If we reexpress the floating leg in terms of forward LIBOR, the forward swap rate becomes

$$r_S(t) = \frac{\Delta t \sum_{n=1}^{N} P(t, T_n) L(t, T_{n-1}, T_n)}{A(t)}.$$
(19.43)

Dividing and multiplying (19.40) by  $A(T_0)$  allows us to express the swaption payoff in a very neat form

$$\text{SWpt}_P(T_0, \kappa) = A(T_0)(r_S(T_0) - \kappa)^+.$$
 (19.44)

**Ouick calculation 19.8** Confirm the last equation.

The annuity factor (19.42) is a portfolio of traded assets and furthermore, it is guaranteed to be positive. Therefore, we can use it as a numéraire to obtain

$$\text{SWpt}_{P}(t,\kappa) = A(t)E^{Q_{A}}\left[\left(r_{S}(T_{0}) - \kappa\right)^{+}\middle|\mathcal{F}_{t}\right].\tag{19.45}$$

 $Q_A$  is called the annuity measure or also the swap measure. From (19.43) it is easy to see that the forward swap rate is a martingale in the annuity measure,

$$r_{S}(t) = E^{Q_{A}}[r_{S}(T_{0})|\mathcal{F}_{t}],\tag{19.46}$$

because the correct numerator is already part of the definition. But with  $r_S(t)$  being a  $Q_A$ -martingale, we can again use Black's formula to price the payer swaption and the result is

$$\text{SWpt}_{P}(t,\kappa) = A(t)(r_{S}(t)\Phi(d_{+}) - \kappa\Phi(d_{-})),\tag{19.47}$$

$$d_{+/-} = \frac{\log\left(\frac{r_{\mathcal{S}}(t)}{\kappa}\right) \pm \frac{1}{2} \int_{t}^{T_{0}} \sigma^{2}(s) ds}{\sqrt{\int_{t}^{T_{0}} \sigma^{2}(s) ds}} \quad \text{and} \quad A(t) = \Delta t \sum_{n=1}^{N} P(t, T_{n}). \tag{19.48}$$

It is not a difficult task to guess what the price of a receiver swaption is. Obviously, the payoff of such a contract at expiry *T*<sup>0</sup> is

$$\text{Swpt}_{R}(T_{0},\kappa) = A(T_{0})(\kappa - r_{S}(T_{0}))^{+}.$$
(19.49)

This identifies the receiver swaption as a put option on the swap rate. We can thus apply all arguments again and obtain

$$\text{Swpt}_{R}(t,\kappa) = A(t)(\kappa\Phi(-d_{-}) - r_{S}(t)\Phi(-d_{+})), \tag{19.50}$$

with *d*+/<sup>−</sup> and *A*(*t*) as in (19.48). As in the cap market, implied volatilities for swaptions with different expiries and different tenors are quoted in the market. It is customary to encode the relevant information in the format *x*Y*y*Y, which means the swaption expires in *x* years and the underlying swap has a lifetime of *y* years. A 2Y5Y payer swaption is thus a call option with 2 years' time to expiry, on the par rate of a 5 years' swap contract. One can thus build a grid with implied volatility information for different tenors and expiries, and extract a volatility surface. There is a typical example of implied at-the-money (ATM) swaption volatility of May 16, 2000 that has become somewhat standard; see for example Brigo and Mercurio (2007, p. 288) or Filipović (2009, p. 24). The data is reproduced in Table 19.1. The resulting implied volatility surface, generated by spline interpolation, is illustrated in Figure 19.1.

There is another surprising application of swaptions. They allow for synthetic replication of a callable bond. A callable bond is a coupon-bearing bond, which allows the

| xY/yY | 1Y   | 2Y   | 3Y   | 4Y   | 5Y   | 6Y   | 7Y   | 8Y   | 9Y   | 10Y  |
|-------|------|------|------|------|------|------|------|------|------|------|
| 1Y    | 16.4 | 15.8 | 14.6 | 13.8 | 13.3 | 12.9 | 12.6 | 12.3 | 12.0 | 11.7 |
| 2Y    | 17.7 | 15.6 | 14.1 | 13.1 | 12.7 | 12.4 | 12.2 | 11.9 | 11.7 | 11.4 |
| 3Y    | 17.6 | 15.5 | 13.9 | 12.7 | 12.3 | 12.1 | 11.9 | 11.7 | 11.5 | 11.3 |
| 4Y    | 16.9 | 14.6 | 12.9 | 11.9 | 11.6 | 11.4 | 11.3 | 11.1 | 11.0 | 10.8 |
| 5Y    | 15.8 | 13.9 | 12.4 | 11.5 | 11.1 | 10.9 | 10.8 | 10.7 | 10.5 | 10.4 |
| 7Y    | 14.5 | 12.9 | 11.6 | 10.8 | 10.4 | 10.3 | 10.1 | 9.9  | 9.8  | 9.6  |
| 10Y   | 13.5 | 11.5 | 10.4 | 9.8  | 9.4  | 9.3  | 9.1  | 8.8  | 8.6  | 8.4  |

**Table 19.1** Implied ATM swaption volatility in % of May 16, 2000

with

![](_page_10_Figure_1.jpeg)

**Fig. 19.1** 3D Implied ATM swaption volatility surface based on the data of May 16, 2000

issuer to prematurely reimburse the principal and cease paying all further coupons. The way this works is best understood in an example.

### **Example 19.2**

Suppose you have issued a coupon-bearing bond with 5 years' time to maturity and annual coupon payments at a rate of 6%. You want to reserve the right to reimburse the principal after 2 years to avoid further coupon payments, but you cannot change the original contract. How can the callable bond be replicated?

### Solution

You can buy a 2Y3Y receiver swaption with the strike rate κ = 6%. If you decide not to exercise, everything stays the same and you have not called the bond. If you exercise, the fixed leg cancels the coupon payments and you are stuck with the floating leg payments and the principal at the end of the contract. But notice that paying LIBOR on the principal due at the end of year 5 is effectively a floating rate note, and we know that this is equivalent to paying the principal at the end of year 2.

........................................................................................................................

**Quick calculation 19.9** Formulate the parity relation for a callable bond.

## **19.5 Eurodollar Futures**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

Eurodollar futures are standardized interest rate future contracts that are traded at the Chicago Mercantile Exchange (CME). Eurodollars are US dollar denominated deposits in institutions outside the United States. The CME interest rate future contracts are linked to the 3-months LIBOR. They are settled at a delivery price of

$$\hat{F}_T = 100 \cdot (1 - L(T, T + 1/4)), \tag{19.51}$$

#### **453 Plain Vanilla Fixed-Income Derivatives**

Specific delivery dates are in March, June, September, and December. Define the 3-months LIBOR future *L*ˆ (*t*,*T*,*T* + 1/4) to be the rate induced by the quoted future price at time *t*,

$$\hat{F}_t = 100 \cdot (1 - \hat{L}(t, T, T + 1/4)). \tag{19.52}$$

Clearly, as *t* tends to *T*, the LIBOR future *L*ˆ (*t*,*T*,*T* + 1/4) approaches *L*ˆ (*T*,*T*,*T* + 1/4) =*L*(*T*,*T* + 1/4). What is a little bit confusing about Eurodollar futures is that the daily settlement is with respect to another price,

$$\tilde{F}_t = P \cdot \left( 1 - \frac{1}{4} \hat{L}(t, T, T + 1/4) \right). \tag{19.53}$$

The principal is always *P* = \$1 million and thus, if there is a 1 bps (0.01%) increase in the LIBOR future, the CME contract buyer has to pay \$25 to the seller.

**Quick calculation 19.10** Verify the last statement.

Because of the daily settlement, it is always costless to enter the future contract. We have seen before that the future price *F*ˆ *t* is a *Q*-martingale. By the same arguments we used to show that the forward LIBOR *L*(*t*, *S*,*T*) is a *QT*-martingale, we can prove that *L*ˆ (*t*,*T*,*T* + 1/4) is a *Q*-martingale. Since the factor 100 in (19.52) is constant and therefore a trivial martingale, we must have

$$-100 \cdot \hat{L}(t, T, T + 1/4) = -100 \cdot E^{Q}[\hat{L}(T, T, T + 1/4)|\mathcal{F}_{t}]. \tag{19.54}$$

Again, the factor −100 cancels out of the equation and leaves the desired result.

**Quick calculation 19.11** Show that *F*˜ *t* in (19.53) is also a *Q*-martingale.

## **19.6 Further Reading**

A comprehensive introduction to the forward measure approach is provided in Cairns (2004, chap. 7). A nice collection of commonly used measures, including hybrid measures, is given in Andersen and Piterbarg (2010a, sect. 4.2). A detailed derivation of Black's formula, using the example of caplets, can be found in Brigo and Mercurio (2007, sect. 6.2). A very accessible introduction to plain vanilla interest rate derivatives is Joshi (2008, chap. 13). A vast collection of standard derivative instruments can be found in Andersen and Piterbarg (2010a, chap. 5). Eurodollar futures are discussed in Andersen and Piterbarg (2010a, sect. 5.4) and Filipović (2009, sect. 8.2). A background in trading and pricing forwards and futures is provided in Jarrow (2002, chap. 12) and Vellekoop (2010).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

#### Problems 19.7

**19.1** Suppose you have an expectation with respect to the *T*-forward measure, based on the information available at time  $t < T$ . You want to reexpress this expectation with respect to the S-forward measure for  $S > T$ ,

$$V_t = P(t,T)E^{Q_T}[V_T|\mathcal{F}_t] = P(t,T)E^{Q_S}\bigg[V_T\frac{dQ_T}{dQ_S}\bigg|\mathcal{F}_t\bigg].$$

Derive the *Radon–Nikodym*-derivative  $\frac{dQ_T}{dQ_s}\Big|_{\mathcal{F}_t}$  and write the solution for  $V_t$ .

**19.2** Use an arbitrage argument, analogous to the one in Table 11.1 on page 212, to prove that in a stochastic interest rate world, the strike price of a forward contract  $F_t(K, T)$  that can be entered costlessly at time  $t = 0$  has to be

$$K = \frac{V_0}{P(0,T)},$$

which is the forward price of a non-dividend paving underlying V at  $t = 0$ .

**19.3** Let today be time  $t$ . Suppose you want to price a plain vanilla option with expiry date T on a discount bond, maturing at S, within the *Black*-76-model, with  $t <$  $T < S$ . Assume the bond volatility is given by

$$\sigma_P(t) = \sigma \sqrt{1 - e^{-(T-t)}}.$$

Compute the quantity  $d_{+/-}$ , required in Black's formula.

**19.4** Use the definition of the forward LIBOR, (19.31) on page 447, to show that the present value of the floating leg of a plain vanilla interest rate swap is indeed

Floating leg = 
$$\Delta t \sum_{n=1}^{N} P(t, T_n) L(t, T_{n-1}, T_n)$$
.

**19.5** Prove that the forward swap rate

$$r_{S}(t) = \frac{P(t, T_{0}) - P(t, T_{N})}{\Delta t \sum_{n=1}^{N} P(t, T_{n})}$$

can be understood as a weighted average of all forward LIBORs within the tenor of the swap.
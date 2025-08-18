✖

# **5 Architecture of Financial Markets**

In this chapter, financial markets are analyzed in the simplest possible setup. Refinements and extensions, to align the theory better with reality, are possible in many ways and often straightforward. But at this point they would be an obstruction in recognizing the fundamental rules of financial markets. It is only on this blueprint that we see the origin of some very deep principles, like the duality between replication and risk-neutral probabilities, easily.

## **5.1 The Arrow–Debreu-World**

Originally, Arrow and Debreu (1954) were concerned with optimal allocation problems in an economy with *N* consumption goods *cn*, where *n* = 1, . . . , *N*. We will modify this idea by looking at one consumption good, but in different states of the world ω*n*. To emphasize this view, we write slightly abusively *c*ω, for ω= 1, . . . , Ω. The remaining framework is the following:

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

- There are only two periods of time, *t* = 0 which is today, and *t* = *T* which is sometime in the future.
- Consumption today, *c*0, is certain.
- Consumption in the future, *c*ω, is random and depends on the state ω= 1, . . . , Ω, to be realized.
- The agent is equipped with an initial endowment *w* (wealth) at time *t* = 0.
- There are no frictions like taxes, trading costs, etc.

Accumulating consumption in all different states into a consumption vector |*c*⟩, the *Arrow–Debreu*-problem becomes maximizing the expected utility *U*[*C*], under the wealth constraint

$$c_0 + \sum_{\omega=1}^{\Omega} \psi_{\omega} c_{\omega} = c_0 + \langle \psi | c \rangle = w. \tag{5.1}$$

If we were talking about the original allocation problem in a world with *N* different commodities, ψ*<sup>n</sup>* would be the price of good *n* in units of *c*0. In our modified framework, ψ<sup>ω</sup> is the price of consuming one unit of the single good in state ω. Because today we have no idea if state ω will realize in the future or not, ψ<sup>ω</sup> is more precisely the price of a claim to one unit of consumption in state ω. The form ⟨ψ| is called the state price bra-vector or the state price form.

Solving a constraint optimization problem of this kind is usually done with Lagrange's method. We then obtain the augmented problem

$$\max_{c_0,\ldots,c_\Omega} U[C] + \lambda \Bigg( w - c_0 - \sum_{\omega=1}^{\Omega} \psi_\omega c_\omega \Bigg), \tag{5.2}$$

with the auxiliary *Lagrange*-multiplier λ. From equating the derivatives with respect to the consumption variables to zero, we get two different kinds of first order conditions,

$$\frac{\partial U}{\partial c_0} = \lambda \quad \text{and} \quad \frac{\partial U}{\partial c_\omega} = \lambda \psi_\omega,\tag{5.3}$$

from which we can conclude that

$$\psi_{\omega} = \frac{\partial U/\partial c_{\omega}}{\partial U/\partial c_0} \tag{5.4}$$

has to hold for ω= 1, . . . , Ω. This statement is completely general and, to see what it means, we have to specify the *von Neumann–Morgenstern*-utility functional. A most popular choice is a time separable version like

$$U[C] = u(c_0) + e^{-\rho T} \sum_{\omega=1}^{\Omega} u(c_{\omega}) p_{\omega}.$$
 (5.5)

The functional is called time separable, because in differentiating (5.5) with respect to *c*<sup>0</sup> and *c*ω, there will be no mixed terms from different times. The factor *e* −ρ*T* , for ρ > 0 mimics impatience of the agent. She would prefer to reach a given consumption level today, rather than in the future. Put another way around, agents need an extra incentive to postpone consumption into the future, because who knows if they will still be alive and healthy to enjoy it? Using (5.5), we can compute the state price (5.4) explicitly,

$$\psi_{\omega} = e^{-\rho T} p_{\omega} \frac{u'(c_{\omega})}{u'(c_0)} = -\text{MRS},\tag{5.6}$$

where MRS is the marginal rate of substitution.

**Quick calculation 5.1** Verify the first equality in (5.6).

The marginal rate of substitution is the exchange relationship between *c*<sup>0</sup> and *c*ω, if we hold all other consumptions fixed; see Figure 5.1. To obtain the MRS, we have to compute the total differential of *U* and set it equal to zero,

$$dU = u'(c_0)dc_0 + e^{-\rho T} p_\omega u'(c_\omega) dc_\omega \stackrel{!}{=} 0.$$
 (5.7)

![](_page_2_Figure_1.jpeg)

![](_page_2_Figure_2.jpeg)

Rearranging terms yields the desired result

$$\frac{dc_0}{dc_\omega} = -e^{-\rho T} p_\omega \frac{u'(c_\omega)}{u'(c_0)} = \text{MRS.}$$

$$(5.8)$$

The MRS is negative, because you have to give up some consumption today to gain something in state  $\omega$  in the future, and at the same time keep your expected utility constant. The marginal rate of substitution tells you how much it would cost to trade one unit of consumption in state  $\omega$  for today's consumption, measured in  $c_0$  units. Thus, the state price  $\psi_{\omega}$  is the price of one additional unit of  $c_{\omega}$ , in terms of  $c_0$  units, leaving everything else unchanged. Note that it is proportional to the probability of state  $\omega$ , to the ratio of marginal utilities of  $c_{\omega}$  and  $c_0$ , and inversely proportional to impatience of the agent.

# 5.2

## The Portfolio Selection Problem

Let's now take a look at a financial market economy. Suppose there are  $N$  securities,  $S_1, \ldots, S_N$ , with different payoffs in different states of the world. We can summarize all this information in a payoff matrix

$$D = \begin{pmatrix} d_{11} & d_{12} & \dots & d_{1N} \\ d_{21} & d_{22} & \dots & d_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ d_{\Omega 1} & d_{\Omega 2} & \dots & d_{\Omega N} \end{pmatrix}, \tag{5.9}$$

where  $d_{\omega n}$  is the payoff of security *n* in state  $\omega$ , in  $c_0$  consumption units. The payoffmatrix collects all securities column by column, and all possible states of the world row by row. Assume you can invest at time  $t = 0$  in security  $S_n$  at a price  $s_n$ . You are then entitled to a payoff  $d_{\omega n}$  at time  $t = T$ . All security prices are collected in the form  $\langle s|$ . Recognize the pattern, all prices are forms. You are allowed to buy or even sell arbitrary fractions of all traded securities at  $t = 0$ . The number  $\theta_n$ , positive or negative, records

the quantity of security  $S_n$  you hold. All information of this kind is assembled in the portfolio vector  $|\theta\rangle$ . The first consequence of this construction is

$$D|\theta\rangle = \begin{pmatrix} d_{11} & \dots & d_{1N} \\ \vdots & \ddots & \vdots \\ d_{\Omega 1} & \dots & d_{\Omega N} \end{pmatrix} \begin{pmatrix} \theta_1 \\ \vdots \\ \theta_N \end{pmatrix} = \begin{pmatrix} c_1 \\ \vdots \\ c_{\Omega} \end{pmatrix} = |c\rangle. \tag{5.10}$$

As you can see, securities are instruments for shifting consumption from period  $t = 0$ to period  $t = T$  and adjusting your desired consumption profile.

Now we have a new optimization problem. We still maximize expected utility, but now the wealth constraint has the form

$$c_0 + \sum_{n=1}^{N} s_n \theta_n = c_0 + \langle s | \theta \rangle = w. \tag{5.11}$$

This new problem has a known solution, if there is a state price form  $\langle \psi |$ , such that

$$\langle s| = \langle \psi|D \tag{5.12}$$

holds. To see this, plug  $(5.12)$  into the wealth constraint and use  $(5.10)$ 

$$c_0 + \langle s|\theta \rangle = c_0 + \langle \psi|D|\theta \rangle = c_0 + \langle \psi|c \rangle = w, \tag{5.13}$$

and we are right back in the *Arrow–Debreu*-world. This is a quite remarkable result. The question is, under which conditions does it hold? The key to the answer is Equation (5.12). There has to be a unique solution for  $\langle \psi |$  for the whole chain of arguments to hold. A necessary condition for such a solution to exist, is that the financial market, summarized by D, contains a full set of  $\Omega$  linearly independent securities. In this case  $DD'$  is invertible and we obtain

$$\langle \psi | = \langle s | D' (DD')^{-1} . \tag{5.14}$$

**Quick calculation 5.2** Confirm the last equation.

Such a market is called complete, because every possible payoff is attainable by a linear combination of traded securities, which means a portfolio. Notice that a complete market alone does not guarantee the existence of a state price form. Thus we have to check, whether or not the potential solution  $(5.14)$  indeed satisfies  $(5.12)$ .

Example 5.1

Consider the following financial market

$$D = \begin{pmatrix} 1 & 3 & 2 \\ 2 & 0 & 4 \end{pmatrix} \quad \text{and} \quad \langle s| = \begin{pmatrix} 1 & 2 & 2 \end{pmatrix}.$$

What is the state price form  $\langle \psi |$  if there is one?

#### Solution

The first and second security are linearly independent, therefore the market is complete. The following building blocks are required in the computation of  $\langle \psi |$ .

$$\langle s|D' = \begin{pmatrix} 11 & 10 \end{pmatrix}$$
 and  $(DD')^{-1} = \frac{1}{180} \begin{pmatrix} 20 & -10 \ -10 & 14 \end{pmatrix}$ .

The potential state price form is then obtained by

$$\langle \psi | = \langle s | D' (DD')^{-1} = \frac{1}{180} \begin{pmatrix} 11 & 10 \end{pmatrix} \begin{pmatrix} 20 & -10 \\ -10 & 14 \end{pmatrix} = \frac{1}{180} \begin{pmatrix} 120 & 30 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & \frac{1}{6} \end{pmatrix}.$$

It remains to check, whether or not  $\langle \psi |$  solves (5.2),

$$\langle \psi | D = \begin{pmatrix} \frac{2}{3} & \frac{1}{6} \end{pmatrix} \begin{pmatrix} 1 & 3 & 2 \\ 2 & 0 & 4 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 2 \end{pmatrix} = \langle s|.$$

Thus,  $\langle \psi |$  is the desired state price form.

**Quick calculation 5.3** Verify the intermediate results in Example 5.1.

## 5.3

## Preference-Free Results

All results derived so far depend on individual preferences and utilities of economic agents. Recall that the state prices are negative marginal rates of substitution, which depend on marginal utility. In this section we will see a far more powerful machinery, leading to completely preference-free results in complete financial markets. But first, we need an additional bit of notation. For two N-dimensional vectors,  $|a\rangle$  and  $|b\rangle$ , define the following relations:

$$|a\rangle \ge |b\rangle \quad \leftrightarrow \quad \text{for all } n, a_n \ge b_n \text{ holds,} |a\rangle > |b\rangle \quad \leftrightarrow \quad |a\rangle \ge |b\rangle, \text{ and } a_n > b_n \text{ for at least one } n, |a\rangle \gg |b\rangle \quad \leftrightarrow \quad \text{for all } n, a_n > b_n \text{ holds.}$$
 (5.15)

Of course, the same relations apply to forms. Now we are in a position to formulate the portfolio selection problem in a more efficient fashion and to define the notion of arbitrage precisely. The portfolio selection problem can be restated in the compressed form

$$|C\rangle = \begin{bmatrix} c_0 \\ |c\rangle \end{bmatrix} = \begin{bmatrix} w \\ |0\rangle \end{bmatrix} + \begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\theta\rangle, \tag{5.16}$$

. . . . . . . . . . . . . . . . . . . .

where [...] indicates a compound vector or a compound matrix, respectively. This notation may look intimidating but it is quite efficient. You can do the algebra with

compound entities just as if they were ordinary vectors and matrices, with scalar coefficients. That is the power of linearity.

**Quick calculation 5.4** Verify that the portfolio selection problem and its wealth constraint is summarized in (5.16).

Imagine now, we held a portfolio |θ⟩ and did a slight modification to obtain a new portfolio |θ ∗ ⟩ = |θ⟩ + |η⟩. Then our overall change in consumption would be

$$|C^*\rangle - |C\rangle = \begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\eta\rangle. \tag{5.17}$$

We call this change in overall consumption an arbitrage opportunity, if

$$\begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\eta\rangle > |0\rangle \tag{5.18}$$

holds. The portfolio |η⟩ offers something for nothing. Either the portfolio costs nothing today, but pays off a positive amount in at least one state of the world, or it has a negative price today, but nonnegative payoffs in the future. Therefore, an arbitrage opportunity is something like a free lunch.

At this point, we make only two structural assumptions about financial markets. First, more is better than less, and second, there is no free lunch. The following theorem is one of the most profound statements in financial economics.

**Theorem 5.1 (Fundamental theorem of asset pricing)** *The following statements about security prices* ⟨*s*| *and payoffs D are equivalent*:

1. *There are no arbitrage opportunities,*

$$\nexists |\eta\rangle: \begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\eta\rangle > |0\rangle.$$

2. *There is a strictly positive state price form,*

$$\exists \langle \psi | \gg \langle 0 | : \langle s | = \langle \psi | D.$$

3. *There is an agent with strictly monotonic increasing preferences U*, *who realizes an optimum in the portfolio selection problem*.

We will prove Theorem 5.1 by showing that the chain 1 ⇒ 2 ⇒ 3 ⇒ 1 holds (cf. Dybvig and Ross, 2003). Proving the first implication is the toughest link in the chain. The major part of the theoretical work on this was done by Harrison and Kreps (1979). To follow their line of very sophisticated reasoning, we need another theorem about linear separation of closed cones that can be found in Duffie (2001, appendix B).

![](_page_6_Figure_1.jpeg)

**Fig. 5.2** Bounded set of points with ε-vicinity of point *x* (left) and convex set of points (right)

**Theorem 5.2 (Separating hyperplane theorem for closed cones)** *Suppose M and K are closed convex cones in* R *<sup>N</sup> that intersect precisely at zero. If K does not contain a linear subspace other than* {0}, *then there is a nonzero linear functional L*,*such that L*[*m*] < *L*[*k*], *for each m in M and each nonzero k in K*.

We have to explain some of the technical terms in Theorem 5.2 in more detail, before we can proceed.

#### **Closedness**

Recall that the coordinate representation of a vector |*k*⟩ marks a point *k* in R *<sup>N</sup>*. A set of points *K* is closed, if for every point *x* outside of *K*, there is an ε > 0, such that the interior of the *x*-centered sphere with radius ε is outside of *K*, too. The concept is illustrated in Figure 5.2 left. A line or a plane are examples of closed sets of points. Here is a counterexample:

# **Example 5.2**

The interval *K* = [0, 1) is not a closed set of points.

#### Proof

Pick the point *x* = 1. In this case the sphere with radius ε is the interval [1 − ε, 1 + ε]. Now choose a point in the interior of that sphere, say *y* = 1 − ε 2 . You can immediately see that there is no ε > 0, such that *y* < [0, 1).

........................................................................................................................

#### **Convexity**

A set of points *M* is called convex, if for two arbitrary points *x* and *y* in *M*, every linear combination

$$\lambda x + (1 - \lambda)y,\tag{5.19}$$

with 0 < λ < 1 is also in *M*. What this means is that every point on the line connecting *x* and *y* has to be in *M*, too; see Figure 5.2 right.

![](_page_7_Figure_1.jpeg)

**Fig. 5.3** Different closed convex cones in R<sup>2</sup> – Closed half-space (left) and linear subspace (right)

**Quick calculation 5.5** Convince yourself that the set *K* in Figure 5.2 left is not convex.

#### **Closed convex cones**

A set of points *K* is a closed convex cone, if it is closed and convex, and if for every point *k* in *K*, α*k* is also in *K*, for α ≥ 0. There are two basic types of closed convex cones we are interested in, closed half-spaces and linear subspaces. An example of a closed half-space is a set of points *K*, generated by all vectors satisfying |*k*⟩ ≥ |0⟩,

$$K = \left\{ k \in \mathbb{R}^N : |k\rangle \ge |0\rangle \right\}. \tag{5.20}$$

This is the positive orthant; see Figure 5.3 left for an example in R 2 . Note that *K* does not contain any linear subspaces, which are lines or planes that extend to infinity in every direction, with exception of the linear subspace {0}, which is merely a point. Another example of a convex cone is the set of points generated by projecting an arbitrary vector in R *<sup>N</sup>* onto a linear subspace,

$$M = \left\{ m : |m\rangle = P|\eta\rangle, \ \eta \in \mathbb{R}^N \right\},\tag{5.21}$$

where *P* is a projection matrix. An R 2 example is given in Figure 5.3 right, where we used the projection matrix

$$P = \begin{pmatrix} 3 & -3 \\ 2 & -2 \end{pmatrix}.\tag{5.22}$$

**Quick calculation 5.6** Check that both examples satisfy the required conditions for closed convex cones.

We are now in a position to apply Theorem 5.2 to prove the first implication of the fundamental theorem of asset pricing. We will track our steps graphically in R 3 , whereas the analytical results are independent of the dimensionality of the vector space.

![](_page_8_Figure_1.jpeg)

**Fig. 5.4** 3D Fundamental theorem of asset pricing – Convex cones *K* and *M* intersecting at zero

#### **1 implies 2:**

Let's first define the set of points generated by the prices and payoffs of all traded securities in the market

$$M = \left\{ m : |m\rangle = \begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\eta\rangle, \ \eta \in \mathbb{R}^N \right\}.$$
 (5.23)

The points *m* span a linear space in R Ω+1

**Quick calculation 5.7** Why is *M* a linear space? Remember what linearity means.

.

If there is no arbitrage, then according to the fundamental theorem, *M* intersects the half-space *K*, defined by

$$K = \left\{ k \in \mathbb{R}^{\Omega+1} : |k\rangle \ge |0\rangle \right\},\tag{5.24}$$

only at zero, *M* ∩ *K* = {0}. Because of this, *M* has to be a linear subspace of R Ω+1 , which means a (hyper-) plane. The situation is illustrated in Figure 5.4. Every point *m* ∈ *M* represents an arbitrage free configuration of security price and state contingent payoffs. Every nonzero point *k* ∈ *K* means an arbitrage opportunity. Note that we satisfy precisely the conditions of the separating hyperplane theorem, so let's use it.

The separating hyperplane theorem ensures that there is a linear functional *L*, such that *L*[*m*] <*L*[*k*] for every *m* ∈ *M* and nonzero *k* ∈ *K*. We know from the *Riesz*representation theorem that a linear functional for every vector in the plane *M* is given by the inner product with a form. But which form is the right one? Let's focus on the two bits of information a form carries, its orientation and its magnitude. The form has to be oriented in a way, such that its inner product with every vector |*m*⟩ is smaller than the inner product with every nonzero vector |*k*⟩. There are some vectors drawn in Figure 5.4 to illustrate the situation. On the one hand, for very tiny vectors, pointing into *K*, the inner product can be very small. On the other hand, *M* is a linear subspace,

![](_page_9_Figure_1.jpeg)

**Fig. 5.5** 3D Fundamental theorem of asset pricing – Convex cones *K* and *M* and coplanar form ⟨*L*|

which means, if there is a vector |*m*⟩, then there is also a vector −|*m*⟩ and infinitely many scaled versions of them. For all those vectors, the inner product with the desired form has to be smaller than the one with a small vector |*k*⟩. If you think it through thoroughly, there is only one possible solution. The desired form ⟨*L*| has to be coplanar with the plane *M*. In this case it is orthogonal to every vector |*m*⟩, which means the inner product is always zero, and it has to point into the direction of *K*, so that the inner product with every vector |*k*⟩ > |0⟩ is positive; see Figure 5.5.

We succeeded in determining the orientation of ⟨*L*|, but there is still one degree of freedom left, its magnitude. It is easy to see in Figure 5.5, that all arguments we have put forward so far hold independently of the spacing of ⟨*L*|. But we can use this ambiguity in a very smart way. We know that the inner product of every vector in the linear subspace *M* with any scaled version of ⟨*L*| has to vanish,

$$\alpha \langle L| \begin{bmatrix} -\langle s| \\ D \end{bmatrix} | \eta \rangle = \alpha \begin{bmatrix} l_0 & \langle l| \end{bmatrix} \begin{bmatrix} -\langle s| \\ D \end{bmatrix} | \eta \rangle = 0, \tag{5.25}$$

where we simply partitioned the form ⟨*L*| into [ *l*<sup>0</sup> ⟨*l* | ] . Now set α = 1 *l*0 and call the form 1 *l*0 ⟨*l* | = ⟨ψ|. We then obtain

$$\begin{bmatrix} 1 & \langle \psi | \end{bmatrix} \begin{bmatrix} -\langle s | \\ D \end{bmatrix} | \eta \rangle = 0. \tag{5.26}$$

But (5.26) has to hold for arbitrary vectors |η⟩, in particular for |η⟩ ≫ |0⟩ or |η⟩ ≪ |0⟩. Thus, we can conclude that

$$\begin{bmatrix} 1 & \langle \psi | \end{bmatrix} \begin{bmatrix} -\langle s | \\ D \end{bmatrix} = \langle 0 | \tag{5.27}$$

has to hold. Expanding and rearranging (5.27) yields

$$\langle s| = \langle \psi|D. \tag{5.28}$$

We are not finished yet. The fundamental theorem claims additionally that the state price form ⟨ψ| is strictly positive. That's where the second part of the separating hyperplane theorem comes in. It ensures that

$$\begin{vmatrix} 1 & \langle \psi | \, | k \rangle > 0, \end{vmatrix} \tag{5.29}$$

for every vector |*k*⟩ > |0⟩ in R Ω+1 . Remember what |*k*⟩ > |0⟩ means. |*k*⟩ is easily allowed to have Ω zeros and only one positive coefficient. But we do not know which one is the positive one. Thus, to guarantee that (5.29) holds, we must have

$$\langle \psi | \gg \langle 0 |. \tag{5.30}$$

This concludes the proof of the first implication of the fundamental theorem. The remaining steps are much easier.

#### **2 implies 3:**

We show by construction that a strictly positive state price form implies the existence of an agent with strictly increasing preferences, who realizes an optimum in the portfolio selection problem. Suppose an agent has expected utility *U* = [ 1 ⟨ψ| ] |*C*⟩. Such preferences are clearly strictly monotonic increasing in every component of |*C*⟩. From (5.16) and (5.28), we have

$$U = \begin{bmatrix} 1 & \langle \psi | \end{bmatrix} \left( \begin{bmatrix} w \\ |0 \rangle \end{bmatrix} + \begin{bmatrix} -\langle s | \\ D \end{bmatrix} |\theta \rangle \right)$$
  
=  $w + \left( -\langle s | + \langle \psi | D \rangle |\theta \rangle \right)$   
=  $w + \langle 0 | \theta \rangle = w.$  (5.31)

We cannot increase utility at all by forming or changing portfolios and thus, (5.31) is already an optimum, no matter which portfolio |θ ∗ ⟩ the agent holds. This concludes the proof of the second implication.

#### **3 implies 1:**

The final step is rather trivial. If there is an agent with strictly increasing preferences, realizing an optimum by holding a portfolio |θ ∗ ⟩, then there cannot be arbitrage opportunities. An arbitrage would increase the agent's expected utility, but |θ ∗ ⟩ is already a maximum. Therefore, we can conclude that there are no arbitrage opportunities. This argument confirms the last implication and completes the proof.

# **5.4 Pareto-Optimal Allocation and the Representative Agent**

The fundamental theorem of asset pricing is a completely general statement. It holds, no matter if the market is complete or incomplete. It even holds for infinite dimensional vector spaces.<sup>1</sup> Complete markets are very attractive from an analytical point of view,

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

<sup>1</sup> The structural consequences of the theorem even remain valid in more general function spaces, where the separating hyperplane theorem is no longer applicable. In this case the *Hahn–Banach*-theorem has to be used (Delbaen and Schachermayer, 1994)

because they guarantee that certain results from equilibrium allocation theory hold. In this section, we look at a financial economy with *M* agents. The first important result is the analogue of the first welfare theorem in economics:

**Theorem 5.3 (Equilibrium allocation)** *Consider an M*-*agents financial economy, with equilibrium portfolio holdings* |θ ∗ 1 ⟩, . . . , |θ ∗ *<sup>M</sup>*⟩. *If the market is complete, then the allocation of consumption is Pareto*-*optimal*.

The first thing you should realize is that the absence of arbitrage opportunities is a necessary condition for equilibrium. If there were arbitrage opportunities left in the market, agents would surely exploit them and thus the market would not be in equilibrium. Of course the opposite is not true, absence of arbitrage does not automatically imply equilibrium of the financial market. However, because we have assumed equilibrium in Theorem 5.3, we can be sure that the market is free of arbitrage opportunities. We will now prove the theorem by contradiction.

A consumption allocation is *Pareto*-optimal, if there is no other allocation, in which no agent realizes less consumption at any time and in any state, but at least one agent consumes more, either at time *t* = 0 or in some state at time *t* =*T*. We will assume, that it is possible for at least one agent to increase consumption and subsequently show that this assumption contradicts the constraints of the optimization problem. So let's assume, there is a collection of portfolios |θ*m*⟩, for *m* = 1, . . . , *M*, such that

$$\sum_{m=1}^{M} \left( c_{0m} + \langle s | \theta_m \rangle \right) > \sum_{m=1}^{M} \left( c_{0m}^* + \langle s | \theta_m^* \rangle \right). \tag{5.32}$$

Let's start by manipulating the right hand side of (5.32). We will use the fact that |θ ∗ *m*⟩ are equilibrium portfolios and thus

$$\sum_{m=1}^{M} |\theta_{m}^{*}\rangle = |0\rangle \tag{5.33}$$

has to hold, because in equilibrium we have market clearing. One then obtains

$$\sum_{m=1}^{M} \left( c_{0m}^{*} + \langle s | \theta_{m}^{*} \rangle \right) = \sum_{m=1}^{M} c_{0m}^{*} + \langle s | \sum_{m=1}^{M} | \theta_{m}^{*} \rangle = \sum_{m=1}^{M} c_{0m}^{*} = W, \tag{5.34}$$

overall consumption equals the total wealth *W* in the economy, measured in *c*<sup>0</sup> units. Now let's take a closer look at the left hand side of (5.32). Because the market is arbitrage free and complete, there is a unique state price form, such that

$$\sum_{m=1}^{M} \left( c_{0m} + \langle s | \theta_m \rangle \right) = \sum_{m=1}^{M} \left( c_{0m} + \langle \psi | D | \theta_m \rangle \right) = \sum_{m=1}^{M} \left( c_{0m} + \langle \psi | c_m \rangle \right). \tag{5.35}$$

Combining these results yields

$$\sum_{m=1}^{M} \left( c_{0m} + \sum_{\omega=1}^{\Omega} \psi_{\omega} c_{\omega m} \right) > \sum_{m=1}^{M} w_{m} = W, \tag{5.36}$$

which violates the wealth constraint of at least one agent in the *Arrow–Debreu*-problem. Thus, our assumption leads to a contradiction and we can conclude that the original allocation, generated by |θ ∗ 1 ⟩, . . . , |θ ∗ *<sup>M</sup>*⟩, is *Pareto*-optimal.

Another important feature of complete markets, at least as long as they are frictionless, is the existence of a representative agent (Constantinides, 1982). We will start by briefly reviewing the optimization problem of a single agent in the *Arrow–Debreu*world. In our multi-agent economy, each single agent has to maximize expected utility, subject to individual wealth constraints. Thus, agent *m*'s problem is

$$\max_{|C_m\rangle} U_m[C_m] \quad \text{subject to} \quad \begin{bmatrix} 1 & \langle \psi | \end{bmatrix} |C_m\rangle = w_m. \tag{5.37}$$

We further assume that the *von Neumann–Morgenstern*-utility functional is the time separable version (5.5) on page 80, and all agents are risk averse. These assumptions are in fact unnecessarily restrictive, but they ensure that the first order conditions of the constraint maximization problem are sufficient. Following the *Lagrange*-formalism, we get agent *m*'s first order condition

$$\frac{\delta U_m}{\delta |C_m\rangle} - \lambda_m \left[1 \quad \langle \psi | \right] \stackrel{!}{=} \langle 0 |, \tag{5.38}$$

and after trivial rearrangement

$$\frac{\delta U_m}{\delta |C_m\rangle} = \lambda_m^* \left[ 1 \quad \langle \psi | \right]. \tag{5.39}$$

Recognize that λ ∗ *<sup>m</sup>* is always positive, because it represents agent *m*'s marginal utility of consumption at *t* = 0.

**Quick calculation 5.8** Provide a formal argument for the last statement.

Now let's turn to the whole financial economy. Define a candidate for the so-called social welfare functional

$$U[C] = \sum_{m=1}^{M} \frac{1}{\lambda_m^*} U_m[C_m]$$
(5.40)

to be maximized with respect to an aggregated wealth constraint,

$$\max_{|C_1\rangle,\dots,|C_M\rangle} U[C] \quad \text{subject to} \quad \sum_{m=1}^M \left[1 \quad \langle \psi | \right] |C_m\rangle = W, \tag{5.41}$$

with *W* = ∑*<sup>M</sup> <sup>m</sup>*=<sup>1</sup> *wm*. It turns out that this is the right guess. Because all λ ∗ *<sup>m</sup>* are positive, first order conditions are still sufficient.

**Quick calculation 5.9** Write the *Lagrange*-function of problem (5.41).

From the *Lagrange*-formalism we now have  $M$  first order conditions of the form

$$\frac{1}{\lambda_m^*} \frac{\delta U}{\delta |C_m\rangle} - \lambda \left[ 1 \quad \langle \psi | \right] \stackrel{!}{=} \langle 0 |. \tag{5.42}$$

There is a unique solution to this problem, if we can find one single  $\lambda^*$ , satisfying all  $M$  first order conditions (5.42). To this end, use the individual requirement (5.39) for a utility maximum of agent  $m$ , to obtain the aggregated first order condition

$$(1 - \lambda^*) \left| 1 \quad \langle \psi \right| = \langle 0|. \tag{5.43}$$

Now it is clear that  $\lambda^* = 1$  solves them all. This means that the social welfare func- $(5.40)$  can be understood as the expected utility functional of some representative agent.

**Quick calculation 5.10** Show that  $U[C] = \sum_{m=1}^{M} \frac{\alpha}{\lambda_m^*} U_m[C_m]$ , with  $\alpha > 0$ , is also an admissible social welfare functional.

Maximizing a social welfare functional results in a *Pareto*-optimal allocation. The converse is also true, if the allocation is *Pareto*-optimal, then a representative agent has realized a maximum in an aggregated expected utility functional (see Hens and Rieger, 2010, p. 190). Large parts of financial economics rely heavily on the analysis of representative agents. At least it makes life a lot easier in many situations.

## 5.5

# Market Completeness and Replicating Portfolios

Complete markets have another pleasant property; the state price form is unique. We will learn later, why uniqueness of state prices does not survive when markets are incomplete. At the moment let's focus on a concrete consequence of this fact: In a complete market, every payoff can be replicated by a portfolio of traded securities. This principle is often stated equivalently as every payoff is attainable. If there is no arbitrage, the price of the replicating portfolio has to be equal to the price of the security it replicates. Otherwise you could sell one short and buy the other, and make a riskless profit.

Let's start the discussion at our initial definition of completeness. We found earlier that a security market is complete, if D contains a full set of  $\Omega$  linearly independent securities. This means technically, we can pick any set of  $\Omega$  linearly independent securities we like, and use them as basis for the payoff space. Let's call this collection  $D^*$ and the associated security prices  $\langle s^*|$ . Of course all implications of the fundamental theorem of asset pricing have to hold for this special collection of securities, too, in particular

$$\langle s^*| = \langle \psi|D^*.\tag{5.44}$$

Now let's ask a few very interesting questions. First of all, what is the price of a security  $S_{\omega}$  with payoff  $|e_{\omega}\rangle$ , which means one  $c_0$ -unit in state  $\omega$ , and zero otherwise? Obviously,

for the replicating portfolio we must have |*e*ω⟩ = *D*<sup>∗</sup> |θω⟩. Because *D*<sup>∗</sup> is an invertible square matrix, we obtain

$$|\theta_{\omega}\rangle = D^{*-1}|e_{\omega}\rangle. \tag{5.45}$$

But what is the price of this portfolio? It is of course the price of each basis-security times its quantity, ⟨*s* ∗ |θω⟩. So let's put the pieces together,

$$\langle s^*|\theta_\omega\rangle = \langle \psi|D^*D^{*-1}|e_\omega\rangle = \langle \psi|e_\omega\rangle = \psi_\omega. \tag{5.46}$$

Isn't that nice? *S*<sup>ω</sup> is called an *Arrow–Debreu*-security. The payoffs of all *Arrow– Debreu*-securities form an orthonormal basis of the payoff space and the state price form collects the associated *Arrow–Debreu*-prices.

Here is another interesting question. What is the price of a security *B*0, with payoff |1⟩, which means a payoff of one *c*0-unit in every possible state of the world? Following our own footsteps, we obtain

$$\langle s^*|\theta_0\rangle = \langle \psi|1\rangle = \sum_{\omega=1}^{\Omega} \psi_{\omega}.$$
 (5.47)

This one seems to be a little more intricate. Think about what it means, if a security pays off one *c*0-unit, no matter what state of the world will be realized. It means that we are dealing with a riskless security. To be a little more precise, *B*<sup>0</sup> is a riskless zerocoupon bond. But we know that today's price of such a security has to be (1 + *r*) −1 , where *r* is the risk-free rate of return from *t* = 0 to *t* = *T*. Thus we can conclude that

$$r = \frac{1}{\sum_{\omega=1}^{\Omega} \psi_{\omega}} - 1. \tag{5.48}$$

**Quick calculation 5.11** Verify the last equation.

Obviously, an arbitrage free and complete market determines a risk-free interest rate. This fact is true, whether a zero-coupon bond is traded or not. In the latter case, *r* is called a shadow risk-free interest rate.

In a complete market, we can replicate arbitrary payoffs, and in the process assign unique arbitrage free prices to the respective securities. Here is an example:

**Example 5.3**

Consider the financial market, determined by the payoff matrix and security price form

$$D = \begin{pmatrix} 1 & 4 & 2 \\ 2 & 0 & 4 \end{pmatrix} \quad \text{and} \quad \langle s| = \begin{pmatrix} 1 & 2 & 2 \end{pmatrix}.$$

There is a new security *S*<sup>4</sup> introduced into the market, with payoff vector

|*d*4⟩ = ( 3 2 ) .

How can *S*<sup>4</sup> be replicated and what is its arbitrage free price?

Solution

It is easy to see that the first two payoff vectors in *D* are linearly independent. We can thus use them as a basis

$$D^* = \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix}.$$

From this, we immediately conclude that

$$|\theta_4\rangle = \begin{pmatrix} 1 \\ \frac{1}{2} \end{pmatrix}$$

solves the problem |*d*4⟩ = *D*<sup>∗</sup> |θ4⟩. The fair price of security *S*<sup>4</sup> is thus

$$s_4 = \langle s^* | \theta_4 \rangle = \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ \frac{1}{2} \end{pmatrix} = 2.$$

Because we can pick a basis arbitrarily, there is more than one replicating portfolio. But all of them have to have the same price, otherwise an arbitrage opportunity would be present.

**Quick calculation 5.12** Verify that using the second and third security in Example 5.3 as a basis, results in a different replicating portfolio, but in the same price for *S*4.

Here comes the big question: What if the market is incomplete? To answer this one, we have to go back to the fundamental theorem of asset pricing. More precisely, to the linear subspace, spanned by all possible arbitrage free configurations of security prices and payoffs

$$M = \left\{ m : |m\rangle = \begin{bmatrix} -\langle s| \\ D \end{bmatrix} |\eta\rangle, \ \eta \in \mathbb{R}^N \right\}.$$
 (5.49)

If the market is complete, *M* is an Ω-dimensional linear subspace of R Ω+1 , like in Figure 5.4 on page 87. If the market is incomplete, *M* is a linear subspace of lower dimension. The situation is illustrated in Figure 5.6. Here, *M* is a one-dimensional linear subspace, a line, in which all payoffs are situated. The separating hyperplane theorem guarantees the existence of a form, orthogonal to every vector in *M*, but it does not guarantee its uniqueness. Indeed, there is a continuum of forms, compatible with the consequences of the separating hyperplane theorem. Two of them are indicated in Figure 5.7. What are the implications of this ambiguity? First of all,

![](_page_16_Figure_1.jpeg)

**Fig. 5.6** 3D Incomplete market – Dimension of subspace *M* is smaller than Ω

we have

$$\langle L| = \begin{bmatrix} 1 & \langle \psi| \end{bmatrix} \tag{5.50}$$

and thus, the state price form itself is not unique. But that is to say, the price of an arbitrary security is not unique, because the relation

$$s_n = \langle \psi | d_n \rangle \tag{5.51}$$

still holds. The truly remarkable fact is that all those different prices are fair, in that they do not allow arbitrage opportunities. You may be puzzled about the last statement. How can there be two different prices for the same security, but no arbitrage opportunity? If you think it through, there are not only two possible prices, but a whole continuum of prices, as there is a continuum of possible linear functionals and state price forms. You can observe the consequences in real markets, which are doubtlessly

![](_page_16_Figure_8.jpeg)

**Fig. 5.7** 3D Incomplete market – Linear subspace *M* with alternative forms ⟨*L*1| and ⟨*L*2|

incomplete, in form of bid–offer spreads. Now you recognize how arbitrage is prevented, despite a whole interval of fair prices. You have to buy at the highest fair price, but can sell only at the lowest fair price.

We can summarize the major consequences of market incompleteness in two statements. First, the state price form is not unique and thus, there is more than one arbitrage free security price. Second, because there is no complete basis contained in *D*, we cannot find a replicating portfolio for an arbitrary security *Sn*. The last statement is often expressed equivalently by observing that not all payoffs are attainable. Perfect replication is thus an exclusive feature of complete markets. On the other hand, every security with non-attainable payoff and observable price, traded in an incomplete market, adds an additional dimension to the linear subspace *M* and thus, brings the market closer to completeness.

## **5.6 Martingale Measures and Duality**

We are now heading towards a duality that is at the heart of quantitative finance. It will reveal its full potential in derivative pricing, but it is built deep into the structure of financial markets. We have already seen some of its building blocks. So essentially, there is only one new ingredient, the notion of martingales. The term martingale originates from horse racing. In probability theory, a martingale describes a fair game. A stochastic process *X<sup>t</sup>* is called a martingale, if

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$E[X_{t+s}|\mathcal{F}_t] = X_t \tag{5.52}$$

holds, for *s* ≥ 0. Of course we assumed that *X<sup>t</sup>* is adapted to the filtration F*<sup>t</sup>* , but that is not the point here. What (5.52) says is that the best prediction for the value the random variable *X* may take tomorrow, is the value observed today. In other words, a martingale is completely unpredictable.

A duality is understood as a different but completely equivalent formal description of a certain issue. In a manner of speaking dual theories represent two sides of one coin. In our case, the coin is the state price form, and we have already seen one side, replication. In a complete market, the state price form is unique, and we can price any state contingent security with known payoff |*dn*⟩ by a replicating portfolio |θ*n*⟩,

$$s_n = \langle s^* | \theta_n \rangle = \langle \psi | d_n \rangle. \tag{5.53}$$

We have also seen that replicating a zero-coupon bond *B*<sup>0</sup> gives rise to a (shadow) risk-free rate of return

$$1 + r = \frac{1}{\sum_{\omega=1}^{\Omega} \psi_{\omega}}.$$
 (5.54)

Let's define a new quantity *q*ω, with

$$q_{\omega} = \frac{\psi_{\omega}}{\sum_{k=1}^{\Omega} \psi_k} \tag{5.55}$$

and analyze it a little bit. Obviously, *q*<sup>ω</sup> > 0 holds for ω= 1, . . . , Ω, because all state prices ψ<sup>ω</sup> are positive. Furthermore, we have

$$\sum_{\omega=1}^{\Omega} q_{\omega} = 1. \tag{5.56}$$

Does that remind you of something? The quantities *q*<sup>ω</sup> have precisely the properties we would expect from a discrete set of probabilities. Let's go one step further. Divide and multiply the right hand side of (5.53) by (5.54) and use (5.55)

$$s_n = \frac{1}{1+r} \sum_{\omega=1}^{\Omega} d_{\omega n} q_{\omega} = \frac{1}{1+r} E^{\mathcal{Q}}[d_n]. \tag{5.57}$$

**Quick calculation 5.13** Verify the first equality in (5.57).

The probability measure *Q*, under which the expectation value in (5.57) is taken, is called an equivalent martingale measure. The expectation value of the future payoff under the measure *Q* is the value of the security today, apart from a discounting factor. Hence the name. It is also called a risk-neutral probability measure, because only the risk-neutral agent would ignore utility and focus only on the expected payoff.

What happens, if the market is incomplete? We know replication breaks down and securities have no longer unique arbitrage free prices. If pricing under the equivalent martingale measure represents a genuine duality, we can expect trouble. The definition of *q*<sup>ω</sup> in (5.55) provides the key. The *q*s are normalized versions of the state prices, and if state prices are not unique, neither are the *q*s. This means, in incomplete markets, we can expect a continuum of equivalent martingale measures. The old problem in a new guise.

## **5.7 Further Reading**

The starting point of the discussion in this chapter is the classic competitive equilibrium of Arrow and Debreu (1954). A concise review can be found in Dybvig and Ross (2003); a comprehensive source is Lengwiler (2004). Original work about the fundamental theorem of asset pricing and equivalent martingale measures is due to Harrison and Kreps (1979) and Harrison and Pliska (1981). A technical exposition including multi-period extensions is found in Elliott and Kopp (2005, chap. 3). A full scale mathematical treatment of the whole subject is provided in Duffie (2003), as well as in Delbaen and Schachermayer (2006). A financial economics' perspective can be found in Cochrane (2005).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

# Problems

5.1 Assume that *von Neumann–Morgenstern*-utility is a time separable functional of the form

$$U[C] = u(c_0) + e^{-\rho T} \sum_{\omega=1}^{\Omega} u(c_{\omega}) p_{\omega}.$$

Show that the price of an arbitrary security can be written as expectation value

$$s_n = E[Md_n],$$

where the random variable  $M$  is called the stochastic discount factor (SDF), and is given by

$$M = e^{-\rho T} \frac{u'(C)}{u'(c_0)}.$$

5.2 Use a zero-coupon bond to show that the expectation value of the stochastic discount factor in Problem 5.1 is

$$E[M] = \frac{1}{1+r}$$

5.3 Show that the risk premium of a security with state contingent payoff  $|d_n\rangle$  is given by  $\text{Cov}[M, d_n]$ . Use the relation

$$Cov[X, Y] = E[XY] - E[X]E[Y]$$

in the process.

**5.4** Consider the payoff matrix

$$D = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 1 & 4 \end{pmatrix}.$$

Check if the financial market is complete, and whether or not any cyclical permutation of the security price form

$$\langle s| = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$$

results in an arbitrage free market.

5.5 Imagine a financial market with one zero-coupon bond and one stock. The riskfree rate of interest over one period of time is  $r = 25\%$  and the initial value of the stock is  $S_0 = 10$ . There are two possible states of the world at  $t = 1$ , say "up" and "down," and the stock takes values

$$S_1(\omega) = \begin{cases} 15 & \text{if } \omega = \uparrow \\ 5 & \text{if } \omega = \downarrow \, . \end{cases}$$

Now a call option on the stock is introduced into the market. Its payoff function is

$$C_1 = \max(S_1 - K, 0),$$

with exercise price *K* = \$13. Compute the risk-neutral probabilities and the fair price *C*<sup>0</sup> of the derivative contract.

**5.6** Consider the same financial market as in Problem 5.5. Imagine at *t* = 0 an agent forms the portfolio

$$\Pi_0 = \frac{1}{5}S_0 - C_0.$$

What is the payoff Π<sup>1</sup> of this portfolio and which security does it replicate? Can you derive the fair price *C*<sup>0</sup> from the replicating portfolio?
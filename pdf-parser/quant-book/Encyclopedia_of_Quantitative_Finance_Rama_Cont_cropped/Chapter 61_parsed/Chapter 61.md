# **Risk Aversion**

An agent is risk averse if he/she dislikes the actions whose outcomes are not certain. In the following, only actions with one-dimensional final outcomes, for example, sums of money, are taken into consideration. To define risk aversion, it is necessary that a probability is associated to every possible consequence, that is, that the actions can be represented as lotteries. A lottery is *simple* if all possible consequences are final outcomes (sums of money) and it is *compound* if other lotteries are included among its consequences. An outcome coincides with a degen*erate* lottery, that is, the lottery that generates it with probability one.

Formally, a decision-making situation under risk is represented by the quintuple  $\langle S; 2^S; p; X; \mathcal{L} \rangle$ , where S is a set of states of the nature;  $2^S$  is its power set (i.e., the set of all subsets of  $S$ , the empty set included); p is a probability distribution on  $2^S$ ; X is a set of outcomes (with  $X \subseteq \mathbb{R}$  if they are onedimensional); and  $\mathcal{L}$  is the set of lotteries. A simple lottery is represented by  $\ell = (x(E), p(E))_{E \in \text{Part}(S)}$ , where outcomes and probabilities are associated with the events  $E \subseteq S$  that form a partition  $Part(S)$  of *S*; a compound lottery by  $\ell = (\ell(E), p(E))_{E \in Part(S)}$ , with  $\ell(E) = (\ell'(E'), p(E'))_{E' \in \text{Part}(E)}$ ; and a degenerate lottery by  $\ell = (x, 1)$ . A simple lottery is also represented by the cumulative probability function  $F: X \to [0, 1]$ , where  $F(.)$  is a nondecreasing function with range [0,1], and, if S is finite, that is,  $S =$  $\{s_1, \ldots, s_m\}$ , by  $\ell = (x_i, p_i)_{i=1}^n$ , where  $p_i = p(E_i)$ with  $E_i = \{s_h \in S : x(s_h) = x_i\}$ . An agent in a risky situation is a system of preferences  $\langle \mathcal{L}, \gtrsim \rangle$  over the set of lotteries. Let  $\langle \mathcal{L}, \gtrsim \rangle$  be regular (i.e., complete and transitive) and continuous. Moreover, let it be strongly monotone with respect to degenerate lotteries, that is,  $(x, 1) \succ (x', 1)$  if  $x > x'$ . Then, preferences can be represented by a utility function  $U$ :  $\mathcal{L} \to \mathbb{R}$ , that is, such that  $U(\ell) \geq U(\ell')$  if and only if  $\ell \gtrsim \ell'$ . This function is not necessarily the expected utility function. However, if the expected utility model is introduced, then every lottery is equivalent to a simple lottery because of the *compound lottery principle* (implied by expected utility), according to which any compound lottery is indifferent to the simple (or reduced) lottery that associates to each final outcome its compound probability, and preferences are represented by the expected utility function,

which is represented by  $EU(\ell) = \int_{x_i \in X} u(x) dF(x)$  if  $F(.)$  is differentiable or  $EU(\ell) = \sum_{i=1}^{n} p_i u(x_i)$  if the lottery is finite. The von Neumann-Morgenstern (or Bernoulli) utility function  $u: X \to \mathbb{R}$  represents the preferences over the set of degenerate lotteries, that is, over the set of outcomes.

**Definition 1** (*Expected Value*). The expected value of a lottery  $\ell \in \mathcal{L}$  is  $EV(\ell) = \int_{x \in X} x \mathrm{d}F(x)$  or, if the lottery is finite,  $EV(\ell) = \sum_{i=1}^{n} p_i x_i$  and the function  $EV: \mathcal{L} \to X$  is the expected value function.

**Definition 2** (Certainty Equivalent). The certainty equivalent  $CE(\ell)$  of a lottery  $\ell \in \mathcal{L}$  is the outcome for which the individual is indifferent between this outcome and the lottery, that is,  $(CE(\ell), 1) \sim \ell$ , where  $(CE(\ell), 1)$  is the degenerate lottery with out*come*  $CE(\ell)$ *. Having*  $U(\ell) = u(CE(\ell))$ *, the certainty* equivalent function is  $CE(\ell) = u^{-1}(U(\ell))$ . If the system of preferences  $\langle \mathcal{L}, \gtrsim \rangle$  can be represented by an expected utility function, then  $CE(\ell) = u^{-1}(EU(\ell)).$ 

**Proposition 1** (Existence and Uniqueness of the Certainty Equivalent). Let us assume that the set of outcomes is compact, that is,  $X = [x, \overline{x}]$  and the system of preferences  $\langle \mathcal{L}, \geq \rangle$  is regular (i.e., complete and transitive), continuous and such that  $(\overline{x}, 1) \geq \ell \geq$  $(x, 1)$  for every  $\ell \in \mathcal{L}$ . Then, there exists one and only one certainty equivalent  $CE(\ell) \in X$  for every  $\ell \in \mathcal{L}$ .

The following discussion on the notion of risk aversion refers, for the sake of simplicity, to finite simple lotteries on a compact set of outcomes, where not specified differently.

#### **Global Risk Aversion**

**Definition 3** (Risk Premium and Global Risk Aversion). The risk premium  $RP(\ell)$  of a lottery is the maximum sum of money that the agent is willing to pay to get the expected value of the lottery in place of the lottery. Therefore,

$$RP(\ell) = EV(\ell) - CE(\ell) \tag{1}$$

since the conditions  $(EV(\ell) - RP(\ell), 1) \sim \ell$  and  $\ell \sim (CE(\ell), 1)$  imply  $EV(\ell) - RP(\ell) = CE(\ell)$ . The agent denotes (global) risk aversion if his/her system of preferences  $\langle \mathcal{L}, \geq \rangle$  requires  $CE(\ell) \leq$  $EV(\ell)$ , so  $RP(\ell) \ge 0$ , for every  $\ell \in \mathcal{L}$ . The agent is risk loving if  $RP(\ell) \leq 0$  and risk neutral if  $RP(\ell) =$ 0. He/she is strictly risk averse if  $RP(\ell) > 0$  for every nondegenerate  $\ell \in \mathcal{L}$  (strictly risk loving if  $RP(\ell) < 0$ ). An agent is globally neither risk averse nor risk loving if there is a pair  $\ell, \ell' \in \mathcal{L}$  for which  $RP(\ell) > 0$  and  $RP(\ell') < 0$ .

Proposition 2 [5]. Let us introduce the set of the lotteries that are not preferred to the certain outcome  $x$  and the set of lotteries that have an expected value not higher than  $x$ , that is,

$$G(x) = \{ \ell \in \mathcal{L} : CE(\ell) \le x \},$$
  
$$H(x) = \{ \ell \in \mathcal{L} : EV(\ell) \le x \}$$
(2)

The agent is risk averse if and only if  $H(x) \subseteq$  $G(x)$  for every  $x \in X$ , risk loving if and only if  $H(x) \supseteq G(x)$ , and risk neutral if and only if  $H(x) =$  $G(x)$ .

In the Hirshleifer-Yaari diagram, where simple lotteries with only two possible outcomes with given probabilities are represented, the certainty equivalent of a lottery  $\ell^* = (x_1^*, p; x_2^*, 1-p)$  is, by definition, determined as the intersection of the  $45^{\circ}$  line and the corresponding indifference curve. Therefore, the certainty equivalent is equal to the coordinates of this point. Moreover, the expected value of the same lottery is equal to the coordinates of the point where the  $45^{\circ}$  line intersects the expected value line (described by the equation  $px_1 + (1 - p)x_2 = EV(\ell^*) = px_1^* + (1 - p)x_2^*$  $p)x_2^*$ ). This line passes through  $\ell^*$  and has the slope equal to  $-\frac{p}{1-p}$ . Thus, the agent is risk averse if the first intersection point is not above the second one, as shown in Figures 1 and 2.

Proposition 2 indicates that risk aversion implies  $H(CE(\ell^*)) \subseteq G(CE(\ell^*))$ . It means that the indifference curve and the expected value line passing through the same point on the  $45^{\circ}$  line do not cross and that the indifference curve is to the north-east with respect to the expected value line.

**Proposition 3** If the expected utility model applies, then the agent is risk averse if and only if his/her von *Neumann–Morgenstern utility function*  $u : X \to \mathbb{R}$  *is* concave, risk loving if and only if it is convex, and risk neutral if and only if it is a linear.

![](_page_1_Figure_8.jpeg)

Figure 1 Indifference curve of a risk averse expected utility agent

![](_page_1_Figure_10.jpeg)

Figure 2 Indifference curve of a risk averse nonexpected utility agent

The inequality  $\sum_{i=1}^{n} p_i u(x_i) \leq u \left(\sum_{i=1}^{n} p_i x_i\right)$ , which is called the *Jensen inequality*, is a definition of concavity and is equivalent to  $EU(\ell) \leq u(EV(\ell)).$ 

In Figure 3 we can see how the concavity of the function  $u(.)$  implies risk aversion. The expected value, expected utility, and certainty equivalent are represented for the lottery  $\ell = (x_1, 0.5; x_2, 0.5)$ .

The concavity of the von Neumann–Morgenstern function  $u(.)$  implies the concavity of the expected utility function with respect to the outcomes. That is, if  $u(\lambda x_i + (1 - \lambda)x_i') \ge \lambda u(x_i) + (1 - \lambda)u(x_i')$ for every pair  $x_i, x_i' \in X$  and every  $\lambda \in [0, 1]$ ,

![](_page_2_Figure_1.jpeg)

Figure 3 Risk aversion and concavity of utility function

then  $EU(\ell'') \ge \lambda EU(\ell) + (1 - \lambda)EU(\ell')$  for every  $\lambda \in [0, 1]$  and every triplet  $\ell, \ell', \ell'' \in \mathcal{L}$ , with  $\ell =$  $(x_i, p_i)_{i=1}^n$ ,  $\ell' = (x'_i, p_i)_{i=1}^n$  and  $\ell'' = (x''_i, p_i)_{i=1}^n$ . Thus, if the agent is risk averse and the expected utility theory holds, the function  $EU(.)$  is concave (and, all the more so, quasiconcave) with respect to the outcomes. Consequently, the indifference curves in the Hirshleifer-Yaari diagram are convex (as described in Figure 1, but not in Figure 2, which can represent an agent who is risk averse but does not maximize expected utility).

Proposition 4 [5]. The agent is risk averse if the certainty equivalent function  $CE: \mathcal{L} \rightarrow X$  is convex with respect to the probabilities. The agent is risk loving if it is concave and risk neutral if it is linear.

The condition stated in Proposition 4 for risk aversion is sufficient, but not necessary, nor is it necessary that the certainty equivalent function  $CE(.)$  is quasiconvex with respect to the probabilities. However, if the expected utility theory holds and there is risk aversion, then the certainty equivalent function is convex with respect to the probabilities: in fact, in such a case, we have  $CE(\ell) = u^{-1} \left( \sum_{i=1}^{n} p_i u(x_i) \right)$ , where function  $u(.)$  is increasing and concave and function  $u^{-1}$ (.) is increasing and convex.

**Definition 4** (Comparison of Risk Aversion across Agents). An agent  $A$  is more risk averse than agent

*B* if their systems of preferences  $\langle \mathcal{L}, \geq^A \rangle$  and  $\langle \mathcal{L}, \geq^B \rangle$ give  $CE_A(\ell) \leq CE_B(\ell)$  for every  $\ell \in \mathcal{L}$ .

In the Hirshleifer-Yaari diagram, this definition implies that the indifference curves of the agents that go through the same point on the  $45^{\circ}$  line do not cross and that the indifference curve of the more risk averse agent is to the north-east with respect to the indifference curve of the less risk averse agent, as shown in Figure 4.

**Proposition 5** [7]. If agent  $A$  is more risk averse than agent  $B$  and the expected utility model applies,

![](_page_2_Figure_10.jpeg)

Figure 4 Indifference curves of two agents of whom one is more risk averse than the other

then the von Neumann-Morgenstern utility function  $u_A(.)$  is a concave transformation of  $u_B(.)$ . That is, there exists an increasing and concave function  $g$ :  $\mathbb{R} \to \mathbb{R}$  such that  $u_A(x) = g(u_B(x))$  for every  $x \in X$ .

## **Local Risk Aversion**

Till now, we considered *global risk aversion*, that is, the relationship  $CE(\ell) \leq EV(\ell)$  was introduced for every lottery  $\ell \in \mathcal{L}$ . Now, let us consider *local risk aversion*, by taking into account only small lotteries, that is, the lotteries that have only little differences in consequences. For this purpose, we denote the lottery  $(x + tx_i, p_i)_{i=1}^n$  with  $x + t\ell$ , where  $\ell = (x_i, p_i)_{i=1}^n$ .

Definition 5 (Local Risk Aversion). An agent is locally risk averse, if, for every  $x \in X$  and  $\ell \in \mathcal{L}$ , there exists a  $t^* > 0$  such that  $CE(x + t\ell) <$  $EV(x + t\ell)$  for all  $t \in [0, t^*]$ . Thus, if the certainty equivalent function can be derived, then the agent is locally risk averse if  $\lim_{t \to 0} \frac{\mathrm{d}}{\mathrm{d}t} (EV(x+t\ell) - CE(x+t\ell)) > 0$  and only if  $\lim_{t \to 0} \frac{\mathrm{d}}{\mathrm{d}t} (EV(x+t\ell) - CE(x+t\ell)) \ge 0$  for every  $x \in X$  and  $\ell \in \mathcal{L}$ . By analogy, the definition holds with reversed inequality signs for the local risk loving.

Although the global risk aversion requires that in the Hirshleifer-Yaari diagram the indifference curve and the expected value line passing through some point on the  $45^{\circ}$  line do not cross and that the indifference curve is to the north-east with respect to the expected value line, this condition needs to be satisfied only in the vicinity of the  $45^{\circ}$  line for the local risk aversion.

**Proposition 6** If the expected utility theory holds, then the agent is locally risk averse if and only if his/her von Neumann-Morgenstern utility function  $u: X \to \mathbb{R}$  is concave. In other words, if the expected utility theory holds, then the conditions for local and global risk aversion (risk loving or neutrality) are the same.

# **Measure of the Risk Aversion**

If the expected utility theory holds, then the local risk aversion can be measured by the concavity of the von Neumann–Morgenstern utility function  $u(.)$ . However, the second derivative of the utility function

 $u''(.)$ , which is a measure of its concavity, is not invariant to increasing linear transformations of  $u(.)$ . An invariant measure is the *de Finetti-Arrow-Pratt* coefficient of risk aversion (due to de Finetti [3], Pratt [7], and Arrow [1]). This measure of (*absolute*) risk *aversion* is defined as

$$r(x) = -\frac{u''(x)}{u'(x)}$$
(3)

There also exists a measure of relative risk aversion  $r_r(x) = -x \frac{u''(x)}{u'(x)}$ , which is important in the case of multiplicative lotteries  $\ell = (\alpha_i W, p_i)_{i=1}^n$ .

The de Finetti-Arrow-Pratt measure can be justified in relation to the local risk premium, which is (by Definition 3)

$$RP(x+t\ell) = EV(x+t\ell) - CE(x+t\ell)$$
  
=  $x + tEV(\ell)$   
 $- u^{-1} \left( \sum_{i=1}^{n} p_i u(x+tx_i) \right)$  (4)

Then, assuming that this function is differentiable with respect to t, we get  $RP(x) =$ 0,  $\frac{\partial RP(x+t\ell)}{\partial t}\Big|_{t=0} = 0$  and  $\frac{\partial^2 RP(x+t\ell)}{\partial t^2}\Big|_{t=0} = 0$  $-\frac{u''(x)}{u'(x)}\sigma^2(\ell)$ . Therefore, in the neighborhood of the certain outcome  $x$ , the risk premium is proportional to the de Finetti-Arrow-Pratt measure. Nevertheless, the fact that only the second derivative of the risk premium can be different from zero at  $t = 0$ , while the first derivative is always equal to zero, means that the expected utility theory allows only for local risk aversion of the second order, while that of the first order is zero. Other theories (e.g., rank-dependent expected *utility*, which is discussed later) also allow for the risk aversion of the first order and can, as a result, describe the preferences that indicate more relevant types of aversion to risk (like the one presented in Allais paradox) than the risk aversion admitted by the expected utility theory and measured by the de Finetti-Arrow-Pratt index.

Local risk aversion in the Hirshleifer-Yaari diagram is linked to the curvature of indifference curves at the point where they intersect the 45° line. In other words, it is linked to the value of the second derivative  $x_2''(x_1)$  at  $x_1 = x$ , where

the function  $x_2(x_1)$  that represents the indifference curve is implicitly defined by the condition  $CE(x_1, x_2) = x$ . Then, if the expected utility theory holds, we get  $x_2(x) = x, x_2'(x) = -\frac{p}{1-p}$  and  $x_2''(x) = -\frac{p}{(1-p)^2} \frac{u''(x)}{u'(x)}$ , that is, the curvature of the indifference curves along the  $45^{\circ}$  line is proportional to the de Finetti-Arrow-Pratt measure of risk aversion.

The dependence of the de Finetti-Arrow-Pratt index  $r(x)$  on x defines the decreasing absolute risk aversion if  $r'(x) < 0$  (increasing if  $r'(x) > 0$ ), as well as, with regard to  $r_r(x)$ , the decreasing relative risk aversion if  $r_r'(x) < 0$  (increasing if  $r_r'(x) > 0$ ).

#### Aversion Toward Increases in Risk

Risk aversion can also be analyzed taking into account the riskiness of lotteries, that is, considering preference for less risky lotteries. However, there does not exist a unique definition of riskiness according to which lotteries can be ordered. In the following, only two definitions of riskiness are examined. Both introduce a partial ordering criterion.

1. The first definition refers to mean preserving spreads (introduced by Rothschild and Stiglitz [10]). A lottery  $\ell = (x_i, p_i)_{i=1}^n$  is not less risky than lottery  $\ell^* = (x_i^*, p_i^*)_{i=1}^n$  if  $\ell$  can be obtained from  $\ell^*$  by mean preserving spreads. That is, if  $EV(\ell) = EV(\ell^*), x_i = x_i^*$  for every  $i =$  $1, \ldots, n$  and  $p_i = p_i^*$  for every  $i = 1, \ldots, n$ except for three outcomes  $x_a > x_b > x_c$ , for which we have  $p_a \ge p_a^*$ ,  $p_b \le p_b^*$ , and  $p_c \ge$  $p_c^*$ . For example,  $\ell = (x_1, p_1; x_2, p_2; x_3, p_3)$  is not less risky than  $\ell^* = (x_1, p_1^*; x_2, p_2^*; x_3, p_3^*)$ <br>if  $p_2 \le p_2^*$ ,  $p_1 = p_1^* + \frac{x_2 - x_3}{x_1 - x_3}(p_2^* - p_2)$ ,  $p_3 = p_3^* + \frac{x_1 - x_2}{x_1 - x_3}(p_2^* - p_2), \text{ and } x_1 > x_2 >$  $x_3$ .

**Definition 6** (Aversion to Mean Preserving Spreads Increases in Risk). An agent is averse to the increases in risk if  $CE(\ell) \leq CE(\ell^*)$  for every pair of lotteries  $\ell, \ell^* \in \mathcal{L}$  with  $\ell$  not less risky than  $\ell^*$  (according to mean preserving spreads).

**Proposition 7** If an agent is averse to mean preserving spreads increases in risk, then he/she is also risk averse (for this reason, sometimes the aversion to mean preserving spreads increases in risk is

called strong risk aversion and the risk aversion as introduced in Definition 3 is called weak risk aversion [2]). To be precise, if  $CE(\ell) \leq CE(\ell^*)$  for every pair  $\ell, \ell^* \in \mathcal{L}$  with  $\ell$  not less risky than  $\ell^*$  (according to mean preserving spreads), then  $CE(\ell) \leq EV(\ell)$  for  $\text{ every } \ell \in \mathcal{L}.$ 

**Proposition 8** If the expected utility model applies, then there is aversion toward mean preserving spreads increases in risk if and only if the von *Neumann–Morgenstern utility function*  $u: X \to \mathbb{R}$  *is* concave.

Note that the concavity of the utility function is a necessary and sufficient condition for both risk aversion and aversion to increases in risk (determined by mean preserving spreads). The equality of this condition holds in the case of expected utility theory. For other theories, we will generally have two different conditions (one for risk aversion and the other for the aversion to increases in risk).

An ordering of the lotteries according to their riskiness that is equivalent to the mean preserving spreads concept (for the lotteries that have equal expected value) is provided by the notion of the second-order stochastic dominance.

**Definition 7** (*First-order Stochastic Dominance*). A lottery  $\ell = (x_i, p_i)_{i=1}^n$ , where  $x_i > x_{i+1}$  for every  $i = 1, \ldots, n - 1$ , first order stochastically dominates lottery  $\ell' = (x_i, p_i')_{i=1}^n$  if  $\sum_{h=1}^i p_h \ge \sum_{h=1}^i p_{h'}$  (or, equivalently,  $\sum_{h=i+1}^n p_h \le \sum_{h=i+1}^n p_{h'}$ ) for every  $i =$  $1, \ldots, n-1$ , that is, with respect to the cumulative probability functions (introduced earlier), if  $F(x) \leq$  $F'(x)$  for every  $x \in X$ .

First-order stochastic dominance means that probabilities of the better (worse) outcomes are higher (lower) in the dominant lottery than in the dominated lottery. It implies that  $EV(\ell) > EV(\ell')$  and, also,  $CE(\ell) \geq CE(\ell')$  for a rational agent.

**Definition 8** (Second-order Stochastic Dominance). A lottery  $\ell = (x_i, p_i)_{i=1}^n$ , where  $x_i > x_{i+1}$  for every  $i = 1, \ldots, n-1$ , second order stochastically dominates lottery  $\ell' = (x_i, p_i')_{i=1}^n$  if  $D_j(\ell, \ell') = \sum_{i=1}^{n-1}$  $(x_i - x_{i+1}) \sum_{h=1}^j (p_h - p_h') \ge 0 \text{ for every } j = 1, \ldots,$  $n-1$ , that is, with respect to the cumulative probability functions in the continuous case, if  $\int_{x}^{x} (F(t) F'(t)$ dt  $\leq 0$  for every  $x \in X = [\underline{x}, \overline{x}]$ . The first-order

![](_page_5_Figure_1.jpeg)

Figure 5 Probability mixture of two lotteries

stochastic dominance implies second-order stochastic dominance, but not vice versa.

**Proposition 9** Let two lotteries  $\ell$  and  $\ell'$  have the same expected value, so that  $\sum_{i=1}^{n-1} (x_i - x_{i+1})$  $\sum_{h=1}^{j} (p_h - p_h') = 0$ . If the lottery  $\ell'$  is more risky than  $\ell$  (according to the mean preserving spreads criterion), then  $\ell$  second-order stochastically dominates  $\ell'$ . Conversely, if  $\ell$  second-order stochastically dominates  $\ell'$ , then  $\ell'$  can be obtained from  $\ell$  by a sequence of mean preserving spreads.

The equivalence of the second-order stochastic dominance and mean preserving spreads for the lotteries with the same expected value implies that the same conditions that determine the aversion to the increases in risk (introduced by mean preserving spreads) also determine the aversion for the lotteries that are second-order stochastically dominated (in comparison between lotteries of the same expected value).

2. The second definition of riskiness refers to *prob*ability mixtures [11]. According to this definition, a compound lottery is, *ceteris paribus*, more risky than a simple lottery. More precisely, let us define as a probability mixture of two simple lotteries  $\ell_a = (x_a(s_j), p(s_j))_{j=1}^m$  and  $\ell_b = (x_b(s_j), p(s_j))_{j=1}^m$ , where  $S = \{s_1, \dots, s_m\}$  is the set of the states of the nature, the two-stages lottery  $\lambda \ell_a \oplus (1 - \lambda) \ell_b = (((x_a(s_i), \lambda), (x_b(s_i),$  $(1 - \lambda)$ ,  $p(s_j)_{j=1}^m$ , where  $\lambda \in [0, 1]$ . Figure 5 represents the simplest case of a probability mixture.

Definition 9 (Aversion to Probability Mixture Increases in Risk). An agent is averse to the increases in risk if  $CE(\lambda \ell_a \oplus (1-\lambda)\ell_b) \le \max\{CE(\ell_a), CE(\ell_b)\}$ *for every pair of lotteries*  $\ell_a, \ell_b \in \mathcal{L}$  *and*  $\lambda \in [0, 1]$ *.* 

Note that the expected utility model implies neutrality toward probability mixture increases in risk, since this model satisfies the compound lottery principle, according to which  $EU(\lambda \ell_a \oplus (1-\lambda)\ell_b) =$  $\lambda EU(\ell_a) + (1 - \lambda)EU(\ell_b).$ 

# **Risk Aversion and Aversion to** Increasing Risk with Regard to **Rank-dependent Expected Utility**

Let us take into consideration a generalization of expected utility theory in order to show some aspects of risk aversion and aversion to increasing risk, which appear very different from the case of expected utility.

**Definition 10** (*Rank-dependent Expected Utility [8*, 4]). The system of preferences  $\langle \mathcal{L}, \gtrsim \rangle$  is represented by rank-dependent expected utility  $U: \mathcal{L} \to \mathbb{R}$  if, for every lottery  $\ell \in \mathcal{L}$  with  $\ell = (x_i, p_i)_{i=1}^n$  and  $x_i > x_{i+1}$ for every  $i = 1, \ldots, n-1$ , where  $x_i \in X$  with  $X =$  $[x,\overline{x}] \subset \mathbb{R}$ , we have

$$U(\ell) = u(x_n) + \sum_{i=1}^{n-1} (u(x_i) - u(x_{i+1}))\varphi\left(\sum_{h=1}^{i} p_h\right)$$
(5)

where function  $u: X \to \mathbb{R}$  represents the system of preferences  $\langle X, \gtrsim \rangle$  over the set of outcomes and function  $\varphi : [0, 1] \rightarrow [0, 1]$ , which is increasing, with  $\varphi(0) = 0$  and  $\varphi(1) = 1$ , distorts the decumulative probability function.

Thus, the rank-dependent expected utility model describes the agent's system of preferences by means of a utility function on outcomes and a probability distortion function (while the expected utility model requires only the first function). Note that, when

the probability distortion function is the identity function, that is, when  $\varphi(p) = p$  for every  $p \in [0, 1]$ , then rank-dependent expected utility coincides with expected utility.

Recalling that an agent is risk averse if  $CE(\ell) \leq$  $EV(\ell)$  for every  $\ell \in \mathcal{L}$ , that is, if the risk premium  $RP(\ell) = EV(\ell) - CE(\ell)$  is nonnegative for every  $\ell \in \mathcal{L}$ , let us split the risk premium  $RP(\ell)$  into two parts: first-order risk premium  $RP_1(\ell) = CE_{\text{EII}}(\ell)$  - $CE(\ell)$  (with  $CE_{\text{EU}}(\ell) = u^{-1} \left( \sum_{i=1}^{n} p_i u(x_i) \right)$ ) and second-order risk premium  $RP_2(\ell) = EV(\ell)$  –  $CE_{\text{EII}}(\ell)$ .

**Proposition 10** [6]. Let  $\langle \mathcal{L}, \geq \rangle$  be represented by rank-dependent expected utility. There is first-order risk aversion, that is,  $RP_1(\ell) = CE_{EII}(\ell) - CE(\ell) >$ 0 for every  $\ell \in \mathcal{L}$ , if and only if probability distortion function  $\varphi : [0, 1] \rightarrow [0, 1]$  is such that  $\varphi(p) < p$  for every  $p \in [0, 1]$ . The agent exhibits second-order risk aversion, that is,  $RP_2(\ell) = EV(\ell) - CE_{\text{EU}}(\ell) > 0$ for every  $\ell \in \mathcal{L}$ , if and only if the utility function  $u: X \to \mathbb{R}$  is concave. As a consequence, an agent is risk averse, that is,  $RP(\ell) = EV(\ell) - CE(\ell) \ge$ 0 for every  $\ell \in \mathcal{L}$ , if  $\varphi(p) \leq p$  for every  $p \in [0, 1]$ and  $u: X \to \mathbb{R}$  is concave. In essence, the condition  $\varphi(p) \leq p$  means that the agent overstates the probabilities of some bad outcomes and understates the probabilities of some better outcomes. Because of the *probability distortion, rank-dependent expected utility* admits first-order risk aversion, therefore allowing for a significant risk aversion even when stakes are small, contrary to expected utility [9]. This may be relevant in finance applications when the agent's choice concerns lotteries in which a small amount of wealth is involved.

**Proposition 11** Let  $\langle \mathcal{L}, \gtrsim \rangle$  be represented by rankdependent expected utility. The agent is locally risk averse if the probability distortion function  $\varphi$ :  $[0, 1] \rightarrow [0, 1]$  is such that  $\varphi(p) < p$  for every  $p \in$  $(0, 1)$  and only if  $\varphi(p) \leq p$ .

In other words, if the rank-dependent expected utility theory holds, then the condition for local risk aversion concerns only the probability distortion function. (As a consequence, the de Finetti-Arrow-Pratt coefficient of risk aversion, which has as its object the utility function  $u(.)$ , is of no importance in the case of rank-dependent expected utility.)

Another interesting point is that the firstorder derivative of risk premium  $RP(x + t\ell)$  with

![](_page_6_Figure_7.jpeg)

Figure 6 Risk premium function of a risk averse agent

![](_page_6_Figure_9.jpeg)

Figure 7 Indifference curve of a risk averse rankdependent expected utility agent

respect to  $t$  is generally nonzero and discontinuous at  $t = 0$ . For example, if  $n = 2$  and  $x_1 >$ uous at  $t = 0$ . For example, if  $n = 2$  and  $x_1 > x_2$ , we get  $\lim_{t \to 0^+} \frac{\partial RP(x+t\ell)}{\partial t} = (x_1 - x_2)(p_1 - \varphi(p_1))$  and  $\lim_{t \to 0^+} \frac{\partial RP(x+t\ell)}{\partial t} = (x_1 - x_2)(p_2 - \varphi(p_2))$ . (However, the expected utility theory would yield  $\lim_{t \to$ a risk averse agent, where  $\tan \alpha = (x_1 - x_2)(p_1 \varphi(p_1)$  and  $\tan \beta = (x_1 - x_2)(p_2 - \varphi(p_2))$ . The curve  $RP_{\text{EU}}(t)$  represents the same function when the expected utility theory holds. In the Hirshleifer-Yaari diagram (Figure 7), the indifference curves have a kink at  $x_1 = x_2$ , with  $\lim_{x_1 - x_2 \to 0^+} \frac{dx_2(x_1)}{dx_1} =$ 

 $\frac{\varphi(p_1)}{1-\varphi(p_1)}=\tan \quad \gamma \quad \text{and} \quad \lim_{x_1-x_2\to 0^-} \frac{\mathrm{d}x_2(x_1)}{\mathrm{d}x_1}=$  $\frac{\varphi(p_2)}{1-\varphi(p_2)}=\tan\delta.$ 

If the expected utility theory is valid, then both risk aversion and aversion toward increases in risk (introduced with mean preserving spreads) come from the same condition, which is concavity of the von Neumann-Morgenstern utility function (Propositions 3 and 8). These conditions are different when the rankdependent expected utility theory holds. Moreover, a rank-dependent expected utility agent may exhibit aversion to probability mixture increases in risk, while the expected utility agent is always neutral.

**Proposition 12** Let  $\langle \mathcal{L}, \geq \rangle$  be represented by rankdependent expected utility. Then, an agent is averse toward (mean preserving spreads) increases in risk if the function  $\varphi : [0, 1] \rightarrow [0, 1]$  is convex and the function  $u: X \to \mathbb{R}$  is concave. He/she is averse toward (probability mixtures) increases in risk if and only if the function  $\varphi : [0, 1] \rightarrow [0, 1]$  is convex.

# References

- Arrow, K.J. (1965). Aspects of the Theory of Risk-[1] Bearing, Yrjö Jahnssonin Sāātiö, Helsinki.
- Cohen, M.D. (1995). Risk-aversion concepts in [2] expected- and non-expected-utility models, Geneva Papers on Risk and Insurance Theory 20, 73-91.
- de Finetti, B. (1952). Sulla preferibilità, Giornale degli [3] Economisti NS 11, 685-709.

- Machina, M.J. (1987). Choice under uncertainty: [4] problems solved and unsolved, Economic Perspectives 1, 121-154.
- Montesano, A. (1999). Risk and uncertainty aversion on [5] certainty equivalent functions, in Beliefs, Interactions and Preferences in Decision Making, M.J. Machina & B. Munier, eds, Kluwer, Dordrecht, pp. 23-52.
- [6] Montesano, A. (1999). Risk and uncertainty aversion with reference to the theories of expected utility. rank dependent expected utility, and Choquet expected utility, in Uncertain Decisions: Bridging Theory and *Experiments*, L. Luini, ed, Kluwer, Boston, pp. 3–37.
- [7] Pratt, J.W. (1964). Risk aversion in the small and in the large, Econometrica 32, 122-136.
- [8] Ouiggin, J. (1982). A theory of anticipated utility, Journal of Economic Behavior and Organization 3. 323-343.
- Rabin, M. (2000). Risk aversion and expected utility [9] theory: a calibration theorem, *Econometrica* **68**,  $1281 - 1292$ .
- [10] Rothschild, M. & Stiglitz, J.E. (1970). Increasing risk: I. A definition, *Journal of Economic Theory* 2, 225–243.
- Wakker, P.P. (1994). Separating marginal utility and [11] probabilistic risk aversion, Theory and Decision 36,  $1 - 44$

# **Related Articles**

Ambiguity: Behavioral Portfolio Selection; **Expected Utility Maximization;** Risk-Return Analysis; Utility Function.

ALDO MONTESANO
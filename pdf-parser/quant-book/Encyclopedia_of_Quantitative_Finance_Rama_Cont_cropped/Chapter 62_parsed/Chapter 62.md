## **Ambiguity**

In the literature on decision making under uncertainty, *ambiguity* is now consistently used to define those decision settings in which an economic agent perceives "[*...*] uncertainty about probability, created by missing information that is relevant and could be known" [17]. Other terms have been used interchangeably, notably "Knightian uncertainty," based on Knight's [32] distinction between "risk" (a context in which all the relevant "odds" are known and unanimously agreed upon) and "uncertainty" (a context in which some "odds" are not known). The term *ambiguity*, which avoids charging uncertainty with too many meanings, was introduced in [12], the paper that first showed how ambiguity represents a normative criticism to Savage's [38] subjective expected utility (SEU) model.

Ellsberg proposed two famous thought experiments involving choices on urns in which the exact distribution of ball colors is unknown (one of which was anticipated in both [29] and [32]). A variant of Ellsberg's so-called two-urn paradox is the following example, due to David Schmeidler. "Suppose that I ask you to make bets on two coins, one taken out of your pocket—a coin, which you have flipped countless times—the other taken out of my pocket. If asked to bet on 'heads' or on 'tails' on one of the two coins, would you rather bet on your coin or mine?" Most people, when posed this question, announce a mild but strict preference for betting on their own coin rather than on somebody else's, *both for heads and for tails*. The rationale is precisely that their coin has a well-understood stochastic behavior, while the other person's coin does not; that is, its behavior is *ambiguous*. The possibility that the coin be biased, although remote, cannot be dismissed altogether. This pattern of preference is called *ambiguity aversion*, and is, as suggested, very common ([6, p. 646] e.g., references many experimental replications of the "paradox".) It is easy to see that it is not compatible with the SEU model. For, suppose that a decision maker has a probabilistic prior *P* over the state space *S* = {*HH , HT, TH , TT*} (where *H T* is the state in which the familiar coin lands heads up and the unfamiliar coin lands tails up, etc.). Then, by saying that he/she prefers a bet that pays off ¤1 if the familiar coin lands heads up—that is, a bet on the event *A* = {*HH , HT*}—to the bet that pays ¤1 if the unfamiliar coin lands heads up—that is, a bet on the event *B* = {*HH , TH* }—an SEU decision maker reveals that

$$u(1) P(A) + u(0) (1 - P(A)) > u(1) P(B)$$
  
+  $u(0) (1 - P(B))$  (1)

that is, *P (A) > P (B)*. Analogously, by preferring the bet on tails on the familiar coin to the bet on tails on the unfamiliar coin, an SEU decision maker reveals that

$$P({TH, TT}) = P(Ac) = 1 - P(A) > 1 - P(B)$$
$$= P(Bc) = P({HT, TT})$$
(2)

that is, *P (A) < P (B)*: a contradiction. Yet, few people would immediately describe these preferences as being an example of irrationality. Ellsberg reports that Savage himself chose in the manner described above, and did not feel that his choices were clearly wrong [12, p. 656]. (Indeed, Savage was aware of the issue well before Ellsberg proposed his thought experiments, for Savage wrote in the *Foundations of Statistics* (pp. 57–58) that "there seem to be some probability relations about which we feel relatively 'sure' as compared to others," adding that he did not know how to make such notion of comparatively "sure" less vague.)

Ellsberg's paper generated quite a bit of debate immediately after its publication (most of which is discussed in Ellsberg's PhD dissertation [13]), but the lack of axiomatically founded models that could encompass a concern for ambiguity while retaining most of the compelling features of the SEU model worked to douse the flames. Moreover, the so-called *Allais paradox* [2], another descriptive failure of expected utility, which predated Ellsberg's by a few years, monopolized the attention of decision theorists until the early 1980s. However, statisticians such as Good [23] and Arthur Dempster [9] did lay the foundations of statistics with sets of probabilities, providing analysis and technical results, which eventually made it into the toolbox of decision theorists.

## **Models of Ambiguity-sensitive Preferences**

The interest in ambiguity as a reason for departure from the SEU model was revived by David Schmeidler, who proposed and characterized axiomatically two of the most successful models of decision making in the presence of ambiguity, the *Choquet expected utility (CEU)* and the *maxmin expected utility* (*MEU*) models.

CEU [39] "resolves" the Ellsberg paradox by allowing a decision maker's willingness to bet on an event to be represented by a set-function that is not necessarily additive; that is, a *v*, which, to disjoint events *A* and *B*, may assign *v(A* ∪ *B)* -= *v(A)* + *v(B)*. More precisely, call a *capacity* any function *v* defined on a *σ*-algebra  of subsets of a state space *S*, which satisfies the following properties: (i) *v(*∅*)* = 0, (ii) *v(S)* = 1, (iii) for any *A, B* ∈  such that *A* ⊆ *B*, *v(A)* ≤ *v(B)*. (Note that a *probability (charge)* is *v*, which satisfies instead of (iii) the property *v(A* ∪ *B)* = *v(A)* + *v(B)* − *v(A* ∩ *B)* for any *A, B* ∈ *-*.) It is simple to see that if *v* represents a decision maker's beliefs, we may observe the preferences described above in the two-coin example. Just substitute *P* in equations (1) and (2) with *v* satisfying *v(A)* = *v(Ac)* = 1*/*2 and *v(B)* = *v(Bc)* = 1*/*4. The obvious question is that of defining expectations for a notion of "belief", which is not a measure. As the model's name suggests, Schmeidler used the notion of integral for capacities, which was developed by Choquet [8]. Formally, given a capacity space *(S, -, v)* and a *-* measurable function *a* : *S* → , the *Choquet integral of a with reference to (w.r.t.) v* is given by the following formula:

$$\int_{S} a(s) \, \mathrm{d}v(s) \equiv \int_{0}^{\infty} v(\{s \in S : a(s) \ge \alpha\}) \, \mathrm{d}\alpha$$
$$+ \int_{-\infty}^{0} [v(\{s \in S : a(s) \ge \alpha\}) - 1] \, \mathrm{d}\alpha \tag{3}$$

This is shown to correspond to Lebesgue integration when the capacity *v* is a probability. Schmeidler provided axioms on a decision maker's preference relation , which guarantee that the latter is represented by the Choquet expectation w.r.t. *v* of a real-valued utility function *u* (on final prizes *x* ∈ *X*). Precisely, given choice options (acts) *f, g* : *S* → *X*,

$$f \succcurlyeq g \Longleftrightarrow \int_{S} u(f(s)) \, \mathrm{d}v(s) \ge \int_{S} u(g(s)) \, \mathrm{d}v(s) \tag{4}$$

That is, the decision maker prefers *f* to *g* whenever the Choquet integral of *u*°*f* is greater than that of *u*°*g*. The interested reader is referred to Schmeidler's paper for details of the axiomatization. For our purpose, it suffices to observe that, not too surprisingly, the key axiomatic departure from SEU (in the variant due to [3]) is a relaxation of the independence axiom—or what Savage calls the *sure-thing principle*—which is the property of preferences that the Ellsberg-like preferences above violate.

Not all capacities give rise to behavior which is averse to ambiguity, as in the above example. Schmeidler proposed the following behavioral notion of aversion to ambiguity. Assuming that the payoffs *x* can themselves be (objective and additive) lotteries over a set of certain prizes, define for any *α* ∈ [0*,* 1] the *α-mixture* of acts *f* and *g* as follows: for any *s* ∈ *S*,

$$(\alpha f + (1 - \alpha)g)(s) \equiv \alpha f(s) + (1 - \alpha)g(s) \quad (5)$$

where the object on the right-hand side is the lottery that pays off prize *f (s)* with probability *α* and prize *g(s)* with probability *(*1 − *α)*. Now, say that a preference satisfies *ambiguity hedging* (Schmeidler calls this property *uncertainty aversion*) if for any *f* and *g* such that *f* ∼ *g* we have

$$\alpha f + (1 - \alpha)g \succcurlyeq f \tag{6}$$

for any *α*. That is, the decision maker *may* prefer to "hedge" the ambiguous returns of two indifferent acts by mixing them appropriately. This makes sense if we consider two acts whose payoff profiles are negatively correlated (over *S*), so that the mixture has a payoff profile, which is flatter, hence less sensitive to the information on *S*, than the original acts. (Ghirardato and Marinacci [20] discuss ambiguity hedging, arguing that it captures more than just the ambiguity aversion of equations 1 and 2.) Schmeidler shows that a CEU decision maker satisfies ambiguity hedging if and only if her capacity *v* is *supermodular*; that is, for any *A, B* ∈ *-*,

$$v(A \cup B) \ge v(A) + v(B) - v(A \cap B) \qquad (7)$$

Ambiguity hedging also plays a key role in the second model of ambiguity-sensitive preferences proposed by Schmeidler, the MEU model introduced alongside that of Itzhak Gilboa [21]. In MEU, the decision maker's preferences are represented by (a utility function *u* and) a *set C* of probability charges on  $(S, \Sigma)$ —which is nonempty, (weak\*-)closed and  $convex$ —as follows:

$$f \succcurlyeq g \Longleftrightarrow \min_{P \in C} \int_{S} u(f(s)) \, \mathrm{d}P(s)$$
  
 
$$\geq \min_{P \in C} \int_{S} u(g(s)) \, \mathrm{d}P(s) \qquad (8)$$

Thus, the presence of ambiguity is reflected by the nonuniqueness of the prior probabilities over the set of states. In the authors' words, "the subject has too little information to form a prior. Hence, (s)he considers a *set* of priors as possible" [21, p. 142]. In the two-coin example, let  $S$  be the product space  $\{H, T\} \times \{H, T\}$  and consider the set of priors

$$C \equiv \bigcup_{a \in [1/4, 3/4]} \{ \{ 1/2, 1/2 \} \times \{ a, 1 - a \} \} \tag{9}$$

It is easy to see that a decision maker with such a C will "assign" to events A and  $A^c$  the weight  $\min_{P \in C} P(A) = 1/2 = \min_{P \in C} P(A^c)$ , and to events B and  $B^c$  the weight  $\min_{P \in C} P(B) = 1/4 =$  $\min_{P \in C} P(B^c)$ , thus displaying the classical Ellsberg preferences. Gilboa and Schmeidler showed that MEU is axiomatically very close to CEU. While ambiguity hedging is required (being single-handedly responsible for the "min" in the representation; see [19]), a weaker version of independence is used.

Ambiguity hedging characterizes the intersection of the CEU and MEU models. Schmeidler [39] shows that a decision maker's preferences have both CEU and MEU representations if and only if (i) the  $v$  in the CEU representation is supermodular, and (ii) the lower envelope of the set  $C$  in the MEU representation,  $C(\cdot) \equiv \min_{P \in C} P(\cdot)$ , is a supermodular capacity and  $C$  is the set of *all* the probability charges that dominate  $C$  (the *core* of  $C$ ). On the other hand, there are CEU preferences that are not MEU (take a capacity  $v$  which is not supermodular), and MEU preferences that are not CEU (see [30, Example 1]).

The CEU and MEU models brought ambiguity back to the forefront of decision theoretic research, and in due course, as "applications" of such theoretical models started to appear, they were key in attracting the attention of mainstream economics and finance.

On the theoretical front, a number of alternative axiomatic models have been developed. First, there are generalizations of CEU and MEU. For instance, Maccheroni et al. [33] presented a model that they

called variational preferences, which relaxes the independence condition used in MEU while retaining the ambiguity hedging condition. An important special case of variational preferences is the so-called multiplier model of Hansen and Sargent [25], a key model in the applications literature to be discussed later. Siniscalchi [42] proposed a model that he called *vector expected utility*, in which an act is evaluated by modifying its expectation (w.r.t. a "baseline probability") by an adjustment function capturing ambiguity attitudes. Such a model is also built with applications in mind, as it (potentially) employs a smaller number of parameters than CEU and MEU.

Second, Bewley [4] (originally circulated in 1986) suggested that ambiguity might result in incompleteness of preferences, rather than in violation of independence. Under such assumptions, he found a representation in which a set of priors  $C$  appears in a "unanimity" sense as follows:

$$f \succcurlyeq g \Longleftrightarrow \int_{S} u(f(s)) \, \mathrm{d}P(s)$$
$$\geq \int_{S} u(g(s)) \, \mathrm{d}P(s) \text{ for all } P \in C \tag{10}$$

That is, the decision maker prefers  $f$  over  $g$  whenever  $f$  dominates  $g$  according to every "possible scenario" in  $C$ . Preferences are undecided otherwise, and Bewley suggested completing them by following an "inertia" rule: the status quo is retained if undominated by any available act. In a model that joins the two research strands just described, Ghirardato et al. [19] showed that if we drop ambiguity hedging from the MEU axioms, we can still obtain the set of priors  $C$  as a "unanimous" representation of a suitably defined incomplete subset of the decision maker's preference relation, which they interpreted as "unambiguous" preference (i.e., a preference that is not affected by the presence of ambiguity). This yields a model-of which both CEU and MEU are special cases—in which the decision maker evaluates act  $f$  via the functional

$$V(f) = a(f) \min_{P \in C} \int_{S} u(f(s)) \, \mathrm{d}P(s)$$
$$+ (1 - a(f)) \max_{P \in C} \int_{S} u(f(s)) \, \mathrm{d}P(s) \tag{11}$$

where *a(f )* ∈ [0*,* 1] is the decision maker's ambiguity aversion in evaluating *f* (a generalization of the decision rule suggested by Hurwicz [27]).

A third modeling approach relaxes the "reduction of compound lotteries" property that is built within the expected utility model. The basic idea is that the decision maker forms a "second-order" probability *µ* over the set of possible priors over *S*, and that he/she does not reduce the resulting compound probability. That is, he/she could evaluate act *f* by first calculating its expectation *EP (u*°*f )* ≡ *u(f (s))* d*P (s)* with respect to each prior *P* that he/she deems possible, and then computing

$$\int_{\Delta} \phi(E_P(u \circ f)) \, \mathrm{d}\mu(P) \tag{12}$$

where denotes the set of all possible probability charges on *(S, -)*, and *φ* : → is a function, which is not necessarily affine. This is the reasoning adopted by Segal [40], followed by Ergin and Gul [16], Klibanoff *et al.* [31], Nau [37], and Seo [41]. The case of SEU corresponds to *φ* being affine, while Klibanoff *et al.* [31] show that *φ* being concave corresponds intuitively to ambiguity averse preferences. That is, the "external" utility function describes ambiguity attitude, while the "internal" one describes risk attitude. An important feature of such a model is that its representation is smooth (in utility space), whereas those of MEU and CEU are generally not. For this reason, this is called the *smooth ambiguity model*.

In concluding this brief survey of decision models, it is important to stress that, owing to space constraint, the focus is on *static* models. The literature on *intertemporal* models is more recent and less developed, in part, because of the fact that non-SEU preferences often violate a property called *dynamic consistency* [18], making it hard to use the traditional dynamic programming tools. Important contributions in this area are found in [14, 22] (characterizing the so-called *recursive MEU* model) and [24, 34].

## **Applications**

As mentioned above, the CEU and MEU models were finally successful in introducing ambiguity into mainstream research in economics and finance. Many papers have been written, which assume that (some) agents have CEU or MEU preferences. The interested reader is referred to [36] for an extensive survey of such applications, while some applications to finance are briefly discussed here.

In a seminal contribution, Dow and Werlang [10] showed that a CEU agent with supermodular capacity may display a nontrivial bid–ask spread on the price of an (ambiguous) Arrow security, even without frictions. If the price of the security falls within such an interval, the agent will not want to trade the security at all (given an initial riskless position). Epstein and Wang [15] employed the recursive MEU model to study the equilibrium of a representative agent economy *a la Lucas `* . They showed that price indeterminacy can arise in equilibrium for reasons that are closely related to Dow and Werlang's observation. Other contributions followed along this line; for example, see [7, 35, 43]. More recently, the smooth ambiguity model has also been receiving attention; see, for example, [28].

Though originally not motivated by the Ellsberg paradox and ambiguity, the "model uncertainty" literature due to Hansen *et al.* ([26], but more comprehensively found in [25]) falls squarely within the scope of the applications of ambiguity. Moreover, both decision models they employ are special cases of the models described above: the "multiplier model" is a special case of variational preferences, and the "constraint model" is a special case of MEU.

Most of the applications of ambiguity to finance—an exception being [11]—are cast in a representative agent environment, with the preferences of the representative agent satisfying in one case MEU, in another CEU, and so on. Recent work on experimental finance by Bossaerts *et al.* [5] and Ahn *et al.* [1] finds that experimental subjects, when making portfolio choices with ambiguous Arrow securities, display substantial heterogeneity in ambiguity attitudes. Because Bossaerts *et al.* [5] show that such heterogeneity may easily result in a breakdown of the representative agent result, such findings cast some doubt on the generality of a representative agent approach to financial markets equilibrium.

## **References**

- [1] Ahn, D., Choi, S., Gale, D. & Shachar, K. (2007). *Estimating Ambiguity Aversion in a Portfolio Choice Experiment*, UC Berkeley, Mimeo.
- [2] Allais, M. (1953). Le comportement de l'homme rationnel devant le risque: Critique des postulats
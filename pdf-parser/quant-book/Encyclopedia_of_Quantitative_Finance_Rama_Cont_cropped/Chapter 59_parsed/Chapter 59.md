# **Utility Function**

## **Behavior and Preferences**

Modern utility theory studies preference orderings over choice sets and their numerical representations. Consider a decision maker (DM) who has to choose among a set  $X$  of alternatives. The set  $X$  is called the DM's choice set. In the deterministic case, which is our focus here, alternatives are certain, without any uncertainty. For example, in consumer theory, the DM is a consumer and  $X$  is the consumption set that he/she faces, that is, a subset of  $\mathbb{R}^n$  whose elements  $x = (x_1, \ldots, x_n)$  represent the consumption bundles available to consumers. In intertemporal choice problems, X is a subset of  $\mathbb{R}^{\infty}$ , the space of sequences  $\{x_t\}_{t=1}^{\infty}$ , where  $x_t$  is the DM's outcome at time  $t$ . Alternatives become more complicated objects under uncertainty, such as random variables in one-period problems and stochastic processes in intertemporal problems. This more general case is not considered here.

DMs have some preferences over the elements of  $X$ ; they may like some alternatives more than others or may be indifferent among some of them. For example, in consumer theory consumers will rank consumption bundles in their consumption sets according to their tastes.

This motivates the introduction of preference orderings  $\succeq$  defined on the choice set X. The ordering  $\succeq$  has the following interpretation: for any two vectors x and y in X, we write  $x \succeq y$  if the DM either strictly prefers  $x$  to  $y$  or is indifferent between the two.

The ordering  $\succeq$  is the basic primitive of the theory. The following two relations are derived from  $\succeq$ :

- 1. for any two vectors x and y in X, we write  $x \succ y$ if the DM strictly prefers x to y. Formally,  $x \succ y$ if  $x \succeq y$ , but not  $y \succeq x$ ;
- 2. for any two vectors  $x$  and  $y$  in  $X$ , we write  $x \sim y$  if the DM is indifferent between x and y. Formally,  $x \sim y$  if both  $x \succeq y$  and  $y \succeq x$ .

On the preference ordering  $\succeq$ , which is the theory's "raw material," some properties are considered.

Axiom 1 (Transitivity). For any three elements x, y, and z in X, if  $x \succeq y$  and  $y \succeq z$ , then  $x \succeq z$ .

Transitivity is a rationality assumption. Its violation generates cycles, for example,  $x \succeq y \succeq z \succ x$ . The most troublesome consequence of such cycles is that there might not exist a best element in the choice set X. For example, suppose that  $X = \{x, y, z\}$  and that  $x \succ y$  and  $y \succ z$ . If transitivity is violated, we get the cycle  $x \succ y \succ z \succ x$  and there is no best element in  $X$ .

Axiom 2 (Completeness). For any two elements  $x$ and y in X,  $x \succeq y$ ,  $y \succeq x$ , or both.

This is a simple, but not innocuous, property. A DM's preference  $\succeq$  satisfies this property if, when faced with any two alternatives in  $X$ , he/she can always say which one he/she prefers. As alternatives may be very different, this might be a strong requirement (see [1, 6], for weakenings of this assumption).

Note that Axiom 2 implies reflexivity, that is,  $x \succeq$ x for all  $x \in X$ . When  $\succeq$  is reflexive and transitive (e.g., when it satisfies Axioms 1 and 2), following the consumer theory terminology, we call indifference curves the equivalence classes  $[x] = \{y \in X : y \sim x\}$ for any  $x \in X$ . We denote the collection  $\{ [x] : x \in X \}$ X} of all indifference curves by  $X/\sim$ , which is a partition of X. That is, each  $x \in X$  belongs to one, and only one, indifference curve.

Axioms 1 and 2 do not depend on any particular structure of the set  $X$ . In most applications, however, X is a subset of an ordered vector space  $(V, \geq)$ , that is, of a space  $V$  that has both a vector and an order structure. The space  $\mathbb{R}^n$  endowed with the natural order  $>$  is an important example of an ordered vector space. Given any  $x, y \in \mathbb{R}^n$ , when the vectors x and y are regarded as consumption bundles,  $x \ge y$  means that the bundle  $x$  has at least as much of each good than the bundle  $y$ , while the convex combination  $\alpha x + (1 - \alpha)y$  is interpreted as a mix of the two vectors (implicitly we are assuming that goods are suitably divisible).

The following axioms are based on the order and vector structures of  $X$ . For simplicity, we assume  $X \subseteq \mathbb{R}^n$ , though most of what follows holds in more general ordered vector spaces with units. Here,  $x > y$ means  $x \ge y$  and  $x \ne y$  (i.e.,  $x_i > y_i$  for at least some  $i = 1, \ldots, n$ .

**Axiom 3 (Monotonicity).** For any two elements  $x$ and y in  $X \subseteq \mathbb{R}^n$ , if  $x > y$ , then  $x \succ y$ .

This axiom connects the order  $\geq$  on X and the DM's preference relation  $\succeq$ . In the context of consumer theory, it says that "the more, the better." In particular, given two vectors x and y with  $x \ge y$ , it is enough that  $x$  has strictly more of at least some good  $i$  to be strictly preferred to  $y$ . This means that all goods are "essential" that is, the DM pays attention to each of them. Moreover, observe that, by Axiom 3 and reflexivity,  $x \geq y$  implies  $x \succeq y$ . This is because  $x \ge y$  if either  $x = y$  or  $x > y$ .

The following two axioms rely on the vector structure of  $X$ .

Axiom 4 (Archimedean). Suppose that  $x$ ,  $y$ , and *z* are any three elements of a convex  $X \subseteq \mathbb{R}^n$  such that  $x \succ y \succ z$ . Then there exist  $\alpha, \beta \in (0, 1)$  such that  $\alpha x + (1 - \alpha)z \succ y \succ \beta x + (1 - \beta)z$ .

According to this axiom, there are no infinitely preferred or infinitely despised alternatives. That is, given any pairs  $x \succ y$  and  $y \succ z$ , alternative x cannot be infinitely better than y, and alternative z cannot be infinitely worse than  $y$ . Indeed, we can always mix  $x$ and z to get better alternatives, that is,  $\alpha x + (1 - \alpha)z$ , or worse alternatives, that is,  $\beta x + (1 - \beta)z$ , than y.

It may be useful to remember the analogous property that holds for real numbers: if  $x$ ,  $y$ , and z are real numbers with  $x > y > z$ , then there exist  $\alpha, \beta \in (0, 1)$  such that  $\alpha x + (1 - \alpha)z > y > \beta x +$  $(1 - \beta)z$ . This property does not hold any more if we consider  $\infty$  and  $-\infty$ , that is, the extended real line  $\mathbb{R} = [-\infty, \infty]$ . Specifically, let  $x = \infty$  or  $z = -\infty$ . In this case,  $x$  is infinitely larger than  $y$ ,  $z$  is infinitely smaller than y, and there are no  $\alpha, \beta \in (0, 1)$  that satisfy the previous inequality. In fact,  $\alpha \infty = \infty$  and  $\beta(-\infty) = -\infty$  for all  $\alpha, \beta \in (0, 1)$ .

Axiom 5 (Convexity). Given any two elements  $x$ and y of a convex set  $X \subseteq \mathbb{R}^n$ , if  $x \sim y$  then  $\alpha x +$  $(1-\alpha)y \succeq x \text{ for all } \alpha \in [0,1].$ 

This axiom captures a preference for mixing: given any two indifferent alternatives, the DM always prefers any of their combination to each of the original alternatives. This preference for mixing is often assumed in applications and is a convexity property of indifference curves,<sup>a</sup> the modern counterpart of the classic assumption of diminishing marginal utility.

Summing up, we have introduced a few properties that are often assumed on the preference  $\succeq$ . All these axioms are behavioral, that is, they are expressed

in terms of choice behavior. In particular, their behavioral meaning is transparent and, with the exception of the Archimedean axiom, they are all behaviorally falsifiable by suitable choice patterns. For example, one can show that a DM does not satisfy the transitivity axiom by finding alternatives  $x, y, z \in X$  over which his/her choices exhibit the cycle  $x \succeq y \succeq z \succ x$ . This choice pattern would be enough to reject the hypothesis that his/her preference over  $X$  is transitive.

The use of preference axioms that have a transparent behavioral interpretation and that are falsifiable through choice behavior is the main methodological tenet of modern utility theory, often called the revealed preference methodology. In fact, choice behavior data are regarded as the only observable data that economic theories can rely upon.

Another important methodological feature of modern utility theory is that it adopts a weak notion of rationality, which requires only the consistency of choices without any demand on their motives. For example, transitivity is viewed as a rationality requirement in this sense because its violations would entail inconsistent patterns of choices that no DM would consciously follow, regardless of his/her motivations (see [15], for a recent discussion of this methodological issue).

#### **Paretian Utility Functions**

Although the preference ordering  $\succsim$  is the fundamental notion, for analytical convenience it is often of interest to find a numerical representation of  $\succeq$ . Such numerical representations are called *utility functions*; formally, a real-valued function  $u: X \to \mathbb{R}$  is a (*Paretian*) utility function if, for any pair  $x, y \in X$ ,

> $x \succeq y$  if and only if  $u(x) \ge u(y)$  $(1)$

In particular, for the derived relations  $\succ$  and  $\sim$  it holds, respectively,  $x \succ y$  if and only if  $u(x) > u(y)$ and  $x \sim y$  if and only if  $u(x) = u(y)$ . Indifference curves can thus be written in terms of utility functions as  $[x] = \{y \in X : u(y) = u(x)\}.$ 

Utility functions are analytically very convenient, but do not have any intrinsic psychological meaning: what matters is that they numerically rank vectors in the same way as the preference ordering  $\succeq$ . This implies, *inter alia*, that every monotone transformation of a utility function is still a utility function, that is, utility functions are invariant under monotone transformations. To see why this is the case, let  $u(X) = \{u(x) : x \in X\} \subseteq \mathbb{R}$  be the range of u and  $f: u(X) \to \mathbb{R}$  a (strictly) monotone function, that is,  $t > s$  implies  $f(t) > f(s)$  for any scalars  $t, s \in u(X)$ . Clearly,  $x \succeq y$  if and only if  $(f \circ u)(x) \ge (f \circ u)(y)$  for any pair  $x, y \in X$ , and this shows that the transformation  $f \circ u$  is still a utility function.

**Example 1** A classic utility function  $u : \mathbb{R}^2_{++} \to \mathbb{R}$ is the Cobb-Douglas utility function:

$$u(x, y) = x^{a}y^{1-a}$$
 with  $0 \le a \le 1$  (2)

Suppose a preference  $\succsim$  is represented by a Cobb-Douglas utility function. Then,  $\succeq$  is also represented by the following monotone transformations of *u*:

1.  $\lg(u(x, y)) = \lg(x^a y^{1-a}) = a \lg x + (1 - a)$  $\lg y;$ 

2. 
$$\sqrt{u(x, y)} = \sqrt{x^a y^{1-a}} = x^{\frac{a}{2}} y^{\frac{1-a}{2}}$$
; and  
3.  $u(x, y)^3 = x^{3a} y^{3(1-a)}$ .

In view of this invariance under monotone transformations, the utility theory presented here is often called *ordinal utility theory*. Observe that in this ordinal theory, utility differences such as  $u(x) - u(y)$  are of no interest. This is because inequalities such as  $u(x) - u(y) > u(z) - u(w)$  have no meaning in this setup: given any such inequality, it is easy to come up with monotone transformations  $f: \mathbb{R} \to \mathbb{R}$  such that  $(f \circ u)(x) - (f \circ u)(y) < (f \circ u)(z) - (f \circ u)(w)$ . An important consequence of this observation is that incremental ratios of utility functions defined on subsets of  $\mathbb{R}^n$  have no interest, except for their sign. For example, the classic notion of decreasing marginal utility, which is based on properties of the partial derivatives  $\partial u(x)/\partial x_k$ , is thus meaningless in ordinal utility theory.

In applications, utility functions  $u: X \to \mathbb{R}$  are often used in optimization problems

$$\max_{x \in C} u(x) \tag{3}$$

where  $C$  is a suitable subset of the choice set  $X$ , determined by possible constraints that limit the DM's choices. For example, in consumer theory,  $C$ 

is given by the budget set

$$C = \left\{ x \in X : \sum_{i=1}^{n} p_i x_i \le w \right\} \tag{4}$$

where w is the consumer's wealth and each  $p_i$  is the price per unit of good  $i$ .

It is immediately seen that the solutions of the optimization problem (3) are the same, regardless of what monotone transformation of  $u$  is selected to make calculations. On the other hand, all these monotone transformations represent the same preference  $\succeq$  and the solutions reflect only the DM's basic preference  $\succeq$ , not the particular utility function used to represent  $\succeq$ . This further shows that  $\succeq$ is the fundamental notion. The choice of which  $u$  to use, among all equivalent monotone transformations, is only a matter of analytical convenience (e.g., in the Cobb-Douglas case, it is often convenient to use the logarithmic version  $a \lg x + (1 - a) \lg y$ ).

The optimization problems  $(3)$ , which play a key role in economics, also illustrate the analytical importance of utility functions. In fact, a numerical representation of preferences allows to use the powerful methods of optimization theory to find and characterize the solutions of problem (3), which would be otherwise impossible, if we were to only rely on the preference  $\succeq$ . In other words, though the study of the preference  $\succeq$  is what gives ordinal utility theory its scientific status by making it a behaviorally founded and falsifiable theory, it is its numerical representation provided by utility functions that gives the theory its operational content.

Given the importance of utility functions, the main problem of ordinal utility theory is to establish conditions under which the preference ordering  $\succsim$ admits a utility representation. This is not a simple problem. We first state an existence result for the special case when the collection  $X/\sim$  of indifference curves is at most countable.

**Theorem 1** A preference ordering  $\succsim$  defined on a choice set X with  $X/\sim$  at most countable satisfies Axioms 1 and 2 if and only if there exists a function  $u: X \to \mathbb{R}$  such that equation (1) holds.

### **Proof 1** [12] page 14.

Matters are more complicated when the collection  $X/\sim$  is uncountable. It is easy to come up with examples of preferences that satisfy Axioms 1 and 2 and do not admit a utility representation (see Example 2). We refer to  $[2, 12, 18]$  for general representation theorems. Here we establish an existence result for the important special case of preferences defined on  $\mathbb{R}^n$ . based on [3]. It is closely related to Theorems 3.3 and 3.6 of Fishburn (1970). For brevity, we omit its proof.

Write  $x \leq \infty$  (respectively,  $x \geq -\infty$ ) when either  $x \in \mathbb{R}^n$  or  $x_i = \infty$  (respectively,  $x_i = -\infty$ ) for each *i*. That is,  $x \leq \infty$  or  $x \geq -\infty$  means that either each  $x_i$  is finite or each  $x_i$  is infinite. A subset of  $\mathbb{R}^n$  is a closed order interval if, given  $-\infty \leq$  $y < z \leq \infty$ , it has the form  $[y, z] = \{x \in \mathbb{R}^n : y \leq x \leq x \leq x \}$  $x \leq z$  and is an open order interval if it has the form  $(y, z) = \{x \in \mathbb{R}^n : y_i < x_i < z_i \text{ for each } i\}.$ The half-open order intervals  $[y, z)$  and  $(y, z]$  are similarly defined. For example,  $[z, \infty) = \{x \in \mathbb{R}^n :$  $x \geq z$ , and so  $[0, \infty) = \mathbb{R}^n_+$ .

A function  $u: X \to \mathbb{R}$  is *monotone* if  $x > y$ implies  $u(x) > u(y)$  and is *quasiconcave* if its upper sets  $\{x : u(x) > t\}$  are convex for all  $t \in$  $\mathbb{R}$  [16]. Since  $\{y: u(y) \ge u(x)\} = \{y: y \succeq x\}$ , the quasi-concavity of  $u$  implies the convexity of the upper contour sets of indifference curves (cf. End Note a).

**Theorem 2** For a preference ordering  $\succeq$  defined on a order interval  $X \subset \mathbb{R}^n$ , the following conditions are *equivalent:* 

1.  $\succeq$  satisfies Axioms 1–4 and

2. there exists a monotonic and continuous function  $u: X \to \mathbb{R}$  such that equation (1) holds.

Moreover, Axiom 5 holds if and only if u is quasiconcave.

Theorem 2 is an important result. Almost every work in economics contains a utility function, often defined on order intervals of  $\mathbb{R}^n$  and assumed to be monotone and quasi-concave. Theorem 2 shows the behavioral conditions that underlie this key modeling assumption.

By Theorem 2, the convexity axiom 5 is equivalent to the quasi-concavity of the utility function  $u$ . This is a substantially weaker property than the concavity of u, which would require  $u(\alpha x + (1 \alpha(y) \ge \alpha u(x) + (1 - \alpha)u(y)$  for all  $x, y \in X$  and all  $\alpha \in [0, 1]$ . For example, any increasing function u:  $\mathbb{R} \to \mathbb{R}$  is automatically quasi-concave.

Since concave utility functions are often used in applications because of their remarkable properties in optimization problems, a natural question is whether, among all monotone transformations  $f \circ u$  of a quasiconcave utility function  $u$ , there exists a concave one and this would ensure the existence of a concave representation of a preference  $\succeq$  that satisfies Axiom 5. This important question was first studied by de Finetti [11], who showed that there exist quasi-concave functions that do not have any concave monotone transformation. Hence, convex indifference curves are not necessarily determined by a concave utility function (the converse is obviously true) and quasiconcavity in Theorem 2 cannot be improved to concavity. Inter *alia*, the seminal paper of de Finetti started the study of quasi-concave functions, later substantially developed by Fenchel [8], which is arguably the most important generalization of concavity.

Finally, observe that the utility function in Theorem 2 is continuous even though none of the axioms involves any topological notion. This is a remarkable consequence of the order and vector structures that the axioms use.

We close with an example of a preference that does not admit a utility representation.

**Example 2** Lexicographic preferences are a classic example of preference orderings that do not admit a utility representation. Set  $X = \mathbb{R}^2$  and say that  $x \succeq y$ if either  $x_1 > y_1$  or  $x_1 = y_1$  and  $x_2 \ge y_2$ . That is, the DM first looks at the first coordinate: if  $x_1 > y_1$ , then  $x \succeq y$ . However, if  $x_1 = y_1$ , then the DM turns his/her attention to the second coordinate: if  $x_2 \ge y_2$ , then  $x \succeq y$ . This is how dictionaries order words and this motivates the name of this particular ordering. Although they satisfy Axioms  $1-3$ , it can be proved  $(18]$ , pages 24–25) that lexicographic preferences do not admit a utility representation (it is easy to check that they do not satisfy the Archimedean axiom).

## **Brief Historical Remarks**

The early development of utility theory is surveyed in the two 1950 articles of George Stigler [24]. Here it is worth noting that originally utility functions were regarded as a primitive notion whose role was to quantify a Benthamian pain/pleasure calculus. In other words, utility functions were viewed as a measure or a quantification of an underlying physiological phenomenon. This view of utility theory is sometimes called *cardinalism* and utility

functions derived within this approach are called *cardinal utility functions*. A key feature of cardinalism is that utility differences and their ratios are meaningful notions that quantify differences in pain/pleasure that DMs experience among different quantities of the outcomes. In particular, marginal utilities measure the marginal pain/pleasure that results from choices and these played a central role in the early cardinal consumer theory.

However, the difficulty of any reliable scientific measurement of cardinal utility raised serious doubts on the scientific status of cardinalism. At the end of the nineteenth century Pareto revolutionized utility theory by showing that an ordinal approach, based on indifference curves as a primitive notion—unlike Edgeworth [7], who introduced them as level curves of an original cardinal utility function—was enough for consumer theory purposes [20]. In particular, Pareto showed that the classic consumer problem could be solved and characterized by replacing marginal utilities with marginal rates of substitutions along indifference curves. For example, the classic key assumption of diminishing marginal utilities is replaced by the convexity property (Axiom 5) of indifference curves (the latter is actually a stronger property, unless utility functions are separable).

Unlike cardinal utility functions, indifference curves and their properties can be empirically determined and tested. Pareto's insight thus represented a key methodological advance and his ordinal approach, later substantially extended by Hicks and Allen [17, 23], is today the mainstream version of consumer theory. More generally, Pareto's ordinal revolution paved the way to the modern use of preferences as the primitive notion of decision theory. In fact, the use of preferences is the natural conceptual development of Pareto's original insight of considering indifference curves as a primitive notion. The first appearance of preferences as primitive notions seems to be in [9, 13]. They earned their current central theoretical place in decision theory with the classic works [4, 9, 12].

The utility theory under certainty outlined here reached its maturity in the 1960s (see, e.g., [5]). Subsequent work on decision theory has been mainly concerned with choice under uncertainty, extending the scope of the seminal contributions [9, 10, 19, 21, 22]. We refer the reader to [14] for a thorough and updated introduction to these more recent advances.

## **End Notes**

a*.* Observe that this convexity property of indifference curves is weaker than the convexity of their upper contour sets {*y* ∈ *X* : *y x*}.

## **References**

- [1] Aumann, R. (1962). Utility theory without the completeness axiom, *Econometrica* **30**, 445–462.
- [2] Bridges, D.S. & Mehta, G.B. (1995). *Representations of Preference Orderings*, Springer-Verlag, Berlin.
- [3] Cerreia-Vioglio, S., Maccheroni, F., Marinacci, M. & Montrucchio, L. (2009). *Uncertainty Averse Preferences, mimeo*.
- [4] Debreu, G. (1959). *Theory of Value*, Yale University Press.
- [5] Debreu, G. (1964). Continuity properties of Paretian utility, *International Economic Review* **5**, 285–293.
- [6] Dubra, J., Maccheroni, F. & Ok, E.A. (2004). Expected utility theory without the completeness axiom, *Journal of Economic Theory* **115**, 118–133.
- [7] Edgeworth, F.Y. (1881). *Mathematical Psychics: An Essay on the Application of Mathematics to the Moral Sciences*, Kegan Paul, London.
- [8] Fenchel, W. (1953). *Convex Cones, Sets, and Functions*, Princeton University Press, Princeton.
- [9] de Finetti, B. (1931). Sul significato soggettivo della probabilita,` *Fundamenta Mathematicae* **18**, 298–329.
- [10] de Finetti, B. (1937). La prevision: ses lois logiques, ses ´ sources subjectives, *Annales de l'Institut Henri Poincar´e* **7**, 1–68.
- [11] de Finetti, B. (1949). Sulle stratificazioni convesse, *Annali di Matematica Pura ed Applicata* **30**, 173–183.
- [12] Fishburn, P.C. (1970). *Utility Theory for Decision Making*, Wiley, New York.
- [13] Frisch, R. (1926). Sur un problem d'economie pure, ´ *Norsk Matematisk Forenings Skrifter* **1**, 1–40.
- [14] Gilboa, I. (2009). *Theory of Decision under Uncertainty*, Cambridge University Press, Cambridge.
- [15] Gilboa I., Maccheroni, F., Marinacci, M. & Schmeidler, D. (2009). Objective and subjective rationality in a multiple priors model, *Econometrica*, forthcoming.
- [16] Greenberg, H.J. & Pierskalla, W.P. (1971). A review of quasi-convex functions, *Operations Research* **19**, 1553–1570.
- [17] Hicks, J.R. & Allen, R.G.D. (1934). A reconsideration of the theory of value I, II, *Economica* **1**, 52–76, 196–219.
- [18] Kreps, D.M. (1988). *Notes on the Theory of Choice*, Westview Press, London.
- [19] von Neumann, J. & Morgenstern, O. (1947). *Theory of Games and Economic Behavior*, 2nd Edition, Princeton University Press, Princeton.
- [20] Pareto, V. (1906). *Manuale di Economia Politica*, Societa Editrice Libraria, Milano. `
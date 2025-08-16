# **Convex Duality**

**Convex duality** refers to a general principle that allows us to associate with an original minimization program (the *primal problem*) a class of concave maximization concave programs (the *dual problem*), which, under some conditions, are equivalent to the primal. The unifying principles underlying these methods can be traced back to the basic duality that exists between a convex set of points in the plane and the set of supporting lines (hyperplanes). Duality tools can be applied to nonconvex programs too, but are most effective for convex problems.

Convex optimization problems naturally arise in many areas of finance; we mention just few of them (see the list of the related entries at the end of this article): maximization of expected utility in complete or incomplete markets, mean–variance portfolio selection and CAPM, utility indifference pricing, selection of the minimal entropy martingale measure, and model calibration. This short and nonexhaustive list should give a hint of the scope of convex duality methods in financial applications.

Consider the following *primal* minimization (convex) problem:

(P): 
$$\min f(v)$$
  
subject to  $v \in A$  (1)

where *A* is a convex subset of some vector space *V* and *f* : *A* → is a convex function. Convex duality principles consist in pairing this problem with a *dual* maximization (concave) problem:

(D): 
$$\max g(w)$$
 sub  $w \in B$  (2)

where *B* is a convex subset of some other vector space *W* (possibly *W* = *V* ) and *g* : *B* → is a concave function.

In general, by applying a duality principle, we usually try to

- 1. find a lower bound for the value of the primal problem, or, better
- 2. find the value of the primal problem, or, even better
- 3. find the solutions, if any, of the primal problem.

Different duality principles differ in the way the dual problem is built. Two main principles are Lagrange duality and Fenchel duality. Even though they are formally equivalent, at least in the finite-dimensional case, they provide different insights into the problem. We will see below how the Lagrange and Fenchel duality principles practically accomplish the tasks 1 to 3 above.

For the topics to be presented below, comprehensive references are [4] and [1] for the finitedimensional case ([1] also provides an extensive account of numerical methods) and [2] for the infinite-dimensional case.

# **Lagrange Duality in Finite-dimensional Problems**

We consider finite-dimensional problems, that is, *V* = *<sup>N</sup>* for some *N* ≥ 1. We denote *v* · *w* the inner product between two vectors *v, w* ∈ *<sup>N</sup>* and use *v* ≥ 0 as a shorthand for *vn* ≥ 0 ∀*n*. Let *f, h*1*,...,hM* : *C* → be *M* + 1 convex functions, where *C* ⊆ *<sup>N</sup>* is a convex set. Setting *h* = *(h*1*,...,hM )*, so that *h* is a convex function from *C* to *<sup>M</sup>* , we consider, as the primal problem, the minimization of *f* under *M* inequality constraints:

(P): 
$$\min f(v)$$
 sub  $v \in A$   
=  $\{v \in C : h(v) \le 0\} \subset \mathbb{R}^N$  (3)

To build a dual problem, we define the so-called Lagrangian function

$$\mathcal{L}(v, w) := f(v) + w \cdot h(v)$$
  
$$v \in C, \ w \in \mathbb{R}^M$$
(4)

and note that *f (v)* = sup*w*≥<sup>0</sup> L*(v, w)* for any *v* ∈ *A*. As a consequence, we can write the primal problem in terms of L:

(P): 
$$\inf_{v \in C} \sup_{w \ge 0} \mathcal{L}(v, w) \tag{5}$$

The dual problem is then defined by switching the supremum with the infimum

(D): 
$$\sup_{w \ge 0} \inf_{v \in C} \mathcal{L}(v, w)$$
 (6)

In the terminology of the introductory section, the dual problem is then

(D): 
$$\max g(w)$$
 sub  $w \in B$   
=  $\{w \in D : w \ge 0\} \subset \mathbb{R}^M$  (7)

where

$$g(w) = \inf_{v \in C} \mathcal{L}(v, w) \tag{8}$$

and  $D = \{w \in \mathbb{R}^M : g(w) > -\infty\}$  is the domain of  $g$ . It can be proved that  $D$  is a convex set and  $g$ is a concave function on  $D$  even if  $f$  is not convex: therefore *the dual problem is always concave*, even when the primal problem is not convex.

We assume throughout *primal* and *dual feasibility*, that is,  $A$  and  $B$  are assumed to be nonempty. Dual feasibility would however be ensured under Slater conditions for A (see below). Let  $p = \inf_A f$  and  $d = \sup_{B} g$  be the (possibly infinite) values of the primal and the dual. A *primal* (dual) solution is  $\widehat{v} \in A$  $(\widehat{w} \in B)$ , if any, such that  $f(\widehat{v}) = p$   $(g(\widehat{w}) = d)$ ; a *solution pair* is a feasible pair  $(\widehat{v}, \widehat{w}) \in A \times B$  made by a primal and a dual solution.

Lagrange Duality Theorem

# 1. Weak duality

Primal boundedness  $(p > -\infty)$  implies dual boundedness  $(d < +\infty)$  and

$$p \ge d \quad (p - d \ge 0 \text{ is called the duality gap}) \quad (9)$$

Moreover, if there is no duality gap  $(p = d)$ , then  $(\widehat{v}, \widehat{w}) \in A \times B$  is a solution pair if and only if

$$\widehat{w} \cdot h(\widehat{v}) = 0 \quad \text{and} \quad \mathcal{L}(\widehat{v}, \widehat{w}) = g(\widehat{w}) \tag{10}$$

In this case,  $\widehat{w}$  is usually called a Lagrange multipliers vector.

# 2. Strong duality

If, in addition, there exists  $v \in C$  such that  $h_m(v) < 0$ for all m (Slater condition), then there is no duality gap and there exists a dual solution.

See  $[4]$  or  $[1]$  for a proof.

Weak duality, whose proof is trivial, holds under very general conditions: in particular, the primal problem need not be convex. It gives a lower bound for the value of the primal problem, which is useful in many practical situations, "branch and bound" algorithms in integer programming being a prominent example. It also provides a workable condition that characterizes a solution pair, at least when there is no duality gap.

Strong duality, on the contrary, requires a precise topological assumption: the interior of the constraint set has to be nonempty (Slater condition). We note, however, that this condition is satisfied in most cases, at least in the present finite-dimensional setting. The proof is then based on a separating hyperplane theorem, that in turn requires convexity assumptions about  $f$  and  $h$ . When strong duality holds, and provided we are able to actually solve the dual problem, we obtain the exact value of the primal (no duality gap).

We can add a finite number (say  $L$ ) of linear equality constraints to  $(P)$ , obtaining

(P): min 
$$f(v)$$
 sub  $v \in A$   
=  $\{v \in C : h(v) \le 0, Qv = r\} \subset \mathbb{R}^N$  (11)

where O is an  $L \times N$  matrix and  $r \in \mathbb{R}^L$ . The Lagrangian is defined as

$$\mathcal{L}(v, w) = f(v) + w^{\text{in}} \cdot h(v) + w^{\text{eq}} \cdot (Qv - r)$$
$$v \in C, \ w = (w^{\text{in}}, w^{\text{eq}}) \in \mathbb{R}^{M \times L} \tag{12}$$

in such a way that

$$\inf_{v \in A} f(v) = \inf_{v \in C} \sup_{w^{\text{in}} \ge 0, \, w^{\text{eq}} \in \mathbb{R}^L} \mathcal{L}(v, w) \tag{13}$$

The dual problem is then

(D): 
$$\max g(w)$$
 sub  $w \in B$   
=  $\{w \in D : w^{\text{in}} \ge 0\} \subset \mathbb{R}^{M \times L}$  (14)

where, as before,  $g(w) = \inf_{v \in C} \mathcal{L}(v, w)$ , and D is the domain of  $g$ . It is worth noting that if the primal problem has equality constraints only, then the only constraint of the dual problem is  $w \in D$ .

A Lagrange duality theorem can then be stated and also proved in this case, reaching similar conclusions. We have just to replace  $\widehat{w}$  with  $\widehat{w}^{\text{in}}$  in the first condition in (10), and modify the Slater condition as follows:

• There exists  $v \in \text{ri}(C)$  such that  $h_m(v) < 0$ for all m and  $Ov = r$  $(15)$  The relative interior  $ri(C)$  is the interior of the convex set  $C$  relative to the affine hull of  $C$ . For instance, if  $C = [0, 1] \times \{0\} \subset \mathbb{R}^2$ , then  $\text{ri}(C) = (0, 1) \times \{0\}$ (because the affine hull of C is  $\mathbb{R} \times \{0\}$ ), while the interior of  $C$  is clearly empty (see [4] for more on relative interiors and related topics about convex sets).

In many concrete problems,  $C$  is a polyhedron, that is, it is the (convex and closed) set defined by a certain finite set of linear inequalities, and all the functions  $h_m$  are affine. If we assume, in addition, that  $f$  may be extended to a finite convex function over *all*  $\mathbb{R}^N$ , Farkas Lemma allows us to prove strong duality without requiring any Slater condition. Remarkably, if  $f$  is linear too, then the existence of a primal solution is ensured.

The Lagrange duality theorem provides us a simple criterion for the existence of a dual solution and a set of conditions characterizing a possible primal solution. It is, however, not directly concerned with the existence of a primal solution. To ensure this, one has to assume stronger conditions such as compactness of  $C$  or coercivity of  $f$ . A third condition ( $f$  linear) has been described above.

We have seen that the dual problem usually looks much better than the primal: it is always concave and its solvability is guaranteed under mild assumptions about the primal. This fact is particularly useful in designing numerical procedures. Moreover, even when the primal is solvable, the dual often proves easier to handle. We provide a simple example that should clarify the point.

A standard linear programming (LP) problem comes, by definition, in the form

(P): 
$$\min c \cdot v$$
 sub  $Qv = r$ ,  $v \ge 0$ ,  $v \in \mathbb{R}^N$  (16)

where  $c \in \mathbb{R}^N$ , Q is a  $L \times N$  matrix and  $r \in \mathbb{R}^L$ . An easy computation shows that the dual problem is  $(T$ denotes transposition)

(D): 
$$\max r \cdot w$$
 sub  $Q^T w \le c$ ,  $w \in \mathbb{R}^L$  (17)

We know that strong duality holds in this case, and that the existence of a solution pair is guaranteed. In particular,  $(Q^T \widehat{w} - c) \cdot \widehat{v} = 0$  is a necessary condition for a pair  $(\widehat{v}, \widehat{w})$  to be a solution. The dual problem, however, has  $L$  variables and  $N$  constraints and thus can often be more tractable than the primal

if  $N$  is much larger than  $L$ . This is the basis for great enhancements in existing numerical methods.

A last remark concerns the word "duality": any dual problem can be turned into an equivalent minimization primal problem. It turns out that the bidual, that is, the dual of this new primal problem, seldom coincides with the original primal problem. LP problems are an important exception: the bidual of an LP problem is the problem itself.

# **Fenchel Duality in Finite-dimensional** Problems

Fenchel duality, that we will derive from Lagrange duality, may be applied to primal problems in the form

(P): 
$$\min \{f_1(v) - f_2(v)\}$$
  
sub  $v \in A = C_1 \cap C_2 \subset \mathbb{R}^N$  (18)

where  $C_1, C_2 \subseteq \mathbb{R}^N$  are convex,  $f_1: C_1 \to \mathbb{R}$  is convex, and  $f_2: C_2 \to \mathbb{R}$  is concave.

Consider the function  $f(x, y) = f_1(x) - f_2(y)$ defined on  $\mathbb{R}^{2N}$  and clearly convex. We can restate the primal as

(P): 
$$\min f(x, y)$$
 sub  $(x, y) \in A'$   
=  $\{(x, y) \in C_1 \times C_2 : x = y\} \subset \mathbb{R}^{2N}$  (19)

where the N fictitious linear constraints  $(x_n = y_n \forall n)$ allow us to apply the Lagrange duality machinery. The Lagrangian function is  $\mathcal{L}(x, y, w) = f_1(x) - f_2(x)$  $f_2(y) + w \cdot (x - y)$  and, using some simple algebra, we compute

$$g(w) = \inf_{x \in C_1, y \in C_2} \mathcal{L}(x, y, w) = f_2^*(w) - f_1^*(w)$$
(20)

where

$$f_1^*(w) = \sup_{x \in C_1} \{w \cdot x - f_1(x)\}\tag{21}$$

is, by definition, the convex conjugate (indeed,  $f_1^*$  is convex) of the convex function  $f_1$ , and

$$f_2^*(w) = \inf_{y \in C_2} \{w \cdot y - f_2(y)\}\tag{22}$$

is the concave conjugate (indeed,  $f_2^*$  is concave) of the concave function  $f_2$ . As a consequence, the dual problem is

(D): 
$$\max \{ f_2^*(w) - f_1^*(w) \}$$
  
sub  $w \in B = C_1^* \cap C_2^* \subset \mathbb{R}^N$  (23)

where  $C_1^*$  and  $C_2^*$  are the domains of  $f_1^*$  and  $f_2^*$ , respectively. Assuming primal feasibility and boundedness, the Lagrange duality theorem yields the Fenchel duality theorem.

## Fenchel Duality Theorem

#### 1. Weak duality

If there is no duality gap,  $(\widehat{v}, \widehat{w})$  is a solution pair if and only if

$$\widehat{v} \cdot \widehat{w} = f_1(\widehat{v}) + f_1^*(\widehat{w}) = f_2(\widehat{v}) + f_2^*(\widehat{w}) \qquad (24)$$

#### 2. Strong duality

There is no duality gap between the primal and the dual, and there is a dual solution, provided one of the following conditions is satisfied:

- (*a*)  $ri(C_1) \cap ri(C_2)$  is nonempty
- (b)  $C_1$  and  $C_2$  are polyhedra and  $f_1$  (resp.  $f_2$ ) *may be extended to a finite convex (concave)* function over all  $\mathbb{R}^N$

# See [4] or [1] for a proof.

We say that a convex function  $f$  is closed if, for any  $a \in \mathbb{R}$ , the set  $\Gamma_a = \{v : f(v) \le a\}$  is closed; a similar definitions applies to concave functions, where the inequality inside  $\Gamma_a$  is reversed. A sufficient, though not necessary condition for  $f$  to be closed is continuity on all  $C$ . A celebrated result (the Fenchel– Moreau theorem) states that  $(f^*)^* \equiv f$ , provided f is a closed (convex or concave) function. Therefore, if in the primal problem  $f_1$  and  $f_2$  are closed, then the dual problem of the dual coincides with the primal, and the duality is therefore *complete*. Thanks to this fact, an application of the Fenchel duality theorem to the dual problem allows us to state that the primal has a solution provided one of the following conditions is satisfied:

- 1.  $\operatorname{ri}(C_1^*) \cap \operatorname{ri}(C_2^*)$  is nonempty.
- 2.  $C_1^*$  and  $C_2^*$  are polyhedra, and  $f_1^*$  (resp.  $f_2^*$ ) may be extended to a finite convex (concave) function over all  $\mathbb{R}^N$ .

Fenchel duality can sometimes be effectively used for general problems in the form

(P): 
$$\min f(v)$$
 sub  $v \in C \subset \mathbb{R}^N$  (25)

where  $f$  and  $C$  are convex. Indeed, such a problem can be cast in the form (18) provided we set  $f_1 = f$ ,  $f_2 = 0$  (concave),  $C_1 = \mathbb{R}^N$ , and  $C_2 = C$ . The dual problem is given by equation  $(23)$ , where

$$f_1^*(w) = \sup_{v \in \mathbb{R}^N} \{w \cdot v - f(v)\}\tag{26}$$

is an unconstrained problem and

$$f_2^*(w) = \inf_{v \in C} w \cdot v \tag{27}$$

has a simple goal function.

We have derived Fenchel duality as a by product of Lagrange duality. However, it is possible to go in the opposite direction, by first proving Fenchel duality (unsurprisingly, using hyperplane separation arguments, see [2]) and then writing a Lagrange problem in the Fenchel form, so that Lagrange duality can be derived (see [3]). Therefore, at least in the finite-dimensional setting, Lagrange and Fenchel duality are formally equivalent.

## **Duality in Infinite-dimensional Problems**

For infinite-dimensional problems, Lagrange or Fenchel duality exhibit a large formal similarity with the finite-dimensional counterparts we have described so far. Nevertheless, the technical topological assumptions, which are needed to ensure duality, become much less trivial when the space  $V = \mathbb{R}^N$ is replaced by an infinite-dimensional Banach space. We give a brief account of these differences.

Let  $V$  be a Banach space and consider the primal problem

(P): 
$$\min f(v) \quad \text{sub } v \in A$$
$$= \{ v \in C : h(v) \le 0 \} \subset V \qquad (28)$$

where  $C \subseteq V$  is a convex set, and  $f : C \to \mathbb{R}$  and  $h :$  $C \to \mathbb{R}^M$  are convex functions. Then, by mimicking the finite-dimensional case, the dual problem is

(D): 
$$\max g(w)$$
 sub  $w \in B$   
=  $\{w \in D : w \ge 0\} \subset \mathbb{R}^M$  (29)

where  $g(w) = \inf_{v \in C} \{f(v) + w \cdot h(v)\}\$ , and D is the domain of  $g$ . We can note that the dual is finitedimensional, but the definition of  $g$  involves an infinite-dimensional problem. A perfect analog of the finite-dimensional Lagrange duality theorem may be derived in this more general case too (see [2]) with essentially the same Slater condition (existence of some  $v \in C$  such that  $h_m(v) < 0$  for any m). We can also introduce a finite set of linear inequalities: this case can be handled in exactly the same way as in the finite-dimensional case. However, the hypothesis  $\text{ri}(C) \neq \emptyset$  is not completely trivial here.

Fenchel duality too can be much generalized. Indeed, let V be a Banach space,  $W = V^*$  its dual space (the Banach space of continuous linear forms on V), and denote by  $\langle v, v^* \rangle$  the action of  $v^* \in V^*$ on  $v \in V$ . Consider the primal problem

(P): 
$$\min \{f_1(v) - f_2(v)\}$$
 sub  $v \in A$   
=  $C_1 \cap C_2 \subset V$  (30)

where  $C_1, C_2 \subseteq V$  are convex sets,  $f_1$  is convex on  $C_1$ , and  $f_2$  is concave on  $C_2$ . Then, again by mimicking the finite-dimensional case, we associate the primal with the dual

(D): 
$$\max \{f_2^*(v^*) - f_1^*(v^*)\}$$
 sub  $v^* \in B$   
=  $C_1^* \cap C_2^* \subset V^*$  (31)

where

$$f_1^*(v^*) = \sup_{v \in C_1} \{ \langle v, v^* \rangle - f_1(v) \} \quad \text{and} \quad f_2^*(v^*)$$
  
= 
$$\inf_{v \in C_2} \{ \langle v, v^* \rangle - f_2(v) \}$$
(32)

are the convex and concave conjugates of  $f_1$  and  $f_2$ , respectively, and  $C_1^*$  and  $C_2^*$  are their domains. Then, with obvious formal modifications, Fenchel duality theorem holds in this case, too (see again [2]). However, to obtain strong duality, we must supplement conditions (a) or (b) with the following

• Either  $\{(v, a) \in V \times \mathbb{R} : f_1(v) < a\}$ or  $\{(v, a) \in V \times \mathbb{R} : f_2(v) > a\}$ has a nonempty interior.

This latter condition, which, in the finite-dimensional setting, follows from (a) or (b), must be checked separately in the present case.

## References

- [1] Bertsekas, D.P. (1995). *Nonlinear Programming*, Athena Scientific, Belmont.
- [2] Luenberger, D.G. (1969). *Optimization by Vector Space* Methods, Wiley, New York.
- [3] Magnanti, T.L. (1974). Fenchel and Lagrange duality are equivalent, Mathematical Programming 7, 253-258.
- [4] Rockafellar, R.T. (1970). Convex Analysis, Princeton University Press, Princeton.

# **Related Articles**

**Capital Asset Pricing Model; Expected Utility** Maximization; Expected Utility Maximization: Duality Methods; Minimal Entropy Martingale Measure; Model Calibration; Optimization Methods; Risk-Return Analysis; Robust Portfolio Optimization; Stochastic Control; Utility **Function; Utility Indifference Valuation.**
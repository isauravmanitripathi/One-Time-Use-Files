# Lévy Copulas

Lévy copulas characterize the dependence among components of multidimensional Lévy processes. They are similar to copulas of probability distributions but are defined at the level of Lévy measures. Lévy copulas separate the dependence structure of a Lévy measure from the one-dimensional marginal measures meaning that any  $d$ -dimensional Lévy measure can be constructed from a set of one-dimensional margins and a Lévy copula. This suggests the construction of parametric multidimensional Lévy models by combining arbitrary one-dimensional Lévy processes with a Lévy copula from a parametric family. The Lévy copulas were introduced in [4] for spectrally one-sided Lévy processes and in [6, 7] in the general case. Subsequent theoretical developments include Barndorff-Nielsen and Lindner [1], who discuss further interpretations of Lévy copulas and various transformations of these objects. Farkas et al. [5] develop deterministic numerical methods for option pricing in models based on Lévy copulas, and the simulation algorithms for multidimensional Lévy processes based on their Lévy copulas are discussed in  $[4, 7]$ .

In finance, Lévy copulas are useful to model joint moves of several assets in various settings including portfolio risk management, option pricing [8], insurance [3], and operational risk modeling [2].

## **Lévy Measures and Tail Integrals**

A Lévy process on  $\mathbb{R}^d$  is described by its characteristic triplet  $(A, \nu, \gamma)$ , where A is a positive semidefinite  $d \times d$  matrix,  $\gamma \in \mathbb{R}^d$ , and  $\nu$  is a positive Radon measure on  $\mathbb{R}^d \setminus \{0\}$ , satisfying  $\int_{\mathbb{R}^d \setminus \{0\}} (\|x\|^2 \wedge 1) \nu(dx) <$  $\infty$  and called the *Lévy measure of X*. The matrix A is the covariance matrix of the continuous martingale (Brownian motion) part of X, and  $\nu$  describes the independent jump part. It makes sense, therefore, to describe the dependence structure of the jump part of  $X$  with a suitable notion of copula at the level of the Lévy measure.

In the same way that the distribution of a random vector can be represented by its distribution function, the Lévy measure of a Lévy process will be represented by its tail integral. If we are only interested in,

say, positive jumps, the definition of the tail integral is simple: given a  $\mathbb{R}^d$ -valued Lévy process with Lévy measure  $\nu$  supported by  $[0,\infty)^d$ , the tail integral of  $\nu$  is the function  $U:(0,\infty)^d\to [0,\infty)$  defined by

 $U(x_1,\ldots,x_d) = \nu((x_1,\infty)\times\cdots\times(x_d,\infty)) \quad (1)$ 

In the general case, care must be taken to avoid the possible singularity of  $\nu$  near zero: so the tail integral is a function  $U : (\mathbb{R} \setminus \{0\})^d \to \mathbb{R}$  defined by

$$U(x_1,\ldots,x_d) := \prod_{i=1}^d \operatorname{sgn}(x_i) \nu \left( \prod_{j=1}^d \mathcal{I}(x_j) \right) \quad (2)$$

where  $\mathcal{I} := (x, \infty)$  if  $x > 0$  and  $\mathcal{I}(x) := (-\infty, x]$  if  $x < 0.$ 

Given an  $\mathbb{R}^d$ -valued Lévy process X and a nonempty set of indices  $I \subset \{1, \ldots, d\}$ , the *I* margin of  $X$  is the Lévy process of lower dimension that contains only those components of  $X$  whose indices are in  $I: X^I := (X^i)_{i \in I}$ . The *I*-marginal tail integral  $U^I$ of X is then simply the tail integral of the process  $X^I$ .

#### Lévy Copulas: The General Case

Central to the theory of Lévy copulas are the notions of a  $d$ -increasing function and the margins of a  $d$ increasing function. Intuitively speaking, a function  $F$  is *d*-increasing if  $dF$  is a positive measure on  $\mathbb{R}^d$  in the sense of Lebesgue-Stieltjes integration. Similarly, the margin  $F^{I}$  is defined so that the measure  $d(F^I)$  induced by  $F^I$  coincides with the I margin of the measure  $dF$ . Let us now turn to precise definitions.

We set  $\overline{\mathbb{R}} := (-\infty, \infty]$  and for  $a, b \in \overline{\mathbb{R}}^d$ , we write  $a \leq b$  if  $a_k \leq b_k$ ,  $k = 1, \ldots, d$ . In this case,  $(a, b]$  denotes the interval

$$(a,b] := (a_1,b_1] \times \cdots \times (a_d,b_d] \tag{3}$$

For a function  $F : \overline{\mathbb{R}}^d \to \overline{\mathbb{R}}$ , the *F*-volume of  $(a, b]$ is defined by

$$V_F((a,b]) := \sum_{u \in \{a_1,b_1\} \times \dots \times \{a_d,b_d\}} (-1)^{N(u)} F(u) \quad (4)$$

where  $N(u) := \#\{k : u_k = a_k\}$ . In particular,  $V_F$  $((a, b]) = F(b) - F(a)$  for  $d = 1$  and  $V_F((a, b]) =$  $F(b_1, b_2) + F(a_1, a_2) - F(a_1, b_2) - F(b_1, a_2)$  for  $d = 2$ . If  $F(u) = \prod_{i=1}^{d} u_i$ , the F volume of any interval is equal to its Lebesgue measure.

A function  $F: \overline{\mathbb{R}}^d \to \overline{\mathbb{R}}$  is called *d* increasing if  $V_F((a, b]) > 0$  for all  $a < b$ . The distribution function of a random vector is one example of a  $d$ increasing function. The tail integral  $U$  was defined in such way that  $(-1)^d U$  is d increasing in every orthant (but not on the entire space).

Let  $F: \overline{\mathbb{R}}^d \to \overline{\mathbb{R}}$  be a *d*-increasing function such that  $F(u_1, \ldots, u_d) = 0$  if  $u_i = 0$  for at least one *i*. For an index set  $I$ , the  $I$  margin of  $F$  is the function  $F^I: \overline{\mathbb{R}}^{|I|} \to \overline{\mathbb{R}}$ , defined by

$$F^{I}((u_{i})_{i\in I}) := \lim_{a\to\infty} \sum_{(u_{i})_{i\in I^{c}\in\{-a,\infty\}^{|I^{c}|}\atop k\in I^{c}} \operatorname{sgn} u_{i}} \quad (5)$$

where  $I^c := \{1, \ldots, d\} \setminus I$ . In particular, we have  $F^{\{1\}}(u) = F(u, \infty) - \lim_{a \to -\infty} F(u, a)$  for  $d = 2$ . To understand the reasoning leading to the above definition of margins, note that any positive measure  $\mu$ on  $\overline{\mathbb{R}}^a$  naturally induces an increasing function *F* via

$$F(u_1, \ldots, u_d) :=$$

$$\mu \Big( (u_1 \wedge 0, u_1 \vee 0] \times \cdots \times (u_d \wedge 0, u_d \vee 0] \Big) \prod_{i=1}^d \operatorname{sgn} u_i$$
(6)

for  $u_1, \ldots, u_d \in \overline{\mathbb{R}}$ . The margins of  $\mu$  are usually defined by

$$\mu^{I}(A) = \mu\left(\{u \in \overline{\mathbb{R}}^{d} : (u_{i})_{i \in I} \in A\}\right), \quad A \subset \overline{\mathbb{R}}^{|I|}$$
(7)

It is now easy to see that the margins of  $F$  are induced by the margins of  $\mu$  in the sense of equation (6).

A function  $F: \overline{\mathbb{R}}^d \to \overline{\mathbb{R}}$  is called *Lévy copula* if it satisfies the following four conditions (the first one is just a nontriviality requirement):

- $(u_1,\ldots,u_d) \neq$ 1.  $F(u_1,\ldots,u_d) \neq \infty$ for  $(\infty,\ldots,\infty);$
- 2.  $F(u_1, \ldots, u_d) = 0$  if  $u_i = 0$  for at least one  $i \in \{1, \ldots, d\};$
- 3.  $F$  is  $d$ -increasing; and
- 4.  $F^{\{i\}}(u) = u$  for any  $i \in \{1, \ldots, d\}, u \in \mathbb{R}$ .

## Lévy Copulas: The Spectrally One-sided Case

If  $X$  has only positive jumps in each component, or if we are only interested in the positive jumps of X, only the values  $F(u_1, \ldots, u_d)$  for  $u_1, \ldots, u_d > 0$ are relevant. We can then set  $F(u_1, \ldots, u_d) = 0$  if  $u_i < 0$  for at least one *i*, which greatly simplifies the definition of the margins:

$$F^{I}((u_{i})_{i\in I}) = F(u_{1}, \dots, u_{d})|_{u_{j} = +\infty, j \notin I} \qquad (8)$$

Taking the margins now amounts to replacing the variable that is being integrated out with infinity-exactly the same procedure as for probability distribution functions. Restricting a Lévy copula to  $[0,\infty]^d$  in such way, we obtain a Lévy copula for spectrally positive Lévy processes, or, for short, a positive Lévy copula.

#### Sklar's Theorem for Lévy Processes

The following theorem  $[4, 7]$  characterizes the dependence structure of Lévy processes in terms of Lévy copulas:

#### Theorem 1

1. Let  $X = (X^1, \ldots, X^d)$  be a  $\mathbb{R}^d$ -valued Lévy process. Then there exists a Lévy copula  $F$  such that the tail integrals of  $X$  satisfy

$$U^{I}((x_{i})_{i\in I}) = F^{I}((U_{i}(x_{i}))_{i\in I}) \tag{9}$$

for any nonempty index set  $I \subset \{1, \ldots, d\}$  and any  $(x_i)_{i \in I} \in (\mathbb{R} \setminus \{0\})^{|I|}$ . The Lévy copula F is unique on  $\prod_{i=1}^d \overline{\text{Ran } U_i}$ .

2. Let F be a d-dimensional Lévy copula and  $U_i, i = 1, \ldots, d$ , tail integrals of real-valued Lévy processes. Then there exists a  $\mathbb{R}^d$ -valued Lévy  $process\ X\ whose\ components\ have\ tail\ integrals$  $U_1, \ldots, U_d$  and whose marginal tail integrals satisfy equation (9) for any nonempty  $I \subset \{1, \ldots, d\}$ and any  $(x_i)_{i \in I} \in (\mathbb{R} \setminus \{0\})^{|I|}$ . The Lévy measure  $v$  of  $X$  is uniquely determined by  $F$  and  $U_i$ ,  $i =$  $1, \ldots, d.$ 

In particular, applying the above theorem with  $I =$  $\{1, \ldots, d\}$ , we obtain the usual formula

$$U(x_1, \ldots, x_d) = F(U_1(x_1), \ldots, U_d(x_d)) \qquad (10)$$

If the one-dimensional marginal Lévy measures are infinite and have no atoms,  $\text{Ran } U_i = (-\infty, 0) \cup$  $(0,\infty)$  for any *i* and one can compute *F* directly *via* 

$$F(u_1, \dots, u_d) = U\big(U_1^{-1}(u_1), \dots, U_d^{-1}(u_d)\big) \quad (11)$$

#### **Examples and Parametric Families**

The components of a pure-iump Lévy process are independent if and only if they never jump together, that is, if the Lévy measure is supported by the coordinate axes. This leads to a characterization of Lévy processes with independent components in terms of their Lévy copulas: the components  $X^1,\ldots,X^d$  of a  $\mathbb{R}^d$ -valued Lévy process X are independent if and only if their Brownian motion parts are independent and if  $X$  has a Lévy copula of the form

$$F_{\perp}(x_1,\ldots,x_d) := \sum_{i=1}^d x_i \prod_{j \neq i} 1_{\{\infty\}}(x_j) \tag{12}$$

The Lévy copula of independence is thus different from the copula of independent random variables  $C_{\perp}(u_1,\ldots,u_d)=u_1\ldots u_d$ , which emphasizes the fact that the two notions are far from being the same and the "copula" intuition cannot always be applied to Lévy copulas.

The complete dependence copula, on the other hand, turns out to have a similar form to the classical case. Recall that a subset S of  $\mathbb{R}^d$  is called *ordered* if, for any two vectors  $u, v \in S$ , either  $u_k < v_k$ ,  $k =$  $1,\ldots,d$  or  $u_k \geq v_k, k = 1,\ldots,d$ . Similarly, S is called *strictly ordered* if, for any two different vectors  $u, v \in S$ , either  $u_k < v_k$ ,  $k = 1, \ldots, d$  or  $u_k > v_k$ ,  $k = 1, \ldots, d$ . Furthermore, set

$$K := \{x \in \mathbb{R}^d : \operatorname{sgn} x_1 = \ldots = \operatorname{sgn} x_d\} \tag{13}$$

The jumps of an  $\mathbb{R}^d$ -valued Lévy process  $X$  are said to be completely dependent or comonotonic if there exists a strictly ordered subset  $S \subset K$  such that  $\Delta X_t := X_t - X_{t-} \in S, t \in \mathbb{R}_+$  (except for some null set of paths). The condition  $\Delta X_t \in K$  means that if the components of a Lévy process are comonotonic, they always jump in the same direction. A  $\mathbb{R}^d$ -valued Lévy process whose Lévy measure is supported by an ordered set  $S \subset K$  is described by the *complete* 

dependence Lévy copula given by

$$F_{\parallel}(x) := \min(|x_1|, \dots, |x_d|) 1_K(x) \prod_{i=1}^d \operatorname{sgn} x_i \quad (14)$$

Conversely, if  $F_{\parallel}$  is a Lévy copula of X, then the Lévy measure of  $X$  is supported by an ordered subset of  $K$ . If, in addition, the tail integrals  $U_i$ of  $X^i$  are continuous and satisfy  $\lim_{x\to 0} U_i(x) = \infty$ ,  $i = 1, \ldots, d$ , then  $F_{\parallel}$  is the unique Lévy copula of  $X$  and the jumps of  $\hat{X}$  are completely dependent. For positive Lévy copulas, expression (14) simplifies to

$$F_{\parallel}(x_1,\ldots,x_d) := \min(x_1,\ldots,x_d) \tag{15}$$

that is, we recover the expression of the complete dependence copula of random variables (but the two functions are defined on different domains!).

One simple and convenient parametric family of positive Lévy copulas is similar to the Clayton family of copulas; it is therefore called the *Clayton–Lévy* copula:

$$F(u_1, \dots, u_d) = \left(\sum_{i=1}^d u_i^{-\theta}\right)^{-1/\theta}, \quad u_1, \dots, u_d \ge 0$$
(16)

The reader can easily check that this copula converges to the complete dependence copula  $F_{\parallel}$  as  $\theta \rightarrow \infty$ and to the independence copula  $F_{\perp}$  as  $\theta \to 0$ . This construction can be generalized to a Lévy copula on  $\overline{\mathbb{R}}^a$ :

$$F(u_1, \ldots, u_d) = 2^{2-d} \left( \sum_{i=1}^d |u_i|^{-\theta} \right)^{-1/\theta} \times \left( \eta \mathbf{1}_{\{u_1 \cdots u_d \ge 0\}} - (1-\eta) \mathbf{1}_{\{u_1 \cdots u_d < 0\}} \right) \tag{17}$$

defines a two-parameter family of Lévy copulas. The role of the parameters is easiest to analyze in the case  $d = 2$ , when equation (17) becomes

$$F(u,v) = \left( |u|^{-\theta} + |v|^{-\theta} \right)^{-1/\theta} \times \left( \eta \mathbf{1}_{\{uv \ge 0\}} - (1-\eta) \mathbf{1}_{\{uv < 0\}} \right) \tag{18}$$

From this equation, it is readily seen that the parameter  $\eta$  determines the dependence of the *sign* of jumps: when  $\eta = 1$ , the two components always jump in the same direction, and when *η* = 0, positive jumps in one component are accompanied by negative jumps in the other and *vice versa*. The parameter *θ* is responsible for the dependence of absolute values of jumps in different components.

Figure 1 shows the scatter plots of weekly returns in an exponential Levy model with variance gamma ´ (*see* **Variance-gamma Model**) margins and the dependence pattern given by the Levy copula (18) ´ with two different sets of dependence parameters,

![](_page_3_Figure_3.jpeg)

**Figure 1** Scatter plots of returns in a two-dimensional variance gamma model with correlation *ρ* = 50% and different tail dependence. (a) Strong tail dependence (*η* = 0*.*75 and *θ* = 10) and (b) weak tail dependence (*η* = 0*.*99 and *θ* = 0*.*61)

both of which lead to a correlation of 50% but have different tail dependence patterns. It is clear that when a precise description of tail events such as simultaneous large jumps is necessary, Levy cop- ´ ulas offer more freedom in modeling dependence than traditional correlation-based approaches. A natural application of Levy copulas arises in the context ´ of multidimensional gap options [8] that are exotic products whose payoff depends on the total number of sharp downside moves in a basket of assets.

## **References**

- [1] Barndorff-Nielsen, O.E. & Lindner, A.M. (2007). Levy ´ copulas: dynamics and transforms of upsilon type, *Scandinavian Journal of Statistics* **34**, 298–316.
- [2] Bocker, K. & Kl ¨ uppelberg, C. (2007). Multivariate oper- ¨ ational risk: dependence modelling with Levy copulas, ´ *ERM Symposium Online Monograph*, Society of Actuaries, and Joint Risk Management, section newsletter.
- [3] Bregman, Y. & Kluppelberg, C. (2005). Ruin estimation ¨ in multivariate models with Clayton dependence structure, *Scandinavian Actuarial Journal* **November**(6), 462–480.
- [4] Cont, R. & Tankov, P. (2004). *Financial Modelling with Jump Processes*, Chapman & Hall/CRC Press.
- [5] Farkas, W., Reich, N. & Schwab, C. (2007). Anisotropic stable Levy copula processes-analytical and numerical ´ aspects, *Mathematical Models and Methods in Applied Sciences* **17**, 1405–1443.
- [6] Kallsen, J. & Tankov, P. (2006). Characterization of dependence of multidimensional Levy processes using ´ Levy copulas, ´ *Journal of Multivariate Analysis* **97**, 1551–1572.
- [7] Tankov, P. (2004). *L´evy Processes in Finance: Inverse Problems and Dependence Modelling*, PhD thesis, Ecole Polytechnique, France.
- [8] Tankov, P. (2008). *Pricing and Hedging Gap Risk*, preprint, available at http://papers.ssrn.com.

## **Related Articles**

**Copulas: Estimation**; **Exponential Levy Models ´** ; **Levy Processes ´** ; **Multivariate Distributions**; **Operational Risk**.

PETER TANKOV
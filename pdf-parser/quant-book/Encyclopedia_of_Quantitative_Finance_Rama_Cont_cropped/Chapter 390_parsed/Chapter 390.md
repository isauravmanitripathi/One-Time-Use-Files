# **Heavy Tails in Insurance**

#### **Heavy-tailed Distributions**

In the class of heavy-tailed distribution functions, subexponential distribution functions are a special class, which have just the right level of generality for risk measurement in insurance and finance models. The name arises from one of their properties: the fact that their right tail decreases more slowly than any exponential tail. This implies that large values can occur in a sample with nonnegligible probability, which proposes the subexponential distribution functions as natural candidates for situations where extremely large values occur in a sample compared to the mean size of the data. Such a pattern is often seen not only in insurance data, for instance, in fire, wind-storm, or flood insurance (collectively known as *catastrophe insurance*) but also in data from finance and communications engineering; see, for example  $[1, 6, 7]$ . Subexponential insurance claims can account for large fluctuations in the risk process of a company. Textbook accounts can be found in  $[2, 4, 6-8]$ .

We present two defining properties of subexponential distribution functions. Let  $(X_k)_{k \in \mathbb{N}}$  be independently and identically distributed positive random variables with distribution function  $F$  such that  $F(x) < 1$  for all  $x > 0$ . Denote by  $\overline{F}(x) = 1 - F(x)$ for  $x \ge 0$ , the tail of F, and for  $n \in \mathbb{N}$ ,

$$\overline{F^{n*}}(x) = 1 - F^{n*}(x)$$
  
=  $\mathbb{P}(X_1 + \dots + X_n > x), \quad x \ge 0$  (1)

the tail of the  $n$ -fold convolution of  $F$ . We then say that F (or X) is subexponential (written  $F \in \mathcal{S}$ ) if one of the following equivalent conditions holds:

(a) 
$$\lim_{x \to \infty} \frac{F^{n*}(x)}{\overline{F}(x)} = n$$
 for some (all)  $n \ge 2$  and

(b) 
$$\lim_{x \to \infty} \frac{\mathbb{P}(X_1 + \dots + X_n > x)}{\mathbb{P}(\max(X_1, \dots, X_n) > x)} = 1 \text{ for some}$$
  
(all)  $n \ge 2$ .

The heavy-tailedness of  $F \in \mathcal{S}$  is demonstrated by the implications

$$F \in \mathcal{S} \Longrightarrow \lim_{x \to \infty} \frac{\overline{F}(x - y)}{\overline{F}(x)} = 1 \quad \forall y \in \mathbb{R} \quad (2)$$

$$\Longrightarrow \frac{\overline{F}(x)}{e^{-\varepsilon x}} \xrightarrow{x \to \infty} \infty \quad \forall \varepsilon > 0 \tag{3}$$

A famous subclass of  $S$  is the class of distribution functions with regularly varying tails; see [3]. For a positive measurable function  $f$ , we write  $f \in \mathcal{R}(\alpha)$ for  $\alpha \in \mathbb{R}$  (f is regularly varying with index  $\alpha$ ) if

$$\lim_{x \to \infty} \frac{f(tx)}{f(x)} = t^{\alpha} \quad \forall t > 0 \tag{4}$$

Let  $\overline{F} \in \mathcal{R}(-\alpha)$  for  $\alpha \ge 0$ ; then it has the representation

$$\overline{F}(x) = x^{-\alpha}\ell(x), \quad x > 0 \tag{5}$$

for some  $\ell \in \mathcal{R}(0)$ .

For regularly varying distribution tails, we can check (a) for  $n = 2$  by splitting the convolution integral and use partial integration to obtain

$$\frac{\overline{F^{2*}}(x)}{\overline{F}(x)} = 2 \int_0^{x/2} \frac{\overline{F}(x-y)}{\overline{F}(x)} dF(y)$$
$$+ \frac{(\overline{F}(x/2))^2}{\overline{F}(x)}, \quad x > 0 \tag{6}$$

Immediately, by equation (4), the last term tends to 0. The integrand satisfies  $\overline{F}(x-y)/\overline{F}(x) \leq \overline{F}(x/2)/$  $\overline{F}(x)$  for  $0 \le y \le x/2$ ; hence, Lebesgue-dominated convergence applies and, since  $F$  satisfies equation  $(2)$ , the integral on the right-hand side tends to 1 as  $x \to \infty$ . Examples of distribution functions with regularly varying tail include the Pareto, Burr, transformed beta (also called *generalized F*), log-gamma, and stable distribution functions (see Table 1.2.6 in [4]).

In addition, the lognormal, the two Benktander families, and the heavy-tailed Weibull (shape parameter less than 1) belong to  $S$ ; see again Table 1.2.6 in [4]. However, a direct proof of this is more difficult than that for the regularly varying case. Subexponentiality is typically established via an integral test for the hazard rate known as *Pitman's criterion* [2].

## **Application to Insurance**

The two main examples in insurance risk theory that use the tail properties of subexponential distributions are aggregated claims tails and ruin probabilities. The *aggregated claims* denoted by *A* (*see* **Accumulated Claims**) are defined as the sum of all claims to the insurance company in a given period. The usual model is

$$A = X_1 + \dots + X_N \tag{7}$$

where *N* is the number of claims and *X*1*, X*2*,...* are the *claim sizes* in the given time interval (*N* and *(Xk )k*<sup>∈</sup> are assumed to be independent and *(Xk )k*<sup>∈</sup> is an independently and identically distributed sequence). The tail of *A* and the associated quantiles are important for assessing the probability of big losses and for Value-at-Risk (*see* **Value-at-Risk**) calculations. The main result in the heavytailed case states that if the *Xk* are subexponential, then (*a(u)* ∼ *b(u)* as *u* → ∞ means that lim*u*→∞ *a(u)/b(u)* = 1)

$$\mathbb{P}(A > x) \sim \mathbb{E}(N)\mathbb{P}(X_1 > x)$$
 as  $x \to \infty$  (8)

provided in addition *Ɛ(z<sup>N</sup> ) <* ∞ for some *z >* 1 (cf. [2], Chapter IX, Lemma 2.2).

The classical insurance risk model is the *Cram´er— Lundberg model* (cf. [2, 4, 6, 8] and *see* **Ruin Theory**), where the *claim times* occur at the jump times of a Poisson*(λ)* process *(N (t))t*<sup>≥</sup><sup>0</sup> (*see* **Poisson Process**) and the claims *(Xk )k*<sup>∈</sup> are again an independently and identically distributed sequence with finite mean. The *risk process* is for *initial reserve u* ≥ 0 and *premium rate c >* 0 defined as

$$R(t) = u + ct - \sum_{k=1}^{N(t)} X_k, \quad t \ge 0 \tag{9}$$

Then the *ruin probability ψ(u) in infinite time* is the probability that *R* ever falls below 0, that is, *ψ(u)* = *-(*inf*t*≥<sup>0</sup> *R(t) <* 0*)*. Define the *integrated tail distribution function FI* by

$$F_I(x) = \frac{1}{\mathbb{E}(X_1)} \int_0^x \overline{F}(y) \mathrm{d}y, \quad x \ge 0 \quad (10)$$

If *FI* is subexponential (which is satisfied for all subexponential distributions *F* mentioned above under the condition that they have a finite mean) and *ρ* = *λƐ(X*1*)/c <* 1, then

$$\psi(u) \sim \frac{\rho}{1-\rho} \int_{u}^{\infty} \overline{F_I}(y) \mathrm{d}y \quad \text{as } u \to \infty \tag{11}$$

a result that is often associated with the names of (in alphabetical order) Borovkov, Cohen, Embrechts, Pakes, Veraverbeke, and von Bahr.

That *FI* plays a role may be understood from the fact that *FI* is the distribution function of the first undershoot of *R(t)* − *u* below 0 under the condition that *R(t)* falls below *u* in finite time. The number *M* of times, where *R(t)* achieves a new local minimum in finite time plus 1, is geometrically distributed with parameter *(*1 − *ρ)*, that is, *-(M* = *n)* = *(*1 − *ρ)ρn, n* ∈ 0. This easily leads to the *Beekman–Bowers–Pollaczek–Khinchine formula*

$$\psi(u) = (1 - \rho) \sum_{n=1}^{\infty} \rho^n \overline{F_I^{n*}}(u), \quad u \ge 0 \quad (12)$$

from which equation (11) is an easy consequence.

For further aspects of ruin theory with heavy tails and a comprehensive set of recent references, see [5].

### **References**

- [1] Adler, R. & Feldman, R.E. (1998). *A Practical Guide to Heavy Tails: Statistical Techniques and Applications*, Birkhauser, Boston. ¨
- [2] Asmussen, S. (2001). *Ruin Probabilities*, World Scientific, Singapore.
- [3] Bingham, N.H., Goldie, C.M. & Teugels, J.L. (1987). *Regular Variation*, Cambridge University Press, Cambridge.
- [4] Embrechts, P., Kluppelberg, C. & Mikosch, T. (1997). ¨ *Modelling Extremal Events for Insurance and Finance*, Springer, Berlin.
- [5] Fasen, V. & Kluppelberg, C. (2008). Large insurance ¨ losses distributions, in E. Melnick & B. Everitt, eds, *Encyclopedia of Quantitative Risk Analysis and Assessment*, John Wiley & Sons, 961–969.
- [6] Mikosch, T. (2004). *Non-Life Insurance Mathematics*, Springer, Berlin.
- [7] Resnick, S.I. (2007). *Heavy-Tail Phenomena: Probabilistic and Statistical Modeling*, Springer, New York.
- [8] Rolski, T., Schmidli, H., Schmidt, V. & Teugels, J. (1999). *Stochastic Processes for Insurance and Finance*, Wiley, Chichester.

### **Related Articles**

#### **Accumulated Claims**; **Heavy Tails**; **Ruin Theory**.

SØREN ASMUSSEN, VICKY FASEN & CLAUDIA KLUPPELBERG ¨
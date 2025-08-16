# **Insurance Risk Models**

## The Classical Risk Model

We start by formulating the simplest risk model, which is based on the following independent objects:

- 1. a Poisson process (see **Poisson Process**)  $N =$  $\{N(t); t > 0\}$  with  $N(0) = 0$  and intensity  $\lambda_0$ , that is,  $E[N(t)] = \lambda_0 t$ ;
- 2. a sequence  $\{Z_k\}_1^{\infty}$  of independent and identically distributed (i.i.d.) random variables, having the common distribution function F, with  $F(0) = 0$ , mean value  $\mu$ , and variance  $\sigma^2$ .

The *risk process*,  $X$ , is defined by

$$X(t) = ct - \sum_{k=1}^{N(t)} Z_k, \quad \left(\sum_{k=1}^{0} Z_k \stackrel{\text{def}}{=} 0\right) \quad (1)$$

where  $c$  is a real constant.

This is the classical model of the risk business of an insurance company, where  $N(t)$  is to be interpreted as the number of claims on the company during the interval  $(0, t]$ . At each point of N, the company has to pay out a stochastic amount of money, and the company receives (deterministically)  $c$  units of money per unit time. The constant  $c$  is called the *gross risk premium* rate.

Many studies based on this model treat *ruin theory* (see Ruin Theory). Basic results about ruin probabilities for the classical risk model go back to 1926 [17] and 1930 [6], while the general ideas underlying the risk model go even farther back to 1903 [16]. A stringent treatment, based on Wiener-Hopf methods, is due to Cramér [7].

In risk theory, the most interesting situation is when  $c > 0$  and  $F(0) = 0$ . This case is generally called *positive risk sums*, and includes most nonlife branches and also the ordinary types of life insurance, where a certain amount of money is paid on the death of a policyholder.

There are, however, situations where the circumstances are reversed, that is, where  $c < 0$  and  $F(0) =$ 1 (see **Life Insurance**). The typical example is life annuity—or pension—insurance, where a life annuity rate  $-c$  is paid from the company to the policyholder and where the claim, that is, the death of the policyholder, will place an amount of money

corresponding to the "expected pension to be paid" at the company's free disposal. Thus the claim means an income, or a negative cost, for the company. This situation is generally called *negative risk sums*.

### **Models for the Occurrence of Claims**

A natural extension, at least from a mathematical point of view, of the Poisson process is to consider the case where the occurrence of the claims is described by a renewal process  $N$ . Let  $S_k$  denote the epoch of the kth claim. A point process is called a *renewal process* (with interoccurrence time distribution  $K^0$ ) if the variables  $S_1$ ,  $S_2 - S_1$ ,  $S_3 - S_2, \ldots$  are independent and if  $S_2 - S_1, S_3 S_2, \ldots$  have the same distribution  $K^0$ . Further, N is called an *ordinary* renewal process if  $S_1$  also has distribution  $K^0$ . N is called a *stationary* renewal process if  $K^0$  has finite mean  $1/\lambda_0$  and if  $S_1$  has distribution  $K$  given by

$$K(t) = \lambda_0 \int_0^t (1 - K^0(s)) \, \mathrm{d}s \tag{2}$$

A Poisson process (*see* **Poisson Process**) is a renewal process with exponentially distributed interoccurrence times. In that case, the ordinary and stationary versions coincide. Probably, the Poisson process is the most realistic renewal process for describing the occurrence of the claims. This, however, does not mean that it is uninteresting to consider renewal models, since often better mathematical clarity is achieved by explicit use of an interoccurrence time distribution. In connection with ruin theory, the renewal model was first studied in [2] and the corresponding risk process is often called the *Sparre Andersen model*. A detailed treatment is given in [21].

Let us now go back to the Poisson case. It is natural to assume that  $\lambda_0$  is proportional to the size of the insurance company. Naturally, the size of the company may vary in time. A simple way to take size variation into account is to let  $N$  be a nonhomogeneous Poisson process.

**Definition 1** A point process  $N$  is called a nonhomogeneous Poisson process with intensity function  $\lambda_0(t)$  if

- (i)  $N(t)$  has independent increments;
- (ii)  $N(t)-N(s)$  is Poisson distributed with mean  $\int_s^t \lambda_0(\tau) d\tau.$

If *λ*0*(t)* ≡ *λ*0, we are back to the Poisson process. The *intensity measure* is defined by

$$\Lambda_0(t) \stackrel{\text{def}}{=} \int_0^t \lambda_0(s) \, \text{d}s, \quad t \ge 0 \tag{3}$$

It is natural to let 0*(t)* have the representation (3), but it is enough to assume that 0*(t)* is a nondecreasing function with 0*(*0*)* = 0 and 0*(t) <* ∞ for each *t <* ∞. If 0*(t)* is continuous, then *N* is *simple*, that is, *N (t)* increases exactly one unit at its epochs of increase.

There may also be variation in the underlying risk. Typical examples are automobile insurance and fire insurance. It is natural to describe the underlying risk as a random process *λ* = {*λ(t)*; *t* ≥ 0} and to let *N* be the corresponding *Cox process.*

We think of a Cox process *N* as generated in the following way. First, a realization *λ*<sup>0</sup> of a random process *λ* is generated. Conditioned upon that realization, *N* is a nonhomogeneous Poisson process with intensity function *λ*0. A Cox process is stationary if and only if the underlying random process is stationary.

Let equation (3) the *random intensity measure* be defined by

$$\Lambda(t) \stackrel{\text{def}}{=} \int_0^t \lambda(s) \, \mathrm{d}s, \quad t \ge 0 \tag{4}$$

Assume that *E*[*(t )*2] *<* ∞ for all *t* ≥ 0. Then

$$E[N(t)] = E[\Lambda(t)] \text{ and } \text{Var}[N(t)]$$
  
=  $E[\Lambda(t)] + \text{Var}[\Lambda(t)] \text{ for all } t \ge 0 \quad (5)$ 

Thus a Cox process is overdispersed relative to a Poisson process.

For details of Cox processes, we refer to [12] or [13].

**Example 1 The Mixed Poisson Process** A Cox process with underlying random process *λ(t)* ≡ *λ*, where *λ* is a random variable, is called a *mixed Poisson process*. A mixed Poisson process where *λ* is -distributed is called a *P´olya process* and for any fixed value of *t* the random variable *N (t)* is negatively binomially distributed.

The mixed Poisson process is a natural model for the accident pattern of an individual policyholder. For instance, in automobile insurance, *λ* may describe the skillfulness of the individual as a driver. The distribution of *λ* may be regarded as a prior distribution. When the company knows more about the driver, the posterior distribution may be used instead.

In 1940, Ove Lundberg had already presented his thesis [18] about Markov point processes and, more particularly, mixed Poisson processes. The mixed Poisson processes have ever since played a prominent role in actuarial mathematics. A survey of mixed Poisson processes is found in [15].

**Example 2 The Ammeter Process** Let  *>* 0 be a fixed value and {*Lk*; *k* = 0*,* 1*,...*} a sequence of nonnegative, i.i.d. random variables. A rather simple Cox process is obtained by letting

$$\lambda(t) = L_k \quad \text{for } k\Delta \le t < (k+1)\Delta \tag{6}$$

The Cox process with this intensity is called an *Ammeter process*, since it is essentially the model considered by Ammeter [1]. A modern treatment of the Ammeter process is found in [14] and [15].

**Example 3 The Markov-modulated Poisson Process** Let *J* = {*J (t)*; *t* ≥ 0} be an *M*-state Markov process with state space {1*,* 2*,..., M*} and {*λ*1*, λ*2*, ..., λM* } a set of nonnegative numbers. The Cox process *N (t)* with *λ(t)* = *λJ (t)* is called a *Markovmodulated Poisson process*.

An equivalent way to express *N* is to consider *M* independent Poisson processes {*N*1*, N*2*,..., NM*} with intensities {*λ*1*, λ*2*,..., λM* } and to let the occurrence of the claims follow *Nk* when *J* = *k*. More formally, we let d*N (t)* = d*NJ (t)(t)*. This model was first studied in insurance by Reinhard [19], in the case *M* = 2 and exponentially distributed claims, and by Asmussen [3] in the general case.

**Example 4 Independent Jump Intensity** Intuitively, an independent jump intensity is a jump process where the jump times form a renewal process and where the value of the intensity between two successive jumps may depend only on the distance between these two jumps. More formally, let *k* , *k* = 1*,* 2*,...* denote the epoch of the *k*th jump of the intensity process and let <sup>0</sup> def =0. Put

$$\sigma_n = \Sigma_n - \Sigma_{n-1}\n$$
  
 $\nn = 1, 2, 3, \dots\n$ 
(7)
  
 $\nL_n = \lambda(\Sigma_{n-1})$ 

![](_page_2_Figure_1.jpeg)

Figure 1 Illustration of notation

Here we understand that  $\lambda$  has right-continuous realizations so that  $\lambda(t) = L_n$  for  $\Sigma_{n-1} \le t < \Sigma_n$ . These notations are illustrated in Figure 1.

An intensity process  $\lambda$  is called *an independent* jump intensity if the random vectors

$$(L_1, \sigma_1), (L_2, \sigma_2), (L_3, \sigma_3), \ldots$$

are independent and if  $(L_2, \sigma_2), (L_3, \sigma_3), \ldots$  have the same distribution.

This model was introduced in [4].

#### **Models for Cost of Claims and Income**

In the classical risk model, the random variables  $\{Z_k\}_1^\infty$  represent the cost of the claims and the gross risk premium rate  $c$ , the income. We, when nothing else is said, assume that  $\{Z_k\}_1^{\infty}$  is i.i.d. and independent of  $N$ .

Usually, the distribution  $F$  of  $Z_k$  is assumed to be either *exponentially bounded* (see Cramér-Lund**berg Estimates**) or to belong to the class  $S$ of subexponential distributions (see Heavy Tails in Insurance). These classes of distributions are also referred to as light tailed and heavy tailed, respectively.

**Definition 2** A distribution F on  $[0, \infty)$  belongs to  $\mathcal{S}$  if

$$\lim_{z \to \infty} \frac{1 - F^{2*}(z)}{1 - F(z)} = 2 \tag{8}$$

The  $\Gamma$ -distribution is a typical example of an exponentially bounded distribution, while the Pareto distribution and the lognormal distribution are subexponential. A class of exponentially distributed distributions of great interest is that of the phase-type distributions (see **Phase-type Distribution**).

It may very well be the case that a light-tailed  $F$  is too "kind" while an  $F \in \mathcal{S}$  is too "dangerous". Then it may be tempting to try to find some intermediate case with nice properties.  $S(\beta)$  is such a class:

**Definition 3** A distribution F on  $[0, \infty)$  belongs to the class  $S(\beta)$ ,  $\beta \geq 0$ , if

(i) 
$$\hat{h}(\beta) < \infty;$$
  
(ii)  $\lim_{z \to \infty} (1 - F^{2*}(z))/(1 - F(z)) = c,$ 

$$\ddot{o} < c < \infty;$$

(iii) 
$$\lim_{z \to \infty} \left(1 - F(z+y)\right) / \left(1 - F(z)\right) = e^{-\beta y}$$

for all real y.

Embrechts [11] has shown that certain generalized inverse Gaussian distributions belong to  $S(\beta)$ .

The classes  $S$  and  $S(\beta)$  were introduced by Chistvakov [5].

Sometimes, it may be natural to allow for dependence between  $\{Z_k\}_1^{\infty}$  and N. As an example, consider the Markov-modulated Poisson process motioned in Example 3. Let  $\{X_1, X_2, \ldots, X_M\}$  be M independent risk processes, as in equation  $(1)$ , where  $X_k$  has Poisson intensity  $\lambda_k$ , claim cost distribution  $F_k$ , and gross risk premium rate  $c_k$ . In automobile insurance, it is natural to allow the weather situation to have influence on both the intensity and the cost. The risk business X now follows  $X_k$  when  $J = k$ , that is,  $dX(t) = dX_{J(t)}(t)$ .

The generalization of a constant premium rate  $c$ mentioned above, may not be the most natural one. Examples of more relevant extensions of the premium rate within the risk model are given below:

- 1. The premiums may depend on the result of the risk business. It is natural to let the premium decrease when risk business increases and vice versa.
- 2. Inflation and interest may be included in the model. If the interest is higher than the inflation, then the premium decreases when risk business decreases and vice versa.
- Part of the risk business may be risky investments 3. (see Ruin Models with Investment Income).

References  $[8, 10]$  are very readable studies focusing mainly on generalizations  $(1)$  and  $(2)$ .

Early studies of generalizations  $(1)$  and  $(2)$  are found in [9, 20], respectively.

The question of "fair" premiums for an individual policyholder is of utmost importance for a company (*see* **Actuarial Premium Principles** and **Credibility Theory**). The discussion in Example 1 about prior and posterior distributions of *λ* is related to credibility theory.

## **References**

- [1] Ammeter, H. (1948). A generalization of the collective theory of risk in regard to fluctuating basic probabilities, *Skandinavisk Aktuarietidskrift*, 171–198.
- [2] Sparre Andersen, E. (1957). On the collective theory of risk in the case of contagion between the claims, *Transactions XVth International Congress of Actuaries*, Vol. 2, New York, 219–229.
- [3] Asmussen, S. (1989). Risk theory in a Markovian environment, *Scandinavian Actuarial Journal*, 66–100.
- [4] Bjork, T. & Grandell, J. (1988) ¨ . Exponential inequalities for ruin probabilities in the Cox case, *Scandinavian Actuarial Journal*, 77–111.
- [5] Chistyakov, P. (1964). Teorema o summah nezavisimyh poloitelnyh sluqa nyh veliqn i ee priloeni k vetvwims sluqa nym processam. Teori Verotnoste i ee Primeneni **9** 710–718 (English translation: A theorem on sums of independent random variables and its applications to branching processes. *Theory of Probability and its Applications* **9**, 640–648).
- [6] Cramer, H. (1930). ´ *On the Mathematical Theory of Risk*, Skandia Jubilee Volume, Stockholm (Reprinted in 1994 *Harald Cram´er Collected Works*, Vol. 1, Martin-Lof, A., ed, Skandia Insurance Company, Springer-Verlag, Berlin, p. 601–678).
- [7] Cramer, H. (1955). ´ *Collective Risk Theory*, Skandia Jubilee Volume, Stockholm (Reprinted in *Harald Cram´er Collected works Vol. II.* (1994), Ed. by Martin-Lof, A., Skandia Insurance Company, Springer-Verlag, Berlin, 1028–1115).
- [8] Dassios, A. & Embrechts, P. (1989). Martingales and insurance risk. *Communications in Statistics. Stochastic Models* **5**, 181–217.
- [9] Davidson, A.A. (1946). *Om ruinproblemet i den kollektiva riskteorin under antagande av variabel s¨akerhetsbelastning*, Fors ¨ akringsmatematiska studier till ¨ agnade ¨

Filip Lundberg, Stockholm, 32–47 (English translation: (1969). On the ruin problem in the collective theory of risk under the assumption of variable safety loading. *Skand. AktuarTidskr.Suppl.* 70–83).

- [10] Delbaen, F. & Haezendonck, J. (1987). Classical risk theory in an economic environment. *Insurance: Mathematics and Economics* **6**, 85–116.
- [11] Embrechts, P. (1983). A property of the generalized inverse Gaussian distribution with some applications. *Journal of Applied Probability* **20**, 537–544.
- [12] Grandell, J. (1976). *Doubly Stochastic Poisson Processes*, Lecture Notes in Mathematics, 529, Springer-Verlag, Berlin.
- [13] Grandell, J. (1991). *Aspects of Risk Theory*, Springer-Verlag, New York.
- [14] Grandell, J. (1995). Some remarks on the Ammeter risk process. *Mitteilungen der Vereinigung schweizerischer Versicherungsmathematiker* **95**, 43–72.
- [15] Grandell, J. (1997). *Mixed Poisson processes*, Chapman & Hall, London.
- [16] Lundberg, F. (1903). *I. Approximerad Framst¨allning av Sannolikhetsfunktionen. II. Aterf¨ ˚ ors¨akring av Kollektivrisker*, Almqvist & Wiksell, Uppsala.
- [17] Lundberg, F. (1926). *F¨ors¨akringsteknisk Riskutj¨amning*, F. Englunds boktryckeri A.B., Stockholm.
- [18] Lundberg, O. (1964). *On Random Processes and their Application to Sickness and Accident Statistics*, 2nd Edition, Almqvist & Wiksell, Uppsala.
- [19] Reinhard, J.M. (1984). *On a class of semi-Markov risk models obtained as classical risk models in a Markovian environment*, *Astin Bulletin*, **16**, 23–43.
- [20] Segerdahl, C.O. (1942). Uber einige risikotheoretische Fragestellungen, *Skandinacisk Aktuarietidskrift*, 43–83.
- [21] Thorin, O. (1982). Probabilities of ruin, *Scandinavian Actuarial Journal* 65–102.

## **Related Articles**

**Actuarial Premium Principles**; **Cramer–Lundberg ´ Estimates**; **Gerber–Shiu Function**; **Poisson Process**; **Point Processes**; **Ruin Theory**; **Ruin Models with Investment Income**.

JAN GRANDELL
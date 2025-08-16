# **Local Times**

The most obvious way to measure the time that a random process  $X$  spends at a value  $b$  on a time interval [0, *t*] is to compute  $\int_0^t 1_{\{X_s=b\}} ds$ . The problem is that this expression might be equal to 0, although the process  $X$  actually visits the value  $b$ . This is realized by the real Brownian motion (for a definition of this process, see Lévy Processes). Indeed, if we denote this process  $B$ , then for every fixed real b the set  $\{s \ge 0 : B_s = b\}$  has 0 Lebesgue measure and is infinite (and uncountable). However, one can measure the time that  $B$  spends at  $b$  by using the notion of *local time* defined by

$$L_t^b = \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_0^t 1_{\{|B_s - b| < \epsilon\}} \, \mathrm{d}s \tag{1}$$

where the limit is a pathwise limit.

For a fixed b, the process  $(L^b_t, t \ge 0)$  is an increasing process that only increases at times when  $B$  takes the value  $b$ . Under the assumption that  $B$  starts at 0, the processes  $(L^0_t, t \ge 0)$  and  $(2 \sup_{0 \le s \le t} B_s, s \ge 0)$ have the same law. This identity is due to Paul Lévy.

As  $b$  varies and  $t$  is fixed, one obtains the process  $(L_t^b, b \in \mathbb{R})$ , which actually represents the density of occupation time of  $B$  during the time interval  $[0, t]$ . This fact corresponds to the following formula called the occupation time formula

$$\int_0^t f(B_s) \, \mathrm{d}s = \int_{\mathbb{R}} f(b) L_t^b \, \mathrm{d}b \tag{2}$$

for every measurable bounded function  $f$ . This formula provides a definition of the local time equivalent to definition (1). For a fixed  $t$ , one does not know, special times excepted, the law of the process  $(L_t^b, b \in \mathbb{R})$ , but a lot of trajectorial results are established. For example, from [6], we have

$$\liminf_{t \to \infty} \sup_{x \in \mathbb{R}} L_t^x (t^{-1} \log \log t)^{1/2} = c \tag{3}$$

with  $0 < c < \infty$ , and

$$\limsup_{t \to \infty} \sup_{x \in \mathbb{R}} L_t^x(t \log \log t)^{-1/2} = \sqrt{2} \tag{4}$$

One of these special times is  $T_a$ , the first hitting time by *B* of a given value *a*. The law of  $(L_{T}^{b}, b \in$  $\mathbb{R}$ ) is described by one of the famous  $Ray-\overline{Knight}$ Theorems (see [8, Chapter XI]).

The local time of  $B$  can also be considered as a doubly indexed process. As such it is a.s. jointly continuous in  $b$  and  $t$  (see [9]) and deterministic functions on  $\mathbb{R} \times \mathbb{R}_+$  can be integrated with respect to  $(L_t^b, b \in \mathbb{R}, t \ge 0)$  (see Itô's Formula).

# **Local Time of a Semimartingale**

Similarly to formula (2), one can define the local time process of a semimartingale  $Y$  (for the definition of a semimartingale, see Stochastic Integrals) by using the following occupation time formula:

$$\int_0^t f(Y_s) \, \mathrm{d}[Y]_s^c = \int_{\mathbb{R}} f(b) L_t^b(Y) \, \mathrm{d}b \qquad (5)$$

where  $([Y]_c^c, s > 0)$  is the continuous part of the quadratic variation of Y also denoted by  $\langle Y \rangle$  (for the definition see Stochastic Integrals). For a fixed  $b\ (L^b(t), t>0)$  is a.s. continuous.

The obtained local time process  $(L_t^b(Y), b \in$  $\mathbb{R}, t \ge 0$ ) satisfies the following formula, called Tanaka's formula:

$$|Y_t - b| = |Y_0 - b| + \int_0^t \text{sgn}(Y_s - b) \, dY_s + \mathbf{L}_t^b$$
  
+ 
$$\sum_{0 < s \le t} \{ |Y_s - b| - |Y_{s-} - b| - \text{sgn}(Y_{s-} - b) \Delta Y_s \}$$

(6)

where the function sgn is defined by  $sgn(x) = 1_{x>0}$  - $1_{x<0}$ . Tanaka's formula actually provides a definition of the local time equivalent to formula (5). Thanks to this formula, Paul Lévy's identity is extended in  $[5]$  to the continuous semimartingales starting from 0 under the form

$$(L_t^0, t \ge 0) \stackrel{\text{(law)}}{=} \left( 2 \sup_{0 \le s \le t} \int_0^s \text{sgn}(-Y_u) \, \text{d}Y_u, t \ge 0 \right) \tag{7}$$

One can actually see Tanaka's formula as an example of extension of Itô's formula (see Itô's Formula).

Local time is also involved in inequalities reminiscent of the Burkholder-Davis-Gundy ones. Indeed, in [2], it is shown that there exist two universal positive and finite constants  $c$  and  $C$  such that

$$cE[\sup_{t} |X_{t}|] \leq E[\sup_{a} L_{\infty}^{a}] \leq CE[\sup_{t} |X_{t}|] \quad (8)$$

for any continuous local martingale  $X$  with  $X_0 = 0.$ 

### **Local Time of a Markov Process**

One can define the local time process of a Markov process  $X$  at a value  $b$  of its state space only if  $b$  is regular for  $X$  (see Markov Processes for the definition of Markov process). This means that starting from  $b$ , the process  $X$  then visits  $b$  at arbitrarily small times. Not every Markov process has this property. For example, a real-valued Lévy process (see Lévy Processes for the definition of that process) has this property at every point if its characteristic exponent  $\psi$  satisfies [3, Chapter II]

$$\int_{-\infty}^{+\infty} \mathcal{R}\left(\frac{1}{1+\psi(x)}\right) \mathrm{d}x < \infty \tag{9}$$

When  $b$  is regular for  $X$ , there exists a unique (up to a multiplicative constant) increasing continuous *additive functional*, that is, an adapted process  $(\ell_t^b(X), t > 0)$  starting from 0 such that

$$\ell^b_{t+s}(X) = \ell^b_t(X) + \ell^b_s(X) o\theta_t \tag{10}$$

increasing only at times when  $X$  takes the value  $b$ . This process is called the *local time* at  $b$ .

When it exists, the local time process  $(\ell^b(X), b \in$  $E, t > 0$ ) of a Markov process X with state space  $E$  might be jointly continuous in  $b$  and  $t$ . A necessary and sufficient condition for that property is given in [1] for Lévy processes as follows: set  $h(a) = \frac{1}{\pi} \int_{-\infty}^{\infty} (1 - \cos ab) \mathcal{R}(1/\psi(b)) \, \mathrm{d}b \text{ and } m(\varepsilon) =$  $\int_{\mathbb{R}} da 1_{\{h(a)<\varepsilon\}}$  for  $\varepsilon > 0$ ; then the considered Lévy process has a continuous local time process if

$$\int_{0+} \sqrt{\text{Log}\left(\frac{1}{m(\varepsilon)}\right)} \,\mathrm{d}\varepsilon < \infty \tag{11}$$

This result concerning Lévy processes has been extended to symmetric Markov processes in [7] and to general Markov processes in [4].

We mention that under condition  $(9)$ , the local time process of a Lévy process  $X$  satisfies the same occupation time formula as for the real Brownian motion:

$$\int_0^t f(X_s) \, \mathrm{d}s = \int_E f(b) \ell_t^b(X) \, \mathrm{d}b \tag{12}$$

In case a random process is both a Markov process with regular points and a semimartingale, it then admits two local time processes that are different (they might coincide as in the case of the Brownian motion). As an example, consider a symmetric stable process  $X$  with index in  $(1, 2)$  (for definition see **Lévy Processes**). We have  $[X]^{c} = 0$ ; hence, as a semimartingale,  $X$  has a local time process that identically equals 0. However, as a Markov process,  $X$  has a local time process that satisfies formula  $(12)$  and hence differs from 0. Besides, in this case, condition  $(11)$  is satisfied.

# References

- [1] Barlow, M.T. (1988). Necessary and sufficient conditions for the continuity of local times for Levy processes, Annals of Probability 16, 1389-1427.
- [2] Barlow, M.T. & Yor, M. (1981). (Semi-) Martingale inequalities and local times, Zeitschrift fur Wahrscheinlichkeitstheorie verw Gebiete 55, 237-254.
- Bertoin, J. (1996). Lévy Processes, Cambridge University [3] Press.
- [4] Eisenbaum, N. & Kaspi, H. (2007). On the continuity of local times of Borel right Markov processes, Annals of Probability 35, 915-934.
- [5] El Karoui, N. & Chaleyat-Maurel, M. (1978). Un problème de réflexion et ses applications au temps local et aux équations différentielles stochastiques sur  $\mathbb{R}$ , in *Temps* locaux-Astérisque, Société mathématiques de France, Paris, Vol. 52-53, pp. 117-144.
- [6] Kesten, H. (1965). An iterated logarithm law for local time, Duke Mathematical Journal 32, 447-456.
- [7] Marcus, M. & Rosen, J. (1995). Sample path properties of the local times of strongly symmetric Markov processes via Gaussian processes, Annals of Probability 20,  $1603 - 1684$
- [8] Revuz, D. & Yor, M. (1999). Continuous Martingale and Brownian Motion, 3rd Edition, Springer.
- [9] Trotter, H. (1958). A property of Brownian motion paths, Illinois Journal of Mathematics 2, 425-433.

#### NATHALIE EISENBAUM
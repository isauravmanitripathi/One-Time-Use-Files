## **Phase-type Distribution**

A phase-type distribution is a probability distribution that results from a system of one or more interrelated Poisson processes occurring in sequence or phases. Such distributions represent one of the most general classes of distributions permitting a probabilistic (i.e., Markovian) interpretation, as they are essentially based on the method of exponential stages technique that was introduced by Erlang in the early twentieth century and later generalized by Neuts in the mid-to-late 1970s. Phase-type distributions also possess a variety of desirable analytical properties that often facilitate their use in terms of yielding exact, algorithmically tractable, solution procedures. Phasetype distributions have been used extensively in many areas of applied probability, particularly in queueing theory (e.g., see [3]), actuarial risk theory (e.g., see [9]), and finance (e.g., see [4]). In addition, thorough treatments of phase-type distributions and their applications can be found in several reference texts including  $[1, 5, 7, 8, 10]$ . In what follows, we present only a brief overview of phase-type distributions and some of their key distributional properties.

In essence, phase-type distributions consist of a "general" mixture of exponentials and are characterized by an absorbing finite-state Markov chain. Specifically, let  $\{X(t), t > 0\}$  represent a homogeneous, continuous-time Markov chain with transient states  $\{1, 2, \ldots, n\}$  and single absorbing state labeled  $n+1$ . Define the row vector  $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_n)$ , wherein  $\alpha_i$  represents the probability of beginning (at time 0) in a transient state  $j, j = 1, 2, \dots, n$ . The infinitesimal generator  $Q$  associated with this Markov process can be represented as

$$Q = \begin{bmatrix} S & \underline{s}_0 \\ \underline{0} & 0 \end{bmatrix} \tag{1}$$

In equation (1), S is an  $n \times n$  nonsingular matrix containing the transition rates among the  $n$  transient states. The diagonal entries of  $S$  are necessarily negative, while the remaining entries of  $S$  are nonnegative. Furthermore,  $\underline{s}_0$  is the  $n \times 1$  column vector of absorption rates into state  $n + 1$  from the individual transient states. Necessarily,  $\underline{s}_0 = -S\underline{e}$ , where  $\underline{e}$ denotes an  $n \times 1$  column vector of ones. In addition, 0 represents a  $1 \times n$  row vector of zeros.

Let  $Y$  represent the time to absorption into state  $n + 1$ , namely  $Y = \inf\{t > 0 \mid X(t) = n + 1\}$ . The random variable  $Y$  is said to have a continuous phase-type distribution with (parametric) representation  $(\alpha, S)$  of dimension *n*, often denoted as  $Y \sim$  $PH_n(\alpha, S)$ . The cumulative distribution function and density function of  $Y$  are given by

$$F(y) = 1 - \underline{\alpha} \exp(Sy)\underline{e} \quad \text{and}$$
  
$$f(y) = \underline{\alpha} \exp(Sy)\underline{s}_0 \quad \text{for} \quad y \ge 0 \tag{2}$$

where the matrix exponential in equation (2) is defined by  $\exp(Sy) = \sum_{m=0}^{\infty} y^m S^m / m!$  Moreover, Y has Laplace-Stieltjes transform and integer moments given by

$$E\{e^{-tY}\} = 1 - \underline{\alpha} \underline{e} + \underline{\alpha}(tI - S)^{-1}\underline{s}_0 \quad \text{and}$$
$$E\{Y^k\} = (-1)^k k! \underline{\alpha} S^{-k} \underline{e} \tag{3}$$

where I denotes an  $n \times n$  identity matrix. Computation of the above matrix-based quantities is a routine task with the aid of most mathematical software packages in use today. A good reference for the calculation of matrix exponentials is [6].

One of the most important and useful features of the phase-type family of distributions is that the phase-type distribution is dense in the set of all positive-valued distributions, implying that it is (theoretically) possible to represent any positive-valued distribution with a "suitable" phasetype approximation. However, we emphasize the fact that the phase-type distribution is a lighttailed distribution (including combinations/mixtures of exponential and Erlang distributions as special cases), and thus it cannot be expected to fit a heavy-tailed distribution in the extreme tail. For an excellent treatment regarding phase-type fitting of arbitrary distributions, see [2] and references therein.

Numerous operations on phase-type distributions lead again to distributions that are phase-type with readily calculable parameters. This is a very appealing quality of phase-type distributions. In particular, convolutions, finite mixtures, and geometric compounds of phase-type distributions are again phasetype distributed. See  $[1, 7]$  for proofs of these results and further closure properties.

In conclusion, we state that a discrete analog to the continuous phase-type distribution exists by considering the time to absorption in an equivalent discrete-time Markov chain. We direct interested readers to [5, 7] for further details on discrete phasetype distributions.

## **References**

- [1] Asmussen, S. (2000). *Ruin Probabilities*, World Scientific, Singapore.
- [2] Asmussen, S. (2000). Matrix-analytic models and their analysis, *Scandinavian Journal of Statistics* **27**, 193–226.
- [3] Asmussen, S. (2003). *Applied Probability and Queues*, 2nd Edition, Springer-Verlag, New York.
- [4] Asmussen, S., Avram, F. & Pistorius, M. (2004). Russian and American put options under exponential phase-type Levy models, ` *Stochastic Processes and their Applications* **109**, 79–111.

- [5] Latouche, G. & Ramaswami, V. (1999). *Introduction to Matrix Analytic Methods in Stochastic Modeling*, ASA SIAM, Philadelphia.
- [6] Moler, C. & Van Loan, C. (2003). Nineteen dubious ways to compute the exponential of a matrix, twenty-five years later, *SIAM Review* **45**, 3–49.
- [7] Neuts, M. (1981). *Matrix-geometric Solutions in Stochastic Models: An Algorithmic Approach*, Johns Hopkins University Press, Baltimore.
- [8] Neuts, M. (1989). *Structured Stochastic Matrices of M/G/1 Type and Their Applications*, Marcel Dekker, New York.
- [9] Rolski, T., Schmidli, H., Schmidt, V. & Teugels, J. (1999). *Stochastic Processes for Insurance and Finance*, John Wiley & Sons, Chichester.
- [10] Wolff, R. (1989). *Stochastic Modeling and the Theory of Queues*, Prentice-Hall, NJ.

STEVE DREKIC
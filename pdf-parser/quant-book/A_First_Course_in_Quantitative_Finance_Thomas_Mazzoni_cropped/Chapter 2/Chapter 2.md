✖

# **2 A Primer on Probability**

Virtually all decisions we make are subject to a more or less large amount of uncertainty. The mathematical language of uncertainty is probability. This short introduction is intended to equip the reader with a conceptual understanding of the most important ideas with respect to quantitative finance. It is by no means an exhaustive treatment of this subject. Furthermore, a basic familiarity with the most fundamental principles of statistics is assumed.

# **2.1 Probability and Measure**

The mathematical laboratory for random experiments is called probability space. Its first constituent is the set of elementary states of the world Ω = {ω1, ω2, . . .} which may or may not realize. The set Ω may as well be an uncountable domain such as a subset of R. The elements ω1, ω2, . . . are merely labels for upcoming states of the world which are distinguishable to us in a certain sense. For example imagine tossing a coin. Apart from the very unusual case of staying on the edge, the coin will eventually come to rest either heads up or tails up. In this sense these two states of the world are distinguishable to us and we may want to label them as

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\Omega = \{H, T\}.\n$$
(2.1)

It is tempting to identify Ω with the set of events which describes the outcome of the random experiment of tossing the coin. However this is not quite true, because not all possible outcomes are contained in Ω, but only those of a certain elementary kind. For example the events "Heads or Tails" or "neither Heads nor Tails" are not contained in Ω. This observation immediately raises the question of what we mean exactly when we are talking of an event? An event is a set of elementary states of the world, for each of which we can tell with certainty whether or not it has realized after the random experiment is over. This is seen very easily by considering the throw of a die. There are six elementary states of the world we can distinguish by reading off the number on the top side after the die has come to rest. We can label these six states by Ω = {1, . . . , 6}. The outcome of throwing an even number for example, corresponds to the event

$$A = \{2, 4, 6\},\tag{2.2}$$

which means the event of throwing a two, a four, or a six. For each state of the world in *A* we can tell by reading off the number on the top side of the die, if it has realized or

not. Therefore, we can eventually answer the question if  $A$  has happened or not with certainty.

There are many more events that can be assembled from elementary states of the world. For example one may want to observe if the number thrown is smaller or equal to three. Which events have to be considered and are there rules for constructing such events? It turns out that there are strict rules by which events are collected in order to guarantee consistent answers for all possible outcomes. A family  $\mathcal{F}$  of sets (events)  $A, A_1, A_2, \ldots$  is called a  $\sigma$ -algebra, if it satisfies the following conditions

In (2.3),  $A^C$  is the complement of A, which contains all elements of  $\Omega$  that are not in A. These rules for  $\sigma$ -algebras have some interesting consequences. First of all,  $\mathcal{F}$  is not empty, which means there has to be at least one event  $A \in \mathcal{F}$ . The second rule now immediately implies that  $A^C \in \mathcal{F}$ , too, and by the third rule  $A \cup A^C = \Omega \in \mathcal{F}$ . But if  $\Omega$  is in  $\mathcal{F}$ , then  $\Omega^C = \emptyset$  is also in  $\mathcal{F}$  by rule two. Therefore, the smallest possible  $\sigma$ -algebra is  $\mathcal{F} = \{\emptyset, \Omega\}$ . Another interesting consequence is that for  $A_1, A_2, \ldots \in \mathcal{F}$  the intersection  $\bigcap_{n=1}^{\infty} A_n$  is also in  $\mathcal{F}$ . This is an immediate consequence of De Morgan's rule

$$\bigcap_{n=1}^{\infty} A_n = \left(\bigcup_{n=1}^{\infty} A_n^C\right)^C. \tag{2.4}$$

**Quick calculation 2.1** Verify that for  $A_1, A_2 \in \mathcal{F}$  the intersection  $A_1 \cap A_2$  is also in  $\mathcal{F}$ .

The pair  $(\Omega, \mathcal{F})$  is called a measurable space. The question of how such a space is constructed generally boils down to the question of how to construct  $\mathcal{F}$ . The smallest possible  $\sigma$ -algebra  $\mathcal{F} = \{0, \Omega\}$  has not enough structure to be of any practical interest. For countable and even for countably infinite  $\Omega$  one may choose the power set, indicated by  $2^{\Omega}$ , which is the family of all possible subsets of  $\Omega$  that can be constructed. There are  $2^{\text{#}\Omega}$  possible subsets, where the symbol # means "number of elements in"; thus the name power set. However, for uncountably infinite sets like  $\Omega = \mathbb{R}$  for example, the power set is too large. Instead one uses the  $\sigma$ -algebra, which is generated by all open intervals  $(a, b)$  in  $\mathbb{R}$  with  $a \leq b$ , the so-called *Borel-* $\sigma$ -algebra  $\mathcal{B}(\mathbb{R})$ . Due to the rules for  $\sigma$ -algebras (2.3), it contains much more than only open intervals. For example the closed intervals, generated by

$$\bigcap_{n=1}^{\infty} \left( a - \frac{1}{n}, b + \frac{1}{n} \right) = [a, b], \tag{2.5}$$

and sets like  $(a, b)^{C} = (-\infty, a] \cup [b, \infty)$  are also in  $\mathcal{B}(\mathbb{R})$ . We could have even chosen the closed or half open intervals in the first place. Roughly speaking, all sets that can be generated from open, half open, or closed intervals in a constructive way are in the *Borel-* $\sigma$ -algebra, but surprisingly, it is still not too large.

![](_page_2_Figure_1.jpeg)

**Fig. 2.1** Probability space as mathematical model for a fair coin toss

This discussion opens another interesting possibility, namely that σ-algebras may be generated. Again consider the throw of a die, where all that matters to us is if the number on the top side is even or odd after the die has settled down. Letting again Ω = {1, . . . , 6}, the σ-algebra generated by this (hypothetical) process is

$$\mathcal{F} = \{0, \{2, 4, 6\}, \{1, 3, 5\}, \Omega\}.$$
 (2.6)

**Quick calculation 2.2** Verify that F is indeed a valid σ-algebra.

A general statement is that the σ-algebra generated by the event *A* is F = {∅, *A*, *A <sup>C</sup>*, Ω}, or shorthand F =σ(*A*). It is easy to see that this σ-algebra is indeed the smallest one containing *A*.

A function µ :F → R + 0 , with the properties

1. 
$$\mu(\emptyset) = 0,$$
  
2.  $\mu\Big(\bigcup_{n=1}^{\infty} A_n\Big) = \sum_{n=1}^{\infty} \mu(A_n), \text{ for } A_1, A_2, \ldots \in \mathcal{F} \text{ and } A_i \cap A_j = \emptyset \text{ for } i \neq j,$ 

$$(2.7)$$

is called a measure on (Ω,F ). The triple (Ω,F , µ) is called a measure space. The concept of measure is the most natural concept of length, assigned to all sets in the σ-algebra. This becomes immediately clear by considering the measurable space (R, B), with the *Borel*-σ-algebra, generated by say the half open intervals(*a*, *b*] with *a* ≤ *b*, and choosing the *Lebesgue*-measure µ ( (*a*, *b*] ) = *b* − *a*. 1 In case of probability theory one assigns the overall length µ(Ω) = 1 to Ω. The associated measure is called probability and is abbreviated *P*(*A*) for *A* ∈ F . Furthermore, the triple (Ω,F ,*P*) is called probability space. Figure 2.1 illustrates the construction of the whole probability space for the (fair) coin toss experiment.

There is much more to say about probability spaces and measures than may yet appear. Measure theory is a very rich and subtle branch of mathematics. Nonetheless, most roads inevitably lead to highly technical concepts, barely accessible to

<sup>1</sup> Technically, the measure cannot be established on B directly, it has to be assigned on the semiring I = { (*a*, *b*] : *a*, *b* ∈ R and *a* ≤ *b* } . Afterwards, it can be extended to B =σ(I), which is the *Borel*-σ-algebra.

non-mathematicians. To progress in understanding the fundamental principles of financial markets they are a "nice to have" but not a key requirement at this point.

# **2.2 Filtrations and the Flow of Information**

In practice most of the time we are dealing not with isolated random experiments, but with processes that we observe from time to time, like the quotes of some preferred stock. Sometimes our expectations may be confirmed, other times we may be surprised by a totally unexpected development. We are observing a stochastic process, piece by piece revealing information over time. How is this flow of information incorporated in the static model of a probability space? Imagine tossing a coin two times in succession. We can label the elementary outcomes of this random experiment

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$\Omega = \{(H, H), (H, T), (T, H), (T, T)\}.\n$$
(2.8)

Now, invent a counting variable *t*, which keeps track of how many times the coin was tossed already. Obviously, this counting variable can take the values *t* ∈ {0, 1, 2}. We can now ask, what is the σ-algebra F*<sup>t</sup>* that is generated by the coin tossing process at stage (time) *t*? At *t* = 0 nothing has happened and all we can say at this time is that one of the four possible states of the world will realize with certainty. Therefore, the σ-algebra at *t* = 0 is

$$\mathcal{F}_0 = \{ \emptyset, \Omega \}. \tag{2.9}$$

Now imagine, the first toss comes out heads. We can now infer that one of the outcomes (*H*, · ) will realize with certainty and (*T*, · ) is no longer possible. Even though we do not yet have complete information, in the language of probability we can already say that the event *A* = { (*H*, *H*), (*H*,*T*) } has happened at time *t* = 1. Remember that event *A* states that either (*H*, *H*) or (*H*,*T*) will realize eventually, which is obviously true if the first toss was heads. An exactly analogous argument holds if the first toss comes out tails, *B*= { (*T*, *H*), (*T*,*T*) } . Taking events *A* and *B*, and adding all required unions and complements, one obtains the largest possible σ-algebra at *t* = 1,

$$\mathcal{F}_1 = \{ \emptyset, \{ (H, H), (H, T) \}, \{ (T, H), (T, T) \}, \Omega \}. \tag{2.10}$$

By comparing F<sup>0</sup> and F<sup>1</sup> it becomes clear how information flows. The finer the partition of the σ-algebra, the more information is revealed by the history of the process. Another important and by no means accidental fact is that F<sup>0</sup> ⊂ F1. It indicates that no past information will ever be forgotten.

Now let's consider the final toss of the coin. After this terminal stage is completed, we know the possible outcomes of the entire experiment in maximum detail. We are now able to say if for example the event { (*T*,*T*) } , or the event { (*H*,*T*) } has happened or not. Thus the family F<sup>2</sup> has the finest possible partition structure. Of course for F<sup>2</sup> to be a σ-algebra, we have also to consider all possible unions and complements. If one neatly adds all required sets, which is a tedious but not a difficult task, the resulting σ-algebra is the power set of Ω,

$$\mathcal{F}_2 = 2^{\Omega} = \{ \emptyset, \{ (H, H) \}, \{ (H, T) \}, \dots, \{ (H, T), (T, H), (T, T) \}, \Omega \}. \tag{2.11}$$

That is to say that every bit of information one can possibly learn about this process is revealed at *t* = 2. The ascending sequence of σ-algebras F*<sup>t</sup>* , with F<sup>0</sup> ⊆ F*<sup>t</sup>* ⊆ F , is called a filtration. If a filtration is generated by successively observing the particular outcomes of a process like the coin toss, it is called the natural filtration of that process. However, since the σ-algebra generated by a particular event is the smallest one, containing the generating event, the terminal σ-algebra of such a natural filtration is usually smaller than the power set of Ω.

**Quick calculation 2.3** Convince yourself that the natural filtration F2, generated by observing the events *A*<sup>1</sup> = { (*H*, *H*), (*H*,*T*) } and *A*<sup>2</sup> = { (*H*,*T*) } , has only eight elements.

# **2.3 Conditional Probability and Independence**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • Consider the probability space (Ω,F ,*P*) and an event *A* ∈ F with *P*(*A*) > 0. Now define

$$\mathcal{F}_A = \{A \cap B : B \in \mathcal{F}\},\tag{2.12}$$

the family of all intersections of *A* with every event in F . Then F*<sup>A</sup>* is itself a σ-algebra on *A* and the pair(*A*,F*A*) is a measurable space. Proving this statement is not very hard, so it seems more beneficial to illustrate it in an example.

# **Example 2.1**

Consider a measurable space (Ω,F ) for a six sided die, with Ω = {1, . . . , 6} and F = 2 Ω. Let *A* = {2, 4, 6} be the event of throwing an even number. Which events are contained in F*<sup>A</sup>* and why is it a σ-algebra on *A*?

#### Solution

Intersecting *A* with all other events in F generates the following family of sets

$$\mathcal{F}_A = \{\emptyset, \{2\}, \{4\}, \{6\}, \{2, 4\}, \{2, 6\}, \{4, 6\}, A\}.$$

But F*<sup>A</sup>* is the power set of *A* and thus it has to be a σ-algebra on *A*. ........................................................................................................................

In case of *P*(*A*) > 0, the probability measure *P*(*B*|*A*) is called the conditional probability of *B* given *A*, and is defined as

$$P(B|A) = \frac{P(B \cap A)}{P(A)}.\t(2.13)$$

The triple ( *A*, F*A*,*P*( · |*A*) ) forms a new measure space or more precisely a new probability space, which is again illustrated in an example.

**Example 2.2**

Take the measurable space (Ω, F ) for the six sided die of Example 2.1 and equip it with the probability measure

$$P(B) = \frac{\#B}{6},$$

for all *B* ∈ F . Now, as before, pick the particular event *A* = {2, 4, 6} of throwing an even number. What are the conditional probabilities of *P*(*A*|*A*), *P* ( {2}|*A* ) , and *P* ( {5}|*A* ) ?

Solution

First observe that under the original probability measure

$$P(A) = \frac{3}{6} = \frac{1}{2}.$$

One thus obtains

$$P(A|A) = \frac{P(A \cap A)}{P(A)} = \frac{P(A)}{P(A)} = 1,$$
  
$$P(\{2\}|A) = \frac{P(\{2\} \cap A)}{P(A)} = \frac{P(\{2\})}{P(A)} = \frac{\frac{1}{6}}{\frac{1}{2}} = \frac{1}{3},$$
  
$$P(\{5\}|A) = \frac{P(\{5\} \cap A)}{P(A)} = \frac{P(\emptyset)}{P(A)} = \frac{0}{\frac{1}{2}} = 0.$$

An immediate corollary to the definition of conditional probability (2.13) is Bayes' rule. Because *P*(*B* ∩ *A*) =*P*(*A* ∩ *B*), we have

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)} = \frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|B^C)P(B^C)}.$$
(2.14)

The last equality holds, because *B* ∩ *B <sup>C</sup>* = ∅ and *B* ∪ *B <sup>C</sup>* = Ω.

**Quick calculation 2.4** Prove this statement by using the additivity property of measures (2.7) on page 9.

Independence is another extremely important concept in probability theory. It means that by observing one event, one is not able to learn anything about another event. This is best understood by recalling that probability is in the first place a measure of length. Geometrically, the concept equivalent to independence is orthogonality. Consider two intervals *A* and *B*, situated on different axes, orthogonal to each other,

![](_page_6_Figure_1.jpeg)

Fig. 2.2 Intervals on orthogonal axes

see Figure 2.2. In this case, the *Lebesgue*-measure for the rectangle  $A \cap B$  is the product of the lengths of each side,  $\mu(A \cap B) = \mu(A)\mu(B)$ , which is of course the area. In complete analogy two events  $A$  and  $B$  are said to be independent, if

$$P(A \cap B) = P(A)P(B) \tag{2.15}$$

holds. But what does it mean that we can learn nothing about a particular event from observing another event? First, let's take a look at an example where independence fails. Again consider the six sided die and take  $A = \{2, 4, 6\}$  to be the event of throwing an even number. Suppose you cannot observe the outcome, but somebody tells you that the number thrown is less than or equal to three. In other words, the event  $B = \{1, 2, 3\}$ has happened. It is immediately clear, that you learn something from the information that  $B$  has happened because there is only one even number in  $B$  but two odd ones. If the die is fair, you would a priori have expected event A to happen roughly half the times you throw the die. Now you still do not know if A has happened or not, but in this situation you would expect it to happen only one third of the times. We can quantify this result by using the formal probability space of Example 2.2 for the fair die, and calculating the conditional probability

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(\{2\})}{P(B)} = \frac{1}{3},\tag{2.16}$$

which is precisely what we claimed it to be.

**Quick calculation 2.5** Confirm the last equality in  $(2.16)$ .

In particular,  $\frac{1}{6} = P(A \cap B) \neq P(A)P(B) = \frac{1}{2} \cdot \frac{1}{2}$ , which confirms that A and B are not independent events. If on the other hand  $B$  is the event of throwing a number smaller than or equal to two,  $B = \{1, 2\}$ , we do not learn anything from the information that  $B$  has happened or has not happened. We would still expect to see an even number in roughly half the times we throw the die. In this case, we can confirm that

$$\frac{1}{6} = P(A \cap B) = P(A)P(B) = \frac{1}{2} \cdot \frac{1}{3},\tag{2.17}$$

which means that A and B are indeed independent. An additional consequence of independence is that the conditional probability of an event collapses to the unconditional one,

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)P(B)}{P(B)} = P(A). \tag{2.18}$$

**Ouick calculation 2.6** Show that for the six sided die, the events of throwing an even number and throwing a number less than or equal to four are also independent.

# 2.4

# Random Variables and Stochastic Processes

Our discussion of probability spaces up to this point was by no means exhaustive. For example, measure theory comes with its own theory of integration, called the *Lebesgue*integral, which is conceptually very different from the *Riemann*-integral taught in high school. Whereas the *Lebesgue*-integral is easier to manipulate on a technical level, it is much harder to evaluate than the *Riemann*-integral, where one can use the fundamental theorem of calculus. Fortunately, except for some exotic functions, the results of both integrals coincide, so that we can establish a link between both worlds. The situation is exactly the same in case of the whole probability space. As we have seen, it is a very rigorous and elegant model for random experiments, but it is also very hard to calculate concrete results. Luckily, there exists a link to map the measurable space  $(\Omega, \mathcal{F})$  onto another measurable space<sup>2</sup>  $(E, \mathcal{B})$ , equipped with a distribution function F, induced by the original probability measure  $P$ . This link is established by a random variable or a stochastic process, respectively.

The designation random variable is a misnomer, because it really is a function  $X$ :  $\Omega \rightarrow E$ , mapping a particular state of the world onto a number. For example in the coin toss experiment, one could easily define the following random variable

$$X(\omega) = \begin{cases} 1 & \text{for } \omega = H, \\ 0 & \text{for } \omega = T. \end{cases}$$
(2.19)

Note that the link established by (2.19) is only meaningful, if for every set  $B \in \mathcal{B}$ , there is also a  $X^{-1}(B) \in \mathcal{F}$ , where the inverse mapping of the random variable X is defined by

$$X^{-1}(B) = \{ \omega \in \Omega : X(\omega) \in B \},\tag{2.20}$$

the set of all states  $\omega$ , in which  $X(\omega)$  belongs to B. If this condition holds,  $X(\omega)$  is also more precisely called a "measurable function." This condition is trivially fulfilled in the above example, because  $(2.19)$  is a one-to-one mapping. A nontrivial example, emphasizing the usefulness of this transformation, is the following:

<sup>&</sup>lt;sup>2</sup> Usually E is a subset of  $\mathbb{R}$ , whereas  $\mathcal{B}$  is the corresponding *Borel-* $\sigma$ -algebra. For countable E,  $\mathcal{B}$  may be chosen as the power set of  $E$ .

#### Example 2.3

Imagine tossing a coin  $N$  times, where each trial is independent of the previous one. Assume that heads is up with probability p and tails with  $1 - p$ . We are now interested in the probability of getting exactly  $k$  times heads.

Solution in the original probability space

Doing it by the book, first we have to set up a sample space

$$\Omega = \{(H, H, \ldots), (T, H, \ldots), \ldots, (T, T, \ldots)\}.$$

 $\Omega$  has already  $2^N$  elements. Because the sample space is countable, we may choose  $\mathcal{F} = 2^{\Omega}$ . Now we have to assign a probability to each event in  $\mathcal{F}$ . Because the tosses are independent, we can assign the probability

$$P(\{\omega\}) = p^{\#H(\omega)}(1-p)^{\#T(\omega)}$$

to each elementary event  $\{\omega\}$ , where in slight abuse of notation  $\#H(\omega)$  and  $\#T(\omega)$  means "number of heads/tails in  $\omega$ ," respectively. But an arbitrary event  $A \in \mathcal{F}$  is a union of those elementary events. Because they are all distinct, we have by the additivity property of measures

$$P(A) = \sum_{\omega \in A} P(\{\omega\}).$$

This assigning of probabilities has to be exercised for all possible events in  $\mathcal{F}$ . Think of it as laying out all events in  $\mathcal{F}$  on a large table and attaching a flag to each of them, labeled with the associated probability. Now we have to look for a very special event in  $\mathcal{F}$ , containing all sample points with exactly k times H and  $N-k$  times T, and no others. Because  $\mathcal{F} = 2^{\Omega}$ , this event has to be present somewhere on the table. Once we have identified it, we can finally read off the probability from its flag and we are done. What a mess.

Solution in the transformed probability space

Define the random variable  $X: \Omega \to E$ , where  $E = \{0, 1, \ldots, N\}$ , and

$$X(\omega) = \#H(\omega).$$

We do not even have to look at the new  $\sigma$ -algebra  $\mathcal{B}$ , because we are solely interested in the event  $B = \{k\}$ , which only contains one elementary sample point. We further know that each  $\omega$  in  $X^{-1}(B)$  has probability  $P(\{\omega\}) = p^k(1-p)^{N-k}$ . All we have to do is to count the number of these pre-images to obtain the so-called probability mass function

$$f(k) = P(X=k) = {N \choose k} p^k (1-p)^{N-k},$$

where  $\binom{N}{k} = \frac{N!}{k!(N-k)!}$  is the number of possible permutations of *k* heads in *N* trials.

We can even go one step further and ask what is the probability of at most  $k$  times heads in  $N$  trials? We then obtain the distribution function of the random variable  $X$ 

$$F(k) = P(X \le k) = \sum_{n=0}^{k} {N \choose n} p^n (1-p)^{N-n}, \qquad (2.21)$$

which is of course the binomial distribution. Obtaining this probability distribution in the original probability space would have certainly been a very cumbersome business.

The realization of a random variable X itself can generate a  $\sigma$ -algebra  $\mathcal{B} = \sigma(X)$ , which induces another  $\sigma$ -algebra in the original probability space via  $X^{-1}$  as in (2.20). This completes the link in both directions. Indeed the same argument can be refined a little bit more. If one observes a whole family of random variables  $X_l(\omega)$ , labeled by a continuous or discrete index set  $0 \le t \le T$ , there is also a family of  $\sigma$ -algebras  $\mathcal{F}_t$ induced by  $X_t^{-1}$  in the original probability space. But this is nothing else than the concept of filtrations. The family of random variables  $X_t(\omega)$  is called a stochastic process. If the filtration  $\mathcal{F}_t$  is generated by the process  $X_t$ , it is called the natural filtration of this process. If the process  $X_t$  is measurable with respect to  $\mathcal{F}_t$ , it is called "adapted" to this  $\sigma$ -algebra. An important example of a stochastic process in finance is the following:

## Example 2.4

The stochastic process  $W_t$ , characterized by the properties

- 1.  $W_0 = 0$
- 2.  $W_t$  has independent increments
- 3.  $W_t W_s \sim N(0, t s)$  for  $0 \le s < t$

is called the *Wiener*-process (or *Brown*ian motion). It is an important part of the famous *Black–Scholes*-theory of option pricing.

#### Explanation

First observe that the process  $W_t$  is specified completely in terms of its distribution function.  $N(0, t - s)$  represents the normal distribution with expectation value 0 and variance  $t - s$ . For any given time interval  $t - s$ , W is a continuous random variable with probability density function $^3$ 

$$f(w) = \frac{1}{\sqrt{2\pi(t-s)}} e^{-\frac{1}{2}\frac{w^2}{t-s}},$$

<sup>&</sup>lt;sup>3</sup> We will at a later time occasionally label the probability density function by  $p$  or  $q$  to refer to the associated probability measure.

which is the continuous analogue of the probability mass function of the discrete random variable *X* in Example 2.3. The corresponding distribution function is obtained not by summation, but by integration

$$F(w) = \int_{-\infty}^{w} f(x) dx.$$

A further subtlety of continuous random variables, originating from the uncountable nature of the sample space Ω, is that a singular point has probability zero. This is immediately obvious, since

$$P(w_1 \leq W \leq w_2) = \int_{w_1}^{w_2} f(x) dx = F(w_2) - F(w_1),$$

and for *w*<sup>1</sup> = *w*2, the integral collapses to zero. The best we can do is to calculate the probability for the small interval [*w*,*w* + *dw*], which is *f*(*w*)*dw*. ........................................................................................................................

A technical consequence of this somewhat peculiar feature of uncountable sample spaces is that there are nonempty sets with probability measure zero. These sets have by no means to be small. If Ω = R and F = B(R), then the whole set Q of rational numbers has probability zero. Such a set is called a null set. A probability space is called complete, if all subsets of null sets are elements of F . Fortunately, it is always possible to include all these subsets, but because most statements exclusively concern events with probability larger than zero, one indicates this restriction by appending the phrase "almost surely." For example the *Wiener*-process has almost surely continuous but non-differentiable trajectories (paths), which means that this property is at most violated by events with probability zero.

# **2.5 Moments of Random Variables**

There are some probability distributions of particular importance in finance. We have seen two of them, the binomial distribution in Example 2.3, and the normal distribution in Example 2.4. While the distribution function is fully sufficient to define the properties of a random variable, it is usually not very descriptive. Moments are additional concepts to characterize some particular features. The first moment of a random variable *X* is its expectation value *m*<sup>1</sup> = *E*[*X*]. It is defined in the discrete/continuous case as

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

$$E[X] = \sum_{n} x_n f(x_n) \quad \text{or} \quad E[X] = \int x f(x) dx, \tag{2.22}$$

respectively, provided that a density function for a continuous random variable exists, which is usually the case. The expectation value is best thought of as the center of probability mass. It is by no means always the "expected" value, as seen in Figure 2.3. Both

![](_page_11_Figure_1.jpeg)

**Fig. 2.3** Probability density functions  $f(x)$  and  $g(y)$  of two random variables  $X$  and  $Y$  with  $E[X] = E[Y] = 0$ 

random variables  $X$  and  $Y$  have expectation zero, but one would certainly not expect a value of  $Y$  to realize in the vicinity of zero.

To obtain the expectation value of a binomially distributed random variable  $X \sim$  $B(p, N)$ , we can either use (2.22), or remember that a single coin is tossed N times independently, and each toss has expectation value  $p = 1 \cdot p + 0 \cdot (1 - p)$ . Thus, the expectation value of  $N$  trials is

$$E[X] = N \cdot p. \tag{2.23}$$

Now consider another random variable Y, which is normally distributed,  $Y \sim N(\mu, \sigma^2)$ . To calculate its expectation value, we have to evaluate the integral

$$E[Y] = \int_{-\infty}^{\infty} y \cdot \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2} \left(\frac{y-\mu}{\sigma}\right)^2} dy. \tag{2.24}$$

To this end let's first make the substitution  $z = \frac{y-\mu}{\sigma}$ , which makes  $dy = \sigma dz$  and leaves the boundary of integration unchanged, and define

$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2},\tag{2.25}$$

which is the probability density function of a standard normally distributed random variable  $Z \sim N(0, 1)$ . With these substitutions one obtains

$$E[Y] = \mu \int_{-\infty}^{\infty} \phi(z) dz + \sigma \int_{-\infty}^{\infty} z \cdot \phi(z) dz.$$
 (2.26)

The first integral in  $(2.26)$  is equal to one, because it simply adds up all probabilities. The second integral is zero. To see that, observe that  $z \cdot \phi(z) = -\phi'(z)$  and

$$\int_{-\infty}^{\infty} -\phi'(z)dz = -\phi(z)\Big|_{-\infty}^{\infty} = 0. \tag{2.27}$$

Hence, the desired expectation value is

$$E[Y] = \mu. \tag{2.28}$$

Whereas the expectation value is defined as the first raw moment, the second moment is usually understood as a central moment, which means a moment around the expectation value, called the variance,  $M_2 = \text{Var}[X]$ . It is defined as

$$Var[X] = E[(X - E[X])^{2}] = E[X^{2}] - E[X]^{2}.$$
 (2.29)

The second equality follows from the fact that  $E[E[X]] = E[X]$ , and that the expectation value is a linear functional,  $E[aX + bY] = aE[X] + bE[Y]$  for  $a, b \in \mathbb{R}$ .

**Quick calculation 2.7** Confirm that the second equality in  $(2.29)$  indeed holds.

The positive root of the variance is called standard deviation, StD[X] =  $\sqrt{\text{Var}[X]}$ . Variance and standard deviation are measures of dispersion around the mean (center of probability mass). For binomially distributed X and normally distributed Y the variance is given here without proof

$$\operatorname{Var}[X] = N \cdot p(1 - p) \quad \text{and} \quad \operatorname{Var}[Y] = \sigma^2. \tag{2.30}$$

It is very convenient that the first two moments of a normal distribution coincide with its parameters. In fact the whole moment structure of a normal distribution is determined by the parameters  $\mu$  and  $\sigma$ . Evaluating the necessary integrals yields

$$M_{k} = \int_{-\infty}^{\infty} (y - \mu)^{k} \cdot \frac{1}{\sqrt{2\pi\sigma^{2}}} e^{-\frac{1}{2}(\frac{y-\mu}{\sigma})^{2}} dy = \begin{cases} 0 & \text{for odd } k, \\ (k-1)!!\sigma^{k} & \text{for even } k, \end{cases}$$
(2.31)

for  $k \ge 1$ , where  $k!! = k \cdot (k-2)!!$  and  $1!! = 1$ . Obviously, all odd moments vanish for normally distributed random variables. This is due to the symmetry of the distribution around  $\mu$ . Odd moments are exclusively related to asymmetries of the distribution. For example the (standardized) third moment is called the "skewness" of the distribution. Even moments are related to the proportion of probability mass located in the tails of the distribution. The more massive the tails, the higher the likelihood for extreme events. The (standardized) fourth moment is called the "kurtosis" and is 3 in case of a normal distribution. Most financial return time series show a dramatically higher kurtosis of 6 to 9, which indicates a more heavy tailed distribution than the normal.

A closely related concept is that of mixed moments. The most prominent representative of this class is the covariance. For two random variables X and Y, the covariance is defined as

$$Cov[X, Y] = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]. \qquad (2.32)$$

**Quick calculation 2.8** Verify the second equality in  $(2.32)$ , again by using the linearity of expectations.

Covariance is a linear measure of dependence between two random variables *X* and *Y*, because the expectation value is a linear functional. Generally, if two random variables have covariance zero this does not mean they are independent!

**Example 2.5**

Consider two random variables *X* ∼ *N*(0, 1) and *Y* = *X* 2 . Obviously, *X* and *Y* are highly dependent but what is their covariance?

#### Solution

Recall that for µ = 0, central moments and raw moments are identical, *M<sup>k</sup>* = *mk*. Applying (2.31) and (2.32) then yields

$$Cov[X, Y] = E[XY] - E[X]E[Y] = E[X^3] - E[X]E[X^2] = 0 + 0 \cdot 1 = 0.$$

........................................................................................................................

If on the other hand two random variables are independent, their covariance is guaranteed to vanish. The only exceptional case is when both random variables are normally distributed. Only in this case are independence and vanishing covariance equivalent statements. The normal distribution is therefore very special.

Often it is more intuitive to use a kind of standardized measure of linear dependence called correlation. This is not a new concept by itself, but merely a rescaled version of the covariance, defined by

$$\rho_{XY} = \frac{\text{Cov}[X, Y]}{\sqrt{\text{Var}[X]\text{Var}[Y]}}.\t(2.33)$$

Conveniently the range of the correlation coefficient is −1 ≤ ρ*XY* ≤ 1. Thus, one may express the linear dependence of two random variables in terms of positive or negative percentage value. Covariance and correlation are in one-to-one correspondence, therefore the term "uncorrelated" may be used interchangeably to also mean zero covariance.

# **2.6 Characteristic Function and Fourier-Transform**

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • The characteristic function of a random variable is essentially the *Fourier*-transform<sup>4</sup> of its probability density function (or its probability mass function in the discrete case)

$$\hat{f}(u) = \frac{1}{(2\pi)^{1-a}} \int_{-\infty}^{\infty} e^{-iux} f(x) dx,$$

<sup>4</sup> There is no genuine definition of a *Fourier*-transform. Most commonly, the *Fourier*-transform of an arbitrary function *f*: R → R is defined as

$$\varphi(u) = \int_{-\infty}^{\infty} e^{iux} f(x) dx = E[e^{iuX}]. \tag{2.34}$$

The letter *i* represents the imaginary unit,  $i = \sqrt{-1}$ . If you are not familiar with complex numbers, you can go over the basics in Appendix A. The characteristic function naturally comes in handy, if one tries to add independent random variables. Recall the example of a fair die. Clearly, the probability for getting any number between one and six is the same, namely  $f(n) = P(X = n) = \frac{1}{6}$  for  $n = 1, \ldots, 6$  and zero for any other number. But now imagine rolling two fair dice, without gluing them together or interfering in any other way. What is the probability of throwing snake eyes? Well, if both dice are fair and independent we simply multiply the probabilities of the single events,

$$g(2) = P(X_1 = 1, X_2 = 1) = f(1) \cdot f(1) = \frac{1}{36}.$$
 (2.35)

But what is the probability of throwing a seven? There are several possibilities of ending up with a seven. For example the first die could show a one and the second a six, or the first roll was a two and the second a five. We have to carefully add up all possibilities of getting a total sum of seven pips. The general solution to this problem is

$$g(k) = \sum_{n=1}^{6} f(n) \cdot f(k - n), \qquad (2.36)$$

for  $k = 2, \ldots, 12$ . The operation in (2.36) is called "folding" and it is the correct method for adding two independent random variables. Nevertheless, folding is usually a very inconvenient way of conducting this calculation. The characteristic function offers a much more efficient alternative. It is a general feature of *Fourier*-transforms that the operation of folding in the initial space translates to the operation of multiplication in *Fourier*-space. Let  $X_1, \ldots, X_N$  be N independent, not necessarily identically distributed random variables with characteristic functions  $\varphi_n(u)$  for  $n = 1, \ldots, N$ , then

$$X = \sum_{n=1}^{N} X_n \quad \Leftrightarrow \quad \varphi(u) = \prod_{n=1}^{N} \varphi_n(u), \tag{2.37}$$

and the probability density function of the sum X is obtained by inverse transforming its characteristic function

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-iux} \varphi(u) du.$$
 (2.38)

and its inverse transformation is

$$f(x) = \frac{1}{(2\pi)^a} \int_{-\infty}^{\infty} e^{iux} \hat{f}(u) du,$$

with a usually chosen to be 1 or  $\frac{1}{2}$ , and  $i = \sqrt{-1}$ . In (2.34) and (2.38), the role of the original and the inverse transformation is interchanged. Nevertheless, we simply call it the Fourier-transform hereafter.

Let's look at some examples and tie up some loose ends.

## Example 2.6

Consider the  $N$  times consecutively conducted coin toss experiment of Example 2.3. Each single toss is represented by a random variable  $X_n$ , with

$$X_n(\omega) = \begin{cases} 1 & \text{for } \omega = H, \\ 0 & \text{for } \omega = T. \end{cases}$$

What is the probability mass function of the sum  $X = X_1 + \cdots + X_N$ , representing the total number of "Heads" in the whole sequence?

Solution

First calculate the characteristic function of the single toss random variable  $X_n$ ,

$$\varphi_n(u) = E[e^{iuX_n}] = e^{iu\cdot 1}p + e^{iu\cdot 0}(1-p).$$

Note that in the discrete case the integral (2.34) reduces to a sum. All "copies" of  $X_n$ are identical, thus the characteristic function of X is

$$\varphi(u) = \varphi_n^N(u) = \left(e^{iu}p + (1-p)\right)^N$$

Using the binomial theorem, one can expand the last expression into a sum

$$\varphi(u) = \sum_{n=0}^{N} {N \choose n} e^{iun} p^n (1-p)^{N-n} = \sum_{n=0}^{N} e^{iun} f(n),$$

which is immediately identified as the expectation value  $E[e^{iuX}]$  with respect to the binomial distribution with probability mass function

$$f(n) = {N \choose n} p^n (1-p)^{N-n}.$$

In Example 2.6 it was not even necessary to calculate the inverse transformation because we were able to read off the resulting distribution from the characteristic function.

As a second example, let's show that a finite sum of independently normally distributed random variables is still normally distributed. To this end, we first compute the characteristic function of a standard normally distributed random variable, which is indeed the only tricky part. Let  $Z \sim N(0, 1)$ , then

$$\begin{split} \varphi_Z(u) &= \int_{-\infty}^{\infty} e^{iuz} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2} dz \\ &= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}(z - iu)^2 - \frac{1}{2}u^2} dz \\ &= e^{-\frac{1}{2}u^2} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}(z - iu)^2} dz, \end{split} \tag{2.39}$$

![](_page_16_Figure_1.jpeg)

**Fig. 2.4** 3D Standard normal probability density function on a complex line parallel to the real axis

where we completed the (imaginary) square in going from the first line to the second line. The question is, what is the integral in the third line? The correct answer is, it is a complex line integral. To see this, make the substitution ζ = *z* − *iu* to obtain

$$\int_{-iu-\infty}^{-iu+\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}\zeta^2} d\zeta = 1.$$
 (2.40)

To see heuristically why the value of this integral is one, we have to recall that the complex line along which the integral is evaluated is parallel to the real line, which means it does not vary in the imaginary direction; see Figure 2.4. Therefore, the area under the curve is not affected by shifting the whole density function in the imaginary direction of the complex plane. The characteristic function of a standard normally distributed random variable *Z* is thus

$$\varphi_Z(u) = e^{-\frac{1}{2}u^2}.\tag{2.41}$$

Obtaining the characteristic function of a random variable *X* ∼ *N*(µ, σ<sup>2</sup> ) is now an easy task using that *X* =σ*Z* + µ holds.

**Quick calculation 2.9** Verify that *X* has expectation value µ and variance σ 2 .

Indeed we get

$$\varphi_X(u) = E[e^{iu(\sigma Z + \mu)}] = e^{iu\mu} E[e^{iu\sigma Z}] = e^{iu\mu} \varphi_Z(u\sigma) \n= \exp\left(iu\mu - \frac{1}{2}u^2\sigma^2\right). \n$$
(2.42)

## **Example 2.7**

Consider a sum of *N* independent and not necessarily identically normally distributed random variables *X<sup>n</sup>* ∼ *N*(µ*n*, σ<sup>2</sup> *n* ) for *n* = 1, . . . , *N*. How is the sum *X* = *X*<sup>1</sup> + · · · + *X<sup>N</sup>* distributed?

#### Solution

To sum up all *Xn*s, we have to multiply their characteristic functions

$$\varphi(u) = \prod_{n=1}^{N} \varphi_n(u) = \exp\left(iu \sum_{n=1}^{N} \mu_n - \frac{1}{2}u^2 \sum_{n=1}^{N} \sigma_n^2\right).$$

From this, we can immediately conclude that *X* ∼ *N*(µ, σ<sup>2</sup> ), with

$$\mu = \sum_{n=1}^{N} \mu_n\n$$
 and  $\n\sigma^2 = \sum_{n=1}^{N} \sigma_n^2\n$ .

Generally, large sums of independent and identically distributed random variables tend to be normally distributed, even if their genuine distribution is far from normal. This peculiar fact is at the heart of the central limit theorem of statistics.

# **2.7 Further Reading**

There are lots of introductory texts on probability theory and statistics. In the context of quantitative finance there is an exceptionally well written textbook by Patrick Roger (2010), available for free at www.bookboon.com. There is also a very accessible and comprehensive book by Sheldon Ross (2010). To tackle the subtleties of measure theory and *Lebesgue*-integration technically, Rudin (1976, chap. 11) is a good starting point and Shreve (2004b, chap. 1) contains a remarkably clear exposition. For a concise but illuminating introduction to measure theory and probability in finance see Bingham and Kiesel (2004, chap. 2). A rigorous, but still largely comprehensible treatment of the whole subject is found in Shiryaev (1996).

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

# **2.8 Problems**

**2.1** Consider the simplified version of a wheel of fortune, given in Figure 2.5. Create a complete probability space as a model for one turn of the wheel. Assume that the wheel is fair in the same idealized way as the die is usually assumed to be.

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

![](_page_17_Figure_12.jpeg)

**Fig. 2.5** Simplified wheel of fortune with three possible outcomes

- **2.2** Calculate the natural filtration in the wheel of fortune example of problem 2.1, generated by the outcome *A* = {2}. Does F<sup>1</sup> = 2 <sup>Ω</sup> hold?
- **2.3** Consider rolling a fair die, with *X*(ω) as the number of pips and the event *A* of throwing an even number. Show that the conditional expectation, given *A*, is greater than the unconditional expectation.
- **2.4** Again consider the die example of Problem 2.3. Show that the property

$$E[X] = E[E[X|A]]$$

holds for *A* being the event of throwing an even number.

**2.5** A theorem by Kolmogorov (see Arnold, 1974, p. 24) states that every stochastic process *X*(*t*), which satisfies the inequality

$$E[|X(t) - X(s)|^{a}] \le c|t - s|^{1+b},$$

for *t* > *s* and a particular set of numbers *a*, *b*, *c* > 0, has almost surely continuous paths. Show that the *Wiener*-process meets this condition. Use the moment structure of normally distributed random variables (2.31) on page 19.

**2.6** Assume *N* ∼ Poi(λ) is a *Poisson*-distributed random variable with probability mass function

$$f(n) = e^{-\lambda} \frac{\lambda^n}{n!},$$

for *n* ∈ N0. Consider a random variable *X*, with

$$X = \sum_{n=0}^{N} X_n,$$

where *X<sup>n</sup>* are independent and identically distributed random variables. Prove that the relation

$$\varphi(u) = \exp[\lambda(\varphi_n(u) - 1)]$$

holds for the characteristic functions of *X* and *Xn*. Use the one-to-one correspondence of conditional probability and conditional distribution functions.
This chapter deals with algorithms at the core of Monte Carlo simulation: methods for generating uniformly distributed random variables and methods for transforming those variables to other distributions. These algorithms may be executed millions of times in the course of a simulation, making efficient implementation especially important.

Uniform and nonuniform random variate generation have each spawned a vast research literature; we do not attempt a comprehensive account of either topic. The books by Bratley, Fox, and Schrage [59], Devroye [95], Fishman [121], Gentle [136], Niederreiter [281], and others provide more extensive coverage of these areas. We treat the case of the normal distribution in more detail than is customary in books on simulation because of its importance in financial engineering.

# 2.1 Random Number Generation

### 2.1.1 General Considerations

At the core of nearly all Monte Carlo simulations is a sequence of apparently random numbers used to drive the simulation. In analyzing Monte Carlo methods, we will treat this driving sequence as though it were genuinely random. This is a convenient fiction that allows us to apply tools from probability and statistics to analyze Monte Carlo computations — convenient because modern *pseudorandom* number generators are sufficiently good at mimicking genuine randomness to make this analysis informative. Nevertheless, we should be aware that the apparently random numbers at the heart of a simulation are in fact produced by completely deterministic algorithms.

The objectives of this section are to discuss some of the primary considerations in the design of random number generators, to present a few simple generators that are good enough for practical use, and to discuss their implementation. We also provide references to a few more sophisticated (though

not necessarily better) methods. Elegant theory has been applied to the problem of random number generation, but it is mostly unrelated to the tools we use elsewhere in the book (with the exception of Chapter 5), so we do not treat the topic in depth. The books of Bratley, Fox, and Schrage [59], Fishman [121], Gentle [136], Knuth [212], and Niederreiter [281], and the survey article of L'Ecuyer [223] provide detailed treatment and extensive references to the literature.

Before discussing sequences that appear to be random but are not, we should specify what we mean by a generator of genuinely random numbers: we mean a mechanism for producing a sequence of random variables  $U_1, U_2, \ldots$ with the property that

- (i) each  $U_i$  is uniformly distributed between 0 and 1;
- (ii) the  $U_i$  are mutually independent.

Property (i) is a convenient but arbitrary normalization; values uniformly distributed between 0 and  $1/2$  would be just as useful, as would values from nearly any other simple distribution. Uniform random variables on the unit interval can be transformed into samples from essentially any other distribution using, for example, methods described in Section  $2.2$  and  $2.3$ . Property (ii) is the more important one. It implies, in particular, that all pairs of values should be uncorrelated and, more generally, that the value of  $U_i$  should not be predictable from  $U_1, \ldots, U_{i-1}$ .

A random number generator (often called a  $pseudorandom$  number generator to emphasize that it only mimics randomness) produces a finite sequence of numbers  $u_1, u_2, \ldots, u_K$  in the unit interval. Typically, the values generated depend in part on input parameters specified by the user.  $Any$  such sequence constitutes a set of possible outcomes of independent uniforms  $U_1, \ldots, U_K$ . A good random number generator is one that satisfies the admittedly vague requirement that small (relative to K) segments of the sequence  $u_1, \ldots, u_K$ should be difficult to distinguish from a realization of independent uniforms.

An effective generator therefore produces values that appear consistent with properties (i) and (ii) above. If the number of values  $K$  is large, the fraction of values falling in any subinterval of the unit interval should be approximately the length of the subinterval — this is uniformity. Independence suggests that there should be no discernible pattern among the values. To put this only slightly more precisely, statistical tests for independence should not easily reject segments of the sequence  $u_1, \ldots, u_K$ .

We can make these and other considerations more concrete through examples. A linear congruential generator is a recurrence of the following form:

$$x_{i+1} = ax_i \bmod m \tag{2.1}$$

$$u_{i+1} = x_{i+1}/m \tag{2.2}$$

Here, the *multiplier*  $a$  and the *modulus*  $m$  are integer constants that determine the values generated, given an initial value (seed)  $x_0$ . The seed is an integer

between 1 and  $m-1$  and is ordinarily specified by the user. The operation y mod m returns the remainder of y (an integer) after division by m. In other  $words,$ 

$$y \bmod m = y - |y/m|m, \tag{2.3}$$

where  $|x|$  denotes the greatest integer less than or equal to x. For example, 7  $\text{mod } 5 \text{ is } 2$ ; 10  $\text{mod } 5 \text{ is } 0$ ; 43  $\text{mod } 5 \text{ is } 3$ ; and 3  $\text{mod } 5 \text{ is } 3$ . Because the result of the mod m operation is always an integer between 0 and  $m-1$ , the output values  $u_i$  produced by (2.1)-(2.2) are always between 0 and  $(m-1)/m$ ; in particular, they lie in the unit interval.

Because of their simplicity and potential for effectiveness, linear congruential generators are among the most widely used in practice. We discuss them in detail in Section 2.1.2. At this point, we use them to illustrate some general considerations in the design of random number generators. Notice that the linear congruential generator has the form

$$x_{i+1} = f(x_i), \quad u_{i+1} = g(x_{i+1}), \tag{2.4}$$

for some deterministic functions  $f$  and  $g$ . If we allow the  $x_i$  to be vectors, then virtually all random number generators fit this general form.

Consider the sequence of  $x_i$  produced in (2.1) by a linear congruential generator with  $a = 6$  and  $m = 11$ . (In practice, m should be large; these values are solely for illustration.) Starting from  $x_0 = 1$ , the next value is 6 mod  $11 = 6$ , followed by  $(6 \cdot 6) \mod 11 = 3$ . The seed  $x_0 = 1$  thus produces  $\text{the sequence}$ 

$$1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1, 6, \ldots$$

Once a value is repeated, the entire sequence repeats. Indeed, since a computer can represent only a finite number of values, any recurrence of the form in  $(2.4)$  will eventually return to a previous  $x_i$  and then repeat all values that followed that  $x_i$ . Observe that in this example all ten distinct integers between 1 and  $m-1$  appeared in the sequence before a value was repeated. (If we were to start the sequence at  $0$ , all subsequent values would be zero, so we do not allow  $x_0 = 0$ .) If we keep  $m = 11$  but take  $a = 3$ , the seed  $x_0 = 1$  yields

$$1, 3, 9, 5, 4, 1, \ldots,$$

whereas  $x_0 = 2$  yields

Thus, in this case, the possible values  $\{1, 2, \ldots, 10\}$  split into two cycles. This means that regardless of what  $x_0$  is chosen, a multiplier of  $a = 3$  produces just five distinct numbers before it repeats, whereas a multiplier of  $a = 6$  produces all ten distinct values before repeating. A linear congruential generator that produces all  $m-1$  distinct values before repeating is said to have *full period*. In practice we would like to be able to generate (at least) tens of millions of distinct values before repeating any. Simply choosing  $m$  to be very large

does not ensure this property because of the possibility that a poor choice of parameters a and m may result in short cycles among the values  $\{1, 2, \ldots, m-1\}$ 1}.

With these examples in mind, we discuss the following general considerations in the construction of a random number generator:

- o *Period length*. As already noted, any random number generator of the form  $(2.4)$  will eventually repeat itself. Other things being equal, we prefer generators with longer periods  $-$  i.e., generators that produce more distinct values before repeating. The longest possible period for a linear congruential generator with modulus m is  $m-1$ . For a linear congruential generator with full period, the gaps between the values  $u_i$  produced are of width  $1/m$ ; hence, the larger m is the more closely the values can approximate a uniform distribution.
- $\circ$  Reproducibility. One might be tempted to look to physical devices a  $\text{computer's clock or a specially designed electronic mechanism}$  — to generate true randomness. One drawback of a genuinely random sequence is that it cannot be reproduced easily. It is often important to be able to rerun a simulation using exactly the same inputs used previously, or to use the same inputs in two or more different simulations. This is easily accomplished with a linear congruential generator or any other procedure of the general form  $(2.4)$  simply by using the same seed  $x_0$ .
- ∘ Speed. Because a random number generator may be called thousands or even millions of times in a single simulation, it must be fast. It is hard to imagine an algorithm simpler or faster than the linear congruential generator; most of the more involved methods to be touched on in Section  $2.1.5$  remain fast in absolute terms, though they involve more operations per value generated. The early literature on random number generation includes strategies for saving computing time through convenient parameter choices. For example, by choosing  $m$  to be a power of 2, the mod  $m$  operation can be implemented by shifting bits, without explicit division. Given current computing speeds, this incremental speed-up does not seem to justify choosing a generator with poor distributional properties.
- o *Portability*. An algorithm for generating random numbers should produce the same sequence of values on all computing platforms. The quest for speed and long periods occasionally leads to implementations that depend on machine-specific representations of numbers. Some implementations of linear congruential generators rely on the way overflow is handled on particular computers. We return to this issue in the next section.
- Randomness. The most important consideration is the hardest to define or ensure. There are two broad aspects to constructing generators with apparent randomness: theoretical properties and statistical tests. Much is known about the structure of points produced by the most widely used generators and this helps narrow the search for good parameter values. Generators with good theoretical properties can then be subjected to statistical scrutiny to

test for evident departures from randomness. Fortunately, the field is sufficiently well developed that for most applications one can comfortably use one of many generators in the literature that have survived rigorous tests and the test of time.

#### 2.1.2 Linear Congruential Generators

The general linear congruential generator, first proposed by Lehmer [229], takes the form

$$x_{i+1} = (ax_i + c) \bmod m$$
  
$$u_{i+1} = x_{i+1}/m$$

This is sometimes called a *mixed* linear congruential generator and the multiplicative case in the previous section a *pure* linear congruential generator. Like  $a$  and  $m$ , the parameter  $c$  must be an integer.

Quite a bit is known about the structure of the sets of values  $\{u_1,\ldots,u_K\}$ produced by this type of algorithm. In particular, simple conditions are available ensuring that the generator has full period  $-$  i.e., that the number of distinct values generated from any seed  $x_0$  is  $m-1$ . If  $c \neq 0$ , the conditions are (Knuth  $[212, p.17]$ )

(a)  $c$  and  $m$  are relatively prime (their only common divisor is 1);

(b) every prime number that divides  $m$  divides  $a-1$ ;

(c)  $a-1$  is divisible by 4 if m is.

As a simple consequence, we observe that if  $m$  is a power of 2, the generator has full period if c is odd and  $a = 4n + 1$  for some integer n.

If  $c = 0$  and m is prime, full period is achieved from any  $x_0 \neq 0$  if

 $\circ a^{m-1} - 1$  is a multiple of m;  $\circ a^{j}-1$  is not a multiple of m for  $j=1,\ldots,m-2$ .

A number a satisfying these two properties is called a *primitive root* of  $m$ . Observe that when  $c = 0$  the sequence  $\{x_i\}$  becomes

$$x_0, ax_0, a^2x_0, a^3x_0, \ldots \pmod{m}$$
.

The sequence first returns to  $x_0$  at the smallest k for which  $a^k x_0 \mod m = x_0$ . This is the smallest k for which  $a^k \mod m = 1$ ; i.e., the smallest k for which  $a^k-1$  is a multiple of m. So, the definition of a primitive root corresponds precisely to the requirement that the sequence not return to  $x_0$  until  $a^{m-1}x_0$ . It can also be verified that when a is a primitive root of m, all  $x_i$  are nonzero if  $x_0$  is nonzero. This is important because if some  $x_i$  were 0, then all subsequent values generated would be too.

Marsaglia [249] demonstrates that little additional generality is achieved by taking  $c \neq 0$ . Since a generator with a nonzero c is slower than one without,

it is now customary to take  $c = 0$ . In this case, it is convenient to take m to be prime, since it is then possible to construct full-period generators simply by finding primitive roots of  $m$ .

Table 2.1 displays moduli and multipliers for seven linear congruential generators that have been recommended in the literature. In each case, the modulus m is a large prime not exceeding  $2^{31} - 1$ . This is the largest integer that can be represented in a 32-bit word (assuming one bit is used to determine the sign) and it also happens to be a prime  $-$  a Mersenne prime. Each multiplier  $a$  in the table is a primitive root of the corresponding modulus, so all generators in the table have full period. The first generator listed was dubbed the "minimal standard" by Park and Miller [294]; though widely used, it appears to be inferior to the others listed. Among the remaining generators, those identified by Fishman and Moore  $[123]$  appear to have slightly better uniformity while those from L'Ecuyer  $[222]$  offer a computational advantage resulting from having comparatively smaller values of  $a$  (in particular,  $a < \sqrt{m}$ ). We discuss this computational advantage and the basis on which these generators have been compared next.

Generators with far longer periods are discussed in Section  $2.1.5$ . L'Ecuyer, Simard, and Wegenkittl [228] reject all "small" generators like those in Table 2.1 as obsolete. Section  $2.1.5$  explains how they remain useful as components of combined generators.

|                  | Modulus $m$ Multiplier $a$ Reference |                                         |
|------------------|--------------------------------------|-----------------------------------------|
| $2^{31}-1$       |                                      | 16807 Lewis, Goodman, and Miller [234], |
| $(= 2147483647)$ |                                      | Park and Miller $[294]$                 |
|                  |                                      | 39373 L'Ecuyer [222]                    |
|                  |                                      | 742938285 Fishman and Moore [123]       |
|                  |                                      | 950706376 Fishman and Moore [123]       |
|                  |                                      | 1226874159 Fishman and Moore [123]      |
| 2147483399       |                                      | $40692$ L'Ecuyer [222]                  |
| 2147483563       |                                      | 40014 L'Ecuyer [222]                    |

**Table 2.1.** Parameters for linear congruential generators. The generator in the first row appears to be inferior to the rest.

#### 2.1.3 Implementation of Linear Congruential Generators

Besides speed, avoiding overflow is the main consideration in implementing a linear congruential generator. If the product  $ax_i$  can be represented exactly for every  $x_i$  in the sequence, then no overflow occurs. If, for example, every integer from 0 to  $a(m-1)$  can be represented exactly in double precision, then implementation in double precision is straightforward.

If the multiplier  $a$  is large, as in three of the generators of Table 2.1, even double precision may not suffice for an exact representation of every product  $ax_i$ . In this case, the generator may be implemented by first representing the multiplier as  $a = 2^{\alpha}a_1 + a_2$ , with  $a_1, a_2 < 2^{\alpha}$ , and then using

$$ax_i \bmod m = (a_1(2^{\alpha}x_i \bmod m) + a_2x_i \bmod m) \bmod m.$$

For example, with  $\alpha = 16$  and  $m = 2^{31} - 1$  this implementation never requires an intermediate value as large as  $2^{47}$ , even though  $ax_i$  could be close to  $2^{62}$ .

Integer arithmetic is sometimes faster than floating point arithmetic, in which case an implementation in integer variables is more appealing than one using double precision. Moreover, if variables  $y$  and  $m$  are represented as integers in a computer, the integer operation  $y/m$  produces  $|y/m|$ , so y mod m can be implemented as  $y - (y/m) * m$  (see (2.3)). However, working in integer variables restricts the magnitude of numbers that can be represented far more than does working in double precision. To avoid overflow, a straightforward implementation of a linear congruential generator in integer variables must be restricted to an unacceptably small modulus — e.g.,  $2^{15} - 1$ . If a is not too large (say  $a \leq \sqrt{m}$ , as in the first two and last two entries of Table 2.1), Bratley, Fox, and Schrage [59] show that a faster implementation is possible using only integer arithmetic, while still avoiding overflow.

Their method is based on the following observations. Let

$$q = \lfloor m/a \rfloor, \quad r = m \bmod a$$

so that the modulus can be represented as  $m = aq + r$ . The calculation to be carried out by the generator is

$$ax_i \bmod m = ax_i - \left\lfloor \frac{ax_i}{m} \right\rfloor m$$
  
=  $\left( ax_i - \left\lfloor \frac{x_i}{q} \right\rfloor m \right) + \left( \left\lfloor \frac{x_i}{q} \right\rfloor - \left\lfloor \frac{ax_i}{m} \right\rfloor \right) m.$  (2.5)

The first term on the right in  $(2.5)$  satisfies

$$\begin{split} ax_i - \left\lfloor \frac{x_i}{q} \right\rfloor m &= ax_i - \left\lfloor \frac{x_i}{q} \right\rfloor (aq+r) \\ &= a \left( x_i - \left\lfloor \frac{x_i}{q} \right\rfloor q \right) - \left\lfloor \frac{x_i}{q} \right\rfloor r \\ &= a(x_i \bmod q) - \left\lfloor \frac{x_i}{q} \right\rfloor r. \end{split}$$

Making this substitution in  $(2.5)$  yields

$$ax_i \bmod m = a(x_i \bmod q) - \left\lfloor \frac{x_i}{q} \right\rfloor r + \left( \left\lfloor \frac{x_i}{q} \right\rfloor - \left\lfloor \frac{ax_i}{m} \right\rfloor \right) m.$$
 (2.6)

To prevent overflow, we need to avoid calculation of the potentially large term  $ax_i$  on the right side of (2.6). In fact, we can entirely avoid calculation of

$$\left(\left\lfloor\frac{x_i}{q}\right\rfloor - \left\lfloor\frac{ax_i}{m}\right\rfloor\right) \tag{2.7}$$

if we can show that this expression takes only the values  $0$  and  $1$ . For in this case, the last term in  $(2.6)$  is either 0 or m, and since the final calculation must result in a value in  $\{0, 1, \ldots, m-1\}$ , the last term in (2.6) is m precisely when

$$a(x_i \bmod q) - \left\lfloor \frac{x_i}{q} \right\rfloor r < 0.$$

Thus, the last term in  $(2.6)$  adds m to the first two terms precisely when not doing so would result in a value outside of  $\{0, 1, \ldots, m-1\}$ .

It remains to verify that  $(2.7)$  takes only the values 0 and 1. This holds if

$$\frac{x_i}{q} - \frac{ax_i}{m} \le 1. \tag{2.8}$$

But  $x_i$  never exceeds  $m-1$ , and

46

$$\frac{m-1}{q} - \frac{a(m-1)}{m} = \frac{r(m-1)}{qm}.$$

Thus, (2.8) holds if  $r \leq q$ ; a simple sufficient condition ensuring this is  $a \leq$  $\sqrt{m}$ .

The result of this argument is that  $(2.6)$  can be implemented so that every intermediate calculation results in an integer between  $-(m-1)$  and  $m-1$ , allowing calculation of  $ax_i \mod m$  without overflow. In particular, explicit calculation of  $(2.7)$  is avoided by checking indirectly whether the result of this calculation would be 0 or 1. L'Ecuyer [222] gives a simple implementation of this idea, which we illustrate in Figure  $2.1$ .

> $(m, a \text{ integer constants})$  $q, r$  precomputed integer constants, with  $q = \lfloor m/a \rfloor, r = m \bmod a$  $x$  integer variable holding the current  $x_i$ )  $k \leftarrow x/q$  $x \leftarrow a \ast (x - k \ast q) - k \ast r$ if  $(x < 0)$   $x \leftarrow x + m$

Fig. 2.1. Implementation of  $ax \mod m$  in integer arithmetic without overflow, assuming  $r \leq q$  (e.g.,  $a \leq \sqrt{m}$ ).

The final step in using a congruential generator — converting the  $x_i \in$  $\{0, 1, \ldots, m-1\}$  to a value in the unit interval — is not displayed in Figure 2.1. This can be implemented by setting  $u \leftarrow x \ast h$  where h is a precomputed constant equal to  $1/m$ .

Of the generators in Table 2.1, the first two and the last two satisfy  $a \leq \sqrt{m}$ and thus may be implemented using Figure  $2.1$ . L'Ecuyer [222] finds that the second, sixth, and seventh generators listed in the table have the best distributional properties among all choices of multiplier  $a$  that are primitive roots of m and satisfy  $a \leq \sqrt{m}$ ,  $m \leq 2^{31} - 1$ . Fishman [121] recommends working in double precision in order to get the somewhat superior uniformity of the large multipliers in Table  $2.1$ . We will see in Section  $2.1.5$  that by combining generators it is possible to maintain the computational advantage of having  $a \leq \sqrt{m}$  without sacrificing uniformity.

### Skipping Ahead

It is occasionally useful to be able to split a random number stream into apparently unrelated subsequences. This can be implemented by initializing the same random number to two or more distinct seeds. Choosing the seeds arbitrarily leaves open the possibility that the ostensibly unrelated subsequences will have substantial overlap. This can be avoided by choosing the seeds far apart along the sequence produced by a random number generator.

With a linear congruential generator, it is easy to skip ahead along the sequence without generating intermediate values. If  $x_{i+1} = ax_i \mod m$ , then

$$x_{i+k} = a^k x_i \bmod m$$

This in turn is equivalent to

$$x_{i+k} = ((a^k \bmod m)x_i) \bmod m.$$

Thus, one could compute the constant  $a^k \mod m$  just once and then easily produce a sequence of values spaced  $k$  apart along the generator's output. See L'Ecuyer, Simard, Chen, and Kelton  $[227]$  for an implementation.

Splitting a random number stream carefully is essential if the subsequences are to be assigned to parallel processors running simulations intended to be independent of each other. Splitting a stream can also be useful when simulation is used to compare results from a model at different parameter values. In comparing results, it is generally preferable to use the same random numbers for both sets of simulations, and to use them for the same purpose in both to the extent possible. For example, if the model involves simulating  $d$ asset prices, one would ordinarily want to arrange matters so that the random numbers used to simulate the *i*th asset at one parameter value are used to simulate the same asset at other parameter values. Dedicating a separate subsequence of the generator to each asset ensures this arrangement.

#### 2.1.4 Lattice Structure

In discussing the generators of Table 2.1, we alluded to comparisons of their distributional properties. We now provide a bit more detail on how these

comparisons are made. See Knuth [212] and Neiderreiter [281] for far more thorough treatments of the topic.

If the random variables  $U_1, U_2, \ldots$  are independent and uniformly distributed over the unit interval, then  $(U_1, U_2)$  is uniformly distributed over the unit square,  $(U_1, U_2, U_3)$  is uniformly distributed over the unit cube, and so on. Hence, one way to evaluate a random number generator is to form points in  $[0,1]^d$  from consecutive output values and measure how uniformly these points fill the space.

The left panel of Figure 2.2 plots consecutive overlapping pairs  $(u_1, u_2)$ ,  $(u_2, u_3), \ldots, (u_{10}, u_{11})$  produced by a linear congruential generator. The parameters of the generator are  $a = 6$  and  $m = 11$ , a case considered in Section 2.1.1. The graph immediately reveals a regular pattern: the ten distinct points obtained from the full period of the generator lie on just two parallel lines through the unit square.

This phenomenon is characteristic of all linear congruential generators (and some other generators as well), though it is of course particularly pronounced in this simple example. Marsaglia [248] showed that overlapping  $d$ tuples formed from consecutive outputs of a linear congruential generator with modulus m lie on at most  $(d!m)^{1/d}$  hyperplanes in the d-dimensional unit cube. For  $m = 2^{31} - 1$ , this is approximately 108 with  $d = 3$  and drops below 39 at  $d = 10$ . Thus, particularly in high dimensions, the lattice structure of even the best possible linear congruential generators distinguishes them from genuinely random numbers.

The right panel of Figure 2.2, based on a similar figure in L'Ecuyer  $[222]$ , shows the positions of points produced by the first generator in Table  $2.1$ . The figure magnifies the strip  $\{(u_1, u_2) : u_1 < .001\}$  and plots the first 10,005 points that fall in this strip starting from a seed of  $x_0 = 8835$ . (These are all the points that fall in the strip out of the first ten million points generated by the sequence starting from that seed.) At this magnification, the lattice structure becomes evident, even in this widely used method.

The lattice structure of linear congruential generators is often used to compare their outputs and select parameters. There are many ways one might try to quantify the degree of equidistribution of points on a lattice. The most widely used in the analysis of random number generators is the *spectral test*, originally proposed by Coveyou and Macpherson [88]. For each dimension  $d$  and each set of parallel hyperplanes containing all points in the lattice, consider the distance between adjacent hyperplanes. The spectral test takes the maximum of these distances over all such sets of parallel hyperplanes.

To see why taking the maximum is appropriate, consider again the left panel of Figure 2.2. The ten points in the graph lie on two positively sloped lines. They also lie on five negatively sloped lines and ten vertical lines. Depending on which set of lines we choose, we get a different measure of distance between adjacent lines. The maximum distance is achieved by the two positively sloped lines passing through the points, and this measure is clearly the one that best captures the wide diagonal swath left empty by the generator.

![](_page_10_Figure_0.jpeg)

Fig. 2.2. Lattice structure of linear congruential generators.

Although the spectral test is an informative measure of uniformity, it does not provide a strict ranking of generators because it produces a separate value for each dimension  $d$ . It is possible for each of two generators to outperform the other at some values of d. Fishman and Moore [123] and L'Ecuyer [222] base their recommendations of the values in Table 2.1 on spectral tests up to dimension  $d = 6$ ; computing the spectral test becomes increasingly difficult in higher dimensions. L'Ecuyer [222] combines results for  $d = 2-6$  into a worstcase figure of merit in order to rank generators.

Niederreiter [281] analyzes the uniformity of point sets in the unit hypercube (including those produced by various random number generators) through discrepancy measures, which have some appealing theoretical features not shared by the spectral test. Discrepancy measures are particularly important in the analysis of *quasi-Monte Carlo* methods.

It is also customary to subject random number generators to various statistical tests of uniformity and independence. See, e.g., Bratley, Fox, and Schrage  $[59]$  or Knuth  $[212]$  for a discussion of some of the tests often used.

Given the inevitable shortcomings of any practical random number generator, it is advisable to use only a small fraction of the period of a generator. This again points to the advantage of generators with long periods — much longer than  $2^{31}$ .

### 2.1.5 Combined Generators and Other Methods

We now turn to a discussion of a few other methods for random number generation. Methods that combine linear congruential generators appear to be particularly promising because they preserve attractive computational features of these generators while extending their period and, in some cases, attenuating

their lattice structure. A combined generator proposed by L'Ecuyer [224] and discussed below appears to meet the requirements for speed, uniformity, and a long period of most current applications. We also note a few other directions of work in the area.

### Combining Generators

One way to move beyond the basic linear congruential generator combines two or more of these generators through summation. Wichmann and Hill [355] propose summing values in the unit interval (i.e., after dividing by the modulus); L'Ecuyer  $[222]$  sums first and then divides.

To make this more explicit, consider J generators, the *j*th having parameters  $a_i, m_i$ :

$$x_{j,i+1} = a_j x_{j,i} \bmod m_j, \quad u_{j,i+1} = x_{j,i+1}/m_j, \quad j = 1, \dots, J.$$

The Wichmann-Hill combination sets  $u_{i+1}$  equal to the fractional part of  $u_{1,i+1} + u_{2,i+1} + \cdots + u_{J,i+1}$ . L'Ecuyer's combination takes the form

$$x_{i+1} = \sum_{j=1}^{J} (-1)^{(j-1)} x_{j,i+1} \mod (m_1 - 1)$$
 (2.9)

and

$$u_{i+1} = \begin{cases} x_{i+1}/m_1, & x_{i+1} > 0; \\ (m_1 - 1)/m_1, & x_{i+1} = 0. \end{cases}$$
(2.10)

This assumes that  $m_1$  is the largest of the  $m_i$ .

A combination of generators can have a much longer period than any of its components. A long period can also be achieved in a single generator by using a larger modulus, but a larger modulus complicates the problem of avoiding overflow. In combining generators, it is possible to choose each multiplier  $a_i$  smaller than  $\sqrt{m_i}$  in order to use the integer implementation of Figure 2.1 for each. The sum in  $(2.9)$  can then also be implemented in integer arithmetic, whereas the Wichmann-Hill summation of  $u_{j,i}$  is a floating point operation. L'Ecuyer [222] gives a portable implementation of  $(2.9)$ – $(2.10)$ . He also examines a combination of the first and sixth generators of Table 2.1 and finds that the combination has no apparent lattice structure at a magnification at which each component generator has a very evident lattice structure. This suggests that combined generators can have superior uniformity properties as well as long periods and computational convenience.

Another way of extending the basic linear congruential generator uses a higher-order recursion of the form

$$x_i = (a_1 x_{i-1} + a_2 x_{i-2} + \cdots a_k x_{i-k}) \bmod m, \tag{2.11}$$

followed by  $u_i = x_i/m$ ; this is called a *multiple recursive* generator, or MRG. A seed for this generator consists of initial values  $x_{k-1}, x_{k-2}, \ldots, x_0$ .

Each of the lagged values  $x_{i-j}$  in (2.11) can take up to m distinct values, so the vector  $(x_{i-1}, \ldots, x_{i-k})$  can take up to  $m^k$  distinct values. The sequence  $x_i$  repeats once this vector returns to a previously visited value, and if the vector ever reaches  $(0,\ldots,0)$  all subsequent  $x_i$  are identically 0. Thus, the longest possible period for (2.11) is  $m^k - 1$ . Knuth [212] gives conditions on  $m$  and  $a_1, \ldots, a_k$  under which this bound is achieved.

L'Ecuyer [224] combines MRGs using essentially the mechanism in  $(2.9)$ - $(2.10)$ . He shows that the combined generator is, in a precise sense, a close approximation to a single MRG with a modulus equal to the product of the moduli of the component MRGs. Thus, the combined generator has the advantages associated with a larger modulus while permitting an implementation using smaller values. L'Ecuyer's investigation further suggests that a combined MRG has a less evident lattice structure than the large-modulus MRG it approximates, indicating a distributional advantage to the method in addition to its computational advantages.

L'Ecuyer  $[224]$  analyzes and recommends a specific combination of two MRGs: the first has modulus  $m = 2^{31} - 1 = 2147483647$  and coefficients  $a_1 = 0, a_2 = 63308, a_3 = -183326$ ; the second has  $m = 2145483479$  and  $a_1 = 86098$ ,  $a_2 = 0$ ,  $a_3 = -539608$ . The combined generator has a period close to  $2^{185}$ . Results of the spectral tests in L'Ecuyer [224] in dimensions 4-20 indicate far superior uniformity for the combined generator than for either of its components. Because none of the coefficients  $a_i$  used in this method is very large, an implementation in integer arithmetic is possible. L'Ecuyer  $[224]$ gives an implementation in the  $C$  programming language which we reproduce in Figure 2.3. We have modified the introduction of the constants for the generator, using #define statements rather than variable declarations for greater speed, as recommended by L'Ecuyer [225]. The variables  $x10, \ldots, x22$  must be initialized to an arbitrary seed before the first call to the routine.

Figure 2.4 reproduces an implementation from L'Ecuyer [225]. L'Ecuyer [225] reports that this combined generator has a period of approximately  $2^{319}$ and good uniformity properties at least up to dimension 32. The variables  $s10, \ldots, s24$  must be initialized to an arbitrary seed before the first call to the routine. The multipliers in this generator are too large to permit a 32-bit integer implementation using the method in Figure  $2.3$ , so Figure  $2.4$  uses floating point arithmetic. L'Ecuyer  $[225]$  finds that the relative speeds of the two methods vary with the computing platform.

### Other Methods

An alternative strategy for random number generation produces a stream of bits that are concatenated to produce integers and then normalized to produce points in the unit interval. Bits can be produced by linear recursions mod 2; e.g.,

$$b_i = (a_1b_{i-1} + a_2b_{i-2} + \cdots a_kb_{i-k}) \bmod 2,$$

```
#define m1 2147483647
 \text{\#define m2 2145483479}#define a12 63308#define a13 -183326#define a21 86098
 #define a23 -539608#define q12 33921
 #define a13 11714
 #define q21 24919
 \text{#define q23 3976}#define r12 12979
 #define r13 2883
\text{#define r21 7417}#define r23 2071
 \text{#define Invmp1 4.656612873077393e-10};int x10, x11, x12, x20, x21, x22;
int
      Random()int h, p12, p13, p21, p23;
      /* Component 1 \, */
      h = x10/q13; p13 = -a13*(x10-h*q13)-h*r13;
      h = x11/q12; p12 = a12*(x11-h*q12)-h*r12;
      if(p13<0) p12 = p12+m1;
      x10 = x11; x11 = x12; x12 = p12-p13; if(x12<0) x12 = x12+m1;
      /* Component 2 \, */
      h = x20/q23; p23 = -a23*(x20-h*q23)-h*r23;
      h = x22/q21; p21 = a21*(x22-h*q21)-h*r21;
      if(p23<0) p23 = p23+m2; if(p21<0) p21 = p21+m2;
      /* Combination */if (x12-x22) return (x12-x22+m1); else return (x12-x22);
      }
double Uniform01()
     int Z;
     Z = \text{Random}(); \text{ if } (Z == 0) \text{ } Z = m1; \text{ return } (Z * \text{Invmp1});
```

Fig. 2.3. Implementation in  $C$  of a combined multiple recursive generator using integer arithmetic. The generator and the implementation are from L'Ecuyer [224].

with all  $a_i$  equal to 0 or 1. This method was proposed by Tausworthe [346]. It can be implemented through a mechanism known as a *feedback shift register*. The implementation and theoretical properties of these generators (and also of *generalized* feedback shift register methods) have been studied extensively. Matsumoto and Nishimura [258] develop a generator of this type with a period of  $2^{19937} - 1$  and apparently excellent uniformity properties. They provide C code for its implementation.

*Inversive* congruential generators use recursions of the form

$$x_{i+1} = (ax_i^- + c) \bmod m,$$

where the (mod m)-inverse  $x^-$  of x is an integer in  $\{1,\ldots,m-1\}$  (unique if it exists) satisfying  $xx^- = 1 \mod m$ . This is an example of a nonlinear congruential generator. Inversive generators are free of the lattice structure

```
double s10, s11, s12, s13, s14, s20, s21, s22, s23, s24;
#define norm 2.3283163396834613e-10
#define m1 4294949027.0#define m2 4294934327.0
#define a12 1154721.0
#define a14 1739991.0
#define a15n 1108499.0
#define a21 1776413.0\text{#define a23 865203.0}#define a25n 1641052.0double MRG32k5a ()
     {
     \text{long } k;double p1, p2;/* Component 1 \ast/
     p1 = a12 * s13 - a15n * s10;<br>if (p1 > 0.0) p1 -= a14 * m1;p1 += a14 * s11; k = p1 / m1; p1 -= k * m1;if (p1 < 0.0) p1 += m1;
     s10 = s11; s11 = s12; s12 = s13; s13 = s14; s14 = p1;
     /* Component 2 * /p2 = a21 * s24 - a25n * s20;if (p2 > 0.0) p2 -= a23 * m2;
     p2 += a23 * s22; k = p2 / m2; p2 -= k * m2;if (p2 < 0.0) p2 += m2;
     s20 = s21; s21 = s22; s22 = s23; s23 = s24; s24 = p2;
     /* Combination */if (p1 \le p2) return ((p1 - p2 + m1) * norm);else return ((p1 - p2) * norm);}
```

Fig. 2.4. Implementation in C of a combined multiple recursive generator using floating point arithmetic. The generator and implementation are from L'Ecuyer  $[225]$ .

characteristic of linear congruential generators but they are much more computationally demanding. They may be useful for comparing results in cases where the deficiencies of a random number generator are cause for concern. See Eichenauer-Herrmann, Herrmann, and Wegenkittl [110] for a survey of this approach and additional references.

## 2.2 General Sampling Methods

With an introduction to random number generation behind us, we henceforth assume the availability of an ideal sequence of random numbers. More precisely, we assume the availability of a sequence  $U_1, U_2, \ldots$  of independent random variables, each satisfying

$$P(U_i \le u) = \begin{cases} 0, \ u < 0\\ u, \ 0 \le u \le 1\\ 1, \ u > 1 \end{cases} \tag{2.12}$$

i.e., each uniformly distributed between 0 and 1. A simulation algorithm transforms these independent uniforms into sample paths of stochastic processes.

1- mar 2

Most simulations entail sampling random variables or random vectors from distributions other than the uniform. A typical simulation uses methods for transforming samples from the uniform distribution to samples from other distributions. There is a large literature on both general purpose methods and specialized algorithms for specific cases. In this section, we present two of the most widely used general techniques: the inverse transform method and the acceptance-rejection method.

### 2.2.1 Inverse Transform Method

Suppose we want to sample from a cumulative distribution function  $F$ ; i.e., we want to generate a random variable X with the property that  $P(X \leq x) =$  $F(x)$  for all x. The inverse transform method sets

$$X = F^{-1}(U), \quad U \sim \text{Unif}[0, 1], \tag{2.13}$$

where  $F^{-1}$  is the inverse of F and Unif[0,1] denotes the uniform distribution on  $[0, 1]$ .

![](_page_15_Figure_7.jpeg)

Fig. 2.5. Inverse transform method.

This transformation is illustrated in Figure  $2.5$  for a hypothetical cumulative distribution F. In the figure, values of u between 0 and  $F(0)$  are mapped to negative values of x whereas values between  $F(0)$  and 1 are mapped to positive values. The left panel of Figure 2.6 depicts a cumulative distribution function with a jump at  $x_0$ ; i.e.,

$$\lim_{x \uparrow x_0} F(x) \equiv F(x-) < F(x+) \equiv \lim_{x \downarrow x_0} F(x).$$

Under the distribution F, the outcome  $x_0$  has probability  $F(x+)-F(x-)$ . As indicated in the figure, all values of u between  $u_1 = F(x-)$  and  $u_2 = F(x+)$ are mapped to  $x_0$ .

The inverse of  $F$  is well-defined if  $F$  is strictly increasing; otherwise, we need a rule to break ties. For example, we may set

$$F^{-1}(u) = \inf\{x : F(x) \ge u\};\tag{2.14}$$

if there are many values of x for which  $F(x) = u$ , this rule chooses the smallest.

We need a rule like  $(2.14)$  in cases where the cumulative distribution F has flat sections, because the inverse of  $F$  is not well-defined at such points; see, e.g., the right panel of Figure 2.6. Observe, however, that if  $F$  is constant over an interval  $[a, b]$  and if X has distribution F, then

$$P(a < X \le b) = F(b) - F(a) = 0,$$

so flat sections of  $F$  correspond to intervals of zero probability for the random variable. If  $F$  has a continuous density, then  $F$  is strictly increasing (and its inverse is well-defined) anywhere the density is nonzero.

![](_page_16_Figure_7.jpeg)

Fig. 2.6. Inverse transform for distributions with jumps (left) or flat sections (right).

To verify that the inverse transform  $(2.13)$  generates samples from F, we check the distribution of the  $X$  it produces:

$$P(X \le x) = P(F^{-1}(U) \le x)$$
  
=  $P(U \le F(x))$   
=  $F(x)$ .

The second equality follows from the fact that, with  $F^{-1}$  as we have defined it, the events  $\{F^{-1}(u) \leq x\}$  and  $\{u \leq F(x)\}$  coincide for all u and x. The last equality follows from  $(2.12)$ .

One may interpret the input  $U$  to the inverse transform method as a random percentile. If F is continuous and  $X \sim F$ , then X is just as likely to fall between, say, the 20th and 30th percentiles of  $F$  as it is to fall between the 85th and 95th. In other words, the percentile at which X falls (namely  $F(X)$ ) is uniformly distributed. The inverse transform method chooses a percentile

level uniformly and then maps it to a corresponding value of the random variable.

We illustrate the method with examples. These examples also show that a direct implementation of the inverse transform method can sometimes be made more efficient through minor modifications.

**Example 2.2.1** *Exponential distribution.* The exponential distribution with mean  $\theta$  has distribution

$$F(x) = 1 - e^{-x/\theta}, \quad x \ge 0.$$

This is, for example, the distribution of the times between jumps of a Poisson process with rate  $1/\theta$ . Inverting the exponential distribution yields the algorithm  $X = -\theta \log(1 - U)$ . This can also be implemented as

$$X = -\theta \log(U) \tag{2.15}$$

because U and  $1-U$  have the same distribution.  $\Box$ 

**Example 2.2.2** Arcsine law. The time at which a standard Brownian motion attains its maximum over the time interval  $[0, 1]$  has distribution

$$F(x) = \frac{2}{\pi} \arcsin(\sqrt{x}), \quad 0 \le x \le 1.$$

The inverse transform method for sampling from this distribution is  $X =$  $\sin^2(U\pi/2), U \sim \text{Unif}[0,1].$  Using the identity  $2\sin^2(t) = 1 - \cos(2t)$  for  $0 \leq$  $t < \pi/2$ , we can simplify the transformation to

$$X = \frac{1}{2} - \frac{1}{2}\cos(U\pi), \quad U \sim \text{Unif}[0, 1].$$

 $\Box$ 

**Example 2.2.3** Rayleigh distribution. If we condition a standard Brownian motion starting at the origin to be at  $b$  at time 1, then its maximum over  $[0, 1]$ has the Rayleigh distribution

$$F(x) = 1 - e^{-2x(x-b)}, \quad x \ge b.$$

Solving the equation  $F(x) = u, u \in (0, 1)$ , results in a quadratic with roots

$$x = \frac{b}{2} \pm \frac{\sqrt{b^2 - 2\log(1 - u)}}{2}$$

The inverse of F is given by the larger of the two roots — in particular, we must have  $x \geq b$  since the maximum of the Brownian path must be at least as large as the terminal value. Thus, replacing  $1-U$  with U as we did in Example  $2.2.1$ , we arrive at

$$X = \frac{b}{2} + \frac{\sqrt{b^2 - 2\log(U)}}{2}$$

Even if the inverse of  $F$  is not known explicitly, the inverse transform method is still applicable through numerical evaluation of  $F^{-1}$ . Computing  $F^{-1}(u)$  is equivalent to finding a root x of the equation  $F(x) - u = 0$ . For a distribution  $F$  with density  $f$ , Newton's method for finding roots produces a sequence of iterates

$$x_{n+1} = x_n - \frac{F(x_n) - u}{f(x_n)},$$

given a starting point  $x_0$ . In the next example, root finding takes a special form.

**Example 2.2.4** Discrete distributions. In the case of a discrete distribution, evaluation of  $F^{-1}$  reduces to a table lookup. Consider, for example, a discrete random variable whose possible values are  $c_1 < \cdots < c_n$ . Let  $p_i$  be the probability attached to  $c_i$ ,  $i = 1, \ldots, n$ , and set  $q_0 = 0$ ,

$$q_i = \sum_{j=1}^i p_j, \quad i = 1, \ldots, n.$$

These are the cumulative probabilities associated with the  $c_i$ ; that is,  $q_i$  =  $F(c_i), i = 1, \ldots, n.$  To sample from this distribution,

- (i) generate a uniform  $U$ ;
- (ii) find  $K \in \{1, \ldots, n\}$  such that  $q_{K-1} < U \leq q_K$ ;

(iii) set  $X = c_K$ .

The second step can be implemented through binary search. Bratley, Fox, and Schrage [59], and Fishman [121] discuss potentially faster methods.  $\Box$ 

Our final example illustrates a general feature of the inverse transform method rather than a specific case.

**Example 2.2.5** Conditional distributions. Suppose  $X$  has distribution  $F$ and consider the problem of sampling X conditional on  $a < X \leq b$ , with  $F(a) < F(b)$ . Using the inverse transform method, this is no more difficult than generating X unconditionally. If  $U \sim \text{Unif}[0,1]$ , then the random variable  $V$  defined by

$$V = F(a) + [F(b) - F(a)]U$$

is uniformly distributed between  $F(a)$  and  $F(b)$ , and  $F^{-1}(V)$  has the desired conditional distribution. To see this, observe that

$$P(F^{-1}(V) \le x) = P(F(a) + [F(b) - F(a)]U \le F(x))$$
  
=  $P(U \le [F(x) - F(a)]/[F(b) - F(a)])$   
=  $[F(x) - F(a)]/[F(b) - F(a)],$ 

and this is precisely the distribution of X given  $a < X \leq b$ . Either of the endpoints  $a, b$  could be infinite in this example.  $\Box$ 

The inverse transform method is seldom the fastest method for sampling from a distribution, but it has important features that make it attractive nevertheless. One is its use in sampling from conditional distributions just illustrated; we point out two others. First, the inverse transform method maps the input U monotonically and — if F is strictly increasing — continuously to the output  $X$ . This can be useful in the implementation of variance reduction techniques and in sensitivity estimation, as we will see in Chapters 4 and 7. Second, the inverse transform method requires just one uniform random variable for each sample generated. This is particularly important in using quasi-Monte Carlo methods where the *dimension* of a problem is often equal to the number of uniforms needed to generate one "path." Methods that require multiple uniforms per variable generated result in higher-dimensional representations for which quasi-Monte Carlo may be much less effective.

#### 2.2.2 Acceptance-Rejection Method

The acceptance-rejection method, introduced by Von Neumann [353], is among the most widely applicable mechanisms for generating random samples. This method generates samples from a target distribution by first generating candidates from a more convenient distribution and then rejecting a random subset of the generated candidates. The rejection mechanism is designed so that the accepted samples are indeed distributed according to the target distribution. The technique is by no means restricted to univariate distributions.

Suppose, then, that we wish to generate samples from a density  $f$  defined on some set  $\mathcal{X}$ . This could be a subset of the real line, of  $\mathbb{R}^d$ , or a more general set. Let g be a density on  $\mathcal{X}$  from which we know how to generate samples and with the property that

$$f(x) \le cg(x)$$
, for all  $x \in \mathcal{X}$ 

for some constant  $c$ . In the acceptance-rejection method, we generate a sample X from g and accept the sample with probability  $f(X)/cg(X)$ ; this can be implemented by sampling U uniformly over  $(0,1)$  and accepting X if  $U \leq$  $f(X)/\text{ca}(X)$ . If X is rejected, a new candidate is sampled from q and the acceptance test applied again. The process repeats until the acceptance test is passed; the accepted value is returned as a sample from  $f$ . Figure 2.7 illustrates a generic implementation.

To verify the validity of the acceptance-rejection method, let  $Y$  be a sample returned by the algorithm and observe that  $Y$  has the distribution of  $X$ conditional on  $U \leq f(X)/cg(X)$ . Thus, for any  $A \subseteq \mathcal{X}$ ,

$$P(Y \in A) = P(X \in A | U \le f(X) / cg(X))$$
  
= 
$$\frac{P(X \in A, U \le f(X) / cg(X))}{P(U \le f(X) / cg(X))}.$$
 (2.16)

Given X, the probability that  $U \leq f(X)/cg(X)$  is simply  $f(X)/cg(X)$  because U is uniform; hence, the denominator in  $(2.16)$  is given by

1. generate  $X$  from distribution  $g$ 2. generate  $U$  from Unif[0,1] 3. if  $U \le f(X)/cg(X)$  $\text{return } X$ otherwise go to Step 1.

Fig. 2.7. The acceptance-rejection method for sampling from density  $f$  using candidates from density  $q$ .

$$P(U \le f(X)/cg(X)) = \int_{\mathcal{X}} \frac{f(x)}{cg(x)}g(x) \, dx = 1/c \tag{2.17}$$

(taking  $0/0 = 1$  if  $g(x) = 0$  somewhere on  $\mathcal{X}$ ). Making this substitution in  $(2.16)$ , we find that

$$P(Y \in A) = cP(X \in A, U \le f(X)/cg(X)) = c \int_A \frac{f(x)}{cg(x)}g(x) \, dx = \int_A f(x) \, dx.$$

Since A is arbitrary, this verifies that Y has density  $f$ .

In fact, this argument shows more: Equation  $(2.17)$  shows that the probability of acceptance on each attempt is  $1/c$ . Because the attempts are mutually independent, the number of candidates generated until one is accepted is geometrically distributed with mean  $c$ . It is therefore preferable to have  $c$  close to 1 (it can never be less than 1 if  $f$  and  $g$  both integrate to 1). Tighter bounds on the target density  $f$  result in fewer wasted samples from  $g$ . Of course, a prerequisite for the method is the ability to sample from  $q$ ; the speed of the method depends on both  $c$  and the effort involved in sampling from  $q$ .

We illustrate the method with examples.

**Example 2.2.6** Beta distribution. The beta density on  $[0, 1]$  with parameters  $\alpha_1, \alpha_2 > 0$  is given by

$$f(x) = \frac{1}{B(\alpha_1, \alpha_2)} x^{\alpha_1 - 1} (1 - x)^{\alpha_2 - 1}, \quad 0 \le x \le 1,$$

with

$$B(\alpha_1, \alpha_2) = \int_0^1 x^{\alpha_1 - 1} (1 - x)^{\alpha_2 - 1} dx = \frac{\Gamma(\alpha_1) \Gamma(\alpha_2)}{\Gamma(\alpha_1 + \alpha_2)}$$

and  $\Gamma$  the gamma function. Varying the parameters  $\alpha_1, \alpha_2$  results in a variety of shapes, making this a versatile family of distributions with bounded support. Among many other applications, beta distributions are used to model the random recovery rate (somewhere between 0 and  $100\%$ ) upon default of a bond subject to credit risk. The case  $\alpha_1 = \alpha_2 = 1/2$  is the arcsine distribution considered in Example  $2.2.2$ .

If  $\alpha_1, \alpha_2 \geq 1$  and at least one of the parameters exceeds 1, the beta density is unimodal and achieves its maximum at  $(\alpha_1 - 1)/(\alpha_1 + \alpha_2 - 2)$ . Let c be the value of the density f at this point. Then  $f(x) \leq c$  for all x, so we may choose g to be the uniform density  $(g(x) = 1, 0 \le x \le 1)$ , which is in fact the beta density with parameters  $\alpha_1 = \alpha_2 = 1$ . In this case, the acceptance-rejection method becomes

Generate  $U_1, U_2$  from Unif[0,1] until  $cU_2 \leq f(U_1)$ Return  $U_1$ 

This is illustrated in Figure 2.8 for parameters  $\alpha_1 = 3$ ,  $\alpha_2 = 2$ .

As is clear from Figure 2.8, generating candidates from the uniform distribution results in many rejected samples and thus many evaluations of  $f$ . (The expected number of candidates generated for each accepted sample is  $c \approx 1.778$  for the density in the figure.) Faster methods for sampling from beta distributions — combining more carefully designed acceptance-rejection schemes with the inverse transform and other methods — are detailed in Devroye [95], Fishman [121], Gentle [136], and Johnson, Kotz, and Balakrishnan [202].  $\Box$ 

![](_page_21_Figure_5.jpeg)

Fig. 2.8. Illustration of the acceptance-rejection method using uniformly distributed candidates.

**Example 2.2.7** Normal from double exponential. Fishman [121, p.173] illustrates the use of the acceptance-rejection method by generating half-normal samples from the exponential distribution. (A half-normal random variable has the distribution of the absolute value of a normal random variable.) Fishman also notes that the method can be used to generate normal random variables and we present the example in this form. Because of its importance

in financial applications, we devote all of Section 2.3 to the normal distribution; we include this example here primarily to further illustrate acceptancerejection.

The double exponential density on  $(-\infty,\infty)$  is  $q(x) = \exp(-|x|)/2$  and the normal density is  $f(x) = \exp(-x^2/2)/\sqrt{2\pi}$ . The ratio is

$$\frac{f(x)}{g(x)} = \sqrt{\frac{2}{\pi}} e^{-\frac{1}{2}x^2 + |x|} \le \sqrt{\frac{2e}{\pi}} \approx 1.3155 \equiv c.$$

Thus, the normal density is dominated by the scaled double exponential density  $cq(x)$ , as illustrated in Figure 2.9. A sample from the double exponential density can be generated using  $(2.15)$  to draw a standard exponential random variable and then randomizing the sign. The rejection test  $u > f(x)/cg(x)$ can be implemented as

$$u > \exp(-\frac{1}{2}x^2 + |x| - \frac{1}{2}) = \exp(-\frac{1}{2}(|x| - 1)^2)$$

In light of the symmetry of both  $f$  and  $q$ , it suffices to generate positive samples and determine the sign only if the sample is accepted; in this case, the absolute value is unnecessary in the rejection test. The combined steps are as follows:

1. generate 
$$U_1, U_2, U_3$$
 from  $\text{Unif}[0,1]$   
2.  $X \leftarrow -\log(U_1)$   
3. if  $U_2 > \exp(-0.5(X-1)^2)$   
go to Step 1  
4. if  $U_3 \leq 0.5$   
 $X \leftarrow -X$   
5. return  $X$ 

**Example 2.2.8** Conditional distributions. Consider the problem of generating a random variable or vector X conditional on  $X \in A$ , for some set A. In the scalar case, this can be accomplished using the inverse transform method if  $A$  is an interval; see Example 2.2.5. In more general settings it may be difficult to sample directly from the conditional distribution. However, so long as it is possible to generate unconditional samples, one may always resort to the following crude procedure:

Generate X until  $X \in A$  $\text{return } X$ 

This may be viewed as a degenerate form of acceptance-rejection. Let  $f$ denote the conditional density and let  $g$  denote the unconditional density; then

$$f(x)/g(x) = \begin{cases} 1/P(X \in A), & x \in A \\ 0, & x \notin A. \end{cases}$$

![](_page_23_Figure_1.jpeg)

Fig. 2.9. Normal density and scaled double exponential.

Thus,  $c = 1/P(X \in A)$  is an upper bound on the ratio. Moreover, since the ratio  $f(x)/cq(x)$  is either 0 or 1 at every x, it is unnecessary to randomize the rejection decision: a candidate X is accepted precisely if  $X \in A$ .  $\Box$ 

Acceptance-rejection can often be accelerated through the *squeeze* method, in which simpler tests are applied before the exact acceptance threshold  $f(x)/c q(x)$  is evaluated. The simpler tests are based on functions that bound  $f(x)/c q(x)$  from above and below. The effectiveness of this method depends on the quality of the bounding functions and the speed with which they can be evaluated. See Fishman  $[121]$  for a detailed discussion.

Although we have restricted attention to sampling from densities, it should be clear that the acceptance-rejection method also applies when  $f$  and  $g$  are replaced with the mass functions of discrete distributions.

The best methods for sampling from a specific distribution invariably rely on special features of the distribution. Acceptance-rejection is frequently combined with other techniques to exploit special features — it is perhaps more a principle than a method.

At the end of Section  $2.2.1$  we noted that one attractive feature of the inverse transform method is that it uses exactly one uniform random variable per nonuniform random variable generated. When simulation problems are formulated as numerical integration problems, the dimension of the integrand is typically the maximum number of uniform variables needed to generate a simulation "path." The effectiveness of quasi-Monte Carlo and related integration methods generally deteriorates as the dimension increases, so in using those methods, we prefer representations that keep the dimension as small as possible. With an acceptance-rejection method, there is ordinarily no upper bound on the number of uniforms required to generate even a single nonuniform variable; simulations that use acceptance-rejection therefore correspond to infinite-dimensional integration problems. For this

63

reason, acceptance-rejection methods are generally inapplicable with quasi-Monte Carlo methods. A further potential drawback of acceptance-rejection methods, compared with the inverse transform method, is that their outputs are generally neither continuous nor monotone functions of the input uniforms. This can diminish the effectiveness of the antithetic variates method. for example.

# 2.3 Normal Random Variables and Vectors

Normal random variables are the building blocks of many financial simulation models, so we discuss methods for sampling from normal distributions in detail. We begin with a brief review of basic properties of normal distributions.

### 2.3.1 Basic Properties

The standard univariate normal distribution has density

$$\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}, \quad -\infty < x < \infty \tag{2.18}$$

and cumulative distribution function

$$\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-u^2/2} du. \tag{2.19}$$

 $Standard$  indicates mean 0 and variance 1. More generally, the normal distribution with mean  $\mu$  and variance  $\sigma^2$ ,  $\sigma > 0$ , has density

$$\phi_{\mu,\sigma}(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

and cumulative distribution

$$\Phi_{\mu,\sigma}(x) = \Phi\left(\frac{x-\mu}{\sigma}\right).$$

The notation  $X \sim N(\mu, \sigma^2)$  abbreviates the statement that the random variable X is normally distributed with mean  $\mu$  and  $\sigma^2$ .

If  $Z \sim N(0,1)$  (i.e., Z has the standard normal distribution), then

$$\mu + \sigma Z \sim N(\mu, \sigma^2).$$

Thus, given a method for generating samples  $Z_1, Z_2, \ldots$  from the standard normal distribution, we can generate samples  $X_1, X_2, \ldots$  from  $N(\mu, \sigma^2)$  by setting  $X_i = \mu + \sigma Z_i$ . It therefore suffices to consider methods for sampling from  $N(0,1)$ .

A d-dimensional normal distribution is characterized by a d-vector  $\mu$  and a  $d \times d$  covariance matrix  $\Sigma$ ; we abbreviate it as  $N(\mu, \Sigma)$ . To qualify as a covariance matrix,  $\Sigma$  must be symmetric (i.e.,  $\Sigma$  and its transpose  $\Sigma^{\top}$  are equal) and positive semidefinite, meaning that

$$x^{\top} \Sigma x \ge 0 \tag{2.20}$$

for all  $x \in \Re^d$ . This is equivalent to the requirement that all eigenvalues of  $\Sigma$  be nonnegative. (As a symmetric matrix,  $\Sigma$  automatically has real eigenvalues.) If  $\Sigma$  is positive definite (meaning that strict inequality holds in (2.20) for all nonzero  $x \in \Re^d$  or, equivalently, that all eigenvalues of  $\Sigma$  are positive), then the normal distribution  $N(\mu, \Sigma)$  has density

$$\phi_{\mu,\Sigma}(x) = \frac{1}{(2\pi)^{d/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^\top \Sigma^{-1}(x-\mu)\right), \quad x \in \Re^d, \quad (2.21)$$

with  $|\Sigma|$  the determinant of  $\Sigma$ . The *standard* d-dimensional normal  $N(0, I_d)$ , with  $I_d$  the  $d \times d$  identity matrix, is the special case

$$\frac{1}{(2\pi)^{d/2}}\exp\left(-\frac{1}{2}x^\top x\right)$$
 .

If  $X \sim N(\mu, \Sigma)$  (i.e., the random vector X has a multivariate normal distribution), then its *i*th component  $X_i$  has distribution  $N(\mu_i, \sigma_i^2)$ , with  $\sigma_i^2 =$  $\Sigma_{ii}$ . The *i*th and *j*th components have covariance

$$\mathsf{Cov}[X_i, X_j] = \mathsf{E}[(X_i - \mu_i)(X_j - \mu_j)] = \Sigma_{ij},$$

which justifies calling  $\Sigma$  the covariance matrix. The correlation between  $X_i$ and  $X_j$  is given by

$$\rho_{ij} = \frac{\Sigma_{ij}}{\sigma_i \sigma_j}.$$

In specifying a multivariate distribution, it is sometimes convenient to use this definition in the opposite direction: specify the marginal standard deviations  $\sigma_i, i = 1, \ldots, d$ , and the correlations  $\rho_{ij}$  from which the covariance matrix

$$\Sigma_{ij} = \sigma_i \sigma_j \rho_{ij} \tag{2.22}$$

is then determined.

If the  $d \times d$  symmetric matrix  $\Sigma$  is positive semidefinite but not positive definite then the rank of  $\Sigma$  is less than d,  $\Sigma$  fails to be invertible, and there is no normal density with covariance matrix  $\Sigma$ . In this case, we can define the normal distribution  $N(\mu,\Sigma)$  as the distribution of  $X = \mu + AZ$  with  $Z \sim N(0, I_d)$  for any  $d \times d$  matrix A satisfying  $AA^{\top} = \Sigma$ . The resulting distribution is independent of which such  $A$  is chosen. The random vector X does not have a density in  $\Re^d$ , but if  $\Sigma$  has rank k then one can find k components of X with a multivariate normal density in  $\mathbb{R}^k$ .

Three further properties of the multivariate normal distribution merit special mention:

**Linear Transformation Property:** Any linear transformation of a normal  $\text{vector is again normal:}$ 

$$X \sim N(\mu, \Sigma) \Rightarrow AX \sim N(A\mu, A\Sigma A^{\top}), \tag{2.23}$$

for any d-vector  $\mu$ , and  $d \times d$  matrix  $\Sigma$ , and any  $k \times d$  matrix A, for any k.

**Conditioning Formula:** Suppose the partitioned vector  $(X_{[1]}, X_{[2]})$  (where each  $X_{[i]}$  may itself be a vector) is multivariate normal with

$$\begin{pmatrix} X_{[1]} \\ X_{[2]} \end{pmatrix} \sim N\left( \begin{pmatrix} \mu_{[1]} \\ \mu_{[2]} \end{pmatrix}, \begin{pmatrix} \Sigma_{[11]} & \Sigma_{[12]} \\ \Sigma_{[21]} & \Sigma_{[22]} \end{pmatrix} \right), \n$$
(2.24)

and suppose  $\Sigma_{[22]}$  has full rank. Then

$$(X_{[1]}|X_{[2]}=x) \sim N(\mu_{[1]} + \Sigma_{[12]}\Sigma_{[22]}^{-1}(x-\mu_{[2]}), \Sigma_{[11]} - \Sigma_{[12]}\Sigma_{[22]}^{-1}\Sigma_{[21]}). \tag{2.25}$$

In (2.24), the dimensions of the  $\mu_{[i]}$  and  $\Sigma_{[ij]}$  are consistent with those of the  $X_{[i]}$ . Equation (2.25) then gives the distribution of  $X_{[1]}$  conditional on  $X_{[2]} = x.$ 

Moment Generating Function: If  $X \sim N(\mu, \Sigma)$  with X d-dimensional, then

$$\mathsf{E}[\exp(\theta^{\top}X)] = \exp\left(\mu^{\top}\theta + \frac{1}{2}\theta^{\top}\Sigma\theta\right) \tag{2.26}$$

for all  $\theta \in \mathbb{R}^d$ .

### 2.3.2 Generating Univariate Normals

We now discuss algorithms for generating samples from univariate normal distributions. As noted in the previous section, it suffices to consider sampling from  $N(0,1)$ . We assume the availability of a sequence  $U_1, U_2, \ldots$  of independent random variables uniformly distributed on the unit interval  $[0, 1]$ and consider methods for transforming these uniform random variables to normally distributed random variables.

### Box-Muller Method

Perhaps the simplest method to implement (though not the fastest or necessarily the most convenient) is the Box-Muller [51] algorithm. This algorithm generates a sample from the bivariate standard normal, each component of which is thus a univariate standard normal. The algorithm is based on the following two properties of the bivariate normal: if  $Z \sim N(0, I_2)$ , then

- 66 2 Generating Random Numbers and Random Variables
- (i)  $R = Z_1^2 + Z_2^2$  is exponentially distributed with mean 2, i.e.,

$$P(R \le x) = 1 - e^{-x/2};$$

(ii) given R, the point  $(Z_1, Z_2)$  is uniformly distributed on the circle of radius  $\sqrt{R}$  centered at the origin.

Thus, to generate  $(Z_1, Z_2)$ , we may first generate R and then choose a point uniformly from the circle of radius  $\sqrt{R}$ . To sample from the exponential distribution we may set  $R = -2\log(U_1)$ , with  $U_1 \sim \text{Unif}[0,1]$ , as in (2.15). To generate a random point on a circle, we may generate a random angle uniformly between 0 and  $2\pi$  and then map the angle to a point on the circle. The random angle may be generated as  $V = 2\pi U_2$ ,  $U_2 \sim \text{Unif}[0,1]$ ; the corresponding point on the circle has coordinates  $(\sqrt{R}\cos(V), \sqrt{R}\sin(V))$ . The complete algorithm is given in Figure 2.10.

generate 
$$U_1, U_2$$
 independent Unif[0,1]  
 $R \leftarrow -2\log(U_1)$   
 $V \leftarrow 2\pi U_2$   
 $Z_1 \leftarrow \sqrt{R}\cos(V), Z_2 \leftarrow \sqrt{R}\sin(V)$   
return  $Z_1, Z_2$ .

**Fig. 2.10.** Box-Muller algorithm for generating normal random variables.

Marsaglia and Bray [250] developed a modification of the Box-Muller method that reduces computing time by avoiding evaluation of the sine and cosine functions. The Marsaglia-Bray method instead uses acceptance-rejection to sample points uniformly in the unit disc and then transforms these points to normal variables.

The algorithm is illustrated in Figure 2.11. The transformation  $U_i \leftarrow 2U_i -$ 1,  $i = 1, 2$ , makes  $(U_1, U_2)$  uniformly distributed over the square  $[-1, 1] \times$  $[-1,1]$ . Accepting only those pairs for which  $X = U_1^2 + U_2^2$  is less than or equal to 1 produces points uniformly distributed over the disc of radius 1 centered at the origin. Conditional on acceptance,  $X$  is uniformly distributed between 0 and 1, so the  $\log X$  in Figure 2.11 has the same effect as the  $\log U_1$ in Figure 2.10. Dividing each accepted  $(U_1, U_2)$  by  $\sqrt{X}$  projects it from the unit disc to the unit circle, on which it is uniformly distributed. Moreover,  $(U_1/\sqrt{X}, U_2/\sqrt{X})$  is independent of X conditional on  $X \leq 1$ . Hence, the justification for the last step in Figure 2.11 is the same as that for the Box-Muller method.

As is the case with most acceptance-rejection methods, there is no upper bound on the number of uniforms the Marsaglia-Bray algorithm may use to generate a single normal variable (or pair of variables). This renders the method inapplicable with quasi-Monte Carlo simulation.

while  $(X > 1)$ generate  $U_1, U_2 \sim \text{Unif}[0,1]$  $U_1 \leftarrow 2 * U_1 - 1, \quad U_2 \leftarrow 2 * U_2 - 1$  $X \leftarrow U_1^2 + U_2^2$  $\text{end}$  $Y \leftarrow \sqrt{-2\log X/X}$  $Z_1 \leftarrow U_1 Y, \quad Z_2 \leftarrow U_2 Y$ return  $Z_1, Z_2$ .

Fig. 2.11. Marsaglia-Bray algorithm for generating normal random variables.

### Approximating the Inverse Normal

Applying the inverse transform method to the normal distribution entails evaluation of  $\Phi^{-1}$ . At first sight, this may seem infeasible. However, there is really no reason to consider  $\Phi^{-1}$  any less tractable than, e.g., a logarithm. Neither can be computed exactly in general, but both can be approximated with sufficient accuracy for applications. We discuss some specific methods for evaluating  $\Phi^{-1}$ .

Because of the symmetry of the normal distribution,

$$\Phi^{-1}(1-u) = -\Phi^{-1}(u), \quad 0 < u < 1;$$

it therefore suffices to approximate  $\Phi^{-1}$  on the interval [0.5, 1] (or the interval  $(0, 0.5]$ ) and then to use the symmetry property to extend the approximation to the rest of the unit interval. Beasley and Springer  $[43]$  provide a rational approximation

$$\Phi^{-1}(u) \approx \frac{\sum_{n=0}^{3} a_n (u - \frac{1}{2})^{2n+1}}{1 + \sum_{n=0}^{3} b_n (u - \frac{1}{2})^{2n}},$$
(2.27)

for  $0.5 \le u \le 0.92$ , with constants  $a_n, b_n$  given in Figure 2.12; for  $u > 0.92$  they use a rational function of  $\sqrt{\log(1-u)}$ . Moro [271] reports greater accuracy in the tails by replacing the second part of the Beasley-Springer approximation with a  $Chebyshev$  approximation

$$\Phi^{-1}(u) \approx g(u) = \sum_{n=0}^{8} c_n [\log(-\log(1-u))]^n, \quad 0.92 \le u < 1, \tag{2.28}$$

with constants  $c_n$  again given in Figure 2.12. Using the symmetry rule, this gives

$$\Phi^{-1}(u) \approx -g(1-u) \quad 0 < u \le .08.$$

With this modification, Moro [271] finds a maximum absolute error of  $3 \times 10^{-9}$ out to seven standard deviations (i.e., over the range  $\Phi(-7) \leq u \leq \Phi(7)$ ). The combined algorithm from Moro  $[271]$  is given in Figure 2.13.

| $a_0 =$ |  | 2.50662823884              | $b_0 =$ | $-8.47351093090$           |
|---------|--|----------------------------|---------|----------------------------|
| $a_1 =$ |  | $-18.61500062529$          | $b_1 =$ | 23.08336743743             |
| $a_2 =$ |  | 41.39119773534             | $b_2 =$ | $-21.06224101826$          |
| $a_3 =$ |  | $-25.44106049637$          | $b_3 =$ | 3.13082909833              |
|         |  |                            |         |                            |
|         |  | $c_0 = 0.3374754822726147$ |         | $c_5 = 0.0003951896511919$ |
|         |  | $c_1 = 0.9761690190917186$ |         | $c_6 = 0.0000321767881768$ |
|         |  | $c_2 = 0.1607979714918209$ |         | $c_7 = 0.0000002888167364$ |
|         |  | $c_3 = 0.0276438810333863$ |         | $c_8 = 0.0000003960315187$ |
|         |  | $c_4 = 0.0038405729373609$ |         |                            |

Fig. 2.12. Constants for approximations to inverse normal.

```
Input: u between 0 and 1
Output: x, approximation to \Phi^{-1}(u).
y \leftarrow u - 0.5if |y| < 0.42r \leftarrow y * yx \leftarrow y * (((a_3 * r + a_2) * r + a_1) * r + a_0) /((((b_3 * r + b_2) * r + b_1) * r + b_0) * r + 1)else
    r \leftarrow u;if (y>0) r \leftarrow 1-ur \leftarrow \log(-\log(r))x \leftarrow c_0 + r * (c_1 + r * (c_2 + r * (c_3 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r * (c_4 + r *r*(c_5+r*(c_6+r*(c_7+r*c_8)))))))if (y < 0) x \leftarrow -xreturn x
```

Fig. 2.13. Beasley-Springer-Moro algorithm for approximating the inverse normal.

The problem of computing  $\Phi^{-1}(u)$  can be posed as one of finding the root x of the equation  $\Phi(x) = u$  and in principle addressed through any general root-finding algorithm. Newton's method, for example, produces the iterates

$$x_{n+1} = x_n - \frac{\Phi(x_n) - u}{\phi(x_n)},$$

or, more explicitly,

$$x_{n+1} = x_n + (u - \Phi(x_n)) \exp(-0.5x_n \cdot x_n + c), \quad c \equiv \log(\sqrt{2\pi}).$$

Marsaglia, Zaman, and Marsaglia [251] recommend the starting point

$$x_0 = \pm \sqrt{|-1.6\log(1.0004 - (1-2u)^2)|},$$

the sign depending on whether  $u \geq 0$  or  $u < 0$ . This starting point gives a surprisingly good approximation to  $\Phi^{-1}(u)$ . A root-finding procedure is useful when extreme precision is more important than speed — for example, in

tabulating "exact" values or evaluating approximations. Also, a small number of Newton steps can be appended to an approximation like the one in Figure 2.13 to further improve accuracy. Adding just a single step to Moro's [271] algorithm appears to reduce the maximum error to the order of  $10^{-15}$ .

### Approximating the Cumulative Normal

Of course, the application of Newton's method presupposes the ability to evaluate  $\Phi$  itself quickly and accurately. Evaluation of the cumulative normal is necessary for many financial applications (including evaluation of the Black-Scholes formula), so we include methods for approximating this function. We present two methods; the first is faster and the second is more accurate, but both are probably fast enough and accurate enough for most applications.

The first method, based on work of Hastings [171], is one of several included in Abramowitz and Stegun [3]. For  $x \geq 0$ , it takes the form

$$\Phi(x) \approx 1 - \phi(x)(b_1t + b_2t^2 + b_3t^3 + b_4t^4 + b_5t^5), \quad t = \frac{1}{1 + px},$$

for constants  $b_i$  and  $p$ . The approximation extends to negative arguments through the identity  $\Phi(-x) = 1 - \Phi(x)$ . The necessary constants and an explicit algorithm for this approximation are given in Figure  $2.14$ . According to Hastings [171, p.169], this method has a maximum absolute error less than  $7.5 \times 10^{-8}$ .

> $p = 0.2316419$  $b_1 = 0.319381530$  $c = \log(\sqrt{2\pi}) = 0.918938533204672$  $b_2 = -0.356563782$  $b_3 = 1.781477937$  $b_4 = -1.821255978$  $b_5 = 1.330274429$ Input:  $x$ Output: y, approximation to  $\Phi(x)$  $a \leftarrow |x|$  $t \leftarrow 1/(1 + a * p)$  $s \leftarrow (((b_5 * t + b_4) * t + b_3) * t + b_2) * t + b_1) * t$  $y \leftarrow s * \exp(-0.5 * x * x - c)$ if  $(x > 0)$   $y \leftarrow 1 - y$ return  $y$ ;

Fig. 2.14. Hastings' [171] approximation to the cumulative normal distribution as modified in Abramowitz and Stegun [3].

The second method we include is from Marsaglia et al.  $[251]$ . Like the Hastings approximation above, this method is based on approximating the

ratio  $(1-\Phi(x))/\phi(x)$ . According to Marsaglia et al. [251], as an approximation to the tail probability  $1 - \Phi(x)$  this method has a maximum relative error of  $10^{-15}$  for  $0 < x < 6.23025$  and  $10^{-12}$  for larger x. (Relative error is much more stringent than absolute error in this setting; a small absolute error is easily achieved for large x using the approximation  $1-\Phi(x) \approx 0$ .) This method takes about three times as long as the Hastings approximation, but both methods are very fast. The complete algorithm appears in Figure 2.15.

```
v_1 = 1.253314137315500v_9 = 0.1231319632579329v_2 = 0.6556795424187985v_{10} = 0.1097872825783083v_3 = 0.4213692292880545v_{11} = 0.09902859647173193v_4 = 0.3045902987101033v_{12} = 0.09017567550106468v_5 = 0.2366523829135607v_{13} = 0.08276628650136917v_6 = 0.1928081047153158v_{14} = 0.0764757610162485v_7 = 0.1623776608968675v_{15} = 0.07106958053885211v_8 = 0.1401041834530502c = \log(\sqrt{2\pi}) = 0.918938533204672Input: x between -15 and 15
Output: y, approximation to \Phi(x).
j \leftarrow \left| \min(|x| + 0.5, 14) \right|z \leftarrow j, \quad h \leftarrow |x| - z, \quad a \leftarrow v_{j+1}b \leftarrow z * a - 1, \quad q \leftarrow 1, \quad s \leftarrow a + h * bfor i = 2, 4, 6, \ldots, 24 - ja \leftarrow (a + z * b)/ib \leftarrow (b + z * a)/(i + 1)q \leftarrow q * h * hs \leftarrow s + q * (a + h * b)\text{end}y = s \times \exp(-0.5 \times x \times x - c)if (x>0) y \leftarrow 1-y\text{return } y
```

Fig. 2.15. Algorithm of Marsaglia et al. [251] to approximate the cumulative normal distribution.

Marsaglia et al. [251] present a faster approximation achieving similar accuracy but requiring 121 tabulated constants. Marsaglia et al. also detail the use of accurate approximations to  $\Phi$  in constructing approximations to  $\Phi^{-1}$  by tabulating "exact" values at a large number of strategically chosen points. Their method entails the use of more than 2000 tabulated constants, but the constants can be computed rather than tabulated, given an accurate approximation to  $\Phi$ .

Other methods for approximating  $\Phi$  and  $\Phi^{-1}$  found in the literature are often based on the error function

2.3 Normal Random Variables and Vectors

$$\operatorname{Erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$$

and its inverse. Observe that for  $x > 0$ ,

$$\text{Erf}(x) = 2\Phi(x\sqrt{2}) - 1, \quad \Phi(x) = \frac{1}{2}[\text{Erf}(x/\sqrt{2}) + 1]$$

and

$$\operatorname{Erf}^{-1}(u) = \frac{1}{\sqrt{2}} \Phi^{-1}(\frac{u+1}{2}), \quad \Phi^{-1}(u) = \sqrt{2} \operatorname{Erf}^{-1}(2u-1),$$

so approximations to Erf and its inverse are easily converted into approximations to  $\Phi$  and its inverse. Hastings [171], in fact, approximates Erf, so the constants in Figure 2.14 (as modified in [3]) differ from his, with  $p$  smaller and the  $b_i$  larger by a factor of  $\sqrt{2}$ .

Devroye [95] discusses several other methods for sampling from the normal distribution, including some that may be substantially faster than evaluation of  $\Phi^{-1}$ . Nevertheless, as discussed in Section 2.2.1, the inverse transform method has some advantages — particularly in the application of variance reduction techniques and low-discrepancy methods — that will often justify the additional computational effort. One advantage is that the inverse transform method requires just one uniform input per normal output: a relevant notion of the *dimension* of a Monte Carlo problem is often the maximum number of uniforms required to generate one sample path, so methods requiring more uniforms per normal sample implicitly result in higher dimensional representations. Another useful property of the inverse transform method is that the mapping  $u \mapsto \Phi^{-1}(u)$  is both continuous and monotone. These properties can sometimes enhance the effectiveness of variance reduction techniques, as we will see in later sections.

### 2.3.3 Generating Multivariate Normals

A multivariate normal distribution  $N(\mu, \Sigma)$  is specified by its mean vector  $\mu$ and covariance matrix  $\Sigma$ . The covariance matrix may be specified implicitly through its diagonal entries  $\sigma_i^2$  and correlations  $\rho_{ij}$  using (2.22); in matrix form.

$$\Sigma = \begin{pmatrix} \sigma_1 & & \\ & \sigma_2 & \\ & & \ddots & \\ & & & \sigma_d \end{pmatrix} \begin{pmatrix} \rho_{11} \ \rho_{12} \ \cdots \ \rho_{1d} \\ \rho_{12} \ \rho_{22} & \ \rho_{2d} \\ \vdots & \ddots & \vdots \\ \rho_{1d} \ \rho_{2d} \ \cdots \ \rho_{dd} \end{pmatrix} \begin{pmatrix} \sigma_1 & & \\ & \sigma_2 & \\ & & \ddots & \\ & & & \sigma_d \end{pmatrix}$$

From the Linear Transformation Property (2.23), we know that if  $Z \sim$  $N(0,I)$  and  $X = \mu + AZ$ , then  $X \sim N(\mu, AA^{\top})$ . Using any of the methods discussed in Section  $2.3.2$ , we can generate independent standard normal random variables  $Z_1, \ldots, Z_d$  and assemble them into a vector  $Z \sim N(0, I)$ . Thus, the problem of sampling X from the multivariate normal  $N(\mu, \Sigma)$  reduces to finding a matrix A for which  $AA^{\top} = \Sigma$ .

71

#### Cholesky Factorization

Among all such  $A$ , a lower triangular one is particularly convenient because it reduces the calculation of  $\mu + AZ$  to the following:

$$X_1 = \mu_1 + A_{11}Z_1$$
  

$$X_2 = \mu_2 + A_{21}Z_1 + A_{22}Z_2$$
  

$$\vdots$$
  

$$X_d = \mu_d + A_{d1}Z_1 + A_{d2}Z_2 + \dots + A_{dd}Z_d$$

A full multiplication of the vector  $Z$  by the matrix  $A$  would require approximately twice as many multiplications and additions. A representation of  $\Sigma$ as  $AA^{\top}$  with A lower triangular is a *Cholesky factorization* of  $\Sigma$ . If  $\Sigma$  is positive definite (as opposed to merely positive semidefinite), it has a Cholesky factorization and the matrix  $A$  is unique up to changes in sign.

Consider a  $2 \times 2$  covariance matrix  $\Sigma$ , represented as

$$\Sigma = \begin{pmatrix} \sigma_1^2 & \sigma_1 \sigma_2 \rho \\ \sigma_1 \sigma_2 \rho & \sigma_2^2 \end{pmatrix}.$$

Assuming  $\sigma_1 > 0$  and  $\sigma_2 > 0$ , the Cholesky factor is

$$A = \begin{pmatrix} \sigma_1 & 0 \\ \rho \sigma_2 & \sqrt{1 - \rho^2} \sigma_2 \end{pmatrix},$$

as is easily verified by evaluating  $AA^{\top}$ . Thus, we can sample from a bivariate normal distribution  $N(\mu, \Sigma)$  by setting

$$X_1 = \mu_1 + \sigma_1 Z_1$$
  
$$X_2 = \mu_2 + \sigma_2 \rho Z_1 + \sigma_2 \sqrt{1 - \rho^2} Z_2,$$

with  $Z_1, Z_2$  independent standard normals.

For the case of a  $d \times d$  covariance matrix  $\Sigma$ , we need to solve

$$\begin{pmatrix} A_{11} \\ A_{21} & A_{22} \\ \vdots & \vdots & \ddots \\ A_{d1} & A_{d2} & \cdots & A_{dd} \end{pmatrix} \begin{pmatrix} A_{11} & A_{21} & \cdots & A_{d1} \\ & A_{22} & \cdots & A_{d2} \\ & & \ddots & \vdots \\ & & & A_{dd} \end{pmatrix} = \Sigma.$$

Traversing the  $\Sigma_{ij}$  by looping over  $j = 1, \ldots, d$  and then  $i = j, \ldots, d$  produces the equations

$$A_{11}^2 = \Sigma_{11}$$
  
$$A_{21}A_{11} = \Sigma_{21}$$
  
:

2.3 Normal Random Variables and Vectors 73

$$A_{d1}A_{11} = \Sigma_{d1}$$
  

$$A_{21}^{2} + A_{22}^{2} = \Sigma_{22}$$
  

$$\vdots$$
  

$$A_{d1}^{2} + \dots + A_{dd}^{2} = \Sigma_{dd}.$$
  
(2.29)

Exactly one new entry of the  $A$  matrix appears in each equation, making it possible to solve for the individual entries sequentially.

More compactly, from the basic identity

$$\Sigma_{ij} = \sum_{k=1}^{j} A_{ik} A_{jk}, \quad j \le i,$$

 $we get$ 

$$A_{ij} = \left(\Sigma_{ij} - \sum_{k=1}^{j-1} A_{ik} A_{jk}\right) / A_{jj}, \quad j < i,$$
 (2.30)

and

$$A_{ii} = \sqrt{\Sigma_{ii} - \sum_{k=1}^{i-1} A_{ik}^2}.$$
 (2.31)

These expressions make possible a simple recursion to find the Cholesky factor. Figure 2.16 displays an algorithm based on one in Golub and Van Loan [162]. Golub and Van Loan [162] give several other versions of the algorithm and also discuss numerical stability.

| Input: Symmetric positive definite matrix $d \times d$ matrix $\Sigma$ |
|------------------------------------------------------------------------|
| Output: Lower triangular A with $AA^{\top} = \Sigma$                   |
|                                                                        |
| $A \leftarrow 0 \ (d \times d \text{ zero matrix})$                    |
| for $j = 1, \ldots, d$                                                 |
| for $i = j, \ldots, d$                                                 |
| $v_i \leftarrow \Sigma_{ij}$                                           |
| for $k = 1, , j - 1$                                                   |
| $v_i \leftarrow v_i - A_{ik} A_{ik}$                                   |
| $A_{ij} \leftarrow v_i / \sqrt{v_j}$                                   |
| $\text{return } A$                                                     |
|                                                                        |

Fig. 2.16. Cholesky factorization.

#### The Semidefinite Case

If  $\Sigma$  is positive definite, an induction argument verifies that the quantity inside the square root in (2.31) is strictly positive so the  $A_{ii}$  are nonzero. This ensures that  $(2.30)$  does not entail division by zero and that the algorithm in Figure  $2.16$  runs to completion.

If, however,  $\Sigma$  is merely positive semidefinite, then it is rank deficient. It follows that any matrix A satisfying  $AA^{\top} = \Sigma$  must also be rank deficient; for if A had full rank, then  $\Sigma$  would too. If A is lower triangular and rank deficient, at least one element of the diagonal of  $A$  must be zero. (The determinant of a triangular matrix is the product of its diagonal elements, and the determinant of A is zero if A is singular.) Thus, for semidefinite  $\Sigma$ , any attempt at Cholesky factorization must produce some  $A_{jj} = 0$  and thus an error in (2.31) and the  $algorithm in Figure 2.16.$ 

From a purely mathematical perspective, the problem is easily solved by making the jth column of A identically zero if  $A_{ij} = 0$ . This can be deduced from the system of equations (2.29): the first element of the jth column of A encountered in this sequence of equations is the diagonal entry; if  $A_{ij} = 0$ , all subsequent equations for the jth column of  $\Sigma$  may be solved with  $A_{ij} = 0$ . In the factorization algorithm of Figure 2.16, this is accomplished by inserting "if  $v_j > 0$ " before the statement " $A_{ij} \leftarrow v_i / \sqrt{v_j}$ ." Thus, if  $v_j = 0$ , the entry  $A_{ij}$  is left at its initial value of zero.

In practice, this solution may be problematic because it involves checking whether an intermediate calculation  $(v_i)$  is exactly zero, making the modified algorithm extremely sensitive to round-off error.

Rather than blindly subjecting a singular covariance matrix to Cholesky factorization, it is therefore preferable to use the structure of the covariance matrix to reduce the problem to one of full rank. If  $X \sim N(0, \Sigma)$  and the  $d \times d$ matrix  $\Sigma$  has rank  $k < d$ , it is possible to express all d components of X as linear combinations of just  $k$  of the components, these  $k$  components having a covariance matrix of rank  $k$ . In other words, it is possible to find a subvector  $\tilde{X} = (X_{i_1}, \ldots, X_{i_k})$  and a  $d \times k$  matrix  $D$  such that  $D\tilde{X} \sim N(0, \Sigma)$  and for which the covariance matrix  $\tilde{\Sigma}$  of  $\tilde{X}$  has full rank k. Cholesky factorization can then be applied to  $\tilde{\Sigma}$  to find  $\tilde{A}$  satisfying  $\tilde{A}\tilde{A}^{\top} = \tilde{\Sigma}$ . The full vector X can be sampled by setting  $X = D\overline{A}Z, Z \sim N(0, I)$ .

Singular covariance matrices often arise from factor models in which a vector of length d is determined by  $k < d$  sources of uncertainty (factors). In this case, the prescription above reduces to using knowledge of the factor structure to generate  $X$ .

### Eigenvector Factorization and Principal Components

The equation  $AA^{\top} = \Sigma$  can also be solved by diagonalizing  $\Sigma$ . As a symmetric  $d \times d$  matrix,  $\Sigma$  has d real eigenvalues  $\lambda_1, \ldots, \lambda_d$ , and because  $\Sigma$  must be positive definite or semidefinite the  $\lambda_i$  are nonnegative. Furthermore,  $\Sigma$  has an associated orthonormal set of eigenvectors  $\{v_1, \ldots, v_d\}$ ; i.e., vectors satisfying

$$v_i^{\top} v_i = 1, \quad v_i^{\top} v_j = 0, \quad j \neq i, \quad i, j = 1, \dots, d,$$

and

 $\hat{\mathcal{L}}$ 

$$\Sigma v_i = \lambda_i v_i.$$

It follows that  $\Sigma = V \Lambda V^{\top}$ , where V is the orthogonal matrix  $(VV^{\top} = I)$ with columns  $v_1, \ldots, v_d$  and  $\Lambda$  is the diagonal matrix with diagonal entries  $\lambda_1, \ldots, \lambda_d$ . Hence, if we choose

$$A = V\Lambda^{1/2} = V \begin{pmatrix} \sqrt{\lambda_1} & & \\ & \sqrt{\lambda_2} & \\ & & \ddots & \\ & & & \sqrt{\lambda_d} \end{pmatrix}, \tag{2.32}$$

then

$$AA^{\top} = V\Lambda V^{\top} = \Sigma.$$

Methods for calculating V and  $\Lambda$  are included in many mathematical software libraries and discussed in detail in Golub and Van Loan [162].

Unlike the Cholesky factor, the matrix A in  $(2.32)$  has no particular structure providing a computational advantage in evaluating  $AZ$ , nor is this matrix faster to compute than the Cholesky factorization. The eigenvectors and eigenvalues of a covariance matrix do however have a statistical interpretation that is occasionally useful. We discuss this interpretation next.

If  $X \sim N(0, \Sigma)$  and  $Z \sim N(0, I)$ , then generating X as AZ for any choice of  $A$  means setting

$$X = a_1 Z_1 + a_2 Z_2 + \dots + a_d Z_d$$

where  $a_j$  is the *j*th column of A. We may interpret the  $Z_j$  as independent factors driving the components of X, with  $A_{ij}$  the "factor loading" of  $Z_j$  on  $X_i$ . If  $\Sigma$  has rank 1, then X may be represented as  $a_1Z_1$  for some vector  $a_1$ , and in this case a single factor suffices to represent X. If  $\Sigma$  has rank k, then  $k$  factors  $Z_1, \ldots, Z_k$  suffice.

If  $\Sigma$  has full rank and  $AA^{\top} = \Sigma$ , then A must have full rank and  $X = AZ$ implies  $Z = BX$  with  $B = A^{-1}$ . Thus, the factors  $Z_j$  are themselves linear combinations of the  $X_i$ . In the special case of A given in (2.32), we have

$$A^{-1} = \Lambda^{-1/2} V^{\top} \tag{2.33}$$

because  $V^{\top}V = I$  (V is orthogonal). It follows that  $Z_i$  is proportional to  $v_i^{\top} X$ , where  $v_j$  is the *j*th column of V and thus an eigenvector of  $\Sigma$ .

The factors  $Z_j$  constructed proportional to the  $v_j^\top X$  are optimal in a precise sense. Suppose we want to find the best single-factor approximation

75

to X; i.e., the linear combination  $w^{\top}X$  that best captures the variability of the components of X. A standard notion of optimality chooses  $w$  to maximize the variance of  $w^{\top}X$ , which is given by  $w^{\top}\Sigma w$ . Since this variance can be made arbitrarily large by multiplying any  $w$  by a constant, it makes sense to impose a normalization through a constraint of the form  $w^{\top}w = 1$ . We are thus led to the problem

$$\max_{w: w^\top w = 1} w^\top \Sigma w.$$

If the eigenvalues of  $\Sigma$  are ordered so that

$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_d,$$

then this optimization problem is solved by  $v_1$ , as is easily verified by appending the constraint with a Lagrange multiplier and differentiating. (This optimality property of eigenvectors is sometimes called Rayleigh's principle.) The problem of finding the next best factor orthogonal to the first reduces to solving

$$\max_{w: w^\top w = 1, w^\top v_1 = 0} w^\top \Sigma w.$$

This optimization problem is solved by  $v_2$ . More generally, the best k-factor approximation chooses factors proportional to  $v_1^{\top}X, v_2^{\top}X, \ldots, v_k^{\top}X$ . Since

$$v_j^\top \Sigma v_j = \lambda_j,$$

normalizing the  $v_i^{\top}X$  to construct unit-variance factors yields

$$Z_j = \frac{1}{\sqrt{\lambda_j}} v_j^\top X,$$

which coincides with (2.33). The transformation  $X = AZ$  recovering X from the  $Z_i$  is precisely the A in (2.32).

The optimality of this representation can be recast in the following way. Suppose that we are given X and that we want to find vectors  $a_1,\ldots,a_k$  in  $\Re^d$  and unit-variance random variables  $Z_1,\ldots,Z_k$  in order to approximate X by  $a_1Z_1 + \cdots + a_kZ_k$ . For any  $k = 1, \ldots, d$ , the mean square approximation  $\text{error}$ 

$$\mathsf{E}\left[\|X - \sum_{i=1}^{k} a_i Z_i\|^2\right], \qquad (\|x\|^2 = x^\top x)$$

is minimized by taking the  $a_i$  to be the columns of A in (2.32) and setting  $Z_i = v_i^\top X / \sqrt{\lambda_i}.$ 

In the statistical literature, the linear combinations  $v_i^{\top}X$  are called the *principal components* of  $X$  (see, e.g., Seber [325]). We may thus say that the principal components provide an optimal lower-dimensional approximation to a random vector. The variance *explained* by the first  $k$  principal components is the ratio

2.3 Normal Random Variables and Vectors 77

$$\frac{\lambda_1 + \dots + \lambda_k}{\lambda_1 + \dots + \lambda_k + \dots + \lambda_d};\tag{2.34}$$

in particular, the first principal component is chosen to explain as much variance as possible. In simulation applications, generating  $X$  from its principal components (i.e., using  $(2.32)$ ) is sometimes useful in designing variance reduction techniques. In some cases, the principal components interpretation suggests that variance reduction should focus first on  $Z_1$ , then on  $Z_2$ , and so on. We will see examples of this in Chapter 4 and related ideas in Section 5.5.

 $\mathcal{L}_{\mathcal{L}}(\mathcal{E}_{\mathcal{L}})$ 

 $\mathcal{L} = \mathcal{L} \oplus \mathcal{L}$ 

 $\mathbf{v} = \mathbf{v}$ 

Constitution .
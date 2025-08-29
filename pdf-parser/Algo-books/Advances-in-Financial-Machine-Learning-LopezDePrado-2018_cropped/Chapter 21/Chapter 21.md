- 4. Palach, J. (2008): *Parallel Programming with Python* , 1st ed. Packt Publishing.
- 5. Summerfield, M. (2013): *Python in Practice: Create Better Programs Using Concurrency, Libraries, and Patterns* , 1st ed. Addison-Wesley.
- 6. Zaccone, G. (2015): *Python Parallel Programming Cookbook* , 1st ed. Packt Publishing.

#### **Notes**

1 *Heisenbugs* , named after Heisenberg's uncertainty principle, describe bugs that change their behavior when scrutinized. Multiprocessing bugs are a prime example.

2 <https://pypi.python.org/pypi/joblib> .

3 [http://scikit-learn.org/stable/developers/performance.html#multi-core](http://scikit-learn.org/stable/developers/performance.html#multi-core-parallelism-using-joblib-parallel)parallelism-using-joblib-parallel .

4 http://stackoverflow.com/questions/1816958/cant-pickle-type[instancemethod-when-using-pythons-multiprocessing-pool-ma](http://stackoverflow.com/questions/1816958/cant-pickle-type-instancemethod-when-using-pythons-multiprocessing-pool-ma) .

# **CHAPTER 21**

# **Brute Force and Quantum Computers**

# **21.1 Motivation**

Discrete mathematics appears naturally in multiple ML problems, including hierarchical clustering, grid searches, decisions based on thresholds, and integer optimization. Sometimes, these problems do not have a known analytical (closed-form) solution, or even a heuristic to approximate it, and our only hope is to search for it through brute force. In this chapter, we will study how a financial problem, intractable to modern supercomputers, can be reformulated as an integer optimization problem. Such a representation makes it amenable to quantum computers. From this example the reader can infer how to translate his particular financial ML intractable problem into a quantum brute force search.

# **21.2 Combinatorial Optimization**

Combinatorial optimization problems can be described as problems where there is a finite number of feasible solutions, which result from combining the discrete values of a finite number of variables. As the number of feasible combinations grows, an exhaustive search becomes impractical. The traveling salesman problem is an example of a combinatorial optimization problem that is known to be NP hard (Woeginger [2003]), that is, the category of problems that are at least as hard as the hardest problems solvable is nondeterministic polynomial time.

What makes an exhaustive search impractical is that standard computers evaluate and store the feasible solutions sequentially. But what if we could evaluate and store all feasible solutions at once? That is the goal of quantum computers. Whereas the bits of a standard computer can only adopt one of two possible states ({0, 1}) at once, quantum computers rely on qubits, which are memory elements that may hold a *linear superposition* of both states. In theory, quantum computers can accomplish this thanks to quantum mechanical phenomena. In some implementations, qubits can support currents flowing in two directions at once, hence providing the desired superposition. This linear superposition property is what makes quantum computers ideally suited for solving NP-hard combinatorial optimization problems. See Williams [2010] for a general treatise on the capabilities of quantum computers.

The best way to understand this approach is through a particular example. We will now see how a dynamic portfolio optimization problem subject to generic transaction cost functions can be represented as a combinatorial optimization problem, tractable to quantum computers. Unlike Garleanu and Pedersen [2012], we will not assume that the returns are drawn from an IID Gaussian distribution. This problem is particularly relevant to large asset managers, as the costs from excessive turnover and implementation shortfall may critically erode the profitability of their investment strategies.

# **21.3 The Objective Function**

Consider a set on assets *X* = { *x <sup>i</sup>* }, *i* = 1, …, *N* , with returns following a multivariate Normal distribution at each time horizon *h* = 1, …, *H* , with varying mean and variance. We will assume that the returns are multivariate Normal, time-independent, however not identically distributed through time. We define a trading trajectory as an *NxH* matrix ω that determines the proportion of capital allocated to each of the *N* assets over each of the *H* horizons. At a particular horizon *h* = 1, …, *H* , we have a forecasted mean μ *<sup>h</sup>* , a forecasted variance *V <sup>h</sup>* and a forecasted transaction cost function τ *<sup>h</sup>* [ω]. This means that, given a trading trajectory ω, we can compute a vector of expected investment returns *r* , as

where τ[ω] can adopt any functional form. Without loss of generality, consider the following:

• 
$$\tau_1 [\omega] = \sum_{n=1}^N c_{n,1} \sqrt{|\omega_{n,1} - \omega_n^*|}$$
  
•  $\tau_h [\omega] = \sum_{n=1}^N c_{n,h} \sqrt{|\omega_{n,h} - \omega_{n,h-1}|}$ , for  $h = 2, ..., H$ 

ω\* *<sup>n</sup>* is the initial allocation to instrument n, *n* = 1, …, *N*

τ[ω] is an *Hx1* vector of transaction costs. In words, the transaction costs associated with each asset are the sum of the square roots of the changes in capital allocations, re-scaled by an asset-specific factor *C <sup>h</sup>* = { *c <sup>n</sup> , <sup>h</sup>* } *<sup>n</sup>* <sup>=</sup> 1, …, *<sup>N</sup>* that changes with *h.* Thus, *C <sup>h</sup>* is an *Nx1* vector that determines the relative transaction cost across assets.

The Sharpe Ratio (Chapter 14) associated with *r* can be computed as (μ *<sup>h</sup>* being net of the risk-free rate)

$$SR[r] = \frac{\sum_{h=1}^{H} \mu_{h}^{'} \omega_{h} - \tau_{h}[\omega]}{\sqrt{\sum_{h=1}^{H} \omega_{h}^{'} V_{h} \omega_{h}}}$$

#### **21.4 The Problem**

We would like to compute the optimal trading trajectory that solves the problem

$$\max_{\omega} SR[r]$$
  
s.t. : 
$$\sum_{i=1}^{N} |\omega_{i,h}| = 1, \ \forall h = 1, \dots, H$$

This problem attempts to compute a global dynamic optimum, in contrast to the static optimum derived by mean-variance optimizers (see Chapter 16). Note that non-continuous transaction costs are embedded in *r* . Compared to standard portfolio optimization applications, this is not a convex (quadratic) programming problem for at least three reasons: (1) Returns are not identically distributed, because μ *<sup>h</sup>* and *V <sup>h</sup>* change with *h.* (2) Transaction costs τ *<sup>h</sup>* [ω] are non-continuous and changing with *h.* (3) The objective function *SR* [ *r* ] is not convex. Next, we will show how to calculate solutions without making use of any analytical property of the objective function (hence the generalized nature of this approach).

## **21.5 An Integer Optimization Approach**

The generality of this problem makes it intractable to standard convex optimization techniques. Our solution strategy is to discretize it so that it becomes amenable to integer optimization. This in turn allows us to use quantum computing technology to find the optimal solution.

# **21.5.1 Pigeonhole Partitions**

Suppose that we count the number of ways that *K* units of capital can be allocated among *N* assets, where we assume *K* > *N* . This is equivalent to finding the number of non-negative integer solutions to *x <sup>1</sup>* + … + *x <sup>N</sup>* = *K* , which has the nice combinatorial solution . This bears a similarity to the classic integer partitioning problem in number theory for which Hardy and Ramanujan (and later, Rademacher) proved an asymptotic expression (see Johansson [2012]). While order does not matter in the partition problem, order is very relevant to the problem we have at hand. For example, if *K* = 6 and *N* = 3, partitions (1, 2, 3) and (3, 2, 1) must be treated as different (obviously (2, 2, 2) does not need to be permutated). Figure 21.1 illustrates how order is important when allocating 6 units of capital to 3 different assets. This means that we must consider all distinct permutations of each partition. Even though there is a nice combinatorial solution to find the number of such allocations, it

may still be computationally intensive to find as *K* and *N* grow large. However, we can use Stirling's approximation to easily arrive at an estimate.

![](_page_4_Figure_1.jpeg)

**Figure 21.1** Partitions (1, 2, 3) and (3, 2, 1) must be treated as different

Snippet 21.1 provides an efficient algorithm to generate the set of all partitions, , where are the natural numbers including zero (whole numbers).

#### **SNIPPET 21.1 PARTITIONS OF** *K* **OBJECTS INTO** *N* **SLOTS**

#### **21.5.2 Feasible Static Solutions**

We would like to compute the set of all feasible solutions at any given horizon *h* , which we denote Ω. Consider a partition set of *K* units into *N* assets, *p <sup>K</sup> , <sup>N</sup>* . For each partition { *p <sup>i</sup>* } *<sup>i</sup>* <sup>=</sup> 1, …, *<sup>N</sup>* ∈ *p <sup>K</sup> , <sup>N</sup>* , we can define a vector of absolute weights such that , where (the full-investment constraint). This full-investment (without leverage) constraint implies that every weight can be either positive or negative, so for every vector of absolute weights {|ω *<sup>i</sup>* |} *<sup>i</sup>* <sup>=</sup> 1, …, *<sup>N</sup>* we can generate 2 *<sup>N</sup>* vectors of (signed) weights. This is accomplished by multiplying the items in {|ω *<sup>i</sup>* |} *<sup>i</sup>* <sup>=</sup> 1, …, *<sup>N</sup>* with the items of the Cartesian product of { − 1, 1} with *N* repetitions. Snippet 21.2 shows how to generate the set Ω of all vectors of weights associated with all partitions, .

#### **SNIPPET 21.2 SET Ω OF ALL VECTORS ASSOCIATED WITH ALL PARTITIONS**

## **21.5.3 Evaluating Trajectories**

Given the set of all vectors Ω, we define the set of all possible trajectories Φ as the Cartesian product of Ω with *H* repetitions. Then, for every trajectory we can evaluate its transaction costs and SR, and select the trajectory with optimal performance across Φ. Snippet 21.3 implements this functionality. The object params is a list of dictionaries that contain the values of *C* , μ, *V.*

#### **SNIPPET 21.3 EVALUATING ALL TRAJECTORIES**

```
import numpy as np
from itertools import product
#-
<pre>def evalTCosts(w,params):</pre>
    # Compute t-costs of a particular trajectory
    \texttt{tcost} = \texttt{np.zeros}(\texttt{w.shape}[1])w = np.zeros(shape=w.shape[0])for i in range(tcost.shape[0]):
        c =params[i]['c']
        tcost[i] = (c *abs(w[:, i] - w) * * .5).sum()w = w[:, i].copy()return tcost
#-
<pre>def evalSR(params, w, tcost):</pre>
    # Evaluate SR over multiple horizons
    mean, cov=0, 0for h in range(w.shape[1]):
        params =params[h]mean = np.dot(w[:, h] .T, params ['mean']) [0] -tcost [h]cov+=np.dot(w[:,h].T,np.dot(params ['cov'],w[:,h]))
    sr=mean/cov**.5
    return sr
\#<pre>def dynOptPort(params, k=None):</pre>
    # Dynamic optimal portfolio
    #1) Generate partitions
    if k is None:k=params[0]['mean'].shape[0]
    n=params[0]['mean'].shape[0]
    w all, sr=getAllWeights(k,n), None
    #2) Generate trajectories as cartesian products
    <pre>for prod in product(w all.T, repeat=len(params)):</pre>
        w =np.array(prod_).T # concatenate product into a trajectory
        tcost =evalTCosts(w ,params)
        sr =evalSR(params,w ,tcost ) # evaluate trajectory
        if sr is None or sr<sr : # store trajectory if better
             sr, w=sr ,w .copy()
    return w
```

Note that this procedure selects an globally optimal trajectory without relying on convex optimization. A solution will be found even if the covariance matrices are ill-conditioned, transaction cost functions are non-continuous, etc. The price we pay for this generality is that calculating the solution is extremely computationally intensive. Indeed, evaluating all trajectories is similar to the traveling-salesman problem. Digital computers are inadequate for this sort of NP-complete or NP-hard problems; however, quantum computers have the advantage of evaluating multiple solutions at once, thanks to the property of linear superposition.

The approach presented in this chapter set the foundation for Rosenberg et al. [2016], which solved the optimal trading trajectory problem using a quantum annealer. The same logic can be applied to a wide range on financial problems involving path dependency, such as a trading trajectory. Intractable ML algorithm can be discretized and translated into a brute force search, intended for a quantum computer.

# **21.6 A Numerical Example**

Below we illustrate how the global optimum can be found in practice, using a digital computer. A quantum computer would evaluate all trajectories at once, whereas the digital computer does this sequentially.

# **21.6.1 Random Matrices**

Snippet 21.4 returns a random matrix of Gaussian values with known rank, which is useful in many applications (see exercises). You may want to consider this code the next time you want to execute multivariate Monte Carlo experiments, or scenario analyses.

#### **SNIPPET 21.4 PRODUCE A RANDOM MATRIX OF A GIVEN RANK**

Snippet 21.5 generates *H* vectors of means, covariance matrices, and transaction cost factors, *C* , μ, *V.* These variables are stored in a params list.

#### **SNIPPET 21.5 GENERATE THE PROBLEM'S PARAMETERS**

## **21.6.2 Static Solution**

Snippet 21.6 computes the performance of the trajectory that results from local (static) optima.

#### **SNIPPET 21.6 COMPUTE AND EVALUATE THE STATIC SOLUTION**

# **21.6.3 Dynamic Solution**

Snippet 21.7 computes the performance associated with the globally dynamic optimal trajectory, applying the functions explained throughout the chapter.

#### **SNIPPET 21.7 COMPUTE AND EVALUATE THE DYNAMIC SOLUTION**

### **Exercises**

- 1. Using the pigeonhole argument, prove that *.*
- 2. Use Snippet 21.4 to produce random matrices of size (1000, 10), sigma = 1 and
  - 1. rank = 1 . Plot the eigenvalues of the covariance matrix.
  - 2. rank = 5 . Plot the eigenvalues of the covariance matrix.
  - 3. rank = 10 . Plot the eigenvalues of the covariance matrix.
  - 4. What pattern do you observe? How would you connect it to Markowitz's curse (Chapter 16)?
- 3. Run the numerical example in Section 21.6:
  - 1. Use size = 3 , and compute the running time with timeit . Repeat 10 batches of 100 executions. How long did it take?
  - 2. Use size = 4 , and timeit . Repeat 10 batches of 100 executions. How long did it take?
- 4. Review all snippets in this chapter.
  - 1. How many could be vectorized?
  - 2. How many could be parallelized, using the techniques from Chapter 20?
  - 3. If you optimize the code, by how much do you think you could speed it up?
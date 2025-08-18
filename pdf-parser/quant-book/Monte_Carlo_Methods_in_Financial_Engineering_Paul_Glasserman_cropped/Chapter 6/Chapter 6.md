This chapter presents methods for reducing discretization error  $-$  the bias in Monte Carlo estimates that results from time-discretization of stochastic differential equations. Chapter 3 gives examples of continuous-time stochastic processes that can be simulated exactly at a finite set of dates, meaning that the joint distribution of the simulated values coincides with that of the continuous-time model at the simulated dates. But these examples are exceptional and most models arising in derivatives pricing can be simulated only approximately. The simplest approximation is the Euler scheme; this method is easy to implement and almost universally applicable, but it is not always sufficiently accurate. This chapter discusses methods for improving the Euler scheme and, as a prerequisite for this, discusses criteria for comparing discretization methods.

The issues addressed in this chapter are orthogonal to those in Chapters 4 and 5. Once a time-discretization method is fixed, applying a variance reduction technique or quasi-Monte Carlo method may improve precision in estimating an expectation at the fixed level of discretization, but it can do nothing to reduce discretization bias.

## 6.1 Introduction

We begin by discussing properties of the Euler scheme, the simplest method for approximate simulation of stochastic differential equations. We then undertake an expansion to refine the Euler scheme and present criteria for comparing methods.

## 6.1.1 The Euler Scheme and a First Refinement

We consider processes  $X$  satisfying a stochastic differential equation (SDE) of the form

$$dX(t) = a(X(t)) dt + b(X(t)) dW(t), \t\t(6.1)$$

usually with  $X(0)$  fixed. In the most general setting we consider, X takes values in  $\mathbb{R}^d$  and W is an m-dimensional standard Brownian motion, in which case a takes values in  $\mathbb{R}^d$  and b takes values in  $\mathbb{R}^{d \times m}$ . Some of the methods in this chapter are most easily introduced in the simpler case of scalar  $X$  and  $W$ . The coefficient functions  $a$  and  $b$  are assumed to satisfy the conditions in Appendix B.2 for existence and uniqueness of a strong solution to the SDE  $(6.1)$ ; indeed, we will need to impose stronger conditions to reduce discretization error.

We use  $\hat{X}$  to denote a time-discretized approximation to X. The Euler (or Euler-Maruyama, after [254]) approximation on a time grid  $0 = t_0 < t_1 <$  $\cdots < t_m$  is defined by  $\hat{X}(0) = X(0)$  and, for  $i = 0, \ldots, m-1$ ,

$$\hat{X}(t_{i+1}) = \hat{X}(t_i) + a(\hat{X}(t_i))[t_{i+1} - t_i] + b(\hat{X}(t_i))\sqrt{t_{i+1} - t_i}Z_{i+1},$$

with  $Z_1, Z_2, \ldots$  independent, *m*-dimensional standard normal random vectors. To lighten notation, we restrict attention to a grid with a fixed spacing  $h$ , meaning that  $t_i = ih$ . Everything we discuss carries over to the more general case provided the largest of the increments  $t_{i+1}-t_i$  decreases to zero. Adaptive methods, in which the time steps depend on the evolution of  $X$  and are thus stochastic, require separate treatment; see, for example, Gaines and Lyons  $[133].$ 

With a fixed time step  $h > 0$ , we may write  $\hat{X}(ih)$  as  $\hat{X}(i)$  and write the Euler scheme as

$$\hat{X}(i+1) = \hat{X}(i) + a(\hat{X}(i))h + b(\hat{X}(i))\sqrt{h}Z_{i+1}.$$
(6.2)

Implementation of this method is straightforward, at least if  $a$  and  $b$  are easy to evaluate. Can we do better? And in what sense is one approximation better than another? These are the questions we address.

In the numerical solution of *ordinary* differential equations, methods of higher-order accuracy often rely on Taylor expansions. If  $b$  were identically zero (and thus  $(6.1)$  non-stochastic),  $(6.2)$  would reduce to a linear approximation, and a natural strategy for improving accuracy would include higherorder terms in a Taylor expansion of  $a(X(t))$ . A similar strategy applies to stochastic differential equations, but it must be carried out consistent with the rules of Itô calculus rather than ordinary calculus.

## A First Refinement

Inspection of the Euler scheme  $(6.2)$  from the perspective of Taylor expansion suggests a possible inconsistency: this approximation expands the drift to  $O(h)$ but the diffusion term only to  $O(\sqrt{h})$ . The approximation to the diffusion term omits  $O(h)$  contributions, so including a term of order h in the drift looks like spurious accuracy. This discrepancy also suggests that to refine the Euler scheme we may want to focus on the diffusion term.

We now carry out this proposal. We will see, however, that whether or not it produces an improvement compared to the Euler scheme depends on how we measure error.

We start with the scalar case  $d = m = 1$ . Recall that the SDE (6.1) abbreviates the relation

$$X(t) = X(0) + \int_0^t a(X(u)) du + \int_0^t b(X(u)) dW(u). \tag{6.3}$$

The Euler scheme results from the approximations

$$\int_{t}^{t+h} a(X(u)) du \approx a(X(t))h \tag{6.4}$$

and

$$\int_{t}^{t+h} b(X(u)) \, dW(u) \approx b(X(t))[W(t+h) - W(t)]. \tag{6.5}$$

In both cases, an integrand over  $[t, t+h]$  is approximated by its value at t. To improve the approximation of the diffusion term, we need a better approximation of  $b(X(u))$  over an interval  $[t, t+h]$ . We therefore examine the evolution of  $b(X(u))$ .

From Itô's formula we get

$$\begin{split} db(X(t)) \\ &= b'(X(t)) \, dX(t) + \tfrac{1}{2} b''(X(t)) b^2(X(t)) \, dt \\ &= \left[ b'(X(t)) a(X(t)) + \tfrac{1}{2} b''(X(t)) b^2(X(t)) \right] \, dt + b'(X(t)) b(X(t)) \, dW(t) \\ &\equiv \mu_b(X(t)) \, dt + \sigma_b(X(t)) \, dW(t), \end{split}$$

where  $b'$  and  $b''$  are the first and second derivatives of b. Applying the Euler approximation to the process  $b(X(t))$  results in the approximation of  $b(X(u))$ ,  $t \leq u \leq t + h$  by

$$\begin{split} b(X(u)) &\approx b(X(t)) + \mu_b(X(t))[u-t] + \sigma_b(X(t))[W(u) - W(t)] \\ &= b(X(t)) + \left(b'(X(t))a(X(t)) + \frac{1}{2}b''(X(t))b^2(X(t))\right)[u-t] \\ &+ b'(X(t))b(X(t))[W(u) - W(t)]. \end{split}$$

Now  $W(u) - W(t)$  is  $O(\sqrt{u-t})$  (in probability) whereas the drift term in this approximation is  $O(u-t)$  and thus of higher order. Dropping this higher-order term yields the simpler approximation

$$b(X(u)) \approx b(X(t)) + b'(X(t))b(X(t))[W(u) - W(t)], \quad u \in [t, t+h]. \tag{6.6}$$

Armed with this approximation, we return to the problem of refining  $(6.5)$ . Instead of freezing  $b(X(u))$  at  $b(X(t))$  over the interval  $[t, t+h]$ , as in (6.5), we use the approximation  $(6.6)$ . Thus, we replace  $(6.5)$  with

$$\int_{t}^{t+h} b(X(u)) dW(u)\n$$

$$\n\approx \int_{t}^{t+h} (b(X(t)) + b'(X(t))b(X(t))[W(u) - W(t)]) dW(u)\n$$

$$\n= b(X(t))[W(t+h) - W(t)]\n$$

$$\n+ b'(X(t))b(X(t)) \left( \int_{t}^{t+h} [W(u) - W(t)] dW(u) \right). \n$$
(6.7)

The proposed refinement uses this expression in place of  $b(\hat{X}(i))\sqrt{h}Z_{i+1}$  in the Euler scheme  $(6.2)$ .

To make this practical, we need to simplify the remaining integral in  $(6.7)$ . We can write this integral as

$$\int_{t}^{t+h} [W(u) - W(t)] dW(u)\n$$

$$\n= \int_{t}^{t+h} W(u) dW(u) - W(t) \int_{t}^{t+h} dW(u)\n$$

$$\n= Y(t+h) - Y(t) - W(t)[W(t+h) - W(t)] \n$$
(6.8)

with

 $\bullet \rightarrow \mathbb{R}^{n\times n-1}$ 

$$Y(t) = \int_0^t W(t) \, dW(t);$$

i.e.,  $Y(0) = 0$  and

$$dY(t) = W(t) \, dW(t).$$

Itô's formula verifies that the solution to this SDE is

$$Y(t) = \frac{1}{2}W(t)^2 - \frac{1}{2}t.$$

Making this substitution in  $(6.8)$  and simplifying, we get

$$\int_{t}^{t+h} [W(u) - W(t)] \, dW(u) = \frac{1}{2} [W(t+h) - W(t)]^2 - \frac{1}{2}h. \tag{6.9}$$

Using this identity in  $(6.7)$ , we get

$$\int_{t}^{t+h} b(X(u)) \, dW(u) \approx b(X(t))[W(t+h) - W(t)]$$
$$+ \frac{1}{2}b'(X(t))b(X(t)) \left( [W(t+h) - W(t)]^2 - h \right).$$

Finally, we use this approximation to approximate  $X(t+h)$ . We refine the one-step Euler approximation

$$X(t+h) \approx X(t) + a(X(t))h + b(X(t))[W(t+h) - W(t)]$$

 $6.1$  Introduction 343

$$X(t+h) \approx X(t) + a(X(t))h + b(X(t))[W(t+h) - W(t)] + \frac{1}{2}b'(X(t))b(X(t))([W(t+h) - W(t)]^2 - h).$$

In a simulation algorithm, we apply this recursively at  $h, 2h, \ldots$ , replacing the increments of W with  $\sqrt{h}Z_{i+1}$ ; more explicitly, we have

$$\begin{split}\n\hat{X}(i+1) &= \hat{X}(i) + a(\hat{X}(i))h + b(\hat{X}(i))\sqrt{h}Z_{i+1} \\
&\quad + \frac{1}{2}b'(\hat{X}(i))b(\hat{X}(i))h(Z_{i+1}^2 - 1). \n\end{split} \n\tag{6.10}$$

This algorithm was derived by Milstein [266] through an analysis of partial differential equations associated with the diffusion  $X$ . It is sometimes called the Milstein scheme, but this terminology is ambiguous because there are several important methods due to Milstein.

The approximation method in  $(6.10)$  adds a term to the Euler scheme. It expands both the drift and diffusion terms to  $O(h)$ . Observe that, conditional on  $\hat{X}(i)$ , the new term

$$\frac{1}{2}b'(\hat{X}(i))b(\hat{X}(i))h(Z_{i+1}^2-1)$$

has mean zero and is uncorrelated with the Euler terms because  $Z_{i+1}^2-1$ and  $Z_{i+1}$  are uncorrelated. The question remains, however, whether and in what sense  $(6.10)$  is an improvement over the Euler scheme. We address this in Section 6.1.2, after discussing the case of vector-valued  $X$  and  $W$ .

## The Multidimensional Case

Suppose, now, that  $X(t) \in \mathbb{R}^d$  and  $W(t) \in \mathbb{R}^m$ . Write  $X_i$ ,  $W_i$ , and  $a_i$  for the ith components of X, W, and a, and write  $b_{ij}$  for the *ij*-entry of b. Then

$$X_i(t+h) = X_i(t) + \int_t^{t+h} a_i(X(u)) du + \sum_{j=1}^m \int_t^{t+h} b_{ij}(X(u)) dW_j(u),$$

and we need to approximate the integrals on the right. As in the Euler scheme, we approximate the drift term using

$$\int_{t}^{t+h} a_i(X(u)) \, du \approx a_i(X(t))h$$

The argument leading to  $(6.7)$  yields

$$\int_{t}^{t+h} b_{ij}(X(u)) dW_{j}(u) \approx b_{ij}(X(t))[W_{j}(t+h) - W_{j}(t)]$$
$$+ \sum_{\ell=1}^{d} \sum_{h=1}^{m} \frac{\partial b_{ij}}{\partial x_{\ell}}(X(t))b_{\ell k}(X(t)) \int_{t}^{t+h} [W_{k}(u) - W_{k}(t)] dW_{j}(u). \quad (6.11)$$

 $to$ 

L,

For  $k = i$ , we can evaluate the integral in (6.11) as in the scalar case:

$$\int_{t}^{t+h} [W_j(u) - W_j(t)] \, dW_j(u) = \frac{1}{2} [W_j(t+h) - W_j(t)]^2 - \frac{1}{2}h.$$

However, there is no comparable expression for the off-diagonal terms

$$\int_{t}^{t+h} [W_k(u) - W_k(t)] dW_j(u), \quad k \neq j.$$

These mixed integrals (or more precisely their differences) are called  $L\acute{e}v\gamma$ *area* terms; see the explanation in Protter [300, p.82], for example. Generating samples from their distribution is a challenging simulation problem. Methods for doing so are developed in Gaines and Lyons  $[132]$  and Wiktorsson  $[356]$ , but the difficulties involved limit the applicability of the expansion  $(6.11)$  in models driven by multidimensional Brownian motion. Fortunately, we will see that for the purpose of estimating an expectation it suffices to simulate rough approximations to these mixed Brownian integrals.

### 6.1.2 Convergence Order

Equation  $(6.10)$  displays a refinement of the Euler scheme based on expanding the diffusion term to  $O(h)$  rather than just  $O(\sqrt{h})$ . To discuss the extent and the sense in which this algorithm is an improvement over the Euler scheme, we need to establish a figure of merit for comparing discretizations.

Two broad categories of error of approximation are commonly used in measuring the quality of discretization methods: criteria based on the pathwise proximity of a discretized process to a continuous process, and criteria based on the proximity of the corresponding distributions. These are generally  $\text{termed }$  strong and weak criteria, respectively.

Let  $\{\hat{X}(0), \hat{X}(h), \hat{X}(2h), \ldots\}$  be any discrete-time approximation to a continuous-time process X. Fix a time T and let  $n = |T/h|$ . Typical strong error criteria are

$$\mathsf{E}\left[\|\hat{X}(nh) - X(T)\|\right], \quad \mathsf{E}\left[\|\hat{X}(nh) - X(T)\|^2\right],$$

and

$$\mathsf{E}\left[\sup_{0\leq t\leq T}\|\hat{X}(\lfloor t/h\rfloor h)-X(t)\|\right],$$

for some vector norm  $\|\cdot\|$ . Each of these expressions measures the deviation between the individual values of  $X$  and the approximation  $X$ .

In contrast, a typical weak error criterion has the form

$$\left| \mathsf{E}[f(\hat{X}(nh))] - \mathsf{E}[f(X(T))] \right|, \tag{6.12}$$

with f ranging over functions from  $\mathbb{R}^d$  to  $\mathbb{R}$  typically satisfying some smoothness conditions. Requiring that an expression of the form  $(6.12)$  converge to zero as  $h$  decreases to zero imposes no constraint on the relation between the outcomes of  $X(nh)$  and  $X(T)$ ; indeed, the two need not even be defined on the same probability space. Making the error criterion  $(6.12)$  small merely requires that the distributions of  $X(nh)$  and  $X(T)$  be close.

For applications in derivatives pricing, weak error criteria are most relevant. We would like to ensure that prices (which are expectations) computed from X are close to prices computed from  $X$ ; we are not otherwise concerned about the paths of the two processes. It is nevertheless useful to be aware of strong error criteria to appreciate the relative merits of alternative discretization methods.

Even after we fix an error criterion, it is rarely possible to ensure that the error using one discretization method will be smaller than the error using another in a specific problem. Instead, we compare methods based on their asymptotic performance for small  $h$ .

Under modest conditions, even the simple Euler scheme converges (with respect to both strong and weak criteria) as the time step  $h$  decreases to zero. We therefore compare discretization schemes based on the *rate* at which they converge. Following Kloeden and Platen [211], we say that a discretization  $\hat{X}$ has strong order of convergence  $\beta > 0$  if

$$\mathsf{E}\left[\|\hat{X}(nh) - X(T)\|\right] \le ch^{\beta} \tag{6.13}$$

for some constant  $c$  and all sufficiently small  $h$ . The discretization scheme has *weak* order of convergence  $\beta$  if

$$\left| \mathsf{E}[f(\hat{X}(nh))] - \mathsf{E}[f(X(T))] \right| \le ch^{\beta} \tag{6.14}$$

for some constant c and all sufficiently small h, for all f in a set  $C_P^{2\beta+2}$ . The set  $C_P^{2\beta+2}$  consists of functions from  $\Re^d$  to  $\Re$  whose derivatives of order  $0, 1, \ldots, 2\beta + 2$  are polynomially bounded. A function  $q: \mathbb{R}^d \to \mathbb{R}$  is polynomially bounded if

$$|g(x)| \le k(1 + ||x||^q)$$

for some constants k and q and all  $x \in \mathbb{R}^d$ . The constant c in (6.14) may depend on  $f$ .

In both (6.13) and (6.14), a larger value of  $\beta$  implies faster convergence to zero of the discretization error. The same scheme will often have a smaller strong order of convergence than its weak order of convergence. For example, the Euler scheme typically has a strong order of  $1/2$ , but it often achieves a weak order of  $1$ .

## Convergence Order of the Euler Scheme

In more detail, the Euler scheme has strong order  $1/2$  under conditions only slightly stronger than those in Theorem  $B.2.1$  of Appendix  $B.2$  for existence

and uniqueness of a (strong) solution to the SDE  $(6.1)$ . We may generalize  $(6.1)$  by allowing the coefficient functions a and b to depend explicitly on time t as well as on  $X(t)$ . Because X is vector-valued, we could alternatively take t to be one of the components of  $X(t)$ ; but that formulation leads to unnecessarily strong conditions for convergence because it requires that the coefficients be as smooth in  $t$  as they are in  $X$ . In addition to the conditions of Theorem  $B.2.1$ , suppose that

$$\mathsf{E}\left[\|X(0) - \hat{X}(0)\|^2\right] \le K\sqrt{h} \tag{6.15}$$

and

$$\|a(x,s) - a(x,t)\| + \|b(x,s) - b(x,t)\| \le K(1 + \|x\|)\sqrt{|t-s|},\qquad(6.16)$$

for some constant  $K$ ; then the Euler scheme has strong order  $1/2$ . (This is proved in Kloeden and Platen [211], pp.342–344. It is observed in Milstein [266] though without explicit hypotheses.) Condition  $(6.15)$  is trivially satisfied if  $X(0)$  is known and we set  $X(0)$  equal to it.

Stronger conditions are required for the Euler scheme to have weak order 1. For example, Theorem  $14.5.2$  of Kloeden and Platen [211] requires that the functions  $a$  and  $b$  be four times continuously differentiable with polynomially bounded derivatives. More generally, the Euler scheme has weak order  $\beta$  if a and b are  $2(\beta+1)$  times continuously differentiable with polynomially bounded derivatives; the condition  $(6.14)$  then applies only to functions f with the same degree of smoothness.

To see how smoothness can lead to a higher weak order than strong order. consider the following argument. Suppose, for simplicity, that  $T = nh$  and that  $X(0)$  is fixed so that  $E[f(X(0))]$  is known. By writing

$$\mathsf{E}[f(X(T))] = \mathsf{E}[f(X(0))] + \mathsf{E}\left[\sum_{i=0}^{n-1} \mathsf{E}[f(X((i+1)h)) - f(X(ih))|X(ih)]\right],$$

we see that accurate estimation of  $E[f(X(T))]$  follows from accurate estimation of the conditional expectations  $\mathsf{E}[f(X((i+1)h))-f(X(ih))|X(ih)].$ Applying a Taylor approximation to  $f$  (and taking X scalar for simplicity),  $we get$ 

$$\mathsf{E}[f(X((i+1)h)) - f(X(ih))|X(ih)] \approx \sum_{j=0}^{r} \frac{f^{(j)}(X(ih))}{j!} \mathsf{E}[(X((i+1)h) - X(ih))^{j}|X(ih)]. \tag{6.17}$$

Thus, if  $f$  is sufficiently smooth, then to achieve a high order of weak convergence a discretization scheme need only approximate conditional *moments* of the increments of the process  $X$ . With sufficient smoothness in the coefficient functions  $a$  and  $b$ , higher conditional moments are of increasingly high order

in h. Smoothness conditions on  $a, b, \text{ and } f$  leading to a weak order of convergence  $\beta$  for the Euler scheme follow from careful accounting of the errors in expanding  $f$  and approximating the conditional moments; see Kloeden and Platen [211], Section 14.5, and Talay [340, 341].

The accuracy of a discretization scheme in estimating an expression of the form  $\mathsf{E}[f(X(T))]$  does not necessarily extend to the simulation of other quantities associated with the same process. In Section 6.4 we discuss difficulties arising in simulating the maximum of a diffusion, for example. Talay and  $\text{Zheng [344]}$  analyze discretization error in estimating quantiles of the distribution of a component of  $X(T)$ . They provide very general conditions under which the bias in a quantile estimate computed from an Euler approximation is  $O(h)$ ; but they also show that the implicit constant in this  $O(h)$  error is large — especially in the tails of the distribution — and that this makes accurate quantile estimation difficult.

### Convergence Order of the Refined Scheme

 $\mathcal{F}$ 

Theorem  $10.3.5$  of Kloeden and Platen [211] and Theorem 2-2 of Talay [340] provide conditions under which Milstein's refinement  $(6.10)$  and its multidimensional generalization based on  $(6.11)$  have strong order 1. The conditions required extend the linear growth, Lipschitz condition, and  $(6.16)$  to derivatives of the coefficient functions  $a$  and  $b$ . Thus, under these relatively modest additional conditions, expanding the diffusion term to  $O(h)$  instead of just  $O(\sqrt{h})$  through the derivation in Section 6.1.1 increases the order of strong convergence.

But the weak order of convergence of the refined scheme  $(6.10)$  is also 1, as it is for the Euler scheme. In this respect, including additional terms as in  $(6.10)$  and  $(6.11)$  — does not result in greater accuracy. This should not be viewed as a deficiency of Milstein's method; rather, the Euler scheme is better than it "should" be, achieving order-1 weak convergence without expanding all terms to  $O(h)$ . This is in fact just the simplest example of a broader pattern of results on the number of terms required to achieve strong or weak convergence of a given order (to which we return in Section  $6.3.1$ ). In order to achieve a weak order greater than that of the Euler scheme, we need to expand dt-integrals to order  $h^2$  and stochastic integrals to order h. We carry this out in the next section to arrive at a method with a higher weak order of convergence.

It is reassuring to know that a discretization scheme has a high order of convergence, but before venturing into our next derivation we should take note of the fact that good accuracy on smooth functions may not be directly relevant to our intended applications: option payoffs are typically nondifferentiable. Bally and Talay  $[34]$  show that the weak order of the Euler scheme holds for very general  $f$  and Yan [357] analyzes SDEs with irregular coefficients, but most of the literature requires significant smoothness assumptions.

U DISCRETIZATION Methods ۰.------------------------------------

When applying higher-order discretization methods, it is essential to test the methods numerically.

## 6.2 Second-Order Methods

We now proceed to further refine the Euler scheme to arrive at a method with weak order 2. The derivation follows the approach used in Section  $6.1.1$ , expanding the integrals of  $a(X(t))$  and  $b(X(t))$  to refine the Euler approximations in  $(6.4)$  and  $(6.5)$ , but now we keep more terms in the expansions. We begin by assuming that in the SDE  $(6.1)$  both X and W are scalar.

## 6.2.1 The Scalar Case

To keep the notation manageable, we adopt some convenient shorthand. With the scalar SDE  $(6.1)$  defining X, we associate the operators

$$\mathcal{L}^{0} = a \frac{d}{dx} + \frac{1}{2} b^{2} \frac{d^{2}}{dx^{2}} \tag{6.18}$$

and

$$\mathcal{L}^1 = b \frac{d}{dx},\tag{6.19}$$

meaning that for any twice differentiable  $f$ , we have

$$\mathcal{L}^{0}f(x) = a(x)f'(x) + \frac{1}{2}b^{2}(x)f''(x)$$

and

$$\mathcal{L}^1 f(x) = b(x)f'(x).$$

This allows us to write Itô's formula as

$$df(X(t)) = \mathcal{L}^0 f(X(t)) dt + \mathcal{L}^1 f(X(t)) dW(t). \tag{6.20}$$

To accommodate functions  $f(t, X(t))$  that depend explicitly on time, we would generalize  $(6.18)$  to

$$\mathcal{L}^{0} = \frac{\partial}{\partial t} + a \frac{\partial}{\partial x} + \frac{1}{2} b^{2} \frac{\partial^{2}}{\partial x^{2}}.$$

As in Section  $6.1.1$ , the key to deriving a discretization scheme lies in approximating the evolution of X over an interval  $[t, t+h]$ . We start from the representation

$$X(t+h) = X(t) + \int_{t}^{t+h} a(X(u)) \, du + \int_{t}^{t+h} b(X(u)) \, dW(u), \qquad (6.21)$$

and approximate each of the two integrals on the right.

The Euler scheme approximates the first integral using the approximation  $a(X(u)) \approx a(X(t))$  for  $u \in [t, t+h]$ . To derive a better approximation for  $a(X(u))$ , we start from the exact representation

$$a(X(u)) = a(X(t)) + \int_t^u \mathcal{L}^0 a(X(s)) \, ds + \int_t^u \mathcal{L}^1 a(X(s)) \, dW(s);$$

this is Itô's formula applied to  $a(X(u))$ . Next we apply the Euler approximation to each of the two integrals appearing in this representation; in other words, we set  $\mathcal{L}^0 a(X(s)) \approx \mathcal{L}^0 a(X(t))$  and  $\mathcal{L}^1 a(X(s)) \approx \mathcal{L}^1 a(X(t))$ for  $s \in [t, u]$  to get

$$a(X(u)) \approx a(X(t)) + \mathcal{L}^0 a(X(t)) \int_t^u ds + \mathcal{L}^1 a(X(t)) \int_t^u dW(s).$$

Now we use this approximation in the first integral in  $(6.21)$  to get

$$\int_{t}^{t+h} a(X(u)) du$$
  

$$\approx a(X(t))h + \mathcal{L}^{0}a(X(t)) \int_{t}^{t+h} \int_{t}^{u} ds \, du + \mathcal{L}^{1}a(X(t)) \int_{t}^{t+h} \int_{t}^{u} dW(s) \, du$$
  

$$\equiv a(X(t))h + \mathcal{L}^{0}a(X(t))I_{(0,0)} + \mathcal{L}^{1}a(X(t))I_{(1,0)}, \tag{6.22}$$

with  $I_{(0,0)}$  and  $I_{(1,0)}$  denoting the indicated double integrals. This gives us our approximation to the first term in integral in  $(6.21)$ .

We use corresponding steps for the second integral in  $(6.21)$ . We approximate the integrand  $b(X(u)), u \in [t, t+h]$  using

$$b(X(u)) = b(X(t)) + \int_t^u \mathcal{L}^0 b(X(s)) \, ds + \int_t^u \mathcal{L}^1 b(X(s)) \, dW(s)$$
  
$$\approx b(X(t)) + \mathcal{L}^0 b(X(t)) \int_t^u \, ds + \mathcal{L}^1 b(X(t)) \int_t^u \, dW(s)$$

and thus approximate the integral as

$$\begin{split} & \int_{t}^{t+h} b(X(u)) \, dW(u) \\ & \approx \ b(X(t))[W(t+h) - W(t)] + \mathcal{L}^{0}b(X(t)) \int_{t}^{t+h} \int_{t}^{u} ds \, dW(u) \\ & \quad + \mathcal{L}^{1}b(X(t)) \int_{t}^{t+h} \int_{t}^{u} dW(s) \, dW(u) \\ & \equiv \ b(X(t))[W(t+h) - W(t)] + \mathcal{L}^{0}b(X(t))I_{(0,1)} + \mathcal{L}^{1}b(X(t))I_{(1,1)}.\tag{6.23} \end{split}$$

Once again, the  $I_{(i,j)}$  denote the indicated double integrals.

If we combine  $(6.22)$  and  $(6.23)$  and make explicit the application of the operators  $\mathcal{L}^0$  and  $\mathcal{L}^1$  to a and b, we arrive at the approximation

$$X(t+h) \approx X(t) + ah + b\Delta W + (aa' + \frac{1}{2}b^2a'')I_{(0,0)} + (ab' + \frac{1}{2}b^2b'')I_{(0,1)} + ba'I_{(1,0)} + bb'I_{(1,1)}, \tag{6.24}$$

with  $\Delta W = W(t+h) - W(t)$ , and the functions a, b and their derivatives all evaluated at  $X(t)$ .

### The Discretization Scheme

To turn the approximation in  $(6.24)$  into an implementable algorithm, we need to be able to simulate the double integrals  $I_{(i,j)}$ . Clearly,

$$I_{(0,0)} = \int_{t}^{t+h} \int_{t}^{u} ds \, du = \frac{1}{2}h^{2}.$$

From  $(6.9)$  we know that

$$I_{(1,1)} = \int_{t}^{t+h} [W(u) - W(t)] \, dW(u) = \frac{1}{2} [(\Delta W)^2 - h].$$

The term  $I_{(0,1)}$  is

$$I_{(0,1)} = \int_{t}^{t+h} \int_{t}^{u} ds \, dW(u) = \int_{t}^{t+h} (u-t) \, dW(u)$$

Applying integration by parts (which can be justified by applying Itô's formula to  $tW(t)$ , we get

$$I_{(0,1)} = hW(t+h) - \int_{t}^{t+h} W(u) du$$
  
$$= h[W(t+h) - W(t)] - \int_{t}^{t+h} [W(u) - W(t)] du$$
  
$$= h\Delta W - I_{(1,0)}.$$
 (6.25)

So, it only remains to examine

$$I_{(1,0)} = \int_{t}^{t+h} [W(u) - W(t)] \, du.$$

Given  $W(t)$ , the area  $I_{(1,0)}$  and the increment  $\Delta W = W(t+h) - W(t)$ are jointly normal. Each has conditional mean 0; the conditional variance of  $\Delta W$  is h and that of  $I_{(1,0)}$  is  $h^3/3$  (see (3.48)). For their covariance, notice first that

$$\mathsf{E}[I_{(1,0)}|W(t),\Delta W] = \frac{1}{2}h\Delta W\tag{6.26}$$

(as illustrated in Figure 6.1), so  $\mathsf{E}[I_{(1,0)}\Delta W] = \frac{1}{2}h^2$ . We may therefore simulate  $W(t + h) - W(t)$  and  $I_{(1,0)}$  as

 $6.2$  Second-Order Methods  $351$ 

$$\begin{pmatrix} \Delta W \\ \Delta I \end{pmatrix} \sim N \left( 0, \begin{pmatrix} h & \frac{1}{2}h^2 \\ \frac{1}{2}h^2 & \frac{1}{3}h^3 \end{pmatrix} \right). \n$$
(6.27)

This leads to the following second-order scheme:

$$\hat{X}((i+1)h) = \hat{X}(ih) + ah + b\Delta W + (ab' + \frac{1}{2}b^2b'')[\Delta Wh - \Delta I] \n+ a'b\Delta I + \frac{1}{2}bb'[\Delta W^2 - h] \n+ (aa' + \frac{1}{2}b^2a'')\frac{1}{2}h^2,\n$$
(6.28)

with the functions a, b and their derivatives all evaluated at  $\hat{X}(ih)$ .

![](_page_12_Figure_5.jpeg)

**Fig. 6.1.** The shaded area is  $\Delta I$ . Given  $W(t)$  and  $W(t+h)$ , the conditional expectation of  $W$  at any intermediate time lies on the straight line connecting these endpoints. The conditional expectation of  $\Delta I$  is given by the area of the triangle with base h and height  $\Delta W = W(t+h) - W(t)$ .

This method was introduced by Milstein [267] in a slightly different form.  $\text{Talay}$  [341] shows that Milstein's scheme has weak order 2 under conditions on the coefficient functions  $a$  and  $b$ . These conditions include the requirement that the functions  $a$  and  $b$  be six times continuously differentiable with uniformly bounded derivatives. The result continues to hold if  $\Delta I$  is replaced by its conditional expectation  $\Delta Wh/2$ ; this type of simplification becomes essential in the vector case, as we explain in the next section.

Implementation of  $(6.28)$  and similar methods requires calculation of the derivatives of the coefficient functions of a diffusion. Methods that use difference approximations to avoid derivative calculations without a loss in convergence order are developed in Milstein [267] and Talay [341]. These types of approximations are called Runge-Kutta methods in analogy with methods used in the numerical solution of ordinary differential equations.

## 6.2.2 The Vector Case

We now extend the scheme in  $(6.28)$  to d-dimensional X driven by mdimensional  $W$ . Much as in the scalar case, we start from the representation

n Luscretization Methods აე∠

$$X_i(t+h) = X_i(t) + \int_t^{t+h} a_i(u) \, du + \sum_{k=1}^m \int_t^{t+h} b_{ik}(u) \, dW_k(u), \quad i = 1, \dots, d,$$

and approximate each of the integrals on the right. In this setting, the relevant operators are

$$\mathcal{L}^{0} = \frac{\partial}{\partial t} + \sum_{i=1}^{d} a_{i} \frac{\partial}{\partial x_{i}} + \frac{1}{2} \sum_{i,j=1}^{d} \sum_{k=1}^{m} b_{ik} b_{jk} \frac{\partial^{2}}{\partial x_{i} \partial x_{j}} \tag{6.29}$$

and it as special states in agent

and

$$\mathcal{L}^{k} = \sum_{i=1}^{d} b_{ik} \frac{\partial}{\partial x_{i}}, \quad k = 1, \dots, m. \tag{6.30}$$

The multidimensional Itô formula for twice continuously differentiable  $f$  :  $\Re^d \to \Re$  becomes

$$df(X(t)) = \mathcal{L}^{0}f(X(t)) dt + \sum_{k=1}^{m} \mathcal{L}^{k}f(X(t)) dW_{k}(t).$$
(6.31)

Applying  $(6.31)$  to  $a_i$ , we get

$$a_i(X(u)) = a_i(X(t)) + \int_t^u \mathcal{L}^0 a_i(X(s)) \, ds + \sum_{k=1}^m \int_t^u \mathcal{L}^k a_i(X(s)) \, dW_k(s).$$

The same steps leading to the approximation  $(6.22)$  in the scalar case now yield the approximation

$$\int_{t}^{t+h} a_i(X(u)) du \approx a_i(X(t))h + \mathcal{L}^0 a_i(X(t))I_{(0,0)} + \sum_{k=1}^m \mathcal{L}^k a_i(X(t))I_{(k,0)},$$

with

$$I_{(k,0)} = \int_{t}^{t+h} \int_{t}^{u} dW_{k}(s) du, \quad k = 1, \ldots, m.$$

Similarly, the representation

$$b_{ik}(X(u)) = b_{ik}(X(t)) + \int_t^u \mathcal{L}^0 b_{ik}(X(s)) \, ds + \sum_{j=1}^m \int_t^u \mathcal{L}^j b_{ik}(X(s)) \, dW_j(s),$$

leads to the approximation

$$\int_{t}^{t+h} b_{ik}(X(u)) \, dW_k(u)$$
  
 
$$\approx b_{ik}(X(t))h + \mathcal{L}^0 b_{ik}(X(t))I_{(0,k)} + \sum_{j=1}^m \mathcal{L}^j b_{ik}(X(t))I_{(j,k)}$$

with

$$I_{(0,k)} = \int_{t}^{t+h} \int_{t}^{u} ds \, dW_k(u), \quad k = 1, \dots, m,$$

and

$$I_{(j,k)} = \int_{t}^{t+h} \int_{t}^{u} dW_{j}(u) dW_{k}(u), \quad j,k = 1,\ldots,m$$

The notational convention for these integrals should be evident: in  $I_{(j,k)}$ we integrate first over  $W_j$  and then over  $W_k$ . This interpretation extends to  $j=0$  if we set  $W_0(t)\equiv t$ .

By combining the expansions above for the integrals of  $a_i$  and  $b_{ik}$ , we arrive at the discretization

$$\begin{split}\n\hat{X}_i(t+h) &= \hat{X}_i(t) + a_i(\hat{X}(t))h + \sum_{k=1}^m b_{ik}(\hat{X}(t))\Delta W_k \\
&\quad + \frac{1}{2}\mathcal{L}^0 a_i(\hat{X}(t))h^2 + \sum_{k=1}^m \mathcal{L}^k a_i(\hat{X}(t))I_{(k,0)} \\
&\quad + \sum_{k=1}^m \left(\mathcal{L}^0 b_{ik}(\hat{X}(t))I_{(0,k)} + \sum_{j=1}^m \mathcal{L}^j b_{ik}(\hat{X}(t))I_{(j,k)}\right), \tag{6.32}\n\end{split}$$

for each  $i = 1, \ldots, d$ . Here we have substituted  $h^2/2$  for  $I_{(0,0)}$  and abbreviated  $W_k(t+h) - W_k(t)$  as  $\Delta W_k$ . The application of each of the operators  $\mathcal{L}^j$  to any of the coefficient functions  $a_i$ ,  $b_{ik}$  produces a polynomial in the coefficient functions and their derivatives; these expressions can be made explicit using  $(6.29)$  and  $(6.30)$ . Using the identity

$$I_{(0,j)} + I_{(j,0)} = \Delta W_j h,$$

which follows from (6.25), we could rewrite all terms involving  $I_{(0,j)}$  as multiples of  $(\Delta W_j h - I_{(j,0)})$  instead. Thus, to implement (6.32) we need to sample, for each  $j = 1, \ldots, m$ , the Brownian increments  $\Delta W_j$  together with the integrals  $I_{(i,0)}$  and  $I_{(i,k)}, k = 1, \ldots, m$ . We address this issue next.

## Commutativity Condition

As noted in Section 6.1.1, the mixed Brownian integrals  $I_{(j,k)}$  with  $j \neq k$  are difficult to simulate, so  $(6.32)$  does not provide a practical algorithm without further simplification. Simulation of the mixed integrals is obviated in models satisfying the *commutativity condition* 

$$\mathcal{L}^k b_{ij} = \mathcal{L}^j b_{ik} \tag{6.33}$$

for all  $i = 1, \ldots, d$ . This is a rather artificial condition and is not often satisfied in practice, but it provides an interesting simplification of the second-order approximation.

÷.

When  $(6.33)$  holds, we may group terms in  $(6.32)$  involving mixed integrals  $I_{(j,k)}, j,k \geq 1$ , and write them as

$$\sum_{j=1}^{m} \sum_{k=1}^{m} \mathcal{L}^{j} b_{ik} I_{(j,k)} = \sum_{j=1}^{m} \mathcal{L}^{j} b_{ij} I_{(j,j)} + \sum_{j=1}^{m} \sum_{k=j+1}^{m} \mathcal{L}^{j} b_{ik} (I_{(j,k)} + I_{(k,j)}).$$

As in the scalar case (6.9), the diagonal term  $I_{(j,j)}$  evaluates to  $(\Delta W_i^2 - h)/2$ and is thus easy to simulate. The utility of the commutativity condition lies in the observation that even though each  $I_{(j,k)}, j \neq k$ , is difficult to simulate, the required sums simplify to

$$I_{(j,k)} + I_{(k,j)} = \Delta W_j \Delta W_k. \tag{6.34}$$

with paragraphic and the same and the same and

This follows from applying Itô's formula to  $W_i(t)W_k(t)$  to get

$$W_j(t+h)W_k(t+h) - W_j(t)W_k(t) = \int_t^{t+h} W_k(u) \, dW_j(u) + \int_t^{t+h} W_j(u) \, dW_k(u)$$

and then subtracting  $W_k(t)\Delta W_i + W_i(t)\Delta W_k$  from both sides.

When the commutativity condition is satisfied, the discretization scheme  $(6.32)$  thus simplifies to

$$\begin{split}\n\hat{X}_{i}(t+h) &= \hat{X}_{i}(t) + a_{i}(\hat{X}(t))h + \sum_{k=1}^{m} b_{ik}(\hat{X}(t))\Delta W_{k} + \frac{1}{2}\mathcal{L}^{0}a_{i}(\hat{X}(t))h^{2} \\
&+ \sum_{k=1}^{m} \left( \left[ \mathcal{L}^{k}a_{i}(\hat{X}(t)) - \mathcal{L}^{0}b_{ik}(\hat{X}(t)) \right] \Delta I_{k} + \mathcal{L}^{0}b_{ik}(\hat{X}(t))\Delta W_{k}h \right) \\
&+ \sum_{j=1}^{m} \left( \mathcal{L}^{j}b_{ij}(\hat{X}(t))\frac{1}{2}(\Delta W_{j}^{2} - h) + \sum_{k=j+1}^{m} \mathcal{L}^{j}b_{ik}(\hat{X}(t))\Delta W_{j}\Delta W_{k} \right), \tag{6.35}\n\end{split}$$

with  $\Delta I_k = I_{(k,0)}$ . Because the components of W are independent of each other, the pairs  $(\Delta W_k, \Delta I_k)$ ,  $k = 1, \ldots, m$ , are independent of each other. Each such pair has the bivariate normal distribution identified in  $(6.27)$  and is thus easy to simulate.

**Example 6.2.1** LIBOR Market Model. As an illustration of the commutativity condition  $(6.33)$ , we consider the LIBOR market model of Section 3.7. Thus, take  $X_i$  to be the *i*th forward rate  $L_i$  in the spot measure dynamics in  $(3.112)$ . This specifies that the evolution of  $L_i$  is governed by an SDE of the  $\text{form}$ 

$$dL_i(t) = L_i(t)\mu_i(L(t),t) dt + L_i(t)\sigma_i(t)^+ dW(t),$$

with, for example,  $\sigma_i$  a deterministic function of time. In the notation of this section,  $b_{ij} = L_i \sigma_{ij}$ . The commutativity condition (6.33) requires

$$\sum_{r=1}^{d} b_{rk} \frac{\partial b_{ij}}{\partial x_r} = \sum_{r=1}^{d} b_{rj} \frac{\partial b_{ik}}{\partial x_r},$$

and this is satisfied because both sides evaluate to  $\sigma_{ij}\sigma_{ik}L_i$ . More generally, the commutativity condition is satisfied whenever  $b_{ij}(X(t))$  factors as the product of a function of  $X_i(t)$  and a deterministic function of time.

If we set  $X_i(t) = \log L_i(t)$  then X solves an SDE of the form

$$dX_i(t) = \left(\mu_i(X(t), t) - \frac{1}{2} \|\sigma_i(t)\|^2\right) dt + \sigma_i(t)^\top dW(t).$$

In this case,  $b_{ij} = \sigma_{ij}$  does not depend on X at all so the commutativity condition is automatically satisfied.  $\Box$ 

## A Simplified Scheme

Even when the commutativity condition fails, the discretization method  $(6.32)$ can be simplified for practical implementation. Talay  $[340]$  and Kloeden and Platen [211,  $p.465$ ] show that the scheme continues to have weak order 2 if each  $\Delta I_j$  is replaced with  $\frac{1}{2}\Delta W_j h$ . (Related simplifications are used in Milstein [267] and Talay [341].) Observe from (6.26) that this amounts to replacing  $\Delta I_j$ with its conditional expectation given  $\Delta W_j$ . As a consequence,  $\frac{1}{2}\Delta W_j h$  has the same covariance with  $\Delta W_j$  as  $\Delta I_j$  does:

$$\mathsf{E}[\Delta W_j \cdot \frac{1}{2} \Delta W_j h] = \frac{1}{2} h \mathsf{E}[\Delta W_j^2] = \frac{1}{2} h^2.$$

It also has the same mean as  $\Delta I_j$  but variance  $h^3/4$  rather than  $h^3/3$ , an error of  $O(h^3)$ . This turns out to be close enough to preserve the order of convergence. In the scalar case  $(6.28)$ , the simplified scheme is

$$\begin{split}\n\ddot{X}(n+1) &= \ddot{X}(n) + ah + b\Delta W \\
&+ \frac{1}{2}(a'b + ab' + \frac{1}{2}b^2b'')\Delta Wh + \frac{1}{2}bb'[\Delta W^2 - h] \\
&+ (aa' + \frac{1}{2}b^2a'')\frac{1}{2}h^2,\n\end{split} \tag{6.36}$$

with a, b, and their derivatives evaluated at  $X(n)$ .

In the vector case, the simplified scheme replaces the double integrals in  $(6.32)$  with simpler random variables. As in the scalar case,  $I_{(0,k)}$  and  $I_{(k,0)}$ are approximated by  $\Delta W_k h/2$ . Each  $I_{(j,j)}, j \neq 0$ , evaluates to  $(\Delta W_j^2 - h)/2$ . For  $j, k$  different from zero and from each other,  $I_{(j,k)}$  is approximated by (Talay [341], Kloeden and Platen [211], Section  $14.2$ )

$$\frac{1}{2}(\Delta W_j \Delta W_k - V_{jk}),\tag{6.37}$$

with  $V_{kj} = -V_{jk}$ , and the  $V_{jk}, j < k$ , independent random variables taking values h and  $-h$  each with probability 1/2. Let  $V_{jj} = h$ . The resulting approximation is, for each coordinate  $i = 1, \ldots, d$ ,

$$\begin{split}\n\ddot{X}_{i}(n+1) &= \\
\dot{X}_{i}(n+1) &= \\
\dot{X}_{i}(n) + a_{i}h + \sum_{k=1}^{m} b_{ik}\Delta W_{k} + \frac{1}{2}\mathcal{L}^{0}a_{i}h^{2} + \frac{1}{2}\sum_{k=1}^{m} \left(\mathcal{L}^{k}a_{i} + \mathcal{L}^{0}b_{ik}\right)\Delta W_{k}h \\
&+ \frac{1}{2}\sum_{k=1}^{m}\sum_{j=1}^{m}\mathcal{L}^{j}b_{ik}\left(\Delta W_{j}\Delta W_{k} - V_{jk}\right),\n\end{split} \tag{6.38}$$

with all  $a_i$ ,  $b_{ij}$ , and their derivatives evaluated at  $\hat{X}(n)$ .

In these simplified schemes, the  $\Delta W$  can be replaced with other random variables  $\widehat{\Delta W}$  with moments up to order 5 that are within  $O(h^3)$  of those of  $\Delta W$ . (See the discussion following (6.17) and, for precise results Kloeden and Platen [211, p.465] and Talay [341, 342].) This includes the three-point distributions

$$P(\widehat{\Delta W} = \pm \sqrt{3h}) = \frac{1}{6}, \quad P(\widehat{\Delta W} = 0) = \frac{2}{3}$$

These are faster to generate, but using normally distributed  $\Delta W$  will generally result in smaller bias. The justification for using  $(6.37)$  also lies in the fact that these simpler random variables have moments up to order five that are within  $O(h^3)$  of those of the  $I_{(i,k)}$ ; see Section 5.12 of Kloeden and Platen [211, p.465], Section 1.6 of Talay [341], or Section 5 of Talay [342]. Talay [341, 342] calls these "Monte Carlo equivalent" families of random variables.

**Example 6.2.2** Stochastic volatility model. In Section 3.4, we noted that the square-root diffusion is sometimes used to model stochastic volatility. Heston's  $[179]$  model is

$$dS(t) = rS(t) dt + \sqrt{V(t)}S(t) dW_1(t)$$
  

$$dV(t) = \kappa(\theta - V(t)) dt + \sqrt{V(t)}(\sigma_1 dW_1(t) + \sigma_2 dW_2(t)),$$

with S interpreted as, e.g., a stock price. The Brownian motions  $W_1$  and  $W_2$ are independent of each other. Heston  $[179]$  derives a formula for option prices in this setting using Fourier transform inversion. This provides a benchmark against which to compare simulation methods.

The simplified second-order scheme  $(6.38)$  for this model is as follows:

$$\begin{split} \hat{S}(i+1) &= \hat{S}(i)(1+rh+\sqrt{\hat{V}(i)}\Delta W_1) + \frac{1}{2}r^2\hat{S}(i)h^2 \\ &+ \left( \left[ r + \frac{\sigma_1 - \kappa}{4} \right] \hat{S}(i)\sqrt{\hat{V}(i)} + \left[ \frac{\kappa\theta}{4} - \frac{\sigma^2}{16} \right] \frac{\hat{S}(i)}{\sqrt{\hat{V}(i)}} \right) \Delta W_1 h \\ &+ \frac{1}{2}\hat{S}(i)(\hat{V}(i) + \frac{\sigma_1}{2})(\Delta W_1^2 - h) + \frac{1}{4}\sigma_2 \hat{S}(i)(\Delta W_2 \Delta W_1 + \xi) \end{split}$$

and

$$\begin{split} &V(i+1) = \\ &\kappa\theta h + (1-\kappa h)\hat{V}(i) + \sqrt{\hat{V}(i)}(\sigma_1\Delta W_1 + \sigma_2\Delta W_2) - \frac{1}{2}\kappa^2(\theta - \hat{V}(i))h^2 \\ &+ \left(\left[\frac{\kappa\theta}{4} - \frac{\sigma^2}{16}\right]\frac{1}{\sqrt{\hat{V}(i)}} - \frac{3\kappa}{2}\sqrt{\hat{V}(i)}\right)(\sigma_1\Delta W_1 + \sigma_2\Delta W_2)h \\ &+ \frac{1}{4}\sigma_1^2(\Delta W_1^2 - h) + \frac{1}{4}\sigma_2^2(\Delta W_2^2 - h) + \frac{1}{2}\sigma_1\sigma_2\Delta W_1\Delta W_2, \end{split}$$

with  $\sigma^2 = \sigma_1^2 + \sigma_2^2$  and  $\xi$  taking the values h and  $-h$  with probability  $1/2$ independent of the Brownian increments. To avoid taking the square root of a negative number or dividing by zero, we replace  $V(i)$  by its absolute value before advancing these recursions.

Figure 6.2 displays numerical results using this scheme and a simple Euler approximation. We use parameters  $S(0) = 100, V(0) = 0.04, r = 5\%, \kappa = 1.2,$  $\theta = 0.04, \sigma = 0.30, \text{ and } \sigma_1 = \rho \sigma \text{ with } \rho = -0.5. \text{ Using Heston's [179] formula,}$ the expectation  $E[e^{-rT}(S(T)-K)^{+}]$  with  $T=1$  and  $K=100$  evaluates to 10.3009. We compare our simulation results against this value to estimate bias. We use simulation time step  $h = T/n$ , with  $n = 3, 6, 12, 25, \text{ and } 100$ and run 2–4 million replications at each  $n$  for each method.

Figure 6.2 plots the estimated log absolute bias against  $\log n$ . The bias in the Euler scheme for this example falls below 0.01 at  $n = 25$  steps per year, whereas the second-order method has a bias this small even at  $n=3$ steps per year. As  $n$  increases, the results for the Euler scheme look roughly consistent with first-order convergence; the second-order method produces smaller estimated biases but its convergence is much more erratic. In fact our use of  $(6.38)$  for this problem lacks theoretical support because the square-root functions in the model dynamics and the kink in the call option payoff violate the smoothness conditions required to ensure second-order convergence. The more regular convergence displayed by the Euler scheme in this example lends itself to the extrapolation method in Section  $6.2.4$ .

## 6.2.3 Incorporating Path-Dependence

The error criterion in (6.14) applies to expectations of the form  $\mathsf{E}[f(X(T))]$ with T fixed. Accurate estimation of  $E[f(X(T))]$  requires accurate approximation only of the distribution of  $X(T)$ . In many pricing problems, however, we are interested not only in the terminal state of an underlying process, but also in the path by which the terminal state is reached. The error criterion  $(6.14)$  does not appear to offer any guarantees on the approximation error in simulating functions of the path, raising the question of whether properties of the Euler and higher-order schemes extend to such functions.

One way to extend the framework of the previous sections to pathdependent quantities is to transform dependence on the past into dependence on supplementary state variables. This section illustrates this idea.

![](_page_19_Figure_2.jpeg)

Fig. 6.2. Estimated bias versus number of steps in discretization of a stochastic volatility model.

Suppose we want to compute a bond price

$$\mathsf{E}\left[\exp\left(-\int_{0}^{T}r(t)\,dt\right)\right] \tag{6.39}$$

with the (risk-neutral) dynamics of the short rate  $r$  described by the scalar  $SDE$ 

$$dr(t) = \mu(r(t)) dt + \sigma(r(t)) dW(t).$$

If we simulate some discretization  $\hat{r}(i) = \hat{r}(ih), i = 0, 1, \ldots, n-1$  with time step  $h = T/n$ , the simplest estimate of the bond price would be

$$\exp\left(-h\sum_{i=0}^{n-1}\hat{r}(i)\right). \tag{6.40}$$

An alternative introduces the variable

$$D(t) = \exp\left(-\int_0^t r(u) \, du\right),\,$$

develops a discretization scheme for the bivariate diffusion

$$d\begin{pmatrix}r(t)\\D(t)\end{pmatrix} = \begin{pmatrix}\mu(r(t))\\-r(t)D(t)\end{pmatrix}dt + \begin{pmatrix}\sigma(r(t))\\0\end{pmatrix}dW(t),\tag{6.41}$$

and uses  $\ddot{D}(nh)$  as an estimate of the bond price (6.39). In (6.41), the driving Brownian motion is still one-dimensional, so we have not really made the problem any more difficult by enlarging the state vector. The difficulties addressed in Section 6.2.2 arise when  $W$  is vector-valued.

The Euler scheme for the bivariate diffusion is

$$\hat{r}(i+1) = \hat{r}(i) + \mu(\hat{r}(i))h + \sigma(\hat{r}(i))\Delta W$$
  
$$\hat{D}(i+1) = \hat{D}(i) - \hat{r}(i)\hat{D}(i)h.$$

Because of the smoothness of the coefficients of the SDE for  $D(t)$ , this discretization inherits whatever order of convergence the coefficients  $\mu$  and  $\sigma$ ensure for  $\hat{r}$ . Beyond this guarantee, the bivariate formulation offers no clear advantage for the Euler scheme compared to simply using  $(6.40)$ . Indeed, if we apply the Euler scheme to  $\log D(t)$  rather than  $D(t)$ , we recover (6.40) exactly.

But we do find a difference when we apply a second-order discretization. The simplified second-order scheme for a generic bivariate diffusion  $X$  driven by a scalar Brownian motion has the form

$$\begin{split} \begin{pmatrix} \hat{X}_1(i+1) \\ \hat{X}_2(i+1) \end{pmatrix} &= \text{Euler terms} + \frac{1}{2} \begin{pmatrix} \mathcal{L}^0 a_1(\hat{X}(i)) \\ \mathcal{L}^0 a_2(\hat{X}(i)) \end{pmatrix} h^2 \\ &+ \frac{1}{2} \begin{pmatrix} \mathcal{L}^1 b_1(\hat{X}(i)) \\ \mathcal{L}^1 b_2(\hat{X}(i)) \end{pmatrix} (\Delta W^2 - h) + \frac{1}{2} \begin{pmatrix} \mathcal{L}^1 a_1(\hat{X}(i)) + \mathcal{L}^0 b_1(\hat{X}(i)) \\ \mathcal{L}^1 a_2(\hat{X}(i)) + \mathcal{L}^0 b_2(\hat{X}(i)) \end{pmatrix} \Delta W h \end{split}$$

with

$$\mathcal{L}^{0} = a_1 \frac{\partial}{\partial x_1} + a_2 \frac{\partial}{\partial x_2} + \frac{1}{2} \left( b_1^2 \frac{\partial^2}{\partial x_1^2} + 2b_1 b_2 \frac{\partial^2}{\partial x_1 x_2} + b_2^2 \frac{\partial^2}{\partial x_2^2} \right)$$

 $\text{and}$ 

$$\mathcal{L}^1 = b_1 \frac{\partial}{\partial x_1} + b_2 \frac{\partial}{\partial x_2}.$$

When specialized to the bond-pricing setting, this discretizes  $r(t)$  as

$$\begin{split} \hat{r}(i+1) &= \hat{r}(i) + \mu h + \sigma \Delta W + \frac{1}{2}\sigma \sigma' [\Delta W^2 - h] \\ &+ \frac{1}{2}(\sigma \mu' + \mu \sigma' + \frac{1}{2}\sigma^2 \sigma'') \Delta W h + \frac{1}{2}(\mu' \mu + \frac{1}{2}\sigma^2 \mu'') h^2 \end{split}$$

with  $\mu$ ,  $\sigma$  and their derivatives on the right evaluated at  $\hat{r}(i)$ . This is exactly the same as the scheme for  $r(t)$  alone. But in discretizing  $D(t)$ , we get

$$\mathcal{L}^1(-r(t)D(t)) = -\sigma(r(t))D(t)$$

and

$$\mathcal{L}^{0}(-r(t)D(t)) = -\mu(r(t))D(t) + r(t)^{2}D(t).$$

Hence, the scheme becomes

$$\hat{D}(i+1) = \hat{D}(i) \left(1 - \hat{r}(i)h + \frac{1}{2}[\hat{r}(i)^2 - \mu(\hat{r}(i))]h^2 - \frac{1}{2}\sigma(\hat{r}(i))\Delta Wh\right),\,$$

which involves terms not reflected in  $(6.40)$ .

Again because of the smoothness of the coefficients for  $D(t)$ , this method has weak order 2 if the scheme for  $r(t)$  itself achieves this order. Thus, the weak error criterion extends to the bond price  $(6.39)$ , though it would not necessarily extend if we applied the crude discretization in  $(6.40)$ .

The same idea clearly applies in computing a function of, e.g.,

$$\left(X(T), \int_0^T X(t) \, dt\right),$$

as might be required in pricing an Asian option. In contrast, incorporating path-dependence through the maximum or minimum of a process (to price a barrier or lookback option, for example) is more delicate. We can define a supplementary variable of the form

$$M(t) = \max_{0 \le s \le t} X(t)$$

to remove dependence on the past of  $X$ , but the method applied above with the discount factor  $D(t)$  does not extend to the bivariate process  $(X(t), M(t))$ . The difficulty lies in the fact that the running maximum  $M(t)$  does not satisfy an SDE with smooth coefficients. For example,  $M$  remains constant except when  $X(t) = M(t)$ . Asmussen, Glynn, and Pitman [24] show that even when  $X$  is ordinary Brownian motion (so that the Euler scheme for  $X$  is exact), the Euler scheme for M has weak order  $1/2$  rather than the weak order 1 associated with smooth coefficient functions. We return to the problem of discretizing the running maximum in Section 6.4.

## 6.2.4 Extrapolation

An alternative approach to achieving second-order accuracy applies *Richard*son extrapolation (also called Romberg extrapolation) to two estimates obtained from a first-order scheme at two different levels of discretization. This is easier to implement than a second-order scheme and usually achieves roughly the same accuracy — sometimes better, sometimes worse. The same idea can (under appropriate conditions) boost the order of convergence of a secondorder or even higher-order scheme, but these extensions are not as effective in practice.

To emphasize the magnitude of the time increment, we write  $\hat{X}^h$  for a discretized process with step size h. We write  $\hat{X}^h(T)$  for the state of the discretized process at time T; more explicitly, this is  $\hat{X}^h(|T/h|h)$ .

As discussed in Section  $6.1.2$ , the Euler scheme often has weak order 1, in which case

$$|\mathsf{E}[f(\ddot{X}^h(T))] - \mathsf{E}[f(X(T))]| \le Ch \tag{6.42}$$

for some constant  $C$ , for all sufficiently small  $h$ , for suitable  $f$ . Talay and Tubaro [343], Bally and Talay [34], and Protter and Talay [301] prove that the bound in  $(6.42)$  can often be strengthened to an equality of the form

 $6.2$  Second-Order Methods 361

$$\mathsf{E}[f(\hat{X}^h(T))] = \mathsf{E}[f(X(T))] + ch + o(h),$$

for some constant  $c$  depending on  $f$ . In this case, the discretization with time step  $2h$  satisfies

$$\mathsf{E}[f(\hat{X}^{2h}(T))] = \mathsf{E}[f(X(T))] + 2ch + o(h),$$

with the same constant  $c$ .

By combining the approximations with time steps  $h$  and  $2h$ , we can eliminate the leading error term. More explicitly, from the previous two equations  $we get$ 

$$2\mathsf{E}[f(\hat{X}^h(T))] - \mathsf{E}[f(\hat{X}^{2h}(T))] = \mathsf{E}[f(X(T))] + o(h). \tag{6.43}$$

This suggests the following algorithm: simulate with time step  $h$  to estimate  $\mathsf{E}[f(\hat{X}^h(T))]$ ; simulate with time step 2h to estimate  $\mathsf{E}[f(\hat{X}^{2h}(T))]$ ; double the first estimate and subtract the second to estimate  $\mathsf{E}[f(X(T))]$ . The bias in this combined estimate is of smaller order than the bias in either of its two components.

Talay and Tubaro [343] and Protter and Talay [301] give conditions under which the  $o(h)$  term in (6.43) is actually  $O(h^2)$  (and indeed under which the error can be expanded in arbitrarily high powers of  $h$ ). This means that applying extrapolation to the Euler scheme produces an estimate with weak order 2. Because the Euler scheme is easy to implement, this offers an attractive alternative to the second-order schemes derived in Sections  $6.2.1$  and  $6.2.2$ .

The variance of the extrapolated estimate is typically reduced if we use consistent Brownian increments in simulating paths of  $\hat{X}^h$  and  $\hat{X}^{2h}$ . Each Brownian increment driving  $\hat{X}^{2h}$  is the sum of two of the increments driving  $\hat{X}^h$ . If we use  $\sqrt{h}Z_1, \sqrt{h}Z_2, \ldots$  as Brownian increments for  $\hat{X}^h$ , we should use  $\sqrt{h}(Z_1+Z_2), \sqrt{h}(Z_3+Z_4), \ldots$  as Brownian increments for  $\hat{X}^{2h}$ . Whether or not we use this construction (as opposed to, e.g., simulating the two independently) has no bearing on the validity of  $(6.43)$  because  $(6.43)$  refers only to expectations and is unaffected by any dependence between  $\hat{X}^h$  and  $\hat{X}^{2h}$ . Observe, however, that

$$\begin{split} \mathsf{Var}\left[2f(\hat{X}^h(T)) - f(\hat{X}^{2h}(T))\right] &= 4\mathsf{Var}\left[f(\hat{X}^h(T))\right] + \mathsf{Var}\left[f(\hat{X}^{2h}(T))\right] \\ &-4\mathsf{Cov}\left[f(\hat{X}^h(T)), f(\hat{X}^{2h}(T))\right]. \end{split}$$

Making  $f(\hat{X}^h(T))$  and  $f(\hat{X}^{2h}(T))$  positively correlated will therefore reduce variance, even though it has no effect on discretization bias. Using consistent Brownian increments will not always produce positive correlation, but it often will. Positive correlation can be guaranteed through monotonicity conditions, for example. This issue is closely related to the effectiveness of antithetic sampling; see Section 4.2, especially the discussion surrounding  $(4.29)$ .

Extrapolation can theoretically be applied to a second-order scheme to further increase the order of convergence. Suppose that we start from a scheme

having weak order 2, such as the simplified scheme  $(6.36)$  or  $(6.38)$ . Suppose that in fact

$$\mathsf{E}[f(\hat{X}^h(T))] = \mathsf{E}[f(X(T))] + ch^2 + o(h^2).$$

Then

$$\begin{split} &\frac{1}{3}(4\mathsf{E}[f(\hat{X}^h(T))] - E[f(\hat{X}^{2h}(T))]) \\ &= \frac{1}{3}(\{4\mathsf{E}[f(X(T))] + 4ch^2 + o(h^2)\} - \{\mathsf{E}[f(X(T))] + 4ch^2 + o(h^2)\}) \\ &= \mathsf{E}[f(X(T))] + o(h^2). \end{split}$$

If the  $o(h^2)$  error is in fact  $O(h^3)$ , then the combination

$$\frac{1}{21}(32\mathsf{E}[f(\hat{X}^h(T))] - 12\mathsf{E}[f(\hat{X}^{2h}(T))] + \mathsf{E}[f(\hat{X}^{4h}(T))])$$

eliminates that term too. Notice that the correct weights to apply to  $\hat{X}^h$ ,  $\hat{X}^{2h}$ , and any other discretization depend on the weak order of convergence of the scheme used.

## 6.3 Extensions

## 6.3.1 General Expansions

The derivations leading to the strong first-order scheme  $(6.10)$  and the weak second-order schemes  $(6.28)$  and  $(6.32)$  generalize to produce approximations that are, in theory, of arbitrarily high weak or strong order, under conditions on the coefficient functions. These higher-order methods can be cumbersome to implement and are of questionable practical significance; but they are of considerable theoretical interest and help underscore a distinction between weak and strong approximations.

We consider a d-dimensional process X driven by an  $m$ -dimensional standard Brownian motion  $W$  through an SDE of the form

$$dX(t) = b_0(X(t)) dt + \sum_{j=1}^d b_j(X(t))^\top dW(t).$$

We have written the drift coefficient as  $b_0$  rather than a to allow more compact notation in the expansions that follow. Let  $\mathcal{L}^0$  be as in (6.29) but with  $a_i$ replaced by  $b_{0i}$  and let  $\mathcal{L}^k$  be as in (6.30),  $k = 1, \ldots, m$ .

For any  $n = 1, 2, \ldots$ , and any  $j_1, j_2, \ldots, j_n \in \{0, 1, \ldots, m\}$ , define the multiple integrals

$$I_{(j_1,j_2,\ldots,j_n)} = \int_t^{t+h} \cdots \int_t^{u_3} \int_t^{u_2} dW_{j_1}(u_1) dW_{j_2}(u_2) \cdots dW_{j_n}(u_n),$$

with the convention that  $dW_0(u) = du$ . These integrals generalize those used in Section 6.2.2. Here, t and h are arbitrary positive numbers; as in Section 6.2.2, our objective is to approximate an arbitrary increment from  $X(t)$ to  $X(t+h)$ .

The general weak expansion of order  $\beta = 1, 2, \ldots$  takes the form

$$X(t+h) \approx X(t) + \sum_{n=1}^{\beta} \sum_{j_1,\ldots,j_n} \mathcal{L}^{j_1} \cdots \mathcal{L}^{j_{n-1}} b_{j_n} I_{(j_1,\ldots,j_n)}, \tag{6.44}$$

with each  $j_i$  ranging over  $0, 1, \ldots, m$ . (This approximation applies to each coordinate of the vectors X and  $b_{i_n}$ .) When  $\beta = 2$ , this reduces to the secondorder scheme in  $(6.32)$ . Kloeden and Platen [211] (Section 14.5) justify the general case and provide conditions under which this approximation produces a scheme with weak order  $\beta$ .

In contrast to (6.44), the general strong expansion of order  $\beta = 1/2, 1$ ,  $3/2, \ldots$  takes the form (Kloeden and Platen [211], Section 14.5)

$$X(t+h) \approx X(t) + \sum_{(j_1,\ldots,j_n)\in\mathcal{A}_{\beta}} \mathcal{L}^{j_1}\cdots\mathcal{L}^{j_{n-1}}b_{j_n}I_{(j_1,\ldots,j_n)}.$$
 (6.45)

The set  $\mathcal{A}_{\beta}$  is defined as follows. A vector of indices  $(j_1,\ldots,j_n)$  is in  $\mathcal{A}_{\beta}$  if either (i) the number of indices  $n$  plus the number of indices that are 0 is less than or equal to  $2\beta$ , or (ii)  $n = \beta + \frac{1}{2}$  and all n indices are 0. Thus, when  $\beta = 1$ , the weak expansion sums over  $j = 0$  and  $j = 1$  (the Euler scheme), whereas the strong expansion sums over  $j = 0, j = 1, \text{ and } (j_1, j_2) = (1, 1)$  to get  $(6.10)$ . Kloeden and Platen [211], Section 10.6, show that  $(6.45)$  indeed results in an approximation with strong order  $\beta$ .

Both expansions  $(6.44)$  and  $(6.45)$  follow from repeated application of the steps we used in  $(6.7)$  and  $(6.22)$ – $(6.23)$ . The distinction between the two expansions can be summarized as follows: the weak expansion treats terms  $\Delta W_j, j \neq 0$ , as having the same order as h, whereas the strong expansion treats them as having order  $h^{1/2}$ . Thus, indices equal to zero (corresponding to "dt" terms rather than " $dW_i$ " terms) count double in reckoning the number of terms to include in the strong expansion  $(6.45)$ .

## 6.3.2 Jump-Diffusion Processes

Let  $\{N(t), t \geq 0\}$  be a Poisson process, let  $\{Y_1, Y_2, \ldots\}$  be i.i.d. random vectors,  $W$  a standard multidimensional Brownian motion with  $N$ ,  $W$ , and  $\{Y_1, Y_2, \ldots\}$  independent of each other. Consider jump-diffusion models of the  $\text{form}$ 

$$dX(t) = a(X(t-)) dt + b(X(t-))^\top dW(t) + c(X(t-), Y_{N(t-)+1}) dN(t). \tag{6.46}$$

Between jumps of the Poission process,  $X$  evolves like a diffusion with coefficient functions a and b; at the nth jump of the Poisson process, the jump in  $X$  is

$$X(t) - X(t-) = c(X(t-), Y_n),$$

a function of the state of X just before the jump and the random variable  $Y_n$ . We discussed a special case of this model in Section  $3.5.1$ . Various processes of this type are used to model the dynamics of underlying assets in pricing derivative securities.

Mikulevicius and Platen  $[265]$  extend the general weak expansion  $(6.44)$ to processes of this type and analyze the discretization schemes that follow from this expansion. Their method uses a pure-diffusion discretization method between the jumps of the Poisson process and applies the function  $c$  to the discretized process to determine the jump in the discretized process at a jump of the Poisson process. The jump magnitudes are thus computed exactly, conditional on the value of the discretized process just before a jump. Mikulevicius and Platen [265] show, in fact, that the weak order of convergence of this method equals the order of the scheme used for the pure-diffusion part, under conditions on the coefficient functions  $a, b, \text{ and } c$ .

In more detail, this method supplements the original time grid  $0, h, 2h, \ldots$ with the jump times of the Poisson process. Because the Poisson process is independent of the Brownian motion, we can imagine generating all of these jump times at the start of a simulation. (See Section  $3.5$  for a discussion of the simulation of Poisson processes.) Let  $0 = \tau_0, \tau_1, \tau_2, \ldots$  be the combined time grid, including both the multiples of  $h$  and the Poisson jump times. The discretization scheme proceeds by simulating  $\hat{X}$  from  $\tau_i$  to  $\tau_{i+1}, i = 0, 1, \ldots$ Given  $\ddot{X}(\tau_i)$ , we apply an Euler scheme or higher-order scheme to generate  $\hat{X}(\tau_{i+1}-)$ , using the coefficient functions a and b. If  $\tau_{i+1}$  is a Poisson jump time — the *n*th, say — we generate  $Y_n$  and set

$$\hat{X}(\tau_{i+1}) = \hat{X}(\tau_{i+1} -) + c(\hat{X}(\tau_{i+1} -), Y_n).$$

If  $\tau_{i+1}$  is not a jump time, we set  $\hat{X}(\tau_{i+1}) = \hat{X}(\tau_{i+1} -)$ .

Glasserman and Merener  $[145]$  apply this method to a version of the LI-BOR market model with jumps. The jump processes they consider are more general than Poisson processes, having arrival rates that depend on the current level of forward rates. They extend the method to this setting by using a bound on the state-dependent arrival rates to construct jumps by thinning a Poisson process. This requires relaxing the smoothness conditions imposed on  $c$  in Mikulevicius and Platen [265].

Maghsoodi  $[245]$  provides various alternative discretization schemes for jump-diffusion processes and considers both strong and weak error criteria. He distinguishes jump-adapted methods (like the one described above) that include the Poisson jump epochs in the time grid from those that use a fixed grid. A jump-adapted method may become computationally burdensome if the jump intensity is very high. Protter and Talay [301] analyze the Euler scheme for stochastic differential equations driven by Lévy processes, which include  $(6.46)$  as a special case. Among other results, they provide error expansions in powers of  $h$  justifying the use of Richardson extrapolation.

### 6.3.3 Convergence of Mean Square Error

. viv.

The availability of discretization schemes of various orders poses a tradeoff: using a higher-order scheme requires more computing time per path and thus reduces the number of paths that can be completed in a fixed amount of time. The number of paths completed affects the standard error of any estimates we compute, but has no effect on discretization bias, which is determined by our choice of scheme. Thus, we face a tradeoff between reducing bias and reducing variance.

We discussed this tradeoff in a more general setting in Section  $1.1.3$  and the asymptotic conclusions reached there apply in the current setting. Here we present a slightly different argument to arrive at the same conclusion.

We suppose that our objective is to minimize mean square error (MSE), the sum of variance and squared bias. Using a discretization scheme of weak order  $\beta$ , we expect

$$\text{Bias} \approx c_1 h^{\beta}$$

for some constant  $c_1$ . For the variance based on n paths we expect

Variance 
$$\approx \frac{c_2}{n}$$

for some constant  $c_2$ . The time step h would generally have some effect on variance; think of  $c_2$  as the limit as h decreases to zero of the variance per replication.

If we make the reasonable assumption that the computing time per path is proportional to the number of steps per path, then it is inversely proportional to h. The total computing time for n paths is then  $nc_3/h$ , for some constant  $c_3.$ 

With these assumptions and approximations, we formulate the problem of minimizing MSE subject to a computational budget  $s$  as follows:

$$\min_{n,h} \left( c_1^2 h^{2\beta} + \frac{c_2}{n} \right) \quad \text{subject to} \quad \frac{nc_3}{h} = s.$$

Using the constraint to eliminate a variable, we put this in the form

$$\min_{h} \left( c_1^2 h^{2\beta} + \frac{c_2 c_3}{hs} \right),$$

 $\text{which is minimized at}$ 

$$h = cs^{-\frac{1}{2\beta + 1}} \tag{6.47}$$

with  $c$  a constant. Substituting this back into our expressions for the squared bias and the variance, we get

$$\text{MSE} \approx c_1' s^{-\frac{2\beta}{2\beta+1}} + c_2' s^{-\frac{2\beta}{2\beta+1}} = c' s^{-\frac{2\beta}{2\beta+1}},$$

for some constants  $c'$ ,  $c'_1$ ,  $c'_2$ . The optimal allocation thus balances variance and squared bias. Also, the optimal root mean square error becomes

$$\sqrt{\text{MSE}} \propto s^{-\frac{\beta}{2\beta+1}}.$$
 (6.48)

This is what we found in Section  $1.1.3$  as well.

These calculations show how the order  $\beta$  of a scheme affects both the optimal allocation of effort and the convergence rate under the optimal allocation. As the convergence order  $\beta$  increases, the optimal convergence rate in (6.48) approaches  $s^{-1/2}$ , the rate associated with unbiased simulation. But for the important cases of  $\beta = 1$  (first-order) and  $\beta = 2$  (second-order) we get rates of  $s^{-1/3}$  and  $s^{-2/5}$ . This makes precise the notion that simulating a process for which a discretization scheme is necessary is harder than simulating a solvable model. It also shows that when very accurate results are required (i.e., when  $s$  is large), a higher-order scheme will ultimately dominate a lower-order scheme.

Duffie and Glynn [100] prove a limit theorem that justifies the convergence rate implied by  $(6.48)$ . They also report numerical results that are generally consistent with their theoretical predictions.

# 6.4 Extremes and Barrier Crossings: Brownian Interpolation

In Section  $6.2.3$  we showed that discretization methods can sometimes be extended to path-dependent payoffs through supplementary state variables. The additional state variables remove dependence on the past; standard discretization procedures can then be applied to the augmented state vector.

In option pricing applications, path-dependence often enters through the maximum or minimum of an underlying asset over the life of the option. This includes, for example, options whose payoffs depend on whether or not an underlying asset crosses a barrier. Here, too, path-dependence can be eliminated by including the running maximum or minimum in the state vector. However, this renders standard discretization procedures inapplicable because of the singular dynamics of these supplementary variables. The running maximum, for example, can increase only when it is equal to the underlying process.

This issue arises even when the underlying process  $X$  is a standard Brownian motion. Let

$$M(t) = \max_{0 \le u \le t} X(u)$$

and let

$$\hat{M}^{h}(n) = \max\{X(0), X(h), X(2h), \dots, X(nh)\}.$$
(6.49)

Then  $\hat{M}^h(n)$  is the maximum of the Euler approximation to X over  $[0, nh]$ ; the Euler approximation to  $X$  is exact for  $X$  itself because  $X$  is Brownian motion. Fix a time T and let  $h = T/n$  so that  $\hat{M}^h(n)$  is the discrete-time approximation of  $M(T)$ . Asmussen, Glynn, and Pitman [24] show that the normalized error

6.4 Extremes and Barrier Crossings: Brownian Interpolation 367

$$h^{-1/2}[\hat{M}^{h}(n) - M(T)]$$

has a limiting distribution as  $h \rightarrow 0$ . This result may be paraphrased as stating that the distribution of  $\hat{M}^h(n)$  converges to that of  $M(T)$  at rate  $h^{1/2}$ . It follows that the weak order of convergence (in the sense of (6.14)) cannot be greater than  $1/2$ . In contrast, we noted in Section 6.1.2 that for SDEs with smooth coefficient functions the Euler scheme has weak order of convergence 1. Thus, the singularity of the dynamics of the running maximum leads to a slower convergence rate.

In the case of Brownian motion, this difficulty can be circumvented by sampling  $M(T)$  directly, rather than through (6.49). We can sample from the joint distribution of  $X(T)$  and  $M(T)$  as follows. First we generate  $X(T)$ from  $N(0,T)$ . Conditional on  $X(T)$  the process  $\{X(t), 0 \le t \le T\}$  becomes a Brownian bridge, so we need to sample from the distribution of the maximum of a Brownian bridge. We discussed how to do this in Example 2.2.3. Given  $X(T)$ , set

$$M(T) = \frac{X(T) + \sqrt{X(T)^2 - 2T\log U}}{2}$$

with  $U \sim \text{Unif}[0,1]$  independent of  $X(T)$ . The pair  $(X(T), M(T))$  then has the joint distribution of the terminal and maximum value of the Brownian motion over  $[0, T]$ .

This procedure, exact for Brownian motion, suggests an approximation for more general processes. Suppose X is a diffusion satisfying the SDE  $(6.1)$ with scalar coefficient functions a and b. Let  $\hat{X}(i) = \hat{X}(ih), i = 0, 1, \ldots$ , be a discrete-time approximation to  $X$ , such as one defined through an Euler or higher-order scheme. The simple estimate (6.49) applied to  $\hat{X}$  is equivalent to taking the maximum over a piecewise linear interpolation of  $X$ . We can expect to get a better approximation by interpolating over the interval  $[ih, (i+1)h]$  using a Brownian motion with fixed parameters  $a_i = a(\hat{X}(i))$ and  $b_i = b(\hat{X}(i))$ . Given the endpoints  $\hat{X}(i)$  and  $\hat{X}((i+1))$ , the maximum of the interpolating Brownian bridge can be simulated using

$$\hat{M}_{i} = \frac{\hat{X}(i+1) + \hat{X}(i) + \sqrt{[\hat{X}(i+1) - \hat{X}(i)]^{2} - 2b_{i}^{2}h\log U_{i}}}{2},\qquad(6.50)$$

with  $U_0, U_1, \ldots$  independent Unif[0,1] random variables. (The value of  $a(\hat{X}(i))$ becomes immaterial once we condition on  $X(i+1)$ .) The maximum of X over  $[0,T]$  can then be approximated using

$$\max\{\hat{M}_0,\hat{M}_1,\ldots,\hat{M}_{n-1}\}.$$

Similar ideas are suggested in Andersen and Brotherton-Ratcliffe [16] and in Beaglehole, Dybvig, and Zhou [41] for pricing lookback options; their numerical results indicate that the approach can be very effective. Baldi  $[31]$  analyzes related techniques in a much more general setting.

S,

In some applications,  $X$  may be better approximated by geometric Brownian motion than by ordinary Brownian motion. This can be accommodated by applying (6.50) to  $\log \hat{X}$  rather than  $\hat{X}$ . This yields

$$\log \hat{M}_i = \frac{\log(\hat{X}(i+1)\hat{X}(i)) + \sqrt{[\log(\hat{X}(i+1)/\hat{X}(i))]^2 - 2(b_i/\hat{X}(i))^2h\log U_i}}{2},$$

and exponentiating produces  $\hat{M}_i$ .

### Barrier Crossings

Similar ideas apply in pricing barrier options with continuously monitored barriers. Suppose  $B > X(0)$  and let

$$\tau = \inf\{t \ge 0 : X(t) > B\}.$$

A knock-out option might have a payoff of the form

$$(K - X(T))^{+}\mathbf{1}_{\{\tau > T\}},\tag{6.51}$$

with K a constant. This requires simulation of  $X(T)$  and the indicator  $\mathbf{1}_{\{\tau > 0\}}$  $T$ .

The simplest method sets

$$\hat{\tau} = \inf\{i : \hat{X}(i) > B\}$$

and approximates  $(X(T), \mathbf{1}_{\{\tau > T\}})$  by  $(X(n), \mathbf{1}_{\{\hat{\tau} > n\}})$  with  $h = T/n$ , for some discretization  $X$ . But even if we could simulate X exactly on the discrete grid  $0, h, 2h, \ldots$ , this would not sample  $\mathbf{1}_{\{\tau > T\}}$  exactly: it is possible for X to cross the barrier at some time t between grid points ih and  $(i + 1)h$  and never be above the barrier at any of the dates  $0, h, 2h, \ldots$ 

The method in  $(6.50)$  can be used to reduce discretization error in sampling the survival indicator  $\mathbf{1}_{\{\tau > T\}}$ . Observe that the barrier is crossed in the interval  $[ih, (i+1)h)$  precisely if the maximum over this interval exceeds B. Hence, we can approximate the survival indicator  $\mathbf{1}_{\{\tau > T\}}$  using

$$\prod_{i=0}^{n-1} \mathbf{1}\{\hat{M}_i \le B\},\tag{6.52}$$

with  $nh = T$  and  $\hat{M}_i$  as in (6.50).

This method can be simplified. Rather than generate  $\hat{M}_i$ , we can sample the indicators  $\mathbf{1}\{\hat{M}_i \leq B\}$  directly. Given  $\hat{X}(i)$  and  $\hat{X}(i+1)$ , this indicator  $\text{takes the value 1 with probability}$ 

$$\hat{p}_i = P(\hat{M}_i \le B | \hat{X}(i), \hat{X}(i+1)) = 1 - \exp\left(-\frac{2(B - \hat{X}(i))(B - \hat{X}(i+1))}{b(\hat{X}(i))^2 h}\right),$$

(assuming B is greater than both  $\hat{X}(i)$  and  $\hat{X}(i+1)$ ) and it takes the value 0 with probability  $1 - \hat{p}_i$ . Thus, we can approximate  $\mathbf{1}_{\{\tau > T\}}$  using

 $\mathcal{D}_{\mathcal{A}}$ 

$$\prod_{i=0}^{n-1} \mathbf{1}\{U_i \le \hat{p}_i\}$$

For fixed  $U_0, U_1, \ldots, U_{n-1}$ , this has the same value as (6.52) but is slightly simpler to evaluate. The probabilities  $\hat{p}_i$  could alternatively be computed based on an approximating geometric (rather than ordinary) Brownian motion.

The discretized process  $\hat{X}$  is often a Markov process and this leads to further simplification. Consider, for example, the payoff in  $(6.51)$ . Using  $(6.52)$ , we approximate the payoff as

$$(K - \hat{X}(n))^{+} \prod_{i=0}^{n-1} \mathbf{1}\{\hat{M}_{i} \le B\}.$$
 (6.53)

The conditional expectation of this expression given the values of  $\hat{X}$  is

$$\mathsf{E}\left[ (K - \hat{X}(n))^{+} \prod_{i=0}^{n-1} \mathbf{1}\{\hat{M}_{i} \leq B\} |\hat{X}(0), \hat{X}(1), \dots, \hat{X}(n) \right]$$
(6.54)  
$$= (K - \hat{X}(n))^{+} \prod_{i=0}^{n-1} \mathsf{E}[\mathbf{1}\{\hat{M}_{i} \leq B\} |\hat{X}(i), \hat{X}(i+1)]$$

$$= (K - \hat{X}(n))^{+} \prod_{i=0}^{n-1} \hat{p}_{i}.$$
 (6.55)

Thus, rather than generate the barrier-crossing indicators, we can just multiply by the probabilities  $\hat{p}_i$ .

Because  $(6.55)$  is the conditional expectation of  $(6.53)$ , the two have the same expectation and thus the same discretization bias. By Jensen's inequality, the second moment of  $(6.53)$  is larger than the second moment of its conditional expectation  $(6.55)$ , so using  $(6.55)$  rather than  $(6.53)$  reduces variance. (This is an instance of a more general strategy for reducing variance known as conditional Monte Carlo, based on replacing an estimator with its conditional expectation; see, Boyle et al.  $[53]$  for other applications in finance.) Using (6.53), we would stop simulating a path once some  $M_i$  exceeds B. Using (6.55), we never generate the  $M_i$  and must therefore simulate every path for n steps, unless some  $\hat{X}(i)$  exceeds B (in which case  $\hat{p}_i = 0$ ). So, although  $(6.55)$  has lower variance, it requires greater computational effort per path. A closely related tradeoff is investigated by Glasserman and Staum  $[146]$ ; they consider estimators in which each transition of an underlying asset is sampled conditional on not crossing a barrier. In their setting, products of survival probabilities like those in  $(6.55)$  serve as likelihood ratios relating the conditional and unconditional evolution of the process.

Baldi, Caramellino, and Iovino [32] develop methods for reducing discretization error in a general class of barrier option simulation problems. They consider single- and double-barrier options with time-varying barriers and develop approximations to the one-step survival probabilities that refine the  $\hat{p}_i$ above. The  $\hat{p}_i$  are based on a single constant barrier and a Brownian approximation over a time interval of length  $h$ . Baldi et al. [32] derive asymptotics of the survival probabilities as  $h \to 0$  for quite general diffusions based, in part, on a linear approximation to upper and lower barriers.

## Averages Revisited

As already noted, the simulation estimators based on  $(6.50)$  or  $(6.52)$  can be viewed as the result of using Brownian motion to interpolate between the points  $X(i)$  and  $X(i+1)$  in a discretization scheme. The same idea can be applied in simulating other path-dependent quantities besides extremes and barrier-crossing indicators.

As an example, consider simulation of the pair

$$\left(X(T), \int_0^T X(t) \, dt\right)$$

for some scalar diffusion  $X$ . In Section 6.2.3, we suggested treating this pair as the state at time  $T$  of a bivariate diffusion and applying a discretization method to this augmented process. An alternative simulates a discretization  $X(i), i = 0, 1, \ldots, n$ , and uses Brownian interpolation to approximate the integral. More explicitly, the approximation is

$$\int_{0}^{T} X(t) dt \approx \sum_{i=0}^{n-1} b_i \hat{A}_i,$$

with  $b_i = b(\hat{X}(i))$  and each  $\hat{A}_i$  sampled from the distribution of

$$\int_t^{t+h} W(u) \, du, \quad W \sim \text{BM}(0,1),$$

conditional on  $W(t) = \hat{X}(i)$  and  $W(t+h) = \hat{X}(i+1)$ . The calculations used to derive  $(6.27)$  show that this conditional distribution is normal with mean  $h(\hat{X}(i+1)+\hat{X}(i))/2$  and variance  $h^3/3$ . Thus, the  $\hat{A}_i$  are easily generated.

This leads to a discretization scheme only slightly different from the one arrived at through the approach in Section 6.2.3. Because of the relative smoothness of the running integral, the effect of Brownian interpolation in this setting is minor compared to the benefit in simulating extremes or barrier crossings.

## 6.5 Changing Variables

We conclude our discussion of discretization methods by considering the flexibility to change variables through invertible transformations of a process. If  $X$ is a d-dimensional diffusion and  $q: \mathbb{R}^d \to \mathbb{R}^d$  is a smooth, invertible transformation, we can define a process  $Y(t) = g(X(t))$ , simulate a discretization  $\hat{Y}$ , and define  $\hat{X} = g^{-1}(\hat{Y})$  to get a discretization of the original process X. Thus, even if we restrict ourselves to a particular discretization method (an Euler or higher-order scheme), we have a great deal of flexibility in how we implement it. Changing variables has the potential to reduce bias and can also be useful in enforcing restrictions (such as nonnegativity) on simulated values. There is little theory available to guide such transformations; we illustrate the idea with some examples.

## Taking Logarithms

Many of the stochastic processes that arise in mathematical finance take only positive values. This property often results from specifying that the diffusion term be proportional to the current level of the process, as in geometric Brownian motion and in the LIBOR market model of Section 3.7. If the coordinates of a d-dimensional process  $X$  are positive, we may define  $Y_i(t) = \log X_i(t), i = 1, \ldots, d$ , apply Itô's formula to derive an SDE satisfied by  $Y = (Y_1, \ldots, Y_d)$ , simulate a discretization  $\hat{Y}$  of Y, and then (if they are needed) approximate the original  $X_i$  with  $\hat{X}_i = \exp(\hat{Y}_i)$ . We encountered this idea in Section  $3.7.3$  in the setting of the LIBOR market model.

Applying a logarithmic transformation can have several benefits. First, it ensures that the simulated  $\hat{X}_i$  are positive because they result from exponentiation, whereas even a high-order scheme applied directly to the dynamics of  $X$  will produce some negative values. Keeping the variables positive can be important if the variables represent asset prices or interest rates.

Second, a logarithmic transformation can enhance the numerical stability of a discretization method, meaning that it can reduce the propagation of round-off error. A process with "additive noise" can generally be simulated with less numerical error than a process with "multiplicative noise." Numerical stability is discussed in greater detail in Kloeden and Platen [211].

Third, a logarithmic transformation can reduce discretization bias. For example, an Euler scheme applied to geometric Brownian motion becomes exact if we first take logarithms. More generally, if the coefficients of a diffusion are nearly proportional to the level of the process, then the coefficitions of the log process are nearly constant.

This idea is illustrated in Figure 6.3, which is similar to examples in Glasserman and Merener [145] and is based on numerical results obtained by Nicolas Merener. The figure shows estimated biases in pricing a six-month caplet maturing in 20 years using the LIBOR market model with the decreasing volatility parameters used in Table 4.2. The largest practical time step in

this setting is the length of the accrual period; the figure compares methods using one, two, and four steps per accrual period with between four and 20 million replications per method. In this example, taking logarithms cuts the absolute bias roughly in half for the Euler scheme. The figure also shows results using a second-order method for rates  $(\times)$  and log rates  $(\circ)$ ; even with 10 million replications, the mean errors in these methods are not statistically distinguishable from zero. In a LIBOR market model with jumps, Glasserman and Merener [145] find experimentally that a first-order scheme applied to log rates is as accurate as a second-order scheme applied to the rates themselves.

![](_page_33_Figure_2.jpeg)

**Fig. 6.3.** Estimated bias versus number of steps in caplet pricing. The  $\times$  and  $\circ$ correspond to second-order schemes for rates and log rates, respectively.

As an aside, we note that the most time-consuming part of simulating an Euler approximation to a LIBOR market model is evaluating the drift coefficient. To save computing time, one might use the same value of the drift for multiple time steps, along the lines of Example 4.1.4, but with occasional updating of the drift. A similar idea is found to be effective in Hunter et al.  $[192]$  as part of a predictor-corrector method (of the type discussed in Chapter 15 of Kloeden and Platen  $[211]$ ).

### Imposing Upper and Lower Bounds

Taking logarithms enforces a lower bound at zero on a discretized process. Suppose the coordinates of X are known to evolve in the interval  $(0,1)$ . How could this be imposed on a discretization of  $X$ ? Enforcing such a condition could be important if, for example, the coordinates of  $X$  are zero-coupon bond prices, which should always be positive and should never exceed their  $face value of 1.$ 

Glasserman and Wang  $[149]$  consider the transformations

6.5 Changing Variables 373

$$Y_i = \Phi^{-1}(X_i) \quad \text{and} \quad Y_i = \log\left(\frac{X_i}{1 - X_i}\right),\tag{6.56}$$

both of which are increasing functions from  $(0,1)$  onto the real line. Itô's formula produces an SDE for  $Y$  from an SDE for  $X$  in either case; the resulting SDE can be discretized and then the inverse transformations applied to produce

$$\hat{X}_i = \Phi(\hat{Y}_i) \quad \text{ or } \quad \hat{X}_i = \frac{\exp(Y_i)}{1 + \exp(\hat{Y}_i)}.$$

If the coordinates of  $X$  correspond to bonds of increasing maturities, we may also want to enforce an ordering of the form

$$1 \ge X_1(t) \ge X_2(t) \ge \dots \ge X_d(t) \ge 1 \tag{6.57}$$

in the discretization. The method in [149] accomplishes this by defining  $Y_1 =$  $g(X_1), Y_i = g(X_i/X_{i-1}), i = 2, \ldots, d$ , with g an increasing function from  $(0, 1)$ to  $\Re$  as in (6.56). Itô's formula gives the dynamics of  $(Y_1,\ldots,Y_d)$  and then a discretization  $(\hat{Y}_1,\ldots,\hat{Y}_d)$ ; applying the inverse of  $g$  produces a discretization  $(\hat{X}_1,\ldots,\hat{X}_d)$  satsifying (6.57).

## Constant Diffusion Transformation

Consider the SDE  $(6.1)$  in the case of scalar X and W. Suppose there exists an invertible, twice continuously differentiable transformation  $q: \Re \to \Re$  for which  $g'(x) = 1/b(x)$ . With  $Y(t) = g(X(t))$ , Itô's formula gives

$$\begin{array}{l} dY(t) = \left[ a(X(t))g'(X(t)) + \frac{1}{2}b^2(X(t))g''(X(t)) \right] \, dt + g'(X(t))b(X(t)) \, dW(t) \\ = \tilde{a}(Y(t)) \, dt + dW(t), \end{array}$$

with  $\tilde{a}(y) = a(f(y))g'(f(y)) + \frac{1}{2}b^2(f(y))g''(f(y))$  and f the inverse of g. Changing variables from  $X$  to  $Y$  thus produces an SDE with a constant diffusion coefficient. This is potentially useful in reducing discretization error, though the impact on the drift cannot be disregarded. Moving all state-dependence from the diffusion to the drift is attractive in combination with a predictorcorrector method, which improves accuracy by averaging current and future levels of the drift coefficient.

To illustrate the constant diffusion transformation we apply it to the square-root diffusion

$$dX(t) = \alpha(\bar{x} - X(t)) dt + \sigma\sqrt{X(t)} dW(t).$$

Let  $Y(t) = 2\sqrt{X}/\sigma$ ; then Y is a Bessel-like process,

$$dY(t) = \left[ \left( \frac{4\alpha \bar{x} - \sigma^2}{2\sigma^2} \right) \frac{1}{Y(t)} - \frac{\alpha}{2} Y(t) \right] dt + dW(t).$$

In Section 3.4 we imposed the condition  $2\alpha \bar{x} \geq \sigma^2$ , and this is precisely the condition required to ensure that Y never reaches zero if  $Y(0) > 0$ .

Now suppose X and W take values in  $\Re^d$  and suppose the  $d \times d$  matrix  $b(x)$  has inverse  $c(x)$ . Ait-Sahalia [7] shows that there is an invertible transformation  $q: \mathbb{R}^d \to \mathbb{R}^d$  such that the diffusion matrix of  $Y(t) = g(X(t))$  is the identity if and only if

$$\frac{\partial c_{ij}}{\partial x_k} = \frac{\partial c_{ik}}{\partial x_j}.$$

for all  $i, j, k = 1, \ldots, d$ . This condition implies the commutativity condition  $(6.33)$ . It follows that processes X that can be transformed to have a constant diffusion matrix are also processes for which a second-order scheme is comparatively easy to implement.

### Martingale Discretization

The requirement that discounted asset prices be martingales is central to the pricing of derivative securities. The martingale property is usually imposed in a continuous-time model; but as we have noted at several points, it is desirable to enforce the property on the simulated approximation as well. Doing so extends the no-arbitrage property to prices computed from a simulation. It also preserves the internal consistency of a simulated model by ensuring that prices of underlying assets computed in a simulation coincide with those used as inputs to the simulation; cf. the discussions in Sections  $3.3.2, 3.6.2, 3.7.3,$ Example  $4.1.3$ , and Section  $4.5$ .

If the SDE  $(6.1)$  has drift coefficient a identically equal to zero, then the Euler and higher-order methods in Sections  $6.1.1$  and  $6.2$  all produce discretizations  $X$  that are discrete-time martingales. In this sense, the martingale property is almost trivially preserved by the discretization methods. However, the variables simulated do not always coincide with the variables to which the martingale property applies. For example, in pricing fixed-income derivatives we often simulate interest rates but the martingale property applies to discounted bonds and not to the interest rates themselves.

The simulation method developed for the Heath-Jarrow-Morton framework in Section  $3.6.2$  may be viewed as a nonstandard Euler scheme — nonstandard because of the modified drift coefficient. We modified the drift in forward rates precisely so that the discretized discounted bond prices would be martingales. In the LIBOR market models of Section 3.7, we argued that an analogous drift modification is infeasible. Instead, in Section 3.7.3 we discussed ways of preserving the martingale property through changes of variables. These methods include discretizing the discounted bond prices directly or discretizing their differences.

Preserving the martingale property is sometimes at odds with preserving bounds on variables. If  $X$  is a positive martingale then the Euler approximation to  $X$  is a martingale but not, in general, a positive process. Both

properties can usually be enforced by discretizing  $\log X$  instead. If X is a martingale taking values in  $(0,1)$ , then defining Y as in  $(6.56)$ , discretizing  $Y$ , and then inverting the transformation preserves the bounds on  $X$  but not the martingale property. Using the transformation  $\Phi^{-1}$ , a simple correction to the drift preserves the martingale property as well as the bounds. As shown in [149], when applied to the multidimensional constraint  $(6.57)$ , this method preserves the constraints and limits departures from the martingale property to terms that are  $o(h)$ , with h the simulation time step.

## 6.6 Concluding Remarks

Å,

The benchmark method for reducing discretization error is the combination of the Euler scheme with two-point extrapolation, as in Section 6.2.4. This technique is easy to implement and is usually faster than a second-order expansion for comparable accuracy, especially in high dimensions. The smoothness conditions required on the coefficient functions to ensure the validity of extrapolation are not always satisfied in financial engineering applications, but similar conditions underlie the theoretical support for second-order approximations.

Second-order and higher-order schemes do have practical applications, but they should always be compared with the simpler alternative of an extrapolated Euler approximation. A theoretical comparison is usually difficult, but the magnitudes of the derivatives of the coefficient functions can provide some indication, with large derivatives unfavorable for higher-order methods. Talay and Tubaro [343] analyze specific models for which they derive explicit expressions for error terms. They show, for example, that the refinement in  $(6.10)$  can produce larger errors than an Euler approximation.

Of the many expansions discussed in this chapter, the most useful (in addition to the extrapolated Euler scheme) are  $(6.28)$  for scalar processes and  $(6.38)$  for vector processes.

For specific applications in financial engineering, a technique that uses information about the problem context is often more effective than a generalpurpose expansion. For example, even a simple logarithmic change of variables can reduce discretization error, with the added benefit of ensuring that positive variables stay positive. The methods of Section 6.4 provide another illustration: they offer simple and effective ways of reducing discretization error in pricing options sensitive to barrier crossings and extreme values of the underlying assets. The simulation methods in Sections 3.6 and 3.7 also address discretization issues for specific models.

The literature on discretization methods for stochastic differential equations offers many modifications of the basic schemes discussed in Sections 6.1.1,  $6.2$ , and  $6.3.1$ . Kloeden and Platen [211] provide a comprehensive treatment of these methods. Another direction of research investigates the law of the error of a discretization method, as in Jacod and Protter  $[193]$ .

This chapter has discussed the use of second-order and higher-order expansions in simulation, but the same techniques are sometimes useful in deriving approximations without recourse to simulation.

 $\mathcal{L} = \mathcal{L}(\mathcal{L}) \mathcal{L}(\mathcal{L})$ 

As the Strategy of Marine
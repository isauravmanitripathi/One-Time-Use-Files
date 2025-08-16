# **Yield Curve Construction**

The objective of an interest rate model is to describe the random movement of a curve of zero-coupon bond prices through time, starting from a known initial condition. In reality, however, only a few shortdated zero-coupon bonds are directly quoted in the market at any given time, a long stretch from the assumption of many models that an initial curve of zero-coupon bond prices is observable for a continuum of maturities. Fortunately, a number of liquid securities depend, in relatively straightforward fashion, on zero-coupon bonds, opening up for the possibility of uncovering zero-coupon bond prices from prices of such securities. Still, as only a finite set of securities are quoted in the market, constructing a continuous curve of zero-coupon bond prices will require us to complement market observation with an interpolation rule, based perhaps on direct assumptions about functional form or perhaps on a regularity norm to be optimized on. A somewhat specialized area of research, discount curve construction relies on techniques from a number of fields, including statistics and computer graphics. We discuss the basic topics in detail and refer the reader to appropriate sources for advanced applications. In the same spirit, we pay scant attention to the subtle intricacies of actual swap and bond market conventions.

# **Discount Curves**

Let  $P(t, T)$  be the time t price of a zero-coupon bond maturing at time  $T$ . Going forward, we use the abbreviated notation  $P(T) = P(0, T)$  where  $P:[0,T] \rightarrow (0,1]$  is a continuous, monotonically declining *discount curve*.  $T$  denotes the maximum maturity considered, typically given as the longest maturity in the set of securities the curve is built to match. Let there be  $N$  such securities—the bench*mark set*—with observable prices  $V_1, \ldots, V_N$ . We fundamentally assume that the time 0 price  $V_i =$  $V_i(0)$  of security *i* can be written as a linear combination of zero-coupon bond prices at different maturities.

$$V_i = \sum_{j=1}^{M} c_{ij} P(t_j), \quad i = 1, \dots, N \tag{1}$$

where  $0 < t_1 < t_2 < \ldots < t_M \leq T$  is a given finite set of dates, in practice obtained by merging together the cash-flow dates of each of the  $N$  benchmark securities. Securities that satisfy relationship (1) include coupon bonds, forward rate agreements (FRAs), as well as fixed-floating interest rate swaps. For instance, consider a newly issued unit-notional fixedfloating swap, paying a coupon of  $c\tau$  at times  $\tau$ ,  $2\tau, 3\tau, \ldots, n\tau$ . If no spread is paid on the floating rate, the time 0 total swap value  $V_S$  to the fixed-rate paver is

$$V_S = 1 - P(n\tau) - \sum_{j=1}^n c\tau P(j\tau) \Rightarrow$$
  
$$1 - V_S = P(n\tau) + \sum_{j=1}^n c\tau P(j\tau)$$
 (2)

which is in the form (1) once we interpret  $V_i =$  $1 - V_{\rm s}$ .

The choice of the securities to be included in the benchmark set depends on the market under consideration. For instance, to construct a treasury bond curve, it is natural to choose a set of treasury bonds and T-bills. On the other hand, if we are interested in constructing a discount curve applicable for bonds issued by a particular firm, we would naturally use bonds and loans used by the firm in question. In many applications, the most important yield curve is the *Libor curve*, constructed out of market quotes for Libor deposits, swaps, and Eurodollar futures. In the construction of this curve, most firms would use a few certificates of deposit for the first 3 months of the curve, followed by a strip of Eurodollar futures<sup>a</sup> (with maturities staggered 3 months apart) out to  $3$ or 4 years. Par swaps are then used for the rest of the curve, often going out to 30 years or more.

# **Matrix Formulation & Transformations**

Define the  $M$ -dimensional discount bond vector

$$\mathbf{P} = (P(t_1), \dots, P(t_M))^\top \tag{3}$$

and let  $\mathbf{V} = (V_1, \ldots, V_N)^\top$  be the vector of observable security prices. Also let  $\mathbf{c} = \{c_{ij}\}\$  be an  $N \times M$ dimensional matrix containing all the cash flows produced by the chosen set of securities.  $\mathbf{c}$  would typically be quite sparse.

In a friction-free market without arbitrage, the fundamental relation

$$\mathbf{V} = \mathbf{c}\mathbf{P} \tag{4}$$

must be satisfied, giving us a starting point to find  $P$ . In practice, however, we normally have  $M > N$ , in which case equation (4) is insufficient to uniquely determine  $P$ . The problem of curve construction essentially boils down to supplementing equation (4) with enough additional assumptions to allow us to extract **P** and to determine  $P(T)$  for values of T not in the cash-flow timing set  $\{t_j\}_{j=1}^M$ .

As it is normally easier to devise an interpolation scheme on a curve that is reasonably flat (rather than exponentially decaying), it is common to perform the curve-fitting exercise on *zero-coupon yields*, rather than directly on discount bond prices<sup>b</sup>. Specifically, we introduce a continuous yield function  $y$ :  $[0,T] \to \mathbb{R}_+$  given by

$$e^{-y(T)T} = P(T) \Rightarrow y(T) = -T^{-1} \ln P(T)$$
 (5)

such that in equation (4)  $\mathbf{P} = (e^{-y(t_1)T_1}, \dots, e^{-y(t_M)T_M})$ . The mapping  $T \mapsto y(T)$  is known as the *yield curve*; it is related to the discount curve by the simple transformation (5). Of related interest is also the instantaneous forward curve  $f(T)$ , given by

$$P(T) = e^{-\int_0^T f(u) du} \Rightarrow f(T) = y(T) + \frac{dy(T)}{dT}T$$
(6)

For more transformations of the discount curve—and a discussion of relative merits in curve construction—see  $[1, 14]$ . For simplicity, in this article we work primarily with  $y(T)$  unless otherwise noted.

# **Construction Principles**

We have at least three options for solving equation (4).

- 1. We can introduce new and unspanned securities such that  $N = M$  and equation (4) allows for exactly one solution.
- 2. We can use a parameterization of the yield curve with precisely  $N$  parameters, using the  $N$  equations in equation (4) to recover these parameters.
- 3. We can search the space of all solutions to equation  $(4)$  and choose the one that is "optimal" according to a given criterion.

Let us provide some comments to these three ideas. First, in option 1, introduction of new securities might not truly be possible—such securities may simply not exist—but sometimes interpolation rules applied to the given benchmark set may allow us to provide reasonable values for an additional set of "fictitious" securities. Although it can occasionally be useful in preprocessing to pad an overly sparse benchmark set, this idea will often require some quite *ad hoc* decisions about the specifics of the fictitious securities, and excessive use may ultimately lead to odd-looking curves and suboptimal hedge reports. When an interpolation rule is to be used, it is typically better to apply it to fundamental quantities such as zero-coupon yields or forward rates, thereby maintaining a higher degree of control over the resulting yield curve.

In option 2 above, parametric functional forms such as that in  $[9]$  are sometimes used, but it is far more common to work with a spline representation with  $N$  user-selected knots (typically at the maturity dates of the benchmark securities), with the level of the yield curve at these knots constituting the  $N$ unknowns to be solved for. We discuss the details of this approach in the section Yield Curve Fitting with  $N$ -knot Splines, using a number of different spline types. We assume some knowledge of spline theory here—classical references are [2, 11].

Option 3 is covered in the section Nonparametric Optimal Yield Curve Fitting and constitutes the most sophisticated approach. It can often be stated in completely nonparametric terms, with the yield curve emerging naturally as the solution to an optimization problem. If carefully stated, this approach can be set up to also handle the situation where the system of equations (4) is (near-) singular, in the sense that either no solutions exist or all solutions are irregular and nonsmooth.

#### Yield Curve Fitting with N-Knot Splines

In this section, we discuss a number of yield Curve algorithms based on polynomial and exponential (tension) splines of various degrees of differentiability. Throughout, we assume that we can select and arrange our benchmark set of securities to guarantee that the maturities of the benchmark securities satisfy

$$T_i > T_{i-1}, \quad i = 2, 3, \dots, N$$
 (7)

where the inequality is strict. Equation  $(7)$  constitutes a "spanning" condition and allows us to select the  $N$ deal maturities as distinct knots in our splines.

#### Bootstrapping

A simple—and widely used—approach involves assuming that the yield curve  $y(T)$  is a continuous piecewise linear spline. This assumption allows for a straightforward solution procedure, known as *boot*strapping. Specifically, we proceed according to the algorithm:

- 1. Let  $y(t_i)$  be known for  $t_i \leq T_{i-1}$ , such that prices for benchmark securities  $1, \ldots, i-1$  are matched.
- 2. Make a guess for  $y(T_i)$ ; linearly interpolate to find  $y(t_i)$ ,  $T_{i-1} < t_i < T_i$ .
- Compute  $V_i$  from the known values of  $P(t_i)$ , 3.  $t_i \leq T_i$ .
- 4. If  $V_i$  equals the market value, stop. Otherwise return to equation (4).
- If  $i < N$ , set  $i = i + 1$  and repeat. 5.

The updating of guesses when iterating over steps 4 and 6 can be handled by a standard one-dimensional root-search algorithm (e.g., the Newton-Raphson or secant methods).

With  $y(T)$  being piecewise linear, the forward curve  $f(T)$  (see equation 6) takes on a discontinuous saw-tooth shape, as shown in Figure 1. It may be tempting to replace the assumption of continuous piecewise linear yields with an assumption of continuous piecewise linear forwards, but such an interpolation rule turns out to be numerically unstable and prone to oscillations. However, we may

instead assume that the forward curve is piecewise flat—or, equivalently, that  $\log P(T)$  is piecewise linear—which again allows for stable application of the bootstrapping principle. For reference, the forward curve resulting from this idea is also shown in Figure 1.

#### *Catmull–Rom Splines*

To ensure that the forward curve stays continuous, we need a yield curve that is at least once differentiable, that is, in  $C^1$ . A common assumption involves setting  $y(T)$  equal to a once differentiable Hermite cubic spline:

$$y(T) = a_{3,i}(T - T_i)^3 + a_{2,i}(T - T_i)^2 + a_{1,i}(T - T_i)$$
$$+ a_{0,i}, \quad T \in [T_i, T_{i+1}] \tag{8}$$

for a series of constants  $a_{3,i}$ ,  $a_{2,i}$ ,  $a_{1,i}$ ,  $a_{0,i}$  to be determined from exogenously given values of  $y(T_i)$ ,  $y(T_{i+1})$ ,  $y'(T_i)$ , and  $y'(T_{i+1})$ . In practice, the first derivatives  $y'(T_i) = dy(T_i)/dT$  are most often specified as finite difference coefficients  $y'(T_i) =$  $(y(T_{i+1}) - y(T_{i-1})) / (T_{i+1} - T_{i-1})$ , giving rise to the so-called *Catmull–Rom spline* [3].

Solving for the Catmull-Rom spline that satisfies equation (4) involves an iterative search for the unknown levels  $y(T_1), \ldots, y(T_N)$ , with each iteration involving a construction of the spline and a computation of  $\mathbf{P} = \left(e^{-y(t_1)t_1}, \ldots, e^{-y(t_M)t_M}\right)$ . Any standard multidimensional root-search algorithm can be applied here. We notice that the Catmull-Rom spline links values of  $y(T)$ ,  $T \in (T_i, T_{i+1})$  to only four knots, namely,  $y(T_{i-1}), y(T_i), y(T_{i+1}), y(T_{i+2}),$ 

![](_page_2_Figure_17.jpeg)

**Figure 1** Yield and forward curve (linear yield bootstrap)

![](_page_3_Figure_1.jpeg)

Figure 2 Yield and forward curve (Catmull–Rom spline)

which simplifies the causality structure in the model and allows for application of "near-bootstrap" methods. Figure 2 shows typical yield and forward curves generated by the Catmull-Rom spline approach, using the same benchmark set as was used to construct Figure 1.

We can easily extend the procedure above beyond Catmull–Rom splines to more complicated  $C^1$  cubic splines in the Hermite class; for instance, it is relatively straightforward to add tension to the Catmull–Rom spline. See [7] for details.

# $C^2$ Cubic Splines

While the spline method introduced in the previous section often produces acceptable yield curves, the method is heuristic in nature and ultimately does not produce a smooth forward curve. To improve on the latter, one alternative is to remain in the realm of cubic splines, but now insist that the curve is twice differentiable everywhere on  $[T_1, T_N]$ . The resulting spline equations are

$$y(T) = \frac{(T_{i+1} - T)^3}{6h_i} y_i'' + \frac{(T - T_i)^3}{6h_i} y_{i+1}'' + (T_{i+1} - T) \left(\frac{y_i}{h_i} - \frac{h_i}{6} y_i''\right) + (T - T_i) \times \left(\frac{y_{i+1}}{h_i} - \frac{h_i}{6} y_{i+1}''\right), \quad T \in [T_i, T_{i+1}]$$
(9)

where  $y''_i = d^2y(T_i)/dT^2$ ,  $y_i = y(T_i)$ , and  $h_i =$  $T_{i+1} - T_i$ . Continuity of the second derivative across

the  $\{T_i\}$  knots requires that  $y''_i$  and  $y_i$ ,  $i = 1, \ldots, N$ , are connected through a tri-diagonal linear system of equations; see [2, 10] for the well-known details. Full specification of this system of equations requires exogenous characterization of behavior at the boundaries  $T_1$  and  $T_N$ . The most common—and often best—specification is that of the *natural spline*, where we set  $y_1'' = y_N'' = 0$ .

As for the Catmull–Rom spline, solving the  $C^2$ cubic spline yield curve that satisfies equation (4) involves a numerical search for the unknown levels<sup>c</sup>  $y_1, \ldots, y_N$ . The fitting problem is typically goodnatured, and virtually all standard root-search packages can tackle it successfully. References [1, 14] use a simple Gauss-Newton scheme, whereas [6] applies a fixed-point-type iteration. Both these simple suggestions are most likely outperformed by the backtracking Newton method or the Broyden method, both of which are described in Press et al. [10]. An example of the forward curve arising from this approach can be seen in Figure 3 (the case  $\sigma = 0$ ).

While the  $C^2$  cubic spline discussed here has attractive smoothness, it is not necessarily an ideal representation of the yield curve. As discussed in [1, 6], among others, twice differentiable cubic spline yield curves are often subject to oscillatory behavior, spurious inflection points, poor extrapolation behavior, and nonlocal behavior when prices in the benchmark set are perturbed. In particular, perturbation of a single benchmark price can cause a slow-decaying "ringing" effect on the  $C^2$  cubic yield curve, with the effect of the perturbation of the benchmark instrument price spilling into the entire yield curve. This behavior is a nuisance in risk-management applications, and is much less present in curves constructed by

![](_page_4_Figure_1.jpeg)

Figure 3 Forward curve (tension spline)

bootstrapping or by the Hermite spline approach.<sup>d</sup> A pragmatic, but inherently inconsistent, approach is to use a  $C^2$  cubic spline for pricing purposes only, but use bootstrapping when stability to perturbations is required. A more sophisticated approach is discussed below.

# $C^2$ Tension Splines

Hermite cubic splines are less prone to nonlocal perturbation behavior than  $C^2$  cubic splines, but accomplish this in a somewhat *ad hoc* fashion by giving up one degree of differentiability. Rather than taking such an extreme step, one wonders whether there may be a way to retain the  $C^2$  feature of the cubic spline, yet still allow control of the curve locality and "stiffness". As it turns out, an attractive remedy to the shortcomings of the pure  $C^2$  cubic spline is to insert some *tension* in the spline, that is, to apply a tensile force to the end points of the spline. Details about this idea can be found in [12]; when applied to the yield Curve setting, the construction involves a modification of the cubic equation (9) for  $y(T)$  to

$$y(T) = \left(\frac{\sinh(\sigma(T_{i+1} - T))}{\sinh(\sigma h_i)} - \frac{T_{i+1} - T}{h_i}\right) \frac{y_i''}{\sigma^2} + \left(\frac{\sinh(\sigma(T - T_i))}{\sinh(\sigma h_i)} - \frac{T - T_i}{h_i}\right) \frac{y_{i+1}''}{\sigma^2} + y_i \frac{T_{i+1} - T}{h_i} + y_{i+1} \frac{T - T_i}{h_i},$$
  
$$T \in [T_i, T_{i+1}] \tag{10}$$

where  $\sigma \ge 0$  is the *tension factor*, and where we recall the definition  $h_i = T_{i+1} - T_i$ .

Among the properties of the tension splines are the facts that setting  $\sigma = 0$  will recover the ordinary  $C^2$  cubic spline, whereas letting  $\sigma \to \infty$  will make the tension spline uniformly approach a linear spline (i.e., the spline we used in the section Bootstrapping). Loosely, we can thus think of a tension spline as a twice differentiable hybrid between a cubic spline and a linear spline. Equally loosely, as we increase  $\sigma$ , inflections and ringing in the cubic spline are gradually "stretched" out of the curve, accompanied by rising (absolute values of) second derivatives at the knots.

More details on tension splines in yield Curve application can be found in [1], which also contains a discussion of computationally efficient local spline bases and the usage of  $T$ -dependent tension factors for additional curve control. For our purposes here, it suffices to note that equation  $(10)$  is structurally similar to equation (9), and also allows for a tri-diagonal matrix equation linking  $y''_i$  and  $y_i$ ,  $i = 1, \ldots, N$ . The solution procedure for the yield curve is therefore the same as in the section  $C^2$  Cubic Splines. Figure 3 illustrates the effect of varying the tension factor on the shape of the instantaneous forward curve  $f(t)$ ; notice how increasing the tension parameter gradually moves us from smooth cubic spline behavior to bootstrap behavior. Examples of how the tension parameter dampens ringing in the forward curve after input perturbations can be found in [1].

#### Nonparametric Methods

The techniques we outlined so far generally suffice for the construction of a discount curve from a "clean" set of non-duplicate benchmark securities, including the carefully selected set of liquid staggered-maturity deposits, futures, and swaps, that most banks assemble for the purpose of constructing a Libor yield curve. In some settings, however, the benchmark set may be significantly less well structured, involving illiquid securities with little order in their cash-flow timing and considerable noise in their prices. This situation may, say, arise when one attempts to construct a yield curve from corporate bonds.

When the input benchmark set is noisy, a straight solution of (4) may be erratic or may not exist. To overcome this, and to reflect that noise in the input data may make us content to solve (4) only to within certain error bounds, we now proceed to replace this equation by minimization of a penalized least-squares norm. Specifically, define the space  $\mathcal{A} = C^2[t_1, t_M]$ of all twice differentiable functions  $[t_1, t_M] \to \mathbb{R}$  and introduce the  $M$ -dimensional discount vector

$$\mathbf{P}(y) = \left( e^{-y(t_1)t_1}, \dots, e^{-y(t_M)t_M} \right) \tag{11}$$

Also, let **W** be a diagonal  $N \times N$  weighting matrix. Then, as our best estimate  $\hat{y}$  of the yield curve we may use

$$\hat{y} = \arg\min_{y \in \mathcal{A}} \mathcal{I}(y) \tag{12}$$
$$\mathcal{I}(y) \equiv \frac{1}{N} \left( \mathbf{V} - \mathbf{c} \mathbf{P}(y) \right)^{\top} \mathbf{W}^{2} \left( \mathbf{V} - \mathbf{c} \mathbf{P}(y) \right)$$
$$+ \lambda \left( \int_{t_{1}}^{t_{M}} \left[ y''(t)^{2} + \sigma^{2} y'(t)^{2} \right] dt \right) \tag{13}$$

where  $\lambda$  and  $\sigma$  are positive constants. The norm  $\mathcal{I}(y)$ consists of three separate terms:

A least-squares penalty term

$$\frac{1}{N} \left( \mathbf{V} - \mathbf{c} \mathbf{P}(y) \right)^{\top} \mathbf{W}^2 \left( \mathbf{V} - \mathbf{c} \mathbf{P}(y) \right)$$
$$= \frac{1}{N} \sum_{i=1}^{N} W_i^2 \left( V_i - \sum_{j=1}^{M} c_{ij} e^{-y(t_j)t_j} \right)^2 \tag{14}$$

where  $W_i$  is the *i*th diagonal element of **W**. This term is an outright precision-of-fit norm and measures the degree to which the constructed discount curve can replicate input security prices. The weight-matrix  $W$  can be used to express the relative importance of the various securities in the benchmark set, or to turn price errors into yield errors.

- A weighted smoothness term  $\lambda \int_{t_1}^{t_M} y''(t)^2 dt$ , penalizing high second-order gradients of  $y$  to avoid kinks and discontinuities.
- A weighted curve-length term  $\lambda \sigma^2 \int_{t_1}^{t_M} y'(t)^2 dt$ ,  $\bullet$ penalizing oscillations and excess convexity/ concavity.

To construct the yield curve, we have replaced the nonlinear root-search problems encountered in the section Yield Curve Fitting with  $N$ -knot Splines with the functional optimization problem (12). Fortunately, the latter approach can be linked to that of the former by the following result, which can be shown by variational methods.

**Proposition 1** The curve  $\hat{y}$  that satisfies equation (12) is a natural exponential tension spline with tension factor  $\sigma$  and knots at all cash-flow dates  $t_1, t_2, \ldots, t_M.$ 

Proposition 1 establishes that the curve we are looking for is a tension spline with tension factor  $\sigma$ , but does not, in itself, allow us to identify the optimal spline directly, beyond the fact that (i) it is a natural spline with boundary conditions  $y''(t_1) =$  $y''(t_M) = 0$ ; (ii) it has knots at all  $t_i$ . Identification of the correct tension spline involves solving for unknown levels  $y(t_1), y(t_2), \ldots, y(t_M)$  to directly optimize equation (13). This optimization problem can be solved by standard methods, for example, by use of the Levenberg-Marquardt method, or the Gauss–Newton method in  $[1, 14]$ .

**Remark 1** If we let  $\sigma = 0$ , the solution to the optimization problem becomes a *cubic smoothing spline;* see [14] for more details on this case.

#### Choice of Smoothing Parameter

The parameter  $\lambda$  may be specified exogenously by the user, as a way to provide a trade-off between pricing accuracy and curve regularity. In practice, however, a good magnitude of  $\lambda$  may sometimes be hard to ascertain by inspection, and a procedure to estimate *λ* directly from the data is often useful. One possibility is to use a cross-validation approach, either outright or through the more efficient generalized cross-validation (GCV) criterion in [4]. Some results along these lines can be found in [14], for instance. A more pragmatic approach is to specify a target value for the least-squares term in equation (13), iterating on *λ* until the target is met; in general, we would expect the least-squares error term to increase monotonically with *λ*. Most trading desks should have little difficulty specifying a meaningful least-squares target error directly from, say, observed bid–offer spreads. We note that the target error value may be set to zero, if a perfect fit to benchmark securities is required.

# **Special Topics**

While our discussion of curve construction algorithms generally relied on the notion that the forward curve should ideally be *smooth*, there may be circumstances where we want to make exceptions. For instance, it may be reasonable to expect instantaneous forwards to jump on or around meetings of monetary authorities, such as the Federal Reserve in the United States. In addition, other "special" situations may exist that might warrant introduction of discontinuities into the forward curve. A well-known example is the turn-of-year (TOY) effect where shortdated loan premiums spike for loans between the last business day of the year and the first business day of the next year. One common way of incorporating TOY-type effects is to exogenously specify an *overlay curve f (t)* on the instantaneous forward curve. Specifically, the forward curve *f (t)* is written as

$$f(t) = \epsilon_f(t) + f^*(t) \tag{15}$$

where *f (t)* is user-specified—and most likely contains discontinuities around special events dates and *f* <sup>∗</sup>*(t)* is unknown. The yield Curve construction problem is then subsequently applied to the construction of *f* <sup>∗</sup>*(t),* using algorithms such as those discussed earlier.

We should note that the curve construction algorithms outlined in this article are meant only for single-currency applications. In a setting with multiple currencies, care must be taken to ensure that discount curves in different currencies are properly related, in the sense that they together replicate the prices for foreign exchange forward agreements, as well as cross-currency floating–floating basis swaps. In general, the ability to match currency markets requires that the discount curve and the forward rate curve (e.g., the Libor curve) be separated into two entities separated by a cross-currency spread; see [5]. It is normally straightforward to embed a singlecurrency yield Curve solver into a cross-currency setting, for instance, by means of an iterative adjustment to the price vector **V** in equation (4). Similar techniques can be used to accommodate the so-called *tenor* basis, that is, the fact that different Libor tenors (e.g., 3-month versus 6-month) in practice do not swap flat against each other.

# **Acknowledgments**

The authors are grateful for the suggestions of Brian Ostrow, Igor Polonsky, David Price, and Branko Radosavljevic.

# **End Notes**

a*.* Owing to their daily mark-to-market provision, Eurodollar futures contracts do not allow for a pricing expression of the form (1), so a preprocessing step is normally employed to convert the futures rate quote to a forward rate quote. *See* **Eurodollar Futures and Options**.

b*.* See, for example, [13] for a discussion of the pitfalls associated with curve interpolators that work directly on the discount function *P (T )* (as in [8]).

c*.* A more contemporary approach replaces this search with a search for coefficients in a local spline basis. Andersen [1] contains more details on this.

d*.* Intuitively, this is because linear and Hermite splines link values of *y(T )* to only a few (2 and 4, respectively) of the values *y(Ti)*, *i* = 1*,...,N*. The *C*<sup>2</sup> cubic spline, on the other hand, links *y(T )* to *all y(Ti), i* = 1*,...,N*.

# **References**

- [1] Andersen, L. (2006). Discount curve construction with tension splines, *Review of Derivatives Research* **10**(3), 227–267.
- [2] de Boor, C. (2001). *A Practical Guide to Splines (revised edition)*, Springer Verlag, New York.
- [3] Catmull, E. & Rom, R. (1974). A class of local interpolating spline, in *Computer Aided Geometric Design*, R.E. Barnhill & R.F. Riesenfled, eds, Academic Press, New York.

# **8 Yield Curve Construction**

- [4] Craven, P. & Wahba, G. (1979). Smoothing noisy data with spline functions: estimating the correct degree of smoothing by the method of generalized crossvalidation, *Numerische Matematik* **31**, 377–403.
- [5] Fruchard, E., Zammouri, C. & Willems, E. (1995). Basis for change, *RISK Magazine* October, 70–75.
- [6] Hagan, P. & West, G. (2006). Interpolation methods for yield curve construction, *Applied Mathematical Finance* **3**(2), 89–129.
- [7] Kochanek, D. & Bartels, R. (1984). Interpolating splines with local tension, continuity, and bias control, *ACM SIGGRAPH* **18**(3), 33–41.
- [8] McCulloch, J.H. (1975). The tax-adjusted yield curve, *Journal of Finance* **30**, 811–830.
- [9] Nelson, C.R. & Siegel, A.F. (1987). Parsimonious modeling of yield curves, *Journal of Business* **60**, 473–489.
- [10] Press, W., Teukolsky, S., Vetterling, W. & Flannery, B. (1992). *Numerical Recipes in C*, Cambridge University Press.
- [11] Schoenberg, I. (1973). *Cardinal Spline Interpolation*. SIAM CBMS-NSF Regional Conference Series in Applied Mathematics 12.

- [12] Schweikert, D.G. (1966). An interpolating curve using a spline in tension, *Journal of Mathematics and Physics* **45**, 312–317.
- [13] Shea, G.S. (1984). Pitfalls in smoothing interest rate terms structure data: equilibrium models and spline approximation, *Journal of Financial and Quantitative Analysis* **19**, 253–269.
- [14] Tanggaard, C. (1997). Nonparametric smoothing of yield curves, *Review of Quantitative Finance and Accounting* **9**, 251–267.

# **Related Articles**

**Eurodollar Futures and Options**; **Hedging of Interest Rate Derivatives**; **LIBOR Rate**.

#### LEIF B.G. ANDERSEN & VLADIMIR V. PITERBARG
# Heath-Jarrow-Morton Approach

## Basics

We consider a financial market model living on a filtered probability space  $(\Omega, \mathcal{F}, F, P)$ , where  $F =$  $\{\mathcal{F}_t\}_{t>0}$  and P is the objective probability measure. The basis is assumed to carry a standard *m*-dimensional *P*-Wiener process  $\bar{W}$ .

Our main object of study is the zero coupon bond market, and we denote the price by  $p(t, T)$ , at t, of a zero coupon bond maturing at  $T$ .

We define, as usual, the *instantaneous forward rate* with maturity  $T$ , contracted at  $t$ , by

$$f(t,T) = -\frac{\partial \log p(t,T)}{\partial T} \tag{1}$$

The instantaneous *short rate at time*  $t$  is defined by  $r(t) = f(t, t).$ 

## The HIM Framework

We now turn to the specification of the Heath-Jarrow-Morton (HJM) framework (see [13]). We start by specifying everything under a given objective measure  $P$ .

**Assumption 1** We assume that, for every fixed  $T >$ 0, the forward rate  $f(\cdot, T)$  has a stochastic differential, which, under the objective measure  $P$ , is given  $bv$ 

$$df(t, T) = \alpha(t, T) dt + \sigma(t, T) d\bar{W}_t \qquad (2)$$

$$f(0,T) = f_{\text{in}}(0,T) \tag{3}$$

where, for each fixed T,  $\alpha(\cdot,T)$  and  $\sigma(\cdot,T)$  are adapted processes. The curve  $f_{\rm in}$  is the initially observed forward rate curve.

It is important to note that the HJM approach to model the evolution of interest rates is not a proposal of a specific model, like, for example, the Cox-Ingersoll-Ross model (see Cox-Ingersoll-Ross (CIR) Model). It is, instead, a frame*work* that is used for analyzing interest-rate models. In fact, *every* interest-rate model can be equivalently formulated in forward rate terms. To turn the HJM

framework into a *model*, we have to specify the volatility and drift structure, that is, we have to specify  $\sigma$  and  $\alpha$ .

There are two main advantages of the HJM approach: First, the forward rate volatility structure  $\sigma(t,T)$  is an *input* to the model, whereas in a factor model such as a short rate model (see Term **Structure Models**), it would be an output. Second, by using the observed forward rate curve as an initial condition, we automatically obtain a perfect fit to the observed yield curve.

The first main result shows how the bond price dynamics are determined by the forward rate dynamics.

**Proposition 1** If the forward rate dynamics are given by equation (2) then the induced bond price dynamics are given by

$$dp(t, T) = p(t, T) \{r(t) + A(t, T)$$
  
+  $\frac{1}{2} \|S(t, T)\|^2 \} dt$   
+  $p(t, T)S(t, T) d\bar{W}_t$  (4)

*where*  $\|\cdot\|$  *denotes the Euclidean norm, and* 

$$\begin{cases}\nA(t,T) = -\int_{t}^{T} \alpha(t,s) \, \mathrm{d}s \\
S(t,T) = -\int_{t}^{T} \sigma(t,s) \, \mathrm{d}s\n\end{cases} \tag{5}$$

### Absence of Arbitrage

Using proposition 1 above, an application of the Girsanov Theorem gives us the following basic result concerning absence of arbitrage.

Theorem 1 (HJM Drift Condition). Assume that the family of forward rates is given by equation  $(2)$ . Then the induced bond market is arbitrage free if and only if there exists a d-dimensional column-vector *process*  $\lambda(t) = [\lambda_1(t), \ldots, \lambda_d(t)]^*$  with the property that for all  $T > 0$  and for all  $t < T$ , we have

$$\alpha(t,T) = \sigma(t,T) \int_t^T \sigma(t,s)^* \, \mathrm{d}s - \sigma(t,T)\lambda(t) \quad (6)$$

In these formulas  $*$  denotes transpose.

## *Martingale Modeling*

In many cases, the specification of the forward rate dynamics is done directly under a martingale measure  $Q$  as

$$df(t, T) = \alpha(t, T) dt + \sigma(t, T) dW_t$$
  
$$f(0, T) = f_{\text{in}}(0, T)$$
 (7)

where  $W$  is a (*d*-dimensional) *Q*-Wiener process. In this setting, absence of arbitrge is no longer an issue, but we have to give conditions that guarantee that all the induced bond price processes have the correct martingale dynamics, that is, short rate as their local rate of return. This directly follows from the earlier result by setting  $\lambda = 0$ .

**Proposition 2** (HJM Drift Condition). *Under the* martingale measure Q, the processes  $\alpha$  and  $\sigma$  must satisfy the following relation, for every  $t$  and every  $T \geq t$ .

$$\alpha(t,T) = \sigma(t,T) \int_{t}^{T} \sigma(t,s)^{*} \, \mathrm{d}s \tag{8}$$

Thus when specifying the forward rate dynamics, (under  $Q$ ) we may freely specify the volatility. The drift is then uniquely determined. In practical applications, one thus has to specify the number  $d$  of Wiener processes as well as the volatility structure.

It is common to assume a deterministic volatility structure, and then try to estimate this as well as the number  $d$  by principal component analysis. The deterministic volatility is very tractable since it will lead to Gaussian forward rates (see Gaussian Interest-Rate Models) and lognormal bond prices. Analytical formulas for bond options are easily available.

The HJM approach has been extended to include a driving marked point process in  $[4]$ , a random measure [3], a Levy process [8], a Gaussian random field [15], and a Levy field [1].

#### The Musiela Parameterization

In many applications, it is more natural to use time  $to$ maturity, rather than time  $of$  maturity, to parameterize bonds and forward rates, and this approach was first described in [6] and [16]. If we denote time to maturity by x, then we have  $x = T - t$ , and in terms of  $x$ , the forward rates are defined as follows.

**Definition 1** *For all*  $x \ge 0$  *the forward rates*  $r_t(x)$ are defined by the relation

$$r_t(x) = f(t, t+x) \tag{9}$$

and we denote by  $r_t$  the forward rate curve  $x \mapsto$  $r_t(x)$  at time t. We can thus view r as a process taking values in some Hilbert space  $\mathcal{H}$  of forward rate curves.

Suppose now that we have the standard HJMtype model for the forward rates under a martingale measure  $O$ 

$$df(t, T) = \alpha(t, T) dt + \sigma_0(t, T) dW_t \qquad (10)$$

where  $\sigma_0$  denotes the HJM volatility structure. The question is to find the Q-dynamics for  $r(t, x)$ , and we have the following result.

**Proposition 3** (Musiela parameterization). *Assume* that the forward rate dynamics under  $O$  are given by (10). Then

$$dr_t(x) = \left\{ \frac{\partial}{\partial x} r_t(x) + D(t, x) \right\} dt + \sigma(t, x) dW_t$$
(11)

where

$$\sigma(t,x) = \sigma_0(t,t+x)$$
  
 
$$D(t,x) = \sigma(t,x) \int_0^x \sigma(t,s)^* ds \qquad (12)$$

If the volatility  $\sigma$  is of the simple deterministic form  $\sigma_t(x) = \sigma(x)$ , then the Musiela equation mentioned above takes the form

$$dr_t = \{ \mathbf{F}r_t + D \} dt + \sigma dW_t$$

where  $D(x) = \sigma(x) \int_0^x \sigma(s) ds$  and the operator **F** is given by  $\partial/\partial x$ . In this case, the forward rate equation is an infinite dimensional linear stochastic differential equation (SDE) on  $\mathcal{H}$  with formal solution

$$r_t = \mathbf{e}^{\mathbf{F}t}r_0 + \int_0^t \mathbf{e}^{\mathbf{F}(t-s)}D \, \mathrm{d}s + \int_0^t \mathbf{e}^{\mathbf{F}(t-s)}\sigma \, \mathrm{d}W_s \tag{13}$$

where the semigroup  $e^{Ft}$  is left translation, that is,  $e^{\mathbf{F}t} f(x) = f(t+x).$ 

## **Geometric Interest Rate Theory**

Assume that the volatility process  $\sigma$  is of the Markovian form  $\sigma_t(x) = \sigma(r_t, x)$ . Then the Musiela equation for the  $r$  process is an infinite dimensional SDE and we write it compactly as

$$dr_t = \mu(r_t) dt + \sigma(r_t) dW(t) \qquad (14)$$

where

$$\mu(r,x) = \frac{\partial}{\partial x}r(x) + D(r,x)$$
$$D(r,x) = \sigma(r,x)\int_0^x \sigma(r,s) \, \mathrm{d}s \tag{15}$$

We can thus view  $\mu$  and  $\sigma$  as vector fields on  $\mathcal{H}$ , and we now formulate a couple of natural problems:

1. Consider a given parameterized family  $\mathcal{G}$  of forward rate curves, such as the Nelson-Siegel family, where forward rates are parameterized as

$$G(z, x) = z_1 + z_2 e^{-z_3 x} + z_4 x e^{-z_3 x} \tag{16}$$

where  $z_1, \ldots, z_4$  are the parameters. The question is now under which conditions this family is consistent with the dynamics of the interestrate model mentioned above? Here consistency is interpreted in the sense that, given an initial forward rate curve in  $\mathcal{G}$ , the interest-rate model will (with probability 1) produce forward rate curves belonging to the given family  $\mathcal{G}$ .

2. When does the given, inherently infinite dimensional, interest-rate model admit a finite dimensional Markovian state space realization, that is, when can the  $r$  process be realized by a system of the form

$$dZ_t = a (Z_t) dt + b (Z_t) dW_t$$
$$r_t(x) = G (Z_t, x)$$
(17)

where  $Z$  (interpreted as the state vector process) is a finite dimensional diffusion,  $a(z)$ ,  $b(z)$  and  $G(z, x)$  are deterministic functions and W is the same Wiener process as in equation  $(11)$ .

#### Consistency

A finitely parameterized family of forward rate curves is a real-valued function of the form  $G(z, x)$  where z lies in some open subset of  $R^k$ , that is, for each fixed parameter vector  $z$ , we have the forward rate curve  $x \mapsto G(z, x)$ . A typical example is the Nelson-Siegel forward curve family in equation (16). The mapping  $G$  can also be viewed as a mapping  $G: \mathcal{Z} \to \mathcal{H}$ , and we now define the *forward curve manifold*  $\mathcal{G}$  as the set of all forward rate curves produced by this family, that is.,  $\mathcal{G} = \text{Im}(G)$ . The main result concerning consistency is as follows (see [2]).

**Theorem 2** (Consistency). *The forward curve*  $manifold \mathcal{G}$  is consistent with the forward rate process if and only if,

$$G'_{x}(z) + D(r) - \frac{1}{2}\sigma'_{r}(r)\sigma(r) \in \text{Im}[G'_{z}(z)]$$
$$\sigma(r) \in \text{Im}[G'_{z}(z)] \quad (18)$$

*hold for all*  $z \in \mathcal{Z}$  *with*  $r = G(z)$ *, where*  $D$  *is defined* in equation  $(15)$ 

Here,  $G'_z$  and  $G'_x$  denote the Frechet derivative of  $G$  with respect to  $z$  and  $x$ , respectively.

The invariance problem was originally posed and studied in [2] and then extended and studied in great depth in [9] and [10]. In particular, it is shown in [9] that no nondegenerate arbitrage-free forward rate model is consistent with the Nelson-Siegel family.

#### Finite Dimensional Markovian Realizations

The existence of finite dimensional Markovian realizations (FDR) was first studied in [7] and [17] where sufficient conditions were given for particular choices of volatility structures (see Markovian Term Structure Models) for a detailed discussion of these special cases and more references. General necessary and sufficient results were first obtained in  $[5]$  and extended in  $[11]$ . For an arbitrary SDE in Hilbert space (with the forward rate SDE as a special case) of the form

$$dr_t = \mu(r_t) dt + \sigma(r_t) dW_t \tag{19}$$

the main general result is as follows.

**Theorem 3** The infinite dimensional SDE above admits an FDR if and only if the Lie algebra generated by the vector fields  $\mu - 1/2\sigma'\sigma$  and  $\sigma$  (where  $\sigma'$ denotes the Frechet derivative) has finite dimension *(evaluated pointwise) in a neighborhood of the initial point r*0*.*

All known examples in the literature are easy consequences of this general result, which can also be extended to stochastic volatility.

A special case of a finite dimensional realization is when a HJM model generates a Markovian short rate process. This corresponds to the case of a two-dimensional realization with running time and short rate as *Z*-factors. For the case of a short rate dependent volatility, it was shown in [14] that this occurs if and only if the model is affine. This result has a remarkable extension in [12], where it is shown that all models admitting finite dimensional realizations are, in fact, affine.

## **References**

- [1] Albeverio, S., Lytvynov, A. & Mahnig, A. (2004). A model of the term structure of interest rates based on Levy fields, *Stochastic Processes and Their Applications* **114**(2), 251–263.
- [2] Bjork, T. & Christensen, B. (1999). Interest rate dynam- ¨ ics and consistent forward rate curves, *Mathematical Finance* **9**(4), 323–348.
- [3] Bjork, T., Di Masi, G., Kabanov, Y. & Runggaldier, W. ¨ (1997). Towards a general theory of bond markets, *Finance and Stochastics* **1**, 141–174.
- [4] Bjork, T., Kabanov, Y. & Runggaldier, W. (1995). Bond ¨ market structure in the presence of a marked point process, *Mathematical Finance* **7**(2), 211–239.
- [5] Bjork, T. & Svensson, L. (2001). On the existence of ¨ finite dimensional realizations for nonlinear forward rate models, *Mathematical Finance* **11**(2), 205–243.

- [6] Brace, A. & Musiela, M. (1994). A multifactor Gauss Markov implementation of Heath, Jarrow, and Morton, *Mathematical Finance* **4**, 259–283.
- [7] Cheyette, O. (1996). *Markov Representation of the Heath–Jarrow–Morton Model*, BARRA, Preprint.
- [8] Eberlein, E. & Raible, S. (1999). Term structure models driven by general Levy processes, *Mathematical Finance* **9**(1), 31–53.
- [9] Filipovic, D. (1999). A note on the Nelson-Siegel family, ´ *Mathematical Finance* **9**(4), 349–359.
- [10] Filipovic, D. (2001). ´ *Consistency Problems for Heath– Jarrow–Morton Interest Rate Models*, *Springer Lecture Notes in Mathematics*, Springer Verlag, Vol. 1760.
- [11] Filipovic, D. & Teichmann, J. (2003). Existence of ´ invariant manifolds for stochastic equations in infinite dimension, *Journal of Functional Analysis* **197**, 398–432.
- [12] Filipovic, D. & Teichmann, J. (2004). On the geometry ´ of the term structure of interest rates, *Proceedings of the Royal Society* **460**, 129–167.
- [13] Heath, D., Jarrow, R. & Morton, A. (1992). Bond pricing and the term structure of interest rates: a new methodology for contingent claims valuation, *Econometrica* **60**, 77–105.
- [14] Jeffrey, A. (1995). Single factor Heath–Jarrow–Morton term structure models based on Markov spot interest rate dynamics, *Journal of Financial and Quantitative Analysis* **30**, 619–642.
- [15] Kennedy, D. (1994). The term structure of interest rates as a Gaussian random field, *Mathematica Finance* **4**, 247–258.
- [16] Musiela, M. (1993). *Stochastic PDE*:*s and term structure models*, Preprint.
- [17] Ritchken, P. & Sankarasubramanian, L. (1995). Volatility structures of forward rates and the dynamics of the term structure, *Mathematical Finance* **5**(1), 55–72.

TOMAS BJORK ¨
# **Markov Functional** Models

Market models (see LIBOR Market Model) are formulated directly in terms of market observable rates. such as LIBORs (see LIBOR Rate), their volatilities, and correlations. They were the first models that could calibrate exactly to Black's formula for pricing liquid instruments for all strikes. Though the models provide an excellent framework for selecting and understanding a model, and have become a benchmark in the market place, they do have one significant drawback. An accurate implementation of a market model can only be done by simulation because of the high dimensionality of the model. This is true even when there is only one stochastic driver.

In this article, we describe models that can fit the observed prices of liquid instruments in a similar fashion to the market models, but which also have the advantage that derivative prices can be calculated just as efficiently as in the most tractable *short-rate* model (see Term Structure Models). To achieve this, we consider the general class of Markovfunctional interest-rate models [4, 8], which, as we shall discuss, can be specified using the numeraire approach restricted to a finite time horizon. The defining characteristic of Markov-functional models is that pure discount bonds prices are at any time a function of some low-dimensional process that is Markovian in some martingale measure. This ensures that the implementation is efficient since it is only necessary to track the driving process, something that is particularly important for Bermudan-style products. Market models do not possess this property for some low-dimensional Markov process and this is the obstacle to their efficient implementation.

## **Numeraire Approach to Specifying Interest-rate Models**

Let  $\{\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P}\}$  be a filtered probability space. Denote by  $D_{tT}$  the value at t of a pure discount bond with maturity  $T$ , an asset that pays a unit amount on its maturity date. There are several ways to model the complete term structure of pure discount bonds,  $\{D_{tT} :$  $0 < t < T < \infty$  and it is not necessary to specify the model under the "real-world" measure  $\mathbb{P}$ . The numeraire approach follows from the definition of a numeraire pair. Let  $\mathbb{N}$  be an *equivalent martingale measure* (see Equivalent Martingale Measures) corresponding to a *numeraire*  $N$  (see Change of Numeraire). Then any numeraire-rebased asset is a martingale under the measure  $\mathbb{N}$ .

Noting that  $D_{TT} = 1$ , we see that

$$D_{tT} = \mathbb{N}_{t} \mathbb{E}_{\mathbb{N}} \left[ N_{T}^{-1} \mid \mathcal{F}_{t} \right] \tag{1}$$

Thus, once we have specified the numeraire pair  $(N, \mathbb{N})$  and the filtration  $\{\mathcal{F}_t\}$ , we have defined a term structure model under the equivalent martingale measure  $\mathbb{N}$ .

For practical applications, it is usual to restrict attention to a finite time horizon,  $0 < t < T$ . Here, to specify a model using the numeraire approach, in addition to knowledge of the numeraire, we need to know its joint distribution under  $\mathbb{N}$  with the pure discount bonds on some boundary curve. In applications that we have encountered, it is sufficient to take these bonds to be  $D_{TS}$ , for  $S \in [T, T']$  for some fixed  $T' \geq T$ . Then we can again use the martingale property of numeraire-rebased assets to recover the pure discount bonds at earlier times for maturities up to  $T'$ .

#### **Markov-functional Models**

We now give a formal definition of a Markovfunctional model. We restrict attention to a finite time horizon and so the definition includes the boundary curve mentioned above. This definition is very general and, if we allow the process driving the model to be of high dimension, the definition will encompass nearly all models of practical interest (including market models). The real spirit of Markovfunctional modeling is explained in the next section when we discuss how to recover the prices of calibrating liquid instruments *via* a functional sweep.

**Definition 1** An interest-rate model is said to be Markov-functional if there exists some numeraire pair  $(N, \mathbb{N})$  and some process x such that

- 1. the process  $x$  is a (time-inhomogeneous) Markov process under the measure  $\mathbb{N}$ ;
- 2. the pure discount bonds are of the form

$$D_{tS} = D_{tS}(x_t), \ 0 \le t \le \min\{S, T\} \qquad (2)$$

From our discussion of the numeraire approach, we see that to completely specify a general Markovfunctional model, it is sufficient to specify the joint law of the numeraire N and the process x under  $\mathbb{N}$ , and the functional form of the discount factors on the boundary. This observation forms the basis for setting up a Markov-functional model in practice.

#### Recap of the Standard Markov-functional Approach

The formal definition above tells us the general properties of the model we wish to develop, but nothing about the practicalities of how to set up a model for a particular pricing problem. Here, we summarize the standard case in which the driving process, denoted by  $x$ , is chosen to be of low dimension and Gaussian. This ensures that the model is efficient to implement. We comment on the choice of covariance structure for  $x$  below. Assuming  $x$  has been chosen, the practical problem we now seek to address is that of setting up a model that is arbitragefree and calibrates well to a set of vanilla instruments appropriate for the product we wish to price. In this article, we restrict our discussion to a special case-the LIBOR Markov-functional model in the terminal measure. For further details on practical aspects of this model, see  $[4, 6, 8]$  and  $[10]$ .

As in a LIBOR market model (see LIBOR Market **Model**), we assume we have a set of contiguous forward LIBORs denoted by  $L^i$  for  $i = 1, \ldots, n$ corresponding to tenor structure  $T_1, \ldots, T_{n+1}$ . We write  $S_i := T_{i+1}$  for  $i = 1, \ldots, n$  and so  $L^i$  is the LIBOR corresponding to the period  $[T_i, S_i]$ .

In this section, we use  $\mathbb{N}$  to denote the terminal measure corresponding to taking the bond  $D_{S_n}$ as numeraire and  $E$  to denote expectations in this measure.

Consider the problem of how to choose the functional forms so that the resulting model calibrates accurately to the prices of the set of caplets (equivalently digital caplets) corresponding to the forward LIBORs  $L^1, \ldots, L^n$ . The model is actually only specified on a grid. That is, we specify the functional forms  $D_{T_iT_i}(x_{T_i})$  for  $1 \le i < j \le n+1$ , since this is all that is (typically) needed in practice. Note that here all we need to recover these discount factors are the functional forms of the numeraire for times  $T_1, \ldots, T_n$ . The functional forms are derived numerically from market prices and the martingale properties necessary to make the model arbitrage-free.

The algorithm for finding the functional forms works back iteratively from the terminal time  $T_n$ . Suppose we have reached  $T_i$ , having already found the functional forms  $D_{T_kS_n}(x_{T_k}), k = i + 1, \ldots,$  $n + 1$ . Trivially, this is true when  $i = n$  as there is nothing to know since  $D_{T_{n+1}S_n}(x_{T_{n+1}}) = 1$ . Then from the martingale property of numeraire-rebased assets we can find

$$\hat{D}_{T_i T_{i+1}}(x_{T_i}) := \frac{D_{T_i T_{i+1}}(x_{T_i})}{D_{T_i S_n}(x_{T_i})} \\
= \mathbb{E}\left[\frac{1}{D_{T_{i+1} S_n}}(x_{T_{i+1}}) \mid x_{T_i}\right] \n$$
(3)

Noting, by definition, that

$$L_{T_i}^i = \frac{1 - D_{T_i T_{i+1}}}{\alpha_i D_{T_i T_{i+1}}} \tag{4}$$

where  $\alpha_i$  is the accrual factor for the interval  $[T_i, S_i]$ , it follows that

$$D_{T_i S_n}(x_{T_i}) = \frac{1}{\hat{D}_{T_i T_{i+1}}(x_{T_i})(1 + \alpha_i L_{T_i}(x_{T_i}))}$$
(5)

Thus we see that to determine the functional form for the numeraire at time  $T_i$ ,  $D_{T_iS_n}(x_{T_i})$ , it is sufficient to find the functional form for  $L_{T_i}^i(x_{T_i})$ . Equivalently, it is sufficient to find the off-diagonal discount factor  $D_{T_i T_{i+1}}(x_{T_i}).$ 

We begin with the case in which the process  $x$ is one dimensional. Here, we view the process  $x$  as capturing the overall level of interest rates.

**One-dimensional Case.** In setting up our model, we make the assumption that the  $i$ th forward LIBOR at time  $T_i$ ,  $L_{T_i}^i$ , is a monotonic increasing function of the variable  $x_{T_i}$ , that is, we assume that  $L_{T_i}^i$  =  $f^{i}(x_{T_{i}})$ , for some monotonic increasing function  $f^{i}$ . The functional forms are found using market prices of digital caplets. This is equivalent to calibrating to caplets as we can recover the price of a caplet with strike  $K$ ,  $C^{i}(K)$ , from the prices of digital caplets:

$$C^{i}(K) = \int_{K}^{\infty} V^{i}(\hat{K}) d\hat{K} \tag{6}$$

where  $V^{i}(K)$  denotes the market value of the digital caplet with strike K (setting at  $T_i$ , paying at  $S_i$ ). In an arbitrage-free model, we must have

$$V^{i}(K) = D_{0S_{n}} \mathbb{E}\left[\frac{D_{T_{i}S_{i}}}{D_{T_{i}S_{n}}} \mathbf{1}\{L^{i}_{T_{i}} > K\}\right] \tag{7}$$

Choose a grid of values  $x^*$  and for each  $x^*$  calculate

$$J_0^i(x^*) := D_{0S_n} \mathbb{E}\left[\frac{D_{T_iS_i}}{D_{T_iS_n}}(x_{T_i})\mathbf{1}\{x_{T_i} > x^*\}\right] \tag{8}$$

$$:= D_{0S_n} \mathbb{E}\bigg[\mathbb{E}\bigg[\frac{D_{T_{i+1}S_i}}{D_{T_{i+1}S_n}}(x_{T_{i+1}})|x_{T_i}\bigg] \mathbf{1}\{x_{T_i} > x^*\}\bigg]$$
(9)

We can do this (numerically) from what we already know, having calibrated the model at all  $T_i$ ,  $j > i$ . Now find the value  $K(x^*)$  such that  $V^i(K(x^*)) =$  $J_0^i(x^*)$ . Equating equations (7) and (9) we find that

$$D_{0S_n} \mathbb{E}\left[\frac{D_{T_iS_i}}{D_{T_iS_n}}(x_{T_i})\mathbf{1}\{L_{T_i}^i(x_{T_i}) > K(x^*)\}\right]$$
  

$$= V^i(K(x^*))$$
  

$$= J_0^i(x^*)$$
  

$$= D_{0S_n} \mathbb{E}\left[\frac{D_{T_iS_i}}{D_{T_iS_n}}(x_{T_i})\mathbf{1}\{x_{T_i} > x^*\}\right]$$
  

$$= D_{0S_n} \mathbb{E}\left[\frac{D_{T_iS_i}}{D_{T_iS_n}}(x_{T_i})\mathbf{1}\{L_{T_i}^i(x_{T_i}) > L_{T_i}^i(x^*)\}\right]$$
  
(10)

Under the assumption that  $L_{T_i}^i(x)$  is increasing in x, we can now conclude that  $L_{T_i}^i(x^*) = K(x^*)$ , thus, repeating this on a grid of values  $x^*$ , we have derived the required functional form.

Multidimensional Case. This is a straightforward generalization of the one-dimensional case. The key to this extension is to ensure in the generalization that we

- 1. retain the univariate and monotonicity properties that were required to make the functional fitting efficient;
- capture desired correlation/covariance 2. the structure.

To do this, we introduce the idea of a *prior model*. The prior model expresses each LIBOR as a function of the driving Markov process  $x$ , which is now of dimension  $k > 1$ . This prior model is chosen to capture the basic dynamics of the market, but may admit arbitrage. We discuss the choice of a prior model based on a market model below. Once the prior model is chosen, the approach now is to regard the Markov-functional sweep as a (small) perturbation of this prior model, which removes the arbitrage.

In particular, we assume that the functional dependence of  $L_{T_i}^i$  on the multidimensional  $x_{T_i}$  is only via the prior model LIBOR  $\tilde{L}^i_{T_i}$ . Thus

$$L_{T_i}^i(x_{T_i}) = f_i\left(\tilde{L}_{T_i}^i(x_{T_i})\right) \tag{11}$$

for some monotonic function  $f_i$ . It is this specialization that enables us to achieve the univariate and monotonicity properties in this higher dimensional setting. The last step is the derivation of the functional forms  $f_i$ . This is almost identical to the one-factor case. For details, the reader is referred to [6].

Covariance Structure of  $x$ -process and Comparison with Market Models. Typically,  $x$  is taken to be a  $k$ -dimensional Gaussian process with  $i$ th component of the form

$$x_t^i = \int_0^t \sigma_s^i dW_s^i \tag{12}$$

where the  $W^i$ s are Brownian motions under the measure  $\mathbb{N}$ , with instantaneous correlations  $dW_t^i dW_t^j =$  $\rho_t^{ij} dt$ . With x of this form, we have explicit knowledge of all marginal and conditional transition densities and all the required conditional expectations can be computed efficiently.

As in any interest-rate model, care must be taken in the choice of the instantaneous volatilities so that the resulting model has the appropriate qualitative behavior. For example, many authors illustrate the features of a model by using a simple exponential form of the instantaneous volatilities. However, use of this, in practice, would lead to a model having unrealistic hedges as the resulting correlation structure does not change in an appropriate way when the implied volatilities change. One appropriate choice based on a Hull-White short-rate model is given in  $[1]$ .

Recall that in a  $k$ -dimensional Markov-functional model, the prior model is chosen with some desired correlation structure in mind. If the instantaneous volatilities  $\sigma^i, i = 1, \ldots, n$  are taken to be separable in that for each *i*,  $\sigma_t^i$  can be written as a vector product of constants depending on  $i$  and a common volatility function  $\sigma_t$ , then it is very easy to form a prior model from the corresponding  $k$ -factor LIBOR market model with the same instantaneous volatilities. A first-order approximation to this model could, for example, be obtained by taking the usual SDE and replacing the time-dependent drift with its time-zero value. This would result in a model with something very close to the desired correlation structure, for which all LIBORs are lognormally distributed, but for which there is significant arbitrage. This makes the approximation too poor for use as a model in practice, but it remains adequate as a starting point for an arbitrage-free Markov-functional model. In fact, it is shown in [1] that in the one-dimensional case, Markov-functional and separable LMM models are very similar across a broad range of parameter values.

**Generalizations.** The discussion above focused on a LIBOR Markov-functional model specified in the terminal measure. For a version of this model that uses the discrete savings account as numeraire and forward induction, see [2]. The Markov-functional method is not restricted to calibrating to the market implied distributions of LIBORs. For a given tenor structure, one can formulate a model that calibrates to any swap rate or LIBOR at each time slice. In addition, the boundary can be extended so that more than one discount factor can be modeled on the final time slice. The details for a swap model can be found in [4, 8]. This is an appropriate choice for pricing *Bermudan swaptions* (*see* **Bermudan Swaptions and Callable Libor Exotics**) as the resulting model can be calibrated to vanilla swaption prices.

A multicurrency Markov-functional model first presented in [5] is described in [3].

If one is willing to employ Monte Carlo methods, the Markov-functional approach can be extended to formulate a high-dimensional model comparable

with a full-rank market model. See [9] for details. For further developments in the high-dimensional setting, see [7].

### **References**

- [1] Bennett, M. & Kennedy, J. (2005). A comparison of Markov-functional and market models: the onedimensional case, *The Journal of Derivatives* **1**(2), 22–43.
- [2] Fries, C. (2007). *Mathematical Finance: Theory, Modeling, Implementation*, John Wiley & Sons.
- [3] Fries, C. & Rott, M. (2004). *Cross Currency and Hybrid Markov-Functional Models*, *SSRN pre-print*, at http://papers.ssrn.com/sol3/papers.cfm?abstract id= 532122.
- [4] Hunt, P., Kennedy, J. & Pelsser, A. (2000). Markovfunctional interest rate models, in *The New Interest Rate Models*, L. Hughston, ed, Risk Books.
- [5] Hunt, P. (2003). The modelling and risks of prdcs. *Proceedings of the ICBI Global Derivatives Conference*, Barcelona.
- [6] Hunt, P. & Kennedy, J. (2004). *Financial Derivatives in Theory And Practice*, 2nd Edition, John Wiley & Sons.
- [7] Hunt, P. & Kennedy, J. (2005). *Longstaff–Schwarz, Effective Model Dimensionality and Reducible Markov-Functional Models*, SSRN pre-print at http://papers.ssrn. com/sol3/papers.cfm?abstract id=627921.
- [8] Hunt, P., Kennedy, J. & Pelsser, A. (2000). Markovfunctional interest rate models, *Finance and Stochastics* **4**(1), 391–408.
- [9] Kaisajuntti, L. & Kennedy, J. (2008). *An n-Dimensional Markov-Functional Interest Rate Model*, SSRN pre-print at http://papers.ssrn.com/sol3/papers.cfm? abstract id=1081337.
- [10] Pelsser, A. (2000). *Efficient Methods For Valuing Interest Rate Derivatives*, Springer Finance.

#### JOANNE KENNEDY